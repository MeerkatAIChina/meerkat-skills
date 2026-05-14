# Subtitle Guide

## Subtitle Generation

The skill generates `.srt` subtitle files during Stage 7 (VOICE).

### SRT Format

```
1
00:00:00,000 --> 00:00:08,690
今天，我们用 Manufacturing AI Efficiency Pro 分析框架...

2
00:00:08,690 --> 00:00:32,000
先看痛点。传统方案...
```

### Timing Accuracy

Each subtitle entry is timed based on actual TTS audio duration:
- Start time = cumulative duration of all previous segments
- End time = start + current segment duration
- Precision: millisecond

### Burn-in Limitations (Windows)

The ffmpeg `subtitles` filter on Windows has path parsing issues. Current workarounds:

1. **Separate SRT delivery** (default) — Deliver `.srt` as standalone file
   - User imports into video editor (剪映/PR/DaVinci)
   - Or use video player that supports external SRT (VLC, PotPlayer)

2. **Manual burn-in** — If you need hardcoded subtitles:
   ```bash
   ffmpeg -i video.mp4 -vf "subtitles='subtitles.srt':force_style='FontSize=24'" output.mp4
   ```
   Note: Run in WSL or Linux environment for reliable subtitle burn-in.

3. **Video editor import** (recommended for production):
   - 剪映: Import video → Text → Import subtitles → Select SRT
   - Premiere Pro: File → Import → Select SRT
   - DaVinci Resolve: Media Pool → Import SRT

### Subtitle Styling

Default style in generated SRT:
- Font: System default sans-serif
- Size: 24px (configurable)
- Color: White with black outline
- Position: Bottom margin 40px

### Future Improvements

- Add `ass` (Advanced SubStation Alpha) format support for richer styling
- Add `vtt` (WebVTT) format for web playback
- Integrate subtitle burn-in via Python `ffmpeg-python` wrapper with proper escaping
