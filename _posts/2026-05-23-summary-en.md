---
layout: default
title: "Horizon Summary: 2026-05-23 (EN)"
date: 2026-05-23
lang: en
---

> From 23 items, 7 important content pieces were selected

---

1. [80386 Microcode Disassembled](#item-1) ⭐️ 9.0/10
2. [Anthropic's Project Glasswing: AI Finds 10K+ Critical Vulnerabilities](#item-2) ⭐️ 9.0/10
3. [Apple Open-Sources corecrypto with Formal Verification of Quantum-Safe Algorithms](#item-3) ⭐️ 9.0/10
4. [SpaceX Starship v3 Test Flight Achieves Key Milestones](#item-4) ⭐️ 8.0/10
5. [Microsoft Widely Deploys Claude Code, Encourages Non-Tech Staff](#item-5) ⭐️ 8.0/10
6. [Microsoft reveals OpenAI's $11.5B quarterly loss](#item-6) ⭐️ 8.0/10
7. [China Fines Futu $2.7B, Tiger $560M for Illegal Securities](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [80386 Microcode Disassembled](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 9.0/10

A detailed disassembly and analysis of the Intel 80386 microprocessor's microcode has been published, revealing how complex x86 instructions were implemented at the microarchitectural level. This reverse engineering achievement demystifies the inner workings of a classic processor, providing valuable insights for computer architecture education and historical preservation. The microcode was extracted from high-resolution die images using AI-assisted techniques, and the disassembly covers the complete microcode ROM of the 80386.

hackernews · nand2mario · May 23, 12:11 · [Discussion](https://news.ycombinator.com/item?id=48247004)

**Background**: Microcode is a layer of low-level instructions that control the internal operations of a CPU, translating complex machine instructions into simpler micro-operations. The 80386, introduced in 1985, was Intel's first 32-bit x86 processor and used microcode to implement many of its instructions. Reverse engineering microcode is challenging because manufacturers keep it proprietary and often encrypt or sign updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=48247004">80386 Microcode Disassembled | Hacker News</a></li>
<li><a href="https://www.altusintel.com/public-yyr4pw/?tt=1779562264">I386 Microcode Disassembly Results Published | Altus Intel</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed admiration for the technical achievement, with users noting the difficulty of black-box analysis and the historical value of understanding older processors. Some comments discussed the process of extracting microcode from die images, while others recommended resources on microprogramming.

**Tags**: `#reverse engineering`, `#microcode`, `#80386`, `#computer architecture`, `#hardware`

---

<a id="item-2"></a>
## [Anthropic's Project Glasswing: AI Finds 10K+ Critical Vulnerabilities](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic announced initial results from Project Glasswing, where its Claude Mythos Preview model discovered over 10,000 high-severity vulnerabilities in critical software within a month, with a 90.6% true positive rate on reviewed findings. This demonstrates that AI can now discover vulnerabilities at a scale and speed that far outpaces human verification and patching, shifting the bottleneck from discovery to remediation and forcing the software industry to accelerate patch cycles. The project scanned thousands of open-source projects, finding 6,202 high-severity vulnerabilities, and partners like Cloudflare reported a 10x improvement in vulnerability discovery rate. Anthropic also released Claude Security, a tool to help enterprises fix vulnerabilities.

telegram · zaihuapd · May 23, 03:16

**Background**: Project Glasswing is an industry-wide cybersecurity initiative launched by Anthropic in April 2026, using the Claude Mythos Preview model to proactively find and fix vulnerabilities in critical open-source software. The model is not publicly available and is used by a consortium of companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://claude.com/product/claude-security">Claude Security | Claude by Anthropic</a></li>

</ul>
</details>

**Discussion**: The discussion highlights concerns about vulnerability fatigue and the strain on open-source maintainers, who are already overwhelmed by the volume of reports. Some argue that AI-driven discovery without corresponding automation in patching could worsen the problem.

**Tags**: `#AI`, `#cybersecurity`, `#vulnerability discovery`, `#Anthropic`, `#open source`

---

<a id="item-3"></a>
## [Apple Open-Sources corecrypto with Formal Verification of Quantum-Safe Algorithms](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

Apple has open-sourced its corecrypto cryptographic library on GitHub, including implementations of the post-quantum algorithms ML-KEM and ML-DSA, along with formal verification proofs that mathematically guarantee their correctness against NIST standards. This marks a major step in cryptographic assurance, as formal verification provides mathematically rigorous guarantees that the code is correct, which is critical for the billions of Apple devices relying on corecrypto for security. It also sets a new precedent for transparency and trust in post-quantum cryptography deployment. The formal verification was performed using the Isabelle proof assistant, with over 200,000 lines of proof script verifying 7,500 lines of C code. Apple also released custom verification tools and Isabelle theory libraries for independent review.

telegram · zaihuapd · May 23, 04:49

**Background**: Post-quantum cryptography aims to secure systems against future quantum computers that could break current public-key algorithms. ML-KEM (FIPS 203) and ML-DSA (FIPS 204) are NIST-standardized algorithms for key encapsulation and digital signatures, respectively. Formal verification uses mathematical proofs to ensure software correctly implements a specification, offering stronger guarantees than testing alone.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/formal-verification-corecrypto/">A blueprint for formal verification of Apple corecrypto</a></li>
<li><a href="https://github.com/apple/corecrypto">GitHub - apple/corecrypto: Apple corecrypto</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#formal verification`, `#open source`, `#Apple`

---

<a id="item-4"></a>
## [SpaceX Starship v3 Test Flight Achieves Key Milestones](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 8.0/10

SpaceX launched the Starship v3 megarocket on its first test flight, successfully achieving stage separation and a controlled landing of the Starship upper stage despite booster engine failures during boost-back and landing burns. This test flight demonstrates significant progress in Starship's heat shield technology and rapid iterative development, bringing SpaceX closer to fully reusable orbital launch capability that could drastically reduce space access costs. The booster experienced one engine failure during ascent and all engines failed during the boost-back burn, though some relit for landing but resulted in a hard, off-target water impact; the Starship upper stage lost one engine but still executed a precise on-target landing.

hackernews · busymom0 · May 22, 23:41 · [Discussion](https://news.ycombinator.com/item?id=48242959)

**Background**: Starship is a two-stage fully reusable super heavy-lift launch vehicle under development by SpaceX, powered by Raptor engines burning liquid methane and liquid oxygen. The v3 version incorporates numerous upgrades, particularly to its heat shield, which must withstand temperatures over 1500°C during reentry. Rapid iteration — building, testing, learning, and improving — is a core development philosophy at SpaceX.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/space/2025/08/spacex-got-good-heat-shield-data-for-starship-so-what-comes-next/">Starship’s heat shield appears to have performed quite well in test - Ars Technica</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacexs-starship-v3-megarocket-will-do-something-completely-new-on-flight-12-take-a-good-look-at-itself">SpaceX's Starship V3 megarocket will do something completely new on Flight 12 — take a good look at itself | Space</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the heat shield performance, noting no visible hot spots or burn-through compared to previous flights. They also highlighted the guidance system's success in landing the ship precisely despite engine issues, though the booster's failure was seen as a setback. The overall sentiment was positive, appreciating SpaceX's 'good enough' rapid iteration approach.

**Tags**: `#spacex`, `#starship`, `#rocket launch`, `#space exploration`, `#engineering`

---

<a id="item-5"></a>
## [Microsoft Widely Deploys Claude Code, Encourages Non-Tech Staff](https://t.me/zaihuapd/41535) ⭐️ 8.0/10

Microsoft is widely deploying Anthropic's Claude Code across key engineering teams, including the CoreAI team and the Experiences & Devices division responsible for Windows, Microsoft 365, and Outlook, and is encouraging non-technical employees to use it for prototyping. Software engineers are now required to use both Claude Code and GitHub Copilot and provide comparative feedback. This move signals a major shift in how AI-assisted coding tools are being adopted within a tech giant, potentially influencing industry-wide practices. By requiring engineers to compare Claude Code with GitHub Copilot, Microsoft is directly evaluating competing AI coding assistants, which could shape future product integrations and partnerships. Claude Code is an AI coding agent developed by Anthropic that runs directly in the IDE and provides code suggestions and visual diffs. Microsoft's push includes non-technical staff, indicating the tool's low barrier to entry for prototyping.

telegram · zaihuapd · May 23, 06:05

**Background**: Claude Code is a series of large language models by Anthropic, trained using constitutional AI for ethical compliance. GitHub Copilot, developed by GitHub and OpenAI, is a widely used AI code completion tool that integrates with popular IDEs. Microsoft owns GitHub and has a close partnership with OpenAI, making its internal adoption of a competitor's tool noteworthy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#Microsoft`, `#Claude Code`, `#GitHub Copilot`, `#software engineering`

---

<a id="item-6"></a>
## [Microsoft reveals OpenAI's $11.5B quarterly loss](https://t.me/zaihuapd/41537) ⭐️ 8.0/10

Microsoft's latest earnings report disclosed that its equity method investment in OpenAI resulted in a $3.1 billion reduction in net profit for the quarter, implying OpenAI incurred a net loss of approximately $11.5 billion in that period. This disclosure highlights the enormous cost of developing advanced AI, raising questions about the sustainability of such investments and the financial health of leading AI companies like OpenAI. Based on Microsoft's roughly 27% stake in OpenAI, the implied quarterly loss is about $11.5 billion; using a pre-tax loss and actual ownership of 32.5%, the loss could exceed $12 billion. This loss is nearly three times OpenAI's $4.3 billion revenue in the first half of the year.

telegram · zaihuapd · May 23, 07:40

**Background**: Equity method accounting requires investors to recognize their share of the investee's profits or losses in their own financial statements, even if no dividends are paid. Microsoft has invested $11.6 billion in OpenAI so far, representing the majority of its $13 billion committed investment. OpenAI's massive losses reflect the high costs of training and running large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.mbalib.com/wiki/权益法">权益法 - MBA智库百科</a></li>
<li><a href="https://baike.baidu.com/item/长期股权投资权益法/9073814">长期股权投资权益法_百度百科</a></li>
<li><a href="https://wallstreetcn.com/articles/3769250">网传 OpenAI “ 股 权 结 构 表”：微软“130亿美元投资”已升至“2283亿美元”</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Microsoft`, `#AI Economics`, `#Financial Report`, `#Investment`

---

<a id="item-7"></a>
## [China Fines Futu $2.7B, Tiger $560M for Illegal Securities](https://t.me/zaihuapd/41539) ⭐️ 8.0/10

Chinese regulators proposed fines of 18.5 billion yuan ($2.7 billion) against Futu Holdings and 4.112 billion yuan ($560 million) against Tiger Brokers' subsidiaries for unauthorized cross-border securities operations in mainland China. This landmark penalty signals a major crackdown on unlicensed cross-border securities activities, potentially reshaping the fintech landscape and affecting millions of Chinese investors using offshore trading platforms. Futu's CEO Li Hua also faces a personal fine of 1.25 million yuan. Both companies have reduced mainland client assets to below 13% of total, and the fines are subject to final determination after procedural steps.

telegram · zaihuapd · May 23, 10:58

**Background**: Futu Holdings and Tiger Brokers are Hong Kong-based online brokerages popular among mainland Chinese investors for trading US and Hong Kong stocks. Chinese securities law requires firms to obtain licenses to solicit or serve mainland clients, which these companies allegedly did without proper authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.guancha.cn/GuanJinRong/2026_05_22_818074.shtml">证 监 会 拟 罚 款金额公布：富途被 罚 18.5亿，老虎被 罚 4.112亿</a></li>
<li><a href="https://www.21jingji.com/article/20260523/herald/e7eb58bb6994d891f986fd9d06c85b1d.html">中国 证 监 会拟对 富 途 罚款18.5亿， 老 虎 证 券 罚没4.112亿 - 21经济网</a></li>

</ul>
</details>

**Tags**: `#regulatory`, `#fintech`, `#China`, `#securities`, `#penalty`

---