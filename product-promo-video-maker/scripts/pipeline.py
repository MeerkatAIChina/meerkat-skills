#!/usr/bin/env python3
"""
Product Promo Video Maker - Main Pipeline
Run all 9 stages from product input to final video.
"""
import asyncio
import json
import os
import sys
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
STAGES_DIR = BASE_DIR / "stages"

# External tools
FFMPEG = r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"
FFPROBE = r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffprobe.exe"

def run_ffmpeg(args):
    """Run ffmpeg command."""
    cmd = [FFMPEG] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg error: {result.stderr}", file=sys.stderr)
    return result

def run_ffprobe(args):
    """Run ffprobe command."""
    cmd = [FFPROB] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# =============================================================================
# Stage 7: VOICE - Generate narration audio + subtitles
# =============================================================================

# =============================================================================
# Stage 7: VOICE - Generate narration audio + subtitles via SiliconFlow TTS
# =============================================================================

SILICONFLOW_API_URL = "https://api.siliconflow.cn/v1/audio/speech"
SILICONFLOW_MODEL = "FunAudioLLM/CosyVoice2-0.5B"
DEFAULT_VOICE = "FunAudioLLM/CosyVoice2-0.5B:alex"

SPEED_MAP = {
    "hero": 0.95,
    "painpoint": 1.05,
    "opportunity": 1.0,
    "value": 0.9,
    "brand": 0.85,
}

def infer_speed(section_id: str) -> float:
    sid = section_id.lower()
    for key, speed in SPEED_MAP.items():
        if key in sid:
            return speed
    return 1.0

def _generate_speech(api_key, text, voice, speed, output_path):
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": SILICONFLOW_MODEL,
        "voice": voice,
        "input": text,
        "response_format": "mp3",
        "speed": speed,
    }
    try:
        import requests
        r = requests.post(SILICONFLOW_API_URL, json=payload, headers=headers, timeout=120)
        if r.status_code == 200 and r.headers.get("content-type") == "audio/mpeg" and len(r.content) > 1000:
            with open(output_path, "wb") as f:
                f.write(r.content)
            return True
        else:
            print(f"  TTS failed: status={r.status_code}, len={len(r.content)}")
            return False
    except Exception as e:
        print(f"  TTS error: {e}")
        return False

def _get_duration(audio_path):
    result = subprocess.run(
        [FFPROBE, "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", audio_path],
        capture_output=True, text=True
    )
    try:
        return float(result.stdout.strip())
    except:
        return 0.0

def stage_voice(config, project_dir):
    """Generate voiceover audio and subtitles via SiliconFlow API."""
    import time
    import requests
    
    voice_dir = project_dir / "07-voice"
    voice_dir.mkdir(exist_ok=True)
    
    narration_md = project_dir / "05-webpage" / "narration.md"
    if not narration_md.exists():
        narration_md = generate_narration(project_dir)
    
    segments = parse_narration(narration_md)
    
    api_key = config.get("siliconflow_api_key", os.environ.get("SILICONFLOW_API_KEY", ""))
    voice = config.get("voice", DEFAULT_VOICE)
    
    audio_files = []
    subtitle_entries = []
    current_time = 0.0
    
    # Check if we have API key
    if not api_key:
        print("WARNING: No SiliconFlow API key found. Skipping TTS generation.")
        print("  To enable voice: set 'siliconflow_api_key' in config or SILICONFLOW_API_KEY env var")
        print("  Continuing with subtitles-only mode...")
        
        # Still generate SRT with estimated durations (1s per 4 chars at normal speed)
        for i, (section_id, text) in enumerate(segments):
            speed = infer_speed(section_id)
            estimated_duration = len(text) / 4.0 * speed  # rough estimate
            
            start = current_time
            end = current_time + estimated_duration
            subtitle_entries.append({"index": i + 1, "start": start, "end": end, "text": text})
            current_time = end
        
        # Generate placeholder narration.md for manual recording
        srt_file = voice_dir / "subtitles.srt"
        with open(srt_file, "w", encoding="utf-8") as f:
            for entry in subtitle_entries:
                f.write(f"{entry['index']}\n")
                f.write(f"{format_time(entry['start'])} --> {format_time(entry['end'])}\n")
                f.write(f"{entry['text']}\n\n")
        
        # Save narration text for manual recording
        with open(voice_dir / "narration.txt", "w", encoding="utf-8") as f:
            for _, text in segments:
                f.write(text + "\n\n")
        
        return {
            "audio": None,
            "subtitles": str(srt_file),
            "total_duration": current_time,
            "segments": len(segments),
            "voice": voice,
            "mode": "subtitles_only",
        }
    
    # Normal TTS generation with SiliconFlow
    print(f"Generating {len(segments)} segments with voice: {voice}")
    
    for i, (section_id, text) in enumerate(segments):
        audio_file = voice_dir / f"seg_{i:02d}_{section_id}.mp3"
        speed = infer_speed(section_id)
        
        print(f"[{i+1}/{len(segments)}] {section_id} (speed={speed}) ... ", end="", flush=True)
        ok = _generate_speech(api_key, text, voice, speed, str(audio_file))
        
        if ok:
            duration = _get_duration(str(audio_file))
            print(f"OK ({duration:.1f}s)")
            audio_files.append(str(audio_file))
            
            start = current_time
            end = current_time + duration
            subtitle_entries.append({"index": i + 1, "start": start, "end": end, "text": text})
            current_time = end
        else:
            print("FAILED")
        
        time.sleep(2)
    
    if not audio_files:
        raise RuntimeError("No audio segments generated successfully")
    
    # Merge audio
    concat_file = voice_dir / "concat.txt"
    with open(concat_file, "w", encoding="utf-8") as f:
        for af in audio_files:
            f.write(f"file '{os.path.abspath(af).replace(chr(92), '/')}'\n")
    
    full_audio = voice_dir / "narration.mp3"
    run_ffmpeg([
        "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c", "copy", str(full_audio)
    ])
    
    # Generate SRT
    srt_file = voice_dir / "subtitles.srt"
    with open(srt_file, "w", encoding="utf-8") as f:
        for entry in subtitle_entries:
            f.write(f"{entry['index']}\n")
            f.write(f"{format_time(entry['start'])} --> {format_time(entry['end'])}\n")
            f.write(f"{entry['text']}\n\n")
    
    return {
        "audio": str(full_audio),
        "subtitles": str(srt_file),
        "total_duration": current_time,
        "segments": len(audio_files),
        "voice": voice,
        "mode": "full_tts",
    }

def stage_burn_subtitles(config, project_dir):
    """Burn subtitles into final video."""
    video_path = project_dir / "08-final" / "final_video.mp4"
    if not video_path.exists():
        video_path = project_dir / "06-record" / "recording.mp4"
    
    srt_path = project_dir / "07-voice" / "subtitles.srt"
    audio_path = project_dir / "07-voice" / "narration.mp3"
    output_path = project_dir / "08-final" / "final_video_subs.mp4"
    
    if not video_path.exists():
        print("No video found for subtitle burning")
        return {"status": "skipped", "reason": "no video"}
    
    if not srt_path.exists():
        print("No subtitles found")
        return {"status": "skipped", "reason": "no subtitles"}
    
    # Step 1: Replace audio
    temp_video = str(output_path).replace(".mp4", "_temp.mp4")
    run_ffmpeg([
        "-y", "-i", str(video_path), "-i", str(audio_path),
        "-c:v", "copy", "-c:a", "aac",
        "-map", "0:v:0", "-map", "1:a:0",
        "-shortest", temp_video
    ])
    
    # Step 2: Burn subtitles (copy SRT to same dir)
    import shutil
    srt_copy = os.path.join(os.path.dirname(temp_video), "subtitles.srt")
    shutil.copy2(str(srt_path), srt_copy)
    
    run_ffmpeg([
        "-y", "-i", temp_video,
        "-vf", "subtitles=subtitles.srt",
        "-c:v", "libx264", "-crf", "23", "-preset", "fast",
        "-c:a", "copy",
        str(output_path)
    ])
    
    # Cleanup
    if os.path.exists(temp_video):
        os.remove(temp_video)
    if os.path.exists(srt_copy):
        os.remove(srt_copy)
    
    return {
        "status": "success",
        "video": str(output_path),
    }

async def stage_voice_legacy(config, project_dir):
    """Generate voiceover audio and subtitles."""
    from edge_tts import Communicate
    
    voice_dir = project_dir / "07-voice"
    voice_dir.mkdir(exist_ok=True)
    
    # Load narration text (generated in stage 3/4)
    narration_md = project_dir / "05-webpage" / "narration.md"
    if not narration_md.exists():
        # Fallback: generate from opportunities
        narration_md = generate_narration(project_dir)
    
    # Parse narration into segments
    segments = parse_narration(narration_md)
    
    # Generate audio per segment
    voice = config.get("voice", "zh-CN-XiaoxiaoNeural")
    rate = config.get("rate", "+0%")
    pitch = config.get("pitch", "+0Hz")
    
    audio_files = []
    subtitle_entries = []
    current_time = 0.0
    
    for i, (section_id, text) in enumerate(segments):
        audio_file = voice_dir / f"seg_{i:02d}_{section_id}.mp3"
        
        communicate = Communicate(text, voice, rate=rate, pitch=pitch)
        await communicate.save(str(audio_file))
        
        # Get duration via ffprobe
        duration_cmd = subprocess.run(
            [FFPROBE, "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(audio_file)],
            capture_output=True, text=True
        )
        duration = float(duration_cmd.stdout.strip())
        
        audio_files.append(str(audio_file))
        
        # Create subtitle entry
        start = current_time
        end = current_time + duration
        subtitle_entries.append({
            "index": i + 1,
            "start": start,
            "end": end,
            "text": text
        })
        current_time = end
    
    # Merge audio files
    concat_file = voice_dir / "concat.txt"
    with open(concat_file, "w", encoding="utf-8") as f:
        for af in audio_files:
            f.write(f"file '{os.path.abspath(af).replace(chr(92), '/')}'\n")
    
    full_audio = voice_dir / "narration.mp3"
    run_ffmpeg([
        "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c:a", "libmp3lame", "-q:a", "2", str(full_audio)
    ])
    
    # Generate SRT file
    srt_file = voice_dir / "subtitles.srt"
    with open(srt_file, "w", encoding="utf-8") as f:
        for entry in subtitle_entries:
            f.write(f"{entry['index']}\n")
            f.write(f"{format_time(entry['start'])} --> {format_time(entry['end'])}\n")
            f.write(f"{entry['text']}\n\n")
    
    return {
        "audio": str(full_audio),
        "subtitles": str(srt_file),
        "total_duration": current_time,
        "segments": len(segments)
    }

def format_time(seconds):
    """Format seconds to SRT time format HH:MM:SS,mmm."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def generate_narration(project_dir):
    """Generate narration.md from opportunities if not exists."""
    opp_file = project_dir / "03-analysis" / "opportunities.json"
    if not opp_file.exists():
        # Fallback: create minimal narration
        text = """# Narration

## Section 1: Hero
今天，我们用 Manufacturing AI Efficiency Pro 的分析框架，深度拆解这款产品。

## Section 2: Painpoint
先看痛点。传统方案效率低下，新产品带来革命性提升。

## Section 3: Opportunities
核心机会：小巧便携、高效续航、精准定位。

## Section 4: Brand
这就是基于 AI 分析框架的深度分析结论。
"""
        out_path = project_dir / "05-webpage" / "narration.md"
        save_text(out_path, text)
        return out_path
    
    # TODO: Generate from opportunities.json
    # For now, create a generic narration
    text = """# Narration

## Section 1: Hero
今天，我们用 Manufacturing AI Efficiency Pro 的分析框架，深度拆解这款产品。

## Section 2: Painpoint
先看痛点。传统方案效率低下，新产品带来革命性提升。

## Section 3: Opportunities
核心机会：小巧便携、高效续航、精准定位。

## Section 4: Brand
这就是基于 AI 分析框架的深度分析结论。
"""
    out_path = project_dir / "05-webpage" / "narration.md"
    save_text(out_path, text)
    return out_path

def parse_narration(narration_path):
    """Parse narration.md into (section_id, text) segments."""
    content = load_text(narration_path)
    segments = []
    current_section = "default"
    current_lines = []
    
    for line in content.split("\n"):
        if line.startswith("## Section"):
            if current_lines:
                segments.append((current_section, " ".join(current_lines).strip()))
                current_lines = []
            # Extract section identifier
            parts = line.replace("## Section", "").strip().split(":")
            current_section = parts[0].strip() if parts else "section"
        elif line.startswith("> "):
            # Quoted narration text
            text = line[2:].strip()
            if text:
                current_lines.append(text)
        elif line.strip() and not line.startswith("#"):
            current_lines.append(line.strip())
    
    if current_lines:
        segments.append((current_section, " ".join(current_lines).strip()))
    
    # If no segments found, create default
    if not segments:
        segments = [("narration", content.strip())]
    
    return segments

# =============================================================================
# Stage 8: COMPOSE - Merge video + audio + subtitles
# =============================================================================

def stage_compose(config, project_dir, voice_result):
    """Compose final video with audio and subtitle burn-in."""
    compose_dir = project_dir / "08-compose"
    compose_dir.mkdir(exist_ok=True)
    
    video_input = project_dir / "06-capture" / "raw-video.mp4"
    audio_input = voice_result.get("audio")
    subtitle_file = voice_result.get("subtitles")
    mode = voice_result.get("mode", "full_tts")
    
    # If video doesn't exist, create from frames or use placeholder
    if not video_input.exists():
        webm_files = list((project_dir / "06-capture").glob("*.webm"))
        if webm_files:
            video_input = webm_files[0]
    
    output = compose_dir / "final_video.mp4"
    
    # Check if we have audio
    if not audio_input or not os.path.exists(audio_input):
        # No audio: just copy video as-is (user can add voice later)
        print(f"No audio available (mode={mode}). Generating video without voiceover.")
        if video_input.exists():
            shutil.copy2(str(video_input), str(output))
        else:
            print("WARNING: No video source found")
            return str(output)
        
        # Also deliver subtitles separately
        if subtitle_file and os.path.exists(subtitle_file):
            shutil.copy2(subtitle_file, compose_dir / "subtitles.srt")
            shutil.copy2(subtitle_file, project_dir / "07-voice" / "subtitles.srt")
        
        return str(output)
    
    # Calculate speed factor to match audio duration
    if video_input.exists():
        video_dur_cmd = subprocess.run(
            [FFPROBE, "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(video_input)],
            capture_output=True, text=True
        )
        video_dur = float(video_dur_cmd.stdout.strip()) if video_dur_cmd.returncode == 0 else 60
    else:
        video_dur = 60
    
    audio_dur = voice_result.get("total_duration", 0)
    speed_factor = video_dur / audio_dur if audio_dur > 0 else 1.0
    
    # Step 1: Adjust video speed
    temp_video = Path(video_input).parent / "temp_video.mp4"
    run_ffmpeg([
        "-y", "-i", str(video_input),
        "-vf", f"setpts={1/speed_factor}*PTS",
        "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        str(temp_video)
    ])
    
    # Step 2: Merge with audio
    run_ffmpeg([
        "-y", "-i", str(temp_video), "-i", str(audio_input),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
        "-shortest", str(output)
    ])
    
    # Step 3: Burn subtitles if available
    if subtitle_file and os.path.exists(subtitle_file):
        import shutil
        srt_copy = str(compose_dir / "subtitles.srt")
        shutil.copy2(subtitle_file, srt_copy)
        
        final_with_subs = compose_dir / "final_video_subs.mp4"
        run_ffmpeg([
            "-y", "-i", str(output),
            "-vf", "subtitles=subtitles.srt",
            "-c:v", "libx264", "-crf", "23", "-preset", "fast",
            "-c:a", "copy",
            str(final_with_subs)
        ])
        if final_with_subs.exists():
            # Replace original with subtitled version
            shutil.move(str(final_with_subs), str(output))
    
    # Cleanup temp
    if temp_video.exists():
        temp_video.unlink()
    
    return str(output)

# =============================================================================
# Stage 9: DELIVER - Package everything
# =============================================================================

def stage_deliver(config, project_dir, final_video):
    """Copy all artifacts to deliver directory."""
    product_name = config.get("product_name", "product").replace(" ", "-").lower()
    date_str = "20260512"  # Could use datetime
    deliver_name = f"{product_name}-{date_str}"
    
    deliver_dir = Path("D:\\demo-dji-mavic3-promo") / "deliver" / deliver_name
    deliver_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy final video
    if os.path.exists(final_video):
        shutil.copy2(final_video, deliver_dir / "final_video.mp4")
    
    # Copy webpage
    webpage_dir = project_dir / "05-webpage"
    if webpage_dir.exists():
        for f in webpage_dir.rglob("*"):
            if f.is_file():
                rel = f.relative_to(webpage_dir)
                dest = deliver_dir / "webpage" / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)
    
    # Copy subtitles
    srt_file = project_dir / "07-voice" / "subtitles.srt"
    if srt_file.exists():
        shutil.copy2(srt_file, deliver_dir / "subtitles.srt")
    
    # Copy audio
    audio_file = project_dir / "07-voice" / "narration.mp3"
    if audio_file.exists():
        shutil.copy2(audio_file, deliver_dir / "narration.mp3")
    
    return str(deliver_dir)

# =============================================================================
# Main entry
# =============================================================================

async def run_pipeline(config, project_dir):
    """Run full pipeline."""
    project_dir = Path(project_dir)
    project_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Pipeline starting: {project_dir}")
    print(f"Config: {json.dumps(config, ensure_ascii=False, indent=2)}")
    
    # Stages 1-6 are assumed to be done (webpage already built)
    # In real usage, these would call the analysis framework skill
    
    print("\n[Stage 7] Generating voiceover...")
    voice_result = stage_voice(config, project_dir)
    print(f"  Audio: {voice_result['audio']}")
    print(f"  Duration: {voice_result['total_duration']:.1f}s")
    print(f"  Segments: {voice_result['segments']}")
    
    print("\n[Stage 8] Composing final video...")
    final_video = stage_compose(config, project_dir, voice_result)
    print(f"  Video: {final_video}")
    
    print("\n[Stage 9] Delivering...")
    deliver_dir = stage_deliver(config, project_dir, final_video)
    print(f"  Deliver: {deliver_dir}")
    
    print("\n[OK] Pipeline complete!")
    return deliver_dir

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", required=True, help="Project working directory")
    parser.add_argument("--config", required=True, help="Path to config JSON")
    args = parser.parse_args()
    
    config = load_json(args.config)
    result = asyncio.run(run_pipeline(config, args.project_dir))
    print(f"\nDelivered to: {result}")
