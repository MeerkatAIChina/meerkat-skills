# skill-positions.yaml 添加 description 字段 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `skill-positions.yaml` 的每个 skill 条目中新增 `description` 字段，值从 `skill.yaml` 的 `description` 属性读取。

**Architecture:** 修改 `generate_skill_positions.py` 的 `build_entry()` 函数，多读取一个字段；更新 `docs/skill-positions.md` 的字段说明表。`skill-positions.yaml` 由脚本重新生成即可。

**Tech Stack:** Python 3, PyYAML

---

### Task 1: 修改 generate_skill_positions.py

**Files:**
- Modify: `.scripts/generate_skill_positions.py:62-78`

- [ ] **Step 1: 在 build_entry() 中读取 description 并加入返回 dict**

将 `build_entry()` 函数中的返回 dict 从：

```python
    return {
        'skill_id': skill_id,
        'name': name,
        'files': collect_files(full),
        'path': skill_path,
    }
```

改为：

```python
    return {
        'skill_id': skill_id,
        'name': name,
        'description': meta.get('description', ''),
        'files': collect_files(full),
        'path': skill_path,
    }
```

- [ ] **Step 2: 验证 — 全量生成并检查输出**

```bash
pip install pyyaml
python .scripts/generate_skill_positions.py
```

检查 `skill-positions.yaml` 中每个条目是否都包含 `description` 字段。

- [ ] **Step 3: 提交**

```bash
git add .scripts/generate_skill_positions.py skill-positions.yaml
git commit -m "feat: add description field to skill-positions.yaml entries"
```

---

### Task 2: 更新 docs/skill-positions.md

**Files:**
- Modify: `docs/skill-positions.md:53-58`

- [ ] **Step 1: 在字段说明表中新增 description 行**

在 `docs/skill-positions.md` 的 skill 条目字段表中，在 `name` 和 `files` 之间插入：

```markdown
| `description` | string | `skill.yaml` 中的 `description` | skill 简要描述 |
```

完整表格变为：

```markdown
| 字段 | 类型 | 来源 | 说明 |
|---|---|---|---|
| `skill_id` | string | `skill.yaml` 中的 `skill_id` | skill 唯一标识 |
| `name` | string | `skill.yaml` 中的 `name` | skill 显示名称 |
| `description` | string | `skill.yaml` 中的 `description` | skill 简要描述 |
| `files` | list | 扫描目录生成 | skill 目录下所有文件（深度优先排列） |
| `path` | string | 扫描目录生成 | skill 目录相对于仓库根目录的路径 |
```

- [ ] **Step 2: 提交**

```bash
git add docs/skill-positions.md
git commit -m "docs: add description field to skill-positions field table"
```
