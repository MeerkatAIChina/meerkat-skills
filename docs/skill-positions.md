# Skill Positions — 技能定位清单

> 轻量级 skill 追踪清单，用于工具快速定位和查找 skills。

---

## skill-positions.yaml

### 文件位置

```
<repo-root>/skill-positions.yaml
```

### 用途

`skill-positions.yaml` 是一个 YAML 格式的技能清单，记录 `skills/` 目录下所有 skill 的简要信息，方便外部工具快速定位和发现可用的 skills。

它独立于 `skill-index.yaml`，两者用途不同、字段不同、互不依赖。

| 文件 | 用途 |
|---|---|
| `skill-positions.yaml` | 轻量定位索引，仅 5 个字段 |
| `skill-index.yaml` | 完整注册索引，包含版本、状态、分类等元数据 |

### 结构

```yaml
updated_at: "2026-05-29"
total_skills: 27
skills:
  - skill_id: product-promo-video-maker
    name: 产品宣发视频生成器
    description: 一键生成产品宣发视频，支持脚本撰写、素材匹配、语音合成与视频剪辑
    files:
      - README.md
      - SKILL.md
      - changelog.md
      - skill.yaml
      - references/analysis-frameworks.md
    path: skills/content/product-promo-video-maker/
```

### 字段说明

| 字段 | 类型 | 说明 |
|---|---|---|
| `updated_at` | string | 最后更新时间（ISO 日期，`YYYY-MM-DD`） |
| `total_skills` | int | 收录的 skill 总数 |
| `skills` | list | skill 条目列表 |

每个 skill 条目包含 5 个字段：

| 字段 | 类型 | 来源 | 说明 |
|---|---|---|---|
| `skill_id` | string | `skill.yaml` 中的 `skill_id` | skill 唯一标识 |
| `name` | string | `skill.yaml` 中的 `name` | skill 显示名称 |
| `description` | string | `skill.yaml` 中的 `description` | skill 简要描述 |
| `files` | list | 扫描目录生成 | skill 目录下所有文件（深度优先排列） |
| `path` | string | 扫描目录生成 | skill 目录相对于仓库根目录的路径 |

### 生成方式

由 `.scripts/generate_skill_positions.py` 脚本自动生成，不应手动编辑。

---

## generate_skill_positions.py

### 文件位置

```
.scripts/generate_skill_positions.py
```

### 用法

```bash
# 全量生成 — 扫描 skills/ 目录，覆盖写入
python .scripts/generate_skill_positions.py

# 增量追加 — 只添加 skills/ 中新增但尚未收录的 skill
python .scripts/generate_skill_positions.py --incremental

# 指定更新 — 按 skill_id 查找并覆盖该 skill 条目
python .scripts/generate_skill_positions.py --skill-id <skill_id>
```

### 工作流程

1. 遍历 `skills/` 目录，识别所有包含 `SKILL.md` + `skill.yaml` 的子目录为有效 skill
2. 从 `skill.yaml` 中提取 `skill_id` 和 `name`
3. 递归扫描 skill 目录，生成 `files` 列表（顶层文件优先，同层按字母排序）
4. 写入 `skill-positions.yaml`

### skill 识别规则

一个目录被识别为 skill 目录的充要条件：同时存在 `SKILL.md` 和 `skill.yaml` 两个文件。

满足这一条件的目录才会被收录，不满足的目录会被静默跳过。
