# 分析框架参考文档

## 可用框架

### 1. manufacturing-ai-efficiency-pro（默认）

适用于 B2B 工业产品、硬件设备、行业解决方案。

**9 步分析流程**:
1. 输入锚定 — 场景名称、业务目标、痛点、角色、约束
2. 三维框架锚定 — APQC + 价值链 + 5M1E
3. 第一层流程拆解 — 3-7 个核心子流程
4. 第二层最小单元 — 5M1E 动作簇拆解
5. AI 提效分级 — Level A/B/C 评估
6. 机会整合 — 3-5 个机会点
7. 人机权责划分 — T34 模型
8. 知识库校准 — 六大目录
9. 闭环迭代 — 短/中/长期路线图

**机会卡片输出 Schema**:
```json
{
  "opportunities": [
    {
      "id": "OP-01",
      "title": "卖点名称",
      "priority": "P0|P1|P2",
      "icon": "emoji",
      "business_goal": "业务目标",
      "pain_point": "现状痛点",
      "entry_action": "切入动作",
      "solution": "方案",
      "data_support": "数据支撑",
      "expected_benefit": "预期收益",
      "difficulty": "落地难点",
      "system_target": "系统落点"
    }
  ]
}
```

**痛点对比输出**:
```json
{
  "painpoint_comparison": {
    "before_label": "传统方案",
    "after_label": "产品名称",
    "before_list": ["痛点1", "痛点2", ...],
    "after_list": ["解决1", "解决2", ...],
    "metrics": [
      { "value": "3×", "label": "效率提升" }
    ]
  }
}
```

### 2. saas-value-proposition

适用于 SaaS、软件、在线服务产品。

**分析维度**:
- 用户痛点 → 功能解法
- 使用场景 → 价值量化
- 竞品差异 → 独特卖点
- 定价锚点 → ROI 计算

**输出 Schema**:
```json
{
  "value_proposition": {
    "headline": "一句话价值主张",
    "subheadline": "补充说明",
    "for_who": "目标用户画像",
    "who_struggle": "用户痛点",
    "our_solution": "我们的解法",
    "unlike": "与竞品不同",
    "benefits": [
      { "metric": "效率提升 300%", "detail": "具体说明" }
    ]
  }
}
```

### 3. consumer-product-appeal

适用于 C 端消费品、智能硬件、生活方式产品。

**分析维度**:
- 感官卖点 — 外观、材质、手感
- 功能卖点 — 核心能力、使用场景
- 情感卖点 — 品牌调性、身份认同
- 社交卖点 — 分享价值、话题性

**输出 Schema**:
```json
{
  "appeal_layers": {
    "sensory": ["卖点1", "卖点2"],
    "functional": ["卖点1", "卖点2"],
    "emotional": ["卖点1", "卖点2"],
    "social": ["卖点1", "卖点2"]
  }
}
```

### 4. custom

用户提供自定义分析维度和输出格式。

**要求**: 用户必须提供:
- 分析维度列表
- 每个维度的字段定义
- 输出 JSON Schema

---

## 框架选择指南

| 产品类型 | 推荐框架 |
|---------|---------|
| 工业设备、无人机、机器人 | `manufacturing-ai-efficiency-pro` |
| SaaS、软件、平台 | `saas-value-proposition` |
| 消费品、智能硬件 | `consumer-product-appeal` |
| 其他 | `custom` |

## LLM 提示词模板

### Manufacturing AI Efficiency Pro 提示词

```
你是一个 Manufacturing AI Efficiency Pro 分析专家。
请对以下产品进行深度拆解，从动作级最小单元识别 AI 落地机会。

产品信息:
{{product_data}}

请按以下格式输出：
1. 九步分析框架概述
2. 7 个机会点（按 P0/P1/P2 分级），每个包含：业务目标、现状痛点、切入动作、方案、数据支撑、预期收益、落地难点、系统落点
3. 前后对比（传统方案 vs 该产品）
4. 价值链定位
5. 量化收益指标

输出必须严格符合以下 JSON Schema:
{{schema}}
```

### SaaS Value Proposition 提示词

```
你是一个 SaaS 产品价值主张专家。
请为以下产品提炼核心价值主张和差异化卖点。

产品信息:
{{product_data}}

输出 JSON 格式:
{{schema}}
```

### Consumer Product Appeal 提示词

```
你是一个消费品卖点提炼专家。
请从感官、功能、情感、社交四个层面分析以下产品。

产品信息:
{{product_data}}

输出 JSON 格式:
{{schema}}
```
