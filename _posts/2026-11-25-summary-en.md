---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 23 items, 10 important content pieces were selected

---

1. [Anthropic claims internal Claude discovered VP≠VNP with Lean 4 proof](#item-1) ⭐️ 10.0/10
2. [OpenAI-linked preprint claims matrix multiplication exponent is exactly 9/4](#item-2) ⭐️ 9.0/10
3. [Anthropic Prices IPO at $83 Per Share, Valued for Nasdaq Debut](#item-3) ⭐️ 9.0/10
4. [Ternary Bonsai 2.5 27B: A 5.9GB Quantized Model for Local Agentic Coding](#item-4) ⭐️ 8.0/10
5. [GPT-6.2 designs protein minibinders from 3D structures without specialized AI models](#item-5) ⭐️ 8.0/10
6. [Check Point management servers hit by PRNG-based session forgery attack](#item-6) ⭐️ 8.0/10
7. [GTA 6 Runs on Windows via Xbox Compatibility Layer](#item-7) ⭐️ 8.0/10
8. [GPT-6.2 Astra Solves 1808 Sketchbook Mystery in 22 Minutes](#item-8) ⭐️ 8.0/10
9. [Huawei and Qualcomm sign broad multi-year patent deal covering 5G and AI](#item-9) ⭐️ 8.0/10
10. [VMware vCenter Hit by Another 9.8 Authentication Bypass, Exploited as Zero-Day](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic claims internal Claude discovered VP≠VNP with Lean 4 proof](https://t.me/zaihuapd/45345) ⭐️ 10.0/10

On November 24, Anthropic reportedly published a paper titled "VP ≠ VNP over every field" along with a Lean 4 formal proof, claiming that an internal research version of Claude discovered the result. The paper presents a superpolynomial arithmetic circuit lower bound for the Hamiltonian cycle polynomial, implying that VP is a proper subclass of VNP and thus resolving Valiant's 1979 algebraic complexity conjecture if verified. If genuine, this would be a landmark result in complexity theory, resolving a long-standing open problem and demonstrating that AI can contribute to frontier mathematical discovery. It would also highlight the growing role of formal verification tools like Lean 4 in certifying advanced mathematical proofs. The result is limited to arithmetic circuits and does not address the P vs NP problem; the paper and code were reportedly written by AI, and the proof underwent auditing against three standard axioms and an independent kernel check. Independent verification by the mathematical community is still needed given the extraordinary nature of the claim.

telegram · zaihuapd · Nov 24, 12:18

**Background**: In algebraic complexity theory, VP and VNP are algebraic analogs of P and NP, introduced by Leslie Valiant in 1979. The VP vs VNP problem asks whether every polynomial family computable by polynomial-size arithmetic circuits (VP) is also in VNP, the class of polynomials with succinct certificates; it is a major open question. Lean 4 is an interactive theorem prover that allows formal verification of mathematical proofs, ensuring correctness down to the axioms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity">Arithmetic circuit complexity - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#complexity-theory`, `#AI-for-math`, `#Lean4`, `#formal-verification`, `#Anthropic`

---

<a id="item-2"></a>
## [OpenAI-linked preprint claims matrix multiplication exponent is exactly 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

A preprint hosted on OpenAI's GitHub claims that the matrix multiplication exponent is exactly 9/4 over every field, meaning multiplying two n×n matrices requires Θ(n^2.25) operations. The paper is reportedly produced by an unreleased OpenAI model and is part of a set of four papers resolving eight problems from a Top 500 open problems in mathematics list. If verified, this would settle a decades-old question about the fundamental complexity of matrix multiplication, a core operation in scientific computing and machine learning. It also highlights the growing role of AI models in producing advanced mathematical research and raises questions about transparency and institutional science. The result establishes a lower bound of Ω(n^2.25), while the upper bound of 2.25 was already known; an algorithm achieving O(n^2.25) was recently published but is far from practical. The paper is attributed to an unreleased model whose recipe is not disclosed, and the title has been corrected from O(n^2.25) to Θ(n^2.25).

hackernews · E-Reverance · Nov 25, 01:19 · [Discussion](https://news.ycombinator.com/item?id=50637220)

**Background**: The matrix multiplication exponent, denoted ω, is the smallest number such that any two n×n matrices can be multiplied using n^(ω+o(1)) field operations. Schoolbook multiplication uses n^3 operations, and decades of research have lowered the best known upper bound to about 2.37, while lower bounds remained much weaker. This preprint claims to pin down the exact value as 9/4, which would be a major breakthrough in algebraic complexity theory.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm">Matrix multiplication algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers">OpenAI bulk release of mathematical papers - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated the implications for AI research and model secrecy, with some suggesting OpenAI may be holding back top models to achieve breakthroughs in a compounding loop. Others noted the title error (O vs Θ) and clarified that the paper proves a lower bound of Ω(n^2.25), not an upper bound, and compared the current AI-driven research wave to Bell Labs while questioning the lack of public benefit.

**Tags**: `#matrix-multiplication`, `#AI-for-math`, `#OpenAI`, `#algorithms`, `#research-breakthrough`

---

<a id="item-3"></a>
## [Anthropic Prices IPO at $83 Per Share, Valued for Nasdaq Debut](https://t.me/zaihuapd/45347) ⭐️ 9.0/10

Anthropic has priced its initial public offering at $83 per share, offering 980 million Class A common shares—about 956 million sold by the company and roughly 23.65 million by existing shareholders. Trading is expected to begin on November 19, 2026, on the Nasdaq Global Select Market under the ticker ANT, with the offering closing on November 20. This is one of the largest AI company IPOs to date, giving Anthropic a massive public-market war chest to compete with OpenAI and other frontier labs. It also provides a rare public valuation benchmark for the AI sector and will be closely watched by investors, competitors, and regulators. The company will not receive proceeds from shares sold by existing shareholders, and underwriters have a 30-day option to purchase up to an additional 147 million shares (a greenshoe/over-allotment option). The offering uses a dual-class structure, with Class A shares typically carrying one vote per share while founders and insiders likely retain superior voting rights through Class B shares.

telegram · zaihuapd · Nov 24, 13:52

**Background**: An IPO is the process by which a private company first sells shares to the public and lists on a stock exchange. The Nasdaq Global Select Market is Nasdaq's top-tier listing segment, home to many major technology companies. A greenshoe option lets underwriters buy extra shares to stabilize the price after listing, while dual-class share structures are common among tech firms that want founders to retain control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nasdaq_Global_Select_Market">Nasdaq Global Select Market</a></li>
<li><a href="https://www.euromoney.com/article/27bjsstsqxhkmh1znxfls/opinion/this-is-how-an-ipo-greenshoe-works/">This is how an IPO greenshoe works - Euromoney</a></li>
<li><a href="https://www.investopedia.com/ask/answers/062215/what-difference-between-class-shares-and-other-common-shares-companys-stock.asp">Class A vs. Class B Shares: Key Voting and Pricing Differences Class A vs. Class B Shares: Key Differences | StartEngine Class A vs Class B Shares: What's Actually Different (Quick ... Class A vs Class B Shares: Differences, Voting Rights ... What Is the Difference Between Class A, Class B, and Class C ... Understanding Class A Shares: Comparison With Class B and C ... Class A vs Class B vs Class C Shares, Explained - SoFi</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#public markets`, `#Nasdaq`

---

<a id="item-4"></a>
## [Ternary Bonsai 2.5 27B: A 5.9GB Quantized Model for Local Agentic Coding](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML released Ternary Bonsai 2.5 27B, a ternary-quantized model derived from Qwen3.8-27B that fits in a 5.9 GB footprint and delivers stronger agentic coding, multi-turn tool use, and multi-step task execution. Community members report running it locally on a Mac Mini M5 Pro with 24GB RAM at 22-25 tokens/s and easily fitting 128k context in memory. This model demonstrates that extremely low-bit quantization can bring frontier-like coding and agentic capabilities to consumer hardware, potentially democratizing local AI development. It also fuels the debate on whether small models are genuinely catching up or simply benefiting from benchmark overfitting and moving targets. The model keeps the hybrid-attention architecture of Qwen3.8-27B unchanged and uses ternary weights (-1, 0, +1), which drastically reduces memory and compute requirements. Community benchmarks show it matches Opus 4.6 on SWE-bench Verified, but skeptics note that SWE-bench Verified may not be fully representative and that direct comparisons with equivalently small models like Qwen3.8 Q1/Q2 quants are needed.

hackernews · b0m · Nov 24, 20:08 · [Discussion](https://news.ycombinator.com/item?id=50633922)

**Background**: Ternary quantization restricts model weights to three values (-1, 0, +1), dramatically shrinking model size and enabling efficient local inference. SWE-bench Verified is a benchmark that evaluates LLMs on resolving real-world GitHub issues, often used as a proxy for coding and agentic ability. PrismML's Bonsai family applies this technique to large models, aiming to make them runnable on modest hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs.prismml.com</a></li>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B: Powering ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the local performance, with one reporting 22-25 tokens/s on a Mac Mini and another noting a 29% reduction in task completion time versus Bonsai 2. The discussion also includes skepticism about benchmark validity, with calls for direct comparisons to similarly sized quantized models and speculation that the results reflect a mix of benchmark overfitting, benchmark evolution, and genuine progress in small models.

**Tags**: `#LLM`, `#quantization`, `#local-inference`, `#SWE-bench`, `#small-models`

---

<a id="item-5"></a>
## [GPT-6.2 designs protein minibinders from 3D structures without specialized AI models](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI reports that GPT-6.2 can design protein minibinders from 3D structures without using specialized protein AI models, as described in a preprint titled 'GPT-6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models'. The model wrote code to generate three-dimensional designs for minibinders targeting five proteins, though it relied on specialized tools like SolubleMPNN for sequence generation. This demonstrates that general-purpose LLMs can act as a glue layer in complex scientific workflows, potentially lowering the barrier to protein design by reducing reliance on multiple specialized models. It signals a growing trend of LLMs being applied to AI-for-science tasks, which could accelerate research in drug discovery and biotechnology. While GPT-6.2 generated the 3D designs, it still required SolubleMPNN to suggest amino acid sequences and other specialized models to select candidates predicted to fold and bind correctly. The community notes that the 'beyond specialized models' claim may be premature, as the model primarily orchestrated existing tools rather than replacing them entirely.

hackernews · acossta · Nov 24, 21:02 · [Discussion](https://news.ycombinator.com/item?id=50634658)

**Background**: Protein design involves creating new proteins with specific functions, such as minibinders—small, stable proteins that bind to targets. Traditionally, this requires specialized AI models like RFdiffusion for structure generation and ProteinMPNN for sequence design. GPT-6 is a general-purpose LLM that can write code, and this work explores its ability to perform protein design tasks without domain-specific models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein-design ... - OpenAI</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56369-w">De novo design of protein minibinder agonists of TLR3 - Nature</a></li>
<li><a href="https://www.nature.com/articles/s41587-023-02115-w">Generative models for protein structures and sequences</a></li>

</ul>
</details>

**Discussion**: Commenters largely question the 'beyond specialized models' framing, noting that GPT-6.2 still relied on SolubleMPNN for sequence generation and other specialized tools for candidate selection. Some see GPT as a valuable 'glue layer' between specialized models, while others criticize the lack of wet-lab validation and debate whether the model truly designed proteins or just orchestrated existing tools.

**Tags**: `#protein-design`, `#LLM`, `#AI-for-science`, `#GPT-6`, `#specialized-models`

---

<a id="item-6"></a>
## [Check Point management servers hit by PRNG-based session forgery attack](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise reported an active intrusion campaign against Check Point Security Management servers, where attackers exploited the HFS loginSrp1 endpoint to collect Math.random() outputs, reconstructed the V8 PRNG state, recovered the session-cookie signing key, and forged admin session cookies. The campaign has compromised servers at 22+ organizations, exposing firewall rules and stored credentials. This attack demonstrates a novel and practical PRNG state-recovery technique that undermines session security in widely used Node.js applications, potentially affecting many other systems that rely on Math.random() for security-sensitive values. It highlights the growing risk of AI-assisted cyberattacks and the need for cryptographically secure randomness in authentication mechanisms. The attacker performed successive logins to the HFS loginSrp1 endpoint, each returning a signed session cookie with a 'sid' derived from Math.random(), and collected enough outputs to reconstruct the internal state of the V8 PRNG. This allowed recovery of the session-cookie signing key and forgery of an admin session cookie; the initial access vector is suspected to be CVE-2026-16232, and the campaign is described as AI-assisted.

hackernews · louiereederson · Nov 24, 16:32 · [Discussion](https://news.ycombinator.com/item?id=50630594)

**Background**: Check Point Security Management servers are central consoles for configuring and monitoring Check Point firewalls and security policies. Node.js uses the V8 JavaScript engine, whose Math.random() is a non-cryptographic pseudorandom number generator (PRNG) that can be predicted if enough output is observed. Session cookies are small pieces of data used to maintain user state; if an attacker can forge a valid admin session cookie, they can bypass authentication and gain administrative access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security...</a></li>
<li><a href="https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/">Check Point Security Management Servers Hacked - SecurityWeek</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/">Hackers compromise Check Point Servers in 22 organizations</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that this is only the beginning of LLM-driven cyberattacks, with sophisticated actors and soon many criminals using AI to attack any online service. Some questioned why Math.random() isn't made secure by default, while others debated the initial access vector and whether all affected organizations had their management servers exposed to the internet.

**Tags**: `#security`, `#vulnerability`, `#PRNG`, `#Node.js`, `#cyberattack`

---

<a id="item-7"></a>
## [GTA 6 Runs on Windows via Xbox Compatibility Layer](https://twitter.com/raul_bs3/status/2125213756238291075) ⭐️ 8.0/10

A Twitter post shows Grand Theft Auto VI running on Windows, achieved by reverse-engineering the leaked Xbox Series X|S build (Build 1.0.2.1) using a Wine-like compatibility layer called Zenith-X, with the game booting in an OS window titled 'Americas'. This marks a significant milestone in game preservation and reverse engineering, demonstrating that modern console exclusives can be made playable on PC through community efforts, potentially pressuring Rockstar to accelerate an official PC port and raising legal questions about leaked builds. The Xbox build lacks DRM or obfuscation, and because Xbox Series consoles share x64 architecture and Windows heritage with PCs, the game's code executes directly without CPU emulation; projects like XCL and VIctory must still reverse-engineer clean-room shims for Xbox system services such as kernelx.dll, XGameRuntime, and d3d12_xs.dll.

hackernews · andrem · Nov 24, 13:19 · [Discussion](https://news.ycombinator.com/item?id=50627783)

**Background**: The Xbox version of GTA 6 was leaked by a hacker named CyberLeek, first as resources and later as the full game binary, including a 209GB torrent with RAGE engine files. Modern Xbox consoles are essentially Windows PCs with extra Xbox-specific libraries, so running console games on Windows mainly requires compatibility layers that substitute for missing console APIs, similar to how Wine and Proton work for Windows games on Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techspot.com/news/114672-gta-6-leaker-releases-xbox-build-executable-modders.html">GTA 6 leaker releases Xbox build executable, and modders say ...</a></li>
<li><a href="https://www.opensourceprojects.dev/post/xcl">Xbox Series X|S games running natively on Windows, no CPU ...</a></li>
<li><a href="https://www.gamespot.com/articles/gta-6-hacker-releases-full-xbox-build-and-pc-modders-are-already-trying-to-get-it-running/">GTA 6 Hacker Releases Full Xbox Build, And PC Modders Are ... GTA 6 Xbox Leak Sparks Windows Emulation Efforts: ScarlettX ... Alleged GTA 6 Xbox Executable Leak: No Playable Windows Port ... Trinitron — GTA 6 PC Native Port & Zenith-X Compatibility Tracker GTA 6 Leaker Releases All Files for Alleged Xbox Build of Game</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the leak's lack of DRM and the Xbox's PC-like architecture made this feasible, while others debated the legal and ethical implications, noting previous GitHub bans and concerns that such efforts could push developers toward cloud-based components to prevent decompilation.

**Tags**: `#reverse-engineering`, `#game-preservation`, `#compatibility-layers`, `#GTA-6`, `#Xbox`

---

<a id="item-8"></a>
## [GPT-6.2 Astra Solves 1808 Sketchbook Mystery in 22 Minutes](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 8.0/10

Historian Mark Humphries reported that GPT-6.2 Astra, with minimal prompting, autonomously identified the creator of an anonymous 1808 sketchbook held at Yale's Beinecke Library in just 22 minutes using public sources. The model found a diary reference to a visit by the vicomte de Chabot and predicted that Chabot's travel journal would confirm the attribution, which it did, leading to a significant historical find. This case study demonstrates that agentic AI can autonomously conduct primary-source historical research, potentially transforming how historians and scholars approach archival work. It raises questions about the role of human expertise in research and could accelerate discoveries in fields reliant on archival evidence. Astra located a little-known source in a paper archive and correctly hypothesized that the vicomte de Chabot's journal, available only by order from Cleveland State University, would confirm the sketchbook's authorship. Humphries notes that while historians may face a crisis of confidence similar to mathematics, the impact will likely be milder because history involves reinterpretation rather than chasing universal truth.

rss · Simon Willison · Nov 24, 16:53

**Background**: GPT-6.2 Astra is a frontier large language model released by OpenAI on November 17, 2026, alongside the more efficient GPT-6.2 Sol. The Beinecke Rare Book and Manuscript Library at Yale University is a major repository of rare books and manuscripts. The sketchbook in question is a digitized item from its collections, and the vicomte de Chabot was a French nobleman whose travels are documented in a journal held at Cleveland State University.

<details><summary>References</summary>
<ul>
<li><a href="https://beinecke.library.yale.edu/">Beinecke Library | Yale Library</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.2_Astra">GPT-6.2 Astra</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#historical research`, `#GPT-6.2`, `#case study`, `#automation`

---

<a id="item-9"></a>
## [Huawei and Qualcomm sign broad multi-year patent deal covering 5G and AI](https://t.me/zaihuapd/45344) ⭐️ 8.0/10

Huawei and Qualcomm announced a multi-year, broad patent cross-licensing agreement covering 5G, computing, AI, and networking, under which Qualcomm will purchase certain Huawei U.S. patents and license Huawei's logic folding chip manufacturing technology. The deal, expected to close after regulatory approval, brings Huawei's cumulative expected contract value from patent licenses to over $6.9 billion. This is a landmark deal between two major wireless technology players, potentially reducing litigation risk and fostering collaboration in 5G and AI. It also marks a significant milestone for Huawei's IP licensing business, which has been generating positive revenue since 2021, and could reshape the tech IP landscape. The agreement includes Qualcomm's purchase of certain Huawei U.S. patents in the same fields and a license to Huawei's logic folding chip manufacturing technology, which aims to compensate for less capable individual chips through system architecture. The transaction is subject to regulatory approval and values Huawei's cumulative patent licensing contracts at over $6.9 billion.

telegram · zaihuapd · Nov 24, 11:38

**Background**: A patent cross-licensing agreement allows two companies to use each other's patented technologies without fear of infringement lawsuits, often settling disputes and enabling freedom to operate. Logic folding is a chip design approach that stacks or folds logic circuits to improve performance without relying solely on shrinking transistors, which is becoming harder as Moore's Law slows. Huawei has been developing this technology as an alternative path to advanced chips amid manufacturing constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://qz.com/huawei-qualcomm-patent-license-deal-100526">Huawei and Qualcomm sign broad multi-year patent license deal</a></li>
<li><a href="https://www.remio.ai/post/huawei-returns-to-flagship-chips-but-logic-folding-faces-its-real-test">Huawei Returns to Flagship Chips , but Logic Folding Faces Its Real...</a></li>
<li><a href="https://www.patsnap.com/resources/blog/freedom-to-operate-search-to-avoid-patent-infringement/">Freedom to operate search to avoid patent infringement | Patsnap</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Qualcomm`, `#patent licensing`, `#5G`, `#AI`

---

<a id="item-10"></a>
## [VMware vCenter Hit by Another 9.8 Authentication Bypass, Exploited as Zero-Day](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) ⭐️ 8.0/10

Broadcom patched 23 VMware vulnerabilities, including a critical 9.8-rated authentication bypass in vCenter's directory service (CVE-2026-123903) that was exploited as a zero-day just days earlier. The flaw allows anyone with network access to vCenter to bypass authentication and gain unauthorized access. This is a critical unauthenticated authentication bypass in a core enterprise virtualization management component, and its active exploitation as a zero-day means organizations are already at risk. It affects any business running VMware vCenter, potentially exposing entire virtual infrastructures to takeover. The vulnerability is an authentication bypass using an alternate path or channel (CWE-288) in the VMware Directory Service, with a CVSS score of 9.8. Broadcom has not listed any workarounds, and this is the second directory service bypass patched within days, following CVE-2026-123890 which CISA added to its Known Exploited Vulnerabilities catalog.

telegram · zaihuapd · Nov 24, 14:50

**Background**: VMware vCenter is a centralized management platform for VMware vSphere virtual infrastructures, and its directory service (vmdir) handles authentication for the platform. An authentication bypass means an attacker can skip login checks entirely and access the system without valid credentials. Zero-day exploitation refers to attacks that occur before a patch is publicly available, giving defenders no time to prepare.

<details><summary>References</summary>
<ul>
<li><a href="https://computingforgeeks.com/vmware-vcenter-cve-2026-123890/">CVE-2026-123890: Fixed vCenter Builds per Branch ...</a></li>
<li><a href="https://securityonline.info/cve-watchtower/cve-2026-123903/">CVE-2026-123903: VMware vCenter, CVSS 9.8</a></li>
<li><a href="https://www.rapid7.com/blog/post/etr-cve-2026-123890-critical-authentication-bypass-vmware-vcenter/">CVE-2026-123890: Critical Authentication Bypass in VMware vCenter</a></li>

</ul>
</details>

**Tags**: `#security`, `#vmware`, `#vcenter`, `#vulnerability`, `#zero-day`

---