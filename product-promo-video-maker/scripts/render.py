#!/usr/bin/env python3
"""
Template rendering engine for product-analyst-webpage-maker.
Reads JSON data + HTML templates → produces single-file index.html.
"""
import json, re, sys, os
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.parent / "assets" / "templates"

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def render_simple(text, ctx):
    """Replace {{key}} and handle {{#each}} / {{#if}} / {{/if}} / {{/each}}"""
    # First pass: handle {{#each ...}} blocks
    def each_replacer(m):
        key = m.group(1).strip()
        inner = m.group(2)
        arr = resolve(ctx, key)
        if not isinstance(arr, list):
            return ""
        out = ""
        for item in arr:
            merged = {**ctx, **item} if isinstance(item, dict) else {**ctx, "this": item}
            out += render_simple(inner, merged)
        return out

    # Handle {{#if key}} blocks
    def if_replacer(m):
        key = m.group(1).strip()
        inner = m.group(2)
        val = resolve(ctx, key)
        if val and val != "false" and val != "False":
            return render_simple(inner, ctx)
        return ""

    text = re.sub(r'\{\{#each\s+(\S+)\}\}(.*?)\{\{/each\}\}', each_replacer, text, flags=re.DOTALL)
    text = re.sub(r'\{\{#if\s+(\S+)\}\}(.*?)\{\{/if\}\}', if_replacer, text, flags=re.DOTALL)

    # Second pass: simple {{key}} and {{key.subkey}}
    def var_replacer(m):
        key = m.group(1).strip()
        val = resolve(ctx, key)
        if val is None:
            return m.group(0)
        return str(val)

    text = re.sub(r'\{\{([^#].*?)\}\}', var_replacer, text)
    return text

def resolve(ctx, key):
    """Resolve dot-notation keys like 'product.name' from nested dicts."""
    if '.' in key:
        parts = key.split('.')
        val = ctx
        for p in parts:
            if isinstance(val, dict):
                val = val.get(p)
            else:
                return None
        return val
    return ctx.get(key)

def build_index_html(product_data, opportunities, images_manifest, config):
    """Main build function."""
    # Load templates
    base = load_text(TEMPLATES_DIR / "base.html")
    styles = load_text(TEMPLATES_DIR / "styles.css")
    scripts = load_text(TEMPLATES_DIR / "scripts.js")

    # Build context
    ctx = {
        "lang": config.get("language", "zh-CN"),
        "page_title": config.get("page_title", "AI 提效深度分析"),
        "product": product_data,
        "info": {"source_url": config.get("source_url", "")},
        "hero": {
            "product_name": product_data.get("product_name", "PRODUCT"),
            "tagline": product_data.get("slogan", ""),
            "framework_badge": f"基于 {config.get('analysis_framework', 'Manufacturing AI Efficiency Pro')} 分析框架",
            "hero_image": images_manifest.get("hero_image", ""),
            "stats": [
                {"number": spec.get("value", ""), "label": spec.get("key", "")}
                for spec in product_data.get("core_specs_highlight", [])
            ]
        },
        "framework": {
            "title": config.get("framework_title", "九步分析框架"),
            "subtitle": config.get("framework_subtitle", ""),
            "steps": opportunities.get("framework_steps", [])
        },
        "painpoint": {
            "title": opportunities.get("painpoint_comparison", {}).get("title", "从前 vs 现在"),
            "desc": opportunities.get("painpoint_comparison", {}).get("desc", ""),
            "before_label": opportunities.get("painpoint_comparison", {}).get("before_label", "传统方案"),
            "after_label": opportunities.get("painpoint_comparison", {}).get("after_label", "新产品"),
            "before_list": opportunities.get("painpoint_comparison", {}).get("before_list", []),
            "after_list": opportunities.get("painpoint_comparison", {}).get("after_list", []),
            "metrics": opportunities.get("painpoint_comparison", {}).get("metrics", [])
        },
        "opportunities": {
            "title": config.get("opportunities_title", "核心 AI 落地机会"),
            "desc": config.get("opportunities_desc", ""),
            "list": [
                {**opp, "feature_image": images_manifest.get(f"feature_{i+1:02d}", "")}
                for i, opp in enumerate(opportunities.get("opportunities", []))
            ]
        },
        "flowchart": {
            "title": config.get("flowchart_title", "产品使用主链路"),
            "desc": config.get("flowchart_desc", "L1 总览图：从任务接收到数据交付的完整流程"),
            "mermaid_code": opportunities.get("flowchart_mermaid", "")
        },
        "valuechain": {
            "title": config.get("valuechain_title", "价值链定位"),
            "nodes": product_data.get("value_chain", [])
        },
        "brand": {
            "logo_text": product_data.get("product_name", "BRAND"),
            "cta_text": product_data.get("slogan", ""),
            "button_text": config.get("cta_button_text", "立即了解"),
            "hero_image": images_manifest.get("brand_image", "")
        },
        "emotion": {
            "title": config.get("emotion_title", "宣发情绪曲线"),
            "points": config.get("emotion_points", []),
            "time_labels": config.get("emotion_time_labels", []),
            "phase_labels": config.get("emotion_phase_labels", []),
            "shot_labels": config.get("emotion_shot_labels", [])
        },
        "styles": styles,
        "scripts": scripts
    }

    # Build sections
    sections_html = ""
    for section_name in config.get("output_sections", ["hero", "framework", "painpoint", "opportunities", "flowchart", "valuechain", "brand"]):
        section_path = TEMPLATES_DIR / "sections" / f"{section_name}.html"
        if section_path.exists():
            section_tpl = load_text(section_path)
            sections_html += render_simple(section_tpl, ctx)
        else:
            print(f"Warning: section template not found: {section_name}", file=sys.stderr)

    ctx["content"] = sections_html

    # Render base template
    final_html = render_simple(base, ctx)
    return final_html


def main():
    """CLI entry point for testing."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--product-data", required=True, help="Path to product-data.json")
    parser.add_argument("--opportunities", required=True, help="Path to opportunities.json")
    parser.add_argument("--images", required=True, help="Path to images-manifest.json")
    parser.add_argument("--config", required=True, help="Path to build-config.json")
    parser.add_argument("--output", required=True, help="Output HTML file path")
    args = parser.parse_args()

    product_data = load_json(args.product_data)
    opportunities = load_json(args.opportunities)
    images_manifest = load_json(args.images)
    config = load_json(args.config)

    html = build_index_html(product_data, opportunities, images_manifest, config)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Built: {args.output}")


if __name__ == "__main__":
    main()
