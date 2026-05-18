# SkillOps Architecture

> 面向 Agent 能力资产的 CI/CD + Eval + Observability + Governance
> Version: v0.1 | 2026-05-18

---

## 核心命题

**不是重做发布系统，而是在现有自动化发版之上补齐 Skill 标准化、评测门禁、灰度治理、运行观测、失败样本回流和半自动优化能力。**

生产级 Skill 自动进化的正确姿势：系统收集失败 → 生成候选优化 → 跑评测 → 给出发布建议 → **人工审批后上线**。不允许未经评测直接覆盖生产版本。

---

## 核心概念

### Skill（技能包）

不是一句 prompt，而是**可复用的任务能力包**，包含：
- `skill.yaml` — 元数据（ID、版本、触发条件、输入输出协议、依赖）
- `SKILL.md` — 核心定义（任务说明、执行步骤、质量标准）
- `prompts/` — 系统提示词 + 用户模板
- `workflows/` — 多节点工作流定义
- `tools/` — 外部 API/脚本契约
- `knowledge/` — 知识库依赖
- `evals/` — 评测集（cases.jsonl + rubric.yaml）
- `examples/` — 正反例输出
- `changelog.md` — 变更记录

### Skill 管道（生命周期）

```
需求进入 → 判断是否新增/更新 Skill → 生成/修改 Skill 包
  → 自动校验与评测 → 人工审核 → 灰度发布
  → 运行日志采集 → 失败样本回流 → 生成候选优化 → 下一轮发布
```

### SkillOps

"面向智能体能力资产的 CI/CD + Eval + Observability + Governance"

| 概念 | 传统软件对应物 | Skill 管道含义 |
|------|-------------|-------------|
| Skill | 模块 / 插件 / 服务能力 | 可被 Agent 调用的任务能力包 |
| Skill Registry | 服务注册中心 / 制品库 | 管理 Skill 元数据、版本、状态和依赖 |
| Eval Gate | 单元测试 / 集成测试 / 质量门禁 | 发布前验证 Skill 输出质量与安全性 |
| Canary | 灰度发布 | 小流量验证 Skill 新版本效果 |
| Trace | 调用链追踪 | 记录 Skill 命中、执行、工具调用和输出质量 |
| Optimizer | 自动化重构建议 / AIOps | 从失败样本中生成候选优化方案 |

---

## 总体架构

```
┌──────────────────────────────────────────────┐
│  业务入口层：飞书 / Web / API / 内部控制台     │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Skill Router：意图识别、Skill 匹配、版本选择  │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Skill Runtime：执行 Prompt / Workflow / Tool │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Skill Eval Gate：格式、事实、工具、质量评测   │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Release & Canary：自动发版、灰度、回滚        │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Observability：日志、Trace、指标、失败样本    │
└──────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────┐
│  Skill Optimizer：样本回流、候选优化、人审     │
└──────────────────────────────────────────────┘
```

---

## 核心模块设计

### 1. Skill Registry（能力注册中心）

管理所有 Skill 的元数据、版本状态、依赖关系、发布记录和评测结果。

**关键字段**：
| 字段 | 说明 |
|------|------|
| `skill_id` | 全局唯一 ID（如 `product-selling-point-insight`）|
| `version` | 语义化版本号（如 `1.3.0`）|
| `status` | draft / testing / staging / canary / production / deprecated |
| `trigger_rules` | 触发条件（关键词、意图、场景、置信度阈值）|
| `input_schema` | 输入字段规范 |
| `output_schema` | 输出结构规范 |
| `dependencies` | 模型、工具、知识库、MCP、工作流依赖 |
| `eval_suite_id` | 绑定评测集 |
| `risk_level` | 风险等级：low / medium / high |
| `rollback_version` | 可回滚版本 |

### 2. Skill Router（能力路由器）

三层路由结构：

| 路由层 | 适用场景 | 说明 |
|--------|---------|------|
| **规则路由** | 高确定性任务 | 明确关键词匹配（如"用户细分""卖点洞察"） |
| **模型路由** | 模糊任务 | LLM 判断意图与 Skill 匹配度，输出置信度和理由 |
| **上下文路由** | 多版本/多用户/多渠道 | 结合用户身份、渠道、项目、权限和灰度策略选择版本 |

### 3. Skill Runtime（执行层）

加载流程：
```
加载 skill.yaml → 加载 SKILL.md → 校验输入 → 注入上下文与记忆
  → 检索知识库 → 调用工具或工作流 → 生成初版输出 → 结构化校验
  → 必要时自修复 → 返回结果并写入 trace
```

### 4. Skill Eval Gate（评测门禁）

**评测类型与指标**：

| 评测类型 | 目标 | 示例指标 |
|---------|------|---------|
| 格式评测 | 输出是否符合 schema 和模板 | JSON 通过率、字段完整率、章节完整率 |
| 任务评测 | 是否完成业务目标 | rubric 得分、专家评分、关键点覆盖率 |
| 工具评测 | 是否正确调用工具 | 工具调用命中率、参数正确率、失败重试率 |
| 事实评测 | 是否存在编造或不当引用 | 幻觉率、引用有效率、证据覆盖率 |
| 安全评测 | 是否越权或泄露敏感信息 | 敏感信息泄露率、权限绕过率 |
| 回归评测 | 历史失败是否被修复且未反复 | 回归集通过率 |

**发布门槛示例**：
```yaml
release_gate:
  min_total_score: 85
  format_pass_rate: 0.98
  tool_call_accuracy: 0.95
  hallucination_rate_max: 0.03
  regression_case_pass_rate: 0.95
  human_review_required: true
```

### 5. Release & Canary（发布与灰度）

状态机：

| 状态 | 含义 | 准入条件 |
|------|------|---------|
| `draft` | 草稿 | Skill 包基本创建完成 |
| `testing` | 测试中 | 通过静态校验，可运行离线 eval |
| `staging` | 预发 | 通过基础评测，进入内部环境验证 |
| `canary` | 灰度 | 小流量线上验证，持续监控指标 |
| `production` | 生产 | 达到发布门槛并审批通过 |
| `deprecated` | 下线 | 不再新增调用，仅保留回滚或审计 |

### 6. Observability（可观测与问题回流）

**指标类型**：

| 类型 | 示例指标 |
|------|---------|
| 业务效果 | Skill 命中率、用户采纳率、人工修改率、用户追问率、任务一次完成率 |
| 模型质量 | Eval 平均分、格式通过率、幻觉率、知识库引用命中率、工具调用准确率 |
| 工程稳定性 | P95 延迟、失败率、超时率、回滚次数、版本变更失败率 |
| 交付效率 | Skill 发布频率、变更前置时间、变更失败率、失败恢复时间 |

### 7. Skill Optimizer（半自动优化层）

**明确边界**：只生成候选版本和优化建议，不直接覆盖生产版本。

优化闭环：
```
收集失败样本 → 自动聚类问题类型 → 生成优化建议
  → 生成候选 Skill vNext → 自动跑 Eval → 与线上版本对比
  → 人工审核 → 进入 staging / canary
```

**问题类型分类**：
| 类型 | 说明 |
|------|------|
| `route_miss` | 应调用 Skill 但未命中 |
| `wrong_skill` | 调用了错误 Skill |
| `format_error` | 输出格式不符合要求 |
| `shallow_output` | 内容过浅，业务不可用 |
| `hallucination` | 编造事实、链接或产品能力 |
| `tool_error` | 工具调用失败或参数错误 |
| `context_missing` | 缺少必要上下文或知识库召回 |
| `user_rejected` | 用户明确否定输出 |

---

## Skill 标准包规范（推荐目录结构）

```
skills/
└── product-selling-point-insight/
    ├── skill.yaml              # 元数据、触发条件、依赖
    ├── SKILL.md                # 核心定义、执行步骤、质量标准
    ├── prompts/
    │   ├── system.md           # 系统提示词
    │   └── user_template.md    # 用户输入模板
    ├── workflows/
    │   └── workflow.json       # 多节点工作流定义
    ├── tools/
    │   └── tool_contracts.yaml # 外部 API/脚本契约
    ├── knowledge/
    │   └── method_notes.md     # 方法论/知识库
    ├── evals/
    │   ├── cases.jsonl         # 评测样本集
    │   └── rubric.yaml         # 评分 rubric
    ├── examples/
    │   ├── good_outputs.md     # 正例
    │   └── bad_outputs.md      # 反例
    └── changelog.md            # 变更记录
```

---

## MVP 实施路线图

### 第一期（4 周）：标准化 + 评测 + 发版门禁

| 周次 | 重点任务 | 交付物 |
|------|---------|--------|
| 第 1 周 | 定义 Skill 包结构与规范 | skill.yaml 模板、SKILL.md 规范、目录模板、命名规范 |
| 第 2 周 | 开发 skillctl validate 与示例 Skill | 静态校验工具、3 个样例 Skill |
| 第 3 周 | 接入基础 Eval Runner | cases.jsonl、rubric.yaml、评测报告模板 |
| 第 4 周 | 接入现有发版流水线 | Eval Gate、staging 发布、失败拦截 |

### 第二期（4-6 周）：Registry + 灰度 + 观测

| 模块 | 交付内容 |
|------|---------|
| Skill Registry | Skill 列表、版本状态、负责人、依赖、评测结果 |
| Canary 发布 | 支持 5% / 10% / 50% / 100% 分阶段放量 |
| Dashboard | 调用量、命中率、失败率、eval 分、P95 延迟、反馈率 |
| Rollback | 一键切换 Registry 指针到上一生产版本 |
| Trace | 每次 Skill 调用记录 route/run/tool/eval/feedback |

### 第三期（6-8 周）：半自动优化

| 能力 | 说明 |
|------|------|
| 失败样本聚类 | 按 route_miss、format_error、hallucination 等类型自动归类 |
| 候选优化生成 | 基于失败样本生成 SKILL.md 或 prompt 修改建议 |
| 测试样本补充 | 将高价值失败案例转为回归测试 |
| 候选版本评测 | 自动比较生产版本与候选版本的得分 |
| 人审发布 | 通过审批后进入 staging/canary |

---

## 生产级判定标准（10 项）

| 判定项 | 达标标准 |
|--------|---------|
| 资产化 | 每个 Skill 有唯一 ID、版本号、负责人和变更记录 |
| 标准化 | 每个 Skill 具有统一目录结构、输入输出协议和依赖声明 |
| 可评测 | 每次发布前运行基础集、回归集和挑战集 |
| 可追踪 | 每次线上调用都能追踪 Skill 版本、路由理由、工具调用和输出结果 |
| 可灰度 | 新版本支持小流量验证和逐步放量 |
| 可回滚 | 异常时能快速回退到指定旧版本 |
| 可治理 | 高风险 Skill 发布需要人工审批 |
| 可优化 | 线上失败样本能回流成评测样本和优化建议 |
| 可度量 | 有调用量、命中率、失败率、采纳率、变更失败率等指标 |
| 可审计 | 保留审批、发布、回滚、评测和变更记录 |

**评估标准**：
- 满足 6 项以下 = 实验系统
- 满足 8 项以上 = 初步生产可用
- 全部满足 = 可对外称为 SkillOps / 智能体能力管道

---

## 推荐技术栈

| 模块 | 推荐方案 | 说明 |
|------|---------|------|
| Skill 仓库 | Git + 目录规范 | 第一期最稳，不建议先做复杂平台 |
| CI/CD | 复用现有 GitHub Actions / GitLab CI / Jenkins | 在现有发版前增加 validate 和 eval |
| Skill Registry | FastAPI + MySQL/PostgreSQL | 适合 Python 技术栈 |
| Runtime | Python 服务 | 统一封装模型、工作流、工具调用和上下文注入 |
| Eval Runner | 自建 runner + LLM-as-judge + rule checker | 按 Skill 类型组合规则评分和模型评分 |
| Trace | OpenTelemetry / LangSmith / 自建日志 | 优先保证 trace 字段完整 |
| Dashboard | Grafana / Metabase / Superset | 快速看指标，不必第一期自研大屏 |
| 灰度 | 配置中心 + 流量分桶 | 按用户、渠道、项目或比例分流 |
| 回滚 | Registry 指针切换 | 回滚本质是切 production 指向的 Skill 版本 |

---

## 风险与治理

| 风险 | 表现 | 控制策略 |
|------|------|---------|
| Skill 膨胀 | Skill 越做越多，边界重叠，路由混乱 | 建立分类体系；上线前要求边界说明；定期清理 deprecated |
| 错误自动固化 | Optimizer 将错误经验写回生产 Skill | 候选版本必须跑回归集；高风险变更必须人工审批 |
| 评测过拟合 | 只对固定测试集表现好，线上仍失败 | 基础集、回归集、挑战集和隐藏集分层；持续补充真实失败样本 |
| 灰度无监控 | 灰度版本变差但没有被发现 | 灰度绑定指标阈值，异常自动暂停或回滚 |
| 依赖漂移 | 知识库、工具、模型版本变化导致 Skill 失效 | 记录依赖版本；依赖变更触发相关 Skill 回归测试 |
| 权限越界 | Skill 调用了不该调用的工具或数据 | 工具白名单、权限校验、敏感操作人审 |
| 成本失控 | 评测和运行链路消耗过高 | 按风险等级设置评测规模；缓存与抽样策略 |

---

## 参考来源

| # | 来源 | 关键观点 |
|---|------|---------|
| [1] | Anthropic Claude API Docs - Agent Skills | Skill 是模块化能力包，包含 instructions、metadata、scripts、templates |
| [2] | Anthropic Engineering - Equipping agents for the real world | Progressive Disclosure：metadata 初筛，需要时再加载 SKILL.md |
| [3] | OpenAI API Docs - Evaluation best practices | Eval 是结构化测试，结合自动指标与人工判断，避免 vibe-based evals |
| [4] | OpenAI API Docs - Working with evals | 构建 eval 流程：描述任务 → 运行测试输入 → 分析结果 → 迭代 |
| [5] | OpenTelemetry Documentation | 供应商中立的可观测框架，覆盖 traces、metrics、logs |
| [6] | LangGraph Documentation | 生产级 agent 编排需要 durable execution、human-in-the-loop、memory、tracing |
| [7] | GitHub Docs - Deployments and environments | deployment protection rules 支持人工审批、等待时间和分支限制 |
| [8] | Google SRE Workbook - Canarying Releases | 先暴露给一小部分流量，与控制组对比后再扩大 |
| [9] | DORA - Software delivery performance metrics | 交付性能同时衡量吞吐与稳定性 |

---

**Contributors**: MeerkatAI Team
**License**: MIT (same as repository)
