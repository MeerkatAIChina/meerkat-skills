# AI SEO Skill — AI 搜索可见度优化专家

> 让品牌在 AI 搜索引擎（ChatGPT、Perplexity、Google AI Overviews、百度 AI、豆包等）中被引用和推荐。

---

## 📌 一句话定位

**AI SEO** 是面向 AI Agent 的专业技能，帮助品牌优化内容以被 AI 搜索引擎引用。不只是传统 SEO 的延伸——目标是让你的内容被 AI"点名推荐"，而不只是排在搜索结果第一页。

---

## 🎯 核心能力

### 1. AI 可见度审计
系统化检查你的品牌在 ChatGPT、Perplexity、Google AI Overviews 等平台的引用情况。对比竞品，定位差距，输出优先级矩阵。

### 2. 三大支柱优化框架
- **结构 (Structure)**：让内容可被 AI 提取（定义块、对比表、FAQ、统计数据块）
- **权威 (Authority)**：让内容值得被引用（引用来源 +40%、统计数据 +37%、专家引言 +30%）
- **存在 (Presence)**：出现在 AI 搜索的地方（Wikipedia、Reddit、知乎、百度百科等第三方平台）

### 3. 中国 AI 搜索生态适配
覆盖 7 大中国 AI 平台（百度 AI、豆包、文心一言、Kimi、通义千问、360 AI、秘塔），包含 ICP 备案、百度百科、知乎/小红书内容策略等中国特有要求。

### 4. AI Agent 可发现性
创建 `/pricing.md`、`llms.txt` 等机器可读文件，让 AI Agent 在代替用户评估产品时能找到并使用你的信息。

### 5. 监控与 ROI 追踪
提供从免费手动检查到专业工具的全套监控方案，追踪 AI 引用率、引荐流量、转化归因。

---

## 📋 适用场景

### ✅ 应该使用
- 品牌希望在 ChatGPT/Perplexity 回答中被引用
- SaaS 产品想出现在 AI 搜索的"最佳 XX 工具"推荐中
- 内容团队需要优化文章让 AI 提取和引用
- 中国市场品牌需要优化百度 AI/豆包/文心一言的可见度
- 想了解为什么竞品被 AI 引用而你没有被引用

### ❌ 不应该使用
- **传统 SEO 优化（排名/关键词/外链）** → 使用 `seo-audit`
- **结构化数据实现** → 使用 `schema-markup`
- **纯内容策略规划** → 使用 `content-strategy`
- **竞品对比页面创建** → 使用 `competitor-alternatives`

---

## 🔄 工作流程

```
Phase 1: 了解 AI 搜索原理
    │  (6 大 AI 平台如何选择引用来源)
    ▼
Phase 2: AI 可见度审计 ──→ ⏸1 确认审计结果
    │  (检查 10-20 个核心查询，分析引用差距)
    ▼
Phase 3: 优化实施 ──→ ⏸2 确认优化策略
    │  (结构优化 + 权威建设 + 第三方存在)
    │  ──→ ⏸3 确认实施结果
    ▼
Phase 4: 持续监控
    │  (AI 引用率、引荐流量、竞品变化)
    │  ──→ ⏸4 月度复盘
```

---

## 🚀 使用方法

### 安装
```bash
# Claude Code
cp -r skills/ai-seo ~/.claude/skills/

# Hermes Agent
cp -r skills/ai-seo ~/.hermes/skills/
```

### 触发方式
Agent 在以下情况自动激活：
- 用户提到 "AI SEO"、"AEO"、"GEO"
- "如何让 ChatGPT 引用我的网站"
- "优化 AI 搜索可见度"
- "出现在 AI Overviews 中"

### 快速上手（80/20 路径）
1. 审计 — 检查核心查询的 AI 引用情况（1-2 小时）
2. 修复 robots.txt — 允许 AI 爬虫（10 分钟）
3. 添加 Schema 标记 — FAQ/Article/HowTo（1-2 天，+30-40% 可见度）
4. 添加统计数据 + 引用来源（每页 1-3 小时，+40% 引用提升）
5. 创建 `/pricing.md`（30 分钟）
6. 月度监控（1 小时/月）

---

## 📊 输出示例

**输入**："帮我做一下 AI SEO 审计，我的产品是项目管理 SaaS，目标查询是 'best project management software'"

**输出（节选）**：
```
AI 可见度审计报告
═══════════════════════════════════
测试查询：20 个核心查询

AI Overviews 出现率：85%（17/20 查询）
你的品牌被引用：2/17 次（11.7%）
竞品 A 被引用：12/17 次（70.6%）

🔴 紧急（P0）：
  - GPTBot 在 robots.txt 中被屏蔽！→ 解除屏蔽
  - 缺少 FAQ Schema → 添加后预估 +30-40% 可见度

🟠 高优（P1）：
  - 5 个页面缺少统计数据 → 添加具体数据+来源
  - 无对比页面 → 创建 "vs 竞品" 对比页

📊 预期：6 个月内引用率从 11.7% 提升到 50%+
```

---

## 🔗 与其他 Skill 的配合

| 配合 Skill | 使用场景 |
|-----------|---------|
| `seo-audit` | 先做传统 SEO 基础优化，再做 AI SEO |
| `schema-markup` | 实施结构化数据标记 |
| `content-strategy` | 规划 AI 优化的内容选题 |
| `competitor-alternatives` | 创建对比页面获取 AI 引用 |
| `copywriting` | 撰写既好读又易被 AI 提取的内容 |

---

## ⚠️ 注意事项与局限性

- **不是即时见效**：AI SEO 是中长期策略，首次引用通常需要 3-4 个月
- **依赖内容质量**：如果基础内容差，AI SEO 优化效果有限
- **平台变化快**：AI 搜索平台算法频繁更新，需持续监控
- **中国市场有特殊规则**：ICP 备案、百度百科、内容合规都是前提条件
- **不能替代传统 SEO**：两者互补，不是替代关系

---

## 📄 许可证

MIT License © 2026 MeerkatAIChina

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
