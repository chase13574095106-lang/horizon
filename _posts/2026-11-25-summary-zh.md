---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> From 23 items, 10 important content pieces were selected

---

1. [Anthropic 称内部 Claude 发现 VP≠VNP 并给出 Lean 4 证明](#item-1) ⭐️ 10.0/10
2. [OpenAI 相关预印本声称矩阵乘法指数恰为 9/4](#item-2) ⭐️ 9.0/10
3. [Anthropic IPO 定价每股 83 美元，即将登陆纳斯达克](#item-3) ⭐️ 9.0/10
4. [Ternary Bonsai 2.5 27B：5.9GB 量化模型，实现本地智能体编程](#item-4) ⭐️ 8.0/10
5. [GPT-6.2 无需专用 AI 模型即可从 3D 结构设计蛋白质微型结合剂](#item-5) ⭐️ 8.0/10
6. [Check Point 管理服务器遭 PRNG 会话伪造攻击](#item-6) ⭐️ 8.0/10
7. [《GTA 6》通过 Xbox 兼容层在 Windows 上运行](#item-7) ⭐️ 8.0/10
8. [GPT-6.2 Astra 22 分钟破解 1808 年素描本之谜](#item-8) ⭐️ 8.0/10
9. [华为与高通签署涵盖 5G 和 AI 的广泛多年专利协议](#item-9) ⭐️ 8.0/10
10. [VMware vCenter 再曝 9.8 分鉴权绕过漏洞，已被零日利用](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 称内部 Claude 发现 VP≠VNP 并给出 Lean 4 证明](https://t.me/zaihuapd/45345) ⭐️ 10.0/10

11 月 24 日，Anthropic 据称公开了论文《VP ≠ VNP over every field》及 Lean 4 形式化证明，并称该结果由内部研究用 Claude 模型发现。论文给出了哈密顿圈多项式的超多项式算术电路下界，据此推出 VP 是 VNP 的真子类，若成立即解决了 Valiant 1979 年的代数复杂度猜想。 若属实，这将是复杂度理论中的里程碑式成果，解决了一个长期悬而未决的问题，并表明 AI 能够参与前沿数学发现。同时，这也凸显了 Lean 4 等形式化验证工具在认证高深数学证明中日益重要的作用。 该结果仅限于算术电路，并不涉及 P 与 NP 问题；论文和代码据称由 AI 撰写，证明经过了三条标准公理审计和独立内核检查。鉴于该声明的非同寻常性，仍需数学界的独立验证。

telegram · zaihuapd · Nov 24, 12:18

**背景**: 在代数复杂度理论中，VP 和 VNP 是 P 和 NP 的代数类比，由 Leslie Valiant 于 1979 年提出。VP vs VNP 问题问的是：是否所有可由多项式大小算术电路计算的多项式族（VP）都属于 VNP（具有简洁证书的多项式类）；这是一个重要的开放问题。Lean 4 是一个交互式定理证明器，允许对数学证明进行形式化验证，确保从公理开始的正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity">Arithmetic circuit complexity - Wikipedia</a></li>

</ul>
</details>

**标签**: `#complexity-theory`, `#AI-for-math`, `#Lean4`, `#formal-verification`, `#Anthropic`

---

<a id="item-2"></a>
## [OpenAI 相关预印本声称矩阵乘法指数恰为 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

OpenAI 的 GitHub 上发布的一篇预印本声称，矩阵乘法指数在所有域上恰好为 9/4，即两个 n×n 矩阵相乘需要 Θ(n^2.25) 次运算。据报道，该论文由 OpenAI 一个未发布的模型生成，是四篇论文中的一部分，共解决了“数学 500 个开放问题”列表中的 8 个问题。 如果得到验证，这将解决一个数十年来关于矩阵乘法基本复杂度的问题，而矩阵乘法是科学计算和机器学习中的核心运算。这也凸显了 AI 模型在产出高级数学研究方面日益增长的作用，并引发了关于透明度和科研体制的讨论。 该结果给出了 Ω(n^2.25) 的下界，而上界 2.25 此前已知；最近发表了一个达到 O(n^2.25) 的算法，但远不实用。论文归功于一个未发布的模型，其配方未公开，标题已从 O(n^2.25) 更正为 Θ(n^2.25)。

hackernews · E-Reverance · Nov 25, 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**背景**: 矩阵乘法指数（记为 ω）是使得任意两个 n×n 矩阵可以用 n^(ω+o(1)) 次域运算相乘的最小实数。朴素乘法需要 n^3 次运算，数十年的研究已将已知上界降至约 2.37，而下界则弱得多。这篇预印本声称精确确定了该值为 9/4，这将是代数复杂性理论中的重大突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm">Matrix multiplication algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers">OpenAI bulk release of mathematical papers - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了这对 AI 研究和模型保密的影响，一些人认为 OpenAI 可能保留顶级模型以在循环中实现突破。其他人指出了标题错误（O 与 Θ），并澄清论文证明的是 Ω(n^2.25) 的下界而非上界，还将当前 AI 驱动的研究浪潮比作贝尔实验室，同时质疑其缺乏公共利益。

**标签**: `#matrix-multiplication`, `#AI-for-math`, `#OpenAI`, `#algorithms`, `#research-breakthrough`

---

<a id="item-3"></a>
## [Anthropic IPO 定价每股 83 美元，即将登陆纳斯达克](https://t.me/zaihuapd/45347) ⭐️ 9.0/10

Anthropic 将其首次公开募股定价为每股 83 美元，发行 9.8 亿股 A 类普通股，其中公司出售约 9.56 亿股，部分股东出售约 2365 万股。股票预计于 2026 年 11 月 19 日在纳斯达克全球精选市场开始交易，代码为 ANT，发行预计于 11 月 20 日完成。 这是迄今为止规模最大的 AI 公司 IPO 之一，将为 Anthropic 提供巨额公开市场资金，以与 OpenAI 等前沿实验室竞争。它也为 AI 行业提供了一个罕见的公开估值基准，将受到投资者、竞争对手和监管机构的密切关注。 公司不会获得现有股东出售股份所得款项，承销商另获 30 天期权，可额外购买最多 1.47 亿股（即“绿鞋”超额配售权）。此次发行采用双重股权结构，A 类普通股通常每股一票，而创始人和内部人士可能通过 B 类股保留更高投票权。

telegram · zaihuapd · Nov 24, 13:52

**背景**: IPO 是私人公司首次向公众发行股票并在证券交易所上市的过程。纳斯达克全球精选市场是纳斯达克最高层级的上市板块，众多大型科技公司在此挂牌。“绿鞋”期权允许承销商在上市后额外购买股份以稳定股价，而双重股权结构在希望创始人保留控制权的科技公司中很常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nasdaq_Global_Select_Market">Nasdaq Global Select Market</a></li>
<li><a href="https://www.euromoney.com/article/27bjsstsqxhkmh1znxfls/opinion/this-is-how-an-ipo-greenshoe-works/">This is how an IPO greenshoe works - Euromoney</a></li>
<li><a href="https://www.investopedia.com/ask/answers/062215/what-difference-between-class-shares-and-other-common-shares-companys-stock.asp">Class A vs. Class B Shares: Key Voting and Pricing Differences Class A vs. Class B Shares: Key Differences | StartEngine Class A vs Class B Shares: What's Actually Different (Quick ... Class A vs Class B Shares: Differences, Voting Rights ... What Is the Difference Between Class A, Class B, and Class C ... Understanding Class A Shares: Comparison With Class B and C ... Class A vs Class B vs Class C Shares, Explained - SoFi</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#public markets`, `#Nasdaq`

---

<a id="item-4"></a>
## [Ternary Bonsai 2.5 27B：5.9GB 量化模型，实现本地智能体编程](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML 发布了 Ternary Bonsai 2.5 27B，这是一个基于 Qwen3.8-27B 的三值量化模型，体积仅 5.9 GB，在智能体编程、多轮工具调用和多步任务执行方面表现更强。社区成员报告称，在配备 24GB 内存的 Mac Mini M5 Pro 上本地运行可达 22-25 tokens/s，并且能轻松在内存中容纳 128k 上下文。 该模型表明，极低比特量化可以将接近前沿的编程和智能体能力带到消费级硬件上，有可能推动本地 AI 开发的普及。同时，它也引发了关于小模型是真正在追赶，还是仅仅受益于基准过拟合和基准漂移的争论。 该模型保持了 Qwen3.8-27B 的混合注意力架构不变，使用三值权重（-1、0、+1），大幅降低了内存和计算需求。社区基准显示其在 SWE-bench Verified 上与 Opus 4.6 相当，但质疑者指出 SWE-bench Verified 可能不完全具有代表性，并且需要与同等规模的小模型（如 Qwen3.8 的 Q1/Q2 量化版）进行直接比较。

hackernews · b0m · Nov 24, 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**背景**: 三值量化将模型权重限制为三个值（-1、0、+1），从而大幅缩小模型体积并实现高效的本地推理。SWE-bench Verified 是一个评估大语言模型解决真实 GitHub 问题能力的基准，常被用作编程和智能体能力的代理指标。PrismML 的 Bonsai 系列将这一技术应用于大型模型，旨在使其能在普通硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com</a></li>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对本地性能印象深刻，有人报告在 Mac Mini 上达到 22-25 tokens/s，另一人指出任务完成时间比 Bonsai 2 减少了 29%。讨论中也包含对基准有效性的质疑，呼吁与同等规模的量化模型进行直接比较，并推测结果反映了基准过拟合、基准演变和小模型真实进步的综合影响。

**标签**: `#LLM`, `#quantization`, `#local-inference`, `#SWE-bench`, `#small-models`

---

<a id="item-5"></a>
## [GPT-6.2 无需专用 AI 模型即可从 3D 结构设计蛋白质微型结合剂](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI 报告称，GPT-6.2 能够在不使用专用蛋白质 AI 模型的情况下，从 3D 结构设计蛋白质微型结合剂，相关成果发表在预印本论文《GPT-6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models》中。该模型编写代码为五种靶蛋白生成微型结合剂的三维设计，但在序列生成方面仍依赖 SolubleMPNN 等专用工具。 这表明通用大语言模型可以在复杂的科学工作流中充当粘合层，通过减少对多个专用模型的依赖，可能降低蛋白质设计的门槛。这标志着 LLM 应用于 AI-for-science 任务的增长趋势，可能加速药物发现和生物技术研究。 尽管 GPT-6.2 生成了三维设计，但它仍需 SolubleMPNN 来建议氨基酸序列，并需要其他专用模型来筛选预测能正确折叠和结合的候选物。社区指出，“超越专用模型”的说法可能为时过早，因为该模型主要编排现有工具，而非完全取代它们。

hackernews · acossta · Nov 24, 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**背景**: 蛋白质设计涉及创建具有特定功能的新蛋白质，例如微型结合剂——一种能结合靶标的小型稳定蛋白质。传统上，这需要 RFdiffusion 等专用 AI 模型进行结构生成，以及 ProteinMPNN 进行序列设计。GPT-6 是一种通用大语言模型，能够编写代码，本研究探索了其在没有领域特定模型的情况下执行蛋白质设计任务的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein-design ... - OpenAI</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56369-w">De novo design of protein minibinder agonists of TLR3 - Nature</a></li>
<li><a href="https://www.nature.com/articles/s41587-023-02115-w">Generative models for protein structures and sequences</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍质疑“超越专用模型”的说法，指出 GPT-6.2 仍依赖 SolubleMPNN 进行序列生成，并依赖其他专用工具进行候选筛选。一些人认为 GPT 是专用模型之间有价值的“粘合层”，而另一些人则批评缺乏湿实验验证，并争论该模型是真正设计了蛋白质还是仅仅编排了现有工具。

**标签**: `#protein-design`, `#LLM`, `#AI-for-science`, `#GPT-6`, `#specialized-models`

---

<a id="item-6"></a>
## [Check Point 管理服务器遭 PRNG 会话伪造攻击](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise 报告了一起针对 Check Point 安全管理服务器的活跃入侵活动，攻击者利用 HFS 的 loginSrp1 端点收集 Math.random() 输出，重建 V8 PRNG 状态，恢复会话 cookie 签名密钥，并伪造管理员会话 cookie。该活动已入侵 22 家以上组织的服务器，暴露了防火墙规则和存储的凭据。 该攻击展示了一种新颖且实用的 PRNG 状态恢复技术，破坏了广泛使用的 Node.js 应用中的会话安全，可能影响许多依赖 Math.random() 生成安全敏感值的其他系统。它凸显了 AI 辅助网络攻击的日益增长的风险，以及认证机制中需要密码学安全随机数的必要性。 攻击者向 HFS 的 loginSrp1 端点连续发起登录，每次返回一个包含由 Math.random() 生成的 'sid' 的签名会话 cookie，收集足够输出后重建了 V8 PRNG 的内部状态。这允许恢复会话 cookie 签名密钥并伪造管理员会话 cookie；初始访问向量疑似为 CVE-2026-16232，该活动被描述为 AI 辅助。

hackernews · louiereederson · Nov 24, 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50630594)

**背景**: Check Point 安全管理服务器是用于配置和监控 Check Point 防火墙及安全策略的中心控制台。Node.js 使用 V8 JavaScript 引擎，其 Math.random() 是一种非密码学伪随机数生成器（PRNG），如果观察到足够多的输出，就可以被预测。会话 cookie 是用于维护用户状态的小段数据；如果攻击者能伪造有效的管理员会话 cookie，就能绕过认证并获得管理权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security...</a></li>
<li><a href="https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/">Check Point Security Management Servers Hacked - SecurityWeek</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/">Hackers compromise Check Point Servers in 22 organizations</a></li>

</ul>
</details>

**社区讨论**: 评论者担心这只是 LLM 驱动网络攻击的开始，老练的攻击者以及很快大量犯罪分子会利用 AI 攻击任何在线服务。一些人质疑为什么 Math.random() 不默认设置为安全，另一些人则讨论初始访问向量以及是否所有受影响组织的管理服务器都暴露在互联网上。

**标签**: `#security`, `#vulnerability`, `#PRNG`, `#Node.js`, `#cyberattack`

---

<a id="item-7"></a>
## [《GTA 6》通过 Xbox 兼容层在 Windows 上运行](https://twitter.com/raul_bs3/status/2125213756238291075) ⭐️ 8.0/10

一条 Twitter 帖子显示《侠盗猎车手 6》在 Windows 上运行，这是通过使用名为 Zenith-X 的类 Wine 兼容层对泄露的 Xbox Series X|S 版本（Build 1.0.2.1）进行逆向工程实现的，游戏在一个标题为“Americas”的操作系统窗口中启动。 这标志着游戏保存和逆向工程领域的一个重要里程碑，表明现代主机独占游戏可以通过社区努力在 PC 上运行，可能促使 Rockstar 加速推出官方 PC 版，并引发关于泄露版本的法律问题。 Xbox 版本没有 DRM 或混淆，并且由于 Xbox Series 主机与 PC 共享 x64 架构和 Windows 血统，游戏代码无需 CPU 模拟即可直接执行；像 XCL 和 VIctory 这样的项目仍需为 Xbox 系统服务（如 kernelx.dll、XGameRuntime 和 d3d12_xs.dll）逆向工程净室垫片。

hackernews · andrem · Nov 24, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=50627783)

**背景**: 《GTA 6》的 Xbox 版本由名为 CyberLeek 的黑客泄露，最初是资源文件，后来是完整的游戏二进制文件，包括一个包含 RAGE 引擎文件的 209GB 种子。现代 Xbox 主机本质上是带有额外 Xbox 专用库的 Windows PC，因此在 Windows 上运行主机游戏主要需要兼容层来替代缺失的主机 API，类似于 Wine 和 Proton 在 Linux 上运行 Windows 游戏的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techspot.com/news/114672-gta-6-leaker-releases-xbox-build-executable-modders.html">GTA 6 leaker releases Xbox build executable, and modders say ...</a></li>
<li><a href="https://www.opensourceprojects.dev/post/xcl">Xbox Series X|S games running natively on Windows, no CPU ...</a></li>
<li><a href="https://www.gamespot.com/articles/gta-6-hacker-releases-full-xbox-build-and-pc-modders-are-already-trying-to-get-it-running/">GTA 6 Hacker Releases Full Xbox Build, And PC Modders Are ... GTA 6 Xbox Leak Sparks Windows Emulation Efforts: ScarlettX ... Alleged GTA 6 Xbox Executable Leak: No Playable Windows Port ... Trinitron — GTA 6 PC Native Port & Zenith-X Compatibility Tracker GTA 6 Leaker Releases All Files for Alleged Xbox Build of Game</a></li>

</ul>
</details>

**社区讨论**: 评论者强调泄露版本缺乏 DRM 以及 Xbox 类似 PC 的架构使这成为可能，而其他人则讨论了法律和伦理影响，指出之前 GitHub 上的禁令以及担忧此类努力可能促使开发者转向基于云的组件以防止反编译。

**标签**: `#reverse-engineering`, `#game-preservation`, `#compatibility-layers`, `#GTA-6`, `#Xbox`

---

<a id="item-8"></a>
## [GPT-6.2 Astra 22 分钟破解 1808 年素描本之谜](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 8.0/10

历史学家 Mark Humphries 报告称，GPT-6.2 Astra 在极少提示下，仅用 22 分钟便利用公开资料自主确定了耶鲁大学贝内克图书馆藏匿名 1808 年素描本的作者。该模型发现了一则关于沙博子爵到访的日记记录，并预测沙博的旅行日志将证实这一归属，结果确实如此，从而带来了一项重要的历史发现。 这一案例表明，智能体 AI 能够自主开展基于原始资料的历史研究，可能改变历史学家和学者处理档案工作的方式。它引发了关于人类专业在研究中的角色的思考，并可能加速依赖档案证据的领域的发现。 Astra 在纸质档案中发现了一份鲜为人知的资料，并正确推测沙博子爵的日志（仅可从克利夫兰州立大学订购）将证实素描本的作者身份。Humphries 指出，尽管历史学家可能面临类似数学领域的信心危机，但影响可能较为温和，因为历史涉及重新阐释而非追求普遍真理。

rss · Simon Willison · Nov 24, 16:53

**背景**: GPT-6.2 Astra 是 OpenAI 于 2026 年 11 月 17 日发布的前沿大语言模型，同时发布的还有更高效的 GPT-6.2 Sol。耶鲁大学贝内克珍本与手稿图书馆是珍本和手稿的重要收藏机构。涉事素描本是该馆藏中的一件数字化藏品，而沙博子爵是一位法国贵族，其旅行记录保存在克利夫兰州立大学的一份日志中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beinecke.library.yale.edu/">Beinecke Library | Yale Library</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.2_Astra">GPT-6.2 Astra</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#historical research`, `#GPT-6.2`, `#case study`, `#automation`

---

<a id="item-9"></a>
## [华为与高通签署涵盖 5G 和 AI 的广泛多年专利协议](https://t.me/zaihuapd/45344) ⭐️ 8.0/10

华为与高通宣布达成一项为期多年、范围广泛的专利交叉许可协议，涵盖 5G、计算、人工智能和网络等领域，高通将购买华为部分美国专利，并获得华为逻辑折叠芯片制造技术的许可。该交易预计在获得监管批准后完成，将使华为专利许可的累计预期合同价值超过 69 亿美元。 这是两家无线技术巨头之间的里程碑式协议，可能降低诉讼风险并促进 5G 和 AI 领域的合作。这也标志着华为知识产权授权业务的重要里程碑，该业务自 2021 年以来已实现正向收入，并可能重塑科技知识产权格局。 协议包括高通购买华为在相同领域的部分美国专利，以及获得华为逻辑折叠芯片制造技术的许可，该技术旨在通过系统架构弥补单个芯片性能的不足。交易需获得监管批准，华为专利许可合同的累计价值超过 69 亿美元。

telegram · zaihuapd · Nov 24, 11:38

**背景**: 专利交叉许可协议允许两家公司使用对方的专利技术而不必担心侵权诉讼，通常用于解决纠纷并确保运营自由。逻辑折叠是一种芯片设计方法，通过堆叠或折叠逻辑电路来提升性能，而不单纯依赖缩小晶体管，这在摩尔定律放缓的背景下变得越来越困难。华为一直在开发这项技术，作为在制造受限情况下通往先进芯片的替代路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/huawei-qualcomm-patent-license-deal-100526">Huawei and Qualcomm sign broad multi-year patent license deal</a></li>
<li><a href="https://www.remio.ai/post/huawei-returns-to-flagship-chips-but-logic-folding-faces-its-real-test">Huawei Returns to Flagship Chips , but Logic Folding Faces Its Real...</a></li>
<li><a href="https://www.patsnap.com/resources/blog/freedom-to-operate-search-to-avoid-patent-infringement/">Freedom to operate search to avoid patent infringement | Patsnap</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Qualcomm`, `#patent licensing`, `#5G`, `#AI`

---

<a id="item-10"></a>
## [VMware vCenter 再曝 9.8 分鉴权绕过漏洞，已被零日利用](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) ⭐️ 8.0/10

Broadcom 为 VMware 产品线发布了 23 个漏洞的补丁，核心是 vCenter 目录服务（vmdir）的鉴权绕过漏洞 CVE-2026-123903，评分 9.8，且该漏洞在补丁发布前几天已被作为零日漏洞利用。攻击者只需能访问 vCenter 即可绕过认证直接进入系统。 这是企业虚拟化管理核心组件中的一个严重免鉴权绕过漏洞，且已被作为零日漏洞主动利用，意味着相关组织已面临实际风险。任何运行 VMware vCenter 的企业都可能受影响，整个虚拟化基础设施可能被接管。 该漏洞是 VMware 目录服务中利用替代路径或通道的鉴权绕过（CWE-288），CVSS 评分为 9.8。Broadcom 未提供任何临时缓解措施，且这是几天内修补的第二个目录服务绕过漏洞，前一个 CVE-2026-123890 已被 CISA 列入已知被利用漏洞目录。

telegram · zaihuapd · Nov 24, 14:50

**背景**: VMware vCenter 是 VMware vSphere 虚拟化基础设施的集中管理平台，其目录服务（vmdir）负责平台的认证功能。鉴权绕过意味着攻击者可以完全跳过登录检查，无需有效凭据即可访问系统。零日利用是指在补丁公开之前就发生的攻击，使防御者没有时间准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://computingforgeeks.com/vmware-vcenter-cve-2026-123890/">CVE-2026-123890: Fixed vCenter Builds per Branch ...</a></li>
<li><a href="https://securityonline.info/cve-watchtower/cve-2026-123903/">CVE-2026-123903: VMware vCenter, CVSS 9.8</a></li>
<li><a href="https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter/">CVE-2026-123890: Critical Authentication Bypass in VMware vCenter</a></li>

</ul>
</details>

**标签**: `#security`, `#vmware`, `#vcenter`, `#vulnerability`, `#zero-day`

---