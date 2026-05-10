# MeerkatAIChina — AI Agent 营销技能库

[![Skills](https://img.shields.io/badge/skills-105-blue)](./skills/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Updated](https://img.shields.io/badge/updated-2026--05--10-orange)](./CHANGELOG.md)

> 🚀 面向快消品、消费品、营销、咨询行业的 AI Agent Skill 开源集合。每个 Skill 可被 Claude Code、OpenClaw、Cursor、Codex、Hermes 等 AI Agent 直接加载使用。

---

## 📖 简介

本仓库是 **MeerkatAIChina** 开源的 AI Agent 营销技能库，收录 105 个经过评估优化的营销相关 Skill，覆盖从内容创作、SEO 优化、广告投放、转化优化到数据分析的全链路营销场景。

### 什么是 Skill？

Skill 是一组可被 AI Agent 加载的专业指令集（`SKILL.md` 文件 + 可选参考文档），让 AI Agent 在特定领域表现出专家级能力。一个 Skill 定义了：
- **何时触发**：什么场景下自动激活
- **工作流程**：按步骤执行的任务链
- **专业知识**：领域特定的框架、模板、最佳实践
- **输出标准**：期望的交付物格式和质量

### 如何使用

```bash
# Claude Code
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git
cp -r skills/copywriting ~/.claude/skills/

# OpenClaw
clawhub install MeerkatAIChina/manufacturing-ai-efficiency-Skill/skills/copywriting

# Hermes Agent
cp -r skills/copywriting ~/.hermes/skills/
```

---

## 📊 技能分类总览

### 📝 内容与文案（8 个）
| Skill | 用途 |
|-------|------|
| `copywriting` | 网站文案写作与优化（首页、落地页、定价页等） |
| `copywriting-frameworks` | 框架驱动文案（AIDA、PAS、BAB 等经典框架） |
| `copy-editing` | 文案编辑润色与语气优化 |
| `content-creator` | 全栈内容营销工具箱 |
| `content-strategy` | 内容策略规划与日历管理 |
| `content-pipeline` | 端到端内容生产流水线 |
| `content-workflow` | 内容创作工作流编排 |
| `content-idea-generator` | 基于定位的内容创意生成 |

### 🔍 SEO 与搜索优化（11 个）
| Skill | 用途 |
|-------|------|
| `ai-seo` | AI 搜索优化（ChatGPT、Perplexity、Gemini 等 LLM 引用优化） |
| `seo-audit` | 全站 SEO 诊断审计 |
| `seo-content-writer` | SEO 优化内容创作 |
| `technical-seo-audit` | 深度技术 SEO 审计（爬虫、索引、Core Web Vitals） |
| `programmatic-seo` | 规模化模板页面生成 |
| `aeo-geo-optimizer` | 答案引擎优化 & 生成式引擎优化 |
| `ai-discoverability-audit` | AI 搜索可见度审计 |
| `schema-markup-generator` | 结构化数据标记生成（JSON-LD） |
| `site-architecture` | 网站架构规划与重组 |
| `llms-txt` | llms.txt 文件生成与维护 |
| `directory-submissions` | 产品目录提交（创业目录、AI 工具目录等） |

### 📊 广告与付费媒体（11 个）
| Skill | 用途 |
|-------|------|
| `google-ads` | Google Ads 平台专家（审计、优化、竞价策略） |
| `facebook-ads` | Meta 广告平台专家（Facebook & Instagram） |
| `linkedin-ads` | LinkedIn 广告平台专家 |
| `tiktok-ads` | TikTok 广告平台专家 |
| `microsoft-ads` | Microsoft Advertising (Bing) 平台专家 |
| `paid-ads` | 跨平台付费广告统一管理 |
| `ad-creative` | 广告创意生成与迭代 |
| `account-structure-review` | 广告账户结构审计 |
| `wasted-spend-finder` | 广告浪费支出分析 |
| `competitor-ads-analyst` | 竞品广告情报分析 |
| `cross-platform-audit` | 跨平台广告统一审计 |

### 🎯 转化优化 CRO（8 个）
| Skill | 用途 |
|-------|------|
| `page-cro` | 页面转化率优化 |
| `form-cro` | 表单转化优化 |
| `signup-flow-cro` | 注册流程转化优化 |
| `popup-cro` | 弹窗/模态框转化优化 |
| `cro-auditor` | 全站 CRO 审计 |
| `homepage-audit` | 首页/落地页转化审计 |
| `ab-test-setup` | A/B 测试规划与实施 |
| `ab-testing-framework` | A/B 和多变量测试方法论 |

### 📧 邮件营销（5 个）
| Skill | 用途 |
|-------|------|
| `cold-email` | B2B 冷邮件撰写 |
| `cold-email-outreach` | 冷邮件外联序列设计 |
| `cold-outreach-sequence` | LinkedIn + 邮件混合外联序列 |
| `email-sequence` | 邮件自动序列 / Drip Campaign |
| `email-composer` | 商务/营销邮件起草 |

### 🔬 市场研究与分析（8 个）
| Skill | 用途 |
|-------|------|
| `competitor-alternatives` | 竞品对比/替代页面创建 |
| `competitor-profiling` | 竞品深度画像分析 |
| `customer-research` | 客户调研与分析 |
| `customer-journey-mapping` | 客户旅程地图绘制 |
| `icp-research` | 理想客户画像构建 |
| `research-digest` | 结构化研究简报生成 |
| `reddit-insights` | Reddit 语义搜索与洞察 |
| `last30days` | 近 30 天全网话题研究 |

### 🏷️ 品牌与定位（6 个）
| Skill | 用途 |
|-------|------|
| `brand-dna` | 品牌 DNA 提取（URL → 品牌标识） |
| `brand-voice-guidelines` | 品牌语调与信息框架 |
| `positioning-basics` | 品牌定位方法论 |
| `product-marketing-context` | 产品营销上下文文档 |
| `marketing-principles` | 经典营销原理应用 |
| `marketing-psychology` | 营销心理学原理应用 |

### 📱 社交媒体（8 个）
| Skill | 用途 |
|-------|------|
| `social-content` | 社交媒体内容创作 |
| `social-card-gen` | 多平台社媒卡片生成 |
| `social-preview` | Open Graph 预览图生成 |
| `social-media-strategy` | 社媒策略与内容日历 |
| `linkedin-authority-builder` | LinkedIn 思想领导力建设 |
| `linkedin-profile-optimizer` | LinkedIn 个人资料优化 |
| `tweet-draft-reviewer` | 推文草稿评审 |
| `community-marketing` | 社区营销与用户运营 |

### 📈 分析与数据（6 个）
| Skill | 用途 |
|-------|------|
| `analytics-tracking` | 分析追踪设置与审计 |
| `google-analytics` | GA 数据分析 |
| `google-tag-manager` | GTM 容器管理 |
| `looker-studio` | Looker Studio 仪表盘 |
| `data-viz-deck` | 数据可视化报告 |
| `utm-attribution-strategy` | UTM 参数与归因策略 |

### 🚀 增长与留存（7 个）
| Skill | 用途 |
|-------|------|
| `churn-prevention` | 客户流失预防 |
| `referral-program` | 推荐计划设计 |
| `lead-magnets` | 引流磁铁设计 |
| `launch-strategy` | 产品发布策略 |
| `co-marketing` | 联合营销伙伴策略 |
| `aso-audit` | App Store/Google Play ASO 审计 |
| `revops` | 收入运营与线索管理 |

### 🛠️ 电商与平台（4 个）
| Skill | 用途 |
|-------|------|
| `shopify` | Shopify 电商营销 |
| `klaviyo-analyst` | Klaviyo 营销分析 |
| `klaviyo-developer` | Klaviyo 开发者集成 |
| `braze` | Braze 客户互动平台 |

### 📄 文档与报告（6 个）
| Skill | 用途 |
|-------|------|
| `case-study-builder` | 案例研究文档生成 |
| `sales-enablement` | 销售赋能材料（Pitch Deck、一页纸等） |
| `release-notes` | Changelog 自动生成 |
| `html-report-builder` | HTML 技术报告生成 |
| `pro-report-builder` | 专业报告与多页文档 |
| `pro-deck-builder` | 专业 Slide Deck 生成 |

### 🎬 多媒体（4 个）
| Skill | 用途 |
|-------|------|
| `image` | AI 营销图片生成与编辑 |
| `video` | AI 营销视频制作 |
| `voice-extractor` | 写作风格提取与文档化 |
| `youtube-summarizer` | YouTube 视频摘要生成 |

### 🔧 开发与效率工具（13 个）
| Skill | 用途 |
|-------|------|
| `repo-scaffold` | GitHub 仓库脚手架初始化 |
| `repo-health` | 仓库健康度审计 |
| `safe-push` | 推送前安全检查 |
| `sync-repos` | 多仓库同步管理 |
| `dep-audit` | 跨仓库依赖审计 |
| `frontend-design` | 高质量前端界面设计 |
| `github-readme` | GitHub README 自动生成 |
| `testimonial-collector` | 客户证言系统化收集 |
| `de-ai-ify` | 去除 AI 味，恢复人声 |
| `go-mode` | 自主目标执行引擎 |
| `plan-my-day` | 日计划智能生成 |
| `daily-briefing-builder` | 每日简报生成 |
| `newsletter-creation-curation` | B2B Newsletter 创建 |

---

## 🏭 制造业 AI 提效分析

本仓库还包含一个独立的制造业专项 Skill：

| Skill | 用途 |
|-------|------|
| `manufacturing-ai-efficiency-pro` | 制造业 AI 提效分析 V2.0 — 流程拆解、AI 机会扫描、人机协同 T34 模型、三层流程图 |

详见 [manufacturing-ai-efficiency-pro/](./manufacturing-ai-efficiency-pro/)

---

## 🔄 持续更新

本仓库由 **SKILL 自动开源日更流水线** 每日维护：

1. 每日 14:30（北京时间）自动扫描 GitHub 和 Hermes 生态
2. 发现新的快消品/消费品/营销/咨询类 Skill
3. 通过达尔文 8 维度评估体系进行至少 5 轮优化迭代
4. 自动推送至 `jdyt` 分支
5. 同步更新本 README

每个 Skill 目录下均包含：
- `SKILL.md` — 技能主定义文件
- `README.md` — 技能详细说明（深入剖析能力、作用、使用方法）

---

## 🤝 贡献

欢迎通过 Issue 或 PR 贡献新的营销 Skill。贡献前请确保：
- SKILL.md 符合 Claude Code / OpenClaw 格式规范
- 包含完整的 frontmatter（name、description、version、author、license）
- 附有 README.md 说明文档

---

## 📄 许可证

MIT License © 2026 MeerkatAIChina
