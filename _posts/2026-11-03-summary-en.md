---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 33 items, 7 important content pieces were selected

---

1. [Astra LLM Directly Edits Qwen Weights, Boosts Math 5x](#item-1) ⭐️ 9.0/10
2. [Anthropic Files for Nasdaq IPO Under Ticker ANT](#item-2) ⭐️ 9.0/10
3. [Subvocal's smart glasses decode silent mouth movements into text using RF sensing](#item-3) ⭐️ 8.0/10
4. [Ubuntu LTS kernels remain unpatched for critical CVE-2026-98432 RCE after nearly three weeks](#item-4) ⭐️ 8.0/10
5. [ChatGPT Share Link Flaw Enables Account Takeover](#item-5) ⭐️ 8.0/10
6. [Raspberry Pi 5 Launches with 2.4GHz Cortex-A76 CPU and Dual 4K60 HDMI](#item-6) ⭐️ 8.0/10
7. [Critical Linux kernel IPv4 TCP use-after-free vulnerability (CVE-2026-98432) allows remote unauthenticated RCE](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Astra LLM Directly Edits Qwen Weights, Boosts Math 5x](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 9.0/10

Astra, an LLM, can read and write neural network weights directly without external tools, improving a small Qwen model's math performance by about 5x. It also identified and fixed a looping failure by subtracting a direction from specific MLP layers. This suggests LLMs may have a native understanding of their own weights, a step toward recursive self-improvement where AI can directly modify and enhance other models. It could fundamentally change how models are fine-tuned and interpreted. Astra traced looping behavior to a direction written by MLPs in layers 15 and 19, then subtracted that direction from 64 output columns (131,072 weights) in each layer. The base model often hit the 32,768-token limit, with 85 of its first 96 practice answers running to the limit.

hackernews · dbreunig · Nov 2, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50341174)

**Background**: Qwen is a family of open-weight large language models developed by Alibaba Cloud. Weight editing involves directly modifying a model's parameters to change its behavior, and recursive self-improvement (RSI) refers to an AI system iteratively designing more capable successors, potentially leading to an intelligence explosion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock and debate: some see this as an emergent capability, while others argue Astra was specifically trained on neural weight data for recursive self-improvement. There is skepticism about whether this is truly emergent or a result of targeted training.

**Tags**: `#LLM`, `#weight editing`, `#model interpretability`, `#recursive self-improvement`, `#Qwen`

---

<a id="item-2"></a>
## [Anthropic Files for Nasdaq IPO Under Ticker ANT](https://t.me/zaihuapd/44858) ⭐️ 9.0/10

Anthropic publicly filed for a Nasdaq IPO under the ticker 'ANT' on October 26, planning to list in mid-November with Morgan Stanley and Goldman Sachs as lead underwriters. The draft prospectus shows first-half revenue of $16.3 billion, up from $1.1 billion a year earlier, and a net loss of $80.7 billion, of which about $72 billion stems from convertible instruments and other financing tools. This is one of the largest AI IPOs ever, marking a paradigm shift in AI company maturity and public market access. It will set a benchmark for how investors value high-growth AI firms and could influence the IPO plans of rivals like OpenAI. The massive net loss is largely a non-cash accounting charge: about $72 billion comes from convertible notes, derivative liabilities, and other financial instruments, so the operating loss is far smaller than the headline figure. The filing also discloses 'catastrophic' risks related to AI safety, and 22 banks are involved in the deal.

telegram · zaihuapd · Nov 2, 15:12

**Background**: An IPO (Initial Public Offering) is the process by which a private company first sells shares to the public and lists on a stock exchange like Nasdaq. A prospectus is the formal document filed with regulators that details a company's finances, risks, and business model. Convertible instruments are financial tools (such as convertible notes) that can be converted into equity, and their accounting treatment can create large non-cash charges that distort net income.

<details><summary>References</summary>
<ul>
<li><a href="https://variety.com/2026/biz/news/anthropic-ipo-filing-ai-risks-humanity-1236931186/">Anthropic IPO Filing: AI Giant Cites 'Catastrophic' Risks</a></li>
<li><a href="https://qz.com/anthropic-ipo-filing-numbers">Anthropic IPO filing : 10 numbers from the prospectus</a></li>
<li><a href="https://applescoop.org/story/anthropic-ipo-filing-s1-revenue-risks-ticker-ant-details">Anthropic 's IPO filing : revenue , risks and 7 standout details</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#finance`, `#Nasdaq`

---

<a id="item-3"></a>
## [Subvocal's smart glasses decode silent mouth movements into text using RF sensing](https://news.ycombinator.com/item?id=50340088) ⭐️ 8.0/10

YC-backed startup The Subvocal Company (YC F26) introduced smart glasses that use radio frequency (RF) sensing to decode silent mouth movements into text at speech speed. The team, founded by Georgia Tech students Aarush and Arnav, pivoted from EMG-based sensing to RF after finding EMG impractical, and built custom low-noise RF hardware with antennas embedded in the glasses frames. This product could enable discreet, hands-free text input in public or quiet environments, benefiting accessibility users and anyone who needs silent computer interaction. It also pushes forward the field of silent speech interfaces, which have primarily been academic prototypes until now. The system works even with lips closed (internal speech) by sensing inside the mouth via RF, but cross-user generalization remains a challenge due to varying facial anatomy, requiring massive data scaling. The company has not disclosed whether inference runs on-glasses or via an app, nor detailed privacy safeguards.

hackernews · aarushyadav · Nov 2, 17:16

**Background**: Silent speech interfaces (SSIs) decode speech intent without audible sound, using signals such as muscle activity (EMG), ultrasound, or radio waves. Subvocal recognition specifically captures subtle speech movements, and prior research includes MIT Media Lab's AlterEgo and Cornell's EchoSpeech glasses. RF sensing offers an alternative to EMG by avoiding skin contact and sweat-related signal changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subvocal_speech_recognition">Subvocal speech recognition</a></li>
<li><a href="https://www.nature.com/articles/s44460-025-00010-2">Sensing technologies for silent speech interfaces - Nature</a></li>
<li><a href="https://www.allaboutcircuits.com/news/moving-sonar-onto-body-cornells-ai-eyeglasses-read-silent-speech/">Moving Sonar Onto the Body: Cornell’s AI Eyeglasses Read Silent ...</a></li>

</ul>
</details>

**Discussion**: Commenters were enthusiastic about the sci-fi-like potential and accessibility benefits, but raised practical concerns about glasses fit for non-standard face shapes, signal processing location (on-glasses vs. app), and privacy risks such as inferring sensitive personal information. Some asked for comparisons to open-source silent speech projects and whether the device works offline.

**Tags**: `#subvocal-speech`, `#smart-glasses`, `#accessibility`, `#privacy`, `#human-computer-interaction`

---

<a id="item-4"></a>
## [Ubuntu LTS kernels remain unpatched for critical CVE-2026-98432 RCE after nearly three weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 8.0/10

Ubuntu has not released fixed kernel packages for CVE-2026-98432, a critical use-after-free vulnerability in the Linux kernel's IPv4 TCP connection handling, leaving Ubuntu 22.04, 24.04, and 26.04 LTS without an official patch for almost three weeks. The flaw has a CVSS score of 9.8 and allows remote code execution. This delay leaves internet-facing and multi-tenant self-hosted systems running Ubuntu LTS kernels exposed to a remotely exploitable flaw with no vendor-supplied fix, forcing administrators to seek unofficial workarounds. It also raises questions about Canonical's patch responsiveness for critical kernel vulnerabilities. The vulnerability is a use-after-free in tcp_v4_syn_recv_sock() where ownership of ireq->ireq_opt is transferred to the child socket without copying, and AlmaLinux has already made patched kernels available in testing. Red Hat has published an interim mitigation (RHSB-2026-016) that it says reduces but does not fully prevent exposure, while Ubuntu has provided no official mitigation guidance.

hackernews · majorchord · Nov 2, 18:39 · [Discussion](https://news.ycombinator.com/item?id=50341462)

**Background**: CVE-2026-98432 is a use-after-free vulnerability in the Linux kernel's IPv4 TCP stack that can be triggered remotely, earning a critical CVSS score of 9.8. Ubuntu LTS releases are widely used for servers and cloud instances, and Canonical typically issues security notices and updated kernel packages for such flaws. A use-after-free occurs when memory is freed but still referenced, potentially allowing an attacker to execute code or crash the system.

<details><summary>References</summary>
<ul>
<li><a href="https://ubuntu.com/security/CVE-2026-98432">CVE-2026-98432 | Ubuntu</a></li>
<li><a href="https://almalinux.org/blog/2026-10-30-cve-2026-98432/">CVE-2026-98432: Patched kernels available in testing | AlmaLinux OS</a></li>
<li><a href="https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432">Ubuntu LTS kernels still unfixed for critical CVE-2026-98432</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted a concrete iptables/nftables mitigation using a U32 drop rule in raw PREROUTING, questioned why Ubuntu has delayed the patch without explanation, and raised broader concerns about unpatched Linux kernels in consumer routers and the risk of LLM-enabled exploitation. Some also criticized the lack of official mitigation guidance from Ubuntu and questioned the credibility of the source.

**Tags**: `#security`, `#linux-kernel`, `#ubuntu`, `#cve`, `#0day`

---

<a id="item-5"></a>
## [ChatGPT Share Link Flaw Enables Account Takeover](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter research team discovered a ChatGPT share link vulnerability that allowed attackers to execute code in a logged-in user's session, read private conversations, and exfiltrate data to external servers simply by having the victim open a malicious link. OpenAI fixed the issue on October 26, rated it P1, and paid a $5,000 bounty. This vulnerability affected a widely used AI product and required no user action beyond clicking a link, highlighting the security risks of rich preview features in chat applications. It underscores the importance of sandboxing and message validation in web components that handle user-supplied content. The flaw exploited message-handling logic between a preview feature and a chart component, specifically involving the third-party MathLive mathematical input component that accepted messages without adequate origin checks. OpenAI reproduced both code-execution and private-chat proof-of-concepts, escalated severity from P2 to P1, and rolled out a server-side fix across two versions of ChatGPT's web frontend.

telegram · zaihuapd · Nov 2, 10:24

**Background**: ChatGPT's Preview feature wraps user-supplied HTML in a locked-down frame on a separate origin to prevent it from reading the main chatgpt.com page. However, researchers found that communication between this restricted frame and trusted components of the main application could be abused. MathLive is a third-party library for rendering mathematical input, and its message-handling logic lacked proper origin validation, allowing an attacker to send crafted messages that the main application would trust.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>
<li><a href="https://cyberinsider.co.uk/patched-chatgpt-sharing-flaw-exposed-private-conversations/">Patched ChatGPT sharing flaw exposed private conversations</a></li>
<li><a href="https://aiweekly.co/alerts/openai-patches-chatgpt-share-link-flaw-that-hijacked-sessions">OpenAI Patches ChatGPT Share-Link Flaw That Hijacked Sessions</a></li>

</ul>
</details>

**Tags**: `#security`, `#ChatGPT`, `#vulnerability`, `#OpenAI`, `#account-takeover`

---

<a id="item-6"></a>
## [Raspberry Pi 5 Launches with 2.4GHz Cortex-A76 CPU and Dual 4K60 HDMI](https://t.me/zaihuapd/44854) ⭐️ 8.0/10

The Raspberry Pi 5 has been officially announced, featuring a 2.4GHz quad-core 64-bit Arm Cortex-A76 CPU, a VideoCore VII GPU, dual 4K60p HDMI outputs, and a 4K60p HEVC decoder. It is priced at $60 for the 4GB model and $80 for the 8GB model, plus local taxes. This is a major hardware upgrade for the widely used Raspberry Pi platform, bringing significantly faster CPU and GPU performance, dual 4K display support, and faster interfaces. It will impact hobbyists, embedded developers, educators, and industrial users who rely on Raspberry Pi for projects and products. The new features include dual-band 802.11ac Wi-Fi, Bluetooth 5.0/BLE, a high-speed microSD card interface supporting SDR104 mode, and two USB 3.0 ports that can run simultaneously at 5Gbps. The Cortex-A76 core offers up to 25% better integer and 35% better floating-point performance compared to the previous Cortex-A75.

telegram · zaihuapd · Nov 2, 12:00

**Background**: The Raspberry Pi is a series of small single-board computers developed by the Raspberry Pi Foundation to promote teaching of basic computer science in schools and in developing countries. The Raspberry Pi 5 is the latest generation, succeeding the Raspberry Pi 4 Model B released in 2019. The Cortex-A76 is a high-performance 64-bit CPU core designed by Arm, and the VideoCore VII is the integrated GPU in the Broadcom BCM2712 SoC used in the Raspberry Pi 5.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_Cortex-A76">ARM Cortex-A76</a></li>
<li><a href="https://www.notebookcheck.net/Broadcom-VideoCore-VII-Benchmarks-and-Specs.873281.0.html">Broadcom VideoCore VII - Benchmarks and Specs - Notebookcheck</a></li>

</ul>
</details>

**Tags**: `#Raspberry Pi`, `#hardware`, `#single-board computer`, `#embedded systems`, `#Arm`

---

<a id="item-7"></a>
## [Critical Linux kernel IPv4 TCP use-after-free vulnerability (CVE-2026-98432) allows remote unauthenticated RCE](https://t.me/zaihuapd/44866) ⭐️ 8.0/10

A critical use-after-free vulnerability, CVE-2026-98432, has been discovered in the Linux kernel's IPv4 TCP handshake path, affecting kernel versions 4.4 and later. A remote, unauthenticated attacker can exploit a race condition by sending crafted IPv4 TCP packets with IP options to trigger remote code execution, and a public RCE exploit for MPTCP listen ports has been released by Anthropic. This vulnerability is remotely exploitable without authentication or user interaction, making it extremely dangerous for any server exposed to the internet. Go services since version 1.24 are exposed by default because Go enables MPTCP on listen sockets by default on Linux, significantly broadening the attack surface. The vulnerability is a race condition in TCP connection request processing that leads to use-after-free, and it is not limited to MPTCP scenarios; even without MPTCP listening, similar attacks may be possible. AWS and Red Hat have published security bulletins, and patches are available in updated kernel versions.

telegram · zaihuapd · Nov 3, 02:37

**Background**: Use-after-free is a memory safety flaw where a program accesses memory after it has been freed, potentially allowing an attacker to execute arbitrary code. MPTCP (Multipath TCP) is an extension of TCP that allows a connection to use multiple network paths simultaneously for better throughput and reliability. Go 1.24 introduced default MPTCP support for listen sockets on Linux, meaning services built with Go automatically use MPTCP unless explicitly disabled.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/2026-160-aws/">CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free ...</a></li>
<li><a href="https://www.fosslinux.com/163418/cve-2026-98432-linux-tcp-use-after-free.htm">CVE-2026-98432: The Linux TCP Use-After-Free Flaw Explained</a></li>
<li><a href="https://access.redhat.com/security/vulnerabilities/RHSB-2026-016">RHSB-2026-016 Use-after-free - kernel IPv4 (CVE-2026-98432)</a></li>

</ul>
</details>

**Tags**: `#security`, `#linux-kernel`, `#vulnerability`, `#CVE`, `#networking`

---