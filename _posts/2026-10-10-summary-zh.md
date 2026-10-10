---
layout: default
title: "Horizon Summary: 2026-10-10 (ZH)"
date: 2026-10-10
lang: zh
---

> From 32 items, 6 important content pieces were selected

---

1. [Cloudflare 收购 Deno，一年后停止运行时开发](#item-1) ⭐️ 9.0/10
2. [Typesafe AI 以 75 亿美元估值融资 8.7 亿美元，引发护城河争议](#item-2) ⭐️ 8.0/10
3. [YouTuber 称因自制摄像头追踪警察而遭警方上门](#item-3) ⭐️ 8.0/10
4. [中国天眼 FAST 发现首例脉冲星原生三体系统](#item-4) ⭐️ 8.0/10
5. [JetBrains 发布开源 12B MoE 编程模型 Mellum2.1](#item-5) ⭐️ 8.0/10
6. [Telegram Desktop 曝一键窃取任意文件漏洞](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare 收购 Deno，一年后停止运行时开发](https://deno.com/blog/cloudflare) ⭐️ 9.0/10

Cloudflare 已收购 Deno，根据公告，Cloudflare 将在未来一年内继续支持 Deno 运行时，每月发布包含错误修复和安全更新的版本，之后将停止对运行时的开发。Deno 将继续保持开源，Cloudflare 欢迎其他人接手其后续开发。 Deno 由 Node.js 创始人 Ryan Dahl 打造，是主打安全优先、原生支持 TypeScript 的 Node.js 替代方案，因此其实际停摆意味着 JavaScript 运行时领域少了一个主要的独立挑战者。此次收购也延续了开发者工具领域整合的大趋势，Cloudflare 将 Deno 的团队和技术并入其 Workers/workerd 生态。 Cloudflare 将在一年内继续每月发布错误修复和安全更新，之后若无人接手，开发将停止；代码库仍保持开源。Deno 的安全模型、对 Web 标准的遵循以及基于 V8 和 Rust 的架构，都是值得关注的技术资产，可能影响 Cloudflare 的 workerd 运行时。

hackernews · ilreb · Oct 9, 13:03 · [社区讨论](https://news.ycombinator.com/item?id=50019911)

**背景**: Deno 是一个基于 V8 引擎和 Rust 构建的 JavaScript 与 TypeScript 运行时，其核心设计理念是默认安全权限和对 Web 标准的遵循。它由 Node.js 原作者 Ryan Dahl 创建，旨在修正他对 Node 设计决策的遗憾。Cloudflare Workers 是一个无服务器平台，其运行时 workerd 同样基于 V8，并以 isolates 而非容器的方式运行代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/reference/how-workers-works/">How Workers works - Cloudflare Docs</a></li>
<li><a href="https://www.imaginarycloud.com/blog/deno-vs-node">Deno vs Node . js in 2026: Which Runtime Should You Choose?</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍表达了惋惜与不满，有人认为自从 Deno 优先考虑 npm 兼容性、偏离最初愿景后，就已预见到这一结局。也有人将此事定性为一次“收购式招聘”，实际上等于关停了 Deno 的开发，并指出这只是开发者工具领域一连串收购中的又一例。

**标签**: `#Deno`, `#Cloudflare`, `#JavaScript`, `#Runtime`, `#Acquisition`

---

<a id="item-2"></a>
## [Typesafe AI 以 75 亿美元估值融资 8.7 亿美元，引发护城河争议](https://typesafe.ai/blog/series-ai) ⭐️ 8.0/10

据公司博客消息，旧金山前沿 AI 实验室 Typesafe AI 宣布完成 8.7 亿美元融资，估值达 75 亿美元。该消息在 Hacker News 上引发激烈讨论，帖子获得 267 分、206 条评论，质疑该公司缺乏可防御的技术护城河。 这轮融资凸显出，即使核心模型迅速被开源替代品商品化，拥有强大营销和产品执行力的 AI 初创公司仍能获得数十亿美元估值。这也加剧了关于当前 AI 投资周期是否已进入炒作泡沫阶段的广泛争论。 Typesafe AI 于 2026 年 9 月结束隐身状态，获得由 DCVC 领投的 4000 万美元种子轮融资，并推出首个模型 Jev——一个旨在在软件内部做出决策的决策模型。社区成员指出，Jev 发布后很快涌现出数十个开源决策模型，而 OpenAI 自家的 Decisions API 和微软的 Decision-1 模型如今也直接参与竞争。

hackernews · tosh · Oct 9, 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50023450)

**背景**: Typesafe AI 是一家构建机器原生智能基础设施的 AI 实验室，专注于软件内部的自动化决策。在 AI 创业生态中，“护城河”指专有数据、网络效应或独特技术等可防御的竞争优势。Gartner 的 AI 技术成熟度曲线追踪新兴 AI 技术从过高期望到实际生产力的演进过程，许多观察者认为当前 AI 融资正处于“期望膨胀期”的顶峰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/">Home - TypeSafe AI</a></li>
<li><a href="https://jevwiki.ai/wiki/entities/typesafe-ai.md">TypeSafe AI ( company ) — jevwiki. ai</a></li>
<li><a href="https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence">Gartner AI Hype Cycle: Why Control Now Drives AI Value</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑态度，认为 Jev 几乎没有护城河，几天内就被开源模型复制，甚至有人怀疑 Hacker News 上存在水军炒作。也有人为公司辩护，指出其强大的工程能力、产品人才、营销实力以及在延迟-质量-成本曲线上的领先地位，是风投仍愿押注该团队的理由。

**标签**: `#AI`, `#funding`, `#startup`, `#venture-capital`, `#hype-cycle`

---

<a id="item-3"></a>
## [YouTuber 称因自制摄像头追踪警察而遭警方上门](https://gizmodo.com/youtuber-says-cops-paid-him-a-visit-after-he-built-flock-style-camera-to-track-cops-2000824306) ⭐️ 8.0/10

据 Gizmodo 报道，一位 YouTuber 声称，在他搭建了一套类似 Flock 的摄像头系统用于追踪警车后，警方上门找过他。此事在 Hacker News 上引发了 216 条评论的讨论，话题涉及自动车牌识别（ALPR）监控、隐私与法律改革。 这一事件凸显了围绕 ALPR 监控日益加剧的紧张关系——公民开始用同样的追踪技术反过来监视执法部门。它提出了尚未解决的问题：这种对等监控是否合法、是否合乎伦理，以及是否需要新的立法来规范谁可以查询 ALPR 数据。 这位 YouTuber 搭建了一套类似 Flock 的摄像头来监控警车，而据称的警方上门表明当局将该行为视为一个问题。评论者指出，Flock 的系统本意是供执法部门查询，而非面向普通公众，因此公民自行开展的追踪在合法性和伦理上有所不同。

hackernews · gumby · Oct 9, 21:06 · [社区讨论](https://news.ycombinator.com/item?id=50026555)

**背景**: Flock Safety 运营着一个由 AI 驱动的车牌识别（ALPR）摄像头网络，可拍摄过往车辆图像并与警察部门共享数据；截至 2026 年 7 月，该公司称其业务覆盖美国 49 个州的 6000 多个社区。ALPR 系统会存储车辆的位置、日期、时间、品牌、型号和颜色等信息，这引发了隐私争议。像 DeFlock 这样的开源项目会绘制这些摄像头的位置地图，而美国的警务改革努力迄今尚未产生全面的联邦立法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number- plate recognition - Wikipedia</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人赞赏新罕布什尔州的法律，该法要求在三分钟内删除未命中的车牌图像，并禁止将数据上传至设备之外；另一些人则认为，如果允许 Flock 存在，就必须通过立法严格限制谁可以查询这些数据。还有人对监控国家表示愤怒，并有人建议打造一个“OpenFlock”，用来追踪那些投票支持安装摄像头的市议员。

**标签**: `#surveillance`, `#privacy`, `#ALPR`, `#civil-liberties`, `#law-enforcement`

---

<a id="item-4"></a>
## [中国天眼 FAST 发现首例脉冲星原生三体系统](https://nao.cas.cn/news/gd/202610/t20261009_8289939.html) ⭐️ 8.0/10

中欧科学家独立确认，中国天眼 FAST 发现的脉冲星 PSR J0435+3233 属于首例仍处于演化阶段的原生三体系统，该系统由脉冲星、白矮星和类太阳恒星组成，内外轨道周期分别为 8 天和 73.5 年。相关成果于 2026 年 10 月 9 日发表于《天体物理学杂志快报》。 这是首例被确认的包含脉冲星的原生三体系统，为研究脉冲星在多星环境中的形成与演化提供了罕见的天然实验室。同时，这也凸显了 FAST 在发现奇异脉冲星系统方面世界领先的灵敏度，巩固了中国在射电天文学领域的地位。 脉冲星 PSR J0435+3233 是一颗自转周期约 3.20 毫秒的毫秒脉冲星，由 FAST 在“多科学目标同时巡天”（CRAFTS）中发现。其自转减慢率异常高，比银河系中其他已知毫秒脉冲星高出两个数量级，使其在周期-周期导数图上位于“自转加速线”之上，其伽马射线脉冲随后也被 Fermi-LAT 探测到。

telegram · zaihuapd · Oct 9, 05:14

**背景**: 脉冲星是高度磁化的快速自转中子星，从磁极发出电磁辐射束，当辐射束扫过地球时便可被观测到。FAST 又称“天眼”，是位于中国贵州喀斯特洼地、口径 500 米的世界最大单口径射电望远镜。“原生”三体系统指三颗恒星共同形成并一直保持引力束缚，而非后来捕获，因此是研究恒星演化的宝贵探针。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.01227">The PSR J 0435 + 3233 Triple System</a></li>
<li><a href="https://english.cas.cn/newsroom/research-news/202604/t20260408_1155383.shtml">Scientists Identify Millisecond Pulsar PSR J 0435 + 3233 , Challenging...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Five-hundred-meter_Aperture_Spherical_Telescope">Five-hundred-meter Aperture Spherical Telescope - Wikipedia</a></li>

</ul>
</details>

**标签**: `#astronomy`, `#FAST telescope`, `#pulsar`, `#triple star system`, `#scientific discovery`

---

<a id="item-5"></a>
## [JetBrains 发布开源 12B MoE 编程模型 Mellum2.1](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 8.0/10

JetBrains 发布了 Mellum2.1，这是一款面向编程代理的开源思考模型，采用 12B 参数的混合专家架构，每个 token 仅激活 2.5B 参数，以 Apache 2.0 许可发布，权重已上线 Hugging Face。该模型通过真实软件工程任务上的强化学习训练，能够探索代码库、编辑文件并检查自己的修改。 这一举动值得关注，因为一家主流 IDE 厂商推出了许可宽松、可自行部署的编程模型，开发者可以在本地运行，而不必依赖封闭的 API 代理。它强化了面向代理式编程工作流的小型高效 MoE 模型趋势，也为开源社区构建本地编程代理提供了一个有说服力的替代方案。 该模型是名为 JetBrains/Mellum2.1-12B-A2.5B-Thinking 的“思考”版本，据报道其在 SWE-Bench（解决真实 GitHub 问题的基准）上达到约 47%。由于 12B 参数中每个 token 仅激活 2.5B，推理成本远低于稠密的 12B 模型，因此本地部署更具可行性。

telegram · zaihuapd · Oct 9, 07:30

**背景**: 混合专家（MoE）是一种机器学习技术，它将模型拆分为多个专门的子网络（即“专家”），每次输入只激活其中一小部分，从而在保持总参数量较大的同时降低每个 token 的计算量。强化学习通过奖励成功结果而非模仿标注样本来训练代理，适合需要探索代码库、进行编辑并检查测试是否通过的编程代理。JetBrains 的 Mellum 系列已从 Mellum 演进到 Mellum2，再到如今的 Mellum2.1，体现了该公司对面向开发者工具的小型自托管模型的押注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/">JetBrains Releases Mellum2.1: A 12B MoE Open Model for Coding...</a></li>
<li><a href="https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking">JetBrains/Mellum2.1-12B-A2.5B-Thinking · Hugging Face</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>

</ul>
</details>

**标签**: `#JetBrains`, `#open-source`, `#coding-agents`, `#LLM`, `#MoE`

---

<a id="item-6"></a>
## [Telegram Desktop 曝一键窃取任意文件漏洞](https://t.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop 7.2.9 以下版本存在一个严重的 IPC 记录分隔符注入漏洞，编号为 CVE-2026-107181。攻击者只需诱导用户点击恶意 tg:// 链接，即可在没有任何确认提示的情况下悄悄窃取本地任意文件。该漏洞已在 7.2.9 版本中修复，官方建议用户尽快升级。 Telegram Desktop 是用户量极大的即时通讯客户端，这个一键窃取文件的漏洞会让浏览器会话、SSH 密钥、加密钱包等敏感数据暴露给远程攻击者。攻击者还可利用窃取的 tdata 会话密钥实现账号接管，因此无论个人用户还是企业组织都应立即打补丁。 该漏洞位于 Core::Sandbox 组件，根源是 tg:// 链接中未转义的分号被当作独立的 IPC 命令处理，配合 interpret: 处理器即可读取本地文件并上传至攻击者控制的频道。目前已有概念验证（PoC）公开，注入的命令滥用了原本用于发布流程的过时内部辅助程序，该程序不进行任何权限检查。

telegram · zaihuapd · Oct 9, 09:51

**背景**: Telegram Desktop 会注册 tg:// 协议处理器，使消息或外部应用中的链接能直接在客户端内打开聊天、个人资料或执行操作。应用内部通过进程间通信（IPC）在这些组件之间传递命令，如果输入未正确转义，攻击者就能在单个链接中夹带额外命令。CVE-2026-107181 正是这类注入漏洞，而它可能泄露的 tdata 文件夹保存着维持 Telegram 账号登录状态的会话密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-107181">CVE-2026-107181 - Telegram Desktop before 7.2.9 IPC Record ...</a></li>
<li><a href="https://cybersecuritynews.com/poc-released-for-telegram-desktop-flaw/">PoC Released for Telegram Desktop Flaw Enabling One-Click ...</a></li>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-107181">CVE-2026-107181 : IPC Record-Separation Injection ...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Telegram`, `#CVE`, `#privacy`

---