---
layout: default
title: "Horizon Summary: 2026-05-19 (ZH)"
date: 2026-05-19
lang: zh
---

> From 32 items, 11 important content pieces were selected

---

1. [谷歌用 AI 彻底改造搜索框](#item-1) ⭐️ 9.0/10
2. [CISA 承包商在 GitHub 泄露 AWS GovCloud 密钥](#item-2) ⭐️ 9.0/10
3. [DeepSeek 会话隔离漏洞泄露用户对话](#item-3) ⭐️ 9.0/10
4. [谷歌发布 Gemini 3.5 Flash，价格翻三倍](#item-4) ⭐️ 8.0/10
5. [Forge：护栏将 8B 模型准确率从 53%提升至 99%](#item-5) ⭐️ 8.0/10
6. [苹果通过无障碍功能推出代理式 AI](#item-6) ⭐️ 8.0/10
7. [Andrej Karpathy 加入 Anthropic 预训练团队](#item-7) ⭐️ 8.0/10
8. [特斯拉得州锂精炼厂日排 23.1 万加仑废水](#item-8) ⭐️ 8.0/10
9. [谷歌 Gemini Omni：视觉惊艳，物理缺陷](#item-9) ⭐️ 8.0/10
10. [中美同意开展人工智能政府间对话](#item-10) ⭐️ 8.0/10
11. [伊朗要求美科技公司为海底电缆付费](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌用 AI 彻底改造搜索框](https://blog.google/products-and-platforms/products/search/search-io-2026/) ⭐️ 9.0/10

谷歌在 2026 年 I/O 大会上宣布对搜索框进行重大改造，集成由全新 Gemini 3.5 Flash 模型驱动的 AI 功能，包括 AI 模式和连接用户 Gmail 和 Google Photos 的个人智能。 新的 AI 模式提供来自多个来源的综合答案，而个人智能允许搜索框访问已连接应用中的个人数据。该更新将扩展到近 200 个国家和 98 种语言，无需订阅。

hackernews · berkeleyjunk · May 19, 18:34 · [社区讨论](https://news.ycombinator.com/item?id=48197370)

**背景**: 谷歌搜索传统上返回网页链接列表。新的 AI 集成使用像 Gemini 这样的大语言模型（LLM）直接生成答案，类似于 AI 聊天机器人。这种转变可能减少用户点击外部网站的需求，影响网站流量和广告收入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/search/search-io-2026/">Google Search’s I/O 2026 updates: AI agents and more</a></li>
<li><a href="https://www.nytimes.com/2026/05/19/business/google-seach-bar-ai-gemini.html">Powered by A.I., Google Changes Its Search Box for the First Time in 25 Years - The New York Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AI 生成的答案表示怀疑，用户 fscaramuzza 指出 AI 经常将随机评论综合成权威答案。其他人如 simonw 提到了“谷歌零”概念，即谷歌停止向其他网站发送流量。一些用户推荐 Kagi 等替代搜索引擎，但他们承认这对普通用户来说难以接受。

**标签**: `#Google`, `#Search`, `#AI`, `#Gemini`, `#Web`

---

<a id="item-2"></a>
## [CISA 承包商在 GitHub 泄露 AWS GovCloud 密钥](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/) ⭐️ 9.0/10

美国网络安全和基础设施安全局（CISA）的一名承包商在公共 GitHub 仓库中泄露了高度敏感的 AWS GovCloud 凭证和内部系统密码，并且在最初被通知时未予回应。 此次泄露将美国关键政府云基础设施暴露给潜在对手，损害国家安全，并凸显了 CISA 在凭证管理和事件响应方面的系统性失败。 该仓库包含一个 AWS-Workspace-Firefox-Passwords.csv 文件，其中列出了数十个 CISA 内部系统的明文用户名和密码；承包商 Nightwing 将询问转给了 CISA。此外，CISA 员工还被发现将敏感文档上传至 ChatGPT，引发了对 AI 训练数据泄露的进一步担忧。

hackernews · LelouBil · May 19, 07:45 · [社区讨论](https://news.ycombinator.com/item?id=48190454)

**背景**: AWS GovCloud 是美国专属的隔离云区域，旨在托管敏感政府工作负载并满足 FedRAMP 等合规要求。CISA 是负责保护国家关键基础设施免受网络威胁的联邦机构。GitHub 是一个广泛使用的代码托管平台，意外凭证泄露问题屡见不鲜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techradar.com/pro/security/cisa-contractor-apparently-leaked-highly-sensitive-government-aws-keys-on-github">CISA contractor apparently leaked 'highly sensitive' government AWS keys on Github | TechRadar</a></li>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://www.aquasec.com/cloud-native-academy/cspm/aws-govcloud/">AWS GovCloud : Basics & How It Compares to Azure & GCP</a></li>

</ul>
</details>

**社区讨论**: 评论者对 CISA 承包商将凭证存储在公共仓库且未回应警告表示震惊，有人怀疑这可能是蜜罐。其他人指出 LLM 无意中训练泄露秘密的更大风险，并呼吁强制进行秘密扫描和审计。

**标签**: `#security`, `#cloud`, `#government`, `#data breach`, `#CISA`

---

<a id="item-3"></a>
## [DeepSeek 会话隔离漏洞泄露用户对话](https://t.me/zaihuapd/41461) ⭐️ 9.0/10

DeepSeek 对话系统存在会话隔离漏洞，攻击者在全新空对话中仅发送未闭合的<think 字符串，即可泄露其他用户的对话片段。该漏洞影响 DeepSeek Web 和 API，且已被公开披露。 该漏洞泄露包括代码、密钥和隐私在内的敏感用户数据，构成严重的隐私风险。它削弱了用户对 DeepSeek 的信任，并凸显了基于 LLM 的服务面临的安全挑战。 该漏洞通过在新空对话中发送未闭合的<think 字符串触发，导致模型返回其他用户的对话片段。该漏洞已被积极利用，并由 cancat2024 于 2026 年 5 月 11 日负责任地报告。

telegram · zaihuapd · May 19, 11:33

**背景**: 会话隔离是多租户系统的基本安全要求，确保一个用户的数据不会被其他用户访问。在基于 LLM 的聊天服务中，对<think 等特殊标记处理不当可能导致上下文泄露。DeepSeek 是一家受欢迎的国产大语言模型提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.80aj.com/2026/05/15/deepseek-privacy-bug-space/">DeepSeek 疑现严重隐私漏洞：输入空格即可查看他人实时对话</a></li>
<li><a href="https://www.cnblogs.com/alisystemsoftware/p/18789453">从 DeepSeek 敏感信息泄露谈可观测系统的数据安全预防 - 阿里云云原生 - 博客园</a></li>
<li><a href="https://blog.csdn.net/Jailman/article/details/146308336">黑客攻击deepseek服务原理解析_deepseek黑客攻击的详细步骤-CSDN博客</a></li>

</ul>
</details>

**社区讨论**: Telegram 社区成员确认了该漏洞的严重性和可复现性，并指出第三方部署也存在此问题，暗示这可能是一个与幻觉相关的缺陷。

**标签**: `#security`, `#vulnerability`, `#DeepSeek`, `#LLM`, `#data leak`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.5 Flash，价格翻三倍](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.5 Flash，其价格相比前代 Gemini 2.5 Flash 上涨了 3 倍，目前每百万输入 token 收费 1.50 美元，每百万输出 token 收费 9.00 美元。 同一级别模型的大幅涨价引发了社区关于性价比的讨论，尤其是 Gemini 3.5 Flash 的价格已接近 Gemini 2.5 Pro，这让人质疑谷歌的定价策略和模型定位。 Gemini 3.5 Flash 提供 1,048,576 token 的上下文窗口，并声称输出速度提升 4 倍，但早期用户报告了高 token 消耗和配额问题。该模型已在全球上线，性能更强的 Gemini 3.5 Pro 预计下个月推出。

hackernews · spectraldrift · May 19, 17:43 · [社区讨论](https://news.ycombinator.com/item?id=48196570)

**背景**: Gemini Flash 系列是谷歌面向日常任务推出的高性价比、高速 AI 模型。前代 Gemini 2.5 Flash 的定价为每百万输入/输出 token 0.30/2.50 美元。同一级别模型价格翻三倍在业界前所未有。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/blog/research/gemini-3.5-flash-launch">Gemini 3.5 Flash: Benchmarks, Pricing, and Complete Specs</a></li>
<li><a href="https://openrouter.ai/google/gemini-3.5-flash">Gemini 3.5 Flash - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models">Models | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: 社区成员对价格翻三倍感到震惊，有用户指出 Gemini 3.5 Flash 的价格已接近 Gemini 2.5 Pro。另一用户报告称，仅两次提示就用完了 Google AI Pro 计划的全部配额，暗示可能存在 bug 或 token 消耗过高的问题。

**标签**: `#AI`, `#Gemini`, `#pricing`, `#model release`, `#Google`

---

<a id="item-5"></a>
## [Forge：护栏将 8B 模型准确率从 53%提升至 99%](https://github.com/antoinezambelli/forge) ⭐️ 8.0/10

Forge 是一个用于自托管 LLM 工具调用的开源可靠性层，通过领域无关的护栏，在不改变模型本身的情况下，将 8B 模型在多步骤代理任务上的准确率从约 53%提升至约 99.3%。 这表明，配备适当护栏的小型本地模型在代理任务上可与前沿 API 媲美，从而降低成本并实现始终在线的本地 AI 系统。它还揭示了当前 LLM 工具调用中缺少错误恢复机制，突出了一个关键架构缺陷。 Forge 的护栏栈包含五层：重试提示、步骤强制、错误恢复、救援解析和上下文压缩。消融研究表明，禁用重试提示会导致准确率下降 24-49 个百分点，禁用错误恢复则下降约 10 个百分点。服务后端也显著影响准确率，相同权重在 llama-server 和 Llamafile 之间观察到 75 个百分点的差异。

hackernews · zambelli · May 19, 12:23 · [社区讨论](https://news.ycombinator.com/item?id=48192383)

**背景**: LLM 护栏是围绕 LLM 的规则、过滤器和检查，以确保安全且有用的行为。在代理部署中，当 LLM 调用外部 API 或执行代码时，会应用工具使用护栏。小型本地模型在多步骤任务中常因错误累积而表现不佳，例如单步准确率 90%时，5 步后成功率仅约 40%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://repello.ai/blog/llm-guardrails">Repello AI - LLM Guardrails : Complete Runtime Protection Guide for...</a></li>
<li><a href="https://aona.ai/glossary/llm-guardrails/">What are LLM Guardrails ? Input, Output & Tool-Use Controls | Aona AI</a></li>
<li><a href="https://medium.com/@koganti.saichandana14/llm-guardrails-how-to-keep-ai-on-track-safe-and-useful-6ebe7235c4cd">LLM Guardrails : How to Keep AI On-Track, Safe, and Useful | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者验证了这些发现，指出类似的结构化护栏对小型模型也有相同效果。一位用户分享说，他们的框架系统在 GSM8K 上将 token 使用量提升了 2 到 10 倍，支持了适当规模的技术可以超越更大模型的观点。另一位指出需要合适的框架来防止错误级联。

**标签**: `#LLM`, `#guardrails`, `#agentic`, `#open-source`, `#reliability`

---

<a id="item-6"></a>
## [苹果通过无障碍功能推出代理式 AI](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/) ⭐️ 8.0/10

苹果宣布了新的无障碍功能，其中融入了代理式 AI，使系统能够自主感知、推理并代表残障用户采取行动。 这标志着苹果战略性地进入代理式 AI 领域，在低风险环境中秘密测试高级自主性，可能重塑 AI 在其生态系统中的部署方式。 这些功能利用设备端 AI 执行描述周围环境或阅读文档等任务，无需用户干预，符合苹果注重隐私的策略。

hackernews · interpol_p · May 19, 12:04 · [社区讨论](https://news.ycombinator.com/item?id=48192224)

**背景**: 代理式 AI 指的是能够在有限监督下追求目标并采取行动的 AI 系统，使用工具和推理。苹果有在普通功能中秘密测试新技术的传统，例如 Touch Bar 引入 T1 芯片为 Apple Silicon 过渡做准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**社区讨论**: 评论者指出苹果通过无障碍功能秘密测试技术的模式，一些人称赞 LLM 在帮助人们方面的实际效用，而另一些人则批评苹果的语音转文字和文本校正功能落后。

**标签**: `#Apple`, `#accessibility`, `#AI`, `#agentic AI`, `#technology strategy`

---

<a id="item-7"></a>
## [Andrej Karpathy 加入 Anthropic 预训练团队](https://twitter.com/karpathy/status/2056753169888334312) ⭐️ 8.0/10

Andrej Karpathy 在 X 平台宣布加入 Anthropic 的预训练团队，负责为 Claude 提供核心知识和能力的大规模训练工作。 Karpathy 是极具影响力的 AI 研究者和教育家，他的加入表明 Anthropic 持续投资于基础模型能力。他的到来可能加速 Claude 的预训练进展，并激励更广泛的 AI 社区。 据 Anthropic 称，Karpathy 本周将开始在预训练团队工作。他曾联合创立 OpenAI，领导特斯拉 Autopilot 视觉系统，并创建了 nanoGPT 等热门教育项目，以及首创了“vibe coding”一词。

hackernews · dmarcos · May 19, 15:07 · [社区讨论](https://news.ycombinator.com/item?id=48194352)

**背景**: Andrej Karpathy 是知名的 AI 研究者，以在 OpenAI 和特斯拉的工作以及 YouTube 频道和 nanoGPT 等教育贡献而闻名。Anthropic 是一家开发 Claude 模型系列的 AI 安全公司。预训练是大型语言模型从海量文本数据中学习以获取通用知识和能力的阶段。

**社区讨论**: 社区表达了兴奋和支持，许多人希望 Karpathy 尽管可能签署了保密协议，仍能继续他的教育分享。有人指出他在最近的采访中预示了这一举动，还有人将其与电影《创》相类比。

**标签**: `#AI`, `#Anthropic`, `#Karpathy`, `#industry news`, `#deep learning`

---

<a id="item-8"></a>
## [特斯拉得州锂精炼厂日排 23.1 万加仑废水](https://www.autonocion.com/us/tesla-lithium-refinery-texas/) ⭐️ 8.0/10

特斯拉位于得州罗布斯敦的锂精炼厂每天排放多达 23.1 万加仑处理后的废水，流入无名沟渠，最终汇入 Petronila Creek 和 Baffin Bay，检测到的污染物包括六价铬和砷。 这引发了重大的环境和监管担忧，因为六价铬是已知的人类致癌物，且排放可能违反许可条款，可能损害热门钓鱼目的地和当地生态系统。 许可证（TPDES）允许每天最多排放 23.1 万加仑，但未明确授予特斯拉使用公共或私人财产进行废水输送的权利；管理该沟渠的排水区从未收到通知。实验室报告显示六价铬浓度为 0.0104 mg/L（略高于报告限值），砷浓度为 0.0025 mg/L（低于联邦饮用水标准）。

hackernews · atombender · May 19, 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48198551)

**背景**: 锂精炼涉及处理锂辉石矿石以生产用于电池的锂化合物，该过程会产生需要处理后方可排放的废水。六价铬是一种有毒的铬形态，用于工业过程，被列为致癌物，因 Erin Brockovich 案而受到公众关注。特斯拉的这家精炼厂号称美国最大，近期开始运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hexavalent_chromium">Hexavalent chromium</a></li>
<li><a href="https://www.kxan.com/news/texas/tesla-lithium-refinery-largest-in-america-now-operating-in-texas/">Tesla lithium refinery , ‘largest in America,’ now operating in Texas</a></li>

</ul>
</details>

**社区讨论**: 评论者就特斯拉是否合规展开辩论：一些人指出检测到的六价铬和砷含量较低，而另一些人则认为排放未列出的污染物以及未通知排水区表明违反了许可规定。特斯拉声称完全合规的声明受到批评，有人称其具有欺骗性。

**标签**: `#environment`, `#Tesla`, `#lithium`, `#pollution`, `#regulation`

---

<a id="item-9"></a>
## [谷歌 Gemini Omni：视觉惊艳，物理缺陷](https://deepmind.google/models/gemini-omni/) ⭐️ 8.0/10

谷歌发布了 Gemini Omni，这是一个统一的多模态视频生成模型，支持通过文本、图像和音频输入来创建和编辑视频，首个型号 Gemini Omni Flash 现已面向订阅用户开放。 此次发布凸显了 AI 视频生成的快速进步，但也强调了空间连贯性和物理模拟方面的持续挑战，这些对于广告和内容创作等实际应用至关重要。 社区测试显示，Gemini Omni 在处理刚体物理（例如叠叠乐塔）和空间一致性方面存在困难，物体在离开画面后常常消失或变形，表明其缺乏深层的 3D 理解能力。

hackernews · meetpateltech · May 19, 17:46 · [社区讨论](https://news.ycombinator.com/item?id=48196609)

**背景**: 像 Gemini Omni 这样的 AI 视频生成模型通过在视频-文本对上进行大规模训练来学习视觉模式，但它们通常无法显式地建模物理定律和 3D 几何。空间连贯性——即在帧之间保持一致的物体身份和位置的能力——仍然是该领域已知的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gemini-omni.ai/">Gemini Omni Video Generator | AI Video Generator & Editor</a></li>
<li><a href="https://reelmind.ai/blog/ai-video-synthesis-creating-consistent-characters-and-scenes">ReelMind - Open Source AI Video Models Community</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户认为 Gemini Omni 与 Seedance 等替代品相比并不令人印象深刻，而另一些用户则指出了空间推理和物理方面的根本性问题。一位测试刚体物理的用户指出，积木会突然消失或变形，表明该模型缺乏对物理世界的结构化理解。

**标签**: `#AI`, `#video generation`, `#Google`, `#spatial reasoning`, `#deep learning`

---

<a id="item-10"></a>
## [中美同意开展人工智能政府间对话](https://www.news.cn/world/20260519/883ac1ee99c74a8fa2441da4d4b40e96/c.html) ⭐️ 8.0/10

在中国外交部 5 月 19 日的声明中，中美两国元首在特朗普总统访华期间同意开展人工智能政府间对话。 这一协议标志着全球两大人工智能强国在 AI 治理方面迈出重要合作步伐，可能影响全球 AI 发展和安全规范的制定。 对话将聚焦人工智能发展与治理，旨在确保该技术服务于人类进步和全球共同福祉。具体时间表和议程尚未公布。

telegram · zaihuapd · May 19, 09:42

**背景**: 人工智能是一个快速发展的领域，具有重大的经济和安全影响。中美两国一直在争夺 AI 领导地位，同时也面临在安全和伦理方面进行国际合作的呼声。此次对话为在政府层面解决这些问题提供了正式渠道。

**标签**: `#AI governance`, `#US-China relations`, `#international policy`, `#diplomacy`

---

<a id="item-11"></a>
## [伊朗要求美科技公司为海底电缆付费](https://arstechnica.com/tech-policy/2026/05/iran-demands-big-tech-pay-fees-for-undersea-internet-cables-in-strait-of-hormuz/) ⭐️ 8.0/10

伊朗宣布将对经过霍尔木兹海峡的海底互联网电缆收费，目标包括 Meta、Google、Amazon、Microsoft 等美国科技巨头，并声称拥有电缆独家维修权。 此举威胁到全球互联网的关键咽喉要道，可能扰乱主要科技公司的数据流，并促使寻找替代电缆路线以规避地缘政治风险。 伊朗官媒发出含蓄的电缆损坏威胁，而地区冲突已导致该区域多个电缆项目停工和维修暂停。

telegram · zaihuapd · May 19, 16:40

**背景**: 霍尔木兹海峡是连接波斯湾与阿曼湾的狭窄水道，全球相当一部分海底互联网电缆经过此处。伊朗领海覆盖海峡部分区域，使其对电缆基础设施拥有影响力。类似的地缘政治紧张局势此前曾影响油轮运输，但此次是首次将压力延伸至数字基础设施。

**标签**: `#geopolitics`, `#internet infrastructure`, `#undersea cables`, `#Iran`, `#tech policy`

---