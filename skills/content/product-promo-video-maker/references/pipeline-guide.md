# Pipeline 执行指南

## 完整执行流程

### 前置检查
1. 确认用户输入了产品信息（URL / 描述 / 文件）
2. 确认目标输出目录可写
3. 加载配置参数（使用默认值填充未指定的参数）

### 阶段执行

#### Stage 1: INGEST
**输入**: 用户提供的原始输入
**操作**:
- 如果输入是 URL:
  - 使用 browser 访问页面
  - 提取页面文本内容（产品名、描述、参数列表）
  - 收集页面中的所有图片 URL（按尺寸排序，保留最大尺寸）
- 如果输入是纯文本描述:
  - 直接保存为 raw_text
- 如果输入是本地文件:
  - 读取文件内容，识别文件类型
  - 如果是图片，记录路径和尺寸

**输出文件**: `01-input/product-info.json`
```json
{
  "input_type": "url|description|files",
  "input_value": "...",
  "product_name": "...",
  "slogan": "...",
  "brand": "...",
  "category": "...",
  "source_url": "...",
  "extracted_at": "...",
  "raw_data": { ... },
  "discovered_images": ["url1", "url2", ...]
}
```

**检查点**: 如果 `01-input/product-info.json` 存在且未过期（<24h），跳过此阶段。

---

#### Stage 2: EXTRACT
**输入**: `01-input/product-info.json`
**操作**:
1. 读取 raw_data
2. 使用 LLM（带 JSON Schema）提取结构化数据
3. 校验 JSON 完整性

**输出文件**: `02-extracted/product-data.json`
```json
{
  "name": "产品名",
  "product_name": "产品全称",
  "slogan": "Slogan",
  "brand": "品牌",
  "category": "类别",
  "core_specs": { "key": "value" },
  "core_specs_highlight": [
    { "key": "参数名", "value": "参数值" }
  ],
  "key_features": [
    { "name": "卖点", "priority": "P0|P1|P2", "icon": "emoji", "image": "配图路径" }
  ],
  "pain_points": { "before": [], "after": [] },
  "scenarios": [],
  "value_chain": [
    { "icon": "emoji", "title": "节点", "desc": "描述" }
  ]
}
```

**关键字段说明**:
- `name` — 模板引擎使用 `{{product.name}}`
- `core_specs_highlight` — Hero 区数据指标展示
- `key_features[].image` — 卖点配图路径

**检查点**: 如果 `02-extracted/product-data.json` 存在且上游未变化，跳过此阶段。

---

#### Stage 3: ANALYZE
**输入**: `02-extracted/product-data.json` + 配置中的 `analysis_framework`
**操作**:
1. 读取 `references/analysis-frameworks.md` 获取对应框架的提示词模板
2. 用 LLM 运行分析，要求输出严格 JSON Schema
3. 校验输出 JSON 是否包含所有必需字段

**输出文件**:
- `03-analysis/opportunities.json` — 机会卡片数组 + 痛点对比 + 流程图 + 框架步骤

**关键输出结构**:
```json
{
  "opportunities": [...],
  "painpoint_comparison": {
    "before_label": "...",
    "after_label": "...",
    "before_list": [...],
    "after_list": [...],
    "metrics": [{ "value": "3×", "label": "..." }]
  },
  "flowchart_mermaid": "graph LR\n...",
  "framework_steps": [
    { "step": "01", "title": "...", "description": "...", "action": "...", "output": "...", "ai_point": "...", "tag": "..." }
  ]
}
```

**检查点**: 如果 `03-analysis/opportunities.json` 存在且上游未变化，跳过此阶段。

---

#### Stage 4: DESIGN
**输入**: `03-analysis/opportunities.json`
**操作**: 生成渲染配置

**输出文件**: `04-design/config.json` + `04-design/images-manifest.json`

`config.json` 示例:
```json
{
  "product_name": "Unitree As2",
  "lang": "zh-CN",
  "page_title": "AI 提效深度分析",
  "source_url": "https://...",
  "analysis_framework": "Manufacturing AI Efficiency Pro",
  "output_sections": ["hero", "framework", "painpoint", "opportunities", "flowchart", "valuechain", "brand"],
  "theme": "robot-theme",
  "framework_title": "九步分析框架",
  "framework_subtitle": "Manufacturing AI Efficiency Pro · 从动作级最小单元识别落地机会",
  "opportunities_title": "核心 AI 落地机会",
  "opportunities_desc": "基于 Manufacturing AI Efficiency Pro 框架的 N 个核心机会点",
  "flowchart_title": "产品使用主链路",
  "flowchart_desc": "L1 总览图：从任务规划到数据交付的完整流程",
  "valuechain_title": "价值链定位",
  "cta_button_text": "立即了解"
}
```

---

#### Stage 5: BUILD
**输入**:
- `02-extracted/product-data.json`
- `03-analysis/opportunities.json`
- `04-design/config.json`
- `04-design/images-manifest.json`
- `assets/templates/`

**操作**:
1. 加载 `base.html` 骨架
2. 按 `output_sections` 注入各 section 模板
3. 替换所有 `{{variable}}` 为实际值
4. 内联 CSS/JS 到单文件
5. 图片使用相对路径

**输出文件**: `05-webpage/index.html`（单文件，零依赖）

**模板变量路径对照**:
```
{{product.name}}        → product_data["name"]
{{product.brand}}       → product_data["brand"]
{{product.slogan}}      → product_data["slogan"]
{{hero.product_name}}   → product_data["product_name"]
{{hero.hero_image}}     → images_manifest["hero_image"]
{{hero.stats}}          → product_data["core_specs_highlight"]
{{framework.title}}     → config["framework_title"]
{{framework.subtitle}}  → config["framework_subtitle"]
{{framework.steps}}     → opportunities["framework_steps"]
{{opportunities.list}}  → opportunities["opportunities"]
{{valuechain.nodes}}    → product_data["value_chain"]
{{brand.logo_text}}     → product_data["product_name"]
{{brand.hero_image}}    → images_manifest["brand_image"]
```

---

#### Stage 6: CAPTURE
**输入**: `05-webpage/index.html`
**操作**:
1. 启动本地 HTTP 服务器 (`python -m http.server`)
2. 使用 `scripts/capture.py` 录制网页滚动
3. 默认 Section 停留时间:
   - hero: 5s
   - framework: 8s
   - painpoint: 6s
   - opportunities: 22s（含卡片滚动）
   - flowchart: 4s
   - valuechain: 4s
   - brand: 4s

**输出文件**: `06-capture/raw-video.mp4`

---

#### Stage 7: VOICE
**输入**: `05-webpage/narration.md`
**操作**: 使用 `scripts/voice.py` 生成配音

**输出文件**:
- `07-voice/narration.mp3` — 完整配音
- `07-voice/subtitles.srt` — 字幕文件
- `07-voice/seg_*.mp3` — 分段音频

**默认配置**:
- Voice: `zh-CN-XiaoxiaoNeural`（微软晓晓）
- Rate: `+0%`
- Pitch: `+0Hz`

---

#### Stage 8: COMPOSE
**输入**: `06-capture/raw-video.mp4` + `07-voice/narration.mp3`
**操作**:
1. 计算音频总时长
2. 调整视频速度匹配音频（`setpts` 滤镜）
3. 合并音画

**输出文件**: `08-compose/final_video.mp4`

**注意**: 字幕在 Windows 上 ffmpeg `subtitles` 滤镜有兼容性问题，当前方案是独立交付 `.srt` 文件，用户可用剪辑软件导入或播放器加载。

---

#### Stage 9: DELIVER
**输入**: 所有上游产物
**操作**: 复制到交付目录

**输出目录结构**:
```
deliver/
  ├── final_video.mp4      # 成品视频
  ├── webpage/             # 分析网页
  │   ├── index.html
  │   └── images/
  ├── narration.mp3        # 配音音频
  └── subtitles.srt        # 字幕文件
```

---

## 断点续做逻辑

每个阶段开始前检查:
```
if (exists(upstream_output) AND upstream_output.md5 == cached_md5):
  skip_stage()
else:
  run_stage()
  cache_md5()
```

**强制重新执行**: 如果用户明确说"重新分析"或"更新框架"，清除对应阶段的缓存。

---

## 错误处理

| 错误场景 | 处理策略 |
|---------|---------|
| URL 无法访问 | 回退到用户描述输入，提示用户提供文本描述 |
| LLM 输出格式错误 | 重试 2 次，如果仍失败，使用默认值填充缺失字段 |
| 图片下载失败 | 降级到下一级来源，最终用 SVG 占位 |
| 模板变量缺失 | 用空字符串或默认值替换，不中断流程 |
| 磁盘空间不足 | 提示用户清理空间，或输出到临时目录 |

---

## 性能优化

1. **并行执行**: Stage 2 和 Stage 5 可以部分并行（提取和找图不依赖）
2. **缓存**: 同一产品 URL 24h 内不再重复抓取
3. **图片压缩**: 下载后自动压缩到 web 适用尺寸（最大 1920px 宽）
4. **增量更新**: 只修改变化的 section，其他部分复用缓存
