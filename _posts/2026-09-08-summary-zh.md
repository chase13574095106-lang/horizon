---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> From 32 items, 7 important content pieces were selected

---

1. [数学家声称在纳维-斯托克斯问题上取得进展，并指控 OpenAI 窃取数据](#item-1) ⭐️ 9.0/10
2. [Kimi K3 2.8T 通过 SSD 流式传输在 MacBook Pro 上以每秒 1 token 运行](#item-2) ⭐️ 8.0/10
3. [OpenAI 发布 ChatGPT Images 2.5 及新 API 模型](#item-3) ⭐️ 8.0/10
4. [美国商务部调查中国 AI 企业海外获取英伟达芯片渠道](#item-4) ⭐️ 8.0/10
5. [字节跳动计划训练 5 万亿参数大模型，反对蒸馏路线](#item-5) ⭐️ 8.0/10
6. [ASML 与台积电推进 High NA EUV 向 12 英寸光掩模升级](#item-6) ⭐️ 8.0/10
7. [中国计划到 2030 年智能算力达 9800 EFLOPS](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [数学家声称在纳维-斯托克斯问题上取得进展，并指控 OpenAI 窃取数据](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 9.0/10

纽约大学库朗研究所的数学家 Tristan Buckmaster 宣布在纳维-斯托克斯相关问题取得进展，包括声称不可压缩多孔介质、Boussinesq 方程和三维不可压缩欧拉方程的有限时间爆破。他还指控 OpenAI 未经许可使用他的工作，并试图施压他配合其公司利益。 这一进展意义重大，因为它涉及数学中一个重要的未解决问题（纳维-斯托克斯存在性与光滑性问题，千禧年大奖问题），并引发了对 AI 公司未经同意使用研究人员数据的严重伦理质疑。这场争议可能影响学术界与 OpenAI 等 AI 公司的合作与信任。 Buckmaster 和 Levent Alpöge 声称在多个流体动力学方程的有限时间爆破问题上取得进展，但他们并未证明千禧年大奖问题的确切形式。OpenAI 承认虽然可能性不大，但无法排除用户交互的去标识化数据帮助改进了他们的模型，这使得 Buckmaster 的工作是否被使用存在模糊性。

hackernews · procedurecall · Sep 8, 05:42 · [社区讨论](https://news.ycombinator.com/item?id=49605915)

**背景**: 纳维-斯托克斯方程描述了粘性流体的运动，是流体力学的基础。克莱数学研究所为三维解的存在性和光滑性的证明提供了 100 万美元的奖金，但至今未解。Buckmaster 是一位备受尊敬的数学家，此前曾因在这些方程上的相关工作获得克莱研究奖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_equations">Navier-Stokes equations - Wikipedia</a></li>
<li><a href="https://cims.nyu.edu/~tristanb/">Tristan Buckmaster</a></li>
<li><a href="https://officechai.com/ai/mathematician-tristan-buckmaster-says-he-cracked-a-fluid-dynamics-problem-with-ai-accuses-openai-of-trying-to-take-credit/">Mathematician Tristan Buckmaster Says He Cracked a Fluid ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 OpenAI 被指控的行为表达了强烈的愤怒和担忧，有人称这是企业越界和不道德的数据使用。也有人指出 OpenAI 声明中的模糊性，质疑 Buckmaster 是否选择了退出数据使用，而另一些人则认为这是 AI 工具加剧学术竞争的例证。

**标签**: `#mathematics`, `#Navier-Stokes`, `#OpenAI`, `#research ethics`, `#AI`

---

<a id="item-2"></a>
## [Kimi K3 2.8T 通过 SSD 流式传输在 MacBook Pro 上以每秒 1 token 运行](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10

一个名为 DeltaFin 的项目声称通过从四个 SSD 流式传输权重，在 MacBook Pro 上以每秒 1 token 的速度运行 2.8 万亿参数的 Kimi K3 模型。这种方法避免了将整个模型加载到内存中，从而在消费级硬件上实现了超大规模模型的本地推理。 这展示了一种新颖的技术，可能允许个人运行远超其内存容量的模型，从而可能使前沿规模的人工智能更加普及。然而，极低的速度（每秒 1 token）凸显了实际限制，使其更像是一个概念验证而非可用的解决方案。 该项目从四个 SSD 流式传输模型权重，可能使用了类似于逐层加载或 SSD 缓存的技术。据报道，速度为每秒 1 token，这意味着生成一个单词可能需要几秒钟，而一个典型的回复可能需要几分钟甚至几小时。

hackernews · Argonautlabs · Sep 8, 20:07 · [社区讨论](https://news.ycombinator.com/item?id=49616257)

**背景**: 大型语言模型（LLM）通常需要海量内存，远超消费级硬件所能提供的。SSD 流式传输是一种新兴技术，它按需将模型的必要部分加载到内存中，以速度换取运行原本不可能运行的模型的能力。Apple 的统一内存架构和高速 SSD 使 MacBook 成为此类实验的热门平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/quantumnic/ssd-llm">GitHub - quantumnic/ssd-llm: Run 70B+ LLMs on Apple Silicon by using SSD as extended memory — intelligent layer streaming and caching for Mac</a></li>
<li><a href="https://tinycomputers.io/posts/partial-llm-loading-running-models-too-big-for-vram.html">Partial LLM Loading: Running Models Too Big for VRAM | TinyComputers.io</a></li>
<li><a href="https://www.mindstudio.ai/blog/ssd-streaming-ai-models-ram-dial">SSD Streaming for AI Models: How to Turn RAM from a Wall into a Dial | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一，一些人对可行性和实用性表示怀疑，指出一个中等长度的提示需要 11 天才能完成。其他人则认为这是一个有前途的开始，而一位用户询问 SSD 如何连接的澄清。

**标签**: `#LLM`, `#SSD`, `#MacBook`, `#Inference`, `#Open Source`

---

<a id="item-3"></a>
## [OpenAI 发布 ChatGPT Images 2.5 及新 API 模型](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 8.0/10

OpenAI 发布了 ChatGPT Images 2.5，这是升级后的图像生成模型，改进了多轮对话中的指令遵循能力，响应更快，并能更好地保留参考照片中的主体。API 现在新增了两个模型 ID：gpt-image-2.5-sunburst 和 gpt-image-2.5-flare。 此次发布意义重大，因为 OpenAI 的图像生成模型已被用于生成超过 30 亿张图像，而新的 API 模型为开发者提供了在精度（Sunburst）和速度（Flare）之间的选择，从而实现更定制化的工作流程。指令遵循和主体保留的改进将可能提升 AI 生成图像在各种应用中的质量和实用性。 根据 OpenAI 的文档，Sunburst 适用于编辑精度要求最高的工作流程，而 Flare 则适合快速、高质量的日常图像生成。Simon Willison 通过升级他的 openai_image.py CLI 工具以支持参考图像，成功地在现有图表中添加了一只浣熊科学家，从而演示了新模型。

rss · Simon Willison · Sep 8, 22:46

**背景**: OpenAI 一直在开发能够根据文本提示创建和编辑图像的图像生成模型。GPT Image 系列（包括 gpt-image-1）已在 API 中提供，新的 2.5 模型在此基础上构建。这些模型在 ChatGPT 中使用，并供开发者通过 API 调用，支持从创意设计到内容生成的各种应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst : New OpenAI Image APIs</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/image-generation">Image generation - OpenAI API</a></li>
<li><a href="https://openai.com/index/image-generation-api/">Introducing our latest image generation model in the API - OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#image generation`, `#API`, `#AI models`

---

<a id="item-4"></a>
## [美国商务部调查中国 AI 企业海外获取英伟达芯片渠道](https://t.me/zaihuapd/43676) ⭐️ 8.0/10

美国商务部工业与安全局（BIS）已启动一项系统性调查，针对中国 AI 企业如何在海外获取和使用英伟达芯片，包括通过远程访问他国计算资源的方式。此前，一名白宫官员指控月之暗面（Moonshot AI）非法获取英伟达芯片并经泰国远程访问。 此次调查可能收紧美国对 AI 芯片的出口管制，限制中国 AI 企业获取先进计算能力，并影响全球 AI 供应链。这凸显了中美科技紧张局势的升级，并可能导致对受控芯片云端远程访问的新规。 据报道，BIS 正在整理两份国家名单：一份是涉嫌将受限芯片走私入境中国的黑市所在地，另一份是中国企业远程租用芯片的国家。调查始于一名白宫官员公开指控月之暗面（其 Kimi K3 模型于 2026 年 7 月发布，性能接近美国水平）非法获取芯片并经泰国远程访问的几天后。

telegram · zaihuapd · Sep 8, 03:35

**背景**: 美国对向中国出口先进英伟达芯片实施了出口管制，以限制其 AI 发展。然而，中国企业寻求变通方式，包括通过第三国云服务访问芯片。BIS 是美国负责执行出口管制的机构，其调查可能检验远程访问受控芯片是否属于其管辖范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.dw.com/zh/中国ai公司月之暗面发布全球最大规模开源模型/a-78011216">中国AI公司月之暗面发布全球最大规模开源模型</a></li>

</ul>
</details>

**标签**: `#US-China tech war`, `#AI chips`, `#export controls`, `#Nvidia`, `#geopolitics`

---

<a id="item-5"></a>
## [字节跳动计划训练 5 万亿参数大模型，反对蒸馏路线](https://t.me/zaihuapd/43677) ⭐️ 8.0/10

据报道，字节跳动正讨论训练一个参数规模超过 5 万亿的大语言模型，由 Seed Foundation 负责人项亮主导，并与预训练数据负责人沈科合作。若落地，将超越阿里 Qwen 3.8-Max 和月之暗面 K3，成为国内已知参数规模最大的模型。 这标志着中国 AI 领域的重大战略转变，字节跳动旨在追求前沿规模模型而非渐进式改进。CEO 张一鸣反对蒸馏路线可能重塑行业实践，并加剧全球 AI 能力的竞争。 该计划仍处于早期阶段。两周前的 Seed 全员会上，张一鸣明确反对蒸馏路线，认为其只是复制 Claude 已有能力、难以实现超越，鼓励团队追求智能上限并接受短期落后。他还认可编程是当下关键方向，并已整合相关工作。

telegram · zaihuapd · Sep 8, 04:05

**背景**: 字节跳动 Seed 团队成立于 2023 年，致力于追求通用智能的上限，研究领域涵盖大语言模型、语音、视觉、世界模型和 AI 基础设施等。模型蒸馏是一种将大型'教师'模型的知识迁移到小型'学生'模型的技术，常用于降低计算成本。阿里 Qwen 3.8-Max 总参数达 2.4 万亿，是目前中国最大的模型之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/zh/">字节跳动Seed</a></li>
<li><a href="https://baike.baidu.com/item/Seed/65823503">Seed（字节跳动旗下团队名称）_百度百科</a></li>
<li><a href="https://ai-bio.cn/qwen-3-8-max/">Qwen 3 . 8 - Max – 阿里云千问团队推出的旗舰大 模 型 | AI工具箱</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#large language models`, `#AI training`, `#China AI`, `#model scale`

---

<a id="item-6"></a>
## [ASML 与台积电推进 High NA EUV 向 12 英寸光掩模升级](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 8.0/10

ASML 与台积电于 9 月 7 日宣布合作，将 High NA EUV 光刻从 6 英寸光掩模过渡到 12 英寸规格，目标是在 2031 年前建立试产线，并在 2033 年前将相关系统用于先进制程量产。 这一举措意义重大，因为 12 英寸光掩模可以提高晶圆厂生产率、降低芯片制造成本并消除拼接限制，这在芯片制造商向更小、更复杂的工艺节点迈进时至关重要。ASML 与台积电以及三星和英特尔的合作可能加速 High NA EUV 在整个行业的采用。 12 英寸光掩模试产线计划于 2031 年建立，High NA EUV 系统预计在 2033 年前进入先进制程量产。台积电计划从 2030 年起将 High NA EUV 用于先进节点的大规模制造，而初期生产将继续使用现有的 6 英寸掩模。

telegram · zaihuapd · Sep 8, 06:55

**背景**: High NA EUV 光刻是一种先进的芯片制造技术，利用更高数值孔径的极紫外光在芯片上制造更小的特征。目前，EUV 中使用的光掩模为 6 英寸，但转向 12 英寸掩模可以实现更大的图案，减少拼接需求并提高生产率。ASML 是 EUV 光刻系统的主要供应商，而台积电是使用这些系统进行先进制程制造的主要芯片制造商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/innovation/asml-tsmc-high-na-euv-12-inch-photomask-pilot-line">High - NA EUV photomask push targets 12 - inch mask pilot line</a></li>
<li><a href="https://www.trendforce.com/news/2026/09/08/news-asml-expands-high-na-euv-push-with-tsmc-samsung-and-intel-12-inch-photomask-pilot-line-set-for-2031/">[News] ASML Expands High - NA EUV Push with TSMC , Samsung and...</a></li>
<li><a href="https://aninews.in/news/business/asml-tsmc-join-hands-for-12-inch-photomasks-target-pilot-line-by-2031-for-next-gen-chipmaking20260908181527/">ASML , TSMC join hands for 12 - inch photomasks , target pilot line by...</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#EUV lithography`, `#ASML`, `#TSMC`, `#chip manufacturing`

---

<a id="item-7"></a>
## [中国计划到 2030 年智能算力达 9800 EFLOPS](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 8.0/10

中国工信部发布五年产业规划，目标是到 2030 年将智能算力提升至 9800 EFLOPS，并在 2026 年至 2030 年累计投入 3.8 万亿元用于信息基础设施建设。规划还提出有序部署万卡级及以上的智能计算集群。 该政策标志着中国在 AI 基础设施领域的重大国家推动，可能重塑全球 AI 竞争格局，并影响 AI 芯片和计算硬件的供应链。它凸显了在出口管制背景下，国产算力和芯片自主化的重要性。 截至 6 月底，中国智能算力达到 2185 EFLOPS，同比增长 177%，这意味着 2030 年目标需要在此基础上增长 4 倍以上。规划强调基础设施与国产算力芯片的适配，体现了对自主可控的战略重视。

telegram · zaihuapd · Sep 8, 11:23

**背景**: EFLOPS（每秒百亿亿次浮点运算）是衡量超级计算机和 AI 训练系统性能的单位，等于每秒 10^18 次浮点运算。'万卡集群'是指整合超过一万张加速卡的高性能计算系统，通常用于训练千亿至万亿参数的大模型。中国推动国产 AI 芯片的研发和应用，主要是受美国出口管制影响，以及出于技术自主可控的需要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Floating_point_operations_per_second">Floating point operations per second - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/item/万卡集群/65379543">万卡集群 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/687404811">AI算力芯片：国产算力行业产业链深度梳理 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#China tech policy`, `#computing power`, `#EFLOPS`, `#national strategy`

---