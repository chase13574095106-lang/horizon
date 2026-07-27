---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 26 items, 10 important content pieces were selected

---

1. [Moonshot AI Open-Sources Kimi K3, a 2.8T-Parameter Model](#item-1) ⭐️ 9.0/10
2. [Critical Fastjson 1.x RCE Without Gadgets or AutoType](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0: Inkling Support, DeepSeek-V4 Optimizations, Flexible Attention](#item-3) ⭐️ 8.0/10
4. [Anthropic Clarifies Stance on Open-Weights Models](#item-4) ⭐️ 8.0/10
5. [Judge Rejects Google's DMCA Defense in Web Scraping Case](#item-5) ⭐️ 8.0/10
6. [Bun's Rust Rewrite Progress: Shipped in Claude Code, 1.4 Delayed](#item-6) ⭐️ 8.0/10
7. [CXMT surges 471.59% on STAR Market debut, record IPO](#item-7) ⭐️ 8.0/10
8. [Google Teases Gemini 4 as Most Ambitious Pretraining Yet](#item-8) ⭐️ 8.0/10
9. [China Refutes US Sanctions Threat Over AI Model Distillation](#item-9) ⭐️ 8.0/10
10. [SMIC Tests China's First Domestic DUV Lithography Machine](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Moonshot AI Open-Sources Kimi K3, a 2.8T-Parameter Model](https://t.me/zaihuapd/42793) ⭐️ 9.0/10

Moonshot AI has released Kimi K3, the world's first open-source 2.8 trillion parameter model, featuring a novel Kimi Delta Attention and Attention Residuals architecture. It achieved the top score of 1679 in the Frontend Code Arena, surpassing Claude Fable 5 and jumping from 18th place with its predecessor Kimi k2.6. Kimi K3 is the largest open-weight model ever released, democratizing access to frontier-scale AI for customization and research. Its top benchmark performance demonstrates that open-source models can compete with and even surpass proprietary leaders in specialized domains like frontend coding. The model uses native MXFP4 quantization, requiring approximately 1.5 TB of VRAM to host, and supports a 1 million token context window with native vision capabilities. It ranks first in 6 out of 7 Frontend Code Arena domains, only trailing in gaming.

telegram · zaihuapd · Jul 27, 06:27

**Background**: Large language models (LLMs) are typically measured by parameter count; 2.8 trillion parameters is an order of magnitude larger than most open models (e.g., Llama 3.1 405B). The Frontend Code Arena evaluates AI models on real-world frontend development tasks like building responsive web apps. Kimi Delta Attention and Attention Residuals are novel architectural innovations that improve efficiency and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://x.com/arena/status/2077824029126504525">Arena.ai on X: "Big news: Kimi-K3 by @Kimi_Moonshot is now #1 in the Frontend Code Arena with 1679 pts, surpassing Claude Fable 5. This is a 17-place jump from Kimi-k2.6 (#18 -> #1). In Frontend, Kimi-K3 ranked #1 in 6 of 7 domains: Brand & Marketing, Reference-Based Design, Data & Analytics, Consumer Product, Simulations, and Content Creation Tools, landing #2 only in Gaming behind Fable 5. The full model weights will be released by July 27. Congrats to the @Kimi_Moonshot team on this major milestone!" / X</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3">China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China works around U.S. compute limits | Tom's Hardware</a></li>
<li><a href="https://www.developersdigest.tech/blog/web-dev-arena">Web Dev Arena: How to Test AI Coding Models on Real Frontend Work - Developers Digest</a></li>

</ul>
</details>

**Discussion**: Community members are excited about the customization potential and IP sovereignty offered by open weights, though some note the high hardware requirements (1.5 TB VRAM) make hosting expensive. One user reported that the model self-identified as 'Claude' when asked, raising concerns about training data contamination.

**Tags**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#benchmark`

---

<a id="item-2"></a>
## [Critical Fastjson 1.x RCE Without Gadgets or AutoType](https://t.me/zaihuapd/42797) ⭐️ 9.0/10

A critical remote code execution vulnerability (CVE-2026-16723, CVSS 9.0) has been disclosed in Fastjson 1.x versions 1.2.68 to 1.2.83, exploitable without autoType or classpath gadgets on JDK 8/17/21. This vulnerability affects a widely-used Java JSON library with no official patch expected, as Fastjson 1.x reached end-of-life in October 2024, leaving many applications exposed to remote attacks. Exploitation requires a Spring Boot executable fat-JAR with SafeMode disabled and the attacker being able to send malicious JSON to the parser. The vulnerability works even with autoType disabled and no classpath gadgets.

telegram · zaihuapd · Jul 27, 10:31

**Background**: Fastjson is a high-performance JSON library for Java developed by Alibaba. Its autoType feature allows deserialization of JSON with type information, which has historically been a source of vulnerabilities. Fastjson 1.x has been succeeded by Fastjson2, a complete rewrite with improved security and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://lilting.ch/en/articles/fastjson-1x-rce-spring-boot-fat-jar">Fastjson CVE-2026-16723: no AutoType, no gadgets ... | lilting channel</a></li>
<li><a href="https://thehackernews.com/2026/07/fastjson-1x-rce-vulnerability-targeted.html">Fastjson 1 . x RCE Vulnerability Targeted in Attacks With No Patched...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#Fastjson`, `#RCE`, `#Java`

---

<a id="item-3"></a>
## [vLLM v0.26.0: Inkling Support, DeepSeek-V4 Optimizations, Flexible Attention](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 introduces full support for the Inkling model family (975B parameters, 1M context), performance optimizations for DeepSeek-V4 (e.g., 2.94% E2E TPOT improvement), fp32 lm_head via head_dtype, and flexible attention backends selectable per KV-cache group. This release significantly expands vLLM's model support and inference efficiency, enabling deployment of cutting-edge models like Inkling and DeepSeek-V4 with state-of-the-art performance. The flexible attention backend and KV offloading enhancements improve scalability for large-scale AI serving. The release includes 411 commits from 212 contributors, with new features such as piecewise CUDA graph support for Inkling, a specialized routing kernel for DeepSeek-V4, and fp32 lm_head for improved generation accuracy. KV offloading now includes tier-owned event handling and object-store secondary tier with workload identity.

github · khluu · Jul 27, 01:06

**Background**: vLLM is an open-source high-throughput LLM inference engine that optimizes memory and computation for serving large language models. The Inkling model is a 975B-parameter Mixture-of-Experts multimodal model from Thinking Machines Lab, supporting text, image, and audio inputs with up to 1M context length. FlashAttention-4 (FA4) is the latest attention algorithm optimized for Hopper GPUs, offering improved performance over FA3.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Anthropic Clarifies Stance on Open-Weights Models](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic published a blog post stating it has never advocated for a ban on open-weights models, but supports mandatory safety testing for all sufficiently capable AI models, both open and closed. This clarifies a major AI lab's position on a contentious regulatory issue, potentially influencing policy debates on how to balance innovation and safety in AI development. Anthropic supports three measures: banning chip sales to China, cracking down on industrial-scale distillation, and mandatory safety testing for capable models. Critics argue that mandatory testing could effectively ban open-weights models if criteria are too costly or restrictive.

hackernews · surprisetalk · Jul 27, 22:03 · [Discussion](https://news.ycombinator.com/item?id=49076057)

**Background**: Open-weights models are AI models whose trained parameters (weights) are publicly released, allowing anyone to download and use them. Unlike open-source, open-weights do not necessarily include training code or data. Mandatory safety testing would require models to pass government-defined tests before release, a concept debated in AI safety circles.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism, arguing that mandatory safety testing could function as a de facto ban on open-weights models if testing is costly or administered restrictively. Some pointed out contradictions in Anthropic's stance, such as supporting chip bans while claiming not to advocate bans.

**Tags**: `#AI safety`, `#open-weights models`, `#regulation`, `#Anthropic`, `#policy`

---

<a id="item-5"></a>
## [Judge Rejects Google's DMCA Defense in Web Scraping Case](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

A U.S. judge ruled that Google cannot use the Digital Millennium Copyright Act (DMCA) to block the scraping of its search results, rejecting Google's attempt to claim copyright protection over search engine result pages (SERPs). This ruling sets a significant legal precedent for web scraping legality, potentially limiting how large tech companies can use copyright law to restrict data access and competition. It could affect the availability of third-party search APIs and tools that rely on scraping. The case involved SerpAPI, a company that scrapes Google search results, and Google's claim that scraping violated the DMCA's anti-circumvention provisions. The judge found that Google's search results are not sufficiently creative to qualify for copyright protection, and that scraping does not involve circumventing a technological measure that effectively controls access to a copyrighted work.

hackernews · cdrnsf · Jul 27, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49073513)

**Background**: The DMCA is a U.S. copyright law that includes provisions against circumventing technological protection measures (TPMs) used to control access to copyrighted works. Web scraping is the automated extraction of data from websites, and its legality often depends on whether the data is publicly accessible and whether the scraping method bypasses access controls. Google had argued that its search results are protected by copyright and that scraping them required circumventing its technical measures.

<details><summary>References</summary>
<ul>
<li><a href="https://datacelix.com/legal-considerations-for-web-scraping/">Legal Considerations For Web Scraping : A Practitioner's Guide To...</a></li>
<li><a href="https://www.promptcloud.com/blog/is-web-scraping-legal-in-us-a-complete-guide/">Is Web Scraping Legal in US | Ethical Scraping Practices</a></li>
<li><a href="https://thunderbit.com/blog/is-web-scraping-legal-us">Is Web Scraping Legal in the US? What the Law Actually Says</a></li>

</ul>
</details>

**Discussion**: Commenters largely supported the ruling, with many criticizing Google's attempt to use copyright to stifle competition. Some noted that Google's deprecation of its search API leaves no legitimate alternative, forcing reliance on scrapers. Others pointed out the irony of a company built on scraping others' data now trying to prevent scraping of its own.

**Tags**: `#DMCA`, `#web scraping`, `#Google`, `#legal`, `#search engines`

---

<a id="item-6"></a>
## [Bun's Rust Rewrite Progress: Shipped in Claude Code, 1.4 Delayed](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun's Rust rewrite has shipped in Claude Code over a month ago, but the Bun v1.4 release is delayed until a promised number of newly passing Node.js tests is achieved. The creator Jarred confirmed the rewrite is going well overall, with PRs for the test improvements pending merge. This rewrite is a major technical shift for Bun, a popular JavaScript runtime, and its success could significantly improve performance and compatibility. The delay highlights the team's commitment to Node.js compatibility, which is critical for adoption. The Rust rewrite was largely assisted by LLMs, translating the original Zig codebase. The 1.4 release is expected most likely next Tuesday once the Node.js test count target is met.

hackernews · tomlockwood · Jul 27, 11:12 · [Discussion](https://news.ycombinator.com/item?id=49067854)

**Background**: Bun is a fast JavaScript runtime originally written in Zig. The decision to rewrite it in Rust was driven by performance and ecosystem considerations. Claude Code is an AI-powered coding tool by Anthropic that assists developers with code understanding and editing.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/goldbergyoni/javascript-testing-best-practices">GitHub - goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript & Node.js testing best practices (August 2025)</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some question the insight from commit counts post-rewrite, while others debate the use of LLMs for translation. A comparison point (Buz) claims sub-second build times by fixing the original Zig codebase, suggesting the rewrite issues were self-inflicted.

**Tags**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#LLM`

---

<a id="item-7"></a>
## [CXMT surges 471.59% on STAR Market debut, record IPO](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10

Changxin Technology (CXMT) opened at 49.5 yuan per share on its first trading day on the STAR Market, a 471.59% surge from its IPO price of 8.66 yuan. The company raised approximately 57.9 billion yuan, with the potential to reach 66.6 billion yuan if the over-allotment option is fully exercised, surpassing SMIC's 2020 record to become the largest IPO on the STAR Market. This record-breaking IPO signals strong market confidence in China's domestic memory chip industry and underscores the strategic importance of semiconductor self-sufficiency. The massive capital injection will accelerate CXMT's DRAM production expansion and technology development, potentially reshaping the global memory chip landscape. CXMT is China's only large-scale integrated DRAM designer and manufacturer. The company expects a net profit attributable to parent of 50-57 billion yuan in the first half of 2026, a significant turnaround from losses. The IPO price was set at 8.66 yuan per share, and the stock code is 688825.SH.

telegram · zaihuapd · Jul 27, 01:29

**Background**: The STAR Market, officially the Shanghai Stock Exchange Science and Technology Innovation Board, was launched in July 2019 to provide Chinese tech companies with greater access to capital markets, similar to Nasdaq. DRAM (Dynamic Random-Access Memory) is a critical component in computers, servers, and consumer electronics, and its production is dominated by a few global players. CXMT's successful listing reflects China's push to build a self-sufficient semiconductor supply chain amid geopolitical tensions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Star_Market_Stock_Market">Star Market Stock Market</a></li>
<li><a href="https://www.mexc.com/crypto-pulse/article/changxin-memory-technologies-cxmt-129628">ChangXin Memory Technologies ($ CXMT )... | MEXC Crypto Pulse</a></li>

</ul>
</details>

**Tags**: `#IPO`, `#semiconductor`, `#memory chips`, `#Chinese tech`, `#stock market`

---

<a id="item-8"></a>
## [Google Teases Gemini 4 as Most Ambitious Pretraining Yet](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

Google CEO Sundar Pichai announced during Alphabet's Q2 2026 earnings call that Gemini 4 pretraining is underway, describing it as the company's most ambitious pretraining project to date, with a target release by the end of 2026. This signals Google's continued commitment to frontier AI development and AGI, potentially setting new benchmarks for large language models. The release could intensify competition among major AI labs and accelerate capabilities in coding, reasoning, and multi-step tasks. Pichai emphasized that Google will prioritize compute allocation for frontier AGI R&D to ensure Gemini 4 remains state-of-the-art upon release. Additionally, the Gemini 3.x Flash series will maintain near-monthly iteration cycles, focusing on intelligent coding improvements.

telegram · zaihuapd · Jul 27, 04:06

**Background**: Gemini is Google's family of large language models developed by DeepMind, with versions like Gemini 1.5, 2.0, and 3.x Flash. Pretraining is the initial phase where a model learns from vast datasets before fine-tuning. Google's previous models have competed with OpenAI's GPT series and Anthropic's Claude.

<details><summary>References</summary>
<ul>
<li><a href="https://andrew.ooo/answers/gemini-4-pretraining-tease-what-we-know-july-2026/">Gemini 4 Pretraining Tease: What We Know So Far (July 2026)</a></li>
<li><a href="https://felloai.com/all-we-know-about-google-gemini-4/">Gemini 4 : Release Date, Pre-Training News & Rumors</a></li>
<li><a href="https://coursiv.io/blog/gemini-4-pretraining">Gemini 4 Training Has Begun: Release Date & What We Know ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Gemini`, `#Large Language Models`, `#AGI`

---

<a id="item-9"></a>
## [China Refutes US Sanctions Threat Over AI Model Distillation](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

On July 27, China's Ministry of Commerce officially refuted US allegations that Chinese AI companies stole intellectual property through model distillation, arguing that US companies also distill Chinese models and that the practice is standard in the industry. This marks a significant escalation in US-China AI tensions, with the US threatening sanctions over a widely used technique. The response highlights the interdependence of the global AI ecosystem and could influence future regulation of open-source models. The Ministry stated that model distillation is a common industry technique and that nearly 200 US startups have urged the US government not to restrict access to Chinese open-source models. China warned it would take necessary measures to protect its enterprises' legitimate rights if US actions cause substantial harm.

telegram · zaihuapd · Jul 27, 11:01

**Background**: Model distillation is a technique where a smaller, more efficient model is trained to mimic the behavior of a larger, more powerful model. It is widely used in the AI industry to reduce computational costs and enable deployment on edge devices. The US has recently investigated Chinese AI companies for allegedly using distillation to copy US models without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://juejin.cn/post/7665780788496007222">今天我们讲讲大 模 型 的“核心” 技 术 ： 蒸 馏 （Model Distillation...</a></li>
<li><a href="https://www.tmtpost.com/7892989.html">Anthropic装糊涂，全球 AI 圈看笑了-钛媒体官方网站</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that nearly 200 US startups oppose restrictions on Chinese open-source models, indicating industry support for open access. Some commenters note the irony of US companies also using distillation, while others debate the ethical boundaries of the technique.

**Tags**: `#AI`, `#geopolitics`, `#model distillation`, `#US-China trade`, `#regulation`

---

<a id="item-10"></a>
## [SMIC Tests China's First Domestic DUV Lithography Machine](https://t.me/zaihuapd/42800) ⭐️ 8.0/10

SMIC is trialing China's first domestically developed deep ultraviolet (DUV) lithography machine, built by Shanghai startup Yuliangsheng, to produce 28nm chips and explore 7nm via multi-patterning. This marks a significant step in China's efforts to reduce reliance on foreign chipmaking equipment, potentially reshaping global semiconductor supply chains and geopolitical dynamics. The machine is mostly domestically sourced but still relies on some imported components. Mass production with stable yields is expected by 2027, and SMIC aims to expand production capacity significantly by 2026.

telegram · zaihuapd · Jul 27, 14:10

**Background**: DUV lithography uses deep ultraviolet light to pattern circuits on chips, and is essential for manufacturing nodes down to 7nm when combined with multi-patterning. Currently, China's most advanced chips rely on ASML's DUV tools, while EUV lithography—needed for sub-7nm nodes—is banned for sale to China due to US export controls.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/china-begins-making-homegrown-duv-chipmaking-tools-information-reports-2026-07-27/">China begins making homegrown DUV chipmaking tools, The...</a></li>
<li><a href="https://waferscope.com/duv-vs-euv-whats-the-real-difference-in-chipmaking/">DUV vs EUV: What’s the Real Difference in Chipmaking?</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#lithography`, `#China`, `#chip manufacturing`, `#export controls`

---