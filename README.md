# Eric Skill Hub

可复用的 Agent Skills。

## write-docs

指导 Agent 编写、重写和评审文档：按读者目标组织结构，核验关键事实与数据，主动设计图表、摘要和阅读引导，并通过六维评分与准出检查完成修订。指令以中文编写，输出文档的语言按用户需求确定。

- 结构与表达：层次递进、措辞具体、减少冗余和重复。
- 证据与准确性：区分事实、推断和假设，注明关键数据口径与来源。
- 图文协同：提炼图内文案、关系与视觉层次，按内容选择成果分区、分层架构或阶段卡片等布局，不固定画风。
- 格式复用：定制图示优先使用 HTML 源稿；支持的平台直接嵌入，否则复用内容与布局生成静态 SVG，必要时输出 PNG。
- 阅读引导：通过摘要、章节结论与高亮块组织长文，包含飞书画板与 HTML 内容块说明。
- 质量准出：阻塞问题优先，六维评分结合读者测试，不以高总分掩盖事实错误。

[查看 Skill](skills/write-docs/SKILL.md) · [评分量规](skills/write-docs/references/quality-rubric.md)

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
