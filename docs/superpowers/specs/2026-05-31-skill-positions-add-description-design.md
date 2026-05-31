# skill-positions.yaml 添加 description 字段

## 目标

在 `skill-positions.yaml` 的每个 skill 条目中新增 `description` 字段，值来源为 `skill.yaml` 中的 `description` 属性。

## 字段位置

条目内字段顺序：`skill_id` → `name` → `description` → `files` → `path`

## 改动文件

### .scripts/generate_skill_positions.py

`build_entry()` 函数中，读取 `description` 并加入返回 dict。缺失时默认空字符串 `""`。

### docs/skill-positions.md

字段说明表中新增一行 `description`，标注来源为 `skill.yaml` 中的 `description`。

## 非改动项

- `skill-positions.yaml` 本身由脚本自动生成，不需手动修改。
- `skill-index.yaml` 已有 description 概念，不受影响。

## 边界处理

- description 缺失 → 空字符串，不阻断生成
- description 含多行文本（YAML `>` / `|`）→ `yaml.safe_load` 已处理，直接作为字符串读取
