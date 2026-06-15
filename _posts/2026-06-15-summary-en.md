---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 29 items, 9 important content pieces were selected

---

1. [Nezha Monitoring Probe Has Critical Path Traversal Vulnerability (CVSS 9.1)](#item-1) ⭐️ 9.0/10
2. [vLLM v0.23.0: DeepSeek-V4 optimizations and Model Runner V2 expansion](#item-2) ⭐️ 8.0/10
3. [Backdoor in Fake LinkedIn Job Interview via npm](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0: P2P Networking Library Released](#item-4) ⭐️ 8.0/10
5. [Fox to Acquire Roku for $22 Billion](#item-5) ⭐️ 8.0/10
6. [Typst 0.15.0: Multiple Bibliographies and Better Footnotes](#item-6) ⭐️ 8.0/10
7. [Why AI hasn't replaced software engineers, and won't](#item-7) ⭐️ 8.0/10
8. [US orders Anthropic to restrict two AI models](#item-8) ⭐️ 8.0/10
9. [Rio 3.5 Model Exposed as Shell of Chinese Open-Source Models](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nezha Monitoring Probe Has Critical Path Traversal Vulnerability (CVSS 9.1)](https://github.com/nezhahq/nezha/security/advisories/GHSA-5c25-7vpj-9mqh) ⭐️ 9.0/10

A critical path traversal vulnerability (CVE-2026-53519, CVSS 9.1) has been disclosed in Nezha monitoring probe versions below v2.0.13, allowing unauthenticated attackers to read JWT secrets via crafted GET requests like /dashboard../data/config.yaml. This vulnerability is critical because Nezha is a widely-used open-source monitoring tool, and exploiting it can lead to full system compromise by forging JWT tokens. Users must urgently upgrade to v2.0.13 or later to prevent data breaches. The vulnerability is a path traversal in the dashboard component, allowing attackers to read arbitrary files such as config.yaml containing JWT secrets. The CVSS score of 9.1 indicates high exploitability and impact, with no authentication required.

telegram · zaihuapd · Jun 15, 09:25

**Background**: Nezha Monitoring is an open-source, lightweight server monitoring and management tool consisting of a dashboard and agents. Path traversal vulnerabilities occur when an application fails to properly validate user-supplied file paths, allowing attackers to access files outside the intended directory. JWT secrets are used to sign authentication tokens; if leaked, attackers can forge tokens and gain unauthorized access.

<details><summary>References</summary>
<ul>
<li><a href="https://owasp.org/www-community/attacks/Path_Traversal">Path Traversal | OWASP Foundation</a></li>
<li><a href="https://blog.echosec.top/p/nezha-monitoring/">『Blog』 NeZha Monitoring 从一到无穷大 | Echosec @QIN2DIM</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#nezha`, `#path traversal`, `#CVE`

---

<a id="item-2"></a>
## [vLLM v0.23.0: DeepSeek-V4 optimizations and Model Runner V2 expansion](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 introduces major optimizations for DeepSeek-V4, including sparse MLA metadata decoupling and a TRTLLM-gen attention kernel, and expands Model Runner V2 (MRv2) by default to Llama and Mistral dense models. This release significantly improves inference performance for DeepSeek-V4, a state-of-the-art MoE model, and makes MRv2 the default for popular dense models, benefiting a large portion of the vLLM user base with faster and more efficient inference. The release includes 408 commits from 200 contributors, adds support for new models like Gemma 4 Unified and Step-3.7-Flash, and introduces multi-tier KV cache offloading with an object-store secondary tier.

github · khluu · Jun 15, 05:27

**Background**: vLLM is an open-source high-throughput LLM inference engine. Model Runner V2 (MRv2) is a ground-up reimplementation of the model runner for cleaner, more modular, and more efficient execution. DeepSeek-V4 is a large Mixture-of-Experts (MoE) model that benefits from specialized attention and memory optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html">Multi-Head, Multi-Query, and Group-Query Attention — TensorRT-LLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#Model Runner V2`, `#open source`

---

<a id="item-3"></a>
## [Backdoor in Fake LinkedIn Job Interview via npm](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 8.0/10

A job applicant discovered a backdoor hidden in a GitHub repository sent by a recruiter during a LinkedIn job interview, which exploited npm's prepare script to execute arbitrary code upon running npm install. This attack highlights a novel social engineering vector targeting developers, exploiting trust in job interviews to compromise systems, and underscores the lack of reporting infrastructure for such cybercrimes. The backdoor was buried in commented-out test code and executed via npm's prepare script, which runs automatically after npm install. The payload communicated with a remote server to receive commands.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm's prepare script is a lifecycle hook that runs automatically after npm install, commonly used for build steps. Attackers can abuse it to execute arbitrary code when a developer installs dependencies, making it a vector for supply chain attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://stackoverflow.com/questions/44499912/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it">node.js - Why is npm running prepare script after... - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that this attack is uncomfortably close to normal interview tasks, and called for better reporting infrastructure for cybercrime. Some questioned why npm's prepare script is not blocked by default.

**Tags**: `#security`, `#supply chain attack`, `#npm`, `#social engineering`, `#cybercrime`

---

<a id="item-4"></a>
## [Iroh 1.0: P2P Networking Library Released](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0, a peer-to-peer networking library written in Rust, has been released, enabling direct connections between app instances without centralized infrastructure and supporting extensible custom transports. This release provides a novel approach to application-layer networking, similar to Tailscale but at the app level, which could simplify building distributed applications and reduce reliance on centralized servers. Iroh 1.0 ships with built-in support for IPv4, IPv6, and relay transports, and introduces a custom transport API for integrating protocols like WebRTC, BLE, or LoRa. The library uses cryptographic dial keys for secure peer identity.

hackernews · chadfowler · Jun 15, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48542480)

**Background**: Peer-to-peer networking allows devices to communicate directly without a central server, but NAT traversal and firewall issues often complicate direct connections. Iroh simplifies this by providing a library that handles these challenges, similar to how Tailscale creates a virtual network at the OS level, but Iroh operates at the application layer, making it easier for app developers to embed P2P capabilities without requiring user accounts or system-level configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://iroh-computer.vercel.app/blog/iroh-0-23-welcoming-nodejs-to-the-family">iroh 0.23.0 - Welcoming Node.js to the family! - Iroh</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion highlights Iroh as an application-layer alternative to Tailscale, with developers praising its custom transport extensibility. Some users questioned the need for yet another P2P library, while others appreciated the cryptographic key-based identity model. A developer noted plans to integrate Iroh into their existing WebRTC-based P2P tool.

**Tags**: `#peer-to-peer`, `#networking`, `#rust`, `#open-source`, `#release`

---

<a id="item-5"></a>
## [Fox to Acquire Roku for $22 Billion](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

Fox Corporation announced a $22 billion acquisition of Roku, the leading streaming hardware and platform company. The deal is expected to close in late 2026, pending regulatory approval. This vertical integration gives Fox direct control over a streaming platform used by roughly 30-50% of U.S. households, raising antitrust concerns and potentially altering the competitive landscape for streaming content and hardware. Users worry about content bias, data privacy, and reduced platform neutrality. The deal values Roku at $22 billion, a premium over its market cap. Fox already owns Tubi, a free ad-supported streaming service, and plans to integrate Roku's ad platform with its own. Roku's hardware business and operating system will remain separate, but Fox gains access to user data and home screen placement.

hackernews · thm · Jun 15, 12:50 · [Discussion](https://news.ycombinator.com/item?id=48540499)

**Background**: Roku is the dominant streaming platform in the U.S., with over 80 million active accounts and a market share of about 30% of streaming devices. Fox is a major content producer with networks like Fox News, Fox Sports, and Tubi. Vertical mergers between content providers and distribution platforms often face antitrust scrutiny due to potential for self-preferencing and market foreclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://fandomwire.com/biggest-concerns-after-foxs-22b-roku-acquisition/">5 Biggest Concerns After Fox's $22 Billion Roku Acquisition</a></li>
<li><a href="https://deadline.com/2026/06/fox-roku-acquisition-streaming-wall-street-1236956272/">Fox And Roku Frame Blockbuster $22B Merger As Streaming Win-Win, But Wall Street Has Questions</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly negative, with users expressing pessimism about Fox's control over Roku's platform. Commenters worry about forced Fox News integration, increased ads, and loss of device neutrality. Some users recommend switching to alternatives like Nvidia Shield with custom launchers.

**Tags**: `#acquisition`, `#streaming`, `#media`, `#hardware`, `#antitrust`

---

<a id="item-6"></a>
## [Typst 0.15.0: Multiple Bibliographies and Better Footnotes](https://typst.app/docs/changelog/0.15.0/) ⭐️ 8.0/10

Typst 0.15.0 introduces support for multiple bibliographies in a single document and improves footnote handling, alongside better HTML export with automatic MathML conversion for equations. These features address long-standing user requests, making Typst more viable for complex academic writing and publishing workflows, and strengthening its position as a LaTeX alternative. The multiple bibliographies feature allows users to separate references by category (e.g., primary and secondary sources), while footnote improvements include better placement and support for discursive footnotes with citations.

hackernews · schu · Jun 15, 17:24 · [Discussion](https://news.ycombinator.com/item?id=48544396)

**Background**: Typst is a markup-based typesetting system designed to be as powerful as LaTeX but easier to learn and use. It compiles to PDF and HTML, and is popular in academia for writing papers, theses, and books.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/typst/typst">GitHub - typst / typst : A markup-based typesetting system that is...</a></li>
<li><a href="https://typst.app/docs/">Typst Documentation</a></li>
<li><a href="https://typst.app/docs/reference/model/bibliography/">Bibliography Function – Typst Documentation</a></li>

</ul>
</details>

**Discussion**: Community sentiment is positive overall, with users praising the new features. However, some users note that footnotes still have limitations, especially for discursive footnotes with bibliography references, and hope for further improvements.

**Tags**: `#typesetting`, `#open source`, `#typst`, `#software release`

---

<a id="item-7"></a>
## [Why AI hasn't replaced software engineers, and won't](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan and Sayash Kapoor published an essay arguing that data does not support the claim that AI will cause mass layoffs in software engineering, citing that zero out of 160+ companies in New York reported AI-related layoffs under the state's new WARN Act disclosure requirement. This essay provides a data-driven counter-argument to the dominant narrative of AI-driven job displacement, showing that even in a field uniquely suited to AI disruption, software engineering remains resilient due to the need for deep human understanding of codebases, business contexts, and verification. The authors identify three real bottlenecks in software engineering that resist automation: deciding what to build, verifying and being accountable for deliverables, and the deep human understanding required for both. They note that AI speeds up typing code but not these core activities.

rss · Simon Willison · Jun 14, 23:54

**Background**: The WARN Act requires employers to provide advance notice of mass layoffs. In March 2025, New York added an AI disclosure checkbox to its WARN filings, asking employers whether layoffs were due to AI. In the first full year, over 160 companies filed notices, but none checked the AI box, suggesting AI is not yet a primary cause of job losses in software engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hunton.com/hunton-employment-labor-perspectives/new-york-warn-act-no-ai-related-layoffs-reported-in-first-year-of-adding-ai-related-disclosure-to-the-system">New York WARN Act: No AI-Related Layoffs Reported in First Year of Adding AI-Related Disclosure to the System</a></li>
<li><a href="https://engineering.princeton.edu/news/2025/01/13/ai-snake-oil-conversation-princeton-ai-experts-arvind-narayanan-and-sayash-kapoor">‘ AI Snake Oil’: A conversation with Princeton AI experts Arvind ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#job displacement`, `#labor economics`

---

<a id="item-8"></a>
## [US orders Anthropic to restrict two AI models](https://t.me/zaihuapd/41960) ⭐️ 8.0/10

The US Commerce Department issued an export control directive to Anthropic, ordering the company to suspend access to its Fable 5 and Mythos 5 AI models for any foreign national, both inside and outside the US. In response, Anthropic disabled access to these models for all customers, including its own foreign employees. This marks a significant escalation in government intervention in AI model distribution, setting a precedent for national security-based export controls on advanced AI. It could reshape how AI companies deploy models globally and affect international access to cutting-edge AI capabilities. Fable 5 and Mythos 5 are the same underlying model with identical weights, differing only in guardrails. Anthropic's other Claude models are not affected, and the company is working to restore access as soon as possible.

telegram · zaihuapd · Jun 15, 08:55

**Background**: The US government has increasingly used export controls to restrict the spread of advanced technologies deemed critical to national security. Anthropic's Mythos-class models, including Fable 5, represent a new tier above its Opus models, with enhanced capabilities in autonomous knowledge work and coding. The directive follows concerns that the models could be jailbroken and pose security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order">Anthropic to disable its most advanced AI models after US order...</a></li>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following... | Fortune</a></li>
<li><a href="https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519">Inside the whirlwind 24 hours that led the White House to slap export ...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#national security`, `#Anthropic`, `#export controls`, `#AI safety`

---

<a id="item-9"></a>
## [Rio 3.5 Model Exposed as Shell of Chinese Open-Source Models](https://mp.weixin.qq.com/s/0oYevRBT8PPxG5hudOXxug) ⭐️ 8.0/10

The Rio 3.5 model, previously celebrated as open-source state-of-the-art, has been revealed to be a 'shell' model combining the Nex and Qwen models. The Rio team subsequently removed the model from Hugging Face and issued an apology, claiming the uploaded version was an erroneous pre-distillation checkpoint. This incident undermines trust in the open-source AI community, as it demonstrates that claimed breakthroughs may be repackaged existing work. It also highlights the need for better provenance verification and transparency in model releases. Nex team found that after removing system prompts, Rio 3.5 identified itself as Nex 79% of the time and could reproduce Nex's unique institutional introduction. Weight analysis of 60 layers showed Rio's weights lie exactly on the line connecting Nex and Qwen, with a mixing ratio of about 0.57:0.43 and collinearity exceeding 0.98, making independent training nearly impossible.

telegram · zaihuapd · Jun 15, 12:39

**Background**: Open-source AI models are often released with claims of state-of-the-art performance, but verifying their originality is challenging. Previous incidents include Cursor's Composer 2 being revealed as actually Kimi, and Stanford team's Llama3-V being accused of copying Tsinghua's MiniCPM-Llama3-V 2.5. These cases highlight recurring issues of model provenance in the open-source community.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/mitomtuna/Rio-3.5-Open-397B-NVFP4">mitomtuna/ Rio - 3 . 5 -Open-397B-NVFP4 · Hugging Face</a></li>
<li><a href="https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B">prefeitura- rio / Rio - 3 . 5 -Open-397B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#model fraud`, `#controversy`, `#machine learning`

---