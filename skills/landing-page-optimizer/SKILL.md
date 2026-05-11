---
name: landing-page-optimizer
description: Landing page audit and optimization for conversion. Covers above-the-fold design, value propositions, CTAs, social proof placement, form design, page speed, and mobile optimization. Use when the user asks about landing page optimization, conversion rate improvement, page audits, or CTA optimization.
version: "1.0.0"
license: MIT
origin: custom
author: Rebecca Rae Barton
author_url: https://github.com/thatrebeccarae
metadata:
  version: 1.0.0
  category: growth
  domain: landing-pages
  updated: 2026-03-18
  tested: 2026-03-18
  tested_with: "Claude Code v2.1"
  hermes:
    tags: [landing-page, cro, conversion, ux, mobile-optimization]
    related_skills: [cro-auditor, ab-testing-framework, copywriting-frameworks, frontend-design, technical-seo-audit, page-cro]
---

# Landing Page Optimizer

Audit and optimize landing pages for maximum conversion.

## Install

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git && cp -r claude-marketing/skills/landing-page-optimizer ~/.claude/skills/
```

## Audit Framework

### Above the Fold (First 5 Seconds)

The visitor must answer 3 questions instantly:
1. **What is this?** (Clear headline)
2. **Why should I care?** (Benefit-focused subheadline)
3. **What do I do next?** (Visible CTA)

### Hero Layout Patterns

| Pattern | Best For | Structure |
|---------|----------|-----------|
| **Left copy / right visual** | SaaS, B2B | Headline + CTA left, product screenshot right |
| **Centered hero** | Simple offers | Centered headline, subheadline, CTA |
| **Video hero** | Complex products | Autoplay background or embedded explainer |
| **Social proof hero** | High-trust needed | Headline with customer logos or metrics |
| **Split test** | Dual audiences | Two distinct paths with separate CTAs |

### Value Proposition Hierarchy

```
H1: Primary benefit (what outcome they get)
Subheadline: How you deliver it (mechanism or differentiator)
Supporting points: 3 proof points or features (bullets)
CTA: Specific action + anxiety reducer
```

### CTA Optimization

**Text:** Action verb + specific outcome ("Start Free Trial" not "Submit")
**Design:** High contrast to background, generous padding, whitespace around it
**Placement:** Above fold, after each content section, sticky on scroll
**Microcopy:** Reduce anxiety below CTA ("No credit card required", "Cancel anytime")

### Social Proof Patterns

| Type | Placement | Impact |
|------|-----------|--------|
| Customer logos | Below hero | Trust (B2B) |
| Metric ("50,000+ users") | Near headline | Scale proof |
| Star rating | Near CTA | Purchase confidence |
| Testimonial quote | Mid-page | Emotional proof |
| Case study result | Deep in page | Detailed proof |
| Trust badges | Near form/checkout | Security |

### Form Optimization

- Every field removed increases completion 5-10%
- Labels above fields (never placeholder-only)
- Inline validation (real-time, not on submit)
- Smart defaults and autofill (autocomplete attributes)
- Multi-step forms outperform single long forms
- Progress indicator for multi-step

### Mobile Optimization

- Touch targets minimum 48x48px
- Single column layout
- Thumb-friendly CTA placement (bottom half of screen)
- No horizontal scrolling
- Simplified navigation (hamburger or none)
- Fast load (LCP <2.5s on 4G)

## Conversion Benchmarks

| Page Type | Good | Average | Poor |
|-----------|------|---------|------|
| SaaS trial signup | >5% | 2-5% | <2% |
| E-commerce product | >3% | 1.5-3% | <1.5% |
| Lead gen (B2B) | >10% | 5-10% | <5% |
| Newsletter signup | >5% | 2-5% | <2% |
| Webinar registration | >30% | 15-30% | <15% |

## Anti-Patterns

1. **Multiple competing CTAs** — one primary action per page
2. **Feature-focused headline** — lead with benefit, not feature
3. **Stock photos** — real product screenshots or real people
4. **Navigation on landing pages** — remove nav for paid traffic pages
5. **Below-fold CTA only** — always have CTA above the fold
6. **No social proof** — every landing page needs trust signals
7. **Slow load time** — every 100ms delay costs 1% conversion
8. **Desktop-only design** — 60%+ traffic is mobile

## Integration with Other Skills

- **cro-auditor** — Broader CRO audit framework; this skill deep-dives on individual pages
- **ab-testing-framework** — Test the changes this skill recommends
- **copywriting-frameworks** — Apply PAS/AIDA to landing page copy
- **frontend-design** — Implement the optimized page design
- **technical-seo-audit** — Page speed and technical optimization

## 中国市场适配

### 中国落地页平台

- **微信落地页 (WeChat Landing Page)** — 微信生态内的落地页，需适配微信内置浏览器（iOS微信对`position:fixed`支持有限）、微信JS-SDK集成
- **百度营销页** — 百度搜索推广落地页，需遵循百度质量度评分规则
- **抖音企业号主页** — 抖音生态内的品牌落地页，重视短视频内容引导
- **小红书专业号主页** — 小红书品牌落地页，强调种草内容和用户笔记互动

### 百度SEO注意事项

- 百度搜索对落地页有**质量度评分**机制，直接影响广告展现概率和点击成本
- 页面打开速度必须 **<3秒**（百度基木鱼标准）
- 内容必须与推广关键词**高度相关**，标题和描述不得有歧义
- 禁止**恶意跳转**（如自动跳转到其他域名的下载页）
- 页面底部需有明确的**品牌信息和联系方式**

### ICP备案

- 所有在中国大陆运营的落地页域名必须完成**ICP备案**（工信部ICP备案号）
- 未备案域名可能被运营商（中国电信、中国联通、中国移动）**直接屏蔽**
- 涉及经营性或电商的还需要**ICP经营许可证**（增值电信业务经营许可证）
- 落地页底部应展示 **ICP备案号**，并链接至工信部备案查询页面（https://beian.miit.gov.cn）

### 中国移动端UX特殊考虑

- **微信内置浏览器兼容性**：iOS微信中`position:fixed`不可靠，建议使用`position:absolute`配合JS滚动处理；`backdrop-filter`不被支持
- **小程序落地页限制**：微信小程序webview内嵌H5落地页，需配置业务域名白名单，且不支持直接唤起其他APP
- **拇指操作区**：中国用户普遍单手操作，核心CTA应放在屏幕下半部
- **二维码入口**：大量中国落地页通过二维码扫码进入，需确保二维码对应的URL参数可追踪

### 广告法规合规

- **广告法禁用词**：不得使用"第一"、"最"、"唯一"、"国家级"、"顶级"、"绝对"等极限用语
- **弹窗广告**：必须有**明显关闭按钮**（不得自动关闭、不得难以识别），违反可被罚款
- **用户信息收集**：需弹出**隐私协议弹窗**，明确告知信息收集目的、使用范围、第三方共享情况
- **价格标注**：涉及价格对比需标注原价依据（如"划线价"需有成交记录支撑）
- **证照展示**：涉及医疗、金融、教育等行业需展示经营许可证照

### 中国CTA规范

- 中国用户偏好引导性CTA文案：
  - ✅ "立即咨询" / "免费咨询"
  - ✅ "免费领取" / "领取优惠" / "领取福利"
  - ✅ "立即体验" / "免费试用"
  - ✅ "查看详情" / "了解更多"
- 避免西式直接CTA如"Start Free Trial"、"Get Started"，应改为中文语境下的温和引导
- CTA按钮常搭配**紧迫感微文案**："仅限今日"、"剩余名额 32"、"已有 12,856 人领取"

### 中国落地页信任信号

- **用户评价截图**（带真实头像和打码昵称）> 客户Logo墙
- **销量数据**："累计销量 100万+" 比 "Trusted by 10,000+ companies" 更有说服力
- **明星/KOL背书**（小红书达人、抖音达人、微博大V）效果远超客户Logo展示
- **媒体报道标志**：腾讯、新浪、网易、36氪等国内知名媒体报道
- **行业认证/奖牌**：国家高新技术企业、ISO认证、行业协会会员等
- **实时数据**："今日已有 328 人咨询" 比静态评价更有说服力
