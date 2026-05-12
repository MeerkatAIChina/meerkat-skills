# Safe Push — 在 `git push` 之前挡住那行不该公开的代码

> 每条 `git push` 背后都可能藏着一个 `git revert` 还没来得及跑的安全事故。Safe Push 让事故变成"幸好还没按回车"。

## 痛点：Push 是单向门，没有回头路

你改了一个 bug，顺手把调试用的 API 密钥写在了文件里。commit message 里提到了客户的内部代号。一个 `git push` 回车下去——12 秒后，一切都在 GitHub 上变成公开历史。

即便你立刻发现、立刻重置、立刻 force push，搜索引擎的缓存、第三方索引服务、fork 了你的代码的人……无法一一追回。**Git 的分布式特性意味着：推出去就是不可逆的。**

现有的 pre-commit hook 能挡住密钥泄露，但它挡不住 commit message 里的敏感文字、挡不住大仓推送到公开远程时的风控触发、也挡不住你想公开却忘了仓库里还有 `.env` 的尴尬。

## 能力：六步防御链

`safe-push` 在每一个 `git push`（尤其是向公开仓库推送）之前建立六道防线：

1. **仓库分类** — 自动检测公开/私有。公开仓库启用全部检查，私有仓库运行核心 PII 扫描。
2. **PII 与密钥扫描** — 基于你的个人 blocklist（`~/.claude/safe-push-blocklist`）扫描 diff 内容。支持 `--full` 模式扫描全部跟踪文件，适合首次推送或定期深度审计。
3. **Commit Message 审计** — 同一个 blocklist 同时扫描 commit message 的标题和正文。"修了一个 bug"不会触发，但"修复客户 X 的上报"会。
4. **推送节流** — 多分支或大量 commit 时自动分批次推送、间隔等待，避免触发 GitHub 的自动化滥用检测。
5. **最终确认** — 在真正执行推送前，完整展示所有 commit message 供你目视确认（覆盖 amend 和本次会话新写的 commit）。
6. **推送 + 验证** — 执行推送后即时验证远程状态。

你的 blocklist 是你自己的。Safe Push 内置了常见模式（API 密钥前缀、私有 IP 范围、Slack token 格式等），但你通过 `~/.claude/safe-push-blocklist` 维护的自定义模式才是真正的主角。

## 谁在用？

- **全栈 / DevOps 工程师**：日常推送到公开仓库前的最后一道安全检查。
- **开源维护者**：管理公共/私有仓库对，确保公开侧不会泄露开发环境信息。
- **安全敏感团队**：金融、医疗、企业内部工具的开发者。
- **独立开发者**：只有一个人的团队更需要自动化安全防线——没有人帮你 double-check。

## 配合其他技能

- **`sync-repos`**：私有→公开同步后必须接 `safe-push`。
- **`repo-scaffold`**：脚手架生成的 `.pii-allowlist` 和 `.commit-msg-blocklist` 是 Safe Push 的 repo 级配置。
- **`release-notes`**：发布前确保 changelog 和 release body 不含敏感信息。

> **"`git push` 是开发者最容易后悔的命令。Safe Push 让后悔变成'差点就'。"**

---

猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用
