---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 36 items, 11 important content pieces were selected

---

1. [OpenAI Releases GPT-5.6 with Three Model Sizes](#item-1) ⭐️ 9.0/10
2. [EU Parliament Passes Chat Control 1.0 via Procedural Vote](#item-2) ⭐️ 9.0/10
3. [Bun Rewritten from Zig to Rust](#item-3) ⭐️ 9.0/10
4. [TypeScript 7.0 Released: Go Rewrite Delivers Up to 12x Speed Boost](#item-4) ⭐️ 9.0/10
5. [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](#item-5) ⭐️ 9.0/10
6. [Postgres rewritten in Rust passes all regression tests](#item-6) ⭐️ 8.0/10
7. [Meta Launches Muse Spark 1.1 Agentic AI Model](#item-7) ⭐️ 8.0/10
8. [OpenAI Introduces GPT-Live for ChatGPT Voice Mode](#item-8) ⭐️ 8.0/10
9. [DJI EV50 VTOL Cargo Drone Reaches 8861m on Everest](#item-9) ⭐️ 8.0/10
10. [National Supercomputing Internet Core Node Launches in Zhengzhou](#item-10) ⭐️ 8.0/10
11. [OpenAI and US War Department to Ban AI for Domestic Surveillance](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-5.6 with Three Model Sizes](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI released GPT-5.6, a new frontier model available in three sizes: Luna, Terra, and Sol. It achieves state-of-the-art results on the ARC-AGI-3 benchmark and introduces improved intent understanding. GPT-5.6 sets a new state-of-the-art on ARC-AGI-3, a benchmark designed to measure human-like reasoning in AI agents, marking a significant step toward more general intelligence. Its improved intent understanding allows the model to better infer user goals, reducing the need for explicit step-by-step instructions. The three model sizes are priced per 1M tokens: Luna $1/$6, Terra $2.50/$15, Sol $5/$30. Sol is the first verified frontier model to beat an ARC-AGI-3 game, achieving a 7.8% score. All models have a knowledge cutoff of February 16, 2026.

hackernews · logickkk1 · Jul 9, 17:04 · [Discussion](https://news.ycombinator.com/item?id=48849066)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, infer goals, and plan actions, measuring human-like intelligence. Intent understanding refers to an AI's ability to infer the user's underlying goal from their query, enabling more natural interactions. GPT-5.6's improvements in this area allow it to better handle ambiguous requests.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>
<li><a href="https://arcprize.org/competitions/2026/arc-agi-3">ARC Prize 2026 - ARC-AGI-3 Competition</a></li>

</ul>
</details>

**Discussion**: Community comments highlight GPT-5.6's SOTA on ARC-AGI-3 and its intent understanding capabilities. Some users discuss model comparisons (e.g., Codex vs. Claude Code) and note that OpenAI omitted Fable 5 from certain benchmarks because it refused to answer advanced biology questions. There is also sentiment that despite OpenAI's closed nature, many hope it outperforms Anthropic.

**Tags**: `#AI`, `#LLM`, `#OpenAI`, `#GPT-5.6`, `#ARC-AGI`

---

<a id="item-2"></a>
## [EU Parliament Passes Chat Control 1.0 via Procedural Vote](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

The EU Parliament passed Chat Control 1.0 on July 9, 2026, allowing warrantless scanning of private messages on platforms like Instagram, Discord, and Gmail until 2028, despite a majority of voting MEPs opposing it (314 against, 276 in favor, 17 abstentions). The measure was adopted because a motion to reject it failed to achieve the required absolute majority of 361 votes. This legislation significantly undermines digital privacy and encryption in the EU, setting a precedent for mass surveillance of private communications. It affects millions of users and could erode trust in digital platforms, while also impacting the broader debate on balancing child protection with civil liberties. The vote was held on the last day before the summer break, with 113 MEPs absent, and used a procedural rule requiring an absolute majority of all MEPs (361) to reject the measure, rather than a simple majority of those voting. The scanning applies to direct messages on unencrypted platforms, while public posts and cloud storage remain unaffected by this specific law.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control refers to a set of EU regulations aimed at combating child sexual abuse material online. Chat Control 1.0, initially proposed in 2022, allows voluntary scanning of private messages by tech companies without a warrant. The regulation had been rejected twice in March 2026 but was revived through a procedural vote. Critics argue it violates privacy and encryption rights, while supporters claim it is necessary to protect children.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm">EU Parliament Passes Chat Control by Default: 314 MEPs Couldn ...</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at the parliamentary maneuver, calling it undemocratic and a step toward totalitarianism. Many highlighted the procedural trick of requiring an absolute majority to reject the law, and the timing of the vote just before the summer break to minimize attendance. Some noted that this could awaken people to structural issues in EU governance.

**Tags**: `#privacy`, `#surveillance`, `#EU legislation`, `#encryption`, `#digital rights`

---

<a id="item-3"></a>
## [Bun Rewritten from Zig to Rust](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Jarred Sumner announced the rewrite of the Bun JavaScript runtime from Zig to Rust, citing memory safety and bug reduction as key motivations. The rewrite was completed in 11 days using advanced agentic engineering workflows powered by frontier AI models. This demonstrates that large-scale rewrites of critical infrastructure are now feasible with AI assistance, challenging the long-held belief that rewrites should never be attempted. It also highlights Rust's growing dominance in systems programming due to its memory safety guarantees. The rewrite cost an estimated $165,000 in API tokens (5.9 billion uncached input tokens, 690 million output tokens). The new Rust-based Bun has been live in Claude Code since June 17, 2026, with 10% faster startup on Linux.

rss · Simon Willison · Jul 8, 23:57

**Background**: Bun is a JavaScript runtime, package manager, and test runner designed as a drop-in replacement for Node.js, originally written in Zig. The rewrite was enabled by a TypeScript-based conformance suite with a million assertions, allowing AI agents to automate the porting process. Agentic workflows involve autonomous AI agents that make decisions and coordinate tasks with minimal human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-workflows">What are agentic workflows? - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-4"></a>
## [TypeScript 7.0 Released: Go Rewrite Delivers Up to 12x Speed Boost](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft has officially released TypeScript 7.0, a major version that rewrites the compiler in Go, achieving 8-12x faster full builds and supporting shared-memory multi-threading. Users can install it via npm, and editors can adopt the new language server through LSP. This release represents a paradigm shift for TypeScript, dramatically improving developer productivity by reducing type-checking and build times by an order of magnitude. It also showcases Go's viability for building high-performance developer tooling, potentially influencing future language infrastructure. TypeScript 7.0 introduces experimental --checkers and --builders flags to customize parallelism, and provides a compatibility package for coexistence with TypeScript 6. However, toolchains for embedded languages like Vue and Svelte are not yet ready and must still use the old version.

telegram · zaihuapd · Jul 9, 04:01

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, widely used for large-scale web development. The previous compiler was written in TypeScript itself (bootstrapped) and ran on JavaScript, which limited performance. The Language Server Protocol (LSP) standardizes communication between editors and language servers, enabling features like code completion and error checking across different IDEs.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/">Announcing TypeScript 7.0 - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler ...</a></li>

</ul>
</details>

**Discussion**: The community has expressed strong enthusiasm for the performance improvements, with many developers noting that the 10x speedup will significantly improve their workflows. Some concerns have been raised about the lack of support for Vue and Svelte toolchains, but overall sentiment is highly positive.

**Tags**: `#TypeScript`, `#Microsoft`, `#Programming Languages`, `#Performance`, `#Open Source`

---

<a id="item-5"></a>
## [Ant Group Open-Sources LingBot-Video, First MoE Embodied Video Model](https://www.qbitai.com/2026/07/446458.html) ⭐️ 9.0/10

Ant Group has open-sourced LingBot-Video, the world's first Mixture-of-Experts (MoE) based embodied video foundation model. It achieves state-of-the-art performance on the RBench robot manipulation benchmark, surpassing models like Wan2.6, Seedance1.5 Pro, and Cosmos3 Super. This breakthrough significantly improves efficiency in embodied AI video generation, activating only ~3B of its 30B parameters per inference, achieving roughly 3x the inference speed of comparable dense models. The open-source release under Apache 2.0 accelerates research in robot action prediction, simulation data generation, and world models. LingBot-Video uses a DiT+MoE architecture to balance capacity and cost, and was trained on a proprietary 70,000-hour embodied data engine covering dexterous manipulation, robot locomotion, and first-person interaction. It also introduces a multi-dimensional reinforcement learning reward system that emphasizes physical plausibility and task completion beyond aesthetics and motion consistency.

telegram · zaihuapd · Jul 9, 04:30

**Background**: Mixture-of-Experts (MoE) is an AI architecture that uses multiple specialized submodels (experts) activated selectively, enabling larger total parameters with lower inference cost. Embodied AI video foundation models generate videos conditioned on robot actions or observations, serving as world models for planning and simulation. DiT (Diffusion Transformer) is a popular backbone for video generation that combines diffusion models with transformer architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? - NVIDIA</a></li>
<li><a href="https://www.emergentmind.com/topics/video-diffusion-transformer-dit">Video Diffusion Transformer (DiT) Overview</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#MoE`, `#video generation`, `#robotics`, `#open source`

---

<a id="item-6"></a>
## [Postgres rewritten in Rust passes all regression tests](https://github.com/malisper/pgrust) ⭐️ 8.0/10

An experimental project called pgrust has used LLMs to rewrite the PostgreSQL database in Rust, achieving a 100% pass rate on the official Postgres regression tests. This demonstrates the potential of LLMs to perform large-scale code rewrites, sparking debate about AI's role in software engineering and the feasibility of rewriting critical infrastructure in memory-safe languages. The project generated 7,101 commits in less than a month, making traditional code review impractical. The rewritten code is licensed under AGPL, a change from PostgreSQL's original license.

hackernews · SweetSoftPillow · Jul 9, 06:18 · [Discussion](https://news.ycombinator.com/item?id=48841676)

**Background**: PostgreSQL is a 30-year-old open-source relational database with a comprehensive regression test suite. Rust is a systems programming language known for memory safety. LLMs (large language models) are AI models that can generate and transform code based on prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/regress.html">PostgreSQL: Documentation: 18: Chapter 31. Regression Tests</a></li>
<li><a href="https://www.postgresql.org/docs/current/regress-run.html">PostgreSQL: Documentation: 18: 31.1. Running the Tests</a></li>
<li><a href="https://arxiv.org/abs/2410.08806">[2410.08806] Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about code review feasibility due to the massive number of AI-generated commits, license compatibility issues (AGPL vs. original PostgreSQL license), and general skepticism about trusting AI rewrites for critical software. Some suggest mirroring production queries to compare behavior.

**Tags**: `#PostgreSQL`, `#Rust`, `#LLM`, `#Database`, `#AI-assisted programming`

---

<a id="item-7"></a>
## [Meta Launches Muse Spark 1.1 Agentic AI Model](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta has released Muse Spark 1.1, a multimodal reasoning model designed for agentic tasks, with a 1M-token context window and improved tool use, computer use, coding, and multimodal understanding. It is available via the Meta Model API with commercial pricing at $1.25/$4.5 per 1M tokens for input/output and $0.15 for cached input. This release marks Meta's entry into the commercial agentic AI market, challenging OpenAI and Anthropic with competitive pricing and open-weight availability. The debate over benchmark validity and open-source strategy could influence how the AI community evaluates and adopts agentic models. The model is evaluated on Terminal-Bench 2.1, but a community comment notes that the evaluation used 6 CPU cores and 8GB RAM, which may exceed the task's resource limits and disqualify the results. The model also supports a 'Thinking' mode in the Meta AI app and at meta.ai.

hackernews · ot · Jul 9, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48846184)

**Background**: Agentic AI models are designed to autonomously perform tasks using tools, code, and computer interactions, going beyond simple text generation. Meta's Muse Spark series is part of its broader strategy to develop frontier AI capabilities while maintaining an open-source approach, though Muse Spark 1.1 is offered as a commercial API with pricing.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/">Introducing Muse Spark 1.1</a></li>
<li><a href="https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report">Muse Spark 1.1 Evaluation Report</a></li>
<li><a href="https://www.datacamp.com/blog/muse-spark-1-1">Muse Spark 1.1: Meta's Agentic Model and API | DataCamp</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about benchmark methodology, with one user arguing that the resource caps used in evaluation violate Terminal-Bench 2.1 rules. Another user shared a practical integration plugin for LLM, while others debated Meta's pricing strategy and open-source role, with some praising the low cost and others expressing skepticism about real-world performance.

**Tags**: `#AI`, `#Meta`, `#agentic model`, `#open source`, `#benchmarking`

---

<a id="item-8"></a>
## [OpenAI Introduces GPT-Live for ChatGPT Voice Mode](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI has upgraded ChatGPT's voice mode with GPT-Live, a new model that can delegate complex tasks to GPT-5.5 in the background while maintaining conversation flow. This upgrade significantly improves the usefulness of ChatGPT's voice mode by enabling real-time delegation of heavy tasks, making it a more capable brainstorming partner and assistant. GPT-Live uses a full-duplex architecture, allowing simultaneous listening and speaking, and can keep talking while GPT-5.5 works on delegated tasks. The previous voice mode was based on an older GPT-4o model with a 2024 knowledge cutoff.

rss · Simon Willison · Jul 8, 23:20

**Background**: ChatGPT voice mode allows users to speak with ChatGPT and hear spoken responses. GPT-5.5 is OpenAI's latest frontier model, released in April 2026, with strong performance on coding, research, and data analysis. GPT-Live is designed to make voice conversations feel more natural and intelligent.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT‑5.5 - OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-live">GPT-Live System Card - OpenAI Deployment Safety Hub</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-Live`, `#ChatGPT`, `#voice mode`, `#AI`

---

<a id="item-9"></a>
## [DJI EV50 VTOL Cargo Drone Reaches 8861m on Everest](https://www.163.com/dy/article/L1CUCV940514R9OJ.html) ⭐️ 8.0/10

DJI's unreleased EV50 VTOL cargo drone successfully flew to an altitude of 8861 meters on Mount Everest during the 'Peak Mission' scientific expedition, setting a record for the highest flight altitude among similar publicly tested drones. This achievement demonstrates the extreme altitude capability of VTOL cargo drones, paving the way for high-altitude logistics and scientific research. It also showcases DJI's technological leadership in drone design and reliability under harsh conditions. The EV50 is a composite-wing VTOL drone that can take off and land vertically and switch to fixed-wing cruise. During the 12-day mission, it completed 32 takeoffs and landings, climbed 3730 meters continuously, and still had 30% battery remaining on return.

telegram · zaihuapd · Jul 9, 06:00

**Background**: VTOL (Vertical Take-Off and Landing) drones combine the vertical lift capability of multi-rotors with the efficient cruise of fixed-wing aircraft. Composite-wing drones are a type of VTOL that uses separate rotors for lift and a fixed wing for forward flight, enabling longer range and endurance. DJI is a leading drone manufacturer, and the EV50 is its first VTOL cargo drone designed for long-distance logistics.

<details><summary>References</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260709A0AKS300">大疆发布首款垂直起降运载无人机DJI EV50：航程150公里 最大载重50千...</a></li>
<li><a href="https://baike.baidu.com/item/复合翼无人机/67152229">复合翼无人机_百度百科</a></li>
<li><a href="https://zh.wikipedia.org/wiki/垂直起降">垂直起降 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#drones`, `#DJI`, `#VTOL`, `#record`, `#logistics`

---

<a id="item-10"></a>
## [National Supercomputing Internet Core Node Launches in Zhengzhou](https://36kr.com/newsflashes/3887797387344387) ⭐️ 8.0/10

On July 9, 2026, the core node of China's National Supercomputing Internet was officially launched in Zhengzhou, providing over 100,000 domestic AI computing cards. This is the largest single domestic AI computing resource pool connected to the platform since its inception. This milestone significantly boosts China's self-reliance in AI computing infrastructure, enabling large-scale AI model training and scientific computing without reliance on foreign chips. It strengthens the national computing resource scheduling system and supports digital transformation across industries. The core node is a single 100,000-card full-precision computing resource pool that can simultaneously support training of trillion-parameter models, AI for Science (AI4S), and large-scale scientific engineering calculations. It has already adapted over 400 mainstream large models and world models.

telegram · zaihuapd · Jul 9, 07:00

**Background**: The National Supercomputing Internet, initiated by China's Ministry of Science and Technology, connects over 30 national supercomputing and intelligent computing centers across 14 provinces. It aims to break the isolated operation model of individual computing centers and build an integrated computing service platform. Domestic AI computing cards, produced by companies like Huawei, Cambricon, and Kunlunxin, have matured from 'usable' to 'easy-to-use' by 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网核心节点/63648019">国家超算互联网核心节点_百度百科 超算互联网 - scnet.cn 国家超算互联网核心节点正式上线：可提供超过10万卡国产AI算力 国家超算互联网核心节点正式上线！_新浪科技_新浪网 国家超算互联网核心节点正式上线|运营|人工智能|工业互联网平台_网易... Top Stories</a></li>
<li><a href="https://baike.baidu.com/item/国产算力卡/67727675">国产算力卡_百度百科</a></li>

</ul>
</details>

**Tags**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#AI chips`

---

<a id="item-11"></a>
## [OpenAI and US War Department to Ban AI for Domestic Surveillance](https://t.me/zaihuapd/42459) ⭐️ 8.0/10

OpenAI and the US Department of War have agreed to amend their AI cooperation contract to include clauses explicitly prohibiting the use of AI systems for domestic surveillance of US citizens. The revision was proposed by OpenAI CEO Sam Altman to address public concerns about mass surveillance. This proactive measure by a leading AI company sets a precedent for ethical AI deployment in military contexts and could influence future AI governance policies. It directly addresses civil liberties concerns and may shape how other tech companies approach contracts with defense agencies. The amended clauses specifically prohibit deliberate surveillance of US citizens and the use of commercially obtained personally identifiable information for tracking or monitoring. The contract has not yet been formally signed, and the move follows a similar controversy that led Anthropic to suspend its agreement with the War Department.

telegram · zaihuapd · Jul 9, 13:22

**Background**: In 2025, the US Department of Defense awarded contracts to multiple AI companies, including OpenAI and Anthropic, to accelerate AI adoption for national security. However, concerns about AI being used for mass domestic surveillance and autonomous weapons led to public backlash and internal debates. Anthropic's contract was suspended after disputes over military use of its AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/our-agreement-with-the-department-of-war/">Our agreement with the Department of War - OpenAI</a></li>
<li><a href="https://tech-insider.org/openai-pentagon-military-ai-deal-2026/">OpenAI Pentagon Deal: 4 Controversial Terms [2026]</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#OpenAI`, `#military AI`, `#surveillance`, `#policy`

---