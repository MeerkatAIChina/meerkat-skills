---
name: competitor-ads-analyst
description: "Extract and analyze competitor advertising from public ad libraries (Facebook Ad Library, Google Ads Transparency Center, TikTok, LinkedIn). Identifies messaging patterns, creative formats, pain points targeted, and positioning gaps. Use for competitive intelligence, campaign planning, and creative inspiration."
version: "1.0.0"
author: "Rebecca Rae Barton"
author_url: "https://github.com/thatrebeccarae"
license: "MIT"
optimized: true
optimized_date: "2026-05-11"
metadata:
  version: "1.0.0"
  category: paid-media
  domain: competitive-intelligence
  updated: "2026-03-13"
  tested: "2026-03-17"
  tested_with: "Claude Code v2.1"
  hermes:
    compatible: true
    min_version: "1.0.0"
---

# Competitor Ads Analyst

Analyze competitor advertising from public ad libraries to understand what messaging, creative formats, and positioning strategies are working.

## Install

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git && cp -r claude-marketing/skills/competitor-ads-analyst ~/.claude/skills/
```

## Core Capabilities

- Extract ads from public ad libraries (Facebook, Google, TikTok, LinkedIn)
- Categorize ad creative by format, message type, and funnel stage
- Identify pain points competitors highlight (with frequency scoring)
- Map competitor positioning and find white space
- Extract headline and copy formulas
- Track creative format trends (UGC, before/after, testimonial, etc.)
- Generate competitive intelligence reports and swipe files

## Ad Library Access

| Platform | URL | Access |
|----------|-----|--------|
| Meta (Facebook/Instagram) | facebook.com/ads/library | Free, public |
| Google Ads | adstransparency.google.com | Free, public |
| TikTok | library.tiktok.com | Free, public |
| LinkedIn | linkedin.com/ad-library | Requires account |

## Workflow

### 1. Define Scope

- **Competitors:** 3-5 companies to analyze
- **Timeframe:** Last 30, 60, or 90 days
- **Platforms:** Which ad libraries to search
- **Focus:** Messaging, creative format, audience targeting, or all

### 2. Extract Ads

For each competitor, collect:
- Ad copy (headline, primary text, CTA)
- Creative format (image, video, carousel, UGC)
- Landing page URL
- Active date range (if visible)
- Platform and placement

### 3. Categorize

Classify each ad by:

**Message Type:**
- Pain point (problem-aware)
- Solution (product-aware)
- Social proof (testimonial, case study, press)
- Offer (discount, free trial, demo)
- Educational (how-to, tip, guide)
- Brand (awareness, positioning)

**Funnel Stage:**
- Top (awareness, problem education)
- Middle (consideration, comparison)
- Bottom (conversion, offer, urgency)

**Creative Format:**
- Static image
- Video (short <15s, medium 15-60s, long >60s)
- Carousel
- UGC-style
- Before/after
- Screenshot/product demo
- Testimonial quote card
- Data/stat visualization

### 4. Analyze Patterns

- **Pain point frequency:** Which problems appear most across competitors?
- **Message clustering:** Are competitors saying the same things?
- **Format preferences:** Which creative types are most used?
- **Positioning map:** Where does each competitor sit on key dimensions?
- **Gaps:** What messages/angles are NO competitors using?

### 5. Generate Output

Choose from: competitive report, swipe file, messaging matrix, or creative brief.

## Key Principles

1. **Analyze patterns, not individual ads.** One ad is an anecdote; 20 ads from 5 competitors is intelligence.
2. **Look for gaps, not just patterns.** The most valuable finding is what competitors are NOT saying.
3. **Separate observation from recommendation.** Report what you see, then separately recommend what to do with it.
4. **Date everything.** Competitive intelligence decays fast.
5. **Never copy, always adapt.** The goal is informed inspiration, not plagiarism.

For analysis frameworks and output templates, see [REFERENCE.md](REFERENCE.md).

---

## 中国市场适配

针对中国数字广告生态的竞品广告分析方法，覆盖中国主流平台和特有的数据采集方式。

### 中国广告平台竞品情报源

与国际市场不同，中国缺乏统一的公开广告库。以下是可用的竞品广告情报来源：

| 平台 | 情报获取方式 | 难度 |
|------|------------|------|
| **抖音/巨量引擎** | 巨量创意（cc.oceanengine.com）搜索竞品素材 | 中等 |
| **腾讯广告** | 创意中心（需广告主账号）查看行业素材 | 较高 |
| **小红书** | 搜索品牌名+关键词，查看信息流和搜索广告 | 低 |
| **快手** | 快手广告创意中心（ad.e.kuaishou.com） | 中等 |
| **百度** | 搜索品牌词查看竞价排名和创意样式 | 低 |
| **微博** | 粉丝通广告可部分可见，超话/话题页监测 | 中等 |
| **B站** | 花火平台查看UP主商单，信息流广告监测 | 中等 |

### 中国竞品广告分析专属维度

除国际通用的分析维度外，中国市场需额外关注：

#### 广告合规策略差异
- 竞品如何规避广告法敏感词？（极限词替代话术）
- 行业准入资质展示方式（金融/医疗/教育）
- 特殊品类广告标识规范程度

#### KOL/KOC投放分析
- 竞品合作的达人量级分布（头部/腰部/KOC）
- 达人内容风格和口播脚本模式
- 评论区互动策略（置顶链接、引导私信、评论区抽奖）
- 挂车/小黄车/购物车等转化组件使用

#### 私域引流模式
- 是否引导至企业微信/个人微信？
- 社群二维码/小程序跳转路径
- 公众号关注引流话术
- 直播引流短视频的素材模式

#### 直播广告素材
- 竞品直播间高光切片的内容模式
- 直播预热视频的创意套路
- 千川/巨量千川投放的直播间引流素材

### 竞品分析本地化框架

```
竞品名称: [品牌]
├── 主投平台: 抖音 / 腾讯 / 小红书 / 快手 / B站
├── 素材类型分布:
│   ├── 信息流视频 (XX%)
│   ├── 搜索广告 (XX%)
│   ├── KOL商单 (XX%)
│   └── 直播引流 (XX%)
├── 核心卖点矩阵:
│   ├── 痛点角度: [描述]
│   ├── 场景角度: [描述]
│   └── 信任角度: [描述]
├── 差异化定位:
│   ├── 竞品强调: [核心信息]
│   └── 市场空白: [竞品未覆盖的角度]
└── 投放节奏:
    ├── 高频投放时段: [时间/节点]
    └── 大促策略: [618/双11/年货节表现]
```

### 工具辅助

- **巨量创意**：搜索和下载竞品素材，查看投放数据和互动指标
- **新榜/蝉妈妈/飞瓜**：抖音/快手/小红书的达人投放和素材监测
- **App Growing**：国内移动广告素材追踪
- **ADX 广告交换**：广告交易平台的数据分析
- **百度指数/微信指数**：品牌搜索热度趋势对照广告投放节奏

### 隐私与合规

- 竞品分析仅用于内部策略参考，不对外发布未授权数据
- 不得爬取或破解平台后端接口
- 引用公开数据时标注来源和时间
- 遵守《个人信息保护法》和《数据安全法》
