#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Adapter — 内容变现分发前的格式转换工具

将产品宣发视频（横屏 16:9）自动转换为多平台适配格式：
- 竖屏 9:16（抖音/小红书/TikTok）
- 正方形 1:1（微信/Instagram）
- 短切片（30s / 60s / 3min）

依赖：ffmpeg（Windows 下需要指定绝对路径）
"""

import os
import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime

# ========== 配置 ==========
# Windows 下 ffmpeg 绝对路径（从 TOOLS.md 读取）
FFMPEG_PATH = os.environ.get("FFMPEG_PATH", r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe")

# 平台格式定义
PLATFORM_PROFILES = {
    "douyin": {
        "name": "抖音",
        "aspect": "9:16",
        "width": 1080,
        "height": 1920,
        "max_duration": None,
        "description": "竖屏全屏，3秒钩子"
    },
    "xiaohongshu": {
        "name": "小红书",
        "aspect": "9:16",
        "width": 1080,
        "height": 1920,
        "max_duration": None,
        "description": "竖屏视频 + 3:4封面"
    },
    "tiktok": {
        "name": "TikTok",
        "aspect": "9:16",
        "width": 1080,
        "height": 1920,
        "max_duration": None,
        "description": "竖屏，3s hook + 趋势音乐"
    },
    "bilibili": {
        "name": "Bilibili",
        "aspect": "16:9",
        "width": 1920,
        "height": 1080,
        "max_duration": None,
        "description": "横屏，知识/评测/故事类"
    },
    "wechat": {
        "name": "微信视频号",
        "aspect": "9:16",
        "width": 1080,
        "height": 1920,
        "max_duration": None,
        "description": "熟人社交，信任前置"
    },
    "youtube": {
        "name": "YouTube",
        "aspect": "16:9",
        "width": 1920,
        "height": 1080,
        "max_duration": None,
        "description": "横屏长视频 + Shorts 竖屏切片"
    },
    "instagram": {
        "name": "Instagram Reels",
        "aspect": "9:16",
        "width": 1080,
        "height": 1920,
        "max_duration": None,
        "description": "竖屏，3s hook"
    }
}

# 切片时长预设
CLIP_PRESETS = {
    "30s": 30,
    "60s": 60,
    "3min": 180,
    "5min": 300
}


def check_ffmpeg():
    """检查 ffmpeg 是否可用"""
    if not os.path.exists(FFMPEG_PATH):
        print(f"❌ ffmpeg 未找到: {FFMPEG_PATH}")
        print("   请设置环境变量 FFMPEG_PATH 或修改脚本中的 FFMPEG_PATH")
        sys.exit(1)
    
    try:
        result = subprocess.run(
            [FFMPEG_PATH, "-version"],
            capture_output=True,
            text=True,
            check=True
        )
        version = result.stdout.split('\n')[0]
        print(f"✅ ffmpeg: {version}")
    except Exception as e:
        print(f"❌ ffmpeg 执行失败: {e}")
        sys.exit(1)


def get_video_info(input_path):
    """使用 ffprobe 获取视频信息"""
    ffprobe_path = FFMPEG_PATH.replace("ffmpeg.exe", "ffprobe.exe")
    
    cmd = [
        ffprobe_path,
        "-v", "error",
        "-show_entries", "format=duration",
        "-show_entries", "stream=width,height,r_frame_rate",
        "-of", "json",
        input_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    
    duration = float(info["format"]["duration"])
    
    # 取第一个视频流
    for stream in info["streams"]:
        if stream.get("width") and stream.get("height"):
            width = stream["width"]
            height = stream["height"]
            fps_str = stream.get("r_frame_rate", "30/1")
            fps = eval(fps_str)  # 如 "30000/1001" → 29.97
            break
    else:
        raise ValueError("未找到视频流")
    
    return {
        "duration": duration,
        "width": width,
        "height": height,
        "fps": fps
    }


def generate_output_path(input_path, output_dir, suffix, ext="mp4"):
    """生成输出文件路径"""
    input_stem = Path(input_path).stem
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{input_stem}_{suffix}_{timestamp}.{ext}"
    return str(output_dir / filename)


def convert_to_vertical(input_path, output_path, target_width=1080, target_height=1920):
    """
    横屏 16:9 → 竖屏 9:16
    策略：从中心裁剪出 9:16 区域，然后缩放到目标分辨率
    """
    info = get_video_info(input_path)
    src_w, src_h = info["width"], info["height"]
    
    # 计算裁剪区域（保持 9:16 比例）
    target_ratio = target_width / target_height  # 9/16 = 0.5625
    src_ratio = src_w / src_h
    
    if src_ratio > target_ratio:
        # 原视频更宽，需要裁掉左右两边
        new_w = int(src_h * target_ratio)
        new_h = src_h
        x = (src_w - new_w) // 2
        y = 0
    else:
        # 原视频更高或比例相同，需要裁掉上下（通常横屏不会发生）
        new_w = src_w
        new_h = int(src_w / target_ratio)
        x = 0
        y = (src_h - new_h) // 2
    
    # ffmpeg 命令
    cmd = [
        FFMPEG_PATH,
        "-y",  # 覆盖输出文件
        "-i", input_path,
        "-vf", f"crop={new_w}:{new_h}:{x}:{y},scale={target_width}:{target_height}:flags=lanczos",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        output_path
    ]
    
    print(f"  🎬 横屏→竖屏: {os.path.basename(output_path)}")
    print(f"     裁剪: {new_w}x{new_h} @ ({x},{y}) → 缩放: {target_width}x{target_height}")
    
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"  ✅ 完成: {output_path}")
    return output_path


def convert_to_square(input_path, output_path, target_size=1080):
    """
    任意比例 → 正方形 1:1
    策略：从中心裁剪出正方形区域，然后缩放
    """
    info = get_video_info(input_path)
    src_w, src_h = info["width"], info["height"]
    
    min_dim = min(src_w, src_h)
    x = (src_w - min_dim) // 2
    y = (src_h - min_dim) // 2
    
    cmd = [
        FFMPEG_PATH,
        "-y",
        "-i", input_path,
        "-vf", f"crop={min_dim}:{min_dim}:{x}:{y},scale={target_size}:{target_size}:flags=lanczos",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        output_path
    ]
    
    print(f"  🎬 正方形: {os.path.basename(output_path)}")
    print(f"     裁剪: {min_dim}x{min_dim} @ ({x},{y}) → 缩放: {target_size}x{target_size}")
    
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"  ✅ 完成: {output_path}")
    return output_path


def create_clips(input_path, output_dir, clip_duration=60):
    """
    将长视频切分为多个短片段
    策略：均匀分段，每段 clip_duration 秒，最后一段可能较短
    """
    info = get_video_info(input_path)
    total_duration = info["duration"]
    src_w, src_h = info["width"], info["height"]
    
    # 先转换为竖屏（切片主要用于短视频平台）
    # 如果原视频是横屏，先转竖屏再切片
    if src_w > src_h:
        print("  📐 原视频为横屏，先转换为竖屏再切片...")
        temp_vertical = os.path.join(output_dir, f"_temp_vertical_{datetime.now().strftime('%H%M%S')}.mp4")
        convert_to_vertical(input_path, temp_vertical)
        input_for_clips = temp_vertical
    else:
        input_for_clips = input_path
    
    num_clips = int(total_duration // clip_duration)
    if total_duration % clip_duration > 5:  # 最后一段 > 5s 才保留
        num_clips += 1
    
    clip_paths = []
    
    for i in range(num_clips):
        start_time = i * clip_duration
        suffix = f"clip_{i+1:02d}of{num_clips:02d}_{clip_duration}s"
        output_path = generate_output_path(input_path, output_dir, suffix)
        
        cmd = [
            FFMPEG_PATH,
            "-y",
            "-ss", str(start_time),
            "-t", str(clip_duration),
            "-i", input_for_clips,
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            output_path
        ]
        
        print(f"  ✂️ 切片 {i+1}/{num_clips}: {start_time}s ~ {min(start_time + clip_duration, total_duration)}s")
        
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  ✅ 完成: {output_path}")
        clip_paths.append(output_path)
    
    # 清理临时文件
    if input_for_clips != input_path and os.path.exists(input_for_clips):
        os.remove(input_for_clips)
        print(f"  🗑️ 清理临时文件")
    
    return clip_paths


def process_platform(input_path, output_dir, platform, create_clips_flag=False, clip_duration=None):
    """处理单个平台"""
    profile = PLATFORM_PROFILES[platform]
    print(f"\n📱 {profile['name']} ({profile['aspect']}) — {profile['description']}")
    
    results = []
    
    if profile["aspect"] == "9:16":
        # 竖屏
        output_path = generate_output_path(input_path, output_dir, platform)
        convert_to_vertical(input_path, output_path, profile["width"], profile["height"])
        results.append({
            "platform": platform,
            "type": "vertical",
            "path": output_path,
            "resolution": f"{profile['width']}x{profile['height']}"
        })
    elif profile["aspect"] == "16:9":
        # 横屏，直接复制或转码（保持原分辨率）
        output_path = generate_output_path(input_path, output_dir, platform)
        
        info = get_video_info(input_path)
        if info["width"] == profile["width"] and info["height"] == profile["height"]:
            # 已经是目标分辨率，直接复制
            print(f"  📋 分辨率已匹配，直接复制")
            import shutil
            shutil.copy2(input_path, output_path)
        else:
            # 需要缩放
            cmd = [
                FFMPEG_PATH,
                "-y",
                "-i", input_path,
                "-vf", f"scale={profile['width']}:{profile['height']}:flags=lanczos",
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "23",
                "-c:a", "aac",
                "-b:a", "192k",
                "-movflags", "+faststart",
                output_path
            ]
            print(f"  🎬 缩放: {os.path.basename(output_path)}")
            subprocess.run(cmd, check=True, capture_output=True)
        
        print(f"  ✅ 完成: {output_path}")
        results.append({
            "platform": platform,
            "type": "original",
            "path": output_path,
            "resolution": f"{profile['width']}x{profile['height']}"
        })
    
    # 切片（如果请求了）
    if create_clips_flag and clip_duration:
        print(f"\n  ✂️ 生成 {clip_duration}s 切片...")
        clip_paths = create_clips(input_path, output_dir, clip_duration)
        for clip_path in clip_paths:
            results.append({
                "platform": platform,
                "type": f"clip_{clip_duration}s",
                "path": clip_path,
                "resolution": "1080x1920"
            })
    
    return results


def generate_manifest(input_path, output_dir, all_results):
    """生成分发清单 manifest.json"""
    manifest = {
        "generated_at": datetime.now().isoformat(),
        "source_video": input_path,
        "output_directory": output_dir,
        "total_files": len(all_results),
        "files": []
    }
    
    for result in all_results:
        info = get_video_info(result["path"])
        manifest["files"].append({
            "platform": result["platform"],
            "type": result["type"],
            "path": result["path"],
            "resolution": result["resolution"],
            "duration": round(info["duration"], 2),
            "size_mb": round(os.path.getsize(result["path"]) / (1024 * 1024), 2)
        })
    
    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"\n📋 分发清单已生成: {manifest_path}")
    return manifest_path


def main():
    parser = argparse.ArgumentParser(
        description="Video Adapter — 将产品宣发视频转换为多平台适配格式",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python video_adapter.py -i DJI_Mavic3_Promo.mp4 -o ./dist --platforms douyin xiaohongshu tiktok
  python video_adapter.py -i video.mp4 -o ./dist --all --clips 60
  python video_adapter.py -i video.mp4 -o ./dist --platforms youtube --square
        """
    )
    
    parser.add_argument("-i", "--input", required=True, help="输入视频文件路径")
    parser.add_argument("-o", "--output", required=True, help="输出目录")
    parser.add_argument("--platforms", nargs="+", choices=list(PLATFORM_PROFILES.keys()),
                        help="目标平台列表 (douyin xiaohongshu tiktok bilibili wechat youtube instagram)")
    parser.add_argument("--all", action="store_true", help="适配所有平台")
    parser.add_argument("--clips", choices=list(CLIP_PRESETS.keys()),
                        help="生成短切片 (30s/60s/3min/5min)")
    parser.add_argument("--square", action="store_true", help="额外生成正方形 1:1 版本")
    parser.add_argument("--ffmpeg", help="ffmpeg 路径 (默认从环境变量 FFMPEG_PATH 或脚本默认值)")
    
    args = parser.parse_args()
    
    # 更新 ffmpeg 路径
    global FFMPEG_PATH
    if args.ffmpeg:
        FFMPEG_PATH = args.ffmpeg
    
    # 检查
    check_ffmpeg()
    
    if not os.path.exists(args.input):
        print(f"❌ 输入文件不存在: {args.input}")
        sys.exit(1)
    
    # 确定平台列表
    if args.all:
        platforms = list(PLATFORM_PROFILES.keys())
    elif args.platforms:
        platforms = args.platforms
    else:
        print("❌ 请指定 --platforms 或 --all")
        sys.exit(1)
    
    print(f"\n🎬 Video Adapter — 多平台格式转换")
    print(f"   输入: {args.input}")
    print(f"   输出: {args.output}")
    print(f"   平台: {', '.join(platforms)}")
    if args.clips:
        print(f"   切片: {args.clips} ({CLIP_PRESETS[args.clips]}s)")
    if args.square:
        print(f"   正方形: 1:1")
    print()
    
    # 获取视频信息
    info = get_video_info(args.input)
    print(f"📊 源视频信息:")
    print(f"   分辨率: {info['width']}x{info['height']}")
    print(f"   时长: {info['duration']:.1f}s")
    print(f"   帧率: {info['fps']:.2f}fps")
    print()
    
    # 处理各平台
    all_results = []
    
    for platform in platforms:
        results = process_platform(
            args.input, args.output, platform,
            create_clips_flag=bool(args.clips),
            clip_duration=CLIP_PRESETS.get(args.clips) if args.clips else None
        )
        all_results.extend(results)
    
    # 正方形版本（如果请求了）
    if args.square:
        print(f"\n📐 生成正方形 1:1 版本...")
        output_path = generate_output_path(args.input, args.output, "square_1x1")
        convert_to_square(args.input, output_path)
        all_results.append({
            "platform": "square",
            "type": "square_1x1",
            "path": output_path,
            "resolution": "1080x1080"
        })
    
    # 生成分发清单
    manifest_path = generate_manifest(args.input, args.output, all_results)
    
    # 输出摘要
    print(f"\n{'='*50}")
    print(f"✅ 全部完成！共生成 {len(all_results)} 个文件")
    print(f"📁 输出目录: {os.path.abspath(args.output)}")
    print(f"📋 分发清单: {manifest_path}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
