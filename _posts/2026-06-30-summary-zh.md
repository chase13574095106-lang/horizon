---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> From 31 items, 7 important content pieces were selected

---

1. [Anthropic 发布 Claude Sonnet 5，增强智能体能力](#item-1) ⭐️ 8.0/10
2. [Claude Code 在请求中嵌入隐写标记](#item-2) ⭐️ 8.0/10
3. [Anthropic 推出 Claude Science 用于安全数据科学](#item-3) ⭐️ 8.0/10
4. [最高法院：获取手机位置数据须凭搜查令](#item-4) ⭐️ 8.0/10
5. [华为开源盘古 2.0 模型，参数规模达 505B](#item-5) ⭐️ 8.0/10
6. [Anthropic 获准恢复 Mythos 5 在关键基础设施的部署](#item-6) ⭐️ 8.0/10
7. [Anthropic 发布 Claude Sonnet 4.6，性能大幅提升](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Sonnet 5，增强智能体能力](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Sonnet 5，这是一个更快、能力更强的模型，具有改进的智能体能力，包括更好的指令遵循和自主工具使用。它在 OSWorld-Verified 上达到 88.3%，超过了人类专家基线 72.4%。 此次发布使先进的智能体能力更易获得且更具成本效益，使开发者能够以低于 Opus 级别模型的推理成本构建自主智能体。同时，它在智能体场景中表现出更高的安全性，减少了不良行为。 Sonnet 5 在智能体编码基准上得分为 63.2%，而 Opus 4.8 为 69.2%，Sonnet 4.6 为 58.1%。然而，社区基准显示它在常识、组合工具调用任务和谜题解决方面存在弱点，并且在较高努力水平下，其每任务成本可能超过 Opus。

hackernews · marinesebastian · Jun 30, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: Claude Sonnet 是 Anthropic 的中端模型系列，介于更快的 Haiku 和更强大的 Opus 之间。智能体 AI 指能够自主规划、使用工具和执行多步骤任务的模型。Sonnet 5 旨在以更低成本提供接近 Opus 的推理能力，适用于生产环境中的智能体工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/">Anthropic launches Claude Sonnet 5 as a cheaper way to run agents | TechCrunch</a></li>
<li><a href="https://dev.to/best_codes/anthropic-just-dropped-claude-sonnet-5-and-the-benchmarks-are-kind-of-insane-3ppc">Anthropic just dropped Claude Sonnet 5, and the benchmarks are kind of insane - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：一些用户称赞 Sonnet 5 在指令遵循和一次性复杂任务执行方面的改进，而另一些用户指出，在中高努力水平下，其每任务成本可能高于 Opus，使 Opus 更具性价比。此外，还有对常识和工具调用任务弱点的担忧。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#agentic`

---

<a id="item-2"></a>
## [Claude Code 在请求中嵌入隐写标记](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

一位安全研究人员发现，Anthropic 的 Claude Code 工具在其 API 请求中嵌入了隐藏的隐写标记，这些标记基于用户的 API 基础 URL 和时区，且未进行透明披露。 这种做法引发了关于用户同意和信任的严重担忧，因为它在用户机器上运行了用户合理预期之外的代码，可能违反 CFAA 等法律框架。 这些标记基于 API 基础 URL 和时区，且隐写技术实现得较为粗糙，可通过逆向工程检测。其意图似乎是识别进行模型蒸馏的中国公司的使用情况。

hackernews · kirushik · Jun 30, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是一种将消息隐藏在非秘密数据（如文本或图像）中的做法。在此背景下，Claude Code 是一个在用户本地机器上运行并向 Anthropic API 发送请求的 AI 编码助手。这些隐藏标记在用户不知情的情况下被嵌入到发送给 API 的提示中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thereallo.dev/blog/claude-code-prompt-steganography">Claude Code Is Steganographically Marking Requests</a></li>
<li><a href="https://arxiv.org/abs/2505.03439">[2505.03439] The Steganographic Potentials of Language Models</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人淡化其严重性，认为意图（防止中国公司进行模型蒸馏）是明确的，而另一些人则强调缺乏透明度以及可能违反 CFAA 的法律问题。还有人批评其实现粗糙，指出更巧妙的隐蔽技术本可避免被检测到。

**标签**: `#AI`, `#privacy`, `#security`, `#steganography`, `#ethics`

---

<a id="item-3"></a>
## [Anthropic 推出 Claude Science 用于安全数据科学](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 发布了 Claude Science，这是一个基于本地服务器的数据科学工具，集成了高性能计算（HPC）集群和数据库，专为制药等安全研究环境设计。 该工具使受限环境中的研究人员能够在不影响安全性的情况下利用 AI 进行数据分析，可能加速药物发现和科学研究。 Claude Science 运行一个带有 Web 界面的本地服务器，支持与机构集群和数据库集成，并生成可审计的工件以确保可重复性。

hackernews · lebovic · Jun 30, 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 在制药等受监管行业，数据科学通常需要在隔离或锁定系统上处理敏感数据。传统的基于云的 AI 工具无法在此类环境中使用。Claude Science 通过本地运行同时提供强大的 AI 辅助分析来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists, is now available</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>
<li><a href="https://grokipedia.com/page/Claude_for_Life_Sciences">Claude for Life Sciences</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，Claude Science 不仅仅是一个绘图工具；它与 HPC 集群和数据库集成，使其对实际研究有价值。一些用户在 RNAi 生物农药设计等特定任务上进行了测试，认为其表现尚可，但存在使用哺乳动物设计规则等局限性。

**标签**: `#AI`, `#data science`, `#Anthropic`, `#research tools`, `#HPC`

---

<a id="item-4"></a>
## [最高法院：获取手机位置数据须凭搜查令](https://www.androidpolice.com/supreme-court-protects-your-cell-phone-location-data-after-googles-role-in-a-conviction/) ⭐️ 8.0/10

美国最高法院以 6 比 3 裁定，警方必须获得搜查令才能获取由 Google 等第三方公司持有的手机位置数据，将第四修正案保护扩展至此类数据。 这一里程碑式的裁决显著加强了数字隐私权，要求执法部门在向科技公司索取位置数据时满足更高的法律标准，影响数百万用户及未来的调查方式。 该案源于 2019 年一起银行劫案，警方使用“地理围栏令”要求 Google 提供特定区域内的用户数据；Google 从数百万用户中筛选出 19 个匿名账户，并最终锁定三人身份，其中包括一名嫌犯。

telegram · zaihuapd · Jun 30, 04:00

**背景**: 第四修正案保护公民免受不合理搜查和扣押，但此前根据“第三方原则”，警方无需搜查令即可获取第三方持有的记录。该裁决推翻了这一原则对手机位置数据的适用，承认个人对其数字行踪享有合理的隐私期待。

**标签**: `#privacy`, `#supreme court`, `#digital rights`, `#law enforcement`, `#fourth amendment`

---

<a id="item-5"></a>
## [华为开源盘古 2.0 模型，参数规模达 505B](https://t.me/zaihuapd/42259) ⭐️ 8.0/10

在华为开发者大会 2026 上，华为宣布开源盘古 openPangu 2.0 模型，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，支持 512K 上下文窗口。该模型针对昇腾 AI 芯片和鸿蒙系统进行了优化，计划从 6 月 30 日起陆续开源七大组件。 此次发布标志着大规模 AI 模型民主化的重要一步，华为开源了 505B 参数的模型，可能加速中国乃至全球的 AI 应用。同时，它巩固了华为在 AI 生态系统中的地位，挑战其他主要参与者，并促进其昇腾硬件平台上的创新。 盘古 2.0 模型支持 512K token 的上下文窗口，能够处理超长文档。开源版本包括预训练代码、模型权重等组件，首批将于 6 月 30 日发布。余承东指出，华为的算力大量用于支持国内其他企业，自身留用的数量有限。

telegram · zaihuapd · Jun 30, 06:01

**背景**: 大型语言模型（LLM）如盘古，是在海量文本数据上训练的人工智能系统，能够生成类似人类的文本。开源此类模型允许全球开发者使用、修改和改进它们，促进合作与创新。华为的盘古系列早在全球 AI 热潮之前就已开始研发，此次发布旨在使其成为领先的开源模型。

**标签**: `#AI`, `#open-source`, `#Huawei`, `#large language model`, `#Pangu`

---

<a id="item-6"></a>
## [Anthropic 获准恢复 Mythos 5 在关键基础设施的部署](https://t.me/zaihuapd/42260) ⭐️ 8.0/10

Anthropic 已重新获得美国政府批准，自 2024 年 6 月 27 日起，可将其最强的网络安全模型 Mythos 5 部署给运营和保卫关键基础设施的组织。 这一决定标志着美国政府政策转向允许先进 AI 模型用于关键基础设施保护，在安全效益与监管监督之间取得平衡。 该批准目前仅涵盖 Mythos 5，不包括 Fable 5 模型，且仅限于特定组织；Anthropic 继续谈判以扩大访问范围。

telegram · zaihuapd · Jun 30, 07:04

**背景**: Anthropic 是一家专注于 AI 安全的公司，开发大型语言模型。Mythos 5 是其最先进的网络安全模型，旨在检测和响应威胁。美国政府此前因安全担忧限制了其部署。

**标签**: `#AI`, `#cybersecurity`, `#government regulation`, `#critical infrastructure`, `#Anthropic`

---

<a id="item-7"></a>
## [Anthropic 发布 Claude Sonnet 4.6，性能大幅提升](https://t.me/zaihuapd/42277) ⭐️ 8.0/10

Anthropic 发布了 Claude Sonnet 4.6 模型，在编程、计算机操作及长文本推理方面实现全面升级，现已作为 Free 和 Pro 用户的默认版本，并提供 1M token 上下文窗口。 此次更新增强了 Claude 对开发者和高级用户的实用性，特别是在复杂编程和自动化计算机任务方面，有望提高生产力并促进在企业环境中的采用。 该模型在 OSWorld 计算机使用评测中取得显著进步，已通过 API 及主流云平台同步上线，定价与前代保持一致。

telegram · zaihuapd · Jun 30, 17:58

**背景**: Claude Sonnet 是 Anthropic 的中端模型，在性能与成本之间取得平衡。4.6 版本专注于编程和计算机交互方面的实用改进，这些领域对 AI 辅助软件开发和自动化至关重要。

**标签**: `#Anthropic`, `#Claude`, `#AI model`, `#coding`, `#computer use`

---