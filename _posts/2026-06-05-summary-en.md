---
layout: default
title: "Horizon Summary: 2026-06-05 (EN)"
date: 2026-06-05
lang: en
---

> From 34 items, 7 important content pieces were selected

---

1. [Microsoft Open Sources pg_durable for In-Database Durable Execution](#item-1) ⭐️ 8.0/10
2. [Google Releases Gemma 4 QAT Models for Efficient On-Device AI](#item-2) ⭐️ 8.0/10
3. [Russian Satellite Cosmos 2546 Linked to Europe GNSS Jamming](#item-3) ⭐️ 8.0/10
4. [Ladybird Browser Bans Public Pull Requests Over AI Code](#item-4) ⭐️ 8.0/10
5. [AI Enthusiasts vs. Skeptics: Race Against Time vs. Entropy](#item-5) ⭐️ 8.0/10
6. [Pentagon may end Anthropic partnership over AI military restrictions](#item-6) ⭐️ 8.0/10
7. [Anthropic Urges Global Slowdown in Frontier AI Development](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft Open Sources pg_durable for In-Database Durable Execution](https://github.com/microsoft/pg_durable) ⭐️ 8.0/10

Microsoft has open-sourced pg_durable, a PostgreSQL extension that enables in-database durable execution of workflows, allowing developers to define multi-step SQL workflows that automatically checkpoint and resume after failures. This brings durable execution capabilities directly into PostgreSQL, reducing the need for external workflow orchestrators like Temporal for certain use cases, and strengthens the Postgres ecosystem with a production-grade solution from Microsoft. pg_durable is built on two Rust libraries: duroxide for the orchestration runtime and another for checkpointing, and it exposes a SQL DSL for building function graphs. It is the durable execution engine inside Azure HorizonDB.

hackernews · coffeemug · Jun 5, 15:59 · [Discussion](https://news.ycombinator.com/item?id=48414367)

**Background**: Durable execution ensures that long-running workflows survive crashes by checkpointing state at each step. Traditionally, this requires external systems like Temporal or Azure Durable Functions. pg_durable embeds this capability directly in PostgreSQL, allowing workflows to be defined and executed within the database.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/pg_durable">GitHub - microsoft/pg_durable: PostgreSQL in-database durable execution</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/horizondb/development/durable-functions">Durable Functions in Azure HorizonDB - Azure HorizonDB | Microsoft Learn</a></li>
<li><a href="https://temporal.io/blog/what-is-durable-execution">The definitive guide to Durable Execution | Temporal</a></li>

</ul>
</details>

**Discussion**: The community is excited about the growing Postgres queue ecosystem, with comments noting alternatives like DBOS and pgQue. Some users question how pg_durable compares to Temporal, especially when workflows span heterogeneous systems. Others express frustration that Azure PostgreSQL lags behind in supporting such extensions.

**Tags**: `#PostgreSQL`, `#durable execution`, `#Microsoft`, `#open source`, `#workflow`

---

<a id="item-2"></a>
## [Google Releases Gemma 4 QAT Models for Efficient On-Device AI](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) ⭐️ 8.0/10

Google has released official quantization-aware training (QAT) models for the Gemma 4 family, enabling efficient compression for mobile and laptop deployment with minimal accuracy loss. This release makes powerful Gemma 4 models practical for on-device AI, allowing developers to run advanced reasoning and agentic workflows on resource-constrained hardware like phones and laptops. The QAT models include a 4-bit quantized version (Q4_0) of Gemma 4 12B, which requires only 6.7GB of VRAM and fits comfortably within 16GB memory. Community tests show the quantized models achieve near-100% accuracy compared to the unquantized BF16 version.

hackernews · theanonymousone · Jun 5, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48414653)

**Background**: Quantization-aware training (QAT) is a technique that integrates weight precision reduction into the model training process, minimizing accuracy loss during compression. Gemma 4 is Google's latest open model family designed for advanced reasoning and agentic tasks. On-device AI requires models to be small enough to run locally without cloud connectivity, making compression techniques like QAT essential.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>

</ul>
</details>

**Discussion**: Community members are impressed with the rapid advancement of the Gemma ecosystem, noting the release of multitoken prediction and official quants. Some users report successful local runs on Macs and phones, while others compare Google's QAT models favorably with third-party alternatives like Unsloth, which claim even better accuracy.

**Tags**: `#quantization`, `#Gemma 4`, `#on-device AI`, `#model compression`, `#efficiency`

---

<a id="item-3"></a>
## [Russian Satellite Cosmos 2546 Linked to Europe GNSS Jamming](https://arxiv.org/abs/2606.03673) ⭐️ 8.0/10

A research paper identifies Russian satellite Cosmos 2546 (NORAD ID 45608) as a source of GNSS interference across Europe since 2019, using a combination of techniques to pinpoint the satellite with high confidence. This finding has significant geopolitical and technical implications, as it attributes widespread GNSS degradation to a specific Russian early warning satellite, potentially escalating tensions and prompting countermeasures. The satellite belongs to the Russian Edinaya Kosmicheskaya Sistema (EKS) early warning constellation, and the paper suggests the entire constellation may be collectively responsible for the interference. The satellite orbits in a highly elliptical orbit (1380–38976 km) with 63.2° inclination.

hackernews · mimorigasaka · Jun 5, 08:32 · [Discussion](https://news.ycombinator.com/item?id=48409664)

**Background**: GNSS (Global Navigation Satellite System) signals, such as GPS, are extremely weak when reaching Earth's surface, making them vulnerable to interference. Jamming can be intentional or unintentional, and identifying the source requires sophisticated analysis of signal characteristics and satellite positions. The Cosmos 2546 satellite was launched in May 2020 and is operated by the Russian Ministry of Defense.

<details><summary>References</summary>
<ul>
<li><a href="https://orbitalradar.com/satellite/45608">COSMOS 2546 — Live Satellite Tracking | Orbital Radar</a></li>
<li><a href="https://www.n2yo.com/satellite/?s=45608">COSMOS 2546 Satellite details 2020-031A NORAD 45608 - N2YO.com</a></li>
<li><a href="https://www.satellitetrackerlive.com/satellites/45608">Cosmos 2546 — NORAD 45608 | Satellite Tracker</a></li>

</ul>
</details>

**Discussion**: Community comments include real-world accounts of daily jamming near Ukraine and Kaliningrad, and speculation about Russian electronic warfare affecting Ukrainian drones. One commenter questions the power required for wide-area jamming, while another links a related Veritasium video.

**Tags**: `#GNSS`, `#interference`, `#satellite`, `#geopolitics`, `#RF`

---

<a id="item-4"></a>
## [Ladybird Browser Bans Public Pull Requests Over AI Code](https://simonwillison.net/2026/Jun/5/andreas-kling/#atom-everything) ⭐️ 8.0/10

Ladybird browser announced it will no longer accept public pull requests, citing that AI-generated code undermines the assumption of good faith effort, and instead requires contributors to take direct responsibility for changes. This policy shift reflects a growing tension in open-source governance as AI-generated code becomes prevalent, potentially setting a precedent for how projects maintain trust and accountability. The change means all contributions must now be submitted through a more formal process where the contributor is clearly responsible. Andreas Kling emphasized that the issue is not whether code was typed by hand, but who takes responsibility for it.

rss · Simon Willison · Jun 5, 11:10

**Background**: Ladybird is an open-source web browser developed by the Ladybird Browser Initiative, a nonprofit organization. It originated as a component of SerenityOS, a hobbyist operating system created by Andreas Kling. The browser is privacy-focused and plans alpha, beta, and stable releases by 2028.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/Andreas_Kling">Andreas Kling</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#ai-ethics`, `#ladybird`, `#software-governance`

---

<a id="item-5"></a>
## [AI Enthusiasts vs. Skeptics: Race Against Time vs. Entropy](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything) ⭐️ 8.0/10

Charity Majors published an article framing the tension between AI enthusiasts racing to adopt AI for capabilities and AI skeptics preserving code quality and trust as a race against time versus a race against entropy. This analysis highlights a real, existential tension within software teams that could determine which companies thrive or fail in the current AI cycle, making it crucial for leaders to bridge the gap between these two groups. Majors notes that both sides are not wrong: enthusiasts see real discontinuous leaps in capabilities, while skeptics warn that shipping code faster than engineers can read it degrades reliability and institutional knowledge. She recommends designing feedback loops to mend the gap in shared reality.

rss · Simon Willison · Jun 4, 23:55

**Background**: The article addresses a common debate in software engineering: the trade-off between rapid AI adoption and maintaining code quality, reliability, and trust. Majors is a well-known engineer and writer who often discusses operational excellence and engineering culture.

**Discussion**: The article was shared on Lobste.rs, where commenters likely discussed the practical challenges of balancing AI adoption with code quality, though no specific comments are provided here.

**Tags**: `#AI`, `#software engineering`, `#technology debate`, `#code quality`

---

<a id="item-6"></a>
## [Pentagon may end Anthropic partnership over AI military restrictions](https://t.me/zaihuapd/41777) ⭐️ 8.0/10

The US Department of Defense is considering terminating its partnership with AI company Anthropic due to disagreements over usage restrictions on the Claude AI model for military applications. Anthropic prohibits using Claude for mass surveillance and fully autonomous weapons, while the DoD demands full access for all lawful purposes, including weapons development and battlefield operations. This dispute highlights a critical tension between AI safety commitments and national security demands, potentially setting a precedent for how AI companies engage with military customers. The outcome could influence industry norms on ethical restrictions and impact the Pentagon's ability to leverage advanced AI for defense. Anthropic has reportedly refused to remove two major safety restrictions from Claude for military use, despite competitors like OpenAI and Google relaxing similar limits. The Pentagon gave Anthropic an ultimatum to comply, but the company has not conceded.

telegram · zaihuapd · Jun 5, 01:27

**Background**: Anthropic is an AI safety-focused company that developed the Claude model, which has been used in military operations such as the capture of Venezuelan leader Nicolás Maduro. The company's usage policy explicitly bans applications that could cause harm, including autonomous weapons and mass surveillance. The DoD, under Secretary Pete Hegseth, seeks unrestricted access to AI for defense purposes, leading to the current standoff.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute - Wikipedia</a></li>
<li><a href="https://www.facebook.com/washingtonpost/posts/breaking-news-anthropic-said-that-it-will-not-concede-to-the-pentagons-terms-for/1289252683066604/">Breaking news: Anthropic said that it will not concede to the Pentagon's ...</a></li>
<li><a href="https://www.reddit.com/r/ClaudeAI/comments/1rem4td/anthropic_ditches_its_core_safety_promise_in_the/">Anthropic ditches its core safety promise in the middle of an AI red ...</a></li>

</ul>
</details>

**Discussion**: Community discussions on Reddit and other platforms show mixed reactions: some users support Anthropic's stance on ethical AI, while others criticize the company for potentially hindering national security. There is also debate about whether Anthropic's restrictions are consistent with its earlier safety promises.

**Tags**: `#AI ethics`, `#military AI`, `#Anthropic`, `#US Department of Defense`, `#AI policy`

---

<a id="item-7"></a>
## [Anthropic Urges Global Slowdown in Frontier AI Development](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 8.0/10

Anthropic has called on major AI labs worldwide to slow the pace of frontier model development, warning that rapid progress could soon lead to recursive self-improvement—where AI systems improve themselves without human intervention—posing significant societal risks. This proposal from a leading AI safety lab highlights growing concerns about uncontrolled AI advancement and the need for global coordination, but it has faced criticism in Washington and Silicon Valley for potentially exaggerating risks and ceding strategic advantage to China. Anthropic recently completed a near-trillion-dollar valuation funding round and has filed a confidential IPO document, adding context to its call for a slowdown. The company warns that without global coordination, a unilateral pause would allow competitors to race ahead.

telegram · zaihuapd · Jun 5, 03:00

**Background**: Recursive self-improvement (RSI) is a process where an AI system rewrites its own code to enhance its capabilities, potentially leading to an intelligence explosion and superintelligence. Anthropic, known for its safety-focused mission, has been delegating more AI development to AI systems themselves, accelerating progress. The company's proposal comes amid geopolitical tensions over AI leadership and industry debates on safety versus competitiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-warns-ai-may-soon-begin-recursive-self-improvement/">Anthropic warns AI may soon begin recursive self-improvement</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#Anthropic`, `#AI regulation`, `#recursive self-improvement`, `#geopolitics`

---