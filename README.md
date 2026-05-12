# 🐱 猫鼬AI — 营销行业 AI Agent 技能库

[![Skills](https://img.shields.io/badge/skills-105-blue)](./skills/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Hermes%20%7C%20OpenClaw%20%7C%20Codex-purple)](./skills/)

> 🚀 **面向快消品、消费品、营销、咨询行业的 AI Agent Skill 开源集合。105 个即装即用的营销技能——从广告投放到 SEO、从内容策略到数据分析、从客户研究到销售赋能，全链路覆盖。**

---

## 📖 关于猫鼬AI

**猫鼬AI（MeerkatAIChina）** 是一家专注于将 AI 真正落地的科技公司。我们不画大饼、不造概念——我们在镜片镀膜车间蹲守 6 个月，只为了做出制造业真正能用的 AI 工具。

这个仓库是我们开源的 **营销行业 AI Agent 技能库**。每一个 Skill 都经过：
1. **行业专家设计** — 不是通用 AI 生成，而是由资深 IE 工程师、营销操盘手、咨询顾问联合打磨
2. **真实场景验证** — 所有方法论来自实际产线和客户项目，不是办公室里的拍脑袋
3. **多平台兼容** — 一份 SKILL.md，可在 Claude Code、Hermes Agent、OpenClaw、Codex CLI 等主流 AI Agent 框架中直接加载

---

## ⚡ 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git

# 2. 加载 Skill 到你的 AI Agent

# Claude Code
cp -r manufacturing-ai-efficiency-Skill/skills/copywriting ~/.claude/skills/

# Hermes Agent
cp -r manufacturing-ai-efficiency-Skill/skills/copywriting ~/.hermes/skills/

# OpenClaw
cp -r manufacturing-ai-efficiency-Skill/skills/copywriting ~/.openclaw/skills/

# Codex CLI
cp -r manufacturing-ai-efficiency-Skill/skills/copywriting ~/.codex/skills/
```

**然后直接在对话中提问即可**，AI Agent 会自动加载对应 Skill。例如：

> "帮我审计我的 Google Ads 账户"
> "用 PAS 框架写一篇 SaaS 产品 Landing Page"
> "分析我的竞争对手在 Facebook 上投了什么广告"

---

## 📊 技能全景（101 个 Skill / 12 大类）

### 📢 广告投放（10 个）
> 从单平台投放审计到跨平台预算分配，覆盖 Google / Meta / LinkedIn / Microsoft / TikTok 全渠道

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `google-ads` | Google Ads 全链路审计——搜索、购物、PMax、Display、YouTube 11 维诊断 | [→](./skills/google-ads/) |
| `facebook-ads` | Meta 广告（Facebook+Instagram）审计——Pixel+CAPI、受众、创意、归因全覆盖 | [→](./skills/facebook-ads/) |
| `linkedin-ads` | LinkedIn B2B 广告——ABM 策略、Lead Gen 表单、职业身份定向 | [→](./skills/linkedin-ads/) |
| `microsoft-ads` | Microsoft Advertising——Bing 搜索+LinkedIn 定向，CPC 低 30-40% 的增量渠道 | [→](./skills/microsoft-ads/) |
| `tiktok-ads` | TikTok 广告——Spark Ads、TikTok Shop、短视频创意公式 | [→](./skills/tiktok-ads/) |
| `paid-ads` | 多平台投放策略总控——平台选择、预算分配、出价策略、素材测试优先级 | [→](./skills/paid-ads/) |
| `cross-platform-audit` | 跨平台统一审计——Google+Meta+Microsoft 并行审计，合并健康评分 | [→](./skills/cross-platform-audit/) |
| `wasted-spend-finder` | 浪费预算猎手——扫描搜索词/展示位/受众/素材，输出可上传的排除清单 CSV | [→](./skills/wasted-spend-finder/) |
| `account-structure-review` | 账户结构审计——检测过度细分、预算碎片、受众重叠，输出合并方案 | [→](./skills/account-structure-review/) |
| `ad-creative` | 广告素材批量生成——多平台适配的标题、描述、完整广告变体 | [→](./skills/ad-creative/) |

### 🔍 SEO 与 AI 搜索（10 个）
> 从传统 SEO 到 AI 搜索可见度（AEO/GEO），覆盖 Google、ChatGPT、Perplexity、Claude

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `seo-audit` | 全站 SEO 审计——技术、内容、外链、本地 SEO 四大模块 | [→](./skills/seo-audit/) |
| `technical-seo-audit` | 深度技术 SEO——可爬行性、索引、Core Web Vitals、规范标签、结构化数据 | [→](./skills/technical-seo-audit/) |
| `seo-content-writer` | SEO 内容创作——品牌语音分析+关键词整合+可读性优化 | [→](./skills/seo-content-writer/) |
| `programmatic-seo` | 规模化页面生成——模板化内容+内链架构+自动化 SEO 优化 | [→](./skills/programmatic-seo/) |
| `schema-markup-generator` | Schema 结构化数据——Article/FAQ/HowTo/Product/Review 等 JSON-LD 生成 | [→](./skills/schema-markup-generator/) |
| `ai-seo` | AI 搜索引擎优化——让内容被 ChatGPT/Perplexity/Claude 引用 | [→](./skills/ai-seo/) |
| `aeo-geo-optimizer` | AEO/GEO 优化——回答引擎和生成引擎的可见度提升 | [→](./skills/aeo-geo-optimizer/) |
| `ai-discoverability-audit` | AI 搜索可见度审计——诊断品牌在 AI 搜索中的展示情况 | [→](./skills/ai-discoverability-audit/) |
| `site-architecture` | 网站架构规划——页面层级、导航、URL 结构、内链策略 | [→](./skills/site-architecture/) |
| `llms-txt` | llms.txt 生成——为 AI 引擎创建结构化内容地图 | [→](./skills/llms-txt/) |

### 📈 转化率优化 / CRO（12 个）
> 从首页到注册、从表单到弹窗、从新用户上手到付费升级，全漏斗转化率诊断和优化

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `cro-auditor` | 全漏斗 CRO 审计——LIFT 模型、启发式评估、优先级排序 | [→](./skills/cro-auditor/) |
| `landing-page-optimizer` | Landing Page 优化——首屏设计、价值主张、CTA、社交证明、移动适配 | [→](./skills/landing-page-optimizer/) |
| `homepage-audit` | 首页转化审计——6 区块加权评分、标题强制重写、影响×投入矩阵 | [→](./skills/homepage-audit/) |
| `page-cro` | 营销页面 CRO——产品页/定价页/功能页的 7 维分析框架 | [→](./skills/page-cro/) |
| `form-cro` | 表单转化优化——逐字段成本分析、单列vs多列、移动端专项 | [→](./skills/form-cro/) |
| `signup-flow-cro` | 注册流程 CRO——字段最小化、先展示价值再索取信息 | [→](./skills/signup-flow-cro/) |
| `popup-cro` | 弹窗优化——6 种触发策略、频率管控、合规要求 | [→](./skills/popup-cro/) |
| `ab-test-setup` | A/B 测试设计——假设框架、样本量计算、ICE 优先级、增长实验引擎 | [→](./skills/ab-test-setup/) |
| `ab-testing-framework` | A/B 测试方法论——频率派/贝叶斯、Z 检验、10 大陷阱 | [→](./skills/ab-testing-framework/) |
| `churn-prevention` | 流失预防——取消流程设计、动态挽留、支付追回、健康度评分 | [→](./skills/churn-prevention/) |
| `onboarding-cro` | 新用户上手优化——从注册到Aha Moment的完整激活方法论 | [→](./skills/onboarding-cro/) |
| `paywall-upgrade-cro` | 付费墙与升级转化——在恰当的时机用恰当的方式让用户付费 | [→](./skills/paywall-upgrade-cro/) |

### ✍️ 内容与文案（11 个）
> 从品牌声音提取到文案框架、从内容策略到全流程流水线

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `copywriting` | 网页文案撰写——首页/Landing/定价/功能/关于页全覆盖 | [→](./skills/copywriting/) |
| `copywriting-frameworks` | 文案框架库——AIDA/PAS/BAB/4Ps/StoryBrand 等 8 大框架 | [→](./skills/copywriting-frameworks/) |
| `copy-editing` | 文案精修——去 AI 味、强说服力、品牌一致性检查 | [→](./skills/copy-editing/) |
| `content-strategy` | 内容策略——写什么、什么时候写、写给谁 | [→](./skills/content-strategy/) |
| `content-creator` | 内容创作工具包——品牌分析+SEO+框架+社交+日历一站式 | [→](./skills/content-creator/) |
| `content-workflow` | 内容生产流水线——研究→起草→编辑→社交分发三阶段 | [→](./skills/content-workflow/) |
| `content-pipeline` | 端到端内容管道——研究→编辑审查→社交分发代理编排 | [→](./skills/content-pipeline/) |
| `content-idea-generator` | 内容创意生成——基于定位的高质量选题，告别灵感枯竭 | [→](./skills/content-idea-generator/) |
| `de-ai-ify` | 去 AI 味——分析 1000+ 篇 AI vs 人类内容，还原真实人声 | [→](./skills/de-ai-ify/) |
| `brand-voice-guidelines` | 品牌声音指南——语调矩阵、消息框架、品牌手册 | [→](./skills/brand-voice-guidelines/) |
| `voice-extractor` | 写作声音提取——从样本中捕捉写作 DNA，训练 AI 模仿你的风格 | [→](./skills/voice-extractor/) |

### 📱 社交媒体（8 个）
> LinkedIn / Twitter / Instagram / TikTok / Reddit 全平台内容创作和策略

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `social-content` | 社交媒体内容创作——5 平台适配+内容裂变+短脚本公式 | [→](./skills/social-content/) |
| `social-media-strategy` | 社交媒体策略——平台选择、内容日历、互动机制、KPI 体系 | [→](./skills/social-media-strategy/) |
| `social-card-gen` | 社交卡片生成——一篇内容生成 Twitter/LinkedIn/Reddit 多平台变体 | [→](./skills/social-card-gen/) |
| `linkedin-authority-builder` | LinkedIn 影响力建设——定位对齐→内容支柱→90 天日历 | [→](./skills/linkedin-authority-builder/) |
| `linkedin-profile-optimizer` | LinkedIn 资料优化——15 分钟评分+重写+AI 可见度检查 | [→](./skills/linkedin-profile-optimizer/) |
| `tweet-draft-reviewer` | Tweet 草稿审查——8 条声音规则评分，低于 7 分自动重写 | [→](./skills/tweet-draft-reviewer/) |
| `community-marketing` | 社区营销——从零启动到规模化运营的完整方法论 | [→](./skills/community-marketing/) |
| `reddit-insights` | Reddit 情报挖掘——从子版块提取真实用户讨论和趋势 | [→](./skills/reddit-insights/) |

### 📧 邮件与自动化（9 个）
> 冷邮件、序列设计、Newsletter、Klaviyo/Braze 营销自动化全链路

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `cold-email` | B2B 冷邮件——4 级个性化体系、多框架、自检清单 | [→](./skills/cold-email/) |
| `cold-email-outreach` | 冷邮件外联工程——个性化+可投递性+跟进节奏+合规(CAN-SPAM/GDPR) | [→](./skills/cold-email-outreach/) |
| `cold-outreach-sequence` | 冷外联序列——LinkedIn+邮件双渠道、研究驱动的个性化 | [→](./skills/cold-outreach-sequence/) |
| `email-composer` | 商务邮件撰写——外联/客户沟通/提案/跟进、语气校准 | [→](./skills/email-composer/) |
| `email-sequence` | 邮件序列设计——Drip Campaign、自动化流程、生命周期邮件 | [→](./skills/email-sequence/) |
| `newsletter-creation-curation` | Newsletter 创建与策展——行业自适应、阶段/角色/地域感知 | [→](./skills/newsletter-creation-curation/) |
| `klaviyo-analyst` | Klaviyo 营销分析——Flow/Segment/Campaign 审计、可投递性 | [→](./skills/klaviyo-analyst/) |
| `klaviyo-developer` | Klaviyo 技术集成——API/SDK/Webhook/OAuth/目录同步 | [→](./skills/klaviyo-developer/) |
| `braze` | Braze 客户互动平台——Canvas 审计、多渠道协同、数据架构 | [→](./skills/braze/) |

### 🎯 市场策略（16 个）
> 定位、定价、竞品分析、客户研究、品牌策略、营销创意、获客工具——市场营销的「战略层」

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `positioning-basics` | 定位基本功——五问定位法、竞争地图、5 项定位测试 | [→](./skills/positioning-basics/) |
| `brand-dna` | 品牌基因提取——从 URL 抓取品牌调性/色彩/字体/受众 | [→](./skills/brand-dna/) |
| `market-research` | 市场研究报告——McKinsey/BCG 风格、50+ 页、Porter 五力/SWOT | [→](./skills/market-research/) |
| `marketing-principles` | 市场营销原理——15 条永恒原则+逆向推演决策引擎 | [→](./skills/marketing-principles/) |
| `marketing-psychology` | 营销心理学——认知偏差/心理模型/行为科学在营销中的应用 | [→](./skills/marketing-psychology/) |
| `pricing-strategy` | 定价策略——定价层级/Freemium/免费试用/包装/涨价策略 | [→](./skills/pricing-strategy/) |
| `product-marketing-context` | 产品营销上下文——产品定位/ICP/竞品/消息框架一站式文档 | [→](./skills/product-marketing-context/) |
| `customer-research` | 客户研究——访谈分析+社区挖掘、JTBD、信度分级 | [→](./skills/customer-research/) |
| `customer-journey-mapping` | 客户旅程地图——从认知到拥护的全触点可视化 | [→](./skills/customer-journey-mapping/) |
| `icp-research` | 理想客户画像——痛点/异议/购买触发/社区足迹全维度 | [→](./skills/icp-research/) |
| `competitor-profiling` | 竞品画像——从 URL 抓取竞品定位/定价/消息/差异化 | [→](./skills/competitor-profiling/) |
| `competitor-ads-analyst` | 竞品广告分析——从 Facebook/Google/TikTok/LinkedIn 广告库提取竞品策略 | [→](./skills/competitor-ads-analyst/) |
| `competitor-alternatives` | 竞品对比页——SEO 优化的竞品对比和替代品页面 4 种格式 | [→](./skills/competitor-alternatives/) |
| `launch-strategy` | 发布策略——产品发布/功能公告/Product Hunt/GTM 全流程 | [→](./skills/launch-strategy/) |
| `marketing-ideas` | 营销创意引擎——139条已验证增长策略，按阶段/预算/时间线筛选 | [→](./skills/marketing-ideas/) |
| `free-tool-strategy` | 免费工具获客策略——Engineering as Marketing 全流程：构思→评估→获客→SEO | [→](./skills/free-tool-strategy/) |

### 📊 数据分析（8 个）
> Google Analytics / GTM / Looker Studio / UTM / 数据可视化 / RevOps

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `analytics-tracking` | 数据追踪体系——GA4/GTM/转化追踪/事件追踪全链路 | [→](./skills/analytics-tracking/) |
| `google-analytics` | Google Analytics 分析——流量模式/用户行为/转化漏斗诊断 | [→](./skills/google-analytics/) |
| `google-tag-manager` | GTM 容器治理——标签架构/触发逻辑/Consent Mode v2/调试 | [→](./skills/google-tag-manager/) |
| `looker-studio` | Looker Studio 仪表盘——数据可视化/数据源连接/营销报告 | [→](./skills/looker-studio/) |
| `utm-attribution-strategy` | UTM 归因策略——标准化 UTM 体系/归因模型/跨渠道衡量 | [→](./skills/utm-attribution-strategy/) |
| `data-viz-deck` | 数据可视化成品——审计数据→PPTX/HTML/Markdown 精美报告 | [→](./skills/data-viz-deck/) |
| `revops` | RevOps 收入运营——线索生命周期/线索评分/市场到销售交接 | [→](./skills/revops/) |
| `daily-briefing-builder` | 每日简报生成——从知识库拉取今日优先事项和待发内容 | [→](./skills/daily-briefing-builder/) |

### 💰 销售赋能（7 个）
> 案例研究、客户证言、Lead Magnet、推荐裂变、联合营销

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `sales-enablement` | 销售赋能——销售材料/提案PPT/异议处理/演示脚本 | [→](./skills/sales-enablement/) |
| `case-study-builder` | 案例研究构建——客户成果→结构化案例→可复用的信任资产 | [→](./skills/case-study-builder/) |
| `testimonial-collector` | 客户证言收集——系统化收集/评分/格式化客户好评 | [→](./skills/testimonial-collector/) |
| `lead-magnets` | 引流磁石——邮件获取的 Lead Magnet 规划/设计/优化 | [→](./skills/lead-magnets/) |
| `referral-program` | 推荐裂变引擎——推荐计划/联盟营销/口碑策略 | [→](./skills/referral-program/) |
| `co-marketing` | 联合营销——找合作伙伴/策划联合 Campaign/资源互换 | [→](./skills/co-marketing/) |
| `directory-submissions` | 目录提交——创业/SaaS/AI/MCP/No-Code 目录的 Backlink 获取 | [→](./skills/directory-submissions/) |

### 📄 咨询输出（3 个）
> 面向咨询顾问的专业交付物——HTML 报告、PPT 演示、多页文档

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `html-report-builder` | HTML 技术报告——深色封面+暖白内容页、Switzer+Cartograph 字体 | [→](./skills/html-report-builder/) |
| `pro-deck-builder` | 专业 PPT——RRBC 设计系统、深色封面+浅色内容、Lora+Inter 字体 | [→](./skills/pro-deck-builder/) |
| `pro-report-builder` | 专业报告——8.5×11 竖版、可定制设计系统、图表+表格+行动方案 | [→](./skills/pro-report-builder/) |

### 🛒 平台与多媒体（5 个）
> Shopify、ASO、视频/图片内容创作、YouTube 情报

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `shopify` | Shopify 电商——店铺审计/转化漏斗/追踪配置/营销工具集成 | [→](./skills/shopify/) |
| `aso-audit` | App Store 优化——Apple App Store + Google Play 列表审计评分 | [→](./skills/aso-audit/) |
| `video` | 视频内容——AI 视频制作/Remotion/Hyperframes/短视频脚本 | [→](./skills/video/) |
| `image` | 图片内容——营销用图生成/编辑/优化（Blog 主图/社媒素材/产品图） | [→](./skills/image/) |
| `youtube-summarizer` | YouTube 摘要——自动获取字幕→结构化摘要→多平台推送 | [→](./skills/youtube-summarizer/) |

### 🔎 情报与研究（2 个）
> 快速研究工具——30 天全网扫描、RSS 情报聚合

| Skill | 一句话说明 | 直达 |
|-------|-----------|------|
| `last30days` | 30 天全网扫描——Reddit+X+Web 同步、7 分钟替代 2 小时手动研究 | [→](./skills/last30days/) |
| `research-digest` | 研究文摘——RSS+Web 多源情报合成、关键发现+数据点+专家视角 | [→](./skills/research-digest/) |

---

## 🏭 制造业专项

本仓库还包含猫鼬AI的旗舰制造业产品：

| 产品 | 说明 | 直达 |
|------|------|------|
| `manufacturing-ai-efficiency-pro` | 制造业 AI 提效全链路扫描器 V2.0 — 流程拆解、AI 机会扫描、人机协同、合规闸门 | [→](./manufacturing-ai-efficiency-pro/) |

---

## 🔄 平台兼容性

所有 Skill 的 SKILL.md 遵循跨平台标准格式，一份文件可在以下 AI Agent 框架中直接加载：

| 平台 | 安装路径 | 加载方式 |
|------|----------|----------|
| **Claude Code** | `~/.claude/skills/` | 自动发现 |
| **Hermes Agent** | `~/.hermes/skills/` | 自动发现 |
| **OpenClaw** | `~/.openclaw/skills/` | 自动发现 |
| **Codex CLI** | `~/.codex/skills/` | 自动发现 |
| **Cursor** | 项目 `.cursor/skills/` | 项目级加载 |

---

## 🤝 贡献指南

欢迎贡献！请确保：

1. **SKILL.md 格式规范**：有效的 YAML frontmatter、≤1024 字符的 description、清晰的步骤化工作流
2. **附中文 README.md**：包含定位、核心能力、适用场景、使用方法
3. **相关工作流可执行**：命令/参数/路径具体明确
4. **测试通过**：在至少一个 AI Agent 平台上验证可用

提交 PR 到 `main` 分支，我们会审核后合并。

---

## 📄 许可证

MIT License © 2026 MeerkatAIChina

---

> **我们不造概念，只做能落地的工具。让每一个市场人都能用上 AI——这是猫鼬AI的承诺。**

> 🐱 [猫鼬AI 官网](https://www.meerkatai.cn/) | [GitHub](https://github.com/MeerkatAIChina)
