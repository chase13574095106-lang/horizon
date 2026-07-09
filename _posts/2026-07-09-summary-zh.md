---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> From 36 items, 11 important content pieces were selected

---

1. [OpenAI 发布 GPT-5.6，提供三种模型尺寸](#item-1) ⭐️ 9.0/10
2. [欧盟议会通过程序性投票批准聊天控制 1.0](#item-2) ⭐️ 9.0/10
3. [Bun 从 Zig 重写为 Rust](#item-3) ⭐️ 9.0/10
4. [TypeScript 7.0 正式发布：Go 重写带来最高 12 倍速度提升](#item-4) ⭐️ 9.0/10
5. [蚂蚁集团开源全球首个 MoE 具身视频基模 LingBot-Video](#item-5) ⭐️ 9.0/10
6. [用 Rust 重写的 Postgres 通过全部回归测试](#item-6) ⭐️ 8.0/10
7. [Meta 发布 Muse Spark 1.1 智能体 AI 模型](#item-7) ⭐️ 8.0/10
8. [OpenAI 为 ChatGPT 语音模式推出 GPT-Live](#item-8) ⭐️ 8.0/10
9. [大疆 EV50 垂直起降运载无人机飞越珠峰 8861 米](#item-9) ⭐️ 8.0/10
10. [国家超算互联网核心节点在郑州上线](#item-10) ⭐️ 8.0/10
11. [OpenAI 与美国战争部拟禁止 AI 用于国内监控](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-5.6，提供三种模型尺寸](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI 发布了 GPT-5.6，这是一款新的前沿模型，提供 Luna、Terra 和 Sol 三种尺寸。它在 ARC-AGI-3 基准测试上取得了最先进的结果，并引入了改进的意图理解能力。 GPT-5.6 在 ARC-AGI-3（一个旨在衡量 AI 智能体类人推理能力的基准测试）上取得了新的最先进水平，标志着向更通用智能迈出了重要一步。其改进的意图理解能力使模型能更好地推断用户目标，减少了对明确分步指令的需求。 三种模型尺寸的定价为每百万 token：Luna $1/$6，Terra $2.50/$15，Sol $5/$30。Sol 是首个通过验证的、在 ARC-AGI-3 游戏中获胜的前沿模型，得分为 7.8%。所有模型的知识截止日期为 2026 年 2 月 16 日。

hackernews · logickkk1 · Jul 9, 17:04 · [社区讨论](https://news.ycombinator.com/item?id=48849066)

**背景**: ARC-AGI-3 是一个交互式推理基准测试，挑战 AI 智能体探索新环境、推断目标并规划行动，以衡量类人智能。意图理解是指 AI 从用户查询中推断其潜在目标的能力，从而实现更自然的交互。GPT-5.6 在此方面的改进使其能更好地处理模糊请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>
<li><a href="https://arcprize.org/competitions/2026/arc-agi-3">ARC Prize 2026 - ARC-AGI-3 Competition</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了 GPT-5.6 在 ARC-AGI-3 上的 SOTA 表现及其意图理解能力。一些用户讨论了模型比较（例如 Codex 与 Claude Code），并指出 OpenAI 在某些基准测试中省略了 Fable 5，因为它拒绝回答高级生物学问题。还有一种情绪是，尽管 OpenAI 不开放，但许多人希望它胜过 Anthropic。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#GPT-5.6`, `#ARC-AGI`

---

<a id="item-2"></a>
## [欧盟议会通过程序性投票批准聊天控制 1.0](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

2026 年 7 月 9 日，欧盟议会通过了聊天控制 1.0，允许在 Instagram、Discord 和 Gmail 等平台上无证扫描私人消息，有效期至 2028 年，尽管投票的欧洲议会议员多数反对（314 票反对，276 票赞成，17 票弃权）。该措施之所以通过，是因为否决动议未能获得所需的 361 票绝对多数。 这项立法严重削弱了欧盟的数字隐私和加密保护，为大规模监控私人通信开创了先例。它影响数百万用户，可能削弱对数字平台的信任，同时也会影响关于平衡儿童保护与公民自由的更广泛辩论。 投票在暑假前的最后一天进行，有 113 名欧洲议会议员缺席，并使用了程序性规则，要求全体议员的绝对多数（361 票）才能否决该措施，而非投票者的简单多数。扫描适用于未加密平台上的直接消息，而公开帖子和云存储不受该特定法律影响。

hackernews · rapnie · Jul 9, 11:03 · [社区讨论](https://news.ycombinator.com/item?id=48843923)

**背景**: 聊天控制是指欧盟旨在打击在线儿童性虐待材料的一系列法规。聊天控制 1.0 最初于 2022 年提出，允许科技公司在没有搜查令的情况下自愿扫描私人消息。该法规在 2026 年 3 月曾被两次否决，但通过程序性投票得以复活。批评者认为它侵犯了隐私和加密权利，而支持者则声称保护儿童是必要的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm">EU Parliament Passes Chat Control by Default: 314 MEPs Couldn ...</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一议会操作表示愤怒，称其不民主，是迈向极权主义的一步。许多人强调了要求绝对多数才能否决法律的程序性把戏，以及投票时间安排在暑假前以尽量减少出席人数。一些人指出，这可能会唤醒人们关注欧盟治理中的结构性问题。

**标签**: `#privacy`, `#surveillance`, `#EU legislation`, `#encryption`, `#digital rights`

---

<a id="item-3"></a>
## [Bun 从 Zig 重写为 Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner 宣布将 Bun JavaScript 运行时从 Zig 重写为 Rust，主要动机是内存安全和减少错误。重写工作借助前沿 AI 模型驱动的先进智能体工程工作流，在 11 天内完成。 这表明借助 AI 辅助，对关键基础设施进行大规模重写现在变得可行，挑战了长期以来“永远不要重写”的信念。同时也凸显了 Rust 因其内存安全保证在系统编程领域日益增长的主导地位。 重写估计花费了 16.5 万美元的 API 代币（59 亿未缓存输入代币、6.9 亿输出代币）。基于 Rust 的新版 Bun 自 2026 年 6 月 17 日起已在 Claude Code 中上线，Linux 上启动速度提升 10%。

rss · Simon Willison · Jul 8, 23:57

**背景**: Bun 是一个 JavaScript 运行时、包管理器和测试运行器，旨在作为 Node.js 的直接替代品，最初用 Zig 编写。重写得以实现得益于一个包含百万断言的 TypeScript 一致性测试套件，使 AI 智能体能够自动化移植过程。智能体工作流涉及自主 AI 智能体，它们能在最少人工干预下做出决策并协调任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-workflows">What are agentic workflows? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**标签**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-4"></a>
## [TypeScript 7.0 正式发布：Go 重写带来最高 12 倍速度提升](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

微软正式发布了 TypeScript 7.0，该版本用 Go 语言重写了编译器，完整构建速度比旧版快 8 到 12 倍，并支持共享内存多线程。用户可通过 npm 直接安装，编辑器也可通过 LSP 使用新的语言服务器。 此版本代表了 TypeScript 的范式转变，通过将类型检查和构建时间降低一个数量级，大幅提升了开发者的生产力。同时，它也展示了 Go 在构建高性能开发者工具方面的可行性，可能影响未来的语言基础设施。 TypeScript 7.0 引入了实验性的 --checkers 和 --builders 参数以自定义并行度，并提供了兼容包以便与 TypeScript 6 共存。但 Vue、Svelte 等嵌入式语言的工具链尚未就绪，目前仍需使用旧版本。

telegram · zaihuapd · Jul 9, 04:01

**背景**: TypeScript 是 JavaScript 的类型超集，可编译为纯 JavaScript，广泛用于大规模 Web 开发。之前的编译器是用 TypeScript 自身（自举）编写并在 JavaScript 上运行，这限制了性能。语言服务器协议（LSP）标准化了编辑器与语言服务器之间的通信，使得跨不同 IDE 的代码补全和错误检查等功能成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/">Announcing TypeScript 7.0 - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler ...</a></li>

</ul>
</details>

**社区讨论**: 社区对性能提升表达了强烈的热情，许多开发者指出 10 倍加速将显著改善他们的工作流程。一些人对 Vue 和 Svelte 工具链缺乏支持表示担忧，但总体情绪非常积极。

**标签**: `#TypeScript`, `#Microsoft`, `#Programming Languages`, `#Performance`, `#Open Source`

---

<a id="item-5"></a>
## [蚂蚁集团开源全球首个 MoE 具身视频基模 LingBot-Video](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

蚂蚁集团开源了全球首个基于混合专家（MoE）架构的具身智能视频生成基础模型 LingBot-Video。该模型在机器人操作评测基准 RBench 上取得了最先进性能，超越了 Wan2.6、Seedance1.5 Pro 和 Cosmos3 Super 等模型。 这一突破显著提升了具身 AI 视频生成的效率，每次推理仅激活约 30 亿参数（总参数 300 亿），推理速度约为同等规模稠密模型的 3 倍。以 Apache 2.0 许可证开源发布，加速了机器人动作预测、仿真数据生成和世界模型等方向的研究。 LingBot-Video 采用 DiT+MoE 架构以平衡容量与成本，并在包含 7 万小时具身数据的自研画像引擎上训练，覆盖灵巧操作、机器人移动和第一视角交互。它还引入了多维强化学习奖励系统，除美学和运动一致性外，重点关注物理合理性和任务完成度。

telegram · zaihuapd · Jul 9, 04:30

**背景**: 混合专家（MoE）是一种 AI 架构，使用多个专门的子模型（专家）选择性激活，从而在降低推理成本的同时实现更大的总参数量。具身 AI 视频基础模型根据机器人动作或观察生成视频，作为规划与仿真的世界模型。DiT（扩散 Transformer）是一种流行的视频生成骨干网络，结合了扩散模型与 Transformer 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? - NVIDIA</a></li>
<li><a href="https://www.emergentmind.com/topics/video-diffusion-transformer-dit">Video Diffusion Transformer (DiT) Overview</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#MoE`, `#video generation`, `#robotics`, `#open source`

---

<a id="item-6"></a>
## [用 Rust 重写的 Postgres 通过全部回归测试](https://github.com/malisper/pgrust) ⭐️ 8.0/10

一个名为 pgrust 的实验性项目利用大语言模型将 PostgreSQL 数据库用 Rust 重写，并成功通过了官方 Postgres 回归测试的全部测试用例。 这展示了 LLM 执行大规模代码重写的潜力，引发了关于 AI 在软件工程中角色以及用内存安全语言重写关键基础设施可行性的讨论。 该项目在不到一个月内生成了 7,101 次提交，使得传统代码审查变得不切实际。重写后的代码采用 AGPL 许可证，与 PostgreSQL 原始许可证不同。

hackernews · SweetSoftPillow · Jul 9, 06:18 · [社区讨论](https://news.ycombinator.com/item?id=48841676)

**背景**: PostgreSQL 是一个有 30 年历史的开源关系型数据库，拥有全面的回归测试套件。Rust 是一种以内存安全著称的系统编程语言。LLM（大语言模型）是能够根据提示生成和转换代码的 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/regress.html">PostgreSQL: Documentation: 18: Chapter 31. Regression Tests</a></li>
<li><a href="https://www.postgresql.org/docs/current/regress-run.html">PostgreSQL: Documentation: 18: 31.1. Running the Tests</a></li>
<li><a href="https://arxiv.org/abs/2410.08806">[2410.08806] Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了由于 AI 生成的大量提交导致代码审查不可行的问题、许可证兼容性问题（AGPL 与原始 PostgreSQL 许可证），以及对关键软件信任 AI 重写的普遍怀疑。有人建议通过镜像生产查询来比较行为。

**标签**: `#PostgreSQL`, `#Rust`, `#LLM`, `#Database`, `#AI-assisted programming`

---

<a id="item-7"></a>
## [Meta 发布 Muse Spark 1.1 智能体 AI 模型](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.1，这是一个专为智能体任务设计的多模态推理模型，拥有 100 万 token 的上下文窗口，并在工具使用、计算机使用、编程和多模态理解方面有所改进。该模型通过 Meta Model API 提供商业定价，输入/输出每 100 万 token 分别为 1.25 美元和 4.5 美元，缓存输入为 0.15 美元。 此次发布标志着 Meta 进入商业智能体 AI 市场，以有竞争力的定价和开放权重挑战 OpenAI 和 Anthropic。关于基准测试有效性和开源策略的争论可能会影响 AI 社区评估和采用智能体模型的方式。 该模型在 Terminal-Bench 2.1 上进行了评估，但社区评论指出评估使用了 6 个 CPU 核心和 8GB 内存，这可能超出任务的资源限制并使结果无效。该模型还在 Meta AI 应用和 meta.ai 上支持“思考”模式。

hackernews · ot · Jul 9, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48846184)

**背景**: 智能体 AI 模型旨在自主使用工具、代码和计算机交互来执行任务，超越简单的文本生成。Meta 的 Muse Spark 系列是其开发前沿 AI 能力同时保持开源策略的一部分，尽管 Muse Spark 1.1 以商业 API 形式提供并定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/">Introducing Muse Spark 1.1</a></li>
<li><a href="https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report">Muse Spark 1.1 Evaluation Report</a></li>
<li><a href="https://www.datacamp.com/blog/muse-spark-1-1">Muse Spark 1.1: Meta's Agentic Model and API | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 社区评论对基准测试方法表示担忧，一位用户认为评估中使用的资源上限违反了 Terminal-Bench 2.1 规则。另一位用户分享了用于 LLM 的实用集成插件，而其他人则讨论了 Meta 的定价策略和开源角色，一些人称赞低成本，另一些人则对实际性能表示怀疑。

**标签**: `#AI`, `#Meta`, `#agentic model`, `#open source`, `#benchmarking`

---

<a id="item-8"></a>
## [OpenAI 为 ChatGPT 语音模式推出 GPT-Live](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI 用 GPT-Live 升级了 ChatGPT 的语音模式，新模型能在后台将复杂任务委托给 GPT-5.5，同时保持对话流畅。 此次升级通过实时委托繁重任务，显著提升了 ChatGPT 语音模式的实用性，使其成为更强大的头脑风暴伙伴和助手。 GPT-Live 采用全双工架构，可同时听和说，并在 GPT-5.5 处理委托任务时继续对话。之前的语音模式基于较旧的 GPT-4o 模型，知识截止于 2024 年。

rss · Simon Willison · Jul 8, 23:20

**背景**: ChatGPT 语音模式允许用户与 ChatGPT 对话并听到语音回复。GPT-5.5 是 OpenAI 于 2026 年 4 月发布的最新前沿模型，在编程、研究和数据分析方面表现强劲。GPT-Live 旨在让语音对话更自然、更智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT‑5.5 - OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-live">GPT-Live System Card - OpenAI Deployment Safety Hub</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-Live`, `#ChatGPT`, `#voice mode`, `#AI`

---

<a id="item-9"></a>
## [大疆 EV50 垂直起降运载无人机飞越珠峰 8861 米](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

大疆尚未发布的 EV50 垂直起降运载无人机在“巅峰使命”珠峰科考中成功飞越 8861 米高度，创下同类公开测试中的最高飞行升限纪录。 这一成就展示了垂直起降运载无人机的极端海拔能力，为高海拔物流和科学研究开辟了道路，同时也彰显了大疆在无人机设计和恶劣环境可靠性方面的技术领先地位。 EV50 是一款复合翼垂直起降无人机，可原地垂直起降并切换至固定翼巡航。在为期 12 天的任务中，它累计完成 32 架次起降，连续爬升 3730 米，返程时仍剩 30%电量。

telegram · zaihuapd · Jul 9, 06:00

**背景**: 垂直起降（VTOL）无人机结合了多旋翼的垂直升力能力和固定翼的高效巡航能力。复合翼无人机是一种 VTOL 类型，使用独立的旋翼提供升力，固定翼用于前飞，从而实现更长的航程和续航。大疆是领先的无人机制造商，EV50 是其首款专为长途物流设计的垂直起降运载无人机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260709A0AKS300">大疆发布首款垂直起降运载无人机DJI EV50：航程150公里 最大载重50千...</a></li>
<li><a href="https://baike.baidu.com/item/复合翼无人机/67152229">复合翼无人机_百度百科</a></li>
<li><a href="https://zh.wikipedia.org/wiki/垂直起降">垂直起降 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#drones`, `#DJI`, `#VTOL`, `#record`, `#logistics`

---

<a id="item-10"></a>
## [国家超算互联网核心节点在郑州上线](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

2026 年 7 月 9 日，国家超算互联网核心节点在郑州正式上线，可提供超过 10 万张国产 AI 算力卡。这是该平台上线以来接入的最大规模单体国产 AI 算力资源池。 这一里程碑显著提升了中国在 AI 计算基础设施上的自主可控能力，使得大规模 AI 模型训练和科学计算不再依赖外国芯片。它强化了全国计算资源调度体系，并支持各行各业的数字化转型。 该核心节点是一个单体十万卡全精度算力资源池，可同时支撑十万亿级参数大模型训练、AI for Science（AI4S）以及超大规模科学工程计算。目前已完成 400 余个主流大模型及世界模型的适配优化。

telegram · zaihuapd · Jul 9, 07:00

**背景**: 国家超算互联网由科技部发起，连接了全国 14 个省市超过 30 家国家级超算中心和智算中心，旨在打破单个算力中心的孤立运营模式，构建一体化算力服务平台。国产 AI 算力卡由华为、寒武纪、昆仑芯等公司生产，到 2026 年已从“能用”进入“好用”阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网核心节点/63648019">国家超算互联网核心节点_百度百科 超算互联网 - scnet.cn 国家超算互联网核心节点正式上线：可提供超过10万卡国产AI算力 国家超算互联网核心节点正式上线！_新浪科技_新浪网 国家超算互联网核心节点正式上线|运营|人工智能|工业互联网平台_网易... Top Stories</a></li>
<li><a href="https://baike.baidu.com/item/国产算力卡/67727675">国产算力卡_百度百科</a></li>

</ul>
</details>

**标签**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#AI chips`

---

<a id="item-11"></a>
## [OpenAI 与美国战争部拟禁止 AI 用于国内监控](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI 与美国战争部已同意修订双方的 AI 合作协议，增加明确禁止将 AI 系统用于对美国公民进行国内监控的条款。该修订由 OpenAI 首席执行官 Sam Altman 主动提出，以回应公众对大规模监控的担忧。 这一由领先 AI 公司采取的主动措施为军事领域的 AI 伦理部署树立了先例，并可能影响未来的 AI 治理政策。它直接回应了公民自由方面的担忧，并可能影响其他科技公司如何处理与国防机构的合同。 修订后的条款明确禁止对美国公民进行蓄意监控，并禁止利用商业获取的个人身份信息进行追踪或监测。该合同尚未正式签署，此举之前，Anthropic 与战争部的协议曾因类似争议而中止。

telegram · zaihuapd · Jul 9, 13:22

**背景**: 2025 年，美国国防部与包括 OpenAI 和 Anthropic 在内的多家 AI 公司签订合同，以加速 AI 在国家安全领域的应用。然而，关于 AI 被用于大规模国内监控和自主武器的担忧引发了公众反弹和内部争论。Anthropic 的合同因对其 AI 模型军事用途的争议而被中止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-agreement-with-the-department-of-war/">Our agreement with the Department of War - OpenAI</a></li>
<li><a href="https://tech-insider.org/openai-pentagon-military-ai-deal-2026/">OpenAI Pentagon Deal: 4 Controversial Terms [2026]</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#OpenAI`, `#military AI`, `#surveillance`, `#policy`

---