# PPT Master — AI 原生可编辑 PPTX 生成

## 简介

PPT Master 是一个 AI 驱动的多格式 SVG 内容生成系统，将 PDF、DOCX、URL、Markdown 等源文档转换为**原生可编辑的 PowerPoint（PPTX）**。每个元素都是真实的 DrawingML 形状（不是图片），可在 PowerPoint 中直接点击编辑。

## 项目定位

- **定位**：内容创作型 Skill（PPT / 小红书 / 朋友圈 / Story 等多格式输出）
- **原始来源**：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)（MIT License，v2.7.0）
- **适配说明**：已按 MeerkatAI Skill Registry 规范包装，保留原始工作流和目录结构

## 适用场景

- 用户要求"做 PPT"、"生成演示文稿"、"把这份报告做成幻灯片"
- 用户提供了 PDF/DOCX/URL/Markdown 源材料，需要转化为视觉化呈现
- 用户需要小红书/朋友圈/Story 等社媒格式的图文内容
- 用户需要路演 PPT、咨询风格报告、学术答辩、产品发布会等特定模板风格
- 用户需要配音版 PPT 或导出为 MP4 视频

## 不适用场景

- 用户没有源材料也没有主题想法（需要先跑 `topic-research` 工作流收集素材）
- 用户要求实时协作编辑（PPT Master 是 AI 生成工具，不是在线协作平台）
- 用户要求数据驱动的实时图表（图表是 SVG 转形状，底层数据不可通过 Excel 编辑）

## 核心能力

### 能力 1：7 步主链路（7-Step Pipeline）

```
Step 1: 源内容处理    → PDF/DOCX/URL → Markdown
Step 2: 项目初始化    → 创建项目目录结构
Step 3: 模板选择      → 自由设计 / 复刻模板 / 使用内置模板库
Step 4: 策略师阶段    → 八项确认（格式/页数/受众/风格/配色/图标/字体/图片）
Step 5: 图片获取      → AI 生成 / 网络搜索 / 用户提供（条件触发）
Step 6: 执行师阶段    → 逐页生成 SVG（串行，单页连续生成）
Step 7: 后处理与导出  → SVG → PPTX（原生形状 + SVG 参考版）
```

### 能力 2：多格式输出

| 格式 | viewBox | 适用场景 |
|------|---------|---------|
| PPT 16:9 | 1280×720 | 标准演示文稿 |
| PPT 4:3 | 1024×768 | 传统投影 |
| 小红书 | 1242×1660 | 社媒图文 |
| 朋友圈 | 1080×1080 | 方形海报 |
| Story | 1080×1920 | 竖屏短视频封面 |
| Banner | 自定义 | 横幅广告 |
| A4 | 自定义 | 打印文档 |

### 能力 3：模板系统

- **内置模板库**：20+ 风格（麦肯锡、谷歌、学术、禅意、像素、发布会等）
- **模板复刻**：用户上传任意 `.pptx`，通过 `/create-template` 工作流提取颜色/字体/布局/素材
- **自定义模板**：基于截图 + AI 分析创建全新模板

### 能力 4：实时预览与视觉编辑

- 生成过程中自动启动浏览器预览（`localhost:5050`）
- 用户可点击任意元素，写修改意见，提交后 AI 重写 SVG 并重新导出
- 支持"应用我的批注"（apply my annotations）

### 能力 5：动画与配音

- **动画**：页面过渡 + 元素入场动画（真实 OOXML，非嵌入视频）
- **配音**：edge-tts（默认）或云 TTS（ElevenLabs / MiniMax / Qwen / CosyVoice，支持克隆语音）
- **视频导出**：PowerPoint 直接导出 MP4（同步配音 + 过渡）

### 能力 6：640+ 矢量图标库

- SVG Repo、Tabler Icons、Simple Icons、Phosphor Icons
- 按需搜索，自动嵌入 SVG

## 执行链路（核心步骤）

### 第一步：意图识别

判断用户请求：
- "做 PPT / 生成幻灯片" → 进入完整 7 步链路
- "用某个模板做" → 需要用户提供模板目录路径（触发 Step 3）
- "只看效果 / 预览" → 启动 live preview（`workflows/live-preview.md`）
- "给 PPT 配音 / 导出视频" → 进入 `workflows/generate-audio.md`
- "复刻一个模板" → 进入 `workflows/create-template.md`

### 第二步：信息收集

**必须收集**：
1. 源材料（PDF / DOCX / URL / Markdown / 文本描述）
2. 目标格式（PPT 16:9 / 小红书 / Story 等）
3. 页数范围
4. 目标受众

**可选收集**：
- 模板路径（如果用户想复用已有模板）
- 风格偏好（"麦肯锡风" / "科技风" / "禅意风"等——不触发模板选择，只作为设计简报）
- 图片策略（AI 生成 / 网络搜索 / 用户提供）

### 第三步：执行 7 步链路

**Step 1 — 源内容处理**：
- PDF → `scripts/source_to_md/pdf_to_md.py`
- DOCX → `scripts/source_to_md/doc_to_md.py`
- URL → `scripts/source_to_md/web_to_md.py`
- Markdown → 直接读取

**Step 2 — 项目初始化**：
```bash
python3 scripts/project_manager.py init <project_name> --format <format>
python3 scripts/project_manager.py import-sources <project_path> <files...> --move
```

**Step 3 — 模板选择**（仅当用户提供模板目录路径时触发）：
```bash
cp <template_dir>/*.svg <project>/templates/
cp <template_dir>/design_spec.md <project>/templates/
```

**Step 4 — 策略师阶段**（BLOCKING，必须等待用户确认）：
- 读取 `references/strategist.md`
- 输出八项确认（格式/页数/受众/风格/配色/图标/字体/图片）
- 用户确认后输出 `design_spec.md` + `spec_lock.md`
- 同时提示分步模式（长文档建议 split mode）

**Step 5 — 图片获取**（条件触发）：
- AI 生成：`scripts/image_gen.py --manifest`
- 网络搜索：`scripts/image_search.py`
- 用户提供：无需操作

**Step 6 — 执行师阶段**：
- 读取角色定义：`references/executor-base.md` + `references/shared-standards.md` + 风格文件
- 启动 live preview：`scripts/svg_editor/server.py --live`
- 逐页生成 SVG（每页前重读 `spec_lock.md`，防止上下文漂移）
- SVG 质量检查：`scripts/svg_quality_checker.py`
- 生成讲稿：`notes/total.md`

**Step 7 — 后处理与导出**：
```bash
# 必须串行执行，每步成功后才能下一步
python3 scripts/total_md_split.py <project_path>
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path> -s final
```

输出：
- `exports/<name>.pptx` — 原生形状版（推荐）
- `backup/<name>_svg.pptx` — SVG 参考版

### 第四步：质量自检

输出前完成：
- [ ] viewBox = "0 0 1280 720"（或对应格式的 viewBox）
- [ ] 无 `<foreignObject>` / `<style>` / `class` / `clipPath` / `mask`
- [ ] 所有文本 ≥ 14px
- [ ] 内容在安全区域内
- [ ] svg_quality_checker.py 0 errors
- [ ] finalize_svg.py 和 svg_to_pptx.py 串行执行成功

## 质量标准

- **SVG 必须手写，禁止脚本批量生成**：每页 SVG 由主 Agent 直接编写，单页连续生成，禁止拆分为子 Agent 或循环脚本
- **串行执行**：7 步必须严格按顺序，禁止跨阶段捆绑或并行执行
- **spec_lock 每页重读**：防止长 PPT 的上下文压缩漂移
- **BLOCKING 不可跳过**：Step 4 八项确认必须等待用户确认
- **禁止推测性执行**：Step 4 阶段不得提前准备 Step 6 的 SVG 代码

## 依赖说明

### 外部依赖

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | 3.10+ | 核心运行时 |
| pip | — | 安装 requirements.txt |

### Python 包

```
pip install -r requirements.txt
```

关键包：lxml、Pillow、cairoSVG、requests、python-dotenv、curl_cffi（微信公众号）

### 可选依赖

| 依赖 | 用途 |
|------|------|
| Node.js 18+ | 微信公众号页面转换 |
| Pandoc | 遗留格式转换（.doc/.odt/.rtf/.tex/.rst/.org/.typ） |
| AI IDE | Claude Code / Cursor / VS Code Copilot / Codebuddy |

### AI 模型推荐

| 模型 | 效果 | 成本 |
|------|------|------|
| Claude Opus / Sonnet | ⭐⭐⭐ 最佳 | ~$0.24/PPT |
| Claude Sonnet | ⭐⭐ 良好 | ~$0.08/PPT |
| VS Code Copilot | ⭐⭐ 可用 | 含在订阅中 |

> **核心原则**：PPT Master 是 harness（工具），模型决定天花板。工具免费，只付模型使用费。

## 安装与使用

### 方式一：作为独立仓库使用（推荐）

```bash
# 1. 克隆原始仓库（获取完整文件）
git clone https://github.com/hugohe3/ppt-master.git
cd ppt-master
pip install -r requirements.txt

# 2. 打开 AI IDE（Claude Code / Cursor / VS Code Copilot）
# 3. 在聊天面板输入："帮我做一份关于 XXX 的 PPT"
```

### 方式二：作为 MeerkatAI Skill 使用

本 Skill 已注册到 `manufacturing-ai-efficiency-Skill` Registry：

```
请使用 ppt-master Skill 帮我：
1. 从 projects/q3-report.pdf 生成一份 10 页的 Q3 汇报 PPT
2. 格式 PPT 16:9，麦肯锡咨询风格
3. 目标受众：公司管理层
```

AI 会自动执行 7 步链路，生成可编辑的 `.pptx`。

## 目录结构

```
ppt-master/
├── skill.yaml              # MeerkatAI 元数据
├── SKILL.md                # 本文件（核心定义）
├── README.md               # 使用文档
├── changelog.md            # 变更记录
├── references/             # 角色定义和技术规范
│   ├── strategist.md       # 策略师角色定义
│   ├── executor-base.md    # 执行师基础规范
│   ├── executor-general.md # 通用风格
│   ├── executor-consultant.md      # 咨询风格
│   ├── executor-consultant-top.md  # 顶级咨询风格
│   ├── shared-standards.md         # SVG/PPT 技术约束
│   ├── canvas-formats.md           # 画布格式规范
│   ├── image-base.md               # 图片基础框架
│   ├── image-generator.md          # AI 生图规范
│   ├── image-searcher.md           # 网络搜图规范
│   ├── image-layout-patterns.md    # 图文排版模式
│   ├── svg-image-embedding.md      # SVG 图片嵌入
│   └── animations.md               # 动画规范
├── scripts/                # 工具脚本
│   ├── source_to_md/       # 源内容转换（PDF/DOCX/Excel/PPT/URL）
│   ├── project_manager.py  # 项目管理
│   ├── analyze_images.py   # 图片分析
│   ├── image_gen.py        # AI 生图（多后端）
│   ├── image_search.py     # 网络搜图
│   ├── svg_quality_checker.py      # SVG 质量检查
│   ├── total_md_split.py           # 讲稿拆分
│   ├── finalize_svg.py             # SVG 后处理
│   ├── svg_to_pptx.py              # PPTX 导出
│   ├── svg_editor/                 # 实时预览编辑器
│   └── update_spec.py              # 规格传播
├── templates/              # 模板库
│   ├── layouts/            # 布局模板（20+ 风格）
│   ├── charts/             # 图表模板
│   └── icons/              # 640+ 矢量图标
├── workflows/              # 独立工作流
│   ├── create-template.md  # 模板创建
│   ├── topic-research.md   # 主题研究
│   ├── resume-execute.md   # 分步续跑
│   ├── verify-charts.md    # 图表校准
│   ├── customize-animations.md   # 动画定制
│   ├── live-preview.md           # 实时预览
│   └── generate-audio.md         # 配音导出
└── examples/               # 示例项目（15 个，229 页）
```

## 关键脚本速查

| 场景 | 命令 |
|------|------|
| PDF 转 Markdown | `python3 scripts/source_to_md/pdf_to_md.py <file>` |
| DOCX 转 Markdown | `python3 scripts/source_to_md/doc_to_md.py <file>` |
| 网页转 Markdown | `python3 scripts/source_to_md/web_to_md.py <url>` |
| 初始化项目 | `python3 scripts/project_manager.py init <name> --format ppt169` |
| 导入源文件 | `python3 scripts/project_manager.py import-sources <path> <files> --move` |
| 分析图片 | `python3 scripts/analyze_images.py <project>/images` |
| AI 生图 | `python3 scripts/image_gen.py --manifest <project>/images/image_prompts.json` |
| SVG 质检 | `python3 scripts/svg_quality_checker.py <project>` |
| 拆分讲稿 | `python3 scripts/total_md_split.py <project>` |
| SVG 后处理 | `python3 scripts/finalize_svg.py <project>` |
| 导出 PPTX | `python3 scripts/svg_to_pptx.py <project> -s final` |
| 启动预览 | `python3 scripts/svg_editor/server.py <project> --live` |
| 更新规格 | `python3 scripts/update_spec.py <project> --propagate` |

## 开发历史

### V2.7.0 (2026-05-15) — 上游最新
- 图表模板库：结构命名，文件名描述视觉特征
- 完整的 simple-icons 品牌图标库
- PPTX ↔ SVG 双向转换

### V2.6.0 (2026-05-05)
- 原生 PPTX ↔ SVG 往返转换
- pptx_to_svg：语义化 OOXML→SVG 转换器

### V2.3.0 (2025-12)
- 初始稳定版本，15 个示例项目，229 页

---

*本 Skill 基于 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)（MIT License）适配。*
*完整工作流和详细规则请参考原始仓库 `skills/ppt-master/SKILL.md`。*
