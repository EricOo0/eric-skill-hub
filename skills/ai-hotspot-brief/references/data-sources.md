# 数据源清单与检索策略

## 一、数据源分级

### S 级（一手权威，优先引用）
- **官方博客/文档**：OpenAI、Google DeepMind、Anthropic、Meta AI、字节跳动等公司的官方发布页
- **论文原文**：arXiv、Nature、Science 等
- **官方定价页/产品页**：用于价格、参数等精确数据

### A 级（专业媒体，信息可靠）
**中文**：
- 量子位（qbitai.com）
- 机器之心（jiqizhixin.com）
- 新智元（jiqizhixin.com 旗下）
- 36氪、虎嗅、晚点LatePost（商业+深度）
- AI 工具导航：未来工具集、ajay.cc、AI基地

**英文**：
- TechCrunch、The Verge、Ars Technica
- Hacker News（news.ycombinator.com）
- Product Hunt（producthunt.com）
- GitHub Trending（github.com/trending）

### B 级（社区讨论，用于补充观点）
- X/Twitter（关注各 AI 公司官方账号和知名研究员）
- Reddit（r/MachineLearning、r/LocalLLaMA）
- 知乎热榜、即刻、微博热搜

## 二、检索策略

### 给定主题时（调研模式）
1. **先搜官方源**：用 `<公司名> <产品名> official` 或直接访问公司官网
2. **再搜专业媒体**：用 `<产品名> site:techcrunch.com` 等限定域名
3. **补充社区讨论**：X/Reddit 看真实反馈
4. **至少 3 个独立来源交叉验证**数据点

### 无主题时（选题模式）
按以下顺序扫描，筛选标准：**信息充足 + 讨论热度高**：
1. Hacker News 首页 top 10
2. 量子位 / 机器之心 最新文章
3. Product Hunt 今日 top 5
4. X 上 AI 领域热帖
5. arXiv 今日 cs.AI 新论文

筛选出 3-5 个候选，每个附一句话说明 + 预估信息密度，让用户选。

## 三、搜索技巧

- 用 `WebSearch` 时优先英文查询（海外源更全），再用中文补充
- 精确数据用 `WebFetch` 直接抓官方页面
- 价格/参数类数据**必须**到官方页面确认，不能只信媒体报道
- 发现多源数据矛盾时，以官方源为准并标注差异

## 四、避免使用的源
- 未经证实的自媒体爆料（除非有官方确认）
- 营销软文、PR 通稿（仅作背景参考）
- 已被官方否认的传闻
