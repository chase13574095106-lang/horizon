---
layout: default
title: "Horizon Summary: 2026-05-14 (EN)"
date: 2026-05-14
lang: en
---

> From 29 items, 10 important content pieces were selected

---

1. [First Public macOS Kernel Exploit on Apple M5](#item-1) ⭐️ 9.0/10
2. [Bun's Rewrite from Zig to Rust Merged](#item-2) ⭐️ 9.0/10
3. [18-Year-Old NGINX RCE Vulnerability (CVE-2026-42945) Threatens Billions of Servers](#item-3) ⭐️ 9.0/10
4. [DeepSeek session isolation bug leaks chat history via <think](#item-4) ⭐️ 9.0/10
5. [Removing Modem and GPS from 2024 RAV4 Hybrid](#item-5) ⭐️ 8.0/10
6. [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM Breakthrough](#item-6) ⭐️ 8.0/10
7. [AI-Assisted Coding May Hinder Developer Learning](#item-7) ⭐️ 8.0/10
8. [Anthropic Partners with SpaceX for Colossus Compute](#item-8) ⭐️ 8.0/10
9. [US Clears H200 Chip Sales to 10 Chinese Firms](#item-9) ⭐️ 8.0/10
10. [JD.com Launches AI Hardware Store, Lists Sanctioned NVIDIA GPUs](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First Public macOS Kernel Exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

The Calif team published the first public kernel memory corruption exploit targeting Apple's M5 chip, potentially bypassing the Memory Tagging Extensions (MTE) hardware security feature. This marks a significant security milestone as it demonstrates a practical bypass of MTE, a key hardware mitigation for memory safety, and highlights the growing role of LLM-assisted exploit development. The exploit was discovered accidentally by Bruce Dang on April 25, and Dion Blazakis joined Calif on April 27 to help land the exploit within a week. The team plans to release a 55-page technical report with full details.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: Apple M5 is Apple's latest ARM-based SoC, built on 3nm process, featuring a next-generation GPU and Neural Accelerators. Memory Tagging Extensions (MTE) is an Armv9 hardware feature designed to detect memory safety errors like use-after-free and buffer overflows, widely adopted in Android and now in Apple silicon. Kernel memory corruption exploits are among the most severe vulnerabilities, as they can give attackers full control over the system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://developer.android.com/ndk/guides/arm-mte">Arm Memory Tagging Extension (MTE) | Android NDK | Android Developers</a></li>

</ul>
</details>

**Discussion**: Commenters expressed both excitement and skepticism: some praised the achievement and noted the potential for LLM-assisted exploits, while others questioned the lack of technical details and how the bug survived MTE. There was also sarcastic speculation about Apple inventing fake vulnerabilities to hype Mythos.

**Tags**: `#macOS`, `#kernel exploit`, `#Apple M5`, `#security`, `#MTE`

---

<a id="item-2"></a>
## [Bun's Rewrite from Zig to Rust Merged](https://github.com/oven-sh/bun/pull/30412) ⭐️ 9.0/10

The pull request to rewrite Bun from Zig to Rust has been merged, resulting in over 1 million lines of Rust code and replacing the previous Zig codebase. This rewrite significantly improves memory safety and reduces bugs like use-after-free and double-free, which are common in Zig, making Bun more reliable for developers. The new codebase contains over 1 million lines of Rust code, with 10,428 unsafe blocks across 736 files, and the rewrite was prepared with detailed mapping of Zig idioms to Rust.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Background**: Bun is a JavaScript runtime, bundler, and package manager designed as a drop-in replacement for Node.js. It originally used Zig, a low-level language focused on safety and performance, but Rust offers stronger memory safety guarantees through its ownership system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: The community debated the complexity of the codebase, with some noting that Bun's Rust code size approaches that of the Rust compiler itself. Others highlighted the extensive preparation and mapping work that made the rewrite possible in a short time.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript Runtime`, `#Software Engineering`

---

<a id="item-3"></a>
## [18-Year-Old NGINX RCE Vulnerability (CVE-2026-42945) Threatens Billions of Servers](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability) ⭐️ 9.0/10

A critical heap buffer overflow vulnerability (CVE-2026-42945, CVSS 9.2) was disclosed in NGINX's ngx_http_rewrite_module, present since 2008, allowing unauthenticated remote code execution. Patches have been released in NGINX Open Source 1.31.0/1.30.1 and NGINX Plus R36 P4/R32 P6. This vulnerability affects billions of production servers globally, including those in Kubernetes ingress layers and API gateways, due to NGINX's widespread use. The 18-year-old flaw underscores the critical need for immediate patching and highlights risks in long-lived codebases. The vulnerability arises from an inconsistency in the two-pass script engine: during the first pass, buffer size is calculated without considering URI character expansion (1 to 3 bytes per char), leading to heap overflow in the second pass. Exploitation requires a rewrite directive with a question mark in the replacement string and a subsequent set directive referencing an unnamed capture group (e.g., $1).

telegram · zaihuapd · May 14, 02:41

**Background**: NGINX is a widely used open-source web server, reverse proxy, and load balancer. The ngx_http_rewrite_module handles URL rewriting using a two-pass script engine: first to calculate buffer size, second to copy the result. A heap buffer overflow occurs when the calculated size is too small, allowing an attacker to overwrite adjacent memory and potentially execute arbitrary code.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.rankiteo.com/f51778747583-f5-vulnerability-may-2026/">F5: Critical 18-Year-Old NGINX Vulnerability Enables Remote Code Execution Attacks</a></li>
<li><a href="https://gist.github.com/alon710/774ec5a75ca3c79658262b161d1067ad">CVE-2026-42945: CVE-2026-42945: Heap-based Buffer Overflow in NGINX ngx_http_rewrite_module - CVE Security Report · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the published proof-of-concept (PoC) assumes ASLR is disabled, but the researchers claim a reliable ASLR bypass exists. Some emphasized that ASLR is a defense-in-depth measure and not a complete mitigation. Others discussed the preconditions (rewrite with ? and set with $1) and suggested using named capture groups as a workaround.

**Tags**: `#NGINX`, `#CVE-2026-42945`, `#remote code execution`, `#security vulnerability`, `#heap buffer overflow`

---

<a id="item-4"></a>
## [DeepSeek session isolation bug leaks chat history via <think](https://github.com/deepseek-ai/DeepSeek-R1/issues/840) ⭐️ 9.0/10

A critical session isolation vulnerability has been discovered in DeepSeek's Web and API dialogue systems: by sending an unclosed <think string in a new empty chat, an attacker can retrieve other users' conversation history, including sensitive data like code, keys, and private information. The bug was responsibly disclosed by user cancat2024 on May 11, 2026, and has since been publicly circulated. This vulnerability poses a severe privacy risk to all DeepSeek users, as it allows unauthorized access to private conversations, potentially exposing proprietary code, credentials, and personal data. The incident highlights critical security shortcomings in AI chat systems and could erode user trust in DeepSeek and similar platforms. The exploit works by sending an unclosed <think token in a brand new chat session, causing the model to hallucinate and return fragments of other users' conversations. The vulnerability affects both DeepSeek's web interface and API, and has been confirmed in third-party deployments as well.

telegram · zaihuapd · May 14, 13:15

**Background**: DeepSeek is a popular Chinese AI model known for its strong reasoning capabilities, often used in chat applications. Session isolation is a fundamental security requirement for multi-tenant AI services, ensuring that one user's data is not visible to others. The <think token is a special marker used by DeepSeek to indicate internal reasoning steps, and its improper handling can lead to context leakage.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/AI_News_CN/36511">Telegram: View @AI_News_CN</a></li>
<li><a href="https://www.80aj.com/2026/05/15/deepseek-privacy-bug-space/">DeepSeek 疑现严重隐私漏洞：输入空格即可查看他人实时对话</a></li>

</ul>
</details>

**Discussion**: The community discussion on GitHub and Telegram confirms the severity, with users noting that third-party deployments are also affected, suggesting the issue stems from model hallucination rather than a simple backend bug. Some commenters express concern over the rapid public spread of the exploit and urge users to avoid sharing sensitive information on DeepSeek until a fix is deployed.

**Tags**: `#security`, `#vulnerability`, `#AI`, `#DeepSeek`, `#data leak`

---

<a id="item-5"></a>
## [Removing Modem and GPS from 2024 RAV4 Hybrid](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

A detailed guide shows how to physically remove the modem and GPS from a 2024 RAV4 hybrid to stop telemetry, but warns that Bluetooth-connected phones still leak data via the car's internet sharing. This matters because modern vehicles collect extensive telemetry, and this guide provides a practical, hands-on solution for privacy-conscious owners, while also highlighting that Bluetooth connections can bypass the removal. The removal involves disconnecting the Data Communication Module (DCM) and GPS antenna; however, CarPlay via USB does not share internet, but both CarPlay and Android Auto still capture their own telemetry.

hackernews · arkadiyt · May 14, 17:08 · [Discussion](https://news.ycombinator.com/item?id=48138136)

**Background**: Modern cars like the Toyota RAV4 have built-in cellular modems and GPS for features like remote services and emergency calls, but they also continuously send telemetry data to the manufacturer. Removing the modem can prevent this, but some functions may be lost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Toyota_RAV4">Toyota RAV 4 - Wikipedia</a></li>
<li><a href="https://www.youtube.com/watch?v=g7xS3uPCBJA">Disable DCM in toyota cars - YouTube</a></li>
<li><a href="https://forum.ih8mud.com/threads/permanently-disable-telemetry-data-transmission-from-16-200s.1347480/">Permanently Disable Telemetry Data Transmission from 16+ 200s</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar experiences with other brands (Subaru, Ford) and noted that removing a fuse can disable telematics without errors. Some expressed surprise that Bluetooth allows internet sharing, while others pointed out that CarPlay/Android Auto still collect data.

**Tags**: `#privacy`, `#automotive`, `#telemetry`, `#hardware hacking`, `#security`

---

<a id="item-6"></a>
## [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM Breakthrough](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

A developer successfully connected an NVIDIA RTX 5090 eGPU to an M4 MacBook Air via PCIe tunneling over Thunderbolt, enabling gaming and LLM inference that were previously impossible on Apple Silicon. This achievement demonstrates that eGPUs can work with Apple Silicon, potentially unlocking high-performance gaming and AI workloads on Macs, and highlights the growing demand for GPU acceleration in the Apple ecosystem. The setup uses PCIe tunneling over Thunderbolt, but Apple's 1.5 GB DMA window limit restricts performance. The eGPU significantly improves LLM prompt processing speed, which is a known bottleneck on Macs.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: eGPUs (external GPUs) allow laptops to use desktop-class graphics cards via Thunderbolt. Apple Silicon Macs lack native eGPU support, but PCIe tunneling can bypass this limitation. LLM inference on Macs suffers from slow prompt processing due to unified memory architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://egpu.io/forums/thunderbolt-enclosures/aoostar-ag02-egpu-not-detected-on-rog-ally-x-usb4-link-ok-no-pcie-tunnel/">AOOSTAR AG02 eGPU not detected on ROG Ally X (USB4 link OK, ...</a></li>
<li><a href="https://blog.starmorph.com/blog/apple-silicon-llm-inference-optimization-guide">Apple Silicon LLM Inference Optimization: The Complete Guide to...</a></li>
<li><a href="https://toolhalla.ai/blog/best-local-llms-mac-studio-2026">Best Local LLMs for Mac Studio in 2026 | ToolHalla</a></li>

</ul>
</details>

**Discussion**: Commenters praised the technical achievement, with some noting the LLM improvements are more impactful than gaming. Others expressed frustration with Apple's lack of official eGPU support and the 1.5 GB DMA window limitation.

**Tags**: `#eGPU`, `#Apple Silicon`, `#Gaming`, `#LLM Inference`, `#PCIe Tunneling`

---

<a id="item-7"></a>
## [AI-Assisted Coding May Hinder Developer Learning](https://jpain.io/god-damn-ai-is-making-me-dumb/) ⭐️ 8.0/10

A developer's blog post titled 'AI is making me dumb' reflects on how reliance on AI coding assistants can reduce deep learning and skill acquisition, sparking a community debate with over 200 comments. This discussion highlights a critical trade-off in software engineering: AI boosts productivity but may undermine long-term developer growth, especially for juniors. It resonates with broader concerns about AI's impact on learning and expertise. The term 'vibe coding'—coined by Andrej Karpathy in February 2025—describes accepting AI-generated code without thorough review. Critics warn of security risks and reduced maintainability, while advocates say it lowers barriers for amateur programmers.

hackernews · Eighth · May 14, 18:19 · [Discussion](https://news.ycombinator.com/item?id=48139148)

**Background**: Vibe coding is a practice where developers describe tasks to an LLM and accept the generated code without deep scrutiny. It gained popularity in 2025, with Collins Dictionary naming it Word of the Year. The debate centers on whether this approach helps or harms skill development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some with experience feel a persistent urge to review AI output, while others (especially juniors) worry about slower onboarding. A few reported learning faster in specialized domains like spectroscopy, suggesting context matters.

**Tags**: `#AI`, `#software engineering`, `#developer experience`, `#learning`, `#vibe coding`

---

<a id="item-8"></a>
## [Anthropic Partners with SpaceX for Colossus Compute](https://t.me/zaihuapd/41371) ⭐️ 8.0/10

Anthropic has signed an agreement with SpaceX to use the entire compute capacity of the Colossus 1 data center, gaining over 300 MW of new capacity and more than 220,000 NVIDIA GPUs within a month. As a result, Claude Code's 5-hour rate limits have been doubled across all paid plans, and API rate limits for Claude Opus have been significantly increased. This partnership provides Anthropic with massive compute resources, enabling faster model training and inference, and directly improves user experience by raising usage limits. It also signals the growing importance of large-scale AI infrastructure and cross-industry collaborations. Colossus 1 is a supercomputer developed by xAI, built in 122 days in Memphis, Tennessee, and is considered the world's largest AI supercomputer. The deal includes over 300 MW of power and 220,000+ NVIDIA GPUs, with immediate effect on Claude Code and API rate limits.

telegram · zaihuapd · May 14, 00:57

**Background**: Anthropic is the company behind the Claude AI assistant, which offers various plans including Pro, Max, and API access. Claude Code is a coding tool that operates under rate limits based on a rolling 5-hour window. Colossus 1, originally built for xAI's Grok chatbot, represents a massive leap in AI compute capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servethehome.com/anthropic-signs-spacex-colossus-1-data-center-to-boost-capacity/">Anthropic Signs SpaceX Colossus 1 Data Center to... - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.sessionwatcher.com/guides/claude-code-rate-limits-explained">Claude Code Rate Limits Explained – 5-Hour... | SessionWatcher</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SpaceX`, `#AI infrastructure`, `#Claude`, `#NVIDIA GPU`

---

<a id="item-9"></a>
## [US Clears H200 Chip Sales to 10 Chinese Firms](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) ⭐️ 8.0/10

The US Commerce Department has approved the sale of Nvidia's H200 AI chips to about 10 Chinese companies, including Alibaba, Tencent, ByteDance, and JD.com, with each customer allowed to purchase up to 75,000 units. However, no deliveries have been completed yet, and some Chinese firms are becoming cautious under Beijing's guidance. This approval signals a potential shift in US export controls on advanced AI chips to China, which could impact the global AI hardware market and the development of China's domestic AI chip industry. Nvidia's CEO Jensen Huang's visit to China underscores the company's efforts to secure a breakthrough in the Chinese market amid ongoing tech tensions. The H200 GPU features 141 GB of HBM3e memory and delivers up to 32 petaflops of FP8 deep learning compute in an eight-way HGX configuration, offering significant performance improvements over the H100. The approvals cover distributors like Lenovo and Foxconn, but no shipments have occurred yet.

telegram · zaihuapd · May 14, 08:57

**Background**: The US has imposed export controls on advanced AI chips to China to limit China's access to cutting-edge technology for military and AI applications. Nvidia's H200 is a high-end GPU designed for AI training and inference, succeeding the H100. The Chinese government encourages domestic chip development while balancing the need for imported high-performance chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/h200/">H200 GPU | NVIDIA</a></li>
<li><a href="https://lenovopress.lenovo.com/lp1944-nvidia-h200-141gb-gpu">ThinkSystem NVIDIA H200 141GB GPUs Product Guide > Lenovo Press</a></li>
<li><a href="https://www.runpod.io/articles/guides/nvidia-h200-gpu">Nvidia H200 GPU: Specs, VRAM, Price, and AI Performance</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#US-China trade`, `#Nvidia`, `#export controls`, `#geopolitics`

---

<a id="item-10"></a>
## [JD.com Launches AI Hardware Store, Lists Sanctioned NVIDIA GPUs](https://u.jd.com/HaDkFMa) ⭐️ 8.0/10

JD.com has launched an 'AI Hardware JD Self-Operated Zone' that lists previously sanctioned NVIDIA GPUs including the H100, RTX 5090 Turbo, and RTX PRO 6000 Blackwell Server Edition for purchase. This move may signal a relaxation of export restrictions on high-end AI hardware to China, which could significantly impact the AI and machine learning industry by providing access to cutting-edge GPUs. The RTX 5090 Turbo is listed as a globally unified, non-crippled specification; the RTX PRO 6000 targets professional rendering and data centers; the H100 was previously suspended from export to China due to sanctions.

telegram · zaihuapd · May 14, 15:15

**Background**: The U.S. has imposed export restrictions on advanced AI chips like the NVIDIA H100 to China, citing national security concerns. JD.com is a major Chinese e-commerce platform, and its self-operated store typically ensures product authenticity and availability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.cn/geforce/graphics-cards/50-series/rtx-5090-d-v2/">GeForce RTX 5090 D v2 显卡 | NVIDIA</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/">RTX PRO 6000 Blackwell Server Edition | NVIDIA</a></li>
<li><a href="https://www.usmart.hk/en/news-detail/7307756841394651962">英偉達GTC：聯想等 Blackwell RTX PRO ... | uSMART</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#NVIDIA`, `#export restrictions`, `#JD.com`, `#GPU`

---