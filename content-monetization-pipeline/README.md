# Content Monetization Pipeline — 内容变现分发管线

> 将已生产的内容资产（产品宣发视频、种草图文、品牌故事）转化为可分发、可追踪、可变现的全链路方案。

---

## 快速开始

### 方式一：作为 OpenClaw Skill 使用

将 `SKILL.md` 作为系统提示词或参考文档提供给 AI：

```
请基于 content-monetization-pipeline/SKILL.md 的规范，
为我的 DJI Mavic 3 宣发视频制定多平台分发和变现方案：
- 目标平台：抖音、小红书、TikTok、B站
- 变现模式：CPS（佣金率 15%，客单价 ¥299）
- 已有内容：dji_final_clean.mp4（横屏 1920x1080，66.9s）
```

### 方式二：视频格式转换脚本（video_adapter.py）

**前置条件**
- Python 3.8+
- ffmpeg（Windows 用户需设置环境变量 `FFMPEG_PATH`）

**安装**
```bash
# 克隆仓库
git clone https://github.com/MeerkatAIChina/manufacturing-ai-efficiency-Skill.git

# 设置 ffmpeg 路径（Windows）
set FFMPEG_PATH=D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe

# 或 Linux/Mac
export FFMPEG_PATH=/usr/bin/ffmpeg
```

**基本用法**

```bash
# 适配指定平台（抖音+小红书+TikTok）
python scripts/video_adapter.py \
  -i dji_final_clean.mp4 \
  -o ./dist \
  --platforms douyin xiaohongshu tiktok

# 适配所有平台 + 生成 60s 切片
python scripts/video_adapter.py \
  -i video.mp4 \
  -o ./dist \
  --all --clips 60

# 仅生成正方形版本（Instagram/微信）
python scripts/video_adapter.py \
  -i video.mp4 \
  -o ./dist \
  --platforms youtube --square
```

**输出结构**
```
dist/
├── dji_final_clean_douyin_20260518_143052.mp4    # 抖音：1080x1920 竖屏
├── dji_final_clean_xiaohongshu_20260518_143055.mp4  # 小红书：1080x1920 竖屏
├── dji_final_clean_tiktok_20260518_143058.mp4      # TikTok：1080x1920 竖屏
├── dji_final_clean_clip_01of02_60s_20260518_143100.mp4  # 60s 切片
├── dji_final_clean_clip_02of02_60s_20260518_143102.mp4  # 60s 切片
├── dji_final_clean_square_1x1_20260518_143104.mp4    # 正方形：1080x1080
└── manifest.json                                      # 分发清单
```

**manifest.json 示例**
```json
{
  "generated_at": "2026-05-18T14:30:52+08:00",
  "source_video": "dji_final_clean.mp4",
  "output_directory": "./dist",
  "total_files": 7,
  "files": [
    {
      "platform": "douyin",
      "type": "vertical",
      "path": ".../dji_final_clean_douyin_20260518_143052.mp4",
      "resolution": "1080x1920",
      "duration": 66.9,
      "size_mb": 15.2
    }
  ]
}
```

---

## 功能详解

### 平台适配矩阵

| 平台 | 标识符 | 格式 | 分辨率 | 特殊要求 |
|------|--------|------|--------|---------|
| 抖音 | `douyin` | 竖屏 9:16 | 1080×1920 | 3s 钩子，完播率优先 |
| 小红书 | `xiaohongshu` | 竖屏 9:16 | 1080×1920 | 封面决定 80% 点击率 |
| TikTok | `tiktok` | 竖屏 9:16 | 1080×1920 | 3s hook + 趋势音乐 |
| Bilibili | `bilibili` | 横屏 16:9 | 1920×1080 | 3-10min，知识/评测类 |
| 微信视频号 | `wechat` | 竖屏 9:16 | 1080×1920 | 熟人社交，信任前置 |
| YouTube | `youtube` | 横屏 16:9 | 1920×1080 | 长视频 + Shorts 切片 |
| Instagram Reels | `instagram` | 竖屏 9:16 | 1080×1920 | 快节奏 + 音乐 |

### 切片功能

| 预设 | 时长 | 适用场景 |
|------|------|---------|
| `30s` | 30 秒 | 抖音极速版、信息流广告 |
| `60s` | 60 秒 | 抖音/快手标准短视频 |
| `3min` | 3 分钟 | B站/YouTube 中视频 |
| `5min` | 5 分钟 | 深度评测、教程 |

**切片策略**：
1. 如果原视频是横屏 → 先转竖屏 → 再切片
2. 均匀分段（每段等长）
3. 自动清理中间临时文件

### 格式转换策略

**横屏 16:9 → 竖屏 9:16**
- 计算目标比例（9/16 = 0.5625）
- 从中心裁剪出匹配区域
- 使用 lanczos 算法缩放至 1080×1920
- 保持音频不变（AAC 192kbps）

**任意比例 → 正方形 1:1**
- 取短边为基准，从中心裁剪正方形
- 缩放至 1080×1080

---

## 与 content-monetization-pipeline SKILL 的协作

### 完整工作流

```
Stage 1-9: product-promo-video-maker
  → 产出：dji_final_clean.mp4（横屏 1920x1080，66.9s）

Stage 10: video_adapter.py（本脚本）
  → 输入：dji_final_clean.mp4
  → 输出：多平台适配视频 + manifest.json

Stage 11-15: content-monetization-pipeline SKILL
  → 输入：manifest.json + 平台列表 + 变现目标
  → 输出：分发排期表 + UTM 追踪链接 + 优惠码 + ROI 追踪模板

Stage 16+: 人工执行发布（或接入平台 API/RPA）
  → 按排期表手动/自动发布
  → 回填数据到 ROI 追踪模板
```

### 为什么分开设计？

| 阶段 | 自动化程度 | 原因 |
|------|-----------|------|
| 视频生产 | ✅ 全自动 | `product-promo-video-maker` 有完整脚本 |
| 格式转换 | ✅ 全自动 | `video_adapter.py` 一行命令 |
| 分发策略 | ⚠️ AI 辅助 | 需要理解产品/受众/平台特征，AI 生成策略 |
| 平台发布 | ❌ 需人工/RPA | 各平台无官方批量 API，需浏览器自动化 |
| 数据追踪 | ⚠️ 半自动 | YAML 模板 + 手动/爬虫回填 |

---

## 命令行参数

```
usage: video_adapter.py [-h] -i INPUT -o OUTPUT
                        [--platforms {douyin,xiaohongshu,tiktok,bilibili,wechat,youtube,instagram} [{...}]]
                        [--all] [--clips {30s,60s,3min,5min}] [--square]
                        [--ffmpeg FFMPEG]

Video Adapter — 将产品宣发视频转换为多平台适配格式

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        输入视频文件路径
  -o OUTPUT, --output OUTPUT
                        输出目录
  --platforms {douyin,xiaohongshu,tiktok,bilibili,wechat,youtube,instagram} [...]
                        目标平台列表
  --all                 适配所有平台
  --clips {30s,60s,3min,5min}
                        生成短切片
  --square              额外生成正方形 1:1 版本
  --ffmpeg FFMPEG       ffmpeg 路径（默认从环境变量 FFMPEG_PATH）

示例:
  python video_adapter.py -i DJI_Mavic3_Promo.mp4 -o ./dist --platforms douyin xiaohongshu tiktok
  python video_adapter.py -i video.mp4 -o ./dist --all --clips 60
  python video_adapter.py -i video.mp4 -o ./dist --platforms youtube --square
```

---

## 依赖

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | 3.8+ | 脚本运行时 |
| ffmpeg | 4.4+ | 视频编码/解码/转换 |
| ffprobe | 4.4+ | 视频信息探测（ffmpeg 自带） |

### ffmpeg 安装

**Windows**
```powershell
# 下载 ffmpeg essentials build
# https://github.com/BtbN/FFmpeg-Builds/releases
# 解压到 D:\tools\ffmpeg\
set FFMPEG_PATH=D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe
```

**macOS**
```bash
brew install ffmpeg
```

**Linux**
```bash
sudo apt update && sudo apt install ffmpeg
```

---

## 故障排查

### ffmpeg 未找到
```
❌ ffmpeg 未找到: D:\tools\ffmpeg\...
```
**解决**：设置环境变量 `FFMPEG_PATH` 或修改脚本中的默认路径

### 视频格式不支持
```
❌ 未找到视频流
```
**解决**：确保输入文件为常见视频格式（MP4/MOV/AVI/MKV）。如为特殊编码，先用 ffmpeg 转码：`ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4`

### 输出文件过大
视频默认使用 `-crf 23`（H.264），如需更小体积可修改脚本中的 crf 值（23→28，质量下降但文件更小）。

---

## 与其他 Skill 的关系

```
product-promo-video-maker/
├── SKILL.md           ← 上游：生产视频
├── scripts/
│   ├── pipeline.py
│   ├── render.py
│   ├── capture.py
│   └── voice.py
│
content-monetization-pipeline/
├── SKILL.md           ← 策略：分发变现方案
├── scripts/
│   └── video_adapter.py  ← 格式转换（你在这里）
│
fast-moving-consumer-goods-ecommerce-operator/
└── SKILL.md           ← 相关：电商运营（CPS/CPE/CPM 结算参考）
```

---

## 许可证

MIT License — 与 manufacturing-ai-efficiency-Skill 仓库一致。

---

*Content Monetization Pipeline v1.0 | 2026-05-18*
