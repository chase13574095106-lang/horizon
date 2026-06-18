---
layout: default
title: "Horizon Summary: 2026-06-18 (EN)"
date: 2026-06-18
lang: en
---

> From 35 items, 9 important content pieces were selected

---

1. [10k GitHub Repos Found Distributing Trojan Malware](#item-1) ⭐️ 9.0/10
2. [Noam Shazeer, Transformer Co-Author, Joins OpenAI](#item-2) ⭐️ 9.0/10
3. [GLM-5.2: Top Open Weights LLM Released](#item-3) ⭐️ 9.0/10
4. [Forced Consent Complaint Leads to €1.8M GDPR Fine for Elkjop](#item-4) ⭐️ 8.0/10
5. [Cornell's CS 6120 Advanced Compilers Course Goes Self-Guided](#item-5) ⭐️ 8.0/10
6. [Hospitals and universities repurpose drugs at 90% lower cost](#item-6) ⭐️ 8.0/10
7. [Modos Color Monitor Pushes E-Paper Displays Further](#item-7) ⭐️ 8.0/10
8. [Infant Diapers Found to Contain Reproductive Toxicant Formamide](#item-8) ⭐️ 8.0/10
9. [Apple and Intel Reach Preliminary Chip Foundry Deal](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [10k GitHub Repos Found Distributing Trojan Malware](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

Security researcher Orchidfiles discovered over 10,000 GitHub repositories distributing Trojan malware, targeting automated agents and dependency systems. The repositories are not forks, have different names, and are constantly updated to evade detection. This widespread supply chain attack threatens the open-source ecosystem, as automated agents and developers may unknowingly download malware into their projects. The scale (10k repos) and active evasion tactics make it a significant security concern. The malware is distributed via fake proof-of-concept exploits and other deceptive repositories. Attackers delete and push new commits every few hours to stay under the radar, and they target new repositories rather than popular ones to avoid scrutiny.

hackernews · theorchid · Jun 18, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48583928)

**Background**: Supply chain attacks on open-source software have been increasing, with attackers injecting malware into dependencies that are automatically downloaded by build tools. GitHub is a common vector because developers often clone repositories without thorough inspection. This campaign exploits automated agents that search for and include dependencies, making it a modern, scalable threat.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/orchidfiles/i-discovered-a-large-scale-malware-distribution-campaign-on-github-4m6o">I discovered a large-scale malware distribution campaign on GitHub</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/thousands-of-github-repositories-deliver-fake-poc-exploits-with-malware/">Thousands of GitHub repositories deliver fake PoC exploits with...</a></li>
<li><a href="https://arstechnica.com/security/2025/07/open-source-repositories-are-seeing-a-rash-of-supply-chain-attacks/">Supply-chain attacks on open source software are getting out of hand ...</a></li>

</ul>
</details>

**Discussion**: Community comments confirm the severity, with users reporting similar experiences of their names being attached to malicious repos. Some discuss the targeting of automated agents and the timing around major elections, while others share detailed write-ups of their own encounters.

**Tags**: `#security`, `#malware`, `#GitHub`, `#supply chain attack`, `#open source`

---

<a id="item-2"></a>
## [Noam Shazeer, Transformer Co-Author, Joins OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 9.0/10

Noam Shazeer, co-author of the seminal 'Attention Is All You Need' paper and former Gemini co-lead at Google, has announced he is joining OpenAI. This move represents a major talent acquisition for OpenAI, potentially accelerating its development of next-generation AI models, while highlighting ongoing talent competition between leading AI labs. Shazeer had recently returned to Google in 2024 via a licensing deal with Character.AI, where he was co-founder, and was appointed Gemini co-lead before leaving again for OpenAI.

hackernews · lukasgross · Jun 18, 00:26 · [Discussion](https://news.ycombinator.com/item?id=48578913)

**Background**: The Transformer architecture, introduced in the 2017 paper 'Attention Is All You Need,' revolutionized deep learning by replacing recurrent layers with self-attention mechanisms, enabling more efficient training and forming the basis for modern large language models like GPT and Gemini. Noam Shazeer was one of the eight co-authors of that paper and has been a key figure in AI research at Google since 2000, contributing to AdSense and later co-leading Gemini.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noam_Shazeer">Noam Shazeer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_architecture">Transformer architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**Discussion**: The community expressed surprise at Shazeer's quick departure from Google after his return, with some speculating about internal disagreements or political views as possible reasons. Others provided context on his career trajectory and contributions, noting the significance of his move for the AI industry.

**Tags**: `#AI`, `#OpenAI`, `#Google`, `#Transformers`, `#Talent`

---

<a id="item-3"></a>
## [GLM-5.2: Top Open Weights LLM Released](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai released GLM-5.2, a 753-billion-parameter open weights LLM under MIT license, achieving top scores on independent benchmarks with a 1 million token context window. This release marks a significant milestone for open-source AI, as GLM-5.2 outperforms other open models on the Artificial Analysis Intelligence Index and ranks second on the Code Arena WebDev leaderboard, rivaling proprietary models at a fraction of the cost. GLM-5.2 uses a Mixture-of-Experts architecture with 40 active parameters, has a 1.51TB model size, and is text-only. It consumes more output tokens per task than competitors (43k vs. 24-37k).

rss · Simon Willison · Jun 17, 23:58

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like text. Open weights models allow developers to download and run the model locally, fostering transparency and customization. Mixture-of-Experts (MoE) models activate only a subset of parameters per token, improving efficiency. A 1M token context window enables processing of very long documents, such as entire code repositories.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/17/glm-52/">GLM-5.2 is probably the most powerful text-only open weights LLM</a></li>
<li><a href="https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost">Z.ai’s open-weights GLM-5.2 beats GPT-5.5 on multiple long-horizon coding benchmarks for 1/6th the cost | VentureBeat</a></li>
<li><a href="https://explore.n1n.ai/blog/run-glm-5-2-locally-open-weights-guide-2026-06-15">Run GLM-5.2 Locally: A Complete Guide to the Open Weights Coding Model | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai</a></li>

</ul>
</details>

**Discussion**: The community is excited about GLM-5.2's performance and open license, but some note its high token usage and lack of vision capabilities. The model's strong coding results without image input surprised many.

**Tags**: `#LLM`, `#open weights`, `#GLM-5.2`, `#AI`, `#benchmarks`

---

<a id="item-4"></a>
## [Forced Consent Complaint Leads to €1.8M GDPR Fine for Elkjop](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

A privacy advocate's complaint about forced consent for Elkjop's customer club resulted in a €1.8 million fine from the Norwegian Data Protection Authority (Datatilsynet) after five years of proceedings. This case demonstrates that GDPR enforcement can hold companies accountable for making consent a condition of service, reinforcing that consent must be freely given. It sets a precedent for similar forced consent practices across Europe. The company argued that membership in the customer club was required to receive marketing offers, which the DPA ruled as unlawful forced consent. The fine amount reflects the seriousness of the violation and the duration of non-compliance.

hackernews · speckx · Jun 18, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48589501)

**Background**: Under GDPR, consent must be freely given, specific, informed, and unambiguous. Forcing users to consent to data processing as a condition of service (e.g., for a customer club) violates this principle. The Norwegian DPA has a reputation for user-centric enforcement.

**Discussion**: Commenters praised the outcome and the Norwegian DPA's user-centric approach, though noted the lengthy process. Some expressed hope that more individuals would exercise their rights, while others highlighted the challenge of pushing back against such practices, especially in the US.

**Tags**: `#GDPR`, `#privacy`, `#consent`, `#data protection`, `#regulation`

---

<a id="item-5"></a>
## [Cornell's CS 6120 Advanced Compilers Course Goes Self-Guided](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 8.0/10

Cornell University's CS 6120: Advanced Compilers course is now available as a free, self-guided online resource, allowing learners worldwide to access its materials at their own pace. This makes high-quality compiler education freely accessible to a broad audience, potentially lowering the barrier to entry for advanced systems topics and fostering a new generation of compiler engineers. The course covers topics like dead code elimination, data flow analysis, dominator analysis, and SSA form, but some commenters note it may not be truly 'advanced' for all topics. The section on dynamic compilers focuses heavily on trace compilation, which some experts consider a dead end.

hackernews · ibobev · Jun 18, 11:04 · [Discussion](https://news.ycombinator.com/item?id=48583606)

**Background**: Compilers translate high-level programming languages into machine code. Advanced compiler courses typically cover optimization techniques and runtime systems. Trace compilation is a just-in-time (JIT) technique that records and compiles frequently executed code paths, but it has been largely abandoned in favor of method-based JIT compilation with type feedback and deoptimization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tracing_just-in-time_compilation">Tracing just-in-time compilation - Wikipedia</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/1852761.1852771">Trace-based compilation in execution environments without interpreters | Proceedings of the 8th International Conference on the Principles and Practice of Programming in Java</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion includes praise for the course's availability but also critical feedback: titzer argues that trace compilation is a dead end and that the course should cover type feedback, speculation, and deoptimization instead. j2kun questions the 'advanced' label, noting that many topics belong in a first compiler course.

**Tags**: `#compilers`, `#education`, `#programming languages`, `#systems`

---

<a id="item-6"></a>
## [Hospitals and universities repurpose drugs at 90% lower cost](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

Hospitals and universities are repurposing existing drugs for new uses at a fraction of the cost, offering affordable treatments for conditions like blindness and rare diseases. This challenges traditional pharmaceutical pricing models and could significantly reduce healthcare costs, especially for rare diseases where new drug development is often not profitable. For example, using bevacizumab (Avastin) for macular degeneration costs about $50 per dose versus $1,500 for ranibizumab (Lucentis), despite being molecularly similar.

hackernews · giuliomagnifico · Jun 18, 10:33 · [Discussion](https://news.ycombinator.com/item?id=48583386)

**Background**: Drug repurposing involves investigating existing approved drugs for new therapeutic purposes. It bypasses many early-stage development costs, making treatments cheaper. However, regulatory pathways for off-label use without manufacturer consent remain limited.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Drug_repurposing">Drug repurposing</a></li>
<li><a href="https://www.fda.gov/news-events/press-announcements/fda-advances-drug-repurposing-address-unmet-medical-needs">FDA Advances Drug Repurposing to Address Unmet Medical Needs</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiences, such as using Spravato (esketamine) for depression, noting that esketamine is a modified version of ketamine patented for profit despite being potentially less effective. Others highlighted nonprofits like Cures Within Reach that fund repurposing studies for rare diseases like Huntington's.

**Tags**: `#drug repurposing`, `#healthcare costs`, `#pharmaceuticals`, `#rare diseases`, `#health policy`

---

<a id="item-7"></a>
## [Modos Color Monitor Pushes E-Paper Displays Further](https://spectrum.ieee.org/modos-e-paper-monitor) ⭐️ 8.0/10

Two-person startup Modos is developing the Modos Flow, a 13.3-inch color e-paper monitor with a native resolution of 3200x2400, touch input, and a 60Hz refresh rate enabled by a new FPGA-based display controller. This marks a significant leap in e-paper technology, offering color, high resolution, and a smooth 60Hz refresh rate that could make e-paper viable for general-purpose computing, reducing eye strain and power consumption compared to traditional LCDs. The Modos Flow builds on the earlier Modos Paper devkit and uses a color filter array (CFA) over a monochrome panel, similar to color LCDs. The 60Hz refresh rate is achieved via a custom FPGA controller, which may impact panel longevity due to increased switching of the electrophoretic medium.

hackernews · Vinnl · Jun 18, 11:41 · [Discussion](https://news.ycombinator.com/item?id=48583897)

**Background**: E-paper displays, like those from E Ink, use electrophoretic technology to reflect light like paper, consuming power only when the image changes. Traditional e-paper has low refresh rates (often <10Hz) and limited color, making it suitable for e-readers but not for dynamic content. Modos aims to overcome these limitations with a high-refresh, color e-paper monitor.

<details><summary>References</summary>
<ul>
<li><a href="https://spectrum.ieee.org/modos-e-paper-monitor">Modos Color Monitor Pushes E-Paper Displays Further - IEEE Spectrum</a></li>
<li><a href="https://www.cnx-software.com/2026/05/27/modos-flow-an-fpga-based-13-3-inch-usb-c-touchscreen-color-e-paper-monitor/">Modos Flow - An FPGA-based 13.3-inch USB-C touchscreen e-paper monitor (Crowdfunding) - CNX Software</a></li>
<li><a href="https://www.modos.tech/blog/modos-paper-monitor">The Modos Paper Monitor | Modos</a></li>

</ul>
</details>

**Discussion**: The community is excited about the Modos Flow's specs, with many seeing it as a breakthrough for e-paper monitors. Some commenters express concerns about panel longevity at higher refresh rates, while others discuss potential use cases like outdoor tablets and low-power auxiliary displays.

**Tags**: `#e-paper`, `#display technology`, `#hardware`, `#startup`

---

<a id="item-8"></a>
## [Infant Diapers Found to Contain Reproductive Toxicant Formamide](https://www.sohu.com/a/1038121771_122014422) ⭐️ 8.0/10

A commissioned test by the Economic Information Daily detected the reproductive toxicant formamide in several major infant diaper brands, including HUGGIES, Bebaby, and Babycare. The substance was also found in the blood and urine of some infants, and a reporter's blood concentration nearly doubled after wearing one diaper overnight. This is significant because formamide is classified as a reproductive toxicant and can be absorbed through the skin, posing a serious health risk to infants whose organs are still developing. The current national standard for diapers does not require testing for formamide, highlighting a critical regulatory gap that needs urgent revision. Formamide is commonly used in adhesives and softeners in diaper production. The European Union classifies it as a Category 1B reproductive toxicant, and it is already banned in cosmetics in China. Experts warn that long-term accumulation may damage the reproductive system, liver, and kidneys.

telegram · zaihuapd · Jun 18, 07:09

**Background**: Formamide is a colorless liquid with a faint ammonia odor, used as a solvent and in manufacturing. It is known to cause reproductive and developmental toxicity in animal studies. In China, diapers are regulated under national standards that focus on physical properties and microbial safety but do not include chemical hazards like formamide. This incident has sparked public concern and calls for updating the standards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sohu.com/a/1038359743_539932">“好奇”、“碧芭宝贝”、“Babycare”多款知名婴儿纸尿裤检测出甲酰胺生殖...</a></li>
<li><a href="https://www.163.com/dy/article/KVNFKETB0511T7D3.html">国标不检就不管？好奇、babycare等品牌陷入“毒纸尿裤”风波|宝宝|甲醛|...</a></li>
<li><a href="https://www.thepaper.cn/newsDetail_forward_33412554">纸尿裤“甲酰胺”风波：品牌自证“未检出”，国标无检测要求_澎湃号·媒体_...</a></li>

</ul>
</details>

**Tags**: `#public health`, `#consumer safety`, `#regulatory gap`, `#toxicology`, `#infant products`

---

<a id="item-9"></a>
## [Apple and Intel Reach Preliminary Chip Foundry Deal](https://t.me/zaihuapd/42031) ⭐️ 8.0/10

Apple and Intel have signed a preliminary agreement for Intel to manufacture some chips for Apple devices, after over a year of negotiations. The deal was finalized in recent months, though specific products (iPhone, iPad, or Mac) are not yet disclosed. This agreement marks a major shift in Apple's chip supply chain, reducing reliance on TSMC and strengthening US domestic semiconductor manufacturing. It also boosts Intel's foundry business, which has struggled with delays and yields, and aligns with US government efforts to onshore chip production. The deal was heavily pushed by the US government, with the Commerce Secretary lobbying Apple CEO Tim Cook multiple times. Intel now has foundry partnerships with Nvidia, SpaceX, and Apple, though the agreement is preliminary and not yet a finalized commercial contract.

telegram · zaihuapd · Jun 18, 09:19

**Background**: Intel was once the world's largest chipmaker but has faced challenges in its foundry business, including low yields and delays. Apple has long relied on TSMC for chip manufacturing, but US government pressure to reduce dependence on Asian suppliers has driven this potential shift. The CHIPS Act and geopolitical tensions have accelerated efforts to bring semiconductor manufacturing back to the US.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel">Intel - Wikipedia</a></li>
<li><a href="https://www.gadgetreview.com/trump-claims-apple-intel-chip-deal-neither-company-confirms">Trump Claims Apple - Intel Chip Deal - Neither... - Gadget Review</a></li>
<li><a href="https://colitco.com/amd-vs-intel-stock-apple-chip-deal-ai-chips-0905202615/">One Analyst Has Picked a Clear Winner in the AMD vs Intel ... - Colitco</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Intel`, `#semiconductor`, `#chip manufacturing`, `#supply chain`

---