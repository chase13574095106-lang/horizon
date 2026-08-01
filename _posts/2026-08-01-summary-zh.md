---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> From 34 items, 8 important content pieces were selected

---

1. [OpenAI 的 Astra 模型在十个长期数学难题上取得突破](#item-1) ⭐️ 9.0/10
2. [NetBSD 11.0 发布，带来快速启动的 MICROVM 内核和防火墙改进](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4-Flash-0731：低成本高智能](#item-3) ⭐️ 8.0/10
4. [无状态 MCP 2.0 重燃兴趣，催生新工具](#item-4) ⭐️ 8.0/10
5. [三大唱片公司提议将 AI 歌曲挡在榜单之外](#item-5) ⭐️ 8.0/10
6. [谷歌确认 Android 16 开发者验证分免费和付费两档](#item-6) ⭐️ 8.0/10
7. [中国在联合国峰会向全球南方推广开放权重 AI，与美国闭源模型形成对比](#item-7) ⭐️ 8.0/10
8. [微软确认今年推出 Copilot 超级应用](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 模型在十个长期数学难题上取得突破](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI 宣布其下一代模型 Astra 的内部版本在十个长期未解决的数学与理论计算机科学问题上取得了进展，涵盖高维球体堆积、非索菲克群存在性、Connes 刚性猜想反例、算术电路下界、量子并行重复、最近向量问题硬度及多色 Ramsey 数等。这些论证已在 Lean 中形式化验证，每个论证生成的 token 成本约为 2000 美元。 这一成就可能对数学和 AI 研究产生重大影响，表明 AI 模型能够为解决困扰人类数十年的问题做出贡献。同时，它也引发了关于 AI 在数学发现中的作用以及 AI 生成证明的透明性和验证需求的重要问题。 这些成果通过人机协作整理成论文，数学论证由 AI 生成，人类负责整理和形式化。OpenAI 对 AI 的作用保持透明，证明可在 GitHub 上的 openai/ten-proofs 仓库中获取，同时还有一篇论文和一个由 LLM 生成的 PDF，用于重建推理过程。然而，独立验证仍在进行中，且未披露尝试但未成功的问题数量。

telegram · zaihuapd · Aug 1, 07:59

**背景**: 球体堆积问题探讨如何在多维空间中排列球体以最大化密度，在编码理论和密码学中有应用。索菲克群是 Gromov 引入的一类群，所有群是否都是索菲克的问题仍未解决。Connes 嵌入问题于 1970 年代提出，询问每个冯诺依曼代数是否能嵌入到超有限 II_1 因子的超幂中，与量子信息理论相关。这些问题在其各自领域中都处于核心地位，且数十年来进展缓慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sofic_group">Sofic group - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Connes_embedding_problem">Connes embedding problem - Wikipedia</a></li>
<li><a href="https://www.sohu.com/a/911584031_122396381">意外突破：新方法刷新高维球体堆积记录_塔格_椭球_问题</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论反映了惊叹与怀疑并存的态度。许多数学家正经历着“深蓝时刻”，对 AI 在数学中的作用既感到兴奋又存在存在主义担忧。一些评论者赞扬 OpenAI 在分享证明和形式化方面的透明度，而另一些人则质疑未披露失败尝试的细节以及独立验证的必要性。这种情绪与陶哲轩关于“大数学”的愿景相呼应，即 AI 处理技术性繁重工作，人类专注于创造性方面。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#formal verification`

---

<a id="item-2"></a>
## [NetBSD 11.0 发布，带来快速启动的 MICROVM 内核和防火墙改进](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 8.0/10

NetBSD 11.0 已正式发布，为 x86（i386 和 amd64）引入了新的 MICROVM 内核，可在约 10 毫秒内启动，并改进了 npf 防火墙，包括二层过滤和用户/组过滤。 这一重要版本增强了 NetBSD 在轻量级虚拟化和边缘计算领域的吸引力，可能吸引对超快启动时间和最小资源占用感兴趣的用户。防火墙改进也增强了其安全性能，使其与其他 BSD 和 Linux 相比更具竞争力。 MICROVM 内核利用 PVH 启动、VirtIO MMIO 和多项内核优化实现了约 10 毫秒的启动时间，专为 QEMU microvm 机器类型设计，该类型不支持 PCI 总线和 ACPI。该版本还通过 compat_linux 改进了 Linux 系统调用兼容性，并包含多项硬件改进。

hackernews · jaypatelani · Aug 1, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49136736)

**背景**: NetBSD 是一个免费、开源的类 Unix 操作系统，以其跨多种硬件平台的可移植性以及对正确性和简洁设计的关注而闻名。MICROVM 内核是一种新配置，可实现极快的虚拟机启动时间，特别适用于无服务器计算和微服务。npf 防火墙是 NetBSD 的包过滤器，新的二层和用户/组过滤功能提供了对网络流量更细粒度的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.netbsd.org/releases/formal-11/NetBSD-11.0.html">Announcing NetBSD 11.0 (July 30, 2026)</a></li>
<li><a href="https://wiki.netbsd.org/users/imil/microvm/">microvm - wiki.netbsd.org</a></li>
<li><a href="https://www.osnews.com/story/145663/netbsd-11-0-released/">NetBSD 11.0 released – OSnews</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了对 BSD 与 Linux 当前状态的兴趣，提出了关于使用、开发和安全加固的问题。一些用户表示有兴趣在旧硬件上运行 NetBSD，并使用 Wine 运行仅限 Windows 的软件，而其他人则强调了该版本的有价值功能，如防火墙改进和 MICROVM 内核的潜力。还有人注意到发布公告对未解决问题表示歉意，但这被视为透明度的积极信号。

**标签**: `#NetBSD`, `#BSD`, `#operating systems`, `#release`, `#virtualization`

---

<a id="item-3"></a>
## [DeepSeek V4-Flash-0731：低成本高智能](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 于 2026 年 7 月 31 日发布了 DeepSeek-V4-Flash-0731，并将 V4-Flash API 转为公开测试版。这款 304B 参数的模型显著增强了智能体能力，定价为每百万输入 token 0.14 美元、每百万输出 token 0.27 美元。 该版本在智能指数上领先于 MiniMax M3 等更大模型，但成本却低得多，提供了顶级性价比。它可能重塑竞争格局，让高性能智能体 AI 以远低于竞争对手的成本变得可及。 该模型总参数为 304B，在 Hugging Face 上大小为 167GB，但部分来源报告为 284B 参数，每个 token 激活 13B。如 Simon Willison 的鹈鹕测试所示，提高推理努力设置可显著提升性能。

rss · Simon Willison · Jul 31, 23:59

**背景**: DeepSeek 是一家以高效开源权重模型闻名的中国 AI 公司。V4-Flash 是 V4 系列中注重效率的变体，专为高吞吐量的智能体工作负载设计。Artificial Analysis 智能指数综合多项基准测试，提供单一智能分数，而每任务成本指标有助于比较性价比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained</a></li>
<li><a href="https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/">DeepSeek Upgrades DeepSeek-V4-Flash-0731 with Major Agentic ...</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#language models`, `#model release`, `#cost efficiency`

---

<a id="item-4"></a>
## [无状态 MCP 2.0 重燃兴趣，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 讨论了 MCP 2.0（2026-07-28 版 Model Context Protocol 规范）的发布，该版本引入了无状态协议核心，他构建了两个新工具 mcp-explorer 和 datasette-mcp 来探索其功能。 此次更新大幅简化了 MCP 的实现并提高了可扩展性，可能重新激发人们对 MCP 的兴趣，将其作为让代理拥有完整 shell 访问权限的更安全、更可审计的替代方案。这可能会促使 MCP 在企业级和本地 AI 应用中得到更广泛的采用。 新的无状态 MCP 使用单个 HTTP 请求，通过 MCP-Protocol-Version 和 Mcp-Method 等头部信息，消除了对会话 ID 和服务器端状态的需求。Simon Willison 构建了 mcp-explorer（一个用于交互式探测 MCP 服务器的 CLI 工具）和 datasette-mcp（可能将 MCP 与 Datasette 集成）。

rss · Simon Willison · Jul 31, 23:13

**背景**: MCP（Model Context Protocol）是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 AI 应用连接到外部工具和数据源。它在 2025 年获得了巨大关注，但后来被 Anthropic 的 Skills 功能所掩盖，后者允许代理更灵活地使用终端和 curl。然而，让代理拥有完整的 shell 访问权限存在安全风险，而无状态 MCP 提供了一种更简单、更可审计的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://arstechnica.com/ai/2026/07/with-a-stateless-makeover-new-mcp-spec-targets-enterprise-scale/">With a stateless makeover, new MCP spec targets enterprise scale - Ars Technica</a></li>
<li><a href="https://news.ycombinator.com/item?id=49088058">MCP 2026-07-28 Specification: transport going stateless | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未提供评论。

**标签**: `#MCP`, `#AI agents`, `#protocol`, `#tools`, `#Simon Willison`

---

<a id="item-5"></a>
## [三大唱片公司提议将 AI 歌曲挡在榜单之外](https://www.theverge.com/ai-artificial-intelligence/973741/ai-music-major-record-labels-charts) ⭐️ 8.0/10

环球音乐、索尼音乐和华纳音乐联合提议，AI 生成的歌曲必须“实质由人创作”才能进入官方音乐榜单。该提案不仅要求明确标注，还要求 AI 服务合法授权、训练数据拥有版权，并符合版权和人格权法律。 该提案可能为音乐行业处理 AI 生成内容树立先例，影响艺术家、AI 开发者和流媒体平台。它解决了榜单完整性和版权问题，随着 AI 音乐的普及，这些议题变得至关重要。 该提案得到 IFPI 的支持，但尚无榜单机构采纳。关键术语如“实质由人创作”定义模糊，索尼音乐和环球音乐未回应置评请求。

telegram · zaihuapd · Aug 1, 02:53

**背景**: IFPI（国际唱片业协会）是代表唱片业的全球组织，保护版权。RIAA（美国唱片业协会）是代表美国主要唱片公司的贸易团体。这些组织此前曾提议对 AI 音乐进行标注，但新提案更为严格，聚焦于榜单准入资格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/國際唱片業協會">國際唱片業協會 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/wiki/美國唱片業協會">美國唱片業協會 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#AI music`, `#copyright`, `#music industry`, `#policy`, `#charts`

---

<a id="item-6"></a>
## [谷歌确认 Android 16 开发者验证分免费和付费两档](https://t.me/zaihuapd/42911) ⭐️ 8.0/10

谷歌已确认 Android 16 将推出新的开发者验证系统，要求所有侧载应用的开发者注册包名和签名密钥。该系统提供免费档（安装次数有限）和付费档（费用 25 美元，与 Google Play 注册费相同）。 这一政策变化可能对侧载实践产生重大影响，影响开发者、隐私倡导者以及 F-Droid 等开源应用商店。它可能增加独立开发者的门槛，并引发对数据收集和潜在审查的担忧。 验证将基于云端，可能需要网络连接，并可能影响开源应用商店的运行。谷歌不会公开侧载开发者名单，但会收集个人信息，引发隐私担忧。

telegram · zaihuapd · Aug 1, 03:08

**背景**: 侧载是指在官方应用商店之外安装应用，通常通过 APK 文件进行。谷歌的新验证系统旨在通过确保开发者经过验证来增强安全性，但因其可能损害开源生态系统和用户隐私而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.android.com/developer-verification">Android developer verification | Android Developers</a></li>
<li><a href="https://developer.android.com/developer-verification/guides">Android developer verification | Android Developers</a></li>
<li><a href="https://support.google.com/android-developer-console/answer/16561738?hl=en">Understanding Android developer verification</a></li>

</ul>
</details>

**标签**: `#Android`, `#Developer Verification`, `#Privacy`, `#Sideloading`, `#Google`

---

<a id="item-7"></a>
## [中国在联合国峰会向全球南方推广开放权重 AI，与美国闭源模型形成对比](https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future) ⭐️ 8.0/10

7 月底在日内瓦联合国“智能向善”峰会上，中国代表团向巴基斯坦、俄罗斯、赞比亚等发展中国家推介中国的开放权重 AI 模型。阿里云架构师王坚表示，中国 AI 可以像能源一样成为其他国家发展的“基石”。 此举将中国定位为美国闭源 AI 模型的替代选择，可能塑造全球 AI 基础设施和标准。这可能导致发展中国家对中国技术的依赖加深，影响 AI 领域的地缘政治平衡。 美国前沿实验室及特朗普政府官员明显缺席此次峰会。美国国务院发言人警告称，中国的做法“将导致对中国基础设施和标准的依赖”。中国的策略被称为“词元外交”，以低于美国竞争对手的价格提供开源模型，并承诺培训各国使用。

telegram · zaihuapd · Aug 1, 10:06

**背景**: 开放权重 AI 模型公开模型的权重，允许他人使用和修改，但可能不完全符合开源的所有标准。中国的 AI 外交是其构建替代美国主导西方全球秩序努力的一部分，最新数据显示，中国 AI 模型在全球词元消耗量上已连续五周超过美国模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semafor.com/article/07/28/2026/token-diplomacy-how-china-is-shaping-the-worlds-ai-future">Token diplomacy: How China is shaping the world’s AI future ...</a></li>
<li><a href="https://thediplomat.com/2026/05/chinas-plan-for-winning-the-ai-race-hinges-on-the-token-economy-not-chips/">China’s Plan for Winning the AI Race Hinges on the Token ...</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202604/06/WS69d3c692a310d6866eb41d92.html">Chinese AI models lead global token consumption</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#open-source AI`, `#China`, `#global south`

---

<a id="item-8"></a>
## [微软确认今年推出 Copilot 超级应用](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 纳德拉在财报电话会议上确认，公司将于今年推出一款 AI“超级应用”，将 Copilot 的聊天、编程和智能体能力整合在一起，同时覆盖消费者和商用场景。此次整合将把 GitHub Copilot、Copilot Cowork 和 Autopilot 等体验合并到一个应用中。 此举标志着微软战略性地将其分散的 AI 产品整合为一个统一入口，可能重塑消费者和企业环境中用户与 AI 的交互方式。同时，这也加剧了与 OpenAI 的 ChatGPT Work 等集成式 AI 平台的竞争，因为该超级应用可能成为日常生产力和编程任务的核心枢纽。 纳德拉指出，Copilot 正从聊天工具演进到“Cowork”和“Autopilots”，超级应用将在本季度将这些体验（包括代码功能）合并。微软上季度营收达到 900 亿美元，主要由 AI 和云业务推动，为这一计划提供了财务支持。

telegram · zaihuapd · Aug 1, 13:18

**背景**: 智能体 AI 指的是能够在有限监督下实现目标的系统，利用模拟人类决策的 AI 智能体。GitHub Copilot 是一款 AI 编程助手，而 Copilot Cowork 则面向企业任务自动化。超级应用旨在通过提供聊天、编程和智能体工作流的一站式服务，解决用户因 AI 工具分散而产生的困扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aiplanetx.com/p/microsoft-copilot-super-app">Microsoft 's Copilot Super App</a></li>
<li><a href="https://windowsforum.com/windows-news.4/microsoft-copilot-super-app-2026-one-hub-for-chat-github-copilot-agents.421314/">Microsoft Copilot Super App (2026): One Hub for... | Windows Forum</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Enterprise`

---