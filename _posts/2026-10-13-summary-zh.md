---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> From 30 items, 7 important content pieces were selected

---

1. [OpenAI 发布内部前沿模型生成的 722 篇数学手稿](#item-1) ⭐️ 9.0/10
2. [网络攻击迫使欧洲超市冷柜进入除霜模式](#item-2) ⭐️ 8.0/10
3. [WiFi 7 路由器被改造成 320 Msps 软件定义无线电接收机](#item-3) ⭐️ 8.0/10
4. [Codex CLI 默认静默安装常驻自更新后台守护进程](#item-4) ⭐️ 8.0/10
5. [Meta 发布前沿 AI 模型 Muse Wonder](#item-5) ⭐️ 8.0/10
6. [PS2 游戏通过静态重编译在浏览器中以 WebAssembly 运行](#item-6) ⭐️ 8.0/10
7. [Python 3.15 发布，带来 PEP 810 显式惰性导入](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布内部前沿模型生成的 722 篇数学手稿](https://t.me/zaihuapd/44351) ⭐️ 9.0/10

OpenAI 在 GitHub 上发布了一个合集，包含由内部未公开的前沿模型生成的 722 篇数学手稿和 372 个结果系列，其中许多证明已用 Lean 形式化验证。该模型在评估期间尝试了约 4000 道题，平均每项结果消耗约 3 小时 ChatGPT Pro 思考算力，OpenAI 还提供了 10 份推理摘要。 此次发布标志着自动推理和 AI 辅助数学研究可能迎来范式转变，表明前沿模型能够大规模攻克长期未解的问题。这可能重塑数学家与 AI 的协作方式，但由于使用的是未公开模型且部分结果仍在验证中，也引发了关于可复现性和 AI 在数学中角色的争论。 许多证明已在 Lean 这一严格的交互式定理证明器中形式化并通过检查，但部分结果仍处于验证阶段，且所用底层模型并未公开。该仓库以 Apache-2.0 许可证发布，平均每项结果约 3 小时 ChatGPT Pro 思考算力的成本也凸显了所投入的巨大资源。

telegram · zaihuapd · Oct 12, 03:00

**背景**: Lean 是当前最先进的交互式定理证明器和函数式编程语言，用于形式化验证数学证明和软件正确性，即由机器依据精确的逻辑规则检查证明。OpenAI 的前沿模型是其能力最强、通常尚未公开的 AI 系统，而 ChatGPT Pro 是提供“思考更久”以获得更可靠回答的模型版本的订阅服务。此次发布参考了普林斯顿高等研究院数学与人工智能咨询小组的建议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/news/story/openai-receives-mixed-response-after-stepping-into-math-world-7666620/">OpenAI receives mixed response after stepping into math ... | LinkedIn</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/chatgpt-solves-372-complex-math-problems-after-hugging-face-hack-sam-altman-reacts-3011300-2026-10-07">ChatGPT solves 372 complex math problems after... - India Today</a></li>
<li><a href="https://lean-lang.org/papers/system.pdf">The Lean Theorem Prover (system description) Proving Software Correctness: A Developer's Guide to Formal ... Software Verification in Lean 2026 - beneficial-ai-foundation ... A Comprehensive Survey of the Lean 4 Theorem Prover ... GitHub - harryjwang/Formal-Verification-Practice: A ...</a></li>

</ul>
</details>

**社区讨论**: 此次发布引发了褒贬不一的反应：人类数学协会发表声明，敦促数学家不要与 OpenAI 合作，而一些评论者则认为，鉴于成果的规模和形式化验证，这些批评站不住脚。争论的焦点在于研究界应当接纳还是抵制 AI 生成的数学成果。

**标签**: `#AI`, `#Mathematics`, `#OpenAI`, `#Lean`, `#Automated Reasoning`

---

<a id="item-2"></a>
## [网络攻击迫使欧洲超市冷柜进入除霜模式](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

一场针对欧洲超市制冷系统的网络攻击远程激活了商用冷柜的自动除霜功能，导致运营中断和商品损坏，法国连锁超市 Intermarché的 150 家门店受到影响。该事件发生于 2026 年 10 月，还波及了配送和店内定价系统。 此次攻击表明，关键食品供应链中的老旧工业控制系统（ICS）和物联网设备可被轻易武器化，暴露出影响零售商、消费者及整体经济的系统性安全漏洞。它凸显了在长期重成本轻韧性的行业中，建立 OT 安全标准和生命周期管理的迫切需求。 被利用的控制器包括已有 15 至 20 年历史的型号，如 Danfoss SM800（2021 年终止支持）和 SC355（2016 年终止支持），这些设备存在已知 CVE 漏洞，但由于轮班作业缺乏安全余量而从未修补。Claroty 的 Team82 此前已在 Danfoss AK-SM 800A 平台的嵌入式 Web 管理界面中发现多个漏洞。

hackernews · Zeekaas · Oct 12, 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**背景**: 商用制冷系统依赖监控控制器来协调各门店的温度、除霜周期和能效。许多此类控制器为远程诊断和节约成本而连接互联网，但运行的是过时且无安全更新的固件。自动除霜本是一项正常功能，通过暂时加热蒸发器来融化霜层；若被恶意触发，则可能使冷冻室温度升高到足以损坏易腐商品的程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers">Freeze the Controller , Defrost the Food: Uncovering Vulnerabilities in...</a></li>
<li><a href="https://itwire.com/guest-articles/guest-research/chilling-discoveries-claroty-finds-multiple-security-vulnerabilities-in-danfoss-and-copeland-refrigeration-controllers">Chilling discoveries: Claroty finds multiple security vulnerabilities in...</a></li>
<li><a href="https://www.machine.news/vulnerabilities-in-refrigeration-systems-highlight-the-chilling-fragility-of-food-supply-chains/">Vulnerabilities in refrigeration systems highlight the chilling fragility of...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，根本原因并非技术无知，而是经济现实：轮班工人缺乏进行安全审查和设备更换周期的资源，一些新型实验室设备甚至需要付费订阅才能运行。还有人指出，Danfoss 漏洞可能与 2026 年 8 月美国军事基地的类似事件有关，质疑是同一攻击者还是受启发的模仿者。

**标签**: `#cybersecurity`, `#IoT`, `#industrial-control-systems`, `#supply-chain`, `#vulnerability`

---

<a id="item-3"></a>
## [WiFi 7 路由器被改造成 320 Msps 软件定义无线电接收机](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

开发者 h0m3us3r 发布了一个开源项目，通过逐寄存器逆向工程，用自定义固件替换了 Gemtek W1700K WiFi 7 路由器中 MediaTek MT7996 射频芯片的原厂固件，将路由器改造成宽带软件定义无线电接收机。改造后的射频芯片可在 2.4、5 和 6 GHz 频段以最高 320 Msps 的速率采集 14 位 IQ 采样，并通过零拷贝 UDP 经 10 GbE 传输到 Linux 主机进行实时频谱渲染。 该项目表明，普通商用 WiFi 7 硬件可以提供以往需要昂贵专用设备才能实现的 SDR 能力，有望让预算有限的频谱监测、射频研究和信号分析在广泛可得的消费级设备上成为可能。它还凸显了逆向工程闭源射频固件如何释放日常网络设备中隐藏的能力。 该射频芯片以 14 位 IQ 采样流式传输且不丢样本，但项目并非完整的收发信机——它仅作为接收机工作，覆盖范围限于 2.4/5/6 GHz 频段，而非从直流到极高频的全频段。由于采用相同的 MT7996 芯片组，评论者认为该方法可能同样适用于内置 PCIe（用于 NVMe）的 Banana Pi R4。

hackernews · djfergus · Oct 12, 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**背景**: 软件定义无线电（SDR）是一种用软件而非专用硬件进行射频信号处理的技术，使单个设备能够接收或发送多种协议和频率。传统 SDR 硬件（如 USRP 或 LimeSDR）价格从数百到数千美元不等，因此爱好者常寻找更便宜的替代方案。WiFi 7 路由器内置了为高吞吐量无线网络设计的高性能射频前端和基带芯片，黑客们越来越多地瞄准这些芯片，将其重新用于通用无线电实验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/turn-a-wifi-7-router-into-a-320msps-software-defined-radio-receiver-38irzaw8t">Turn a WiFi 7 Router into a 320Msps Software Defined Radio ...</a></li>
<li><a href="https://hackaday.com/2026/10/12/wifi-router-does-software-defined-radio/">WiFi Router Does Software-Defined Radio - Hackaday</a></li>
<li><a href="https://github.com/open-sdr/openwifi-hw">GitHub - open-sdr/openwifi-hw: open-source IEEE 802.11 WiFi ... h0m3us3r on X: "Turned a WiFi 7 router into a 320Msps SDR ... OpenWiFi: Open Source FPGA and SDR Based WiFi Implementation Ham Hacks: Hacking skills for breaking Into… | Bishop Fox Top 10 Hacking Devices for Ethical Hackers in 2026</a></li>

</ul>
</details>

**社区讨论**: 评论者反响热烈，有人指出同一位开发者此前还基于 ESP32 WiFi 微控制器构建过 SDR，并希望此类项目能让 SDR 能力普及到日常笔记本电脑上。其他人指出由于芯片组相同，该项目很可能兼容 Banana Pi R4；一位评论者强调了以如此低成本获得 5 GHz 频段 320 Msps 接收机的非凡价值，还有人推测手机 FM 收音机可能也是软件定义的。

**标签**: `#SDR`, `#WiFi 7`, `#hardware hacking`, `#RF`, `#embedded systems`

---

<a id="item-4"></a>
## [Codex CLI 默认静默安装常驻自更新后台守护进程](https://github.com/openai/codex/issues/48195) ⭐️ 8.0/10

自 0.157.0 版本起，只要打开一个交互式 Codex CLI 会话，就会静默启动一个常驻后台守护进程（app-server --managed-daemon），该进程在窗口关闭后依然存活，会把约 374MB 的平台包复制到一个与已安装 CLI 解耦的版本化目录中，并启动一个分离的更新器，每小时检查一次更新。这一行为没有文档说明，也没有官方开关可以关闭，从而引发了一个获得 480 分、245 条评论的 GitHub issue。 Codex CLI 是一款被广泛使用的 AI 编程代理，因此一个静默常驻的守护进程改变了每一位使用它的开发者所面临的信任与资源模型，影响磁盘占用、权限以及工具的可预测性。这场反弹凸显出人们对 AI 编程助手在未经用户明确同意的情况下安装后台服务并自动更新这一做法的日益审视。 该守护进程会为每个版本复制约 374MB 到版本化目录中，据一位用户称，旧版本累计占用了约 12GB；另一位用户报告说，自动更新会随机破坏权限，使 .git 变为只读，从而阻塞任务。在 ~/.codex/config.toml 中存在一个功能开关（[features] daemon_auto_start = false），守护进程还会在 ~/.codex 下写入 pid 和锁文件，但这些都没有文档说明。

hackernews · whimblepop · Oct 12, 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**背景**: Codex CLI 是 OpenAI 推出的轻量级编程代理，在终端本地运行，通常通过 npm 以 @openai/codex 安装。后台守护进程是一种在终端关闭后仍持续运行的长驻进程，常用于管理会话或执行更新。争议的核心在于：这样一个常驻且自更新的组件是否应该默认静默安装，而不是让用户主动选择启用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codex.danielvaughan.com/2026/09/25/codex-cli-daemon-auto-start-stable-default-v0157/">Daemon Auto-Start Is Now the Stable Default in Codex CLI v0 ...</a></li>
<li><a href="https://daily.dev/posts/codex-cli-installs-a-persistent-self-updating-background-daemon-by-default-unpmj86e7">Codex CLI installs a persistent, self-updating background ...</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai/ codex : Lightweight coding agent that runs in your...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多持批评态度：有人指出没有文档化的设置可以关闭该守护进程，但提到了一个未文档化的功能开关；有人报告旧版本累计占用约 12GB；还有人描述了自动更新导致 .git 变为只读并阻塞任务的 bug。其他人则将其与 Claude Code 作不利比较（有用户称 Claude Code 采用类似模式），并称赞像 hax 这样依赖 bash、而非过度工程化工具链的极简框架。

**标签**: `#Codex CLI`, `#OpenAI`, `#background daemon`, `#developer tools`, `#AI coding assistants`

---

<a id="item-5"></a>
## [Meta 发布前沿 AI 模型 Muse Wonder](https://research.meta.ai/blog/muse-wonder) ⭐️ 8.0/10

Meta 发布了新的前沿 AI 模型 Muse Wonder，并声称其在 DeepSWE、SWE-Marathon 等第三方独立测试的智能体与编程基准上名列前茅。该模型将很快为 Meta 的 Muse 个人助理智能体提供支持，覆盖每月 20 美元和 100 美元两档订阅用户。 作为来自主要实验室的发布，Muse Wonder 加剧了前沿 AI 开发者之间的竞争，并可能改变智能体与编程模型市场的力量格局。它被整合进 Meta 的订阅制助理，也表明 Meta 正推动将先进 AI 能力直接变现给消费者。 此次发布包含 Muse Wonder 系列及一个“Full”版本，Meta 同时推出了 Muse Agent——一个拥有自己虚拟计算机的自主智能体。早期社区测试结果不一：有人发现该模型在图像转 HTML 任务上的表现弱于 Opus 5.5 等竞品，还有用户报告了严重的隐私问题，即他人的个人资料出现在其 Meta 登录认证界面中。

hackernews · meetpateltech · Oct 12, 16:48 · [社区讨论](https://news.ycombinator.com/item?id=50059115)

**背景**: 前沿模型是指在特定时间点能力最强的 AI 模型之一，通常是主要实验室的最新旗舰产品，该术语在政策和行业中被用来描述其能力可能带来新风险的模型。Meta 的 AI 产品此前已多次面临隐私担忧，包括其隐私政策变更允许将用户内容用于 AI 训练，以及有报道称 Meta AI 应用存在严重的隐私问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://getmorefromai.com/glossary/frontier-model">Frontier model : Definition , Examples, and Why It... | GetMoreFromAI</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人认为更多公司接近前沿有助于防止权力过度集中，另一些人则报告了具体问题。一位用户详细描述了 Meta 登录流程中个人资料和邮箱暴露的严重隐私担忧，技术对比显示 Muse Wonder 在图像转 HTML 测试中落后于 Opus 5.5，有人指出该任务上它更接近 Sonnet 或 Haiku 的水平。

**标签**: `#AI`, `#Meta`, `#frontier models`, `#privacy`, `#benchmarks`

---

<a id="item-6"></a>
## [PS2 游戏通过静态重编译在浏览器中以 WebAssembly 运行](https://github.com/snuri00/ps2-web-recomp) ⭐️ 8.0/10

开发者 snuri00 在 GitHub 上发布了 ps2-web-recomp 项目，它把 PlayStation 2 游戏静态重编译为 C++，再编译成 WebAssembly，并与一个用 WebGPU 渲染的 PS2 操作系统和硬件重实现链接。首个支持的游戏《GT 赛车 4》据称在笔记本集成显卡上以两倍于 PS2 原生分辨率满速运行（50 FPS），且完全不需要传统模拟器。 这表明静态重编译能以接近原生的性能把主机游戏带到网页上，可能为游戏保存开辟一条绕过传统模拟器的新分发途径。它也凸显了从 N64 到 PS Vita 等各主机重编译项目日益增多的趋势，并引发了关于性能、合法性和对社区构建二进制文件信任度的讨论。 该项目将 PS2 的 Emotion Engine MIPS 机器码提前翻译为 C++，再编译为 WebAssembly，并与一个用 WebGPU 绘制的 PS2 操作系统和硬件重实现链接。它是同一作者 psp-web-recomp 项目的姊妹项目，采用相同方法，但目前只成功运行了首个游戏。

hackernews · deadxwarrior · Oct 12, 06:46 · [社区讨论](https://news.ycombinator.com/item?id=50052251)

**背景**: 静态重编译是二进制翻译的一种形式，它在运行前就把程序的机器码从一种指令集架构翻译到另一种，而不是像动态重编译或模拟器那样在运行时翻译。这种方法能带来接近原生的性能，因为翻译后的代码直接在目标平台上运行，已被 N64Recomp 等项目用于移植任天堂 64 游戏。PS2 的主 CPU 是 Emotion Engine，一款基于 MIPS 的处理器，历史上很难高效模拟，PCSX2 等模拟器就体现了这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/snuri00/ps2-web-recomp">Show HN: PS2 games statically recompiled to WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_recompilation">Static recompilation</a></li>
<li><a href="https://en.wikipedia.org/wiki/PCSX2">PCSX2 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术成就表示赞叹，有人指出 AI 虽然冲击了自己的职业，却也让这类重编译工作成为可能。有人担心反编译和重编译项目可能藏有恶意软件，因为它们缺乏成熟模拟器社区那样的信任和审查，还有评论者建议把重编译器本身也编译成 WebAssembly，以便直接在浏览器中完成转换。另一位开发者分享了自己类似的 PS Vita ARM 到 WASM 转译器项目，还有人开玩笑说会怀念《GT 赛车》漫长的 CD 加载画面。

**标签**: `#WebAssembly`, `#Game Emulation`, `#Static Recompilation`, `#PS2`, `#Security`

---

<a id="item-7"></a>
## [Python 3.15 发布，带来 PEP 810 显式惰性导入](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 已正式发布，其“What's New”指南由发布经理 Hugo van Kemenade 整理。最受关注的新特性是 PEP 810 显式惰性导入，开发者可以写 `lazy import json` 或 `lazy from pathlib import Path`，模块只会在其符号首次被使用时才真正加载。该版本还加入了 PEP 798 推导式中的解包语法，同时标志着 Python 3.10 支持周期的结束。 惰性导入直接解决了长期存在的痛点：导入 sentence_transformers 这类重量级依赖可能让命令行工具启动多花数秒，这正是 Simon Willison 不得不在 LLM 插件文档中推荐手动惰性导入的原因。如今它成为一等公民式的显式语言特性，使这种优化对整个 Python 生态都安全且可预测；而 3.10 的退役则推动库维护者采用 3.11 时代的特性。 PEP 810 是 CPython 在惰性导入上的第二次尝试：此前“全局隐式惰性导入”的 PEP 690 因复杂性和不可预测性于 2022 至 2023 年被指导委员会否决，而新设计完全显式、按需启用。该特性最早随 2026 年 5 月 7 日发布的 Python 3.15 beta 1 提供；新的推导式解包语法 `[*sublist for sublist in lists]` 等价于 `[x for L in lists for x in L]` 这样的嵌套循环。

rss · Simon Willison · Oct 12, 18:15

**背景**: Python 是一门广泛使用的开源编程语言，每年发布的新版本都会增加语法与性能改进，同时淘汰最旧的支持版本。PEP（Python 增强提案）是提出并批准语言变更的正式设计文档。惰性导入指模块不在导入时执行，而是在其名称真正被使用时才加载，以少量间接性换取更快的启动速度。2022 年 10 月发布的 Python 3.11 正是 Willison 现在可以开始使用的版本，因为 3.10 已不再受支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps . python .org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://docs.python.org/3/whatsnew/3.11.html">What’s New In Python 3.11 — Python 3.15.0 documentation</a></li>

</ul>
</details>

**标签**: `#Python`, `#Programming Languages`, `#Software Engineering`, `#PEP 810`, `#Open Source`

---