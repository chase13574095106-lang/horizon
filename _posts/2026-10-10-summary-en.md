---
layout: default
title: "Horizon Summary: 2026-10-10 (EN)"
date: 2026-10-10
lang: en
---

> From 32 items, 6 important content pieces were selected

---

1. [Cloudflare Acquires Deno, Ending Runtime Development in One Year](#item-1) ⭐️ 9.0/10
2. [Typesafe AI raises $870M at $7.5B valuation, sparking moat debate](#item-2) ⭐️ 8.0/10
3. [YouTuber Says Police Visited After He Built Camera to Track Cops](#item-3) ⭐️ 8.0/10
4. [China's FAST Telescope Discovers First Native Triple System with a Pulsar](#item-4) ⭐️ 8.0/10
5. [JetBrains Releases Mellum2.1, an Open 12B MoE Coding Model](#item-5) ⭐️ 8.0/10
6. [Telegram Desktop Flaw Allows One-Click Arbitrary File Theft](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Acquires Deno, Ending Runtime Development in One Year](https://deno.com/blog/cloudflare) ⭐️ 9.0/10

Cloudflare has acquired Deno, and per the announcement, will support the Deno runtime for another year with monthly bug-fix and security releases before ending its own development of the runtime. Deno will remain open source, with Cloudflare inviting others to continue its development. Deno was created by Node.js creator Ryan Dahl as a security-first, TypeScript-native alternative to Node.js, so its effective wind-down removes one of the main independent challengers in the JavaScript runtime space. The acquisition also continues a broader trend of developer-tooling consolidation, with Cloudflare absorbing Deno's team and technology into its Workers/workerd ecosystem. Cloudflare will keep shipping monthly bug-fix and security releases for one year, after which development stops unless another party takes over; the codebase stays open source. Deno's security model and Web Standards compliance, plus its V8-and-Rust foundation, are notable technical assets that could influence Cloudflare's workerd runtime.

hackernews · ilreb · Oct 9, 13:03 · [Discussion](https://news.ycombinator.com/item?id=50019911)

**Background**: Deno is a JavaScript and TypeScript runtime built on the V8 engine and Rust, designed with secure-by-default permissions and Web Standards compliance as core principles. It was created by Ryan Dahl, the original author of Node.js, as a response to design decisions he regretted in Node. Cloudflare Workers is a serverless platform whose runtime, workerd, also uses V8 and runs code in isolates rather than containers.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/reference/how-workers-works/">How Workers works - Cloudflare Docs</a></li>
<li><a href="https://www.imaginarycloud.com/blog/deno-vs-node">Deno vs Node . js in 2026: Which Runtime Should You Choose?</a></li>

</ul>
</details>

**Discussion**: Commenters expressed sadness and frustration, with some saying they saw this coming once Deno prioritized npm compatibility and drifted from its original vision. Others framed the event as an acquihire that effectively shuts down Deno development, and noted it as another entry in a long list of developer-tooling acquisitions.

**Tags**: `#Deno`, `#Cloudflare`, `#JavaScript`, `#Runtime`, `#Acquisition`

---

<a id="item-2"></a>
## [Typesafe AI raises $870M at $7.5B valuation, sparking moat debate](https://typesafe.ai/blog/series-ai) ⭐️ 8.0/10

Typesafe AI, a San Francisco frontier AI lab, announced an $870 million funding round at a $7.5 billion valuation, according to its company blog. The announcement triggered a heated Hacker News thread with 267 points and 206 comments questioning the company's lack of a defensible technology moat. The round highlights how AI startups with strong marketing and product execution can command multi-billion-dollar valuations even when their core models are rapidly commoditized by open-source alternatives. It also fuels the broader debate over whether the current AI investment cycle has entered a hype-driven bubble phase. Typesafe AI left stealth in September 2026 with a $40 million seed round led by DCVC and its first model, Jev, a decision model designed to make decisions within software. Community members note that Jev was quickly followed by dozens of open-source decision models, and that OpenAI's own Decisions API and Microsoft's Decision-1 model now compete directly.

hackernews · tosh · Oct 9, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50023450)

**Background**: Typesafe AI is an AI lab building machine-native intelligence infrastructure for automation, focused on decision-making within software. In the AI startup ecosystem, 'moat' refers to a defensible competitive advantage such as proprietary data, network effects, or unique technology. The Gartner AI Hype Cycle tracks how emerging AI technologies move from inflated expectations to productive use, and many observers place current AI funding in the peak-of-inflated-expectations phase.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/">Home - TypeSafe AI</a></li>
<li><a href="https://jevwiki.ai/wiki/entities/typesafe-ai.md">TypeSafe AI ( company ) — jevwiki. ai</a></li>
<li><a href="https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence">Gartner AI Hype Cycle: Why Control Now Drives AI Value</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical, arguing that Jev has virtually no moat and was duplicated by open-source models within days, with some suspecting astroturfing on Hacker News. Others defended the company, pointing to strong engineering, product talent, marketing muscle, and leadership on the latency-quality-cost curve as reasons VCs might still bet on the team.

**Tags**: `#AI`, `#funding`, `#startup`, `#venture-capital`, `#hype-cycle`

---

<a id="item-3"></a>
## [YouTuber Says Police Visited After He Built Camera to Track Cops](https://gizmodo.com/youtuber-says-cops-paid-him-a-visit-after-he-built-flock-style-camera-to-track-cops-2000824306) ⭐️ 8.0/10

A YouTuber claims that police paid him a visit after he built a Flock-style camera system designed to track police vehicles, according to a Gizmodo report. The story sparked a 216-comment Hacker News debate about ALPR surveillance, privacy, and legal reform. The incident highlights the growing tension around ALPR surveillance, as citizens begin turning the same tracking technology against law enforcement. It raises unresolved questions about whether reciprocal surveillance is legal or ethical, and whether new legislation is needed to govern who can search ALPR data. The YouTuber built a Flock-style camera to monitor police vehicles, and the reported police visit suggests authorities viewed the project as a concern. Commenters noted that Flock's system is intended to be searchable by law enforcement rather than the general public, making citizen-run tracking legally and ethically distinct.

hackernews · gumby · Oct 9, 21:06 · [Discussion](https://news.ycombinator.com/item?id=50026555)

**Background**: Flock Safety operates a network of AI-powered license plate reader (ALPR) cameras that capture images of passing vehicles and share data with police departments; as of July 2026 it says it operates in over 6,000 communities across 49 US states. ALPR systems store details such as a car's location, date, time, make, model, and color, which has fueled privacy debates. Open-source projects like DeFlock map the locations of these cameras, and police reform efforts in the US have so far produced no comprehensive federal legislation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number- plate recognition - Wikipedia</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some praised New Hampshire's law requiring deletion of non-hit plate images within three minutes and banning off-device uploads, while others argued that if Flock is allowed, legislation must tightly restrict who can search the data. Several expressed outrage at the surveillance state, and one suggested building an 'OpenFlock' to track city council members who voted for the cameras.

**Tags**: `#surveillance`, `#privacy`, `#ALPR`, `#civil-liberties`, `#law-enforcement`

---

<a id="item-4"></a>
## [China's FAST Telescope Discovers First Native Triple System with a Pulsar](https://nao.cas.cn/news/gd/202610/t20261009_8289939.html) ⭐️ 8.0/10

Chinese and European scientists independently confirmed that pulsar PSR J0435+3233, discovered by China's FAST telescope, belongs to the first known native triple star system still in its evolutionary stage, consisting of a pulsar, a white dwarf, and a Sun-like star with inner and outer orbital periods of 8 days and 73.5 years. The result was published in The Astrophysical Journal Letters on October 9, 2026. This is the first confirmed native triple system containing a pulsar, offering a rare natural laboratory for studying how pulsars form and evolve in multi-star environments. It also highlights FAST's world-leading sensitivity in discovering exotic pulsar systems, strengthening China's position in radio astronomy. The pulsar PSR J0435+3233 is a millisecond pulsar with a spin period of about 3.20 ms, discovered by FAST during the Commensal Radio Astronomy FAST Survey (CRAFTS). Its unusually high spin-down rate, two orders of magnitude greater than other known millisecond pulsars in the Milky Way, places it above the 'spin-up line' in the period–period-derivative diagram, and its gamma-ray pulsations were later detected with Fermi-LAT.

telegram · zaihuapd · Oct 9, 05:14

**Background**: Pulsars are highly magnetized, rapidly rotating neutron stars that emit beams of electromagnetic radiation from their magnetic poles, detectable when the beam sweeps past Earth. FAST, also known as Tianyan, is the world's largest single-dish radio telescope, with a 500-meter aperture located in a karst depression in Guizhou, China. A 'native' triple system means the three stars formed together and have remained gravitationally bound, rather than being captured later, making it a valuable probe of stellar evolution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.01227">The PSR J 0435 + 3233 Triple System</a></li>
<li><a href="https://english.cas.cn/newsroom/research-news/202604/t20260408_1155383.shtml">Scientists Identify Millisecond Pulsar PSR J 0435 + 3233 , Challenging...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Five-hundred-meter_Aperture_Spherical_Telescope">Five-hundred-meter Aperture Spherical Telescope - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#FAST telescope`, `#pulsar`, `#triple star system`, `#scientific discovery`

---

<a id="item-5"></a>
## [JetBrains Releases Mellum2.1, an Open 12B MoE Coding Model](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 8.0/10

JetBrains released Mellum2.1, an open-source thinking model for coding agents that uses a 12B mixture-of-experts architecture with 2.5B active parameters per token, shipped under the Apache 2.0 license with weights available on Hugging Face. The model was trained with reinforcement learning on real software-engineering tasks, allowing it to explore codebases, edit files, and verify its own changes. This is a notable move because a major IDE vendor is shipping a permissively licensed, self-hostable coding model that developers can run locally instead of relying on closed API-based agents. It strengthens the trend toward small, efficient MoE models purpose-built for agentic coding workflows, and gives the open-source community a credible alternative for building local coding agents. The model is a 'thinking' variant named JetBrains/Mellum2.1-12B-A2.5B-Thinking, and reports indicate it reaches roughly 47% on SWE-Bench, a benchmark for resolving real GitHub issues. Because only 2.5B of the 12B parameters are active per token, inference is far cheaper than a dense 12B model, making local deployment practical.

telegram · zaihuapd · Oct 9, 07:30

**Background**: Mixture-of-experts (MoE) is a machine learning technique that splits a model into multiple specialized sub-networks, or 'experts', so that only a small subset is activated for each input; this keeps total parameter count high while cutting compute per token. Reinforcement learning trains an agent by rewarding successful outcomes rather than imitating labeled examples, which suits coding agents that must explore a repository, make edits, and check whether tests pass. JetBrains' Mellum line has evolved from Mellum to Mellum2 and now Mellum2.1, reflecting the company's bet on small, self-hosted models for developer tooling.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/">JetBrains Releases Mellum2.1: A 12B MoE Open Model for Coding...</a></li>
<li><a href="https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking">JetBrains/Mellum2.1-12B-A2.5B-Thinking · Hugging Face</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#JetBrains`, `#open-source`, `#coding-agents`, `#LLM`, `#MoE`

---

<a id="item-6"></a>
## [Telegram Desktop Flaw Allows One-Click Arbitrary File Theft](https://t.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop versions below 7.2.9 contain a critical IPC record-separator injection vulnerability tracked as CVE-2026-107181, which lets attackers silently steal arbitrary local files when a user clicks a malicious tg:// link, with no confirmation prompt. The flaw was fixed in version 7.2.9, and users are urged to upgrade immediately. Because Telegram Desktop is a widely used messaging client, a one-click file-theft flaw exposes sensitive data such as browser sessions, SSH keys, and crypto wallets to remote attackers. It also enables account takeover via stolen tdata session keys, making immediate patching critical for both individual users and organizations. The vulnerability resides in Core::Sandbox and stems from unescaped semicolons in tg:// links being treated as separate IPC commands, which combined with the interpret: handler can read and upload local files to an attacker-controlled channel. A proof-of-concept has been released, and the injected command abuses an outdated internal helper originally designed for release publishing that performs no permission checks.

telegram · zaihuapd · Oct 9, 09:51

**Background**: Telegram Desktop registers the tg:// protocol handler so that links in messages or external apps can open chats, profiles, or perform actions directly in the client. Internally, the app uses inter-process communication (IPC) to pass these commands between components, and if input is not properly escaped, an attacker can smuggle extra commands into a single link. CVE-2026-107181 is exactly this kind of injection flaw, and the tdata folder it can expose stores the session keys that keep a Telegram account logged in.

<details><summary>References</summary>
<ul>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-107181">CVE-2026-107181 - Telegram Desktop before 7.2.9 IPC Record ...</a></li>
<li><a href="https://cybersecuritynews.com/poc-released-for-telegram-desktop-flaw/">PoC Released for Telegram Desktop Flaw Enabling One-Click ...</a></li>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-107181">CVE-2026-107181 : IPC Record-Separation Injection ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#Telegram`, `#CVE`, `#privacy`

---