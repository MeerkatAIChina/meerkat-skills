#!/usr/bin/env python3
"""
Webpage capture script for product-promo-video-maker.
Uses Playwright to record scrolling webpage video.
"""
import time
import subprocess
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def capture_webpage(
    server_url: str = "http://localhost:8767",
    output_dir: str = "./06-capture",
    sections_config: list = None,
    viewport_width: int = 1920,
    viewport_height: int = 1080
):
    """
    Record webpage scrolling through all sections.
    
    Args:
        server_url: Local HTTP server URL hosting the webpage
        output_dir: Directory to save captured video
        sections_config: List of (section_id, duration_seconds) tuples
        viewport_width: Browser viewport width
        viewport_height: Browser viewport height
    
    Returns:
        Path to captured raw video file (.webm)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if sections_config is None:
        sections_config = [
            ("hero", 5),
            ("framework", 8),
            ("painpoint", 6),
            ("opportunities", 22),
            ("flowchart", 4),
            ("valuechain", 4),
            ("brand", 4),
        ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        context = browser.new_context(
            viewport={"width": viewport_width, "height": viewport_height},
            record_video_dir=str(output_dir),
            record_video_size={"width": viewport_width, "height": viewport_height}
        )
        page = context.new_page()
        
        # Navigate and wait for full load
        page.goto(server_url)
        page.wait_for_load_state("networkidle")
        time.sleep(2)  # Let particles/animations start
        
        # Scroll through each section
        for section_id, duration in sections_config:
            print(f"Recording section: {section_id} ({duration}s)")
            page.evaluate(
                f"document.getElementById('{section_id}').scrollIntoView({{behavior:'smooth'}})"
            )
            time.sleep(1.5)  # Scroll animation
            
            if section_id == "opportunities":
                # Scroll within section to show multiple cards
                cards = page.query_selector_all(".opportunity-card")
                for i, card in enumerate(cards[:4]):
                    card.scroll_into_view_if_needed()
                    time.sleep(4)
            else:
                time.sleep(duration)
        
        # Scroll back to top
        page.evaluate('window.scrollTo({top:0,behavior:"smooth"})')
        time.sleep(2)
        
        context.close()
        browser.close()
    
    # Find generated webm file
    webm_files = list(output_dir.glob("*.webm"))
    if webm_files:
        webm_path = webm_files[0]
        print(f"Captured: {webm_path}")
        return str(webm_path)
    else:
        raise FileNotFoundError("No video file generated")

def convert_webm_to_mp4(webm_path: str, mp4_path: str = None, ffmpeg_path: str = None):
    """Convert webm to mp4 using ffmpeg."""
    if mp4_path is None:
        mp4_path = str(Path(webm_path).with_suffix(".mp4"))
    if ffmpeg_path is None:
        ffmpeg_path = r"D:\tools\ffmpeg\ffmpeg-8.1.1-essentials_build\bin\ffmpeg.exe"
    
    cmd = [
        ffmpeg_path, "-y", "-i", webm_path,
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        mp4_path
    ]
    subprocess.run(cmd, capture_output=True)
    os.remove(webm_path)
    print(f"Converted to: {mp4_path}")
    return mp4_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-url", default="http://localhost:8767")
    parser.add_argument("--output-dir", default="./06-capture")
    parser.add_argument("--viewport-width", type=int, default=1920)
    parser.add_argument("--viewport-height", type=int, default=1080)
    args = parser.parse_args()
    
    webm = capture_webpage(
        server_url=args.server_url,
        output_dir=args.output_dir,
        viewport_width=args.viewport_width,
        viewport_height=args.viewport_height
    )
    mp4 = convert_webm_to_mp4(webm)
    print(f"Final video: {mp4}")
