# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目定位

这是 MeerkatAI 的 **Skill Registry（技能注册表）**，一个元基础设施项目 —— 不是执行具体 Skill，而是管理所有 Skill 的统一发版仓库。27 个 Skill 按类别（engineering/design/manufacturing/commercial/content/creative/product/operations）存放在 `skills/` 下。

## Skill 目录结构

每个 Skill 目录必须包含：

```
skills/<category>/<skill-name>/
├── SKILL.md          # 【必须】核心定义（提示词、执行步骤、质量标准）
├── skill.yaml        # 【必须】元数据（ID、版本、触发条件、输入输出协议）
├── README.md         # 【必须】Skill 说明文档
└── changelog.md      # 【建议】变更记录
```

可选子目录：`references/`（参考知识）、`scripts/`（工具脚本）、`templates/`（模板）、`workflows/`（工作流定义）、`assets/`（静态资源）。

## 常用命令

```bash
# 校验全部 Skill 的 skill.yaml 合法性
python .scripts/skillctl_validate.py skills/

# 校验单个 Skill
python .scripts/skillctl_validate.py skills/manufacturing/manufacturing-ai-efficiency-pro/

# 生成/更新 skill-positions.yaml（全量覆盖）
python .scripts/generate_skill_positions.py

# 增量追加（只添加新 Skill）
python .scripts/generate_skill_positions.py --incremental

# 按 skill_id 更新单个 Skill 条目
python .scripts/generate_skill_positions.py --skill-id <skill_id>

# 安装依赖（脚本需要 PyYAML）
pip install pyyaml
```

## 关键索引文件

| 文件 | 用途 |
|---|---|
| `skill-index.yaml` | 完整注册索引，含版本、status、category、type、risk_level 等元数据。**手动维护。** |
| `skill-positions.yaml` | 轻量定位清单，仅 5 字段（skill_id/name/description/files/path）。由 `generate_skill_positions.py` **自动生成，不应手动编辑。** |

两者互不依赖，用途不同。

## 新增 Skill 流程

1. 创建目录 `skills/<category>/<skill-name>/`
2. 编写 `SKILL.md` + `skill.yaml` + `README.md` + `changelog.md`
3. 运行 `python .scripts/skillctl_validate.py skills/<category>/<skill-name>/` 确保校验通过
4. 手动更新 `skill-index.yaml` 添加新 Skill 元数据
5. 运行 `python .scripts/generate_skill_positions.py --skill-id <skill-id>` 更新 positions
6. 更新 `README.md` 和 `SKILL-REGISTRY.md` 的 Skill 清单

## skill.yaml 规范

详见 `docs/skill-yaml-spec.md`。必填字段：`skill_id`（kebab-case 全局唯一）、`name`、`version`（语义化）、`status`（draft/testing/staging/canary/production/deprecated）、`owner`、`risk_level`（low/medium/high）、`description`（≥20 字符）、`trigger`（至少含 keywords 或 intent）。

## 发版流程

- `main` 分支为稳定发版
- 开发在 `feature/<name>` 分支进行，PR 目标为 `ling` 分支
- 推送 `v*` 标签触发 GitHub Actions（`.github/workflows/release.yml`），自动将 `skills/` 和 `skill-positions.yaml` 上传至阿里云 OSS
