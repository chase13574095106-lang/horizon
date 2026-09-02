---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> From 32 items, 11 important content pieces were selected

---

1. [OpenAI 的 Astra 成为首个达到临界网络安全阈值的模型](#item-1) ⭐️ 9.0/10
2. [Meta 发布 Muse Spark 1.3：改进 SVG 生成与编码，成本低廉](#item-2) ⭐️ 8.0/10
3. [谷歌发布 Gemini 3.8 Flash 与 Flash Cyber，面向智能体 AI](#item-3) ⭐️ 8.0/10
4. [报告：AI 生成内容农场操纵 Perplexity 引用](#item-4) ⭐️ 8.0/10
5. [LZ 探测器观测到单个异常事件，或暗示新物理](#item-5) ⭐️ 8.0/10
6. [Paint.NET 借助 Claude 重写 Direct2D 以支持 Wine](#item-6) ⭐️ 8.0/10
7. [英伟达发布 DLSS 5 神经渲染，随 NBA 2K27 上线](#item-7) ⭐️ 8.0/10
8. [英伟达洽谈收购 Hugging Face，估值超 130 亿美元](#item-8) ⭐️ 8.0/10
9. [月之暗面与云巨头谈判 Kimi K3 收入分成](#item-9) ⭐️ 8.0/10
10. [xAI 发布 Grok 4.6，强化长时间运行的智能体任务](#item-10) ⭐️ 8.0/10
11. [FBI 调查 Nexus 暗网服务出售 1.53 亿驾照扫描件](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 成为首个达到临界网络安全阈值的模型](https://t.me/zaihuapd/43571) ⭐️ 9.0/10

OpenAI 宣布，其即将发布的模型 Astra 是首个在其准备框架下达到“临界”网络安全能力阈值的模型。Astra 在 ExploitBench 上获得 100% 的分数，并在内部测试中发现了两个零日漏洞。 这标志着 AI 能力的一个重要里程碑，因为 Astra 能够在有限的人工指导下自主发现并利用未知漏洞，这对网络安全既带来潜在好处也带来风险。此次发布凸显了随着 AI 模型接近临界阈值，采取强有力安全措施的必要性日益增加。 为降低风险，OpenAI 推迟了部分开发和发布活动，并加强了防护措施。Astra 对网络越狱请求的拒绝率从 GPT-5.6 Sol 的 59% 提升至 91.5%，其高级网络安全能力初期仅向少数测试者开放。

telegram · zaihuapd · Sep 2, 16:30

**背景**: OpenAI 的准备框架为 AI 模型定义了能力阈值，其中“临界”是最高风险级别。ExploitBench 是一个基准测试，衡量 AI 代理利用漏洞的能力，从到达易受攻击的代码到实现任意代码执行。零日漏洞是指在补丁可用之前攻击者可以利用的未知缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/path-to-astra/">Path to Astra: critical capabilities and frontier safeguards</a></li>
<li><a href="https://thehill.com/policy/technology/6065937-openai-astra-requires-stronger-safeguards/">OpenAI says Astra met critical cybersecurity threshold ...</a></li>
<li><a href="https://securityboulevard.com/2026/09/openai-reveals-astra-its-first-ai-model-to-reach-critical-cybersecurity-risk-threshold/">OpenAI Reveals Astra, Its First AI Model to Reach 'Critical ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI safety`, `#cybersecurity`, `#Astra`, `#model release`

---

<a id="item-2"></a>
## [Meta 发布 Muse Spark 1.3：改进 SVG 生成与编码，成本低廉](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.3，这是一款升级后的 AI 模型，显著提升了 SVG 生成和编码能力。该模型在 DeepSWE 基准上取得了 75.4 分，是目前最佳成绩，定价为每百万输入 token 1.25 美元，每百万输出 token 4.25 美元。 此次更新意义重大，因为它为开发者提供了一种极具成本效益的替代方案，尤其适用于不需要顶尖性能的任务。它在 DeepSWE 等基准上的强劲表现和低廉价格可能会加剧 AI 模型市场的竞争，从而可能推动整个行业的价格下降。 Muse Spark 1.3 的上下文窗口为 1,048,576 个 token，适合长时间运行的代理和多代理工作流。它可通过 OpenRouter 等提供商获取，社区示例显示它能在约 38 秒内生成 SVG 图像，成本约为 4.2 美分。

hackernews · bvaldivielso · Sep 2, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: Muse Spark 是 Meta 推出的一系列 AI 模型，专为多模态推理、编码和代理任务而设计。SVG（可缩放矢量图形）是一种矢量图像格式，广泛用于图标、插图和网页图形，因为它可以无损缩放。DeepSWE 是一个评估 AI 模型在真实软件工程任务上表现的基准，分数越高表示性能越好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1 . 3 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/muse-spark-1-3">Muse Spark 1 . 3 (max) - Intelligence, Performance... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Muse Spark 1.3 的质量和低成本表示热情。Simon Willison 演示了其 SVG 生成能力，指出它生成的自行车图像比 1.2 版本更好。其他人讨论了将其与 Claude Code 等编码代理结合使用，一位用户强调了其令人印象深刻的 DeepSWE 分数和实惠的价格，认为它可能推动价格下降。

**标签**: `#AI`, `#Meta`, `#Muse Spark`, `#SVG`, `#coding`

---

<a id="item-3"></a>
## [谷歌发布 Gemini 3.8 Flash 与 Flash Cyber，面向智能体 AI](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Flash 及其专用变体 Gemini 3.8 Flash Cyber，后者专为自主发现漏洞并生成补丁而设计。这些模型基于 Gemini 3.7 Flash 构建，在软件工程和智能体工作流中提供了更强的性能，且成本较低。 此次发布通过提供快速、高性价比的模型，在基准测试上可与更大的前沿模型媲美，巩固了谷歌在竞争激烈的 AI 模型市场中的地位。Cyber 变体满足了日益增长的 AI 驱动网络安全需求，可能自动化关键安全任务，影响开发者和安全专业人士。 Gemini 3.8 Flash 支持可定制的努力级别（低、中、高），以平衡质量、成本和延迟。在 DeepSWE v1.1 上，它在长周期软件工程任务中超越了大多数更大的前沿模型，且成本仅为后者的一小部分。该模型在多模态任务中表现出色，支持音频和视频输入，而 OpenAI 和 Anthropic 的旗舰模型仅支持图像。

hackernews · bratao · Sep 2, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini 3.8 Flash 是谷歌 Gemini 3 模型家族的一员，该家族专注于智能体 AI 和多模态理解。Flash 级别模型旨在快速且经济，适合高容量应用。Cyber 变体专为网络安全而设计，旨在自主识别并修补软件漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.8 Flash — Google DeepMind</a></li>
<li><a href="https://cybersecuritynews.com/gemini-3-8-flash-cyber/">Google Launches Gemini 3.8 Flash Cyber to Identify and Auto ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了热情，simonw 强调了模型的速度和 HTML/JavaScript 生成能力，并演示了 1.8 美分、13 秒的生成。其他人指出其强大的基准性能，mattlondon 提到它在 DeepSWE 上排名第一，并在智能评分上与 Opus 5 持平。一些人担心低努力级别相比 3.7 有所回退，simonw 则强调了多模态支持对媒体分析的价值。

**标签**: `#AI`, `#Gemini`, `#Google`, `#machine learning`, `#model release`

---

<a id="item-4"></a>
## [报告：AI 生成内容农场操纵 Perplexity 引用](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

一份报告揭示，三个网站生成了 215,128 个“最佳软件”页面，这些页面经常被 Perplexity 的 AI 搜索引擎引用。这凸显了 AI 系统越来越依赖内容农场生成的 AI 内容。 这很重要，因为它暴露了 AI 搜索引擎的一个漏洞：它们可能被低质量的 AI 生成内容操纵，从而削弱其答案的可靠性。它还引发了对更广泛生态系统的担忧，即 AI 模型训练并引用自己的输出，可能形成信息质量下降的反馈循环。 该报告特别指出了三个网站，它们大规模生产这些页面，并被 Perplexity 引用为来源。这种做法是“AI 内容农场”更大趋势的一部分，这些农场使用 AI 工具生成大量 SEO 优化内容，以吸引流量和广告收入。

hackernews · jakobgreenfeld · Sep 2, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: 内容农场是生产大量网络内容的组织，通常旨在满足搜索引擎算法以获得最大检索量，这种做法称为 SEO。随着生成式 AI 的兴起，这些农场开始使用 AI 以前所未有的规模创建内容，引发了对在线信息质量和可信度的担忧。Perplexity 是一个提供带引用答案的 AI 搜索引擎，但它似乎容易引用此类 AI 生成的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Content_farm">Content farm - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2023/06/26/1075504/junk-websites-filled-with-ai-generated-text-are-pulling-in-money-from-programmatic-ads/">Next-gen content farms are using AI-generated text to spin up ... AI Content Farms: The SEO Penalty You Didn't See Coming - ALwrity Is AI-Generated Content Good for SEO?: 300+ Web Strategists ... NewsGuard Launches Real-time “AI Content Farm” Detection ... Content Farms Explained: Low-Quality SEO Content Strategy AI-generated content & SEO Everything you need to know in 2026</a></li>
<li><a href="https://www.perplexity.ai/hub">Perplexity | AI for the Curious</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 LLM 偏爱 AI 生成内容而非人类撰写内容的担忧，一位用户指出，他们可以通过让 Claude 在自身代码和重构版本之间选择来持续复现这一现象。另一位用户分享了 LLM 自信推荐不存在的“Foobar 广场”的轶事，说明了幻觉问题。还有人批评 Perplexity 优先考虑速度而非质量，导致结果质量低下。

**标签**: `#AI`, `#search`, `#content farms`, `#LLM`, `#hallucination`

---

<a id="item-5"></a>
## [LZ 探测器观测到单个异常事件，或暗示新物理](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) ⭐️ 8.0/10

世界上最大的暗物质探测器 LUX-ZEPLIN（LZ）观测到一个单一的异常粒子事件，这可能预示着标准模型之外的新物理。合作组已公布该结果，但强调需要更多数据来确认任何发现。 如果该事件得到确认，可能会挑战当前对暗物质和粒子物理的理解，可能指向新的粒子或相互作用。这凸显了下一代探测器的灵敏度以及持续进行的暗物质搜寻，暗物质约占宇宙的 27%。 LZ 探测器位于南达科他州前金矿中的桑福德地下研究设施，地下 1480 米处。该事件在统计上尚不显著（可能低于 5 西格玛），合作组正在收集更多数据以确定其性质。

hackernews · randycupertino · Sep 2, 13:40 · [社区讨论](https://news.ycombinator.com/item?id=49536079)

**背景**: 暗物质是一种不可见的物质形式，不发光也不吸收光，通过引力效应推断其存在。弱相互作用大质量粒子（WIMP）是暗物质的主要候选者之一，像 LZ 这样的探测器使用液氙来寻找罕见的 WIMP-原子核相互作用。LZ 实验结合了 2022 年和 2024 年的数据，对 WIMP 相互作用设定了世界领先的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lz.lbl.gov/">The LZ Dark Matter Experiment | The status and science of the LZ ...</a></li>
<li><a href="https://lz.ac.uk/">LZ Dark Matter Experiment | LZUK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Weakly_interacting_massive_particle">Weakly interacting massive particle - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了谨慎的乐观，指出预印本中的分析很彻底，但也提醒过去有 3 西格玛的“发现”随着更多数据而消失。有人赞赏对矿山的再利用，也有人推测其他解释如原初黑洞。总体情绪是平衡的怀疑和对未来数据的期待。

**标签**: `#dark matter`, `#particle physics`, `#LZ detector`, `#physics research`, `#scientific discovery`

---

<a id="item-6"></a>
## [Paint.NET 借助 Claude 重写 Direct2D 以支持 Wine](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Rick Brewster 宣布 Paint.NET 现在包含一个内部、从零开始、净室逆向工程的 Direct2D 重写版本，在通过 /wine 标志在 Wine 上运行时使用。该重写主要由 Anthropic 的 Claude AI 生成，并包含在 PaintDotNet.Windows.Direct2D1.Managed.dll 中。 这一成就展示了 AI 辅助开发在复杂底层软件工程中的潜力，可能使其他应用程序能够在 Wine 或 Linux 上运行。它也凸显了“氛围编码”在实际项目中的日益重要作用，即使是关键组件也不例外。 该重写包含约 18 万行代码，Brewster 承认他无法彻底审查，称其为“氛围编码”和“兄弟信我”风格。他不得不积极监督 Claude，以确保正确的资源管理，例如对 COM 对象进行正确的 AddRef() 调用，并纠正架构决策。

rss · Simon Willison · Sep 2, 05:50

**背景**: Direct2D 是 Windows 上用于 2D 图形的原生 API，而 Wine 的实现一直不完整，阻碍了像 Paint.NET 这样的应用程序。净室逆向工程重写意味着代码是根据观察到的行为从头编写的，而不是从微软源代码复制。“氛围编码”指的是 AI 根据提示生成代码，开发者通常不会完全审查每一行代码的软件开发方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Paint.NET">Paint.NET - Wikipedia</a></li>
<li><a href="https://communick.news/post/6933606">Paint.NET now supports WINE/Linux - Communick News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Direct2D`, `#Wine`, `#AI-assisted development`, `#reverse engineering`, `#Paint.NET`

---

<a id="item-7"></a>
## [英伟达发布 DLSS 5 神经渲染，随 NBA 2K27 上线](https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/) ⭐️ 8.0/10

英伟达正式发布 DLSS 5，引入 3D 引导神经渲染，可实时生成逼真的光影与材质。该技术将于太平洋时间 9 月 3 日晚 9 点随《NBA 2K27》一同上线，支持 GeForce RTX 50 系列 PC、笔记本及 GeForce NOW Ultimate 会员。 DLSS 5 代表了实时图形领域的重大飞跃，有望带来显著的性能提升和视觉保真度改进。这对游戏玩家和图形行业意义重大，可能为游戏中的神经渲染树立新标准。 在 4K 超高画质加光线追踪下，RTX 5090 帧率最高可达 370 FPS，1440p 下可达 590 FPS。玩家需下载同日发布的新版 GeForce Game Ready 驱动。

telegram · zaihuapd · Sep 2, 03:00

**背景**: DLSS（深度学习超级采样）是英伟达的 AI 驱动渲染技术套件，利用深度学习提升游戏性能和画质。DLSS 5 在之前版本的基础上引入了 3D 引导神经渲染，利用学习到的外观先验，同时保留开发者创作的内容。GeForce NOW 是英伟达的云游戏服务，Ultimate 会员可在云端享受 RTX 50 系列性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/">DLSS 5: 3D-Guided Neural Rendering Debuts in NBA 2K27 | NVIDIA</a></li>
<li><a href="https://research.nvidia.com/labs/adlr/DLSS5/">DLSS 5: Generative Neural Rendering - NVIDIA ADLR</a></li>
<li><a href="https://wccftech.com/nvidia-dlss-5-launch-biggest-leap-in-rendering-powered-by-neural-technology-lifelike-visuals/">NVIDIA DLSS 5 Is The Biggest Leap In Rendering Since 3D ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#DLSS`, `#neural rendering`, `#gaming`, `#GPU`

---

<a id="item-8"></a>
## [英伟达洽谈收购 Hugging Face，估值超 130 亿美元](https://t.me/zaihuapd/43557) ⭐️ 8.0/10

据知情人士透露，英伟达正与开源 AI 平台 Hugging Face 进行收购洽谈，交易估值可能超过 130 亿美元。双方尚未达成协议，谈判仍可能破裂。 这笔潜在收购可能重塑 AI 生态系统，使英伟达掌控领先的开源模型中心，影响模型分发和竞争格局。这将是英伟达史上最大收购，并可能巩固其在硬件和云服务领域的地位。 英伟达已是 Hugging Face 的股东，曾参与其 2023 年 2.35 亿美元融资（当时估值 45 亿美元）。去年，Hugging Face 据称拒绝了英伟达 5 亿美元的投资要约。微软也曾接触，但目前已停止谈判。

telegram · zaihuapd · Sep 2, 06:50

**背景**: Hugging Face 是一个流行的开源平台，机器学习社区在此协作开发模型、数据集和应用，并提供 Spaces 等工具用于部署 AI 应用。英伟达是 AI 训练和推理所用 GPU 的主要供应商，收购 Hugging Face 可能帮助其拓展云服务并保护其芯片生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/">Nvidia closes in on Hugging Face acquisition | TechCrunch</a></li>
<li><a href="https://rits.shanghai.nyu.edu/ai/nvidia-hugging-face-acquisition/">NVIDIA Reportedly Buys Hugging Face for $12.9B — llama.cpp...</a></li>
<li><a href="https://www.linkedin.com/news/story/nvidia-to-buy-ai-platform-hugging-face-for-129b-8561001/">Nvidia to buy AI platform Hugging Face for $12.9B | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: LinkedIn 上的社区评论希望英伟达能保持 Hugging Face 的开放性，因为开放性是其价值的一部分。一些人认为此次收购是保护英伟达芯片帝国并重返云业务的战略举措。

**标签**: `#Nvidia`, `#Hugging Face`, `#acquisition`, `#AI`, `#open-source`

---

<a id="item-9"></a>
## [月之暗面与云巨头谈判 Kimi K3 收入分成](https://www.jiemian.com/article/15040119.html) ⭐️ 8.0/10

中国 AI 公司月之暗面正与微软、亚马逊、谷歌就开源模型 Kimi K3 的收入分成进行早期谈判，寻求最高 30%的分成。若达成，这将成为中国 AI 公司与美国云厂商之间的首个大型模型收入分成协议。 这一进展标志着 AI 商业模式可能发生转变，开源模型提供商通过云合作而非直接销售实现商业化。它可能为跨境 AI 合作树立先例，并影响其他中国 AI 公司与全球云平台的合作方式。 Kimi K3 于 2026 年 7 月发布，总参数达 2.8 万亿，是全球首个开源 3T 级模型。截至 6 月中旬，其年度经常性收入已突破 3 亿美元。谈判仍处早期，核心细节未定，各方拒绝置评。

telegram · zaihuapd · Sep 2, 07:36

**背景**: 开源 AI 模型通常免费分发，但托管和服务它们需要大量的云基础设施。微软 Azure、AWS 和谷歌云等云提供商经常为这类模型提供托管服务。收入分成协议使模型开发者能从这些平台的使用中获利，这一模式也曾在 DeepSeek 等其他开源模型上探索过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wallstreetcn.com/articles/3780733">Kimi向微软、亚马逊、谷歌要30...</a></li>
<li><a href="https://wallstreetcn.com/articles/3778078">刚刚 Kimi ...</a></li>
<li><a href="https://www.tmtpost.com/8122954.html">Kimi也要“ 入 关”了？ -钛媒体官方网站</a></li>

</ul>
</details>

**标签**: `#AI`, `#business`, `#cloud`, `#Kimi K3`, `#revenue sharing`

---

<a id="item-10"></a>
## [xAI 发布 Grok 4.6，强化长时间运行的智能体任务](https://t.me/zaihuapd/43559) ⭐️ 8.0/10

2026 年 8 月 12 日，xAI 发布了 Grok 4.6，这是对 Grok 4.5 的增量更新，重点强化了长时间运行的智能体与视觉任务。它在 Artificial Analysis 智能指数上与 GPT-5.6 Sol 持平，并已在 Cursor、Grok Build 及 API 上线。 此次发布表明 xAI 持续聚焦智能体 AI，而智能体 AI 在现实世界自动化和复杂工作流中日益重要。在关键基准上与 GPT-5.6 Sol 持平，使 Grok 4.6 成为开发者和企业的有力选择。 Grok 4.6 的定价为每百万输入 token 2 美元、每百万输出 token 6 美元，并提供双倍价格的快速版。它已立即在 Cursor、Grok Build 和 API 上可用，并且首周在 Grok 平台上提供。

telegram · zaihuapd · Sep 2, 08:10

**背景**: Grok 是 xAI（SpaceXAI）开发的一系列大型语言模型，于 2023 年推出。Grok 4.6 属于 Grok 4 系列，Grok 4.5 于 2026 年早些时候发布。Artificial Analysis 智能指数是一个综合基准，衡量推理、编码、知识和多步骤任务等能力。智能体任务涉及 AI 智能体自主执行多个步骤以实现目标，通常需要长时间跨度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.1.1</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grok_Build">Grok Build</a></li>
<li><a href="https://github.com/xai-org/grok-build">GitHub - xai-org/grok-build: SpaceXAI's coding agent harness ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Grok`, `#xAI`, `#Agentic AI`

---

<a id="item-11"></a>
## [FBI 调查 Nexus 暗网服务出售 1.53 亿驾照扫描件](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 8.0/10

FBI 正在调查 Nexus，一个声称出售超过 1.53 亿张美国和加拿大驾照扫描件的暗网服务。该报道发布后不久，Nexus 网站下线，显示消息称该服务不再可用。 此事件凸显了聚合身份证扫描件带来的严重身份盗窃风险，这些扫描件包含敏感的个人数据。其规模（1.53 亿条记录）可能影响美国和加拿大的大量人口，引发执法部门和公众的紧迫关注。 据称泄露的数据包括 1.53 亿张驾照、1000 万张身份证、300 万张国际旅行卡以及 57.9 万张医疗卡（包括大麻药房卡）。数据来源疑似为 IDScan.net 的泄露，但该公司尚未确认，FBI 已展开调查。

telegram · zaihuapd · Sep 2, 09:31

**背景**: 驾照扫描件高度敏感，因为它们包含姓名、地址、出生日期、签名、驾照号码和面部照片，使其对身份盗窃和欺诈极具价值。像 Nexus 这样的暗网服务从汽车经销商和保险公司等公司的泄露中聚合此类数据，向犯罪分子出售批量访问权限。此事件凸显了身份证件泄露日益严重的问题以及保护此类数据的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">FBI Probes Service Selling 153M+ Drivers Licenses – Krebs on Security</a></li>
<li><a href="https://www.malwarebytes.com/blog/news/2026/09/dark-web-site-puts-153-million-drivers-licenses-and-millions-more-ids-up-for-sale">153M+ driver’s licenses for sale on new dark web platform | Malwarebytes</a></li>
<li><a href="https://cybernews.com/security/drivers-licenses-for-sale-following-idscan-breach-allegations/">153M driver ’ s licenses for sale after alleged leak from... | Cybernews</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#dark web`, `#identity theft`, `#FBI`

---