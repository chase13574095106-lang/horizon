---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> From 33 items, 13 important content pieces were selected

---

1. [GitHub 推出堆叠拉取请求公开预览](#item-1) ⭐️ 9.0/10
2. [OpenAI 将 GPT-5.6 Luna 价格降低 80%](#item-2) ⭐️ 9.0/10
3. [Anthropic 的 AI 发现 NIST 后量子候选算法 HAWK 严重漏洞](#item-3) ⭐️ 9.0/10
4. [廉价电视流媒体棒预装恶意软件](#item-4) ⭐️ 8.0/10
5. [DeepMind 的 Gemini Robotics 2 实现机器人全身控制](#item-5) ⭐️ 8.0/10
6. [欧足联及 55 个会员协会威胁抵制国际足联赛事](#item-6) ⭐️ 8.0/10
7. [μ子谜团被破解，旧结果失效](#item-7) ⭐️ 8.0/10
8. [AI 辅助重构的经济效益](#item-8) ⭐️ 8.0/10
9. [GCC 指导委员会通过 AI 贡献政策](#item-9) ⭐️ 8.0/10
10. [英国拟放宽苹果和谷歌支付规则](#item-10) ⭐️ 8.0/10
11. [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动](#item-11) ⭐️ 8.0/10
12. [谷歌 DeepMind 解散诺贝尔奖级 AlphaFold 团队，核心成员转投 Anthropic](#item-12) ⭐️ 8.0/10
13. [欧盟启动 AI 超级工厂招标，拟撬动 3000 亿欧元投资](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GitHub 推出堆叠拉取请求公开预览](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 9.0/10

GitHub 已发布堆叠拉取请求的公开预览，允许开发者将大型更改拆分为一系列有序的、相互依赖的小型拉取请求，这些请求可以独立审查和合并。 此功能通过支持增量代码审查和减少合并冲突，显著改善了开发者工作流程，使管理复杂更改更加容易。这是 GitHub 历史上最大的发布之一，影响了从 Actions 到 UI 的几乎所有服务。 该功能可通过 GitHub CLI 的 `gh stack` 扩展使用，用户可从 `gh.io/stacks` 安装。但存在一些未修复的 bug，例如在某些情况下合并整个堆栈会失败，以及压缩合并需要堆栈中每个 PR 重新批准。

hackernews · tomzorz · Jul 30, 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49112232)

**背景**: 堆叠拉取请求是一种工作流程，将更改组织成一系列相互依赖的拉取请求，每个请求代表整体更改的一个逻辑层。这种方法在大型代码库中很常见，以促进并行审查和更快的迭代。GitHub 的实现与现有的拉取请求功能（如审查和检查）集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/">Stacked pull requests are now in public preview - GitHub Changelog</a></li>
<li><a href="https://github.github.com/gh-stack/">GitHub Stacked PRs | GitHub Stacked PRs</a></li>
<li><a href="https://docs.github.com/en/pull-requests/how-tos/stacked-pull-requests">Stacked pull requests 🥞 - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些开发者对工作流程改进感到兴奋，而另一些则报告了重大 bug，例如堆栈合并失败和需要重新批准。一位 GitHub 团队成员承认了这些问题，并承诺会推出更多更新。

**标签**: `#GitHub`, `#version control`, `#developer workflow`, `#pull requests`, `#software engineering`

---

<a id="item-2"></a>
## [OpenAI 将 GPT-5.6 Luna 价格降低 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 9.0/10

OpenAI 宣布将其最快、最经济的模型 GPT-5.6 Luna 的价格降低 80%，使其输入令牌每百万个 0.10 美元，输出令牌每百万个 0.60 美元。 这一大幅降价标志着 AI 模型性价比提升的新阶段，使企业能够大规模部署高容量 AI 工作流，并让先进 AI 更加普及。 此次降价适用于 Luna 和 Terra 模型，其中 Luna 的成本降低了 80%。改进源于内核优化（使服务成本降低 20%）和实验（使令牌生成效率提高超过 15%）。

hackernews · tedsanders · Jul 30, 17:15 · [社区讨论](https://news.ycombinator.com/item?id=49112867)

**背景**: GPT-5.6 是 OpenAI 最新的模型系列，包括 Sol（旗舰）、Terra（均衡）和 Luna（高性价比）。Luna 原本就是一款便宜且能力强的模型，此次 5 倍降价使其对深度研究、多智能体系统等高容量任务更具吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/">Advancing the price - performance frontier with GPT-5.6 | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了惊讶和兴奋，将此次降价比作从拨号上网到宽带的转变。有人指出，虽然 Luna 非常强大，但区分琐碎和非琐碎任务仍然是一个难题。其他人则强调了在相同成本下运行更多并行代理的潜力。

**标签**: `#AI`, `#GPT-5.6`, `#pricing`, `#OpenAI`, `#inference`

---

<a id="item-3"></a>
## [Anthropic 的 AI 发现 NIST 后量子候选算法 HAWK 严重漏洞](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic 宣布，其 Claude Mythos Preview 模型在大约 60 小时内发现了 NIST 后量子候选算法 HAWK 的严重弱点，将其有效密钥强度从 2^64 降至 2^38。该攻击耗费约 10 万美元 API 费用，而人类专家此前两年未能发现。 这一突破表明，AI 现在在发现密码学弱点方面可以超越人类密码分析员，可能加速后量子算法的安全评估。它也凸显了组织采用密码敏捷性并在联邦截止日期前迁移到标准化后量子密码学的紧迫性。 该攻击不在多项式时间内运行，因此更大的密钥仍然安全，HAWK 也尚未被公开撤回。Anthropic 还报告了对七轮 AES-128 的改进攻击，但完整 AES-128 使用十轮，因此生产系统不受影响。

telegram · zaihuapd · Jul 30, 05:47

**背景**: 后量子密码学旨在开发能够抵抗未来量子计算机的算法，量子计算机可能破解当前加密。NIST 一直在进行多轮标准化过程；HAWK 是数字签名的第三轮候选算法。白宫行政令要求联邦机构在 2030 年前迁移到抗量子密钥体系，在 2031 年前完成数字签名迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate... - Ars Technica</a></li>
<li><a href="https://www.techzine.eu/news/applications/143290/mythos-knocks-hawk-out-of-the-race-for-a-post-quantum-standard/">Mythos knocks HAWK out of the race for a post - quantum standard</a></li>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调这是 AI 在密码学中的突破性应用，但一些评论者警告该攻击不是多项式时间，因此并未完全破解 HAWK。其他人则争论成本效益以及 AI 是否会取代人类密码分析员还是作为工具使用。

**标签**: `#AI`, `#cryptography`, `#post-quantum`, `#NIST`, `#security`

---

<a id="item-4"></a>
## [廉价电视流媒体棒预装恶意软件](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) ⭐️ 8.0/10

一篇安全文章警告称，许多廉价电视流媒体棒（如 H96 型号）出厂即预装恶意软件，可用于广告欺诈和住宅代理僵尸网络，带来严重的隐私和安全风险。 这很重要，因为数百万消费者在不知情的情况下将这些受感染的设备带入家中，使攻击者能够利用他们的互联网连接进行欺诈活动，甚至可能对关键基础设施发起攻击。 该恶意软件可在用户不知情的情况下静默启动浏览器、访问网站、点击广告，并用于住宅代理任务。尽管屡次收到警告，主要电商平台仍在销售数百种此类型号。

hackernews · speckx · Jul 30, 17:04 · [社区讨论](https://news.ycombinator.com/item?id=49112744)

**背景**: 住宅代理僵尸网络利用受感染的家庭设备通过真实住宅 IP 地址路由互联网流量，使欺诈活动看似合法。广告欺诈恶意软件生成虚假点击和展示以窃取广告收入。这些廉价流媒体棒通常运行过时的 Android 版本且无安全补丁，极易成为攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/">Read This Before You Buy That TV Streaming Stick – Krebs on Security</a></li>
<li><a href="https://spur.us/blog/residential-proxies-the-legal-botnet-that-nobody-talks-about">Residential Proxies : The Legal Botnet Nobody Talks About</a></li>
<li><a href="https://captchafox.com/learn/residential-proxies">What Are Residential Proxies ? Bot Attacks & Detection</a></li>

</ul>
</details>

**社区讨论**: 评论者对亚马逊、百思买等主要零售商销售这些有害设备却几乎不承担责任表示不满。有人分享了使用类似产品的亲身经历，也有人指出设备安全方面的疏忽同样会导致风险。少数评论者讨论了自行构建安全流媒体设备作为替代方案。

**标签**: `#security`, `#privacy`, `#IoT`, `#botnet`, `#streaming`

---

<a id="item-5"></a>
## [DeepMind 的 Gemini Robotics 2 实现机器人全身控制](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind 发布了 Gemini Robotics 2，该模型为人形机器人赋予全身智能，使其能够执行协调的全身运动和高级灵巧操作任务，并支持多机器人在共享空间中的协同工作。 这标志着从仅控制上半身到全身智能的重大进步，可能加速人形机器人在家庭和工作场所等真实环境中的部署。这一进展类似于大型语言模型所经历的快速改进，预示着在不久的将来会出现变革性的应用。 该系统集成了一个用于理解的视觉语言模型，以及两个分别控制全身和手部动作的视觉语言动作模型。之前的模型仅控制上半身执行桌面任务，而 Gemini Robotics 2 扩展到了全身运动。

hackernews · ai2027 · Jul 30, 15:15 · [社区讨论](https://news.ycombinator.com/item?id=49111237)

**背景**: 人形机器人传统上由于执行器和控制算法的限制，难以实现流畅、协调的全身运动。DeepMind 的方法利用大型基础模型（如 Gemini）直接从视觉和语言输入生成机器人动作，绕过了传统编程。这项工作建立在早期专注于上半身操作的 Gemini Robotics 模型之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body intelligence to robots — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/gemini-robotics/">Gemini Robotics 2</a></li>
<li><a href="https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/">Google's new Gemini Robotics 2 platform allows for 'intelligent whole-body control' - Engadget</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一位 DeepMind 研究员称赞该实验室在前沿模型和机器人领域的广度，而其他人则对当前机器人的速度和执行器质量表示怀疑。一些人将其与早期 LLM 的进展相类比，认为快速改进是可能的。

**标签**: `#robotics`, `#AI`, `#DeepMind`, `#Gemini`, `#whole body intelligence`

---

<a id="item-6"></a>
## [欧足联及 55 个会员协会威胁抵制国际足联赛事](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/) ⭐️ 8.0/10

欧足联及其 55 个会员协会发表联合声明，威胁如果国际足联继续推进扩大世俱杯以及引入外部投资进入其赛事的计划，他们将抵制包括世界杯在内的国际足联赛事。 这一威胁标志着全球足球治理可能出现的分裂，因为欧足联代表着最强大、最赚钱的足球地区。抵制行动可能削弱国际足联的旗舰赛事，并迫使国际足球的权力结构进行重组。 该声明特别反对国际足联将世俱杯扩军至 32 支球队的计划，以及拟议创建一项由国际足联支持的新国际俱乐部赛事。欧足联认为这些举措优先考虑商业回报，而非球员和运动的福祉。

hackernews · dickfickling · Jul 30, 18:40 · [社区讨论](https://news.ycombinator.com/item?id=49113929)

**背景**: 国际足联和欧足联长期以来一直是世界足球中最有权势的两个机构，但在治理、赛事形式和财务控制方面的紧张局势不断升级。国际足联最近推动更频繁、更大规模的赛事，包括两年一届世界杯的提议，遭到了欧足联和其他联合会的强烈反对。

**社区讨论**: 评论者普遍支持欧足联的立场，批评国际足联主席因凡蒂诺腐败，并优先考虑金钱而非运动本身。一些人建议欧足联自行举办世界杯，而另一些人则警告说，外部投资将使足球变成由股东回报驱动的商业活动。

**标签**: `#sports`, `#governance`, `#FIFA`, `#UEFA`, `#boycott`

---

<a id="item-7"></a>
## [μ子谜团被破解，旧结果失效](https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/) ⭐️ 8.0/10

物理学家解决了一个长期存在的μ子异常问题，表明先前的实验结果存在缺陷，不再与理论预测一致。 这一发现改变了粒子物理学的基础，可能消除了标准模型之外新物理的一个关键线索，并重新引导未来的研究方向。 费米实验室的 Muon g-2 实验测量了μ子的反常磁矩，但更新的格点 QCD 计算使理论与实验一致，将差异从 4.2 西格玛降低到 0.5 西格玛。

hackernews · ibobev · Jul 30, 15:22 · [社区讨论](https://news.ycombinator.com/item?id=49111305)

**背景**: μ子的磁矩是标准模型的一个敏感测试。测量值与预测值之间的持续差异，即μ子 g-2 异常，曾暗示可能存在新粒子。最近格点 QCD 的进展改进了理论预测，解决了这一异常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muon_g−2_Experiment">Muon g−2 Experiment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Muon_g-2">Muon g-2 - Wikipedia</a></li>
<li><a href="https://muon-g-2.fnal.gov/">Fermilab | Muon g-2</a></li>

</ul>
</details>

**社区讨论**: 评论对长期问题的解决表示欣慰，有用户开玩笑说幸好没花十年时间研究这个问题。其他人则反思科学哲学，指出即使有缺陷的模型也能用于预测，范式转变是进步的一部分。

**标签**: `#physics`, `#muon`, `#particle physics`, `#scientific discovery`

---

<a id="item-8"></a>
## [AI 辅助重构的经济效益](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 8.0/10

Martin Fowler 发表了一篇文章，量化了使用 AI 辅助代码重构的经济效益，展示了在 token 效率和代码质量方面的可衡量改进。 这项分析为 AI 在软件工程中的价值提供了基于实际数据的定量证据，超越了模糊的宣称，给出了可指导投资决策的具体测量结果。 文章包含了应用 AI 辅助重构时 token 消耗减少和推理改进的具体指标，并附有实际用例示例。

hackernews · javaeeeee · Jul 30, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=49111176)

**背景**: 重构是指在不改变代码外部行为的前提下重组现有代码的过程，通常旨在提高可读性、可维护性或性能。像大语言模型这样的 AI 工具可以通过建议或自动化部分过程来辅助重构，但其经济影响此前尚不明确。

**社区讨论**: 评论者指出，程序员常被忽视的最佳实践正在为 AI 重新发现，并称赞文章具体且基于实际的批评。一些人强调在代理式重构中需要人工监督，因为 AI 可能缺乏对项目整体背景的理解。

**标签**: `#refactoring`, `#AI`, `#software engineering`, `#economics`, `#best practices`

---

<a id="item-9"></a>
## [GCC 指导委员会通过 AI 贡献政策](https://lwn.net/Articles/1086041/) ⭐️ 8.0/10

GCC 指导委员会已接受 GCC AI 政策工作组推荐的 AI 贡献政策，为处理对 GCC 项目的机器生成贡献制定了指导方针。 该政策为大型开源项目如何管理 AI 生成的代码树立了先例，解决了质量、版权和社区治理问题。它将影响其他项目的类似政策，并影响使用 AI 工具进行贡献的开发者。 该政策要求披露贡献中的 AI 参与，并可能限制或要求对机器生成的补丁进行人工审查。完整政策文本可在 GCC forge 仓库中找到。

hackernews · arto · Jul 30, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=49108685)

**背景**: GCC（GNU 编译器套件）是一个关键的开源编译器项目。指导委员会成立于 1998 年，负责项目的重大决策。随着 AI 生成的代码变得普遍，项目需要政策来确保贡献质量和法律清晰度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1086041/">GCC steering committee announces AI policy [LWN.net]</a></li>
<li><a href="https://gcc.gnu.org/steering.html">GCC steering committee - GNU Project</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出支持和怀疑的混合态度。一些人赞扬 GNU 项目的欢迎态度，而另一些人则指出，AI 公司可能从开源项目采用此类政策中受益，因为这保持了仓库的清洁以供训练数据使用。一句引人注目的引述强调了 AI 使财富能够获取技能而技能无法获取财富的担忧。

**标签**: `#open source`, `#AI policy`, `#GCC`, `#community governance`, `#software engineering`

---

<a id="item-10"></a>
## [英国拟放宽苹果和谷歌支付规则](https://t.me/zaihuapd/42855) ⭐️ 8.0/10

6 月 30 日，英国竞争与市场管理局（CMA）提议允许应用开发者将用户引导至苹果和谷歌应用商店之外的支付选项，并可能要求苹果开放 NFC 技术，以便在 iOS 应用中提供非接触式支付。 该提案可能大幅降低苹果和谷歌向开发者收取的费用，促进移动生态系统竞争，并为全球数字市场监管树立先例。 CMA 表示，苹果或谷歌对引导用户收取的任何费用必须公平合理，且低于当前应用商店佣金，节省的费用应让消费者受益或用于创新。该提案是英国 2024 年《数字市场、竞争与消费者法案》下咨询的一部分。

telegram · zaihuapd · Jul 30, 02:10

**背景**: 苹果和谷歌去年被 CMA 认定在移动生态中具有“战略市场地位”，使监管机构拥有更强的干预权力。英国 2024 年《数字市场、竞争与消费者法案》近期生效，授权 CMA 对具有该地位的公司施加行为要求。NFC（近场通信）技术可实现通过智能手机和卡片进行非接触式支付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets,_Competition_and_Consumers_Act_2024">Digital Markets, Competition and Consumers Act 2024 - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2025/01/23/uk-probes-apple-and-google-over-mobile-ecosystem-market-power/">UK probes Apple and Google over ' mobile ecosystem ' market power</a></li>
<li><a href="https://stripe.com/resources/more/how-to-accept-contactless-nfc-payments-from-customers">What are contactless NFC payments? A guide for businesses</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#app store`, `#regulation`, `#Apple`, `#Google`

---

<a id="item-11"></a>
## [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动](https://t.me/zaihuapd/42859) ⭐️ 8.0/10

2026 年 7 月 29 日，俄罗斯联邦安全局（FSB）依据《俄罗斯联邦刑法典》第 205.1 条第 1.1 款，对 Telegram 创始人帕维尔·杜罗夫提起协助恐怖活动的刑事指控，并将其列入国际通缉名单。 这一针对大型科技创始人的前所未有的法律行动，可能为平台责任和言论自由树立危险先例，进而影响加密通讯服务在全球的运营方式。 FSB 指控 Telegram 管理层拒不删除被乌克兰情报机构及恐怖、极端主义组织用于在俄境内策划和协调破坏活动、恐怖袭击、大规模杀戮及网络诈骗的频道、群组和机器人，造成包括妇女儿童在内的多人伤亡和数十亿卢布损失。

telegram · zaihuapd · Jul 30, 03:45

**背景**: Telegram 是由帕维尔·杜罗夫创立的加密通讯平台，他于 2014 年因拒绝遵守政府要求封锁反对派团体而离开俄罗斯。该平台因托管极端主义内容而受到批评，但也因保护用户隐私而受到赞扬。《俄罗斯联邦刑法典》第 205.1 条涉及协助恐怖活动，最高可判处终身监禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cj4kexqkpzno">Russia charges Telegram founder Pavel Durov with facilitating...</a></li>
<li><a href="https://www.aljazeera.com/news/2026/7/29/russia-charges-telegram-founder-pavel-durov-with-aiding-terrorism">Russia charges Telegram founder Pavel Durov with... | Al Jazeera</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pavel_Durov">Pavel Durov - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#legal`, `#terrorism`

---

<a id="item-12"></a>
## [谷歌 DeepMind 解散诺贝尔奖级 AlphaFold 团队，核心成员转投 Anthropic](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 8.0/10

谷歌 DeepMind 解散了曾获诺贝尔奖的蛋白质结构预测 AI 系统 AlphaFold 的研发团队，并将大部分成员调至其他项目。三名核心研究人员 John Jumper、Jonas Adler 和 Alexander Pritzel 已离职，加入 AI 安全与开发领域的竞争对手 Anthropic。 此举标志着 DeepMind 的战略重心从结构生物学转向大语言模型和其他 AI 前沿领域，可能会减缓 AI 驱动药物发现的进展。同时，这也凸显了顶级 AI 实验室之间激烈的人才竞争，Anthropic 获得了关键的专业人才。 近四分之一的 AlphaFold 原始论文作者已完全离开公司，其他人则内部转岗至 Gemini、酶设计、核聚变和基因组学等项目。部分人转至 Alphabet 旗下的药物研发公司 Isomorphic Labs。

telegram · zaihuapd · Jul 30, 07:45

**背景**: AlphaFold 是 DeepMind 开发的 AI 系统，能从氨基酸序列预测蛋白质三维结构，在 2020 年的 CASP14 竞赛中取得了突破性精度。其创造者 Demis Hassabis 和 John Jumper 因此获得了 2024 年诺贝尔化学奖。该系统已被广泛应用于生物学和药物发现领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini ( language model ) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AlphaFold`, `#DeepMind`, `#Anthropic`, `#AI Research`, `#Talent Movement`

---

<a id="item-13"></a>
## [欧盟启动 AI 超级工厂招标，拟撬动 3000 亿欧元投资](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

欧盟委员会正式启动 AI 超级工厂招标，旨在撬动约 3000 亿欧元投资，其中 100 亿欧元来自欧盟和成员国资金。招标支持最多七座 AI 超级工厂，投标截止日期为 11 月 12 日，中标结果预计 2027 年 7 月公布。 该举措标志着欧盟在建设自主 AI 基础设施、与美国和中国在先进 AI 开发领域竞争方面的重大战略推进。这些超级工厂将支持训练包含数万亿参数的下一代 AI 模型，影响医疗、清洁技术和太空等领域。 招标分为选址和扩建两个阶段。项目须在签约后 18 个月内投入运营。欧洲高性能计算联合体（EuroHPC JU）负责监督该计划。

telegram · zaihuapd · Jul 30, 11:50

**背景**: AI 超级工厂是专门用于开发和训练超大规模 AI 模型的大型设施，需要大量计算基础设施。欧盟已承诺建立四到五座此类设施，欧洲投资银行也提供融资支持。此举旨在减少欧洲对非欧盟数据中心和 AI 能力的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eurohpc-ju.europa.eu/ai-gigafactories_en">AI Gigafactories - The European High Performance Computing Joint Undertaking (EuroHPC JU)</a></li>
<li><a href="https://www.eib.org/en/press/all/2025-491-eib-group-and-european-commission-join-forces-to-finance-ai-gigafactories">EIB Group and European Commission join forces to finance AI gigafactories</a></li>
<li><a href="https://www.polytechnique-insights.com/en/columns/digital/european-ai-gigafactories-the-true-the-false-and-the-uncertain/">European AI gigafactories: the true, the false and the uncertain</a></li>

</ul>
</details>

**标签**: `#AI`, `#EU`, `#infrastructure`, `#investment`, `#policy`

---