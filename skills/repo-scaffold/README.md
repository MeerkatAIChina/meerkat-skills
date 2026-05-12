# Repo Scaffold — 新仓库的第一块积木，也是旧仓库的补完计划

> 标准化的起点决定了协作的效率。一个没有 CONTRIBUTING.md 的仓库会让潜在贡献者转身就走；一个没有 SECURITY.md 的仓库让安全研究者不知道该往哪报告漏洞。

## 痛点：搭仓库 ≠ git init

`git init` 只需一秒，但让一个仓库真正"准备好迎接协作"需要十几个标准化文件。很多开发者要么缺东西（忘了 .editorconfig），要么套用别的项目的模板（Python 项目的 .gitignore 里留着 node_modules），要么干脆裸奔。

更麻烦的是"补课"——已有一定代码量的仓库想补全标准文件时，最怕的是覆盖已有内容。没人愿意看到自己手写的 CONTRIBUTING.md 被模板替换掉。

## 能力：语言感知 + 零覆盖保障

`repo-scaffold` 是一款**项目类型感知型脚手架**。它会扫描你的仓库，识别技术栈（Node.js / Python / Rust / Go / 多语言），然后为每一种语言定制最适合的模板。

一次命令可以生成以下全部文件（按需选择）：

- **LICENSE**（MIT / Apache-2.0 / ISC / GPL-3.0 / BSD-2-Clause 可选）
- **.gitignore** — 根据检测到的语言组合精确匹配 ignore 模式
- **CONTRIBUTING.md** — Fork→Branch→PR 完整流程 + 分支命名规范 + 代码风格指引
- **SECURITY.md** — 支持版本表 + 漏洞报告渠道 + 响应时间线
- **CODEOWNERS** — 自动按目录结构映射所有者
- **.editorconfig** — 根据语言设置缩进、换行、字符集
- **YAML 表单式 Issue 模板**（Bug Report + Feature Request）
- **Pull Request 模板**（变更摘要 + 类型勾选 + 测试清单）
- **CI 骨架**（GitHub Actions，含 lint + test 步骤）
- **安全标记文件**（`.public-repo`、`.pii-allowlist`、`.commit-msg-blocklist`，公开仓库专用）

核心原则只有一条：**绝不覆盖已有文件**。每次运行先扫描冲突、列出计划、等你确认后才执行。已存在的文件永远安全。

## 谁在用？

- **新项目启动者**：从零到一，5 分钟搭完一套专业仓库骨架。
- **准备开源的团队**：私有仓库公开前补齐安全策略、社区文件和 CI 配置。
- **多仓库管理者**：统一组织中所有仓库的标准文件结构。
- **技术写作 / DevRel**：为开源项目快速配置符合社区规范的协作基础设施。

## 配合其他技能

- **`repo-health`**：先做体检定位缺口，再用 `repo-scaffold` 精准补全。
- **`github-readme`**：脚手架搭完，一键生成专业的 README。
- **`safe-push`**：公开仓库标记文件（`.public-repo` 等）与 `safe-push` 的安全扫描流程联动。
- **`sync-repos`**：如果你有私有/公开仓库对，脚手架配置的排除模式直接对接同步机制。

> **"开发者喜欢写代码，不喜欢搭架子。让脚手架帮你把架子搭好——你只管写代码。"**

---

猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用
