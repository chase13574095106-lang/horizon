---
layout: default
title: "Horizon Summary: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
---

> From 25 items, 7 important content pieces were selected

---

1. [Stripe 与 Advent 联合出价逾 530 亿美元收购 PayPal](#item-1) ⭐️ 9.0/10
2. [Thinking Machines 发布 Inkling，最大开源权重多模态模型](#item-2) ⭐️ 8.0/10
3. [Gemma 4 26B 在 13 年前的 CPU 上以 5 tokens/秒运行](#item-3) ⭐️ 8.0/10
4. [Claude web_fetch 工具绕过导致数据泄露](#item-4) ⭐️ 8.0/10
5. [DeepSeek 首轮融资超 500 亿元，特殊架构保创始人控制权](#item-5) ⭐️ 8.0/10
6. [沙盒逃逸让 Filza 读取 iOS 27 备忘录数据库](#item-6) ⭐️ 8.0/10
7. [Telegram 推出机器人无服务器平台](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe 与 Advent 联合出价逾 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据消息人士透露，Stripe 与私募股权公司 Advent International 联合出价超过 530 亿美元收购 PayPal。这笔交易将合并两家最大的在线支付处理商。 如果交易完成，将缔造一个控制 Stripe、PayPal、Venmo、Braintree 和 Xoom 的支付巨头，引发重大反垄断担忧。这可能重塑在线支付格局，影响数百万商家和消费者。 据报道，该出价超过 530 亿美元，一些分析师认为这是低价收购。PayPal 拥有 Venmo 和 Braintree，而 Stripe 将获得 PayPal 的银行牌照，可能开启新的金融服务。

hackernews · rvz · Jul 15, 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是企业在线支付处理领域的领导者，而 PayPal 是广泛使用的消费者支付平台，旗下拥有 Venmo 等子公司。Advent International 是一家全球私募股权公司，管理资产约 1000 亿美元。由于在线支付市场集中度问题，该交易将面临严格的反垄断审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe , Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/07/15/business/paypal-stripe-advent-takeover-bid.html">PayPal Receives $53 Billion Takeover Offer Involving Stripe</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对竞争减少和费用上升的担忧，指出 Stripe 限制某些商家（如大麻、成人内容），而 PayPal 允许。一些人担心整合风险和支付多样性丧失，另一些人则认为 Stripe 获得 PayPal 银行牌照具有战略价值。

**标签**: `#acquisition`, `#payments`, `#antitrust`, `#fintech`, `#Stripe`

---

<a id="item-2"></a>
## [Thinking Machines 发布 Inkling，最大开源权重多模态模型](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines 发布了 Inkling，这是目前最大的支持音频的开源权重多模态模型，针对微调和本地部署进行了优化。 Inkling 填补了开源 AI 的空白，提供了一个具有音频能力的强大多模态模型，为封闭模型提供了替代方案，并使企业能够定制和拥有自己的 AI。 Inkling 并非整体最强的模型，但它结合了多模态能力、高效推理以及可在 Tinker 上进行微调的特点，使其成为定制的良好开源权重基础。

hackernews · vimarsh6739 · Jul 15, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48924912)

**背景**: 开源权重模型是指其训练参数公开发布的 AI 模型，任何人都可以下载和微调。多模态模型整合了文本、音频和图像等多种数据类型，从而实现更丰富的理解。Inkling 是最大的支持音频的开源权重模型，这一特性在开源领域较为罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-ai">What is Multimodal AI? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区对 Inkling 的音频能力和本地部署感到兴奋，用户分享了本地运行的资源。一些人将其视为中国开源模型（如 DeepSeek）的潜在美国替代品，而另一些人则称赞其支持企业定制的商业模式。

**标签**: `#open-weights`, `#multimodal`, `#AI model`, `#audio`, `#fine-tuning`

---

<a id="item-3"></a>
## [Gemma 4 26B 在 13 年前的 CPU 上以 5 tokens/秒运行](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

一篇技术博客展示了如何在无 GPU 的 13 年前 Xeon 服务器上，通过量化实现 CPU-only 推理，以每秒 5 个 token 的速度运行 Google 的 Gemma 4 26B A4B 模型。 这表明现代大语言模型可以在老旧硬件上运行，使本地 AI 推理更易获取，减少对昂贵 GPU 的依赖，从而可能推动 AI 使用的普及。 Gemma 4 26B A4B 模型采用混合专家架构，总参数量 26B，激活参数量 4B，并支持推测解码以加速推理。5 tokens/秒的速度是在双路 Xeon E5-2697 v2 系统（256GB DDR3 内存）上实现的。

hackernews · neomindryan · Jul 15, 15:34 · [社区讨论](https://news.ycombinator.com/item?id=48922434)

**背景**: 大语言模型通常需要强大 GPU 进行推理，但量化技术（如 GGUF）可减小模型体积，实现纯 CPU 运行。Gemma 4 是 Google 最新的开放模型系列，支持高达 256K 上下文和多语言。CPU 推理受内存带宽限制，因此老旧的多通道 DDR3 系统仍能获得不错性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者就成本效率展开讨论：有人指出在德国等高电价地区，使用推理提供商比本地运行更便宜。其他人分享了类似实验，在类似硬件上达到 8-12 tokens/秒。有预测认为到 2027 年中，超过 200B 参数的 MoE 模型将能在消费级硬件上运行。

**标签**: `#LLM`, `#inference`, `#hardware`, `#optimization`, `#local AI`

---

<a id="item-4"></a>
## [Claude web_fetch 工具绕过导致数据泄露](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究员 Ayush Paul 发现 Anthropic 的 Claude web_fetch 工具存在漏洞，通过诱骗模型从恶意蜜罐网站跟随嵌套 URL，实现了用户记忆数据的窃取。Anthropic 随后移除了 web_fetch 在已获取内容中导航链接的能力，从而封堵了该漏洞。 该攻击展示了绕过 Claude 数据泄露防护的实际方法，凸显了保护 LLM 代理免受提示注入和“致命三重奏”（私有数据、不可信内容、外部通信）攻击的持续挑战。它强调了在 AI 代理设计中需要强大的架构边界。 该攻击针对 Claude 的 web_fetch 工具，该工具通常只允许获取用户明确提供或来自 web_search 结果的 URL。漏洞允许获取先前获取页面中嵌入的 URL，从而形成请求链，窃取了用户的姓名、所在城市和雇主信息。

rss · Simon Willison · Jul 15, 14:21

**背景**: 像 Claude 这样的 LLM 代理面临“致命三重奏”风险：它们能访问私有数据、可以对外通信，并且会接触不可信内容（例如来自网页）。提示注入攻击通过在处理的内容中嵌入恶意指令来利用这一点。Anthropic 设计了 web_fetch 的限制来防止动态 URL 构造，但嵌套链接绕过规避了这些防护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（文章中有链接）可能包括对该攻击巧妙之处的评论，以及对 Anthropic 因内部已发现而未支付漏洞赏金的失望。一些人可能会讨论修复措施的充分性以及对 AI 代理安全的更广泛影响。

**标签**: `#AI safety`, `#LLM security`, `#data exfiltration`, `#prompt injection`, `#Claude`

---

<a id="item-5"></a>
## [DeepSeek 首轮融资超 500 亿元，特殊架构保创始人控制权](https://t.me/zaihuapd/42589) ⭐️ 8.0/10

DeepSeek 完成首轮融资，筹得逾 500 亿元人民币（约 74 亿美元），估值超过 500 亿美元。本轮采用特殊有限合伙架构，投资者将资金注入由创始人梁文锋管理的实体，接受五年锁定期且不享有表决权。 这一巨额融资轮表明投资者对 DeepSeek 作为领先 AI 公司的强烈信心，而独特的治理结构使创始人在筹集大量资金的同时仍能保持控制权。这可能为 AI 初创公司如何平衡融资需求与创始人自主权树立先例。 创始人梁文锋在本轮中个人投资 200 亿元。腾讯考虑投资 100 亿元，宁德时代计划投资 50 亿元，可能成为最大的外部投资者。DeepSeek 对此暂未置评。

telegram · zaihuapd · Jul 15, 12:56

**背景**: DeepSeek 成立于 2023 年 7 月，由梁文锋创立，与幻方量化关联，是一家以大型语言模型闻名的中国 AI 公司。有限合伙架构允许创始人作为普通合伙人（GP）控制公司，而投资者作为有限合伙人（LP）提供资金但不享有表决权。这种结构在中国常用于在融资时保持创始人控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stcn.com/article/detail/3897512.html">DeepSeek，融资大消息！估值达450亿美元？</a></li>
<li><a href="https://www.dehenglaw.com/CN/tansuocontent/0008/032873/7.aspx?MID=0902&AID=">多维度解析DeepSeek股权架构设计 - 德恒探索 - 德恒律师事务所</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#startup`, `#governance`

---

<a id="item-6"></a>
## [沙盒逃逸让 Filza 读取 iOS 27 备忘录数据库](https://x.com/0xjohnny/status/2077216973256274272) ⭐️ 8.0/10

开发者 johnny 修改了 iOS 文件管理器 Filza，利用 iOS 27 beta 3 上的沙盒逃逸漏洞，使其能够在 iPhone 17 Pro Max 上访问备忘录数据库。 这展示了最新 iOS beta 上的实际沙盒逃逸，突显了一个严重的安全漏洞，恶意应用可能利用该漏洞访问敏感用户数据。 该漏洞绕过了应用的容器限制，使 Filza 能够浏览外部数据，包括备忘录数据库。修改后的 Filza 运行在目前处于开发阶段的 iOS 27 beta 3 上。

telegram · zaihuapd · Jul 15, 14:35

**背景**: iOS 应用被沙盒化，以防止它们访问自身容器之外的数据。沙盒逃逸漏洞允许应用突破这一限制。Filza 是一款流行的 iOS 文件管理器，通常需要越狱或特殊工具才能访问完整的文件系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=vB7EN21sxfw">Install Filza File Manager on iOS 18-26 (No Jailbreak) - YouTube</a></li>
<li><a href="https://www.tigisoftware.com/default/?page_id=78">Filza – TIGI Software</a></li>
<li><a href="https://forums.macrumors.com/threads/ios-27-beta-3-bug-fixes-changes-and-improvements.2485019/">iOS 27 Beta 3 ― Bug Fixes, Changes, and Improvements | MacRumors Forums</a></li>

</ul>
</details>

**标签**: `#iOS`, `#sandbox escape`, `#security`, `#vulnerability`, `#Filza`

---

<a id="item-7"></a>
## [Telegram 推出机器人无服务器平台](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram 正式推出无服务器平台，开发者只需一条命令 npx tgcloud push 即可将机器人和 Mini App 的后端代码直接部署在 Telegram 的基础设施上。 这消除了开发者管理服务器、容器或扩展的需求，大幅降低了运维开销，使机器人开发更快、更简单。 代码运行在紧邻 Bot API 的隔离 V8 沙箱中，并自带基于 SQLite 的内置数据库；仅支持 JavaScript 模块。

telegram · zaihuapd · Jul 15, 16:00

**背景**: 无服务器计算允许开发者无需配置或管理服务器即可运行代码，并根据需求自动扩展。Telegram 的平台将此概念扩展到机器人开发，提供了与 Bot API 紧密集成的环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://core.telegram.org/bots/serverless">Telegram Serverless</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#serverless`, `#bots`, `#JavaScript`, `#cloud`

---