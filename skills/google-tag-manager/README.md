# Google Tag Manager — 容器治理与埋点工程化

> **GTM 不是"那个套代码的盒子"，而是数据质量的守门人。**

---

## 你有多久没审计过你的 GTM 容器了？

打开一个运行了两年的 GTM 容器，你大概率会看到：

- 10 个已暂停但从没清理的旧标签
- 3 个重复的 GA4 配置标签（同一个测量 ID 配了三次）
- 一个自定义 HTML 标签里有 200 行 jQuery，没人敢动
- 转化标签挂在 "All Pages" 触发器上，每条 URL 都在烧归因数据

GTM 是"上线容易治理难"的典型。部署一个新标签只需要 5 分钟，但治理烂掉的容器可能需要 5 天。这个技能就是你的**GTM 容器治理武器库**。

---

## 核心能力全景

### 🔍 容器全量审计（8 步法）

从转化标签验证 → 标签清单 → 触发器审查 → 变量审计 → 文件夹组织 → 命名规范评估 → Consent Mode 检查 → 优先级推荐——每一步都输出问题清单 + 修复方案 + 影响/工作量评级。

### 🏗️ 标签架构设计

覆盖所有主流标签类型的最佳实践：

| 标签类型 | GTM 缩写 | 核心规则 |
|----------|----------|----------|
| GA4 配置 | `gaawc` | 每个域名一个，测量 ID 用常量变量 |
| GA4 事件 | `gaawe` | 引用配置标签，参数走数据层变量 |
| Google Ads 转化 | — | 转化 ID + 标签 + 去重 ID，禁止 All Pages |
| Meta Pixel | — | 优先用社区模板，不写 Custom HTML |
| 自定义 HTML | — | **仅当无模板可用时才使用** |

### 🎯 触发器设计原则

触发器选型是数据质量的第一道防线：

- **页面加载型**（Page View / DOM Ready / Window Loaded）→ 需要 DOM 的分析标签
- **自定义事件型** → 数据层事件，精确匹配事件名
- **Consent Initialization** → 必须最先触发，在一切测量标签之前
- **绝对禁止**：用 All Pages 触发转化/再营销标签

### 🔐 Consent Mode v2 实施

四个核心参数（`analytics_storage` / `ad_storage` / `ad_user_data` / `ad_personalization`）的配置逻辑，高级模式 vs 基础模式的选择，以及与 CookieBot / OneTrust 等 CMP 的集成顺序——初始化顺序错误意味着整个同意管理失效。

### 🖥️ 服务器端 GTM（sGTM）决策指南

什么时候值得从浏览器端迁移到服务器端？核心决策因子：广告拦截器数据损失率、Meta CAPI 需求、隐私合规压力、每月 $30-50 的 GCP 费用和技术团队的运维能力。

### 🐛 调试三板斧

- **Preview Mode + Tag Assistant**：事件时间线 + 标签触发状态 + 变量值
- **浏览器 Console**：`window.dataLayer` 快照检查
- **Network Tab**：GA4 collect 请求参数验证，`gcs` 参数检查同意状态

---

## 八条硬规则

这个技能在每一次建议中都会严格执行以下红线：

1. 🚫 **有数据层就绝不推荐 DOM 抓取**——dataLayer 是前后端的合约
2. 🚫 **转化/再营销标签绝不允许挂 All Pages 触发器**
3. 🚫 **有社区模板就绝不推荐 Custom HTML**
4. ✅ **Consent Mode 默认值必须在测量标签之前触发**
5. ✅ **测量 ID / 转化 ID / API Key 必须走常量变量，禁止硬编码**
6. ✅ **已废弃的 UA 标签必须清理**
7. ✅ **每次 ecommerce push 前必须清空上一次数据**
8. ✅ **一个变更集一个工作区，永远不在默认工作区操作**

---

## 与 AGENTS.md 生态联动

- **Google Analytics 技能** → GTM 负责把标签发好，GA 技能负责分析到达的数据
- **GTM Implementer Agent** → 这个技能是诊断层/规划层，Agent 是 API 执行层
- **Analytics Tracking 技能** → 追踪方案规划，GTM 负责落地

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
