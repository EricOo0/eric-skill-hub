#!/usr/bin/env python3
"""EdgeTTS 生成每句配音 + 时间轴。

用法: python3 gen_audio.py <script.json> <out_dir>

script.json: [{"who":"cat","text":"..."}, ...]
out_dir: 输出 audio/line-XX.mp3 和 timeline-dialogue.json
"""
import asyncio, sys, os, json, subprocess
import edge_tts

VOICES = {'cat': 'zh-CN-XiaoxiaoNeural', 'dog': 'zh-CN-YunjianNeural'}
RATE = '+8%'
GAP = 0.25  # 句间停顿秒

async def gen(script_path, out_dir):
    with open(script_path) as f:
        lines = json.load(f)
    audio_dir = os.path.join(out_dir, 'audio')
    os.makedirs(audio_dir, exist_ok=True)

    for i, line in enumerate(lines):
        out = os.path.join(audio_dir, f'line-{i:02d}.mp3')
        if not os.path.exists(out):
            comm = edge_tts.Communicate(line['text'], VOICES[line['who']], rate=RATE)
            await comm.save(out)

    # 计算时间轴
    timeline = []
    t = 0.0
    for i, line in enumerate(lines):
        mp3 = os.path.join(audio_dir, f'line-{i:02d}.mp3')
        r = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
             '-of', 'default=noprint_wrappers=1:nokey=1', mp3],
            capture_output=True, text=True)
        dur = float(r.stdout.strip())
        timeline.append({
            **line, 'line': i,
            'start': round(t, 2),
            'end': round(t + dur, 2),
            'dur': round(dur, 2),
        })
        t += dur + GAP

    tl_path = os.path.join(out_dir, 'timeline-dialogue.json')
    with open(tl_path, 'w') as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)
    print(f"done: {len(timeline)} lines, total {round(t,1)}s -> {tl_path}")

if __name__ == '__main__':
    asyncio.run(gen(sys.argv[1], sys.argv[2]))
