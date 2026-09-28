#!/usr/bin/env python3
"""按时间轴把每句音频拼成一条音轨。

用法: python3 mix_audio.py <timeline.json> <audio_dir> <output.aac>
"""
import json, subprocess, sys

def main(timeline_path, audio_dir, output):
    with open(timeline_path) as f:
        tl = json.load(f)
    inputs, filters = [], []
    for i, e in enumerate(tl):
        inputs += ['-i', f'{audio_dir}/line-{i:02d}.mp3']
        delay_ms = int(e['start'] * 1000)
        filters.append(f'[{i}:a]adelay={delay_ms}|{delay_ms},apad=pad_dur=0.2[a{i}]')
    mix = ''.join(f'[a{i}]' for i in range(len(tl))) + \
          f'amix=inputs={len(tl)}:duration=longest:normalize=0[aout]'
    filters.append(mix)
    cmd = ['ffmpeg', '-y'] + inputs + \
          ['-filter_complex', ';'.join(filters),
           '-map', '[aout]', '-c:a', 'aac', '-b:a', '192k', output]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f'audio track -> {output}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
