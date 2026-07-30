---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 33 items, 13 important content pieces were selected

---

1. [GitHub Launches Stacked Pull Requests in Public Preview](#item-1) ⭐️ 9.0/10
2. [OpenAI slashes GPT-5.6 Luna price by 80%](#item-2) ⭐️ 9.0/10
3. [Anthropic's AI Finds Critical Flaw in NIST Post-Quantum Candidate HAWK](#item-3) ⭐️ 9.0/10
4. [Cheap TV Streaming Sticks Pre-Infected with Malware](#item-4) ⭐️ 8.0/10
5. [DeepMind's Gemini Robotics 2 Enables Whole-Body Robot Control](#item-5) ⭐️ 8.0/10
6. [UEFA and 55 national associations threaten FIFA boycott](#item-6) ⭐️ 8.0/10
7. [Muon Mystery Solved, Old Results Invalidated](#item-7) ⭐️ 8.0/10
8. [Economic Benefits of AI-Assisted Refactoring](#item-8) ⭐️ 8.0/10
9. [GCC Steering Committee Adopts AI Contributions Policy](#item-9) ⭐️ 8.0/10
10. [UK Proposes Loosening Apple and Google Payment Rules](#item-10) ⭐️ 8.0/10
11. [Russia Charges Telegram Founder Durov with Aiding Terrorism](#item-11) ⭐️ 8.0/10
12. [Google DeepMind disbands Nobel-winning AlphaFold team, key members move to Anthropic](#item-12) ⭐️ 8.0/10
13. [EU Launches AI Gigafactory Tender to Mobilize €300B](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GitHub Launches Stacked Pull Requests in Public Preview](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 9.0/10

GitHub has released stacked pull requests in public preview, allowing developers to break large changes into an ordered series of smaller, dependent pull requests that can be reviewed and merged independently. This feature significantly improves developer workflow by enabling incremental code review and reducing merge conflicts, making it easier to manage complex changes. It is one of the largest launches in GitHub history, affecting nearly every service from Actions to the UI. The feature is available via the GitHub CLI with the `gh stack` extension, and users can install it from `gh.io/stacks`. However, some bugs remain, such as merging an entire stack being broken in certain cases, and squash-and-merge requiring re-approval for each PR in the stack.

hackernews · tomzorz · Jul 30, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49112232)

**Background**: Stacked pull requests are a workflow where changes are organized into a chain of dependent pull requests, each representing a logical layer of the overall change. This approach is common in large codebases to facilitate parallel review and faster iteration. GitHub's implementation integrates with existing pull request features like reviews and checks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/">Stacked pull requests are now in public preview - GitHub Changelog</a></li>
<li><a href="https://github.github.com/gh-stack/">GitHub Stacked PRs | GitHub Stacked PRs</a></li>
<li><a href="https://docs.github.com/en/pull-requests/how-tos/stacked-pull-requests">Stacked pull requests 🥞 - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: The community response is mixed: some developers are excited about the workflow improvement, while others report significant bugs, such as broken stack merging and re-approval requirements. A GitHub team member acknowledged the issues and promised more updates.

**Tags**: `#GitHub`, `#version control`, `#developer workflow`, `#pull requests`, `#software engineering`

---

<a id="item-2"></a>
## [OpenAI slashes GPT-5.6 Luna price by 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 9.0/10

OpenAI announced an 80% price reduction for GPT-5.6 Luna, its fastest and most affordable model, making it $0.10 per million input tokens and $0.60 per million output tokens. This dramatic price cut signals a new phase of price-performance improvements in AI models, enabling enterprises to deploy high-volume AI workflows at scale and making advanced AI more accessible. The price reduction applies to both Luna and Terra models, with Luna now costing 80% less. The improvements stem from kernel optimizations that reduced serving cost by 20% and experiments that increased token-generation efficiency by over 15%.

hackernews · tedsanders · Jul 30, 17:15 · [Discussion](https://news.ycombinator.com/item?id=49112867)

**Background**: GPT-5.6 is OpenAI's latest model family, including Sol (flagship), Terra (balanced), and Luna (cost-efficient). Luna was already a cheap and capable model, and this 5x price drop makes it even more attractive for high-volume tasks like deep research and multi-agent systems.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/">Advancing the price - performance frontier with GPT-5.6 | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**Discussion**: Community members expressed surprise and excitement, comparing the price drop to the dial-up to broadband transition. Some noted that while Luna is very capable, distinguishing between trivial and non-trivial tasks remains a hard problem. Others highlighted the potential for running many more parallel agents at the same cost.

**Tags**: `#AI`, `#GPT-5.6`, `#pricing`, `#OpenAI`, `#inference`

---

<a id="item-3"></a>
## [Anthropic's AI Finds Critical Flaw in NIST Post-Quantum Candidate HAWK](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic announced that its Claude Mythos Preview model discovered a serious weakness in the NIST post-quantum candidate algorithm HAWK within about 60 hours, reducing its effective key strength from 2^64 to 2^38. The attack cost approximately $100,000 in API fees and was missed by human experts for two years. This breakthrough demonstrates that AI can now outperform human cryptanalysts in discovering cryptographic weaknesses, potentially accelerating the security evaluation of post-quantum algorithms. It also underscores the urgency for organizations to adopt cryptographic agility and migrate to standardized post-quantum cryptography by federal deadlines. The attack does not run in polynomial time, so larger key sizes remain secure, and HAWK has not been publicly withdrawn. Anthropic also reported an improved attack on seven rounds of AES-128, but full AES-128 uses ten rounds, so production systems are unaffected.

telegram · zaihuapd · Jul 30, 05:47

**Background**: Post-quantum cryptography aims to develop algorithms resistant to future quantum computers that could break current encryption. NIST has been running a multi-round standardization process; HAWK was a third-round candidate for digital signatures. The White House executive order mandates federal agencies to migrate to quantum-resistant key systems by 2030 and digital signatures by 2031.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate... - Ars Technica</a></li>
<li><a href="https://www.techzine.eu/news/applications/143290/mythos-knocks-hawk-out-of-the-race-for-a-post-quantum-standard/">Mythos knocks HAWK out of the race for a post - quantum standard</a></li>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that this is a groundbreaking use of AI in cryptography, but some commenters caution that the attack is not polynomial-time and thus does not break HAWK entirely. Others debate the cost-effectiveness and whether AI will replace human cryptanalysts or serve as a tool.

**Tags**: `#AI`, `#cryptography`, `#post-quantum`, `#NIST`, `#security`

---

<a id="item-4"></a>
## [Cheap TV Streaming Sticks Pre-Infected with Malware](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) ⭐️ 8.0/10

A security article warns that many cheap TV streaming sticks, such as the H96 model, come pre-infected with malware that enables ad fraud and residential proxy botnets, posing significant privacy and security risks. This matters because millions of consumers unknowingly bring these compromised devices into their homes, allowing attackers to use their internet connections for fraudulent activities and potentially launch attacks on critical infrastructure. The malware can silently launch browsers, visit websites, click ads, and be used for residential proxy tasks, all without the user's knowledge. Major e-commerce platforms continue to sell hundreds of such models despite repeated warnings.

hackernews · speckx · Jul 30, 17:04 · [Discussion](https://news.ycombinator.com/item?id=49112744)

**Background**: Residential proxy botnets use compromised home devices to route internet traffic through real residential IP addresses, making fraudulent activity appear legitimate. Ad fraud malware generates fake clicks and impressions to steal advertising revenue. These cheap streaming sticks often run outdated Android versions with no security patches, making them easy targets.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/">Read This Before You Buy That TV Streaming Stick – Krebs on Security</a></li>
<li><a href="https://spur.us/blog/residential-proxies-the-legal-botnet-that-nobody-talks-about">Residential Proxies : The Legal Botnet Nobody Talks About</a></li>
<li><a href="https://captchafox.com/learn/residential-proxies">What Are Residential Proxies ? Bot Attacks & Detection</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration that major retailers like Amazon and Best Buy face little accountability for selling these harmful devices. Some shared personal experiences with similar products, while others noted that even incompetence in device security can lead to the same risks. A few commenters discussed building their own secure streaming devices as an alternative.

**Tags**: `#security`, `#privacy`, `#IoT`, `#botnet`, `#streaming`

---

<a id="item-5"></a>
## [DeepMind's Gemini Robotics 2 Enables Whole-Body Robot Control](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind released Gemini Robotics 2, a model that enables whole-body intelligence for humanoid robots, allowing them to perform coordinated full-body motions and advanced dexterity tasks. It also supports multi-robot coordination in shared spaces. This marks a significant step from upper-body-only control to whole-body intelligence, potentially accelerating the deployment of humanoid robots in real-world environments like homes and workplaces. The progress mirrors the rapid improvement seen in large language models, suggesting transformative applications in the near future. The system integrates a vision-language model for understanding and two vision-language-action models for full-body and hand control. Previous models only controlled the upper body for table-top tasks, while Gemini Robotics 2 expands to whole-body motions.

hackernews · ai2027 · Jul 30, 15:15 · [Discussion](https://news.ycombinator.com/item?id=49111237)

**Background**: Humanoid robots have traditionally struggled with fluid, coordinated whole-body movements due to limitations in actuators and control algorithms. DeepMind's approach leverages large foundation models (like Gemini) to generate robot actions directly from visual and language inputs, bypassing traditional programming. This work builds on earlier Gemini Robotics models that focused on upper-body manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body intelligence to robots — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/gemini-robotics/">Gemini Robotics 2</a></li>
<li><a href="https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/">Google's new Gemini Robotics 2 platform allows for 'intelligent whole-body control' - Engadget</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: a DeepMind researcher praises the lab's breadth across frontier models and robotics, while others express skepticism about current robot speed and actuator quality. Some draw parallels to early LLM progress, suggesting rapid improvement is possible.

**Tags**: `#robotics`, `#AI`, `#DeepMind`, `#Gemini`, `#whole body intelligence`

---

<a id="item-6"></a>
## [UEFA and 55 national associations threaten FIFA boycott](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/) ⭐️ 8.0/10

UEFA and its 55 national associations have issued a joint statement threatening to boycott FIFA competitions, including the World Cup, if FIFA proceeds with plans to expand the Club World Cup and introduce external investment into its tournaments. This threat signals a potential schism in global football governance, as UEFA represents the most powerful and lucrative football region. A boycott could undermine FIFA's flagship events and force a restructuring of international football's power dynamics. The statement specifically opposes FIFA's plan to expand the Club World Cup to 32 teams and the proposed creation of a new FIFA-backed international club competition. UEFA argues these moves prioritize commercial returns over the well-being of players and the sport.

hackernews · dickfickling · Jul 30, 18:40 · [Discussion](https://news.ycombinator.com/item?id=49113929)

**Background**: FIFA and UEFA have long been the two most powerful bodies in world football, but tensions have escalated over governance, competition formats, and financial control. FIFA's recent push for more frequent and larger tournaments, including a biennial World Cup proposal, has been met with strong opposition from UEFA and other confederations.

**Discussion**: Commenters largely support UEFA's stance, criticizing FIFA President Infantino for corruption and prioritizing money over the sport. Some suggest UEFA should host its own World Cup, while others warn that external investment would turn football into a business driven by shareholder returns.

**Tags**: `#sports`, `#governance`, `#FIFA`, `#UEFA`, `#boycott`

---

<a id="item-7"></a>
## [Muon Mystery Solved, Old Results Invalidated](https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/) ⭐️ 8.0/10

Physicists have resolved a long-standing muon anomaly, showing that previous experimental results were flawed and no longer align with theoretical predictions. This resolution shifts the foundation of particle physics, potentially eliminating a key hint of new physics beyond the Standard Model and redirecting future research. The Muon g-2 experiment at Fermilab measured the muon's anomalous magnetic moment, but updated lattice QCD calculations now bring theory and experiment into agreement, reducing the discrepancy from 4.2 sigma to 0.5 sigma.

hackernews · ibobev · Jul 30, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49111305)

**Background**: The muon's magnetic moment is a sensitive test of the Standard Model. A persistent discrepancy between measured and predicted values, known as the muon g-2 anomaly, had suggested possible new particles. Recent advances in lattice QCD have refined the theoretical prediction, resolving the anomaly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muon_g−2_Experiment">Muon g−2 Experiment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Muon_g-2">Muon g-2 - Wikipedia</a></li>
<li><a href="https://muon-g-2.fnal.gov/">Fermilab | Muon g-2</a></li>

</ul>
</details>

**Discussion**: Comments express relief that the long-standing problem is resolved, with one user joking about spending years on the issue. Others reflect on the philosophy of science, noting that even flawed models can be useful for predictions, and that paradigm shifts are part of progress.

**Tags**: `#physics`, `#muon`, `#particle physics`, `#scientific discovery`

---

<a id="item-8"></a>
## [Economic Benefits of AI-Assisted Refactoring](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 8.0/10

Martin Fowler published an article quantifying the economic benefits of using AI to assist in code refactoring, showing measurable improvements in token efficiency and code quality. This analysis provides grounded, quantitative evidence for AI's value in software engineering, moving beyond vague claims to specific measurements that can guide investment decisions. The article includes specific metrics on token consumption reduction and reasoning improvements when AI-assisted refactoring is applied, with real use case examples.

hackernews · javaeeeee · Jul 30, 15:10 · [Discussion](https://news.ycombinator.com/item?id=49111176)

**Background**: Refactoring is the process of restructuring existing code without changing its external behavior, often to improve readability, maintainability, or performance. AI tools like large language models can assist by suggesting or automating parts of this process, but their economic impact has been unclear.

**Discussion**: Commenters noted that best practices for programmers, often ignored, are being rediscovered for AI, and praised the article for its specific, grounded critique. Some highlighted the need for human oversight in agentic refactoring, as AI may lack understanding of the overall project context.

**Tags**: `#refactoring`, `#AI`, `#software engineering`, `#economics`, `#best practices`

---

<a id="item-9"></a>
## [GCC Steering Committee Adopts AI Contributions Policy](https://lwn.net/Articles/1086041/) ⭐️ 8.0/10

The GCC steering committee has accepted an AI contributions policy recommended by the GCC AI policy working group, establishing guidelines for handling machine-generated contributions to the GCC project. This policy sets a precedent for how major open source projects manage AI-generated code, addressing quality, copyright, and community governance concerns. It will influence similar policies in other projects and affect developers using AI tools to contribute. The policy requires disclosure of AI involvement in contributions and may restrict or require human review for machine-generated patches. The full policy text is available on the GCC forge repository.

hackernews · arto · Jul 30, 11:45 · [Discussion](https://news.ycombinator.com/item?id=49108685)

**Background**: GCC (GNU Compiler Collection) is a key open source compiler project. The steering committee, founded in 1998, makes major decisions for the project. As AI-generated code becomes common, projects need policies to ensure contribution quality and legal clarity.

<details><summary>References</summary>
<ul>
<li><a href="https://lwn.net/Articles/1086041/">GCC steering committee announces AI policy [LWN.net]</a></li>
<li><a href="https://gcc.gnu.org/steering.html">GCC steering committee - GNU Project</a></li>

</ul>
</details>

**Discussion**: Community comments show a mix of support and skepticism. Some praise the GNU project's welcoming attitude, while others note that AI companies may benefit from open source projects adopting such policies, as it keeps repositories clean for training data. A notable quote highlights concerns about AI enabling wealth to access skill without skill accessing wealth.

**Tags**: `#open source`, `#AI policy`, `#GCC`, `#community governance`, `#software engineering`

---

<a id="item-10"></a>
## [UK Proposes Loosening Apple and Google Payment Rules](https://t.me/zaihuapd/42855) ⭐️ 8.0/10

On June 30, the UK's Competition and Markets Authority (CMA) proposed allowing app developers to direct users to payment options outside Apple and Google's app stores, and potentially requiring Apple to open NFC technology for contactless payments on iOS. This proposal could significantly reduce the fees Apple and Google charge developers, foster competition in the mobile ecosystem, and set a precedent for digital market regulation globally. The CMA stated that any fees charged by Apple or Google for directing users must be fair, reasonable, and lower than current app store commissions, with savings passed to consumers or used for innovation. The proposal is part of a consultation under the UK's new Digital Markets, Competition and Consumers Act 2024.

telegram · zaihuapd · Jul 30, 02:10

**Background**: Apple and Google were designated as having 'strategic market status' in mobile ecosystems by the CMA last year, giving the regulator stronger powers to intervene. The UK's Digital Markets, Competition and Consumers Act 2024, which came into force recently, empowers the CMA to impose conduct requirements on firms with such status. NFC (Near Field Communication) technology enables contactless payments via smartphones and cards.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets,_Competition_and_Consumers_Act_2024">Digital Markets, Competition and Consumers Act 2024 - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2025/01/23/uk-probes-apple-and-google-over-mobile-ecosystem-market-power/">UK probes Apple and Google over ' mobile ecosystem ' market power</a></li>
<li><a href="https://stripe.com/resources/more/how-to-accept-contactless-nfc-payments-from-customers">What are contactless NFC payments? A guide for businesses</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#app store`, `#regulation`, `#Apple`, `#Google`

---

<a id="item-11"></a>
## [Russia Charges Telegram Founder Durov with Aiding Terrorism](https://t.me/zaihuapd/42859) ⭐️ 8.0/10

On July 29, 2026, Russia's Federal Security Service (FSB) filed criminal charges against Telegram founder Pavel Durov under Article 205.1.1.1 of the Russian Criminal Code for aiding terrorism, and placed him on an international wanted list. This unprecedented legal action against a major tech founder by a state actor could set a dangerous precedent for platform liability and free speech, potentially affecting how encrypted messaging services operate globally. The FSB alleges that Telegram's management refused to delete channels, groups, and bots used by Ukrainian intelligence and terrorist organizations to coordinate sabotage, terrorist attacks, mass killings, and cyber fraud in Russia, resulting in numerous casualties and billions of rubles in damages.

telegram · zaihuapd · Jul 30, 03:45

**Background**: Telegram is an encrypted messaging platform founded by Pavel Durov, who left Russia in 2014 after refusing to comply with government demands to block opposition groups. The platform has been criticized for hosting extremist content, but also praised for protecting user privacy. Article 205.1 of the Russian Criminal Code covers aiding terrorism and carries a potential sentence of up to life imprisonment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cj4kexqkpzno">Russia charges Telegram founder Pavel Durov with facilitating...</a></li>
<li><a href="https://www.aljazeera.com/news/2026/7/29/russia-charges-telegram-founder-pavel-durov-with-aiding-terrorism">Russia charges Telegram founder Pavel Durov with... | Al Jazeera</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pavel_Durov">Pavel Durov - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#legal`, `#terrorism`

---

<a id="item-12"></a>
## [Google DeepMind disbands Nobel-winning AlphaFold team, key members move to Anthropic](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 8.0/10

Google DeepMind has disbanded the team behind AlphaFold, the Nobel Prize-winning AI system for protein structure prediction, and reassigned most members to other projects. Three core researchers—John Jumper, Jonas Adler, and Alexander Pritzel—have left to join Anthropic, a competitor in AI safety and development. This move signals a strategic shift at DeepMind away from structural biology toward large language models and other AI frontiers, potentially slowing progress in AI-driven drug discovery. It also highlights intense talent competition among top AI labs, with Anthropic gaining key expertise. Nearly a quarter of the original AlphaFold paper authors have left the company entirely, while others were internally transferred to projects like Gemini, enzyme design, nuclear fusion, and genomics. Some moved to Isomorphic Labs, Alphabet's drug discovery spin-off.

telegram · zaihuapd · Jul 30, 07:45

**Background**: AlphaFold is an AI system developed by DeepMind that predicts protein 3D structures from amino acid sequences, achieving breakthrough accuracy in the CASP14 competition in 2020. Its creators, Demis Hassabis and John Jumper, shared the 2024 Nobel Prize in Chemistry for this work. The system has been widely used in biology and drug discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini ( language model ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AlphaFold`, `#DeepMind`, `#Anthropic`, `#AI Research`, `#Talent Movement`

---

<a id="item-13"></a>
## [EU Launches AI Gigafactory Tender to Mobilize €300B](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

The European Commission has officially launched a tender for AI gigafactories, aiming to mobilize approximately €300 billion in investment, with €10 billion from EU and member state funds. The tender supports up to seven AI gigafactories, with bids due by November 12 and winners expected by July 2027. This initiative represents a major strategic push by the EU to build sovereign AI infrastructure and compete with the US and China in advanced AI development. The gigafactories will enable training of next-generation AI models with trillions of parameters, impacting sectors like medicine, cleantech, and space. The tender covers two phases: site selection and expansion. Projects must become operational within 18 months of signing the contract. The European High Performance Computing Joint Undertaking (EuroHPC JU) is overseeing the initiative.

telegram · zaihuapd · Jul 30, 11:50

**Background**: AI gigafactories are large-scale facilities dedicated to developing and training very large AI models, requiring extensive computing infrastructure. The EU has committed to establishing four to five such facilities, with the European Investment Bank also supporting financing. This effort aims to reduce European dependence on non-EU data centers and AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eurohpc-ju.europa.eu/ai-gigafactories_en">AI Gigafactories - The European High Performance Computing Joint Undertaking (EuroHPC JU)</a></li>
<li><a href="https://www.eib.org/en/press/all/2025-491-eib-group-and-european-commission-join-forces-to-finance-ai-gigafactories">EIB Group and European Commission join forces to finance AI gigafactories</a></li>
<li><a href="https://www.polytechnique-insights.com/en/columns/digital/european-ai-gigafactories-the-true-the-false-and-the-uncertain/">European AI gigafactories: the true, the false and the uncertain</a></li>

</ul>
</details>

**Tags**: `#AI`, `#EU`, `#infrastructure`, `#investment`, `#policy`

---