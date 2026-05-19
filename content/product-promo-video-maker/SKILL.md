---
name: product-promo-video-maker
description: Generate a complete product promotional video (HTML analysis page + screen recording + voiceover + subtitles) from any product input. Use when: (1) creating a product promo video with structured analysis, (2) building a marketing video with narration and subtitles, (3) generating a product showcase with selling points and visual effects, (4) producing a distribution-ready MP4 from product info. Input: product URL, description, or files. Output: analysis webpage + final_with_voice.mp4. Not for: simple slideshow videos without structured analysis.
---

# Product Promo Video Maker

Generate a complete, distribution-ready product promotional video from any product input.

## Input

Three input types supported:
1. **Product URL** — e.g. `https://enterprise.dji.com/cn/mavic-3-enterprise`
2. **Product description** — plain text with name, specs, features
3. **Local files** — images + docs dropped by user

## Output

```
deliver/
  ├── final_video.mp4     # Promo video with voiceover + matching timing
  ├── webpage/            # Analysis webpage (open in browser)
  │   ├── index.html
  │   └── images/
  ├── narration.mp3       # Voiceover audio
  └── subtitles.srt     # Subtitle file
```

## Pipeline (9 stages)

```
INGEST → EXTRACT → ANALYZE → DESIGN → BUILD → CAPTURE → VOICE → COMPOSE → DELIVER
```

### Stage 1: INGEST
Read user input. If URL: use browser to extract text/images. If description: save raw text. If files: index paths.

Output: `01-input/product-info.json`

### Stage 2: EXTRACT
Use LLM with JSON Schema to extract structured data:
- `name`, `product_name`, `slogan`, `brand`, `category`
- `core_specs`: key-value map
- `core_specs_highlight`: array of `{key, value}` for hero stats display
- `key_features`: array of `{name, priority, icon, image}`
- `pain_points`: `{before: [], after: []}`
- `scenarios`: array
- `value_chain`: array of `{icon, title, desc}`

Output: `02-extracted/product-data.json`

### Stage 3: ANALYZE
Call the configured analysis framework (default: `manufacturing-ai-efficiency-pro`).

Generates:
- `opportunities`: array of 8-field opportunity cards
- `painpoint_comparison`: before/after lists + metrics
- `flowchart_mermaid`: Mermaid diagram code
- `framework_steps`: 9-step detailed breakdown

Output: `03-analysis/opportunities.json`

### Stage 4: DESIGN
Select template config based on user parameters.

Output: `04-design/config.json` + `04-design/images-manifest.json`

### Stage 5: BUILD
Render `index.html` using template system. Inline all CSS/JS. Fetch product images.

Output: `05-webpage/index.html` + `images/`

**Template variables**:
```
{{product.name}} → product_data["name"]
{{hero.hero_image}} → images_manifest["hero_image"]
{{framework.steps}} → opportunities["framework_steps"]
{{opportunities.list}} → opportunities["opportunities"]
{{valuechain.nodes}} → product_data["value_chain"]
```

### Stage 6: CAPTURE
Use Playwright (`scripts/capture.py`) to record webpage scrolling through all sections.

Output: `06-capture/raw-video.mp4`

**Default section timing**:
| Section | Duration |
|---------|----------|
| hero | 5s |
| framework | 8s |
| painpoint | 6s |
| opportunities | 22s (scrolls 4 cards) |
| flowchart | 4s |
| valuechain | 4s |
| brand | 4s |

### Stage 7: VOICE
Generate narration audio using SiliconFlow TTS (`scripts/voice.py`). System preset voice (alex) with automatic speed variation per section type. Produce subtitle timestamps.

Output: `07-voice/narration.mp3` + `07-voice/subtitles.srt`

**Default TTS config**:
- Provider: `SiliconFlow` (`FunAudioLLM/CosyVoice2-0.5B`)
- Voice: `alex` (沉稳男声, system preset)
- Alternatives: `benjamin`(低沉), `charles`(磁性), `david`(欢快), `anna`(沉稳女声), `bella`(激情女声), `claire`(温柔), `diana`(欢快女声)
- Speed mapping: hero 0.95x / painpoint 1.05x / opportunity 1.0x / value 0.9x / brand 0.85x
- API key required: `siliconflow_api_key` in config or `SILICONFLOW_API_KEY` env var

### Stage 8: COMPOSE
Use ffmpeg to merge video + audio. Video speed adjusted to match audio duration.

Output: `08-compose/final_video.mp4`

**Note**: Subtitle burn-in on Windows has ffmpeg path compatibility issues. Current solution: deliver `.srt` as separate file for editor import or player loading.

### Stage 9: DELIVER
Copy all artifacts to clean deliver directory.

## Configuration

| Parameter | Default | Options |
|-----------|---------|---------|
| `analysis_framework` | `manufacturing-ai-efficiency-pro` | See `references/analysis-frameworks.md` |
| `output_format` | `landscape` | `landscape` (1920×1080), `portrait` (720×1280) |
| `theme` | `dark-industrial` | `dark-industrial`, `robot-theme` |
| `tts.provider` | `siliconflow` | `siliconflow`, `none` |
| `tts.siliconflow_api_key` | *(required for voice)* | Get from [cloud.siliconflow.com](https://cloud.siliconflow.com/account/ak) |
| `tts.voice` | `alex` | `alex`, `benjamin`, `charles`, `david`, `anna`, `bella`, `claire`, `diana` |
| `tts.fallback_provider` | `edge-tts` | `edge-tts` (local, no key needed but lower quality) |
| `include_subtitles` | `true` | `true`, `false` |
| `language` | `zh-CN` | `zh-CN`, `en-US` |
| `duration_target` | `60` | Any integer (seconds, used for pacing guidance) |

## Tool Dependencies

- `browser` — Product page extraction
- `web_search` / `kimi_search` — Image search fallback
- `read` / `write` — File operations
- Playwright — Webpage recording (`chromium` channel with `msedge`)
- ffmpeg — Video composition (required)
- **SiliconFlow API key** — TTS voice generation (optional, see "开箱即用" below)

## 开箱即用 / Out-of-the-Box Usage

**模式 A：完整语音版（推荐）**
1. 注册 [SiliconFlow](https://cloud.siliconflow.com/account/ak) 获取 API key（免费额度足够测试）
2. 复制 `config.template.json` 为 `config.json`，填入 `siliconflow_api_key`
3. 运行 pipeline → 自动出带语音 + 字幕的视频

**模式 B：无 API key 版（纯视频 + 字幕文本）**
- 不填 key → 跳过语音合成，出视频 + `subtitles.srt` + `narration.txt`
- 用户可：① 自己配音后导入剪辑软件 ② 用其他 TTS 工具生成音频后合成

**必需依赖：**
- ffmpeg（配置 `ffmpeg_path` 和 `ffprobe_path`）
- Python 3.10+ + `requests` 库
- Playwright（用于录屏）

**可选依赖：**
- SiliconFlow API key（模式 A）
- `edge-tts` pip 包（旧版 fallback，不推荐）

## File Structure

```
product-promo-video-maker/
├── SKILL.md                          # This file
├── assets/
│   ├── templates/
│   │   ├── base.html                 # HTML skeleton
│   │   ├── styles.css               # CSS (supports dark-industrial + robot-theme)
│   │   ├── scripts.js               # Particle canvas + scroll animations
│   │   └── sections/
│   │       ├── hero.html            # Product showcase + stats
│   │       ├── framework.html       # 9-step timeline with details
│   │       ├── painpoint.html       # Before/after comparison
│   │       ├── opportunities.html   # 8-field opportunity cards
│   │       ├── flowchart.html       # Mermaid container
│   │       ├── valuechain.html      # Value chain nodes
│   │       ├── emotion.html         # SVG emotion curve
│   │       └── brand.html           # Brand closing
│   └── themes/
│       ├── dark-industrial.css      # Default dark theme (blue accent)
│       └── robot-theme.css          # Robot/tech theme (orange accent)
├── scripts/
│   ├── pipeline.py                  # Main 9-stage orchestrator
│   ├── render.py                     # Template rendering engine
│   ├── capture.py                    # Playwright webpage recording
│   └── voice.py                      # TTS + subtitle generation
└── references/
    ├── analysis-frameworks.md         # Available frameworks + schemas
    ├── pipeline-guide.md             # Stage-by-stage execution details
    ├── template-guide.md             # Template rendering guide
    ├── template-variables.md         # Complete variable reference
    └── subtitle-guide.md            # Subtitle generation + burn-in notes
```

## Usage Example

```
User: "帮我做一个 DJI Mavic 3 行业版的宣传视频"
→ Skill triggers
→ Stage 1: Extract product info from URL
→ Stage 3: Run manufacturing-ai-efficiency-pro framework → 7 opportunity cards
→ Stage 5: Build analysis webpage with dark-industrial theme
→ Stage 6: Record 60s scrolling video via Playwright
→ Stage 7: Generate narration + subtitles (zh-CN-XiaoxiaoNeural)
→ Stage 8: Compose final video with speed-matched timing
→ Stage 9: Deliver to deliver/dji-mavic3-20260512/
```

## Known Limitations

1. **Subtitle burn-in on Windows**: ffmpeg `subtitles` filter requires SRT in same directory. Use `force_style` parameter with care (avoid `&` in shell).
2. **Image quality depends on source**: Product page images may be low-res. Recommend using official store/press kit images when available.
3. **TTS prosody**: SiliconFlow system presets (alex/benjamin/etc) are stable and clean but don't clone user's personal voice. For personal voice cloning: requires FishAudio API key or local GPU deployment (F5-TTS / GPT-SoVITS / IndexTTS).
4. **Framework coverage**: Only `manufacturing-ai-efficiency-pro` fully implemented. SaaS / consumer frameworks have schemas but not full prompts.

## Development History

- **v1.0** (2026-05-12) — Initial release based on DJI Mavic 3 and Unitree As2 demos
  - Validated end-to-end pipeline with 2 real products
  - Support: landscape output, Edge TTS, dark-industrial + robot themes
  - Template system: 8 sections, Mustache-style variable syntax

- **v1.1** (2026-05-14) — TTS migration: Edge TTS → SiliconFlow system presets
  - Replaced Edge TTS with SiliconFlow `FunAudioLLM/CosyVoice2-0.5B` system presets
  - Added automatic speed variation: painpoint 1.05x, brand 0.85x, hero 0.95x, etc.
  - Added subtitle burn-in support (ffmpeg `subtitles` filter)
  - Added **no-key fallback mode**: skips TTS, outputs video + SRT + narration.txt
  - Added `config.template.json` for easy configuration
  - Removed rhythm parasitism issue by using system presets (no voice cloning)
  - Known limitation: personal voice cloning requires FishAudio API or local GPU

## References

- `references/pipeline-guide.md` — Stage-by-stage execution details + checkpoint logic
- `references/analysis-frameworks.md` — Available frameworks, their schemas, and LLM prompts
- `references/template-guide.md` — How to render templates, customize themes, add new sections
- `references/template-variables.md` — Complete variable reference for all sections
- `references/subtitle-guide.md` — Subtitle generation, burn-in workarounds, editor import
