# 端到端工作流示例

以"每日 AI 快讯"为例，从素材到成片。

## 目录结构

```
my-brief/
├── dialogue-script.json      # 对话脚本
├── sources.md                # 事实素材（可选，用于核对）
├── assets/
│   └── (HTML 模板拷贝过来，改 SCRIPT 和角色图)
├── audio/                    # TTS 输出
├── frames/                   # 逐帧渲染输出
├── timeline-dialogue.json    # 时间轴
└── output.mp4                # 成片
```

## 完整命令

```bash
SKILL=/Users/bytedance/Desktop/daily/.agents/skills/ai-brief-video
WORK=/path/to/my-brief
cd $WORK

# 1. 写对话脚本 dialogue-script.json

# 2. TTS + 时间轴
python3 $SKILL/scripts/gen_audio.py dialogue-script.json .

# 3. 拷贝 HTML 模板，修改 SCRIPT 和角色图
cp $SKILL/assets/dialogue-template.html scene.html
cp $SKILL/assets/pet-dog.png .
cp $SKILL/assets/pet-cat.png .
# 编辑 scene.html 的 window.SCRIPT

# 4. 逐帧渲染（Playwright 需全局安装或指定模块路径）
node $SKILL/scripts/render_frames.js scene.html timeline-dialogue.json frames

# 5. 合成音频
python3 $SKILL/scripts/mix_audio.py timeline-dialogue.json audio audio/full-track.aac

# 6. 合成视频
ffmpeg -y -framerate 30 -i frames/%05d.png -i audio/full-track.aac \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -shortest output.mp4
```

## Playwright 模块路径

如果 `require('playwright')` 找不到，用实际安装路径替换脚本顶部，或在脚本同目录装：

```bash
npm install playwright
npx playwright install chromium  # 或用 channel:'chrome' 跳过
```

模板里 `chromium.launch({channel:'chrome'})` 用系统 Chrome，无需单独装 chromium。

## 画面比例

1080x1920 竖屏，30fps。如需横屏，修改 HTML 的 `width/height` 和 Playwright viewport。
