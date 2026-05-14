# 模板变量参考

## 全局变量

来自 `product-data.json`:

| 变量 | 类型 | 示例 |
|------|------|------|
| `{{product.name}}` | string | "DJI Mavic 3 行业系列" |
| `{{product.slogan}}` | string | "便携新秀，效率随行" |
| `{{product.brand}}` | string | "DJI" |
| `{{product.category}}` | string | "industrial_drone" |

来自 `product-info.json`:

| 变量 | 类型 | 示例 |
|------|------|------|
| `{{info.source_url}}` | string | "https://enterprise.dji.com/..." |
| `{{info.extracted_at}}` | string | ISO timestamp |

## Hero Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{hero.product_name}}` | product.name | "DJI MAVIC 3" |
| `{{hero.tagline}}` | product.slogan | "行业系列 — 便携新秀，效率随行" |
| `{{hero.framework_badge}}` | analysis framework | "基于 Manufacturing AI Efficiency Pro 分析框架" |
| `{{hero.hero_image}}` | assets | "images/product-hero.png" |
| `{{hero.stats}}` | product.core_specs | array of {number, label} |

## Framework Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{framework.title}}` | fixed | "九步分析框架" |
| `{{framework.subtitle}}` | fixed | "Manufacturing AI Efficiency Pro · ..." |
| `{{framework.steps}}` | analysis output | array of {step, title, desc, tag} |

## Painpoint Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{painpoint.before_label}}` | painpoint_comparison | "传统方案" |
| `{{painpoint.after_label}}` | painpoint_comparison | "Mavic 3 行业版" |
| `{{painpoint.before_list}}` | painpoint_comparison | ["箱式运输需2-3人", ...] |
| `{{painpoint.after_list}}` | painpoint_comparison | ["单手可握", ...] |
| `{{painpoint.metrics}}` | painpoint_comparison | [{value, label}, ...] |

## Opportunities Section 变量

来自 `opportunities.json`:

| 变量 | 类型 | 路径 |
|------|------|------|
| `{{opportunities}}` | array | opportunities[] |

每个 opportunity 对象的字段:

| 字段 | 类型 | 模板中使用 |
|------|------|-----------|
| `id` | string | `{{id}}` |
| `title` | string | `{{title}}` |
| `priority` | string | `{{priority}}` (P0/P1/P2) |
| `icon` | string | `{{icon}}` |
| `business_goal` | string | `{{business_goal}}` |
| `pain_point` | string | `{{pain_point}}` |
| `entry_action` | string | `{{entry_action}}` |
| `solution` | string | `{{solution}}` |
| `data_support` | string | `{{data_support}}` |
| `expected_benefit` | string | `{{expected_benefit}}` |
| `difficulty` | string | `{{difficulty}}` |
| `system_target` | string | `{{system_target}}` |
| `feature_image` | string | `{{feature_image}}` (from assets) |

## Flowchart Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{flowchart.title}}` | fixed | "产品使用主链路" |
| `{{flowchart.desc}}` | fixed | "L1 总览图..." |
| `{{flowchart.mermaid_code}}` | analysis | Mermaid diagram text |

## Value Chain Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{valuechain.nodes}}` | product.value_chain | [{icon, title, desc}, ...] |

## Brand Section 变量

| 变量 | 来源 | 示例 |
|------|------|------|
| `{{brand.logo_text}}` | product.name | "DJI MAVIC 3" |
| `{{brand.cta_text}}` | product.slogan | "行业系列 — 便携新秀，效率随行" |
| `{{brand.button_text}}` | fixed | "立即了解" |
| `{{brand.hero_image}}` | assets | "images/brand-scene.jpg" |

## Assets 变量

| 变量 | 路径规则 |
|------|---------|
| `{{assets.hero_image}}` | `images/product-hero.*` |
| `{{assets.feature_images}}` | `images/feature-*.*` (按 opportunity 顺序匹配) |
| `{{assets.scene_images}}` | `images/scene-*.*` |
| `{{assets.brand_image}}` | `images/brand-*.*` |

## 条件变量

```
{{#if include_video_pipeline}}
  视频相关 section 内容
{{/if}}

{{#if has_feature_image}}
  <div class="opportunity-image"><img src="{{feature_image}}" /></div>
{{/if}}
```

## 循环语法

```html
<!-- 框架步骤循环 -->
{{#each framework.steps}}
  <div class="framework-card" data-step="{{step}}">
    <h3>{{title}}</h3>
    <p>{{desc}}</p>
    <span class="framework-tag">{{tag}}</span>
  </div>
{{/each}}

<!-- 机会卡片循环 -->
{{#each opportunities}}
  <div class="opportunity-card">
    <div class="opportunity-header">
      <span class="icon">{{icon}}</span>
      <h3>{{title}}</h3>
      <span class="priority-{{priority}}">{{priority}}</span>
    </div>
    <div class="opportunity-body">
      <div class="field"><div class="field-label">业务目标</div><div class="field-value highlight">{{business_goal}}</div></div>
      <div class="field"><div class="field-label">现状痛点</div><div class="field-value">{{pain_point}}</div></div>
      ...
    </div>
    {{#if feature_image}}
    <div class="opportunity-image"><img src="{{feature_image}}" alt="{{title}}" /></div>
    {{/if}}
  </div>
{{/each}}

<!-- 数据指标循环 -->
{{#each hero.stats}}
  <div class="stat-item">
    <span class="stat-number">{{number}}</span>
    <div class="stat-label">{{label}}</div>
  </div>
{{/each}}
```

## 优先级样式映射

| priority | CSS class | 颜色 |
|----------|-----------|------|
| P0 | `priority-p0` | `#00ff88` (green) |
| P1 | `priority-p1` | `#FFD700` (gold) |
| P2 | `priority-p2` | `#555555` (gray) |

## 主题变量

CSS 自定义属性（在 `:root` 中定义，按主题切换）:

```css
:root {
  --bg-dark: #0a0a0a;
  --bg-card: #151515;
  --accent-blue: #00aaff;
  --accent-gold: #FFD700;
  --accent-green: #00ff88;
  --accent-red: #ff4444;
  --accent-purple: #a855f7;
  --text-primary: #ffffff;
  --text-secondary: #a0a0a0;
  --text-muted: #555555;
  --border-subtle: #222222;
}
```

主题文件在 `assets/templates/themes/` 下:
- `dark-industrial.css` — 深色工业风（默认）
- `light-minimal.css` — 浅色极简
- `dark-cyber.css` — 赛博朋克
