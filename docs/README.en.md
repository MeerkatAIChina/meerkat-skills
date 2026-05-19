## English

### Project Positioning

This repository is the **MeerkatAI Skill Registry** for:

- **Skill Standardized Releases**: Packaging Agent capabilities from various domains into reusable Skill specifications
- **Skill Pipeline Workflow**: Supporting version management, dependency tracking, and continuous iteration
- **Multi-Domain Coverage**: Manufacturing, R&D engineering, design & creativity, commercial operations, and more
- **Unified Standards**: All Skills follow consistent structure, quality standards, and output formats

#### Difference from Ordinary Agent Prompts

| Dimension | Ordinary Prompt | MeerkatAI Skill |
|---|---|---|
| **Structure** | Loose natural language | Unified chapter specification (Intro→Framework→Pipeline→Output→QC) |
| **Depth** | Stays at recommendation level | Drills down to action level with quantitative metrics and evidence chains |
| **Actionable** | Abstract conclusions | Execution actions + responsible roles + system landing points + acceptance thresholds |
| **Reusable** | One-time conversation | Versionable, distributable, pipeline-integrable |
| **Quality Gates** | None | Input completeness score + compliance gates + 24-item self-checklist |

---

### Repository Structure

```
manufacturing-ai-efficiency-Skill/          # Registry Root
├── README.md                               # This file (Registry Overview)
├── skill-index.yaml                        # [Registry Index] Aggregated metadata for all Skills
│
├── skills/engineering/                     # 🔧 Engineering (9 Skills)
│   ├── ai-engineer/                        #   AI Engineer (ML/LLM dev & deployment)
│   ├── autonomous-optimization-architect/
│   ├── backend-architecture/               #   Backend Architecture Design
│   ├── devops-automator/                   #   DevOps Automation
│   ├── embedded-firmware-engineer/         #   Embedded Firmware Engineer
│   ├── frontend-development/               #   Frontend Development
│   ├── rapid-prototyper/                   #   Rapid Prototyping (MVP in 3 days)
│   ├── security-engineer/                  #   Security Engineering
│   └── senior-developer/                   #   Senior Full-Stack Developer
│
├── skills/design/                          # 🎨 Design & Creativity (7 Skills)
│   ├── brand-guardian/                     #   Brand Consistency Guardian
│   ├── image-prompt-engineer/              #   Image Prompt Engineering
│   ├── inclusive-visuals-specialist/       #   Inclusive Visual Design
│   ├── ui-design/                          #   UI Design
│   ├── ux-architect/                       #   UX Architecture
│   ├── ux-research/                        #   UX Research
│   └── visual-storyteller/                 #   Visual Storytelling
│
├── skills/manufacturing/                   # 🏭 Manufacturing (1 ⭐ Flagship)
│   └── manufacturing-ai-efficiency-pro/      #   Manufacturing AI Efficiency (V2.0)
│       └── references/                     #     APQC / 5M1E / T34 frameworks
│
├── skills/commercial/                      # 🛒 Commercial Operations (2)
│   ├── fast-moving-consumer-goods-ecommerce-operator/
│   └── fast-moving-consumer-goods-supply-chain/
│
├── skills/content/                         # 📱 Content & Marketing (3)
│   ├── content-monetization-pipeline/      #   V1.0, hybrid
│   ├── ppt-master/                         #   V2.7, production, flagship
│   │   ├── SKILL.md
│   │   ├── skill.yaml
│   │   ├── README.md
│   │   ├── references/
│   │   ├── scripts/                        #     50+ Python scripts
│   │   ├── templates/                      #     layouts + icons + charts
│   │   └── workflows/
│   └── product-promo-video-maker/          #   V1.1
│       ├── SKILL.md
│       ├── README.md
│       ├── config.template.json
│       ├── assets/                         #     templates & themes
│       ├── references/
│       └── scripts/                        #     capture/pipeline/render/voice.py
│
├── skills/creative/                        # ✨ Creative Enhancement (1)
│   └── whimsy-injector/                    #   Whimsy & Fun Injector
│
├── skills/product/                         # 📦 Product Application (2)
│   ├── filament-optimization-specialist/   #   3D Printing Filament Optimization
│   └── mobile-app-builder/                 #   Mobile App Builder
│
├── skills/operations/                      # ⚙️ Operations (1)
│   └── skillops-manager/                   #   V1.0, production
│       ├── SKILL.md
│       ├── README.md
│       ├── skill.yaml
│       └── scripts/
│           └── skillctl.py                   #     Skill Lifecycle Management CLI
│
├── docs/                                   # Specification Documents
│   ├── skill-yaml-spec.md                  #   Skill YAML Metadata Spec v1.0
│   └── skillops-architecture.md            #   SkillOps CI/CD Architecture
│
└── .scripts/                               # Repository-level scripts (hidden)
    ├── batch_generate_skill_yaml.py        #   Batch YAML generation script
    └── skillctl_validate.py                #   Skill validation script
```

---

### Skill Catalog (26 Skills)

#### 🔧 Engineering (9)

| Skill | Positioning | Source |
|-------|-------------|--------|
| `ai-engineer` | ML model development, LLM integration, MLOps, production deployment | agency-agents |
| `autonomous-optimization-architect` | System performance & cost autonomous optimization | agency-agents |
| `backend-architecture` | Backend architecture design & system architecture | agency-agents |
| `devops-automator` | DevOps process automation & CI/CD | agency-agents |
| `embedded-firmware-engineer` | Embedded firmware, RTOS, driver development | agency-agents |
| `frontend-development` | Frontend development & technical implementation | agency-agents |
| `rapid-prototyper` | Rapid MVP prototyping within 3 days | agency-agents |
| `security-engineer` | Security audit, vulnerability repair & protection | agency-agents |
| `senior-developer` | Senior full-stack technical decisions | agency-agents |

#### 🎨 Design & Creativity (7)

| Skill | Positioning | Source |
|-------|-------------|--------|
| `brand-guardian` | Brand consistency guard & optimization | agency-agents |
| `image-prompt-engineer` | Image prompt engineering optimization | agency-agents |
| `inclusive-visuals-specialist` | Inclusive & accessible visual design | agency-agents |
| `ui-design` | UI interface design & component specifications | agency-agents |
| `ux-architect` | UX architecture & experience optimization | agency-agents |
| `ux-research` | User research & requirement insights | agency-agents |
| `visual-storyteller` | Visual storytelling & brand narrative | agency-agents |

#### 🏭 Manufacturing (1 ⭐ Flagship)

| Skill | Positioning | Version |
|-------|-------------|---------|
| `manufacturing-ai-efficiency-pro` | Manufacturing process breakdown → AI efficiency scan → human-AI collaboration | **V2.0** |

#### 🛒 Commercial Operations (2)

| Skill | Positioning | Source |
|-------|-------------|--------|
| `fast-moving-consumer-goods-ecommerce-operator` | FMCG e-commerce operations | agency-agents |
| `fast-moving-consumer-goods-supply-chain` | FMCG supply chain management | agency-agents |

#### 📱 Content & Marketing (3)

| Skill | Positioning | Version |
|-------|-------------|---------|
| `content-monetization-pipeline` | Content assets → multi-platform distribution → monetization | **V1.0** |
| `ppt-master` | AI-native editable PPTX generation (SVG→DrawingML) | **V2.7** |
| `product-promo-video-maker` | Product page analysis → web rendering → screen recording → voice synthesis → video | **V1.1** |

#### ✨ Creative Enhancement (1)

| Skill | Positioning | Source |
|-------|-------------|--------|
| `whimsy-injector` | Whimsy & fun creative injection & optimization | agency-agents |

#### 📦 Product Application (2)

| Skill | Positioning | Source |
|-------|-------------|--------|
| `filament-optimization-specialist` | 3D printing filament optimization & parameter tuning | agency-agents |
| `mobile-app-builder` | Mobile app full-stack building | agency-agents |

#### ⚙️ Operations (1)

| Skill | Positioning | Version |
|-------|-------------|---------|
| `skillops-manager` | Skill create/validate/eval/release/governance lifecycle | **V1.0** |

---

### Flagship Skill Deep-Dive: `manufacturing-ai-efficiency-pro`

> The **most complete and complex** Skill in this repository, representing the highest standard of MeerkatAI Skill specifications.

#### Core Capabilities

Break down manufacturing problems into **verifiable, traceable, and actionable** human-AI collaboration workflows:

- **Scenario Breakdown**: Value chain layer (R&D/Production/Sales/Service) → subprocess layer → **action-level minimum units**
- **AI Feasibility Assessment**: Action-by-action classification Level A (AI autonomous) / B (human-AI collaboration) / C (human-led)
- **Deliverable Output**: 3-5 opportunity cards, each with data prerequisites, system transformation points, ROI, and Go/No-Go thresholds

#### 9-Step Execution Pipeline

```
1. Input Anchoring → 2. 3D Framework Anchoring (APQC+Value Chain+5M1E)
→ 3. L1 Process Breakdown (3-7 subprocesses)
→ 4. L2 Minimum Unit Refinement (action-level, 6-10 per subprocess)
→ 5. AI Efficiency Grading (4-dimension scoring)
→ 6. Core AI Opportunity Integration (opportunity cards)
→ 7. Human-AI Responsibility Division (T34 Model)
→ 8. Industry Knowledge Base Calibration
→ 9. Closed-Loop Iteration (roadmap 1-6mo / 6-12mo / 12-24mo)
```

#### Quality Gate System

| Gate Type | Description |
|-----------|-------------|
| **Input Completeness Score** | 0-100 points, <60 blocks deep analysis |
| **Content Granularity Gate** | Pause if pain points/constraints/data objects/roles unclear |
| **Compliance Gate** | Quality red lines + safety environment + approval responsibility |
| **Data Readiness Grading** | D0→D3, suggest foundation补齐 if mismatch |
| **24-Item Self-Checklist** | Mandatory pre-output inspection |

---

### Usage

#### Method 1: Direct Use in AI IDE

Use `SKILL.md` as system prompt or reference document:

```
Please analyze the following manufacturing scenario for AI efficiency opportunities
based on the specifications in skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md:
[ paste scenario description ]
```

#### Method 2: Register in OpenClaw/Trae

```bash
# Clone repository
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git

# Copy desired Skill to skills directory
cp manufacturing-ai-efficiency-Skill/skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md \
   ~/.openclaw/workspace/skills/
```

#### Method 3: Programmatic Invocation

```python
# Read Skill definition
with open("skills/manufacturing/manufacturing-ai-efficiency-pro/SKILL.md", "r") as f:
    skill_definition = f.read()

# Inject Skill into AI session
response = ai.chat(
    system_prompt=skill_definition,
    user_input=user_scenario
)
```

---

### Contribution Guide

#### Adding a New Skill

1. Create `feature/<skill-name>` branch
2. Create directory `skills/<category>/<skill-name>/`
3. Write `SKILL.md` + `skill.yaml` + `README.md` + `changelog.md` per spec
4. Update this README Skill catalog + `skill-index.yaml`
5. Submit PR to `ling` branch

#### Improving Existing Skills

1. Create `feature/<skill-name>-improvement` branch
2. Modify corresponding `SKILL.md`
3. Update version (e.g., V1.0 → V1.1)
4. Add **Development History** section at end of `SKILL.md`
5. Submit PR with improvement rationale and impact

---

### License

This project uses the **MIT License**.

- Free to use, copy, modify
- Available for commercial or non-commercial purposes
- Distribution copies must retain original license and copyright notice

---

**Made with ❤️ for AI Agent Skill Standardization**
