# Daily Briefing Builder — 用 Claude Code 生成你的晨间简报

> **不依赖 SaaS、不接 API、不开浏览器——在你的终端里跑一条命令，今天的待办、待发内容和天气就全出来了。**

---

## 为什么需要"晨间简报生成器"？

作为内容营销人，你的一天从"今天我该干什么"的迷茫中开始。翻开 Obsidian，找到今日待办，检查有哪些内容还没发，再去查天气——这三个动作每天重复，每次花 5-10 分钟。

Daily Briefing Builder 把这三步浓缩成一个 **Claude Code 命令**，30 秒内输出一份干净的晨间简报：

```
☀️ Morning Brief — Friday, February 28

TODAY'S 3 ACTIONS
1. 完成 Q1 内容日历
2. 给 BAMBF 客户开发票
3. 发布关于 AI 运维的 LinkedIn 帖子

READY TO POST (5 of 9)
[linkedin] 没人讨论你的 AI 系统失效时会怎样...
[twitter] 异步 AI 运维是真实的...
[newsletter] 真正有效的 AI 营销系统...
...and 4 more in the pipeline

WEATHER
Ann Arbor: ☀️ +42°F
```

---

## 它是怎么工作的？

这套技能在 Claude Code 会话中运行，分四个阶段：

### Phase 1：信息采集

Claude Code 会先确认两件事：

- **你的 Obsidian Vault 路径**（例如 `/root/obsidian-vault`）
- **你的城市名称**（用于天气查询，wttr.in 格式，如 `Ann+Arbor`）

两个值都确认后才会进入下一步——**不会瞎猜**。

### Phase 2：数据提取

然后执行三条 Shell 命令：

1. **读取今日待办** — 从 `vault/bambf/tracking/daily-actions/YYYY-MM-DD.md` 提取 `## Today's 3 Actions` 标题下的三个优先级事项
2. **扫描未发布内容** — 遍历 `vault/content/ready-to-post/` 目录下所有包含 `**Posted:** ❌` 标记的 Markdown 文件，按修改时间倒序排列，自动识别平台（linkedin / twitter / newsletter 等）
3. **获取天气** — 通过 `curl wttr.in/CITY?format=3` 拉取当前天气（纯文本单行格式）

### Phase 3：格式化输出

按固定模板排版成易读的终稿输出。最多展示 5 条待发内容（按最新修改时间优先），超过则显示"还有 X 条在管线中"。

### Phase 4：自检（Self-Critique）

在输出给用户之前，自动执行四项内部检查：

- ✅ **待办准确性**：文件是否找到？待办事项是否被正确解析？
- ✅ **内容完整性**：待发内容数量是否与扫描结果一致？
- ✅ **天气有效性**：curl 是否返回了有效结果？
- ✅ **格式规范性**：没有散落的 Shell 原始输出，三个板块齐全

**四项全通过才交付。**

---

## 前置条件（极简）

- **Claude Code** 具备 Bash 工具权限
- **Obsidian Vault** 中有 `content/ready-to-post/` 文件夹（文件内需含 `**Posted:** ❌` 才会被识别为"未发布"）
- **curl** 已安装（天气查询依赖 curl，若不可用则优雅降级，不影响其他内容输出）
- 每日待办文件为**可选项**——缺少时仍会输出其余内容

---

## 为什么它值得你用？

| 传统方式 | Daily Briefing Builder |
|----------|----------------------|
| 打开 Obsidian → 找到今日待办 → 阅读 | 终端直接输出 |
| 打开内容文件夹 → 逐文件检查发布状态 | 一键扫描，按平台分类 |
| 打开浏览器 → 搜索天气 | 同一视图，不切换窗口 |
| 3 步操作，5-10 分钟 | 1 条命令，30 秒 |

> 本质上是一个"反碎片化"工具——让你的早晨从聚焦开始，而不是从切换 4 个窗口开始。

---

## 自定义适配

如果你使用的是不同的文件路径或标题格式，在调用技能时直接告诉 Claude Code：

```
Run the Daily Briefing Builder skill. 
我的 Vault 在 /home/me/notes，城市是 Tokyo。
每日待办在 daily/tasks/ 下，标题是"今日计划"。
```

Claude Code 会按照你的描述调整 Phase 2 中的 Shell 命令。

---

## 与 AGENTS.md 生态的联系

这个技能是内容营销日常工作流的"起点"——它告诉你今天该做什么、有什么待发内容。接下来可以联动：

- 内容创作技能 → 编写待发帖子
- 社交发布技能 → 执行跨平台发布
- 数据分析技能 → 回顾昨日/上周的内容表现

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
