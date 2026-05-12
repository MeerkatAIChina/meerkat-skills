# Schema Markup Generator — 让搜索引擎不光收录你，还"展示"你

> **你排在第一页，但搜索结果里的你只是一条干巴巴的蓝色链接。竞品呢？星星评分、FAQ 折叠、面包屑路径——同样的排名，点击率差了 3 倍。**

---

## 一、排名≠可见度

传统 SEO 让你上了第一页。但第一页有 10 个结果——用户扫一眼，最先点击的不是排第一的那个，是视觉上最突出的那个。什么最突出？**Rich Results**：带评分的、带 FAQ 下拉的、带步骤图的、带价格和库存的。

这些 Rich Results 不是 Google 猜出来的——是你用 **Schema Markup（结构化数据）** 喂给它的。`schema-markup-generator` 让你不用背 Schema.org 的几百个字段和必填规则，只需告诉它：这是什么类型的内容？它直接给你生成可用的 JSON-LD。

---

## 二、先搞清楚：这个 Skill 不是什么

| ❌ 不是 | ✅ 正确选择 |
|---------|------------|
| Schema 策略规划工具 | 它是 Schema 代码生成器 → 策略层面先做审计 |
| 保证 Rich Results | 生成合规 Schema，是否展示由搜索引擎决定 |
| 只管一种类型 | 覆盖 Article/FAQ/HowTo/Product/Review/LocalBusiness/Event/Person/Breadcrumb 等 |
| 替代结构化数据审计 | 审计 → 用 `seo-audit` 或 `technical-seo-audit` |

---

## 三、真实场景演示

**场景**：一个 SaaS 产品帮助中心有 40 篇教程，每篇都是详细的 How-To 内容，但搜索结果里只有普通链接。

**`schema-markup-generator` 会怎么做？**

```
1. 识别内容类型 → HowTo（教程类）

2. 生成 JSON-LD：
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "如何设置自动化工作流",
  "description": "从零搭建你的第一条自动化规则",
  "totalTime": "PT15M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "进入自动化面板",
      "text": "登录后台，点击左侧导航的「自动化」……",
      "image": "https://help.example.com/images/step1.png"
    },
    ...
  ]
}

3. 验证建议 → 贴到 Google Rich Results Test 验证

4. 扩展建议 → 教程页面同时加 Article Schema + BreadcrumbList
```

---

## 四、核心能力矩阵

| Schema 类型 | Rich Result 效果 | 适用场景 |
|------------|-----------------|---------|
| **Article** | 增强列表（作者/日期） | 博客、新闻、指南 |
| **FAQPage** | 可展开 Q&A 在搜索结果 | 帮助中心、产品页 FAQ |
| **HowTo** | 步骤预览在搜索结果 | 教程、操作指南 |
| **Product** | 价格/库存/评分 | 电商产品页 |
| **Review** | 星评分在搜索结果 | 评价页、对比页 |
| **LocalBusiness** | 地图/营业时间/电话 | 本地服务、门店 |
| **BreadcrumbList** | 面包屑路径 | 全站所有页面 |
| **Event** | 日期/地点/票务 | 活动/会议/课程 |
| **Person** | Knowledge Panel | 作者页、创始人页 |
| **Organization** | 品牌 Knowledge Panel | 关于页、公司页 |

**每种 Schema 输出**：完整的 JSON-LD 代码块 + 必填/推荐字段说明 + 验证链接。

---

## 五、谁应该用

- ✅ **内容运营**：写完文章不知道要不要加 Schema，加什么，怎么写
- ✅ **电商运营**：产品页不展示价格和评分 → 加 Product Schema
- ✅ **开发者**：不想背 Schema.org 规范，只需要可用的 JSON-LD
- ✅ **SEO 顾问**：批量交付 Schema 实施代码

---

## 六、简单上手步骤

```bash
cp -r skills/schema-markup-generator ~/.claude/skills/
```

触发方式：
> "给我的博客文章生成 Article Schema"
> "我的产品页需要 Product Schema，包括评分和价格"
> "这篇文章有 FAQ 模块，帮我加 FAQPage Schema"

Agent 会问你页面的具体内容（标题、作者、日期、价格等），然后直接输出 JSON-LD + 插入位置说明。

---

## 七、配合使用

| 配合 Skill | 为什么 |
|-----------|--------|
| `aeo-geo-optimizer` | Schema 是 AI 搜索的核心信号 → 用 AEO 定策略，用本 Skill 实施 |
| `seo-audit` | 审计发现 Schema 缺失 → 直接跳转本 Skill 生成 |
| `technical-seo-audit` | 验证 Schema 是否正确部署 + 无冲突 |
| `seo-content-writer` | 文章结构对齐 Schema 结构（FAQ 标题 = H2） |
| `programmatic-seo` | 大规模页面需要配套的 Schema 模板 |

---

> **第一页是入场券，Rich Result 是 VIP 通道。差 3 行 JSON-LD，点击率能差出一个量级。**

> 猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI
