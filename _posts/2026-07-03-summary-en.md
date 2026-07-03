---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 46 items, 8 important content pieces were selected

---

1. [Karpathy Launches NanoChat: ChatGPT Clone for $100](#item-1) ⭐️ 8.0/10
2. [EU Parliament Spyware Investigator Hacked with Pegasus](#item-2) ⭐️ 8.0/10
3. [Open Source AI Gap Map Launched by Current AI](#item-3) ⭐️ 8.0/10
4. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-4) ⭐️ 8.0/10
5. [Huawei Atlas 350 with Ascend 950PR claims 2.87x H20 performance](#item-5) ⭐️ 8.0/10
6. [Alibaba Orders Employees to Uninstall Claude by July 10](#item-6) ⭐️ 8.0/10
7. [NASA Launches Rescue Satellite to Save Aging Swift Telescope](#item-7) ⭐️ 8.0/10
8. [Tencent's Atuin AI Beats Mythos in CyberGym Benchmark](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy Launches NanoChat: ChatGPT Clone for $100](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

Andrej Karpathy released nanochat, a minimal, full-stack training and inference pipeline for a ChatGPT-like chatbot, built from scratch in a single codebase with minimal dependencies. This project democratizes access to conversational AI by showing that a functional ChatGPT alternative can be built for as little as $100, potentially enabling broader experimentation and education in the field. Nanochat builds on Karpathy's earlier nanoGPT but extends it from pretraining to a full chatbot pipeline, including a Rust tokenizer and approximately 8,000 lines of code.

github · karpathy · Jul 3, 17:47

**Background**: NanoGPT, released three years ago, focused only on pretraining language models. Nanochat completes the picture by adding fine-tuning and inference, making it a practical chatbot. The project aims to be hackable and dependency-lite, appealing to developers and researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can buy. · GitHub</a></li>
<li><a href="https://x.com/karpathy/status/1977755427569111362?lang=en">Excited to release new repo: nanochat! (it's ...</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1o5qo0r/it_has_been_4_hrs_since_the_release_of_nanochat/">r/LocalLLaMA on Reddit: It has been 4 hrs since the release of nanochat from Karpathy and no sign of it here! A new full-stack implementation of an LLM like ChatGPT in a single, clean, minimal, hackable, dependency-lite codebase</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed interest in nanochat, noting its 8,000 LOC and Rust tokenizer, with some questioning the novelty compared to nanoGPT. Overall sentiment was positive, with many planning to explore the code.

**Tags**: `#LLM`, `#ChatGPT`, `#open-source`, `#cost-effective`, `#AI`

---

<a id="item-2"></a>
## [EU Parliament Spyware Investigator Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab confirmed that a member of the European Parliament committee investigating spyware was successfully infected with Pegasus spyware on multiple occasions in 2022 and 2023, compromising sensitive data including medical information and government documents. This attack directly undermines the integrity of a democratic institution's investigative process and highlights the ongoing threat of commercial spyware to elected officials and public accountability. The infections occurred on October 21, 2022, and March 6–7, 2023, targeting a member of the European Parliament's Committee of Inquiry to investigate the use of Pegasus and equivalent surveillance spyware (PEGA Committee).

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a powerful spyware developed by the Israeli company NSO Group, capable of remotely compromising mobile devices and extracting data. Citizen Lab is a leading research organization at the University of Toronto that investigates digital threats and has exposed numerous Pegasus infections worldwide.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony of a spyware investigator being hacked, with some pointing to broader Greek and Italian scandals involving state abuse of Pegasus. Others discussed device hardening measures, suggesting that using GrapheneOS or enabling lockdown mode could have raised the cost of the attack.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-3"></a>
## [Open Source AI Gap Map Launched by Current AI](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 products across the open source AI stack, including 266 software tools, 85 models, 50 datasets, and 20 hardware projects. This map provides a structured, publicly accessible resource for understanding the open source AI ecosystem, helping developers, researchers, and policymakers identify gaps and opportunities. The underlying data is released under MIT license, enabling further analysis and community contributions. The map organizes products into 14 categories across 3 layers (model components, product/UX, and infrastructure), and tracks over 16,000 GitHub repos. The data is available as YAML files and CSV on GitHub, and can be explored via Datasette Lite.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global partnership with $400 million committed, aiming to build a public option for AI. The Gap Map is an attempt to systematically catalog the open source AI landscape, which has grown rapidly but lacks a comprehensive index. The project is backed by significant funding and aims to support the open source AI community.

**Tags**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

---

<a id="item-4"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic has accused Alibaba of conducting the largest known distillation attack on its Claude AI model, using nearly 25,000 fraudulent accounts to generate over 28.8 million interactions between April 22 and June 5, 2026, to illicitly extract Claude's capabilities. This allegation highlights a serious security and intellectual property threat in the AI industry, as distillation attacks can undermine export controls and allow foreign competitors to replicate proprietary models without authorization, potentially eroding the competitive advantage of US AI companies. Anthropic claims that Alibaba and its Qwen AI lab were involved in the attack, which targeted Claude's capabilities through repeated queries to train a competing model. The attack occurred over a 45-day period and involved millions of interactions, making it the largest such attack Anthropic has ever detected.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where a weaker model learns from a stronger model's outputs to replicate its capabilities. While legitimate for internal use, using another company's proprietary model without permission is considered intellectual property theft. Anthropic has been vocal about the risks of distillation attacks, which can bypass export controls and spread advanced AI capabilities globally.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#model distillation`, `#Anthropic`, `#Alibaba`

---

<a id="item-5"></a>
## [Huawei Atlas 350 with Ascend 950PR claims 2.87x H20 performance](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

At the 2026 Huawei China Partner Conference, Huawei officially launched and released the Atlas 350 AI accelerator card featuring the new Ascend 950PR processor, claiming 2.87 times the single-card compute power of NVIDIA's H20 GPU and support for FP4 low-precision inference. This release marks a significant step for Huawei in the AI hardware race, potentially reducing China's dependence on NVIDIA chips for AI inference. The FP4 support and high memory capacity (112GB HBM) could lower inference costs and latency for large models like 70B-parameter ones. The Atlas 350 is claimed to be the only accelerator card in China supporting FP4 inference, with 112GB HBM capacity enabling single-card loading of 70B-parameter models. Performance improvements over the previous generation include vector compute, interconnect bandwidth, and self-developed HBM.

telegram · zaihuapd · Jul 3, 08:35

**Background**: NVIDIA's H20 GPU is a modified version of the H100 designed for the Chinese market due to US export restrictions. FP4 is a 4-bit floating-point format that NVIDIA introduced for efficient AI inference, and Huawei's adoption of FP4 indicates alignment with industry trends. The Ascend 950PR is Huawei's latest AI chip, delivering 1.56 petaflops according to some reports.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/">Ascend 950PR AI Chip: Everything you need to know</a></li>
<li><a href="https://nerdleveltech.com/huawei-ascend-950pr-atlas-350-ai-chip-challenges-nvidia">Huawei Ascend 950PR Beats NVIDIA H20: 2.8× FP8, CUDA-Ready</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#AI hardware`, `#Ascend`, `#Atlas 350`, `#FP4`

---

<a id="item-6"></a>
## [Alibaba Orders Employees to Uninstall Claude by July 10](https://t.me/zaihuapd/42334) ⭐️ 8.0/10

Alibaba has internally ordered all employees to uninstall Anthropic products, including Claude models (Sonnet, Opus, Fable) and Claude Code agent, effective July 10. This follows Anthropic's accusation that Alibaba used approximately 25,000 fake accounts to interact with Claude over 28 million times between April 22 and June 5. This incident highlights growing tensions between major tech companies over AI model security and intellectual property. It could set a precedent for how companies enforce usage policies and respond to accusations of model distillation, affecting the broader AI ecosystem. The ban covers all Anthropic products, including Claude models (Sonnet, Opus, Fable) and Claude Code agent. Previously, Alibaba reimbursed employees for using external models like Claude, GPT, and Gemini. Anthropic has since tightened its risk control strategies.

telegram · zaihuapd · Jul 3, 13:00

**Background**: Claude is a family of large language models developed by Anthropic, an AI safety company. Claude Code is an agentic coding tool that reads codebases and executes commands. Model distillation is a technique where a smaller model is trained to mimic a larger one, often using the larger model's outputs. Accusations of unauthorized distillation can lead to legal and policy disputes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html">Anthropic accuses Alibaba of campaign to extract AI capabilities</a></li>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI policy`, `#corporate security`

---

<a id="item-7"></a>
## [NASA Launches Rescue Satellite to Save Aging Swift Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

On July 3, 2026, NASA launched the LINK spacecraft, built by Katalyst Space, to rendezvous with the 20-year-old Swift space telescope and boost its orbit by about 240 kilometers, preventing an imminent atmospheric reentry. This mission marks the first time a private spacecraft will attempt to capture and service a U.S. government satellite, demonstrating a novel approach to extending the life of aging space assets and reducing space debris. The LINK spacecraft will use a robotic arm to grapple Swift and then fire its thrusters to raise the orbit. If successful, Swift could resume science observations as early as September 2026.

telegram · zaihuapd · Jul 3, 15:43

**Background**: The Swift Observatory, launched in 2004, studies gamma-ray bursts and other cosmic phenomena. Its orbit has been decaying due to increased solar activity, and without intervention, it would have burned up in Earth's atmosphere by late 2026. On-orbit satellite servicing is a growing field, with previous missions like the repair of the Solar Maximum Mission in 1984.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_rescue_mission">Swift Boost Mission - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift Observatory - NASA</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/nasa-to-launch-ambitious-mission-to-save-a-space-telescope-from-burning-up-in-earths-atmosphere">NASA launches rescue mission to save Swift space telescope from burning up in Earth's atmosphere | Space</a></li>

</ul>
</details>

**Tags**: `#NASA`, `#space telescope`, `#satellite servicing`, `#space technology`

---

<a id="item-8"></a>
## [Tencent's Atuin AI Beats Mythos in CyberGym Benchmark](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab's Atuin AI achieved an 84.0% score on the CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview, and discovered multiple critical vulnerabilities in open-source projects at less than 0.1% of Mythos's cost. This demonstrates that open-source, locally deployable AI models can outperform proprietary systems in cybersecurity tasks at a fraction of the cost, potentially democratizing advanced vulnerability detection and reducing reliance on expensive commercial AI services. Atuin AI is built on the open-source GLM-5.1 model and discovered previously undetected critical vulnerabilities in curl, gnark, OpenSSL, Python cryptography, and Java bc-java, with severity scores up to 9.3. It ranked 1st in severe vulnerability severity and 5th in total count on the Berkeley BVI real-world vulnerability list.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a large-scale cybersecurity evaluation framework from UC Berkeley that tests AI agents on real-world vulnerability analysis using 1,507 historical vulnerabilities from 188 software projects. GLM-5.1 is an open-source flagship model by Z.AI designed for long-horizon agentic tasks. Anthropic's Project Glasswing uses Claude Mythos Preview to proactively fix vulnerabilities before attackers exploit them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities ...</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.1">zai-org/GLM-5.1 · Hugging Face</a></li>
<li><a href="https://news.aibase.com/zh/news/26923">27年老漏洞被AI识破!苹果谷歌联手 Anthropic 开启“ 玻 璃 翼 ”护航</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#benchmark`, `#vulnerability detection`, `#open-source`

---