---
layout: default
title: "Horizon Summary: 2026-06-05 (ZH)"
date: 2026-06-05
lang: zh
---

> From 34 items, 7 important content pieces were selected

---

1. [微软开源 pg_durable，实现数据库内持久执行](#item-1) ⭐️ 8.0/10
2. [谷歌发布 Gemma 4 QAT 模型，提升移动端和笔记本端 AI 效率](#item-2) ⭐️ 8.0/10
3. [俄罗斯卫星 Cosmos 2546 被指干扰欧洲 GNSS 信号](#item-3) ⭐️ 8.0/10
4. [Ladybird 浏览器因 AI 代码禁止公开拉取请求](#item-4) ⭐️ 8.0/10
5. [AI 爱好者与怀疑者：与时间赛跑 vs. 对抗熵增](#item-5) ⭐️ 8.0/10
6. [五角大楼或因 AI 军事限制终止与 Anthropic 合作](#item-6) ⭐️ 8.0/10
7. [Anthropic 呼吁全球放缓前沿 AI 开发](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软开源 pg_durable，实现数据库内持久执行](https://github.com/microsoft/pg_durable) ⭐️ 8.0/10

微软开源了 pg_durable，这是一个 PostgreSQL 扩展，支持在数据库内持久执行工作流，允许开发者定义多步骤 SQL 工作流，并在失败后自动检查点并恢复执行。 这直接将持久执行能力引入 PostgreSQL，减少了在某些场景下对外部工作流编排器（如 Temporal）的需求，并通过微软提供的生产级解决方案增强了 Postgres 生态系统。 pg_durable 基于两个 Rust 库构建：duroxide 提供编排运行时，另一个库负责检查点，并通过 SQL DSL 构建函数图。它是 Azure HorizonDB 内部的持久执行引擎。

hackernews · coffeemug · Jun 5, 15:59 · [社区讨论](https://news.ycombinator.com/item?id=48414367)

**背景**: 持久执行通过在每一步检查点状态来确保长时间运行的工作流在崩溃后仍能存活。传统上，这需要外部系统如 Temporal 或 Azure Durable Functions。pg_durable 将此能力直接嵌入 PostgreSQL，允许在数据库内定义和执行工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/pg_durable">GitHub - microsoft/pg_durable: PostgreSQL in-database durable execution</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/horizondb/development/durable-functions">Durable Functions in Azure HorizonDB - Azure HorizonDB | Microsoft Learn</a></li>
<li><a href="https://temporal.io/blog/what-is-durable-execution">The definitive guide to Durable Execution | Temporal</a></li>

</ul>
</details>

**社区讨论**: 社区对不断增长的 Postgres 队列生态系统感到兴奋，评论提到了 DBOS 和 pgQue 等替代方案。一些用户质疑 pg_durable 与 Temporal 相比如何，特别是当工作流跨越异构系统时。其他人则对 Azure PostgreSQL 在支持此类扩展方面滞后表示不满。

**标签**: `#PostgreSQL`, `#durable execution`, `#Microsoft`, `#open source`, `#workflow`

---

<a id="item-2"></a>
## [谷歌发布 Gemma 4 QAT 模型，提升移动端和笔记本端 AI 效率](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) ⭐️ 8.0/10

谷歌发布了 Gemma 4 系列的官方量化感知训练（QAT）模型，能够在移动设备和笔记本电脑上实现高效部署，且精度损失极小。 此次发布使强大的 Gemma 4 模型在设备端 AI 中变得实用，开发者可以在手机、笔记本等资源受限的硬件上运行高级推理和智能体工作流。 QAT 模型包括 Gemma 4 12B 的 4 位量化版本（Q4_0），仅需 6.7GB 显存，可轻松适配 16GB 内存。社区测试显示，量化模型相比未量化的 BF16 版本实现了接近 100%的准确率。

hackernews · theanonymousone · Jun 5, 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48414653)

**背景**: 量化感知训练（QAT）是一种将权重精度降低融入模型训练过程的技术，可在压缩时最小化精度损失。Gemma 4 是谷歌最新的开放模型系列，专为高级推理和智能体任务设计。设备端 AI 要求模型足够小以在本地运行而无需云连接，因此 QAT 等压缩技术至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Gemma 生态系统的快速进展印象深刻，注意到多 token 预测和官方量化版本的发布。一些用户报告在 Mac 和手机上成功本地运行，而另一些用户则将谷歌的 QAT 模型与 Unsloth 等第三方方案进行比较，后者声称精度更高。

**标签**: `#quantization`, `#Gemma 4`, `#on-device AI`, `#model compression`, `#efficiency`

---

<a id="item-3"></a>
## [俄罗斯卫星 Cosmos 2546 被指干扰欧洲 GNSS 信号](https://arxiv.org/abs/2606.03673) ⭐️ 8.0/10

一篇研究论文通过多种技术手段，以高置信度识别出俄罗斯卫星 Cosmos 2546（NORAD 编号 45608）是自 2019 年以来欧洲范围内 GNSS 干扰的来源之一。 这一发现具有重要的地缘政治和技术意义，它将广泛的 GNSS 信号降级归因于一颗特定的俄罗斯预警卫星，可能加剧紧张局势并促使采取反制措施。 该卫星属于俄罗斯“统一太空系统”（EKS）预警星座，论文指出整个星座可能共同导致了干扰。该卫星运行在高度椭圆轨道（1380–38976 公里），倾角 63.2°。

hackernews · mimorigasaka · Jun 5, 08:32 · [社区讨论](https://news.ycombinator.com/item?id=48409664)

**背景**: GNSS（全球导航卫星系统）信号（如 GPS）到达地面时极其微弱，因此容易受到干扰。干扰可能是有意或无意的，识别干扰源需要对信号特征和卫星位置进行复杂分析。Cosmos 2546 卫星于 2020 年 5 月发射，由俄罗斯国防部运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orbitalradar.com/satellite/45608">COSMOS 2546 — Live Satellite Tracking | Orbital Radar</a></li>
<li><a href="https://www.n2yo.com/satellite/?s=45608">COSMOS 2546 Satellite details 2020-031A NORAD 45608 - N2YO.com</a></li>
<li><a href="https://www.satellitetrackerlive.com/satellites/45608">Cosmos 2546 — NORAD 45608 | Satellite Tracker</a></li>

</ul>
</details>

**社区讨论**: 社区评论包括在乌克兰和加里宁格勒附近每天遭遇干扰的真实经历，以及关于俄罗斯电子战影响乌克兰无人机的猜测。一位评论者质疑广域干扰所需的功率，另一位则链接了相关的 Veritasium 视频。

**标签**: `#GNSS`, `#interference`, `#satellite`, `#geopolitics`, `#RF`

---

<a id="item-4"></a>
## [Ladybird 浏览器因 AI 代码禁止公开拉取请求](https://simonwillison.net/2026/Jun/5/andreas-kling/#atom-everything) ⭐️ 8.0/10

Ladybird 浏览器宣布不再接受公开的拉取请求，理由是 AI 生成的代码破坏了善意努力的假设，并要求贡献者直接对变更负责。 这一政策转变反映了随着 AI 生成代码的普及，开源治理中日益加剧的紧张关系，可能为项目如何维护信任和问责制树立先例。 这一变更意味着所有贡献现在必须通过更正式的流程提交，贡献者需明确承担责任。Andreas Kling 强调，问题不在于代码是否手动输入，而在于谁为其负责。

rss · Simon Willison · Jun 5, 11:10

**背景**: Ladybird 是一个由非营利组织 Ladybird Browser Initiative 开发的开源网络浏览器。它最初是 SerenityOS（由 Andreas Kling 创建的业余操作系统）的一个组件。该浏览器注重隐私，计划在 2028 年前发布 alpha、beta 和稳定版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/Andreas_Kling">Andreas Kling</a></li>

</ul>
</details>

**标签**: `#open-source`, `#ai-ethics`, `#ladybird`, `#software-governance`

---

<a id="item-5"></a>
## [AI 爱好者与怀疑者：与时间赛跑 vs. 对抗熵增](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything) ⭐️ 8.0/10

Charity Majors 发表文章，将 AI 爱好者急于采用 AI 以提升能力与 AI 怀疑者维护代码质量和信任之间的张力，描述为与时间赛跑和对抗熵增。 这一分析揭示了软件团队中真实存在的生存张力，可能决定在当前 AI 周期中哪些公司会成功或失败，因此领导者弥合这两类群体之间的鸿沟至关重要。 Majors 指出双方都没有错：爱好者看到了真正不连续的能力飞跃，而怀疑者警告说，以工程师无法阅读的速度交付代码会降低可靠性和机构知识。她建议设计反馈循环来弥合共享现实中的鸿沟。

rss · Simon Willison · Jun 4, 23:55

**背景**: 这篇文章讨论了软件工程中一个常见的辩论：快速采用 AI 与维护代码质量、可靠性和信任之间的权衡。Majors 是一位知名的工程师和作家，经常讨论运维卓越和工程文化。

**社区讨论**: 该文章在 Lobste.rs 上被分享，评论者可能讨论了平衡 AI 采用与代码质量的实际挑战，但此处未提供具体评论。

**标签**: `#AI`, `#software engineering`, `#technology debate`, `#code quality`

---

<a id="item-6"></a>
## [五角大楼或因 AI 军事限制终止与 Anthropic 合作](https://t.me/zaihuapd/41777) ⭐️ 8.0/10

美国国防部正考虑终止与 AI 公司 Anthropic 的合作，原因是双方在 Claude AI 模型的军事用途限制上存在分歧。Anthropic 禁止将 Claude 用于大规模监控和全自动武器系统，而国防部要求获得包括武器研发和战场行动在内的所有合法用途授权。 这场争端凸显了 AI 安全承诺与国家安全需求之间的关键矛盾，可能为 AI 公司如何与军事客户合作树立先例。其结果可能影响行业在伦理限制方面的规范，并影响五角大楼利用先进 AI 进行防御的能力。 据报道，Anthropic 拒绝为军事用途移除 Claude 的两项主要安全限制，尽管 OpenAI 和 Google 等竞争对手已放宽类似限制。五角大楼向 Anthropic 发出最后通牒要求其遵守，但该公司并未让步。

telegram · zaihuapd · Jun 5, 01:27

**背景**: Anthropic 是一家专注于 AI 安全的公司，开发了 Claude 模型，该模型曾用于抓捕委内瑞拉领导人尼古拉斯·马杜罗的军事行动。公司的使用政策明确禁止可能造成伤害的应用，包括自主武器和大规模监控。在国防部长皮特·赫格塞斯领导下，国防部寻求不受限制地使用 AI 进行防御，导致了当前的僵局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute - Wikipedia</a></li>
<li><a href="https://www.facebook.com/washingtonpost/posts/breaking-news-anthropic-said-that-it-will-not-concede-to-the-pentagons-terms-for/1289252683066604/">Breaking news: Anthropic said that it will not concede to the Pentagon's ...</a></li>
<li><a href="https://www.reddit.com/r/ClaudeAI/comments/1rem4td/anthropic_ditches_its_core_safety_promise_in_the/">Anthropic ditches its core safety promise in the middle of an AI red ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 等平台上的社区讨论反应不一：一些用户支持 Anthropic 在 AI 伦理上的立场，而另一些人则批评该公司可能阻碍国家安全。还有关于 Anthropic 的限制是否与其早期的安全承诺一致的辩论。

**标签**: `#AI ethics`, `#military AI`, `#Anthropic`, `#US Department of Defense`, `#AI policy`

---

<a id="item-7"></a>
## [Anthropic 呼吁全球放缓前沿 AI 开发](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 8.0/10

Anthropic 呼吁全球主要 AI 实验室放缓前沿模型开发节奏，警告快速进步可能很快导致递归自我改进——即 AI 系统无需人类干预即可自我改进——带来重大社会风险。 这一来自领先 AI 安全实验室的提议凸显了人们对不受控 AI 进步以及全球协调必要性的日益担忧，但在华盛顿和硅谷遭到批评，被认为可能夸大风险并将战略优势拱手让给中国。 Anthropic 近日刚完成近万亿美元估值的融资，并已提交 IPO 保密文件，为其放缓呼吁增添了背景。该公司警告，若没有全球协调机制，单方暂停只会让对手抢跑。

telegram · zaihuapd · Jun 5, 03:00

**背景**: 递归自我改进（RSI）是指 AI 系统重写自身代码以增强能力的过程，可能导致智能爆炸和超级智能。以安全为使命著称的 Anthropic 已将越来越多的 AI 开发工作委托给 AI 系统自身，从而加速了进展。该公司的提议正值 AI 领导权的地缘政治紧张局势以及行业内关于安全与竞争力之争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-warns-ai-may-soon-begin-recursive-self-improvement/">Anthropic warns AI may soon begin recursive self-improvement</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Anthropic`, `#AI regulation`, `#recursive self-improvement`, `#geopolitics`

---