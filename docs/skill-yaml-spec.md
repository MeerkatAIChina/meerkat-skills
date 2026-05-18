# Skill YAML Specification v1.0

> MeerkatAI Skill Registry 元数据规范
> 每个 Skill 根目录必须包含 `skill.yaml`，作为 Registry 索引和 CI 校验的入口。

---

## 文件位置

```
skills/
└── <skill-name>/
    ├── skill.yaml      # 本文件【必须】
    ├── SKILL.md        # 核心定义【必须】
    └── ...
```

---

## 完整字段定义

```yaml
# ========== 身份标识 ==========
skill_id: "product-promo-video-maker"      # 【必须】全局唯一 ID，kebab-case
name: "产品宣发视频生成器"                  # 【必须】中文名称
version: "1.1.0"                           # 【必须】语义化版本号
status: "production"                       # 【必须】见下方状态机

# ========== 责任与归属 ==========
owner: "LinkmasterLing"                   # 【必须】负责人或团队
risk_level: "medium"                       # 【必须】low / medium / high
created_at: "2026-05-12"                   # 【建议】创建日期
updated_at: "2026-05-18"                   # 【建议】最后更新日期

# ========== 功能定位 ==========
description: >                             # 【必须】一句话描述
  从产
品网页抓取卖点 → 生成 HTML 故事板 → Playwright 录屏 → AI 配音 → ffmpeg 合成 MP4

category: "content-creation"                # 【建议】分类，见下方分类表
type: "hybrid"                             # 【必须】skill 类型，见下方类型表

# ========== 触发条件 ==========
trigger:                                    # 【必须】至少一种触发方式
  keywords:                                 # 关键词触发
    - "产品视频"
    - "宣发视频"
    - "promo video"
  intent:                                   # 意图触发
    - "product_video_generation"
    - "promotional_content_creation"
  min_confidence: 0.75                      # 意图匹配最低置信度

# ========== 输入输出协议 ==========
input_schema:                              # 【建议】输入字段规范
  required:
    - product_url
  optional:
    - theme
    - voice_style
    - target_platforms

output_schema:                             # 【建议】输出格式规范
  type: "mp4"
  additional_files:
    - "narration.txt"
    - "storyboard.html"

# ========== 依赖声明 ==========
dependencies:                              # 【建议】外部依赖
  models:
    - "kimi-coding/k2.6"
  tools:
    - "ffmpeg"
    - "playwright"
  knowledge_bases:
    - "product-analysis-framework"
  skills:
    - "product-analyst-webpage-maker"       # 上游 skill

# ========== 评测绑定 ==========
eval:                                      # 【production 必须】
  suite_id: "product-promo-video-eval-v1"   # 评测集 ID
  min_score: 85                           # 发布最低分
  format_pass_rate: 0.98
  regression_pass_rate: 0.95

# ========== 发布策略 ==========
release:                                   # 【建议】发布配置
  strategy: "canary"
  canary_steps: [10, 50, 100]
  rollback_version: "1.0.0"

# ========== 变更记录指针 ==========
changelog: "changelog.md"                  # 【建议】相对路径
```

---

## 状态机（status）

| 状态 | 含义 | 准入条件 | Registry 是否路由 |
|------|------|---------|-----------------|
| `draft` | 草稿 | 目录结构基本完整 | ❌ 否 |
| `testing` | 测试中 | 通过 `skillctl validate` | ❌ 否（仅开发者自测） |
| `staging` | 预发 | 通过离线 eval | ⚠️ 内部环境 |
| `canary` | 灰度 | 通过 staging 验证 + 人工审批 | ✅ 小流量 |
| `production` | 生产 | 通过 canary 监控 | ✅ 全量 |
| `deprecated` | 下线 | 不再维护 | ❌ 否（保留回滚/审计） |

**状态流转规则**：
```
draft → testing → staging → canary → production
                ↘
                 deprecated
```
- 不允许 `draft` → `production` 跳跃
- `production` → `deprecated` 需标注替代 Skill ID
- `canary` 失败自动回退到上一 `production` 版本

---

## Skill 类型（type）

| 类型 | 说明 | 示例 |
|------|------|------|
| `prompt` | 主要依赖提示词 | 文案优化、提纲生成 |
| `workflow` | 多节点工作流 | 用户细分、趋势扫描 |
| `tool` | 强依赖外部 API/脚本 | 表格生成、网页抓取、视频转换 |
| `hybrid` | Prompt + Workflow + Tool + Knowledge | 竞品洞察、产品概念提案 |

---

## 分类体系（category）

| 分类 | 说明 |
|------|------|
| `engineering` | 工程研发 |
| `design` | 设计创意 |
| `manufacturing` | 制造业 |
| `ecommerce` | 商业运营 |
| `product` | 产品应用 |
| `creative` | 创意增强 |
| `content-creation` | 宣发内容 |
| `research` | 学术研究 |
| `data` | 数据分析 |
| `operations` | 运维管理 |

---

## 校验规则（skillctl validate 检查项）

### 必须字段（缺失即失败）
- [ ] `skill_id`：存在、非空、全局唯一（Registry 内查重）、kebab-case
- [ ] `name`：存在、非空、中文
- [ ] `version`：存在、符合语义化版本规范（MAJOR.MINOR.PATCH）
- [ ] `status`：存在、值在状态机枚举内
- [ ] `owner`：存在、非空
- [ ] `risk_level`：存在、值为 low/medium/high
- [ ] `description`：存在、非空、字符数 ≥ 20
- [ ] `trigger`：存在、至少包含 keywords 或 intent 之一
- [ ] `SKILL.md`：同目录下必须存在

### 建议字段（缺失警告，不失败）
- [ ] `created_at` / `updated_at`：日期格式 YYYY-MM-DD
- [ ] `category`：值在分类表内
- [ ] `type`：值为 prompt/workflow/tool/hybrid
- [ ] `input_schema`：有 required 字段列表
- [ ] `output_schema`：有 type 字段
- [ ] `eval`：production/canary 状态必须存在
- [ ] `dependencies`：如有 tools，检查是否声明
- [ ] `changelog`：文件路径是否存在

### 结构检查
- [ ] 文件名：`skill.yaml`（小写，无后缀变体）
- [ ] 格式：合法 YAML，可被解析
- [ ] 编码：UTF-8

---

## 示例：完整 skill.yaml

```yaml
skill_id: "content-monetization-pipeline"
name: "内容变现分发管线"
version: "1.0.0"
status: "production"

owner: "LinkmasterLing"
risk_level: "medium"
created_at: "2026-05-18"
updated_at: "2026-05-18"

description: >
  将已生产的内容资产（视频/图文）转化为可分发、可追踪、可变现的全链路方案。
  支持多平台格式转换、发布排期、ROI 追踪和矩阵放大策略。

category: "content-creation"
type: "hybrid"

trigger:
  keywords:
    - "内容分发"
    - "变现"
    - "多平台发布"
    - "ROI 追踪"
  intent:
    - "content_distribution"
    - "monetization_strategy"
  min_confidence: 0.75

input_schema:
  required:
    - content_asset
    - target_platforms
  optional:
    - monetization_model
    - budget
    - schedule

output_schema:
  type: "markdown"
  additional_files:
    - "manifest.json"
    - "tracking_template.yaml"

dependencies:
  models:
    - "kimi-coding/k2.6"
  tools:
    - "ffmpeg"
  skills:
    - "product-promo-video-maker"

eval:
  suite_id: "content-monetization-eval-v1"
  min_score: 85
  format_pass_rate: 0.98
  regression_pass_rate: 0.95

release:
  strategy: "canary"
  canary_steps: [10, 50, 100]
  rollback_version: "0.9.0"

changelog: "changelog.md"
```

---

## 版本升级规则

| 变更类型 | 版本号变化 | 是否需要重新 eval |
|---------|-----------|-----------------|
| 修复 typo、补充文档 | patch +1 | 否（可选 smoke test） |
| 新增功能、调整链路 | minor +1 | ✅ 是 |
| 重构架构、更换模型 | major +1 | ✅ 是（全量回归） |
| 变更 input/output schema | major +1 | ✅ 是（全量回归） |
| 新增/删除依赖 | minor/major | ✅ 是 |

---

**规范版本：v1.0**
**生效日期：2026-05-18**
