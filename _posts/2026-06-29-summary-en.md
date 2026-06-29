---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 30 items, 8 important content pieces were selected

---

1. [Supreme Court rules geofence warrants need Fourth Amendment protections](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0 Adds MiniMax-M3, Optimizes DeepSeek-V4](#item-2) ⭐️ 8.0/10
3. [Rocket Lab to Acquire Iridium in $8B Deal](#item-3) ⭐️ 8.0/10
4. [WATaBoy: JIT-Compiling Game Boy to WASM Outperforms Native Interpreter](#item-4) ⭐️ 8.0/10
5. [Deep Dive: The Full CUDA Kernel Launch Path](#item-5) ⭐️ 8.0/10
6. [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Agentic Coding](#item-6) ⭐️ 8.0/10
7. [Samsung and SK Hynix Unveil Massive AI Investments](#item-7) ⭐️ 8.0/10
8. [CXMT and Tencent Sign ~$3B DRAM Supply Deal](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Supreme Court rules geofence warrants need Fourth Amendment protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled that geofence warrants, which compel tech companies to identify all mobile devices in a specific area, must comply with Fourth Amendment protections against unreasonable searches and seizures. This landmark decision significantly limits warrantless access to location data, strengthening digital privacy rights for millions of smartphone users and setting a precedent for future surveillance technologies. The case involved a bank robbery where Google provided location data of 19 accounts within 150 meters of the bank; the Court required warrants to be specific and limited in scope, rejecting broad geofence requests.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, allows law enforcement to search a database for all active mobile devices within a defined area during a specific time. The Fourth Amendment protects against unreasonable searches, but courts have struggled to apply it to digital location data. The Supreme Court's 2018 Carpenter v. United States decision established that accessing historical cell-site location data requires a warrant, and this ruling extends similar protections to geofence warrants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted historical examples like the Paula Broadwell case to show that location tracking can identify suspects even without phones. Some expressed concern that warrants are often rubber-stamped, while others noted the ruling's broader implications for presidential power and the unitary executive theory.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#fourth amendment`, `#digital rights`

---

<a id="item-2"></a>
## [vLLM v0.24.0 Adds MiniMax-M3, Optimizes DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 introduces support for the MiniMax-M3 model and delivers major optimizations for DeepSeek-V4, including a FlashInfer sparse index cache and prefill chunk-planning improvements. The release also expands the Model Runner V2 to support quantized models by default and adds a new streaming parser engine for tool-call and reasoning parsing. This release significantly expands vLLM's model ecosystem by supporting frontier models like MiniMax-M3 and DeepSeek-V4, making high-performance inference more accessible. The optimizations improve throughput and latency, benefiting developers deploying large language models in production. The release includes 571 commits from 256 contributors, with 77 new contributors. Key technical additions include MXFP4 support for MiniMax-M3, a cluster-cooperative topK kernel for DeepSeek-V4, and integration of DeepEP v2 for expert parallelism.

github · khluu · Jun 29, 19:41

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models, originally developed at UC Berkeley. It uses PagedAttention to manage KV-cache memory efficiently. MiniMax-M3 is a multimodal MoE model with 1M context window, while DeepSeek-V4 is a 1-trillion-parameter MoE model.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M3">MiniMaxAI/ MiniMax - M 3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#open source`

---

<a id="item-3"></a>
## [Rocket Lab to Acquire Iridium in $8B Deal](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

Rocket Lab announced on June 29, 2025, that it will acquire Iridium Communications in a cash-and-stock deal valued at approximately $8 billion, with an offer of $54 per share. The transaction has been unanimously approved by both boards and is expected to close by mid-2027, subject to shareholder and regulatory approvals. This acquisition creates a fully integrated space company combining Rocket Lab's launch and spacecraft manufacturing with Iridium's profitable LEO satellite constellation, L-band spectrum, and over 500 partner ecosystem. It positions Rocket Lab to compete more broadly in satellite IoT, direct-to-device, and PNT applications, while securing a baseline of regular launches for its growing launch business. Iridium operates 66 active LEO satellites at ~781 km altitude with near-polar orbit, providing global voice and data coverage. The company reported 2025 revenue of $871.7 million and EBITDA of $495 million (57% margin), with over 2.55 million active subscribers. Rocket Lab has secured a $3.6 billion bridge loan commitment to support the deal.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: Rocket Lab is a publicly traded aerospace manufacturer and launch service provider, best known for its Electron rocket which has completed over 75 missions as of early 2026. Iridium Communications owns and operates the Iridium satellite constellation, a global LEO network originally developed by Motorola and operational since 1998. The constellation uses inter-satellite links to provide coverage over poles and oceans without ground stations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab">Rocket Lab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Iridium_Communications">Iridium Communications - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some see the deal as a smart strategic move to secure launch demand and expand into satellite services, similar to SpaceX's use of Starlink. Others express concerns about space debris and the commercialization of low Earth orbit. A few commenters note Rocket Lab's shift from a New Zealand pride to an American company.

**Tags**: `#space`, `#acquisition`, `#satellite`, `#Rocket Lab`, `#Iridium`

---

<a id="item-4"></a>
## [WATaBoy: JIT-Compiling Game Boy to WASM Outperforms Native Interpreter](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

WATaBoy is a Game Boy emulator that uses just-in-time (JIT) compilation to translate SM83 instructions into WebAssembly (WASM), achieving performance that beats native interpreters by leveraging the browser's JIT engine. This approach cleverly bypasses iOS's JIT restrictions by running inside a web browser, enabling high-performance emulation on devices where native JIT is banned. It also demonstrates that WASM can serve as an effective intermediate representation for emulation JITs. The emulator compiles Game Boy SM83 opcodes to WASM modules at runtime, which are then further JIT-compiled by the browser's WASM engine to native code. Benchmarks show it outperforms a native interpreter, though Firefox is about 25% slower than Chrome/Safari.

hackernews · energeticbark · Jun 29, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48720190)

**Background**: JIT compilation is a technique that compiles code at runtime to improve performance, but Apple restricts JIT on iOS except for web browsers' JavaScript and WebAssembly engines. WebAssembly is a low-level binary format designed for near-native performance in browsers, and modern browsers further JIT-compile WASM to machine code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/EnergeticBark/WATaBoy">GitHub - EnergeticBark/ WATaBoy : A Game Boy emulator with an...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project as impressive undergraduate work and noted the clever workaround for iOS JIT restrictions. Some questioned why Firefox is slower, and one commenter noted that WASM overhead (~20%) is far less than interpreter overhead (~1000%), making the result expected but still cool.

**Tags**: `#JIT compilation`, `#WebAssembly`, `#emulation`, `#Game Boy`, `#iOS`

---

<a id="item-5"></a>
## [Deep Dive: The Full CUDA Kernel Launch Path](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10

A detailed technical blog post explains the complete CPU-to-GPU path when launching a CUDA kernel, covering driver interaction, command submission via doorbell registers, and the role of Queue Management Descriptors (QMDs). This deep-dive bridges the gap between high-level CUDA syntax and low-level hardware mechanisms, helping developers understand performance implications and debug kernel launch overhead. It also highlights the complexity that libraries and frameworks abstract away. The post explains that the CPU writes a QMD to a circular buffer and rings a doorbell register to notify the GPU, which then fetches and executes the kernel. Community comments note that control codes involve a table lookup, not just bits in the control word.

hackernews · mezark · Jun 29, 13:11 · [Discussion](https://news.ycombinator.com/item?id=48718863)

**Background**: CUDA kernels are functions that run on NVIDIA GPUs. Launching a kernel involves the CPU sending commands to the GPU via the CUDA driver and hardware mechanisms like doorbell registers and command queues. Most tutorials focus on kernel code itself, but the launch path from CPU to GPU is equally important for understanding performance and system behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html">2.3. Writing SIMT Kernels — CUDA Programming Guide</a></li>
<li><a href="https://dev.to/dianejwilliams/part-4-command-stream-and-rendering-pipeline-command-submission-26am">Part 4: Command Stream and Rendering Pipeline... - DEV Community</a></li>

</ul>
</details>

**Discussion**: Commenters praised the post for clarifying the doorbell and QMD mechanisms, which connect CUDA syntax to actual GPU submission. Some noted that control codes are more complex (table lookup), and others appreciated the explanation of default stream semaphores, contrasting CUDA's implicit synchronization with Vulkan's explicit approach.

**Tags**: `#CUDA`, `#GPU`, `#systems programming`, `#NVIDIA`, `#kernel launch`

---

<a id="item-6"></a>
## [Ornith-1.0: Open-Weight Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of MIT-licensed open-weight LLMs for agentic coding, with sizes from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5 (both Apache 2.0). It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. Ornith-1.0 introduces a self-scaffolding training framework where the model learns to generate both code solutions and the task-specific harnesses, enabling more autonomous and effective coding agents. This could significantly advance open-source AI-assisted software development. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants. Early user reports indicate strong performance on agentic coding tasks, such as navigating codebases and executing multi-step tool calls, with inference speeds up to 103 tokens/second on consumer hardware.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents that autonomously plan, write, test, and modify code with minimal human intervention. Traditional LLM-based coding assistants rely on fixed, human-designed scaffolds (harnesses) to guide the agent's workflow. Ornith-1.0's self-scaffolding approach treats the scaffold as a learnable component, jointly optimized with the model's policy during reinforcement learning.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://github.com/deepreinforce-ai/Ornith-1">GitHub - deepreinforce -ai/ Ornith - 1 · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#model release`

---

<a id="item-7"></a>
## [Samsung and SK Hynix Unveil Massive AI Investments](https://t.me/zaihuapd/42235) ⭐️ 8.0/10

Samsung and SK Hynix will announce massive AI investments at a national briefing on June 29, with Samsung planning a 6480 billion USD ten-year spending plan, the largest in Korean history. This signals a strategic shift towards AI infrastructure by major semiconductor companies, potentially reshaping the global AI hardware landscape and intensifying competition with other chipmakers. SK Hynix plans to double its production capacity within five years and raise $29 billion through a U.S. listing. The briefing will also focus on semiconductors, AI data centers, and physical AI.

telegram · zaihuapd · Jun 29, 07:00

**Background**: Physical AI refers to technology that enables autonomous machines like robots and self-driving cars to perceive, understand, and execute complex operations in the real world. AI data centers are critical infrastructure for training and deploying large AI models, consuming significant energy. Samsung and SK Hynix are leading memory chip manufacturers, with HBM (High Bandwidth Memory) being essential for AI accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/Odaily_News/158245">Odaily资讯速递 – Telegram</a></li>
<li><a href="https://m.pedaily.cn/news/564774">就因为会「搬砖」了， 物 理 AI 一夜爆火|投资界</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#AI investment`, `#Samsung`, `#SK Hynix`, `#hardware`

---

<a id="item-8"></a>
## [CXMT and Tencent Sign ~$3B DRAM Supply Deal](https://www.reuters.com/world/china/chinas-cxmt-wins-3-billion-memory-supply-deal-with-tencent-sources-say-2026-06-29/) ⭐️ 8.0/10

ChangXin Memory Technologies (CXMT) has signed a long-term DRAM supply agreement with Tencent valued at over 200 billion yuan (approximately $2.94 billion), covering server memory chips for several years. This deal marks a significant shift in China's memory supply chain, reducing reliance on foreign DRAM suppliers and strengthening domestic semiconductor ecosystem. It also highlights Tencent's strategic move to secure critical components amid global memory shortages. The agreement is reported to last three to five years, according to sources. CXMT is also reportedly in talks with other major Chinese internet companies including Alibaba Cloud, ByteDance, and Xiaomi for similar deals.

telegram · zaihuapd · Jun 29, 09:31

**Background**: CXMT is a Chinese DRAM manufacturer founded in 2016, headquartered in Hefei, Anhui. DRAM chips are critical components in servers used for cloud computing, databases, and AI workloads. The global memory shortage has made long-term supply contracts a priority for many companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://m.ithome.com/html/970041.htm">消息称腾讯与长鑫 存 储签署 200 多亿元 内 存 芯 片 供应协议 - IT之家</a></li>
<li><a href="https://f5.pm/go-425897.html">腾讯与长鑫 存 储签署 内 存 芯 片 供应协议</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#semiconductors`, `#China`, `#Tencent`, `#supply chain`

---