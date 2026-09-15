---
layout: default
title: "Horizon Summary: 2026-09-15 (EN)"
date: 2026-09-15
lang: en
---

> From 26 items, 11 important content pieces were selected

---

1. [E-ink frame listens for birds and draws them as 1800s illustrations](#item-1) ⭐️ 8.0/10
2. [Internet Archive Fights Off AI Scraping Surge on Wayback Machine](#item-2) ⭐️ 8.0/10
3. [Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking](#item-3) ⭐️ 8.0/10
4. [Strix.ai AI agent found live Baseten GitHub admin token in 25 minutes](#item-4) ⭐️ 8.0/10
5. [US confirms for first time it has deployed space weapons](#item-5) ⭐️ 8.0/10
6. [Bruce Schneier: 25 Years of Mass Surveillance Is Enough](#item-6) ⭐️ 8.0/10
7. [Anthropic Accuses 7 Chinese AI Labs of Large-Scale Claude Distillation](#item-7) ⭐️ 8.0/10
8. [China's 15th Five-Year Plan Targets Advanced Chips and OpenHarmony](#item-8) ⭐️ 8.0/10
9. [US and UK Lawmakers Push Bills to Ban Superintelligent AI](#item-9) ⭐️ 8.0/10
10. [Google Opens Anthropic's Claude Opus 5 to All Engineers Internally](#item-10) ⭐️ 8.0/10
11. [MediaTek Launches Dimensity 9600 Pro on TSMC 2nm](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [E-ink frame listens for birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

Developer Arne Munthe-Kaas released 'fugleramme' on GitHub, an ESP32-powered e-ink frame that continuously listens for bird calls, identifies species using the BirdNET classifier, and displays them as 1800s-style field-guide illustrations. The project includes over 800 cut-outs covering more than 400 species and was shared on Hacker News, where it earned 1233 upvotes and 172 comments. The project demonstrates how low-power embedded hardware and open-source machine learning can be combined to create ambient, delightful experiences rather than purely utilitarian devices. It also highlights the growing ecosystem of DIY bird-monitoring tools and could inspire more builders to explore e-ink plus edge-AI projects. BirdNET is a traditional neural network rather than an LLM, trained to identify over 3,000 of the world's most common bird species from acoustic data. The frame uses e-ink for low power consumption, and community members note that BLE-based e-ink drivers can last years on a single 2000mAh battery even with multiple daily refreshes.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: BirdNET is an open-source research project from Cornell University that uses AI and neural networks to identify bird species from sound recordings. E-ink displays are reflective screens that consume power only when the image changes, making them ideal for always-on, low-maintenance devices. ESP32 is a popular low-cost microcontroller with Wi-Fi and Bluetooth, widely used in DIY IoT and hardware projects.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.hackster.io/news/this-diy-e-ink-display-brings-local-bird-sightings-to-your-wall-dd773e1558e5">This DIY E Ink Display Brings Local Bird Sightings to Your Wall</a></li>
<li><a href="https://news.ycombinator.com/item?id=49711544">Show HN: An e-ink frame that hears birds and draws them as 1800s ...</a></li>

</ul>
</details>

**Discussion**: Commenters were highly enthusiastic, calling it 'the coolest thing on HN' and praising its blend of ideas into something magical. Some noted that BirdNET is a traditional neural network, not an LLM, and others shared their own e-ink projects, highlighting the joy of simple, single-purpose devices. A few joked about IP over Avian Carriers finally being within reach.

**Tags**: `#e-ink`, `#ESP32`, `#bird-classification`, `#hardware`, `#creative-engineering`

---

<a id="item-2"></a>
## [Internet Archive Fights Off AI Scraping Surge on Wayback Machine](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

The Internet Archive published an update stating that the Wayback Machine has been hit by waves of high-volume automated traffic and that new protections have been put in place to keep the service running. The Archive believes much of this traffic comes from scrapers trying to bypass blocks on original sites by harvesting the Wayback Machine's archived copies instead. The Internet Archive is critical public infrastructure for web preservation, and sustained scraping pressure threatens its ability to keep offering free, open access to archived web pages. The incident also shows how the AI training data arms race can cause collateral damage to non-profit digital libraries, potentially pushing more sites to opt out of archiving altogether. The Archive has already seen some sites opt out of being archived as a result of the scraping, and access has not been fully consistent, though the service has maintained open access without centralized gatekeepers like Cloudflare. Some users report intermittent 429 rate-limit errors from certain networks, suggesting the new protections may affect legitimate visitors as well as bots.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**Background**: The Internet Archive is a US-based 501(c)(3) non-profit founded in 1996 that provides 'universal access to all knowledge,' most famously through the Wayback Machine, which stores snapshots of web pages over time. Web archiving preserves documents that would otherwise disappear when sites change or shut down, and the Archive has long advocated for a free and open internet. In recent years, AI companies' demand for training data has driven massive scraping of online content, raising ethical and legal questions about consent and sustainability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.facebook.com/internetnetarchive/posts/publishers-have-real-questions-about-ai-but-lets-be-clear-the-wayback-machine-is/1456103409888954/">The Wayback Machine isn't a backdoor for AI scraping. For 30 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>
<li><a href="https://www.prolific.com/resources/ai-data-scraping-ethics-and-data-quality-challenges">AI data scraping : ethics and data quality challenges | Prolific</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the Internet Archive as essential infrastructure and condemned the scrapers, with one noting that the AI arms race causes collateral damage and that regulation with hefty fines may be the only real solution. Others shared practical observations, such as intermittent 429 errors from work networks while home or phone access works fine, and appreciation that Tor access remains available without a centralized gatekeeper.

**Tags**: `#internet-archive`, `#web-scraping`, `#ai-ethics`, `#digital-preservation`, `#open-web`

---

<a id="item-3"></a>
## [Google Releases Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google has released Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, described as its most advanced live dialogue models yet, with the Extended Thinking variant adding background reasoning during live audio sessions. The base model replaces the older gemini-3.1-flash-live-preview string with gemini-3.8-live and scores 97.7% on Big Bench Audio. This is a major update to one of the most widely used voice-capable AI models, and it directly affects developers building real-time conversational agents, since they must update their client integrations and model strings. It also intensifies competition among frontier voice models, where Google has been seen as lagging behind rivals despite its data, TPU hardware, and advertising resources. The Extended Thinking variant introduces background reasoning during live audio sessions, but the thinking_level parameter is not supported for the standard gemini-3.8-live model. The base model offers near real-time visual input processing, automatic mid-conversation switching across 97 supported languages, and background tool/API execution, all at a competitive price point.

hackernews · leumon · Sep 15, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49715947)

**Background**: Gemini Live is Google's family of models designed for real-time, natural spoken conversation rather than text-only chat, and it is accessed through Google's Live API. Developers specify a model string such as gemini-3.8-live to route requests to a particular version, so new releases require client-side updates. Big Bench Audio is a benchmark used to measure audio understanding and reasoning performance of these live models.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3.8 Live Extended Thinking - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live">Learn about the Gemini 3 . 8 Live model from Google</a></li>

</ul>
</details>

**Discussion**: Commenters were largely positive, with one user praising Gemini's Afrikaans conversation and grammar lessons as the most joyful LLM use case, and another calling the release solid with good accent handling, pleasant voices, and low latency, plus usable access on a workspace account. Others were more skeptical, questioning when Gemini will overtake rivals like Fable and Astra and asking when Gemini 4 will arrive, while one user shared a phone-based demo built with LiveKit and Gemini.

**Tags**: `#Gemini`, `#AI`, `#LLM`, `#Google`, `#Model Release`

---

<a id="item-4"></a>
## [Strix.ai AI agent found live Baseten GitHub admin token in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix.ai's AI penetration-testing agent discovered a live Baseten GitHub personal access token (PAT) for the 'basetenbot' account embedded in Docker build history, gaining admin access to Baseten's production repositories within 25 minutes. The token had admin and push access to Baseten's main product repo, GitOps cluster repo, Homebrew tap, and read/write access to other private repositories. This incident highlights the growing risk of leaked credentials in CI/CD pipelines and Docker build history, and demonstrates how AI agents can automate and accelerate penetration testing to find critical vulnerabilities. It also raises ethical and legal questions about security vendors using real-world victims as marketing case studies. The token was found in Docker build history after Strix identified a Baseten image repository; Baseten made the Harbor project private and rotated the token after being notified, but the incident sparked debate over whether Strix crossed ethical lines by pulling an image and publicly naming the victim.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**Background**: Baseten is an AI inference platform for deploying and operating machine learning models in production. GitHub personal access tokens (PATs) are authentication credentials that grant access to repositories and can be leaked if embedded in Docker build arguments or environment variables, as these are stored in image history and retrievable via 'docker history'. Strix.ai is a security company that uses AI agents for automated penetration testing.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/ise/hidden-risks-of-docker-build-time-arguments-and-how-to-secure-your-secrets/">The Hidden Risks of Docker Build Time Arguments and How to Secure Your Secrets - ISE Developer Blog</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>
<li><a href="https://www.baseten.co/">Inference Platform : Deploy AI models in production | Baseten</a></li>

</ul>
</details>

**Discussion**: Commenters debated the ethics and legality of Strix's disclosure, with some praising the technical find and others criticizing the marketing tone and naming of the victim. Concerns were raised about the legality of the penetration test and the potential for similar agent-driven exploits in other organizations.

**Tags**: `#security`, `#ai-agents`, `#penetration-testing`, `#supply-chain-security`, `#github`

---

<a id="item-5"></a>
## [US confirms for first time it has deployed space weapons](https://www.bbc.com/news/articles/ck790xg41ygro) ⭐️ 8.0/10

The US has officially confirmed for the first time that it has deployed space weapons, sparking discussion on the militarization of space and its implications.

hackernews · harporoeder · Sep 15, 03:47 · [Discussion](https://news.ycombinator.com/item?id=49707473)

**Tags**: `#space weapons`, `#military technology`, `#geopolitics`, `#space policy`, `#directed energy`

---

<a id="item-6"></a>
## [Bruce Schneier: 25 Years of Mass Surveillance Is Enough](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

Bruce Schneier published a piece titled "25 Years of Mass Surveillance Is Enough," arguing that mass surveillance has become a routine law-enforcement tool and should be rolled back. The essay sparked a large Hacker News discussion with 762 points and 281 comments on privacy, policy, and resistance. Schneier is one of the most influential public-interest technologists, so his argument carries weight in policy debates over surveillance powers such as Section 702 and executive emergency orders. The scale of the community response shows sustained concern that surveillance programs are expanding rather than shrinking. Schneier's essay specifically notes that ICE uses mass surveillance in immigration enforcement and against people exercising First Amendment rights to protest, illustrating how these tools reach beyond counterterrorism. Commenters also flagged NSPM-7 as a development that could make mass surveillance significantly more pervasive.

hackernews · iamnothere · Sep 15, 11:26 · [Discussion](https://news.ycombinator.com/item?id=49710883)

**Background**: Mass surveillance in the United States has expanded since the 2001 Patriot Act era, relying on annual presidential executive orders that maintain a continuing state of national emergency. Programs justified under Section 702 of the Foreign Intelligence Surveillance Act have repeatedly been shown to collect data on Americans, and critics argue surveillance chills speech, enables discrimination, and fails to prevent terrorism.

<details><summary>References</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html">25 Years of Mass Surveillance Is Enough - Schneier on Security</a></li>
<li><a href="https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough">25 Years of Mass Surveillance Is Enough | Lawfare</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mass_surveillance_in_the_United_States">Mass surveillance in the United States - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with Schneier, with one invoking the Tao Te Ching to argue that restrictions breed the disorder they aim to prevent, and another warning that surveillance is "just getting started." Others proposed practical countermeasures: building easy-to-use self-hosted services to leverage First and Fourth Amendment protections, and limiting camera networks to local jurisdictions to prevent federal overreach.

**Tags**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-7"></a>
## [Anthropic Accuses 7 Chinese AI Labs of Large-Scale Claude Distillation](https://t.me/zaihuapd/43826) ⭐️ 8.0/10

Anthropic released a report stating that since February of this year it has detected and blocked large-scale "distillation" activities targeting Claude by seven Chinese AI labs, explicitly naming Alibaba, Zhipu, Xiaomi, SenseTime, and MiniMax. Alibaba's activity was the largest, generating over 151 million interactions between May and July — peaking at nearly 3 million per day — which Anthropic says was used to train Qwen 3.5, 3.6, and 3.7 as well as reinforcement learning environments and model architecture research, while Zhipu produced over 3.4 million interactions in just 17 days and also attempted to extract other leading U.S. models. This is one of the most concrete public accusations of cross-border model distillation to date, and it raises hard questions about how AI labs enforce usage policies, how competitive dynamics between U.S. and Chinese model developers are evolving, and what legal or ethical exposure companies face when training on a rival's outputs. The specific interaction counts and named model versions give the dispute unusual evidentiary weight, and the outcome could shape terms of service, API monitoring, and export-control debates across the industry. Anthropic frames the activity as coordinated distillation rather than ordinary API use, citing Alibaba's roughly 3 million daily interactions at peak and Zhipu's 3.4 million interactions over 17 days, and it says the data fed into Qwen 3.5, 3.6, and 3.7 plus reinforcement learning environments and architecture research. The report does not disclose the full technical evidence or the other two unnamed labs, and Anthropic has not said whether it plans legal action or further account restrictions.

telegram · zaihuapd · Sep 15, 01:02

**Background**: Knowledge distillation is a standard machine-learning technique in which a smaller model is trained to imitate the outputs of a larger, more capable one, letting developers build cheaper and faster models without training from scratch. Using a competitor's commercial API at scale to generate that training data is generally prohibited by terms of service, but detection is difficult because the traffic can look like ordinary usage. Qwen is Alibaba Cloud's family of large language models, and reinforcement learning environments are simulated settings where models learn by trial and reward.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>
<li><a href="https://snorkel.ai/blog/llm-distillation-demystified-a-complete-guide/">LLM distillation demystified: a complete guide - Snorkel AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#model distillation`, `#China AI`, `#Claude`

---

<a id="item-8"></a>
## [China's 15th Five-Year Plan Targets Advanced Chips and OpenHarmony](https://www.secrss.com/articles/93961) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology (MIIT) and the National Development and Reform Commission (NDRC) jointly issued the 15th Five-Year Plan for the electronic information manufacturing industry, laying out 17 key tasks. The plan calls for improving advanced process node capabilities, achieving breakthroughs in high-end smartphone core chips and high-performance PC chips, and strengthening the adoption of domestic operating systems such as OpenHarmony. This top-level policy directive signals that China will continue to channel significant state resources into semiconductor self-sufficiency and domestic OS ecosystems over the next five years, potentially reshaping global chip supply chains and reducing reliance on foreign technologies. It will directly affect chipmakers, device manufacturers, and software developers targeting the Chinese market. The plan sets a target of exceeding 30 trillion RMB in revenue for enterprises above designated size by 2030, with R&D investment intensity reaching 3.5%. It also promotes the development of RISC-V, AI chips and terminals, and BeiDou-related fields.

telegram · zaihuapd · Sep 15, 03:10

**Background**: Five-Year Plans are China's central economic planning documents that set national priorities for a five-year period; the 15th plan covers 2026–2030. Advanced process nodes refer to cutting-edge semiconductor fabrication technologies (e.g., 7nm, 5nm, 3nm) that determine chip performance and power efficiency. OpenHarmony is an open-source, IoT-centric operating system derived from Huawei's HarmonyOS, while RISC-V is an open-standard instruction set architecture that allows companies to design custom processors without licensing fees.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_device_fabrication">Semiconductor device fabrication - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#China tech policy`, `#semiconductors`, `#OpenHarmony`, `#RISC-V`, `#AI chips`

---

<a id="item-9"></a>
## [US and UK Lawmakers Push Bills to Ban Superintelligent AI](https://t.me/zaihuapd/43832) ⭐️ 8.0/10

US Senator Bernie Sanders announced he will introduce a "Ban Artificial Superintelligence Act" to prohibit developing AI smarter than humans and pause other advanced AI research, while UK MP Sobal introduced what is reportedly the first such bill in a G7 parliament, requiring government power to monitor and restrict superintelligent "precursor" systems. These legislative efforts mark some of the most aggressive attempts yet by major Western governments to regulate frontier AI, potentially setting precedents for global AI governance and affecting how AI labs in the US and UK develop advanced systems. Both bills also call on their governments to push for a global treaty, though passage prospects are slim; UC Berkeley professor Stuart Russell warned AI could cause a "Chernobyl-level disaster" such as coordinated disruption of financial, communications, or power grid systems.

telegram · zaihuapd · Sep 15, 04:26

**Background**: Superintelligence refers to a hypothetical software-based AI system with intellect beyond human intelligence, and its potential creation has long been debated in future-studies and AI-safety circles. Catastrophic AI risks are often grouped into categories such as malicious use, AI races, organizational risks, and rogue systems, echoing concerns raised by researchers and policymakers worldwide.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-superintelligence">What Is Artificial Superintelligence? | IBM</a></li>
<li><a href="https://safe.ai/ai-risk">AI Risks that Could Lead to Catastrophe | CAIS</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#superintelligence`, `#AI safety`, `#legislation`, `#technology policy`

---

<a id="item-10"></a>
## [Google Opens Anthropic's Claude Opus 5 to All Engineers Internally](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 8.0/10

Google has granted all of its engineers company-wide access to Anthropic's Claude (Opus 5), its most capable coding model, for internal development — but only within Google's own Antigravity development platform. Previously, Google generally barred most employees from using external coding tools such as Claude Code and OpenAI's Codex, requiring them to use its in-house Gemini instead. This is a notable reversal for a company that owns a competing frontier model, and it signals that even Google feels competitive pressure in AI coding tools. It also underscores the deepening strategic ties between Google and Anthropic, a company Google has backed and plans to invest up to $40 billion in, and could influence how other large tech firms adopt external AI models. Claude is offered as a per-employee quota supplement rather than a replacement: a Google spokesperson said Gemini remains the primary model for internal development. Access is also confined to the Antigravity platform, meaning engineers cannot freely use Claude Code or other external tools outside that environment.

telegram · zaihuapd · Sep 15, 05:31

**Background**: Claude is Anthropic's family of large language models, released in three tiers — Haiku, Sonnet, and Opus — with Opus being the most capable and aimed at demanding reasoning, coding, and long-horizon agentic work. Claude Code is Anthropic's agentic coding tool that reads a codebase, edits files, and runs commands from the terminal, IDE, or browser. Google Antigravity is Google's agent-first development platform, an evolution of the IDE designed for orchestrating AI agents rather than just writing code by hand.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://mume.ai/anthropic/claude-opus-5">Claude Opus 5 by anthropic | Mume AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Anthropic`, `#Claude`, `#Software Engineering`

---

<a id="item-11"></a>
## [MediaTek Launches Dimensity 9600 Pro on TSMC 2nm](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 8.0/10

On September 15, MediaTek unveiled the Dimensity 9600 Pro, its first flagship smartphone chip built on TSMC's 2nm process, alongside the 3nm Dimensity 9600M. The 9600 Pro features a dedicated AI processor that MediaTek says improves prompt processing and model startup performance by 51% over the previous generation, with the first phones shipping soon. This is a milestone for mobile silicon: MediaTek becomes one of the first to put TSMC's 2nm node into a smartphone chip, pushing the leading edge of semiconductor manufacturing into handsets. The 51% AI uplift also signals that on-device AI performance, not just raw CPU speed, is now a primary battleground for flagship Android phones. The 9600 Pro pairs the 2nm process with a 4.55GHz CPU and a unified 'Native AI Architecture' that fuses NPU, CPU, GPU, and ISP, and it supports 4K/240fps slow-motion video. The 9600M, by contrast, stays on a 3nm node, giving MediaTek a two-tier flagship lineup.

telegram · zaihuapd · Sep 15, 08:57

**Background**: Chip process nodes like '2nm' and '3nm' refer to the manufacturing technology used to build processors; smaller nodes generally mean more transistors packed into the same area, delivering better performance and power efficiency. TSMC's N2 is its first-generation nanosheet (gate-all-around) technology, which the company says offers roughly 10-15% higher performance at the same power or 20-30% lower power at the same performance compared with its prior N3E node. On-device AI means running AI models such as large language models directly on the phone rather than in the cloud, which requires strong dedicated neural processing hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.androidauthority.com/mediatek-dimensity-9600-pro-3711305/">The Dimensity 9600 Pro is the flagship chipset Google wishes the...</a></li>

</ul>
</details>

**Tags**: `#MediaTek`, `#Dimensity 9600 Pro`, `#TSMC 2nm`, `#mobile chips`, `#on-device AI`

---