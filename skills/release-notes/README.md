# Release Notes — 让 Changelog 从"写不动"变成"自动出草稿"

> 用户不看你的 commit history，他们看 changelog。一个没有 changelog 的发布，约等于没说"我到底改了什么"。

## 痛点：Changelog 永远是发布前最后一秒的负担

你刚刚修了 23 个 bug、加了 4 个 feature、重构了 3 个模块。Product Manager 在 Slack 上好声好气地问："release notes 写了吗？"你看着 30+ 条 git log 陷入沉默。

更糟糕的是：你的 commit message 风格混搭——有的遵循 Conventional Commits，有的是"fix stuff"，有的是凌晨三点写的表情包。手动整理分类、写人话描述、按语义化版本规则判断该升大版本还是小版本……这过程消耗的不只是时间，更是心力。

## 能力：从 Git 历史到标准 Changelog 的全自动流水线

`release-notes` 把"写 changelog"这件事拆成机器擅长和人擅长的两部分——机器负责收集、分类、格式化，人负责审阅和决策。

三种工作模式：

- **`changelog`** — 读取上次 tag 以来的所有 commit，按类型自动分类（Added / Fixed / Breaking Changes / Changed / Documentation / Maintenance / Security），输出标准的 [Keep a Changelog](https://keepachangelog.com/) 格式条目，预置到 CHANGELOG.md 顶部。
- **`release`** — 在 changelog 基础上，自动建议语义化版本号（Major / Minor / Patch），并可选择通过 `gh release create` 创建 GitHub Release。
- **`init`** — 走查整个 Git 历史，为从未有过 changelog 的项目生成完整回溯版 CHANGELOG.md。

智能之处在于：它会自动关联 GitHub 上的已合并 PR——PR 标题通常比 commit message 更干净易读，优先使用 PR 标题作为描述。遇到无法归类的 commit，会标出来让你手动判断，而不是猜测。

**绝不自动发布。** 每一次写入文件、每一次创建 GitHub Release，都等你确认后才执行。这是一个辅助工具，不是自动挡。

## 谁在用？

- **开源项目维护者**：保持 changelog 更新频率，用标准格式赢得用户信任。
- **产品 / 工程经理**：发布前不再追着开发要 release notes。
- **独立开发者**：一个人维护多个库时，自动化 changelog 是救命稻草。
- **技术写作 / DevRel**：基于 changelog 快速生成发布博客和技术公告。

## 配合其他技能

- **`repo-health`**：检查 CHANGELOG.md 是否存在及新鲜度。
- **`safe-push`**：release body 和 changelog 内容推送前做敏感信息扫描。
- **`sync-repos`**：发布到公开仓库前确认同步状态无遗漏。

> **"Changelog 不是写给机器看的，是写给下一个接手项目的人看的——包括三个月后的你自己。"**

---

猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用
