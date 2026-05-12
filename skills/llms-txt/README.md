# 🧠 llms.txt — 让你的项目被 AI 读懂

> 你的开源项目、技术文档、产品官网，正在被 ChatGPT、Claude、Perplexity 回答问题时"引用"——但 AI 真的理解你的项目吗？给 AI 写一份"阅读理解指南"，让大模型准确描述你、推荐你、引用你。

---

## 为什么你需要 llms.txt？

当有人在 ChatGPT 里问"推荐一个好用的 Python 异步框架"时，AI 给出的答案来自它对海量文档的理解。但问题是——你的文档可能写得很好，却散落在几十个页面里，AI 抓取时只能看到碎片，没人帮它梳理"重点在哪"。

**llms.txt 就是这份"重点清单"**。

它是由 Jeremy Howard（Answer.AI 创始人）提出的开放规范——在项目根目录放置一个纯文本 Markdown 文件，用结构化的方式告诉大语言模型：

- 这个项目是做什么的
- 给谁用、解决什么问题
- 最重要的文档入口在哪里
- 按什么逻辑组织内容

**效果**：AI 引用你的项目时更准确、推荐时更有依据、描述时更贴近你的定位。

---

## 它能做什么？

### 📄 `/llms-txt generate` — 自动生成

扫描你的代码仓库（或文档站点），自动识别所有文档资产：

- README.md、GETTING_STARTED.md
- `docs/` 目录下的指南、教程、API 参考
- OpenAPI 规范、CHANGELOG、CONTRIBUTING 指南
- 架构决策文档、部署配置、示例代码目录

然后按**优先级三级体系**自动排列：

| 优先级 | 内容类型 | 为什么重要 |
|--------|---------|-----------|
| **P0** | README、入门指南、API 参考 | AI 理解项目的"第一印象" |
| **P1** | 教程、架构文档、工作流指南 | 深入理解——怎么用、为什么这样设计 |
| **P2** | CHANGELOG、贡献指南、FAQ | 辅助信息——历史、社区、排错 |

### 🔍 `/llms-txt audit` — 审计现有文件

检查已有 llms.txt 的完整性：是否有断链？描述是否过时？是否遗漏了新增的高价值文档？输出具体的修复建议。

### 🔄 `/llms-txt update` — 增量更新

保留你手动编辑的描述，只刷新文件路径和新增/删除的页面引用——不会覆盖你的精心措辞。

### 📚 可选：生成 `llms-full.txt`

对于小型项目，可以生成一个"全文版"，将关键文档的完整内容内联到一个文件中，让 AI 在一个上下文窗口内读完所有核心信息。

---

## 核心设计原则

1. **精选，而非倾倒** — 列出 10-30 个最重要的页面，而不是把所有 500 个文件都塞进去
2. **入口优先** — 前几条必须回答：这是什么？给谁用？怎么开始？
3. **面向行动的摘要** — "如何为 SSO 提供商配置身份验证"优于"身份验证配置页面"
4. **按学习路径组织** — 用新人学习项目的逻辑分段，而不是按仓库目录结构
5. **保持新鲜** — 断链的 llms.txt 比没有更糟糕；文档大改后跑一次 audit

---

## 典型输出示例

```markdown
# MyProject

> 一个高性能的 Python 异步 Web 框架，专为实时应用设计。
> 适合构建 WebSocket 服务、实时数据管道和 API 网关。

## 入门
- [快速开始](https://docs.example.com/quickstart): 5 分钟搭建第一个服务
- [安装指南](https://docs.example.com/install): 各平台安装说明
- [核心概念](https://docs.example.com/concepts): 理解异步模型和中间件

## API 参考
- [路由系统](https://docs.example.com/api/routing): 路由注册、参数匹配、中间件注入
- [WebSocket API](https://docs.example.com/api/websocket): 连接管理、广播、房间

## 指南
- [生产部署](https://docs.example.com/guides/deploy): Docker、K8s、负载均衡配置
- [性能调优](https://docs.example.com/guides/perf): 基准测试和优化建议
```

---

## 与 robots.txt 的区别

| | robots.txt | llms.txt |
|---|---|---|
| **面向谁** | 搜索引擎爬虫 | AI 大语言模型 |
| **说什么** | 哪些页面可以抓、哪些不可以 | 哪些内容最重要、怎么组织 |
| **格式** | 纯文本指令 | Markdown 结构化列表 |
| **影响** | 索引范围 | AI 理解和引用准确度 |

**两者互补**：robots.txt 管理抓取许可（包括 AI 爬虫如 GPTBot、ClaudeBot），llms.txt 管理理解质量。

---

## 快速上手

在对话中直接说：
- "给我的项目生成一个 llms.txt"
- "审计一下我的 llms.txt 有没有问题"
- "文档大改完了，更新 llms.txt"

AI 会自动扫描你的仓库结构，按优先级提取内容，生成符合规范的 Markdown 文件。

---

## 技能联动

- **aeo-geo-optimizer** → llms.txt 是 AI 搜索可见度策略的一部分，两者叠加效果翻倍
- **technical-seo-audit** → 先生成 llms.txt 前确保 AI 爬虫能正常访问你的文档
- **ai-discoverability-audit** → 审计你的品牌在 AI 搜索中的表现，llms.txt 是提升分数的重要举措

---

*猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用*
