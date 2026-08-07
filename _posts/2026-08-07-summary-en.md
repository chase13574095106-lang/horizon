---
layout: default
title: "Horizon Summary: 2026-08-07 (EN)"
date: 2026-08-07
lang: en
---

> From 26 items, 12 important content pieces were selected

---

1. [pgrust: Rewriting Postgres in Rust for 300x Faster Analytics](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731: Faster, Cheaper, and Praised by Users](#item-2) ⭐️ 8.0/10
3. [Tech Worker Disillusionment: A Crisis of Faith](#item-3) ⭐️ 8.0/10
4. [Oracle Bans AI-Generated Code in OpenJDK](#item-4) ⭐️ 8.0/10
5. [2027 Memory Capacity Reportedly Sold Out Amid AI Demand](#item-5) ⭐️ 8.0/10
6. [A Year of Fighting Scrapers on a 1.5 Million-Page Website](#item-6) ⭐️ 8.0/10
7. [New Mexico Court Orders Meta to Pay $567M for Child Mental Health Harms](#item-7) ⭐️ 8.0/10
8. [Wyzer: A New Language Targeting Distributed Deadlocks](#item-8) ⭐️ 8.0/10
9. [US Probes Chinese AI Firms' Offshore Access to Nvidia Chips](#item-9) ⭐️ 8.0/10
10. [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding](#item-10) ⭐️ 8.0/10
11. [Critical OAuth Flaw in sub2api Allows Account Takeover via Email](#item-11) ⭐️ 8.0/10
12. [OpenAI Reportedly to Release New Model Astra Next Week](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [pgrust: Rewriting Postgres in Rust for 300x Faster Analytics](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 9.0/10

The article describes pgrust, a Rust-based reimplementation of Postgres's query execution and storage layers, achieving a 300x speedup over Postgres on Clickbench, an analytical benchmark, through batching, operator fusion, and SIMD. On OLTP benchmarks, pgrust is 30% faster than Postgres. This demonstrates a significant performance leap for Postgres in analytics workloads, potentially influencing future database design and offering a viable alternative for high-performance analytics. It also sparks discussion about trust and adoption of community-driven rewrites of critical infrastructure. The optimizations focus on reducing CPU and memory bandwidth usage in the query engine. The project prioritizes correctness through formal verification and differential fuzz testing, having proven over 1000 user-facing functions match Postgres logic.

hackernews · poly2it · Aug 7, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49208535)

**Background**: Postgres is a popular open-source relational database, but its query engine is not optimized for analytical workloads compared to specialized systems like Clickhouse. pgrust is a complete rewrite of Postgres's core in Rust, aiming to improve performance while maintaining compatibility. Techniques like batching, operator fusion, and SIMD are common in modern analytical databases to speed up query processing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now faster than Postgres and Clickhouse · GitHub</a></li>
<li><a href="https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/">Rebuilding Postgres for 300x faster analytics: batching, operator ...</a></li>
<li><a href="https://dev.to/terminalchai/pgrust-the-open-source-project-rewriting-postgresql-in-rust-4860">pgrust: The Open-Source Project Rewriting PostgreSQL in Rust - DEV Community</a></li>

</ul>
</details>

**Discussion**: The author engaged in the discussion, addressing trust concerns by highlighting formal verification and fuzz testing. Some commenters expressed skepticism about adoption due to trust in the Postgres team, while others praised the adaptive planning and potential for embedding pgrust as an alternative to SQLite.

**Tags**: `#database`, `#postgres`, `#query-engine`, `#performance`, `#rust`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731: Faster, Cheaper, and Praised by Users](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek released V4 Flash 0731, an updated version of its efficiency-optimized Mixture-of-Experts model, featuring a 1M-token context window and adjustable reasoning effort. Users report significant performance improvements over the previous preview, with high speed and low cost. This release offers a compelling balance of performance and cost, potentially disrupting the AI model market by providing a cheaper alternative to proprietary models like Claude and GPT-4. It could accelerate adoption of open-weight models for coding and agentic tasks. The model has 284B total parameters with 13B activated, and supports a 1M-token context. It outperforms DeepSeek V4 Pro (Preview) on benchmarks despite its smaller activated size, and is broadly competitive with leading proprietary models. Pricing is dynamic, with peak-time rates defined by China time, which may affect users outside Asia.

hackernews · tosh · Aug 7, 17:56 · [Discussion](https://news.ycombinator.com/item?id=49214008)

**Background**: DeepSeek is a Chinese AI research company known for releasing open-weight models that rival proprietary systems. V4 Flash is an efficiency-focused variant of the V4 series, designed for fast inference and high-throughput workloads, making it suitable for agentic coding and data analysis. The ARC-AGI-2 benchmark tests abstract reasoning, and the model's performance on it is notable given its text-only nature.

<details><summary>References</summary>
<ul>
<li><a href="https://www.together.ai/models/deepseek-v4-flash-0731">DeepSeek V 4 Flash 0731 API | Together AI</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash/benchmarks">DeepSeek V4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Users are enthusiastic about the model's speed and cost-effectiveness, with one user noting it's 'good enough for almost everything' and cheap enough that costs are irrelevant. Another user highlighted the speed on high-end hardware, achieving ~8k tok/s prefill and ~250 tok/s on a single stream. However, there is a concern about account bans, as one user reported their Claude account was banned after attempting to authenticate from a JetBrains IDE, and another noted peak-time pricing is based on China time, which could affect non-Asian users.

**Tags**: `#AI`, `#LLM`, `#DeepSeek`, `#model release`, `#performance`

---

<a id="item-3"></a>
## [Tech Worker Disillusionment: A Crisis of Faith](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

An article in Noema Magazine explores the widespread sadness and loss of faith among tech workers, questioning the future of the industry and its workforce. The piece has sparked significant discussion, with 275 points and 411 comments on Hacker News. This article highlights a growing crisis in the tech industry, where workers are increasingly disillusioned with their careers. The high engagement suggests it resonates deeply with many, potentially impacting talent retention and industry culture. The article references historical parallels, such as the decline of the printing trade, and discusses the toxicity of the online world. Commenters share personal experiences of burnout and a desire for more grounded occupations, though some note the financial impracticality of leaving tech.

hackernews · RickJWagner · Aug 7, 12:42 · [Discussion](https://news.ycombinator.com/item?id=49209539)

**Background**: The tech industry has long been seen as a path to success, but recent years have seen rising concerns about burnout, mental health, and the ethical implications of technology. This article taps into a broader conversation about the sustainability of tech careers and the well-being of those who build our digital world.

**Discussion**: Commenters express a range of views, from comparing tech's decline to the printing trade's demise to noting the toxicity of the web. Some share personal stories of reduced passion and daydreams of escaping, while others point out the financial barriers to leaving the industry.

**Tags**: `#tech culture`, `#mental health`, `#career`, `#industry trends`, `#workforce`

---

<a id="item-4"></a>
## [Oracle Bans AI-Generated Code in OpenJDK](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) ⭐️ 8.0/10

Oracle has implemented an interim policy banning AI-generated code contributions to OpenJDK, effective April 9, 2026. The policy prohibits content generated by large language models, diffusion models, or similar deep-learning systems in OpenJDK contributions. This policy affects the widely-used OpenJDK project, which underpins many business-critical systems. It highlights the tension between AI adoption and legal/review concerns in open-source communities, potentially setting a precedent for other projects. The interim policy applies to community contributions but may not affect core developers. Oracle cites reviewer burden and legal uncertainty around copyright as reasons, despite its own enthusiasm for AI-generated code in other products like GraalVM.

hackernews · delduca · Aug 7, 17:36 · [Discussion](https://news.ycombinator.com/item?id=49213754)

**Background**: OpenJDK is the open-source implementation of the Java Platform, Standard Edition, and is maintained by a community under Oracle's stewardship. The project has a history of legal scrutiny, including past copyright disputes, which may explain Oracle's cautious approach. The interim policy is a stopgap measure while Oracle's lawyers draft a final policy.

<details><summary>References</summary>
<ul>
<li><a href="https://openjdk.org/legal/ai">OpenJDK Interim Policy on Generative AI</a></li>
<li><a href="https://www.techzine.eu/news/devops/143395/oracle-bans-ai-generated-contributions-to-openjdk/">Oracle bans AI-generated contributions to OpenJDK - Techzine Global</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed reactions: some see the ban as sensible given legal risks and reviewer burden, while others note the irony of Oracle's AI investments. Some commenters point out that the policy may primarily target community submissions, not core developers, and question the feasibility of enforcing such a ban.

**Tags**: `#OpenJDK`, `#AI policy`, `#open source`, `#legal`, `#Oracle`

---

<a id="item-5"></a>
## [2027 Memory Capacity Reportedly Sold Out Amid AI Demand](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 8.0/10

Reports indicate that memory capacity for 2027 is already sold out, with memory makers locking customers into long-term agreements. This highlights severe supply constraints driven by AI demand and HBM production trade-offs. This development signals a prolonged memory shortage that could impact consumer electronics prices and availability. It underscores the strategic importance of memory in the AI era, affecting manufacturers, cloud providers, and end users. HBM production consumes roughly three times the wafer capacity of DDR5 for the same bit count, constraining non-HBM supply. Memory makers are using advance payment deposit models with contracts spanning three to five years, leaving no room for new buyers.

hackernews · inigyou · Aug 7, 07:58 · [Discussion](https://news.ycombinator.com/item?id=49207236)

**Background**: Memory capacity refers to the production output of DRAM chips used in computers, servers, and other devices. High Bandwidth Memory (HBM) is a specialized type of DRAM stacked vertically to provide high speed for AI accelerators, but its production is less efficient in terms of wafer usage, leading to trade-offs with conventional memory like DDR5.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/351344/memory-makers-seal-2027-deals-no-room-for-new-buyers">Memory Makers Seal 2027 Deals: No Room for New... | TechPowerUp</a></li>
<li><a href="https://www.intelligentliving.co/hbm-ram-ai-datacenter-ddr5-supply-chain/">HBM is Coming for Your PC's RAM: AI Datacenter High-Bandwidth Memory Squeezes Global DDR5 RAM Supply Chain</a></li>
<li><a href="https://wccftech.com/aletheia-warns-hbm-prices-will-double-in-2027-as-memory-becomes-ais-most-critical-component/">Aletheia Warns HBM Prices Will Double in 2027 as Memory Becomes...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about the impact on consumer prices and availability, with some noting inflationary effects. Others highlighted the technical trade-offs of HBM production and shared personal strategies like stockpiling older RAM or avoiding AI to reduce memory pressure.

**Tags**: `#memory`, `#HBM`, `#supply chain`, `#AI hardware`, `#semiconductors`

---

<a id="item-6"></a>
## [A Year of Fighting Scrapers on a 1.5 Million-Page Website](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) ⭐️ 8.0/10

A website owner detailed a year-long battle against scrapers, reporting that bots accounted for 99% of traffic and caused a 500% cost spike in one month. The post highlights the trade-offs of using Cloudflare's anti-bot services and the financial burden on small site owners. This story underscores the growing challenge of bot traffic for independent web publishers, who face rising costs and must decide between openness and protection. It also sparks debate about the centralization of web control in companies like Cloudflare and the need for alternative solutions. The site's normal monthly cost is around $90, but a bad spike month saw a 500% increase, partly due to Cloudflare's D1 database costs. The author acknowledges being a scraper themselves, scraping public documents, which adds nuance to the anti-scraping stance.

hackernews · petercooper · Aug 7, 14:51 · [Discussion](https://news.ycombinator.com/item?id=49211386)

**Background**: Web scraping is the automated extraction of data from websites, often used for price monitoring, content aggregation, or AI training. Anti-bot services like Cloudflare Bot Management use machine learning and behavioral analysis to detect and block malicious bots, but they can also block legitimate users and raise costs for site owners.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/bot-mitigation/">Cloudflare Bot Management - Stop Bad Bots</a></li>
<li><a href="https://finedata.ai/blog/anti-bot-detection-2026/">Anti - Bot Detection: How Cloudflare , DataDome, and PerimeterX Work</a></li>
<li><a href="https://medium.com/@mayankchandel2567/how-does-cloudflare-bot-detection-work-d77179756cdc">How does Cloudflare bot detection works | by Mayank... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about outsourcing web access decisions to large companies like Cloudflare, noting it undermines the open web. Some suggested alternative solutions like Anubis, a proof-of-work-based bot detection tool, while others recommended moving to static sites to reduce costs. A commenter shared that Claude's search bot fetched 205,000 pages from their site with only one referral, highlighting the lack of compensation for scraped content.

**Tags**: `#web scraping`, `#bots`, `#Cloudflare`, `#website costs`, `#anti-bot`

---

<a id="item-7"></a>
## [New Mexico Court Orders Meta to Pay $567M for Child Mental Health Harms](https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta) ⭐️ 8.0/10

On August 6, 2026, a New Mexico court ordered Meta to pay $567 million for harms to children's mental health, with reports also citing a $942 million figure. The ruling requires Meta to make changes for underage users. This landmark ruling sets a significant legal precedent for holding social media platforms accountable for child safety and mental health impacts. It could influence other jurisdictions and pressure Meta to revise its algorithms and policies for younger users. The court found Meta violated New Mexico's public-nuisance law (NMSA 1978 § 30-8-1). The $567 million figure is notable given New Mexico's small population (~2 million), making the per-capita impact substantial relative to Meta's revenue.

hackernews · boplicity · Aug 7, 00:06 · [Discussion](https://news.ycombinator.com/item?id=49204352)

**Background**: Social media platforms like Instagram and TikTok have faced growing scrutiny over their impact on young users' mental health, including addictive design and harmful content. This case is part of broader efforts by states and countries to regulate social media for minors, with some jurisdictions already implementing bans or restrictions.

**Discussion**: Commenters noted that while the fine may seem small relative to Meta's global revenue, it is significant for a small jurisdiction like New Mexico. Some expressed concerns about the addictive nature of short-form video platforms and the need for algorithm changes, while others debated the legal basis and proportionality of the ruling.

**Tags**: `#Meta`, `#legal`, `#child safety`, `#social media`, `#mental health`

---

<a id="item-8"></a>
## [Wyzer: A New Language Targeting Distributed Deadlocks](https://github.com/Wyzer-Lang/wyzer) ⭐️ 8.0/10

Wyzer is a new statically typed, compiled, resource-oriented programming language that integrates choreographic programming and Perceus memory management to prevent distributed deadlocks. The project is nearing its 0.1.0 release after five months of research and a few weeks of development. Wyzer addresses a critical gap in distributed systems safety that mainstream languages like Rust do not cover, potentially offering a new way to write deadlock-free distributed applications. If successful, it could influence future language design and provide a practical alternative for developers building reliable distributed systems. Wyzer uses linear/affine types and Perceus reference counting instead of borrow checkers and lifetimes, which the author claims is computationally simpler for LSPs to understand. The language generalizes choreographic programming, a paradigm where a single program describes interactions among multiple participants, which is compiled to executable code for each participant.

hackernews · v0id_isgood · Aug 7, 12:28 · [Discussion](https://news.ycombinator.com/item?id=49209385)

**Background**: Choreographic programming is a programming paradigm for distributed systems where programs are written as compositions of interactions among multiple concurrent participants, ensuring deadlock-freedom by construction. Perceus is a garbage-free reference counting memory management technique, originally implemented in the Koka language, that offers competitive performance with low memory overhead. Wyzer aims to combine these concepts in a high-level language to address distributed deadlocks and protocol mismatches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Choreographic_programming">Choreographic programming</a></li>
<li><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2020/11/perceus-tr-v1.pdf">Perceus: Garbage Free Reference Counting with Reuse</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3453483.3454032">Perceus: garbage free reference counting with reuse | Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation</a></li>

</ul>
</details>

**Discussion**: The community is generally positive about the project's ambition and novelty, with comments praising the clear documentation and the attempt to bring academic concepts into practice. However, some commenters question how the language guarantees deadlock-freedom and request more examples and clarification on the underlying mechanisms.

**Tags**: `#programming language`, `#distributed systems`, `#choreographic programming`, `#memory management`, `#Rust alternative`

---

<a id="item-9"></a>
## [US Probes Chinese AI Firms' Offshore Access to Nvidia Chips](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10

The US Commerce Department's Bureau of Industry and Security (BIS) has launched a systematic review of how Chinese AI companies access Nvidia chips overseas, including via remote cloud computing. This follows allegations that Moonshot AI's Kimi K3 model used illegally obtained Nvidia chips accessed remotely through Thailand. This review could lead to new regulations restricting Chinese firms' access to advanced AI chips via cloud services, potentially reshaping the global AI supply chain. It also escalates US-China tech tensions, affecting major players like Nvidia, Alibaba, and Moonshot AI. BIS is compiling two lists: countries suspected of harboring black markets for smuggled restricted chips, and countries where Chinese firms remotely rent chips. The legality of restricting remote access is questionable, but the US House has passed a bipartisan bill to grant such authority, likely facing opposition from Nvidia and others. Alibaba is reportedly linked to a Singapore shell company using Nvidia chips in Malaysia via Megaspeed.

telegram · zaihuapd · Aug 7, 11:18

**Background**: The US has imposed export controls on advanced AI chips to China to slow its technological progress. However, Chinese firms have sought alternative access, including through cloud computing and third-country intermediaries. The Remote Access Security Act (H.R. 2683), passed by the House in January 2026, aims to close this loophole by regulating cloud-based access to advanced chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://channel.cx.ms/posts/6066">#article #read...</a></li>
<li><a href="https://info.51.ca/articles/1481007">黄仁勋身边神秘样女子 是 芯 片 偷卖中国的要角？_ 无忧资讯</a></li>

</ul>
</details>

**Tags**: `#US-China tech war`, `#AI chips`, `#export controls`, `#NVIDIA`, `#cloud computing`

---

<a id="item-10"></a>
## [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding](https://www.gelonghui.com/live/2599953) ⭐️ 8.0/10

SK Hynix has confirmed that its next-generation V10 NAND flash will feature 375 layers, marking the company's first use of wafer bonding technology. The company claims a 2.5x improvement in performance per watt over the previous generation, optimized for AI infrastructure. This milestone is significant for the semiconductor industry as it pushes NAND stacking beyond 300 layers, addressing the growing demand for high-capacity, energy-efficient memory in AI workloads. It also signals a shift toward wafer bonding as a key enabler for future NAND scaling, potentially influencing competitors like Samsung and Kioxia. The V10 NAND is the successor to the 321-layer V9 '4D NAND' and is SK Hynix's first NAND product to employ wafer bonding. According to industry sources, SK Hynix has completed production verification and plans to mass-produce the 375-layer NAND by the end of 2026, without building a new fab.

telegram · zaihuapd · Aug 7, 12:19

**Background**: NAND flash memory is a non-volatile storage technology used in SSDs and mobile devices. Increasing the number of stacked layers boosts storage density, but traditional stacking faces challenges in performance and power efficiency. Wafer bonding, also known as hybrid bonding, involves manufacturing memory cells and peripheral logic separately and then bonding them together, improving performance and enabling higher layer counts. This technique is being adopted by major memory makers like Samsung and SK Hynix to meet the demands of AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendforce.com/news/2025/12/08/news-sk-hynix-reportedly-accelerates-hybrid-bonding-for-300-layer-v10-nand-eying-2027-mass-production/">[News] SK hynix Reportedly Accelerates Hybrid Bonding for 300-Layer V10 NAND, Eying 2027 Mass Production</a></li>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=11210">SK hynix to Mass Produce 375-Layer NAND by Year-End, Introduce Molybdenum < Semiconductor < 기사본문 - The Elec Inc.</a></li>
<li><a href="https://www.trendforce.com/news/2026/06/12/news-the-race-to-400-layer-nand-roadmaps-and-key-technologies-driving-samsung-sk-hynix-and-kioxia/">[News] The Race to 400-Layer NAND: Roadmaps and Key Technologies Driving Samsung, SK hynix, and Kioxia</a></li>

</ul>
</details>

**Tags**: `#NAND`, `#SK Hynix`, `#semiconductor`, `#AI infrastructure`, `#memory technology`

---

<a id="item-11"></a>
## [Critical OAuth Flaw in sub2api Allows Account Takeover via Email](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

A critical OAuth account takeover vulnerability (CVSS 8.8) has been disclosed in sub2api v0.1.171 and earlier versions. An attacker can bind their OAuth identity to a victim's account using only the victim's email, without needing a password, verification code, or user interaction. This vulnerability allows complete account takeover, giving attackers control over API keys, billing balances, and subscription quotas. It poses a severe risk to all sub2api users, especially those sharing subscriptions, and highlights the importance of proper OAuth implementation in open-source projects. The flaw lies in the pending session flow's existingUser branch, which fails to verify passwords or verification codes. By setting the target user ID to the victim's, the attacker completes OAuth binding, and subsequent OAuth logins resolve to the victim's account.

telegram · zaihuapd · Aug 7, 14:59

**Background**: OAuth 2.0 is a widely used authorization framework that allows users to log in via third-party providers. Account takeover vulnerabilities often arise when the OAuth flow improperly links identities to existing accounts, especially when user-controlled parameters like email or user ID are not validated. This issue is tracked as CVE-2026-27812.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-27812/">CVE-2026-27812: Sub2API Auth Bypass Vulnerability</a></li>
<li><a href="https://github.com/Wei-Shaw/sub2api">GitHub - Wei-Shaw/sub2api: Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。</a></li>
<li><a href="https://book.hacktricks.xyz/pentesting-web/oauth-to-account-takeover">OAuth to Account takeover - HackTricks</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights the severity of the vulnerability, with users expressing concern over the ease of exploitation and the potential impact on shared subscription services. Some are calling for immediate patching and thorough security audits of similar OAuth implementations.

**Tags**: `#security`, `#OAuth`, `#vulnerability`, `#account takeover`, `#sub2api`

---

<a id="item-12"></a>
## [OpenAI Reportedly to Release New Model Astra Next Week](https://t.me/zaihuapd/43046) ⭐️ 8.0/10

OpenAI is reportedly preparing to release a new large model named Astra as soon as next week. The model, which is said to be a fresh pretraining and the largest since GPT-4.5, has an internal test version codenamed 'mewfour' that has been designated as a release candidate. If confirmed, Astra would mark a major milestone in OpenAI's model development, potentially advancing capabilities in scientific reasoning and complex problem-solving. Its release could significantly impact the AI industry and competitive landscape, affecting developers, researchers, and businesses that rely on cutting-edge AI models. According to the leak, Astra is a completely new pretraining and the largest model OpenAI has trained since GPT-4.5. The latest internal test version, codenamed 'mewfour', has been set as the release candidate, suggesting the model is nearing finalization.

telegram · zaihuapd · Aug 7, 16:44

**Background**: OpenAI has been developing increasingly powerful large language models, with GPT-4.5 being a previous major release. Recently, OpenAI teased Astra as its next major model, noting that an internal version solved ten long-standing problems in mathematics and theoretical computer science, indicating a focus on scientific reasoning. The model is expected to be a significant step forward in AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/artificial-intelligence/openai-teases-astra-its-next-major-ai-model-after-it-solves-10-long-standing-math-problems/">OpenAI teases Astra, its next major AI model, after it solves 10 long-standing math problems</a></li>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer science | OpenAI</a></li>
<li><a href="https://garymarcus.substack.com/p/openais-amazing-but-vastly-oversold">OpenAI’s amazing — but vastly oversold — new model Astra</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI model`, `#rumor`, `#GPT-4.5`, `#large language model`

---