---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> From 27 items, 6 important content pieces were selected

---

1. [OpenWrt One：开源硬件路由器获得社区关注](#item-1) ⭐️ 8.0/10
2. [Anthropic 发现语言模型中的全局工作空间](#item-2) ⭐️ 8.0/10
3. [FBI 利用微软 GDID 追踪 VPN 黑客](#item-3) ⭐️ 8.0/10
4. [B 站向 BiliRoaming 开源项目发律师函](#item-4) ⭐️ 8.0/10
5. [腾讯开源混元 Hy3 预览版 MoE 模型](#item-5) ⭐️ 8.0/10
6. [SpaceX 猎鹰 9 号碎片在高空造成金属污染](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenWrt One：开源硬件路由器获得社区关注](https://openwrt.org/toh/openwrt/one) ⭐️ 8.0/10

OpenWrt One 是一款默认运行 OpenWrt 的开源硬件路由器，售价约 89-106 美元，配备双频 Wi-Fi 6、两个以太网端口和三个 USB 端口。 该设备为商业路由器提供了可靠、可定制且耐用的替代方案，通过开源固件延长设备寿命并提供高级功能。 OpenWrt One 基于 MediaTek Filogic 820 芯片组，配备 1GB RAM，并带有用于恢复的 USB-C 控制台端口。同时，支持 Wi-Fi 7 的 OpenWrt Two 也在开发中。

hackernews · peter_d_sherman · Jul 6, 18:23 · [社区讨论](https://news.ycombinator.com/item?id=48808482)

**背景**: OpenWrt 是一种高度可定制的路由器开源固件，最初源自 Linksys WRT54G。它允许用户替换原厂固件以获得 VPN、VLAN 和更好的安全更新等功能，从而延长硬件的使用寿命。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/openwrt/comments/1h4uuzr/opensource_openwrt_one_router_released_at_89/">r/openwrt on Reddit: Open-source OpenWrt One router released at $89 — 'hacker-friendly device' sports two Ethernet ports, three USB ports, with dual-band Wi-Fi 6</a></li>
<li><a href="https://docs.banana-pi.org/en/OpenWRT-One/BananaPi_OpenWRT-One">Banana Pi OpenWrt One Router | BananaPi Docs</a></li>
<li><a href="https://openwrt.org/toh/openwrt/one">[OpenWrt Wiki] OpenWrt One</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了浓厚兴趣，用户称赞其价格和可靠性潜力。一些人指出 OpenWrt 安装可能复杂，但开源硬件方法被视为积极的一步。还讨论了与其他解决方案（如 OPNSense）的比较。

**标签**: `#OpenWrt`, `#open hardware`, `#router`, `#networking`, `#DIY`

---

<a id="item-2"></a>
## [Anthropic 发现语言模型中的全局工作空间](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 的研究识别出语言模型中存在一个共享的“全局工作空间”（J-Space），它能够整合不同上下文的信息，类似于人类的意识觉知。 这一发现为理解语言模型如何实现连贯推理提供了新视角，并通过揭示信息整合的中心枢纽，可能为未来的可解释性和安全性研究提供参考。 J-Space 被定义为模型残差流中变化对最终 logits 影响最大的子空间，并且它似乎在不同输入和任务之间共享。

hackernews · in-silico · Jul 6, 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**背景**: 全局工作空间理论（GWT）由 Bernard Baars 于 1988 年提出，是一种意识认知框架，其中中央工作空间将信息广播给专门的模块。Anthropic 的可解释性团队研究语言模型的内部工作机制，以提升 AI 安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_Workspace_Theory">Global workspace theory - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/tracing-thoughts-language-model">Tracing the thoughts of a large language model \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/team/interpretability">Interpretability Research \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该研究表示兴奋，但也提出了技术性批评，例如与意识觉知的比较是否合理，并指出了与先前工作（如通过复制层来提升数学能力）的联系。

**标签**: `#AI research`, `#language models`, `#neural networks`, `#interpretability`, `#Anthropic`

---

<a id="item-3"></a>
## [FBI 利用微软 GDID 追踪 VPN 黑客](https://www.itnews.com.au/news/microsoft-device-telemetry-key-to-unmasking-alleged-scattered-spider-hacker-627148) ⭐️ 8.0/10

美国联邦调查局利用微软的全球设备标识符（GDID），将 19 岁的 Scattered Spider 黑客组织成员 Peter Stokes 的 Windows 设备与犯罪活动关联起来，尽管他使用了 VPN 隐藏 IP 地址，仍将其逮捕。 此案表明，执法机构可利用微软的 GDID 识别依赖 VPN 匿名上网的用户，引发了对 Windows 中持久设备追踪功能的重大隐私担忧。 GDID 是在 Windows 安装过程中生成的持久标识符，即使更新也不会改变，用户无法通过常规设置轻易修改；只有完全重装操作系统才会生成新的 GDID。

telegram · zaihuapd · Jul 6, 04:15

**背景**: 微软的全球设备标识符（GDID）是在首次设置时分配给每台 Windows 设备的唯一 128 位标识符，用于遥测和诊断目的，但其持久性使其成为强大的追踪工具。在此案中，FBI 将 GDID 记录与 Snapchat、苹果和 Facebook 的登录数据进行交叉比对，确认了嫌疑人的身份。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://uk.pcmag.com/security/166029/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device-id">A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows...</a></li>
<li><a href="https://securityonline.info/microsoft-gdid-tracking/">Microsoft GDID Tracking: How Windows Caught a Hacker</a></li>
<li><a href="https://yro.slashdot.org/story/26/07/05/1633210/windows-11-identifier-code-used-to-arrest-19-year-old-over-alleged-ransomware-spree">Windows 11 Identifier Code Used to Arrest 19-Year-Old Over Alleged ...</a></li>

</ul>
</details>

**社区讨论**: Slashdot 等论坛上的评论对微软的监控能力表示担忧，一些用户质疑此类追踪的合法性，另一些用户则指出用户应了解 GDID 的存在，并考虑使用注重隐私的操作系统。

**标签**: `#privacy`, `#security`, `#Microsoft`, `#law enforcement`, `#device tracking`

---

<a id="item-4"></a>
## [B 站向 BiliRoaming 开源项目发律师函](https://github.com/yujincheng08/BiliRoaming) ⭐️ 8.0/10

B 站委托律师事务所向开源项目 BiliRoaming 发出侵权告知函，要求其停止逆向分析并删除绕过区域限制和付费内容保护的代码。 这一法律行动凸显了平台版权保护与开源逆向工程之间的持续紧张关系，可能为类似项目在中国的处理方式树立先例。 函件特别指出包括 Hook 播放鉴权、将付费番剧改写为可观看、绕过安全传输锁定和改写 CDN 回源等行为，要求项目方在 2 日内回复。

telegram · zaihuapd · Jul 6, 08:21

**背景**: BiliRoaming 是一个 Android 上的 Xposed 模块，用于解除 B 站番剧的区域限制并提供其他功能。Xposed 是一个框架，允许模块在运行时修改应用行为而无需改动 APK 文件。逆向工程是指分析软件以理解其内部工作原理，通常用于创建兼容或未经授权的修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modules.lsposed.org/module/me.iacn.biliroaming/">哔哩漫游/ BiliRoaming · Xposed Module Repository</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>

</ul>
</details>

**标签**: `#open source`, `#reverse engineering`, `#legal`, `#Bilibili`, `#Xposed`

---

<a id="item-5"></a>
## [腾讯开源混元 Hy3 预览版 MoE 模型](https://t.me/zaihuapd/42385) ⭐️ 8.0/10

腾讯正式发布并开源混元 Hy3 预览版语言模型，该模型采用混合专家（MoE）架构，总参数量 295B，激活参数 21B，支持 256K 上下文长度。 此次发布推动了开源 AI 发展，提供了一个针对推理和智能体任务优化的大规模 MoE 模型，推理速度显著提升（首 token 延迟降低 54%），可惠及构建复杂应用的开发者。 该模型的核心能力定位于复杂推理与智能体应用，在数学、科学和代码生成任务中表现显著提升，目前已集成到元宝、腾讯文档等腾讯产品中。

telegram · zaihuapd · Jul 6, 10:09

**背景**: 混合专家模型（MoE）使用多个专门的子模型（专家）和一个路由器，为每个输入选择激活哪些专家，从而在保持推理效率的同时实现更大的总参数量。首 token 延迟（TTFT）衡量生成第一个输出 token 所需的时间，是实时应用的关键指标。智能体应用指能够自主规划并使用工具和推理执行任务的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/81886457827">混合专家模型（Mixture of Experts，MoE）详解（附代码）</a></li>
<li><a href="https://blog.csdn.net/qq_25295605/article/details/141140475">如何评判大模型的输出速度？ 首 Token 延 迟 和其余 Token ... -CSDN博客</a></li>
<li><a href="https://blog.csdn.net/DEVELOPERAA/article/details/150848357">一文搞懂多 智 能 体 ：OpenManus（ Agent +Flow+Tool+Prompt...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#MoE`, `#Tencent`, `#open-source`

---

<a id="item-6"></a>
## [SpaceX 猎鹰 9 号碎片在高空造成金属污染](https://t.me/zaihuapd/42387) ⭐️ 8.0/10

2026 年 2 月 19 日发表在《Communications Earth & Environment》上的一项新研究，在 SpaceX 猎鹰 9 号上级火箭于欧洲上空失控再入后，于 96 公里高空探测到锂原子羽流，锂浓度飙升了 10 倍。 这是首次直接测量到火箭再入产生的金属污染，揭示了不断发展的航天工业对环境的新影响，可能威胁臭氧层并改变高层大气化学。 锂羽流是通过德国地面站的高精度激光雷达探测到的，测量值约为每立方厘米 3 个原子。此前研究表明，航天器再入产生的锂、铝、铜和铅等金属已超过自然宇宙尘埃的流入量。

telegram · zaihuapd · Jul 6, 11:17

**背景**: 当火箭再入地球大气层时，它们会燃烧并将金属释放到高层大气中。与坠落地面的太空垃圾不同，这些汽化的金属可以在高空持续存在，并可能影响大气过程，包括臭氧消耗。猎鹰 9 号上级火箭于 2025 年 2 月 19 日在欧洲上空失控再入，产生了可见的火球。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s43247-025-03154-8">Measurement of a lithium plume from the uncontrolled re-entry of a Falcon 9 rocket | Communications Earth & Environment</a></li>
<li><a href="https://skyandtelescope.org/astronomy-news/rocket-reentry-leaves-lithium-in-earths-upper-atmosphere/">Rocket Reentry Leaves Lithium in Earth's Upper Atmosphere - Sky & Telescope</a></li>
<li><a href="https://www.sciencenews.org/article/rocket-reentry-metal-pollution-detected">Metal pollution from a rocket reentry detected for the first time</a></li>

</ul>
</details>

**标签**: `#space debris`, `#atmospheric pollution`, `#SpaceX`, `#environmental impact`, `#rocket launches`

---