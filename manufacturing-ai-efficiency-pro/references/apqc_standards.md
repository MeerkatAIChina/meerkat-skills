# APQC 制造业流程分类框架

## 目的与使用方式
本文件用于将制造业场景快速映射到 APQC（American Productivity & Quality Center）流程分类框架，为 AI 提效分析提供标准化的流程归类依据。

**核心原则**：
- 优先按"业务目的"归类，而不是按部门名称归类
- 如果同一场景横跨多个流程，输出主分类和次分类
- 如果用户使用企业内部术语，先保留原术语，再补 APQC 标准术语
- 如果无法精确到二级分类，至少给出一级分类并说明判断依据

---

## APQC 流程分类框架（PCF）概览

### 制造业相关一级分类（13 类）

| 编号 | 一级分类 | 说明 | 制造业典型场景 |
|------|----------|------|----------------|
| 1.0 | Develop Vision and Strategy | 战略、经营规划、能力布局 | 制造战略、产能规划、数字化路线图 |
| 2.0 | Develop and Manage Products and Services | 产品研发、工艺开发、变更管理 | 产品设计、试产导入、工艺优化 |
| 3.0 | Market and Sell Products and Services | 市场、销售、报价、订单获取 | 客户开发、报价管理、订单承接 |
| 4.0 | Deliver Physical Products | 采购、计划、生产、物流、交付 | 供应链、排产、制造执行、仓储配送 |
| 5.0 | Deliver Services | 交付后的服务履约 | 安装、维保、驻场支持 |
| 6.0 | Manage Customer Service | 客诉、售后响应、服务闭环 | 客诉处理、退换维修、质量追踪 |
| 7.0 | Develop and Manage Human Capital | 组织与人才管理 | 班组培训、技能矩阵、岗位胜任力 |
| 8.0 | Manage Information Technology | IT 系统建设与治理 | ERP、MES、WMS、QMS、数据平台 |
| 9.0 | Manage Financial Resources | 财务预算、成本、核算 | 制造成本、预算控制、绩效核算 |
| 10.0 | Acquire, Construct, and Manage Assets | 设备、厂房、资产管理 | 设备维护、产线改造、固定资产 |
| 11.0 | Manage Enterprise Risk, Compliance, and Resiliency | 风险、合规、安全、韧性 | EHS、质量合规、供应风险 |
| 12.0 | Manage External Relationships | 外部合作与监管关系 | 供应商、客户、政府、审厂 |
| 13.0 | Develop and Manage Business Capabilities | 能力体系与业务改进 | 流程再造、精益改善、数智化能力 |

---

## 制造业高频二级分类映射

### 4.0 Deliver Physical Products（生产制造）- 最常用

| 二级分类 | 说明 | 典型场景 | AI 提效机会示例 |
|----------|------|----------|----------------|
| 4.1 | Develop Production and Materials Planning | 生产与物料计划 | 需求预测、S&OP、主生产计划、物料需求计划 | 需求预测模型、计划自动排程 |
| 4.2 | Perform Production Operations | 生产作业执行 | 工单下达、工序执行、装配、测试、包装 | 作业指导、异常预警、质量判定辅助 |
| 4.3 | Monitor and Control Production | 生产监控与控制 | 生产进度监控、异常处置、绩效分析 | 实时监控、异常分诊、绩效自动统计 |
| 4.4 | Manage Inventory and Warehousing | 库存与仓储管理 | 入库、出库、盘点、配送、库存控制 | 库存优化、智能拣选、AGV 调度 |
| 4.5 | Manage Quality | 质量管理 | 来料检验、过程检验、终检、质量分析 | 视觉检测、质量预测、根因分析 |

### 2.0 Develop and Manage Products and Services（产品研发）

| 二级分类 | 说明 | 典型场景 | AI 提效机会示例 |
|----------|------|----------|----------------|
| 2.1 | Develop Product and Service Strategy | 产品服务战略 | 产品规划、技术路线、组合管理 | 市场趋势分析、竞品分析 |
| 2.2 | Design Products and Services | 产品设计 | 详细设计、DFMEA、设计验证 | 设计规则校验、相似方案推荐 |
| 2.3 | Manage Product and Service Portfolio | 产品组合管理 | 生命周期管理、变更管理 | 变更影响分析、版本管理 |
| 2.4 | Develop and Industrialize Manufacturing Processes | 工艺开发与导入 | 工艺设计、试产、工艺验证 | 工艺参数优化、试产数据分析 |

### 10.0 Acquire, Construct, and Manage Assets（设备资产）

| 二级分类 | 说明 | 典型场景 | AI 提效机会示例 |
|----------|------|----------|----------------|
| 10.1 | Develop Asset Management Strategy | 资产管理战略 | 资产规划、投资决策 | 投资回报分析、产能规划 |
| 10.2 | Acquire and Construct Assets | 资产购置与建设 | 设备采购、安装调试、验收 | 供应商评估、安装进度监控 |
| 10.3 | Maintain and Manage Assets | 资产维护管理 | 点检、保养、维修、改造 | 预测性维护、维修工单自动分派 |
| 10.4 | Decommission and Dispose Assets | 资产退役处置 | 报废、处置、更新 | 报废评估、更新建议 |

### 6.0 Manage Customer Service（客户服务）

| 二级分类 | 说明 | 典型场景 | AI 提效机会示例 |
|----------|------|----------|----------------|
| 6.1 | Develop Customer Service Strategy | 客户服务战略 | 服务策略、服务网络规划 | 服务需求预测、网络优化 |
| 6.2 | Manage Customer Service Operations | 客户服务运营 | 服务请求处理、投诉处理 | 自动分类、根因推荐、CAPA 生成 |
| 6.3 | Manage Customer Complaints | 客户投诉管理 | 投诉受理、调查、8D 报告 | 投诉分诊、8D 报告辅助生成 |
| 6.4 | Manage Warranty and Returns | 保修与退货管理 | 保修索赔、退货处理 | 保修欺诈检测、退货分析 |

---

## 典型场景快速映射表

| 典型场景 | 主分类 | 次分类 | 判断依据 |
|----------|--------|--------|----------|
| 研发立项、样机试制、BOM 变更 | 2.0 | 2.4 | 核心目标是工艺开发与导入 |
| 需求预测、S&OP、主生产计划 | 4.0 | 4.1 | 核心目标是生产与物料计划 |
| 生产排程、工单下达、工序执行 | 4.0 | 4.2 | 核心目标是生产作业执行 |
| 设备点检、保养、维修协同 | 10.0 | 10.3 | 核心目标是资产维护管理 |
| 质量检验、异常分析、8D 闭环 | 4.0 | 4.5 | 核心目标是生产质量管理 |
| 仓储、配送、发运、追溯 | 4.0 | 4.4 | 核心目标是库存与仓储管理 |
| 客诉、售后、现场服务 | 6.0 | 6.2/6.3 | 核心目标是客户服务运营 |
| 培训、技能认证、班组能力建设 | 7.0 | - | 核心目标是人力资本发展 |
| MES、ERP、QMS 功能优化 | 8.0 | - | 核心目标是 IT 系统管理 |
| 采购寻源、供应商交付、来料质量 | 4.0 | 4.1/4.5 | 涉及物料计划和来料质量 |
| 安全环保、EHS 管理 | 11.0 | - | 核心目标是企业风险管理 |
| 成本核算、预算控制 | 9.0 | - | 核心目标是财务管理 |

---

## 输出格式规范

### 标准输出模板

```markdown
- **APQC 分类**：[一级分类编号] [一级分类名称] / [二级分类编号] [二级分类名称]
- **判断依据**：[1-2 句话说明归类理由]
- **关联分类**（如有）：[次分类编号及名称]
- **企业术语映射**：[企业内部术语] = [APQC 标准术语]
```

### 示例输出

**示例 1：镀膜工艺监控场景**
```markdown
- **APQC 分类**：4.0 Deliver Physical Products / 4.3 Monitor and Control Production
- **判断依据**：场景核心目标是监控镀膜工艺参数、识别异常并预警，属于生产过程的监控与控制
- **关联分类**：4.5 Manage Quality（涉及工艺质量判定）
- **企业术语映射**：镀膜 = Coating / 薄膜沉积工艺
```

**示例 2：装配首件确认场景**
```markdown
- **APQC 分类**：4.0 Deliver Physical Products / 4.2 Perform Production Operations
- **判断依据**：场景核心目标是换型后首件质量确认并放行，属于生产作业执行环节
- **关联分类**：4.5 Manage Quality（涉及首件检验）
- **企业术语映射**：首件确认 = First Article Inspection / FAI
```

**示例 3：客户投诉追溯场景**
```markdown
- **APQC 分类**：6.0 Manage Customer Service / 6.3 Manage Customer Complaints
- **判断依据**：场景核心目标是快速追溯客户投诉产品全流程信息并定位根因，属于客户投诉管理
- **关联分类**：4.5 Manage Quality（涉及质量追溯）、4.3 Monitor and Control Production（涉及生产数据）
- **企业术语映射**：追溯 = Traceability / 全流程追溯
```

---

## 与 SKILL.md 的集成规则

### 在报告中的落点
1. **场景定位章节**：必须明确 APQC 主次分类
2. **流程图节点**：每个子流程节点必须标注 APQC 标签（如 APQC:4.3.1）
3. **机会卡**：每个 AI 机会点必须关联 APQC 分类

### 读取时机
- 涉及 APQC 分类时读取本文件
- 需要标准化流程术语时读取本文件
- 需要判断流程归属时读取本文件

### 与其他 References 的协同
- 与 `manufacturing_value_chain.md` 协同：APQC 提供标准分类，价值链提供研产供销服定位
- 与 `ie_analysis_toolkit.md` 协同：APQC 用于流程归类，IE 工具用于动作拆解
- 与 `standards_and_maturity_framework.md` 协同：APQC 用于流程定位，标准体系用于合规约束

---

## 注意事项

### 常见误区
1. **按部门归类**：错误地将生产部门的所有场景都归为 4.0，应看业务目的
2. **忽略跨流程**：很多场景横跨多个 APQC 分类，需要标注主分类和次分类
3. **过度细化**：不需要强行归类到三级、四级分类，一到二级即可
4. **术语混淆**：企业术语与 APQC 术语需要映射，不要直接覆盖

### 特殊场景处理
- **横跨多分类**：输出主分类 + 次分类，如"主：4.2，次：4.5"
- **信息不足**：标注"D0 级"，仅给出最可能的一级分类
- **新兴场景**：如 AI 模型训练，可归入 8.0（IT）或 13.0（能力建设）

---

**版本**：V2.0（根据 SKILL.md 迭代更新）  
**最后更新**：2026-04-02  
**维护原则**：随 SKILL.md 迭代而更新，保持术语和分类一致性
