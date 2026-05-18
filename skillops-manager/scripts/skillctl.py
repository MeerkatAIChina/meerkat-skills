#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skillctl — SkillOps 统一 CLI 入口

用法：
    python skillctl.py create <skill_id> <name> [options]     # 创建新 Skill 骨架
    python skillctl.py validate [path]                        # 校验 Skill 包
    python skillctl.py eval-init <skill_id>                   # 初始化评测集
    python skillctl.py version-check <skill_id> <old_ver> <new_ver>  # 版本升级检查
    python skillctl.py report [path]                          # 生成仓库健康报告
    python skillctl.py list [path]                            # 列出所有 Skill

环境变量：
    SKILLS_ROOT — Skill 仓库根目录（默认当前目录）
"""

import os
import sys
import yaml
import json
import argparse
from pathlib import Path
from datetime import datetime

SKILLS_ROOT = Path(os.environ.get("SKILLS_ROOT", ".")).resolve()
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def _load_skill_yaml(skill_dir: Path) -> dict:
    with open(skill_dir / "skill.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def cmd_create(skill_id: str, name: str, category: str = "product", risk: str = "medium"):
    """创建新 Skill 骨架"""
    skill_dir = SKILLS_ROOT / skill_id
    if skill_dir.exists():
        print(f"❌ 目录已存在: {skill_dir}")
        sys.exit(1)

    skill_dir.mkdir(parents=True)
    (skill_dir / "evals").mkdir()
    (skill_dir / "examples").mkdir()
    (skill_dir / "prompts").mkdir()
    (skill_dir / "knowledge").mkdir()
    (skill_dir / "workflows").mkdir()
    (skill_dir / "tools").mkdir()

    # 生成 skill.yaml
    skill_yaml = {
        "skill_id": skill_id,
        "name": name,
        "version": "0.1.0",
        "status": "draft",
        "owner": os.environ.get("SKILL_OWNER", "unknown"),
        "risk_level": risk,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "updated_at": datetime.now().strftime("%Y-%m-%d"),
        "description": f"{name} Skill",
        "category": category,
        "type": "hybrid",
        "trigger": {
            "keywords": [skill_id.replace("-", " ")],
            "min_confidence": 0.75,
        },
    }

    with open(skill_dir / "skill.yaml", "w", encoding="utf-8") as f:
        yaml.dump(skill_yaml, f, allow_unicode=True, sort_keys=False)

    # 生成 SKILL.md 骨架
    skill_md = f"""---
skill_id: "{skill_id}"
name: "{name}"
version: "0.1.0"
status: "draft"
---

# {name}

## 简介
{name} 的 Skill 描述（请补充）

## 项目定位
- **定位**：（请补充）
- **原始来源**：（请补充）
- **适配说明**：（请补充）

## 适用场景
- （请补充场景 1）
- （请补充场景 2）

## 不适用场景
- （请补充边界 1）
- （请补充边界 2）

## 核心能力

### 能力 1：（请命名）
（请描述核心能力）

## 执行链路

### 第一步：（请命名）
（请描述步骤）

## 质量标准

- （请补充质量标准 1）
- （请补充质量标准 2）

## 依赖说明

- **上游 Skill**：（请补充）
- **外部工具**：（请补充）
- **知识库**：（请补充）

## 开发历史

### V0.1.0 ({datetime.now().strftime("%Y-%m-%d")})
- 初始版本

---

*本 Skill 遵循 MeerkatAI Skill Registry 规范，适用 MIT License。*
"""

    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(skill_md)

    # 生成 evals 骨架
    cases = {
        "case_id": f"{skill_id}_001",
        "input": {"prompt": "示例输入"},
        "expected_behavior": ["行为 1", "行为 2"],
        "rubric": {"completeness": 50, "accuracy": 50},
    }
    with open(skill_dir / "evals" / "cases.jsonl", "w", encoding="utf-8") as f:
        f.write(json.dumps(cases, ensure_ascii=False) + "\n")

    rubric = {
        "dimensions": [
            {"name": "completeness", "weight": 50, "criteria": "输出完整度"},
            {"name": "accuracy", "weight": 50, "criteria": "事实准确性"},
        ],
        "total": 100,
    }
    with open(skill_dir / "evals" / "rubric.yaml", "w", encoding="utf-8") as f:
        yaml.dump(rubric, f, allow_unicode=True)

    # 生成 changelog
    with open(skill_dir / "changelog.md", "w", encoding="utf-8") as f:
        f.write(f"# Changelog\n\n## V0.1.0 ({datetime.now().strftime('%Y-%m-%d')})\n- 初始版本\n")

    print(f"✅ 创建成功: {skill_dir}")
    print(f"   文件: skill.yaml, SKILL.md, evals/, examples/, prompts/, knowledge/")
    print(f"   下一步: 编辑 SKILL.md 补充业务逻辑，然后运行 'skillctl validate {skill_id}'")


def cmd_validate(target_path: str = "."):
    """调用 skillctl_validate.py"""
    validate_script = SKILLS_ROOT / "scripts" / "skillctl_validate.py"
    if not validate_script.exists():
        print(f"❌ 校验脚本不存在: {validate_script}")
        sys.exit(1)

    target = Path(target_path)
    if not target.is_absolute():
        target = SKILLS_ROOT / target

    os.system(f'python "{validate_script}" "{target}"')


def cmd_eval_init(skill_id: str):
    """初始化评测集"""
    skill_dir = SKILLS_ROOT / skill_id
    if not skill_dir.exists():
        print(f"❌ Skill 不存在: {skill_id}")
        sys.exit(1)

    # 读取 SKILL.md 提取关键信息
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ SKILL.md 不存在")
        sys.exit(1)

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # 简单提取执行步骤作为测试维度
    import re
    steps = re.findall(r"### 第[一二三四五六七八九十]步[：:]([^\n]+)", content)
    if not steps:
        steps = ["核心能力验证"]

    # 生成 rubric
    weight = 100 // len(steps) if steps else 100
    dimensions = []
    for step in steps[:5]:
        dimensions.append({
            "name": step.strip().replace(" ", "_").lower()[:30],
            "weight": weight,
            "criteria": f"验证 {step.strip()}",
        })

    # 调整最后一个维度使总和为 100
    if dimensions:
        total = sum(d["weight"] for d in dimensions)
        dimensions[-1]["weight"] += (100 - total)

    rubric = {"dimensions": dimensions, "total": 100}

    with open(skill_dir / "evals" / "rubric.yaml", "w", encoding="utf-8") as f:
        yaml.dump(rubric, f, allow_unicode=True)

    # 生成示例 cases
    cases = []
    for i in range(min(5, len(steps)) if steps else 3):
        cases.append({
            "case_id": f"{skill_id}_{i+1:03d}",
            "input": {"prompt": f"测试场景 {i+1}: {steps[i] if i < len(steps) else '通用场景'}"},
            "expected_behavior": [f"完成 {steps[i] if i < len(steps) else '核心能力'}"],
            "rubric": {d["name"]: d["weight"] for d in dimensions},
        })

    with open(skill_dir / "evals" / "cases.jsonl", "w", encoding="utf-8") as f:
        for case in cases:
            f.write(json.dumps(case, ensure_ascii=False) + "\n")

    print(f"✅ 评测集初始化完成: {skill_id}/evals/")
    print(f"   生成 {len(cases)} 个测试样本 + {len(dimensions)} 个评分维度")
    print(f"   请根据实际业务场景补充具体测试数据")


def cmd_version_check(skill_id: str, old_ver: str, new_ver: str, change_desc: str = ""):
    """版本升级检查"""
    # 解析版本号
    old = list(map(int, old_ver.split(".")[:3]))
    new = list(map(int, new_ver.split(".")[:3]))

    if old == new:
        print("⚠️ 版本号相同，无需升级")
        return

    # 判断升级类型
    if old[0] != new[0]:
        level = "MAJOR"
        needs_eval = True
        reason = "主版本变更（架构重构、模型更换、schema 变更）"
    elif old[1] != new[1]:
        level = "MINOR"
        needs_eval = True
        reason = "次版本变更（新增功能、链路调整）"
    else:
        level = "PATCH"
        needs_eval = False
        reason = "补丁变更（文档修复、typo）"

    print(f"📊 版本升级检查: {skill_id}")
    print(f"   旧版本: {old_ver}")
    print(f"   新版本: {new_ver}")
    print(f"   升级级别: {level}")
    print(f"   原因: {reason}")
    print(f"   是否需要重新 eval: {'✅ 是' if needs_eval else '⚠️ 建议 smoke test'}")

    if needs_eval:
        print(f"   建议: 运行 'skillctl eval-init {skill_id}' 补充回归测试")


def cmd_report(target_path: str = "."):
    """生成仓库健康报告"""
    target = Path(target_path)
    if not target.is_absolute():
        target = SKILLS_ROOT / target

    skills = []
    exclude = {".git", "docs", "scripts", "references", "shared", ".github", "__pycache__"}

    for item in sorted(target.iterdir()):
        if not item.is_dir() or item.name.startswith(".") or item.name in exclude:
            continue
        skill_yaml = item / "skill.yaml"
        if not skill_yaml.exists():
            continue

        try:
            with open(skill_yaml, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception:
            continue

        skills.append({
            "id": data.get("skill_id", item.name),
            "name": data.get("name", item.name),
            "version": data.get("version", "?"),
            "status": data.get("status", "?"),
            "category": data.get("category", "?"),
            "risk": data.get("risk_level", "?"),
            "has_evals": (item / "evals" / "cases.jsonl").exists(),
        })

    # 统计
    total = len(skills)
    by_status = {}
    by_category = {}
    eval_coverage = sum(1 for s in skills if s["has_evals"])

    for s in skills:
        by_status[s["status"]] = by_status.get(s["status"], 0) + 1
        by_category[s["category"]] = by_category.get(s["category"], 0) + 1

    print(f"\n{'='*60}")
    print(f"Skill Registry 健康报告")
    print(f"{'='*60}")
    print(f"总计 Skill: {total}")
    print(f"评测覆盖: {eval_coverage}/{total} ({eval_coverage*100//total if total else 0}%)")
    print()

    print("按状态分布:")
    for status, count in sorted(by_status.items()):
        print(f"   {status:12s}: {count:3d}")

    print()
    print("按分类分布:")
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"   {cat:20s}: {count:3d}")

    print()
    print("最近更新 Skill (按版本号排序前 5):")
    recent = sorted(skills, key=lambda s: s["version"], reverse=True)[:5]
    for s in recent:
        eval_icon = "✅" if s["has_evals"] else "❌"
        print(f"   {eval_icon} {s['id']:40s} v{s['version']:8s} [{s['status']}]")

    print(f"{'='*60}")


def cmd_list(target_path: str = "."):
    """列出所有 Skill"""
    target = Path(target_path)
    if not target.is_absolute():
        target = SKILLS_ROOT / target

    exclude = {".git", "docs", "scripts", "references", "shared", ".github", "__pycache__"}
    skills = []

    for item in sorted(target.iterdir()):
        if not item.is_dir() or item.name.startswith(".") or item.name in exclude:
            continue
        if (item / "skill.yaml").exists():
            try:
                data = _load_skill_yaml(item)
                skills.append({
                    "id": data.get("skill_id", item.name),
                    "name": data.get("name", item.name),
                    "version": data.get("version", "?"),
                    "status": data.get("status", "?"),
                })
            except Exception:
                skills.append({"id": item.name, "name": "?", "version": "?", "status": "?"})

    print(f"\n{'ID':40s} {'Name':30s} {'Version':8s} {'Status':12s}")
    print("-" * 90)
    for s in skills:
        print(f"{s['id']:40s} {s['name']:30s} {s['version']:8s} {s['status']:12s}")
    print(f"\n总计: {len(skills)} 个 Skill")


def main():
    parser = argparse.ArgumentParser(description="SkillOps 统一 CLI")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # create
    create_parser = subparsers.add_parser("create", help="创建新 Skill 骨架")
    create_parser.add_argument("skill_id", help="Skill ID (kebab-case)")
    create_parser.add_argument("name", help="Skill 中文名称")
    create_parser.add_argument("--category", default="product", help="分类")
    create_parser.add_argument("--risk", default="medium", choices=["low", "medium", "high"], help="风险等级")

    # validate
    validate_parser = subparsers.add_parser("validate", help="校验 Skill 包")
    validate_parser.add_argument("path", nargs="?", default=".", help="目标路径")

    # eval-init
    eval_parser = subparsers.add_parser("eval-init", help="初始化评测集")
    eval_parser.add_argument("skill_id", help="Skill ID")

    # version-check
    version_parser = subparsers.add_parser("version-check", help="版本升级检查")
    version_parser.add_argument("skill_id", help="Skill ID")
    version_parser.add_argument("old_ver", help="旧版本号")
    version_parser.add_argument("new_ver", help="新版本号")
    version_parser.add_argument("--change-desc", default="", help="变更描述")

    # report
    report_parser = subparsers.add_parser("report", help="生成仓库健康报告")
    report_parser.add_argument("path", nargs="?", default=".", help="目标路径")

    # list
    list_parser = subparsers.add_parser("list", help="列出所有 Skill")
    list_parser.add_argument("path", nargs="?", default=".", help="目标路径")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "create":
        cmd_create(args.skill_id, args.name, args.category, args.risk)
    elif args.command == "validate":
        cmd_validate(args.path)
    elif args.command == "eval-init":
        cmd_eval_init(args.skill_id)
    elif args.command == "version-check":
        cmd_version_check(args.skill_id, args.old_ver, args.new_ver, args.change_desc)
    elif args.command == "report":
        cmd_report(args.path)
    elif args.command == "list":
        cmd_list(args.path)


if __name__ == "__main__":
    main()
