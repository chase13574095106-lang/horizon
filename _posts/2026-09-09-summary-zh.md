---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> From 36 items, 9 important content pieces were selected

---

1. [OpenAI 声称解决纳维-斯托克斯问题，引发优先权争议](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-6 Astra，评测登顶并实现数学突破](#item-2) ⭐️ 9.0/10
3. [vLLM v0.29.0：Model Runner V2 成为默认，新增模型并提升性能](#item-3) ⭐️ 8.0/10
4. [苹果发布可折叠 iPhone Duo](#item-4) ⭐️ 8.0/10
5. [Shopify 收购 Tailwind CSS 框架](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 或模仿 GPT-5.5 Pro 推理轨迹](#item-6) ⭐️ 8.0/10
7. [研究人员详述谷歌广告恶意软件滥用，引发热议](#item-7) ⭐️ 8.0/10
8. [陶哲轩警告 AI 可能耗尽开放数学问题](#item-8) ⭐️ 8.0/10
9. [DeepSeek V4.1 Flash 内测：原生多模态，更快更便宜](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 声称解决纳维-斯托克斯问题，引发优先权争议](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

2026 年 9 月 8 日，OpenAI 宣布其未发布的内部模型，利用约 10,000 个 AI 智能体集群，解决了千禧年大奖难题之一的纳维-斯托克斯存在性与光滑性问题。该结果已用 Lean 形式化，但尚未经过外部数学家验证。 如果得到验证，这将是数学和人工智能领域的范式转变，展示了 AI 解决最困难开放问题的能力。同时，它也引发了对研究伦理、优先权争议以及 AI 公司之间竞争动态的严重关切。 OpenAI 表示，在所有尝试的问题中，智能体发送了 490 万条消息，使用了约 3000 亿个输出 token，其中仅纳维-斯托克斯问题就占 270 万条消息和 1300 亿个 token。该方法基于 Diego Córdoba 和 Luis Martínez-Zoroa 在 2023 年提出的流体方程爆破现象方法。OpenAI 表示，如果被授予 100 万美元的克莱千禧年奖，它将拒绝接受。

rss · Simon Willison · Sep 8, 23:55

**背景**: 纳维-斯托克斯存在性与光滑性问题询问描述流体运动的纳维-斯托克斯方程的解在三维空间中是否始终保持光滑。它是克莱数学研究所于 2000 年设立的七个千禧年大奖难题之一，每个问题奖金 100 万美元。截至 2026 年，只有庞加莱猜想被正式解决。该公告伴随着与 Tristan Buckmaster 和 Levent Alpöge 的优先权争议，他们声称更早得出了密切相关的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**社区讨论**: 新闻条目中未提供社区讨论，但基于争议，情绪可能分化：有人担心 OpenAI 涉嫌使用泄露信息以及 AI 驱动研究的伦理问题。一些人可能质疑未经验证结果的有效性，而另一些人可能将其视为 AI 的里程碑。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#Navier-Stokes`, `#Millennium Prize`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-6 Astra，评测登顶并实现数学突破](https://t.me/zaihuapd/43707) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Astra，称其为迄今最智能、最对齐的模型。它在多个基准测试中取得顶尖成绩，包括 FrontierMath Tier 4 的 98%、ARC-AGI-3 的 99.9%和 ExploitBench 的 100%，并将素数间隔的上界推进到 186。 此次发布标志着 AI 能力的一次重大飞跃，尤其是在数学推理和智能体任务方面，可能加速网络安全和科学发现等领域的研究与应用。高分基准成绩表明 GPT-6 Astra 可能树立新的 AI 性能标准，影响 AI 开发者之间的竞争格局。 GPT-6 Astra 在 OpenAI 标准 API 下的定价为每百万输入 token 10 美元，每百万输出 token 50 美元，缓存读取和写入另行收费。API 为 GPT-6 Astra 提供快速模式，处理速度最高可达标准模式的 2.5 倍。OpenAI 还披露，模型的思维链（CoT）可监测性显著下降，因为模型能控制自身推理过程，并在更少甚至无需语言化推理的情况下完成复杂任务。

telegram · zaihuapd · Sep 9, 07:10

**背景**: FrontierMath 是一个由专家数学家设计的高难度数学问题基准，其中 Tier 4 难度最高，接近研究级问题。ARC-AGI-3 是一个交互式推理基准，测试 AI 智能体探索新环境和推断目标的能力；ExploitBench 则衡量 AI 在真实世界漏洞利用任务中的能力，从定位漏洞代码到任意代码执行。这些基准旨在推动 AI 超越简单的模式识别，进入更复杂的智能体推理领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epoch.ai/benchmarks/frontiermath-tier-4-v2">FrontierMath Tier 4 (v2) | Epoch AI</a></li>
<li><a href="https://arcprize.org/blog/astra">OpenAI's GPT-6 Astra on ARC-AGI-3 | ARC Prize</a></li>
<li><a href="https://exploitbench.ai/">ExploitBench</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些用户对 GPT-6 Astra 的能力表示惊叹，如 MSPAINT 计算机使用演示；另一些用户则报告性能不一致，称 Astra 在最近一次更新前“令人惊叹”，之后感觉像 Sol。还有关于 Transformer 模型中隐藏推理影响的讨论，以及对思维链可监测性下降的担忧，部分用户分享了关于计算极限和 CoT 需求的相关研究链接。

**标签**: `#OpenAI`, `#GPT-6`, `#AI model release`, `#benchmarks`, `#mathematics`

---

<a id="item-3"></a>
## [vLLM v0.29.0：Model Runner V2 成为默认，新增模型并提升性能](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 是一个重要版本，包含来自 277 位贡献者的 594 次提交，将 Model Runner V2 设为所有模型的默认运行器，并新增了对 Hy4-preview、Qwen3.8-Flash-Next 和 Kimi K3 等模型的支持。该版本还为 Kimi-K3 和 DeepSeek V4 引入了显著的性能优化，并新增了推测解码和 RL 权重同步等功能。 该版本通过采用更高效的默认执行路径并支持最新的先进模型，巩固了 vLLM 作为领先的开源 LLM 推理引擎的地位。针对 DeepSeek V4 和 Kimi K3 等模型的性能优化将直接惠及在生产环境中部署这些模型的开发者，降低延迟和成本。 Model Runner V2 (MRV2) 现已成为所有模型的默认运行器，完成了从 pooling 模型开始的推广，并引入了用于 KV cache 自动调整大小的 CUDA graph 内存分析和 batch-sharded 采样。破坏性变更包括移除了十个已弃用的模型架构，并将 `python -m vllm.entrypoints.openai.api_server` 弃用，推荐使用 `vllm serve`。

github · khluu · Sep 9, 08:54

**背景**: vLLM 是一个用于大型语言模型（LLM）的高吞吐量、内存高效的推理和服务引擎。Model Runner V2 是一个内部执行框架，与之前的版本相比，它提高了性能和灵活性。该版本还支持多 Token 预测（MTP）和 DeepSeek 稀疏注意力（DSA）等高级功能，这些技术旨在加速推理并高效处理长上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://arxiv.org/abs/2512.02556">DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#AI/ML`, `#open source`

---

<a id="item-4"></a>
## [苹果发布可折叠 iPhone Duo](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果发布了可折叠 iPhone Duo，标志着该公司进入可折叠智能手机市场。这一公告引发了大量社区讨论，在新闻平台上获得了 794 个点赞和 1555 条评论。 这是苹果首款可折叠 iPhone，是一次重大的产品发布，可能重塑消费者对可折叠设备的期望。社区对设计和演示的批判性分析表明存在浓厚的兴趣和辩论，可能影响苹果未来的产品决策。 iPhone Duo 被描述为即使在展开前也比之前的 iPhone 更宽，社区成员根据上手视频指出其没有折痕。由 John Ternus 主导的演示风格被批评为排练过度、情感平淡。

hackernews · thecosmicfrog · Sep 9, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 可折叠智能手机使用柔性显示屏，使设备能够折叠，从而在紧凑的形态中提供更大的屏幕。苹果进入这一市场是在三星等竞争对手推出可折叠设备多年之后。iPhone Duo 的设计旨在提供类似平板电脑的体验，同时可折叠以便放入口袋。

**社区讨论**: 社区评论反应不一：一些人称赞 Duo 的设计和没有折痕，而另一些人则批评演示风格和手机越来越大的趋势。一位评论者提到 ISO 216 纸张标准作为设计灵感，另一位则表达了对更小手机的渴望，凸显了消费者偏好的分歧。

**标签**: `#Apple`, `#iPhone`, `#foldable`, `#consumer tech`, `#product launch`

---

<a id="item-5"></a>
## [Shopify 收购 Tailwind CSS 框架](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购流行的开源 CSS 框架 Tailwind，这一消息在 Tailwind 博客上公布。此次收购发生在模板销售因 AI 影响而大幅下滑的背景下。 此次收购凸显了 AI 对传统 Web 开发业务模式日益增长的影响，即使是主要的开源工具也面临收入挑战。这也表明 Shopify 有意加强其开发者生态系统和设计工具。 Tailwind CSS 背后的公司 Tailwind Labs 此前曾报告，由于 AI 对模板销售的影响，文档流量下降了 40%，工程人员减少了 75%。此次收购包括 Tailwind 品牌及其团队，目前没有发布新模板的计划。

hackernews · EdwinHoksberg · Sep 9, 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个实用优先的 CSS 框架，允许开发者直接在 HTML 中设置网站样式，这与 Bootstrap 等传统框架不同。Shopify 是一个领先的电子商务平台，已进行多次收购以扩展其服务，此举可能旨在将 Tailwind 的设计能力整合到其生态系统中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shopify">Shopify - Wikipedia</a></li>
<li><a href="https://tracxn.com/d/acquisitions/acquisitions-by-shopify/__NNWgXlWtRBr7FVe-BI1BiwMHs246IPF8HlqlcE5kZno">List of 19 Acquisitions by Shopify (Aug 2026) - Tracxn</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有悲伤也有理解，用户指出 AI 对模板销售的影响是不可避免的。一些人质疑在新项目中使用 Tailwind 的必要性，因为现代 CSS 功能已很强大，而另一些人则对团队表示祝福，并认可 Tailwind 的教育价值。

**标签**: `#acquisition`, `#Tailwind`, `#Shopify`, `#CSS`, `#AI impact`

---

<a id="item-6"></a>
## [Qwen 3.8 或模仿 GPT-5.5 Pro 推理轨迹](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

一份 gist 声称 Qwen 3.8 的推理预填充与 GPT-5.5 Pro 高度相似，暗示可能存在对专有模型的蒸馏。该分析利用一种技术恢复 OpenAI 模型的隐藏思维链，并比较了推理的初始步骤。 这一发现引发了关于 AI 行业训练实践的重大问题，特别是使用专有模型输出训练开源模型的做法。它可能影响围绕模型开发和蒸馏方法的信任与监管审查。 该技术包括使用最先进的模型运行基准测试，恢复其思维链，然后将推理的前 1% 作为开源模型的前缀。Qwen 3.8 0902 在相关论文于 8 月 10 日发布后训练，因此它可能已经见过那些特定的思维。

hackernews · wsxiaoys · Sep 9, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49630026)

**背景**: 推理预填充是指模型在生成最终答案之前产生的初始思维链令牌。蒸馏是一种技术，其中较小的模型被训练来模仿较大的教师模型的输出。讨论中提到的“窃取思维”方法是一种已知的利用手段，用于恢复像 OpenAI 这样的模型隐藏的推理过程，这些模型通常不会暴露其完整的思维链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49630026">Qwen 3.8 follows GPT-5.5 Pro reasoning prefills | Hacker News</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/qwen-3-8-9b-distilled-qwen-3-8-is-here-6dcbca16a319">Qwen 3.8–9B: Distilled Qwen 3.8 is here !! | by Mehul Gupta | Data Science in Your Pocket | Aug, 2026 | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/qwen3-8-9b-distillation-local">Qwen3.8-9B: Running the Community-Distilled Model Locally | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区评论对蒸馏主张的有效性进行了辩论，一些人指出两个模型可能都在相同的基准解决方案上训练。其他人则质疑原始推理令牌的可用性，以及重叠是否足以证明蒸馏。

**标签**: `#AI`, `#LLM`, `#distillation`, `#Qwen`, `#GPT`

---

<a id="item-7"></a>
## [研究人员详述谷歌广告恶意软件滥用，引发热议](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

一名安全研究人员发布了一篇详细文章，讲述他们如何成功通过谷歌广告宣传恶意软件，揭露了该平台广告审核流程中的严重漏洞。这篇题为《我如何在谷歌广告上宣传恶意软件》的文章在 Hacker News 上迅速获得关注，获得 342 分和 207 条评论。 这一揭露凸显了恶意广告（malvertising）的持续威胁，网络犯罪分子利用受信任的广告平台分发恶意软件，可能影响数百万用户。它强调了在线广告中加强人工审核和更强大的自动检测系统的必要性，因为当前措施显然不足。 研究人员的账户最初被拒绝，但在 Hacker News 上引起关注后又被恢复，这表明谷歌的自动化系统可能只有在公众关注后才标记了该内容。社区评论揭示了人们对谷歌依赖自动化系统以及缺乏人工联系点来解决此类问题的普遍不满。

hackernews · xlii · Sep 9, 11:43 · [社区讨论](https://news.ycombinator.com/item?id=49624856)

**背景**: 恶意广告（malvertising）是一种日益增长的网络安全威胁，攻击者在谷歌广告等合法平台上投放恶意广告，诱骗用户下载恶意软件或访问钓鱼网站。谷歌有明确禁止恶意软件分发的政策，但执行往往依赖可被绕过的自动化系统。Zscaler 和微软等机构的最新研究记录了导致信息窃取器和勒索软件的恶意广告活动，凸显了问题的严重性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/adspolicy/answer/15939580?hl=en">Malicious Software - Advertising Policies Help - Google Help</a></li>
<li><a href="https://www.csoonline.com/article/4186813/attackers-abuse-google-ads-gitlab-and-claude-to-deliver-malware.html">Attackers abuse Google Ads, GitLab, and Claude to deliver malware</a></li>
<li><a href="https://www.zscaler.com/blogs/security-research/malvertising-campaign-leading-zemot">Malvertising Campaign Leading To Zemot | Zscaler</a></li>

</ul>
</details>

**社区讨论**: 社区评论强烈批评谷歌的自动化审核，用户分享了被忽视或不公平对待的个人经历。有人指出谷歌并非唯一，许多公司躲在自动化系统后面，并建议监管要求提供人工联系点。研究人员关于账户恢复的更新引发了复杂情绪，既承认公众压力的作用，也感叹需要如此放大才能解决问题。

**标签**: `#security`, `#google ads`, `#malware`, `#online advertising`, `#cybersecurity`

---

<a id="item-8"></a>
## [陶哲轩警告 AI 可能耗尽开放数学问题](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 8.0/10

著名数学家陶哲轩公开警告，AI 驱动的研究努力可能迅速耗尽数学中富有成效的开放问题库，从而可能阻碍研究人员分享有前景的研究方向。他在 Mathstodon 上发表的评论强调，激励机制的转变可能破坏数百年来的开放科学传统。 这一警告意义重大，因为它指出了 AI 在研究中的一个潜在意外后果：侵蚀了数学进步所依赖的协作性开放科学实践。如果研究人员为避免 AI 驱动的竞争而囤积问题，可能会减缓创新并损害该领域的长期健康，影响数学家、AI 开发者以及更广泛的科学界。 陶哲轩特别指出，即使有人正在研究某个问题的传闻，也可能引发大规模的 AI 驱动努力，在原始研究者充分发展其工作之前就解决该问题。这导致对开放问题的“不可再生”开采，使得有前景的方向变得稀缺，分享它们的激励也随之减少。

rss · Simon Willison · Sep 9, 00:20

**背景**: 开放科学是一场促进研究透明度和协作的运动，允许科学家公开分享发现、数据和想法。在数学领域，分享开放问题一直是促进集体进步的传统。近期 AI 的进展，例如解决纳维-斯托克斯问题，展示了 AI 应对复杂数学挑战的能力，但也引发了对公平性和研究速度的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/">AI Has Solved One of Math ’s $1 Million Millennium Prize Problems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_science">Open science - Wikipedia</a></li>
<li><a href="https://theoutpost.ai/news-story/ai-achieves-major-breakthrough-on-1-million-navier-stokes-problem-transforming-mathematics-forever-30584/">OpenAI Solves Navier-Stokes Millennium Problem Amid Scandal</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#open science`, `#mathematics`, `#research incentives`

---

<a id="item-9"></a>
## [DeepSeek V4.1 Flash 内测：原生多模态，更快更便宜](https://t.me/zaihuapd/43708) ⭐️ 8.0/10

DeepSeek 已开始对 V4.1 Flash 进行限时内测，这是一个中间版本模型，引入了原生多模态支持、更强的能力、更快的生成速度和更低的成本。该模型通过相同的 base_url 访问，模型名为 'deepseek-v4.1-flash-expires-on-0910'，计费与 deepseek-v4-flash 相同。 此次发布意义重大，标志着 DeepSeek 以新架构进军原生多模态 AI，可能提升其在全球 AI 竞赛中的竞争力。更快的速度和更低的成本相结合，可能使先进的多模态能力更容易被开发者和企业获取。 该模型采用新的模型结构，是对先前版本的完全重新训练，而非微调。内测期间，每个账号限流 20 并发，模型名中包含到期日期 0910，表明其临时可用性。

telegram · zaihuapd · Sep 9, 07:18

**背景**: DeepSeek 是一家以开源权重大型语言模型闻名的中国 AI 实验室。V4.1 Flash 是 V4 系列中的中间版本更新，该系列包括 V4-Pro（1.6T 参数）和 V4-Flash（284B 参数），均采用混合专家（MoE）架构。原生多模态支持意味着模型可以直接处理和理解多种类型的数据（如文本和图像），而无需单独的组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/09/09/deepseek-v4-1-flash-multimodal-limited-beta/">DeepSeek begins limited-time beta of V4.1 Flash multimodal model · TechNode</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-1-flash-leak">DeepSeek V 4 . 1 Flash Beta: Flash Prices Just Got Cheaper</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 Explained: V 4 -Pro 1.6T vs V 4 - Flash 284B (2026)</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI model`, `#multimodal`, `#LLM`, `#release`

---