---
name: market-research
description: "Generate comprehensive market research reports (50+ pages) in the style of top consulting firms (McKinsey, BCG, Gartner). Professional LaTeX formatting, strategic analysis frameworks (Porter's Five Forces, PESTLE, SWOT, TAM/SAM/SOM, BCG Matrix), and deep research integration."
version: "1.0.0"
license: MIT
origin: custom
author: Rebecca Rae Barton
author_url: https://github.com/thatrebeccarae
metadata:
  version: "1.0.0"
  category: strategy
  domain: research
  updated: 2026-03-13
  tested: 2026-03-17
  tested_with: "Claude Code v2.1"
  hermes:
    tags: [market-research, consulting, strategy, competitive-analysis, industry-report]
    related_skills: [competitor-profiling, customer-research, icp-research, positioning-basics, research-digest]
---

# Market Research

Consulting-grade market research reports with professional formatting and strategic analysis frameworks.

## Install

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git && cp -r claude-marketing/skills/market-research ~/.claude/skills/
```

## Core Capabilities

- **Porter's Five Forces** — competitive intensity analysis
- **PESTLE Analysis** — macro-environmental scanning
- **SWOT Analysis** — strengths, weaknesses, opportunities, threats
- **TAM/SAM/SOM** — market sizing
- **BCG Matrix** — portfolio positioning
- **Value Chain Analysis** — margin and efficiency mapping
- **Competitive Positioning Maps** — quadrant-based competitor mapping

## Report Structure

| Chapter | Content |
|---------|---------|
| 1. Executive Summary | Key findings, market size, growth rate, top recommendations |
| 2. Market Overview | Definition, scope, segmentation, history |
| 3. Market Size & Growth | TAM/SAM/SOM, CAGR, revenue forecasts |
| 4. Industry Dynamics | Porter's Five Forces assessment |
| 5. Competitive Landscape | Player profiles, market share, positioning map |
| 6. Customer Analysis | Segments, behavior, needs, trends |
| 7. Technology & Innovation | Emerging tech, disruption risk, adoption curves |
| 8. Regulatory & Macro | PESTLE analysis, compliance landscape |
| 9. Opportunities & Threats | SWOT synthesis, scenario analysis |
| 10. Strategic Recommendations | Prioritized actions, implementation roadmap |
| 11. Appendices | Data tables, methodology, bibliography |

## Workflow

### Phase 1: Research
- Define market boundaries and scope
- Deep web research for market data, reports, earnings calls
- Collect data points: market size, growth rates, player revenue, funding
- Identify 5-10 key competitors with detailed profiles
- Gather regulatory and macroeconomic data

### Phase 2: Analysis
- Apply each framework to the collected data
- Cross-reference findings across frameworks
- Identify convergent themes and contradictions
- Build scenario models (base, optimistic, pessimistic)
- Score opportunities by attractiveness and feasibility

### Phase 3: Visual Generation
- Market growth charts and TAM/SAM/SOM diagrams
- Competitive positioning maps (2x2 quadrants)
- Porter's Five Forces radar chart
- Risk heatmaps
- Industry ecosystem maps

### Phase 4: Writing
- Structured prose in consulting style (not bullets)
- Every claim backed by data with source citation
- Key insight callout boxes throughout
- Executive summary written last (distilled from findings)

### Phase 5: Compilation
- LaTeX formatting with custom style package
- Table of contents, bibliography, appendices
- PDF generation via LaTeX compiler

## Output Format

Professional LaTeX with custom environments:
- **Key Insight boxes** — highlighted findings
- **Market Data callouts** — statistics with source
- **Risk boxes** — threats with severity rating
- **Recommendation boxes** — prioritized actions
- **SWOT boxes** — four-quadrant analysis
- **Porter's Five Forces boxes** — force-by-force assessment
- **Pull quotes** — notable expert opinions
- **Stat boxes** — large-format key numbers

## 中国市场适配

### 中国数据源
- **艾瑞咨询 (iResearch)** — 互联网及新经济行业研究
- **易观 (Analysys)** — 数字经济与行业数字化分析
- **QuestMobile** — 移动互联网用户行为数据
- **国家统计局** — 宏观经济与行业官方统计数据
- **中国互联网络信息中心 (CNNIC)** — 互联网发展统计报告
- **36氪研究院** — 新兴行业与创业生态研究

### 监管框架
- **网络安全法** — 对在线数据收集与跨境传输的要求
- **数据安全法** — 数据分类分级保护制度
- **个人信息保护法 (PIPL)** — 对市场调研中消费者数据收集的严格限制，需确保合规获取用户数据

### 中国特有分析维度
- **政策环境分析 (Policy)** — 替代PESTLE中的Political，重点关注：
  - 五年规划（如"十四五"规划）对目标产业的政策导向
  - 产业政策（补贴、税收优惠、准入限制）
  - 双循环战略对内外需市场的影响
  - 反垄断与平台经济监管动态

### 本地化报告格式
- 中国市场研究报告偏好**图表密集型**呈现，数据可视化比重应高于欧美报告
- Executive Summary需包含**政策风险提示**，这是中国客户特别关注的环节
- 市场预测建议提供基准、乐观、悲观三情景分析

### 合规注意事项
- 涉及上市公司的市场分析需注明"**不构成投资建议**"
- 引用中国数据源必须标注**来源机构和发布日期**
- 涉及外资准入限制行业（如金融、媒体、电信）需标注相关政策依据
- 地图类可视化需使用审图号合规的中国标准地图

## Quality Standards

1. **Every claim needs a source.** No unsourced statistics.
2. **Recency matters.** Prefer data from the last 2 years.
3. **Triangulate.** Cross-reference market sizes across 3+ sources.
4. **Acknowledge uncertainty.** Use ranges, not false precision.
5. **Actionable recommendations.** Each recommendation has: what, why, how, expected impact.
6. **No filler.** Every paragraph must add information or insight.

For analysis templates, LaTeX formatting, and data patterns, see [REFERENCE.md](REFERENCE.md).
