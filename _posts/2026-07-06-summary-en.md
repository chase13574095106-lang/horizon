---
layout: default
title: "Horizon Summary: 2026-07-06 (EN)"
date: 2026-07-06
lang: en
---

> From 27 items, 6 important content pieces were selected

---

1. [OpenWrt One: Open Hardware Router Gains Community Traction](#item-1) ⭐️ 8.0/10
2. [Anthropic Finds Global Workspace in Language Models](#item-2) ⭐️ 8.0/10
3. [FBI Uses Microsoft GDID to Track Hacker Despite VPN](#item-3) ⭐️ 8.0/10
4. [Bilibili Sends Legal Notice to BiliRoaming Open Source Project](#item-4) ⭐️ 8.0/10
5. [Tencent Open-Sources Hy3 Preview MoE Model](#item-5) ⭐️ 8.0/10
6. [SpaceX Falcon 9 Debris Creates Metal Pollution in Upper Atmosphere](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenWrt One: Open Hardware Router Gains Community Traction](https://openwrt.org/toh/openwrt/one) ⭐️ 8.0/10

The OpenWrt One, an open hardware router running OpenWrt by default, has been released at around $89-$106, featuring dual-band Wi-Fi 6, two Ethernet ports, and three USB ports. This device offers a reliable, customizable, and long-lasting alternative to commercial routers, extending device life and providing advanced capabilities through open-source firmware. The OpenWrt One is based on the MediaTek Filogic 820 chipset and includes 1GB of RAM, with a USB-C console port for recovery. An OpenWrt Two with Wi-Fi 7 is also in development.

hackernews · peter_d_sherman · Jul 6, 18:23 · [Discussion](https://news.ycombinator.com/item?id=48808482)

**Background**: OpenWrt is a highly customizable open-source firmware for routers, originally derived from the Linksys WRT54G. It allows users to replace stock firmware to gain features like VPNs, VLANs, and better security updates, extending the useful life of hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/openwrt/comments/1h4uuzr/opensource_openwrt_one_router_released_at_89/">r/openwrt on Reddit: Open-source OpenWrt One router released at $89 — 'hacker-friendly device' sports two Ethernet ports, three USB ports, with dual-band Wi-Fi 6</a></li>
<li><a href="https://docs.banana-pi.org/en/OpenWRT-One/BananaPi_OpenWRT-One">Banana Pi OpenWrt One Router | BananaPi Docs</a></li>
<li><a href="https://openwrt.org/toh/openwrt/one">[OpenWrt Wiki] OpenWrt One</a></li>

</ul>
</details>

**Discussion**: Community comments express strong interest, with users praising the price and potential for reliability. Some note that OpenWrt installation can be complex, but the open hardware approach is seen as a positive step. Comparisons with other solutions like OPNSense are also discussed.

**Tags**: `#OpenWrt`, `#open hardware`, `#router`, `#networking`, `#DIY`

---

<a id="item-2"></a>
## [Anthropic Finds Global Workspace in Language Models](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic's research identifies a shared 'global workspace' (J-Space) in language models that integrates information across different contexts, analogous to conscious awareness in humans. This discovery provides a new lens for understanding how language models achieve coherent reasoning and may inform future interpretability and safety research by revealing a central hub for information integration. The J-Space is defined as the subspace of the model's residual stream where changes most affect final logits, and it appears to be shared across diverse inputs and tasks.

hackernews · in-silico · Jul 6, 17:44 · [Discussion](https://news.ycombinator.com/item?id=48808002)

**Background**: Global Workspace Theory (GWT), proposed by Bernard Baars in 1988, is a cognitive framework for consciousness where a central workspace broadcasts information to specialized modules. Anthropic's interpretability team investigates the internal workings of language models to improve AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_Workspace_Theory">Global workspace theory - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/tracing-thoughts-language-model">Tracing the thoughts of a large language model \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/team/interpretability">Interpretability Research \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the research but also raise technical critiques, such as whether the comparison to conscious awareness is justified, and note connections to prior work like layer duplication for math improvement.

**Tags**: `#AI research`, `#language models`, `#neural networks`, `#interpretability`, `#Anthropic`

---

<a id="item-3"></a>
## [FBI Uses Microsoft GDID to Track Hacker Despite VPN](https://www.itnews.com.au/news/microsoft-device-telemetry-key-to-unmasking-alleged-scattered-spider-hacker-627148) ⭐️ 8.0/10

The FBI arrested 19-year-old Peter Stokes, a member of the Scattered Spider hacking group, by using Microsoft's Global Device ID (GDID) to link his Windows device to the crime, even though he used a VPN to hide his IP address. This case reveals that Microsoft's GDID can be used by law enforcement to unmask users who rely on VPNs for anonymity, raising significant privacy concerns about persistent device tracking in Windows. The GDID is a persistent identifier generated during Windows installation that remains unchanged even after updates, and users cannot easily modify it through normal settings; only a full OS reinstall generates a new GDID.

telegram · zaihuapd · Jul 6, 04:15

**Background**: Microsoft's Global Device ID (GDID) is a unique 128-bit identifier assigned to each Windows device during initial setup. It is used for telemetry and diagnostic purposes, but its persistence makes it a powerful tracking tool. In this case, the FBI cross-referenced GDID records with login data from Snapchat, Apple, and Facebook to confirm the suspect's identity.

<details><summary>References</summary>
<ul>
<li><a href="https://uk.pcmag.com/security/166029/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device-id">A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows...</a></li>
<li><a href="https://securityonline.info/microsoft-gdid-tracking/">Microsoft GDID Tracking: How Windows Caught a Hacker</a></li>
<li><a href="https://yro.slashdot.org/story/26/07/05/1633210/windows-11-identifier-code-used-to-arrest-19-year-old-over-alleged-ransomware-spree">Windows 11 Identifier Code Used to Arrest 19-Year-Old Over Alleged ...</a></li>

</ul>
</details>

**Discussion**: Comments on Slashdot and other forums express concern over Microsoft's surveillance capabilities, with some users questioning the legality of such tracking and others noting that users should be aware of the GDID's existence and consider using privacy-focused operating systems.

**Tags**: `#privacy`, `#security`, `#Microsoft`, `#law enforcement`, `#device tracking`

---

<a id="item-4"></a>
## [Bilibili Sends Legal Notice to BiliRoaming Open Source Project](https://github.com/yujincheng08/BiliRoaming) ⭐️ 8.0/10

Bilibili, through a law firm, sent a cease-and-desist letter to the BiliRoaming open source project, demanding it stop reverse engineering and remove code that bypasses regional restrictions and paid content protections. This legal action highlights the ongoing tension between platform copyright enforcement and open source reverse engineering, potentially setting a precedent for how similar projects are treated in China. The letter specifically cites behaviors such as hooking playback authentication, rewriting paid bangumi to be viewable, bypassing secure transport locks, and altering CDN origin. The project is required to respond within two days.

telegram · zaihuapd · Jul 6, 08:21

**Background**: BiliRoaming is an Xposed module for Android that removes regional restrictions on Bilibili's bangumi (anime) content and provides other features. Xposed is a framework that allows modules to modify app behavior at runtime without altering APK files. Reverse engineering involves analyzing software to understand its inner workings, often to create compatible or unauthorized modifications.

<details><summary>References</summary>
<ul>
<li><a href="https://modules.lsposed.org/module/me.iacn.biliroaming/">哔哩漫游/ BiliRoaming · Xposed Module Repository</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open source`, `#reverse engineering`, `#legal`, `#Bilibili`, `#Xposed`

---

<a id="item-5"></a>
## [Tencent Open-Sources Hy3 Preview MoE Model](https://t.me/zaihuapd/42385) ⭐️ 8.0/10

Tencent has officially released and open-sourced the Hy3 preview language model, a Mixture-of-Experts (MoE) architecture with 295B total parameters, 21B active parameters, and support for 256K context length. This release advances open-source AI by providing a large-scale MoE model optimized for reasoning and agent tasks, with significant inference speed improvements (54% reduction in first-token latency) that can benefit developers building complex applications. The model's core capabilities focus on complex reasoning and agent applications, showing notable improvements in math, science, and code generation tasks. It is already integrated into Tencent products like Yuanbao and Tencent Docs.

telegram · zaihuapd · Jul 6, 10:09

**Background**: A Mixture-of-Experts (MoE) model uses multiple specialized sub-models (experts) with a router to select which experts to activate for each input, enabling larger total parameters while keeping inference efficient. First-token latency (TTFT) measures the time to generate the first output token, a key metric for real-time applications. Agent applications refer to AI systems that can autonomously plan and execute tasks using tools and reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/81886457827">混合专家模型（Mixture of Experts，MoE）详解（附代码）</a></li>
<li><a href="https://blog.csdn.net/qq_25295605/article/details/141140475">如何评判大模型的输出速度？ 首 Token 延 迟 和其余 Token ... -CSDN博客</a></li>
<li><a href="https://blog.csdn.net/DEVELOPERAA/article/details/150848357">一文搞懂多 智 能 体 ：OpenManus（ Agent +Flow+Tool+Prompt...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#MoE`, `#Tencent`, `#open-source`

---

<a id="item-6"></a>
## [SpaceX Falcon 9 Debris Creates Metal Pollution in Upper Atmosphere](https://t.me/zaihuapd/42387) ⭐️ 8.0/10

A new study published in Communications Earth & Environment on February 19, 2026, detected a lithium atom plume at 96 km altitude following the uncontrolled re-entry of a SpaceX Falcon 9 upper stage over Europe, with lithium concentrations spiking 10-fold. This is the first direct measurement of metal pollution from rocket re-entry, revealing a novel environmental impact of the growing space industry that could threaten the ozone layer and alter upper atmospheric chemistry. The lithium plume was detected using high-precision LIDAR from a ground station in Germany, measuring about 3 atoms per cubic centimeter. Previous studies have shown that metals like lithium, aluminum, copper, and lead from spacecraft re-entry already exceed natural cosmic dust influx.

telegram · zaihuapd · Jul 6, 11:17

**Background**: When rockets re-enter Earth's atmosphere, they burn up and release metals into the upper atmosphere. Unlike space debris falling to the ground, these vaporized metals can persist at high altitudes and potentially affect atmospheric processes, including ozone depletion. The Falcon 9 upper stage made an uncontrolled re-entry over Europe on February 19, 2025, creating a visible fireball.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s43247-025-03154-8">Measurement of a lithium plume from the uncontrolled re-entry of a Falcon 9 rocket | Communications Earth & Environment</a></li>
<li><a href="https://skyandtelescope.org/astronomy-news/rocket-reentry-leaves-lithium-in-earths-upper-atmosphere/">Rocket Reentry Leaves Lithium in Earth's Upper Atmosphere - Sky & Telescope</a></li>
<li><a href="https://www.sciencenews.org/article/rocket-reentry-metal-pollution-detected">Metal pollution from a rocket reentry detected for the first time</a></li>

</ul>
</details>

**Tags**: `#space debris`, `#atmospheric pollution`, `#SpaceX`, `#environmental impact`, `#rocket launches`

---