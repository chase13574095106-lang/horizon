---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 27 items, 8 important content pieces were selected

---

1. [Kimi Releases 2.8 Trillion Parameter K3 Model with 1M Context](#item-1) ⭐️ 9.0/10
2. [Huawei Ascend 950 SuperPoD Debuts, Claims 6.7x Nvidia Performance](#item-2) ⭐️ 9.0/10
3. [First Atmosphere Detected on Rocky Exoplanet in Habitable Zone](#item-3) ⭐️ 8.0/10
4. [Firefox Runs Inside Another Browser via WebAssembly](#item-4) ⭐️ 8.0/10
5. [Truth Social to Sell Real-Time Trump Posts to Wall Street](#item-5) ⭐️ 8.0/10
6. [Trump Administration Proposes Drastic Visa Duration Cuts](#item-6) ⭐️ 8.0/10
7. [US Lawmakers Urge Ban on Chinese Memory Chips in Allied Supply Chains](#item-7) ⭐️ 8.0/10
8. [OpenAI CFO Proposes 'Useful Intelligence per Dollar' as AI ROI Metric](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi Releases 2.8 Trillion Parameter K3 Model with 1M Context](https://t.me/zaihuapd/42619) ⭐️ 9.0/10

Kimi has released K3, a 2.8 trillion parameter open-source model with a 1M-token context window, claiming performance second only to Claude Fable 5 and GPT-5.6 Sol. The model uses Kimi Delta Attention and Attention Residuals architecture with sparse Mixture of Experts, activating 16 out of 896 experts. This marks the world's first open-source model in the 3-trillion-parameter class, potentially democratizing access to frontier AI capabilities. Its novel attention architecture could influence future model designs across the industry. K3 achieves approximately 2.5x improvement in scaling efficiency over its predecessor K2. The model natively supports visual understanding and complete weights will be released in the coming days.

telegram · zaihuapd · Jul 17, 00:02

**Background**: Kimi Delta Attention is a hybrid linear attention mechanism that extends Gated DeltaNet with finer-grained gating, outperforming full attention in various scenarios. Attention Residuals allow each layer to selectively aggregate information from previous layers, improving representational capacity. Sparse Mixture of Experts (MoE) activates only a subset of experts per token, enabling large parameter counts with manageable computational cost.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-Linear">GitHub - MoonshotAI/Kimi-Linear</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: Comments discuss the 'Pelican benchmark' (SVG generation of a pelican on a bicycle) as a test for model quality, with some noting Kimi K3's tokenizer quirks suggesting a hidden system prompt. One user compared pricing and speed, finding Kimi cheapest by 5x but slowest by 2x.

**Tags**: `#AI`, `#open-source`, `#large language model`, `#Kimi`, `#Mixture of Experts`

---

<a id="item-2"></a>
## [Huawei Ascend 950 SuperPoD Debuts, Claims 6.7x Nvidia Performance](https://www.ithome.com/0/978/019.htm) ⭐️ 9.0/10

At WAIC 2026, Huawei publicly demonstrated the Ascend 950 SuperPoD (Atlas 950 SuperPoD) for the first time, claiming it delivers 1 EFLOPS FP8 and 2 EFLOPS FP4 compute power across 1,024 Ascend NPUs, achieving 6.7 times the total compute of Nvidia's NVL144 system. This marks a major milestone in AI hardware, potentially reshaping the competitive landscape between Huawei and Nvidia in high-performance AI computing, especially given geopolitical constraints on China's access to advanced chips. The SuperPoD uses Huawei's proprietary Lingqu (UnifiedBus) interconnect protocol and a supernode architecture to scale to 1,024 cards with 256 TB of unified memory. Additionally, the Ascend 384 SuperPoD has already been commercially deployed in over 750 systems across industries like internet, telecom, and finance.

telegram · zaihuapd · Jul 17, 10:27

**Background**: SuperPoD (Super Power Domain) is a high-performance computing architecture that uses high-speed interconnects to pool multiple accelerators (GPUs/NPUs) into a single logical machine, overcoming traditional PCIe bottlenecks. Huawei's Lingqu protocol is a five-layer unified interconnect designed to replace PCIe, NVLink, and RDMA, supporting up to 8,192 cards without convergence loss.

<details><summary>References</summary>
<ul>
<li><a href="https://www.toutiao.com/article/7551352889764020755/">华为全联接大会 2025：发布灵衢互联协议与多系列超节点产品，引领 AI ...</a></li>
<li><a href="https://locsic.com/zh/thinking/lingqu-unifiedbus-protocol-analysis/">灵衢协议深度分析：中国算力突围的互联赌注 — Locsic</a></li>
<li><a href="https://lucaberton.com/blog/huawei-atlas-950-superpod-ai-infrastructure/">Huawei Atlas 950 AI SuperPoD : 8,192 NPUs as One Machine</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#AI hardware`, `#Ascend 950`, `#supercomputing`, `#Nvidia competition`

---

<a id="item-3"></a>
## [First Atmosphere Detected on Rocky Exoplanet in Habitable Zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

Astronomers have detected helium escaping from LHS 1140b, a rocky exoplanet in the habitable zone of a red dwarf star 48 light-years away, marking the first confirmed atmosphere on an Earth-like planet in such a region. This discovery challenges the assumption that rocky planets around red dwarfs cannot retain atmospheres due to intense stellar radiation, and it provides a prime target for future telescopes like JWST to search for biosignatures. The detection was made using the Magellan Clay telescope, and JWST emission spectroscopy ruled out a mini-Neptune interpretation, confirming LHS 1140b is rocky. The planet is tidally locked and likely has a helium-rich atmosphere.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: Red dwarf stars are cooler and smaller than the Sun, placing their habitable zones much closer, which exposes planets to intense stellar flares and radiation. Until now, it was uncertain whether rocky planets in such harsh environments could retain an atmosphere. LHS 1140b is one of the selected targets under the Rocky Worlds Director's Discretionary Time Program.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ufl.edu/2026/07/exoplanet/">New study reveals potential atmosphere on rocky planet of nearby star</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-02200-5">Found: a rocky exoplanet with an atmosphere — could it host life?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Habitability_of_red_dwarf_systems">Habitability of red dwarf systems - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that a rocky planet around a red dwarf could retain an atmosphere, with one noting that JWST data ruled out a mini-Neptune. Others discussed future propulsion systems to reach the planet and the potential for a solar lens telescope to study such worlds.

**Tags**: `#exoplanets`, `#astronomy`, `#atmosphere`, `#JWST`, `#habitable zone`

---

<a id="item-4"></a>
## [Firefox Runs Inside Another Browser via WebAssembly](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 8.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, enabling it to run inside another browser tab with a real Firefox UI. The project used AI-assisted code translation with Claude Opus and Fable models, costing an estimated $25,000 in tokens. This demonstrates a new level of browser isolation and portability, potentially enabling secure sandboxing of entire browsers within browsers. It also showcases the practical use of AI for large-scale code translation, reducing the engineering effort required for such a feat. The demo uses the Wisp protocol over WebSocket to proxy all network traffic through Puter's servers, because WebAssembly in browsers cannot open arbitrary network connections. The project claims end-to-end encryption, and inspection confirmed that HTTPS traffic remains encrypted while HTTP traffic is in cleartext.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern browsers at near-native speed. Compiling a full browser like Firefox to Wasm is challenging because browsers are complex, multi-process applications; Firefox was chosen for its strong single-process support. The Wisp protocol is a low-overhead protocol for proxying multiple TCP/UDP sockets over a single WebSocket connection.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly - developer.puter.com</a></li>
<li><a href="https://github.com/HeyPuter/firefox-wasm">HeyPuter/firefox-wasm: Firefox in WebAssembly - GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Firefox`, `#Browser`, `#AI-assisted development`, `#WebSocket`

---

<a id="item-5"></a>
## [Truth Social to Sell Real-Time Trump Posts to Wall Street](https://www.cnn.com/2026/07/16/business/truth-social-data-wall-street) ⭐️ 8.0/10

Trump Media & Technology Group announced Truth API, a paid data feed providing millisecond-speed access to the top 10 accounts' posts on Truth Social, starting August 1, 2026, targeting high-frequency trading firms. This move directly monetizes Trump's social media posts for algorithmic trading, raising serious ethical concerns about presidential conflicts of interest and potential market manipulation, as Trump's posts have historically moved markets. The API will deliver posts from the top 10 accounts in real time, with pricing undisclosed. CNN previously reported that Trump used Truth Social to promote stocks he had just purchased.

telegram · zaihuapd · Jul 17, 01:02

**Background**: High-frequency trading (HFT) uses algorithms to execute trades in milliseconds, often relying on speed advantages. Truth Social has become Trump's primary channel for policy announcements, with posts on tariffs and geopolitical events causing significant market swings. The sale of such data to Wall Street blurs the line between presidential duties and private business interests.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hindustantimes.com/world-news/us-news/trump-media-launches-truth-api-to-give-banks-faster-access-to-truth-social-posts-101784225959242.html">Trump Media launches Truth API to give banks... | Hindustan Times</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/20982511912">高频交易（HFT）：算法交易的闪电世界 - 知乎</a></li>

</ul>
</details>

**Tags**: `#API`, `#algorithmic trading`, `#social media`, `#ethics`, `#financial markets`

---

<a id="item-6"></a>
## [Trump Administration Proposes Drastic Visa Duration Cuts](https://t.me/zaihuapd/42623) ⭐️ 8.0/10

The Trump administration proposed new regulations on Wednesday that would significantly shorten the maximum validity periods for student, exchange visitor, and media visas, with Chinese journalists limited to just 90 days. This policy could severely impact international students and researchers in STEM fields, including AI and software engineering, who rely on longer visa durations for their studies and work. It also threatens press freedom by imposing restrictive time limits on foreign journalists, especially those from China. Under the proposed rule, student and exchange visitor visas would be capped at four years, while media visas would be limited to 240 days for most countries and just 90 days for Chinese citizens. Visa holders could apply for extensions but would need to repeatedly submit additional applications.

telegram · zaihuapd · Jul 17, 04:41

**Background**: The U.S. currently hosts about 1.6 million international students on F visas, and in fiscal year 2024, issued approximately 355,000 exchange visitor visas and 13,000 media visas. The Trump administration stated the move aims to better monitor visa holders' stays as part of broader efforts to curb legal immigration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.abcdreamusa.com/f2-visa-guide/">F 2 签 证 ：美国留学陪读 签 证 大指南 - ABC Dream USA</a></li>
<li><a href="https://www.btmusa.cn/J1Project.html">J-1 交 流 访 问 者 签 证 | 美国 访 问 学者申请 - 贝特曼集团</a></li>
<li><a href="https://m.iask.sina.com.cn/b/6cK3ycOx5n3.html">美国记者和媒体签证是什么？美国记者和媒体签 – 手机爱问</a></li>

</ul>
</details>

**Tags**: `#US immigration policy`, `#visa regulations`, `#international students`, `#press freedom`, `#political impact`

---

<a id="item-7"></a>
## [US Lawmakers Urge Ban on Chinese Memory Chips in Allied Supply Chains](https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security) ⭐️ 8.0/10

US House China Committee Chairman John Moolenaar and Representative George Whitesides sent a letter to Commerce Secretary Howard Lutnick urging the addition of CXMT to the Entity List and further restrictions on YMTC, citing unacceptable national security risks from reliance on Chinese memory chips. This move could reshape global semiconductor supply chains by blocking Chinese memory chips from entering US and allied markets, potentially impacting companies like Apple and affecting AI infrastructure that relies on DRAM and NAND flash. The lawmakers also urged coordination with Japan, South Korea, and the EU to prevent Chinese memory makers from establishing footholds in allied supply chains, especially as shortages arise. They argued that purchases of Chinese memory chips could fund the PLA's dual-use technology development.

telegram · zaihuapd · Jul 17, 14:00

**Background**: CXMT is a Chinese DRAM manufacturer, while YMTC specializes in NAND flash memory. The Entity List is a US trade blacklist that restricts access to American technology without a license. These companies have been previously targeted by US export controls, but this letter seeks broader restrictions including allied supply chains.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#supply chain`, `#US-China tech war`, `#memory chips`, `#geopolitics`

---

<a id="item-8"></a>
## [OpenAI CFO Proposes 'Useful Intelligence per Dollar' as AI ROI Metric](https://openai.com/index/a-scorecard-for-the-ai-age) ⭐️ 8.0/10

OpenAI CFO Sarah Friar introduced 'useful intelligence per dollar' as a new metric for measuring AI return on investment, shifting focus from token cost to task value. The framework was presented alongside performance highlights of the newly released GPT-5.6 series, including the flagship Sol model which achieved a record in coding tasks. This metric could reshape how enterprises evaluate AI investments, emphasizing value delivered over raw cost. It also highlights the efficiency gains of advanced models like GPT-5.6 Sol, which uses 54% fewer output tokens than a leading competitor for coding tasks. The framework includes four dimensions: useful work completed, full cost per successful task, reliability of AI outputs, and whether each dollar generates more value as usage scales. Friar noted that the lowest token price does not equal the lowest task cost, as a more powerful model may get the right answer in one attempt, saving money overall.

telegram · zaihuapd · Jul 17, 15:00

**Background**: Traditionally, software ROI is measured by adoption metrics like user count or license renewals. For AI, many companies have focused on token cost per query, but this ignores the value of the work completed. The new metric aims to capture the actual business value generated by AI, encouraging investment in more capable models that may have higher per-token cost but lower overall task cost.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/">预览 GPT‑5.6 Sol：新一代模型 - OpenAI</a></li>
<li><a href="https://www.chatgpt-cnblog.com/guides/chatgpt/gpt-5.6-release-guide.html">GPT-5.6 震撼发布！Sol/Terra/Luna 三档齐发，编码超越 Claude，国内 ...</a></li>

</ul>
</details>

**Tags**: `#AI ROI`, `#OpenAI`, `#GPT-5.6`, `#productivity metrics`, `#cost efficiency`

---