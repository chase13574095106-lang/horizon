---
layout: default
title: "Horizon Summary: 2026-06-24 (EN)"
date: 2026-06-24
lang: en
---

> From 27 items, 6 important content pieces were selected

---

1. [OpenAI unveils first custom AI inference chip Jalapeño](#item-1) ⭐️ 9.0/10
2. [Nub: A Bun-like toolkit for Node.js without replacing runtime](#item-2) ⭐️ 8.0/10
3. [NSA Loses Access to Anthropic's Mythos AI Tool](#item-3) ⭐️ 8.0/10
4. [Generative AI for Homework May Lower Chinese Students' Exam Scores](#item-4) ⭐️ 8.0/10
5. [Cloudflare and Browsers Propose PACT to Replace CAPTCHAs](#item-5) ⭐️ 8.0/10
6. [Micron Q3 FY2026: Revenue Surges 346%, Net Profit $28.2B](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI unveils first custom AI inference chip Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI, in partnership with Broadcom and manufactured by TSMC, unveiled its first custom AI inference chip named Jalapeño, designed specifically for large language model workloads. The chip was developed from concept to production in nine months, accelerated by OpenAI's own AI models. This marks a major strategic move by OpenAI to reduce dependence on GPU suppliers like Nvidia and optimize inference costs, which are becoming the primary expense for AI services. The chip could significantly lower the cost of running ChatGPT and other OpenAI products, potentially reshaping the AI hardware landscape. Early testing shows Jalapeño delivers significantly better performance per watt than current state-of-the-art AI accelerators, though detailed benchmarks have not been released. Broadcom CEO Hock Tan stated the accelerator shows cost savings of roughly 50% compared with typical AI GPUs.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference is the process of generating responses from trained models, as opposed to training which builds the model. Inference is becoming a major cost center for AI companies like OpenAI, as serving millions of users requires massive compute resources. Custom inference chips can be more efficient than general-purpose GPUs by optimizing for specific workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/openai-unveils-custom-chip-it-designed-with-broadcom-boost-its-ai-infrastructure-2026-06-24/">OpenAI unveils custom chip it designed with Broadcom to boost ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about OpenAI's claim that AI models accelerated the chip design, calling it potentially meaningless marketing. Others discussed the technical merits of inference chips, with some noting that burning model weights into silicon could yield even greater efficiency, though at the cost of flexibility.

**Tags**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [Nub: A Bun-like toolkit for Node.js without replacing runtime](https://github.com/nubjs/nub) ⭐️ 8.0/10

Colin McDonnell released Nub, an all-in-one toolkit for Node.js that adds transpilation, module resolution, and polyfills via a --require preload hook, enhancing developer experience without forking Node's runtime. Nub offers a pragmatic alternative to Bun by augmenting Node.js with similar developer experience improvements, potentially reducing fragmentation in the JavaScript ecosystem and allowing teams to adopt modern features without switching runtimes. Nub uses the oxc transpiler packaged as a Node-API add-on, registers a module resolution hook, and injects polyfills for APIs like Worker and Temporal. It runs on stock Node.js without modifying the runtime.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Bun is an all-in-one JavaScript runtime that includes a transpiler, bundler, and package manager, offering improved developer experience over Node.js. Nub takes a different approach by layering similar capabilities on top of Node.js via preload hooks, rather than creating a new runtime. This allows users to keep using Node.js while gaining some of Bun's benefits.

**Discussion**: The community response is positive, with users praising the pragmatic approach and reporting successful adoption in production. One commenter noted the author's background as the creator of Zod and former Bun employee, while another raised a technical question about ESM support via --require vs --import.

**Tags**: `#Node.js`, `#developer tools`, `#JavaScript`, `#tooling`, `#open source`

---

<a id="item-3"></a>
## [NSA Loses Access to Anthropic's Mythos AI Tool](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html) ⭐️ 8.0/10

The NSA lost access to Anthropic's advanced AI tool 'Mythos' after a contract dispute, reportedly because Anthropic refused to renew the agreement amid tensions over a $200 million Pentagon contract. This incident highlights the growing tension between national security agencies and AI companies over access to cutting-edge models, raising concerns about AI security, supply chain risks, and the balance of power in AI governance. Mythos is a powerful AI model designed for cybersecurity tasks, capable of identifying software vulnerabilities rapidly. The NSA had been using it through a contract that was not finalized, and some Pentagon officials now want the NSA to explore alternative models.

hackernews · thm · Jun 24, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48658300)

**Background**: Anthropic, the company behind the Claude AI models, developed Mythos as part of its Project Glasswing program, offering early access to trusted organizations for vulnerability detection. In February 2026, the Pentagon designated Anthropic a supply chain risk and signed replacement deals with seven other companies, but the NSA continued evaluating Mythos. The dispute escalated when Anthropic refused to renew the NSA's access, leading to the current loss of capability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html">N.S.A. Lost Access to Powerful A.I. Model Amid Anthropic Dispute</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://www.nextgov.com/artificial-intelligence/2026/06/parts-nsa-lose-mythos-5-access-amid-anthropic-supply-chain-dispute/414366/">Parts of NSA lose Mythos 5 access amid Anthropic supply chain ...</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some users express relief that the NSA lost access, citing concerns about surveillance and power, while others question the severity of the loss, noting that the government could seize the model weights if needed. There is also debate about Mythos's actual capabilities, with one commenter claiming it could break into classified systems in hours.

**Tags**: `#AI`, `#national security`, `#Anthropic`, `#NSA`, `#AI governance`

---

<a id="item-4"></a>
## [Generative AI for Homework May Lower Chinese Students' Exam Scores](https://cepr.org/publications/dp21577) ⭐️ 8.0/10

A 30-month study tracking 26,811 Chinese students in grades 7–12 found that using generative AI for homework improved assignment scores by 18% and reduced completion time by 30%, but led to a 20% drop in closed-book exam scores within six months and an 18–24% decline in high-stakes exam scores after about two years. This research provides large-scale, longitudinal evidence that generative AI can undermine deep learning and exam performance, especially for high-achieving students, raising critical concerns for educators and policymakers about integrating AI into education. The study found that about 80% of AI users exhibited an 'homework outsourcing' pattern—very short homework time but high scores—and these students bore the largest exam losses; those who maintained homework time similar to non-AI users suffered smaller declines. Social science subjects saw the largest losses, followed by STEM and languages, with younger students, high achievers, and boys more affected.

telegram · zaihuapd · Jun 24, 05:15

**Background**: Generative AI, such as large language models, can produce human-like text and solve problems, making it attractive for completing homework. However, closed-book exams require students to recall and apply knowledge without external aids, testing genuine understanding. The study highlights a potential trade-off: AI boosts short-term homework performance but may hinder long-term knowledge retention and exam success.

**Tags**: `#generative AI`, `#education`, `#student performance`, `#research`, `#China`

---

<a id="item-5"></a>
## [Cloudflare and Browsers Propose PACT to Replace CAPTCHAs](https://www.techtimes.com/articles/318891/20260623/cloudflare-chrome-firefox-plan-replace-captchas-cryptographic-tokens.htm) ⭐️ 8.0/10

Cloudflare, together with Chrome, Firefox, Edge, and Shopify, has proposed the PACT protocol to replace CAPTCHAs with anonymous cryptographic tokens using blind signatures. If adopted, PACT could eliminate the need for users to solve annoying image puzzles while preserving privacy, significantly improving web user experience and security. The protocol is based on the IETF's Privacy Pass standard and uses blind signatures to issue tokens without revealing user identity or browsing history. However, it remains a proposal with no finalized standards body or timeline, and Apple has not joined.

telegram · zaihuapd · Jun 24, 06:30

**Background**: CAPTCHAs are widely used to distinguish humans from bots, but they are often frustrating for users and can be bypassed by advanced AI. Privacy Pass is an IETF working group that develops protocols for anonymous authentication. Blind signatures allow a server to sign a message without seeing its content, enabling privacy-preserving token issuance.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pactprotocol.io/">PACT Protocol | PACT Protocol Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/wg/privacypass/about/">Privacy Pass (privacypass) - Internet Engineering Task Force</a></li>

</ul>
</details>

**Tags**: `#web security`, `#CAPTCHA replacement`, `#cryptographic tokens`, `#Privacy Pass`, `#IETF`

---

<a id="item-6"></a>
## [Micron Q3 FY2026: Revenue Surges 346%, Net Profit $28.2B](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

Micron Technology reported record Q3 FY2026 results with revenue of $41.46 billion, up 346% year-over-year, and net profit of $28.24 billion, driven by AI demand for high-performance memory. Non-GAAP gross margin reached 84.9%. This explosive growth underscores the critical role of memory in AI infrastructure, with Micron's HBM4 already in mass production and HBM4E expected in 2027. The results signal sustained demand and pricing power for memory makers. Data center revenue surged 653% to $11.52 billion, and cloud memory grew 306% to $13.77 billion. Micron expects next-quarter revenue of $50 billion and gross margin of 86%, and has signed 16 long-term strategic agreements locking orders for 3-5 years.

telegram · zaihuapd · Jun 24, 22:22

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked DRAM technology used in AI accelerators like NVIDIA GPUs, offering much higher bandwidth than traditional DDR memory. HBM4 is the latest generation, while HBM4E is an enhanced version expected to begin production in 2027. Non-GAAP gross margin excludes certain one-time charges, providing a clearer view of operational profitability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.wevolver.com/article/high-bandwidth-memory">High Bandwidth Memory : Concepts, Architecture, and Applications</a></li>
<li><a href="https://www.digitaltoday.co.kr/en/view/53615/memory-big-two-near-hbm4e-race-mass-production-timeline-becomes-key-battleground">Memory big two near HBM 4 E race as mass production timing...</a></li>

</ul>
</details>

**Tags**: `#Micron`, `#semiconductors`, `#AI infrastructure`, `#HBM`, `#financial results`

---