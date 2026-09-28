---
name: ai-brief-video
description: 把每日 AI 快讯（或任何文字稿）生成猫狗对话式短视频。两个卡通角色（金渐层猫 + 西高地狗）逐句对话，上方配动态讲解场景，EdgeTTS 配音，输出 1080x1920 竖屏 MP4。当用户需要把新闻/快讯/知识内容做成对话形式的竖屏短视频时使用。
---

# AI 快讯对话视频生成

## 适用场景

输入：几条快讯的事实素材（标题+要点+来源）。
输出：1080x1920、30fps、猫狗对话形式的 MP4 短视频，含 TTS 配音和动态讲解场景。

## 依赖

- `python3` + `edge_tts`（TTS）
- `playwright`（Python 或 Node，用于逐帧渲染 HTML）
- `ffmpeg` + `ffprobe`（音频拼接、视频合成）
- Chrome（Playwright 用 `channel:'chrome'`）

## 整体流程

```
素材 → 对话脚本 → TTS 配音 → 时间轴 → HTML 场景 → 逐帧渲染 → 合成视频
```

### 1. 编写对话脚本（dialogue-script.json）

把事实素材改写成 A/B 两人对话。猫（提问者，好奇）用女声，狗（讲解者，沉稳）用男声。每句一个对象：

```json
[
  {"who":"cat","text":"今天有啥新鲜事？"},
  {"who":"dog","text":"三条。第一条，Kimi 出了个浏览器扩展。"}
]
```

要求：基于事实，不编造参数；口语化，每句 10-40 字；结尾给一句总结。

### 2. 生成配音 + 时间轴

运行 `scripts/gen_audio.py <script.json> <out_dir>`：

- 猫用 `zh-CN-XiaoxiaoNeural`，狗用 `zh-CN-YunjianNeural`，语速 `+8%`
- 输出 `audio/line-00.mp3` ... 以及 `timeline-dialogue.json`（含每句 start/end/dur，句间留 0.25s 静音）

### 3. 制作 HTML 场景

从 `assets/dialogue-template.html` 复制到工作目录，修改：

- 角色图片：替换 `.pet.dog img` 和 `.pet.cat img` 的 src（用真实宠物抠图，`rembg` 去背景）
- `window.SCRIPT`：填入对话脚本（带 name 字段）
- 讲解场景：`assets/dialogue-template.html` 内置三套动态场景（Kimi 浏览器录制 / Skild 球场对练 / Colibrì 硬盘搬运），按 `topicFor(idx)` 切换；可自行增删
- `window.render(idx)`：必须暴露到全局，供渲染脚本调用

布局（1080x1920）：顶部品牌条 → 上方动态讲解区（640px高）→ 对话气泡 → 左右角色 → 底部三新闻卡 + 进度条。

### 4. 逐帧渲染

运行 `scripts/render_frames.js <html_path> <timeline.json> <frames_dir>`：

- Playwright 打开 HTML，按 30fps 遍历总时长
- 每帧根据时间找当前句子，调用 `window.render(idx)`
- 输出 `frames/00000.png` ... 

关键：**必须调用页面暴露的 `window.render`**，不要在渲染脚本里重写逻辑，否则场景切换/卡片高亮不会生效。

### 5. 合成视频

```bash
# 合成音频（按时间轴对齐）
python3 scripts/mix_audio.py <timeline.json> <audio_dir> audio/full-track.aac

# 合成视频
ffmpeg -y -framerate 30 -i frames/%05d.png -i audio/full-track.aac \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -shortest output.mp4
```

## 关键决策

| 问题 | 选择 | 原因 |
|------|------|------|
| 角色形象 | 真实宠物照片抠图 | 用户否定 SVG 手绘"奇怪组合"；生图工具不可用时，真实照片最稳 |
| 对话动效 | HTML/CSS 动画 | 角色是 2D 照片，three.js 无加成；CSS 头部晃动+嘴部开合足够 |
| 讲解场景 | HTML/CSS 动态场景 | 不依赖官方静态图，内容与讲解同步（录制/对练/搬运） |
| 配音 | EdgeTTS | 免费、中文质量好、两角色区分度够 |
| 渲染 | Playwright 逐帧截图 | 时间轴精确对齐音频，ffmpeg 合成 |

## 常见坑

- **场景不切换**：渲染脚本没调 `window.render`，而是自己改 DOM。检查渲染脚本是否调用页面暴露的 render。
- **角色嘴部黑点**：叠加的 `.mouth` 元素在 silent 时应 `opacity:0`，只在 `.speaking .mouth` 显示。
- **气泡和角色距离远**：气泡 `top` 要贴近角色头顶（角色 `bottom` + 角色高度 ≈ 气泡底部）。
- **TTS 句间停顿**：时间轴每句 end 后加 0.25s，避免衔接生硬。

## Resources

### scripts/
- `gen_audio.py` — EdgeTTS 生成每句配音 + 时间轴
- `render_frames.js` — Playwright 逐帧渲染（需安装 playwright Node 包）
- `mix_audio.py` — 按时间轴拼接音频

### assets/
- `dialogue-template.html` — 对话场景 HTML 模板（含三套动态讲解场景）
- `pet-dog.png` / `pet-cat.png` — 角色占位图（用真实宠物抠图替换）

### references/
- `workflow.md` — 完整端到端命令示例
