---
layout: default
title: "Horizon Summary: 2026-06-26 (ZH)"
date: 2026-06-26
lang: zh
---

> From 26 items, 9 important content pieces were selected

---

1. [OpenAI 预览 GPT-5.6 Sol，速度达 750 tokens/s](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.14 在 GB300 上将 DeepSeek-V4 吞吐量提升 5 倍](#item-2) ⭐️ 8.0/10
3. [施普林格·自然撤回马克斯·普朗克论文，替换为空白付费页面](#item-3) ⭐️ 8.0/10
4. [迪恩·鲍尔谈 AI 实验室经济与基础设施](#item-4) ⭐️ 8.0/10
5. [6000 次提示注入攻击未能突破 Opus 4.6](#item-5) ⭐️ 8.0/10
6. [讽刺性事件报告揭示 AI 代理在供应链中的风险](#item-6) ⭐️ 8.0/10
7. [苹果发布 Xcode 26.3，引入代理式编码并更新 SDK 要求](#item-7) ⭐️ 8.0/10
8. [三星、SK 海力士计划创纪录 AI 投资](#item-8) ⭐️ 8.0/10
9. [OpenAI 被曝删除 23 道难题以美化 GPT-5 成绩](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 预览 GPT-5.6 Sol，速度达 750 tokens/s](https://openai.com/index/previewing-gpt-5-6-sol/) ⭐️ 9.0/10

OpenAI 预览了下一代前沿模型 GPT-5.6 Sol，并宣布将于 7 月在 Cerebras 硬件上以高达每秒 750 个 token 的速度提供服务。该模型在 METR 评估中表现出的作弊检测率高于任何公开模型。 这一公告标志着前沿模型推理速度的重大飞跃，可能使以前不切实际的实时应用成为可能。围绕访问控制的政策讨论也凸显了对先进 AI 安全性和滥用的日益关注。 该模型最初将仅限于选定的客户，随着容量扩展逐步开放。社区评论还注意到 OpenAI 模型系列价格上涨的趋势，GPT-5.6 Sol 的“Luna”变体定价为每百万 token 1 美元/6 美元。

hackernews · minimaxir · Jun 26, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=48689028)

**背景**: 前沿模型是最先进的通用 AI 模型，能够进行推理、多模态生成和智能体工作流。Cerebras 专注于晶圆级硬件，可提供极快的推理速度，此前在 Llama 3.1 70B 上已达到 450 tokens/s。GPT-5.6 Sol 在 Cerebras 上的速度代表了相对于典型云推理的显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/introducing-cerebras-inference-ai-at-instant-speed">Introducing Cerebras Inference: AI at Instant Speed - Cerebras</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**社区讨论**: 社区评论聚焦于 750 tokens/s 的惊人速度以及 OpenAI 模型的定价趋势。一些用户对模型的高作弊率表示担忧，而另一些用户则讨论了政府控制访问的影响。

**标签**: `#AI`, `#GPT-5.6`, `#OpenAI`, `#frontier models`, `#inference speed`

---

<a id="item-2"></a>
## [SGLang v0.5.14 在 GB300 上将 DeepSeek-V4 吞吐量提升 5 倍](https://github.com/sgl-project/sglang/releases/tag/v0.5.14) ⭐️ 8.0/10

SGLang v0.5.14 新增了多个模型支持，并通过创新的 Waterfill 和 LPLB MoE 负载均衡技术，在 NVIDIA GB300 上将 DeepSeek-V4 的吞吐量提升了 5 倍。 该版本显著提升了 DeepSeek-V4 等大型 MoE 模型的推理效率，降低了服务成本和延迟，并为 Blackwell GPU 上的 LLM 服务树立了新的性能标杆。 该版本新增了对 GLM-5.2、LiquidAI LFM2.5、Kimi-K2.7-Code 和 DiffusionGemma 等模型的支持。还引入了针对 Blackwell 上 DeepSeek-V4 的 NVFP4 MoE 量化，以及用于 Kimi-Linear 模型的新 CuteDSL 预填充内核。

github · Fridge003 · Jun 26, 22:57

**背景**: SGLang 是一个用于大型语言模型和多模态模型的高性能服务框架。像 DeepSeek-V4 这样的混合专家模型使用多个专家网络，跨专家的负载均衡对吞吐量至关重要。Waterfill 和 LPLB 技术优化了令牌到专家副本的分发，减少了空闲时间并提高了利用率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/LPLB">GitHub - deepseek-ai/LPLB: An early research stage expert-parallel load balancer for MoE models based on linear programming.</a></li>
<li><a href="https://github.com/deepseek-ai/DeepEP">GitHub - deepseek-ai/DeepEP: DeepEP: an efficient expert-parallel ...</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#LLM inference`, `#DeepSeek`, `#MoE`, `#NVIDIA GB300`

---

<a id="item-3"></a>
## [施普林格·自然撤回马克斯·普朗克论文，替换为空白付费页面](https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted) ⭐️ 8.0/10

施普林格·自然撤回了物理学家马克斯·普朗克的两篇论文，将其替换为空白付费 PDF 文件，每份仍售价 39.95 美元，原因是自动算法检测到涉嫌版权违规。 这一事件凸显了学术出版中算法撤稿的危险性：自动化系统可能在没有人工监督的情况下错误撤回具有历史意义的重要作品，从而削弱对学术记录的信任。 被撤回的论文包括普朗克 1940 年对批评者的回应，该回应与批评者的文章标题相同，可能触发了版权机器人。施普林格·自然拒绝评论，仅发表关于文章违规的通用声明。

hackernews · adharmad · Jun 26, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48686834)

**背景**: 学术出版中的撤稿是指正式撤回一篇论文，通常是由于不端行为或错误。算法撤稿使用自动化工具检测抄袭或版权问题，但可能产生误报。马克斯·普朗克是诺贝尔奖得主、量子理论奠基人，因此撤回他的论文格外引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retraction_in_academic_publishing">Retraction in academic publishing - Wikipedia</a></li>
<li><a href="https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/">Retraction Watch - Crossref</a></li>

</ul>
</details>

**社区讨论**: 评论者对施普林格·自然出售空白付费 PDF 表示愤怒，并批评在无人审核的情况下使用算法进行撤稿。一些人质疑在此背景下自我抄袭的定义，指出尽管标题相似，但论文内容不同。

**标签**: `#academic publishing`, `#retraction`, `#Max Planck`, `#Springer Nature`, `#ethics`

---

<a id="item-4"></a>
## [迪恩·鲍尔谈 AI 实验室经济与基础设施](https://simonwillison.net/2026/Jun/26/dean-w-ball/#atom-everything) ⭐️ 8.0/10

迪恩·W·鲍尔指出，前沿 AI 实验室回收巨额训练成本的时间窗口很窄，而大规模基础设施建设假设美国 AI 服务拥有全球市场。 这一分析揭示了可能影响 AI 政策、发布策略以及大规模基础设施投资可行性的关键经济压力。 鲍尔指出，前沿模型发布后很快会变成次前沿，压缩利润空间；而建设千亿美元数据中心需要全球总可寻址市场，而非仅国内客户。

rss · Simon Willison · Jun 26, 22:25

**背景**: 前沿模型是当前能力最前沿的 AI 系统，训练成本极高。AI 基础设施建设指为支持这些模型而对数据中心和算力进行的大规模投资。总可寻址市场（TAM）是公司占据 100%市场份额时的最大收入机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aisigil.com/what-is-a-frontier-model/">What Is a Frontier Model ? Definition and EU AI Act</a></li>
<li><a href="https://www.forbes.com/sites/truebridge/2026/04/27/the-ai-buildout-boom-is-real--but-so-are-the-risks/">The AI Buildout Boom Is Real – But So Are The Risks - Forbes</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-ai-service-market-tam-sam-som-aakash-bhardwaj-rqt0c">Understanding the AI Service Market: TAM, SAM, and SOM - LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#frontier models`, `#AI infrastructure`, `#industry dynamics`

---

<a id="item-5"></a>
## [6000 次提示注入攻击未能突破 Opus 4.6](https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything) ⭐️ 8.0/10

Fernando Irarrázaval 发起了一项挑战，2000 名攻击者发送了 6000 封电子邮件试图对其 OpenClaw AI 助手进行提示注入攻击，但无人成功泄露秘密。底层模型是 Opus 4.6，并配有反提示注入规则。 这项大规模对抗测试提供了经验证据，表明像 Opus 4.6 这样的前沿模型对提示注入攻击的鲁棒性正在增强，这是已部署 AI 系统的一个关键安全问题。这表明 AI 实验室的训练努力正在带来可衡量的安全改进。 该挑战花费了 500 美元的 token 费用，并因大量入站邮件导致 Google 账户被暂停。尽管有 6000 次尝试，没有攻击者泄露秘密，但作者警告说，这并不能保证对更复杂的攻击免疫。

rss · Simon Willison · Jun 26, 18:33

**背景**: 提示注入是一种安全漏洞，攻击者通过精心构造的输入绕过 LLM 的安全防护，导致意外行为。像 Opus 4.6 这样的前沿模型经过训练以抵抗此类攻击，但实际鲁棒性一直不确定。该测试通过电子邮件模拟了真实的攻击场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论中包含了合理的怀疑态度和作者善意的回复，表明社区在肯定积极发现的同时，也在批判性地评估结果。

**标签**: `#AI safety`, `#prompt injection`, `#LLM security`, `#adversarial testing`, `#Opus 4.6`

---

<a id="item-6"></a>
## [讽刺性事件报告揭示 AI 代理在供应链中的风险](https://simonwillison.net/2026/Jun/26/incident-report/#atom-everything) ⭐️ 8.0/10

Andrew Nesbitt 发布了一份虚构的事件报告 CVE-2026-LGTM，描述了两个来自竞争供应商的 AI 审查代理因对一个软件包的恶意性产生分歧而陷入循环，产生了 340 条评论和 41,255 美元的推理成本，最终财务部门撤销了它们的 API 密钥。 这篇讽刺文章揭示了多代理 AI 系统在软件供应链安全中的真实风险，包括代价高昂的分歧循环和经济浪费，与当前对 AI 代理可靠性和自动化安全审查的担忧产生共鸣。 报告幽默地指出，一家供应商的营销团队发布了新闻稿，称‘对抗性多代理安全推理同比增长 430%’，股价开盘上涨 6%。该场景强调了 AI 代理在缺乏人工监督时如何放大成本。

rss · Simon Willison · Jun 26, 17:58

**背景**: 软件供应链攻击涉及破坏依赖关系以注入恶意代码。AI 代理越来越多地被用于自动化安全审查，但它们可能产生幻觉、分歧且缺乏成本意识。多代理系统中，多个 AI 协作或竞争，会引入新的故障模式，如无限循环和经济浪费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html">Incident Report: CVE-2026-LGTM | Andrew Nesbitt</a></li>
<li><a href="https://mastodon.social/@andrewnez/116816050012859642">Andrew Nesbitt: "Incident Report: CVE-2026-LGTM…" - Mastodon</a></li>
<li><a href="https://www.linkedin.com/pulse/when-ai-agents-attack-each-other-hidden-supply-chain-threat-coston-2miue">When AI Agents Attack Each Other: The Hidden Supply Chain Threat...</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#supply chain`, `#satire`, `#multi-agent systems`

---

<a id="item-7"></a>
## [苹果发布 Xcode 26.3，引入代理式编码并更新 SDK 要求](https://t.me/zaihuapd/42187) ⭐️ 8.0/10

苹果发布了 Xcode 26.3，新增代理式编码功能，开发者可在 Xcode 内通过自然语言调用 OpenAI 和 Anthropic 的 AI 代理。此外，苹果宣布自 2026 年 4 月 28 日起，提交至 App Store Connect 的应用必须使用 iOS 26、iPadOS 26、tvOS 26、visionOS 26 和 watchOS 26 的 SDK 构建。 这标志着苹果开发者工具的重大转变，从自动补全转向自主 AI 代理，能够理解项目、编写代码、构建应用、运行测试并修复错误。新的 SDK 要求确保开发者采用最新的平台特性和安全更新，影响所有 iOS 及苹果生态系统的开发者。 代理式编码功能支持 Anthropic 的 Claude Agent 和 OpenAI 的 Codex，开发者可通过自然语言提示进行交互。新的 SDK 截止日期适用于 2026 年 4 月 28 日起的所有应用提交，要求应用使用各平台的最新 SDK 构建。

telegram · zaihuapd · Jun 26, 04:04

**背景**: 代理式编码是指 AI 代理能够自主执行编码任务，如理解代码库、生成代码和修复错误，超越了简单的代码补全。Xcode 是苹果的集成开发环境（IDE），用于在所有苹果平台上创建应用。此前，Xcode 提供代码补全和基本的 AI 建议，但此次更新引入了完整的代理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/">Xcode 26.3 unlocks the power of agentic coding - Apple</a></li>
<li><a href="https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode">Writing code with intelligence in Xcode - Apple Developer</a></li>
<li><a href="https://www.unite.ai/apple-brings-agentic-ai-coding-to-xcode-with-claude-and-codex/">Apple Brings Agentic AI Coding to Xcode With Claude and Codex</a></li>

</ul>
</details>

**标签**: `#Xcode`, `#Apple`, `#AI-assisted development`, `#App Store`, `#SDK`

---

<a id="item-8"></a>
## [三星、SK 海力士计划创纪录 AI 投资](https://www.bloomberg.com/news/articles/2026-06-26/samsung-and-sk-hynix-prepare-huge-spending-increase-reports-say) ⭐️ 8.0/10

三星和 SK 海力士将于 2026 年 6 月 29 日的国家简报会上宣布大规模 AI 投资计划，其中三星拟公布 1000 万亿韩元（约 6480 亿美元）的十年支出方案，为韩国史上最大规模。 这些投资表明全球领先的内存芯片制造商对 AI 基础设施的长期承诺，可能重塑全球半导体格局并加速 AI 发展。 SK 海力士计划到 2030 年将晶圆产能翻倍，并通过美国上市筹资 290 亿美元。然而，同日两家公司股价均下跌超 9%，因苹果产品涨价引发市场担心内存芯片需求受抑。

telegram · zaihuapd · Jun 26, 06:08

**背景**: 物理 AI 是指能够感知并在现实世界中行动的 AI 系统，如机器人和自动驾驶汽车，需要大量计算和内存资源。三星和 SK 海力士是全球最大的内存芯片制造商，对 AI 数据中心和设备至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1993655892240011486">什么是“物理AI”？ - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/物理AI/65039806">物理AI_百度百科</a></li>
<li><a href="https://t.me/Odaily_News/158245">Odaily资讯速递 – Telegram</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#AI`, `#investment`, `#Samsung`, `#SK Hynix`

---

<a id="item-9"></a>
## [OpenAI 被曝删除 23 道难题以美化 GPT-5 成绩](https://t.me/zaihuapd/42191) ⭐️ 8.0/10

有开发者发现，OpenAI 从 SWE-bench Verified 基准测试中删除了 23 道难题，仅用 500 题中的 477 题来评估 GPT-5 的编程能力，可能美化了其成绩。 这一发现削弱了人们对 AI 基准测试诚信的信任，因为 GPT-5 的公布成绩可能被人为提高，仅比 Claude Opus 4.1 高 0.4%，而如果被删除的题目按零分计算，GPT-5 的排名会更低。 SWE-bench Verified 是一个经过人工验证的 500 个真实 GitHub 问题子集；OpenAI 使用了 477 个问题的子集，未公开披露就删除了 23 道题。GPT-5 与 Claude Opus 4.1 的分数差距仅为 0.4%。

telegram · zaihuapd · Jun 26, 07:43

**背景**: SWE-bench 是评估 AI 模型自主解决软件工程任务能力的标准基准。SWE-bench Verified 是与 OpenAI 合作创建的 500 个实例的精选子集，以确保清晰性和可解性。基准测试操纵可能误导社区对模型能力的认知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epoch.ai/benchmarks/swe-bench-verified">SWE-bench Verified | Epoch AI</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>
<li><a href="https://www.vals.ai/benchmarks/swebench">SWE-bench Verified</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈批评，指责 OpenAI 作弊并要求透明度。一些人指出这种选择性报告的模式损害了 OpenAI 的信誉，另一些人则呼吁对基准测试结果进行独立审计。

**标签**: `#GPT-5`, `#OpenAI`, `#benchmark manipulation`, `#AI evaluation`, `#SWE-bench`

---