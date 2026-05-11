# MeerkatAIChina — AI Agent 营销技能库

[![Skills](https://img.shields.io/badge/skills-108-blue)](./skills/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Updated](https://img.shields.io/badge/updated-2026-05-11-orange)](./CHANGELOG.md)

> 🚀 面向快消品、消费品、营销、咨询行业的 AI Agent Skill 开源集合。每个 Skill 可被 Claude Code、OpenClaw、Cursor、Codex、Hermes 等 AI Agent 直接加载使用。

---

## 📖 简介

本仓库是 **MeerkatAIChina** 开源的 AI Agent 营销技能库，收录 108 个营销相关 Skill，覆盖从内容创作、SEO、广告投放到数据分析的全链路场景。

### 如何使用

```bash
# Claude Code
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git
cp -r skills/copywriting ~/.claude/skills/

# Hermes Agent
cp -r skills/copywriting ~/.hermes/skills/
```

### Skill 质量

每个 Skill 通过机器检查（6 维度 60 分制）确保基础质量：Frontmatter 规范、工作流清晰、异常处理、用户确认点、指令具体性、引用完整性。

当前通过率：33/108（31%）

---

## 📊 技能分类总览

### 📝 内容与文案（8 个）
| Skill | 机器检查 | 状态 |
|-------|---------|------|
| `copywriting` | 58/60 | ✅ 已加工 |
| `copywriting-frameworks` | 38/60 | ⏳ 待加工 |
| `content-idea-generator` | 36/60 | ⏳ 待加工 |
| `content-strategy` | 53/60 | ✅ 已加工 |
| `content-workflow` | 36/60 | ⏳ 待加工 |
| `content-creator` | 33/60 | ⏳ 待加工 |
| `content-pipeline` | 33/60 | ⏳ 待加工 |
| `copy-editing` | 31/60 | ⏳ 待加工 |

### 🔍 SEO与搜索优化（11 个）
| Skill | 机器检查 | 状态 |
|-------|---------|------|
| `site-architecture` | 45/60 | ✅ 通过 |
| `schema-markup-generator` | 44/60 | ✅ 通过 |
| `ai-seo` | 43/60 | ✅ 已加工 |
| `llms-txt` | 42/60 | ✅ 通过 |
| `ai-discoverability-audit` | 41/60 | ⏳ 待加工 |
| `aeo-geo-optimizer` | 39/60 | ✅ 通过 |
| `programmatic-seo` | 38/60 | ⏳ 待加工 |
| `technical-seo-audit` | 38/60 | ⏳ 待加工 |
| `seo-audit` | 37/60 | ✅ 通过 |
| `directory-submissions` | 36/60 | ⏳ 待加工 |
| `seo-content-writer` | 36/60 | ⏳ 待加工 |

### 📊 广告与付费媒体（11 个）
| Skill | 机器检查 | 状态 |
|-------|---------|------|
| `account-structure-review` | 44/60 | ✅ 通过 |
| `cross-platform-audit` | 38/60 | ⏳ 待加工 |
| `linkedin-ads` | 38/60 | ⏳ 待加工 |
| `ad-creative` | 37/60 | ⏳ 待加工 |
| `paid-ads` | 37/60 | ⏳ 待加工 |
| `competitor-ads-analyst` | 36/60 | ⏳ 待加工 |
| `wasted-spend-finder` | 36/60 | ⏳ 待加工 |
| `tiktok-ads` | 33/60 | ⏳ 待加工 |
| `facebook-ads` | 31/60 | ⏳ 待加工 |
| `google-ads` | 31/60 | ⏳ 待加工 |
| `microsoft-ads` | 31/60 | ⏳ 待加工 |

### 📦 其他（78 个）
| Skill | 机器检查 | 状态 |
|-------|---------|------|
| `last30days` | 49/60 | ✅ 通过 |
| `newsletter-creation-curation` | 48/60 | ✅ 通过 |
| `image` | 47/60 | ✅ 通过 |
| `klaviyo-developer` | 47/60 | ✅ 通过 |
| `community-marketing` | 44/60 | ✅ 通过 |
| `plan-my-day` | 44/60 | ✅ 通过 |
| `sync-repos` | 44/60 | ✅ 通过 |
| `utm-attribution-strategy` | 44/60 | ✅ 通过 |
| `de-ai-ify` | 43/60 | ⏳ 待加工 |
| `github-readme` | 43/60 | ⏳ 待加工 |
| `ab-test-setup` | 42/60 | ✅ 通过 |
| `cold-email` | 42/60 | ✅ 通过 |
| `go-mode` | 42/60 | ⏳ 待加工 |
| `klaviyo-analyst` | 42/60 | ✅ 通过 |
| `linkedin-profile-optimizer` | 42/60 | ✅ 通过 |
| `looker-studio` | 42/60 | ✅ 通过 |
| `reddit-insights` | 42/60 | ✅ 通过 |
| `shopify` | 42/60 | ✅ 通过 |
| `social-content` | 42/60 | ✅ 通过 |
| `aso-audit` | 41/60 | ⏳ 待加工 |
| `pro-report-builder` | 41/60 | ⏳ 待加工 |
| `social-card-gen` | 41/60 | ⏳ 待加工 |
| `voice-extractor` | 41/60 | ⏳ 待加工 |
| `video` | 40/60 | ✅ 通过 |
| `ab-testing-framework` | 39/60 | ✅ 通过 |
| `co-marketing` | 39/60 | ⏳ 待加工 |
| `brand-dna` | 38/60 | ⏳ 待加工 |
| `brand-voice-guidelines` | 38/60 | ⏳ 待加工 |
| `cold-email-outreach` | 38/60 | ⏳ 待加工 |
| `cro-auditor` | 38/60 | ⏳ 待加工 |
| `repo-health` | 38/60 | ⏳ 待加工 |
| `social-media-strategy` | 38/60 | ⏳ 待加工 |
| `social-preview` | 38/60 | ⏳ 待加工 |
| `youtube-summarizer` | 38/60 | ⏳ 待加工 |
| `braze` | 37/60 | ✅ 通过 |
| `google-analytics` | 37/60 | ✅ 通过 |
| `referral-program` | 37/60 | ⏳ 待加工 |
| `case-study-builder` | 36/60 | ⏳ 待加工 |
| `cold-outreach-sequence` | 36/60 | ⏳ 待加工 |
| `competitor-alternatives` | 36/60 | ⏳ 待加工 |
| `competitor-profiling` | 36/60 | ⏳ 待加工 |
| `customer-research` | 36/60 | ⏳ 待加工 |
| `daily-briefing-builder` | 36/60 | ⏳ 待加工 |
| `data-viz-deck` | 36/60 | ⏳ 待加工 |
| `dep-audit` | 36/60 | ⏳ 待加工 |
| `email-composer` | 36/60 | ⏳ 待加工 |
| `form-cro` | 36/60 | ⏳ 待加工 |
| `google-tag-manager` | 36/60 | ⏳ 待加工 |
| `homepage-audit` | 36/60 | ⏳ 待加工 |
| `icp-research` | 36/60 | ⏳ 待加工 |
| `linkedin-authority-builder` | 36/60 | ⏳ 待加工 |
| `marketing-principles` | 36/60 | ⏳ 待加工 |
| `positioning-basics` | 36/60 | ⏳ 待加工 |
| `product-marketing-context` | 36/60 | ⏳ 待加工 |
| `research-digest` | 36/60 | ⏳ 待加工 |
| `testimonial-collector` | 36/60 | ⏳ 待加工 |
| `tweet-draft-reviewer` | 36/60 | ⏳ 待加工 |
| `churn-prevention` | 35/60 | ✅ 通过 |
| `sales-enablement` | 35/60 | ✅ 通过 |
| `pro-deck-builder` | 33/60 | ⏳ 待加工 |
| `release-notes` | 33/60 | ⏳ 待加工 |
| `repo-scaffold` | 33/60 | ⏳ 待加工 |
| `revops` | 32/60 | ⏳ 待加工 |
| `analytics-tracking` | 31/60 | ⏳ 待加工 |
| `email-sequence` | 31/60 | ⏳ 待加工 |
| `frontend-design` | 31/60 | ⏳ 待加工 |
| `html-report-builder` | 31/60 | ⏳ 待加工 |
| `lead-magnets` | 31/60 | ⏳ 待加工 |
| `marketing-psychology` | 31/60 | ✅ 已加工 |
| `page-cro` | 31/60 | ⏳ 待加工 |
| `popup-cro` | 31/60 | ⏳ 待加工 |
| `signup-flow-cro` | 31/60 | ⏳ 待加工 |
| `launch-strategy` | 29/60 | ⏳ 待加工 |
| `customer-journey-mapping` | 28/60 | ⏳ 待加工 |
| `safe-push` | 23/60 | ⏳ 待加工 |
| `pricing-strategy` | 44/60 | ✅ 通过 |
| `market-research` | 42/60 | ✅ 通过 |
| `landing-page-optimizer` | 43/60 | ✅ 通过 |


---

## 🏭 制造业 AI 提效分析

本仓库还包含独立的制造业专项 Skill：

| Skill | 用途 |
|-------|------|
| `manufacturing-ai-efficiency-pro` | 制造业 AI 提效分析 V2.0 — 流程拆解、AI 机会扫描、人机协同 T34 模型 |

详见 [manufacturing-ai-efficiency-pro/](./manufacturing-ai-efficiency-pro/)

---

## 🔄 持续更新

本仓库由 **SKILL 自动策展流水线** 每日维护：

| 时间 | 任务 | 内容 |
|------|------|------|
| 14:30 | Part 1：新品入库 | 发现 2-4 个新 skill → 机器检查 → 格式标准化 + 中国市场适配 → 推送 |
| 15:00 | Part 2：存量加工 | 选取 2-3 个已有 skill → 机器检查 → 格式标准化 + 中国市场适配 → 推送 |

每个加工后的 Skill 包含：
- `SKILL.md` — 标准化技能定义（Hermes + Claude Code 双兼容）
- `README.md` — 中文详细说明文档

---

## 🤝 贡献

欢迎通过 Issue 或 PR 贡献。贡献前请确保：
- SKILL.md 符合标准格式
- 通过机器检查（≥35/60）
- 附有中文 README.md

---

## 📄 许可证

MIT License © 2026 MeerkatAIChina
