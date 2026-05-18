#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成 skill.yaml 工具

用法：
    python batch_generate_skill_yaml.py /path/to/skills/ --owner "LinkmasterLing"
"""

import os
import sys
import yaml
import re
from pathlib import Path
from datetime import datetime

# 目录名到分类映射（推断）
CATEGORY_MAP = {
    "ai_engineer": "engineering",
    "autonomous_optimization_architect": "engineering",
    "backend-architecture": "engineering",
    "devops_automator": "engineering",
    "frontend-development": "engineering",
    "mobile_app_builder": "engineering",
    "rapid_prototyper": "engineering",
    "security_engineer": "engineering",
    "senior_developer": "engineering",
    "filament_optimization_specialist": "engineering",
    "brand-guardian-optimization": "creative",
    "image-prompt-engineer-optimization": "creative",
    "inclusive-visuals-specialist-optimization": "creative",
    "ui-design": "design",
    "ux-architect-optimization": "design",
    "ux-research": "design",
    "visual-storyteller-optimization": "creative",
    "whimsy-injector-optimization": "creative",
    "manufacturing-ai-efficiency-pro": "manufacturing",
    "fast-moving-consumer-goods-ecommerce-operator": "ecommerce",
    "fast-moving-consumer-goods-supply-chain": "ecommerce",
    "product-promo-video-maker": "content-creation",
    "content-monetization-pipeline": "content-creation",
}

# 目录名到类型映射
TYPE_MAP = {
    "manufacturing-ai-efficiency-pro": "hybrid",
    "product-promo-video-maker": "hybrid",
    "content-monetization-pipeline": "hybrid",
}

# 默认类型
DEFAULT_TYPE = "prompt"

# 风险等级推断
HIGH_RISK_KEYWORDS = ["security", "manufacturing", "devops"]
MEDIUM_RISK_KEYWORDS = ["content", "video", "monetization", "ecommerce", "product"]


def infer_risk_level(skill_id: str) -> str:
    sid_lower = skill_id.lower()
    for kw in HIGH_RISK_KEYWORDS:
        if kw in sid_lower:
            return "high"
    for kw in MEDIUM_RISK_KEYWORDS:
        if kw in sid_lower:
            return "medium"
    return "low"


def extract_name_from_skill_md(skill_md_path: Path) -> str:
    """从 SKILL.md 第一行标题提取名称"""
    try:
        with open(skill_md_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # 匹配 # 标题 或 --- name: 格式
                if line.startswith("# "):
                    return line[2:].strip().replace("制造业 AI 提效全链路扫描器", "制造业 AI 提效").replace("产品宣发视频生成", "产品宣发视频")
                if line.startswith("name:"):
                    return line.split(":", 1)[1].strip().strip('"')
    except Exception:
        pass
    return None


def extract_description_from_skill_md(skill_md_path: Path) -> str:
    """从 SKILL.md 提取描述"""
    try:
        with open(skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            # 尝试匹配 description 字段
            match = re.search(r'description:\s*["\']?([^"\'\n]+)', content)
            if match:
                return match.group(1).strip()
            # 尝试匹配 ## 简介 后面的内容
            match = re.search(r'## 简介\s*\n+([^#\n][^\n]*)', content)
            if match:
                return match.group(1).strip()
            # 尝试匹配第一段非空行
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('---') and len(line) > 20:
                    return line[:200]
    except Exception:
        pass
    return None


def generate_skill_yaml(skill_dir: Path, owner: str) -> dict:
    """为单个 skill 目录生成 skill.yaml 数据"""
    skill_id = skill_dir.name
    
    # 尝试读取 SKILL.md 获取信息
    skill_md = skill_dir / "SKILL.md"
    name = extract_name_from_skill_md(skill_md) or skill_id.replace("-", " ").replace("_", " ").title()
    description = extract_description_from_skill_md(skill_md) or f"{name} Skill"
    
    # 推断分类
    category = CATEGORY_MAP.get(skill_id, "product")
    
    # 推断类型
    skill_type = TYPE_MAP.get(skill_id, DEFAULT_TYPE)
    
    # 推断风险等级
    risk_level = infer_risk_level(skill_id)
    
    # 检查是否有 tools/ 目录
    has_tools = (skill_dir / "tools").exists() or (skill_dir / "scripts").exists()
    
    # 检查是否有 evals/ 目录
    has_evals = (skill_dir / "evals").exists()
    
    # 推断触发关键词（从 skill_id 和 name）
    keywords = [skill_id.replace("-", " ").replace("_", " ")]
    # 尝试从 SKILL.md 提取触发关键词
    try:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
            # 匹配 ## 调用时机 / ## 适用场景 后面的关键词
            match = re.search(r'## (?:调用时机|适用场景|Trigger).*?\n([\s\S]{0,500})', content, re.IGNORECASE)
            if match:
                text = match.group(1)
                # 提取列表项
                items = re.findall(r'[-*]\s*([^\n]+)', text)
                for item in items[:3]:
                    keywords.append(item.strip()[:30])
    except Exception:
        pass
    
    # 去重并限制
    keywords = list(dict.fromkeys([k for k in keywords if k]))[:5]
    
    # 构建基础数据
    data = {
        "skill_id": skill_id,
        "name": name,
        "version": "1.0.0",
        "status": "production" if has_evals else "testing",
        "owner": owner,
        "risk_level": risk_level,
        "created_at": "2026-05-18",
        "updated_at": "2026-05-18",
        "description": description[:300],
        "category": category,
        "type": skill_type,
        "trigger": {
            "keywords": keywords,
            "min_confidence": 0.75,
        },
    }
    
    # 如果有 evals/，添加 eval 配置
    if has_evals:
        data["eval"] = {
            "suite_id": f"{skill_id}-eval-v1",
            "min_score": 85,
        }
    
    # 如果有 scripts/ 或 tools/，添加 dependencies
    if has_tools:
        data["dependencies"] = {
            "tools": ["external_scripts"]
        }
    
    # 添加 changelog 指针
    changelog_path = skill_dir / "changelog.md"
    if changelog_path.exists():
        data["changelog"] = "changelog.md"
    
    return data


def generate_and_write(skills_dir: Path, owner: str, dry_run: bool = False):
    """批量生成 skill.yaml"""
    exclude = {".git", "docs", "references", "scripts", "shared", ".github", "__pycache__"}
    generated = 0
    skipped = 0
    
    for item in sorted(skills_dir.iterdir()):
        if not item.is_dir():
            continue
        if item.name.startswith(".") or item.name in exclude:
            continue
        
        skill_yaml_path = item / "skill.yaml"
        
        if skill_yaml_path.exists():
            print(f"⏭️  跳过（已存在）: {item.name}")
            skipped += 1
            continue
        
        data = generate_skill_yaml(item, owner)
        
        if dry_run:
            print(f"[DRY-RUN] 将生成: {item.name}/skill.yaml")
            print(f"  skill_id: {data['skill_id']}")
            print(f"  name: {data['name']}")
            print(f"  category: {data['category']}")
            print()
        else:
            with open(skill_yaml_path, "w", encoding="utf-8") as f:
                yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
            print(f"✅ 生成: {item.name}/skill.yaml")
            generated += 1
    
    print(f"\n{'='*50}")
    print(f"总计: 生成 {generated} 个 | 跳过 {skipped} 个")
    print(f"{'='*50}")
    return generated


def main():
    import argparse
    parser = argparse.ArgumentParser(description="批量生成 skill.yaml")
    parser.add_argument("path", help="Skills 根目录")
    parser.add_argument("--owner", default="LinkmasterLing", help="默认负责人")
    parser.add_argument("--dry-run", action="store_true", help="只显示，不写入")
    args = parser.parse_args()
    
    skills_dir = Path(args.path).resolve()
    if not skills_dir.exists():
        print(f"❌ 目录不存在: {skills_dir}")
        sys.exit(1)
    
    generate_and_write(skills_dir, args.owner, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
