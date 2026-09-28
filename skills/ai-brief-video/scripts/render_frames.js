#!/usr/bin/env node
/**
 * Playwright 逐帧渲染 HTML 场景。
 * 用法: node render_frames.js <html_path> <timeline.json> <frames_dir>
 *
 * HTML 必须暴露 window.render(idx) 来显示第 idx 句。
 */
const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const [htmlPath, timelinePath, framesDir] = process.argv.slice(2);
  if (!htmlPath || !timelinePath || !framesDir) {
    console.error('usage: node render_frames.js <html> <timeline.json> <frames_dir>');
    process.exit(1);
  }
  const timeline = JSON.parse(fs.readFileSync(timelinePath));
  const fps = 30;
  const totalDur = timeline[timeline.length - 1].end + 0.5;
  const totalFrames = Math.ceil(totalDur * fps);

  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1,
  });
  await page.goto(`file://${htmlPath}`);
  await page.waitForTimeout(600);

  fs.rmSync(framesDir, { recursive: true, force: true });
  fs.mkdirSync(framesDir, { recursive: true });

  for (let f = 0; f < totalFrames; f++) {
    const t = f / fps;
    let lineIdx = 0;
    for (let i = 0; i < timeline.length; i++) {
      if (t >= timeline[i].start - 0.001 && t < timeline[i].end + 0.001) { lineIdx = i; break; }
      if (t < timeline[i].start) { lineIdx = Math.max(0, i - 1); break; }
      if (i === timeline.length - 1) lineIdx = i;
    }
    await page.evaluate((idx) => window.render(idx), lineIdx);
    await page.screenshot({ path: `${framesDir}/${String(f).padStart(5, '0')}.png` });
    if (f % 60 === 0) console.log(`frame ${f}/${totalFrames} (${Math.round(f / totalFrames * 100)}%)`);
  }
  await browser.close();
  console.log('rendered', totalFrames, 'frames');
})();
