---
layout: default
title: "Horizon Summary: 2026-10-23 (ZH)"
date: 2026-10-23
lang: zh
---

> From 37 items, 13 important content pieces were selected

---

1. [Quad9 因 DNS 封锁令退出法国市场](#item-1) ⭐️ 8.0/10
2. [NVIDIA OpenShell：面向自主 AI 代理的安全运行时](#item-2) ⭐️ 8.0/10
3. [HackiOS 通过 QEMU 在安卓手机上启动完整 iOS 16.5 固件](#item-3) ⭐️ 8.0/10
4. [任天堂 Switch 2 通过软件漏洞被破解](#item-4) ⭐️ 8.0/10
5. [eMudhra 因弱密钥事件退出全球 SSL/TLS 证书业务](#item-5) ⭐️ 8.0/10
6. [Anthropic 将 Agent Skills 标准捐赠给 Agentic AI 基金会](#item-6) ⭐️ 8.0/10
7. [Anthropic 发布 Claude API 2026-10-21 版本，移除温度等采样参数](#item-7) ⭐️ 8.0/10
8. [澳大利亚联邦法院裁定苹果和谷歌滥用市场支配地位](#item-8) ⭐️ 8.0/10
9. [特斯拉 Cybercab 在北美投产，无方向盘无人驾驶出租车](#item-9) ⭐️ 8.0/10
10. [研究：关闭 ACR 后智能电视仍上报数据](#item-10) ⭐️ 8.0/10
11. [甲骨文发布 Java SE 高危漏洞安全警报](#item-11) ⭐️ 8.0/10
12. [333 个被植入后门的 Tor 出口节点下线](#item-12) ⭐️ 8.0/10
13. [禁运的 Nvidia B300 芯片现身中国国有网络](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Quad9 因 DNS 封锁令退出法国市场](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 8.0/10

注重隐私的公共 DNS 解析器 Quad9 宣布，由于法院命令要求其封锁特定域名并对不遵守行为处以罚款，将于 2024 年 11 月 24 日后停止在法国的服务。这一决定源于与索尼音乐娱乐有限公司的法律纠纷，索尼通过 VPN 绕过 Quad9 的 geoIP 封锁并成功主张 Quad9 未遵守命令，导致 Quad9 被处以藐视法庭罚款。 这为要求 DNS 解析器对其不托管的内容负责开创了先例，可能迫使其他公共 DNS 提供商实施封锁或退出市场，从而导致互联网碎片化并削弱注重隐私的服务。它凸显了版权执法与互联网基础设施开放、全球性之间日益加剧的紧张关系。 Quad9 计划在 11 月 24 日后使用 geoIP 过滤器封锁法国用户，但其 CTO 承认 geoIP 封锁不足以选择性地拒绝解析某些域名。此案与法国广播公司针对谷歌、Cloudflare 和思科采取的类似行动如出一辙，思科已在两年前退出该市场。

hackernews · farrokhi · Oct 22, 14:32 · [社区讨论](https://news.ycombinator.com/item?id=50195959)

**背景**: Quad9 是一个免费的公共 DNS 解析器，可拦截恶意域名并强调用户隐私。DNS 解析器将人类可读的域名转换为 IP 地址，充当互联网的目录。在法国，法院已命令 DNS 提供商封锁盗版网站，不遵守规定可能导致罚款。此案是政府及版权所有者向中间商施压以执行内容封锁的更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quad9.net/">Quad9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://www.unveildns.com/blog/geo-blocking-dns.html">Geo - blocking DNS by client country — UnveilDNS Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一法律结果表示不满，将 DNS 解析器比作因列出罪犯号码而受罚的电话簿。一些人建议 DNS 解析器应停止解析起诉它们的公司的域名，另一些人则指出这与思科早前退出法国的情况相似。

**标签**: `#DNS`, `#privacy`, `#legal`, `#internet governance`, `#France`

---

<a id="item-2"></a>
## [NVIDIA OpenShell：面向自主 AI 代理的安全运行时](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA 发布了 OpenShell 0.1.0，这是一个开源运行时，通过对文件访问、软件包安装、API 调用和凭据使用执行声明式策略，为成群的自主 AI 代理提供沙箱隔离。该运行时结合了沙箱执行、受控服务访问、凭据管理和形式化策略分析，且无需重写代理。 随着组织部署需要广泛访问文件、API 和凭据的自主代理集群，OpenShell 解决了防止数据外泄和未授权操作的关键安全缺口。Cadence、Slack 和 Gecko 等公司的采用表明，运行时治理正成为企业 AI 代理部署的基础层。 OpenShell 在外部执行策略，使代理能够读取文件、安装软件包和调用 API，而无需不受限制地访问数据、机密或网络；然而，社区指出平衡能力与安全仍是一个固有的权衡，即使有基于域的网络限制，防止数据外泄（例如代码库泄露）仍是一个未解决的挑战。

hackernews · niemandhier · Oct 22, 17:44 · [社区讨论](https://news.ycombinator.com/item?id=50198675)

**背景**: 自主 AI 代理越来越多地用于执行编码、研究和系统管理等复杂任务，但它们对工具和数据的广泛访问带来了意外或恶意数据外泄的风险。传统容器共享主机内核，通常不足以隔离 AI 生成的代码，因此出现了微虚拟机、gVisor 和硬件强制隔离等沙箱方法。OpenShell 是 NVIDIA 进入这一领域的举措，提供了一个策略驱动的运行时，管理代理的执行、可见性和推理路由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/">Add Runtime Controls to AI Agents with NVIDIA OpenShell</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor & isolation ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍认为在容器中运行代理至关重要，一些人分享了 iron proxy 等用于网络限制和凭据交换的实用替代方案。怀疑者认为 OpenShell 关于在不牺牲安全的情况下提供完整能力的承诺是自相矛盾的，其他人则强调防止数据外泄仍未解决；一位用户报告在 OpenShell 之上构建了一层用于团队策略和安全的 git 使用，并指出没有边界的目标寻求型代理是真实的风险。

**标签**: `#AI agents`, `#security`, `#sandboxing`, `#NVIDIA`, `#runtime`

---

<a id="item-3"></a>
## [HackiOS 通过 QEMU 在安卓手机上启动完整 iOS 16.5 固件](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 8.0/10

一个名为 HackiOS 的项目展示了如何在安卓设备（包括 POCO X5 Pro 5G 和部分小米机型）上，通过 QEMU 和定制的 XNU 内核启动完整的 iOS 16.5 固件。该项目提供了自己的 EFI 加载器、UEFI 移植以及苹果闭源驱动的替代品，使得未经修改的 iOS 16.5 用户空间能够从 launchd 到 SpringBoard 再到应用程序完整运行。 这是一项极具新颖性的技术成就，推动了虚拟化和逆向工程的边界，表明苹果专有的 iOS 软件栈可以在非苹果硬件上运行。它可能对安全研究、设备再利用以及关于软件自由和硬件锁定的持续辩论产生重大影响。 该项目更像是一个研究平台而非日常使用的 ROM：每次会话持续一定秒数，之后内核返回加载器并交出日志。它依赖 QEMU 进行系统仿真，并在兼容层上包含一个 Linux Wi-Fi 驱动，但可能缺乏完整的硬件加速，性能上可能存在限制。

hackernews · aghuang · Oct 22, 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50196718)

**背景**: XNU 是苹果的混合内核，结合了 Mach 微内核和 BSD 组件，是 macOS、iOS 及其他苹果操作系统的基础。QEMU 是一个开源虚拟化工具，可以模拟硬件，使操作系统能在不同架构上运行。iOS 固件（IPSW 文件）包含完整的操作系统镜像，但通常通过硬件检查和签名组件锁定在苹果设备上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XNU_kernel">XNU kernel</a></li>
<li><a href="https://www.qemu.org/docs/master/system/introduction.html">Introduction — QEMU documentation</a></li>
<li><a href="https://github.com/oosexgang/hackios-xnu-kernel">GitHub - oosexgang/hackios- xnu - kernel · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人对在 QEMU 和安卓硬件上运行 iOS 的技术壮举表示赞赏，而另一些人则担心可能被滥用（例如制造假 iPhone），并质疑项目的动机。一位评论者指出网站设计不佳但赞扬了成就，另一位则猜测 AI 安全措施可能影响了项目的发布。

**标签**: `#iOS`, `#Android`, `#virtualization`, `#QEMU`, `#reverse-engineering`

---

<a id="item-4"></a>
## [任天堂 Switch 2 通过软件漏洞被破解](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 8.0/10

一位开发者发布博客文章，详细介绍了首个仅通过软件实现的任天堂 Switch 2 破解方法，该方法可在最新固件上运行，并已通过《马力欧卡丁车世界》的模组演示。据报道，该漏洞利用了与 SmileBASIC 4 相关的漏洞，并在 LLM 驱动的自动化工具协助下完成。 此次破解发生在游戏机发布仅 16 个月后，可能为自制软件、游戏模组以及潜在的游戏转储打开大门，从而使 Switch 2 独占游戏能在任意硬件上运行——这对任天堂来说是最坏的情况。它还凸显了 LLM 和自动化如何加速硬件安全研究。 该漏洞仅通过软件实现，可在最新固件上运行，利用了与 SmileBASIC 4 相关的漏洞。破解已通过《马力欧卡丁车世界》的模组演示，但距离成为常见的盗版手段还很远。

hackernews · ledoge · Oct 22, 08:01 · [社区讨论](https://news.ycombinator.com/item?id=50192536)

**背景**: 破解游戏机意味着绕过其安全措施以运行非官方软件，例如自制应用程序、模组或盗版游戏。任天堂 Switch 2 是任天堂于 2025 年发布的最新游戏机，其安全性一直是黑客关注的重点。SmileBASIC 4 是任天堂平台上可用的编程环境，此类软件中的漏洞有时可被利用以获取更广泛的系统访问权限。LLM 越来越多地用于逆向工程，以自动化反编译和漏洞发现等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kotaku.com/nintendo-switch-2-jailbreak-hack-exploit-piracy-homebrew-emulation-modding-2000748784">The Switch 2 Has Been Jailbroken For The First Time</a></li>
<li><a href="https://www.androidauthority.com/nintendo-switch-2-software-jailbreak-3727013/">Nintendo Switch 2 jailbreak could open the door to a world of mods</a></li>
<li><a href="https://github.com/ram-elgov/awesome-llm-reverse-engineering">Awesome‑LLM‑Reverse‑Engineering - GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术壮举表示惊叹，一些人预测 Switch 2 游戏转储可能在几小时内出现，从而通过重编译/反编译让独占游戏在任意硬件上运行。其他人则强调了巧妙的自动化设置，包括用于控制器输入和 HDMI 捕获的 JetKVM，以及用于在游戏机崩溃时按下电源按钮的 SwitchBot Bot。少数人质疑在 Codex 的限制下如何将其用于安全研究，而其他人则强调人类研究者的专业知识仍然至关重要。

**标签**: `#console hacking`, `#security research`, `#Nintendo Switch 2`, `#LLM automation`, `#reverse engineering`

---

<a id="item-5"></a>
## [eMudhra 因弱密钥事件退出全球 SSL/TLS 证书业务](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 8.0/10

印度证书颁发机构 eMudhra 宣布，其董事会在一名研究人员证明其八个中间 CA 私钥弱到可被破解的五天后，决定退出全球 SSL/TLS 证书业务。该公司将继续提供吊销和证书状态服务，直到所有已签发证书过期或被替换，并将完成对浏览器根计划的剩余承诺，包括一份完整的根本原因报告。 这一事件凸显了证书颁发机构健壮的密钥生成和透明度至关重要，因为弱密钥可能允许攻击者为任何域名伪造证书并拦截流量。eMudhra 的退出影响了其全球客户，并突显了浏览器根计划和安全社区对 CA 问责制的日益严格的审查。 被攻破的密钥是中间 CA 私钥，其弱点允许研究人员破解其中八个，Cloudflare 的博客和 Chrome 通过 Mozilla Bugzilla 的公开质询详细说明了这一点。eMudhra 声称其全球 SSL/TLS 基础设施与其他业务分开运行，但批评者质疑“没有从受影响的 CA 签发终端实体证书”的说法，因为任何人都可以从该 CA 签发证书。

hackernews · bo0tzz · Oct 22, 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50195110)

**背景**: 证书颁发机构（CA）颁发数字证书，将公钥与域名绑定，从而实现 HTTPS 和安全通信。每个 CA 使用其私钥签署证书，如果该私钥较弱或被攻破，攻击者可以创建欺诈性证书来冒充网站。浏览器根计划（如 Chrome 的根计划）为 CA 设定严格的安全要求，并在发生事件时可以不信任它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise/">8 eMudhra certificates are compromised. | Cloudflare Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者强烈批评 eMudhra 的安全实践和透明度，一些人嘲笑该公司的回应，并质疑其“没有签发终端实体证书”的说法。讨论还强调了 Chrome 对 eMudhra 的严厉公开质询，并链接到 Mozilla Bugzilla 的评论，总体情绪是这一事件揭示了严重的问责问题。

**标签**: `#SSL/TLS`, `#certificate-authority`, `#security`, `#PKI`, `#industry-news`

---

<a id="item-6"></a>
## [Anthropic 将 Agent Skills 标准捐赠给 Agentic AI 基金会](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 8.0/10

Anthropic 宣布将其 Agent Skills 标准捐赠给 Linux 基金会旗下的 Agentic AI 基金会（AAIF），这是继此前捐赠 Model Context Protocol（MCP）之后的又一举措。AAIF 由 Anthropic、Block 和 OpenAI 于去年共同创立，旨在托管厂商中立的智能体 AI 标准。 此举标志着智能体工具正朝着标准化和互操作性方向推进，这对基于这些协议构建应用的开发者具有很高价值。通过将 Agent Skills 置于厂商中立的基金会之下，Anthropic 旨在保持标准的开放性和社区驱动性，减少智能体 AI 生态的碎片化。 AAIF 于 2025 年 12 月成立，创始贡献包括 Anthropic 的 MCP、Block 的 goose 和 OpenAI 的 AGENTS.md。Simon Willison 指出，他去年 12 月就预测了这一捐赠，当时 Anthropic 首次宣布技能为开放标准，他还使用 datasette-mcp 插件让 Claude 找到了那篇帖子。

rss · Simon Willison · Oct 22, 18:09

**背景**: Agent Skills 是 Anthropic 开发的一种格式，允许 AI 智能体使用模块化能力来更可靠地处理复杂的现实世界任务。Model Context Protocol（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范大语言模型等 AI 系统连接外部工具和数据源的方式。Linux 基金会是一个托管众多开源项目和标准的非营利组织，AAIF 是其推动智能体 AI 开放互操作标准的倡议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">Donating Agent Skills to the Agentic AI Foundation \ Anthropic</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#open-standards`, `#anthropic`, `#ai-governance`, `#developer-tools`

---

<a id="item-7"></a>
## [Anthropic 发布 Claude API 2026-10-21 版本，移除温度等采样参数](https://x.com/ClaudeDevs/status/2113013247209021918) ⭐️ 8.0/10

Anthropic 发布了 Claude API 版本 2026-10-21，这是自 2023 年以来的首次正式版本更新，移除了 temperature、top_p 和 top_k 参数，继续传入这些参数将返回 400 错误。SDK 和 ant CLI 现在默认使用新版本，认证头改为 Authorization: Bearer，而旧版 2023-06-01 仍可用且未被弃用。 对于依赖采样参数来控制输出随机性和创造性的开发者来说，这是一个破坏性变更，也标志着平台的重大转变，可能促使团队重新思考如何调整模型行为。切换到 Bearer 认证也会影响手动构建请求头的集成。 新版本可在 Claude API、AWS 上的 Claude Platform、Microsoft Foundry 和 Google Cloud 上使用，但在 Amazon Bedrock 上仅适用于 Claude 4.7 及更高版本的模型。移除 temperature、top_p 和 top_k 意味着开发者无法再通过这些参数直接调整响应的随机性。

telegram · zaihuapd · Oct 22, 03:54

**背景**: Temperature、top_p 和 top_k 是大型语言模型 API 中常见的采样参数，用于控制生成文本的随机性和多样性。Temperature 缩放概率分布，top_p 将采样限制在累积概率质量内，top_k 则将采样限制在前 k 个 token。Bearer 认证是一种 HTTP 认证方案，令牌通过 Authorization 头发送，广泛用于 API 访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/versioning">Versions - Claude Platform Docs - Anthropic</a></li>
<li><a href="https://freeacademy.ai/blog/llm-parameters-temperature-top-p-top-k-max-tokens">LLM Parameters Explained: Temperature , Top - P , Top - K</a></li>
<li><a href="https://reqbin.com/req/5k564bhv/get-request-bearer-token-authorization-header-example">How do I Send a Request with Bearer Token Authorization Header ?</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude API`, `#breaking changes`, `#LLM`, `#API design`

---

<a id="item-8"></a>
## [澳大利亚联邦法院裁定苹果和谷歌滥用市场支配地位](https://t.me/zaihuapd/44612) ⭐️ 8.0/10

2025 年 8 月 12 日，澳大利亚联邦法院作出口头裁决，认定苹果和谷歌在应用商店及支付系统领域滥用市场支配地位，实质性削弱了竞争，违反了当地竞争法。 该裁决可能迫使苹果和谷歌向第三方支付提供商开放其应用商店支付系统，从而重塑开发者经济，并为全球针对应用商店守门人的反垄断行动树立先例。 完整判决尚未公布，因涉及保密争议而暂时封存，苹果和谷歌已表示将对部分裁决内容提出异议；Epic Games 称此次判决是开发者和消费者的胜利。

telegram · zaihuapd · Oct 22, 06:54

**背景**: 全球范围内对应用商店的反垄断审查日益加强，监管机构认为苹果的 App Store 和谷歌的 Play 商店在应用分发和应用内支付方面拥有垄断地位。类似案件，如美国的 Epic Games 诉苹果案以及欧盟和其他司法管辖区的多项调查，都对这种行为提出了挑战。澳大利亚的裁决加大了对科技巨头改变其商业模式的压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.21jingji.com/article/20210502/herald/ef0a229a83d7410c60db2cdec3f239dc_zaker.html">解读丨欧盟为何 反 垄 断 剑指苹果 应 用 商 店 ？ 指控关键点有哪些？ - 21...</a></li>
<li><a href="https://36kr.com/p/1396370413271812">Epic ...</a></li>
<li><a href="https://juejin.cn/post/7486465253817253924">Google Play 应 用 商 店 结算 系 统 被罚款2020...</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#app-store`, `#apple`, `#google`, `#regulation`

---

<a id="item-9"></a>
## [特斯拉 Cybercab 在北美投产，无方向盘无人驾驶出租车](https://t.me/zaihuapd/44614) ⭐️ 8.0/10

特斯拉宣布，其专为自动驾驶设计的 Cybercab 已在北美启动量产。这款车型取消了方向盘、踏板和后视镜，完全围绕车载 AI 驾驶系统打造，是特斯拉 Robotaxi 网约车业务的核心车型。 这是大型车企首批完全取消手动控制装置的量产车型之一，对自动驾驶行业和特斯拉的 Robotaxi 计划都具有里程碑意义。若进展顺利，可能加速行业向无人驾驶网约车转型，并促使监管机构和竞争对手加快调整。 Cybercab 是一款双座纯电 Robotaxi，采用纯视觉传感器方案，并且没有后窗和任何手动控制装置。其实际落地仍取决于监管机构对无方向盘车辆的批准，而美国的相关规则目前才刚刚开始明确。

telegram · zaihuapd · Oct 22, 07:54

**背景**: 特斯拉一直在推进 Robotaxi 网约车服务，并于 2025 年在得克萨斯州投放了首批车队，而 Cybercab 正是为该网络量身打造的车型。美国传统联邦安全标准要求车辆配备方向盘和踏板等手动控制装置，因此完全无人驾驶车辆需要监管豁免或规则更新。近期监管机构已开始批准无方向盘的 Robotaxi，例如亚马逊的 Zoox，表明规则正在逐步跟上技术发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://apnews.com/article/zoox-nhtsa-robotaxi-steering-wheel-1bdb3bb8ecc80a23721504315cfa50ce">Some robotaxis approved to operate without steering wheels ...</a></li>
<li><a href="https://www.axios.com/2026/03/18/robotaxi-autonomous-av-steering-wheel">U.S. paves road for vehicles with no steering wheel - Axios</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous vehicles`, `#Robotaxi`, `#Cybercab`, `#AI`

---

<a id="item-10"></a>
## [研究：关闭 ACR 后智能电视仍上报数据](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 8.0/10

一项针对 10 家厂商的 12 台智能电视、共 5943 次受控实验的研究发现，部分机型在用户于设置中关闭自动内容识别（ACR）后，仍会继续发送与内容相关的数据。有两个平台以未加密方式传输观看信息：VIDAA OS 通过明文 MQTT 发送包含不可重置设备 ID 和音频指纹的数据，而 Vizio 的 WatchFree+则在未加密的 DNS 查询中暴露节目名称。 这项研究表明，选择退出 ACR 并不能可靠地阻止智能电视上报观看数据，削弱了用户对隐私控制的信任。这些发现影响数百万智能电视用户，并凸显了在消费设备数据收集方面加强监管和透明度的必要性。 该研究在 12 台电视上进行了 5943 次受控实验，发现 VIDAA OS 使用明文 MQTT 传输不可重置的设备 ID 和音频指纹，而 Vizio 的 WatchFree+通过未加密的 DNS 查询和与流媒体提供商 Amagi 相关的 TLS 服务器名称字段泄露节目名称。用户无法通过现有设置关闭这些传输。

telegram · zaihuapd · Oct 22, 09:50

**背景**: 自动内容识别（ACR）是大多数智能电视内置的软件，它会截取屏幕上任何内容（包括 DVD、游戏和有线电视）的截图或音频片段，并发送到服务器以识别用户正在观看的内容。这些数据用于定向广告和收视分析。MQTT 是一种常用于物联网设备的轻量级消息协议，未加密时可能将数据暴露给网络观察者。DNS 查询用于将域名解析为 IP 地址，除非使用 DNS-over-HTTPS，否则通常未加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/10/does-opting-out-of-smart-tv-tracking-work-research-finds-suspicious-traffic/">Does opting out of smart TV tracking work? Research... - Ars Technica</a></li>
<li><a href="https://cyberinsider.com/smart-tv-privacy-study-finds-tracking-persists-even-when-opting-out/">Smart TV privacy study finds tracking persists even when ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/MQTT">MQTT - Wikipedia</a></li>

</ul>
</details>

**标签**: `#privacy`, `#smart-tv`, `#ACR`, `#data-leak`, `#security-research`

---

<a id="item-11"></a>
## [甲骨文发布 Java SE 高危漏洞安全警报](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 8.0/10

甲骨文针对 CVE-2026-91403 发布安全警报，该漏洞位于 Java SE 的 JSSE 组件，CVSS 评分高达 9.1，攻击者无需身份验证即可远程利用。受影响版本包括 Java SE 8u511、11.0.33、17.0.21、21.0.13、25.0.5、27.0.1 以及多个 GraalVM 版本，目前补丁已发布。 该漏洞无需身份验证即可远程利用，且影响广泛部署的平台，可能危及无数基于 Java 的应用程序的数据机密性和完整性。使用受影响版本的组织应优先修补以防范潜在攻击。 该漏洞存在于负责安全通信的 JSSE 组件中，成功利用可能导致数据机密性和完整性受损。甲骨文已发布补丁，并敦促用户立即升级至受支持版本。

telegram · zaihuapd · Oct 22, 12:30

**背景**: JSSE（Java 安全套接字扩展）是一个 Java API，使用 SSL 和 TLS 协议实现安全的互联网通信，为传输中的数据提供加密和身份验证。它是 Java 运行时环境的核心组件，广泛用于 Web 服务器、客户端和企业应用程序中保护敏感信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/alert-cve-2026-91403.html">Oracle Security Alert Advisory - CVE - 2026 - 91403</a></li>
<li><a href="https://en.wikipedia.org/wiki/Java_Secure_Socket_Extension">Java Secure Socket Extension - Wikipedia</a></li>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html">Java Secure Socket Extension ( JSSE ) Reference Guide</a></li>

</ul>
</details>

**标签**: `#security`, `#Java`, `#vulnerability`, `#Oracle`, `#CVE`

---

<a id="item-12"></a>
## [333 个被植入后门的 Tor 出口节点下线](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

一名 Tor 运营者扫描了约 3000 个出口中继，发现 333 个被植入 Ebury 后门，约占所有出口的 10%。这些节点于 10 月 4 日被标记为 BadExit，次日全部下线。 此次事件影响了约十分之一的 Tor 出口能力，攻击者可窃取 SSH 凭据并拦截那些连接恰好经过受感染中继的用户的未加密邮件流量。这凸显了依赖 Tor 出口节点传输敏感流量的风险，并强调了端到端加密的重要性。 该后门将 22 端口的 SSH 连接劫持到 12 台拦截服务器以窃取凭据，攻击者自 8 月起已入侵这些服务器，并屏蔽部分端口以专门收集未加密的邮件流量。最初的入侵途径尚无定论。

telegram · zaihuapd · Oct 22, 14:52

**背景**: Ebury 是一种针对 Linux 服务器的 OpenSSH 后门和凭据窃取工具，最早出现于 2009 年，用于维持僵尸网络和窃取凭据。Tor 出口节点是流量离开 Tor 网络的节点，BadExit 标记会告知客户端避免使用该中继进行出口连接。当出口节点被入侵时，攻击者可以监控或操纵通过该节点离开的流量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://attack.mitre.org/software/S0377/">Ebury, Software S0377 | MITRE ATT&CK®</a></li>
<li><a href="https://tor.stackexchange.com/questions/253/what-specifically-causes-an-exit-to-get-a-bad-exit-flag">directory - What specifically causes an Exit to get a Bad Exit flag?</a></li>

</ul>
</details>

**标签**: `#Tor`, `#security`, `#backdoor`, `#Ebury`, `#network-security`

---

<a id="item-13"></a>
## [禁运的 Nvidia B300 芯片现身中国国有网络](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

中国国资控股的半导体租赁集团据称为 AI 公司荣耀视图科技融资购入 32 台搭载 Nvidia B300 芯片的华硕服务器，这属于一笔总额超 30 亿元、涉及 700 余台服务器的大交易，计划部署于中国移动宁夏枢纽。备案引发关注后，该租赁集团重新提交文件并抹去了硬件描述，Nvidia 表示正联合代工伙伴展开调查。 该报道暗示可能违反了美国对最先进 Nvidia AI 芯片的出口管制，这可能引发更严格的执法并加剧中美科技紧张关系。它还引发了对出口管制有效性和 AI 硬件供应链完整性的质疑，影响政策制定者、芯片制造商和云服务提供商。 B300 属于美国最严格的出口管制层级，对华基本禁运；这些服务器为华硕品牌，是一笔 30 亿元、700 余台服务器交易的一部分。Nvidia 表示正与代工伙伴调查，华硕则声称遵守出口管制。

telegram · zaihuapd · Oct 22, 15:22

**背景**: Nvidia B300 是面向 AI 工作负载的高端 Blackwell 架构 GPU，美国出口规则限制其对华销售，以防止军事和战略用途。中国移动宁夏枢纽是位于中卫的大型数据中心园区，利用廉价绿色电力和自然冷却支持 AI 计算。中国企业越来越多地通过租赁安排和第三方中介获取受限硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neuralwired.com/2026/06/05/nvidia-chip-export-controls-china-2026/">Nvidia & US Chip Export Controls: Complete 2026 Guide</a></li>
<li><a href="https://gpusmith.com/articles/en/nvidia-gpu-export-restrictions">NVIDIA GPU Export Restrictions: Current US Chip Controls 2026</a></li>
<li><a href="https://www.datacentermap.com/china/zhongwei/china-mobile-ningxia/">China Mobile Ningxia Data Center in Zhongwei | Fengyun Road</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#export controls`, `#China`, `#AI hardware`, `#semiconductor`

---