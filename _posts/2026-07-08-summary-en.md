---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 29 items, 14 important content pieces were selected

---

1. [TypeScript 7.0 Announced with Up to 11.9x Speedup](#item-1) ⭐️ 9.0/10
2. [OpenAI Announces GPT-5.6 Public Launch Thursday](#item-2) ⭐️ 9.0/10
3. [Mistral Unveils Robostral Navigate for Map-Less Robot Navigation](#item-3) ⭐️ 8.0/10
4. [OpenAI Launches GPT-Live with GPT-5.5 Delegation](#item-4) ⭐️ 8.0/10
5. [OpenBSD Use-After-Free Bug Enables Local Root Escalation](#item-5) ⭐️ 8.0/10
6. [EU Revives Private Message Scanning Rules](#item-6) ⭐️ 8.0/10
7. [Cloudflare Meerkat: First Production Async Consensus](#item-7) ⭐️ 8.0/10
8. [DeepSeek Develops Own AI Chip to Reduce Reliance on Nvidia and Huawei](#item-8) ⭐️ 8.0/10
9. [SpaceXAI to Release Grok 4.5 Tomorrow](#item-9) ⭐️ 8.0/10
10. [Top AI Firms Get Poor Safety Ratings, Anthropic Leads with C+](#item-10) ⭐️ 8.0/10
11. [Huawei 5G flagship returns overseas with peak speed over 1100 Mbps](#item-11) ⭐️ 8.0/10
12. [Critical Android Remote Root Exploit Chain Disclosed](#item-12) ⭐️ 8.0/10
13. [Meituan OWL (LongCat) Free Test Model Suspected of Leaking Chat Data](#item-13) ⭐️ 8.0/10
14. [Smartphone apps identified via leaked EM signals with 99% accuracy](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 Announced with Up to 11.9x Speedup](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft announced TypeScript 7.0, a major version release that delivers dramatic performance improvements, achieving up to 11.9x speedup on large codebases like VS Code (from 125.7s to 10.6s). This release significantly reduces compilation times for large TypeScript projects, improving developer productivity and making TypeScript more viable for even larger codebases. It also demonstrates Microsoft's continued investment in the language's performance. The speedups were measured on several codebases: VS Code (11.9x), Sentry (8.9x), Bluesky (8.7x), Playwright (8.7x), and tldraw (7.7x). However, some users noted compatibility issues with tools like ts-jest, requiring workarounds.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, widely used for large-scale web development. Performance has been a long-standing pain point, especially for projects with millions of lines of code. This release focuses on optimizing the compiler and language service.

**Discussion**: The community is largely positive, celebrating the performance gains and the team's effort. However, some users raised concerns about compatibility with common tools like ts-jest and the complexity of managing multiple tsconfig files for projects with mixed environments (e.g., web app with Node.js tooling).

**Tags**: `#TypeScript`, `#performance`, `#programming languages`, `#Microsoft`

---

<a id="item-2"></a>
## [OpenAI Announces GPT-5.6 Public Launch Thursday](https://x.com/OpenAI/status/2074704958419792299) ⭐️ 9.0/10

OpenAI has announced the public release of the GPT-5.6 series, including Sol, Terra, and Luna, on Thursday, July 9, 2026, with global preview access being expanded immediately. This release marks a significant leap in AI capabilities, with Sol setting new benchmarks in reasoning, coding, and cybersecurity, potentially reshaping enterprise and developer workflows. Sol is the flagship model for frontier reasoning and long-horizon agentic tasks, while Terra offers balanced performance at 2x lower cost than GPT-5.5, and Luna is the fastest, most affordable option.

telegram · zaihuapd · Jul 8, 04:17

**Background**: GPT-5.6 is the latest iteration of OpenAI's large language model series. The three models—Sol, Terra, and Luna—are designed for different use cases: Sol for advanced reasoning and agentic work, Terra as a cost-effective general-purpose model, and Luna for high-speed, low-cost inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/gpt-5-6-release-date-features-benchmarks-2026">GPT-5.6: Public Launch July 9 — Sol, Terra, Luna - explainx.ai</a></li>
<li><a href="https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna/1384931">Introducing GPT-5.6 series: Sol, Terra and Luna</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**Tags**: `#GPT-5.6`, `#OpenAI`, `#AI release`, `#large language model`

---

<a id="item-3"></a>
## [Mistral Unveils Robostral Navigate for Map-Less Robot Navigation](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI has released Robostral Navigate, an 8-billion-parameter model that enables robots to navigate complex environments using only a single RGB camera and natural language instructions, achieving 76.6% on the R2R-CE benchmark without depth sensors, LiDAR, or multiple cameras. This marks Mistral's first formal product for embodied AI, extending its reach from language models into physical systems, and could lower the cost and complexity of robotics navigation for hobbyists and researchers by eliminating the need for expensive sensors and pre-built maps. The model is not openly available, which limits hobbyist experimentation; however, it addresses the 'kidnapped robot' problem by enabling map-less navigation from a single camera feed, a significant advancement over traditional map-based approaches.

hackernews · ottomengis · Jul 8, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48832212)

**Background**: Map-less navigation allows robots to move through unknown environments without a pre-built map, using real-time sensor data to avoid obstacles and reach goals. Traditional approaches often rely on expensive sensors like LiDAR or multiple cameras, while Mistral's model uses only a single RGB camera, making it more accessible. The 'kidnapped robot' problem refers to a robot losing its localization after being moved without its knowledge, which map-less methods can overcome.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://alphasignal.ai/news/mistral-s-robostral-navigate-beats-sensor-heavy-robots-with-just-one-camera">Mistral's Robostral Navigate Beats Sensor-Heavy Robots With ...</a></li>
<li><a href="https://www.siliconreport.com/mistral-ai-releases-robostral-navigate-a-single-camera-robotics-model-95dac18d">Mistral AI Releases Robostral Navigate, a Single-Camera ...</a></li>

</ul>
</details>

**Discussion**: The community is excited about the map-less navigation capability and its potential for hobbyist projects like farm robots, but disappointed that the model is not openly available. Some commenters note that map-less outdoor navigation has existed, but indoor map-less navigation is relatively new, and they speculate about the underlying technology similar to Stanford's PIGEON model.

**Tags**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-4"></a>
## [OpenAI Launches GPT-Live with GPT-5.5 Delegation](https://openai.com/index/introducing-gpt-live/) ⭐️ 8.0/10

OpenAI has introduced GPT-Live, a new voice mode for ChatGPT that can delegate complex reasoning tasks to GPT-5.5 in the background, enabling more natural and productive conversations. The feature is now available globally. GPT-Live bridges the gap between voice interaction and frontier-level reasoning, allowing users to have extended, productive conversations without being limited by older voice models. This could significantly enhance AI-assisted work, brainstorming, and research. GPT-Live can delegate questions requiring web search or harder reasoning to GPT-5.5, which runs in the background while the conversation continues. Early testers reported hour-long conversations with effective brainstorming, though some noted limitations in tool integration and occasional interruption bugs.

hackernews · logickkk1 · Jul 8, 17:03 · [Discussion](https://news.ycombinator.com/item?id=48834405)

**Background**: Previous voice modes in ChatGPT used models that were several generations behind the frontier, limiting their reasoning capabilities. GPT-5.5 is OpenAI's latest frontier reasoning model, capable of extended thinking and near-frontier performance on complex tasks. GPT-Live combines the responsiveness of a dedicated voice model with the power of GPT-5.5 through background delegation.

<details><summary>References</summary>
<ul>
<li><a href="https://pulse2.com/openai-introduces-gpt-live-to-power-more-natural-chatgpt-voice-interactions/">OpenAI Introduces GPT-Live To Power More Natural ChatGPT ...</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-live-chatgpt-voice-full-duplex">OpenAI's GPT-Live: ChatGPT voice that listens and talks - TNW</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were generally positive, with one user praising hour-long brainstorming sessions. However, some expressed concerns about AI replacing human relationships, and others noted the lack of tool/connector support in voice mode as a missed opportunity.

**Tags**: `#AI`, `#voice mode`, `#OpenAI`, `#GPT-5.5`, `#Hacker News`

---

<a id="item-5"></a>
## [OpenBSD Use-After-Free Bug Enables Local Root Escalation](https://nvd.nist.gov/vuln/detail/cve-2026-57589) ⭐️ 8.0/10

A use-after-free vulnerability (CVE-2026-57589) in OpenBSD through version 7.9 allows a local attacker to escalate privileges to root. The bug was discovered as part of OpenAI's Patch The Planet initiative in collaboration with Trail of Bits. This vulnerability is significant because OpenBSD is renowned for its security focus, and a local privilege escalation to root undermines its core security guarantees. The discovery also highlights the growing role of AI-assisted vulnerability research in finding bugs in even the most hardened systems. The use-after-free occurs during a context switch after a tsleep call, leading to memory corruption that can be exploited for privilege escalation. The vulnerability has a CVSS score of 8.0, indicating high severity, though it requires local access to exploit.

hackernews · linggen · Jul 8, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48831658)

**Background**: A use-after-free vulnerability occurs when a program continues to use a memory pointer after the memory has been freed, potentially allowing an attacker to execute arbitrary code. OpenBSD is a Unix-like operating system that prioritizes security, famously claiming only two remote holes in the default install in over two decades. Local privilege escalation means an attacker with limited user access can gain full root control of the system.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48831658">OpenBSD has a use-after-free allowing local privilege escalation ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed mixed reactions: some praised OpenBSD's security culture for having so few bugs, while others questioned why the vulnerability wasn't listed on OpenBSD's security page. The involvement of AI-assisted discovery (Patch The Planet) sparked debate about the effectiveness of such tools in finding vulnerabilities in security-focused OSes.

**Tags**: `#security`, `#OpenBSD`, `#vulnerability`, `#privilege escalation`, `#AI-assisted security`

---

<a id="item-6"></a>
## [EU Revives Private Message Scanning Rules](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 8.0/10

The European Parliament has approved an urgent procedure to fast-track legislation that would revive the expired 'Chat Control 1.0' rules, allowing online platforms to voluntarily scan private messages for child sexual abuse material (CSAM). A decisive vote is scheduled for July 9. This move threatens end-to-end encryption (E2EE) by enabling client-side scanning, which could undermine privacy for all EU citizens. If passed, it may set a precedent for other regions to adopt similar surveillance measures. The vote was 331 in favor and 304 against, showing a narrow margin. Critics warn that 'Chat Control 2.0' would mandate scanning and ban E2EE, while the current proposal only permits voluntary scanning.

hackernews · ggirelli · Jul 8, 16:53 · [Discussion](https://news.ycombinator.com/item?id=48834296)

**Background**: End-to-end encryption (E2EE) ensures that only the sender and intended recipient can read messages, preventing third parties—including service providers—from accessing content. Governments and child protection groups argue that E2EE hinders investigations into CSAM, while privacy advocates warn that scanning mechanisms create backdoors that could be exploited for mass surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/">EU now one step away from reviving private message scanning rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption</a></li>
<li><a href="https://cybernews.com/security/chat-control-eu-scanning-messages/">Will the EU start scanning your private messages? - Cybernews</a></li>

</ul>
</details>

**Discussion**: Community comments express strong opposition, with users highlighting the involvement of the Internet Watch Foundation in pushing client-side scanning. Some note that 'Chat Control 1.0' allows voluntary scanning (already expected for platforms like Facebook), while 'Chat Control 2.0' is the real threat. A call to action urges EU citizens to contact their representatives via fightchatcontrol.eu.

**Tags**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#technology policy`

---

<a id="item-7"></a>
## [Cloudflare Meerkat: First Production Async Consensus](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare announced Meerkat, a globally distributed consensus algorithm based on QuePaxa, which achieves asynchronous consensus without relying on timeouts. This is the first production implementation of an asynchronous consensus algorithm. Meerkat could significantly improve the robustness of distributed systems under adverse network conditions, as it does not depend on timeouts for liveness. This is particularly valuable for global-scale services like Cloudflare's, where network delays can vary wildly. Meerkat is based on QuePaxa, a randomized asynchronous consensus protocol that uses hedging instead of timeouts to achieve efficiency comparable to leader-based protocols under normal conditions. The algorithm requires global consensus for every operation, including reads, which may introduce higher latency for read-heavy workloads.

hackernews · bobnamob · Jul 8, 13:18 · [Discussion](https://news.ycombinator.com/item?id=48831565)

**Background**: Traditional consensus algorithms like Paxos and Raft rely on timeouts to detect failures and ensure progress, making them partially synchronous. Asynchronous consensus algorithms, such as QuePaxa, do not require timeouts and can make progress even under arbitrary network delays, but they have historically been less efficient in normal cases. Meerkat aims to bridge this gap by providing a practical implementation of an asynchronous protocol.

<details><summary>References</summary>
<ul>
<li><a href="https://bford.info/pub/os/quepaxa/">QuePaxa: Escaping the Tyranny of Timeouts in Consensus – Bryan Ford's Home Page</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Pasindu Tennage* EPFL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Consensus_(computer_science)">Consensus (computer science) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that Meerkat is the first production implementation of an asynchronous consensus algorithm, which is a significant milestone. Some commenters note that requiring global consensus for reads may limit its use to niche applications, while others argue it could be very useful for messy networks where leader-based protocols struggle.

**Tags**: `#distributed systems`, `#consensus algorithms`, `#Cloudflare`, `#asynchronous consensus`, `#QuePaxa`

---

<a id="item-8"></a>
## [DeepSeek Develops Own AI Chip to Reduce Reliance on Nvidia and Huawei](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

Three sources revealed that Chinese AI company DeepSeek is developing its own AI chip focused on inference, aiming to reduce dependence on Nvidia and Huawei chips. The effort began about a year ago and is still in early stages, with DeepSeek recruiting chip design engineers and engaging with design, foundry, and memory companies. This strategic move could reshape the AI hardware landscape in China, especially under US export restrictions that limit access to advanced chips. If successful, DeepSeek could reduce its vulnerability to supply chain disruptions and potentially offer a competitive alternative to Nvidia and Huawei in the inference chip market. The chip is designed specifically for inference, not training, which is a less computationally intensive but high-volume task. DeepSeek has already started recruiting chip design engineers in recent months and is in talks with chip design, foundry, and memory companies.

telegram · zaihuapd · Jul 8, 05:20

**Background**: DeepSeek is a Chinese AI company known for developing cost-effective large language models like DeepSeek-R1, which rival OpenAI's GPT-4. The company has previously relied on Nvidia H800 and Huawei Ascend chips, but US export controls have restricted access to advanced AI chips, prompting Chinese firms to seek domestic alternatives. Inference chips are specialized for running trained models to generate responses, as opposed to training chips used for model development.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/">Facing US export controls, China's DeepSeek plans to make its own chips - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#inference`, `#export controls`

---

<a id="item-9"></a>
## [SpaceXAI to Release Grok 4.5 Tomorrow](https://x.com/elonmusk/status/2074740539874775163) ⭐️ 8.0/10

SpaceXAI announced it will publicly release Grok 4.5, an Opus-level model that is faster, more token-efficient, and cheaper, starting tomorrow. This release marks the first public model from SpaceXAI since its IPO, potentially intensifying competition in the frontier AI market by offering a high-performance model at lower cost. Grok 4.5 is described as an 'Opus-class' model, a tier typically associated with Anthropic's Claude Opus series, but with improved speed and efficiency. Benchmarks show it excels in STEM and knowledge work, though its pricing is premium.

telegram · zaihuapd · Jul 8, 07:09

**Background**: Opus-level models refer to Anthropic's Claude Opus line, known for deep reasoning and coding capabilities. SpaceXAI, founded by Elon Musk, has been developing the Grok series as a competitor to models like GPT-4 and Claude. The company went public several weeks ago, and Grok 4.5 is its first major release since then.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/">SpaceXAI releases Grok 4.5, which Elon describes as an 'Opus ...</a></li>
<li><a href="https://cursor.com/blog/grok-4-5">Introducing Grok 4.5 - Cursor</a></li>
<li><a href="https://benchable.ai/models/x-ai/grok-4.5-20260708">xAI: Grok 4.5 - AI Model Details & Benchmarks</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Grok`, `#SpaceXAI`

---

<a id="item-10"></a>
## [Top AI Firms Get Poor Safety Ratings, Anthropic Leads with C+](http://z.ai/) ⭐️ 8.0/10

The Future of Life Institute's latest AI Safety Index, released in February 2026, grades nine leading AI companies on their safety practices, with no company receiving an A. Anthropic tops the list with a C+, while OpenAI and Google DeepMind get C, Meta gets D+, and xAI, DeepSeek, and Mistral receive F. This report highlights systemic failures in risk management among the most influential AI developers, raising concerns about the industry's ability to self-regulate. The findings could pressure governments to accelerate AI safety regulations and increase public scrutiny of companies' military AI collaborations. The index evaluates companies on six safety domains: testing, transparency, misuse controls, governance, and more. Many companies have shifted their policies to allow military use of their AI, which the report flags as a risk factor.

telegram · zaihuapd · Jul 8, 11:30

**Background**: The Future of Life Institute is a nonprofit that advocates for responsible AI development. Its AI Safety Index aims to provide an independent assessment of how well leading AI labs are addressing catastrophic risks. The report comes amid growing global debate over AI safety and the ethics of military AI applications.

<details><summary>References</summary>
<ul>
<li><a href="https://futureoflife.org/ai-safety-index-winter-2025/">AI Safety Index: Winter 2025 - Future of Life Institute</a></li>
<li><a href="https://time.com/article/2026/07/07/ai-safety-rankings-openai-anthropic-meta/">The Latest AI Safety Rankings Are In. Nobody Gets an A - TIME</a></li>
<li><a href="https://www.latimes.com/entertainment-arts/business/story/2025-12-05/ai-artificial-intelligence-company-scorecard-ranks-safety-humanity">A safety report card ranks AI company efforts to protect ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#industry report`, `#risk management`

---

<a id="item-11"></a>
## [Huawei 5G flagship returns overseas with peak speed over 1100 Mbps](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

Huawei's Pura 90 Pro Max international version natively supports 5G, with overseas tests showing peak download speeds exceeding 1100 Mbps, marking the return of Huawei's 5G flagship to overseas markets after seven years of US sanctions. This signals Huawei's successful breakthrough in 5G chip supply and its strategic comeback in the global smartphone market, potentially reshaping competition with Apple and Samsung in high-end segments. The device runs HarmonyOS 6.0.0.125 and features 5A communication technology, which Huawei clarifies is not a new network standard but a branding for advanced connectivity experience, including faster access and lower latency.

telegram · zaihuapd · Jul 8, 12:17

**Background**: Since 2019, US sanctions prevented Huawei from using 5G chips and Google Mobile Services, crippling its overseas phone business. In 2023, the Mate 60 series surprised the market with a domestically produced 5G chip, and subsequent updates like HarmonyOS 6.0.0.125 introduced 5A branding, laying the groundwork for the international 5G comeback.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://news.qq.com/rain/a/20260107A02IIR00">华为 Mate 60 等机型获 HarmonyOS 6.0.0.125 升级，实装 5A 通信</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#5G`, `#smartphones`, `#US sanctions`, `#telecommunications`

---

<a id="item-12"></a>
## [Critical Android Remote Root Exploit Chain Disclosed](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Security firm Nebula disclosed a remote root exploit chain called IonStack that compromises Android devices up to version 17 via a single malicious URL click, combining a Firefox browser vulnerability and a 15-year-old Linux kernel flaw (CVE-2026-43499, GhostLock). A proof-of-concept has been released on GitHub. This is the first public root exploit for Android 17, demonstrating that even the latest Android version is vulnerable to remote compromise. The attack requires no user interaction beyond clicking a link, making it highly dangerous for all Android users. The exploit chain uses a Firefox browser vulnerability (affecting Firefox 151.0.2 and earlier) to achieve initial code execution, then leverages the GhostLock Linux kernel vulnerability for privilege escalation to root. The Linux kernel has already been patched, but Android devices may not receive updates promptly.

telegram · zaihuapd · Jul 8, 13:01

**Background**: Android security relies on sandboxing and permission models to isolate apps and limit damage from exploits. A remote root exploit bypasses these protections entirely, giving an attacker full control over the device. The GhostLock vulnerability is a use-after-free bug in the Linux kernel's rt_mutex code, present since 2011.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>
<li><a href="https://cybersecuritynews.com/15-year-old-ghostlock-linux-kernel-vulnerability/">15-year-old GhostLock Linux Kernel Vulnerability Enables ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-13"></a>
## [Meituan OWL (LongCat) Free Test Model Suspected of Leaking Chat Data](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

Meituan's OWL (LongCat) free test model on OpenRouter is suspected of leaking user conversation data, with exposed data appearing in a now-private GitHub repository. The repository was publicly accessible at least until July 7, 2026, and was later detected by a Discord bot token scanner. This incident highlights significant privacy risks in using free AI models, especially from major companies like Meituan, as user conversations may be exposed. It underscores the need for users to avoid sharing sensitive information like API keys or private data with large language models. The leaked data was found in a GitHub repository that has since been made private, and the exposure was flagged by a Discord bot token scanner that automatically detects and revokes exposed tokens. The OWL model is the free test version of Meituan's LongCat-2.0, a 1.6-trillion-parameter MoE model that previously topped OpenRouter rankings under the alias Owl Alpha.

telegram · zaihuapd · Jul 8, 13:35

**Background**: Meituan's LongCat-2.0 is a 1.6-trillion-parameter Mixture-of-Experts (MoE) model open-sourced under the MIT license, trained entirely on domestic Chinese chips. The OWL model was offered as a free test model on OpenRouter, a platform that aggregates various AI models. Similar incidents have occurred with other providers like Google and DeepSeek, where user data may be used for model improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://aitoolsrecap.com/Blog/longcat-2-meituan-open-source-chinese-chips-2026">LongCat-2.0: The 1.6T Open-Source AI That Was Secretly ...</a></li>
<li><a href="https://www.opensourceforu.com/2026/06/meituan-open-sources-longcat-2-0-under-mit-license/">Meituan Open Sources LongCat-2.0 Under MIT License</a></li>
<li><a href="https://longcat.chat/blog/longcat-2.0/">Introducing LongCat-2.0</a></li>

</ul>
</details>

**Discussion**: The community expressed concern over the data leak, with many users warning others not to input sensitive information into large language models. Some noted that this incident reinforces the importance of treating conversation logs as sensitive data assets.

**Tags**: `#data leak`, `#AI security`, `#LLM`, `#Meituan`, `#privacy`

---

<a id="item-14"></a>
## [Smartphone apps identified via leaked EM signals with 99% accuracy](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

Chinese researchers developed a non-contact forensic technique that identifies smartphone apps and user actions by analyzing low-frequency electromagnetic emissions leaked during device operation, achieving up to 99.07% accuracy on iPhone 15 Pro, Xiaomi 15 Pro, and OPPO Reno 13. This side-channel attack works even when the phone is offline, in flight mode, encrypted, or locked, posing a serious privacy threat as it requires no access to the device's operating system or stored data. The method targets low-frequency electromagnetic signals (below 1 MHz) emitted by smartphone components like power management ICs and displays, and uses machine learning to classify app-specific patterns. The study was published in the peer-reviewed journal Radioengineering on May 22.

telegram · zaihuapd · Jul 8, 16:05

**Background**: A side-channel attack exploits unintended information leakage from a system's physical operation, such as timing, power consumption, or electromagnetic emissions. Unlike traditional cyberattacks that target software vulnerabilities, side-channel attacks analyze physical byproducts to infer sensitive data. This technique is similar to TEMPEST attacks, which recover signals from electronic equipment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side-channel attack</a></li>
<li><a href="https://www.nationpress.com/sciencetech/china-researchers-id-apps-via-phone-radio-leak">Chinese researchers crack smartphone app ID via radio signals</a></li>
<li><a href="https://www.newsbang.com/news/article/story_id-p008-155706">Chinese Researchers Identify Smartphone Apps via Leaked ...</a></li>

</ul>
</details>

**Tags**: `#side-channel attack`, `#smartphone security`, `#electromagnetic signals`, `#privacy`, `#forensics`

---