# MeerkatAI Skill Registry — 总览与索引

> 统一的 Skill 发版仓库，支持多领域 AI Agent 能力标准化复用与持续迭代。
> 
> 本文件是 Registry 的运行时索引，与 `skill-index.yaml` 保持同步。

---

## 定位

**元基础设施项目** —— 不是具体执行 Skill，而是管理所有 Skill 的"家"。

| 角色 | 说明 |
|------|------|
| **Skill 仓库** | 26 个 Skill 的分类存储、版本管理、元数据索引 |
| **Registry 索引** | `skill-index.yaml` 聚合全部 Skill 元数据，供 AI IDE / OpenClaw 路由查询 |
| **发版管道** | `ling` 分支开发 → PR → `main` 稳定发版 |
| **规范定义** | `docs/skill-yaml-spec.md` + `docs/skillops-architecture.md` |

---

## 目录结构

```
manufacturing-ai-efficiency-Skill/          # Registry 根
├── README.md                               # 本文件（Skill Registry 总览）
├── SKILL-REGISTRY.md                       # 【本文件】Registry 索引与使用指南
├── skill-index.yaml                        # 聚合索引 (26 skills 元数据)
│
├── commercial/                             # 🛒 商业运营 (2)
│   ├── fast-moving-consumer-goods-ecommerce-operator/
│   └── fast-moving-consumer-goods-supply-chain/
│
├── content/                                # 📱 内容宣发 (3)
│   ├── content-monetization-pipeline/      # V1.0, hybrid
│   ├── ppt-master/                         # V2.7, production, 旗舰
│   │   ├── SKILL.md
│   │   ├── skill.yaml
│   │   ├── README.md
│   │   ├── references/
│   │   ├── scripts/                        # 50+ Python (svg_to_pptx/...)
│   │   ├── templates/                        # layouts + icons + charts
│   │   └── workflows/
│   └── product-promo-video-maker/          # V1.1
│
├── creative/                               # ✨ 创意增强 (1)
│   └── whimsy-injector/
│
├── design/                                 # 🎨 设计创意 (7)
│   ├── brand-guardian/
│   ├── image-prompt-engineer/
│   ├── inclusive-visuals-specialist/
│   ├── ui-design/
│   ├── ux-architect/
│   ├── ux-research/
│   └── visual-storyteller/
│
├── docs/                                   # 规范文档
│   ├── skill-yaml-spec.md                  #   YAML 元数据规范 v1.0
│   └── skillops-architecture.md            #   SkillOps CI/CD 架构
│
├── engineering/                            # 🔧 工程研发 (9)
│   ├── ai-engineer/
│   ├── autonomous-optimization-architect/
│   ├── backend-architecture/
│   ├── devops-automator/
│   ├── embedded-firmware-engineer/         # 2026-05-19 新增 (远程合并)
│   ├── frontend-development/
│   ├── rapid-prototyper/
│   ├── security-engineer/
│   └── senior-developer/
│
├── manufacturing/                          # 🏭 制造业 (1 旗舰)
│   └── manufacturing-ai-efficiency-pro/      # V2.0, 49KB SKILL.md
│       └── references/                     #   APQC / 5M1E / T34
│
├── operations/                             # ⚙️ 运维管理 (1)
│   └── skillops-manager/                   # V1.0, production
│       └── scripts/
│           └── skillctl.py                   # Skill 生命周期 CLI
│
├── product/                                # 📦 产品应用 (2)
│   ├── filament-optimization-specialist/
│   └── mobile-app-builder/
│
├── references/                             # 各 Skill 原始来源追溯
│
├── .scripts/                               # 仓库级脚本 (hidden)
│   ├── batch_generate_skill_yaml.py
│   └── skillctl_validate.py
│
└── .backup/                                # 备份 (hidden)
    └── stage2-2026-05-19/
```

---

## Skill 清单 (26 个)

### 🔧 工程研发类（9 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `ai-engineer` | ML 模型开发、LLM 集成、MLOps、生产部署 | 1.0.0 | testing |
| `autonomous-optimization-architect` | 系统性能与成本自主优化架构 | 1.0.0 | testing |
| `backend-architecture` | 后端架构设计与系统架构 | 1.0.0 | testing |
| `devops-automator` | DevOps 流程自动化与 CI/CD | 1.0.0 | testing |
| `embedded-firmware-engineer` | 嵌入式固件开发、RTOS、驱动 | 1.0.0 | testing |
| `frontend-development` | 前端开发与技术实现 | 1.0.0 | testing |
| `rapid-prototyper` | 3 天内出 MVP 的快速原型开发 | 1.0.0 | testing |
| `security-engineer` | 安全审计、漏洞修复与防护策略 | 1.0.0 | testing |
| `senior-developer` | 高级开发工程师全栈技术决策 | 1.0.0 | testing |

### 🎨 设计创意类（7 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `brand-guardian` | 品牌一致性守护与优化 | 1.0.0 | testing |
| `image-prompt-engineer` | 图像 Prompt 工程优化 | 1.0.0 | testing |
| `inclusive-visuals-specialist` | 包容性视觉设计 | 1.0.0 | testing |
| `ui-design` | UI 界面设计与组件规范 | 1.0.0 | testing |
| `ux-architect` | UX 架构与体验优化 | 1.0.0 | testing |
| `ux-research` | 用户研究与需求洞察 | 1.0.0 | testing |
| `visual-storyteller` | 视觉叙事与品牌故事 | 1.0.0 | testing |

### 🏭 制造业类（1 个 ⭐ 旗舰）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `manufacturing-ai-efficiency-pro` | 制造业流程拆解→AI 提效扫描→人机协同方案 | **2.0** | production |

### 🛒 商业运营类（2 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `fast-moving-consumer-goods-ecommerce-operator` | 快消品电商运营 | 1.0.0 | testing |
| `fast-moving-consumer-goods-supply-chain` | 快消品供应链管理 | 1.0.0 | testing |

### 📱 内容宣发类（3 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `content-monetization-pipeline` | 内容资产→多平台分发→变现结算全链路 | **1.0** | testing |
| `ppt-master` | AI 原生可编辑 PPTX 生成（SVG→DrawingML） | **2.7** | production |
| `product-promo-video-maker` | 产品页分析→网页渲染→录屏→语音合成→视频合成 | **1.1** | testing |

### ✨ 创意增强类（1 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `whimsy-injector` | 趣味性创意注入与优化 | 1.0.0 | testing |

### 📦 产品应用类（2 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `filament-optimization-specialist` | 3D 打印耗材优化与参数调优 | 1.0.0 | testing |
| `mobile-app-builder` | 移动应用全栈构建 | 1.0.0 | testing |

### ⚙️ 运维管理类（1 个）

| Skill | 定位 | 版本 | 状态 |
|-------|------|------|------|
| `skillops-manager` | Skill 创建、校验、评测、发布、治理全生命周期 | **1.0** | production |

---

## 使用方式

### 1. 查询 Registry (AI IDE)

```python
# 读取 Registry 索引
import yaml
with open("skill-index.yaml") as f:
    index = yaml.safe_load(f)

# 按分类筛选
content_skills = [s for s in index["skills"] if s["category"] == "content-creation"]
```

### 2. 使用具体 Skill

```bash
# 方式 A: 直接加载 SKILL.md 给 AI IDE
cat content/ppt-master/SKILL.md | # 作为 system prompt

# 方式 B: 在 OpenClaw/Trae 中注册
cp content/ppt-master/SKILL.md ~/.openclaw/workspace/skills/
```

### 3. 新增 Skill

1. `git checkout -b feature/<skill-name>`
2. 新建 `<<category>>/<skill-name>/` 目录
3. 按规范填写 `SKILL.md` + `skill.yaml` + `README.md` + `changelog.md`
4. 更新 `skill-index.yaml`
5. PR → `ling` 分支

---

## 变更历史

| 日期 | 事件 |
|------|------|
| 2026-05-18 | `manufacturing-ai-efficiency-pro` V2.0 旗舰 + 20+ agency-agents Skill 迁移 |
| 2026-05-18 | `content-monetization-pipeline` V1.0 新增 |
| 2026-05-18 | `product-promo-video-maker` V1.1 新增 |
| 2026-05-18 | `skillops-manager` V1.0 新增 (SkillOps 元管理) |
| 2026-05-18 | `ppt-master` V2.7 纳入 (hugohe3/ppt-master fork) |
| 2026-05-19 | **Stage 1**: 24 skill.yaml 标准化 (15 字段完整) |
| 2026-05-19 | **Stage 2**: 24 Skill 重组为 8 个分类目录 |
| 2026-05-19 | **Fix**: 根目录清理 (`scripts/` → `.scripts/`, 备份隐藏) |
| 2026-05-19 | 远程合并 `embedded-firmware-engineer` → 归入 `engineering/` |

---

*Registry Version: 2026.05.19-v3 | 26 skills across 8 categories*