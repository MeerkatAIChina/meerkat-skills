# SkillOps 管理器 — skillctl CLI

> 统一的 Skill 生命周期管理入口，覆盖创建、校验、评测、发布和治理。

---

## 快速开始

```bash
# 创建新 Skill 骨架
python skillops-manager/scripts/skillctl.py create product-insight-skill "产品洞察 Skill" --category product --risk medium

# 校验仓库中所有 Skill
python skillops-manager/scripts/skillctl.py validate .

# 为某个 Skill 初始化评测集
python skillops-manager/scripts/skillctl.py eval-init product-promo-video-maker

# 检查版本升级是否需要重新评测
python skillops-manager/scripts/skillctl.py version-check product-promo-video-maker 1.0.0 1.1.0

# 生成仓库健康报告
python skillops-manager/scripts/skillctl.py report .

# 列出所有 Skill
python skillops-manager/scripts/skillctl.py list .
```

---

## 命令详解

### `create` — 创建新 Skill 骨架

```bash
python skillctl.py create <skill_id> <name> [options]

选项：
  --category  分类（engineering/design/manufacturing/ecommerce/product/content-creation/research/data/operations）
  --risk      风险等级（low/medium/high）

输出：
  <skill_id>/
    ├── skill.yaml          # 预填元数据
    ├── SKILL.md            # 标准章节骨架
    ├── evals/
    │   ├── cases.jsonl     # 测试样本骨架
    │   └── rubric.yaml     # 评分标准骨架
    ├── examples/           # 正例/反例目录
    ├── prompts/            # 提示词目录
    ├── knowledge/          # 知识库目录
    ├── workflows/          # 工作流目录
    ├── tools/              # 工具契约目录
    └── changelog.md        # 变更记录
```

### `validate` — 校验 Skill 包

```bash
python skillctl.py validate [path]
```

调用 `scripts/skillctl_validate.py`，检查：
- 目录结构完整性（skill.yaml + SKILL.md）
- skill.yaml 必填字段（9 项）
- 字段格式合规（version 语义化、status 在状态机内）
- production/canary 强制 eval 配置

### `eval-init` — 初始化评测集

```bash
python skillctl.py eval-init <skill_id>
```

分析 SKILL.md 中的执行步骤，自动生成：
- `evals/rubric.yaml` — 按步骤拆分评分维度（总分 100）
- `evals/cases.jsonl` — 5 个示例测试样本

**注意**：生成的是骨架，需要根据实际业务场景补充具体数据。

### `version-check` — 版本升级检查

```bash
python skillctl.py version-check <skill_id> <old_ver> <new_ver> [--change-desc "..."]
```

根据语义化版本规则判断：

| 变更 | 版本号 | 是否需要 eval |
|------|--------|-------------|
| 补丁（文档/typo） | patch +1 | 可选 smoke test |
| 功能新增/链路调整 | minor +1 | ✅ 必须 |
| 架构重构/模型更换 | major +1 | ✅ 全量回归 |

### `report` — 仓库健康报告

```bash
python skillctl.py report [path]
```

输出统计：
- Skill 总数、按状态分布、按分类分布
- 评测覆盖度（有 evals/ 的 Skill 比例）
- 最近更新 Skill 列表

### `list` — 列出所有 Skill

```bash
python skillctl.py list [path]
```

以表格形式输出所有 Skill 的 ID、名称、版本、状态。

---

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `SKILLS_ROOT` | Skill 仓库根目录 | 当前目录 |
| `SKILL_OWNER` | 新建 Skill 的默认负责人 | unknown |

---

## 依赖

- Python 3.8+
- PyYAML（`pip install pyyaml`）

---

## 作为 OpenClaw Skill 使用

在 OpenClaw 中，你可以这样调用：

```
请使用 skillops-manager Skill 帮我：
1. 创建一个抖音内容分发 Skill（skill_id: douyin-distributor）
2. 校验整个仓库的 Skill 质量
3. 给 product-promo-video-maker 生成评测集
```

---

**Version: 1.0.0 | 2026-05-18**
