#!/usr/bin/env python3
"""
Voice generation script for product-promo-video-maker.
Generates narration audio + subtitle file using SiliconFlow TTS (system preset voice).

Current default: FunAudioLLM/CosyVoice2-0.5B:alex (沉稳男声)
Alternative presets: benjamin(低沉男声), charles(磁性男声), david(欢快男声),
                     anna(沉稳女声), bella(激情女声), claire(温柔女声), diana(欢快女声)
"""
import json
import os
import subprocess
import time
import requests
from pathlib import Path

FFPROBE = r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffprobe.exe"
FFMPEG = r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"

# SiliconFlow API config
SILICONFLOW_API_URL = "https://api.siliconflow.cn/v1/audio/speech"
SILICONFLOW_MODEL = "FunAudioLLM/CosyVoice2-0.5B"
DEFAULT_VOICE = "FunAudioLLM/CosyVoice2-0.5B:alex"  # 沉稳男声

# Speed mapping per section type
SPEED_MAP = {
    "hero": 0.95,
    "painpoint": 1.05,
    "opportunity": 1.0,
    "value": 0.9,
    "brand": 0.85,
}

def format_time_srt(seconds: float) -> str:
    """Format seconds to SRT time format HH:MM:SS,mmm."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def parse_narration(narration_path: str):
    """Parse narration.md into (section_id, text, speed) segments."""
    with open(narration_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    segments = []
    current_section = "default"
    current_lines = []
    
    for line in content.split("\n"):
        if line.startswith("## Section"):
            if current_lines:
                seg_text = " ".join(current_lines).strip()
                speed = _infer_speed(current_section)
                segments.append((current_section, seg_text, speed))
                current_lines = []
            parts = line.replace("## Section", "").strip().split(":")
            current_section = parts[0].strip().lower() if parts else "section"
            # Infer section type from header text
            if len(parts) > 1:
                header_text = parts[1].strip().lower()
                if "painpoint" in header_text or "痛点" in header_text:
                    current_section = "painpoint"
                elif "opportunity" in header_text or "机会" in header_text:
                    current_section = "opportunity"
                elif "value" in header_text or "价值链" in header_text:
                    current_section = "value"
                elif "brand" in header_text or "品牌" in header_text:
                    current_section = "brand"
                elif "hero" in header_text:
                    current_section = "hero"
        elif line.startswith("> "):
            text = line[2:].strip()
            if text:
                current_lines.append(text)
        elif line.strip() and not line.startswith("#"):
            current_lines.append(line.strip())
    
    if current_lines:
        seg_text = " ".join(current_lines).strip()
        speed = _infer_speed(current_section)
        segments.append((current_section, seg_text, speed))
    
    if not segments:
        segments = [("narration", content.strip(), 1.0)]
    
    return segments

def _infer_speed(section_id: str) -> float:
    """Infer speech speed from section ID."""
    sid = section_id.lower()
    for key, speed in SPEED_MAP.items():
        if key in sid:
            return speed
    return 1.0

def generate_speech(api_key: str, text: str, voice: str, speed: float, output_path: str) -> bool:
    """Generate single speech segment via SiliconFlow API."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": SILICONFLOW_MODEL,
        "voice": voice,
        "input": text,
        "response_format": "mp3",
        "speed": speed,
    }
    
    try:
        r = requests.post(SILICONFLOW_API_URL, json=payload, headers=headers, timeout=120)
        if r.status_code == 200 and r.headers.get("content-type") == "audio/mpeg" and len(r.content) > 1000:
            with open(output_path, "wb") as f:
                f.write(r.content)
            return True
        else:
            print(f"  TTS failed: status={r.status_code}, ct={r.headers.get('content-type')}, len={len(r.content)}")
            return False
    except Exception as e:
        print(f"  TTS error: {e}")
        return False

def get_duration(audio_path: str, ffprobe_path: str = None) -> float:
    """Get audio duration via ffprobe."""
    if ffprobe_path is None:
        ffprobe_path = FFPROBE
    result = subprocess.run(
        [ffprobe_path, "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", audio_path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except:
        return 0.0

def generate_voiceover(
    narration_path: str,
    api_key: str,
    output_dir: str = "./07-voice",
    voice: str = None,
    ffmpeg_path: str = None,
    ffprobe_path: str = None
):
    """
    Generate voiceover audio and subtitles using SiliconFlow TTS.
    
    Args:
        narration_path: Path to narration.md file
        api_key: SiliconFlow API key
        output_dir: Directory to save audio files
        voice: TTS voice preset (default: alex)
        ffmpeg_path: Path to ffmpeg binary
        ffprobe_path: Path to ffprobe binary
    
    Returns:
        dict with audio path, subtitles path, total duration, segment count
    """
    if voice is None:
        voice = DEFAULT_VOICE
    if ffmpeg_path is None:
        ffmpeg_path = FFMPEG
    if ffprobe_path is None:
        ffprobe_path = FFPROBE
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    segments = parse_narration(narration_path)
    audio_files = []
    subtitle_entries = []
    current_time = 0.0
    
    print(f"Generating {len(segments)} segments with voice: {voice}")
    
    for i, (section_id, text, speed) in enumerate(segments):
        audio_file = output_dir / f"seg_{i:02d}_{section_id}.mp3"
        print(f"[{i+1}/{len(segments)}] {section_id} (speed={speed}) ... ", end="", flush=True)
        
        ok = generate_speech(api_key, text, voice, speed, str(audio_file))
        if ok:
            duration = get_duration(str(audio_file), ffprobe_path)
            print(f"OK ({int(duration)}s)")
            audio_files.append(str(audio_file))
            
            start = current_time
            end = current_time + duration
            subtitle_entries.append({
                "index": i + 1,
                "start": start,
                "end": end,
                "text": text
            })
            current_time = end
        else:
            print("FAILED")
        
        time.sleep(2)  # Rate limit buffer
    
    if not audio_files:
        raise RuntimeError("No audio segments generated successfully")
    
    # Merge audio
    concat_file = output_dir / "concat.txt"
    with open(concat_file, "w", encoding="utf-8") as f:
        for af in audio_files:
            f.write(f"file '{os.path.abspath(af).replace(chr(92), '/')}'\n")
    
    full_audio = output_dir / "narration.mp3"
    subprocess.run([
        ffmpeg_path, "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", str(full_audio)
    ], capture_output=True)
    
    # Generate SRT
    srt_file = output_dir / "subtitles.srt"
    with open(srt_file, "w", encoding="utf-8") as f:
        for entry in subtitle_entries:
            f.write(f"{entry['index']}\n")
            f.write(f"{format_time_srt(entry['start'])} --> {format_time_srt(entry['end'])}\n")
            f.write(f"{entry['text']}\n\n")
    
    return {
        "audio": str(full_audio),
        "subtitles": str(srt_file),
        "total_duration": current_time,
        "segments": len(audio_files),
        "voice": voice,
    }

def burn_subtitles(video_path: str, audio_path: str, srt_path: str, output_path: str, ffmpeg_path: str = None):
    """
    Replace video audio with narration and burn subtitles into video.
    
    Two-step process:
    1. Replace audio: video + narration -> intermediate
    2. Burn subtitles: intermediate + SRT -> final
    """
    if ffmpeg_path is None:
        ffmpeg_path = FFMPEG
    
    # Step 1: Replace audio
    temp_video = output_path.replace(".mp4", "_temp.mp4")
    subprocess.run([
        ffmpeg_path, "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac",
        "-map", "0:v:0", "-map", "1:a:0",
        "-shortest", temp_video
    ], capture_output=True)
    
    # Step 2: Burn subtitles (SRT must be in same dir as video for subtitles filter)
    import shutil
    srt_dir = os.path.dirname(os.path.abspath(temp_video))
    srt_name = os.path.basename(srt_path)
    temp_srt = os.path.join(srt_dir, srt_name)
    shutil.copy2(srt_path, temp_srt)
    
    subprocess.run([
        ffmpeg_path, "-y",
        "-i", temp_video,
        "-vf", f"subtitles={srt_name}",
        "-c:v", "libx264", "-crf", "23", "-preset", "fast",
        "-c:a", "copy",
        output_path
    ], capture_output=True)
    
    # Cleanup temp
    if os.path.exists(temp_video):
        os.remove(temp_video)
    if os.path.exists(temp_srt) and temp_srt != srt_path:
        os.remove(temp_srt)
    
    return os.path.exists(output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", required=True, help="Path to narration.md")
    parser.add_argument("--api-key", required=True, help="SiliconFlow API key")
    parser.add_argument("--output-dir", default="./07-voice")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="Voice preset (e.g., alex, benjamin, charles)")
    parser.add_argument("--video", help="Optional: video path to burn subtitles into")
    parser.add_argument("--output-video", help="Optional: output video path with burned subtitles")
    args = parser.parse_args()
    
    result = generate_voiceover(
        narration_path=args.narration,
        api_key=args.api_key,
        output_dir=args.output_dir,
        voice=args.voice,
    )
    
    print(f"\nAudio: {result['audio']}")
    print(f"Subtitles: {result['subtitles']}")
    print(f"Duration: {result['total_duration']:.1f}s")
    print(f"Segments: {result['segments']}")
    print(f"Voice: {result['voice']}")
    
    if args.video and args.output_video:
        ok = burn_subtitles(args.video, result['audio'], result['subtitles'], args.output_video)
        print(f"Video with subtitles: {args.output_video} ({'OK' if ok else 'FAILED'})")
