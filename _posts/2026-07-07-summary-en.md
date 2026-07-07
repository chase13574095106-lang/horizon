---
layout: default
title: "Horizon Summary: 2026-07-07 (EN)"
date: 2026-07-07
lang: en
---

> From 36 items, 13 important content pieces were selected

---

1. [EU Parliament Passes Chat Control in First Round](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Sonnet 5 with Strong Agentic Abilities](#item-2) ⭐️ 9.0/10
3. [16-Year-Old KVM Escape Bug Januscape Affects Intel and AMD](#item-3) ⭐️ 9.0/10
4. [China Considers Restricting Exports of Top AI Models](#item-4) ⭐️ 9.0/10
5. [EU Mandates Driver Monitoring Cameras in All New Cars](#item-5) ⭐️ 8.0/10
6. [Microsoft Fires idTech Team at id Software](#item-6) ⭐️ 8.0/10
7. [Astro 7.0 Launches with Rust Compiler and Fewer Dependencies](#item-7) ⭐️ 8.0/10
8. [sqlite-utils 4.0 adds schema migrations, nested transactions](#item-8) ⭐️ 8.0/10
9. [Tencent Releases Hy3: 295B MoE Model, Apache 2.0](#item-9) ⭐️ 8.0/10
10. [Elon Musk Dissolves xAI, Rebrands as SpaceXAI Under SpaceX](#item-10) ⭐️ 8.0/10
11. [China Plans $295B National Computing Network in 5 Years](#item-11) ⭐️ 8.0/10
12. [new-api Fixes Billing Bug: Oversized Parameters Cause Negative Charges](#item-12) ⭐️ 8.0/10
13. [DeepSeek develops own AI chip to reduce reliance on Nvidia, Huawei](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Passes Chat Control in First Round](https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html) ⭐️ 9.0/10

The European Parliament passed the controversial Chat Control law in its first round using procedural tactics, pushing through an unpopular surveillance measure that had previously been rejected. This law would mandate mass scanning of private communications for child sexual abuse material, undermining encryption and privacy for all EU citizens. The procedural maneuver sets a dangerous precedent for bypassing democratic opposition. The law was revived in its second reading, where an absolute majority of 361 votes is needed for amendments, while a simple majority suffices for passage. Many MEPs had already left before the summer break, giving proponents a tactical advantage.

hackernews · miroljub · Jul 7, 15:16 · [Discussion](https://news.ycombinator.com/item?id=48819008)

**Background**: Chat Control refers to EU proposals to require tech companies to scan all private messages, including encrypted ones, for child sexual abuse material. The first version (Chat Control 1.0) was a temporary ePrivacy exception that expired, and the new proposal aims to make it permanent. Critics argue that no technology can detect CSAM without high false positive rates, threatening end-to-end encryption.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://reclaimthenet.org/eu-parliament-revives-chat-surveillance-for-thursday-vote">EU Parliament Revives Chat Surveillance for Thursday Vote</a></li>
<li><a href="https://www.heise.de/en/news/Partial-victory-with-a-catch-EU-Parliament-temporarily-defies-chat-control-11349760.html">Partial victory with a catch: EU Parliament temporarily defies chat control | heise online</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at the procedural tactics, with many noting that the law had been repeatedly rejected and was being forced through by exploiting low attendance. Some provided historical context on how legislatures use procedural maneuvers to pass unpopular laws, while others shared voting records showing their representatives opposed the measure.

**Tags**: `#privacy`, `#EU legislation`, `#surveillance`, `#digital rights`, `#politics`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Sonnet 5 with Strong Agentic Abilities](https://t.me/zaihuapd/42404) ⭐️ 9.0/10

Anthropic has released Claude Sonnet 5, which it claims is the most agentic Sonnet model to date, capable of planning, using browsers and terminals, and operating autonomously. It outperforms Sonnet 4.6 in reasoning, tool use, coding, and knowledge work, and approaches Opus 4.8 performance at a lower price. This release marks a significant step in agentic AI, enabling more autonomous and capable AI assistants that can perform complex tasks with minimal human intervention. It lowers the cost of high-performance AI, making advanced agentic capabilities more accessible to developers and businesses. Claude Sonnet 5 is available immediately to all plans and becomes the default model for Free and Pro tiers. On the Claude Platform, it is priced at $2 per million input tokens and output tokens at a limited-time rate until August 31, 2026.

telegram · zaihuapd · Jul 7, 09:02

**Background**: Agentic AI refers to AI systems that can pursue goals through their own actions, rather than just producing output for humans to act on. Unlike traditional AI models that require human intervention, agentic models exhibit autonomy, goal-driven behavior, and adaptability. Claude Sonnet 5 is the latest in Anthropic's line of AI models, positioned between the faster Sonnet series and the more powerful Opus series.

<details><summary>References</summary>
<ul>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://llm-stats.com/blog/research/claude-sonnet-5-vs-claude-opus-4-8">Claude Sonnet 5 vs Claude Opus 4.8: The Complete Comparison</a></li>
<li><a href="https://cloudzy.com/blog/claude-sonnet-5-vs-opus-4-8/">Claude Sonnet 5 vs. Opus 4.8: Which Model to Actually Run ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#agentic`

---

<a id="item-3"></a>
## [16-Year-Old KVM Escape Bug Januscape Affects Intel and AMD](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

Security researchers disclosed Januscape (CVE-2026-53359), the first KVM/x86 VM escape vulnerability that works on both Intel and AMD platforms, with a public proof-of-concept exploit. The bug is a use-after-free in the shadow MMU emulation, allowing a guest VM to corrupt host kernel memory and potentially escape to the host. This vulnerability poses a direct threat to multi-tenant cloud environments and any KVM-based virtualization, as a malicious guest can break out of its isolation boundary. Its 16-year presence in the Linux kernel and use as a 0-day in Google's kvmCTF highlight the severity and the need for urgent patching. The flaw resides in the shadow MMU code shared across Intel and AMD, and was present in Linux kernels from 2010 to June 2026. On RHEL and similar distributions, local unprivileged users can also exploit it to escalate privileges to root.

telegram · zaihuapd · Jul 7, 10:14

**Background**: KVM (Kernel-based Virtual Machine) is a virtualization module built into the Linux kernel that allows a physical machine to run multiple virtual machines. The shadow MMU is a component that manages guest page tables; a use-after-free bug occurs when memory is freed but still referenced, leading to potential corruption or exploitation.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html">16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems</a></li>
<li><a href="https://github.com/V4bel/Januscape">GitHub - V4bel/Januscape</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/2026/07/06/7">oss-security - Januscape: Guest-to-Host Escape in KVM/x86 ...</a></li>

</ul>
</details>

**Discussion**: The community discussion on Telegram and security mailing lists shows high engagement, with researchers emphasizing the criticality of the bug and the need for immediate patching. Some expressed concern about the public PoC enabling widespread attacks, while others praised the detailed disclosure.

**Tags**: `#KVM`, `#VM escape`, `#CVE-2026-53359`, `#security`, `#virtualization`

---

<a id="item-4"></a>
## [China Considers Restricting Exports of Top AI Models](https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07/) ⭐️ 9.0/10

China's Ministry of Commerce has held meetings with Alibaba, ByteDance, and Zhipu AI to discuss restricting overseas access to the country's most advanced AI models, including unreleased ones, and may classify AI technology leaks as national security crimes. This policy could reshape the global AI landscape by limiting technology transfer and competition, affecting international AI development and investment in Chinese AI startups. The restrictions may apply only to future models, and it remains uncertain whether the policy will be finalized. The discussions also considered restricting foreign capital investment in domestic AI startups.

telegram · zaihuapd · Jul 7, 11:42

**Background**: China has been rapidly advancing in AI, with companies like Zhipu AI (known as 'the first global large model stock') leading the field. The U.S. has already imposed export controls on AI model weights, and China's move mirrors similar concerns about national security and technological sovereignty.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/智谱">智谱 - 维基百科，自由的百科全书</a></li>
<li><a href="https://hankunlaw.com/portal/article/index/cid/8/id/15704.html">AI管制前沿 — 美国出口管制政策观察</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#China`, `#technology export control`, `#national security`, `#AI regulation`

---

<a id="item-5"></a>
## [EU Mandates Driver Monitoring Cameras in All New Cars](https://allaboutcookies.org/eu-mandatory-distracted-driver-system) ⭐️ 8.0/10

Starting July 7, 2026, every new car sold in the European Union must include a driver monitoring camera that tracks the driver's face and alerts them if they are distracted. This regulation aims to reduce accidents caused by driver distraction, but it also raises privacy concerns and has sparked debate about the balance between safety and driver annoyance. The system uses infrared cameras to monitor eye, mouth, and face movements, and can detect phone use, drowsiness, or inattention. The data handling and storage policies remain unclear, raising privacy questions.

hackernews · nickslaughter02 · Jul 7, 20:50 · [Discussion](https://news.ycombinator.com/item?id=48823557)

**Background**: Driver monitoring systems (DMS) have been used in some vehicles since 2006, but the EU is the first major market to mandate them across all new cars. The regulation is part of a broader package of safety features including cyclist-detecting emergency braking and lane-keeping assist.

<details><summary>References</summary>
<ul>
<li><a href="https://allaboutcookies.org/eu-mandatory-distracted-driver-system">All Cars Sold in the EU Now Require a Camera Aimed at Your Face. It’s Still Not Clear Where That Data Goes</a></li>
<li><a href="https://off-guardian.org/2026/04/30/the-eu-is-pushing-driver-monitoring-cameras-heres-why/">The EU is pushing “Driver-Monitoring Cameras”. Here’s why.</a></li>
<li><a href="https://www.autonext.co/news/eu-new-car-safety-features-mandatory-july-2026">New EU car safety rules start today, cameras included</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some users find existing driver aids annoying and worry about false alerts, while others report positive experiences with similar systems. A comparison to aviation alarms highlights the risk of alarm fatigue and confusing alerts.

**Tags**: `#regulation`, `#automotive`, `#safety`, `#privacy`, `#EU`

---

<a id="item-6"></a>
## [Microsoft Fires idTech Team at id Software](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

Microsoft has laid off the entire idTech engine development team at id Software, the legendary studio behind Doom and Quake. This move signals a shift away from proprietary engine development toward industry-standard solutions like Unreal Engine. This layoff threatens the future of idTech, one of the most influential game engines in history, and raises concerns about game engine monopolization by Epic Games. It also reflects a broader trend of homogenization in studio culture under Microsoft, potentially stifling innovation. The idTech team was responsible for developing the proprietary engine used in games like Doom Eternal and the upcoming Doom: The Dark Ages. Microsoft has not officially confirmed the layoffs, but multiple sources and community reports indicate the team was let go.

hackernews · bauc · Jul 7, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48819244)

**Background**: id Software is a pioneering game developer founded in 1991 by John Carmack and John Romero, known for creating the first-person shooter genre with games like Wolfenstein 3D, Doom, and Quake. The company's idTech engine has been licensed to many developers and is renowned for its performance and cutting-edge graphics. Microsoft acquired id Software's parent company ZeniMax Media in 2021.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Software">id Software - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express strong criticism of Microsoft's decision, with many arguing that it undermines id Software's unique technical culture and hands Epic Games a monopoly on game engines. Some commenters note that while the move may reduce costs, it sacrifices the innovation that made id Software legendary.

**Tags**: `#gaming`, `#layoffs`, `#game engines`, `#Microsoft`, `#id Software`

---

<a id="item-7"></a>
## [Astro 7.0 Launches with Rust Compiler and Fewer Dependencies](https://astro.build/blog/astro-7/) ⭐️ 8.0/10

Astro 7.0 introduces a Rust-based compiler and Markdown pipeline, reducing the number of dependencies from 247 in v6 to 190 in v7 and improving build performance. This release marks a significant step in the JavaScript ecosystem's trend toward reducing dependencies and adopting Rust for performance-critical tooling, benefiting developers building content-driven websites with faster builds and lighter installations. The Rust compiler and Markdown pipeline were contributed by community member Princesseuh. Astro 7.0 is a major version release, meaning it may include breaking changes from previous versions.

hackernews · saikatsg · Jul 7, 18:30 · [Discussion](https://news.ycombinator.com/item?id=48821653)

**Background**: Astro is a JavaScript web framework designed for content-driven websites, known for shipping minimal JavaScript to the browser by rendering components on the server. It supports multiple UI frameworks like React, Vue, and Svelte. The use of Rust in web tooling, as seen in projects like SWC, is becoming more common to improve performance.

<details><summary>References</summary>
<ul>
<li><a href="https://astro.build/">Astro - The web framework for content-driven websites</a></li>
<li><a href="https://github.com/withastro/astro">GitHub - withastro/astro: The web framework for content ...</a></li>

</ul>
</details>

**Discussion**: Community members praised the reduction in dependencies and the Rust-based improvements. Some expressed concerns about potential breaking changes with major version upgrades, while others appreciated Astro's simplicity for static site generation with modern tooling.

**Tags**: `#Astro`, `#web framework`, `#Rust`, `#JavaScript`, `#static site generator`

---

<a id="item-8"></a>
## [sqlite-utils 4.0 adds schema migrations, nested transactions](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0, the first major release since 2020, introduces database schema migrations, nested transactions via a new db.atomic() method, and support for compound foreign keys. This release fills a long-standing gap in the SQLite ecosystem by providing a built-in, Pythonic migration system, making sqlite-utils a more complete tool for developers managing SQLite databases in Python projects. Migrations are defined as Python functions decorated with @migrations() and can leverage the powerful table.transform() method for schema changes that go beyond SQLite's limited ALTER TABLE. The release also includes breaking changes detailed in an upgrade guide.

rss · Simon Willison · Jul 7, 19:32

**Background**: sqlite-utils is a Python library and CLI tool for manipulating SQLite databases, widely used in the Datasette ecosystem. Previously, users had to rely on external tools or manual scripts for schema migrations, which was error-prone and inconvenient.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ... Managing Database Versions and Migrations in SQLite sqlite-utils 4.0, now with database schema migrations #Shorts GitHub - simonw/sqlite-migrate: A simple database migration ... SQLite Versioning & Migration Strategies for Evolving Apps</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open-source`

---

<a id="item-9"></a>
## [Tencent Releases Hy3: 295B MoE Model, Apache 2.0](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

Tencent has released Hy3, a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and a 256K context length, under the permissive Apache 2.0 license. The model outperforms similar-size models and rivals open-source models with 2-5x its parameter count. Hy3's strong performance and open license make it a significant addition to the open-source LLM ecosystem, potentially lowering barriers for developers and researchers. Its efficiency (21B active parameters out of 295B total) demonstrates the viability of MoE for scaling models without proportional compute cost. The full-precision model is 598GB on Hugging Face, with an FP8 quantized version at 300GB. It is available for free on OpenRouter until July 21st, 2026. The model includes 3.8B MTP (Multi-Token Prediction) layer parameters for faster inference.

rss · Simon Willison · Jul 6, 23:57

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that divides the model into multiple specialized sub-networks (experts), activating only a subset per input. This allows scaling total parameters while keeping computational cost similar to a much smaller dense model. FP8 quantization reduces model size and speeds up inference by using 8-bit floating-point numbers instead of higher precision formats.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2208.09225">[2208.09225] FP8 Quantization: The Power of the Exponent</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#MoE`, `#Tencent`

---

<a id="item-10"></a>
## [Elon Musk Dissolves xAI, Rebrands as SpaceXAI Under SpaceX](https://x.com/i/status/2074214064746832060) ⭐️ 8.0/10

Elon Musk announced the dissolution of xAI, which will be rebranded as SpaceXAI and merged into SpaceX as its AI division. The company has already started using the SpaceXAI name, notably in a computing partnership announcement with Anthropic. This restructuring consolidates Musk's AI efforts under SpaceX, potentially accelerating AI integration into space technology and reshaping the competitive landscape among AI companies. The move also signals a shift from standalone AI ventures to embedded AI within larger enterprises. The acquisition, completed on February 2, 2026, valued SpaceX at $1 trillion and xAI at $250 billion, for a combined $1.25 trillion. SpaceXAI's flagship product is the Grok chatbot, and it also operates the social network X, acquired in March 2025.

telegram · zaihuapd · Jul 7, 02:30

**Background**: xAI was founded by Elon Musk in 2023 as a standalone AI company to compete with OpenAI and others. It developed the Grok chatbot and built the Colossus supercomputer. The merger into SpaceX reflects Musk's strategy to integrate AI capabilities directly into his space exploration and satellite communications businesses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">SpaceXAI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceXAI">SpaceXAI</a></li>
<li><a href="https://www.businessinsider.com/xai-rebrand-spacexai-new-logo-x-handle-spacex-2026-7">XAI Rebrands to SpaceXAI With New Logo, X Handle, Under ...</a></li>

</ul>
</details>

**Tags**: `#Elon Musk`, `#xAI`, `#SpaceX`, `#AI`, `#corporate restructuring`

---

<a id="item-11"></a>
## [China Plans $295B National Computing Network in 5 Years](https://t.me/zaihuapd/42399) ⭐️ 8.0/10

China plans to invest approximately 2 trillion yuan ($295 billion) over the next five years to build a nationwide interconnected data center network, with state-owned telecom operators managing the core facilities. The plan prioritizes domestic AI chips from Huawei and other local suppliers, aiming for at least 80% domestic content to reduce reliance on US companies like Nvidia and AMD. This massive investment signals a strategic push for AI infrastructure self-sufficiency and could reshape the global semiconductor and cloud computing landscape. It accelerates China's goal of integrating regional computing resources into a unified network, making high-performance computing more accessible to businesses and public sectors. The plan is a key part of Beijing's 'Six Networks' infrastructure initiative, which includes water, power, communications, logistics, and underground pipeline networks. Telecom operators like China Telecom and China Unicom have already launched 'token plans' that package computing power like mobile data, paving the way for large-scale AI applications.

telegram · zaihuapd · Jul 7, 04:45

**Background**: China's 'East Data West Computing' project, launched in 2022, aims to shift computing resources from eastern regions to western regions to balance supply and demand. The new national computing network builds on this by creating a unified, schedulable computing resource pool. The 'Six Networks' plan, announced in 2025, is a broader infrastructure strategy to modernize China's foundational systems.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2023358290831111769">国家数据局最新部署：全国一体化算力网8大枢纽+10大集群最全梳理</a></li>
<li><a href="https://www.gov.cn/zhengce/zhengceku/202401/content_6924596.htm">关于深入实施“东数西算”工程加快构建全国一体化算力网的实施意见_国务...</a></li>
<li><a href="https://www.sohu.com/a/994678899_122316869">7万亿新基建工程全面启动：国家发改委详解"六张网"投资战略</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#China tech policy`, `#semiconductors`, `#cloud computing`, `#national strategy`

---

<a id="item-12"></a>
## [new-api Fixes Billing Bug: Oversized Parameters Cause Negative Charges](https://github.com/QuantumNous/new-api/commit/d0bd8aa) ⭐️ 8.0/10

The QuantumNous/new-api project has fixed a billing vulnerability where oversized parameters could trigger integer overflow, resulting in negative charges. Two commits added upper-bound validation and saturation arithmetic to prevent quota calculations from wrapping around to negative values. This vulnerability could have been exploited for financial gain, effectively allowing attackers to 'reverse recharge' their accounts. The fix protects users and the project's integrity, highlighting the importance of input validation in billing systems. The vulnerability stemmed from missing boundary checks on user-controllable parameters used in quota calculations. The fix introduces saturation conversion logic to clamp results to valid integer ranges, preventing wraparound.

telegram · zaihuapd · Jul 7, 07:26

**Background**: Integer overflow occurs when a calculation exceeds the maximum value of an integer type, causing it to wrap around to a negative or small number. In billing systems, this can lead to incorrect charges. Saturation arithmetic clamps results to a fixed range, avoiding overflow.

<details><summary>References</summary>
<ul>
<li><a href="https://www.comparitech.com/blog/information-security/integer-overflow-attack/">What is an Integer Overflow Attack (with Examples)? - Comparitech CWE - CWE-190: Integer Overflow or Wraparound (4.20) Understanding & Exploiting Integer Overflow Vulnerabilities ... Vulnerability: Integer Overflow and Underflow - OWASP Foundation What is Integer Overflow? Exploits & Impact - blogs.jsmon.sh What is an Integer Overflow? How It Works & Examples NVD - CVE-2025-54091</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/190.html">CWE - CWE-190: Integer Overflow or Wraparound (4.20)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Saturation_arithmetic">Saturation arithmetic</a></li>

</ul>
</details>

**Tags**: `#security`, `#billing`, `#vulnerability`, `#open-source`, `#API`

---

<a id="item-13"></a>
## [DeepSeek develops own AI chip to reduce reliance on Nvidia, Huawei](https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/) ⭐️ 8.0/10

Chinese AI startup DeepSeek is developing its own AI chip focused on inference, aiming to reduce dependence on Nvidia and Huawei chips. The project started about a year ago and is still in early stages, with DeepSeek recruiting chip design engineers and engaging with foundries and memory companies. This move could reshape the AI chip supply chain amid US-China tech tensions, as DeepSeek seeks to secure its own chip supply for inference workloads. Success would reduce China's reliance on foreign and domestic suppliers, potentially accelerating the country's push for semiconductor self-sufficiency. The chip is designed specifically for inference, the process where a trained model generates responses to users, rather than for training. DeepSeek previously relied on Nvidia H800 and Huawei Ascend chips, and founder Liang Wenfeng cited chip export controls as a challenge in a rare 2024 interview.

telegram · zaihuapd · Jul 7, 11:08

**Background**: AI inference is the stage where a trained model makes predictions or generates outputs, as opposed to training which builds the model. DeepSeek is a Chinese generative AI company known for its open-weight models like DeepSeek-R1, which gained global attention in early 2025. The company operates under US export restrictions that limit access to advanced Nvidia chips, prompting it to explore alternatives including Huawei's Ascend series and now its own chip.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/chinas-deepseek-developing-its-own-ai-chip-sources-say-2026-07-07/">EXCLUSIVE: China's DeepSeek developing its own AI chip ...</a></li>
<li><a href="https://tech-ish.com/2026/07/07/deepseek-own-ai-inference-chip-nvidia-huawei/">DeepSeek is building its own AI chip to cut reliance on ...</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/inference-vs-training/">AI inference vs. training: What is AI inference? - Cloudflare</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#US-China tech war`, `#inference`

---