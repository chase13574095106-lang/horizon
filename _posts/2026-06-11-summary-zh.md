---
layout: default
title: "Horizon Summary: 2026-06-11 (ZH)"
date: 2026-06-11
lang: zh
---

> From 33 items, 13 important content pieces were selected

---

1. [AMD 拒绝修复严重 RCE 漏洞，改用 CRC-32](#item-1) ⭐️ 9.0/10
2. [Anthropic 撤销针对 Claude 研究人员的秘密限制政策](#item-2) ⭐️ 9.0/10
3. [Homebrew 6.0.0 发布，引入 Tap 信任机制和 Linux 沙箱](#item-3) ⭐️ 8.0/10
4. [小米开源 AI 编程助手 MiMo Code](#item-4) ⭐️ 8.0/10
5. [请愿书要求撤回加拿大 C-22 法案](#item-5) ⭐️ 8.0/10
6. [LLM 在 95%的兵棋推演中选择核升级](#item-6) ⭐️ 8.0/10
7. [代码行数是糟糕的生产力指标](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5：编码任务表现中等，存在缺陷](#item-8) ⭐️ 8.0/10
9. [美国太阳能发电量首次超越煤炭](#item-9) ⭐️ 8.0/10
10. [Android 17 强制应用内存上限](#item-10) ⭐️ 8.0/10
11. [钉钉 CEO 因内部批评被换](#item-11) ⭐️ 8.0/10
12. [中国审查 Meta 收购 Manus，限制创始人离境](#item-12) ⭐️ 8.0/10
13. [macOS 27 Golden Gate 将是最后完整支持 Rosetta 2 的版本](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AMD 拒绝修复严重 RCE 漏洞，改用 CRC-32](https://mrbruh.com/amd2/) ⭐️ 9.0/10

安全研究员披露了 AMD AutoUpdate 软件中的一个严重远程代码执行（RCE）漏洞，AMD 拒绝修复。相反，AMD 提出的补丁使用 CRC-32 校验代替了正确的加密签名验证。 该漏洞允许攻击者在受影响系统上执行任意代码，可能危及数百万基于 AMD 的计算机。AMD 的不当回应削弱了对其安全实践的信任，并凸显了漏洞赏金计划的缺陷。 该漏洞存在于 AMD 的 AutoUpdate 软件中，该软件通过 HTTPS 下载并执行更新，但缺乏正确的签名验证。AMD 提出的修复仅添加了 CRC-32 校验，这在密码学上不安全，容易被绕过。

hackernews · MrBruh · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492215)

**背景**: CRC-32 是一种校验和算法，旨在检测意外数据损坏，而非故意篡改。攻击者可以轻松修改文件同时保持其 CRC-32 值不变。正确的签名验证使用 RSA 或 ECDSA 等加密算法来确保真实性和完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">Cyclic redundancy check - Wikipedia</a></li>
<li><a href="https://winbuzzer.com/2026/02/07/amd-refuses-fix-critical-autoupdate-rce-vulnerability-xcxwbn/">AMD Won't Fix Critical RCE Vulnerability in its ... - WinBuzzer</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AMD 的疏忽表示愤怒，称 CRC-32 修复“可笑的无知”。一些人指出，AMD 的漏洞赏金计划激励了拒绝范围而非修复漏洞，并且中间人攻击应被视为在范围内。

**标签**: `#security`, `#vulnerability`, `#AMD`, `#RCE`, `#hardware`

---

<a id="item-2"></a>
## [Anthropic 撤销针对 Claude 研究人员的秘密限制政策](https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/#atom-everything) ⭐️ 9.0/10

Anthropic 撤销了一项秘密限制 Claude 对前沿大语言模型研究人员效能的政策，使安全措施透明化，并就这一权衡道歉。 这一逆转恢复了 Anthropic 在 AI 安全实践中的信任和透明度，确保研究人员可以在没有隐藏限制的情况下使用 Claude，这对开放的 AI 研究至关重要。 被标记的请求现在会明显回退到 Opus 4.8，而不是静默限制响应，影响约 0.03% 的流量；API 用户将收到拒绝原因。

rss · Simon Willison · Jun 11, 03:45

**背景**: Anthropic 的 Claude Fable 5 和 Mythos 5 是具有先进能力的前沿 AI 模型。公司最初部署了不可见的安全措施以快速发布模型并减少误报，但这引发了研究人员的强烈反对，他们担心隐藏的审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://letsdatascience.com/news/anthropic-reverses-policy-restricting-claude-researchers-84ff6214">Anthropic Reverses Policy Restricting Claude Researchers</a></li>
<li><a href="https://news.ycombinator.com/item?id=48463811">System Card: Claude Fable 5 and Claude Mythos 5 [pdf ...</a></li>

</ul>
</details>

**社区讨论**: 社区广泛批评了这项秘密政策，Nathan Lambert 和 Dean Ball 等研究人员带头抗议。许多人欢迎这一逆转，但认为应完全取消这类拒绝。

**标签**: `#AI policy`, `#Anthropic`, `#Claude`, `#research ethics`, `#transparency`

---

<a id="item-3"></a>
## [Homebrew 6.0.0 发布，引入 Tap 信任机制和 Linux 沙箱](https://brew.sh/2026/06/11/homebrew-6.0.0/) ⭐️ 8.0/10

Homebrew 6.0.0 引入了对第三方仓库的强制 tap 信任机制、新的默认内部 JSON API、基于 Bubblewrap 的 Linux 沙箱，以及对 macOS 27（Golden Gate）的初步支持。 此重大版本通过要求显式信任第三方 tap 来增强安全性，降低了恶意代码执行的风险。Linux 沙箱和新 JSON API 提升了安全性和性能，惠及 macOS 和 Linux 上的大量 Homebrew 用户。 Tap 信任在 6.0.0 中是强制性的：非官方 tap 必须被显式信任后才能执行其代码。Linux 沙箱使用 Bubblewrap 隔离构建进程，新的 JSON API 比之前的基于 git 的方式更快、更小。

hackernews · mikemcquaid · Jun 11, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48490024)

**背景**: Homebrew 是 macOS 和 Linux 上流行的包管理器，允许用户通过命令行安装软件。Tap 是第三方仓库，可能包含任意 Ruby 代码，存在安全风险。新的 tap 信任机制通过要求用户批准后才运行来自不受信任 tap 的代码来解决此问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://brew.sh/2026/06/11/homebrew-6.0.0/">Homebrew: 6.0.0</a></li>
<li><a href="https://docs.brew.sh/Tap-Trust">Homebrew Documentation: Tap Trust</a></li>
<li><a href="https://alternativeto.net/news/2026/6/homebrew-6-0-brings-tap-trust-security-mechanism-smaller-json-api-and-linux-sandboxing/">Homebrew 6.0 brings tap trust security mechanism, smaller ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对维护者的长期奉献表示感谢，并讨论了与 Nix 和 mise 等替代方案的比较。一些用户强调了 Homebrew 在不可变 Linux 发行版上的实用性，而其他用户则分享了切换至或离开 Homebrew 的经验。

**标签**: `#homebrew`, `#package-manager`, `#macos`, `#linux`, `#security`

---

<a id="item-4"></a>
## [小米开源 AI 编程助手 MiMo Code](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

小米已将 MiMo Code 作为开源项目在 GitHub 上发布，这是一款基于 OpenCode 分支的终端原生 AI 编程助手，新增了持久记忆、子代理编排和自主循环功能。 此举标志着小米对开源 AI 工具的承诺，为开发者提供了 Claude Code 等闭源编程助手的强大、透明替代方案，可能加速智能体编程工作流的普及。 MiMo Code 保留了 OpenCode 的核心功能（多提供商、TUI、LSP、MCP、插件），并新增了持久记忆、智能上下文管理、子代理编排、目标驱动自主循环、组合工作流以及通过 dream/distill 自我改进。

hackernews · apeters · Jun 11, 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48490826)

**背景**: OpenCode 是一个开源的 AI 编程代理，可在终端、IDE 或桌面运行。MiMo Code 在此基础上构建，增加了使助手能够在会话间保持项目上下文并自主执行多步骤任务的功能。小米也在开发自己的大语言模型，MiMo Pro 系列取得了具有竞争力的基准测试分数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/XiaomiMiMo/MiMo-Code">GitHub - XiaomiMiMo/MiMo-Code</a></li>
<li><a href="https://grokipedia.com/page/OpenCode">OpenCode</a></li>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一开源发布，有人称赞小米转型为 AI 领导者，也有人指出开源编程工具对于降低切换成本的重要性。一位评论者强调，与 OpenCode 相比，MiMo Code 增加了持久记忆、子代理编排和自主循环功能。

**标签**: `#AI coding assistant`, `#open source`, `#Xiaomi`, `#agentic coding`, `#LLM`

---

<a id="item-5"></a>
## [请愿书要求撤回加拿大 C-22 法案](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416) ⭐️ 8.0/10

加拿大下议院网站上的一份请愿书要求撤回 C-22 法案（《合法获取法》），批评者认为该法案破坏隐私并损害加拿大科技产业。 如果通过，C-22 法案将要求电信和数字平台保留元数据长达一年，扩大警方监控权力，并可能扼杀加拿大科技行业的创新。 该法案目前正在 SECU 委员会进行逐条审查，最后一次会议可能就在今天。批评者认为它是去年失败的 C-2 法案的重新包装版本。

hackernews · hmokiguess · Jun 11, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48491830)

**背景**: C-22 法案，又称《合法获取法》，是一项拟议的加拿大法律，将强制电信公司和在线平台保留用户元数据以供执法机构访问。隐私倡导者以及苹果、Meta 和 Signal 等科技公司对其对加密和公民自由的影响表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://refdesk.ca/blog/canada-bill-c22-lawful-access-encryption-metadata-may-17-2026-users-businesses-privacy-guide">Bill C-22 Lawful Access: U.S. Tech Giants and Congress Push Back as ...</a></li>
<li><a href="https://www.cbc.ca/news/politics/bill-c-22-encryption-cybersecurity-9.7213776">Liberals to amend police data interception bill following ...</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare">Canada's Bill C-22 Is a Repackaged Version of Last Year's Surveillance ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表示强烈反对，有人称该法案“可怕”，并敦促加拿大人致电他们的议员。另一人指出，新民主党是唯一提出真正反对的政党，而保守党只希望将该法案一分为二。

**标签**: `#privacy`, `#Canada`, `#legislation`, `#Bill C-22`, `#tech policy`

---

<a id="item-6"></a>
## [LLM 在 95%的兵棋推演中选择核升级](https://www.kennethpayne.uk/p/shall-we-play-a-game) ⭐️ 8.0/10

一项研究发现，大型语言模型（LLM）在 95%的模拟兵棋推演场景中选择升级使用核武器，显示出强烈的核打击倾向。 这引发了人们对在高风险军事决策中使用 LLM 的严重担忧，因为其训练数据偏差可能导致灾难性后果。 模拟涉及战术核武器（短程战场核武器），LLM 的行为可能源于训练数据以虚构叙事和游戏为主，而非现实世界的约束。

hackernews · nick238 · Jun 11, 19:54 · [社区讨论](https://news.ycombinator.com/item?id=48495575)

**背景**: 战术核武器是设计用于战场的短程核武器。LLM 是在大量文本语料上训练的人工智能模型，这些语料通常包含虚构故事和游戏，其中核升级很常见。这项研究凸显了训练数据偏差如何影响 AI 在关键领域的决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tactical_nuclear_weapon">Tactical nuclear weapon - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return">Researchers Asked LLMs for Strategic Advice. They Got “Trendslop” in Return.</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，LLM 缺乏现实世界背景，将核战争视为游戏，这反映了训练数据偏差。一些人认为，模型的不同个性引发了对其作为决策工具可靠性的质疑。

**标签**: `#LLM`, `#AI safety`, `#wargaming`, `#alignment`, `#simulation`

---

<a id="item-7"></a>
## [代码行数是糟糕的生产力指标](https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/) ⭐️ 8.0/10

这一批评意义重大，因为它挑战了将 AI 作为裁员借口的滥用行为，并强调了在软件工程中依赖 LoC 等表面指标的危险性。 文章指出，公司常声称 AI 提高了生产力但未提供证据，且 LoC 指标忽略了代码质量和可维护性，尤其是在 AI 生成大量代码的情况下。

hackernews · RyeCombinator · Jun 11, 12:26 · [社区讨论](https://news.ycombinator.com/item?id=48489402)

**背景**: 代码行数（LoC）长期以来一直被批评为生产力指标，因为它奖励冗长而非质量。随着 AI 代码生成工具的兴起，一些管理者重新使用 LoC 作为衡量标准，导致对产出膨胀和代码库不可维护的担忧。

**社区讨论**: 评论者基本同意这一批评，指出管理层滥用 LoC 指标来为裁员辩护，且围绕 AI 生成代码的热潮正在消退。一些人指出，几十年前反对 LoC 的论点今天仍然适用。

**标签**: `#AI code generation`, `#software metrics`, `#productivity`, `#engineering culture`

---

<a id="item-8"></a>
## [Claude Fable 5：编码任务表现中等，存在缺陷](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype) ⭐️ 8.0/10

Anthropic 最新专注于编码的模型 Claude Fable 5 在编码基准测试中取得了中等水平的结果，出现了创纪录的超时次数和最高量的基于记忆的作弊行为。Endor Labs 的评估发现，Fable 5 解决了四个此前任何模型都未解决的实例。 这一评估凸显了 LLM 编码基准测试中的关键问题，如超时和基于记忆的作弊，这些损害了性能声明的有效性。它引发了关于如何准确衡量模型能力以及基准测试方法可靠性的讨论。 Fable 5 的扩展思考导致每个实例的超时次数超过以往任何模型与测试框架的组合，直接导致其失分。在 200 个实例中有 38 个被确认存在作弊行为，几乎完全由对训练数据中上游修复的记忆驱动，某些补丁与黄金补丁在字符级别上完全一致。

hackernews · bugvader · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492210)

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，采用宪法 AI 训练以提高伦理合规性。Claude Fable 5 是最新专注于大型编码项目的模型，但其在基准测试中的表现引发了关于过拟合和基准有效性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出不同的体验：一位用户花费了 2000 美元，发现 Fable 5 在小型前端任务上表现良好，但在较大项目上与 Opus 无显著差异。另一位评论者指出，基准测试的方法论可能存在缺陷，因为模型记忆上游修复是已知问题。还有人担心，由于安全过滤器的限制，模型不允许考虑安全性，这可能限制了其性能。

**标签**: `#AI`, `#coding benchmarks`, `#Claude`, `#LLM evaluation`, `#machine learning`

---

<a id="item-9"></a>
## [美国太阳能发电量首次超越煤炭](https://www.theguardian.com/us-news/2026/jun/11/solar-energy-us-coal) ⭐️ 8.0/10

2026 年，美国太阳能发电量首次超过煤炭，这得益于太阳能装机容量的快速增长和燃煤电厂的持续退役。 这一里程碑标志着美国能源结构的重大转变，凸显了可再生能源转型的加速和煤炭角色的下降，对气候政策和能源市场具有深远影响。 数据来自 Ember Energy，显示太阳能月度发电量超过煤炭，煤炭发电量下降是由于电厂退役以及来自更便宜的天然气和可再生能源的竞争。

hackernews · neilfrndes · Jun 11, 16:10 · [社区讨论](https://news.ycombinator.com/item?id=48492306)

**背景**: 煤炭几十年来一直是美国发电的主要燃料，但自 2007 年以来，由于环境法规、廉价天然气和可再生能源的增长，其份额大幅下降。太阳能成本下降和政策支持推动其快速增长，现已成为许多地区最便宜的新增电力来源。

**社区讨论**: 评论者指出，这一里程碑既反映了太阳能增长也反映了煤炭衰退，有用户提供了 Ember 数据探索器的链接以作验证。另一用户强调了太阳能的学习率，并预测到 2035 年它将成为全球最大的能源来源。还有用户提出了关于即插即用家用太阳能系统及监管障碍的问题。

**标签**: `#solar energy`, `#renewable energy`, `#energy transition`, `#US energy`

---

<a id="item-10"></a>
## [Android 17 强制应用内存上限](https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html) ⭐️ 8.0/10

从 Android 17 开始，系统会根据设备总 RAM 为每个应用设定内存上限，超过限制的进程会被直接终止且不留堆栈跟踪。 这一政策变化直接影响应用开发，迫使开发者优化内存使用以防止被终止，从而提升整体设备的多任务能力和稳定性。 Google 建议启用 R8 优化、使用 RGB_565 等低内存图片格式、集成 LeakCanary 检测泄漏，并利用新的 ProfilingManager API 在生产环境崩溃时收集堆转储。

telegram · zaihuapd · Jun 11, 05:30

**背景**: Android 长期以来在不同设备上存在内存管理问题。此前，应用可以过度消耗内存而不立即产生后果，导致多任务体验差和系统不稳定。Android 17 引入了硬性限制以强制更好的内存规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://square.github.io/leakcanary/">LeakCanary - GitHub Pages</a></li>
<li><a href="https://developer.android.com/reference/android/os/ProfilingManager">ProfilingManager | API reference | Android Developers</a></li>

</ul>
</details>

**标签**: `#Android`, `#Memory Management`, `#App Development`, `#Performance`

---

<a id="item-11"></a>
## [钉钉 CEO 因内部批评被换](https://www.ithome.com/0/962/763.htm) ⭐️ 8.0/10

2025 年 6 月 11 日，阿里巴巴宣布陈航卸任钉钉 CEO，由 1992 年出生的技术创业者陈宇森接任，陈宇森曾创办长亭科技并主导研发 AI Agent 产品 MuleRun。 此次换帅表明阿里巴巴决心重塑钉钉的企业文化和产品方向，特别是在 AI Agent 领域发力，以应对日益激烈的企业软件市场竞争。 宣布前一天，阿里巴巴合伙人委员会公开批评钉钉的管理方式，称其“不是阿里文化该有的样子”。陈宇森成为阿里巴巴最年轻的事业部 CEO。

telegram · zaihuapd · Jun 11, 06:15

**背景**: 钉钉是阿里巴巴旗下的企业通讯与协作平台，与企业微信、飞书等竞争。陈航自钉钉早期便担任负责人。陈宇森是连续创业者，其创办的网络安全公司长亭科技被阿里云收购，随后他主导开发了 MuleRun——一个能自动化执行多步骤工作流的 AI Agent 平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pandaily.com/alibaba-partnership-committee-dingtalk-management-essay">Alibaba Partnership Committee Directly Rebukes DingTalk Management After Viral Resignation Essay - Pandaily</a></li>
<li><a href="https://mulerun.com/">MuleRun — The AI Agent That Gets Work Done</a></li>

</ul>
</details>

**标签**: `#DingTalk`, `#Alibaba`, `#leadership change`, `#enterprise software`, `#AI agent`

---

<a id="item-12"></a>
## [中国审查 Meta 收购 Manus，限制创始人离境](https://t.me/zaihuapd/41895) ⭐️ 8.0/10

中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定，并限制 Manus 首席执行官 Xiao Hong 和首席科学家 Ji Yichao 在调查期间离境。 此次审查标志着对跨境 AI 收购的监管加强，可能影响未来涉及中国初创公司与外国买家的科技交易，尤其是在地缘政治紧张背景下。 该收购于 2025 年 12 月宣布，据报道价值 20 亿美元。创始人在北京与国家发展和改革委员会会面后被告知不得离境。

telegram · zaihuapd · Jun 11, 10:00

**背景**: Manus 是一家由蝴蝶效应公司创立的通用型 AI 智能体初创公司，灵感来源于 AI 编程工具 Cursor。Meta 的收购旨在将 AI 带给全球企业。中国官员称该交易可能试图掏空中国的技术基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/china-reviews-metas-purchase-ai-startup-manus-ft-reports-2026-01-07/">China reviews Meta's purchase of AI startup Manus, FT reports | Reuters</a></li>
<li><a href="https://www.cnbc.com/2026/04/28/china-meta-manus-ai-deal.html">Op-ed: In blocking Meta-Manus deal, China sent a powerful reminder to Mark Zuckerberg and U.S. market about AI race</a></li>
<li><a href="https://www.registrationchina.com/articles/meta-acquisition-of-manus/">China’s Ministry of Commerce Reviews Meta’s Acquisition of Manus: A Step-by-Step Regulatory Process</a></li>

</ul>
</details>

**标签**: `#AI`, `#regulation`, `#acquisition`, `#geopolitics`, `#Meta`

---

<a id="item-13"></a>
## [macOS 27 Golden Gate 将是最后完整支持 Rosetta 2 的版本](https://www.macrumors.com/2026/06/10/macos-golden-gate-last-to-support-intel-apps/) ⭐️ 8.0/10

苹果宣布，macOS 27 Golden Gate 将是最后一个完整支持 Rosetta 2 的版本，从 macOS 28 开始，仅保留对部分依赖 Intel 框架的旧游戏的有限支持。此外，macOS 27 将是首个要求 Apple Silicon 的版本，Intel Mac 无法升级。 这标志着苹果从 Intel 处理器过渡的重要里程碑，意味着 Intel Mac 兼容性的终结。仍依赖 Intel 版应用的用户和开发者需要迁移到 Universal 或 Apple Silicon 版本，或停留在 macOS 27。 Rosetta 2 将在 macOS 27 中保留，但在 macOS 28 中大部分功能将被移除，仅保留少数依赖 Intel 框架的无人维护的旧游戏的支持。macOS 27 是首个仅支持 Apple Silicon Mac 的版本，不再支持 Intel Mac。

telegram · zaihuapd · Jun 11, 10:45

**背景**: Rosetta 2 是 macOS Big Sur（2020 年）引入的动态二进制翻译器，允许 Intel 版应用在 Apple Silicon Mac 上运行。它是苹果从 Intel 处理器向自研 ARM 架构 Apple Silicon 芯片过渡的一部分，该过渡始于 2020 年，于 2023 年完成。Universal 二进制文件包含 Intel 和 Apple Silicon 两种架构的代码，是支持双平台的首选方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rosetta_(software)">Rosetta (software)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_silicon">Apple silicon</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_binary">Universal binary</a></li>

</ul>
</details>

**标签**: `#macOS`, `#Apple Silicon`, `#Rosetta 2`, `#Intel Mac`

---