---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> From 33 items, 10 important content pieces were selected

---

1. [美国科学陷入危机：资金与信任崩塌](#item-1) ⭐️ 9.0/10
2. [哪吒监控存在高危路径穿越漏洞（CVSS 9.1）](#item-2) ⭐️ 9.0/10
3. [Epic Games 开源游戏开发版本控制系统 Lore](#item-3) ⭐️ 8.0/10
4. [美国推迟将 DeepSeek 列入黑名单，标记 100 多家中国企业](#item-4) ⭐️ 8.0/10
5. [GLM-5.2 登顶开源权重排行榜，媲美闭源模型](#item-5) ⭐️ 8.0/10
6. [RFC 10008 标准化 HTTP QUERY 方法](#item-6) ⭐️ 8.0/10
7. [AI 要求更强的工程纪律，而非更少](#item-7) ⭐️ 8.0/10
8. [Android 17 发布：强制大屏适配，新增 AI 功能](#item-8) ⭐️ 8.0/10
9. [GitHub Copilot 2026 年 6 月起改为按使用量计费](#item-9) ⭐️ 8.0/10
10. [中国将科创板第五套标准扩展至 AI 与硬科技](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美国科学陷入危机：资金与信任崩塌](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 9.0/10

《科学美国人》的一篇文章报道称，美国科学与政治之间的契约已经破裂，导致研究人员外流、资金崩溃以及科学界普遍感到绝望。 这种破裂威胁到美国在研究和创新领域的领导地位，因为才华横溢的科学家离开美国或放弃学术界，可能对国家竞争力和全球科学进步造成长期损害。 文章指出，科研经费枯竭，签证限制阻碍外国人才，甚至资深科学家也在准备后备计划。社区评论描述了研究人员哭泣、移居国外以及实验室转为兼职雇佣的情况。

hackernews · presspot · Jun 17, 09:54 · [社区讨论](https://news.ycombinator.com/item?id=48568058)

**背景**: 几十年来，美国科学依赖于两党共识，即联邦对基础研究的资助至关重要。近期的政治两极分化和预算削减削弱了这种支持，而签证政策使得吸引全球人才更加困难。结果是研究人员信心日益下降的危机。

**社区讨论**: 评论表达了深深的痛苦：一位用户的妻子是光镊专家，经常哭泣并即将移居国外；另一位指出科研经费和外国学生招聘都已崩溃。然而，一位评论者将混乱视为建立新联系和筹款的机会。

**标签**: `#science policy`, `#research funding`, `#academia`, `#U.S. politics`

---

<a id="item-2"></a>
## [哪吒监控存在高危路径穿越漏洞（CVSS 9.1）](https://t.me/zaihuapd/42001) ⭐️ 9.0/10

哪吒监控（Nezha）v2.0.13 以下版本被发现存在严重未授权路径穿越漏洞（CVE-2026-53519，CVSS 9.1），攻击者通过构造 GET 请求（如 /dashboard../data/config.yaml）即可读取配置文件，获取其中的 JWT 密钥。 该漏洞可泄露 JWT 密钥，攻击者能伪造身份认证令牌，未经授权访问监控面板，进而可能危及所有被监控的服务器。所有使用该广泛部署的开源工具的用户必须立即升级到 v2.0.13 或更高版本。 该漏洞是仪表盘组件中的路径穿越问题，允许通过 ../ 序列进行目录遍历。CVSS 评分为 9.1，属于严重级别，且利用该漏洞无需身份认证。

telegram · zaihuapd · Jun 17, 01:25

**背景**: 哪吒监控是一款开源、轻量级的服务器监控与运维工具，由主控端（Dashboard）和被控端（Agent）组成。路径穿越漏洞允许攻击者通过操纵文件路径访问预期目录之外的文件。JWT（JSON Web Token）常用于身份认证；若密钥泄露，攻击者可伪造令牌并冒充合法用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nezha.wiki/index.html">哪吒监控 - 服务器监控与运维工具 | 使用文档</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1922425405224223705">开源、轻量、易用的服务器监控，实战部署哪吒监控 - 知乎</a></li>
<li><a href="https://blog.dejavu.moe/posts/nezha-dashboard-deploy-guide/">哪吒监控面板部署教程 | Dejavu's Blog</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#nezha`, `#path traversal`, `#CVE`

---

<a id="item-3"></a>
## [Epic Games 开源游戏开发版本控制系统 Lore](https://lore.org/) ⭐️ 8.0/10

Epic Games 开源了 Lore，这是一个专为大型二进制文件和独占文件锁定而设计的版本控制系统，旨在满足游戏开发工作流的需求。它之前作为 Unreal Revision Control 在内部使用，现在已在 GitHub 上发布。 Lore 直接挑战了 Perforce 在游戏开发领域的主导地位，提供了一个比 Git 更好地处理大型资产和独占锁定的开源替代方案。这可以降低游戏工作室的成本和供应商锁定风险，并改善艺术家与开发者之间的协作。 Lore 针对代码与大型二进制资产（如纹理和 3D 模型）结合的项目进行了优化，并支持艺术家所需的独占文件锁定。它已集成到 Fortnite 的 Unreal Editor 中，现在以开源许可证在 GitHub 上提供。

hackernews · regnerba · Jun 17, 14:30 · [社区讨论](https://news.ycombinator.com/item?id=48571081)

**背景**: 版本控制系统（VCS）用于跟踪文件随时间的变化。Git 广泛用于代码，但处理大型二进制文件时表现不佳，且缺乏原生的独占文件锁定功能，而这对于 3D 模型等游戏资产至关重要，因为同时编辑可能导致冲突。Perforce（Helix Core）是游戏开发领域的现有领导者，提供强大的大型文件支持和锁定功能，但它是专有软件且管理复杂。Lore 旨在结合两者的优点：类似 Git 的分支简单性和类似 Perforce 的可扩展性与锁定功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/lore: Lore is a next-generation, open ...</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System</a></li>
<li><a href="https://www.theregister.com/devops/2026/06/17/git-good-with-epic-games-new-open-source-vcs-lore/5257978">Git good with Epic Games' new open source VCS, Lore</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调，Lore 是 Perforce 在游戏开发领域的直接竞争对手，而不是 Git 的通用替代品。评论者指出 Git 的用户界面不友好，Perforce 的复杂性是一个痛点，但有些人担心 Epic 对该项目的长期承诺，因为这不是他们的核心业务。

**标签**: `#version control`, `#game development`, `#open source`, `#scalability`

---

<a id="item-4"></a>
## [美国推迟将 DeepSeek 列入黑名单，标记 100 多家中国企业](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

美国推迟将中国 AI 初创公司 DeepSeek、内存芯片制造商 CXMT 及其他 100 多家中国企业列入贸易黑名单，尽管认定它们构成国家安全风险。 这一决定凸显了持续的中美科技紧张局势，可能影响全球 AI 供应链，因为 DeepSeek 是一家重要的开放权重 AI 模型开发商，其低成本高性能模型已颠覆行业。 该黑名单（即实体清单）限制美国公司向列入实体销售商品和服务，但不禁止从它们购买。DeepSeek 的模型是开放权重的，并使用受出口限制的英伟达 GPU 进行训练。

hackernews · giuliomagnifico · Jun 17, 03:55 · [社区讨论](https://news.ycombinator.com/item?id=48565498)

**背景**: DeepSeek 是一家成立于 2023 年的中国 AI 公司，其开发的 DeepSeek-R1 模型以极低的训练成本达到了与 OpenAI 的 GPT-4 相当的水平。其成功被称为美国的“斯普特尼克时刻”，引发了尽管有芯片出口限制但中国 AI 能力的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/">Exclusive: US holds off blacklisting China's DeepSeek, more than 100 firms deemed security risks, sources say | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/06/53241723/trump-admin-holds-off-blacklisting-deepseek-and-over-100-chinese-firms-flagged-as-security-risks">Trump Administration Holds Off Blacklisting DeepSeek And More Than 100 Chinese Companies Flagged As Secur - Benzinga</a></li>

</ul>
</details>

**社区讨论**: 评论者对执行力度表示怀疑，有人称之为“美国版防火墙”，另有人指出像 Z.ai 这样的中国 AI 公司已在实体清单上但影响有限。一些用户质疑未公布具体名单，并争论此类限制的有效性。

**标签**: `#AI regulation`, `#geopolitics`, `#DeepSeek`, `#US-China trade`, `#tech policy`

---

<a id="item-5"></a>
## [GLM-5.2 登顶开源权重排行榜，媲美闭源模型](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 8.0/10

Z.AI 于 2026 年 6 月 13 日发布的 GLM-5.2 已成为 Artificial Analysis 智能指数上领先的开源权重模型，以远低于 Opus 4.7 等闭源模型的成本接近前沿性能。 这一进展挑战了 Anthropic、OpenAI 和 Google 等闭源 AI 提供商的主导地位，以极低的价格提供可比的性能，可能颠覆 AI 市场格局。 GLM-5.2 支持 100 万 token 的上下文窗口，专为长周期智能体工作流和复杂多步自动化设计。社区报告显示，部分提供商以每月 50 美元提供无限 token，API 价格比 Z.AI 官方价格低 3 倍。

hackernews · himata4113 · Jun 17, 09:12 · [社区讨论](https://news.ycombinator.com/item?id=48567759)

**背景**: Artificial Analysis 智能指数是一个纯文本、英语的评估套件，对模型的质量、价格、速度和延迟进行基准测试。开源权重模型允许开发者在自己的基础设施上运行，减少对专有 API 的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5 . 2 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 GLM-5.2 的竞争性定价和性能感到兴奋，有人称其为对闭源提供商的“巨大打击”。但也有人对推理效率表示担忧，一位用户报告该模型在一个简单的编码任务上花费了 15 分钟和 45k token。

**标签**: `#AI`, `#open source`, `#LLM`, `#benchmarks`, `#pricing`

---

<a id="item-6"></a>
## [RFC 10008 标准化 HTTP QUERY 方法](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 8.0/10

RFC 10008 引入了 HTTP QUERY 方法，这是一种安全且幂等的请求方法，允许包含请求体，解决了使用 GET 请求体时的互操作性问题。 这个新方法提供了一种标准化的方式来发送复杂查询（例如大型 JSON 过滤器、图像输入），同时不破坏缓存语义，有利于 GraphQL 和搜索端点等 API。 QUERY 类似于 POST，但要求是安全且幂等的，意味着它可以自动重试而不会产生副作用。请求体包含在缓存键中，这可能导致无界的缓存键。

hackernews · schappim · Jun 17, 10:51 · [社区讨论](https://news.ycombinator.com/item?id=48568502)

**背景**: 根据 RFC 9110，HTTP GET 请求不应包含请求体，但一些开发者为了复杂查询而发送带有请求体的 GET，导致缓存和互操作性问题。POST 不是幂等的，会触发重新提交警告。QUERY 通过提供一种带有请求体的安全且幂等的方法填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008: The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://byteiota.com/rfc-10008-http-query-method-ends-the-post-workaround/">RFC 10008: HTTP QUERY Method Ends the POST Workaround</a></li>
<li><a href="https://www.baeldung.com/cs/http-get-with-body">Why an HTTP Get Request Shouldn’t Have a Body | Baeldung on Computer Science</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了将请求体包含在缓存键中的问题，指出这暗示了无界且用户控制的缓存键。有人想知道 HTML 表单是否会添加对 QUERY 的支持，以避免 POST 重新提交警告。其他人指出他们多年来一直在发送 GET 请求体，突显了实际需求。

**标签**: `#HTTP`, `#RFC`, `#protocol`, `#web`, `#caching`

---

<a id="item-7"></a>
## [AI 要求更强的工程纪律，而非更少](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline) ⭐️ 8.0/10

一篇高分文章指出，AI 生成代码的兴起要求更严格的工程实践以维持系统理解和代码质量，这与认为 AI 减少纪律需求的看法相反。 这很重要，因为 AI 正在改变软件开发，如果不加强纪律，代码库可能变得难以管理，损害长期可维护性和团队生产力。 文章强调，AI 使代码变得廉价且可丢弃，瓶颈从编写代码转向评估和理解代码，这需要更严格的审查和文档。

hackernews · BerislavLopac · Jun 17, 14:20 · [社区讨论](https://news.ycombinator.com/item?id=48570948)

**背景**: 传统上，软件工程纪律包括仔细的代码审查、测试和文档以确保质量。像 LLM 这样的 AI 工具可以快速生成代码，但这些代码往往缺乏上下文，可能引入细微错误，使评估更加困难。

**社区讨论**: 评论者讨论这一转变：有人指出 AI 使得区分有能力的工程师和仅仅粘贴 AI 输出的人更加困难，而其他人则强调评估和人类理解变得比以往更加关键。

**标签**: `#AI`, `#software engineering`, `#code quality`, `#engineering discipline`

---

<a id="item-8"></a>
## [Android 17 发布：强制大屏适配，新增 AI 功能](https://android-developers.googleblog.com/2026/06/Android-17.html) ⭐️ 8.0/10

Android 17 已正式推送至 Pixel 设备，源代码同步开放。该版本强制要求应用自适应大屏，通过 AppFunctions 引入 Gemini AI 集成，增强隐私控制，并将开发全面转向 Jetpack Compose。 此次更新通过强制大屏支持和系统级 AI 集成，从根本上改变了 Android 开发方式。开发者必须调整应用以适应新的 UI 范式和隐私要求，这将影响整个 Android 生态系统。 AppFunctions 允许应用将功能暴露为 Android MCP 的工具，使 Gemini 等 AI 助手能够调用应用功能。隐私增强包括临时权限和联系人选择器，本地网络通信现在需要用户授权。

telegram · zaihuapd · Jun 17, 01:02

**背景**: Android 传统上使用基于 XML 布局的 View 系统，但 Google 一直在推广声明式 UI 工具包 Jetpack Compose 作为未来方向。大屏适配此前只是鼓励而非强制。AppFunctions 是一个新 API，与模型上下文协议 (MCP) 集成，实现设备端 AI 编排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/06/Android-17.html">Android Developers Blog: Android 17 is here</a></li>
<li><a href="https://developer.android.com/ai/appfunctions">Overview of AppFunctions | AI | Android Developers</a></li>
<li><a href="https://developer.android.com/develop/ui/compose/migrate/compare-metrics">Compare Compose and View metrics | Jetpack Compose | Android Developers</a></li>

</ul>
</details>

**标签**: `#Android`, `#Mobile Development`, `#AI Integration`, `#Privacy`, `#Jetpack Compose`

---

<a id="item-9"></a>
## [GitHub Copilot 2026 年 6 月起改为按使用量计费](https://t.me/zaihuapd/42003) ⭐️ 8.0/10

GitHub 宣布从 2026 年 6 月 1 日起，GitHub Copilot 将从固定订阅费转为按 token 消耗计费。仍处于年度计划中的老用户可沿用旧计费模式直至计划到期，但新公布的模型乘数表显示，GPT-5.5 的请求计费乘数高达 57 倍。 这一计费转变可能大幅增加重度 Copilot 用户的成本，尤其是依赖 GPT-5.5 等高级模型的用户。它将 GitHub 的计费与实际计算消耗对齐，可能使 AI 编程助手对重度用户更昂贵，同时为偶尔使用的用户提供更灵活的计费方式。 在新模式下，用户每月获得一定数量的 GitHub AI Credits 额度，每个模型有对应的 token 乘数。GPT-5.5 的乘数为 57 倍，即一次请求消耗 57 倍的基础额度。老用户在当前年度计划到期前不受影响。

telegram · zaihuapd · Jun 17, 03:16

**背景**: GitHub Copilot 是一款 AI 驱动的代码补全工具，可在开发者输入时建议代码片段和函数。此前它采用固定月费或年费提供无限访问。转向基于 token 的计费反映了更广泛的行业趋势，即 AI 服务按处理单元（token）收费，类似于 OpenAI 和其他提供商对 API 使用的计费方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans">Model multipliers for annual plans on request-based billing ...</a></li>
<li><a href="https://kalinga.ai/github-copilot-token-based-billing-guide/">GitHub Copilot Token -Based Billing : Shocking 2026 Ultimate Guide</a></li>
<li><a href="https://www.boomkas.com/blog/github-copilot-token-billing-developer-impact">The End of an Era: GitHub Copilot 's Shift to Token -Based Bil</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#pricing`, `#AI coding assistant`, `#token billing`

---

<a id="item-10"></a>
## [中国将科创板第五套标准扩展至 AI 与硬科技](https://mp.weixin.qq.com/s/ywLPXkSlqY9S5Vwp8G5saA) ⭐️ 8.0/10

中国证监会主席吴清在 2026 年陆家嘴论坛上宣布，科创板第五套上市标准的适用范围将扩大至人工智能、量子科技、生物制造和具身智能等领域，允许未盈利的硬科技企业上市。 这一政策转向为资本密集型的人工智能和硬科技初创企业提供了关键的融资渠道，可能加速中国的技术自主和全球竞争力，同时监管机构承诺打击炒作以维护市场诚信。 此前仅适用于生物科技公司的第五套标准，现已扩展至人工智能及其他硬科技领域。证监会还计划推出储架发行等再融资改革，并将发布规范资本市场人工智能应用的指导意见。

telegram · zaihuapd · Jun 17, 08:30

**背景**: 科创板于 2019 年推出，是中国对标纳斯达克的科技板块。其第五套上市标准允许尚未盈利或营收的公司上市，前提是满足一定的研发和市值门槛。储架发行是一种“一次核准，多次发行”的再融资机制，允许企业在一段时间内灵活分次融资。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://macrochina.com.cn/news_speed/hgjj/20250627123825.shtml">macrochina.com.cn/news_speed/hgjj/20250627123825.shtml</a></li>
<li><a href="https://baike.baidu.com/item/储架发行制度/1648322">储架发行制度_百度百科</a></li>
<li><a href="https://github.com/tianxingchen/Embodied-AI-Guide">GitHub - TianxingChen/Embodied-AI-Guide: [Lumina具身智能社区] 具身智能技术指南 Embodied-AI-Guide · GitHub</a></li>

</ul>
</details>

**标签**: `#China`, `#AI regulation`, `#IPO`, `#capital markets`, `#technology policy`

---