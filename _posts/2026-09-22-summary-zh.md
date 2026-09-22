---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> From 36 items, 13 important content pieces were selected

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，大幅降价](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，大幅下调价格](#item-2) ⭐️ 9.0/10
3. [五角大楼称过度依赖 AI 导致伊朗学校遭致命打击](#item-3) ⭐️ 9.0/10
4. [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](#item-4) ⭐️ 9.0/10
5. [vLLM v0.30.0 发布：新增 Fast Start GPU 权重缓存守护进程与大量新模型](#item-5) ⭐️ 8.0/10
6. [ShinyHunters 声称窃取 FBI 全体员工数据](#item-6) ⭐️ 8.0/10
7. [25 位菲尔兹奖得主警告 AI 或与数学研究目标错位](#item-7) ⭐️ 8.0/10
8. [阿里发布真武 V900，宣称最强国产 AI 芯片、算力提升 3 倍](#item-8) ⭐️ 8.0/10
9. [Cloudflare Python Workers 正式全面可用](#item-9) ⭐️ 8.0/10
10. [DeepSeek 与清华发布 DSec 沙箱平台技术报告](#item-10) ⭐️ 8.0/10
11. [美国提议与中方建立 AI 事件通报渠道](#item-11) ⭐️ 8.0/10
12. [中国调查 DeepSeek 与月之暗面涉嫌向 Claude 泄露数据](#item-12) ⭐️ 8.0/10
13. [DeepSeek 将向联合国安理会通报 AI 风险](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，大幅降价](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna，这是新一代模型，以不同的能力与成本组合将前沿智能带入日常工作。两款模型的定价大约只有 GPT-5.6 Sol 和 GPT-5.6 Luna 促销价的一半，并且运行时的 token 消耗也比前代更少。 大幅降价可能显著降低运行 AI 智能体和企业工作负载的成本，并加剧与 Anthropic 的 Claude Code 等对手的竞争。在模型供应商之间做选择的开发者和企业将需要重新评估能力、使用限额与成本之间的权衡。 OpenAI 表示 GPT-6 Sol 的错误率只有 GPT-5.6 的一半，而 GPT-6 Luna 以远低的成本达到了此前更高层级模型的性能。GPT-6 系列还改进了提示缓存，默认缓存命中率更高，缓存输入读取可享 90%折扣，并允许在对话中途更改推理强度或可用工具而不丢失缓存。

hackernews · OfficialTurkey · Sep 22, 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 一直在快速迭代其 GPT 模型系列，GPT-5.6 是上一代产品，分为较高层级的 Sol 和较低层级的 Luna 两个版本。提示缓存是一种存储提示部分内容的技术，使重复请求成本更低、运行更快，对智能体和高并发工作负载尤为重要。此次发布正值 OpenAI 的 Codex 与 Anthropic 的 Claude Code 等 AI 编程助手激烈竞争之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">VentureBeatOpenAI releases GPT-6 Sol and Luna models, slashing API ...</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI's GPT - 6 Sol doubles its accuracy rate - for half the cost - ZDNET</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者高度关注定价，simonw 称 GPT-6 Luna 价格仅为 GPT-5.6 Luna 的一半是“一件大事”。其他人则讨论 Codex 与 Claude Code 之间的使用限额，m_fayer 表达了对 GPT-5.6 Sol 的依恋，担心技术上更强的继任者可能用起来不那么自然。

**标签**: `#OpenAI`, `#GPT-6`, `#AI models`, `#pricing`, `#Hacker News`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，大幅下调价格](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，这是其公开呼吁“为前沿发展减速”之后的首个模型，具备更强的沟通表达能力，并在所有计费层级上大幅降价：缓存读取从每百万 token 0.50 美元降至 0.20 美元，输入从 5 美元降至 4 美元，输出从 25 美元降至 20 美元，缓存写入从 6.25 美元降至 5 美元。该模型在发布前由 Frontier Design 和 METR 等外部评估机构进行测试，并在 OpenRouter 上由五家服务商提供。 此次降价直接冲击 DeepSeek 等更便宜的竞争对手——已有用户表示在成本敏感的智能体编程任务中更偏好后者；同时，这一发布也与 Anthropic 自己宣称的“放缓前沿发展”的安全立场相矛盾。作为 OpenRouter 上支出最高的模型之一，Opus 的定价调整可能重塑整个大模型 API 市场的服务商经济格局。 Anthropic 强调 Opus 5.5“比以往模型表达更自然”，会把最重要的信息放在前面，使长时间协作更易跟进，并将其同时定位为可用性与安全性上的改进。该模型可通过 Amazon Bedrock、Azure、Google Vertex、AWS 上的 Claude Platform 以及 Anthropic 官方渠道使用，在 OpenRouter 上支持自动故障转移和服务商锁定。

hackernews · km144 · Sep 22, 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: Anthropic 的 Claude 系列分为 Haiku、Sonnet 和 Opus 三个层级，其中 Opus 能力最强。“前沿模型”指某一时刻最先进的 AI 系统，其训练依赖海量数据，成本可高达数亿美元，通常用于支撑高级推理和智能体工作流。Anthropic 一直以注重安全的实验室自居，其近期提出的“为前沿发展减速”主张，指的是放缓追逐更强模型的竞赛节奏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对降价表示欢迎，有人指出 Opus 5 很可能是 OpenRouter 上支出最高的模型；也有人批评 Anthropic 一边高喊“为前沿发展减速”，一边继续快速发布新模型，前后矛盾。部分用户表示在廉价且“勤奋”的智能体编程任务上更青睐 DeepSeek v4.1，还有人分享了不同思考等级下的“鹈鹕”基准测试图片。

**标签**: `#AI/ML`, `#LLM`, `#Anthropic`, `#Model Release`, `#AI Safety`

---

<a id="item-3"></a>
## [五角大楼称过度依赖 AI 导致伊朗学校遭致命打击](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

五角大楼一份报告认定，美国"未能履行尽一切可行努力核实"伊朗米纳布一所学校为军事目标的义务，且这一失职"超出了单纯疏忽"。报告将此次致命导弹打击部分归因于对 AI 辅助瞄准工具的过度依赖，其中包括 Palantir 公司的 Maven 智能系统，该系统基于过时情报数据将该学校列为推荐目标。 这是首批被确认的 AI 辅助军事瞄准导致大规模平民伤亡的案例之一，加剧了全球关于问责、人类监督以及 AI 在致命决策中局限性的争论。此事可能加速推动具有约束力的军事 AI 国际规范，并重塑各国国防机构部署和审计此类系统的方式。 米纳布目标因数据过时被归类为伊斯兰革命卫队设施，并与其他候选目标一同输入 Maven 系统，最终作为推荐结果输出；官员表示部分用户期望 Maven 能标记过时记录或矛盾之处，但目前尚不清楚他们为何会有这种预期。报告认定失职"超出单纯疏忽"且美国行为"鲁莽"，这大幅提升了法律层面的严重性。

hackernews · devonnull · Sep 22, 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**背景**: Maven 智能系统是美国国防部与科技行业长达十年合作的产物，旨在增强情报分析、监视和瞄准能力，其设计定位是辅助而非取代人类操作员。瞄准中的 AI 决策支持系统可以提出军事目标建议并给出可操作的建议，而研究早已警告"自动化偏见"——即人类在高压力环境下过度信任 AI 输出的倾向。国际人道法要求冲突各方尽一切可行努力核实目标为合法军事目标，且武器使用决策的人类责任必须保留，因为问责无法转移给机器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brennancenter.org/our-work/research-reports/militarys-use-ai-explained">The Military’s Use of AI, Explained | Brennan Center for Justice</a></li>
<li><a href="https://blogs.icrc.org/law-and-policy/2024/08/29/artificial-intelligence-in-military-decision-making-supporting-humans-not-replacing-them/">AI in military decision-making: supporting humans, not replacing them</a></li>
<li><a href="https://www.hrw.org/report/2015/04/09/mind-gap/lack-accountability-killer-robots">Mind the Gap: The Lack of Accountability for Killer Robots | HRW</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为 AI 本身并非根本元凶，有人指出细节表明失误更多是人为和程序性的，而非算法问题。多人强烈主张，将决策权转移给 AI 并不能免除人类的责任，因为"AI 无法在法庭上受审"，并批评五角大楼和 Palantir 相互推诿而非承担责任。还有人指出更深层的问题：不了解 AI 盲点的官员将其奉为"终极分析师"，期待系统从未具备的能力。

**标签**: `#AI ethics`, `#military AI`, `#accountability`, `#AI limitations`, `#defense technology`

---

<a id="item-4"></a>
## [OpenAI 开始有限预览 GPT-5.6 系列：Sol、Terra、Luna](https://t.me/zaihuapd/43990) ⭐️ 9.0/10

OpenAI 已开始对 GPT-5.6 系列进行有限预览，推出三个层级：旗舰模型 Sol、均衡型 Terra 和低成本 Luna。Sol 主打更强的编码、生物安全和网络安全能力，并新增 max 推理强度和 ultra 模式；Terra 性能接近 GPT-5.5 且便宜 2 倍，Luna 则定位为最低成本选择。 这是一次重要的模型发布，重新划分了 OpenAI 在能力与价格上的产品层级，可能对竞争对手形成压力，并改变开发者和企业对性价比的预期。这种分层结构也表明 OpenAI 正按任务复杂度和预算对市场进行细分。 此次预览最初仅面向少数可信伙伴，通过 API 和 Codex 提供，OpenAI 称这是应美国政府要求采取的短期步骤，并计划在未来几周扩大到 ChatGPT 和 Codex。Sol 搭载了 OpenAI 迄今最强大的安全防护体系。

telegram · zaihuapd · Sep 22, 18:04

**背景**: OpenAI 的 GPT 系列是驱动 ChatGPT 和 API 的大型语言模型，每一代通常都会在推理、编码和安全性上有所提升。Codex 是 OpenAI 的 AI 编码智能体，可通过 ChatGPT 网页版、CLI、桌面应用和 IDE 集成使用，也是此次 GPT-5.6 预览的首批入口之一。生物安全和网络安全能力指的是模型协助或防御生物与网络威胁的潜力，随着 AI 模型能力增强，这一领域正受到越来越多的政策关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-sol-terra-luna-explained">What Is GPT-5.6? OpenAI's Sol, Terra, and Luna Model Tiers Explained | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#API`, `#Codex`

---

<a id="item-5"></a>
## [vLLM v0.30.0 发布：新增 Fast Start GPU 权重缓存守护进程与大量新模型](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布了 v0.30.0，这是一次重大更新，包含来自 315 位贡献者（其中 104 位是新贡献者）的 762 个提交，新增支持 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass、Bailing V3 VL 和 Nanbeige4.2 等模型。最核心的特性是 Fast Start：一个常驻的每 GPU 权重缓存守护进程，将量化后、按 TP 分片的权重保留在 GPU 显存中，使引擎重启时通过 CUDA IPC 以 `--load-format ipc_cache` 直接映射权重，而无需从磁盘重新加载。 vLLM 是使用最广泛的开源大模型推理与服务引擎之一，其版本发布直接影响生产团队的模型部署方式。Fast Start 针对的是最突出的运维痛点之一——缓慢的冷启动与引擎重启，而大量新模型支持则让 vLLM 持续跟上快速演进的开放权重模型架构前沿。 Fast Start 现已覆盖 FP4 检查点和多节点张量并行；本次发布还加入了支持按请求退出的 Gumbel-max 水印生成与检测、面向稀疏 MLA 解码的 HiSparse 主机端 KV 分层、Model Runner V2 的多项改进（在 H200 上图捕获时间从 12 秒降至 2 秒，引擎初始化从 28.9 秒降至 8.2 秒），以及通过 `quantization_config.targets` 实现的定向在线量化，并在 SM100/103 上默认使用 FlashInfer CuTeDSL NVFP4 W4A16 取代 Marlin。

github · khluu · Sep 22, 05:20

**背景**: vLLM 是一个开源的高吞吐、显存高效的大模型服务引擎，支持 NVIDIA、AMD、Intel GPU 以及 x86/ARM/PowerPC CPU，并通过插件支持 TPU、Gaudi、Ascend 等加速器。其核心创新是 PagedAttention，通过分页块管理 KV 缓存以减少显存浪费，并常配合张量并行（TP）将模型切分到多张 GPU 上。MXFP8、NVFP4 等量化格式通过降低权重与激活精度来减少显存占用，而 FlashMLA 是 DeepSeek 为自家 V3 系列模型开发的优化多头潜在注意力（MLA）内核库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm -project/ vllm : A high-throughput and memory-efficient...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/configuration/optimization/">Optimization and Tuning - vLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#GPU optimization`

---

<a id="item-6"></a>
## [ShinyHunters 声称窃取 FBI 全体员工数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

黑客组织 ShinyHunters 声称窃取了 FBI 全体员工的个人数据，据称是通过 PeopleSoft 零日漏洞获得的，该漏洞还暴露了 FBI 用于存储员工和申请人信息的 AWS GovCloud 环境。该组织对记者表示，他们并不认为自己的计划是勒索，而是“胁迫”，并称此次行动并非出于经济动机。 如果得到证实，这将是美国联邦执法数据史上最严重的泄露事件之一，可能使特工、分析师及支持人员面临外国情报机构或犯罪分子的针对性威胁。这也引发了人们对政府人力资源系统和云基础设施安全性的严重质疑，令人回想起 2015 年 OPM 黑客事件中 2210 万条记录被泄露的往事。 据称被盗数据来自 PeopleSoft 初始入侵后访问的系统，包括 FBI 用于存储员工和申请人记录的 AWS GovCloud 环境。ShinyHunters 尚未公开提供完整数据集的证据，FBI 也未正式确认此次泄露，因此该声明的范围和真实性仍不确定。

hackernews · spenvo · Sep 22, 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49805278)

**背景**: ShinyHunters 是一个知名的黑客组织，此前曾声称对 AT&T、Ticketmaster 和 Santander 等公司的数据泄露事件负责。PeopleSoft 是 Oracle 开发的企业资源规划（ERP）软件套件，被政府机构和大型组织广泛用于人力资源、薪资和学生管理。AWS GovCloud 是专为托管敏感政府数据而设计的云区域，符合更高的合规要求。评论者提到的 2015 年美国人事管理办公室（OPM）泄露事件暴露了超过 2210 万名现任和前任联邦雇员的个人数据，至今仍是政府数据安全失败的基准案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive.ph">Archive.ph</a></li>

</ul>
</details>

**社区讨论**: 评论者对大组织保护敏感数据库的能力表示极度悲观，有人指出主要国家行为体可能已经掌握了大部分医疗和传记数据。其他人则用《太空堡垒卡拉狄加》中的物理隔离系统作类比，并批评 FBI 的能力，还有人争论 ShinyHunters 威胁的行为属于勒索还是胁迫，其中一人建议提出古怪的公开羞辱要求而非金钱支付。

**标签**: `#cybersecurity`, `#data breach`, `#FBI`, `#hacking`, `#national security`

---

<a id="item-7"></a>
## [25 位菲尔兹奖得主警告 AI 或与数学研究目标错位](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

包括陶哲轩、邓煜在内的 25 位菲尔兹奖得主发表联合声明，警告将 AI 快速用于解决数学问题可能导致 AI 发展目标与数学研究目标“严重错位”。声明认为，把数学解题作为 AI 能力的基准，可能损害数学研究和学术生态。 这是全球最高荣誉数学家罕见的集体发声，表明 AI 用于数学的热潮可能扭曲研究激励、评价指标和学术诚信。它很可能影响资助机构、期刊和 AI 实验室对自动数学推理进展的评估方式。 声明指出，大型语言模型近年来在解决重大数学问题上的能力大幅提升，但警告 AI 批量生成成果可能压缩验证、交流和引用前人成果所需的时间，并引发署名、抄袭等问题。声明同时承认，AI 有望提升研究效率，其影响取决于人们如何使用这项技术。

telegram · zaihuapd · Sep 22, 03:00

**背景**: 菲尔兹奖由国际数学联盟每四年颁发一次，授予不超过四位 40 岁以下的数学家，常被称为“数学界的诺贝尔奖”；截至 2026 年共有 68 人获奖。2006 年获奖者陶哲轩是加州大学洛杉矶分校教授，以偏微分方程、组合数学和数论方面的研究闻名，也是关于 AI 在数学中作用的重要发声者。GPT-4o、DeepSeek-V3、Gemini-2.0 等大型语言模型在数学推理基准上的表现快速提升，引发了这些基准是否代表真正数学理解的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fields_Medal">Fields Medal</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao</a></li>
<li><a href="https://arxiv.org/html/2506.00309v1">Evaluation of LLMs for mathematical problem solving</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Academic Publishing`, `#Fields Medal`

---

<a id="item-8"></a>
## [阿里发布真武 V900，宣称最强国产 AI 芯片、算力提升 3 倍](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

在 2026 云栖大会上，阿里平头哥发布训推一体 AI 芯片真武 V900，宣称是国产最强 AI 芯片，算力达到真武 M890 的 3 倍，支持 216GB 显存与 1200GB/s 片间带宽。CEO 吴泳铭表示，自研 M890 超节点已支撑 2 万亿参数大模型推理，本季度将规模化上架阿里云，同时阿里计划打造 50 万卡广域超节点集群，并将 Qwen 模型扩展至 5 至 10 万亿参数。 这一发布表明阿里正在构建模型、芯片、云三位一体的垂直整合体系，以在出口管制背景下减少对外国加速器的依赖，而 50 万卡、1GW 算力的集群将跻身全球最大 AI 训练基础设施之列。这也抬高了国内竞争门槛，此前华为的 Atlas 超节点集群一直被视为国内最强。 真武 V900 是训推一体芯片，具备 216GB 显存和 1200GB/s 片间带宽，但阿里尚未公布制程工艺、峰值算力、功耗等详细规格。规划中的 50 万卡广域超节点集群目标算力 1GW、带宽 200PB/s、通信延迟 6 微秒，技术底座包括真武 V900、NPO 光模块、HPN 8.0 网络与 CPFS 存储，旨在支撑十万亿级 MoE 模型训练。

telegram · zaihuapd · Sep 22, 03:30

**背景**: 平头哥是阿里巴巴旗下的自研芯片设计部门，真武系列是其 AI 加速器产品线，M890 为上一代产品，V900 定位为其继任者，路线图中还披露了后续的 J900。超节点是通过高速互连将大量加速器紧密耦合而成的集群，用于训练和推理单节点无法容纳的超大模型。Qwen（通义千问）是阿里开放权重的大语言模型系列，参数量（如 5 至 10 万亿）是衡量模型规模的粗略指标，万亿参数级 MoE 模型需要大规模分布式训练基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/005/602.htm">最强国产 AI 芯 片 阿里 平 头 哥 真 武 V 900 ...</a></li>
<li><a href="https://www.chooseai.net/news/7318/">阿里云计划建 50 万卡广域超节点集群：1GW 算力、6 微秒通信延迟-Choo...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2085708631140579231">阿里研究员透露Qwen4.5后模型将扩展至5-10T参数 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Alibaba`, `#T-Head`, `#Qwen`, `#datacenter infrastructure`

---

<a id="item-9"></a>
## [Cloudflare Python Workers 正式全面可用](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

9 月 21 日，Cloudflare 宣布 Python Workers 正式全面可用（GA），Python 成为其开发者平台的一级支持语言，可无缝接入 Workers AI、R2 和 D1 等服务。该功能两年前首次推出，如今原生支持 FastAPI、Django、Flask 等框架，并新增底层网络能力，允许直接在 Workers 中运行 PostgreSQL 等数据库以及 LangChain 等 AI 库。 这一里程碑大幅降低了 Python 开发者在边缘部署应用的门槛，因为他们现在可以使用熟悉的框架和 AI 库，而无需离开 Cloudflare 的无服务器环境。它标志着边缘计算正朝着对 Python 的一级支持方向发生更广泛的转变，可能影响整个行业构建和部署云应用的方式。 Python Workers 通过 Pyodide（一个编译为 WebAssembly 的 Python 解释器）在 V8 隔离环境中运行，这实现了广泛的 Python 应用支持，但与原生运行时相比可能存在性能和兼容性限制。GA 版本包含对 Python 标准库和包的支持，并通过 Workers AI 与 Cloudflare 的全球网络集成以实现 AI 推理。

telegram · zaihuapd · Sep 22, 04:00

**背景**: Cloudflare Workers 是一个无服务器平台，允许开发者无需管理基础设施即可在 Cloudflare 的全球边缘网络上运行代码。Python Workers 两年前首次推出，旨在将 Python 引入这一环境，利用 WebAssembly 和 Pyodide 在 V8 隔离环境中运行 Python 代码。Workers AI 提供由无服务器 GPU 驱动的 AI 推理，R2 是免出口费用的对象存储服务，D1 是无服务器 SQL 数据库，它们都是 Cloudflare 开发者平台的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/">How Python Workers Work - Cloudflare Docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Python`, `#Serverless`, `#Edge Computing`, `#Workers AI`

---

<a id="item-10"></a>
## [DeepSeek 与清华发布 DSec 沙箱平台技术报告](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI 与清华大学联合发布《DeepSeek Elastic Compute（DSec）》技术报告，公开了一个每天服务约 300 万个沙箱实例、支撑大规模智能体训练与评测的沙箱基础设施平台。该平台通过统一 SDK 提供 FnCall、容器、Firecracker microVM 和完整 VM 四种后端，并将有状态的 rollout 执行与可抢占的 GPU 训练解耦。 智能体训练与评测越来越依赖大量隔离的执行环境，DSec 表明这类基础设施可以在生产规模下实现高密度部署和快速创建。报告中的优化方案与生产指标为其他构建强化学习和智能体系统的团队提供了具体参考，也进一步巩固了 DeepSeek 在开放 AI 基础设施领域的地位。 DSec 单个生产单元约使用 160 个节点，峰值并发超过 38 万个沙箱，创建速度超过每秒 5000 个；单节点可高密度承载 3200 个容器或 800 个 microVM。通过基于 3FS 分布式文件系统按需加载 EROFS 镜像，而非全量拉取 Docker 镜像，DSec 报告任务完成时间快 1.7 倍、磁盘写入减少 57%，内存共享与回收机制使峰值内存占用下降约 40%。

telegram · zaihuapd · Sep 22, 04:45

**背景**: 沙箱是用于安全运行不可信代码的隔离执行环境，在训练需要与工具、操作系统或安全场景交互的 AI 智能体时至关重要。Firecracker 是 AWS 开源的虚拟化技术，可创建具有强隔离性和低开销的轻量级 microVM；EROFS 则是针对容器和沙箱镜像优化的只读 Linux 文件系统。3FS 是 DeepSeek 自研的面向 AI 训练与推理负载的高性能分布式文件系统，DSec 正是基于这些组件实现每天服务数百万个沙箱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/3FS">GitHub - deepseek-ai/3FS: A high-performance distributed file ...</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast ... GitHub - firecracker-microvm/firecracker: Secure and fast ... I tried Firecracker microVMs for self-hosted services, and it ... firecracker-microvm/firecracker | DeepWiki Run Your First Firecracker microVM - labs.iximiuz.com What Is a Firecracker VM? · Learn</a></li>
<li><a href="https://docs.kernel.org/filesystems/erofs.html">EROFS - Enhanced Read-Only File System — The Linux Kernel documentation</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#agent training`, `#sandbox`, `#DeepSeek`, `#systems`

---

<a id="item-11"></a>
## [美国提议与中方建立 AI 事件通报渠道](https://x.com/rohanpaul_ai/status/2102254209597157548) ⭐️ 8.0/10

美国提议与中方建立人工智能事件通报渠道，用于通报达到国家安全门槛的 AI 相关事件，该提议出自 9 月 20 日纽约会谈。美国财长贝森特称此举旨在提高两国间的透明度，双方还计划围绕共同风险建立定期的美中 AI 对话。 这是 AI 治理领域一项重大的地缘政治进展，标志着全球两大 AI 强国可能转向双边透明与风险管理。若该机制得以落实，将有助于降低因危险 AI 事件引发误判的风险，并为国际 AI 安全合作树立先例。 该提议尚未成为双边协议或条约，中方官方声明确认双方讨论了 AI 相关议题，但未明确表示接受这一具体机制。该渠道仅覆盖达到国家安全门槛的事件，而此类门槛的界定标准仍不明确。

telegram · zaihuapd · Sep 22, 06:48

**背景**: AI 事件通报系统是一套结构化流程，用于系统性地收集、分析并缓解由 AI 系统直接或间接造成的伤害事件。美国和中国是全球两大 AI 强国，而在此次对话之前，两国在 AI 安全领域的双边接触已基本冻结约两年。此类对话的范围界定十分困难，因为“AI”可以指从自动驾驶汽车、人脸识别到自主武器和大语言模型等几乎所有事物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ai-incident-reporting-systems">AI Incident Reporting Systems</a></li>
<li><a href="https://www.brookings.edu/articles/a-roadmap-for-a-us-china-ai-dialogue/">A roadmap for a US - China AI dialogue | Brookings</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o3MjlyOUVSRWsxaVhIcmY2bGp5Z0FQAQ?hl=en-US&gl=US&ceid=US:en">US proposes AI incident alert system in talks with China - Overview</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#US-China relations`, `#AI safety`, `#policy`, `#national security`

---

<a id="item-12"></a>
## [中国调查 DeepSeek 与月之暗面涉嫌向 Claude 泄露数据](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

据知情人士称，中国互联网监管机构正在调查 DeepSeek 和月之暗面，起因是这两家公司被指控将敏感用户数据转发给 Anthropic 的 Claude 模型。此次调查是在 Anthropic 于 9 月 10 日发布 154 页报告之后展开的，该报告指控 7 家中国公司大规模违规使用 Claude，并举例称 DeepSeek 曾把一名警方监控系统开发工程师的请求转发给 Claude。 此案处于 AI 治理、数据隐私和中美科技紧张局势的交汇点，可能为中国监管机构如何监管涉及外国 AI 模型的跨境数据流动树立先例。这也可能影响 DeepSeek 和月之暗面这两家中国最知名 AI 初创公司的运营方式及其国际形象。 Anthropic 的报告点名 7 家中国公司大规模违反其 Claude 使用政策，其中 DeepSeek 的例子涉及一名从事警方监控系统开发的工程师。调查由中国互联网监管机构进行，但目前尚未公布正式指控或处罚。

telegram · zaihuapd · Sep 22, 14:37

**背景**: DeepSeek 是一家总部位于杭州的 AI 公司，由对冲基金幻方量化所有，开发开放权重的大语言模型，并于 2025 年 1 月发布 DeepSeek-R1 聊天机器人，一度在美国 iOS 应用商店超越 ChatGPT 成为下载量最高的免费应用。月之暗面是一家中国初创公司，以其 Kimi 系列模型闻名，包括开源的推理导向模型 Kimi K2 Thinking。Anthropic 是 Claude 助手背后的美国 AI 安全公司，其指控中国企业滥用 Claude 的报告引发了此次监管审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://free.theresanaiforthat.com/company/moonshot-ai/">Moonshot AI | There's An AI For That</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---

<a id="item-13"></a>
## [DeepSeek 将向联合国安理会通报 AI 风险](https://t.me/zaihuapd/43989) ⭐️ 8.0/10

两名知情人士称，中国 AI 初创公司 DeepSeek 将于本周向由 15 个成员组成的联合国安理会通报人工智能带来的风险；OpenAI 首席执行官 Sam Altman 计划出席周三关于 AI 与国际安全的会议，Anthropic 高层代表预计也将参加。DeepSeek 和月之暗面（Moonshot）等中国 AI 公司受邀发言，但 DeepSeek 创始人梁文锋不打算出席，相关安排仍可能临时变动。 这标志着中美主要 AI 实验室罕见地同时出现在联合国最高安全机构面前，表明 AI 风险已被视为关乎国际和平与安全的问题，而不再只是技术或商业议题。这可能影响正在形成的全球 AI 治理规范，并让中国 AI 开发者直接参与国际安全预期的制定。 简报会定于周三在由 15 个成员组成的安理会举行，Altman 计划出席，Anthropic 将派出高层代表，而 DeepSeek 创始人梁文锋预计不会到场。据路透社援引的消息人士称，发言名单和具体安排仍可能临时变动。

telegram · zaihuapd · Sep 22, 17:39

**背景**: 联合国安理会于 2023 年 7 月首次开会讨论 AI 对国际和平与安全的影响，此后成员国普遍认识到 AI 可能重塑经济、战争与缔造和平的方式。DeepSeek 是一家总部位于杭州的中国 AI 公司，由对冲基金幻方量化资助，开发开放权重的大语言模型；Anthropic 则是美国一家 AI 安全与研究公司，开发了 Claude 助手。让这些实验室在安理会亮相，反映出将前沿 AI 纳入多边审视的趋势正在增强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.securitycouncilreport.org/atf/cf/{65BFCF9B-6D27-4E9C-8CD3-CF6E4FF96FF9}/Concept+Note+AI+UNSC+Signature+Event+(1).pdf">CONCEPT NOTE: UN Security Council Briefing on Artificial ...</a></li>
<li><a href="https://www.anthropic.com/careers">Careers \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#DeepSeek`, `#UN Security Council`, `#AI safety`, `#international security`

---