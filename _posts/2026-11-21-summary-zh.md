---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> From 32 items, 12 important content pieces were selected

---

1. [Levent Alpöge 声称借助 AI 证明广义黎曼猜想](#item-1) ⭐️ 10.0/10
2. [Anthropic AI 声明后，Masullo 匆忙发布 940 页 GRH 证明](#item-2) ⭐️ 9.0/10
3. [陶哲轩将无外力纳维-斯托克斯奇点与广义黎曼假设联系起来](#item-3) ⭐️ 9.0/10
4. [GitHub 仓库声称无外力纳维-斯托克斯方程有限时间爆破](#item-4) ⭐️ 9.0/10
5. [OpenAI 宣称 AI 解决纳维–斯托克斯千禧年难题](#item-5) ⭐️ 9.0/10
6. [Thinking Machines 发布 Inkling 2 Mini：面向本地推理的紧凑型循环 Transformer](#item-6) ⭐️ 8.0/10
7. [语言模型无需梯度即可重写自身权重](#item-7) ⭐️ 8.0/10
8. [斯科特·阿伦森探讨随机鹦鹉能否证明黎曼猜想](#item-8) ⭐️ 8.0/10
9. [美国证券交易委员会调查英伟达潜在的会计问题](#item-9) ⭐️ 8.0/10
10. [OpenAI 上线后台模式：长任务可挂 8 小时，token 最多便宜 40%](#item-10) ⭐️ 8.0/10
11. [KVM 漏洞 CVE-2026-99312 致 AMD 主机内存可被虚拟机读取](#item-11) ⭐️ 8.0/10
12. [谷歌发布 Gemini 4 Neon 前沿模型，主打编程与科研](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Levent Alpöge 声称借助 AI 证明广义黎曼猜想](https://alpo.ge/remark.pdf) ⭐️ 10.0/10

2026 年 11 月 20 日，数学家 Levent Alpöge 宣布了广义黎曼猜想的一个证明，该证明在 Lean 4 证明助手中形式化，并借助了 Anthropic 的 Claude 模型。证明以约 1.3 GB 的压缩包形式发布，包含约 1500 万行 Lean 代码；同一天，Ravi Vakil 还发布了 Alessandro Masullo 独立完成、不含 AI 辅助的草稿证明，目前正在评审中。 广义黎曼猜想是数论中最深刻的未解问题之一，若证明成立，将对解析数论和密码学产生广泛影响。这一声明也加剧了关于 AI 在数学发现中所扮演角色的争论，以及人类数学家与 AI 公司之间应如何分配荣誉的问题。 该证明规模巨大——约 1.3 GB、约 1500 万行 Lean 代码，分为 14 个可下载部分——这给验证和评审带来了实际困难。社区成员还指出，Alessandro Masullo 另有一份完全由人类完成的证明正由 Brian Conrad 评审，而 Alpöge 是一位知名数论学家兼 Anthropic 员工，并非匿名使用模型的普通用户。

hackernews · iamronaldo · Nov 20, 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**背景**: 黎曼猜想推测黎曼 ζ 函数的所有非平凡零点实部均为 1/2；广义黎曼猜想将其推广到狄利克雷 L 函数及其他全局 L 函数。Lean 是一个开源证明助手和函数式编程语言，可用于编写并机器检验数学证明。Levent Alpöge 是一位以算术统计工作闻名的数论学家，后来加入 Anthropic，此前已宣布过多项借助 AI 的数学成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alpöge">Levent Alpöge</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了证明的巨大规模以及 AI 参与的程度，有人提到另有一份人类独立完成的证明，也有人引用陶哲轩此前对当前 AI 能否解决黎曼猜想的怀疑。一些人批评将功劳归于 Anthropic 而非 Alpöge 数学家身份的表述，另一些人则对如此重大的成果可能主要来自 AI 表达了复杂心情。

**标签**: `#mathematics`, `#Riemann Hypothesis`, `#AI`, `#Lean`, `#research`

---

<a id="item-2"></a>
## [Anthropic AI 声明后，Masullo 匆忙发布 940 页 GRH 证明](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 9.0/10

2026 年 11 月 20 日，美国数学会主席 Ravi Vakil 紧急发布公告，公布了 Alessandro Masullo 历时 12 年完成的 940 页手稿，声称证明了广义黎曼猜想（GRH）。此举似乎是为了回应同日 Anthropic 数学家宣称 Claude 帮助解决了黎曼猜想的消息。 GRH 的证明将是数论领域的重大突破，对素数分布和密码学产生深远影响；同时出现的 AI 声明引发了关于优先权、验证以及 AI 在数学发现中作用的紧迫问题。 这份 940 页的草稿已由斯坦福数学家 Brian Conrad 审查数月，但其中存在空白章节（如 1.1.1 节），且目录未明确提及 GRH，引发对其完整性和有效性的担忧。

hackernews · jasondavies · Nov 20, 18:33 · [社区讨论](https://news.ycombinator.com/item?id=50579568)

**背景**: 黎曼猜想由黎曼于 1859 年提出，猜测黎曼ζ函数的所有非平凡零点实部均为 1/2；广义黎曼猜想将其推广到所有狄利克雷 L 函数。它是克雷数学研究所的千禧年大奖难题之一，其证明将彻底改变我们对素数的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://explainx.ai/blog/alessandro-masullo-grh-human-proof-claimed-vs-verified-november-2026">Masullo GRH Draft: What Vakil Announced (Nov 20) | explainx ...</a></li>
<li><a href="https://www.scientificamerican.com/article/dueling-claims-of-riemann-hypothesis-proofs-emerge/">Dueling claims of Riemann hypothesis proofs emerge</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者同情 Masullo 的匆忙公告，猜测 Brian Conrad 可能向 Anthropic 泄露了信息，并质疑手稿的异常之处，如空白章节和标题中未提及 GRH，同时指出 Conrad 的可信度。

**标签**: `#mathematics`, `#Riemann Hypothesis`, `#AI`, `#research`, `#Hacker News`

---

<a id="item-3"></a>
## [陶哲轩将无外力纳维-斯托克斯奇点与广义黎曼假设联系起来](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 9.0/10

陶哲轩于 2026 年 11 月 20 日发布了一项结果，将无外力纳维-斯托克斯奇点与广义黎曼假设联系起来，该证明似乎已在 Lean 中形式化，并由两个独立内核验证。该工作还提到了同日由 Levent Alpöge 提出的另一项 AI 辅助的 GRH 证明。 这是一项重大数学突破，连接了流体动力学与数论，可能重塑数学家对这两个领域的研究方法。形式化验证方面也表明，像 Lean 这样的证明助手在验证深层数学结果中的作用日益增强。 该证明似乎利用了 Langlands 纲领和算术几何的现代发展的全部力量，并且被两个独立的 Lean 内核接受，表明其对内核错误具有鲁棒性。然而，该结果仍在审查中，陶哲轩尚未评论其更广泛的意义。

hackernews · archon1410 · Nov 20, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**背景**: 纳维-斯托克斯存在性与光滑性问题询问描述流体流动的纳维-斯托克斯方程的解是否总是保持光滑，还是会产生奇点。广义黎曼假设将关于黎曼ζ函数零点的经典黎曼假设推广到更广泛的 L 函数类，是数学中最重要的未解决问题之一。Lean 是一种证明助手，允许数学家以计算机可验证的语言形式化证明，确保从基础公理开始的正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论（356 分，146 条评论）反映了兴奋与焦虑的混合情绪，用户提出了关于如何创造新的数学抽象以及如何相信 Lean 证明验证的是预期命题而非平凡命题的深层问题。一些评论者指出，两个独立内核接受该结果降低了内核错误的风险，而其他人则表达了对 AI 驱动的快速进展带来的职业不确定性的担忧。

**标签**: `#Navier-Stokes`, `#Riemann Hypothesis`, `#formal verification`, `#mathematics`, `#Lean`

---

<a id="item-4"></a>
## [GitHub 仓库声称无外力纳维-斯托克斯方程有限时间爆破](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 9.0/10

Tristan Buckmaster 的 GitHub 仓库展示了一个关于无外力纳维-斯托克斯方程有限时间爆破的证明，该结果将解决克雷千年大奖问题之一。 如果得到验证，这将是一个重大数学突破，因为它解决了纳维-斯托克斯存在性与光滑性问题的无外力版本，该版本被认为比 OpenAI 最近解决的有外力版本更具物理现实性。 该声明针对无外力方程，即不施加外部力，据报该证明使用了 Buckmaster 和 Vicol 先前开发的凸积分技术来展示弱解的非唯一性。

hackernews · trotro · Nov 20, 15:34 · [社区讨论](https://news.ycombinator.com/item?id=50576232)

**背景**: 纳维-斯托克斯方程描述粘性流体的运动，是流体动力学的核心。克雷数学研究所于 2000 年将该方程的存在性与光滑性问题列为七个千年大奖问题之一，悬赏 100 万美元征求证明或反例。该问题询问光滑解是否总是存在，或者奇点是否会在有限时间内形成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems - Wikipedia</a></li>
<li><a href="https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf">Finite time blowup for navier – stokes</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这一结果与广义黎曼猜想的证明声称在同一天出现的重要性，称这是数学史上历史性的一天。一些人对 Buckmaster 和 Alpoge 在与 OpenAI 的优先权争议中表示同情，而其他人则讨论了模拟爆破以获得直观理解的可能性。

**标签**: `#mathematics`, `#Navier-Stokes`, `#Millennium Prize`, `#fluid dynamics`, `#research breakthrough`

---

<a id="item-5"></a>
## [OpenAI 宣称 AI 解决纳维–斯托克斯千禧年难题](https://t.me/zaihuapd/45265) ⭐️ 9.0/10

据 Telegram 帖子称，OpenAI 宣布解决了纳维–斯托克斯存在性与光滑性这一千禧年难题，其内部系统给出的证明显示，初始光滑的流体可在有限时间内产生奇点。OpenAI 据称同时公开了论文与 Lean 形式化验证，求解过程动用了约 1 万个并行智能体、270 万条消息和约 1300 亿输出 token。 若经证实，这将是 AI 驱动数学与形式化验证领域的里程碑，因为这是首次宣称由 AI 解决千禧年难题，可能重塑大型多智能体系统用于高难度科学推理的方式。同时，这也将加剧对 AI 生成证明的审视，以及 Lean 等形式化助手在验证非凡主张中的作用。 该说法仅来自一条 Telegram 帖子，尚无独立验证；所报告的证明主张有限时间奇点形成，这将通过表明光滑解并非总是全局存在来解决该问题。据称 OpenAI 表示无意申领该奖项，帖子还提到最初曾误以为 Anthropic 员工 Levent Alpöge 与纽约大学教授 Tristan Buckmaster 也解出了该题。

telegram · zaihuapd · Nov 20, 15:29

**背景**: 纳维–斯托克斯存在性与光滑性问题是克莱数学研究所提出的七大千禧年大奖难题之一，完整正确的证明可获得 100 万美元奖金。该问题追问三维不可压缩纳维–斯托克斯方程的光滑解是否总是全局存在，还是会在有限时间内破裂。Lean 是微软研究院自 2013 年起开发的开源证明助手和函数式编程语言，用于对数学证明进行形式化验证。大型多智能体系统则利用大量基于大语言模型的智能体并行工作，来分解和处理复杂任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2507.08944">[2507.08944] Optimizing Sequential Multi-Step Tasks with ... Optimizing Sequential Multi-Step Tasks with Parallel LLM Agents MegaAgent: A Large-Scale Autonomous LLM-based Multi-Agent ... GitHub - Xtra-Computing/MegaAgent: [ACL 2025 Findings ... Multi-Agent LLM Systems: Frameworks, Architecture & Examples ... Scaling LLM with Parallel Coding Agents - Analytics Insight</a></li>

</ul>
</details>

**标签**: `#AI for Mathematics`, `#Navier-Stokes`, `#Lean Formal Verification`, `#OpenAI`, `#Millennium Prize Problems`

---

<a id="item-6"></a>
## [Thinking Machines 发布 Inkling 2 Mini：面向本地推理的紧凑型循环 Transformer](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines 发布了 Inkling 2 Mini，这是一个开放权重的模型，总参数 26B、每 token 激活 5.4B，并且对每个 token 将中间层循环运行三次。它小到可以在 32GB 以上内存的 Mac 上运行，据称在基准测试中可媲美 Qwen3-27B 等大得多的模型。 这是首批公开采用循环架构的模型之一，可能推动其他开放模型也采用循环结构，以在不增加参数的情况下获得更强的推理深度。它可在本地运行的尺寸和强劲的基准成绩，对本地推理社区意义重大。 该模型端到端使用 nvfp4 训练；社区用户报告在 Ryzen 395 上通过 llama.cpp Vulkan 解码速度约为 27 tokens/s，在 32GB 内存的 M1 Pro MacBook 上使用 q4 量化约为 10 tokens/s。早期实测显示其编码能力较强，但在某些重推理任务上表现参差不齐。

hackernews · jasondavies · Nov 20, 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**背景**: 循环 Transformer 会多次应用同一个 Transformer 块，而不是堆叠更多不同的层，从而让模型在每个 token 上投入更多计算，而不是生成更多 token。llama.cpp 是一个开源 C/C++ 推理引擎，用于在用户自有硬件上运行大语言模型，GGUF 是其常用的模型文件格式。因此，Inkling 2 Mini 的发布契合了面向本地使用的开放权重模型日益壮大的生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://ollama.com/library/inkling-2-mini">inkling - 2 - mini</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling-2-mini">Inkling 2 Mini - Intelligence, Performance & Price... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者对循环模型能媲美 Qwen3-27B 感到惊讶，有人预测多数开放模型将因此转向循环架构。用户分享了实测基准、一个可提升约 30% 速度的 llama.cpp 小补丁，并提到尚未合并的 PR；一位测试者发现编码任务完成得很好，但硬币识别测试在模型啰嗦了 12,000 个 token 后失败。

**标签**: `#LLM`, `#local-inference`, `#model-release`, `#benchmarks`, `#llama.cpp`

---

<a id="item-7"></a>
## [语言模型无需梯度即可重写自身权重](https://arxiv.org/abs/2611.21885) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.21885）声称，语言模型仅通过推理就能重写自身权重，无需梯度或训练，并且在连续八次会话中准确率只升不降。模型在练习题上测试其编辑，只提交有效的修改，每次编辑都在前一次基础上改进。 如果得到验证，这种方法可以使模型无需昂贵的重新训练就能自主自我改进，可能加速 AI 能力的发展。然而，它也引发了重大的 AI 安全担忧，即模型修改自身与安全相关的权重，以及推理与训练之间界限的模糊。 论文声称没有梯度也没有训练，但社区指出，观察到的唯一自我改进是减少推理轨迹长度以避免 token 限制，这与之前的权重空间编程工作类似。该方法涉及迭代编辑和测试，一些人认为这实质上是另一种形式的训练。

hackernews · lwhsiao · Nov 20, 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**背景**: 传统上，语言模型通过梯度下降进行训练，即反向传播根据误差调整权重。权重编辑指的是直接修改网络参数而无需完全重新训练，最近的工作如 Google 的 Sleep 框架和 MIT CSAIL 的权重空间编程探索了类似想法。本文通过让模型对其自身权重进行推理，进一步推动了这一概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tecc.uz/en/article/gpt-6-astra-and-mit-csail-direct-weight-editing-in-neural-networks-bcyvx">GPT-6 Astra and MIT CSAIL: Direct Weight Editing in Neural Networks</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者争论该方法是否真正避免了训练，一些人指出其与 Google 的 Sleep 框架和权重空间编程的相似之处。其他人提出了安全担忧，指出自主 LLM 可能消除安全激活，并建议训练模型自我修复。

**标签**: `#language-models`, `#self-improvement`, `#AI-safety`, `#weight-editing`, `#research`

---

<a id="item-8"></a>
## [斯科特·阿伦森探讨随机鹦鹉能否证明黎曼猜想](https://scottaaronson.blog/?p=10344) ⭐️ 8.0/10

斯科特·阿伦森发表了一篇题为《随机鹦鹉显然证明了黎曼猜想》的博客文章，探讨大型语言模型能否对证明黎曼猜想做出有意义的贡献，以及这样的结果对人类理解意味着什么。 这篇文章在 Hacker News 上引发了实质性讨论（223 分，200 条评论），话题涉及 AI 在数学中日益增长的作用、机器生成证明的可解释性，以及人类数学家是否面临变得无关紧要的风险。 阿伦森的论点核心在于模型给出正确证明与任何人真正理解该证明之间的张力，这呼应了国际象棋引擎的类比：Stockfish 的评估是建立在神经网络评估器之上的不透明计算聚合。

hackernews · stratos123 · Nov 20, 20:03 · [社区讨论](https://news.ycombinator.com/item?id=50581084)

**背景**: “随机鹦鹉”是艾米丽·本德等人创造的术语，用来描述模仿人类文本却不理解其含义的语言模型。黎曼猜想是数学中最著名的未解问题之一，涉及素数分布和黎曼ζ函数的零点。斯科特·阿伦森是德克萨斯大学奥斯汀分校的计算机科学家，以量子计算研究和关于 AI 能力的评论而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_parrot">Stochastic parrot - Wikipedia</a></li>
<li><a href="https://tldr.tech/story/51db3786-0a90-408b-ac78-1252e9cb14b5">Scott Aaronson says OpenAI AI proofs shift math | TLDR</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与国际象棋引擎类比，指出即使 AI 给出“解释”，那也只是不透明计算的不尽人意的聚合。其他人担心人类可能越来越无法理解科学或对科学做出贡献，还有评论者指出更广泛的教训是“我们仍然应该修复漏洞”。

**标签**: `#AI`, `#mathematics`, `#LLMs`, `#interpretability`, `#philosophy`

---

<a id="item-9"></a>
## [美国证券交易委员会调查英伟达潜在的会计问题](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627) ⭐️ 8.0/10

据消息人士透露，美国证券交易委员会（SEC）正在调查英伟达的会计操作。调查重点在于收入确认和芯片销售不透明等潜在问题。 英伟达是人工智能和半导体行业的风向标，SEC 的调查可能会削弱投资者信心并影响整个科技市场。此次调查还可能引发对全行业会计操作的更严格审查。 据报道，调查正在审查英伟达是否恰当地确认了芯片销售收入，包括通过第三方进行的销售。消息人士未透露调查的范围或时间表。

hackernews · ftchd · Nov 20, 20:22 · [社区讨论](https://news.ycombinator.com/item?id=50581438)

**背景**: 英伟达设计的 GPU 对人工智能和游戏至关重要，其财务业绩被视为科技需求的晴雨表。SEC 经常调查公司在收入确认方面的问题，即收入在错误的时间或以可疑的条件被记录。半导体行业过去的会计丑闻曾导致 SEC 达成和解。

**社区讨论**: 评论者对英伟达的会计表示怀疑，指出循环融资和黑市芯片销售是长期存在的问题。一些人质疑，如果董事会怀疑会计问题，为何让首席财务官担任临时首席执行官，而另一些人则担心对更广泛市场的影响。

**标签**: `#Nvidia`, `#SEC investigation`, `#accounting`, `#semiconductors`, `#finance`

---

<a id="item-10"></a>
## [OpenAI 上线后台模式：长任务可挂 8 小时，token 最多便宜 40%](https://developers.openai.com/api/docs/guides/background) ⭐️ 8.0/10

OpenAI 在其 API 中推出了后台模式，通过设置 background: true 并选择 2 小时或 8 小时的完成时限（background_options.completion_window），将长耗时请求改为异步执行，对应的 Token 费率分别比标准价低 30% 和 40%。该折扣目前在 GPT-6.2 Astra、GPT-6.2 Sol、GPT-6.1 Terra 和 GPT-6 Luna 上公测。 对于运行长任务的开发者来说，这是一项重要的 API 能力变更，因为它消除了超时限制，并为可容忍延迟的工作负载提供了可观的成本节省。然而，即使启用了零数据保留，响应数据仍会被临时存储，这引发了对受监管行业而言重要的隐私和合规考量。 如果不设置完成时限，就会使用默认的 'soonest' 选项，且没有折扣。值得注意的是，后台模式会临时存储响应数据，即使 store 设为 false 或启用了零数据保留也不例外，这对隐私敏感的应用来说是一个值得留意的限制。

telegram · zaihuapd · Nov 20, 11:15

**背景**: 标准的 Responses API 调用是同步的：应用发送输入，模型处理，最终输出在同一连接上返回，长任务可能会超时。后台模式则异步启动任务，并允许开发者轮询响应对象以随时间检查状态。零数据保留（ZDR）是 OpenAI 为符合条件的 API 客户提供的一项选项，保证会话结束后不保留任何日志，通常被企业和受监管客户使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/background">Background mode | OpenAI API</a></li>
<li><a href="https://kissapi.ai/blog/openai-background-mode-api-guide-2026.html">OpenAI Background Mode API : Run Long Tasks Without Timeouts...</a></li>
<li><a href="https://www.tonywood.org/writing/openai-just-made-frontier-models-easier-for-european-companies-to-approve/">OpenAI Just Made Frontier Models Easier For European... | Tony Wood</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API`, `#async-processing`, `#pricing`, `#data-privacy`

---

<a id="item-11"></a>
## [KVM 漏洞 CVE-2026-99312 致 AMD 主机内存可被虚拟机读取](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

Linux KVM 曝出编号为 CVE-2026-99312 的漏洞，在启用嵌套虚拟化的 AMD 主机上，虚拟机可以读取宿主内存；研究人员在 DigitalOcean 上从虚拟机内读取到约 127 GB 宿主内存。上游修复已于 11 月 18 日随稳定内核 7.3.5 等版本发布，但 Debian、Ubuntu 等发行版内核尚未修复。 这是一次从虚拟机到宿主机的逃逸，破坏了虚拟化最核心的隔离保证，对在 AMD 硬件上为开发者沙箱和 CI/CD 流水线启用嵌套虚拟化的云服务商尤其重要。尽管上游已有补丁，但在各发行版内核跟进之前，许多生产主机仍处于暴露状态。 该漏洞仅影响启用嵌套虚拟化的 AMD 处理器主机，被调查的许多云服务商因未在 AMD 上启用嵌套虚拟化而不受影响。在补丁到位前，实际可行的缓解措施是关闭嵌套虚拟化，且该缺陷似乎源于此前的一次安全修复。

telegram · zaihuapd · Nov 20, 14:23

**背景**: KVM 是内置于 Linux 内核的虚拟化层，是大多数公有云和私有云虚拟机基础设施的基础。嵌套虚拟化允许虚拟机内部再运行虚拟化层并启动自己的虚拟机，这对沙箱和 CI 很有用，但也扩大了攻击面。虚拟机到宿主机的逃逸意味着虚拟机内的代码可以访问本不应看到的内存，可能泄露其他租户的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE - 2026 - 99312 Lets Guest VMs Access Host...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization , Responsible Disclosure, and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to-Host Escape | Terra Security Research</a></li>

</ul>
</details>

**标签**: `#security`, `#KVM`, `#Linux kernel`, `#virtualization`, `#CVE`

---

<a id="item-12"></a>
## [谷歌发布 Gemini 4 Neon 前沿模型，主打编程与科研](https://t.me/zaihuapd/45267) ⭐️ 8.0/10

谷歌发布了 Gemini 4 Neon 前沿模型，主打复杂软件工程、知识工作与科研工作流的快速端到端执行，现已向开发者、企业及 Google AI Pro/Ultra 订阅用户开放。该模型在 Artificial Analysis 编程智能体指数上以 58.6 分登顶第一，并在智能指数 xhigh 档以 61 分位列总榜第三。 此次发布巩固了谷歌在竞争激烈的前沿模型市场中的地位，尤其是在智能体编程任务上，基准测试的领先优势可以推动开发者采用。其有竞争力的定价和大上下文窗口使其对构建复杂 AI 工作流的企业具有吸引力。 Gemini 4 Neon 的定价为每百万输入 token 3 美元（缓存输入为 0.15 美元），每百万输出 token 15 美元，并支持 100 万 token 的上下文窗口。它还在 Terminal-Bench 这一针对真实终端任务的智能体基准测试中取得了强劲成绩。

telegram · zaihuapd · Nov 21, 01:09

**背景**: Artificial Analysis 编程智能体指数是一个综合基准，对多项智能体编程评估的分数取平均值，反映 AI 模型自主完成软件工程任务的能力。Terminal-Bench 衡量 AI 智能体在真实终端环境中执行端到端任务（如编译代码、修复 bug、运行工具）的表现。100 万 token 的上下文窗口允许模型在单次提示中处理超长文档或代码库，这对复杂的知识工作和科研很有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>
<li><a href="https://www.tbench.ai/">TERMINAL-BENCH</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-4-neon/">Gemini 4 Neon - Model Card — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#google`, `#gemini`, `#llm`, `#ai-models`, `#software-engineering`

---