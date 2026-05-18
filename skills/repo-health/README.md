# 🏥 仓库健康体检 — 你的 GitHub 项目该做一次全面体检了

> **就像你不会一年不做体检，你的开源项目也不该等到 Star 停滞、Issue 堆积才想起检查。**

---

## 你正面临的痛点

你有一个 GitHub 仓库——可能是公司的开源项目、营销落地页代码、或技术博客源码。它一直在跑，但你也说不清：有没有缺少关键文件？分支保护开了没？有人在 git 里提交了 `.env` 文件吗？CHANGELOG 停在去年？

更致命的是：**当你想把这个仓库开源时，你完全不知道还差什么**——缺少 SECURITY.md 意味着安全报告无处可投，缺少 CODE_OF_CONDUCT.md 挡住了一半的潜在贡献者，缺少 CONTRIBUTING.md 让外部开发者无从下手。

---

## 这个 Skill 能做什么

| ✅ 能做 | ❌ 不做 |
|---------|---------|
| 扫描 11 项标准文件（LICENSE/README/.gitignore/SECURITY/CONTRIBUTING/CODEOWNERS 等） | 不会在普通审计模式下修改任何文件 |
| 通过 GitHub API 检查仓库配置（描述/Topics/分支保护/默认分支名/社交预览图） | 不会运行 `npm install` 或任何安装命令 |
| 检测代码卫生问题（过期分支/跟踪的 .env 文件/大二进制文件） | 不会推送代码或创建 Commit |
| 生成 0-100 分健康报告 + A-F 字母评级 + 优先级修复清单 | 不会对无本地访问权限的仓库进行评分 |
| `--fix` 模式自动生成缺失的标准文件（SECURITY/CONTRIBUTING/CODE_OF_CONDUCT/.editorconfig/模板） | 不会覆盖已有文件 |

---

## 核心能力

| 能力 | 说明 |
|------|------|
| **文件存在性检查** | 11 项标准文件逐一检测，公开/私有仓库标准不同 |
| **GitHub 配置审计** | 描述/Topics/主页 URL/默认分支/分支保护/社交预览——6 项配置检查 |
| **文档质量评估** | README 长度和结构 + CHANGELOG 格式和新鲜度 |
| **代码卫生扫描** | 过期分支/跟踪的 secrets 文件（.env/credentials）/ 大二进制文件（>5MB） |
| **自动修复** | `--fix` 模式按需生成缺失文件，内置 PII 擦洗 |

### 五维评分体系
| 维度 | 权重 | 检查内容 |
|------|------|---------|
| **标准文件** | 30% | LICENSE / SECURITY.md / CONTRIBUTING.md / CODEOWNERS / .gitignore / .editorconfig / 模板文件 |
| **GitHub 配置** | 15% | 描述 / Topics / 分支保护 / 默认分支名 |
| **文档质量** | 25% | README 完整度 / CHANGELOG 存在性和新鲜度 |
| **代码卫生** | 20% | 过期分支 / 跟踪的 secrets / 大二进制文件 |
| **社区建设** | 10% | CODE_OF_CONDUCT / Issue 模板 / PR 模板 / CONTRIBUTING.md |

---

## 谁应该用

- ✅ 准备将私有仓库开源——需要知道还缺什么标准文件
- ✅ 开源项目维护者——定期健康检查，保持项目可信度
- ✅ 技术市场负责人——你管理的每个对外仓库都是品牌资产
- ✅ 咨询顾问——接手客户项目时先做全面的仓库健康基线
- ✅ 团队技术负责人——确保所有项目仓库保持统一标准

---

## 配合其他 Skill

| 联动 Skill | 怎么配合 |
|-----------|---------|
| `github-readme` | repo-health 检测 README 存在性和长度，github-readme 做深度审计和内容优化 |
| `dep-audit` | repo-health 做结构健康，dep-audit 做依赖安全——完整的技术资产治理 |
| `release-notes` | repo-health 检查 CHANGELOG 存在性，release-notes 帮你生成它 |
| `schema-markup-generator` | 公开仓库的健康度也影响 AI 引擎对你项目的理解 |

---

## 金句

> **GitHub 仓库不是你代码的停车场——它是你品牌在开发者世界的名片。连 SECURITY.md 都没有的仓库，就像没有门锁的店铺。用 repo-health，给你的技术资产做一次全面体检。**

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
