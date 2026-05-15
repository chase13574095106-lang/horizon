---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 32 items, 8 important content pieces were selected

---

1. [Pixel 10 0-Click Exploit Chain Disclosed by Project Zero](#item-1) ⭐️ 9.0/10
2. [First Public Apple M5 Kernel Exploit in 5 Days with AI](#item-2) ⭐️ 9.0/10
3. [vLLM v0.21.0: Breaking Changes, KV Offload, Spec Decode](#item-3) ⭐️ 8.0/10
4. [AI Psychosis: Companies Outsourcing Thinking to AI](#item-4) ⭐️ 8.0/10
5. [DOJ demands Apple and Google unmask 100k app users](#item-5) ⭐️ 8.0/10
6. [OCaml in Space with Stack Annotations](#item-6) ⭐️ 8.0/10
7. [arXiv Bans Authors for Unverified LLM Content for 1 Year](#item-7) ⭐️ 8.0/10
8. [Trump Discusses AI Guardrails and Nvidia H200 with Xi](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pixel 10 0-Click Exploit Chain Disclosed by Project Zero](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a 0-click exploit chain for the Pixel 10 that allows attackers to gain root access without any user interaction, leveraging vulnerabilities in AI-powered message analysis features. This exploit chain highlights how AI features in mobile devices expand the attack surface, making 0-click attacks more feasible, and underscores the importance of timely patching across the Android ecosystem. The exploit chain required only two software defects to achieve kernel privileges from a 0-click context, and the vendor patched the vulnerability within 90 days, which is notably fast for an Android driver bug.

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: A 0-click exploit allows an attacker to compromise a device without any user action, such as opening a message or clicking a link. AI-powered message analysis decodes media before the user opens it, increasing the attack surface for such exploits. Project Zero is Google's security research team that discovers and discloses vulnerabilities to improve platform security.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/01/pixel-0-click-part-3.html">A 0 - click exploit chain for the Pixel 9 Part 3: Where do... - Project Zero</a></li>
<li><a href="https://oxo.is/blog/2026/05/13/news-2026-05-13-a-0-click-exploit-chain-for-the-pixel-10-when-a-door-closes/">A 0 - click exploit chain for the Pixel 10: When a Door Closes...</a></li>
<li><a href="https://projectzero.google/2020/01/policy-and-disclosure-2020-edition.html">Policy and Disclosure : 2020 Edition - Project Zero</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about AI features increasing attack surface, with one noting that reading SMS without user consent is a recurring lesson. Another praised Google's fast patch time but worried about the rest of Android. Some debated whether AI is accelerating exploit discovery or just increasing media attention.

**Tags**: `#security`, `#exploit`, `#Android`, `#Pixel`, `#Project Zero`

---

<a id="item-2"></a>
## [First Public Apple M5 Kernel Exploit in 5 Days with AI](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Security researcher Calif, in collaboration with Anthropic's Mythos Preview AI system, achieved the first public kernel memory corruption exploit for Apple M5 macOS in just 5 days, bypassing Apple's MIE hardware memory protection. This demonstrates that even Apple's most advanced hardware memory protection (MIE) can be broken by combining expert human skill with cutting-edge AI, raising serious questions about the long-term effectiveness of hardware-level security measures. The exploit chain targets macOS 26.4.1 on M5 hardware, using two vulnerabilities and multiple techniques to escalate from a non-privileged user to root shell using only normal system calls. A full 55-page technical report will be released after Apple's fix.

telegram · zaihuapd · May 15, 02:15

**Background**: Apple's Memory Integrity Enforcement (MIE) is a hardware-level memory safety protection introduced in 2025, designed to prevent memory corruption attacks on the kernel. It represents five years of engineering effort and is considered an industry-first always-on protection. Kernel memory corruption exploits are a common method for privilege escalation on operating systems.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory safety in Apple devices - Apple Security Research</a></li>
<li><a href="https://9to5mac.com/2026/05/14/calif-team-details-how-anthropic-mythos-helped-build-a-working-macos-exploit-in-five-days/">Anthropic Mythos helped Calif build a macOS exploit in five... - 9to5Mac</a></li>

</ul>
</details>

**Tags**: `#Apple M5`, `#kernel exploit`, `#macOS security`, `#AI-assisted hacking`, `#MIE bypass`

---

<a id="item-3"></a>
## [vLLM v0.21.0: Breaking Changes, KV Offload, Spec Decode](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 deprecates transformers v4, requires C++20, integrates KV offload with Hybrid Memory Allocator (HMA), adds speculative decoding support for reasoning models, and introduces a TOKENSPEED_MLA backend for Blackwell GPUs. This release significantly impacts production LLM inference systems by enforcing a mandatory migration to transformers v5 and a C++20 compiler, while also improving memory efficiency and inference speed through KV offloading and speculative decoding for reasoning models. The KV offload with HMA includes scheduler-side sliding window groups and full HMA enablement. Speculative decoding now respects reasoning/thinking budgets, enabling correct spec decode for models like DeepSeek-R1. The TOKENSPEED_MLA backend targets DeepSeek-R1/Kimi-K25 prefill and decode on Blackwell GPUs.

github · khluu · May 15, 08:44

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models. KV cache offloading moves key-value cache data from GPU to CPU memory to reduce GPU memory pressure, while speculative decoding uses a smaller draft model to accelerate generation. The Hybrid Memory Allocator (HMA) optimizes memory allocation for models with mixed attention types.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm-project/vllm</a></li>
<li><a href="https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html">Inside vLLM’s New KV Offloading Connector: Smarter Memory Transfer for Maximizing Inference Throughput | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/tokenspeed_mla/">tokenspeed _ mla - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#transformers`, `#GPU`, `#speculative decoding`

---

<a id="item-4"></a>
## [AI Psychosis: Companies Outsourcing Thinking to AI](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto criticizes companies for outsourcing decision-making and code writing to AI without human oversight, warning of unstable systems and 'AI psychosis'. This highlights a critical risk in AI adoption: over-reliance on AI without human judgment can create fragile, unmaintainable systems, especially in software engineering and finance. The term 'AI psychosis' originally refers to individuals developing delusions from AI interactions, but here it's used metaphorically for organizations blindly trusting AI outputs.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: AI psychosis is a phenomenon where interactions with AI trigger or worsen paranoia and delusions in vulnerable individuals. In software engineering, AI tools like code generators are increasingly used, but without proper review, they can introduce bugs and security risks that compound over time.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chatbot_psychosis">Chatbot psychosis - Wikipedia</a></li>
<li><a href="https://www.news-medical.net/health/AI-Psychosis-How-Artificial-Intelligence-May-Trigger-Delusions-and-Paranoia.aspx">AI Psychosis : How Artificial Intelligence May Trigger Delusions and...</a></li>
<li><a href="https://www.groovyweb.co/blog/outsource-ai-development-risks-benefits-right-partner-2026">Outsource AI Development: Risks , Benefits & Partner Guide</a></li>

</ul>
</details>

**Discussion**: Commenters agree with the critique, noting that purely AI-written systems may become too complex for humans to understand, leading to instability. Some argue that using AI as a tool is fine, but blindly trusting its output is the real problem.

**Tags**: `#AI`, `#software engineering`, `#risk management`, `#AI adoption`

---

<a id="item-5"></a>
## [DOJ demands Apple and Google unmask 100k app users](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice has issued subpoenas to Apple and Google demanding they unmask over 100,000 users of a popular car-tinkering app as part of an emissions crackdown. This case raises significant privacy and centralization concerns, as it sets a precedent for government surveillance through app stores and could chill legitimate vehicle modification and research. The app in question is used to modify vehicle software, including disabling emissions controls, which may violate the Clean Air Act. The DOJ seeks user identities to identify potential witnesses, but critics argue this is a fishing expedition.

hackernews · tencentshill · May 15, 17:28 · [Discussion](https://news.ycombinator.com/item?id=48151383)

**Background**: Vehicle software tinkering has been a contentious issue, with exemptions under the DMCA allowing some modifications for security research. However, defeating emissions controls is illegal under the Clean Air Act. The centralized nature of app stores like Apple's App Store and Google Play makes them a target for government subpoenas.

<details><summary>References</summary>
<ul>
<li><a href="https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/">U.S. DOJ demands Apple and Google unmask over 100,000 users of popular car-tinkering app in emissions crackdown</a></li>
<li><a href="https://www.bbc.com/news/technology-34656699">Smart car software tinkering legal - US ruling - BBC News</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some criticized the government's approach as overreach and a privacy violation, while others argued that users who defeat emissions controls deserve scrutiny. Concerns were raised about the precedent for future surveillance and the role of centralized app distribution.

**Tags**: `#privacy`, `#government surveillance`, `#app stores`, `#legal`, `#automotive`

---

<a id="item-6"></a>
## [OCaml in Space with Stack Annotations](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

A project called OxCaml uses stack annotations in OCaml to eliminate GC pressure, achieving sub-10ns p99.9 latency on packet dispatch in a space application. This demonstrates that garbage-collected languages can achieve ultra-low latency suitable for space and high-frequency trading, by using type annotations to move allocations to the stack. Switching to OxCaml with exclave stack annotations dropped p99.9 latency from 29 ns to 9 ns per packet, and reduced minor GCs from 394 to zero over 25 million packets.

hackernews · yminsky · May 15, 10:55 · [Discussion](https://news.ycombinator.com/item?id=48147058)

**Background**: OCaml is a garbage-collected language commonly used in systems programming. Stack annotations allow developers to explicitly allocate data on the stack instead of the heap, reducing GC pressure and improving latency predictability.

<details><summary>References</summary>
<ul>
<li><a href="https://oxcaml.org/documentation/stack-allocation/intro/">OxCaml | Stack allocation | Intro</a></li>
<li><a href="https://ocamlpro.com/blog/2020_03_23_in_depth_look_at_best_fit_gc/">An in-depth Look at OCaml’s new “Best-fit” Garbage Collector Strategy | OCamlPro</a></li>
<li><a href="https://dev.realworldocaml.org/garbage-collector.html">Understanding the Garbage Collector - Real World OCaml</a></li>

</ul>
</details>

**Discussion**: Commenters noted prior use of OCaml in space (e.g., GHGSat-D in 2016) and discussed the difficulty of bending GC languages for low-latency scenarios. Some questioned the security of reinventing protocols like CCSDS.

**Tags**: `#OCaml`, `#garbage collection`, `#space software`, `#low-latency`, `#systems programming`

---

<a id="item-7"></a>
## [arXiv Bans Authors for Unverified LLM Content for 1 Year](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv announced a 1-year ban for authors who submit papers containing unverified LLM-generated content, such as hallucinated citations, leftover meta-comments, or placeholder data. This policy sets a clear precedent for academic integrity in AI research, holding authors accountable for all content regardless of how it was generated, and aims to curb the rising issue of LLM hallucinations in scholarly publications. After the ban ends, authors must have their subsequent submissions accepted by a credible peer-reviewed venue before they can resubmit to arXiv. The policy specifically targets hallucinated citations, LLM-generated meta-comments, and placeholder data like 'replace with real experimental data'.

telegram · zaihuapd · May 15, 04:30

**Background**: arXiv is a widely used preprint repository for scientific papers, especially in physics, mathematics, and computer science. LLMs like GPT-4 can generate plausible but incorrect citations, known as hallucinations, which have become a growing concern in academic publishing. The arXiv code of conduct states that authorship implies responsibility for all content, regardless of how it was produced.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.07723">LLM hallucinations in the wild</a></li>
<li><a href="https://www.factors.ai/blog/llm-hallucination-detection-examples">LLM Hallucination Examples: What They Are and How to Detect Them</a></li>

</ul>
</details>

**Discussion**: The Telegram channel discussion validated the importance of this policy, with community members expressing support for arXiv's clear stance against unverified LLM content, though some noted challenges in enforcement and detection.

**Tags**: `#arXiv`, `#LLM`, `#academic integrity`, `#AI policy`, `#publishing`

---

<a id="item-8"></a>
## [Trump Discusses AI Guardrails and Nvidia H200 with Xi](https://www.bloomberg.com/news/articles/2026-05-15/trump-says-he-discussed-ai-guardrails-nvidia-s-chips-with-xi) ⭐️ 8.0/10

President Trump revealed that he discussed AI guardrails and Nvidia's H200 chip exports with Chinese President Xi Jinping during his visit to China, noting that China has chosen not to buy the H200 and is instead developing its own chips. This high-level discussion underscores the ongoing US-China tensions over AI chip export controls, which directly impact global AI supply chains and the technological sovereignty of both nations. The US has permitted Nvidia to supply H200 chips to China, but Beijing has not approved any purchases, and no deliveries have been made. Previously, China also refused imports of the lower-performance H20 chip.

telegram · zaihuapd · May 15, 15:13

**Background**: AI guardrails refer to safety mechanisms that ensure AI systems operate within acceptable boundaries. The H200 is Nvidia's advanced AI chip, subject to US export controls. China's push for domestic chip development aims to reduce reliance on foreign technology.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/AI_guardrails">AI guardrails</a></li>
<li><a href="https://grokipedia.com/page/2026_Chinese_restrictions_on_Nvidia_H200_chips">2026 Chinese restrictions on Nvidia H200 chips</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductors`, `#US-China trade`, `#export controls`, `#geopolitics`

---