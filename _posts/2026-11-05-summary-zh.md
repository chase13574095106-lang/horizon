---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> From 31 items, 8 important content pieces were selected

---

1. [Kimi K3.1 Pro：三万亿参数开放权重模型，支持百万级上下文](#item-1) ⭐️ 9.0/10
2. [AI 迫使软件行业面对 40 年技术债务](#item-2) ⭐️ 8.0/10
3. [Go 1.27 推出稳定的 encoding/json/v2 API](#item-3) ⭐️ 8.0/10
4. [Anthropic 推出 FlashProve，通过密码学实现可证明的大语言模型推理](#item-4) ⭐️ 8.0/10
5. [腾讯发布 Hy4 开放权重模型，聚焦游戏开发并开源科学模型](#item-5) ⭐️ 8.0/10
6. [支付宝联合多方发布中国首个智能体商业信任协议 ACT](#item-6) ⭐️ 8.0/10
7. [腾讯向甲骨文租用 10 万枚 AI 芯片，交易额达 70 亿美元](#item-7) ⭐️ 8.0/10
8. [OpenAI 发布 ChatGPT Images 2.0，新增推理与联网搜索能力](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3.1 Pro：三万亿参数开放权重模型，支持百万级上下文](https://t.me/zaihuapd/44920) ⭐️ 9.0/10

Kimi 正式发布 K3.1 Pro，这是 K3.1 系列的首款模型，也是其目前最强的三万亿参数级开放权重模型，支持 100 万 token 上下文窗口。该模型基于 Kimi K3 进行后训练，并在数百个下游领域开展大规模联合强化学习，同时推出速度为标准版 2—3 倍的 Highspeed 版本。 一款三万亿参数级开放权重模型，具备 100 万 token 上下文，并在 Terminal-Bench 4.0 上以 65.7% 对 58.2% 超过 GPT-6 Astra，可能显著改变开放权重大模型的格局，为企业提供可自托管的强有力闭源前沿模型替代方案。其发布也加剧了推理服务商之间的竞争，已有多个第三方平台上线托管。 该模型原生支持多模态与智能体能力，编程能力升级集中在长流程执行和完整项目交付；在 Terminal-Bench 4.0 上得分 65.7%，高于 GPT-6 Astra 的 58.2%，接近 Claude。不过，本地运行完整的三万亿参数模型可能需要大型多 GPU 节点（如 8 块 B300），因此大多数用户将依赖托管推理服务。

telegram · zaihuapd · Nov 4, 15:47

**背景**: Kimi 是月之暗面（Moonshot AI）旗下的大模型品牌，“开放权重”意味着模型的训练参数可公开下载，支持自托管和微调，这与仅提供 API 的闭源模型不同。Terminal-Bench 4.0 是一项在 66 个真实命令行与容器化任务上评估 AI 智能体的基准测试，相比 3.0 版本修复了若干问题以减少测量噪声。100 万 token 的上下文窗口使模型能在单次提示中处理超长输入，例如完整代码库或大量文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3.1-Pro">moonshotai/Kimi-K3.1-Pro - Hugging Face</a></li>
<li><a href="https://www.kimi.ai/blog/kimi-k3-1-pro">Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence</a></li>
<li><a href="https://www.tbench.ai/news/terminal-bench-4-0">Terminal-Bench 4.0</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人认为该模型是“刷榜”（benchmaxxed），并未明显超越 DeepSeek V4.1-Flash；也有人表示实际测试表现强劲，称其是对大多数用例都非常出色的开放模型发布。多位评论者指出，Together、Modal 等第三方推理服务商在相同价格下提供更高吞吐量，暗示成本仍有下降空间；还有评论强调这类发布面向企业而非普通用户。

**标签**: `#LLM`, `#open-weights`, `#Kimi`, `#model-release`, `#benchmarks`

---

<a id="item-2"></a>
## [AI 迫使软件行业面对 40 年技术债务](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) ⭐️ 8.0/10

IEEE Spectrum 的一篇文章认为，AI 正迫使软件行业面对 40 年来积累的技术债务，这在 Hacker News 上引发了 635 条评论和 1068 个点赞的热烈讨论。 这场辩论突显了一个关键矛盾：AI 能快速发现并修复漏洞，但也可能造成无休止的修复工作循环，而非真正消除债务，这影响着开发者和组织如何优先考虑安全与维护。 评论者指出，许多技术债务问题需要重构而非简单补丁，一些人引用《哥德尔、艾舍尔、巴赫》来论证理论上不可能有完全安全的系统。

hackernews · pseudolus · Nov 4, 11:52 · [社区讨论](https://news.ycombinator.com/item?id=50364336)

**背景**: 技术债务是指选择简单但有限的解决方案而非更好方法时，未来返工所需的隐含成本。AI 驱动的漏洞管理利用机器学习来检测和修补安全漏洞，但其对代码质量和安全的长期影响仍存争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/helgihg_in-software-engineering-we-have-a-term-called-activity-7139304651337764865-Y8CS">Helgi Hrafn Gunnarsson on LinkedIn: In software engineering , we...</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-vulnerability-management/">AI Vulnerability Management: Risks, Tools & Best Practices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论呈现两极分化：一些人希望 AI 能偶然发现隐藏的后门和 0-day 漏洞，从而带来更健壮的软件，而另一些人担心这会形成强制性的无功能修复工作 treadmill。一位评论者指出，AI 审计可能最终让开源安全承诺成真，另一位引用《哥德尔、艾舍尔、巴赫》论证所有系统本质上都是可破的。

**标签**: `#AI`, `#cybersecurity`, `#technical debt`, `#software engineering`, `#vulnerability management`

---

<a id="item-3"></a>
## [Go 1.27 推出稳定的 encoding/json/v2 API](https://go.dev/blog/jsonv2) ⭐️ 8.0/10

Go 团队在 Go 1.27 中正式发布了稳定且普遍可用的 encoding/json/v2 和 encoding/json/jsontext 包，这是对 15 年前首次推出的原始 encoding/json 包的重大修订。 此次更新解决了最广泛使用的编程语言之一在 JSON 处理方面长期存在的限制和痛点，并将影响无数依赖 JSON 进行 API、配置和数据交换的 Go 开发者。 v1 版本的 encoding/json 包仍然可用，并受 Go 1 兼容性承诺的保护，因此现有代码将无限期继续工作；两个包相互兼容，并提供了迁移指南以帮助开发者安全过渡。

hackernews · olexsmir · Nov 4, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=50369106)

**背景**: JSON（JavaScript 对象表示法）是一种广泛使用的数据交换格式，而 Go 的 encoding/json 包自语言早期以来一直是 Go 中编码和解码 JSON 的标准方式。随着时间的推移，该包积累了限制和设计问题，促使 Go 团队尝试新的 API，最终演变为 encoding/json/v2。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/jsonv2">A new Go API for JSON - The Go Programming Language</a></li>
<li><a href="https://go.dev/doc/jsonv2-migration">encoding/json/v2 Migration Guide - The Go Programming Language</a></li>
<li><a href="https://pkg.go.dev/encoding/json/v2">json package - encoding/json/v2 - Go Packages</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些开发者欢迎新 API，但对移除 MarshalIndent 表示遗憾，因为这使得简单的美化打印变得更加复杂；其他人则讨论 SIMD 等高级解析技术，并反思 AI 如何改变他们编写 Go 代码的方式。

**标签**: `#go`, `#json`, `#api-design`, `#programming-languages`, `#performance`

---

<a id="item-4"></a>
## [Anthropic 推出 FlashProve，通过密码学实现可证明的大语言模型推理](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic 发布了 FlashProve，这是一个开源原型，利用密码学证明来验证是哪些模型权重和计算产生了特定的大语言模型推理结果，专门针对大型混合专家模型。该系统先对模型进行承诺，然后为每个请求生成证明，且不会泄露专有模型权重的任何信息。 这项工作解决了封闭模型提供商面临的一个关键信任问题：客户如何能确定提供商服务器上实际运行的是哪些权重？它可以增强 AI 服务中的问责制和归因，尽管高昂的计算开销可能会限制其立即实际部署。 该承诺有效期约为 1600 万次请求，大小约为 6.5 MB，证明验证在 24 线程上需要 17 秒（单线程 21 秒）。该方法相比普通推理带来 90-100 倍的计算开销，并且它建立在 VerInf 等先前工作之上，这引发了归属争议。

hackernews · ltononro · Nov 4, 17:17 · [社区讨论](https://news.ycombinator.com/item?id=50368626)

**背景**: 零知识证明（ZKP）允许一方证明某个陈述为真，而不泄露底层数据。在大语言模型的背景下，ZKP 可用于证明特定模型产生了给定输出，同时保持模型权重保密。Anthropic 的 FlashProve 是朝着使此类证明对大型混合专家模型（在最先进 AI 系统中越来越常见）实用化迈出的一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models</a></li>
<li><a href="https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity/">Anthropic is working on a system to prove AI models ... | TechCrunch</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3658644.3670334">zkLLM: Zero Knowledge Proofs for Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了归属争议，指出 FlashProve 建立在 VerInf 项目之上却几乎没有给予认可。其他人则认为，对于开放权重模型，简单地重新运行推理是更便宜、更简单的替代方案，而来自多个独立提供商概率性证明可以避免 90-100 倍的开销。一些人还质疑 17 秒证明验证的实用性以及对确定性推理的需求。

**标签**: `#llm-inference`, `#cryptography`, `#zero-knowledge-proofs`, `#ai-safety`, `#research`

---

<a id="item-5"></a>
## [腾讯发布 Hy4 开放权重模型，聚焦游戏开发并开源科学模型](https://hy.tencent.ai/research/hy4) ⭐️ 8.0/10

腾讯发布了 Hy4，这是一个新的开放权重基础模型，专注于游戏开发，并开源了两个科学基础模型：用于单细胞表示的 HyCell 和用于物理场建模的 HyPDE，它们由 Hy4 和 Hyra 2.0 共同开发。 此次发布意义重大，因为它提供了一个强大的开放权重替代方案，针对游戏开发进行了领域特定调优，并为科学研究贡献了开源工具，可能加速这些领域的工作，并提供了相较于专有模型的透明选择。 Hy4 是一个混合专家模型，总参数 770B，每 token 激活 49B，上下文窗口达 100 万 token，以 Apache 2.0 许可证发布；它针对虚幻引擎、Unity 和 Godot 进行了广泛适配，并支持多人游戏开发，但腾讯承认在研究级数学和长周期编码方面与顶级专有模型存在差距。

hackernews · Philpax · Nov 4, 14:11 · [社区讨论](https://news.ycombinator.com/item?id=50365780)

**背景**: 腾讯 Hy（原混元）是腾讯开发的一系列大语言模型，采用开放权重和混合专家架构。开放权重模型允许开发者下载并在本地运行模型，而专有模型只能通过 API 访问。游戏开发和科学研究是新兴的应用领域，专用基础模型可以显著提高生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tencent_Hy">Tencent Hy - Wikipedia</a></li>
<li><a href="https://www.eesel.ai/blog/tencent-hy4-review">Tencent Hy 4 review: is the 770B open - weight model worth it? | eesel AI</a></li>
<li><a href="https://kie.ai/blog/what-is-tencent-hy4">What Is Tencent Hy 4 ? 770B MoE, 1M Context</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬腾讯开源科学工具，将其与一些限制研究的美国初创公司形成对比，并指出游戏开发重点很有趣。其他人赞赏其坦诚承认与专有模型的差距，还有一位指出 Hy4 在数据分析基准中很彻底但速度慢，每个问题运行许多查询。

**标签**: `#open-weight-models`, `#foundation-models`, `#game-development`, `#AI-research`, `#open-source`

---

<a id="item-6"></a>
## [支付宝联合多方发布中国首个智能体商业信任协议 ACT](https://t.me/zaihuapd/44909) ⭐️ 8.0/10

1 月 16 日，支付宝联合千问 App、淘宝闪购等伙伴发布了智能体商业信任协议（ACT Protocol），这是中国首个面向 Agent 商业需求设计的开放技术框架。该协议使用户可在千问 App 等终端以对话方式完成比价、领券及支付，实现跨平台自动化购物。 这是中国首个智能体商业信任协议，由支付宝、千问、淘宝闪购等主要平台支持，有望为 AI 智能体与电商及支付基础设施的交互制定行业标准。它可能加速 AI 智能体驱动的购物普及，并为智能体经济中安全、用户授权的交易树立先例。 支付宝为此构建了四大核心基础设施标准，确保 AI 执行流程可追溯、可验证，且付款环节始终由用户主导或授权，同时降低商家接入成本。该协议注重信任与问责，要求每笔 AI 执行的交易都有清晰的委托和授权链。

telegram · zaihuapd · Nov 4, 08:45

**背景**: 智能体商业是指 AI 智能体代表用户跨平台进行购物和支付。ACT 协议扩展了 MCP（模型上下文协议）等概念，增加了委托支付授权，使 AI 智能体能够通过支付宝的支付通道进行交易。这是蚂蚁集团更广泛的 AI 商业基础设施建设的一部分，其中包括面向商家的 AI 开放平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://settlegrid.ai/learn/protocols/alipay-trust">ACTP — Agentic Commerce Trust Protocol ( Alipay / Ant Group)</a></li>
<li><a href="https://pandaily.com/alipay-ai-open-platform-agent-commerce-jul2026">Alipay Launches AI Open Platform: The Agent Commerce ... - Pandaily</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-payments-100m-users-4-competing-protocols-one-galong-yao-6smvc">Agentic Payments： 100M Users， 4 Competing Protocols ， and One...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#e-commerce`, `#payment protocols`, `#agent commerce`, `#Alipay`

---

<a id="item-7"></a>
## [腾讯向甲骨文租用 10 万枚 AI 芯片，交易额达 70 亿美元](https://t.me/zaihuapd/44912) ⭐️ 8.0/10

腾讯与甲骨文签订了一份价值约 70 亿美元的五年期租约，租用约 10 万枚因美国出口限制而无法直接购买的先进 AI 芯片。该交易覆盖东南亚多个数据中心，是腾讯迄今为止最大的海外租赁交易。 这笔交易凸显了中国科技巨头如何通过海外租赁来规避美国出口管制，获取先进 AI 算力。它可能加速腾讯的 AI 模型与智能体开发，同时引发华盛顿对芯片限制有效性的担忧。 约 30%的款项需要预付，租期五年，覆盖甲骨文在东南亚的多个数据中心。该安排利用了一个漏洞，即允许中国公司在海外租用而非购买先进芯片。

telegram · zaihuapd · Nov 4, 11:01

**背景**: 美国出口管制禁止中国公司直接购买英伟达高端 GPU 等先进 AI 芯片，旨在减缓中国 AI 发展。然而，从海外云服务商租用算力一直处于灰色地带，中国企业越来越多地采用这种安排。甲骨文在东南亚运营着大量数据中心，使其成为此类租赁的关键合作伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/oracle-kills-7bn-tencent-ai-chip-deal-under-trump-pressure">Oracle Kills $7BN Tencent AI Chip Deal Under Trump... | ZeroHedge</a></li>
<li><a href="https://www.explainx.ai/blog/trump-ai-chip-export-controls-china-remote-access-august-2026">Trump AI Chip Rules: Closing the Cloud Loophole (Aug 2026 ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#Tencent`, `#Oracle`, `#cloud infrastructure`

---

<a id="item-8"></a>
## [OpenAI 发布 ChatGPT Images 2.0，新增推理与联网搜索能力](https://t.me/zaihuapd/44923) ⭐️ 8.0/10

OpenAI 发布了基于 GPT Image 2 模型的 ChatGPT Images 2.0，该模型在图像生成中引入了“思考”能力，可实现逻辑推理与联网搜索。它能够根据单一提示词生成多达 8 张视觉一致的图像，支持漫画、UI 元素等复杂构图，并最高可生成 2K 分辨率的图像。 此次发布标志着图像生成从纯文本到图像的转变，迈向推理驱动和搜索增强的创作方式，有望显著提升专业设计和营销工作流的准确性与一致性。增强的文本渲染能力，尤其是对中文、日文、韩文等非拉丁文字的支持，解决了长期存在的痛点，并提升了全球用户的可访问性。 该模型每次提示最多可输出 8 张一致的图像，并支持最高 2K 分辨率，但根据第三方评估，它在处理长文本和复杂非拉丁文字时仍可能吃力。它可通过 ChatGPT 和 API 使用，并已集成到 Viggle AI、Microsoft Copilot 等第三方平台。

telegram · zaihuapd · Nov 4, 23:42

**背景**: GPT Image 是 OpenAI 继 DALL-E 之后推出的图像生成模型系列，作为 ChatGPT Images 原生集成于 ChatGPT 中。2025 年 3 月发布的首个版本曾因其吉卜力工作室风格的图像而走红。ChatGPT Images 2.0 是一次重大更新，增加了视觉推理和多语言文本渲染能力，基于 GPT 系列的深度学习方法从自然语言描述生成图像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT_Image">GPT Image</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-0/">Introducing ChatGPT Images 2 . 0 | OpenAI</a></li>
<li><a href="https://imagvio.ai/gpt-image-2">GPT Image 2 AI — Fuse 16 Images , Render Any Text | Imagvio AI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#image-generation`, `#multimodal-AI`, `#text-rendering`, `#product-release`

---