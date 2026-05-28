# 👁️ Watchers — 自动化竞品情报监控，不错过任何风吹草动

> RSS、JSON API、GitHub 动态——设好定时任务，只在有新内容时才通知你。

## 😩 痛点

营销人员需要持续跟踪竞品动态、行业趋势、定价变化、新品发布……但手动监控既枯燥又容易遗漏。等你发现竞品降价了，市场窗口可能已经关闭。人工刷 RSS 和 GitHub？效率太低，关键信息容易被淹没。

## ✅ 能做什么 vs ❌ 不做什么

| ✅ 能做 | ❌ 不做 |
|---|---|
| RSS / Atom 订阅源自动监控 | 社交媒体舆情监听 |
| JSON API 端点轮询 + 新条目检测 | 情感分析 / NLP 文本挖掘 |
| GitHub 仓库 Issue / PR / Release / Commit 跟踪 | 替代 Brandwatch / Meltwater 等商业工具 |
| 水印去重（首次运行建立基线，只推增量） | 全量历史数据回放 |
| Cron 定时集成，静默无变化 / 有变化才通知 | 实时 WebSocket 推送 |
| 可扩展模板，自定义 watcher 只需几行代码 | — |

## 🧠 核心能力

- **3 个开箱即用脚本**：`watch_rss.py`（RSS 订阅）、`watch_http_json.py`（JSON API）、`watch_github.py`（GitHub 追踪）
- **水印去重机制**：首次运行自动建立基线，后续只报告新增条目，不重复推送
- **有界 ID 集合**：最多保留 500 条记录，防止状态文件无限膨胀
- **Cron 原生集成**：配合 Hermes Agent 的 cron 任务，无人值守持续监控
- **输出格式统一**：每条新条目输出标题 + URL + 可选摘要，空输出 = 静默

## 🎯 谁适合用

- **营销分析师**：监控竞品博客、产品更新、定价变动
- **竞品情报团队**：系统化跟踪目标企业的 GitHub 和 API 动态
- **产品营销**：第一时间获知竞品新功能发布和 Changelog
- **增长黑客**：监控行业 RSS 源，捕捉趋势信号和合作机会

## 🔗 搭配使用

| 搭配技能 | 用途 |
|---|---|
| `last30days` | 回顾过去 30 天的关键事件和趋势 |
| `research-digest` | 将监控到的信息整理成研究报告 |
| `competitor-profiling` | 基于监控数据构建竞品画像 |
| `competitor-ads-analyst` | 分析竞品广告投放策略 |

## 🚀 快速开始

```bash
# 监控 Hacker News RSS
python scripts/watch_rss.py --name hn --url https://news.ycombinator.com/rss --max 5

# 跟踪 GitHub 仓库动态
python scripts/watch_github.py --name hermes --repo NousResearch/hermes-agent --scope issues

# 轮询任意 JSON API
python scripts/watch_http_json.py --name api --url https://api.example.com/events --id-field event_id --items-path data.events
```

设好 cron，剩下的交给它。**竞品动了，你第一个知道。**

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
