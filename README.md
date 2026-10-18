# Eric Skill Hub

可复用的 Agent Skills。

## write-docs

指导 Agent 编写、重写、润色和评审方案、说明、指南、报告、复盘及知识文章：按读者目标和文体组织内容，核验关键事实与数据，主动设计必要图表与阅读引导，通过全文表达编辑、六维评分和读者测试完成修订。指令以中文编写，输出语言按用户需求确定；中文句法建议不套用到其他语言。

- 结构与表达：先检查全文信息推进，再调整句法和措辞；保留作者判断、正式程度及不确定性，减少冗余与机械结构，不依赖禁用词表。
- 证据与准确性：区分事实、推断和假设，注明关键数据口径与来源。
- 图文协同：提炼图内文案、关系与视觉层次，按内容选择成果分区、分层架构或阶段卡片等布局，不固定画风。
- 格式复用：定制图示优先使用 HTML 源稿；支持的平台直接嵌入，否则复用内容与布局生成静态 SVG，必要时输出 PNG。
- 阅读引导：按阅读需要使用摘要、章节引导与高亮，不强制每节重复总结；包含飞书画板与 HTML 内容块说明。
- 质量准出：阻塞问题优先，六维评分结合读者测试，不以高总分掩盖事实错误。

[查看 Skill](skills/write-docs/SKILL.md) · [表达编辑](skills/write-docs/references/prose-editing.md) · [评分量规](skills/write-docs/references/quality-rubric.md)

## ai-hotspot-brief

AI / 互联网热点图文科普内容生产，面向小红书、抖音等平台。支持两种模式：给定主题时做多源调研提炼；未给主题时扫描数据源筛选讨论度高的热点候选。

- 内容深度：一句话定义、核心数据、跨领域横向对比、用户视角 FAQ、金句收尾，卡片数量按信息密度自由决策。
- 言之有据：每个数据点标注来源，配套文案附参考来源 URL，无法验证的信息不写入。
- 交付格式：3:4 竖版 PNG 图文卡片（720×960 高清）+ 不超过 1000 字的配套文案，可直接发布。
- 可读性准出：导出前逐卡检查文字溢出、重叠与行距，PNG 导出后抽检渲染效果。

[查看 Skill](skills/ai-hotspot-brief/SKILL.md)

## 安装

需要可用的 Node.js / npm 环境。

```bash
npx skills add EricOo0/eric-skill-hub --skill write-docs
```

交互选择目标 Agent。也可指定全局安装到 Codex：

```bash
npx skills add EricOo0/eric-skill-hub --skill write-docs -a codex -g
```

查看可用 Skill：

```bash
npx skills add EricOo0/eric-skill-hub --list
```

## 使用

```text
用 write-docs 帮我写这份文档，面向……，希望读者看完能够……
```

```text
用 write-docs 评审这份文档，给出准出判断，先不要修改原文。
```

安装仅提供写作与评审指令，不会自动配置飞书账号、授权或其他外部工具。相关操作使用运行环境中实际可用的能力。
