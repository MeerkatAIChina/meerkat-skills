# Looker Studio — 把数据炼成决策引擎

> **你花 80% 的时间做报表，还是花 80% 的时间看报表做决策？**

---

## 为什么要专门为一个 BI 工具建技能？

Looker Studio（原 Google Data Studio）看起来很简单：拖拽图表、连上数据源、调调颜色——半小时就能出个仪表盘。但"能看"和"能用"之间隔着一整套设计思维：

- 为什么大多数营销仪表盘沦为"僵尸报表"？（没人打开，打开也看不懂）
- KPI 到底是放 15 个还是 3 个？
- 面对老板和面对执行团队，同一个仪表盘该怎么设计不同视图？
- 渠道分组是用默认的 GA4 分组，还是自己写 CASE 语句做自定义归并？

这个技能从**仪表盘架构**到**公式编写**到**自动化推送**，覆盖 Looker Studio 从入门到精通的完整链路。

---

## 核心交付能力

### 📐 仪表盘架构设计

按受众分层设计三套视图：

| 受众 | 核心特征 | 刷新频率 |
|------|----------|----------|
| **高管视图** | 3-5 个 KPI 记分卡 + 趋势线 + 一句话洞察 | 每周 |
| **经理视图** | 渠道拆分 + 周期对比 + 预算进度 | 每日 |
| **执行视图** | 广告组级 / 关键词级 / 着陆页级明细 | 实时 |

### 📊 模板库（开箱即用）

这个技能内置了多套经过验证的仪表盘模板结构：

- **营销绩效仪表盘**：5 页，覆盖高管总览 → 付费媒体深挖 → SEO → 邮件 CRM → 转化漏斗
- **电商仪表盘**：营收概览 + 客户获取（CAC / LTV：CAC / 首单归因）
- **SEO 仪表盘**：Search Console 数据驱动，点击/展现/CTR/排名 + Top 查询 + 页面级表现
- **DTC CRM 仪表盘**：Klaviyo 数据驱动的邮件 & 短信效果、Flow vs Campaign 对比、生命周期分层
- **收入归因仪表盘**：Klaviyo 归因 vs Shopify 实际营收核对，追踪归因缺口

### 🧮 计算字段配方库

```looker-studio
// 自定义渠道分组（替代 GA4 默认分组）
CASE
  WHEN REGEXP_MATCH(source_medium, "google.*cpc") THEN "Google Ads"
  WHEN REGEXP_MATCH(source_medium, "facebook|meta") THEN "Meta Ads"
  WHEN REGEXP_MATCH(source_medium, "email|klaviyo") THEN "Email"
  ELSE "Other"
END

// 周期对比
CASE
  WHEN date >= DATE_DIFF(TODAY(), INTERVAL 30 DAY) THEN "本期"
  WHEN date >= DATE_DIFF(TODAY(), INTERVAL 60 DAY) THEN "上期"
  ELSE "更早"
END
```

> ⚠️ 关键规则：Looker Studio **不支持公式注释**（`--`、`//`、`/* */` 都会报错）。用字段描述写文档。

### 🎨 图表选择决策树

| 数据特征 | 首选图表 | 避免 |
|----------|----------|------|
| KPI + 对比 | 记分卡 + 增量箭头 | 饼图 |
| 趋势 | 折线图 / 面积图 | 柱状图（>7 个周期） |
| 分类对比 | 横向柱状图 | 3D 图表 |
| 占比 | 堆叠柱状图 / 环形图 | 饼图（>6 个切片） |
| 地理位置 | 地理热力图 | 表格 |

### 🔌 数据源连接

- **免费原生连接器**：GA4、Google Ads、Search Console、BigQuery、Google Sheets
- **GSheets 免费管道**：通过 Python 脚本将 Klaviyo / Shopify 数据同步到 Google Sheets → Looker Studio 直接连接，**无需付费三方连接器**

### 📬 自动化推送

- 定时 PDF 邮件推送（每日/每周/每月）
- 嵌入到网页/门户
- 模板化复制用于多客户交付

---

## 谁最需要这个技能？

- **效果营销经理**：需要一份同时给老板看和给自己优化用的仪表盘
- **代理机构交付负责人**：需为客户快速搭建标准化报表体系
- **DTC 电商运营**：Klaviyo + Shopify + GA4 三源合一，看清归因
- **SEO 团队**：Search Console 数据可视化，而非在原生后台翻来翻去

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
