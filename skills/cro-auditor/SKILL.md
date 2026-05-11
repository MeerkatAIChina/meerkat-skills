---
name: cro-auditor
description: "Conversion Rate Optimization auditing for landing pages, signup flows, checkout funnels, forms, and CTAs. Identifies friction points, runs heuristic evaluations, produces prioritized recommendations using ICE/PIE frameworks. Use when the user asks about conversion optimization, funnel analysis, landing page audits, form optimization, CTA testing, or checkout improvement."
version: "1.0.0"
author: "Rebecca Rae Barton"
author_url: "https://github.com/thatrebeccarae"
license: "MIT"
optimized: true
optimized_date: "2026-05-11"
metadata:
  version: "1.0.0"
  category: growth
  domain: conversion-optimization
  updated: "2026-03-18"
  tested: "2026-03-18"
  tested_with: "Claude Code v2.1"
  hermes:
    compatible: true
    min_version: "1.0.0"
---

# CRO Auditor

Conversion Rate Optimization — audit landing pages, funnels, forms, and CTAs for friction and opportunities.

## Install

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git && cp -r claude-marketing/skills/cro-auditor ~/.claude/skills/
```

## Audit Framework

### Heuristic Evaluation (LIFT Model)

Score each page element on 6 dimensions:

| Factor | Question | Increases/Decreases Conversion |
|--------|----------|-------------------------------|
| **Value Proposition** | Is the benefit clear and compelling? | Increases |
| **Relevance** | Does this match what brought the user here? | Increases |
| **Clarity** | Is the message and action obvious? | Increases |
| **Urgency** | Is there a reason to act now? | Increases |
| **Anxiety** | Are there concerns about taking action? | Decreases |
| **Distraction** | Are there elements competing for attention? | Decreases |

### Page-Level Audit Checklist

#### Above the Fold
- [ ] Value proposition visible without scrolling
- [ ] Primary CTA visible and prominent
- [ ] Hero image/visual supports the message (not stock photo)
- [ ] Navigation does not distract from primary conversion goal
- [ ] Page loads in under 2.5 seconds (LCP)

#### Value Proposition
- [ ] Headline communicates specific benefit (not feature)
- [ ] Subheadline provides supporting detail
- [ ] Unique differentiator is clear (why you vs alternatives)
- [ ] Social proof near the value proposition (logos, count, rating)

#### Call to Action
- [ ] CTA text is action-oriented and specific ("Start Free Trial" not "Submit")
- [ ] CTA button contrasts with page design (stands out visually)
- [ ] Single primary CTA per page section (no competing actions)
- [ ] CTA appears multiple times on long pages (top, middle, bottom)
- [ ] Microcopy near CTA reduces anxiety ("No credit card required")

#### Social Proof
- [ ] Customer logos (if B2B)
- [ ] Testimonials with real names, photos, and specific results
- [ ] Case studies or metrics ("Helped 5,000+ companies increase revenue by 34%")
- [ ] Trust badges (security, certifications, awards)
- [ ] User count or activity ("Join 50,000+ marketers")

#### Forms
- [ ] Minimum fields necessary (every field reduces conversion 5-10%)
- [ ] Labels above fields (not placeholder-only)
- [ ] Inline validation with helpful error messages
- [ ] Progress indicator for multi-step forms
- [ ] Autofill enabled (autocomplete attributes)
- [ ] Mobile-friendly input types (tel, email, number)

#### Friction & Anxiety
- [ ] No unexpected costs or requirements revealed late
- [ ] Privacy policy and terms linked (not gating)
- [ ] Money-back guarantee or free trial clearly stated
- [ ] Contact information visible (phone, chat, email)
- [ ] FAQ section addressing common objections

### Funnel Analysis

#### Funnel Mapping

```
Awareness → Interest → Desire → Action → Retention
   ↓          ↓          ↓        ↓          ↓
 Ad/SEO → Landing → Pricing → Signup → Onboarding
            Page      Page      Form      Flow
```

For each stage:
1. **Traffic volume**: How many users enter this stage?
2. **Drop-off rate**: What percentage leave without advancing?
3. **Top exit pages**: Where exactly do users abandon?
4. **Friction indicators**: Time on page, scroll depth, rage clicks

#### Conversion Benchmarks

| Page Type | Good | Average | Poor |
|-----------|------|---------|------|
| Landing page (paid traffic) | >5% | 2-5% | <2% |
| Landing page (organic) | >3% | 1-3% | <1% |
| Signup form | >25% | 10-25% | <10% |
| Checkout (e-commerce) | >3% | 1.5-3% | <1.5% |
| Free trial → paid | >25% | 10-25% | <10% |
| Email opt-in | >5% | 2-5% | <2% |
| Pricing page → signup | >10% | 5-10% | <5% |

### Prioritization Frameworks

#### ICE Score

| Dimension | Definition | Scale |
|-----------|-----------|-------|
| **Impact** | How much will this change improve conversion? | 1-10 |
| **Confidence** | How sure are we this will work? | 1-10 |
| **Ease** | How easy is it to implement? | 1-10 |

**ICE Score** = (Impact + Confidence + Ease) / 3

#### PIE Score

| Dimension | Definition | Scale |
|-----------|-----------|-------|
| **Potential** | How much room for improvement? | 1-10 |
| **Importance** | How valuable is the traffic to this page? | 1-10 |
| **Ease** | How easy is it to run a test? | 1-10 |

**PIE Score** = (Potential + Importance + Ease) / 3

## Audit Output Format

### Executive Summary
- Current conversion rate vs benchmark
- Top 3 conversion killers identified
- Estimated revenue impact of fixes
- Quick wins (implementable in <1 day)

### Issue Format

```
**Issue:** [What is wrong]
**Location:** [Page/element affected]
**Impact:** [HIGH/MEDIUM/LOW] — [Estimated conversion impact]
**Evidence:** [Data, heuristic principle, or benchmark comparison]
**Fix:** [Specific recommendation]
**Test:** [A/B test hypothesis: "Changing X will increase Y by Z%"]
**ICE Score:** [X/10]
```

### A/B Test Recommendations

For each recommendation, provide:
- **Hypothesis**: If we [change], then [metric] will [improve/increase] because [reason]
- **Primary metric**: The conversion metric to measure
- **Minimum sample size**: Based on current traffic and expected effect size
- **Test duration**: Minimum days to reach significance (usually 2-4 weeks)

## Common Conversion Killers

1. **Slow page load** — Every 100ms delay reduces conversion by 1%
2. **Unclear value proposition** — Visitor cannot answer "What is this and why should I care?" in 5 seconds
3. **Too many form fields** — Each additional field reduces completion by 5-10%
4. **Weak CTA** — Generic text ("Submit", "Click Here") vs specific ("Start Free Trial")
5. **No social proof** — 92% of consumers read reviews before purchasing
6. **Hidden costs** — Unexpected shipping/fees are the #1 reason for cart abandonment
7. **Competing CTAs** — Multiple equal-weight actions create decision paralysis
8. **Mobile friction** — Tiny buttons, horizontal scroll, slow load on mobile
9. **Trust deficit** — No security badges, reviews, or contact info
10. **Exit without capture** — No email capture, exit intent, or remarketing pixel

## Integration with Other Skills

- **google-analytics** — Pull conversion data to ground CRO recommendations in real metrics
- **landing-page-optimizer** — Deep-dive on specific landing pages (when built)
- **a-b-testing-framework** — Design and analyze tests for CRO recommendations (when built)
- **pro-report-builder** — Generate professional CRO audit deliverable

---

## 中国市场适配

针对中国电商和SaaS环境的转化率优化指南，涵盖平台特有规则、支付习惯和合规要求。

### 中国主流电商平台转化优化

#### 天猫/淘宝详情页优化

| 维度 | 优化要点 |
|------|---------|
| **主图** | 前5张决定点击率，第1张白底产品图，第2张场景图，第3张卖点图，第4张细节图，第5张对比/尺寸图 |
| **详情页首屏** | 3秒内展示核心卖点+促销信息，视频优先于图文 |
| **SKU引导** | 默认选中性价比最高SKU（而非最低价），减少决策时间 |
| **评价区** | "问大家"板块需主动运营，买家秀≥50条对转化有显著提升 |
| **店铺DSR** | 评分低于4.7会显著降低转化，需监测描述/服务/物流三项 |

#### 京东商品页优化

| 维度 | 优化要点 |
|------|---------|
| **京东好店标识** | 直接影响搜索加权和用户信任，保持认证状态 |
| **京东物流标识** | "京东物流/211限时达"标签对转化提升20-30% |
| **PLUS会员价** | 展示PLUS专享价吸引高价值用户 |
| **问答区** | 需定期维护，专业性回答提升转化 |
| **主图视频** | 京东对主图视频有流量加权 |

#### 拼多多转化要点

| 维度 | 优化要点 |
|------|---------|
| **价格锚点** | "已拼XX万件"和"单独购买价vs拼单价"对比是核心转化驱动 |
| **限时/限量感** | 倒计时和库存余量展示触发紧迫感 |
| **多多果园/砍价** | 社交裂变组件嵌入转化路径 |
| **退货包运费** | 显著降低决策焦虑 |
| **评价** | 带图/带视频评价权重远高于纯文字 |

### 中国电商支付与信任要素

**支付方式覆盖：**
- 支付宝（覆盖率最高，必选项）
- 微信支付（小程序/社交电商必备）
- 花呗/白条分期（高客单价商品转化利器，需标注费率）
- 云闪付/银行卡（补充覆盖）

**信任信号本地化：**
- 天猫/京东官方认证标识优先于国际安全认证
- "7天无理由退换" 是底线信任要素（非加分项）
- "运费险" 标识对女装/鞋靴品类转化影响显著
- "假一赔十" 承诺比 "正品保证" 更有说服力
- 企业店铺认证 + 营业执照公示
- 在线客服响应速度（消费者对客服即时响应有高期待）

### 中国SaaS与B2B转化优化

**微信生态转化路径：**
```
公众号文章/视频号 → 企微名片/社群二维码 → 企微私域 → Demo预约/试用
```

关键优化点：
- 落地页必须适配微信内置浏览器（非Safari/Chrome标准）
- 表单字段最少化（手机号+验证码优于邮箱注册）
- 小程序形态优于H5（加载更快，微信生态内转化率高3-5倍）
- 企业微信客服组件：嵌入网页的即时通讯入口

**ICP备案与合规：**
- 所有对外服务页面必须有ICP备案号（页脚展示）
- 涉及经营类目需EDI/ICP许可证
- 隐私政策必须符合《个人信息保护法》：
  - 明确告知收集哪些信息
  - 说明使用目的和范围
  - 提供撤回同意的方式
  - Cookie/SDK收集需单独弹窗确认

### 中国移动端转化优化要点

移动端流量占比超过90%的中国市场，移动优化是CRO的基础：

- **首屏加载**：2秒内完成（小程序H5场景下用户耐心更低）
- **一键登录**：接入运营商一键登录（免验证码），转化率提升30-50%
- **微信授权登录**：减少注册摩擦，非敏感场景首选
- **悬浮窗/客服按钮**：右下角悬浮客服图标是标配（不要用弹窗覆盖整个屏幕）
- **底部固定CTA**：移动端始终可见的购买/咨询按钮
- **分期免息标识**：高客单价品类（3C/家电/教育）在价格旁标注"X期免息"

### 中国CRO特有合规红线

1. **价格标注**：《价格法》要求明确标注原价和促销价，原价须有成交记录支撑
2. **虚假促销**：不得先涨后降，大促期间价格需有历史成交最低价约束
3. **刷单/刷评**：《反不正当竞争法》和《电子商务法》明确禁止，平台稽查严格
4. **好评返现**：天猫/京东/美团等平台禁止"好评返现卡"，违规可导致下架
5. **诱导分享**：微信生态禁止利益诱导分享朋友圈/群聊
6. **弹窗广告**：必须确保一键关闭，不得有关闭后继续弹出的行为
