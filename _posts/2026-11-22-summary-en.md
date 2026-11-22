---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 24 items, 5 important content pieces were selected

---

1. [Lean formalization claims to verify Riemann Hypothesis](#item-1) ⭐️ 9.0/10
2. [Zhejiang University achieves first real-machine QRAM on superconducting chip](#item-2) ⭐️ 9.0/10
3. [GPGME Double-Free Vulnerability Disclosed, Affecting Versions Before 2.3.0](#item-3) ⭐️ 8.0/10
4. [Microsoft enables multi-PC AI model sharing via RDMA over USB4 on Windows](#item-4) ⭐️ 8.0/10
5. [Oral RAS(ON) inhibitor daraxonrasib shows 60.7% response in first-line pancreatic cancer](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Lean formalization claims to verify Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

Anthropic mathematician Levent Alpöge announced on November 20 that he used Claude to produce a Lean-encoded proof of the Riemann Hypothesis, including the Generalized Riemann Hypothesis, with a detailed manuscript exceeding 250,000 pages. If validated, this would be a paradigm-shifting result in mathematics, resolving a 165-year-old Millennium Prize Problem and demonstrating that AI-assisted formal verification can tackle the deepest open questions. The proof relies on the Lean theorem prover and its kernel for correctness, but independent verification is complicated by the possibility of bugs across multiple checkers and the massive scale of the formalization.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**Background**: The Riemann Hypothesis, proposed by Bernhard Riemann in 1859, concerns the distribution of prime numbers and is one of the most famous unsolved problems in mathematics. Formal verification involves encoding a mathematical proof in a language like Lean so that a computer can check every logical step, providing high confidence in correctness. The Generalized Riemann Hypothesis extends the conjecture to a broader class of functions called L-functions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>
<li><a href="https://4m4.it/posts/when-the-proof-checker-becomes-part-of-the-experiment/index.html">When the Proof Checker Becomes Part of the Experiment – Random...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the reliability of the proof, noting that while multiple independent checkers with consistency proofs make a bug-induced false proof unlikely, past incidents like a fake Collatz refutation show checkers are not perfectly independent. Some praised Levent Alpöge's skill in eliciting the proof from Claude, and others highlighted the massive formalization of modern mathematics as a major result in itself.

**Tags**: `#Lean`, `#Riemann Hypothesis`, `#formal verification`, `#mathematics`, `#AI-assisted proof`

---

<a id="item-2"></a>
## [Zhejiang University achieves first real-machine QRAM on superconducting chip](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

A Zhejiang University team demonstrated the world's first real-machine implementation of quantum random access memory (QRAM) on its self-fabricated superconducting quantum chip 'Tianmu-2', running prototypes that retrieved 4-bit and 8-bit data with 80.9% and 60.4% accuracy, respectively. The work was published in Nature Physics. QRAM is a long-sought building block for quantum computing, acting as a 'high-speed memory' that could enable quantum algorithms requiring fast access to large datasets, such as quantum machine learning and database search. This first hardware demonstration moves QRAM from theory to experiment and could accelerate the development of practical quantum architectures. The team reported that their optimized circuit reduces circuit depth by more than 30% compared to unoptimized schemes, and they experimentally verified for the first time that the architecture exhibits local noise resilience. The next step is to scale up QRAM research.

telegram · zaihuapd · Nov 21, 08:31

**Background**: Quantum random access memory (QRAM) is a quantum analogue of classical RAM that uses quantum superposition of addresses to access data in parallel, potentially enabling exponential reductions in memory-call requirements. Superconducting qubits are one of the leading platforms for quantum computing, and 'Tianmu-2' is a chip developed by Zhejiang University. Circuit depth is a key metric because shallower circuits are less exposed to noise and decoherence, which is critical for near-term quantum devices.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2305.10310v1">QRAM : A Survey and Critique</a></li>
<li><a href="https://www.emergentmind.com/topics/quantum-random-access-memory-qram">Quantum Random Access Memory ( qRAM )</a></li>
<li><a href="https://inspirehep.net/files/a4f25eaa7405134a37080762f30e88af">Resilience of Quantum Random Access Memory to Generic Noise</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#hardware`, `#research breakthrough`

---

<a id="item-3"></a>
## [GPGME Double-Free Vulnerability Disclosed, Affecting Versions Before 2.3.0](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

A double-free vulnerability was disclosed in GPGME (GnuPG Made Easy) affecting all versions prior to 2.3.0, with a coordinated disclosure date of 2026-11-20 after GitLab accelerated its release due to the Ruby2Shell bug. The vulnerability was discovered by Johan Carlsson and reported via GitLab on 2026-11-12. GPGME is a widely used cryptographic library integrated into many applications, including most mail clients, XMPP clients, Samba, and GitLab for signed commits, so a memory corruption flaw could potentially lead to code execution in these contexts. The disclosure highlights the importance of upstream patch propagation and the risks of memory-unsafe languages in critical security software. The vulnerability is technically a double-free bug rather than a full remote code execution chain, as noted by community members, and a Red Hat patch from five years ago appears to have addressed it but was missed upstream. All software using GPGME prior to 2.3.0, whether as a shared library, DLL, or statically linked, is affected, including Gpg4win, GnuPG Desktop, and many mail clients.

hackernews · gdgghhhhh · Nov 21, 08:32 · [Discussion](https://news.ycombinator.com/item?id=50587208)

**Background**: GPGME (GnuPG Made Easy) is a C library that provides a high-level API for applications to use GnuPG for encryption, decryption, and signing. A double-free vulnerability occurs when a program frees the same memory address twice, which can lead to memory corruption and potentially be exploited for code execution. This class of bug is common in C/C++ code and is often mitigated by modern tooling and memory-safe languages like Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gnupg.org/documentation/manuals/gpgme/">Top (The ‘ GnuPG Made Easy’ Reference Manual)</a></li>
<li><a href="https://github.com/gpg/gpgme">GitHub - gpg/ gpgme : GnuPG Made Easy. NOTE: Maintainers are not...</a></li>
<li><a href="https://directory.fsf.org/wiki/GPGME">GPGME - Free Software Directory</a></li>

</ul>
</details>

**Discussion**: Commenters debated the severity, with one noting it is a double-free bug rather than a full RCE chain and questioning if reports are intentionally overstated. Another pointed out that Red Hat fixed it five years ago but upstream missed it, while others emphasized the need for Rust-level tooling in C/C++ and listed affected software like mail clients, Samba, and Flatpak.

**Tags**: `#security`, `#gnupg`, `#vulnerability`, `#cryptography`, `#open-source`

---

<a id="item-4"></a>
## [Microsoft enables multi-PC AI model sharing via RDMA over USB4 on Windows](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft released a developer preview of RDMA over USB4 for Windows, allowing multiple PCs to pool memory and GPU resources over standard USB4 cables to run a single local AI model. In a demo, three AMD Ryzen AI Max+ 395 systems ran the Qwen3-235B-A22B model at 4-bit quantization at about 18.5 tokens per second. This lowers the barrier to running large language models locally by letting users combine existing hardware without specialized networking gear like high-speed NICs or switches. It could impact edge AI and distributed computing, making it feasible for small teams or enthusiasts to run models that would otherwise require a single high-memory machine. The technology will be rolled out through the Windows Insider experimental channel, with no timeline announced for general availability. The demo used 4-bit quantized Qwen3-235B-A22B, a large model with 235 billion parameters, and achieved 18.5 tokens/s across three machines.

telegram · zaihuapd · Nov 21, 06:13

**Background**: RDMA (Remote Direct Memory Access) allows computers to access each other's memory directly without involving the CPU, traditionally used in high-performance networking like InfiniBand. USB4 is a high-speed connector standard that supports data rates up to 40 Gbps. By bringing RDMA over USB4 to Windows, Microsoft enables direct memory sharing between PCs using a common port, eliminating the need for specialized network hardware. The AMD Ryzen AI Max+ 395 is a recent APU with integrated GPU and unified memory, suitable for local AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://club.dns-shop.ru/digest/189601-windows-11-nauchili-obedinyat-pamyat-i-gpu-pk-cherez-usb4-dlya-lok/">Windows 11 научили объединять память и GPU ПК через...</a></li>
<li><a href="https://www.cozumpark.com/windows-11e-usb4-rdma-destegi-geliyor-birden-fazla-bilgisayarin-gucu-birlesecek/">Windows 11'e USB 4 RDMA Desteği Geliyor: Birden... - ÇözümPark</a></li>

</ul>
</details>

**Tags**: `#RDMA`, `#USB4`, `#local AI`, `#distributed computing`, `#Windows`

---

<a id="item-5"></a>
## [Oral RAS(ON) inhibitor daraxonrasib shows 60.7% response in first-line pancreatic cancer](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 8.0/10

At the EORTC-NCI-AACR (ENA 2026) conference on November 20, researchers presented late-breaking data from a Phase I/II trial of daraxonrasib, an oral RAS(ON) multi-selective inhibitor, combined with gemcitabine/nab-paclitaxel in 61 previously untreated metastatic pancreatic ductal adenocarcinoma patients. The regimen achieved a confirmed objective response rate of 60.7%, a complete response rate of 8.2% (about 1 in 12), a disease control rate of 90.2%, median progression-free survival of 12.8 months, and a 12-month overall survival rate of 76.6% at a median follow-up of 18.3 months. Metastatic pancreatic cancer is one of the deadliest cancers, with historical 1-year survival rates of only 22–48% under standard chemotherapy, so a first-line oral targeted regimen showing this level of activity could represent a major therapeutic advance. If confirmed in the ongoing Phase III trial, daraxonrasib combination therapy may become a new standard of care for patients with RAS-mutant pancreatic cancer. The results come from a single-arm Phase I/II study without a chemotherapy control group, and the lead investigator emphasized that efficacy comparisons must await the ongoing Phase III trial. Daraxonrasib is an oral RAS(ON) multi-selective inhibitor that targets the active GTP-bound state of RAS and covers multiple KRAS/NRAS mutations, rather than a single G12C-specific agent; it was approved by the FDA on August 26 (brand name RASONQUE) for previously treated patients based on the Phase III RMC-302 trial, which showed a median overall survival of 13.2 vs 6.7 months.

telegram · zaihuapd · Nov 21, 11:24

**Background**: Pancreatic ductal adenocarcinoma (PDAC) is driven in most cases by mutations in the RAS family of genes, particularly KRAS, which promote uncontrolled cell growth. Traditional RAS inhibitors targeted the inactive (OFF) state and had limited success in PDAC; daraxonrasib belongs to a newer class of RAS(ON) inhibitors that bind the active state of the protein and are designed to be more effective in tumors dependent on active RAS signaling. The current standard first-line chemotherapy for metastatic pancreatic cancer includes gemcitabine plus nab-paclitaxel (the MPACT regimen) or mFOLFIRINOX, both of which offer modest survival benefits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.drugs.com/rasonque.html">Rasonque ( daraxonrasib ): Uses, Dosage, Side Effects</a></li>
<li><a href="https://www.onclive.com/view/daraxonrasib-monotherapy-elicits-meaningful-responses-in-previously-treated-ras-mutated-pancreatic-cancer">Daraxonrasib Monotherapy Elicits Meaningful Responses in... | OncLive</a></li>
<li><a href="https://www.cancer.gov/types/pancreatic/research/nab-paclitaxel-gemcitabine">Nab - Paclitaxel Plus Gemcitabine for Metastatic Pancreatic Cancer</a></li>

</ul>
</details>

**Tags**: `#pancreatic cancer`, `#oncology`, `#RAS inhibitor`, `#clinical trial`, `#targeted therapy`

---