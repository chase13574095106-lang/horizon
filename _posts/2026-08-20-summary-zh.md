---
layout: default
title: "Horizon Summary: 2026-08-20 (ZH)"
date: 2026-08-20
lang: zh
---

> From 31 items, 8 important content pieces were selected

---

1. [恶意 Rust crate arrayref 执行构建时负载](#item-1) ⭐️ 9.0/10
2. [AliExpress 利用无声 WebAudio 进行指纹识别并破坏蓝牙多点连接](#item-2) ⭐️ 8.0/10
3. [Linux 7.2 发布，支持 HDMI 2.1](#item-3) ⭐️ 8.0/10
4. [125M Transformer 在 iPhone 上自动续写钢琴曲](#item-4) ⭐️ 8.0/10
5. [AI 使中国学生作业分数提高 18%但考试分数下降 20%](#item-5) ⭐️ 8.0/10
6. [Stripe 以超 70 亿美元收购 OpenRouter](#item-6) ⭐️ 8.0/10
7. [陶哲轩警告：AI 或引发自哥德尔以来数学界最大危机](#item-7) ⭐️ 8.0/10
8. [反向图像搜索服务泄露数百万张面部照片](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [恶意 Rust crate arrayref 执行构建时负载](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 9.0/10

流行的 Rust crate 'arrayref' 的一个恶意版本（0.3.10）被发布到 crates.io，并在构建时执行了下载并运行后门的负载。Rust 安全响应团队确认了该攻击，并删除了恶意版本，这些版本在线约 86 分钟。 这一事件凸显了 Rust 生态系统中严重的供应链安全风险，即使是广泛使用的 crate 也可能被攻破。它强调了采取更好安全措施的必要性，例如对构建脚本进行沙箱化以及改进 crates.io 的事件响应。 恶意 crate 有一个构建脚本，会下载恶意负载，该活动的基础设施与近期朝鲜的供应链攻击有重叠。其他恶意 crate（proc-macro1、proc-macro-en、aovine、arone、aronenao、tinymember）也被删除。

hackernews · abhisek · Aug 20, 13:23 · [社区讨论](https://news.ycombinator.com/item?id=49374269)

**背景**: Rust 是一种以安全性和性能著称的系统编程语言，它使用名为 Cargo 的包管理器，并有一个中央注册表 crates.io。构建脚本（build.rs）在编译时执行，可能被利用来运行任意代码，因此成为供应链攻击的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates with...</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref : Significant Overlap... | Wiz Blog</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 crates.io 处理该事件的方式表示不满，指出缺乏安全公告，恶意版本消失但没有明确指示。有人呼吁对构建脚本进行沙箱化，并采取更“内置电池”的方法来减少依赖膨胀，同时担心 Rust 项目中传递依赖数量过多的问题。

**标签**: `#security`, `#supply-chain`, `#rust`, `#malware`, `#open-source`

---

<a id="item-2"></a>
## [AliExpress 利用无声 WebAudio 进行指纹识别并破坏蓝牙多点连接](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 8.0/10

有报道发现，AliExpress 会静默播放 WebAudio 来对用户设备进行指纹识别，同时还会干扰蓝牙多点连接。这一技术由 laserphile 在博客文章中详细披露，凸显了一种新的侵犯隐私的手段。 此事意义重大，因为它揭示了一种新的隐私威胁，既影响用户追踪，也影响蓝牙设备的正常功能。这可能影响数百万 AliExpress 用户，并引发对电商此类做法伦理性的担忧。 静默音频播放用于 WebAudio 指纹识别，利用硬件和软件的差异生成唯一标识符。这种播放会干扰蓝牙多点连接，导致耳机等设备意外切换连接。该技术即使在标签页不活跃时也可能生效，并可能允许网站在移动浏览器后台运行。

hackernews · emctech · Aug 20, 10:08 · [社区讨论](https://news.ycombinator.com/item?id=49372583)

**背景**: WebAudio 指纹识别是一种浏览器识别技术，通过 Web Audio API 测量浏览器处理声音的方式。硬件、操作系统和浏览器引擎的微小差异会产生略有不同的结果，使网站能够将音频处理作为指纹的一部分。蓝牙多点连接是一项功能，允许单个蓝牙耳机同时连接至少两个源设备，例如笔记本电脑和智能手机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fingerprint.com/blog/audio-fingerprinting/">Audio Fingerprinting : What It Is + How It Works with Web API</a></li>
<li><a href="https://browserinsight.net/blog/audio-fingerprinting">Audio Fingerprinting : How AudioContext Identifies Your Device</a></li>
<li><a href="https://www.bose.com/stories/bluetooth-multipoint">What Is Bluetooth Multipoint and How Do I Use It? | Bose</a></li>
<li><a href="https://www.soundguys.com/bluetooth-multipoint-explained-28601/">What is Bluetooth multipoint ? - SoundGuys</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了担忧并分享了个人经历。有人指出静默音频播放不会触发扬声器图标，并猜测这是否允许在移动端后台运行。还有人报告了助听器和汽车音频的蓝牙中断问题，并将其与 AliExpress 联系起来。一位评论者提到 Firefox 已基本缓解了 WebAudio 指纹识别，并提供了详细链接。另一位则讽刺地质疑苹果是否会因其封闭系统的隐私立场而将 AliExpress 从 App Store 下架。

**标签**: `#privacy`, `#WebAudio`, `#fingerprinting`, `#Bluetooth`, `#security`

---

<a id="item-3"></a>
## [Linux 7.2 发布，支持 HDMI 2.1](https://www.igalia.com/2026/08/19/Linux-72-Released.html) ⭐️ 8.0/10

Linux 内核 7.2 已发布，支持 HDMI 2.1 并包含其他改进。此次发布值得注意的是加入了缓存感知调度功能，该功能已开发一年多。 此次发布对开源社区意义重大，因为它在 Linux 内核中加入了期待已久的 HDMI 2.1 支持，可能改善使用现代硬件用户的显示体验。同时，它还引入了缓存感知调度等性能增强功能，可惠及多种工作负载。 内核中的 HDMI 2.1 支持可实现更高的分辨率和刷新率，但需要经过认证的超高速 HDMI 线缆才能充分利用这些功能。该内核也将成为即将发布的发行版（如 Ubuntu 26.10）的默认内核。

hackernews · mariuz · Aug 20, 15:46 · [社区讨论](https://news.ycombinator.com/item?id=49376265)

**背景**: HDMI 2.1 是一种显示接口标准，支持更高带宽，可实现 4K@120Hz 和 8K@60Hz 等功能。Linux 内核是许多操作系统的核心，其更新带来新的硬件支持和性能改进。缓存感知调度是一种基于 CPU 缓存拓扑优化任务放置的技术，可减少缓存未命中并提高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.com/news/linux-kernel-7-2-release/">Linux 7 . 2 Arrives With Cache Aware Scheduling After More Than...</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.2-rc7-Released">Linux 7 . 2 -rc7 Released Following Another Exhausting... - Phoronix</a></li>
<li><a href="https://www.hdmi.org/spec/index">HDMI Technology: Specifications and Programs</a></li>

</ul>
</details>

**社区讨论**: 社区讨论表现出好奇与热情。一位用户询问 AMD 开源驱动中 HDMI 2.1 阻碍的解决情况，另一位则质疑此类新闻的目标受众。其他人对更新树莓派 4 表示兴奋，并比较 HDMI 与 DisplayPort。总体情绪积极，用户对提供的背景表示赞赏。

**标签**: `#Linux`, `#kernel`, `#HDMI 2.1`, `#open source`

---

<a id="item-4"></a>
## [125M Transformer 在 iPhone 上自动续写钢琴曲](https://simedw.com/2026/08/20/midi-autocomplete/) ⭐️ 8.0/10

一位开发者训练了一个 125M 参数的 transformer 模型，在 iPhone 15 上实时自动续写钢琴演奏，速度约为每秒 108 个音符，并发布了免费应用。该模型通过演奏几个 MIDI 音符进行提示，并完全在设备上继续演奏。 这展示了 transformer 模型在音乐生成中的新颖应用，并实现了设备端性能，凸显了在消费级硬件上运行此类模型的可行性。它可能为音乐家激发新的创作工具，并扩展设备端机器学习在文本和图像之外的应用。 该模型每次推进一个完整的音符，而不是通过多次传递生成音符属性。该应用免费，开发者乐于回答关于模型、训练、Core ML 以及失败方法的问题。

hackernews · simedw · Aug 20, 12:04 · [社区讨论](https://news.ycombinator.com/item?id=49373456)

**背景**: Transformer 已被用于符号音乐生成，例如 Music Transformer，它使用相对注意力来建模音乐序列。Core ML 是苹果的设备端机器学习框架，利用 Apple Neural Engine (ANE) 实现高效推理。该项目将“自动补全”概念（类似于 GitHub Copilot 等代码补全工具）应用于音乐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simedw.com/2026/08/20/midi-autocomplete/">Training a 125M-parameter Model to Autocomplete Piano - SimEdw's Blog</a></li>
<li><a href="https://openreview.net/pdf?id=rJe4ShAcF7">Published as a conference paper at ICLR 2019 MUSIC TRANSFORMER:</a></li>
<li><a href="https://hackernoon.com/why-a-fast-core-ml-model-can-still-make-your-iphone-app-feel-slow">Why a Fast Core ML Model Can Still Make Your iPhone... | HackerNoon</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了与古典作曲家训练和 AI 设计工具的相似之处，一位钢琴家认为这有助于更快地探索死胡同。其他人询问了数据规模和训练细节，一位用户对《致爱丽丝》的意外续写感到不安。还有人分享了算法生成旋律项目的链接。

**标签**: `#transformer`, `#music generation`, `#on-device ML`, `#Core ML`, `#MIDI`

---

<a id="item-5"></a>
## [AI 使中国学生作业分数提高 18%但考试分数下降 20%](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning) ⭐️ 8.0/10

一项追踪 2.7 万名 12 至 18 岁中国学生的研究发现，使用豆包等 AI 工具使平均作业分数提高 18%，每项作业耗时从 64 分钟降至 45 分钟，但六个月后考试分数比不使用 AI 的学生低 20%。 这凸显了 AI 辅助学习中的一个关键权衡：虽然 AI 能提高作业效率和分数，但如果用于走捷径而非理解概念，可能会妨碍深度学习并降低考试成绩。该发现对教育工作者、政策制定者和教育科技开发者在负责任地将 AI 融入教育方面具有重要意义。 研究发现，成绩下滑集中在赶作业的学生中，而那些将 AI 用作私人辅导并花同样时间理解概念的学生成绩未受损。文章还提到另一项研究显示，借助聊天机器人学习的大学生测试得分更高，且优势在一周后仍保持。

telegram · zaihuapd · Aug 20, 03:58

**背景**: 豆包是字节跳动推出的 AI 大模型家族，包括文本生成、图像生成等多种能力。该研究结果与关于 AI 在教育中作用的广泛讨论一致，AI 工具可以提供个性化辅导，但也可能助长走捷径而损害学习。《经济学人》的报道为这些发现增加了可信度，这些发现与关于 AI 在课堂中角色的持续辩论相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dku.wang/tool/328.html">豆 包 大 模 型 - 字节跳动推出的 AI ...</a></li>
<li><a href="https://www.sohu.com/a/877733704_121924584">AI教育助力家庭作业：技术革新与个性化学习解析_辅导_工具_孩子</a></li>
<li><a href="https://blog.csdn.net/shejizuopin/article/details/146496489">人工智能教育应用：个性化学习与智能辅导-CSDN博客</a></li>

</ul>
</details>

**标签**: `#AI in education`, `#student performance`, `#China`, `#edtech`, `#research`

---

<a id="item-6"></a>
## [Stripe 以超 70 亿美元收购 OpenRouter](https://t.me/zaihuapd/43290) ⭐️ 8.0/10

据彭博社报道，Stripe 已与 OpenRouter 达成收购协议，金额超过 70 亿美元。最终价格仍可能变动，Stripe 拒绝就传闻置评。 此次收购标志着 Stripe 进军 AI 基础设施领域的重要举措，可能重塑开发者访问和支付 AI 模型的方式。这可能增强 Stripe 在 AI 经济中的地位，并对更广泛的开发者工具生态产生影响。 OpenRouter 成立于 2023 年，提供超过 400 个 AI 模型的访问服务，并称截至今年 5 月已服务 800 万名开发者。据 Banking Dive 报道，收购价格约为 75 亿美元。

telegram · zaihuapd · Aug 20, 07:00

**背景**: OpenRouter 是一个提供统一 API 的平台，可访问来自 OpenAI、Anthropic、Google 和 Meta 等提供商的多种 AI 模型，并具备自动回退和价格/性能路由功能。Stripe 是一家主要的在线支付公司，一直在扩展 AI 相关服务，此次收购将把 AI 模型访问与支付基础设施整合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/19/stripe-openrouter-fintech-ai-model-marketplace-.html">Stripe to buy OpenRouter as fintech expands deeper into AI</a></li>
<li><a href="https://www.bankingdive.com/news/stripe-openrouter-acquisition-ai-7-billion/828357/">Stripe , OpenRouter finally strike a deal | Banking Dive</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/stripe-acquires-openrouter-7b-turning-091812340.html?fr=sycsrp_catchall">Stripe Acquires OpenRouter for $7B+, Turning Model Routing Into a...</a></li>

</ul>
</details>

**标签**: `#acquisition`, `#AI`, `#Stripe`, `#OpenRouter`, `#developer tools`

---

<a id="item-7"></a>
## [陶哲轩警告：AI 或引发自哥德尔以来数学界最大危机](https://the-decoder.com/terence-tao-says-ai-could-trigger-maths-biggest-crisis-since-godel/) ⭐️ 8.0/10

陶哲轩在为 2026 年国际数学家大会撰写的文章中警告，AI 可能导致证明过剩，以至于无人能完全理解，并将此比作 20 世纪初的基础危机。他援引 First-Proof 项目：在第二轮中，10 道未发表研究题中有 7 道至少被一个 AI 系统判定为合格，每题成本为数十至数百美元。 这一警告凸显了数学领域可能发生的范式转变，即重点可能从产生证明转向验证和理解证明，这对数学知识的验证和信任方式具有深远影响。它可能影响数学家、AI 开发者以及更广泛的科学界，因为 AI 生成的证明可能挑战传统的严谨性和理解标准。 First-Proof 项目由包括 Lauren Williams 在内的数学家组织，收集了 10 道未发表的“引理”，并给 AI 系统一周时间解决；总体而言，LLM 至少解决了其中 6 道。陶哲轩认为，即使通过形式验证，无人能清晰讲解的证明也应被视为不完整，强调了人类理解在数学中的重要性。

telegram · zaihuapd · Aug 20, 13:19

**背景**: 20 世纪初的数学基础危机由罗素悖论和哥德尔不完备定理等引发，挑战了形式系统的一致性和完备性。形式验证利用计算证明助手机械地检查证明，但不一定提供人类可理解的解释。First-Proof 项目是一项评估 AI 在研究级数学中能力的倡议，通过使用未发表的问题来防止 AI 从网上找到解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1stproof.org/">First Proof Project</a></li>
<li><a href="https://current.fas.harvard.edu/stories/first-proofs-second-batch-math-problems-test-ai">First Proof’s second batch of math problems test AI | Harvard FAS</a></li>
<li><a href="https://cacm.acm.org/research/formally-verified-mathematics/">Formally Verified Mathematics – Communications of the ACM</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#research`, `#proof verification`, `#Terence Tao`

---

<a id="item-8"></a>
## [反向图像搜索服务泄露数百万张面部照片](https://arstechnica.com/gadgets/2026/08/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/) ⭐️ 8.0/10

一家反向图像搜索服务发生数据泄露，暴露了一个 450 GB 的数据库，其中包含超过 900 万张人物面部图像以及相关的个人信息，如电子邮件地址、电话号码和 IP 地址。该服务已限制对数据库的访问，但影响范围和补救措施尚不明确。 此次泄露意义重大，因为面部图像是不可变的生物识别数据，不像密码那样可以重置。泄露的数据可能被用于未经授权的身份识别、追踪或诈骗，对数百万人的隐私和身份安全构成严重威胁。 泄露的数据库约 450 GB，包含超过 900 万张图像，部分记录包含电子邮件地址、电话号码和 IP 地址。专家警告，这些数据可能被用于身份盗窃或监控，该事件凸显了在缺乏充分保护的情况下存储生物识别数据的风险。

telegram · zaihuapd · Aug 20, 15:14

**背景**: 反向图像搜索服务允许用户查找图像在网上的出现位置或识别相似图像。生物识别数据，如面部图像，是独特且永久的，因此特别敏感。与密码不同，生物识别数据一旦泄露就无法更改，这就是为什么涉及此类数据的泄露会引起高度关注。福布斯文章指出生物识别数据是不可变的，诺顿也强调了生物识别泄露的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2025/04/25/what-happens-if-biometric-data-is-breached-and-how-to-prevent-it/">What Happens If Biometric Data Is Breached (And How To Prevent It)</a></li>
<li><a href="https://us.norton.com/blog/emerging-threats/biometric-data-breach-database-exposes-fingerprints-and-facial-recognition-data">Biometric data breach : Database exposes fingerprints and... | Norton</a></li>

</ul>
</details>

**标签**: `#data breach`, `#privacy`, `#biometric data`, `#security`, `#cybersecurity`

---