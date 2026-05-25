# MeerkatAI Skill Registry

> 统一的 Skill 发版仓库，支持多领域 AI Agent 能力标准化复用与持续迭代。
>
> 📋 **[Registry 索引与使用指南 → SKILL-REGISTRY.md](SKILL-REGISTRY.md)**
> （26 skills, 8 categories, 完整目录树与变更历史）

🇺🇸 **English Version → [docs/README.en.md](docs/README.en.md)**

---

## 项目定位

本仓库是 **MeerkatAI 的 Skill Registry（技能注册表）**，用于：

- **Skill 标准化发版**：将各领域 Agent 能力封装为可复用的 Skill 规范
- **Skill 管道工作流**：支持 Skill 的版本管理、依赖追踪与持续迭代
- **多场景覆盖**：制造业、研发工程、设计创意、商业运营等领域
- **统一规范**：所有 Skill 遵循一致的结构、质量标准与输出格式

#### 与普通 Agent Prompt 的区别

| | 普通 Prompt | MeerkatAI Skill |
|---|---|---|
| 2026-05-25 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-24 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-23 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-22 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-21 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-20 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-19 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| 2026-05-19 | `incident-response-commander` (Incident Response Commander Agent) 新增 | agency-agents → engineering |
| **结构化** | 松散的自然语言 | 统一的章节规范（简介→框架→链路→输出→质检） |
| **深度** | 停留在建议层 | 下钻到动作级，附带量化指标与证据链 |
| **可落地** | 抽象结论 | 执行动作 + 责任角色 + 系统落点 + 验收阈值 |
| **可复用** | 一次性对话 | 可版本化、可分发、可管道化集成 |
| **质量门禁** | 无 | 输入完整度评分 + 合规闸门 + 24 项自检清单 |

---

### 仓库结构

```
manufacturing-ai-efficiency-Skill/          # Skill Registry 根目录
├── README.md                               # 本文件（Skill Registry 总览）
├── skill-index.yaml                        # 【Registry 索引】聚合全部 Skill 元数据
│
├── skills/engineering/                     # 🔧 工程研发类（9 个 Skill）
│   ├── ai-engineer/                        #   AI 工程师（ML/LLM 开发部署）
│   ├── autonomous-optimization-architect/  #   自主优化架构师
│   ├── backend-architecture/               #   后端架构设计
│   ├── devops-automator/                   #   DevOps 自动化
│   ├── embedded-firmware-engineer/         #   嵌入式固件工程师
│   ├── frontend-development/               #   前端开发
│   ├── rapid-prototyper/                   #   快速原型开发
│   ├── security-engineer/                  #   安全工程师
│   └── senior-developer/                   #   高级开发工程师
│
├── skills/design/                          # 🎨 设计创意类（7 个 Skill）
│   ├── brand-guardian/                     #   品牌守护者
│   ├── image-prompt-engineer/              #   图像提示工程师
│   ├── inclusive-visuals-specialist/       #   包容性视觉专家
│   ├── ui-design/                          #   UI 设计
│   ├── ux-architect/                       #   UX 架构师
│   ├── ux-research/                        #   UX 研究
│   └── visual-storyteller/                 #   视觉叙事师
│
├── skills/manufacturing/                   # 🏭 制造业类（1 个 ⭐ 旗舰）
│   └── manufacturing-ai-efficiency-pro/      #   制造业 AI 提效分析（V2.0）
│       └── references/                     #     制造业专用参考资料
│
├── skills/commercial/                      # 🛒 商业运营类（2 个）
│   ├── fast-moving-consumer-goods-ecommerce-operator/   # 快消电商运营
│   └── fast-moving-consumer-goods-supply-chain/         # 快消供应链
│
├── skills/content/                         # 📱 内容宣发类（3 个）
│   ├── content-monetization-pipeline/      #   内容变现分发管线（V1.0）
│   ├── ppt-master/                         #   📊 PPT Master — AI 原生 PPTX（V2.7）
│   │   ├── SKILL.md
│   │   ├── skill.yaml
│   │   ├── README.md
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
├── skills/creative/                        # ✨ 创意增强类（1 个）
│   └── whimsy-injector/                    #   趣味注入师
│
├── skills/product/                         # 📦 产品应用类（2 个）
│   ├── filament-optimization-specialist/   #   耗材优化专家（3D 打印）
│   └── mobile-app-builder/               #   移动应用构建
│
├── skills/operations/                      # ⚙️ 运维管理类（1 个）
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
└── .scripts/                               # 仓库级脚本 (hidden)
    ├── batch_generate_skill_yaml.py        #   批量生成 YAML 脚本
    └── skillctl_validate.py                #   Skill 校验脚本
```

---

### Skill 清单（26 个）

#### 🔧 工程研发类（9 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `ai-engineer` | ML 模型开发、LLM 集成、MLOps、生产部署 | agency-agents |
| `autonomous-optimization-architect` | 系统性能与成本自主优化架构 | agency-agents |
| `backend-architecture` | 后端架构设计与系统架构 | agency-agents |
| `devops-automator` | DevOps 流程自动化与 CI/CD | agency-agents |
| `embedded-firmware-engineer` | 嵌入式固件开发、RTOS、驱动 | agency-agents |
| `frontend-development` | 前端开发与技术实现 | agency-agents |
| `rapid-prototyper` | 3 天内出 MVP 的快速原型开发 | agency-agents |
| `security-engineer` | 安全审计、漏洞修复与防护策略 | agency-agents |
| `senior-developer` | 高级开发工程师全栈技术决策 | agency-agents |

#### 🎨 设计创意类（7 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `brand-guardian` | 品牌一致性守护与优化 | agency-agents |
| `image-prompt-engineer` | 图像 Prompt 工程优化 | agency-agents |
| `inclusive-visuals-specialist` | 包容性视觉设计 | agency-agents |
| `ui-design` | UI 界面设计与组件规范 | agency-agents |
| `ux-architect` | UX 架构与体验优化 | agency-agents |
| `ux-research` | 用户研究与需求洞察 | agency-agents |
| `visual-storyteller` | 视觉叙事与品牌故事 | agency-agents |

#### 🏭 制造业类（1 个 ⭐ 旗舰）

| Skill | 定位 | 版本 |
|-------|------|------|
| `manufacturing-ai-efficiency-pro` | 制造业流程拆解→AI 提效扫描→人机协同方案 | **V2.0** |

#### 🛒 商业运营类（2 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `fast-moving-consumer-goods-ecommerce-operator` | 快消品电商运营 | agency-agents |
| `fast-moving-consumer-goods-supply-chain` | 快消品供应链管理 | agency-agents |

#### 📱 内容宣发类（3 个）

| Skill | 定位 | 版本 |
|-------|------|------|
| `content-monetization-pipeline` | 内容资产→多平台分发→变现结算全链路 | **V1.0** |
| `ppt-master` | AI 原生可编辑 PPTX 生成（SVG→DrawingML） | **V2.7** |
| `product-promo-video-maker` | 产品页分析→网页渲染→录屏→语音合成→视频合成 | **V1.1** |

#### ✨ 创意增强类（1 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `whimsy-injector` | 趣味性创意注入与优化 | agency-agents |

#### 📦 产品应用类（2 个）

| Skill | 定位 | 来源 |
|-------|------|------|
| `filament-optimization-specialist` | 3D 打印耗材优化与参数调优 | agency-agents |
| `mobile-app-builder` | 移动应用全栈构建 | agency-agents |

#### ⚙️ 运维管理类（1 个）

| Skill | 定位 | 版本 |
|-------|------|------|
| `skillops-manager` | Skill 创建、校验、评测、发布、治理全生命周期 | **V1.0** |

---

### 旗舰 Skill 详解：`manufacturing-ai-efficiency-pro`

> 本仓库中**最完整、最复杂**的 Skill，代表了 MeerkatAI Skill 规范的最高水准。

#### 核心能力

将制造业问题拆解为**可验证、可追溯、可落地**的人机协同工作流：

- **场景拆解**：从价值链层（研产供销服）→ 子流程层 → **动作级最小单元**
- **AI 可行性判断**：逐动作判定 Level A（AI 自闭环）/ B（人机协同）/ C（人主导）
- **落地方案输出**：3-5 张机会卡，每张含数据前提、系统改造点、收益、Go/No-Go 阈值

#### 九步执行链路

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

#### 质量门禁体系

| 门禁类型 | 说明 |
|---------|------|
| **输入完整度评分** | 0-100 分，<60 分不进入深度分析 |
| **内容颗粒度闸门** | 痛点/约束/数据对象/角色未明确则暂停 |
| **合规闸门** | 质量红线 + 安全环境 + 审批责任，不通过则降级 |
| **数据准备度分级** | D0→D3，不匹配则建议先补基础 |
| **24 项自检清单** | 输出前强制检查 |

---

### 使用方法

#### 方式一：直接在 AI 工具中使用

将 `SKILL.md` 内容作为系统提示词或参考文档提供给 AI：

```
请基于 skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md 的规范，
分析以下制造业场景的 AI 提效空间：
[粘贴场景描述]
```

#### 方式二：在 OpenClaw/Trae 中注册

```bash
# 克隆仓库
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git

# 复制所需 Skill 到 skills 目录
cp manufacturing-ai-efficiency-Skill/skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md \
   ~/.openclaw/workspace/skills/
```

#### 方式三：编程式调用

```python
# 读取 Skill 定义
with open("skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md", "r") as f:
    skill_definition = f.read()

# 将 Skill 注入 AI 会话
response = ai.chat(
    system_prompt=skill_definition,
    user_input=user_scenario
)
```

---

### 贡献指南

#### 新增 Skill

1. 创建 `feature/<skill-name>` 分支
2. 新建目录 `skills/<category>/<skill-name>/`
3. 按规范填写 `SKILL.md` + `skill.yaml` + `README.md` + `changelog.md`
4. 更新本 README 的 Skill 清单 + `skill-index.yaml`
5. 提交 PR 到 `ling` 分支

#### 改进现有 Skill

1. 创建 `feature/<skill-name>-improvement` 分支
2. 修改对应 `SKILL.md`
3. 更新版本号（如 V1.0 → V1.1）
4. 在 `SKILL.md` 末尾添加 **Development History** 章节
5. 提交 PR，说明改进原因和影响

---

### 许可证

本项目采用 **MIT License** 开源许可证。

- 自由使用、复制、修改
- 可用于商业或非商业目的
- 分发副本需保留原始许可证和版权声明

---

**Made with ❤️ for AI Agent Skill Standardization**