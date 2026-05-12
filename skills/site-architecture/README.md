# Site Architecture — 你网站的结构混乱，用户迷路了，搜索引擎也迷路了

> **你的产品很好、内容也好，但用户在你的网站里找了 3 分钟找不到想要的东西。不是内容不够——是导航和层级背叛了你的内容。**

---

## 一、好内容放错了位置 = 不存在

网站架构是最被低估的 SEO 战术。为什么？因为它太"基础"了，基础到大家默认"我们已经有导航了啊"。但问问你的数据：有多少人从首页开始，翻了三层菜单才找到目标页？有多少核心转化页，在整站中没有一条内链指向它？

`site-architecture` 不帮你写代码，不帮你做设计。它帮你做一件事：**画清楚你的网站应该长什么样**。页面的父子关系、导航的层级、URL 的命名规则、内链的流通路径——这些事情想清楚了，用户找得到、搜索引擎爬得到。

---

## 二、先搞清楚：这个 Skill 不是什么

| ❌ 不是 | ✅ 正确选择 |
|---------|------------|
| 网站开发/实现 | 它是信息架构设计 → 开发团队按设计实现 |
| XML Sitemap 生成 | XML Sitemap 是技术 SEO 范畴 → 用 `seo-audit` |
| UI/UX 视觉设计 | 它关注的是信息层级和导航逻辑，不是视觉 |
| 只给建议不给结构 | 输出 ASCII 树状图 + Mermaid 可视化 + URL 映射表 |
| 内容策略 | 架构是页面之间的关系 → 写什么内容 → 用 `content-strategy` |

---

## 三、真实场景演示

**场景**：一个 SaaS 做了三年，网站从 20 页长到 200 页，结构完全失控。产品页、博客、文档混在一起，用户抱怨"找不到定价页"。

**`site-architecture` 会怎么做？**

```
Step 1: 诊断当前结构
→ 提取当前 URL 结构 → 发现 4 种不一致的 URL 模式：
  /product/analytics
  /features/automation
  /solutions/enterprise
  /enterprise-plan
→ 产品功能分散在 3 个不同父级下，用户找不到完整功能列表

Step 2: 重构方案
ASCII 树状图：
  Home (/)
  ├── Product (/product)
  │   ├── Features (/product/features)
  │   │   ├── Analytics (/product/features/analytics)
  │   │   ├── Automation (/product/features/automation)
  │   │   └── Integrations (/product/features/integrations)
  │   └── Pricing (/product/pricing)
  ├── Solutions (/solutions)
  │   ├── Enterprise (/solutions/enterprise)
  │   └── Small Business (/solutions/small-business)
  ├── Blog (/blog)
  │   └── [Category] (/blog/category/slug)
  ├── Docs (/docs)
  └── About (/about)

Step 3: 导航规范
  Header: Product | Solutions | Blog | Docs | Pricing | CTA
  Footer: Product列 / Resources列 / Company列 / Legal列

Step 4: 内链策略
→ Pricing 页：每条功能描述链接到对应 Features 页
→ Blog 文章：涉及产品功能时链接到 Features 页
→ Case Study：链接到对应 Solutions 页

Step 5: 301 重定向映射
→ /features/automation → /product/features/automation
→ /enterprise-plan → /solutions/enterprise
→ ...共 27 条重定向
```

---

## 四、核心能力矩阵

| 能力 | 输出 |
|------|------|
| **页面层级设计** | ASCII 树状图，标注层级、URL、优先级 |
| **导航设计** | Header/Footer/Sidebar/Breadcrumb 规范 |
| **URL 结构规范** | 命名规则、层级对应、反模式警告 |
| **可视化站点地图** | Mermaid 图（带导航分区标注） |
| **内链架构** | Hub & Spoke 模型 + 孤岛页面排查 |
| **重定向映射** | 旧 URL → 新 URL 的 301 映射表 |
| **站点类型模板** | SaaS / 电商 / 内容 / 文档 / 混合型模板 |

---

## 五、谁应该用

- ✅ **新站策划**：从零开始，第一件事不是设计首页，是画清楚结构
- ✅ **网站改版**：旧站结构混乱 → 重构层级和导航
- ✅ **SEO 负责人**：搜索引擎爬不到深层页面 → 优化信息架构
- ✅ **产品/市场团队**：页面越来越多，需要一个"总图"来管理

---

## 六、简单上手步骤

```bash
cp -r skills/site-architecture ~/.claude/skills/
```

触发方式：
> "帮我规划一个 SaaS 营销网站的信息架构"
> "我们的网站结构很乱，帮我重新设计导航和页面层级"
> "画一个我们网站的可视化站点地图"

Agent 会先了解你的站点类型、页面数量、核心页面，然后输出完整的架构方案。

---

## 七、配合使用

| 配合 Skill | 为什么 |
|-----------|--------|
| `seo-audit` | 先审计发现架构问题 → 用本 Skill 重建设计 |
| `technical-seo-audit` | 架构设计完成后 → 验证爬取深度和内链健康 |
| `programmatic-seo` | pSEO 页面需要严密的架构来做内链和爬取管理 |
| `content-strategy` | 架构定义了"框架" → 内容策略填充"内容" |
| `page-cro` | 架构设计完成后 → 单页面的转化优化 |

---

> **用户在你的网站上迷路，其实只有两种可能：要么你根本没想过他们要去哪，要么你把路标藏起来了。好架构把这两种可能都消灭掉。**

> 猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用
