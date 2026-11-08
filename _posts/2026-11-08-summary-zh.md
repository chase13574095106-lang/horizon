---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> From 33 items, 6 important content pieces were selected

---

1. [MaxxBench 通过变异编码任务质疑 DeepSWE 分数](#item-1) ⭐️ 8.0/10
2. [浏览器版《极品飞车：地下狂飙 2》在线多人游戏发布](#item-2) ⭐️ 8.0/10
3. [自 2022 年起，每台 Mac 都运行着未记录的个人知识图谱守护进程](#item-3) ⭐️ 8.0/10
4. [Asahi Linux 进展报告 7.3：Fedora Asahi Remix 同日发布与许可挑战](#item-4) ⭐️ 8.0/10
5. [甲骨文迫于美国压力取消与腾讯 70 亿美元 AI 芯片租赁协议](#item-5) ⭐️ 8.0/10
6. [GitHub 新架构 Rubicon 每秒处理 7200 次推送](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MaxxBench 通过变异编码任务质疑 DeepSWE 分数](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 8.0/10

Unlap AI 推出的新基准 MaxxBench 对 89 个 DeepSWE 编码任务进行变异，通过修改指令或起始代码（例如要求小写文件名或 UTC 时间戳），同时将补丁增长的中位数控制在仅 17 行（3.5%）。它测试编码智能体是否能适应新要求，而不是依赖对原始基准的记忆或猜测答案。 这一批评引发了对 DeepSWE 分数有效性的担忧，该分数被广泛用于对编码智能体进行排名，并表明较小模型可能对存在缺陷或过于简单的评估环境过拟合。这对依赖基准声明来选择模型的 AI/ML 从业者以及设计 RL 训练环境的实验室都很重要。 MaxxBench 怀疑前沿模型可能在强化学习和后训练评估过程中发展出独特的基准感知模式，而评估工具中过度代表的设置——例如最大推理努力或 mini-swe-agent 仅 bash 的提示循环——可能触发该模式。该基准还指出 DeepSWE 本身包含错误，实际建议包括避免使用“最大模式”。

hackernews · antiuniverse · Nov 7, 17:19 · [社区讨论](https://news.ycombinator.com/item?id=50406222)

**背景**: DeepSWE 是一个评估基于 LLM 的编码智能体在软件工程任务上表现的基准，通常使用 pass@1 分数对模型进行排名。基准过拟合是指模型过度针对特定基准进行优化，而没有真正提升通用能力，这是 LLM 评估中的一个已知问题。MaxxBench 在此基础上创建 DeepSWE 任务的变体，以测试真正的适应能力而非记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maxxbench.unlap.ai/research/why-maxxbench/">Introducing MaxxBench: Benchmarking Task Adaptation and ...</a></li>
<li><a href="https://daily.dev/posts/maxxbench-nice-deepswe-score-but-is-it-true--ue9ulip60">MaxxBench – "Nice DeepSWE score. But is it true?"</a></li>
<li><a href="https://arxiv.org/html/2412.03597v1">The Vulnerability of Language Model Benchmarks: Do They ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为较小模型最容易对较简单的 RL 环境过拟合，peri-cl 指出名称中带“-flash”的模型下降最严重，而 rao-v 将问题归因于实验室在创建反映基准任务的 RL 环境时不够严谨。Systemerror7A69 因 DeepSWE 中的错误而对基准普遍持怀疑态度，antirez 则认为较小模型之所以表现不佳，是因为在基准变化中强先验被反转了。

**标签**: `#llm-benchmarks`, `#evaluation`, `#overfitting`, `#rl-environments`, `#ai-ml`

---

<a id="item-2"></a>
## [浏览器版《极品飞车：地下狂飙 2》在线多人游戏发布](https://nfsu2.xyz/) ⭐️ 8.0/10

一个基于浏览器的《极品飞车：地下狂飙 2》在线多人版本已在 nfsu2.xyz 发布，该项目通过逆向工程和 WebGPU 构建，目前正越来越受欢迎。 该项目展示了 WebGPU 在浏览器中运行完整 3D 游戏的潜力，并凸显了通过逆向工程进行游戏保存的日益增长的努力，引发了关于废弃软件和法律挑战的讨论。 该游戏完全在浏览器中使用 WebGPU 运行，在 Linux 上，用户需要在 Chromium 中启用不安全的 WebGPU 功能才能游玩。该网站的法律地位不确定，因为它托管受版权保护的内容，可能面临下架请求。

hackernews · fluxusars · Nov 7, 09:36 · [社区讨论](https://news.ycombinator.com/item?id=50403052)

**背景**: 《极品飞车：地下狂飙 2》是一款 2004 年的赛车游戏，已不再官方提供，通常被视为废弃软件。WebGPU 是一种现代 Web API，允许在浏览器中高效利用 GPU 进行图形和计算。逆向工程涉及分析游戏代码以重新创建或适配到新平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>
<li><a href="https://github.com/yugecin/nfsu2-re">GitHub - yugecin/nfsu2-re: hobby reverse engineering project ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Abandonware">Abandonware - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术成就和怀旧体验印象深刻，但对网站的合法性及可能被下架表示担忧。一些人对为受版权保护的内容 soliciting 捐款提出质疑，而另一些人则希望由于游戏已无法获取而让该项目保留。

**标签**: `#game preservation`, `#reverse engineering`, `#WebGPU`, `#abandonware`, `#browser gaming`

---

<a id="item-3"></a>
## [自 2022 年起，每台 Mac 都运行着未记录的个人知识图谱守护进程](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 8.0/10

一项新分析揭示，自 macOS 13（2022 年）起，每台 Mac 都附带两个未记录的守护进程——knowledgeconstructiond 和 intelligenceplatformd，它们会构建关于用户、其联系人及其行为的个人知识图谱。这些数据以 51 个明文 SQLite 数据库的形式存储在~/Library/IntelligencePlatform 中，受 TCC 完全磁盘访问权限保护。 这一发现引发了重大的隐私担忧，因为该系统在未经用户明确同意或公开文档说明的情况下持续收集并关联个人信息，可能为 Apple Intelligence 功能提供支持，但也创建了用户关系和活动的详细画像。它影响所有 Mac 用户，并可能削弱人们对苹果隐私承诺的信任。 知识图谱每天重建，并会忘记已删除的联系人，但底层模型和存储的三元组对用户仍不透明，仅有一份简短的手册页作为文档。这些守护进程在 Intel 和 Apple silicon Mac 上均运行，旨在为未来的 Apple Intelligence 语言模型提供上下文。

hackernews · infwhispers · Nov 7, 09:46 · [社区讨论](https://news.ycombinator.com/item?id=50403097)

**背景**: Apple Intelligence 是苹果的一套 AI 功能，依赖设备端处理以保护隐私。个人知识图谱是实体（如人物、地点和事件）及其关系的结构化表示，用于为 AI 模型提供上下文。守护进程是 macOS 等类 Unix 系统中的后台进程。TCC（透明度、同意和控制）是 macOS 的隐私框架，要求应用在访问敏感数据时获得用户许可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://8rank.ai/game/apple-intelligence-personal-knowledge-graph">Anatomy of Apple's Personal Knowledge Graph — Eighth Rank</a></li>
<li><a href="https://techplanet.today/post/apples-hidden-personal-knowledge-graph-understanding-macoss-undocumented-family-classifier">Apple's Hidden Personal Knowledge Graph: Understanding macOS ...</a></li>
<li><a href="https://www.worldcybernews.com/articles/1884">macOS Builds Undocumented Personal Knowledge Graph Since ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了多种观点：一些人认为如果选择加入，数据收集可能有用，但对持续记录提出了社会担忧；另一些人鉴于照片应用的人脸识别等现有功能并不感到惊讶；还有人强调透明度和同意的必要性，并引用了史蒂夫·乔布斯过去关于隐私的言论。研究作者也加入讨论回答问题。

**标签**: `#privacy`, `#macOS`, `#Apple Intelligence`, `#knowledge-graph`, `#surveillance`

---

<a id="item-4"></a>
## [Asahi Linux 进展报告 7.3：Fedora Asahi Remix 同日发布与许可挑战](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 8.0/10

Asahi Linux 发布了进展报告 7.3，重点介绍了 Fedora Asahi Remix 于 11 月 3 日与 Fedora Linux 45 同日发布，这是该项目首次实现与上游 Fedora 的同步发布。报告还讨论了 Apple Silicon 的持续开发工作，以及多起试图利用项目宽松许可证劫持其成果的事件。 与上游 Fedora 实现同日发布显著提升了用户体验，能够及时提供更新和安全补丁，巩固了 Asahi Linux 作为 Apple Silicon Mac 上可行 Linux 选择的地位。许可问题引发了关于开源项目如何在保持宽松许可证的同时保护其成果的重要讨论。 报告指出，这是 Fedora Asahi Remix 首次与上游 Fedora 同日发布，是该项目的集成里程碑。报告还提到，项目面临多起试图利用其宽松许可证来取代项目并激进地将 Apple Silicon 上的 Linux 商业化的行为。

hackernews · ackyshake · Nov 7, 05:20 · [社区讨论](https://news.ycombinator.com/item?id=50401867)

**背景**: Asahi Linux 是一个由志愿者驱动的开源项目，通过逆向工程 SoC 将 Linux 内核及相关软件移植到 Apple Silicon Mac 上，因为苹果不提供官方文档。Fedora Asahi Remix 是 Asahi Linux 的旗舰发行版，基于 Fedora Linux，为 M1 和 M2 Mac 提供完善的 Linux 体验。该项目依赖 MIT 等宽松许可证，允许他人以较少限制使用和修改代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asahilinux.org/about/">About - Asahi Linux</a></li>
<li><a href="https://asahilinux.org/fedora/?pubDate=20251127">Fedora Asahi Remix - Asahi Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Fedora 同日发布表示高度赞赏，一位长期资助者称其为“令人欣喜的消息”。一个主要担忧是缺乏 USB-C 显示器支持，一位用户称这是其采用 Asahi Linux 的唯一障碍；另一位评论者质疑许可劫持尝试是否指 Omarchy 项目，并对 Asahi 的工作采用 MIT 而非 GPL 许可证表示惊讶。还有开发者宣传了自己的项目 Gravity Linux，声称支持 Vulkan 1.4 并在休眠到内存方面取得进展。

**标签**: `#Linux`, `#Apple Silicon`, `#Open Source`, `#Fedora`, `#Asahi Linux`

---

<a id="item-5"></a>
## [甲骨文迫于美国压力取消与腾讯 70 亿美元 AI 芯片租赁协议](https://t.me/zaihuapd/44975) ⭐️ 8.0/10

甲骨文取消了一项为期五年、价值约 70 亿美元的协议，该协议原计划通过其东南亚数据中心向腾讯出租约 10 万枚先进 AI 芯片。在美国官员向甲骨文表达担忧、公司承受特朗普政府压力后，交易被终止；腾讯此前已支付约 30%的首付款。 此次取消表明，美国出口管制正从直接的芯片销售延伸到云租赁安排，而中国企业此前正是通过这类安排获取受限硬件。这为任何可能规避管制的 AI 基础设施交易敲响了地缘政治警钟，将影响云服务商、中国 AI 开发者以及全球数据中心布局。 该租赁协议于今年早些时候签署，原计划让腾讯通过甲骨文在东南亚的多个数据中心获取约 10 万枚先进 AI 芯片，首付款约占 30%。这一安排被视为绕开美国出口管制的合法途径，而国会尚未堵上该漏洞；协议取消使腾讯的海外算力计划面临不确定性。

telegram · zaihuapd · Nov 7, 02:00

**背景**: 自 2022 年以来，美国对输往中国的先进 AI 芯片实施并不断收紧出口管制，禁止英伟达等公司向中国运送最先进的处理器。中国企业一直在寻找变通办法，包括从美国云服务商运营的海外数据中心租赁算力。甲骨文是美国主要的云和数据中心运营商，在东南亚拥有多处设施，因此成为这类安排的关键节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/tencent-oracle-ai-chips-lease-deal-100126">Tencent leases 100,000 AI chips from Oracle in $7 billion deal</a></li>
<li><a href="https://santageai.com/news/2026/10/02/tencent-oracle-100000-chips-7-billion">Tencent Leases 100,000 AI Chips From Oracle for $7 Billion</a></li>
<li><a href="https://www.globaltimes.cn/page/202611/1373811.shtml">China ‘isn't buying’ Nvidia chips . Why are some... - Global Times</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#Oracle`, `#Tencent`, `#geopolitics`

---

<a id="item-6"></a>
## [GitHub 新架构 Rubicon 每秒处理 7200 次推送](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub 推出了代号为 Rubicon 的新 Git 存储架构，在内部测试中支持 5000 个 AI 智能体同时协作操作单个仓库，每秒处理 7200 次推送，并保持较低的读取延迟。该架构将 Git 对象存入 Azure Blob Storage，由 Ref-CAS 管理引用状态，并使用虚拟副本处理读写操作和后台数据包压缩。 这是 Git 存储领域的一项重大工程突破，能够支持大规模并发，满足 AI 智能体向仓库推送这一新兴工作负载的需求。它可能重塑开发者平台处理智能体开发的方式，并为版本控制系统的可扩展性树立新标杆。 Rubicon 将存储与计算解耦，仅对引用更新施加顺序要求，Ref-CAS 使用由法定人数提交的比较并交换事务。该架构目前处于有限私有预览阶段，将逐步扩大推广范围。

telegram · zaihuapd · Nov 7, 14:12

**背景**: Git 传统上将对象存储在数据包文件中，并使用引用（分支、标签）指向提交。随着 AI 智能体日益自动化代码更改，仓库可能面临数千次并发写入，而传统的 Git 存储架构难以高效处理。GitHub 的 Rubicon 重新设计了存储，分离关注点并最小化协调，允许各组件独立扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub’s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://lumienai.com/news/github-project-rubicon-new-git-storage-architecture">GitHub’s “Project Rubicon”: A New Git Storage Built for…</a></li>
<li><a href="https://xiaohu.ai/en/article/github-rubicon-git-storage/">GitHub Rebuilds Git Storage for AI: Letting 5,000 Concurrent ...</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Git`, `#Storage Architecture`, `#AI Agents`, `#Scalability`

---