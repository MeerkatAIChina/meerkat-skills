# AEO/GEO Optimizer — 让 AI 搜索引擎"点名推荐"你

> **你的网站在 Google 排第一，但 ChatGPT 回答用户问题的时候提都不提你。这不是偶然——传统的 SEO 信号，AI 搜索引擎根本不买账。**

---

## 一、搜索正在经历 20 年来最大的范式转移

十年前，搜索 = 在搜索框输入关键词 → 得到 10 条蓝色链接。现在呢？用户问 ChatGPT、Perplexity、豆包、百度 AI——AI 直接给答案，附带引用来源。

**如果你的内容没有被 AI 引用，你就是这个新兴搜索渠道里的透明人。** AEO（Answer Engine Optimization）+ GEO（Generative Engine Optimization）就是专门解决这个问题：让你的内容成为 AI 回答中被引用、被信任、被推荐的来源。

---

## 二、先搞清楚：这个 Skill 不是什么

| ❌ 不是 | ✅ 正确选择 |
|---------|------------|
| 传统 SEO 替代品 | AEO/GEO 是传统 SEO 的叠加层，不是替代 |
| 只在 ChatGPT 里有效 | 覆盖 ChatGPT、Perplexity、Claude、Google AI Overviews、Bing Copilot 等 |
| 保证 AI 引用 | 优化内容结构让 AI 更容易提取，引用是结果不是承诺 |
| 不需要技术基础 | 需要 robots.txt 放行 AI 爬虫 + Schema 标记 |
| 一次性工作 | AI 搜索平台持续演进，需要持续监控和迭代 |

---

## 三、真实场景演示

**场景**：一个项目管理 SaaS，用户在 Google 能搜到他们，但在 ChatGPT 被问"最好的项目管理工具有哪些"时从未出现。

**`aeo-geo-optimizer` 会怎么做？**

```
Step 1: 当下可见度测试
→ 向 ChatGPT/Perplexity/Claude 发出查询
→ 结果：品牌未被引用，竞品 A 出现 3 次，竞品 B 出现 2 次
→ 文档化：哪类查询缺位？竞品为什么被引用？

Step 2: 内容评分（AEO 记分卡）
→ 直接回答：文章开头有总结，但未用 Q&A 结构（2/5）
→ 数据密度：有观点但少具体数字和引用来源（2/5）
→ Schema：缺少 Article 和 FAQ Schema（1/5）
→ 新鲜度：无发布日期（1/5）
→ 综合：16/40 → 需要优化

Step 3: 结构优化
→ 文章按"直接回答模式"重构：
   H2: 2026年最好的项目管理工具有哪些？
   开篇一句话答案 → 对比表 → 每种工具一句话+独特数据
→ 每个 H2 下第一句话给出直接答案
→ 统计数据加来源引用（"根据 G2 2026 年报告"）
→ 添加 FAQ Schema 覆盖 5 个最常见查询
→ robots.txt 确保 GPTBot/PerplexityBot/ClaudeBot 放行

Step 4: 监控方案
→ 月度手动查询关键 query
→ 服务器日志追踪 AI 爬虫访问频率
→ GA4 引荐流量标记 AI 平台来源
```

---

## 四、核心能力矩阵

| 能力 | 具体内容 |
|------|---------|
| **AI 可见度测试** | 对核心查询在 ChatGPT/Perplexity/Claude/Google AI Overview 上测试引用情况 |
| **AEO 记分卡** | 8 维度评分：直接回答 / 数据密度 / 来源归因 / 结构 / Schema / 新鲜度 / 作者权威 / 可引用性 |
| **内容重构模式** | 直接回答 / 定义 / 对比 / 统计数据 四种 AI 友好的内容模板 |
| **写作指南** | 先给答案、用具体数字、点名来源、自包含段落、对比表优先 |
| **AI 爬虫管理** | 6 大 AI 爬虫 UA 识别 + robots.txt 建议 + 放行决策框架 |
| **监控体系** | 手动检查 / 日志分析 / 品牌提及监控 / 引荐流量追踪 |

---

## 五、谁应该用

- ✅ **品牌希望在 AI 搜索中被推荐**（"最好的 XX 工具"类查询）
- ✅ **内容团队**：调整写作结构让 AI 更容易提取信息
- ✅ **SaaS 市场负责人**：构建被 AI 引用的产品对比和评估内容
- ✅ **SEO 负责人**：在传统 SEO 基础上叠加 AI 搜索优化

---

## 六、简单上手步骤

```bash
cp -r skills/aeo-geo-optimizer ~/.claude/skills/
```

触发方式：
> "帮我优化网站内容，让它在 ChatGPT 的回答中被引用"
> "我想知道我的品牌在 AI 搜索中的可见度怎么样"

Agent 会先用核心查询做 AI 可见度测试 → 输出记分卡 + 差距分析 → 给出逐页优化方案。

---

## 七、配合使用

| 配合 Skill | 为什么 |
|-----------|--------|
| `schema-markup-generator` | AEO 审计推荐 Schema 类型 → 直接生成 JSON-LD |
| `seo-content-writer` | 用 AEO 写作模式创建 AI 友好的新内容 |
| `technical-seo-audit` | 确保技术基础（robots.txt/速度/索引）不妨碍 AI 爬虫 |
| `seo-audit` | 传统 SEO 和 AI SEO 双线作战 |
| `llms-txt` | 为项目级 AI 可发现性提供机器可读的站点地图 |

---

> **AI 搜索不是"未来"——它已经来了。你的竞品已经在优化，你还要等多久？**

> 猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI
