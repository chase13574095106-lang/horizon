---
layout: default
title: "Horizon Summary: 2026-06-17 (EN)"
date: 2026-06-17
lang: en
---

> From 33 items, 10 important content pieces were selected

---

1. [U.S. science in crisis as funding and trust collapse](#item-1) ⭐️ 9.0/10
2. [Critical Path Traversal in Nezha Monitor (CVSS 9.1)](#item-2) ⭐️ 9.0/10
3. [Epic Games Open-Sources Lore VCS for Game Dev](#item-3) ⭐️ 8.0/10
4. [US delays blacklisting DeepSeek, flags 100+ Chinese firms](#item-4) ⭐️ 8.0/10
5. [GLM-5.2 tops open weights leaderboard, rivals proprietary models](#item-5) ⭐️ 8.0/10
6. [RFC 10008 Standardizes HTTP QUERY Method](#item-6) ⭐️ 8.0/10
7. [AI Demands More Engineering Discipline, Not Less](#item-7) ⭐️ 8.0/10
8. [Android 17 Released: Mandatory Large Screen, AI Features](#item-8) ⭐️ 8.0/10
9. [GitHub Copilot switches to usage-based billing in June 2026](#item-9) ⭐️ 8.0/10
10. [China Expands STAR Market Listing Rules to AI and Hard Tech](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [U.S. science in crisis as funding and trust collapse](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 9.0/10

A Scientific American article reports that the compact between U.S. science and politics is broken, leading to a researcher exodus, funding collapse, and widespread despair in the scientific community. This breakdown threatens U.S. leadership in research and innovation, as talented scientists leave the country or abandon academia, potentially causing long-term damage to national competitiveness and global scientific progress. The article highlights that grant funding has dried up, visa restrictions block foreign talent, and even established scientists are preparing backup plans. Community comments describe researchers crying, moving abroad, and labs shifting to part-time employment.

hackernews · presspot · Jun 17, 09:54 · [Discussion](https://news.ycombinator.com/item?id=48568058)

**Background**: For decades, U.S. science relied on a bipartisan consensus that federal funding for basic research was essential. Recent political polarization and budget cuts have eroded this support, while visa policies have made it harder to attract global talent. The result is a growing crisis of confidence among researchers.

**Discussion**: Comments express deep distress: one user's wife, an expert in optical traps, cries frequently and is moving abroad; another notes that grant funding and foreign student hiring have both collapsed. However, one commenter sees chaos as an opportunity for new connections and fundraising.

**Tags**: `#science policy`, `#research funding`, `#academia`, `#U.S. politics`

---

<a id="item-2"></a>
## [Critical Path Traversal in Nezha Monitor (CVSS 9.1)](https://t.me/zaihuapd/42001) ⭐️ 9.0/10

A critical unauthenticated path traversal vulnerability (CVE-2026-53519, CVSS 9.1) has been discovered in Nezha monitoring tool versions below 2.0.13, allowing attackers to read configuration files and extract JWT secrets by sending a crafted GET request such as /dashboard../data/config.yaml. This vulnerability exposes JWT secrets, enabling attackers to forge authentication tokens and gain unauthorized access to the monitoring dashboard, potentially compromising all monitored servers. Immediate patching to version 2.0.13 or later is critical for all users of this widely-used open-source tool. The vulnerability is a path traversal issue in the dashboard component, allowing directory traversal via ../ sequences. The CVSS score of 9.1 indicates critical severity, and no authentication is required to exploit it.

telegram · zaihuapd · Jun 17, 01:25

**Background**: Nezha is an open-source, lightweight server monitoring and运维 tool that consists of a dashboard and agents. Path traversal vulnerabilities allow attackers to access files outside the intended directory by manipulating file paths. JWT (JSON Web Token) is commonly used for authentication; if the secret key is leaked, attackers can forge tokens and impersonate legitimate users.

<details><summary>References</summary>
<ul>
<li><a href="https://nezha.wiki/index.html">哪吒监控 - 服务器监控与运维工具 | 使用文档</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1922425405224223705">开源、轻量、易用的服务器监控，实战部署哪吒监控 - 知乎</a></li>
<li><a href="https://blog.dejavu.moe/posts/nezha-dashboard-deploy-guide/">哪吒监控面板部署教程 | Dejavu's Blog</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#nezha`, `#path traversal`, `#CVE`

---

<a id="item-3"></a>
## [Epic Games Open-Sources Lore VCS for Game Dev](https://lore.org/) ⭐️ 8.0/10

Epic Games has open-sourced Lore, a version control system designed for scalability with large binary files and exclusive file locking, targeting game development workflows. It was previously used internally as Unreal Revision Control and is now available on GitHub. Lore directly challenges Perforce's dominance in game development by offering an open-source alternative that handles large assets and exclusive locks better than Git. This could reduce costs and vendor lock-in for game studios, and improve collaboration between artists and developers. Lore is optimized for projects combining code with large binary assets, such as textures and 3D models, and supports exclusive file locking required by artists. It is built into Unreal Editor for Fortnite and is now available under an open-source license on GitHub.

hackernews · regnerba · Jun 17, 14:30 · [Discussion](https://news.ycombinator.com/item?id=48571081)

**Background**: Version control systems (VCS) track changes to files over time. Git is widely used for code but struggles with large binary files and lacks native exclusive file locking, which is critical for game assets like 3D models where simultaneous edits can cause conflicts. Perforce (Helix Core) is the incumbent in game development, offering robust large-file support and locking, but it is proprietary and complex to administer. Lore aims to combine the best of both worlds: Git-like branching simplicity with Perforce-like scalability and locking.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/lore: Lore is a next-generation, open ...</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System</a></li>
<li><a href="https://www.theregister.com/devops/2026/06/17/git-good-with-epic-games-new-open-source-vcs-lore/5257978">Git good with Epic Games' new open source VCS, Lore</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights that Lore is a direct competitor to Perforce for game development, not a general Git replacement. Commenters note that Git's UI is user-unfriendly and that Perforce's complexity is a pain point, but some express concern about Epic's long-term commitment to the project, given it is not core to their business.

**Tags**: `#version control`, `#game development`, `#open source`, `#scalability`

---

<a id="item-4"></a>
## [US delays blacklisting DeepSeek, flags 100+ Chinese firms](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

The U.S. has delayed adding Chinese AI startup DeepSeek, memory chipmaker CXMT, and over 100 other Chinese companies to a trade blacklist, despite deeming them national security risks. This decision highlights ongoing U.S.-China tech tensions and could affect the global AI supply chain, as DeepSeek is a major open-weight AI model developer that has disrupted the industry with low-cost, high-performance models. The blacklist, known as the Entity List, restricts U.S. companies from selling goods and services to listed entities but does not prohibit buying from them. DeepSeek's models are open-weight and trained using export-restricted Nvidia GPUs.

hackernews · giuliomagnifico · Jun 17, 03:55 · [Discussion](https://news.ycombinator.com/item?id=48565498)

**Background**: DeepSeek is a Chinese AI company founded in 2023 that developed the DeepSeek-R1 model, which rivals OpenAI's GPT-4 at a fraction of the training cost. Its success has been described as a 'Sputnik moment' for the U.S., triggering concerns about China's AI capabilities despite chip export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/">Exclusive: US holds off blacklisting China's DeepSeek, more than 100 firms deemed security risks, sources say | Reuters</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/06/53241723/trump-admin-holds-off-blacklisting-deepseek-and-over-100-chinese-firms-flagged-as-security-risks">Trump Administration Holds Off Blacklisting DeepSeek And More Than 100 Chinese Companies Flagged As Secur - Benzinga</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about enforcement, with one calling it a 'Great Firewall of America' and another noting that Chinese AI firms like Z.ai are already on the Entity List with limited impact. Some users questioned the lack of a published list and debated the effectiveness of such restrictions.

**Tags**: `#AI regulation`, `#geopolitics`, `#DeepSeek`, `#US-China trade`, `#tech policy`

---

<a id="item-5"></a>
## [GLM-5.2 tops open weights leaderboard, rivals proprietary models](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) ⭐️ 8.0/10

GLM-5.2, released by Z.AI on June 13, 2026, has become the leading open weights model on the Artificial Analysis Intelligence Index, approaching frontier performance at a fraction of the cost of proprietary models like Opus 4.7. This development challenges the dominance of proprietary AI providers like Anthropic, OpenAI, and Google, offering comparable quality at drastically lower prices and potentially disrupting the AI market. GLM-5.2 supports a 1M-token context window and is designed for long-horizon agent workflows and complex multi-step automation. Community reports indicate some providers offer unlimited tokens for $50/month, with API rates up to 3x lower than official Z.AI rates.

hackernews · himata4113 · Jun 17, 09:12 · [Discussion](https://news.ycombinator.com/item?id=48567759)

**Background**: The Artificial Analysis Intelligence Index is a text-only, English-language evaluation suite that benchmarks models across quality, price, speed, and latency. Open weights models allow developers to run them on their own infrastructure, reducing reliance on proprietary APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM - 5 . 2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5 . 2 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Community members are excited about GLM-5.2's competitive pricing and performance, with some calling it a 'huge blow' to proprietary providers. However, concerns about reasoning efficiency were raised, as one user reported the model spending 15 minutes and 45k tokens on a simple coding task.

**Tags**: `#AI`, `#open source`, `#LLM`, `#benchmarks`, `#pricing`

---

<a id="item-6"></a>
## [RFC 10008 Standardizes HTTP QUERY Method](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 8.0/10

RFC 10008 introduces the QUERY HTTP method, a safe and idempotent request method that allows a request body, solving interoperability issues with using GET bodies. This new method provides a standardized way to send complex queries (e.g., large JSON filters, image inputs) without breaking caching semantics, benefiting APIs like GraphQL and search endpoints. QUERY is similar to POST but is required to be safe and idempotent, meaning it can be automatically retried without side effects. The request body is included in the cache key, which may lead to unbounded cache keys.

hackernews · schappim · Jun 17, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48568502)

**Background**: HTTP GET requests are not supposed to have a body according to RFC 9110, but some developers have been sending bodies with GET for complex queries, causing caching and interoperability issues. POST is not idempotent and triggers re-submission warnings. QUERY fills this gap by providing a safe, idempotent method with a body.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008: The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://byteiota.com/rfc-10008-http-query-method-ends-the-post-workaround/">RFC 10008: HTTP QUERY Method Ends the POST Workaround</a></li>
<li><a href="https://www.baeldung.com/cs/http-get-with-body">Why an HTTP Get Request Shouldn’t Have a Body | Baeldung on Computer Science</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the inclusion of the request body in the cache key, noting it implies an unbounded and user-controlled cache key. Some wondered if HTML forms will add support for QUERY to avoid POST re-submission warnings. Others noted that they have been sending GET bodies for years, highlighting the real-world need.

**Tags**: `#HTTP`, `#RFC`, `#protocol`, `#web`, `#caching`

---

<a id="item-7"></a>
## [AI Demands More Engineering Discipline, Not Less](https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline) ⭐️ 8.0/10

A high-scoring article argues that the rise of AI-generated code necessitates stricter engineering practices to maintain system understanding and code quality, contrary to the belief that AI reduces the need for discipline. This matters because AI is transforming software development, and without increased discipline, codebases risk becoming unmanageable, undermining long-term maintainability and team productivity. The article highlights that with AI, code becomes cheap and disposable, shifting the bottleneck from writing code to evaluating and understanding it, which requires more rigorous review and documentation.

hackernews · BerislavLopac · Jun 17, 14:20 · [Discussion](https://news.ycombinator.com/item?id=48570948)

**Background**: Traditionally, software engineering discipline involved careful code review, testing, and documentation to ensure quality. AI tools like LLMs can generate code quickly, but this code often lacks context and may introduce subtle bugs, making evaluation harder.

**Discussion**: Commenters debate the shift: some note that AI makes it harder to distinguish competent engineers from those just pasting AI output, while others emphasize that evaluation and human understanding become more critical than ever.

**Tags**: `#AI`, `#software engineering`, `#code quality`, `#engineering discipline`

---

<a id="item-8"></a>
## [Android 17 Released: Mandatory Large Screen, AI Features](https://android-developers.googleblog.com/2026/06/Android-17.html) ⭐️ 8.0/10

Android 17 has been officially released for Pixel devices, with source code available. It mandates large screen adaptation, introduces AI integration via AppFunctions for Gemini, enhances privacy controls, and shifts development to Jetpack Compose. This update fundamentally changes Android development by making large screen support mandatory and pushing AI integration at the system level. Developers must adapt their apps to new UI paradigms and privacy requirements, impacting the entire Android ecosystem. AppFunctions allows apps to expose capabilities as tools for Android MCP, enabling AI assistants like Gemini to invoke app functions. Privacy enhancements include temporary permissions and a contact picker, while local network communication now requires user authorization.

telegram · zaihuapd · Jun 17, 01:02

**Background**: Android has traditionally used a View system based on XML layouts, but Google has been promoting Jetpack Compose, a declarative UI toolkit, as the future. Large screen adaptation has been encouraged but not mandatory until now. AppFunctions is a new API that integrates with the Model Context Protocol (MCP) to enable on-device AI orchestration.

<details><summary>References</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/06/Android-17.html">Android Developers Blog: Android 17 is here</a></li>
<li><a href="https://developer.android.com/ai/appfunctions">Overview of AppFunctions | AI | Android Developers</a></li>
<li><a href="https://developer.android.com/develop/ui/compose/migrate/compare-metrics">Compare Compose and View metrics | Jetpack Compose | Android Developers</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Mobile Development`, `#AI Integration`, `#Privacy`, `#Jetpack Compose`

---

<a id="item-9"></a>
## [GitHub Copilot switches to usage-based billing in June 2026](https://t.me/zaihuapd/42003) ⭐️ 8.0/10

GitHub announced that starting June 1, 2026, GitHub Copilot will transition from flat-rate subscriptions to token-based billing, where users pay for AI processing tokens consumed. Legacy users on annual plans can keep the old pricing until their plan expires, but a new multiplier table shows GPT-5.5 requests will cost 57 times the base token rate. This pricing shift could significantly increase costs for heavy Copilot users, especially those relying on advanced models like GPT-5.5. It aligns GitHub's billing with actual compute consumption, potentially making AI coding assistants more expensive for power users while enabling more flexible usage for occasional users. Under the new model, users receive a monthly allowance of GitHub AI Credits, with each model having a token multiplier. For GPT-5.5, the multiplier is 57x, meaning one request consumes 57 times the base credits. Legacy annual plan users are exempt until their current plan ends.

telegram · zaihuapd · Jun 17, 03:16

**Background**: GitHub Copilot is an AI-powered code completion tool that suggests code snippets and functions as developers type. Previously, it charged a flat monthly or annual fee for unlimited access. The shift to token-based billing mirrors broader industry trends where AI services charge based on processing units (tokens), similar to how OpenAI and other providers bill for API usage.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans">Model multipliers for annual plans on request-based billing ...</a></li>
<li><a href="https://kalinga.ai/github-copilot-token-based-billing-guide/">GitHub Copilot Token -Based Billing : Shocking 2026 Ultimate Guide</a></li>
<li><a href="https://www.boomkas.com/blog/github-copilot-token-billing-developer-impact">The End of an Era: GitHub Copilot 's Shift to Token -Based Bil</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#pricing`, `#AI coding assistant`, `#token billing`

---

<a id="item-10"></a>
## [China Expands STAR Market Listing Rules to AI and Hard Tech](https://mp.weixin.qq.com/s/ywLPXkSlqY9S5Vwp8G5saA) ⭐️ 8.0/10

China's securities regulator announced at the 2026 Lujiazui Forum that the STAR Market's fifth set of listing standards will be expanded to cover AI, quantum computing, biomanufacturing, and embodied intelligence, allowing unprofitable hard-tech companies to go public. This policy shift provides a critical funding channel for capital-intensive AI and hard-tech startups, potentially accelerating China's technological self-sufficiency and global competitiveness, while the regulator's promise to crack down on hype aims to maintain market integrity. The fifth set of standards, previously used for biotech firms, now includes AI and other hard-tech sectors. The regulator also plans to introduce shelf offering reforms for refinancing and will issue guidelines to regulate AI use in capital markets.

telegram · zaihuapd · Jun 17, 08:30

**Background**: The STAR Market, launched in 2019, is China's Nasdaq-style board for tech companies. Its fifth set of listing standards allows pre-revenue or unprofitable companies to list if they meet certain R&D and market value thresholds. Shelf offering is a 'one approval, multiple issuances' mechanism that enables companies to raise funds flexibly over time.

<details><summary>References</summary>
<ul>
<li><a href="http://macrochina.com.cn/news_speed/hgjj/20250627123825.shtml">macrochina.com.cn/news_speed/hgjj/20250627123825.shtml</a></li>
<li><a href="https://baike.baidu.com/item/储架发行制度/1648322">储架发行制度_百度百科</a></li>
<li><a href="https://github.com/tianxingchen/Embodied-AI-Guide">GitHub - TianxingChen/Embodied-AI-Guide: [Lumina具身智能社区] 具身智能技术指南 Embodied-AI-Guide · GitHub</a></li>

</ul>
</details>

**Tags**: `#China`, `#AI regulation`, `#IPO`, `#capital markets`, `#technology policy`

---