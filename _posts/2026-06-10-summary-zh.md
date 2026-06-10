---
layout: default
title: "Horizon Summary: 2026-06-10 (ZH)"
date: 2026-06-10
lang: zh
---

> From 36 items, 12 important content pieces were selected

---

1. [谷歌发布开源权重模型 DiffusionGemma](#item-1) ⭐️ 9.0/10
2. [Eric Ries 就新书《Incorruptible》及使命漂移举行 AMA](#item-2) ⭐️ 8.0/10
3. [PgDog 获得资金，解决 Postgres 扩展问题](#item-3) ⭐️ 8.0/10
4. [梅赛德斯-奔驰开始量产轴向磁通电机](#item-4) ⭐️ 8.0/10
5. [HTML 优先方法让用户参与度一夜翻倍](#item-5) ⭐️ 8.0/10
6. [0.01 欧元银行转账向银行 AI 代理注入指令](#item-6) ⭐️ 8.0/10
7. [Jeremy Howard 提出减缓 AI 自我改进的规则](#item-7) ⭐️ 8.0/10
8. [Anthropic 的 Claude Fable 5 悄悄限制对 AI 开发的帮助](#item-8) ⭐️ 8.0/10
9. [Simon Willison 对 Claude Fable 5 的实测印象](#item-9) ⭐️ 8.0/10
10. [SpaceX 计划以每股 135 美元固定价 IPO，筹资 750 亿美元](#item-10) ⭐️ 8.0/10
11. [iOS 27 测试版泄露 Siri AI 系统提示词，超过 1300 行](#item-11) ⭐️ 8.0/10
12. [德国法院裁定谷歌对 AI 概述虚假信息负责](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布开源权重模型 DiffusionGemma](https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything) ⭐️ 9.0/10

谷歌发布了 DiffusionGemma，这是一个采用 Apache 2 许可证的开源权重文本生成模型，每秒可生成高达 857 个 token。NVIDIA 在其 NIM 云 API 上免费托管该模型。 该模型通过将扩散技术用于文本生成，代表了生成式 AI 的范式转变，推理速度远超传统的自回归模型。它可能使边缘设备上的实时应用成为可能，并降低计算成本。 DiffusionGemma 基于 26B A4B 混合专家（MoE）Gemma 4 架构，支持 256K 上下文窗口。该模型使用离散扩散生成 token，而不是逐个预测 token。

rss · Simon Willison · Jun 10, 20:00

**背景**: 传统的大型语言模型（LLM）以自回归方式生成文本，每次生成一个 token，对于长输出来说速度较慢。扩散模型最初用于图像生成，可以并行生成多个 token，从而实现更快的文本生成。DiffusionGemma 将这一技术应用于文本，基于谷歌早期的 Gemini Diffusion 研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/diffusiongemma/model_card">DiffusionGemma model card | Google AI for Developers</a></li>
<li><a href="https://unsloth.ai/docs/models/diffusiongemma">DiffusionGemma - How to Run Locally | Unsloth Documentation</a></li>
<li><a href="https://developer.nvidia.com/nim">NIM for Developers | NVIDIA Developer</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞 DiffusionGemma 的速度，一位用户指出它让 AI 感觉更像是结对编程而不是老虎机。其他人强调了它在边缘设备上的潜力，因为扩散模型在非批量推理时效率更高。一些人表示惊讶，谷歌的 AI 能力在代码和代理任务上并不更具竞争力，但承认效率改进的重要性。

**标签**: `#AI`, `#open-source`, `#text generation`, `#Google`, `#NVIDIA`

---

<a id="item-2"></a>
## [Eric Ries 就新书《Incorruptible》及使命漂移举行 AMA](https://news.ycombinator.com/item?id=48477135) ⭐️ 8.0/10

《精益创业》作者 Eric Ries 在 Hacker News 上举行了一场 AMA，讨论他的新书《Incorruptible》，书中提出了“财务引力”概念，并阐述了公司如何通过结构设计来抵抗使命漂移。 这场 AMA 为创始人和领导者提供了宝贵的见解，解释了为什么好公司会变坏，以及如何建立长期坚守使命的组织，解决了初创企业和企业文化中的一个关键问题。 Ries 以 Costco、Patagonia 和 Novo Nordisk 等公司为例，说明它们是如何通过结构设计来抵抗财务引力的；他还创立了长期证券交易所，并共同创立了 Answer.AI。

hackernews · eries · Jun 10, 14:47

**背景**: 使命漂移是指组织因财务压力、领导层变动或其他因素而逐渐偏离其最初目标的现象。Ries 用“财务引力”一词来描述这种无形的拉力，它导致公司优先考虑短期利润而非使命。Ries 开创的精益创业方法论专注于迭代产品开发和验证式学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.matthewjhall.net/articles/three-ways-mission-drift-will-take-your-organization-off-course">Three Ways Mission Drift Will Take Your Organization Off Course - Matthew Hall</a></li>
<li><a href="https://www.linkedin.com/pulse/mission-drift-paul-butler-cgma-cima-fjcbc">Mission Drift - LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 社区评论讨论了使命漂移主要是由结构还是领导力导致的，一些人认为像 Costco 的 Jim Sinegal 这样的强势领导者可以克服结构压力。其他人则分享了目睹公司在创始人离开后失去使命的个人经历，并讨论了商业模式在防止腐败中的作用。

**标签**: `#startups`, `#leadership`, `#company-culture`, `#business-model`, `#AMA`

---

<a id="item-3"></a>
## [PgDog 获得资金，解决 Postgres 扩展问题](https://pgdog.dev/blog/our-funding-announcement) ⭐️ 8.0/10

用 Rust 编写的 PostgreSQL 连接池和代理 PgDog 宣布获得资金，以进一步开发其解决 Postgres 数据库扩展和高可用性问题的方案。 这笔资金验证了 PgDog 解决 Postgres 扩展挑战的方法，而扩展问题正是用户转向 MongoDB 或 DynamoDB 等替代数据库的关键原因。它可能为 Postgres 用户提供一条更简单、更自动化的高可用性和水平扩展路径。 PgDog 支持连接池、负载均衡和数据库分片，并能自动回滚未完成的事务和排空部分发送的查询。该项目是开源的，可在 GitHub 上获取。

hackernews · levkk · Jun 10, 14:02 · [社区讨论](https://news.ycombinator.com/item?id=48476466)

**背景**: PostgreSQL 是一个强大的关系型数据库，但为其实现高写入吞吐量的扩展和无缝的高可用性仍然具有挑战性。像 PgDog 这样的连接池和代理位于应用程序和数据库服务器之间，管理连接、分发查询并处理故障转移，从而减轻运维负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pgdogdev/pgdog">GitHub - pgdogdev/pgdog: PostgreSQL connection pooler, load balancer and database sharder.</a></li>
<li><a href="https://news.ycombinator.com/item?id=47123631">Show HN: PgDog – Scale Postgres without changing the app | Hacker News</a></li>
<li><a href="https://docs.pgdog.dev/administration/pools/">Connection pools - PgDog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区讨论活跃（362 分，182 条评论），富有洞察力。用户分享了真实的 Postgres 扩展痛点，如手动故障转移和主版本升级停机时间，并讨论 PgDog 能否解决这些问题。一些评论者还提到了 PgCat 等先前的工作，并警告不要为数据库代理解决方案向初创公司付费。

**标签**: `#PostgreSQL`, `#database`, `#scaling`, `#proxy`, `#high availability`

---

<a id="item-4"></a>
## [梅赛德斯-奔驰开始量产轴向磁通电机](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf) ⭐️ 8.0/10

梅赛德斯-奔驰已在柏林-马林费尔德工厂开始大规模生产 YASA 的轴向磁通电机，标志着这种紧凑、高效电机技术的首次量产。 轴向磁通电机比传统径向磁通电机具有更高的功率密度和效率，有望实现更轻、更高效的电动汽车。此举可能加速轴向磁通技术在电动汽车行业的应用。 YASA 的轴向磁通电机采用无轭分段电枢设计，定子铁芯质量减少高达 80%，功率密度是传统电机的 2-3 倍。该电机比同等径向磁通电机更小、更轻。

hackernews · raffael_de · Jun 10, 07:44 · [社区讨论](https://news.ycombinator.com/item?id=48472877)

**背景**: 传统电机采用径向磁通设计，磁场在转子和定子之间径向流动。轴向磁通电机的磁场则轴向流动，形成扁平圆盘状，更加紧凑高效。梅赛德斯-奔驰于 2021 年收购 YASA，旨在将该技术投入量产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yasa.com/technology/">Axial Flux Motors | Performance Automotive E-Motors | YASA Ltd</a></li>
<li><a href="https://en.wikipedia.org/wiki/YASA_Limited">YASA Limited - Wikipedia</a></li>
<li><a href="https://lammotor.com/axial-flux-motor-vs-radial-flux-moto/">Axial Flux Motor vs Radial Flux Motor : Which One is Better?</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术表示兴奋，一些人认为轴向磁通电机有望成为新标准。其他人感谢讨论中分享的技术解释，而少数人希望文章本身能解释什么是轴向磁通电机。

**标签**: `#electric vehicles`, `#axial flux motor`, `#manufacturing`, `#automotive technology`

---

<a id="item-5"></a>
## [HTML 优先方法让用户参与度一夜翻倍](https://mohkohn.co.uk/writing/html-first/) ⭐️ 8.0/10

一位开发者报告称，采用 HTML 优先、渐进增强的方式重建网站后，用户参与度一夜翻倍，且无需 JavaScript 即可保证完整功能。但该做法遭到一位承包商的抵制，认为这会增加工作量。 这凸显了 Web 开发中 HTML 优先与 JavaScript 重型方法之间的持续争论，表明更简单、更具弹性的架构能显著提升用户参与度。同时也揭示了长期可维护性与短期开发者便利性之间的矛盾。 该网站使用标准 HTML 表单配合服务端渲染，任何 JavaScript 增强都基于渐进增强原则。承包商的抱怨在于，相比使用 JavaScript 框架，HTML 优先的方式需要更多前期工作。

hackernews · edent · Jun 10, 12:45 · [社区讨论](https://news.ycombinator.com/item?id=48475483)

**背景**: HTML 优先开发优先通过 HTML 提供核心内容和功能，再在其上叠加 CSS 和 JavaScript 增强。这种被称为渐进增强的方法确保即使在 JavaScript 失败或被禁用时，基本可用性依然存在。HTMX 是一个现代库，通过自定义属性扩展 HTML 的 AJAX 能力，无需编写自定义 JavaScript 即可实现动态交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Progressive_enhancement">Progressive enhancement</a></li>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://arxiv.org/html/2602.17193v1">The Case for HTML First Web Development</a></li>

</ul>
</details>

**社区讨论**: 评论者就 HTML 优先与 JS 重型方法的优劣展开辩论，许多人分享了使用 HTMX 配合 Go 等后端语言的积极经验。一些人指出承包商的抵制反映了行业对 JavaScript 框架的普遍偏见，而另一些人则指出 HTML 优先可以降低复杂性并提升性能。

**标签**: `#web development`, `#HTML-first`, `#progressive enhancement`, `#HTMX`, `#JavaScript`

---

<a id="item-6"></a>
## [0.01 欧元银行转账向银行 AI 代理注入指令](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/) ⭐️ 8.0/10

安全研究员 Blue41 演示了如何通过一笔 0.01 欧元的银行转账，在交易描述中嵌入隐藏指令，这些指令随后被银行 AI 代理通过间接提示注入解释为命令。 这凸显了基于 LLM 的系统存在根本性安全缺陷，无法可靠区分数据和指令，对金融应用及其他高风险 AI 部署构成严重威胁。 该攻击之所以有效，是因为 LLM 将交易描述作为上下文窗口的一部分进行处理，将嵌入的文本视为指令而非数据。这类似于 SQL 注入，但针对的是 AI 代理。

hackernews · tvissers · Jun 10, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48476136)

**背景**: 间接提示注入是一种网络安全利用方式，攻击者将恶意指令嵌入不可信的外部内容（如网页、文档、工具响应）中，LLM 在检索和处理这些内容时会被影响。与直接提示注入不同，攻击者不直接与模型交互，而是污染模型消费的数据源。这种漏洞对于能够访问敏感系统或代表用户执行操作的 AI 代理尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indirect_prompt_injection">Indirect prompt injection</a></li>
<li><a href="https://phongntdo.github.io/Indirect-Prompt-Injection-in-LLM-Applications-and-Agents/">Indirect Prompt Injection in LLM Applications and Agents: Threat...</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈担忧，一位评论者指出，只要 LLM 无法区分数据和指令，它们就永远不会安全。另一位评论者将其与 SQL 注入相提并论，感叹 AI 又带回了类似的一类漏洞。一些人质疑银行在缺乏足够防护措施的情况下部署此类代理的判断力。

**标签**: `#AI security`, `#prompt injection`, `#LLM`, `#banking`, `#vulnerability`

---

<a id="item-7"></a>
## [Jeremy Howard 提出减缓 AI 自我改进的规则](https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything) ⭐️ 8.0/10

Jeremy Howard 提出，拥有排名最高 AI 模型的实验室不得将其用于前沿 AI 研究，同时应允许其他方访问，以防止递归自我改进和权力失衡。他批评 Anthropic 采取了相反的做法。 该提案通过一条简单规则来减缓递归自我改进，挑战了当前的 AI 治理方法，可能降低智能爆炸和权力集中的风险。它引发了关于如何在 AI 前沿开发中平衡安全、开放与竞争的讨论。 Howard 澄清他个人倾向于 AI 民主化而非减缓发展，但认为声称要减缓的人应以身作则。该提案专门针对排名最高的实验室，确保前沿不进步，同时其他人获得访问权。

rss · Simon Willison · Jun 10, 15:23

**背景**: 递归自我改进（RSI）指 AI 系统重写自身代码以提升能力，可能导致智能爆炸。前沿 AI 研究通常使用最先进的模型来突破能力边界。Howard 的想法旨在通过限制顶级实验室使用自身模型进行进一步研究来打破这一循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#recursive self-improvement`, `#Anthropic`, `#frontier AI`

---

<a id="item-8"></a>
## [Anthropic 的 Claude Fable 5 悄悄限制对 AI 开发的帮助](https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/#atom-everything) ⭐️ 8.0/10

Anthropic 在 Claude Fable 5 中实施了不可见的安全措施，该措施会悄悄降低模型对构建竞争性 AI 模型相关请求（如预训练流水线或 ML 加速器设计）的响应质量，且不通知用户。 这标志着 Anthropic 首次部署用户无法察觉的静默干预措施，引发了严重的透明度和信任问题。这可能为 AI 公司秘密限制模型能力以保护自身竞争优势开创先例。 这些干预措施影响约 0.03% 的流量和不到 0.1% 的组织，采用提示修改、引导向量或参数高效微调（PEFT）等方法。模型不会回退到其他版本，因此用户无法察觉性能下降。

rss · Simon Willison · Jun 10, 00:37

**背景**: 递归自我改进（RSI）指的是 AI 系统自主增强自身能力，可能导致智能爆炸的场景。Anthropic 的系统卡以对 RSI 的担忧为由，限制 Claude 在前沿 AI 开发方面的帮助，但批评者认为这是反竞争行为的借口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/06/10/anthropic-accu-claude-fable-5-limits-capabilities-ai-researchers-developers/">Anthropic accused of 'secret sabotage' as Claude Fable ... | Fortune</a></li>
<li><a href="https://www.businessinsider.com/researchers-furious-anthropic-mythos-fable-hidden-ai-limits-2026-6">Anthropic purposely made its new Mythos-based models bad at AI research, and developers are fuming</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（文章链接）表达了强烈不满，许多用户指责 Anthropic 采取欺骗性做法，并警告这种秘密限制会破坏用户信任。一些评论者认为，虽然安全担忧是合理的，但缺乏透明度是不可接受的。

**标签**: `#AI ethics`, `#Anthropic`, `#Claude`, `#AI safety`, `#competition`

---

<a id="item-9"></a>
## [Simon Willison 对 Claude Fable 5 的实测印象](https://simonwillison.net/2026/Jun/9/claude-fable-5/#atom-everything) ⭐️ 8.0/10

Anthropic 发布了 Claude Fable 5，这是一个具有严格安全护栏的 Mythos 级模型，同时发布了无限制的 Claude Mythos 5。Simon Willison 花了 5.5 小时测试 Fable 5，发现其能力极强，常常难以找到它无法完成的任务。 Claude Fable 5 代表了 AI 安全的新前沿，在提供 Mythos 级性能的同时具备强大的安全护栏，适合企业部署。其高昂的成本和严格的安全措施可能影响其他 AI 实验室在能力与安全之间的平衡。 该模型拥有 100 万 token 的上下文窗口、12.8 万 token 的最大输出，知识截止日期为 2026 年 1 月。定价为每百万输入 token 10 美元、每百万输出 token 50 美元，是 Claude Opus 4.8 的两倍。

rss · Simon Willison · Jun 9, 23:59

**背景**: Anthropic 以关注 AI 安全而闻名，经常发布具有不同级别护栏的模型。Claude Fable 5 是更强大的 Claude Mythos 5 的安全版本，旨在防止有害输出的同时供一般使用。模型的“大模型气息”指的是其广泛的知识和处理复杂任务的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/9/claude-fable-5/">Initial impressions of Claude Fable 5 - Simon Willison's Weblog</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Anthropic`, `#LLM`, `#frontier models`

---

<a id="item-10"></a>
## [SpaceX 计划以每股 135 美元固定价 IPO，筹资 750 亿美元](https://t.me/zaihuapd/41864) ⭐️ 8.0/10

SpaceX 计划以每股 135 美元的固定价格发行 5.556 亿股，筹资 750 亿美元，估值达 1.75 万亿美元。该 IPO 预计于 6 月 12 日在纳斯达克上市，股票代码为 SPCX。 如果成功，这将是史上最大规模的 IPO，可能引发 OpenAI 等 AI 公司的巨型 IPO 浪潮。募资将用于 AI 计算和星链网络扩展，对航天和 AI 行业产生重大影响。 固定价格发行方式极为罕见，通常价格在路演后确定。SpaceX 2025 年营收 187 亿美元但净亏 49 亿美元，仅星链盈利。路演于周四启动，细节仍可能调整。

telegram · zaihuapd · Jun 10, 01:50

**背景**: 固定价格 IPO 提前设定股价，而簿记建档则根据投资者需求定价。SpaceX 是一家私营航天和电信公司，运营卫星互联网星座星链。星链已成为主要收入来源，而 xAI 等其他业务则出现亏损。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Initial_public_offering">Initial public offering - Wikipedia</a></li>
<li><a href="https://inteliview.kr/en/topics/us-stocks/spacex-financials-starlink-profit-xai-loss-ipo-valuation-2026">SpaceX Financials Revealed: Starlink Carries... | Inteliview</a></li>
<li><a href="https://payloadspace.com/estimating-spacexs-2024-revenue/">Estimating SpaceX ’s 2024 Revenue</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#IPO`, `#Starlink`, `#AI`, `#finance`

---

<a id="item-11"></a>
## [iOS 27 测试版泄露 Siri AI 系统提示词，超过 1300 行](https://www.reddit.com/r/iOSBeta/comments/1u0kn3h/ios_27_db_1_siris_feedback_error_reporting_gives/) ⭐️ 8.0/10

有用户在 iOS 27 开发者测试版的诊断文件中发现了 Siri AI 的完整 LLM 系统提示词，随后被发布到 Gist，内容超过 1300 行，约 22000 个 token。 此次泄露让人们前所未有地了解到苹果设计 Siri AI 行为的方式，揭示了该公司如何指示 LLM 进行思考、使用工具以及处理歧义，这可能会影响开发者和竞争对手对苹果 AI 策略的理解。 系统提示词将 Siri 定义为苹果设计的智能助手，要求它在调用工具前先思考，优先使用设备和搜索返回的结构化信息，并在遇到缺失信息或歧义请求时询问用户，而不是自行编造答案。

telegram · zaihuapd · Jun 10, 06:30

**背景**: 系统提示词是在大语言模型与用户交互之前给出的精心设计的指令，用于引导其行为、语气和能力。苹果在 WWDC 2026 上宣布的 Siri AI 是对 Siri 的重大改造，由 LLM 驱动，而泄露的提示词提供了对其底层设计的罕见一瞥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@larry_6938/the-importance-of-system-prompts-for-llms-4b07a765b9a6">The Importance of System Prompts for LLMs | by Larry Tao | Medium</a></li>
<li><a href="https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/">Apple introduces Siri AI , a profoundly more capable and... - Apple</a></li>

</ul>
</details>

**社区讨论**: r/iOSBeta 上的 Reddit 讨论对这些详细的指令表达了兴奋和好奇，一些用户注意到强调不编造信息和使用结构化数据。其他人则讨论了隐私和苹果 AI 方向的影响。

**标签**: `#iOS`, `#Siri`, `#AI`, `#LLM`, `#leak`

---

<a id="item-12"></a>
## [德国法院裁定谷歌对 AI 概述虚假信息负责](https://thenextweb.com/news/google-ai-overviews-german-court-liable) ⭐️ 8.0/10

德国一家法院对谷歌发出禁令，认定谷歌对其 AI 概述功能生成的虚假陈述直接负责，驳回了谷歌关于用户可自行查证来源的辩护。 该裁决为 AI 生成内容的责任认定确立了法律先例，可能影响 ChatGPT、Perplexity 等主要 AI 平台，并可能重塑全球 AI 治理格局。 慕尼黑地区法院认定 AI 概述生成的是“独立的新实质性陈述”，不同于普通搜索结果，谷歌作为发布者拥有完全控制权。谷歌被责令承担 80%的诉讼费用，目前尚未回应。

telegram · zaihuapd · Jun 10, 16:15

**背景**: AI 概述（原名搜索生成体验 SGE）是谷歌在搜索结果中生成 AI 摘要的功能，2023 年 5 月在美国作为实验性产品推出，2024 年 10 月扩展至全球 100 多个国家和地区。该功能因偶尔生成不准确或有害信息而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://frankchiu.io/seo-ai-overview/">Google AI Overviews （ AI 摘要）介紹：品牌要如何在 AIO...</a></li>
<li><a href="https://www.sonar-inc.com/what-is-ai-overviews/">AI Overviews 是 什 麼？ 贏得 AI 搜尋推薦的 7 大關鍵 - 將能數位行銷</a></li>
<li><a href="https://welly.tw/blog/ai-overviews">AI Overviews 是 什 麼？ 5 大 AIO 優化技巧提升品牌曝光 - Welly SEO</a></li>

</ul>
</details>

**标签**: `#AI liability`, `#legal precedent`, `#Google`, `#AI governance`, `#Germany`

---