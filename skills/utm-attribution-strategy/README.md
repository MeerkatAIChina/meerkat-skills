# UTM & 归因策略 — 回答"钱花在哪有效"的终极问题

> **UTM 参数只是几个 URL 后缀——但滥用 3 个月后，你的 GA4 会变成垃圾站。**

---

## 归因混乱的代价比你想象的大

打开 GA4 的"流量获取"报告，如果你看到：

- `google` 和 `Google` 和 `google-organic` 被识别为三个不同来源
- `utm_medium=social` 和 `utm_medium=social-media` 和 `utm_medium=`（空值）
- 一条内部链接上不知不觉带了 UTM 参数，把所有会话归因刷新了一遍

那么恭喜——你的数据已经被"UTM 污染"了。修复这些历史数据几乎不可能，唯一的办法是**从现在开始建立规范**。

UTM & Attribution Strategy 技能帮你建立一套**从命名到模型到审计**的完整归因体系，确保每一条营销支出都能追溯到产出。

---

## 核心能力

### 📝 UTM 参数标准化体系

**五个标准参数，一个都不能乱用：**

| 参数 | 职责 | 反面教材 |
|------|------|----------|
| `utm_source` | 流量从哪里来 | `google` vs `Google`（大小写敏感） |
| `utm_medium` | 营销介质 | 写成 `social-media` 而不是 GA4 认可的 `social` |
| `utm_campaign` | 活动名称 | `spring_sale` 和 `spring-sale` 被视为两个活动 |
| `utm_term` | 付费关键词 | 只在搜索广告中使用 |
| `utm_content` | 创意变体区分 | 写成 `cta1` 而不是 `cta-start-trial-hero` |

### 🏷️ 推荐命名规则

```
规则一：全小写。永远。GA4 大小写敏感。
规则二：用连字符 `-` 分隔，不用下划线 `_` 或空格。
规则三：描述要精准但不冗长。
规则四：整条 UTM 字符串中无 PII（姓名、邮箱、账号 ID）。
规则五：内部链接绝对不带 UTM 参数。
```

### 📋 各渠道 UTM 模板速查

| 渠道 | 模板 URL | 备注 |
|------|----------|------|
| Google 搜索广告 | `?utm_source=google&utm_medium=cpc&utm_campaign=xxx&utm_term=xxx` | Google Ads 会同时发送 gclid |
| Meta 广告 | `?utm_source=facebook&utm_medium=paid-social&utm_campaign=xxx&utm_content=xxx` | Meta 会同时发送 fbclid |
| LinkedIn 广告 | `?utm_source=linkedin&utm_medium=paid-social&utm_campaign=xxx&utm_content=xxx` | LinkedIn 需手动配置 |
| 邮件营销 | `?utm_source=newsletter&utm_medium=email&utm_campaign=xxx&utm_content=xxx` | content 可以标记按钮位置 |
| 网红合作 | `?utm_source=influencer-[name]&utm_medium=influencer&utm_campaign=xxx` | 便于区分不同 KOL |

---

### 🧭 归因模型选择决策树

"最后一次点击"不是错——但如果你的销售周期长达 3 个月，它就是在系统性地低估品牌建设和内容营销的价值。

```
销售周期 < 7 天        → 末次点击 / 数据驱动
销售周期 7-30 天       → 位置归因 / 数据驱动
销售周期 > 30 天       → 时间衰减 / 数据驱动
月转化 > 1000 次       → 数据驱动（无脑选）
品牌认知活动            → 首次点击辅助分析
效果营销评估            → 末次点击辅助分析
需要综合视角            → 位置归因（40% 首次 + 40% 末次 + 20% 中间）
```

### 🔍 UTM 审计检查清单（10 项）

- [ ] 所有付费活动都带有 UTM 参数
- [ ] 命名规范已文档化并在团队间共享
- [ ] 无大小写不一致（全部小写）
- [ ] 无空格（使用连字符）
- [ ] `utm_medium` 值与 GA4 默认渠道分组对齐
- [ ] 内部链接无 UTM 参数
- [ ] UTM 参数在落地页 URL 而非跳转后的 URL
- [ ] 无 PII 泄露
- [ ] 短链接/链接缩短器保留了 UTM 参数
- [ ] 302 跳转保留了 UTM 参数

---

## 七大常见错误

1. **内部链接带 UTM** — 最致命的错误，会重置会话归因
2. **命名不一致** — `facebook` / `Facebook` / `fb` 变成三个独立来源
3. **缺少 utm_medium** — 流量落入 GA4 的 `(other)` 分组
4. **非标准 utm_medium 值** — 导致渠道分组失败
5. **自然搜索结果加 UTM** — Google 已自动标记，叠加上去产生重复数据
6. **UTM 里塞 PII** — 违反隐私政策
7. **忘记点击后的跟踪** — UTM 只追踪点击，不追踪点击后发生了什么

---

## 生态联动

| 协同技能 | 关系 |
|----------|------|
| **Google Analytics** | UTM 数据进入 GA4，GA 技能负责分析 |
| **Analytics Tracking** | UTM 策略是整体追踪方案的一部分 |
| **Google Ads / Meta Ads / LinkedIn Ads** | 各广告平台需要手动或自动配置 UTM |

---

*猫鼬AI × 开源社区联合打磨 | Claude Code / Hermes Agent 通用*
