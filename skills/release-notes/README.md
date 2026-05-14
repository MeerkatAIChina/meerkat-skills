# 📝 发布说明生成器 — 从 Git 提交到用户能看懂的 Changelog

> **一句话：自动扫描 Git 提交历史，分类整理成用户友好、结构清晰的产品更新日志——告别手动翻 Commit 写 Release Notes 的苦力活。**

---

## 🤔 你的 Changelog 是不是长这样？

- 「Bug fixes and performance improvements」——用户看了跟没看一样
- 开发者写的 Commit message（`fix: resolve race condition in async handler`）直接贴给用户看
- 手动整理 Changelog 花了 2 小时，最后还是漏了几个重要更新
- 版本号管理混乱——不知道这次该升 Major 还是 Minor

**发布说明生成器**把 Git 提交自动翻译成用户能看懂的更新日志——自动分类（新功能/修复/破坏性变更/文档）、自动建议版本号、自动格式化——让你的产品更新传达专业且有温度。

---

## 🎯 边界说明

| ✅ 能做什么 | ❌ 不做什么 |
|-----------|-----------|
| 从 Git 提交历史自动生成 Changelog 条目 | 不自动发布——每次生成都需要人工确认 |
| 按 Conventional Commits 规范自动分类提交（feat/fix/breaking/docs…） | 不修改已有的 Changelog 条目 |
| 自动建议 Semantic Versioning 版本号（Major/Minor/Patch） | 不自动创建 Git Tag |
| 合并 PR 标题优化描述（PR 标题通常比 Commit 更清晰） | 不自动推送到生产环境 |
| 生成 GitHub Release（通过 `gh release create`） | 不替代完整的 Release 管理流程 |
| 回填历史 Changelog——支持从空项目生成完整 CHANGELOG.md | — |
| 遵循 Keep a Changelog 格式规范 | — |

---

## 🧰 核心能力

| 能力 | 说明 |
|------|------|
| **提交扫描** | `git log` 获取自上次 Tag 以来的所有提交，排除 Merge 提交 |
| **PR 关联** | 通过 `gh pr list` 获取已合并的 PR，用 PR 标题优化描述文案 |
| **自动分类** | Conventional Commits → 9 大分类（Added/Fixed/Breaking/Changed/Docs/Deprecated/Removed/Security/Maintenance） |
| **非规范提交推断** | 对不符合 Conventional Commits 的提交，通过关键词分析自动推断类别 |
| **版本号建议** | 基于变更内容自动推断语义化版本号（Major/Minor/Patch） |
| **Keep a Changelog** | 输出符合 keepachangelog.com 规范的结构化条目 |
| **人工审核闸门** | 生成后展示给用户确认，不自动写入 |
| **GitHub Release** | 可选通过 `gh release create` 创建 GitHub Release |
| **回填模式** | 无历史 Changelog 的项目，一键从全量 Tag 历史生成完整 CHANGELOG.md |

---

## 👤 谁应该用

- ✅ 产品营销经理——每次发版需要写用户能看懂的 Release Notes
- ✅ 开发者/技术负责人——不想手动整理 Changelog，但需要规范的发布流程
- ✅ 开源项目维护者——Keep a Changelog 格式 + GitHub Release 一站式
- ✅ 创业公司 CTO——自动化发布流程的一个关键环节
- ✅ 客户成功团队——需要了解每个版本改了啥，好跟客户沟通

---

## 🔗 配合其他 SKILL

| 搭配 SKILL | 联动场景 |
|-----------|---------|
| `launch-strategy` | 发布说明 + 发布策略 = 完整的产品发布 GTM |
| `newsletter-creation-curation` | Release Notes → 产品更新 Newsletter 发送给用户 |
| `social-content` | 把 Changelog 亮点转成社交媒体发布内容 |
| `internal-comms` | 内部全员同步产品更新 |
| `email-composer` | 给客户/用户写产品更新邮件 |

---

## 💡 金句

> **你的 Git 提交是写给开发者的。你的 Changelog 是写给用户的。这个技能帮你把前者翻译成后者。**

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
