---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 25 items, 6 important content pieces were selected

---

1. [SGLang v0.5.12 新增对 DeepSeek V4 的完整推理支持](#item-1) ⭐️ 9.0/10
2. [δ-Mem：基于 Delta 规则的固定大小 LLM 记忆方法](#item-2) ⭐️ 8.0/10
3. [前沿 AI 打破开放 CTF 竞赛模式](#item-3) ⭐️ 8.0/10
4. [DeepSeek-V4-Flash 重燃 LLM 操控兴趣](#item-4) ⭐️ 8.0/10
5. [谷歌将操纵 AI 搜索结果列为垃圾内容](#item-5) ⭐️ 8.0/10
6. [GitHub Copilot 桌面应用进入技术预览](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.12 新增对 DeepSeek V4 的完整推理支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 9.0/10

SGLang v0.5.12 已发布，新增对 DeepSeek V4 的完整推理支持，包括张量并行、专家并行、上下文并行和数据并行注意力，以及针对 MegaMoE 优化的 DeepGemm 和 FlashMLA 内核。 此版本使得在包括 Nvidia B300/B200/H200/H100 和 AMD MI35X 在内的多种硬件上高效部署 DeepSeek V4（一个 1.6 万亿参数的最先进模型）成为可能，显著降低了在生产中运行大规模 MoE 模型的门槛。 关键特性包括用于将非活跃 KV 缓存卸载到 CPU 内存的 HiSparse、带有 UnifiedRadixTree 的 HiCache、速度更快且精度损失可忽略的 W4A4 MegaMoE 内核，以及适用于所有 Nvidia GPU 的统一 Docker 标签。

github · Fridge003 · May 16, 18:23

**背景**: DeepSeek V4 是一个采用混合专家（MoE）架构的大型语言模型，总参数达 1.6 万亿，激活参数为 490 亿。SGLang 是一个开源推理框架，专为高效服务大型语言模型而设计，支持高级并行性和内核优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-04-10-sglang-hisparse/">HiSparse : Turbocharging Sparse Attention with... | LMSYS Org</a></li>
<li><a href="https://www.morphllm.com/deepseek-v4">DeepSeek V4: Architecture, Benchmarks, and API Guide (2026)</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#DeepSeek`, `#SGLang`, `#inference`, `#parallelism`

---

<a id="item-2"></a>
## [δ-Mem：基于 Delta 规则的固定大小 LLM 记忆方法](https://arxiv.org/abs/2605.12357) ⭐️ 8.0/10

δ-Mem 提出了一种通过 delta 规则学习更新的固定大小状态矩阵，用于压缩历史信息，实现大型语言模型的高效在线记忆。 该方法解决了 LLM 对高效长期记忆日益增长的需求，有望在不扩展上下文窗口的情况下降低计算成本，并实现更具上下文感知能力的 AI 代理。 Delta 规则学习增量更新状态矩阵，但社区评论指出容量限制和查询关联挑战仍未解决，且该方法类似于向现有 LLM 添加 DeltaNet 超网络。

hackernews · 44za12 · May 16, 09:30 · [社区讨论](https://news.ycombinator.com/item?id=48158506)

**背景**: 大型语言模型通常具有固定的上下文窗口，限制了它们在长对话或会话间记忆信息的能力。在线记忆方法旨在将过去的交互压缩成紧凑的表示，以便后续保留和查询，但它们在记忆大小、检索准确性和计算效率之间存在权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Learning_rule">Learning rule - Wikipedia</a></li>
<li><a href="https://supermemory.ai/blog/3-ways-to-build-llms-with-long-term-memory/">3 Ways To Build LLMs With Long-Term Memory</a></li>
<li><a href="https://machinelearningatscale.substack.com/p/deep-dive-into-memory-for-llms-architectures">Deep dive into "Memory for LLMs" architectures</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：有人欣赏该方法，但指出它没有解决根本的容量限制问题；另有人指出标题被错误修改，并认为该工作创新性不高。还有人对跨会话记住指南等实际应用感兴趣。

**标签**: `#LLM`, `#memory`, `#compression`, `#deep learning`, `#efficiency`

---

<a id="item-3"></a>
## [前沿 AI 打破开放 CTF 竞赛模式](https://kabir.au/blog/the-ctf-scene-is-dead) ⭐️ 8.0/10

一篇博客文章指出，前沿 AI 模型通过提供即时解决方案，从根本上破坏了开放 CTF（夺旗赛）模式，削弱了协作学习体验，并对传统竞赛结构构成挑战。 这种颠覆威胁到 CTF 的教育价值——CTF 是网络安全技能的关键训练场——并迫使社区在 AI 时代重新思考挑战设计和竞赛规则。 文章强调，AI 现在可以在几分钟内解决典型的 CTF 挑战，将焦点从解决问题转向 AI 辅助获取旗帜，使得参与和构建 CTF 挑战的成就感都降低了。

hackernews · frays · May 16, 07:01 · [社区讨论](https://news.ycombinator.com/item?id=48157559)

**背景**: 夺旗赛（CTF）是网络安全竞赛，参与者通过解决挑战来寻找隐藏的“旗帜”并获取积分。它们广泛用于逆向工程、密码学、Web 漏洞利用等领域的技能学习和培养。前沿 AI 模型（如先进的大语言模型）现在可以自动化许多此类任务，引发了对这类竞赛未来的质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.paloaltonetworks.com/blog/2026/04/defenders-guide-frontier-ai-impact-cybersecurity/">Defender's Guide to the Frontier AI Impact on Cybersecurity</a></li>
<li><a href="https://www.cyber.gov.au/about-us/view-all-content/news/frontier-models-and-their-impact-on-cyber-security-update">Frontier AI models and their impact on cyber security | Cyber.gov.au</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 AI 破坏 CTF 参与和构建的沮丧，有人指出协作解决问题的体验已丧失。一些人建议提高挑战难度或禁止 AI，另一些人则将其与 LLM 对更广泛教育带来的挑战相类比。

**标签**: `#AI`, `#CTF`, `#cybersecurity`, `#education`, `#community`

---

<a id="item-4"></a>
## [DeepSeek-V4-Flash 重燃 LLM 操控兴趣](https://www.seangoedecke.com/steering-vectors/) ⭐️ 8.0/10

DeepSeek-V4-Flash 重新点燃了人们对 LLM 操控向量的兴趣，像 DwarfStar 4 这样的项目展示了其能够有效移除拒绝行为并实现新的交互工作流。 这一发展使 LLM 操控再次变得实用，允许用户解除模型审查并探索新颖的用户界面，这可能使 AI 定制民主化并挑战安全对齐规范。 根据 antirez 的说法，操控技术可以通过识别并中和单一的拒绝方向来完全移除 DeepSeek-V4-Flash 的拒绝行为。然而，有效使用需要精心设计的数据集并理解操控功能。

hackernews · Brajeshwar · May 16, 14:58 · [社区讨论](https://news.ycombinator.com/item?id=48160807)

**背景**: LLM 操控向量是模型潜在空间中控制特定行为（如拒绝或政治偏见）的方向，无需重新训练。早期研究发现，LLM 中的拒绝行为通常由单一方向介导，因此可通过操控移除。DeepSeek-V4-Flash 是最近重新激发这一技术兴趣的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bobrupakroy.medium.com/steering-large-language-models-with-activation-vectors-a-practical-guide-45866b3697ac">Steering Large Language Models with Activation Vectors ... | Medium</a></li>
<li><a href="https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction">Refusal in LLMs is mediated by a single... — AI Alignment Forum</a></li>
<li><a href="https://www.lesswrong.com/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms">A Sober Look at Steering Vectors for LLMs — LessWrong</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了移除拒绝行为（abliteration）和新 UI 工作流的潜力，antirez 澄清 DwarfStar 4 是其自己的项目，而非精简版的 llama.cpp。一些人指出操控向量在实践中的应用尚未被充分探索。

**标签**: `#LLM`, `#steering vectors`, `#DeepSeek`, `#AI safety`, `#uncensoring`

---

<a id="item-5"></a>
## [谷歌将操纵 AI 搜索结果列为垃圾内容](https://www.theverge.com/tech/931416/google-ai-search-spam-policy) ⭐️ 8.0/10

谷歌更新了搜索垃圾内容政策，明确禁止操纵生成式 AI 搜索回应，涵盖 AI Overview 和 AI Mode，并将此类手法与传统搜索排名操纵同等对待。 该政策直接针对新兴的生成式引擎优化（GEO）实践，标志着执法方式的重大转变，影响依赖 AI 搜索可见性的 SEO 专业人士和内容创作者。 违规网站可能被降权或完全从搜索结果中移除。常见的 GEO 手法包括批量生成偏向性的“最佳推荐”内容，或在网页中埋入提示语以诱导 AI 模型将某个站点视为权威来源。

telegram · zaihuapd · May 16, 06:31

**背景**: 生成式引擎优化（GEO）是指优化内容以出现在 ChatGPT、Perplexity 和谷歌 AI Overview 等 AI 驱动搜索引擎中的做法。随着用户越来越依赖 AI 生成的答案，企业试图操纵这些系统，促使谷歌更新其长期以来的垃圾内容政策以涵盖 AI 特定的操纵行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://foundingengine.com/ai-search/">AI Search Optimization ( GEO ) — Founding Engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google`, `#AI search`, `#spam policy`, `#GEO`, `#SEO`

---

<a id="item-6"></a>
## [GitHub Copilot 桌面应用进入技术预览](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) ⭐️ 8.0/10

GitHub Copilot 桌面应用现已进入技术预览，开发者可以从 issue、PR、提示词或历史会话启动隔离的开发会话，在应用内查看差异、运行测试、创建 PR，并使用 Agent Merge 自动处理 review 评论和合并。 该应用将代理驱动开发带入专用桌面环境，简化了整个 PR 生命周期，减少了开发者的上下文切换。这标志着向完全 AI 辅助编码工作流迈出了重要一步。 Copilot Pro 和 Pro+ 订阅者可立即申请抢先体验；Business 和 Enterprise 用户将在本周内陆续开放访问，但组织管理员需在策略中开启预览和 CLI 权限。该应用支持同时运行多个隔离的代理会话，每个会话都有自己的分支。

telegram · zaihuapd · May 16, 15:07

**背景**: GitHub Copilot 是一个 AI 驱动的代码补全和辅助工具。新的桌面应用将 Copilot 的能力扩展到 IDE 集成之外，提供了一个独立的代理开发环境。Agent Merge 是一项自动解决合并冲突和处理 PR review 评论的功能，此前作为云代理功能引入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/">GitHub Copilot app is now available in technical preview</a></li>
<li><a href="https://docs.github.com/en/copilot/concepts/agents/github-copilot-app">About the GitHub Copilot app</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions">Working with agent sessions in the GitHub Copilot app</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#AI-assisted development`, `#developer tools`, `#technical preview`

---