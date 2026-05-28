# 🎬 HyperFrames — 把 HTML 变成营销视频，告别昂贵的视频制作

> 一条命令，从 HTML 合成到 MP4 营销视频——不用学 Premiere，不用等外包。

## 😩 痛点

营销团队需要大量视频内容：产品宣传片、社交媒体短视频、字幕讲解、落地页演示……但传统视频制作流程昂贵、周期长、迭代慢。每次改一行字幕都要重新走一遍剪辑流程。

## ✅ 能做什么 vs ❌ 不做什么

| ✅ 能做 | ❌ 不做 |
|---|---|
| HTML → MP4/WebM 视频渲染 | 实时直播推流 |
| TTS 语音合成 + 字幕自动同步 | 替代 Premiere / DaVinci 等专业剪辑 |
| 音频驱动的视觉特效（节拍同步、频谱脉冲） | 纯数学公式动画（用 `manim-video`） |
| 场景转场（闪白、液态擦除、色差分裂等 shader 过渡） | 图片生成 / 表情包（用 `meme-generation`） |
| 网站 URL → 宣传视频的一键抓取流水线 | 视频会议或流媒体 |
| 9 种开箱即用模板（产品推广、瑞士网格、动态字体等） | — |

## 🧠 核心能力

- **GSAP 动画引擎**：每一帧确定性渲染，支持 tween、缓动、交错、时间轴控制
- **9 个专业模板**：`product-promo`、`warm-grain`、`swiss-grid`、`kinetic-type`、`nyt-graph` 等，开箱即用
- **TTS 语音合成**：内置多语言语音（英语、西班牙语、法语、日语、中文等），一行命令生成旁白
- **字幕自动同步**：Whisper 转录 → 词级时间戳 → 自动对齐音频波形
- **Shader 转场**：`flash-through-white`、`liquid-wipe`、`cross-warp-morph`、`chromatic-split` 等高级转场效果
- **网站转视频**：7 步流水线：抓取 → 设计规范 → 剧本 → 分镜 → 合成 → 渲染 → 交付
- **音频反应式视觉**：低频 → 脉冲缩放，高频 → 发光效果，整体振幅 → 透明度/位移

## 🎯 谁适合用

- **内容营销人员**：快速批量生产产品视频、功能演示
- **社交媒体运营**：TikTok / Instagram / YouTube 风格的短视频模板
- **产品营销**：从落地页 URL 直接生成宣传视频
- **营销代理机构**：降低客户视频项目的交付成本和周期

## 🔗 搭配使用

| 搭配技能 | 用途 |
|---|---|
| `remotion-video` | React 组件驱动的编程式视频 |
| `video` | 通用视频处理和剪辑 |
| `social-content` | 社交媒体内容批量生成 |
| `meme-generation` | 表情包和病毒式传播素材 |

## 🚀 快速开始

```bash
npx hyperframes init my-video --example product-promo
cd my-video
npx hyperframes preview          # 浏览器实时预览
npx hyperframes render --quality high --output promo.mp4
```

一行命令，HTML 即视频。**再也不用等视频团队排期了。**

---

*猫鼬AI × 开源社区联合打磨 | 兼容 Claude Code · Hermes Agent · OpenClaw · Codex CLI*
