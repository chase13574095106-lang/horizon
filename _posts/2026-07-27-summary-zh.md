---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> From 26 items, 10 important content pieces were selected

---

1. [月之暗面开源 2.8 万亿参数模型 Kimi K3](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x 无 gadget 高危 RCE 漏洞](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0：支持 Inkling 模型、优化 DeepSeek-V4、灵活注意力后端](#item-3) ⭐️ 8.0/10
4. [Anthropic 澄清对开放权重模型的立场](#item-4) ⭐️ 8.0/10
5. [法官驳回谷歌用 DMCA 抗辩网络抓取案](#item-5) ⭐️ 8.0/10
6. [Bun 的 Rust 重写进展：已在 Claude Code 中发布，1.4 版本推迟](#item-6) ⭐️ 8.0/10
7. [长鑫科技科创板首日暴涨 471.59%，创 IPO 纪录](#item-7) ⭐️ 8.0/10
8. [谷歌透露 Gemini 4 为迄今最雄心预训练项目](#item-8) ⭐️ 8.0/10
9. [中方驳斥美方以 AI 模型蒸馏为由的制裁威胁](#item-9) ⭐️ 8.0/10
10. [中芯国际测试中国首台国产 DUV 光刻机](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [月之暗面开源 2.8 万亿参数模型 Kimi K3](https://t.me/zaihuapd/42793) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是全球首个开源的 2.8 万亿参数模型，采用了全新的 Kimi Delta Attention 和 Attention Residuals 架构。它在 Frontend Code Arena 中以 1679 分排名第一，超越了 Claude Fable 5，相比前代 Kimi k2.6 的第 18 名实现了大幅跃升。 Kimi K3 是有史以来发布的最大开源权重模型，使前沿规模 AI 的定制和研究更加民主化。其顶尖的基准测试表现表明，开源模型在特定领域（如前端编程）能够与专有领导者竞争甚至超越它们。 该模型采用原生 MXFP4 量化，托管需要约 1.5 TB 显存，并支持 100 万 token 上下文窗口和原生视觉能力。它在 Frontend Code Arena 的 7 个领域中 6 个排名第一，仅在游戏领域落后。

telegram · zaihuapd · Jul 27, 06:27

**背景**: 大型语言模型通常以参数量衡量；2.8 万亿参数比大多数开源模型（如 Llama 3.1 405B）大一个数量级。Frontend Code Arena 评估 AI 模型在真实前端开发任务（如构建响应式网页应用）上的表现。Kimi Delta Attention 和 Attention Residuals 是提高效率和性能的新型架构创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/arena/status/2077824029126504525">Arena.ai on X: "Big news: Kimi-K3 by @Kimi_Moonshot is now #1 in the Frontend Code Arena with 1679 pts, surpassing Claude Fable 5. This is a 17-place jump from Kimi-k2.6 (#18 -> #1). In Frontend, Kimi-K3 ranked #1 in 6 of 7 domains: Brand & Marketing, Reference-Based Design, Data & Analytics, Consumer Product, Simulations, and Content Creation Tools, landing #2 only in Gaming behind Fable 5. The full model weights will be released by July 27. Congrats to the @Kimi_Moonshot team on this major milestone!" / X</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3">China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits | Tom's Hardware</a></li>
<li><a href="https://www.developersdigest.tech/blog/web-dev-arena">Web Dev Arena: How to Test AI Coding Models on Real Frontend Work - Developers Digest</a></li>

</ul>
</details>

**社区讨论**: 社区成员对开源权重带来的定制潜力和数据主权感到兴奋，但也有人指出高硬件要求（1.5 TB 显存）使得托管成本高昂。一位用户报告称，该模型在被问及时自称是“Claude”，引发了对训练数据污染的担忧。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#benchmark`

---

<a id="item-2"></a>
## [Fastjson 1.x 无 gadget 高危 RCE 漏洞](https://t.me/zaihuapd/42797) ⭐️ 9.0/10

Fastjson 1.x 版本 1.2.68 至 1.2.83 被披露存在一个高危远程代码执行漏洞（CVE-2026-16723，CVSS 9.0），无需开启 autoType 或依赖 classpath gadget，可在 JDK 8/17/21 上利用。 该漏洞影响广泛使用的 Java JSON 库，且由于 Fastjson 1.x 已于 2024 年 10 月停止维护，官方极大概率不会发布补丁，导致大量应用面临远程攻击风险。 利用条件包括 Spring Boot 可执行 fat-JAR、SafeMode 处于关闭状态，且攻击者能够向解析器发送恶意 JSON。即使 autoType 关闭且无 classpath gadget，漏洞仍可利用。

telegram · zaihuapd · Jul 27, 10:31

**背景**: Fastjson 是阿里巴巴开发的 Java 高性能 JSON 库。其 autoType 功能允许在反序列化时携带类型信息，历史上曾多次引发漏洞。Fastjson 1.x 已被完全重构的 Fastjson2 取代，后者在安全性和性能上均有提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lilting.ch/en/articles/fastjson-1x-rce-spring-boot-fat-jar">Fastjson CVE-2026-16723: no AutoType, no gadgets ... | lilting channel</a></li>
<li><a href="https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html">Fastjson 1 . x RCE Vulnerability Targeted in Attacks With No Patched...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Fastjson`, `#RCE`, `#Java`

---

<a id="item-3"></a>
## [vLLM v0.26.0：支持 Inkling 模型、优化 DeepSeek-V4、灵活注意力后端](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 引入了对 Inkling 模型系列（975B 参数、1M 上下文）的全面支持、DeepSeek-V4 的性能优化（例如端到端 TPOT 提升 2.94%）、通过 head_dtype 实现的 fp32 lm_head，以及可按 KV 缓存组选择的灵活注意力后端。 此版本显著扩展了 vLLM 的模型支持和推理效率，使 Inkling 和 DeepSeek-V4 等前沿模型能够以最先进的性能进行部署。灵活的注意力后端和 KV 卸载增强功能提高了大规模 AI 服务的可扩展性。 该版本包含来自 212 位贡献者的 411 次提交，新功能包括 Inkling 的分段 CUDA 图支持、DeepSeek-V4 的专用路由内核，以及用于提高生成准确性的 fp32 lm_head。KV 卸载现在包括层级拥有的事件处理和带有工作负载标识的对象存储辅助层级。

github · khluu · Jul 27, 01:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，用于优化服务大型语言模型时的内存和计算。Inkling 模型是 Thinking Machines Lab 推出的 975B 参数混合专家多模态模型，支持文本、图像和音频输入，上下文长度可达 1M。FlashAttention-4 (FA4) 是最新的注意力算法，针对 Hopper GPU 进行了优化，性能优于 FA3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Anthropic 澄清对开放权重模型的立场](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布博文，声明其从未主张禁止开放权重模型，但支持对所有足够强大的 AI 模型（包括开放和封闭模型）进行强制性安全测试。 这澄清了一家主要 AI 实验室在一个有争议的监管问题上的立场，可能影响关于如何在 AI 开发中平衡创新与安全的政策辩论。 Anthropic 支持三项措施：禁止向中国出售芯片、打击工业规模的蒸馏行为，以及对强大模型进行强制性安全测试。批评者认为，如果标准过于昂贵或限制性，强制性测试可能实际上禁止了开放权重模型。

hackernews · surprisetalk · Jul 27, 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型是指其训练参数（权重）公开发布的 AI 模型，允许任何人下载和使用。与开源不同，开放权重不一定包含训练代码或数据。强制性安全测试要求模型在发布前通过政府定义的测试，这一概念在 AI 安全界存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了怀疑，认为如果测试成本高昂或管理严格，强制性安全测试可能实际上禁止了开放权重模型。一些人指出 Anthropic 立场中的矛盾，例如在声称不主张禁令的同时支持芯片禁令。

**标签**: `#AI safety`, `#open-weights models`, `#regulation`, `#Anthropic`, `#policy`

---

<a id="item-5"></a>
## [法官驳回谷歌用 DMCA 抗辩网络抓取案](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

美国一名法官裁定，谷歌不能利用《数字千年版权法》（DMCA）来阻止对其搜索结果的抓取，驳回了谷歌试图对搜索引擎结果页面主张版权保护的请求。 该裁决为网络抓取的合法性树立了重要的法律先例，可能限制大型科技公司利用版权法限制数据访问和竞争的方式。它可能影响依赖抓取的第三方搜索 API 和工具的可用性。 该案涉及抓取谷歌搜索结果的 SerpAPI 公司，谷歌声称抓取违反了 DMCA 的反规避条款。法官认为，谷歌的搜索结果缺乏足够的创造性，不符合版权保护条件，并且抓取行为并未规避有效控制受版权作品访问的技术措施。

hackernews · cdrnsf · Jul 27, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: DMCA 是美国版权法，包含禁止规避用于控制受版权作品访问的技术保护措施的条款。网络抓取是从网站自动提取数据的过程，其合法性通常取决于数据是否公开可访问以及抓取方法是否绕过了访问控制。谷歌曾辩称其搜索结果受版权保护，抓取它们需要规避其技术措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datacelix.com/legal-considerations-for-web-scraping/">Legal Considerations For Web Scraping : A Practitioner's Guide To...</a></li>
<li><a href="https://www.promptcloud.com/blog/is-web-scraping-legal-in-us-a-complete-guide/">Is Web Scraping Legal in US | Ethical Scraping Practices</a></li>
<li><a href="https://thunderbit.com/blog/is-web-scraping-legal-us">Is Web Scraping Legal in the US? What the Law Actually Says</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该裁决，许多人批评谷歌试图利用版权扼杀竞争。一些人指出，谷歌弃用其搜索 API 导致没有合法替代方案，迫使人们依赖抓取工具。还有人指出，一家靠抓取他人数据起家的公司现在试图阻止别人抓取其数据，这颇具讽刺意味。

**标签**: `#DMCA`, `#web scraping`, `#Google`, `#legal`, `#search engines`

---

<a id="item-6"></a>
## [Bun 的 Rust 重写进展：已在 Claude Code 中发布，1.4 版本推迟](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun 的 Rust 重写已在一个多月前在 Claude Code 中发布，但 Bun v1.4 版本因尚未达到承诺的新通过 Node.js 测试数量而推迟。创建者 Jarred 确认重写整体进展顺利，相关测试改进的 PR 正在等待合并。 这次重写对流行的 JavaScript 运行时 Bun 来说是一次重大的技术转变，其成功可能显著提升性能和兼容性。推迟发布凸显了团队对 Node.js 兼容性的承诺，这对采用至关重要。 Rust 重写很大程度上借助了 LLM 的帮助，将原始的 Zig 代码库进行了转换。1.4 版本预计最迟在下周二发布，前提是达到 Node.js 测试数量的目标。

hackernews · tomlockwood · Jul 27, 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是一个最初用 Zig 编写的快速 JavaScript 运行时。决定用 Rust 重写是出于性能和生态系统的考虑。Claude Code 是 Anthropic 开发的一款 AI 辅助编码工具，帮助开发者理解和编辑代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/goldbergyoni/javascript-testing-best-practices">GitHub - goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript & Node.js testing best practices (August 2025)</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：有人质疑重写后从提交数量中能获得的洞察，而另一些人则争论使用 LLM 进行翻译的合理性。一个对比项目（Buz）声称通过修复原始 Zig 代码库实现了亚秒级构建时间，暗示重写的问题可能是自找的。

**标签**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#LLM`

---

<a id="item-7"></a>
## [长鑫科技科创板首日暴涨 471.59%，创 IPO 纪录](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10

长鑫科技（CXMT）在科创板上市首日开盘报 49.5 元/股，较发行价 8.66 元/股暴涨 471.59%。公司实际募集资金约 579 亿元，若超额配售选择权全额行使，预计募资总额约 666 亿元，超过 2020 年中芯国际的纪录，成为科创板史上最大 IPO。 这一创纪录的 IPO 表明市场对中国国产存储芯片行业信心强劲，凸显了半导体自主可控的战略重要性。巨额资金注入将加速长鑫科技的 DRAM 产能扩张和技术研发，可能重塑全球存储芯片格局。 长鑫科技是中国唯一大规模集成 DRAM 设计制造商。公司预计 2026 年上半年归母净利润 500 亿至 570 亿元，同比大幅扭亏。发行价为 8.66 元/股，股票代码 688825.SH。

telegram · zaihuapd · Jul 27, 01:29

**背景**: 科创板（上海证券交易所科创板）于 2019 年 7 月成立，旨在为中国科技公司提供更大的资本市场准入，类似于纳斯达克。DRAM（动态随机存取存储器）是计算机、服务器和消费电子产品中的关键部件，其生产由少数全球巨头主导。长鑫科技的成功上市反映了中国在地缘政治紧张背景下推动半导体供应链自主可控的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Star_Market_Stock_Market">Star Market Stock Market</a></li>
<li><a href="https://www.mexc.com/crypto-pulse/article/changxin-memory-technologies-cxmt-129628">ChangXin Memory Technologies ($ CXMT )... | MEXC Crypto Pulse</a></li>

</ul>
</details>

**标签**: `#IPO`, `#semiconductor`, `#memory chips`, `#Chinese tech`, `#stock market`

---

<a id="item-8"></a>
## [谷歌透露 Gemini 4 为迄今最雄心预训练项目](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

谷歌 CEO Sundar Pichai 在 Alphabet 2026 年第二季度财报电话会议上宣布，Gemini 4 预训练已启动，称其为公司迄今为止最具雄心的预训练项目，目标是在 2026 年底前发布。 这标志着谷歌继续致力于前沿 AI 和 AGI 开发，可能为大型语言模型设定新基准。该模型的发布可能加剧主要 AI 实验室之间的竞争，并加速编码、推理和多步骤任务等能力的提升。 Pichai 强调谷歌将优先将算力分配给前沿 AGI 研发，以确保 Gemini 4 在发布时仍处于行业前沿。此外，Gemini 3.x Flash 系列将保持几乎每月一次的迭代频率，重点提升智能编码等能力。

telegram · zaihuapd · Jul 27, 04:06

**背景**: Gemini 是谷歌 DeepMind 开发的大型语言模型系列，包括 Gemini 1.5、2.0 和 3.x Flash 等版本。预训练是模型在微调之前从海量数据集中学习的初始阶段。谷歌之前的模型与 OpenAI 的 GPT 系列和 Anthropic 的 Claude 竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://andrew.ooo/answers/gemini-4-pretraining-tease-what-we-know-july-2026/">Gemini 4 Pretraining Tease: What We Know So Far (July 2026)</a></li>
<li><a href="https://felloai.com/all-we-know-about-google-gemini-4/">Gemini 4 : Release Date, Pre-Training News & Rumors</a></li>
<li><a href="https://coursiv.io/blog/gemini-4-pretraining">Gemini 4 Training Has Begun: Release Date & What We Know ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Gemini`, `#Large Language Models`, `#AGI`

---

<a id="item-9"></a>
## [中方驳斥美方以 AI 模型蒸馏为由的制裁威胁](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

7 月 27 日，中国商务部正式驳斥美方关于中国 AI 企业通过模型蒸馏窃取知识产权的指控，指出美国企业同样在蒸馏中国模型，且该技术是行业标准做法。 这标志着中美 AI 紧张局势显著升级，美国因一项广泛使用的技术威胁制裁。中方的回应凸显了全球 AI 生态系统的相互依存性，并可能影响未来对开源模型的监管。 商务部指出，模型蒸馏是行业常用技术，近 200 家美国初创企业已呼吁美国政府不要限制访问中国开源模型。中方警告，若美方行为造成实质性损害，将采取必要措施维护中国企业合法权益。

telegram · zaihuapd · Jul 27, 11:01

**背景**: 模型蒸馏是一种训练较小、更高效模型以模仿更大、更强模型行为的技术。它在 AI 行业中被广泛用于降低计算成本并实现边缘设备部署。美国近期调查中国 AI 企业，指控其未经授权使用蒸馏技术复制美国模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7665780788496007222">今天我们讲讲大 模 型 的“核心” 技 术 ： 蒸 馏 （Model Distillation...</a></li>
<li><a href="https://www.tmtpost.com/7892989.html">Anthropic装糊涂，全球 AI 圈看笑了-钛媒体官方网站</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，近 200 家美国初创企业反对限制中国开源模型，显示业界对开放访问的支持。一些评论者指出美国公司同样使用蒸馏技术的讽刺之处，另一些人则讨论该技术的伦理边界。

**标签**: `#AI`, `#geopolitics`, `#model distillation`, `#US-China trade`, `#regulation`

---

<a id="item-10"></a>
## [中芯国际测试中国首台国产 DUV 光刻机](https://t.me/zaihuapd/42800) ⭐️ 8.0/10

中芯国际正在试运行中国首台由上海初创公司宇量昇研发的深紫外（DUV）光刻机，用于生产 28 纳米芯片，并尝试通过多重图形化工艺实现 7 纳米。 这标志着中国在减少对外国芯片制造设备依赖方面迈出了重要一步，可能重塑全球半导体供应链和地缘政治格局。 该设备大部分零部件已实现国产化，但仍依赖部分进口。预计 2027 年实现量产和稳定良率，中芯国际目标在 2026 年前大幅扩产。

telegram · zaihuapd · Jul 27, 14:10

**背景**: DUV 光刻利用深紫外光在芯片上刻印电路，结合多重图形化技术可制造 7 纳米节点。目前中国最先进的芯片仍依赖荷兰 ASML 的 DUV 设备，而用于 7 纳米以下节点的 EUV 光刻机因美国出口管制被禁止对华销售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/china-begins-making-homegrown-duv-chipmaking-tools-information-reports-2026-07-27/">China begins making homegrown DUV chipmaking tools, The...</a></li>
<li><a href="https://waferscope.com/duv-vs-euv-whats-the-real-difference-in-chipmaking/">DUV vs EUV: What’s the Real Difference in Chipmaking?</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#lithography`, `#China`, `#chip manufacturing`, `#export controls`

---