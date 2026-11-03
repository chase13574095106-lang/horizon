---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> From 33 items, 7 important content pieces were selected

---

1. [Astra 大模型直接编辑 Qwen 权重，数学能力提升 5 倍](#item-1) ⭐️ 9.0/10
2. [Anthropic 以股票代码 ANT 申请纳斯达克 IPO](#item-2) ⭐️ 9.0/10
3. [Subvocal 智能眼镜利用射频传感将无声口型解码为文本](#item-3) ⭐️ 8.0/10
4. [Ubuntu LTS 内核近三周未修复关键 CVE-2026-98432 远程代码执行漏洞](#item-4) ⭐️ 8.0/10
5. [ChatGPT 分享链接漏洞可致账号被接管](#item-5) ⭐️ 8.0/10
6. [树莓派 5 发布，搭载 2.4GHz Cortex-A76 CPU 和双 4K60 HDMI](#item-6) ⭐️ 8.0/10
7. [Linux 内核 IPv4 TCP 高危释放后使用漏洞（CVE-2026-98432）可远程未授权 RCE](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Astra 大模型直接编辑 Qwen 权重，数学能力提升 5 倍](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 9.0/10

Astra 是一个大语言模型，能够无需外部工具直接读取和写入神经网络权重，将一个小型 Qwen 模型的数学性能提升了约 5 倍。它还通过从特定 MLP 层中减去一个方向来识别并修复了循环失败问题。 这表明大语言模型可能对其自身权重具有原生理解能力，这是迈向递归自我改进的一步，即 AI 可以直接修改和增强其他模型。这可能从根本上改变模型的微调和解释方式。 Astra 将循环行为追溯到第 15 和 19 层 MLP 写入的一个方向，然后从每层的 64 个输出列（131,072 个权重）中减去该方向。基础模型经常达到 32,768 个 token 的限制，其前 96 个练习答案中有 85 个达到了限制。

hackernews · dbreunig · Nov 2, 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**背景**: Qwen 是由阿里云开发的一系列开放权重的大语言模型。权重编辑涉及直接修改模型参数以改变其行为，而递归自我改进（RSI）是指 AI 系统迭代设计更强大的后继系统，可能引发智能爆炸。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了震惊和争论：一些人认为这是一种涌现能力，而另一些人则认为 Astra 是专门针对神经权重数据训练以实现递归自我改进的。对于这是否真正是涌现的还是针对性训练的结果存在怀疑。

**标签**: `#LLM`, `#weight editing`, `#model interpretability`, `#recursive self-improvement`, `#Qwen`

---

<a id="item-2"></a>
## [Anthropic 以股票代码 ANT 申请纳斯达克 IPO](https://t.me/zaihuapd/44858) ⭐️ 9.0/10

10 月 26 日，Anthropic 公开提交纳斯达克 IPO 申请，股票代码为「ANT」，计划于 11 月中旬挂牌，由摩根士丹利和高盛牵头。招股书草稿显示，公司上半年营收为 163 亿美元，去年同期仅为 11 亿美元；净亏损 807 亿美元，其中约 720 亿美元来自可转债等融资工具。 这是有史以来规模最大的 AI IPO 之一，标志着 AI 公司在成熟度和公开市场准入方面发生范式转变。它将为投资者如何估值高增长 AI 公司设定基准，并可能影响 OpenAI 等竞争对手的 IPO 计划。 巨额净亏损主要来自非现金会计费用：约 720 亿美元源于可转债、衍生负债及其他金融工具，因此经营性亏损远小于表面数字。招股书还披露了与 AI 安全相关的「灾难性」风险，并有 22 家银行参与此次交易。

telegram · zaihuapd · Nov 2, 15:12

**背景**: IPO（首次公开募股）是私营公司首次向公众出售股票并在纳斯达克等证券交易所上市的过程。招股书是向监管机构提交的正式文件，详细说明公司的财务、风险和商业模式。可转换工具是一种可以转换为股权的金融工具（如可转换票据），其会计处理可能产生巨额非现金费用，从而扭曲净利润。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://variety.com/2026/biz/news/anthropic-ipo-filing-ai-risks-humanity-1236931186/">Anthropic IPO Filing: AI Giant Cites 'Catastrophic' Risks</a></li>
<li><a href="https://qz.com/anthropic-ipo-filing-numbers">Anthropic IPO filing : 10 numbers from the prospectus</a></li>
<li><a href="https://applescoop.org/story/anthropic-ipo-filing-s1-revenue-risks-ticker-ant-details">Anthropic 's IPO filing : revenue , risks and 7 standout details</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#finance`, `#Nasdaq`

---

<a id="item-3"></a>
## [Subvocal 智能眼镜利用射频传感将无声口型解码为文本](https://news.ycombinator.com/item?id=50340088) ⭐️ 8.0/10

YC 支持的初创公司 The Subvocal Company（YC F26）推出了一款智能眼镜，利用射频（RF）传感将无声的口型动作以说话速度解码为文本。该团队由佐治亚理工学院学生 Aarush 和 Arnav 创立，在发现肌电（EMG）传感不实用后转向射频方案，并构建了定制的低噪声射频硬件，将天线嵌入眼镜框架中。 该产品有望在公共或安静环境中实现隐蔽的免手文本输入，惠及无障碍用户以及任何需要无声计算机交互的人。它还推动了无声语音接口领域的发展，此前该领域主要停留在学术原型阶段。 该系统通过射频感知口腔内部，即使闭唇（内部言语）也能工作，但由于面部解剖结构差异，跨用户泛化仍是一大挑战，需要大规模数据扩展。该公司尚未披露推理是在眼镜上运行还是通过应用进行，也未详细说明隐私保护措施。

hackernews · aarushyadav · Nov 2, 17:16

**背景**: 无声语音接口（SSI）无需可听声音即可解码说话意图，利用肌电活动（EMG）、超声波或无线电波等信号。默读识别专门捕捉细微的说话动作，此前的研究包括 MIT Media Lab 的 AlterEgo 和康奈尔的 EchoSpeech 眼镜。射频传感通过避免皮肤接触和汗液相关的信号变化，提供了肌电之外的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subvocal_speech_recognition">Subvocal speech recognition</a></li>
<li><a href="https://www.nature.com/articles/s44460-025-00010-2">Sensing technologies for silent speech interfaces - Nature</a></li>
<li><a href="https://www.allaboutcircuits.com/news/moving-sonar-onto-body-cornells-ai-eyeglasses-read-silent-speech/">Moving Sonar Onto the Body: Cornell’s AI Eyeglasses Read Silent ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对该技术科幻般的潜力和无障碍益处表示热情，但也提出了实际担忧：非标准脸型的眼镜适配问题、信号处理位置（眼镜上还是应用中）以及隐私风险（如推断敏感个人信息）。一些人要求与开源无声语音项目进行比较，并询问设备是否可离线工作。

**标签**: `#subvocal-speech`, `#smart-glasses`, `#accessibility`, `#privacy`, `#human-computer-interaction`

---

<a id="item-4"></a>
## [Ubuntu LTS 内核近三周未修复关键 CVE-2026-98432 远程代码执行漏洞](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 8.0/10

Ubuntu 尚未为 CVE-2026-98432 发布修复后的内核包，该漏洞是 Linux 内核 IPv4 TCP 连接处理中的关键释放后使用漏洞，导致 Ubuntu 22.04、24.04 和 26.04 LTS 在近三周内没有官方补丁。该漏洞的 CVSS 评分为 9.8，可导致远程代码执行。 这一延迟使运行 Ubuntu LTS 内核的互联网暴露和多租户自托管系统面临可远程利用的漏洞，且没有厂商提供的修复，迫使管理员寻求非官方变通方案。这也引发了对 Canonical 修复关键内核漏洞响应速度的质疑。 该漏洞是 tcp_v4_syn_recv_sock() 中的释放后使用问题，其中 ireq->ireq_opt 的所有权被转移给子套接字而未进行复制，AlmaLinux 已在测试版中提供修复后的内核。Red Hat 发布了临时缓解措施（RHSB-2026-016），称其可降低但无法完全防止暴露，而 Ubuntu 未提供官方缓解指导。

hackernews · majorchord · Nov 2, 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50341462)

**背景**: CVE-2026-98432 是 Linux 内核 IPv4 TCP 协议栈中的释放后使用漏洞，可被远程触发，CVSS 评分为 9.8 的关键级别。Ubuntu LTS 版本广泛用于服务器和云实例，Canonical 通常会对这类漏洞发布安全公告和更新的内核包。释放后使用是指内存被释放后仍被引用，可能允许攻击者执行代码或导致系统崩溃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ubuntu.com/security/CVE-2026-98432">CVE-2026-98432 | Ubuntu</a></li>
<li><a href="https://almalinux.org/blog/2026-10-30-cve-2026-98432/">CVE-2026-98432: Patched kernels available in testing | AlmaLinux OS</a></li>
<li><a href="https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432">Ubuntu LTS kernels still unfixed for critical CVE-2026-98432</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了一个具体的 iptables/nftables 缓解措施，即在 raw PREROUTING 中使用 U32 丢弃规则，质疑 Ubuntu 为何在没有解释的情况下延迟补丁，并提出了对消费级路由器中未修补 Linux 内核以及 LLM 辅助利用风险的更广泛担忧。一些人还批评 Ubuntu 缺乏官方缓解指导，并质疑来源的可信度。

**标签**: `#security`, `#linux-kernel`, `#ubuntu`, `#cve`, `#0day`

---

<a id="item-5"></a>
## [ChatGPT 分享链接漏洞可致账号被接管](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter 研究团队发现了一个 ChatGPT 分享链接漏洞，攻击者只需诱使受害者打开恶意链接，便可在已登录用户的会话中执行代码、读取私密对话并将数据发送至外部服务器。OpenAI 已于 10 月 26 日修复该漏洞，将其定级为 P1，并支付了 5000 美元赏金。 该漏洞影响了一款广泛使用的 AI 产品，且用户只需点击链接即可中招，凸显了聊天应用中富预览功能的安全风险。这也强调了在处理用户提供内容的 Web 组件中，沙箱隔离和消息验证的重要性。 该漏洞利用了预览功能与图表组件之间的消息处理逻辑缺陷，具体涉及第三方数学输入组件 MathLive，该组件在接受消息时未充分检查来源。OpenAI 复现了代码执行和私密对话两个概念验证，将严重性从 P2 提升至 P1，并在 ChatGPT 网页前端的两个版本上部署了服务器端修复。

telegram · zaihuapd · Nov 2, 10:24

**背景**: ChatGPT 的预览功能将用户提供的 HTML 封装在独立源上的锁定框架中，以防止其读取主站 chatgpt.com 页面。然而，研究人员发现，这个受限框架与主应用可信组件之间的通信可能被滥用。MathLive 是一个用于渲染数学输入的第三方库，其消息处理逻辑缺乏正确的来源验证，使得攻击者能够发送主应用会信任的伪造消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>
<li><a href="https://cyberinsider.co.uk/patched-chatgpt-sharing-flaw-exposed-private-conversations/">Patched ChatGPT sharing flaw exposed private conversations</a></li>
<li><a href="https://aiweekly.co/alerts/openai-patches-chatgpt-share-link-flaw-that-hijacked-sessions">OpenAI Patches ChatGPT Share-Link Flaw That Hijacked Sessions</a></li>

</ul>
</details>

**标签**: `#security`, `#ChatGPT`, `#vulnerability`, `#OpenAI`, `#account-takeover`

---

<a id="item-6"></a>
## [树莓派 5 发布，搭载 2.4GHz Cortex-A76 CPU 和双 4K60 HDMI](https://t.me/zaihuapd/44854) ⭐️ 8.0/10

树莓派 5 正式发布，搭载 2.4GHz 四核 64 位 Arm Cortex-A76 CPU、VideoCore VII GPU、双 4K60p HDMI 输出和 4K60p HEVC 解码器。4GB 型号售价 60 美元，8GB 型号售价 80 美元，另加当地税费。 这是广泛使用的树莓派平台的一次重大硬件升级，带来了显著提升的 CPU 和 GPU 性能、双 4K 显示支持以及更快的接口。它将影响依赖树莓派进行项目开发的爱好者、嵌入式开发者、教育工作者和工业用户。 新特性包括双频 802.11ac Wi-Fi、蓝牙 5.0/BLE、支持 SDR104 模式的高速 microSD 卡接口，以及两个可同时以 5Gbps 运行的 USB 3.0 端口。Cortex-A76 核心相比前代 Cortex-A75，整数性能提升高达 25%，浮点性能提升 35%。

telegram · zaihuapd · Nov 2, 12:00

**背景**: 树莓派是由树莓派基金会开发的一系列小型单板计算机，旨在促进学校和发展中国家的基础计算机科学教育。树莓派 5 是最新一代产品，接替 2019 年发布的树莓派 4 Model B。Cortex-A76 是 Arm 设计的高性能 64 位 CPU 核心，VideoCore VII 是树莓派 5 所使用的 Broadcom BCM2712 SoC 中的集成 GPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_Cortex-A76">ARM Cortex-A76</a></li>
<li><a href="https://www.notebookcheck.net/Broadcom-VideoCore-VII-Benchmarks-and-Specs.873281.0.html">Broadcom VideoCore VII - Benchmarks and Specs - Notebookcheck</a></li>

</ul>
</details>

**标签**: `#Raspberry Pi`, `#hardware`, `#single-board computer`, `#embedded systems`, `#Arm`

---

<a id="item-7"></a>
## [Linux 内核 IPv4 TCP 高危释放后使用漏洞（CVE-2026-98432）可远程未授权 RCE](https://t.me/zaihuapd/44866) ⭐️ 8.0/10

Linux 内核 IPv4 TCP 握手路径中发现一个高危释放后使用漏洞 CVE-2026-98432，影响内核 4.4 及更高版本。远程未授权攻击者可通过发送带有 IP 选项的精心构造的 IPv4 TCP 数据包利用竞争条件触发远程代码执行，且 Anthropic 已公布了针对 MPTCP 监听端口的 RCE 利用示例。 该漏洞无需认证或用户交互即可远程利用，对任何暴露在互联网上的服务器都极其危险。自 Go 1.24 起，Go 在 Linux 上默认对监听套接字启用 MPTCP，导致用 Go 编写的服务默认处于暴露状态，显著扩大了攻击面。 该漏洞是 TCP 连接请求处理中的竞争条件导致释放后使用，且不仅限于 MPTCP 场景；即使没有 MPTCP 监听，也可能受到同类攻击。AWS 和 Red Hat 已发布安全公告，更新后的内核版本中已提供补丁。

telegram · zaihuapd · Nov 3, 02:37

**背景**: 释放后使用是一种内存安全漏洞，程序在内存被释放后仍访问该内存，可能允许攻击者执行任意代码。MPTCP（多路径 TCP）是 TCP 的扩展，允许一个连接同时使用多条网络路径以提高吞吐量和可靠性。Go 1.24 在 Linux 上为监听套接字引入了默认的 MPTCP 支持，这意味着用 Go 构建的服务除非显式禁用，否则会自动使用 MPTCP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/2026-160-aws/">CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free ...</a></li>
<li><a href="https://www.fosslinux.com/163418/cve-2026-98432-linux-tcp-use-after-free.htm">CVE-2026-98432: The Linux TCP Use-After-Free Flaw Explained</a></li>
<li><a href="https://access.redhat.com/security/vulnerabilities/RHSB-2026-016">RHSB-2026-016 Use-after-free - kernel IPv4 (CVE-2026-98432)</a></li>

</ul>
</details>

**标签**: `#security`, `#linux-kernel`, `#vulnerability`, `#CVE`, `#networking`

---