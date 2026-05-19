#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skillctl validate — Skill 包静态校验工具

校验项：
1. 目录结构完整性（skill.yaml + SKILL.md 必须存在）
2. skill.yaml 格式合法（YAML 可解析，UTF-8 编码）
3. 必填字段齐全（skill_id, name, version, status, owner, risk_level, description, trigger）
4. 字段格式合规（version 语义化、status 在状态机内、risk_level 枚举值）
5. production/canary 状态必须有 eval 配置
6. SKILL.md 同目录存在

用法：
    python skillctl_validate.py /path/to/skills/  # 校验整个 skills/ 目录
    python skillctl_validate.py /path/to/skills/manufacturing-ai-efficiency-pro/  # 校验单个 skill
    python skillctl_validate.py /path/to/skills/ --json  # JSON 格式输出

退出码：
    0 — 全部通过
    1 — 有失败项
"""

import os
import sys
import yaml
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# ========== 常量定义 ==========

REQUIRED_FIELDS = [
    "skill_id",
    "name",
    "version",
    "status",
    "owner",
    "risk_level",
    "description",
    "trigger",
]

VALID_STATUSES = [
    "draft",
    "testing",
    "staging",
    "canary",
    "production",
    "deprecated",
]

VALID_RISK_LEVELS = ["low", "medium", "high"]

VALID_TYPES = ["prompt", "workflow", "tool", "hybrid"]

VALID_CATEGORIES = [
    "engineering",
    "design",
    "manufacturing",
    "ecommerce",
    "product",
    "creative",
    "content-creation",
    "research",
    "data",
    "operations",
]

SEMVER_PATTERN = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-[\w.]+)?$")

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

SKILL_ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class ValidationResult:
    def __init__(self, skill_path: str):
        self.skill_path = skill_path
        self.skill_id = None
        self.version = None
        self.passed = True
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.infos: List[str] = []

    def error(self, msg: str):
        self.errors.append(msg)
        self.passed = False

    def warn(self, msg: str):
        self.warnings.append(msg)

    def info(self, msg: str):
        self.infos.append(msg)

    def to_dict(self) -> Dict:
        return {
            "skill_path": self.skill_path,
            "skill_id": self.skill_id,
            "version": self.version,
            "passed": self.passed,
            "errors": self.errors,
            "warnings": self.warnings,
            "infos": self.infos,
        }


def validate_skill_yaml(skill_dir: Path) -> ValidationResult:
    """校验单个 Skill 目录"""
    result = ValidationResult(str(skill_dir))

    # 1. 检查 skill.yaml 存在
    skill_yaml = skill_dir / "skill.yaml"
    if not skill_yaml.exists():
        result.error("缺少 skill.yaml（必须存在）")
        return result

    # 2. 检查 SKILL.md 存在
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        result.error("缺少 SKILL.md（必须存在）")
    else:
        result.info("SKILL.md 存在")

    # 3. 解析 YAML
    try:
        with open(skill_yaml, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        result.error(f"YAML 解析失败: {e}")
        return result
    except UnicodeDecodeError as e:
        result.error(f"编码错误（必须为 UTF-8）: {e}")
        return result

    if data is None:
        result.error("skill.yaml 为空文件")
        return result

    if not isinstance(data, dict):
        result.error("skill.yaml 根节点必须是字典（mapping）")
        return result

    # 记录元数据
    result.skill_id = data.get("skill_id", "UNKNOWN")
    result.version = data.get("version", "UNKNOWN")

    # 4. 必填字段检查
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] is None or data[field] == "":
            result.error(f"必填字段缺失或为空: '{field}'")

    # 5. 字段格式校验
    if "skill_id" in data and data["skill_id"]:
        sid = data["skill_id"]
        if not SKILL_ID_PATTERN.match(sid):
            result.error(f"skill_id 格式不合规: '{sid}'（必须为 kebab-case: a-z, 0-9, -）")
        expected_id = skill_dir.name
        if sid != expected_id:
            result.warn(f"skill_id '{sid}' 与目录名 '{expected_id}' 不一致（建议保持一致）")

    if "version" in data and data["version"]:
        ver = data["version"]
        if not SEMVER_PATTERN.match(ver):
            result.error(f"version 格式不合规: '{ver}'（必须为语义化版本，如 1.2.3）")

    if "status" in data and data["status"]:
        st = data["status"]
        if st not in VALID_STATUSES:
            result.error(
                f"status 值不合规: '{st}'（必须为: {', '.join(VALID_STATUSES)}）"
            )

    if "risk_level" in data and data["risk_level"]:
        rl = data["risk_level"]
        if rl not in VALID_RISK_LEVELS:
            result.error(
                f"risk_level 值不合规: '{rl}'（必须为: {', '.join(VALID_RISK_LEVELS)}）"
            )

    if "type" in data and data["type"]:
        t = data["type"]
        if t not in VALID_TYPES:
            result.warn(f"type 值不在推荐列表: '{t}'（推荐: {', '.join(VALID_TYPES)}）")

    if "category" in data and data["category"]:
        c = data["category"]
        if c not in VALID_CATEGORIES:
            result.warn(
                f"category 值不在推荐列表: '{c}'（推荐: {', '.join(VALID_CATEGORIES)}）"
            )

    if "description" in data and data["description"]:
        desc = data["description"]
        if len(desc) < 20:
            result.warn(f"description 过短（{len(desc)} 字符），建议 ≥ 20 字符")

    if "trigger" in data and data["trigger"]:
        trigger = data["trigger"]
        if not isinstance(trigger, dict):
            result.error("trigger 必须是字典（mapping）")
        else:
            has_keywords = "keywords" in trigger and trigger["keywords"]
            has_intent = "intent" in trigger and trigger["intent"]
            if not has_keywords and not has_intent:
                result.error("trigger 必须包含 'keywords' 或 'intent' 至少一项")

    if "created_at" in data and data["created_at"]:
        if not DATE_PATTERN.match(str(data["created_at"])):
            result.warn("created_at 格式建议为 YYYY-MM-DD")

    if "updated_at" in data and data["updated_at"]:
        if not DATE_PATTERN.match(str(data["updated_at"])):
            result.warn("updated_at 格式建议为 YYYY-MM-DD")

    # 6. production / canary 状态强制要求 eval
    status = data.get("status", "")
    if status in ("canary", "production"):
        if "eval" not in data or not data["eval"]:
            result.error(f"status='{status}' 时必须配置 eval 字段（评测绑定）")
        else:
            eval_data = data["eval"]
            if not isinstance(eval_data, dict):
                result.error("eval 必须是字典（mapping）")
            else:
                if "suite_id" not in eval_data or not eval_data["suite_id"]:
                    result.error("eval.suite_id 不能为空（必须绑定评测集 ID）")
                if "min_score" not in eval_data:
                    result.warn("eval.min_score 建议配置（发布最低分门槛）")

    # 7. 建议字段检查（仅警告）
    suggested_fields = [
        "category",
        "type",
        "input_schema",
        "output_schema",
        "dependencies",
        "release",
        "changelog",
    ]
    for field in suggested_fields:
        if field not in data or data[field] is None or data[field] == "":
            result.warn(f"建议字段缺失: '{field}'")

    # 8. changelog 文件存在性检查
    if "changelog" in data and data["changelog"]:
        changelog_path = skill_dir / data["changelog"]
        if not changelog_path.exists():
            result.warn(f"changelog 文件不存在: {data['changelog']}")

    return result


def validate_skills_directory(skills_dir: Path) -> List[ValidationResult]:
    """校验整个 skills 目录"""
    results = []

    if not skills_dir.exists():
        print(f"❌ 目录不存在: {skills_dir}")
        sys.exit(1)

    # 遍历所有子目录（排除 .git, docs, references 等非 skill 目录）
    exclude_names = {".git", "docs", "references", "scripts", "shared", ".github"}

    for item in sorted(skills_dir.iterdir()):
        if not item.is_dir():
            continue
        if item.name.startswith("."):
            continue
        if item.name in exclude_names:
            continue

        result = validate_skill_yaml(item)
        results.append(result)

    return results


def print_report(results: List[ValidationResult], json_output: bool = False):
    """输出校验报告"""
    if json_output:
        report = [r.to_dict() for r in results]
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    print(f"\n{'=' * 60}")
    print(f"Skill 包校验报告")
    print(f"{'=' * 60}")
    print(f"总计: {total} 个 Skill | ✅ 通过: {passed} | ❌ 失败: {failed}")
    print(f"{'=' * 60}\n")

    for r in results:
        status_icon = "✅" if r.passed else "❌"
        skill_name = r.skill_id or Path(r.skill_path).name
        version = r.version or "-"
        print(f"{status_icon} {skill_name} (v{version})")

        for err in r.errors:
            print(f"   ❌ ERROR: {err}")
        for warn in r.warnings:
            print(f"   ⚠️  WARN: {warn}")
        for info in r.infos:
            print(f"   ℹ️  INFO: {info}")

        print()

    print(f"{'=' * 60}")
    if failed > 0:
        print(f"结果: {failed} 个 Skill 未通过校验，请修复后重试")
    else:
        print(f"结果: 全部 {total} 个 Skill 通过校验 🎉")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(
        description="Skill 包静态校验工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python skillctl_validate.py ./skills/
  python skillctl_validate.py ./skills/product-promo-video-maker/
  python skillctl_validate.py ./skills/ --json
        """,
    )
    parser.add_argument("path", help="Skill 目录或 skills 根目录")
    parser.add_argument("--json", action="store_true", help="JSON 格式输出")

    args = parser.parse_args()

    target = Path(args.path).resolve()

    # 判断是单个 skill 目录还是 skills 根目录
    if (target / "skill.yaml").exists():
        # 单个 skill
        results = [validate_skill_yaml(target)]
    else:
        # 假设是 skills 根目录
        results = validate_skills_directory(target)

    print_report(results, json_output=args.json)

    # 如果有失败，返回非零退出码
    has_failures = any(not r.passed for r in results)
    sys.exit(1 if has_failures else 0)


if __name__ == "__main__":
    main()
