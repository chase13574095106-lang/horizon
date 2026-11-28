---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 27 items, 4 important content pieces were selected

---

1. [OpenSec discloses critical Linux NFS server vulnerability allowing unauthenticated root access](#item-1) ⭐️ 9.0/10
2. [Mixue Invests 500M RMB in DeepSeek's ~100B RMB Round](#item-2) ⭐️ 8.0/10
3. [Anthropic secretly weakens Claude's responses to frontier AI development requests, affecting 0.03% of traffic](#item-3) ⭐️ 8.0/10
4. [Minecraft Java Edition hit by high-severity RCE via malicious fonts](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenSec discloses critical Linux NFS server vulnerability allowing unauthenticated root access](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec disclosed CVE-2026-99362, a pre-authentication heap overflow in the Linux kernel's NFS server (nfsd) with a CVSS score of 9.8, allowing unauthenticated remote attackers to gain root access via a single TCP connection to port 2049. The vulnerability has existed since Linux 3.16 (2014) and affects hosts running NFSv4.1 or 4.2; fixes are available in kernel versions 6.12.117, 6.18.61, 7.3.2, and 7.4-rc1. This is a critical remote kernel vulnerability that can be exploited without authentication, putting file servers, NAS devices, and cluster storage nodes at risk of full compromise. Its presence since 2014 means a vast number of systems may be exposed, and immediate patching or firewall mitigation is essential. The overflow writes 61 bytes past a kernel heap object, which can be chained to achieve a root shell. Mitigation without patching involves restricting access to tcp/2049 via firewall, and the CVE was publicly disclosed on November 20, 2026.

telegram · zaihuapd · Nov 27, 12:57

**Background**: NFS (Network File System) is a widely used protocol for sharing files over a network, and nfsd is the Linux kernel's NFS server implementation. NFSv4.1 and 4.2 are recent versions that include features like session trunking and server-side copy, and they listen on TCP port 2049. A pre-authentication vulnerability means an attacker can exploit it before any login or credential check, making it especially dangerous. CVSS is a standard scoring system where 9.8 indicates critical severity.

<details><summary>References</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS2ROOT (CVE-2026-99362): pre -auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS2ROOT Linux flaw can let attackers gain root privileges</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#security`, `#vulnerability`, `#nfs`, `#cve`

---

<a id="item-2"></a>
## [Mixue Invests 500M RMB in DeepSeek's ~100B RMB Round](https://m.sohu.com/a/1107027659_115479) ⭐️ 8.0/10

DeepSeek completed a second funding round of roughly 100–105.5 billion RMB at a post-money valuation of about 615.5 billion RMB, with Mixue Ice Cream & Tea (蜜雪冰城) committing 500 million RMB through the Tianjin Lisi Xingshen fund managed by Lisi Capital. The round added 31 new backers, including Tencent, CATL, China Mobile, and vivo. This is one of the largest AI funding rounds in China, valuing DeepSeek at over 600 billion RMB and drawing in both strategic tech/energy giants and an unexpected consumer brand. It signals that DeepSeek is becoming a national AI champion with broad corporate backing, which could accelerate its compute buildout and commercial expansion. Mixue's 500 million RMB went through the Tianjin Lisi Xingshen fund, which was initially registered with 2.64 billion RMB and later closed at 7.52 billion RMB—reportedly the largest blind-pool RMB VC fundraise this year. Mixue Group reported 2025 revenue of 33.56 billion RMB and net profit attributable to shareholders of about 5.89 billion RMB.

telegram · zaihuapd · Nov 27, 06:33

**Background**: DeepSeek is a Chinese AI research company known for open-source frontier large language models such as DeepSeek-V3, a 671-billion-parameter Mixture-of-Experts model. A blind-pool fund is a venture capital vehicle that raises capital before identifying specific investments, giving managers broad discretion. Mixue Ice Cream & Tea is China's largest bubble-tea and ice-cream chain, known for its low-price strategy and massive franchise network.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/盲池基金/67559001">盲池基金 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/623993110">对比 】专项基金 VS 盲池基金 - 知乎</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI funding`, `#venture capital`, `#China tech`, `#industry news`

---

<a id="item-3"></a>
## [Anthropic secretly weakens Claude's responses to frontier AI development requests, affecting 0.03% of traffic](https://news.ycombinator.com/item?id=50664325) ⭐️ 8.0/10

Anthropic's June system card for Claude Mythos 5 and Fable 5 discloses that the company covertly degrades Claude's answers to requests aimed at developing frontier AI models, using prompt rewriting, steering vectors, and parameter-efficient fine-tuning. The intervention affects about 0.03% of traffic and fewer than 0.1% of organizations, and users cannot detect it or fall back to another model as with safety refusals. This reveals a controversial policy where Anthropic silently degrades model outputs for AI development requests, raising transparency and ethics concerns about undisclosed behavioral modifications. It could set a precedent for how AI labs police competitor research and affect developers who use Claude for legitimate ML engineering work. The intervention covers tasks like pretraining pipelines, distributed training, and accelerator design, while most coding work is unaffected; using Claude to develop competing models already violates the terms of service. The system card resurfaced this week due to developer discussions on Hacker News.

telegram · zaihuapd · Nov 27, 13:42

**Background**: System cards are documents Anthropic publishes to describe a model's capabilities, safety evaluations, and responsible deployment decisions. Steering vectors are directions added to a model's internal activations at inference time to shift its behavior, while parameter-efficient fine-tuning adapts a large model by updating only a small fraction of its parameters. Anthropic's terms of service prohibit using Claude to build competing AI models, and this disclosure shows the company enforces that rule through silent degradation rather than explicit refusal.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.40998">[2610.40998] Steering Vectors as a Training Signal in LLM ...</a></li>
<li><a href="https://www.lesswrong.com/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms">A Sober Look at Steering Vectors for LLMs — LessWrong</a></li>
<li><a href="https://grokipedia.com/page/Parameter-Efficient_Fine-Tuning_PEFT">Parameter-Efficient Fine-Tuning (PEFT)</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion adds community validation and diverse viewpoints, with commenters debating the transparency and ethics of silently degrading outputs, though the impact is limited to roughly 0.03% of traffic.

**Tags**: `#AI ethics`, `#Anthropic`, `#model transparency`, `#AI policy`, `#Hacker News`

---

<a id="item-4"></a>
## [Minecraft Java Edition hit by high-severity RCE via malicious fonts](https://t.me/zaihuapd/45413) ⭐️ 8.0/10

On November 22, a high-severity remote code execution vulnerability named minecraft2shell was disclosed, affecting Minecraft Java Edition versions 1.20.5 through 1.21.10 and snapshots 26.1 to 26.4. The flaw allows a malicious TrueType font in a server resource pack to trigger an out-of-bounds write in FreeType 2.14.3 and earlier, leading to arbitrary code execution on Windows clients. This is a critical security issue because Minecraft servers can push resource packs to connecting clients, meaning any player joining a malicious server could be compromised without warning. With no official patch yet and a vast player base, server operators and players are urged to exercise caution until Mojang releases a fix. The vulnerability stems from an out-of-bounds write in FreeType, the font rendering library used by Minecraft via LWJGL. Mojang currently uses lwjgl-freetype 3.4.3, which is affected, and no patch is available; versions 1.20.4 and earlier, as well as Bedrock Edition, are not impacted.

telegram · zaihuapd · Nov 27, 18:04

**Background**: FreeType is a widely used open-source library for rendering fonts, and Minecraft Java Edition relies on it to display text, including custom fonts from resource packs. Resource packs are collections of assets that servers can automatically send to clients to change textures, sounds, and fonts. A remote code execution (RCE) flaw lets an attacker run arbitrary code on a victim's machine, often leading to full system compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability - wurst.wiki</a></li>
<li><a href="https://liquidbounce.net/blog/minecraft2shell-vulnerability-AK0X5CE6">Minecraft2Shell Vulnerability - liquidbounce.net</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/minecraft2shell-minecraft-java-rce-resource-pack.html">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights that Mojang fixed the issue for version 26.3 on November 24, and players are advised to restart their game to receive the update. There is concern that many servers may still be running vulnerable versions, and users are sharing mitigation tips such as avoiding untrusted servers.

**Tags**: `#security`, `#vulnerability`, `#Minecraft`, `#RCE`, `#FreeType`

---