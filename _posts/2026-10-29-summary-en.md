---
layout: default
title: "Horizon Summary: 2026-10-29 (EN)"
date: 2026-10-29
lang: en
---

> From 31 items, 8 important content pieces were selected

---

1. [Google Releases Gemini 4 Argon with 87% Physical Reasoning Score](#item-1) ⭐️ 9.0/10
2. [Fingerprinting Script's Obfuscated Code Mistaken for Bioweapons, Triggering LLM Refusals](#item-2) ⭐️ 8.0/10
3. [Google Announces Gemini 4 Carbon, a Restricted Frontier AI Model](#item-3) ⭐️ 8.0/10
4. [Apple unveils MacBook Pro with PROLED XDR display and touchscreen](#item-4) ⭐️ 8.0/10
5. [Apple's git still trusts compromised eMudhra certificates](#item-5) ⭐️ 8.0/10
6. [Google proposes sleep framework for continual learning in LLMs](#item-6) ⭐️ 8.0/10
7. [OpenAI Releases GPT-6.1 Terra with Halved API Pricing](#item-7) ⭐️ 8.0/10
8. [CXMT to Start HBM3E Production Despite 20-30% Yields](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Releases Gemini 4 Argon with 87% Physical Reasoning Score](https://t.me/zaihuapd/44764) ⭐️ 9.0/10

Google has released Gemini 4 Argon, a new multimodal reasoning model that strengthens physical understanding, code generation, and visual-semantic reasoning. It achieves 87% on the embodied reasoning benchmark ERQA using pure reasoning, outperforming other frontier models, and can control robots like Boston Dynamics Spot to perform tasks such as picking up and throwing objects. This release marks a significant leap in multimodal reasoning for robotics, showing that a general-purpose model can directly control complex robots and generate simulation data to improve real-world performance. It could accelerate development in embodied AI and lower the barrier for deploying capable robots in real-world scenarios. Argon can generate simulation data that boosts real robot task success rates from 56% to 75% while reducing task time from 35 seconds to 24 seconds. It is now available through the google-genai SDK, with pricing at $2 per million input tokens and $X per million output tokens (output price truncated in source).

telegram · zaihuapd · Oct 28, 17:09

**Background**: ERQA (Embodied Reasoning Question Answering) is a benchmark designed to evaluate how well multimodal AI models perform on embodied reasoning tasks, covering spatial reasoning and real-world robotics scenarios. Boston Dynamics Spot is a quadruped robot known for agile mobility and, with an added arm, mobile manipulation capabilities. The google-genai SDK provides a unified interface for developers to integrate Gemini models into applications.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/embodiedreasoning/ERQA">GitHub - embodiedreasoning/ERQA: Embodied Reasoning Question ...</a></li>
<li><a href="https://bostondynamics.com/products/spot/">Spot | Boston Dynamics</a></li>
<li><a href="https://github.com/googleapis/python-genai">GitHub - googleapis/python-genai: Google Gen AI Python SDK ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal`, `#robotics`, `#Google`, `#Gemini`

---

<a id="item-2"></a>
## [Fingerprinting Script's Obfuscated Code Mistaken for Bioweapons, Triggering LLM Refusals](https://nullpt.rs/fingerprinting-bioweapons) ⭐️ 8.0/10

A blog post on nullpt.rs investigates how a browser fingerprinting script's obfuscated JavaScript resembles bioweapon-related content, causing large language models to refuse analysis. The Hacker News discussion (185 comments) highlights broader implications for AI safety filters and adversarial obfuscation. This incident underscores the challenge of false positives in LLM safety filters, where legitimate security research or benign code can be blocked, hindering defensive work. It also reveals an emerging arms race between obfuscation techniques and AI moderation, with implications for web security and AI safety. The fingerprinting script likely uses obfuscation techniques such as string encoding or packing that produce patterns resembling dangerous content, triggering safety classifiers. Community members note that some models (e.g., GLM-5.3) complied with analysis requests while frontier commercial models refused, suggesting variability in safety filter strictness.

hackernews · hazebooth · Oct 28, 17:13 · [Discussion](https://news.ycombinator.com/item?id=50276998)

**Background**: Browser fingerprinting scripts collect device and browser attributes to uniquely identify users, often for bot detection or tracking. To prevent reverse engineering, these scripts are commonly obfuscated, making their code hard to read. LLM safety filters are trained to block requests that appear to involve harmful topics like bioweapons, but they can produce false positives on obfuscated or security-related code.

<details><summary>References</summary>
<ul>
<li><a href="https://klu.ai/glossary/llm-guardrails">LLM Guardrails — Klu</a></li>
<li><a href="https://community.openai.com/t/recent-safety-filter-update-causing-high-false-positives-on-legitimate-academic-ml-research/1410325">Recent Safety Filter Update Causing High False Positives on...</a></li>
<li><a href="https://arxiv.org/abs/2606.11755">[2606.11755] Acoda: Adversarial Code Obfuscation for ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared anecdotes about watermarks and anti-LLM strings causing unintended blocking, and expressed amazement at the fractal-like arms race between obfuscation and AI moderation. Some noted that certain models like GLM-5.3 were more permissive, while others joked about the absurdity of the situation.

**Tags**: `#fingerprinting`, `#LLM safety`, `#obfuscation`, `#web security`, `#AI moderation`

---

<a id="item-3"></a>
## [Google Announces Gemini 4 Carbon, a Restricted Frontier AI Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) ⭐️ 8.0/10

Google announced Gemini 4 Carbon, its newest frontier AI model, which ranks #1 on the Artificial Analysis Intelligence Index v5.0 with a score of 59 and shows significant gains in coding and cybersecurity capabilities. The model builds on Gemini 4 Argon, launched two weeks earlier, but is restricted to select cybersecurity experts and not publicly available. This release highlights Google's rapid iteration pace in the frontier model race, but the restricted access and confusing model naming (Carbon, Argon, Pro, Ultra, Flash) have sparked debate about product clarity and benchmark validity. The focus on cybersecurity and long-horizon capabilities signals a strategic push into high-stakes enterprise and government applications. Gemini 4 Carbon achieved 88.2% on SEC-bench and shows reduced misalignment and fabrication rates in internal coding environments, but it is essentially a slightly better version of Argon and is not publicly accessible. The model's benchmark scores were presented without a release date for general availability, raising questions about their relevance in a fast-moving field.

hackernews · acossta · Oct 28, 17:01 · [Discussion](https://news.ycombinator.com/item?id=50276792)

**Background**: Gemini is Google's flagship family of large language models, offered in multiple tiers such as Ultra, Pro, Flash, and Lite to serve different performance and cost needs. Frontier models like Gemini 4 Carbon are the most advanced and expensive versions, often used for specialized tasks like cybersecurity and complex reasoning. The Artificial Analysis Intelligence Index is a composite benchmark that evaluates models across reasoning, knowledge, mathematics, and coding.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/">Introducing Gemini 4 Carbon</a></li>
<li><a href="https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/">Google announces Gemini 4 Carbon, its latest frontier AI ...</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-carbon">Gemini 4 Carbon (high) - Intelligence, Performance... | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed frustration over Google's confusing model naming and tiering, with one joking they'd struggle to figure out how to prompt Gemini 4 Argon even with $100. Others argued that showing benchmarks without releasing the model is meaningless in a fast-moving field, and some suggested standardizing model tiers like Ultra, Pro, Flash, and Lite similar to SEMVER.

**Tags**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-4"></a>
## [Apple unveils MacBook Pro with PROLED XDR display and touchscreen](https://www.apple.com/macbook-pro/proled-xdr-display/) ⭐️ 8.0/10

Apple announced a new MacBook Pro featuring a PROLED XDR display based on tandem OLED technology and, for the first time, a touchscreen. The 14-inch and 16-inch models also see significant weight reductions of about 15% and a thinner design. This marks Apple's first touchscreen Mac, a major shift in the Mac's interaction paradigm that could reshape professional workflows and influence the broader laptop market. The new display technology also sets a new benchmark for laptop visual performance. The PROLED XDR display offers up to 1000 nits sustained full-screen brightness, 2000 nits peak HDR brightness, and a 10,000,000:1 contrast ratio. The laptops retain M5 Pro and M5 Max chips, and the 14-inch model claims up to 22 hours of video playback.

hackernews · etothet · Oct 28, 17:10 · [Discussion](https://news.ycombinator.com/item?id=50276940)

**Background**: XDR (Extreme Dynamic Range) is Apple's branding for high-dynamic-range displays, previously used on Pro Display XDR and iPad Pro with mini-LED backlights. PROLED XDR is a new iteration that uses tandem OLED technology, which stacks two OLED layers to boost brightness and longevity compared to traditional OLED. OLED displays emit light per pixel without a backlight, enabling deeper blacks and thinner panels, but can suffer from burn-in over time.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/macbook-pro/proled-xdr-display/pdf/PROLED_XDR_Display_Technical_Paper.pdf">PROLED XDR DISPLAY Technology Overview - Apple</a></li>
<li><a href="https://support.apple.com/en-us/109039">About the Super Retina display and Super Retina XDR display ... Pro Display XDR - Tech Specs - Apple Support Apple Display Technology Explained - Retina vs Liquid Retina ... What Is XDR Display & Apple EDR on Mac? (2026 Guide) Beyond the Hype: Inside Apple’s New PROLED XDR Display Technology Apple launches PROLED XDR OLED display on MacBook Pro | The ...</a></li>
<li><a href="https://www.macrumors.com/2026/10/28/touchscreen-macbook-pro-debut-these-5-features/">Touchscreen MacBook Pro to Debut Today With These... - MacRumors</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some argue that adding a touchscreen will create usability complaints because macOS UI elements are too small for fingers, while others praise the significant weight reduction and thinner design. Some question the value of touch on laptops, citing fingerprints and the precision of a mouse, and others feel Apple's design efforts are declining.

**Tags**: `#Apple`, `#MacBook Pro`, `#hardware`, `#display technology`, `#touchscreen`

---

<a id="item-5"></a>
## [Apple's git still trusts compromised eMudhra certificates](https://emudhra.we-have-a-problem.com/apple.html) ⭐️ 8.0/10

As of October 28, 2026, Apple's macOS and its bundled developer tools—including git, curl, and python3—still trust eight compromised eMudhra intermediate certificates, despite being notified of the incident on October 17. Apple's recommended mitigation requires manually editing the certificate chain, and subsequent OS updates may revert these changes, reintroducing the vulnerability. This is a significant security issue because it affects not only git but many system-provided utilities that rely on the OS trust store, potentially exposing developers and macOS users to man-in-the-middle attacks. It highlights the chaotic state of OS-level certificate management and raises questions about Apple's security practices. The compromised certificates use weak keys with single-digit or double-digit integers instead of the mandatory 384 bits of pseudo-random security, allowing attackers to impersonate the intermediate CAs. Apple's mitigation involves manual certificate chain edits, but OS updates may revert them, as has happened at least once.

hackernews · galadran · Oct 28, 11:03 · [Discussion](https://news.ycombinator.com/item?id=50271640)

**Background**: eMudhra is a certificate authority that issued eight intermediate certificates with weak private keys, which were discovered in October 2026. These certificates are trusted by many operating systems and applications, enabling attackers to intercept TLS traffic. macOS uses a system trust store that is utilized by bundled tools like git and curl, so compromised certificates in that store affect those utilities.

<details><summary>References</summary>
<ul>
<li><a href="https://emudhra.we-have-a-problem.com/apple.html">Apple's git still trusts the compromised eMudhra certificates</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here's what you need ...</a></li>
<li><a href="https://blog.talosintelligence.com/compromised-intermediate-certificates/">Compromised eMudhra intermediate certificates</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage that Apple's guidance requires manual certificate chain edits and that OS updates may revert the mitigation, with some noting the issue affects many system utilities beyond git. Others criticized the chaotic state of OS-level certificate management and suggested that Apple should easily remove revoked CA certs in a system update. One commenter speculated that the weak key generation might have been intentional, though no evidence was provided.

**Tags**: `#security`, `#macOS`, `#TLS certificates`, `#git`, `#certificate management`

---

<a id="item-6"></a>
## [Google proposes sleep framework for continual learning in LLMs](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research has introduced a 'sleep framework' for continual learning that adds offline consolidation phases, alternating between active interaction and offline sleep, allowing LLMs to consolidate short-term context into long-term parameters. The method outperforms baselines such as GPT-4 and SFT on tasks including 10-million-token long-context, continual translation, and math reasoning. This work addresses catastrophic forgetting, a major obstacle to deploying LLMs that continuously learn from new data, and could enable models to acquire new skills without losing prior knowledge. If validated, it may influence how future LLMs are trained and updated in dynamic environments. The framework alternates between an active wake phase and an offline sleep phase, where the model consolidates knowledge; it was evaluated on long-context (10M tokens), continual translation, and math reasoning, showing gains over GPT-4 and SFT baselines. However, it is a research proposal, and details such as computational overhead and scalability remain to be fully assessed.

telegram · zaihuapd · Oct 28, 01:46

**Background**: Catastrophic forgetting refers to the tendency of neural networks, including large language models, to lose previously learned knowledge when trained on new tasks or data. Continual learning aims to enable models to learn sequentially without forgetting, and offline consolidation—inspired by how biological brains consolidate memories during sleep—is a promising approach. Traditional machine learning separates training and inference, but continual learning blurs this distinction, requiring models to constantly adapt.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/">The sleep framework: A new way for LLMs to retain knowledge ...</a></li>
<li><a href="https://www.nerdheadz.com/blog/continual-learning-llms-offline-phase-sleep">Continual Learning in LLMs : The Sleep Problem | NerdHeadz Blog</a></li>
<li><a href="https://arxiv.org/abs/2402.01364">[2402.01364] Continual Learning for Large Language Models: A Survey</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#LLM`, `#catastrophic forgetting`, `#Google Research`, `#sleep framework`

---

<a id="item-7"></a>
## [OpenAI Releases GPT-6.1 Terra with Halved API Pricing](https://t.me/zaihuapd/44750) ⭐️ 8.0/10

OpenAI has released GPT-6.1 Terra, a new model emphasizing visual reasoning, precise computer use, and more natural writing, with standard API pricing 50% lower than GPT-5.6 Terra. It is now available to Plus, Pro, Enterprise, and Edu users of ChatGPT Work and Codex. This release significantly lowers the cost of advanced AI capabilities, making vision and computer-use features more accessible to developers and businesses. The substantial benchmark improvements and price cut could pressure competitors to offer similar capabilities at lower prices. GPT-6.1 Terra scores 15 percentage points higher than GPT-5.6 Terra on benchmarks at roughly one-third the cost, and its error rate at low reasoning effort drops from 53.6% to 16.7%. The standard API pricing is set per million input tokens, though the exact price was not specified in the source.

telegram · zaihuapd · Oct 28, 03:26

**Background**: GPT-6.1 Terra is a mid-range model in OpenAI's GPT-6.1 line, designed for daily agentic scenarios, programming, and text tasks, with strong screenshot understanding. ChatGPT Work is an agent for longer, multi-step work and finished deliverables, while Codex is OpenAI's AI coding partner available across ChatGPT, editors, and the terminal. The model's computer-use capabilities refer to its ability to interact with software interfaces, such as clicking and typing, to automate tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/gpt-6-1-terra">GPT - 6 . 1 Terra API: Visual Reasoning & Writing | Kie.ai</a></li>
<li><a href="https://simonwillison.net/2026/Oct/26/gpt-61-terra/">GPT - 6 . 1 Terra | Simon Willison’s Weblog</a></li>
<li><a href="https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex">ChatGPT Work and Codex - OpenAI Help Center</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#LLM`, `#model-release`, `#API-pricing`, `#benchmarks`

---

<a id="item-8"></a>
## [CXMT to Start HBM3E Production Despite 20-30% Yields](https://www.reuters.com/world/china/chinas-cxmt-start-advanced-ai-memory-production-despite-poor-yields-sources-say-2026-10-28/) ⭐️ 8.0/10

CXMT has sampled HBM3E to multiple domestic AI chip designers and plans to begin limited production within two months, according to two sources cited by Reuters. However, its yields are only 20-30%, far below SK Hynix's roughly 70%, and testing shows performance closer to SK Hynix's previous-generation HBM3. This marks a major milestone for China's AI memory self-sufficiency under US export controls, as domestic AI chip designers currently face a severe shortage of high-bandwidth memory. Even with low yields and lagging performance, CXMT's entry could reduce reliance on foreign suppliers and reshape the competitive landscape for AI hardware in China. CXMT's HBM3E is expected to be priced higher than comparable overseas products, reflecting the cost pressures of low yields and limited scale. The performance gap means it may not match the latest HBM3E from SK Hynix, Micron, or Samsung, which offer higher bandwidth and power efficiency for AI training and inference.

telegram · zaihuapd · Oct 28, 06:19

**Background**: High Bandwidth Memory (HBM) is a type of DRAM stacked vertically and connected via advanced packaging, delivering much higher bandwidth than conventional memory—critical for AI accelerators. HBM3E is an enhanced version of HBM3, offering greater capacity and speed; SK Hynix, Micron, and Samsung are the leading suppliers. CXMT, founded in 2016 and headquartered in Hefei, is China's largest DRAM manufacturer and a key player in Beijing's push for semiconductor self-sufficiency. Yield rate refers to the percentage of manufactured chips that meet performance specifications, and low yields significantly increase per-chip costs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yield_(metric)">Yield (metric) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#HBM3E`, `#CXMT`, `#semiconductor manufacturing`, `#AI memory`, `#export controls`

---