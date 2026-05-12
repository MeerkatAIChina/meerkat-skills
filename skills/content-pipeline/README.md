# Content Pipeline Skill — Agent 编排式内容生产流水线

> 自动化内容全流程：串联研究分析员、主编审校、社交放大器三个子 Agent，从选题到发布素材一气呵成。

---

## 📌 定位

**Content Pipeline** 是内容生产流水线的自动化编排层。它实际启动子 Agent 并管理流程推进——不同于 `content-workflow` 的手动指导，Pipeline 让 Agent 自动完成\"研究 → 审校 → 分发\"的全链路。

> 💡 与 `content-workflow` 的区别：`content-workflow` 给你框架和检查清单，你来执行；`content-pipeline` 直接启动子 Agent 自动跑流程。

---

## 🎯 核心能力

### 1. 三 Agent 自动编排
按顺序启动三个子 Agent：
- **research-analyst** — 生成话题研究简报，输出 `research-briefs/YYYY-MM-DD-topic-slug.md`
- **editor-in-chief** — 审核草稿的声音一致性、结构质量、SEO、论证质量，输出审校报告
- **social-amplifier** — 生成多平台分发素材包：LinkedIn（2 变体）、Twitter/X 线程、邮件标题、可引用金句、标签

### 2. 灵活进入点
- **全流程**：`/content-pipeline "话题"` — 从零开始
- **跳过研究**：`/content-pipeline review ./draft.md` — 直接进入编辑审校
- **仅分发**：`/content-pipeline distribute ./article.md` — 只生成社交素材包

### 3. 流水线状态管理
通过文件存在性自动追踪进度——研究简报存在 = Stage 1 完成，审校报告存在 = Stage 2 完成，社交素材包存在 = Stage 3 完成。可以随时从中断点恢复。

### 4. 可配置的子 Agent
每个阶段的子 Agent 可替换为你自己的专业 Agent——研究用任意研究分析 Agent，编辑用任意审校 Agent。

---

## 📋 适用场景

### ✅ 应该使用
- 需要端到端自动化内容生产（从想法到全渠道素材）
- 团队已有固定内容制作流程，想用 Agent 提效
- 想批量处理多篇内容的\"研究→审校→分发\"
- 需要可恢复的流水线（避免中断后重来）
- 希望子 Agent 可替换，灵活适配不同工具链

### ❌ 不应该使用
- 想手动控制每个阶段 → 使用 `content-workflow`
- 只需要具体某一步（如仅写文案） → 使用 `copywriting`
- 内容策略规划 → 使用 `content-strategy`

---

## 🔄 工作流程

```
/content-pipeline "话题"
        │
        ▼
┌──────────────────┐
│ Stage 1: 研究     │ ← research-analyst Agent
│ 输出: 研究简报    │
└────────┬─────────┘
         │ 用户审阅 → 决定是否继续
         ▼
┌──────────────────┐
│ Stage 2: 编辑审校 │ ← editor-in-chief Agent
│ 输出: 审校报告    │   声音/结构/SEO/论证/标题变体
└────────┬─────────┘
         │ 用户决定 → 发布/修改/迭代
         ▼
┌──────────────────┐
│ Stage 3: 社交分发 │ ← social-amplifier Agent
│ 输出: 分发素材包  │   LinkedIn/Twitter/邮件/金句
└──────────────────┘
```

---

## 🚀 使用方法

### 安装

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git
cp -r claude-marketing/skills/content-pipeline ~/.claude/skills/
```

### 快速命令

```bash
# 全流程（从选题开始）
/content-pipeline "为什么 MCP 是新一代 API"

# 从现有草稿进入审校
/content-pipeline review ./drafts/article-draft.md

# 仅生成分发素材
/content-pipeline distribute ./content/published-article.md

# 查看当前进度
/content-pipeline status
```

### 建议发布节奏
- **研究**：周一/周二
- **起草**：周二/周三
- **审校**：周三/周四
- **发布**：周四/周五

---

## 🔗 与其他 Skill 的配合

| 场景 | 配合 Skill | 说明 |
|------|-----------|------|
| SEO 深度优化 | Stage 2 + `seo-content-writer` | 审校阶段叠加 SEO 写作优化 |
| 品牌声音校验 | Stage 2 + `content-creator` | 在编辑审校前用脚本分析声音一致性 |
| RSS 驱动研究 | Stage 1 + `research-digest` | 替代内置研究，用 RSS 源驱动选题 |
| 内容策略顶层规划 | `content-strategy` → `content-pipeline` | 策略定方向，Pipeline 跑执行 |

---

## ⚠️ 注意事项与局限性

### 局限性
- **依赖子 Agent 能力** — 研究、审校、分发质量取决于配置的子 Agent
- **没有审批层级** — 目前只有用户单点确认，不支持多人协作审批
- **无法直接发布** — 产出的是文件和素材包，不直接对接 CMS 或社交平台 API
- **流水线文件管理** — 多篇内容并行时需手动管理文件路径，避免覆盖

### 最佳实践
- 每篇内容独立目录，避免文件冲突
- 审校阶段不跳过——这是质量的关键闸门
- 分发素材包发布前再做一次人工审核
- 保留所有中间文件，方便回溯和迭代

---

## 📄 许可证

MIT License © Rebecca Rae Barton
