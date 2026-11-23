---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> From 24 items, 3 important content pieces were selected

---

1. [Masullo 黎曼猜想的 Lean 形式化进度图引发争议](#item-1) ⭐️ 8.0/10
2. [OpenAI 提出以困惑度作为衡量模型智能的共享指标](#item-2) ⭐️ 8.0/10
3. [美商务部将定稿规则，封堵中国 AI 公司远程用芯](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Masullo 黎曼猜想的 Lean 形式化进度图引发争议](https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3) ⭐️ 8.0/10

针对 Alessandro Masullo 声称证明广义黎曼猜想的 940 页手稿，其 Lean 形式化进度图已发布，同时 Hacker News 上 131 条评论的讨论对该证明的正确性及其获得的背书提出了质疑。 这一事件凸显了传统同行评审与新兴形式化验证方法之间的张力，并引发了在 AI 时代如何验证和认可数学证明的疑问。 进度图追踪了 Lean 形式化工作，但社区成员警告高完成度并不代表正确性，因为一个漏洞就可能使整个证明失效；该手稿被标注为“全人类完成，无 AI 参与”，且尚未经过同行评审。

hackernews · Qision · Nov 22, 23:12 · [社区讨论](https://news.ycombinator.com/item?id=50605045)

**背景**: Lean 是一种用于数学形式化的证明助手和函数式编程语言，拥有一个名为 Mathlib 的综合数学库。形式化涉及用机器可检查的语言编写定义和证明，可以验证正确性，但极其耗时。广义黎曼猜想是数论中一个重要的未解决问题，Masullo 的手稿是作为未完成草稿发布的 proposed 证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://www.arpaia.io/files/mathematics/riemann-hypothesis-masullo.pdf">Alessandro Masullo’s Proof of the Riemann Hypothesis</a></li>
<li><a href="https://riemannhypothesisclaude.org/alessandro-masullo">Alessandro Masullo's GRH Proof: What Vakil Announced</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了严重怀疑：一位参与该仓库的数学家指出，现在判断是否存在重大漏洞还为时过早，而其他人则指出 Ravi Vakil 声称他甚至没有看过该文档，Brian Conrad 表示需要“重大修订”。一些人还对 AI 和公司对数学的影响表示担忧。

**标签**: `#Lean`, `#formalization`, `#mathematics`, `#proof-verification`, `#academic-discourse`

---

<a id="item-2"></a>
## [OpenAI 提出以困惑度作为衡量模型智能的共享指标](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI 发表文章，主张将困惑度（等价于交叉熵损失）确立为比较不同模型开发者并制定共享安全标准的指标，同时提高了其自身预训练进展的透明度。该文章在 Hacker News 上引发了大规模讨论（485 分，334 条评论），探讨为何这种简单的下一词元预测损失与模型能力如此强相关。 如果被采纳，困惑度可能成为一个简单、标准化的基准，用于跨开发者比较模型，取代每天涌现的日益复杂的基准测试。这将影响模型开发者、安全研究人员以及任何需要评估或信任大语言模型能力的人，因为它能够促成共享安全标准并实现更透明的预训练进展报告。 困惑度是模型在预测序列中下一个词元时的惊讶程度；最差情况下等于词汇表大小，最好情况下为 1。评论者指出，微软已表示加入这一努力，Mustafa Suleyman 分享称 MAI-2 Base 在 OpenAI 的评估集上对数困惑度为 0.819，但低困惑度并不保证高质量生成、事实准确性或对齐行为。

hackernews · acossta · Nov 22, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**背景**: 困惑度是一种信息论度量，衡量概率模型对样本的预测能力，在语言建模中它等价于指数化的交叉熵损失，而交叉熵损失正是下一词元预测的训练信号。困惑度越低，意味着模型对实际词元赋予更高概率，预测性能更好。预测即压缩、原始数据上的压缩率体现智能这一观点早在先前工作中被提出，社区讨论将其与强化学习和推理模型的更广泛趋势联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cross-entropy">Cross-entropy - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者认为，在强化学习兴起的背景下，困惑度与智能之间的强相关性令人惊讶，但许多人同意从预测即压缩的角度回看这是合理的。一位评论者链接到 2008 年论证此观点的论文，另一位则强调了微软据称的参与并分享了 MAI-2 Base 的结果。总体情绪积极，赞赏在日益复杂的评估中有一个简单的基准。

**标签**: `#llm`, `#perplexity`, `#machine-learning`, `#model-evaluation`, `#information-theory`

---

<a id="item-3"></a>
## [美商务部将定稿规则，封堵中国 AI 公司远程用芯](https://t.me/zaihuapd/45289) ⭐️ 8.0/10

美国商务部正在敲定一项规则，阻止中国 AI 公司通过境外数据中心远程使用先进 AI 芯片，最早可能于本月公布。该规则将现有的半导体出口限制扩展至马来西亚、新加坡、泰国等七个东南亚国家，以封堵远程访问和芯片走私漏洞。 该规则将美国出口管制的范围从实体芯片运输大幅扩展至远程访问，可能重塑中国企业的全球 AI 算力获取途径。它直接影响到英伟达等主要公司（英伟达曾游说反对该措施），并可能改变整个东南亚的数据中心战略。 该规则是在与其他政府机构磋商后定稿的，白宫此前已要求国会立法要求商务部制定这一规则。英伟达曾辩称美国 AI 基础设施需在全球取胜，但政府仍继续推进以封堵远程访问缺口。

telegram · zaihuapd · Nov 22, 04:34

**背景**: 美国对先进 AI 芯片（如英伟达 GPU）的出口管制传统上侧重于限制向特定国家（尤其是中国）的实体运输。然而，中国企业可以通过位于第三国的数据中心远程访问芯片来绕过这些限制。这项新规则旨在通过将管制扩展至更多国家并规范远程访问来封堵这一漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.freemalaysiatoday.com/category/nation/2025/07/04/us-to-restrict-ai-chip-shipments-to-malaysia-thailand">US to restrict AI chip shipments to Malaysia , Thailand | FMT</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-lobbies-white-house-and-wins-loosened-ai-gpu-export-control-to-china-u-s-lawmakers-reportedly-reject-gain-ai-act">Nvidia lobbies White House and wins loosened AI GPU export control...</a></li>

</ul>
</details>

**标签**: `#export controls`, `#AI chips`, `#US-China tech`, `#semiconductor policy`, `#Nvidia`

---