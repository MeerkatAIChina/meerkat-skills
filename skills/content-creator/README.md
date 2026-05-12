# Content Creator Skill — AI 内容营销工具箱

> 集成品牌声音分析、SEO 优化、内容框架、社媒策略和内容日历规划的一站式内容营销工具箱——附带可执行 Python 脚本，从分析到产出全线贯通。

---

## 📌 定位

**Content Creator** 是一个综合性的内容营销技能。它不止帮你写内容，还帮你建立品牌声音体系、优化 SEO、规划内容日历、适配多平台分发——一套工具覆盖内容营销全链路。

> 💡 与 `seo-content-writer` 的区别：`seo-content-writer` 专注于深度 SEO 写作优化（关键词研究、元标签、标题层级），而本 Skill 是更广泛的内容营销工具箱——品牌声音开发、内容日历、多平台策略。

---

## 🎯 核心能力

### 1. 品牌声音分析
使用 `brand_voice_analyzer.py` 脚本分析现有内容的语音特征、可读性和一致性。输出语音画像（正式度、语调、视角）、可读性评分、句式结构分析，以及优化建议。

### 2. SEO 优化博文创作
从关键词研究到内容结构到优化检查的完整流程：
- 关键词研究（主词 + 3-5 次词 + 10-15 LSI 词）
- 博文模板驱动的内容结构生成
- `seo_optimizer.py` 自动化 SEO 评分和优化建议（关键词密度、标题层级、内外链、元描述）

### 3. 社交媒体内容适配
基于核心信息，通过内容再利用矩阵快速适配不同平台：
- 博文 → LinkedIn 帖子 + Twitter 线程 + 邮件通讯
- 适配平台规格：长度、发布时间、图片尺寸

### 4. 内容日历规划
按月设定目标和 KPI，按周分配内容主题，遵循 40/25/25/10 内容支柱配比，批量创建同一周所有内容。

---

## 📋 适用场景

### ✅ 应该使用
- 需要系统化建立品牌声音和内容体系
- 撰写并优化 SEO 博文（1,500-2,500 字深度内容）
- 将一篇核心内容适配到多个社交平台
- 制定月度/季度内容日历
- 用脚本自动化品牌声音一致性检查

### ❌ 不应该使用
- 纯文案写作（无 SEO 需求） → 使用 `copywriting`
- 深度技术 SEO 审计 → 使用 `seo-audit`
- 内容策略层面规划 → 使用 `content-strategy`

---

## 🔄 核心工作流

### 品牌声音开发
```
分析现有内容 → 确定声音属性 → 创建声音样本 → 一致性测试 → 输出品牌指南
```

### SEO 博文创作
```
关键词研究 → 内容结构（博文模板） → 草稿撰写 → SEO 优化检查 → 应用建议 → 发布
```

### 社交媒体适配
```
核心信息 → 平台选择 → 内容再利用矩阵适配 → 平台规格优化 → 发布排期
```

---

## 🚀 使用方法

### 安装

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git
cp -r claude-marketing/skills/content-creator ~/.claude/skills/
```

### 关键脚本

**品牌声音分析器**
```bash
python scripts/brand_voice_analyzer.py existing_content.txt
```
输出：语音画像（正式度/语调/视角）、可读性评分、句式结构分析、优化建议。

**SEO 优化器**
```bash
python scripts/seo_optimizer.py blog_post.md "主关键词" "次要,关键词,列表"
```
输出：SEO 评分（0-100）、关键词密度分析、结构评估、元标签建议、具体优化建议。

---

## 🔗 与其他 Skill 的配合

| 场景 | 配合 Skill | 说明 |
|------|-----------|------|
| 品牌声音 + 文案产出 | `content-creator` → `copywriting` | 先生成品牌声音指南，再对齐写文案 |
| SEO 深化优化 | `content-creator` → `seo-content-writer` | 深度 SEO 写作优化 |
| 内容策略顶层规划 | `content-strategy` → `content-creator` | 策略定方向，Creator 落地执行 |
| 社媒策略 | `social-media-strategy` | 多平台分发策略 |

---

## ⚠️ 注意事项与局限性

### 局限性
- **需要 Python 环境运行脚本** — 品牌声音分析和 SEO 优化需要本地 Python
- **SEO 数据依赖用户输入** — 关键词研究不能替代专业工具（Ahrefs/SEMrush）
- **品牌声音需要迭代** — 首次分析结果可能与品牌预期有偏差，需要 1-2 轮校准
- **日历规划不含平台自动发布** — 需手动或配合第三方工具执行排期

### 质量指标参考
- SEO 评分建议 75/100 以上
- 可读性匹配目标受众水平
- 全篇品牌声音一致性
- 每篇内容有清晰价值主张和可执行要点

---

## 📄 许可证

MIT License © Rebecca Rae Barton

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
