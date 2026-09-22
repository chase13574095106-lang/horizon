---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 36 items, 13 important content pieces were selected

---

1. [OpenAI Releases GPT-6 Sol and Luna with Major Price Cuts](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Opus 5.5 With Major Price Cuts](#item-2) ⭐️ 9.0/10
3. [Pentagon Blames AI Overreliance for Deadly Strike on Iranian School](#item-3) ⭐️ 9.0/10
4. [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](#item-4) ⭐️ 9.0/10
5. [vLLM v0.30.0 ships Fast Start GPU weight-cache daemon and many new models](#item-5) ⭐️ 8.0/10
6. [ShinyHunters Claims Breach of FBI Employee Data](#item-6) ⭐️ 8.0/10
7. [25 Fields Medalists Warn AI May Be Misaligned with Math Research Goals](#item-7) ⭐️ 8.0/10
8. [Alibaba unveils Zhenwu V900, claims strongest domestic AI chip with 3x compute](#item-8) ⭐️ 8.0/10
9. [Cloudflare Python Workers Reach General Availability](#item-9) ⭐️ 8.0/10
10. [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](#item-10) ⭐️ 8.0/10
11. [US Proposes AI Incident Notification Channel with China](#item-11) ⭐️ 8.0/10
12. [China Probes DeepSeek and Moonshot Over Data Leaks to Anthropic's Claude](#item-12) ⭐️ 8.0/10
13. [DeepSeek to Brief UN Security Council on AI Risks](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-6 Sol and Luna with Major Price Cuts](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI announced GPT-6 Sol and GPT-6 Luna, a new generation of models that bring frontier intelligence to everyday work with different balances of capability and cost. Both models are priced at roughly half of what OpenAI charged for GPT-5.6 Sol and GPT-5.6 Luna under their promotional pricing, and they use fewer tokens to run than their predecessors. The steep price cuts could significantly lower the cost of running AI agents and enterprise workloads, intensifying competition with rivals like Anthropic's Claude Code. Developers and businesses choosing between model providers will need to reassess the trade-offs between capability, usage limits, and cost. OpenAI says GPT-6 Sol makes half as many mistakes as GPT-5.6, while GPT-6 Luna matches previous higher-tier performance at far lower cost. The GPT-6 family also changes prompt caching, with higher default cache hit rates and a 90% discount on cached input reads, and allows changing reasoning effort or available tools mid-conversation without losing the cache.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**Background**: OpenAI has been iterating rapidly on its GPT model lineup, with GPT-5.6 serving as the previous generation for both its higher-tier Sol and lower-tier Luna variants. Prompt caching is a technique that stores parts of a prompt so repeated requests cost less and run faster, making it important for agentic and high-volume workloads. The new release arrives amid intense competition among AI coding assistants such as OpenAI's Codex and Anthropic's Claude Code.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more">VentureBeatOpenAI releases GPT-6 Sol and Luna models, slashing API ...</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI's GPT - 6 Sol doubles its accuracy rate - for half the cost - ZDNET</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters focused heavily on the pricing, with simonw calling GPT-6 Luna being half the price of GPT-5.6 Luna 'a really big deal.' Others debated usage limits between Codex and Claude Code, and m_fayer expressed attachment to GPT-5.6 Sol, worrying that a technically better successor might not feel as natural to work with.

**Tags**: `#OpenAI`, `#GPT-6`, `#AI models`, `#pricing`, `#Hacker News`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Opus 5.5 With Major Price Cuts](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic released Claude Opus 5.5, its first model since publicly calling for 'pacing the frontier,' featuring improved communication abilities and across-the-board price cuts: cache reads dropped from $0.50 to $0.20 per million tokens, input from $5 to $4, output from $25 to $20, and cache writes from $6.25 to $5. The model was tested before release by external evaluators including Frontier Design and METR, and is served by five providers on OpenRouter. The price cuts directly challenge cheaper competitors like DeepSeek, which some users say they now prefer for cost-sensitive agentic coding tasks, while the release undercuts Anthropic's own stated safety stance on slowing frontier development. As one of the highest-spend models on OpenRouter, Opus's pricing shift could reshape provider economics across the LLM API market. Anthropic emphasizes that Opus 5.5 'communicates more naturally than prior models,' putting key information up front and making long work sessions easier to follow, which the company frames as both a usability and safety benefit. The model is available through Amazon Bedrock, Azure, Google Vertex, Claude Platform on AWS, and Anthropic itself, with automatic failover and provider pinning on OpenRouter.

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**Background**: Anthropic's Claude family ships in three tiers—Haiku, Sonnet, and Opus—with Opus as the most capable. 'Frontier models' are the most advanced AI systems available at a given moment, trained on massive datasets at costs that can reach hundreds of millions of dollars, and they typically power advanced reasoning and agentic workflows. Anthropic has positioned itself as a safety-focused lab, and its recent call to 'pace the frontier' referred to slowing the race toward ever-more-capable models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**Discussion**: Commenters widely celebrated the price drop, with one noting Opus 5 was likely the highest-spend model on OpenRouter, while others criticized the apparent contradiction between Anthropic's 'pacing the frontier' rhetoric and its continued rapid releases. Some users said they now prefer DeepSeek v4.1 for cheap, hardworking agentic coding, and one shared pelican benchmark images across thinking levels.

**Tags**: `#AI/ML`, `#LLM`, `#Anthropic`, `#Model Release`, `#AI Safety`

---

<a id="item-3"></a>
## [Pentagon Blames AI Overreliance for Deadly Strike on Iranian School](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

A Pentagon report concluded that the U.S. "failed in its obligation to do everything feasible to verify" that an Iranian school in Minab was a military objective, and that the failure "went beyond mere negligence." The report attributed the deadly missile strike partly to overreliance on AI-assisted targeting tools, including Palantir's Maven Smart System, which recommended the school based on outdated intelligence data. This is one of the first confirmed cases where AI-assisted military targeting contributed to mass civilian casualties, intensifying global debate over accountability, human oversight, and the limits of AI in lethal decision-making. It could accelerate calls for binding international norms on military AI and reshape how defense agencies deploy and audit such systems. The Minab site had been cataloged as an Islamic Revolutionary Guard Corps facility due to outdated data and was fed into Maven alongside other candidates, emerging as a recommendation; officials said some users expected Maven to flag stale records or contradictions, though it is unclear why they held that expectation. The report's finding that the failure "went beyond mere negligence" and that the U.S. acted "recklessly" raises the legal stakes considerably.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**Background**: The Maven Smart System is the product of a decade-long collaboration between the U.S. Department of Defense and the tech industry to enhance intelligence analysis, surveillance, and targeting; it is designed to support human operators, not replace them. AI decision-support systems in targeting can propose military objectives and give actionable recommendations, and research has long warned of "automation bias" — the human tendency to over-trust AI outputs, especially under high-pressure conditions. International humanitarian law requires that parties to a conflict do everything feasible to verify that a target is a legitimate military objective, and human responsibility for decisions on the use of weapons must be retained since accountability cannot be transferred to machines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.brennancenter.org/our-work/research-reports/militarys-use-ai-explained">The Military’s Use of AI, Explained | Brennan Center for Justice</a></li>
<li><a href="https://blogs.icrc.org/law-and-policy/2024/08/29/artificial-intelligence-in-military-decision-making-supporting-humans-not-replacing-them/">AI in military decision-making: supporting humans, not replacing them</a></li>
<li><a href="https://www.hrw.org/report/2015/04/09/mind-gap/lack-accountability-killer-robots">Mind the Gap: The Lack of Accountability for Killer Robots | HRW</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agreed that AI itself is not the root culprit, with one noting the details suggest the failure was human and procedural rather than algorithmic. Several argued strongly that shifting decision-making authority to AI does not absolve humans of responsibility, since "an AI can't be tried in a court," and criticized both the Pentagon and Palantir for deflecting blame rather than accepting accountability. Others pointed to a deeper problem: officials who don't understand AI's blind spots embraced it as an "ultimate analyst," expecting capabilities the system never had.

**Tags**: `#AI ethics`, `#military AI`, `#accountability`, `#AI limitations`, `#defense technology`

---

<a id="item-4"></a>
## [OpenAI Begins Limited Preview of GPT-5.6 Series: Sol, Terra, Luna](https://t.me/zaihuapd/43990) ⭐️ 9.0/10

OpenAI has started a limited preview of its GPT-5.6 series, introducing three tiers: Sol (flagship), Terra (balanced), and Luna (low-cost). Sol emphasizes stronger coding, biosecurity, and cybersecurity capabilities, and adds a new 'max' reasoning intensity plus an 'ultra' mode, while Terra offers performance close to GPT-5.5 at 2x lower cost and Luna targets the lowest-cost segment. This is a major model release that reshapes OpenAI's product lineup across capability and price tiers, potentially pressuring competitors and changing cost-performance expectations for developers and enterprises. The tiered structure also signals OpenAI's strategy of segmenting the market by task complexity and budget. The preview is initially limited to a small number of trusted partners via the API and Codex, and OpenAI describes it as a short-term step taken at the request of the U.S. government, with plans to expand to ChatGPT and Codex in the coming weeks. Sol launches with OpenAI's most robust safety stack to date.

telegram · zaihuapd · Sep 22, 18:04

**Background**: OpenAI's GPT series are large language models that power ChatGPT and the API, with each generation typically improving reasoning, coding, and safety. Codex is OpenAI's AI coding agent, available through the ChatGPT web app, CLI, desktop app, and IDE integrations, and it is one of the first surfaces for the GPT-5.6 preview. Biosecurity and cybersecurity capabilities refer to a model's potential to assist with or defend against biological and cyber threats, an area of growing policy concern as AI models become more capable.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-5-6-sol-terra-luna-explained">What Is GPT-5.6? OpenAI's Sol, Terra, and Luna Model Tiers Explained | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#API`, `#Codex`

---

<a id="item-5"></a>
## [vLLM v0.30.0 ships Fast Start GPU weight-cache daemon and many new models](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a major update with 762 commits from 315 contributors (104 of them new), adding support for models such as DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon, Cohere Compass, Bailing V3 VL and Nanbeige4.2. The headline feature is Fast Start, a persistent per-GPU weight-cache daemon that keeps post-quantized, TP-sharded weights in GPU memory so engines restart by mapping them over CUDA IPC with `--load-format ipc_cache` instead of reloading from disk. vLLM is one of the most widely used open-source LLM inference and serving engines, so its releases directly shape how production teams deploy models. Fast Start attacks one of the biggest operational pain points — slow cold starts and engine restarts — while the broad model support keeps vLLM aligned with the fast-moving frontier of open-weight architectures. Fast Start now also covers FP4 checkpoints and multi-node tensor parallelism, and the release adds Gumbel-max watermarking with per-request opt-out, HiSparse host-resident KV tiering for sparse-MLA decode, Model Runner V2 improvements (graph capture cut from 12s to 2s and engine init from 28.9s to 8.2s on H200), plus targeted online quantization via `quantization_config.targets` and FlashInfer CuTeDSL NVFP4 W4A16 as the default over Marlin on SM100/103.

github · khluu · Sep 22, 05:20

**Background**: vLLM is an open-source high-throughput, memory-efficient engine for serving large language models, supporting NVIDIA, AMD, Intel GPUs and x86/ARM/PowerPC CPUs plus plugins for TPUs, Gaudi, Ascend and other accelerators. Its core innovation is PagedAttention, which manages the KV cache in paged blocks to reduce memory waste, and it is commonly used with tensor parallelism (TP) to shard a model across multiple GPUs. Quantization formats like MXFP8 and NVFP4 reduce weight and activation precision to cut VRAM usage, while FlashMLA is DeepSeek's library of optimized multi-head latent attention (MLA) kernels used by its V3-series models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm -project/ vllm : A high-throughput and memory-efficient...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/configuration/optimization/">Optimization and Tuning - vLLM</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#GPU optimization`

---

<a id="item-6"></a>
## [ShinyHunters Claims Breach of FBI Employee Data](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

The hacking group ShinyHunters claims to have stolen data on all FBI employees, reportedly obtained through a PeopleSoft zero-day vulnerability that also exposed the FBI's AWS GovCloud environment storing employee and applicant information. The group told reporters it does not consider its planned action extortion but rather 'coercion,' and stated the campaign is not financially motivated. If confirmed, this would be one of the most significant breaches of U.S. federal law enforcement data, potentially exposing agents, analysts, and support staff to targeting by foreign intelligence services or criminal actors. It also raises serious questions about the security of government HR and cloud infrastructure, echoing past incidents like the 2015 OPM hack that compromised 22.1 million records. The stolen data reportedly came from systems accessed after an initial PeopleSoft compromise, including the FBI's AWS GovCloud environment used for employee and applicant records. ShinyHunters has not provided public proof of the full dataset, and the FBI has not officially confirmed the breach, leaving the scope and authenticity of the claim uncertain.

hackernews · spenvo · Sep 22, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49805278)

**Background**: ShinyHunters is a well-known hacking group that has previously claimed responsibility for breaches of companies like AT&T, Ticketmaster, and Santander. PeopleSoft is an enterprise resource planning (ERP) software suite made by Oracle, widely used by government agencies and large organizations for HR, payroll, and student administration. AWS GovCloud is a specialized cloud region designed to host sensitive government data at higher compliance levels. The 2015 Office of Personnel Management (OPM) breach, referenced by commenters, exposed personal data of over 22 million current and former federal employees and remains a benchmark for government data security failures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive.ph">Archive.ph</a></li>

</ul>
</details>

**Discussion**: Commenters expressed deep pessimism about the ability of any large organization to protect sensitive databases, with one noting that major state actors likely already possess most medical and biographical data. Others drew analogies to Battlestar Galactica's air-gapped systems and criticized the FBI's competence, while some debated whether ShinyHunters' threatened action constitutes extortion or coercion, with one suggesting a bizarre public humiliation demand instead of financial payment.

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#hacking`, `#national security`

---

<a id="item-7"></a>
## [25 Fields Medalists Warn AI May Be Misaligned with Math Research Goals](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

A group of 25 Fields Medalists, including Terence Tao and Deng Yu, issued a joint statement warning that the rapid use of AI to solve mathematical problems could cause AI development goals to become 'severely misaligned' with the true aims of mathematical research. The statement argues that treating math problem-solving as a benchmark for AI capability may harm mathematical research and the academic ecosystem. This is a rare collective intervention by the world's most decorated mathematicians, signaling that the AI-for-math boom could distort research incentives, evaluation metrics, and academic integrity. It will likely influence how funders, journals, and AI labs assess progress in automated mathematical reasoning. The statement notes that large language models have recently made major gains in solving significant mathematical problems, but warns that AI-generated output at scale could compress the time needed for verification, communication, and citing prior work, and raise issues around authorship and plagiarism. It also acknowledges that AI could improve research efficiency, with the outcome depending on how the technology is used.

telegram · zaihuapd · Sep 22, 03:00

**Background**: The Fields Medal is awarded every four years by the International Mathematical Union to up to four mathematicians under 40, and is widely described as the 'Nobel Prize of Mathematics'; 68 people have received it as of 2026. Terence Tao, a 2006 recipient, is a UCLA professor known for work in partial differential equations, combinatorics, and number theory, and has been an influential voice on AI's role in mathematics. Large language models such as GPT-4o, DeepSeek-V3, and Gemini-2.0 have shown rapidly improving performance on mathematical reasoning benchmarks, prompting debate about whether such benchmarks capture genuine mathematical understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fields_Medal">Fields Medal</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao</a></li>
<li><a href="https://arxiv.org/html/2506.00309v1">Evaluation of LLMs for mathematical problem solving</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Academic Publishing`, `#Fields Medal`

---

<a id="item-8"></a>
## [Alibaba unveils Zhenwu V900, claims strongest domestic AI chip with 3x compute](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

At the 2026 Yunqi Conference, Alibaba's T-Head (Pingtouge) unveiled the Zhenwu V900, a train-and-inference integrated AI chip it claims is China's strongest, delivering 3x the compute of the Zhenwu M890 with 216GB of memory and 1200GB/s inter-die bandwidth. CEO Wu Yongming said the self-developed M890 supernode already supports inference for 2-trillion-parameter models and will be scaled onto Alibaba Cloud this quarter, while the company plans a 500,000-card wide-area supernode cluster and Qwen models of 5-10 trillion parameters. The announcement signals that Alibaba is building a vertically integrated stack of models, chips, and cloud to reduce reliance on foreign accelerators amid export controls, and a 500,000-card cluster with 1GW of compute would rank among the world's largest AI training infrastructures. It also raises the competitive bar for domestic rivals such as Huawei, whose Atlas supernode clusters were previously positioned as the strongest in China. The V900 is a train-and-inference integrated chip with 216GB of memory and 1200GB/s inter-die bandwidth, but Alibaba has not disclosed detailed specs such as process node, peak throughput, or power consumption. The planned 500,000-card wide-area supernode cluster targets 1GW of compute, 200PB/s bandwidth, and 6-microsecond communication latency, built on the V900, NPO optical modules, HPN 8.0 networking, and CPFS storage, with the goal of supporting 10-trillion-parameter MoE model training.

telegram · zaihuapd · Sep 22, 03:30

**Background**: T-Head (Pingtouge) is Alibaba's in-house chip design unit, and the Zhenwu series is its AI accelerator line; the M890 is the previous generation, and the V900 is positioned as its successor, with a further J900 also on the disclosed roadmap. Supernodes are tightly coupled clusters of many accelerators connected by high-speed interconnects, designed to train and serve very large models that cannot fit on a single node. Qwen is Alibaba's open-weight large language model family, and parameter count (such as 5-10 trillion) is a rough measure of model scale, with trillion-parameter MoE models requiring massive distributed training infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/1/005/602.htm">最强国产 AI 芯 片 阿里 平 头 哥 真 武 V 900 ...</a></li>
<li><a href="https://www.chooseai.net/news/7318/">阿里云计划建 50 万卡广域超节点集群：1GW 算力、6 微秒通信延迟-Choo...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2085708631140579231">阿里研究员透露Qwen4.5后模型将扩展至5-10T参数 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Alibaba`, `#T-Head`, `#Qwen`, `#datacenter infrastructure`

---

<a id="item-9"></a>
## [Cloudflare Python Workers Reach General Availability](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

On September 21, Cloudflare announced the general availability of Python Workers, making Python a first-class language on its developer platform with seamless access to Workers AI, R2, and D1. The feature, first launched two years ago, now natively supports frameworks like FastAPI, Django, and Flask, and adds low-level networking capabilities that allow running PostgreSQL and AI libraries such as LangChain directly within Workers. This milestone significantly lowers the barrier for Python developers to deploy applications on the edge, as they can now use familiar frameworks and AI libraries without leaving Cloudflare's serverless environment. It signals a broader shift in edge computing toward first-class support for Python, potentially affecting how cloud applications are built and deployed across the industry. Python Workers run via Pyodide, a WebAssembly-compiled Python interpreter, inside V8 isolates, which enables broad Python application support but may impose performance and compatibility constraints compared to native runtimes. The GA release includes support for the Python standard library and packages, and integrates with Cloudflare's global network for AI inference through Workers AI.

telegram · zaihuapd · Sep 22, 04:00

**Background**: Cloudflare Workers is a serverless platform that lets developers run code across Cloudflare's global edge network without managing infrastructure. Python Workers were first introduced two years ago as a way to bring Python to this environment, using WebAssembly and Pyodide to run Python code in V8 isolates. Workers AI provides serverless GPU-powered AI inference, while R2 is an egress-free object storage service and D1 is a serverless SQL database, all part of Cloudflare's developer platform.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/">How Python Workers Work - Cloudflare Docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Python`, `#Serverless`, `#Edge Computing`, `#Workers AI`

---

<a id="item-10"></a>
## [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI and Tsinghua University jointly released a technical report on DeepSeek Elastic Compute (DSec), a sandbox infrastructure platform that serves about 3 million sandbox instances per day and supports large-scale agent training and evaluation. The platform offers four backends — FnCall, containers, Firecracker microVMs, and full VMs — through a unified SDK, and decouples stateful rollout execution from preemptible GPU training. Agent training and evaluation increasingly depend on massive numbers of isolated execution environments, and DSec shows that such infrastructure can be operated at production scale with high density and fast creation rates. The reported optimizations and production metrics provide a concrete reference for other teams building reinforcement learning and agent systems, and reinforce DeepSeek's position in open AI infrastructure. A single production unit of DSec uses about 160 nodes, with peak concurrency exceeding 380,000 sandboxes and a creation rate above 5,000 per second; one node can host up to 3,200 containers or 800 microVMs. By loading EROFS images on demand from the 3FS distributed file system instead of pulling full Docker images, DSec reports 1.7x faster task completion and 57% less disk write, while memory sharing and reclamation cut peak memory usage by about 40%.

telegram · zaihuapd · Sep 22, 04:45

**Background**: Sandboxes are isolated execution environments used to safely run untrusted code, which is essential when training AI agents that interact with tools, operating systems, or security scenarios. Firecracker is an open-source virtualization technology from AWS that creates lightweight microVMs with strong isolation and low overhead, while EROFS is a read-only Linux filesystem optimized for container and sandbox images. 3FS is DeepSeek's own high-performance distributed file system designed for AI training and inference workloads, and DSec builds on these components to serve millions of sandboxes per day.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/3FS">GitHub - deepseek-ai/3FS: A high-performance distributed file ...</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast ... GitHub - firecracker-microvm/firecracker: Secure and fast ... I tried Firecracker microVMs for self-hosted services, and it ... firecracker-microvm/firecracker | DeepWiki Run Your First Firecracker microVM - labs.iximiuz.com What Is a Firecracker VM? · Learn</a></li>
<li><a href="https://docs.kernel.org/filesystems/erofs.html">EROFS - Enhanced Read-Only File System — The Linux Kernel documentation</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#agent training`, `#sandbox`, `#DeepSeek`, `#systems`

---

<a id="item-11"></a>
## [US Proposes AI Incident Notification Channel with China](https://x.com/rohanpaul_ai/status/2102254209597157548) ⭐️ 8.0/10

The United States has proposed establishing an AI incident notification channel with China to report AI-related events that meet national security thresholds, a proposal raised during September 20 talks in New York. US Treasury Secretary Bessent said the aim is to improve transparency between the two countries, and the two sides also plan regular US-China AI dialogue on shared risks. This is a significant geopolitical development in AI governance, signaling a potential shift toward bilateral transparency and risk management between the world's two leading AI powers. If realized, such a channel could reduce the risk of miscalculation over dangerous AI incidents and set a precedent for international AI safety cooperation. The proposal has not yet become a bilateral agreement or treaty, and China's official statement confirmed that AI-related issues were discussed but did not explicitly accept the specific mechanism. The channel would only cover incidents meeting national security thresholds, leaving the definition of such thresholds unresolved.

telegram · zaihuapd · Sep 22, 06:48

**Background**: AI incident reporting systems are structured processes for systematically collecting, analyzing, and mitigating harm events caused directly or indirectly by AI systems. The US and China are the world's two leading AI powers, and bilateral engagement on AI safety had been largely frozen for about two years before this dialogue. Scoping such talks is difficult because 'AI' can mean anything from self-driving cars and facial recognition to autonomous weapons and large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ai-incident-reporting-systems">AI Incident Reporting Systems</a></li>
<li><a href="https://www.brookings.edu/articles/a-roadmap-for-a-us-china-ai-dialogue/">A roadmap for a US - China AI dialogue | Brookings</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2o3MjlyOUVSRWsxaVhIcmY2bGp5Z0FQAQ?hl=en-US&gl=US&ceid=US:en">US proposes AI incident alert system in talks with China - Overview</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#US-China relations`, `#AI safety`, `#policy`, `#national security`

---

<a id="item-12"></a>
## [China Probes DeepSeek and Moonshot Over Data Leaks to Anthropic's Claude](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic) ⭐️ 8.0/10

China's internet regulator is investigating DeepSeek and Moonshot AI over allegations that they forwarded sensitive user data to Anthropic's Claude model, according to people familiar with the matter. The probe follows a 154-page report Anthropic published on September 10, which accused seven Chinese companies of large-scale misuse of Claude and cited an example of DeepSeek forwarding a request from an engineer working on police surveillance systems. This case sits at the intersection of AI governance, data privacy, and escalating US-China tech tensions, and could set precedents for how Chinese regulators police cross-border data flows involving foreign AI models. It may also affect how DeepSeek and Moonshot — two of China's most prominent AI startups — operate and are perceived internationally. Anthropic's report specifically names seven Chinese companies for large-scale violations of its Claude usage policies, with the DeepSeek example involving an engineer working on police surveillance systems. The investigation is being conducted by China's internet regulator, though no formal charges or penalties have been announced yet.

telegram · zaihuapd · Sep 22, 14:37

**Background**: DeepSeek is a Hangzhou-based AI company owned by hedge fund High-Flyer that develops open-weight large language models and released its DeepSeek-R1 chatbot in January 2025, which briefly surpassed ChatGPT as the most downloaded free app on the US iOS App Store. Moonshot AI is a Chinese startup known for its Kimi series of models, including the open-source reasoning-oriented Kimi K2 Thinking. Anthropic is the US AI safety company behind the Claude assistant, and its report accusing Chinese firms of misusing Claude triggered the regulatory scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://free.theresanaiforthat.com/company/moonshot-ai/">Moonshot AI | There's An AI For That</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#data privacy`, `#DeepSeek`, `#Moonshot AI`, `#Anthropic`

---

<a id="item-13"></a>
## [DeepSeek to Brief UN Security Council on AI Risks](https://t.me/zaihuapd/43989) ⭐️ 8.0/10

Two sources say Chinese AI startup DeepSeek will brief the 15-member UN Security Council this week on the risks posed by artificial intelligence, with OpenAI CEO Sam Altman and senior Anthropic representatives also expected to attend the Wednesday session on AI and international security. DeepSeek and Moonshot are among the Chinese AI firms invited to speak, though DeepSeek founder Liang Wenfeng does not plan to attend and the arrangements could still change. This marks a rare moment where leading Chinese and US AI labs appear before the UN's top security body together, signaling that AI risk is now treated as a matter of international peace and security rather than purely a technical or commercial issue. It could shape emerging global AI governance norms and give Chinese AI developers a direct voice in setting international safety expectations. The briefing is scheduled for Wednesday before the 15-member Security Council, with Altman planning to attend and Anthropic sending senior representatives, while DeepSeek founder Liang Wenfeng is not expected to appear. The lineup of speakers and arrangements remain subject to last-minute changes, according to the sources cited by Reuters.

telegram · zaihuapd · Sep 22, 17:39

**Background**: The UN Security Council first convened in July 2023 to discuss how AI affects international peace and security, and member states have since recognized its potential to reshape economics, warfare, and peacemaking. DeepSeek is a Hangzhou-based Chinese AI company, funded by the hedge fund High-Flyer, that develops open-weights large language models, while Anthropic is a US AI safety and research company behind the Claude assistant. Bringing these labs before the Council reflects growing momentum to place frontier AI under multilateral scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.securitycouncilreport.org/atf/cf/{65BFCF9B-6D27-4E9C-8CD3-CF6E4FF96FF9}/Concept+Note+AI+UNSC+Signature+Event+(1).pdf">CONCEPT NOTE: UN Security Council Briefing on Artificial ...</a></li>
<li><a href="https://www.anthropic.com/careers">Careers \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#DeepSeek`, `#UN Security Council`, `#AI safety`, `#international security`

---