---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> From 27 items, 13 important content pieces were selected

---

1. [Claude Fable 声称找到雅可比猜想反例](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x 无 gadget 高危 RCE 漏洞](#item-2) ⭐️ 9.0/10
3. [智谱建成全国产芯片 1 吉瓦数据中心](#item-3) ⭐️ 9.0/10
4. [中国开放权重 AI 策略取得进展](#item-4) ⭐️ 8.0/10
5. [黑客清空罗马尼亚土地登记数据库](#item-5) ⭐️ 8.0/10
6. [arXiv 上 AI 写作检测：到 2026 年 39%被标记](#item-6) ⭐️ 8.0/10
7. [Kimi K3、Qwen 3.8 与 Anthropic 的潜在危机](#item-7) ⭐️ 8.0/10
8. [本·汤普森提议美国立法将 AI 训练数据视为合理使用](#item-8) ⭐️ 8.0/10
9. [Sam Altman 2022 年邮件揭示开源策略](#item-9) ⭐️ 8.0/10
10. [Hugging Face 遭 AI 智能体入侵，商业大模型拒绝协助取证](#item-10) ⭐️ 8.0/10
11. [特朗普政府或限制美企使用中国开放权重 AI 模型](#item-11) ⭐️ 8.0/10
12. [美军应用被发现嵌入中俄代码](#item-12) ⭐️ 8.0/10
13. [欧盟拟共享生物识别数据以换取美国免签](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Fable 声称找到雅可比猜想反例](https://zh.wikipedia.org/zh-cn/%E9%9B%85%E5%8F%AF%E6%AF%94%E7%8C%9C%E6%83%B3) ⭐️ 9.0/10

2026 年 7 月 19 日，Anthropic 员工兼数学家 Levent Alpöge 在三维空间中给出了雅可比猜想的一个显式反例，该反例是在 Anthropic 的大语言模型 Claude Fable 5 的帮助下发现的。 如果得到验证，这将推翻一个在代数几何中悬而未决超过 80 年的难题，并展示了 AI 辅助数学研究的潜力。 该反例针对的是 N > 2 的情况；N = 2 时的雅可比猜想仍未解决。该发现是在 2026 年世界杯决赛期间做出的，并附有 WolframAlpha 验证链接。

telegram · zaihuapd · Jul 20, 05:34

**背景**: 雅可比猜想最初于 1884 年针对两个变量提出，1939 年推广到一般形式，它断言如果多项式映射的雅可比行列式是非零常数，则该映射具有多项式逆映射。该猜想以大量错误证明而闻名，并且是 Smale 21 世纪问题列表中的第 16 个问题。Claude Fable 5 是 Anthropic 于 2026 年 6 月发布的最先进的大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 数学界反应热烈且带有怀疑；许多研究者要求提供反例的构造细节和推理过程。由于缺乏同行评审，人们持谨慎乐观态度。

**标签**: `#mathematics`, `#Jacobian Conjecture`, `#AI-assisted research`, `#breakthrough`

---

<a id="item-2"></a>
## [Fastjson 1.x 无 gadget 高危 RCE 漏洞](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 9.0/10

安全研究员 Kirill Firsov 披露，Fastjson 1.2.68 至 1.2.83 版本存在高危远程代码执行漏洞，无需开启 autoType 或依赖 classpath gadget，影响 JDK 8、17 和 21。 该漏洞至关重要，因为 Fastjson 在 Java 应用中广泛使用，且无需 gadget 或 autoType 使得利用更加容易。由于 Fastjson 1.x 已于 2024 年 10 月停止维护，官方极大概率不会发布补丁，用户必须迁移到 Fastjson2 或启用 SafeMode。 该漏洞影响 Fastjson 1.2.68 至 1.2.83 版本，无需开启 autoType 或 classpath 上的任何 gadget 即可触发。唯一的缓解措施是升级到 Fastjson2，或通过 JVM 参数、代码或配置文件启用 SafeMode。

telegram · zaihuapd · Jul 20, 14:32

**背景**: Fastjson 是阿里巴巴开发的流行 Java JSON 序列化/反序列化库。其 autoType 功能允许通过 JSON 中的 @type 指定 Java 类名，这历来是反序列化漏洞的根源。SafeMode 完全禁用 autoType，从而防止此类攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en">fastjson _ safemode _en · alibaba/ fastjson Wiki · GitHub</a></li>
<li><a href="https://jfrog.com/blog/cve-2022-25845-analyzing-the-fastjson-auto-type-bypass-rce-vulnerability/">CVE-2022-25845 - Fastjson RCE vulnerability analysis</a></li>
<li><a href="https://www.huaweicloud.com/intl/en-us/notice/20200530105656853.html">Remote Code Execution Vulnerability in Fastjson 1.2.68 and Earlier...</a></li>

</ul>
</details>

**标签**: `#Fastjson`, `#RCE`, `#vulnerability`, `#security`, `#Java`

---

<a id="item-3"></a>
## [智谱建成全国产芯片 1 吉瓦数据中心](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 9.0/10

智谱 AI 完成了一座全部采用国产芯片、功率达 1 吉瓦的数据中心建设，并已开始部分运营，用于支持其 GLM AI 模型的训练。 这一里程碑表明中国有能力在不依赖外国芯片的情况下建设大规模 AI 基础设施，对地缘政治韧性及提升国内 AI 能力至关重要。 该 1 吉瓦设施可同时为约 75 万户家庭供电，是中国 AI 实验室建造的最大规模数据中心之一，拥有多个各含超万枚芯片的计算集群。

telegram · zaihuapd · Jul 20, 15:43

**背景**: 智谱 AI（国际品牌名 Z.ai）是中国领先的 AI 公司，也是开源 GLM 系列大语言模型的开发者。美国于 2025 年 1 月将智谱 AI 列入实体清单，限制其获取先进美国芯片，这加速了中国推动国产芯片替代的进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zhipu_AI">Zhipu AI</a></li>
<li><a href="https://techplustrends.com/1gw-data-center-power-consumption-guide/">“1GW Data Center Power Consumption: Why 2026 Infrastructure ...</a></li>
<li><a href="https://llm-stats.com/">AI Leaderboard 2026: Compare & Rank 300+ Top AI Models by...</a></li>

</ul>
</details>

**标签**: `#AI`, `#data center`, `#China`, `#chips`, `#infrastructure`

---

<a id="item-4"></a>
## [中国开放权重 AI 策略取得进展](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

一篇分析文章认为，中国的开放权重 AI 模型正在超越美国的专有模型，并将其与历史上市场向自由和开放软件转变的趋势相类比。文章声称 80%的初创公司正在使用中国模型，但一些评论者对此数据提出质疑。 这一趋势可能重塑全球 AI 格局，使先进 AI 更易获取，并减少对昂贵专有模型的依赖。同时，它也凸显了中美 AI 发展路径的战略分歧。 开放权重模型并非完全开源；它们允许免费使用和微调，但通常需要为托管付费。文章指出，OpenAI 和 Anthropic 等美国公司收取高推理利润率以收回成本，而中国模型则以更低成本提供。

hackernews · benwerd · Jul 20, 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48979269)

**背景**: 开放权重 AI 模型是指公开训练参数（权重）的模型，允许他人运行、微调和部署。这与 GPT-4 等仅提供 API 访问的专有模型形成对比。中国在其许多领先 AI 模型中采用了开放权重策略，例如百度和 Kimi 的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/open-source-ai-china-kimi-american-ai-industry-openai-anthropic-2026-7">Americans Are Freaking Out Over China 's Open - Source AI Strategy</a></li>
<li><a href="https://ashleydudarenok.com/china-ai-strategy/">China AI Strategy : Policy, Regulation & Global Impact in 2025</a></li>
<li><a href="https://www.uscc.gov/research/two-loops-how-chinas-open-ai-strategy-reinforces-its-industrial-dominance">Two Loops: How China ’s Open AI Strategy Reinforces Its Industrial...</a></li>

</ul>
</details>

**社区讨论**: 评论者就 80%初创公司使用中国模型的说法展开辩论，有人指出自身经验显示美国模型仍占主导。另一些人认为开放权重模型最终将因成本和灵活性胜出，尽管推理成本可能仍然较高。还有人指出开放权重并非真正开源，但仍比专有模型具有显著优势。

**标签**: `#AI`, `#open-source`, `#China`, `#market dynamics`, `#strategy`

---

<a id="item-5"></a>
## [黑客清空罗马尼亚土地登记数据库](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

一名黑客清空了罗马尼亚整个土地登记数据库，但官方利用离线备份恢复了服务，并正在将机构系统迁移至政府云。 此次针对关键国家基础设施的攻击本可能造成大规模社会混乱，包括无法证明土地所有权，凸显了离线备份和安全政府 IT 系统的重要性。 黑客被确认为来自阿尔及利亚的 Zakaria Mahdjoub，声称删除了备份，但该机构拥有离线副本。迁移至罗马尼亚政府云的工作由特别电信服务局（STS）协调，预计于 7 月 22 日完成。

hackernews · speckx · Jul 20, 13:28 · [社区讨论](https://news.ycombinator.com/item?id=48978605)

**背景**: 土地登记是记录财产所有权、抵押贷款和其他权利的关键政府数据库。丢失此类数据可能导致房地产交易、法律纠纷和税收征收瘫痪。离线备份是防御勒索软件和破坏性攻击的关键手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newsdirectory3.com/romania-land-registry-paralysed-by-major-cyberattack/">Romania Land Registry Paralysed by Major... - News Directory 3</a></li>
<li><a href="https://buzzverified.com/romania-land-registry-hack/">Romania Land Registry Hack - buzzverified.com</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，此次攻击可能源于政府 IT 合同中的腐败，关系户未能实施真正的安全措施。其他人将其与韩国类似的数据丢失事件相提并论，强调了健全备份实践的必要性。

**标签**: `#cybersecurity`, `#infrastructure`, `#data loss`, `#Romania`, `#hacking`

---

<a id="item-6"></a>
## [arXiv 上 AI 写作检测：到 2026 年 39%被标记](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

一项对 2021 年至 2026 年间 12,750 篇 arXiv 论文的分析发现，到 2026 年 1 月，约 39%的论文被标记为 AI 写作，其中计算机科学领域高达 65%，而数学领域仅略高于基线，为 0.7%。 这一测量结果凸显了 LLM 在学术写作中的快速普及，引发了对学术出版诚信以及 AI 检测工具可靠性的担忧——这些工具甚至可能对 LLM 出现前的人类写作产生误报。 该检测器经过调校以避免误报，在 ChatGPT 出现前的检测率仅为 0.4%。然而，社区测试显示，一篇 2015 年的 IEEE 论文被标记为 74%机器写作，表明可能存在校准问题。

hackernews · dopamine_daddy · Jul 20, 16:36 · [社区讨论](https://news.ycombinator.com/item?id=48981206)

**背景**: arXiv 是一个免费的开放获取预印本库，涵盖物理、数学和计算机科学等领域。自 2022 年底 ChatGPT 发布以来，LLM 越来越多地被用于辅助或生成学术文本，促使人们努力检测这类使用情况。然而，没有一种检测方法是 100%准确的，区分人类与 AI 写作仍然具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.01268v1">Mapping the Increasing Use of LLMs in Scientific Papers</a></li>
<li><a href="https://undetectable.ai/blog/how-to-detect-ai-writing-guide/">How to Detect AI Writing in 2025: Full Guide</a></li>

</ul>
</details>

**社区讨论**: 社区成员对检测可靠性表示怀疑，一位用户指出其 2011 年的论文被标记为 27%机器写作，2012 年的博士论文为 40%，这表明检测器可能将人类写作与 AI 输出混淆。另一位评论者认为，没有任何基于文本的检测器能可靠区分完全相同的人类和 AI 段落，凸显了根本性的局限。

**标签**: `#AI detection`, `#arXiv`, `#academic publishing`, `#LLM impact`, `#measurement`

---

<a id="item-7"></a>
## [Kimi K3、Qwen 3.8 与 Anthropic 的潜在危机](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

Moonshot AI 发布了拥有 2.8 万亿参数的开源权重模型 Kimi K3，阿里巴巴推出了 2.4 万亿参数的多模态模型 Qwen 3.8，加剧了与 Anthropic 和 OpenAI 的竞争。同时，Anthropic 面临内部动荡以及涉及 Figma 的利益冲突丑闻。 中国 AI 实验室快速发布强大的开源权重模型，标志着前沿 AI 能力的商品化，可能削弱 Anthropic 和 OpenAI 等专有实验室的商业模式。Anthropic 面临的道德和竞争压力可能重塑 AI 行业格局。 Kimi K3 拥有 100 万 token 的上下文窗口，针对深度推理和智能体工作流进行了优化，承诺于 2026 年 7 月开放权重。Qwen 3.8 采用稀疏混合专家架构，可处理文本、图像、视频和文档，声称性能仅次于 Fable 5。

hackernews · cl42 · Jul 20, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48980019)

**背景**: Anthropic 和 OpenAI 等前沿 AI 实验室传统上依赖专有模型和高订阅费。中国初创公司推出的竞争性开源权重模型威胁到 AI 能力的商品化，迫使实验室通过速度、专业化或道德品牌来差异化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/alibabas-qwen-takes-on-kimi-k3-with-open-weight-qwen-3-8-says-model-is-second-only-to-fable-5/">Alibaba's Qwen takes on Kimi K3 with open-weight Qwen 3.8, says model is "second only to Fable 5"</a></li>
<li><a href="https://www.youtube.com/watch?v=6-ccuwX4gCQ">Chinese AI Startup Moonshot Unveils Kimi K 3 Model - YouTube</a></li>
<li><a href="https://www.anthropic.com/economic-index">The Anthropic Economic Index \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者就开源权重模型是否会商品化 AI 展开辩论，有人认为用户会为稍好的模型支付溢价。其他人则强调道德问题，如 Figma-Anthropic 冲突，并指出炒作周期正在缩短，暗示 AI 进展可能达到平台期。

**标签**: `#AI`, `#LLMs`, `#economics`, `#open-source`, `#Anthropic`

---

<a id="item-8"></a>
## [本·汤普森提议美国立法将 AI 训练数据视为合理使用](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

本·汤普森提议美国通过一项法律，明确将 AI 训练数据收集视为合理使用，并禁止禁止模型蒸馏的服务条款，旨在帮助美国开放模型与中国对手竞争。 该提案解决了 AI 实验室在未经许可数据上训练却禁止对其模型进行蒸馏的虚伪问题，并可能通过允许美国开放模型利用前沿模型的蒸馏来重塑中美 AI 竞争格局。 汤普森还推测，阿里巴巴决定以开放权重发布 Qwen 3.8 Max 可能受到了习近平最近鼓励开源和合作的讲话的影响。

rss · Simon Willison · Jul 20, 17:09

**背景**: 模型蒸馏是一种将知识从大型 AI 模型转移到较小模型的技术，通常通过查询大型模型的 API 实现。目前，美国法院对使用受版权保护的数据进行 AI 训练的合法性存在争议，合理使用是一个关键辩护。汤普森的提案将把训练数据的合理使用写入法律，并阻止公司通过服务条款阻止蒸馏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://houstonlawreview.org/article/147422-fair-use-and-the-origin-of-ai-training">Fair Use and the Origin of AI Training | Published in Houston Law Review</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source AI`, `#copyright`, `#model distillation`, `#US-China competition`

---

<a id="item-9"></a>
## [Sam Altman 2022 年邮件揭示开源策略](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

2026 年 Musk 诉 Altman 案中曝光的一封 2022 年 Sam Altman 发给 OpenAI 董事会的邮件，概述了发布一个可在消费硬件上本地运行的开源 GPT-3 级别模型的计划，旨在阻止 Stability AI 等竞争对手。 这揭示了 OpenAI 内部将开源发布作为竞争策略的战略思考，为开源与专有 AI 开发之间的复杂动态提供了线索。 邮件特别提到要在 Stability AI 或其他公司之前发布一个具有近似 GPT-3 能力的模型，并认为这样的发布将阻止竞争对手，并使新项目更难获得资金。

rss · Simon Willison · Jul 20, 03:47

**背景**: GPT-3 是 OpenAI 于 2020 年发布的拥有 1750 亿参数的大型语言模型，以其少样本学习能力而闻名。以 Stable Diffusion 闻名的 Stability AI 后来在 2023 年发布了 StableLM 等开源语言模型。这封邮件早于 ChatGPT 的公开发布，反映了 OpenAI 早期对开源策略的考量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-3">GPT-3 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://www.theverge.com/2023/4/19/23689883/stability-ai-open-source-large-language-model-stablelm">Stability AI announces new open-source large language model | The Verge</a></li>

</ul>
</details>

**标签**: `#openai`, `#open-source`, `#ai-ethics`, `#sam-altman`, `#generative-ai`

---

<a id="item-10"></a>
## [Hugging Face 遭 AI 智能体入侵，商业大模型拒绝协助取证](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face 披露了 2026 年 7 月的一起安全事件：攻击者利用数据集处理流程中的两处代码执行漏洞，由自主 AI 智能体框架驱动，窃取了内部数据集和服务凭证。在事件响应中，商业大模型 API 因安全护栏拒绝分析攻击日志，团队被迫使用本地部署的 GLM 5.2 处理了超过 1.7 万条攻击记录。 这起事件凸显了新型 AI 驱动攻击，并揭示了一个关键盲点：商业大模型可能拒绝协助 AI 攻击的取证分析，从而削弱应急响应能力。它强调了组织需要维护本地、无限制的模型用于安全运营，并引发了对依赖专有 AI 服务的质疑。 攻击者利用了 Hugging Face 数据集处理流程中的两处代码执行漏洞，类似于微软 Semantic Kernel 框架中披露的 CVE-2026-25592 和 CVE-2026-26030。Hugging Face 确认公开的模型、数据集和 Spaces 未被篡改，软件供应链无异常；已修复漏洞、轮换受影响凭证，并建议用户轮换令牌并检查近期活动。

telegram · zaihuapd · Jul 20, 10:41

**背景**: Hugging Face 是一个托管 AI 模型、数据集和演示应用（Spaces）的主要平台。AI 智能体框架（如 Semantic Kernel）支持自主 AI 系统，但如果安全措施不当，可能引入代码执行漏洞。GLM 5.2 是 Z.ai（原智谱 AI）推出的开源大语言模型，采用 MIT 许可证发布，可本地部署且无限制性安全过滤器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/">When prompts become shells: RCE vulnerabilities in AI agent frameworks | Microsoft Security Blog</a></li>
<li><a href="https://z.ai/blog/glm-5.2">GLM-5.2: Built for Long-Horizon Tasks</a></li>

</ul>
</details>

**标签**: `#security`, `#AI safety`, `#Hugging Face`, `#LLM`, `#incident response`

---

<a id="item-11"></a>
## [特朗普政府或限制美企使用中国开放权重 AI 模型](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

Axios 报道称，特朗普政府正考虑通过软性限制手段，阻止美国企业使用像 Kimi K3 这样性能强劲且价格低廉的中国开放权重 AI 模型，而非直接封禁。 此举可能重塑全球 AI 竞争格局，限制美国企业获取高性价比的开放权重模型，从而减缓 AI 应用与创新。同时凸显了闭源 AI 巨头与开放权重运动之间的紧张关系。 Kimi K3 是 Moonshot AI 开发的 2.8 万亿参数开放权重多模态推理模型，输入价格每百万 token 仅 3 美元。拟议的限制措施包括采购规则、实体清单威胁和舆论压力，而非硬性封禁。

telegram · zaihuapd · Jul 20, 11:49

**背景**: 开放权重模型发布训练好的神经网络权重，允许用户自行托管和微调，比封闭 API 提供更多控制权。Kimi K3 是中国一系列有竞争力的开放权重模型的最新代表，以极低成本缩小了与美国模型的性能差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**社区讨论**: 新闻中未提供社区评论。

**标签**: `#AI policy`, `#open-source`, `#US-China`, `#Kimi K3`, `#regulation`

---

<a id="item-12"></a>
## [美军应用被发现嵌入中俄代码](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

普渡大学研究人员发现，面向美军人员推广的 220 多款应用中，近三分之二嵌入了来自中国和俄罗斯的第三方代码，包括华为 SDK。 这引发了国家安全担忧，因为嵌入的代码可被远程更新，从而从军事设备中窃取敏感数据，可能危及作战安全。 尽管未观察到数据流向华为服务器，但 SDK 可远程更新，存在潜在风险。在 103 名受访军人中，76%至 83%对应用包含中、俄、伊朗或朝鲜代码表示极度不安。

telegram · zaihuapd · Jul 20, 13:42

**背景**: 第三方 SDK 是应用集成的软件库，用于添加分析或认证等功能。华为的 SDK 因潜在的数据收集问题被美国政府列为国家安全威胁。美国国防部此前曾报告对手利用商业位置数据监视中东美军人员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://conzit.com/post/security-risks-foreign-code-in-military-apps-exposed">Security Risks: Foreign Code in Military Apps Exposed</a></li>

</ul>
</details>

**标签**: `#security`, `#military`, `#supply chain`, `#privacy`, `#SDK`

---

<a id="item-13"></a>
## [欧盟拟共享生物识别数据以换取美国免签](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/) ⭐️ 8.0/10

欧盟委员会正与特朗普政府谈判一项“增强边境安全伙伴关系”（EBSP）框架协议，根据该协议，美国将获得欧盟成员国生物识别数据库的访问权限，以换取欧盟公民的免签旅行待遇。 该协议可能为大规模监控和敏感生物识别数据的商品化树立危险先例，并可能压制欧洲的政治异议和 activism。 泄露的草案显示，欧盟几乎全盘接受了美方对数据无限制访问的要求，包括生物识别信息和基于政治观点的“风险指标”。该协议不会直接允许美国当局访问欧盟数据库，但要求在 2026 年底前达成操作性安排。

telegram · zaihuapd · Jul 20, 15:08

**背景**: 美国免签计划允许特定国家公民免签赴美停留最多 90 天。作为交换，伙伴国必须满足安全要求，包括共享旅客信息。EBSP 框架是这些谈判的最新版本，美国已将 2026 年 12 月 31 日定为达成协议的最后期限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ayedo.de/en/posts/transatlantischer-zugriff-auf-biometrische-daten-uneinigkeit-unter-eu-mitgliedstaaten/">Transatlantic Access to Biometric Data: Disagreement Among EU ...</a></li>
<li><a href="https://discover.passportindex.org/policy-and-regulations/visa-free-travel-personal-data-and-esta-where-do-u-s-eu-talks-stand/">Visa-Free Travel, Personal Data and ESTA: Where Do U . S .- EU Talks...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#biometric data`, `#EU-US relations`, `#surveillance`, `#civil liberties`

---