# Content Workflow Skill — 端到端内容生产流水线

> 从调研到编辑审校到社交分发——一套完整的三阶段内容创作工作流。覆盖博文、LinkedIn、Twitter 线程、邮件通讯和深度长文。

---

## 📌 定位

**Content Workflow** 是一套手动执行的内容生产流水线指南。它将内容创作拆解为三个清晰阶段：研究 → 起草与编辑 → 分发，每个阶段输出明确的交付物。你可以从任意阶段进入，也可以跑完整流程。

> 💡 与 `content-pipeline` 的区别：`content-workflow` 是手动工作流指南（框架+检查清单），`content-pipeline` 是自动化编排层（实际启动子 Agent 并按流程推进）。

---

## 🎯 核心能力

### 1. 三阶段结构化流水线
- **Stage 1 — 研究**：话题调研 + 来源评估 + 数据提取 + 对立观点 + 独特角度开发 → 输出研究简报
- **Stage 2 — 起草与编辑**：按内容类型框架撰写 + 编辑审校（声音一致性/结构质量/SEO/事实准确性/可读性） + 修订 → 输出精炼草稿
- **Stage 3 — 分发**：适配多平台——LinkedIn 帖子 + Twitter/X 线程 + 邮件标题 + 可引用金句 → 输出分发素材包

### 2. 灵活进入模式
- `--full`：完整三阶段流水线
- `--from-draft`：跳过研究，直接进入编辑审校
- `--distribute`：仅对已定稿内容生成分发素材包

### 3. 明确的状态跟踪
```
stub → draft → reviewed → approved → published → measured
                                ↘ rejected (终止)
```
每篇内容的状态一目了然，避免发布未经审批的内容。

### 4. 多内容类型支持
覆盖博文、LinkedIn 帖子、Twitter 线程、邮件通讯、深度长文，每种类型有对应研究深度、草稿长度和分发策略。

---

## 📋 适用场景

### ✅ 应该使用
- 需要规范化的内容生产流程（个体创作者或小型团队）
- 一篇内容要适配多个分发渠道
- 有草稿需要专业的编辑审校
- 需要建立\"研究-写作-分发\"的 SOP
- 在发布前需要明确的人工审批关卡

### ❌ 不应该使用
- 需要自动化编排（Agent 自动推进） → 使用 `content-pipeline`
- 内容策略规划 → 使用 `content-strategy`
- SEO 深度优化 → 使用 `seo-content-writer`

---

## 🔄 工作流程

```
                    ┌── ── → --from-draft ── ──┐
                    │                            │
Stage 1: 研究  →  Stage 2: 起草与编辑  →  Stage 3: 分发
  │                   │                          │
  ▼                   ▼                          ▼
研究简报            精炼草稿                  分发素材包
(来源+数据点       (声音一致性检查           (LinkedIn+Twitter
 +推荐角度)         +结构质量+SEO)            +邮件标题+金句)
                    │
            ┌───────┴───────┐
            ▼               ▼
        approved         rejected
            │
            ▼
        published → measured
```

---

## 🚀 使用方法

### 安装

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git
cp -r claude-marketing/skills/content-workflow ~/.claude/skills/
```

### 使用模式

```bash
# 完整流水线
/content-workflow "为什么 MCP 是新一代 API"

# 从现有草稿开始
/content-workflow --from-draft ./drafts/article-draft.md

# 仅生成分发素材
/content-workflow --distribute ./content/final-article.md
```

---

## 🔗 与其他 Skill 的配合

| 场景 | 配合 Skill | 说明 |
|------|-----------|------|
| 流水线编排自动化 | `content-workflow` → `content-pipeline` | 从手动流程升级为 Agent 自动编排 |
| 研究阶段强化 | `research-digest` | 用 RSS 源充实研究素材 |
| SEO 深度优化 | `seo-content-writer` | 在 Stage 2 中调用，强化 SEO |
| 品牌声音校验 | `content-creator` | 在编辑审校阶段用脚本分析声音一致性 |

---

## ⚠️ 注意事项与局限性

### 局限性
- **手动执行** — 不自动启动子 Agent，需人工推进各阶段
- **不适合超大规模内容团队** — 缺乏审批层级、权限管理和协作功能
- **分发不含排期发布** — 产出的是分发素材，实际发布需配合其他工具
- **研究阶段依赖网络搜索** — 无法访问内部数据库或付费研究平台

### 核心原则
1. 先研究再写——再短的内容也值得花 10 分钟查资料
2. 一稿多用——写好一篇，适配各平台格式
3. 不跳过人工审批——永远不要在未经确认的情况下发布
4. 量一切——追踪数据，用表现指导后续内容决策

---

## 📄 许可证

MIT License © Rebecca Rae Barton
