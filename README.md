# MeerkatAI Skill Registry

> 统一的 Skill 发版仓库，支持多领域 AI Agent 能力标准化复用与持续迭代。

---

## 项目定位

本仓库是 **MeerkatAI 的 Skill Registry（技能注册表）**，用于：

- **Skill 标准化发版**：将各领域 Agent 能力封装为可复用的 Skill 规范
- **Skill 管道工作流**：支持 Skill 的版本管理、依赖追踪与持续迭代
- **多场景覆盖**：制造业、研发工程、设计创意、商业运营等领域
- **统一规范**：所有 Skill 遵循一致的结构、质量标准与输出格式

### 与普通 Agent Prompt 的区别

| | 普通 Prompt | MeerkatAI Skill |
|---|---|---|
| **结构化** | 松散的自然语言 | 统一的章节规范（简介→框架→链路→输出→质检） |
| **深度** | 停留在建议层 | 下钻到动作级，附带量化指标与证据链 |
| **可落地** | 抽象结论 | 执行动作 + 责任角色 + 系统落点 + 验收阈值 |
| **可复用** | 一次性对话 | 可版本化、可分发、可管道化集成 |
| **质量门禁** | 无 | 输入完整度评分 + 合规闸门 + 24 项自检清单 |

---

## 仓库结构

```
manufacturing-ai-efficiency-Skill/          # Skill Registry 根目录
├── README.md                               # 本文件（Skill Registry 总览）
├── skill-index.yaml                        # 【Registry 索引】聚合全部 Skill 元数据
│
├── engineering/                            # 🔧 工程研发类（8 个 Skill）
│   ├── ai-engineer/                        #   AI 工程师（ML/LLM 开发部署）
│   ├── autonomous-optimization-architect/  #   自主优化架构师
│   ├── backend-architecture/               #   后端架构设计
│   ├── devops-automator/                   #   DevOps 自动化
│   ├── frontend-development/               #   前端开发
│   ├── rapid-prototyper/                   #   快速原型开发
│   ├── security-engineer/                  #   安全工程师
│   └── senior-developer/                   #   高级开发工程师
│
├── design/                                 # 🎨 设计创意类（7 个 Skill）
│   ├── brand-guardian/                     #   品牌守护者
│   ├── image-prompt-engineer/              #   图像提示工程师
│   ├── inclusive-visuals-specialist/       #   包容性视觉专家
│   ├── ui-design/                          #   UI 设计
│   ├── ux-architect/                       #   UX 架构师
│   ├── ux-research/                        #   UX 研究
│   └── visual-storyteller/                 #   视觉叙事师
│
├── manufacturing/                          # 🏭 制造业类（1 个 ⭐ 旗舰）
│   └── manufacturing-ai-efficiency-pro/      #   制造业 AI 提效分析（V2.0）
│       └── references/                     #     制造业专用参考资料
│           ├── apqc_standards.md
│           ├── ie_analysis_toolkit.md
│           ├── manufacturing_value_chain.md
│           ├── standards_and_maturity_framework.md
│           └── tencent_t34_model.md
│
├── commercial/                             # 🛒 商业运营类（2 个）
│   ├── fast-moving-consumer-goods-ecommerce-operator/   # 快消电商运营
│   └── fast-moving-consumer-goods-supply-chain/         # 快消供应链
│
├── content/                                # 📱 内容宣发类（3 个）
│   ├── content-monetization-pipeline/      #   内容变现分发管线（V1.0）
│   ├── ppt-master/                         #   📊 PPT Master — AI 原生 PPTX（V2.7）
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── skill.yaml
│   │   ├── references/
│   │   ├── scripts/                        #     50+ Python 脚本
│   │   ├── templates/                        #     布局 + 图标 + 图表
│   │   └── workflows/
│   └── product-promo-video-maker/          #   📹 产品宣发视频生成（V1.1）
│       ├── SKILL.md
│       ├── README.md
│       ├── config.template.json
│       ├── assets/                           #     模板与主题资源
│       ├── references/
│       └── scripts/                          #     capture/pipeline/render/voice.py
│
├── creative/                               # ✨ 创意增强类（1 个）
│   └── whimsy-injector/                    #   趣味注入师
│
├── product/                                # 📦 产品应用类（2 个）
│   ├── filament-optimization-specialist/   #   耗材优化专家（3D 打印）
│   └── mobile-app-builder/               #   移动应用构建
│
├── operations/                             # ⚙️ 运维管理类（1 个）
│   └── skillops-manager/                   #   SkillOps 管理器（V1.0）
│       ├── SKILL.md
│       ├── README.md
│       ├── skill.yaml
│       └── scripts/
│           └── skillctl.py                   #     Skill 生命周期管理 CLI
│
├── docs/                                   # 规范文档
│   ├── skill-yaml-spec.md                  #   Skill YAML 元数据规范 v1.0
│   └── skillops-architecture.md            #   SkillOps 架构设计
│
├── references/                             # 各 Skill 原始来源参考资料
│   ├── backend-architecture-source.md
│   ├── brand-guardian-source.md
│   ├── frontend-development-source.md
│   ├── image-prompt-engineer-source.md
│   ├── inclusive-visuals-specialist-source.md
│   ├── ui-design-source.md
│   ├── ux-architect-source.md
│   ├── ux-research-source.md
│   ├── visual-storyteller-source.md
│   └── whimsy-injector-source.md
│
└── scripts/                                # 仓库级脚本
    ├── batch_generate_skill_yaml.py        #   批量生成 YAML 脚本
    ├── skillctl_validate.py                #   Skill 校验脚本
    ├── stage1-normalization-log.md         #   阶段 1 规范化日志
    └── stage2-reorganization-log.md        #   阶段 2 重组日志
```

---

## Skill 清单（25 个）

### 🔧 工程研发类（8 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `ai-engineer` | ML 模型开发、LLM 集成、MLOps、生产部署 | agency-agents |
| `autonomous-optimization-architect` | 系统性能与成本自主优化架构 | agency-agents |
| `backend-architecture` | 后端架构设计与系统架构 | agency-agents |
| `devops-automator` | DevOps 流程自动化与 CI/CD | agency-agents |
| `frontend-development` | 前端开发与技术实现 | agency-agents |
| `rapid-prototyper` | 3 天内出 MVP 的快速原型开发 | agency-agents |
| `security-engineer` | 安全审计、漏洞修复与防护策略 | agency-agents |
| `senior-developer` | 高级开发工程师全栈技术决策 | agency-agents |

### 🎨 设计创意类（7 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `brand-guardian` | 品牌一致性守护与优化 | agency-agents |
| `image-prompt-engineer` | 图像 Prompt 工程优化 | agency-agents |
| `inclusive-visuals-specialist` | 包容性视觉设计 | agency-agents |
| `ui-design` | UI 界面设计与组件规范 | agency-agents |
| `ux-architect` | UX 架构与体验优化 | agency-agents |
| `ux-research` | 用户研究与需求洞察 | agency-agents |
| `visual-storyteller` | 视觉叙事与品牌故事 | agency-agents |

### 🏭 制造业类（1 个 ⭐ 旗舰）

| Skill | 定位 | 版本 |
|-------|------|------|
| `manufacturing-ai-efficiency-pro` | 制造业流程拆解→AI 提效扫描→人机协同方案 | **V2.0** |

### 🛒 商业运营类（2 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `fast-moving-consumer-goods-ecommerce-operator` | 快消品电商运营 | agency-agents |
| `fast-moving-consumer-goods-supply-chain` | 快消品供应链管理 | agency-agents |

### 📱 内容宣发类（3 个）

| Skill | 定位 | 版本 |
|-------|------|------|
| `content-monetization-pipeline` | 内容资产→多平台分发→变现结算全链路 | **V1.0** |
| `ppt-master` | AI 原生可编辑 PPTX 生成（SVG→DrawingML） | **V2.7** |
| `product-promo-video-maker` | 产品页分析→网页渲染→录屏→语音合成→视频合成 | **V1.1** |

### ✨ 创意增强类（1 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `whimsy-injector` | 趣味性创意注入与优化 | agency-agents |

### 📦 产品应用类（2 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `filament-optimization-specialist` | 3D 打印耗材优化与参数调优 | agency-agents |
| `mobile-app-builder` | 移动应用全栈构建 | agency-agents |

### ⚙️ 运维管理类（1 个）

| Skill | 定位 | 版本 |
|-------|------|------|
| `skillops-manager` | Skill 创建、校验、评测、发布、治理全生命周期 | **V1.0** |

---

## 旗舰 Skill 详解：`manufacturing-ai-efficiency-pro`

---

## 旗舰 Skill 详解：`manufacturing-ai-efficiency-pro`

> 本仓库中**最完整、最复杂**的 Skill，代表了 MeerkatAI Skill 规范的最高水准。

### 核心能力

将制造业问题拆解为**可验证、可追溯、可落地**的人机协同工作流：

- **场景拆解**：从价值链层（研产供销服）→ 子流程层 → **动作级最小单元**
- **AI 可行性判断**：逐动作判定 Level A（AI 自闭环）/ B（人机协同）/ C（人主导）
- **落地方案输出**：3-5 张机会卡，每张含数据前提、系统改造点、收益、Go/No-Go 阈值

### 九步执行链路

```
1. 输入锚定 → 2. 三维框架锚定（APQC+价值链+5M1E）
→ 3. 第一层流程拆解（3-7 个子流程）
→ 4. 第二层最小单元细化（动作级，6-10 个/子流程）
→ 5. AI 提效分级评估（4 维评分）
→ 6. 核心 AI 落地机会整合（机会卡）
→ 7. 人机权责划分（T34 模型）
→ 8. 行业知识库校准
→ 9. 闭环迭代（路线图 1-6月/6-12月/12-24月）
```

### 质量门禁体系

| 门禁类型 | 说明 |
|---------|------|
| **输入完整度评分** | 0-100 分，<60 分不进入深度分析 |
| **内容颗粒度闸门** | 痛点/约束/数据对象/角色未明确则暂停 |
| **合规闸门** | 质量红线 + 安全环境 + 审批责任，不通过则降级 |
| **数据准备度分级** | D0→D3，不匹配则建议先补基础 |
| **24 项自检清单** | 输出前强制检查 |

### 三层流程图规范

- **L1 总览图**：管理视角，8-15 节点，研产供销服全链
- **L2 分图**：执行视角，6-12 节点/子流程，含 APQC+5M1E+Owner
- **L3 详图**：动作级，6-10 节点/子流程，含 AI 等级+数据流向+Go/No-Go

### 文件规模

- `SKILL.md`：~49KB（最完整的 Skill 定义）
- `references/`：5 份制造业专用参考框架
- 附带 `scripts/validate_process.py` 输出校验脚本

---

## Skill 目录结构规范

每个 Skill 目录必须遵循以下结构：

```
<skill-name>/
├── SKILL.md                    # 【必须】Skill 核心定义文件
│   ├── 简介 / 项目定位
│   ├── 适用场景 / 不适用场景
│   ├── 核心分析框架
│   ├── Skill 工作方式（步骤链路）
│   ├── 主链路执行框架
│   ├── 输出结果格式
│   ├── 质量检查清单
│   └── 附录：原始 Skill 内容（保留来源追溯）
│
├── references/                 # 【可选】Skill 专用参考资料
│   └── *.md
│
├── examples/                   # 【可选】输入/输出示例
│   ├── input_example.md
│   └── output_example.md
│
└── scripts/                    # 【可选】校验/工具脚本
    └── validate_process.py
```

### SKILL.md 标准章节

| 章节 | 说明 | 优先级 |
|------|------|--------|
| 简介 | 一句话说明 Skill 用途 | 必须 |
| 项目定位 | 定位类型 + 原始来源 + 适配说明 | 必须 |
| 适用/不适用场景 | 边界清晰的触发条件 | 必须 |
| 核心分析框架 | 拆解方法论（对象化/证据链/量化/人机协同） | 必须 |
| Skill 工作方式 | 执行步骤（通常 6-8 步） | 必须 |
| 主链路执行框架 | 场景拆解→AI 判断→落地方案 | 必须 |
| 输出结果格式 | 交付物结构 | 必须 |
| 质量检查清单 | 自检标准（通常 10 项） | 必须 |
| 附录 | 原始来源追溯（YAML frontmatter + 原始内容） | 必须 |

---

## Skill 管道工作流（发版流程）

本仓库支持标准化的 Skill 发版与迭代流程：

### 1. Skill 开发阶段

```
开发者本地 → 按规范编写 SKILL.md → 自测质量清单 → 提交到 feature 分支
```

### 2. Skill 评审阶段

```
PR 提交 → 结构合规检查（目录/章节/字段）→ 内容深度评审 → references 完整性检查
```

### 3. Skill 发版阶段

```
合并到 main 分支 → 打版本标签（v1.0, v2.0...）→ 更新 Registry 索引（本 README）
```

### 4. Skill 使用阶段

```
用户/Agent 读取 SKILL.md → 按规范执行 → 输出交付物 → 运行校验脚本
```

### 分支策略

| 分支 | 用途 |
|------|------|
| `main` | 稳定发版分支，只接受已评审的 Skill |
| `ling` | 开发/集成分支，聚合待发版 Skill |
| `feature/<skill-name>` | 单个 Skill 的独立开发分支 |
| `jdyt` | 特定项目分支 |

---

## 使用方法

### 方式一：直接在 AI 工具中使用

将 `SKILL.md` 内容作为系统提示词或参考文档提供给 AI：

```
请基于 manufacturing-ai-efficiency-pro/SKILL.md 的规范，
分析以下制造业场景的 AI 提效空间：
[粘贴场景描述]
```

### 方式二：在 OpenClaw/Trae 中注册

```bash
# 克隆仓库
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git

# 复制所需 Skill 到 skills 目录
cp manufacturing-ai-efficiency-Skill/manufacturing-ai-efficiency-pro/SKILL.md \
   ~/.openclaw/workspace/skills/
```

### 方式三：编程式调用

```python
# 读取 Skill 定义
with open("manufacturing-ai-efficiency-pro/SKILL.md", "r") as f:
    skill_definition = f.read()

# 将 Skill 注入 AI 会话
response = ai.chat(
    system_prompt=skill_definition,
    user_input=user_scenario
)
```

---

## 当前版本状态

| Skill | 版本 | 状态 | 备注 |
|-------|------|------|------|
| `manufacturing-ai-efficiency-pro` | **V2.0** | ✅ 稳定 | 旗舰 Skill，三层流程图 + 评分闸门 |
| `content-monetization-pipeline` | **V1.0** | ✅ 新增 | 内容资产→多平台分发→变现结算全链路 |
| `product-promo-video-maker` | **V1.1** | ✅ 新增 | 产品宣发视频全自动生成 |
| 其他 21 个 Skill | V1.0 | ✅ 可用 | 基于 agency-agents 标准化包装 |

---

## 贡献指南

### 新增 Skill

1. 创建 `feature/<skill-name>` 分支
2. 新建目录 `<skill-name>/`
3. 按**Skill 目录结构规范**编写 `SKILL.md`
4. 如有需要，添加 `references/`、`examples/`、`scripts/`
5. 在 `references/` 根目录添加 `*-source.md`（追溯原始来源）
6. 更新本 README 的 Skill 清单
7. 提交 PR 到 `ling` 分支

### 改进现有 Skill

1. 创建 `feature/<skill-name>-improvement` 分支
2. 修改对应 `SKILL.md`
3. 更新版本号（如 V1.0 → V1.1）
4. 在 `SKILL.md` 末尾添加 **Development History** 章节
5. 提交 PR，说明改进原因和影响

### 质量要求

- 所有新增/修改必须通过**24 项自检清单**（参考 `manufacturing-ai-efficiency-pro`）
- 必须保留原始来源追溯（YAML frontmatter + 附录）
- 禁止空话、强制量化、强制证据链
- 目录和文件名使用小写 + 连字符格式

---

## 许可证

本项目采用 **MIT License** 开源许可证。

- 自由使用、复制、修改
- 可用于商业或非商业目的
- 分发副本需保留原始许可证和版权声明

---

## 相关资源

- **Skill 规范参考**：[OpenClaw AgentSkills 文档](https://docs.openclaw.ai)
- **原始来源**：[agency-agents](https://github.com/msitarzewski/agency-agents)（部分 Skill 基于此改编）
- **旗舰 Skill 详细文档**：见 `manufacturing-ai-efficiency-pro/SKILL.md`

---

**Made with ❤️ for AI Agent Skill Standardization**
�� `manufacturing-ai-efficiency-pro/SKILL.md`

---

**Made with ❤️ for AI Agent Skill Standardization**
