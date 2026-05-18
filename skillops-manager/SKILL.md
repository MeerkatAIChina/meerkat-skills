# SkillOps 管理器

## 简介
本 Skill 是 MeerkatAI Skill Registry 的元管理层，负责 Skill 的创建、校验、评测、发布和治理。它是 SkillOps 能力生产线的入口，让每个 Skill 的生命周期都有标准可循。

## 项目定位
- **定位**：运维管理型 Skill（元管理层，不直接面向业务场景，面向 Skill 资产本身）
- **原始来源**：MeerkatAI 内部 SkillOps 架构设计 v0.1
- **适配说明**：已按 MeerkatAI Skill Registry 规范包装，包含统一 CLI 入口和骨架模板

## 适用场景
- 用户要求"新建一个 Skill"或"创建 Skill 骨架"
- 用户要求"检查仓库里 Skill 的质量"
- 用户要求"给某个 Skill 生成评测集"
- 用户要求"评估 Skill 版本是否需要升级"
- 用户要求"生成 Skill 仓库的健康报告"
- 用户要求"把现有 prompt 封装为标准 Skill 包"

## 不适用场景
- 用户要求执行具体的业务 Skill（如"帮我生成产品视频"）—— 应调用对应业务 Skill
- 用户要求修改 SkillOps 架构本身 —— 这是架构层变更，需要人工评审

## 核心能力

### 能力 1：Skill 创建（create）
根据用户提供的业务描述，自动生成符合 MeerkatAI 标准的 Skill 骨架目录。

**输出包含**：
- `skill.yaml` — 预填元数据（ID/名称/版本/分类/触发条件）
- `SKILL.md` — 标准章节骨架（简介→定位→场景→框架→链路→输出→质检）
- `evals/cases.jsonl` — 空评测集骨架（带示例格式）
- `evals/rubric.yaml` — 评分 rubric 骨架
- `examples/` — 正例/反例目录
- `changelog.md` — 初始变更记录

**质量标准**：
- skill_id 必须为 kebab-case（如 `product-video-maker`）
- 目录名必须与 skill_id 完全一致
- SKILL.md 必须包含 7 个标准章节
- 触发条件必须包含 keywords 或 intent 至少一项

### 能力 2：Skill 校验（validate）
调用 `skillctl_validate.py`，对仓库中所有 Skill 或指定 Skill 执行静态校验。

**校验维度**：
1. 目录结构完整性（skill.yaml + SKILL.md 必须存在）
2. skill.yaml 必填字段齐全（9 项）
3. 字段格式合规（version 语义化、status 在状态机内）
4. production/canary 状态强制要求 eval 配置
5. SKILL.md 同目录存在

**输出**：校验报告（通过/失败/警告清单）

### 能力 3：评测集初始化（eval-init）
分析 SKILL.md 中的执行链路和输出要求，自动生成评测集骨架。

**生成逻辑**：
- 提取 SKILL.md 中的"执行步骤"作为测试维度
- 提取"质量标准"作为评分 rubric
- 根据 input_schema 生成 10-20 个测试输入样本
- 每个样本标注预期行为和评分权重

**输出**：
- `evals/cases.jsonl` — 测试样本集
- `evals/rubric.yaml` — 评分标准

### 能力 4：版本升级检查（version-check）
对比两个版本的变更，判断是否满足版本号升级规则。

**升级规则**：
| 变更类型 | 版本号变化 | 是否需要重新 eval |
|---------|-----------|-----------------|
| 修复 typo、补充文档 | patch +1 | 否（可选 smoke test） |
| 新增功能、调整链路 | minor +1 | ✅ 是 |
| 重构架构、更换模型 | major +1 | ✅ 是（全量回归） |
| 变更 input/output schema | major +1 | ✅ 是（全量回归） |
| 新增/删除依赖 | minor/major | ✅ 是 |

**输出**：版本升级建议 + eval 必要性判断

### 能力 5：仓库健康报告（report）
生成整个 Registry 的健康度评估。

**统计维度**：
- Skill 总数、按状态分布（draft/testing/staging/canary/production）
- 按分类分布（engineering/design/manufacturing/ecommerce...）
- 校验通过率（有多少 Skill 通过 validate）
- 评测覆盖度（有多少 Skill 有 evals/）
- 风险等级分布
- 最近变更活跃 Skill 列表

## 执行链路（必须按顺序）

### 第一步：意图识别
判断用户请求属于哪种能力：
- "新建/创建 Skill" → **create**
- "检查/校验/质量" → **validate**
- "评测/测试集" → **eval-init**
- "版本/升级" → **version-check**
- "报告/健康度" → **report**
- 模糊请求 → 询问用户意图，给出 5 种能力的简要说明

### 第二步：信息收集
**create 场景需要**：
1. Skill 的业务目标（一句话描述）
2. 适用场景（什么时候调用）
3. 输入要求（必须收集什么信息）
4. 核心输出（交付什么成果）
5. 触发关键词（用户说什么话应该激活这个 Skill）
6. 分类（engineering/design/manufacturing/ecommerce/content-creation...）
7. 风险等级（low/medium/high）

**validate 场景需要**：
- 目标路径（整个仓库或单个 Skill 目录）

**eval-init 场景需要**：
- 目标 Skill ID

**version-check 场景需要**：
- 两个版本的 diff 或变更描述

### 第三步：执行对应能力
根据识别结果，调用对应的能力逻辑。

**create 输出**：
- 完整的目录结构和文件内容（Markdown 代码块）
- 说明用户需要补充的部分
- 建议下一步：运行 validate 确认骨架合规

**validate 输出**：
- 校验报告（通过/失败/警告）
- 失败项的修复建议

**eval-init 输出**：
- cases.jsonl 内容（JSONL 格式）
- rubric.yaml 内容
- 说明如何补充具体测试数据

**version-check 输出**：
- 版本升级建议
- eval 必要性判断

**report 输出**：
- 仓库健康度统计表
- 问题 Skill 列表
- 改进建议

### 第四步：质量自检
输出前完成以下检查：
- [ ] create 输出的 skill_id 是 kebab-case
- [ ] create 输出的目录结构符合规范
- [ ] validate 报告区分 ERROR/WARN/INFO
- [ ] eval-init 的 rubric 总分是否为 100
- [ ] version-check 的版本号变化是否符合规则
- [ ] report 的数据是否准确（基于实际文件统计）

## 质量标准

- **禁止编造 Skill ID**：必须从用户输入或现有目录中提取
- **禁止跳过必填字段**：create 时必须收集 7 项基本信息
- **禁止生成不合规的目录结构**：必须严格遵循 skill-yaml-spec.md
- **validate 必须真实**：不能假设所有 Skill 都通过，必须指出具体问题
- **report 必须基于实际数据**：不能编造统计数据

## 依赖说明

- **上游规范**：`docs/skill-yaml-spec.md`（元数据规范）、`docs/skillops-architecture.md`（架构设计）
- **执行工具**：`scripts/skillctl_validate.py`（校验）、`scripts/batch_generate_skill_yaml.py`（批量生成）
- **本 Skill 本身**：是元管理层，不依赖具体业务 Skill

## 开发历史

### V1.0 (2026-05-18)
- 初始版本：5 种核心能力（create / validate / eval-init / version-check / report）
- 包含统一 CLI 入口 `scripts/skillctl.py`
- 包含新 Skill 骨架模板 `templates/`
- 依赖现有校验和批量生成脚本

---

*本 Skill 遵循 MeerkatAI Skill Registry 规范，适用 MIT License。*
