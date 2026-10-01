---
layout: default
title: "Horizon Summary: 2026-10-01 (EN)"
date: 2026-10-01
lang: en
---

> From 26 items, 6 important content pieces were selected

---

1. [Google Announces Gemini 4 Argon Flagship AI Model](#item-1) ⭐️ 9.0/10
2. [DeepSeek Open-Sources Foundational Components for Huawei Ascend](#item-2) ⭐️ 8.0/10
3. [Trump and Six AI Giants Sign Voluntary AI Safety Accord](#item-3) ⭐️ 8.0/10
4. [Cloudflare to Enter the Public Certificate Authority Market](#item-4) ⭐️ 8.0/10
5. [Kimi K3 Becomes First Chinese Model in OpenAI's Codex Enterprise Billing](#item-5) ⭐️ 8.0/10
6. [Reddit to Kill RSS Feeds and Public API Access Over AI Bots](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Announces Gemini 4 Argon Flagship AI Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 9.0/10

Google announced Gemini 4 Argon, a new flagship AI model excelling in coding, reasoning, and multimodality, with an introductory price of $2 per million input tokens and $10 per million output tokens. The model is currently being iterated on with early testers before broader release to developers, enterprises, and consumers. This release intensifies the ongoing AI model leapfrogging race among frontier labs, challenging the notion that AI is a winner-takes-all field and suggesting a more distributed competitive landscape across hyperscalers, neoclouds, and startups. It directly impacts developers and enterprises choosing AI providers, emphasizing the need for replaceable model and provider strategies. Gemini 4 Argon (High) is among the leading models in intelligence and reasonably priced compared to similar models, with cached input tokens priced at 95% off the input token price. It trails Gemini 3.8 Flash by about 14 points on the Vals task set, though this gap may not generalize to other tasks.

hackernews · bradleyg223 · Sep 30, 20:04 · [Discussion](https://news.ycombinator.com/item?id=49913571)

**Background**: Gemini is Google's family of multimodal AI models, and Argon is the latest flagship iteration. The AI industry has seen rapid model releases from multiple labs, with performance and pricing comparisons tracked by platforms like Artificial Analysis. The term 'leapfrogging' refers to labs alternately releasing models that surpass each other's capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-argon">Gemini 4 Argon ( high ) - Intelligence , Performance & Price Analysis</a></li>
<li><a href="https://news.ycombinator.com/item?id=49914236">Gemini 4 Argon ( High ): Intelligence , Performance and Price Analysis</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters highlighted Gemini's practical capabilities, with one user describing how Gemini 3.8 Flash reverse-engineered a GPU driver to fix a ROCm issue. Others debated the competitive landscape, noting that leapfrogging continues and challenging Dario Amodei's winner-takes-all theory, while some criticized the delayed release and advised keeping models replaceable.

**Tags**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Model Release`

---

<a id="item-2"></a>
## [DeepSeek Open-Sources Foundational Components for Huawei Ascend](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

On September 30, 2026, DeepSeek open-sourced a suite of foundational components for Huawei's Ascend platform, including the TileLang high-level compiler toolchain, compute libraries, and distributed communication libraries that mirror its NVIDIA-platform offerings. The release covers DeepGEMM Ascend, DeepEP Ascend, TileKernels, FlashMLA, and DeepSelect, with DeepSeek claiming performance close to hardware limits in multiple benchmarks and confirming joint work with Huawei on a 128-card supernode for the Ascend 950. This is a full-stack software release that directly challenges NVIDIA's CUDA ecosystem dominance by giving Ascend users production-grade compiler, kernel, and communication tooling that mirrors DeepSeek's NVIDIA stack. It lowers the barrier for running DeepSeek-family and other large models on domestic Chinese hardware, and the 128-card supernode collaboration signals that Huawei's scale-out strategy is being paired with serious software investment. DeepGEMM Ascend is a port of DeepGEMM to the Huawei Ascend platform that is fully API-compatible with the original, supporting BF16, FP8, and FP4 GEMM as well as MQA logits, so existing code built around DeepGEMM's interfaces can keep the same development workflow. TileLang is a Pythonic DSL built on Apache TVM that lets developers write high-level tile-based kernels without sacrificing low-level control.

telegram · zaihuapd · Sep 30, 03:09

**Background**: Huawei's Ascend NPUs are China's leading non-NVIDIA AI accelerators, and the Ascend 950 is paired with Huawei's "SuperNode" architecture, which connects thousands of chips (the Atlas 950 SuperNode supports 8,192 Ascend 950 DT chips) to compensate for per-chip gaps versus NVIDIA's B200/B300 through system-level scale. DeepSeek's models have been cited as running on Atlas 950 SuperNode infrastructure, making DeepSeek one of the most prominent software partners for the platform. DeepGEMM is DeepSeek's high-performance GEMM kernel library for NVIDIA GPUs, and TileLang is a tile-based kernel programming language used for writing efficient GPU/NPU operators.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/ DeepGEMM - Ascend : DeepGEMM - Ascend ...</a></li>
<li><a href="https://tilelang.com/">TileLang 0.1.14 documentation</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Huawei Ascend`, `#AI infrastructure`, `#open source`, `#distributed computing`

---

<a id="item-3"></a>
## [Trump and Six AI Giants Sign Voluntary AI Safety Accord](https://t.me/zaihuapd/44123) ⭐️ 8.0/10

On September 29, President Trump and the heads of Google, Anthropic, Meta, OpenAI, xAI, and Nvidia jointly signed a one-page AI agreement, which Trump posted on Truth Social and described as having "moral binding force." The accord requires companies to establish four layers of control: external audits, independent board oversight, and monitoring of cybersecurity and bio/chem threats during model training and deployment. This is the first time all major US frontier AI players and the White House have jointly committed to a common oversight framework, signaling a shift toward voluntary industry self-governance rather than binding regulation. It could shape how AI safety is audited and governed globally, though its lack of legal enforcement raises questions about real-world impact. The agreement is a one-page document with no legal enforcement mechanism, relying instead on "moral binding force" and voluntary compliance. It replicates the structure of financial auditing—internal controls, external checks, and board oversight—but without the disclosure rules that make financial audits useful to outsiders.

telegram · zaihuapd · Sep 30, 05:15

**Background**: AI alignment is a subfield of AI safety focused on steering AI systems toward intended goals, preferences, or ethical principles, and misaligned systems can pursue unintended objectives. As advanced models like large language models become more capable, researchers and executives have warned about risks including strategic deception and power-seeking. The new accord attempts to address these risks through governance mechanisms similar to those used in regulated industries like finance and aviation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://shattered.io/white-house-ai-accord-outside-audits-explicit-2026/">White House AI Accord Makes Outside Audits Explicit</a></li>
<li><a href="https://forklog.com/en/ai-companies-agree-to-voluntary-model-oversight/">AI Companies Agree to Voluntary Model Oversight | ForkLog</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#AI Governance`, `#Policy`, `#Tech Industry`, `#Regulation`

---

<a id="item-4"></a>
## [Cloudflare to Enter the Public Certificate Authority Market](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare has announced plans to become a public certificate authority, applying to the Chrome, Apple, Microsoft, and Mozilla root programs and signing an agreement with GlobalSign to acquire a widely trusted root certificate. The company has not yet begun issuing certificates, but intends to prioritize ACME-based automated issuance and renewal, with production Merkle Tree Certificates (MTCs) planned for Q1 2027 to serve a post-quantum internet. Cloudflare's entry into the public CA market could disrupt the established certificate authority landscape, which has long been dominated by a handful of players like DigiCert, Sectigo, and Let's Encrypt. As a major CDN and internet infrastructure provider, Cloudflare is well positioned to push ACME-first automation and post-quantum readiness, potentially accelerating industry-wide adoption of more efficient certificate technologies. Cloudflare plans to issue production Merkle Tree Certificates (MTCs) by Q1 2027, a novel certificate format that uses Merkle trees to dramatically reduce the data exchanged during TLS handshakes. The company has not yet started issuing certificates, and its root acquisition from GlobalSign is subject to regulatory approval and root program acceptance.

telegram · zaihuapd · Sep 30, 06:26

**Background**: A certificate authority (CA) is a trusted entity that issues digital certificates used to verify identities and enable encrypted connections (HTTPS) on the web. To be trusted by browsers, a CA must be included in root programs maintained by companies like Google, Apple, Microsoft, and Mozilla. ACME (Automated Certificate Management Environment) is an IETF standard protocol that automates the issuance and renewal of domain-validated certificates, widely used by services like Let's Encrypt. Merkle Tree Certificates (MTCs) are a proposed certificate format that uses Merkle trees to compress certificate data, making them smaller and more efficient, which is especially important for post-quantum cryptography where certificates are much larger.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sectigo.com/blog/what-are-merkle-tree-certificates-mtcs">What are Merkle Tree Certificates (MTCs)? | Sectigo® Official</a></li>
<li><a href="https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/">What is post - quantum cryptography (PQC)?</a></li>
<li><a href="https://aawjq20.buzz/p/https/docs.aws.amazon.com/acm/latest/userguide/acm-acme.html">ACME certificate automation - AWS Certificate Manager</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Certificate Authority`, `#PKI`, `#Post-Quantum`, `#ACME`

---

<a id="item-5"></a>
## [Kimi K3 Becomes First Chinese Model in OpenAI's Codex Enterprise Billing](https://36kr.com/newsflashes/4005691489112198) ⭐️ 8.0/10

US AI infrastructure company Baseten announced that enterprise users can now use Kimi K3 inside OpenAI's Codex coding tool, with usage fees billed directly against their existing OpenAI procurement commitments rather than requiring a new vendor onboarding process. This makes Kimi K3 the first Chinese open-source model to enter OpenAI's mainstream enterprise payment and settlement channel. This is a notable shift in enterprise AI procurement: a Chinese open-weight model is now reachable through a US vendor's existing enterprise billing rails, lowering adoption friction for companies already committed to OpenAI. It signals growing cross-vendor integration in the enterprise AI stack and could reshape how enterprises evaluate non-US models. Kimi K3 is Moonshot AI's flagship open-weight model, a 2.8-trillion-parameter mixture-of-experts system that routes each token through only 16 of its 896 experts, and it is positioned for complex coding and long-horizon agentic workflows. The integration is delivered via Baseten's inference infrastructure, and billing flows through existing OpenAI enterprise commitments rather than a separate contract.

telegram · zaihuapd · Sep 30, 11:23

**Background**: OpenAI's Codex is an AI coding partner designed for multi-agent software engineering workflows, and enterprises typically access such tools through pre-negotiated procurement commitments. Baseten is a US AI infrastructure company founded in 2019 that provides a serverless inference platform for deploying and scaling models in production. Kimi K3, released by Moonshot AI, is the largest open-weight model ever released and is available on platforms such as Hugging Face and OpenRouter.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform: Deploy AI models in production | Baseten</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://k3-kimi.com/">Kimi K 3 : 2.8T Open-Weight Model — Benchmarks, Pricing & Guides</a></li>

</ul>
</details>

**Tags**: `#AI`, `#enterprise`, `#OpenAI`, `#Kimi K3`, `#model integration`

---

<a id="item-6"></a>
## [Reddit to Kill RSS Feeds and Public API Access Over AI Bots](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit announced it will discontinue RSS feed support on November 13 and shut down public API access by March 2027, citing large-scale scraping and automated abuse, particularly by AI bots. Third-party apps and bot developers must register by January 12, 2027 or lose API access, and moderators are being advised to switch to Discord Relay. This is a major platform policy change that affects developers, researchers, moderators, and ordinary users who rely on open access to Reddit content, and it further erodes the open web by removing standardized, machine-readable feeds. It also has significant implications for AI training data pipelines and the third-party ecosystem built on Reddit's public API. RSS feeds stop on November 13, public API access ends by March 2027, and third-party developers must register by January 12, 2027 to retain access. Reddit is directing moderators toward Discord Relay as a replacement for feed-based workflows, though no technical details on the registration process or relay capabilities were provided.

telegram · zaihuapd · Oct 1, 00:27

**Background**: RSS (Really Simple Syndication) is a standardized XML-based web feed format that lets users and applications track updates from websites in a single news aggregator, and it has been a core building block of the open web since the early 2000s. Reddit's public API has similarly allowed third-party clients, bots, and research tools to read posts and comments programmatically. Reddit earns roughly 10% of its revenue from data licensing deals with Google and OpenAI that expire in 2027, giving the company a strong incentive to control how its content is accessed and scraped.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSS_feed">RSS feed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reddit_Public_Access_Network">Reddit Public Access Network</a></li>
<li><a href="https://publicapis.io/reddit-api">Reddit API — API Key, Docs & Examples | PublicAPIs.io</a></li>

</ul>
</details>

**Tags**: `#Reddit`, `#API`, `#RSS`, `#AI scraping`, `#platform policy`

---