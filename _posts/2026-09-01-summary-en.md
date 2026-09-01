---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 30 items, 6 important content pieces were selected

---

1. [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](#item-1) ⭐️ 8.0/10
2. [NAT as the Original Sin of Internet Centralization](#item-2) ⭐️ 8.0/10
3. [Claude Shared Links Indexed by Search Engines, Leaking User Data](#item-3) ⭐️ 8.0/10
4. [OpenClaw 2.0: Largest Update with 16K Pull Requests](#item-4) ⭐️ 8.0/10
5. [Apple Announces CEO Transition: Tim Cook to Step Down, John Ternus to Take Over](#item-5) ⭐️ 8.0/10
6. [Xiaomi Unveils Three Xuanjie Chips, AI Flagship SoC to Debut in Xiaomi 18 Fold](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed Manifest V2 (MV2) extensions from the Chrome Web Store, including the popular ad blocker uBlock Origin. This marks the final phase of the MV2 deprecation, with Chrome 150 and 151 eliminating workarounds that allowed MV2 extensions to continue functioning. This affects millions of users who relied on uBlock Origin for effective ad blocking, raising concerns about safety and browser monopoly. It also pressures users to migrate to alternatives like Firefox, which continues to support MV2 extensions. The Chrome Web Store no longer accepts MV2 extensions, and starting June 3, 2026, Chrome Beta, Dev, and Canary channels show warnings for installed MV2 extensions. Chrome 150 (released June 30, 2026) dropped the flag that restored MV2 installs, and Chrome 151 (stable July 28, 2026) removed the AllowLegacyMV2Extensions code path entirely. uBlock Origin received a final update on August 31, 2026, but it will no longer work in Chrome.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Manifest V3 (MV3) is the new extension platform introduced by Google to improve security, privacy, and performance, but it restricts ad-blocking capabilities by limiting the use of blocking web requests. uBlock Origin, a highly effective content blocker, relies on MV2's broader APIs, and its developer has stated that the MV3 version (uBlock Origin Lite) is less powerful. Google began phasing out MV2 in 2024, and by 2026, over 85% of actively maintained extensions have migrated to MV3.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://blog.google/chromium/manifest-v2-phase-out-begins/">Manifest V2 phase-out begins</a></li>
<li><a href="https://appuals.com/ublock-origin-not-working-manifest-v2-shutdown/">uBlock Origin Not Working in Chrome? Fixes After ... - Appuals</a></li>

</ul>
</details>

**Discussion**: Community comments express strong dissatisfaction with Google's decision, framing ad blocking as a safety issue, especially for less tech-savvy users. Many users recommend switching to Firefox, which continues to support uBlock Origin effectively, and criticize Google's unilateral control over the web.

**Tags**: `#Chrome`, `#Manifest V2`, `#ad-blocking`, `#uBlock Origin`, `#browser`

---

<a id="item-2"></a>
## [NAT as the Original Sin of Internet Centralization](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

An essay argues that Network Address Translation (NAT) is a root cause of internet centralization, sparking a discussion where the original Linux NAT implementer, Rusty Russell, acknowledges his role in eroding public endpoints. This debate highlights how a technical workaround for IPv4 address scarcity has shaped the modern internet's client-server model and centralization, affecting anyone who runs servers or values a decentralized web. Rusty Russell explains that his implementation avoided port reservation to squeeze more connections into one IP address, making incoming traffic from different addresses unroutable. The discussion also contrasts regular NAT with Carrier Grade NAT (CGNAT), which is seen as more restrictive.

hackernews · robinpie · Aug 31, 02:23 · [Discussion](https://news.ycombinator.com/item?id=49504905)

**Background**: NAT was introduced in RFC 1631 (1994) as a short-term solution to IPv4 address depletion and routing scalability. It maps multiple private IP addresses to a single public IP, conserving address space but breaking the end-to-end principle, which originally allowed any host to act as a server. This has contributed to the rise of centralized services and the client-server model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-address-translation-nat.html">What Is Network Address Translation (NAT)? - Cisco</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-nottingham-avoiding-internet-centralization-05.html">Centralization , Decentralization, and Internet Standards</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some agree that NAT is a significant factor in centralization, while others argue it's an exaggeration, noting that regular NAT is manageable and has protected insecure devices. Rusty Russell's admission adds weight to the critique, but some point out that poor UX and CGNAT are the real problems.

**Tags**: `#NAT`, `#internet architecture`, `#centralization`, `#networking`, `#history`

---

<a id="item-3"></a>
## [Claude Shared Links Indexed by Search Engines, Leaking User Data](https://t.me/zaihuapd/43511) ⭐️ 8.0/10

Anthropic's Claude shared conversation links are being indexed by search engines like Google and Bing due to missing noindex tags, exposing sensitive user data. This was confirmed by WIRED and other outlets in late July 2026. This privacy vulnerability affects thousands of users, exposing API keys, cryptocurrency wallets, personal information, and corporate secrets. It underscores the importance of proper privacy controls in AI chat features and could damage trust in Anthropic's platform. The shared links lack the 'noindex' meta tag that search engines respect, and Anthropic's robots.txt disallow rules do not remove already indexed pages. Affected data includes legal consultations, healthcare information, and social security numbers, and Anthropic has not yet fixed the issue.

telegram · zaihuapd · Aug 31, 03:22

**Background**: Claude's shared conversation feature allows users to create public links to their chats. Without a noindex tag, these links can be crawled and indexed by search engines, making them publicly discoverable. Similar issues occurred with ChatGPT about a year ago, which were quickly fixed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/private-claude-chats-exposed-in-google-and-bing-search-results/">Private Claude Chats Exposed in Google and Bing Search Results | WIRED</a></li>
<li><a href="https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/">Indexed Claude Chats Show Why Disallow Is Not Noindex</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/private-claude-conversations-have-been-indexed-by-search-engines/">Private Claude Conversations Have Been Indexed by Search Engines - CNET</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#Claude`, `#Anthropic`, `#data leak`

---

<a id="item-4"></a>
## [OpenClaw 2.0: Largest Update with 16K Pull Requests](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw released version 2.0 on August 30, its largest update ever, incorporating over 16,000 pull requests from 933 contributors, including 569 first-time participants. The update spans all aspects of the platform, from installation and messaging to memory, skills, models, browser, plugins, and security. This release marks a significant milestone for OpenClaw, a widely-used open-source project, demonstrating strong community engagement and rapid development. The comprehensive improvements, including enhanced security features like private credential requests, could attract more users and solidify its position in the AI agent ecosystem. The update includes a simplified installation process, a rebuilt browser experience, and new shared cloud sessions for multi-user collaboration. Notably, it introduces a private credential request feature that allows users to securely share credentials with an agent without exposing them in chat.

telegram · zaihuapd · Aug 31, 04:38

**Background**: OpenClaw is an open-source AI agent platform that gained viral attention when it was released late last year. A pull request (PR) is a key collaboration feature in GitHub, allowing developers to propose changes to a codebase, which maintainers review before merging. This update's scale, with over 16,000 PRs, highlights the project's active contributor base and the collaborative nature of open-source development.

<details><summary>References</summary>
<ul>
<li><a href="https://mashable.com/tech/openclaw-2-0-released-agentic-ai">OpenClaw 2 . 0 : How to try the updated AI agent, what's new | Mashable</a></li>
<li><a href="https://docs.openclaw.ai/releases/2026.8.1">v2026.8.1 (AKA OpenClaw 2 . 0 ) - OpenClaw</a></li>
<li><a href="https://docs.github.com/articles/about-pull-requests?/">Pull requests - GitHub Docs</a></li>

</ul>
</details>

**Tags**: `#OpenClaw`, `#software release`, `#open source`, `#developer tools`, `#collaboration`

---

<a id="item-5"></a>
## [Apple Announces CEO Transition: Tim Cook to Step Down, John Ternus to Take Over](https://t.me/zaihuapd/43516) ⭐️ 8.0/10

Apple has announced a leadership transition: current CEO Tim Cook will become Executive Chairman of the Board, and John Ternus, Senior Vice President of Hardware Engineering, will become CEO on September 1, 2026. The board has unanimously approved the arrangement. This marks the first CEO change at Apple in over a decade, signaling a new era for the world's most valuable company. Ternus's promotion reflects Apple's continued focus on hardware innovation, and the transition will impact product strategy, investor confidence, and the broader tech industry. Tim Cook will remain CEO through the summer to ensure a smooth transition, while current Chairman Arthur Levinson will become Lead Independent Director on September 1. John Ternus, who joined Apple in 2001 and has led hardware engineering since 2013, will also join the board on the same day.

telegram · zaihuapd · Aug 31, 10:21

**Background**: Tim Cook has served as Apple's CEO since 2011, succeeding Steve Jobs, and has overseen the company's growth into a $3 trillion market cap giant. John Ternus has been a key figure in Apple's hardware development, overseeing the iPhone, Mac, iPad, and AirPods lines. This transition is part of a planned succession process, with Cook moving to an executive chairman role to provide continuity.

**Tags**: `#Apple`, `#CEO transition`, `#Tim Cook`, `#John Ternus`, `#tech industry`

---

<a id="item-6"></a>
## [Xiaomi Unveils Three Xuanjie Chips, AI Flagship SoC to Debut in Xiaomi 18 Fold](https://t.me/zaihuapd/43524) ⭐️ 8.0/10

Xiaomi announced three new Xuanjie chips at a technical communication meeting in Beijing on August 24, 2026: the AI flagship SoC Xuanjie O3, the high-bandwidth AI accelerator Xuanjie O100, and the 3nm automotive AI chip Xuanjie D100. All three chips have completed tape-out validation and are set to power a full ecosystem of AI computing across human, vehicle, and home scenarios. This marks Xiaomi's significant expansion into self-developed silicon, covering mobile, AI acceleration, and automotive domains, which could reduce reliance on external suppliers and enhance device integration. The debut of the Xuanjie O3 in the Xiaomi 18 Fold signals Xiaomi's ambition to compete at the high end of the smartphone market with differentiated AI capabilities. The Xuanjie O3 features a ten-core all-big-core CPU with a multi-core score exceeding 15,000, and a G2-Ultra NX GPU with 85% performance improvement and 64% power reduction. It is also the world's first mobile processor to support LPDDR6 memory. The Xuanjie O100 uses 6nm wafer-on-wafer advanced packaging to achieve 1.22 TB/s bandwidth, while the Xuanjie D100 integrates 20 CPU cores and 16 NPU cores, supporting up to 160GB unified memory for local deployment of 200B-parameter models.

telegram · zaihuapd · Aug 31, 15:15

**Background**: Xuanjie is Xiaomi's self-developed chip series, aiming to build an AI computing foundation across its ecosystem. LPDDR6 is a low-power memory standard developed by JEDEC, offering higher bandwidth and efficiency compared to LPDDR5X, and is expected to be adopted in next-generation mobile processors. The automotive chip market is growing as carmakers seek to integrate advanced AI capabilities for autonomous driving.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/993/813.htm">构筑人车家 AI 算力底座，小米 玄 戒 发布三款自研芯片贯通全场景 - IT之家</a></li>
<li><a href="https://zhidx.com/p/587490.html">小米连发三个芯片大招！首秀3nm智驾芯片，玄戒O3搭折叠旗舰9月开卖 - 智东西</a></li>
<li><a href="https://www.163.com/dy/article/L55S5HBO051480KF.html">前瞻全球产业早报：小米发布国内首款3nm智驾高算力AI芯片|英伟达|机器人|hbm|chip|小米集团|知名企业|nvidia_网易订阅</a></li>

</ul>
</details>

**Tags**: `#Xiaomi`, `#chip`, `#AI`, `#SoC`, `#hardware`

---