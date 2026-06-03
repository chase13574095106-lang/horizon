---
layout: default
title: "Horizon Summary: 2026-06-03 (EN)"
date: 2026-06-03
lang: en
---

> From 30 items, 11 important content pieces were selected

---

1. [Elixir v1.20 Introduces Gradual Typing](#item-1) ⭐️ 9.0/10
2. [Soundbar Hacked via Bluetooth to Act as Keyboard](#item-2) ⭐️ 9.0/10
3. [Let's Encrypt Plans Post-Quantum Merkle Tree Certificates](#item-3) ⭐️ 9.0/10
4. [HTTP/2 Bomb DoS Attack Threatens Major Web Servers](#item-4) ⭐️ 9.0/10
5. [Google's Gemma 4 12B: Encoder-Free Multimodal Model](#item-5) ⭐️ 8.0/10
6. [DaVinci Resolve 21 Adds Photo Management, Motion Graphics](#item-6) ⭐️ 8.0/10
7. [Uber Caps AI Tool Spending at $1,500/Month per Tool](#item-7) ⭐️ 8.0/10
8. [Espressif Announces ESP32-S31 RISC-V SoC with SIMD and Bitscrambler](#item-8) ⭐️ 8.0/10
9. [SpaceX Plans $75B Fixed-Price IPO at $135 Per Share](#item-9) ⭐️ 8.0/10
10. [Massive Proxy Service Blocking by GFW on March 4](#item-10) ⭐️ 8.0/10
11. [Google lets websites opt out of AI search results](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Elixir v1.20 Introduces Gradual Typing](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) ⭐️ 9.0/10

Elixir v1.20, released on June 3, 2026, introduces gradual typing, allowing developers to optionally add type annotations to their code for static type checking. This marks a major evolution for Elixir, bridging the gap between dynamic and static typing, which can improve code reliability and developer productivity without sacrificing the language's dynamic flexibility. The gradual type system is based on the 'Strong Arrows' approach, which aims to provide soundness and performance. It is initially opt-in, meaning existing codebases remain unaffected until type annotations are added.

hackernews · cloud8421 · Jun 3, 19:02 · [Discussion](https://news.ycombinator.com/item?id=48388324)

**Background**: Elixir is a dynamic, functional language built on the Erlang VM. Gradual typing allows mixing typed and untyped code, enabling a smooth transition from dynamic to static typing. This feature has been long anticipated by the community.

<details><summary>References</summary>
<ul>
<li><a href="https://elixir-lang.org/blog/2023/09/20/strong-arrows-gradual-typing/">Strong arrows: a new approach to gradual typing - The Elixir ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gradual_typing">Gradual typing - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is largely excited, with long-time developers praising the addition. Some users compare it to Dialyzer's success typing, while others express concerns about potential performance overhead or the complexity of gradual typing in practice.

**Tags**: `#Elixir`, `#gradual typing`, `#programming languages`, `#type systems`

---

<a id="item-2"></a>
## [Soundbar Hacked via Bluetooth to Act as Keyboard](https://blog.nns.ee/2026/06/03/katana-badusb/) ⭐️ 9.0/10

A researcher exploited a Bluetooth firmware update vulnerability in the Creative Sound Blaster Katana V2X soundbar to reflash its firmware without authentication, turning it into a keyboard that can inject keystrokes into a connected PC. This demonstrates a novel attack vector where a seemingly innocuous peripheral (a soundbar) can be weaponized remotely via Bluetooth, bypassing traditional security assumptions. It highlights the risks of insecure firmware update mechanisms and vendor negligence in addressing vulnerabilities. The attack requires no pairing or user interaction; the soundbar is connected to the host PC via USB, and the researcher added a USB HID descriptor to make it recognized as a keyboard. The vendor, Creative, reportedly did not consider this a security vulnerability.

hackernews · xx_ns · Jun 3, 10:53 · [Discussion](https://news.ycombinator.com/item?id=48382310)

**Background**: BadUSB is a class of attacks where a USB device emulates a keyboard to inject keystrokes. The Creative Sound Blaster Katana V2X is a soundbar that supports firmware updates over Bluetooth. The researcher reverse-engineered the update protocol and found it lacked authentication, allowing arbitrary firmware to be flashed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BadUSB">BadUSB - Wikipedia</a></li>
<li><a href="https://support.creative.com/Products/ProductDetails.aspx?prodID=23937&prodName=Sound+Blaster+Katana+V2X">Creative Worldwide Support - Sound Blaster Katana V 2 X</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Creative's dismissal of the vulnerability, with one noting that SingCERT was told it 'does not present a cybersecurity risk.' Others speculated about broader implications, such as supply chain worms, and praised the researcher for publishing a third-party patch.

**Tags**: `#security`, `#vulnerability`, `#bluetooth`, `#firmware`, `#badusb`

---

<a id="item-3"></a>
## [Let's Encrypt Plans Post-Quantum Merkle Tree Certificates](https://letsencrypt.org/2026/06/03/pq-certs) ⭐️ 9.0/10

Let's Encrypt announced plans to adopt Merkle Tree Certificates (MTCs) for post-quantum security, addressing the near-term risk of quantum code cracking. This marks a major shift in web PKI infrastructure. This transition is significant because it proactively addresses the threat of quantum computers breaking current public-key cryptography, which could compromise all TLS-secured communications. If successful, it will set a new standard for web security and trust. Merkle Tree Certificates are smaller than today's certificates, as the handshake includes only one signature, one public key, and one inclusion proof. They also make transparency a built-in property of issuance, unlike the current bolted-on Certificate Transparency system.

hackernews · SGran · Jun 3, 15:06 · [Discussion](https://news.ycombinator.com/item?id=48385114)

**Background**: Post-quantum cryptography aims to develop cryptographic systems that are secure against both classical and quantum computers. Current public-key algorithms like RSA and ECC are vulnerable to Shor's algorithm running on a sufficiently powerful quantum computer. Merkle Tree Certificates are a novel approach that uses Merkle trees to aggregate certificates, reducing handshake size and enabling efficient post-quantum signatures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digicert.com/blog/google-merkle-tree-certificates">How Google's Merkle Tree Certificates Reshape Web Trust | DigiCert</a></li>
<li><a href="https://www.infoq.com/news/2025/11/cloudflare-merkle-tree-certifica/">Cloudflare Proposes Merkle Tree Certificates to Solve Post - Quantum ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is engaged and generally positive, with comments highlighting the science-fiction nature of planning for quantum threats and the technical challenges of transitioning. Some users discuss hybrid constructions and the trade-offs of moving away from battle-tested systems like ed25519.

**Tags**: `#post-quantum cryptography`, `#Let's Encrypt`, `#TLS`, `#Merkle Tree Certificates`, `#web security`

---

<a id="item-4"></a>
## [HTTP/2 Bomb DoS Attack Threatens Major Web Servers](https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb) ⭐️ 9.0/10

Researchers have disclosed a remote denial-of-service attack called HTTP/2 Bomb that exploits HPACK compression amplification combined with slow connection holding to exhaust server memory, affecting NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora with default HTTP/2 configurations. This vulnerability allows a single attacker with a modest 100 Mbps home connection to render multiple major web servers unavailable within seconds, posing a critical threat to internet infrastructure and services relying on these servers. Apache httpd and Envoy can have 32 GB of memory occupied by a single client in about 20 seconds; NGINX has patched the issue in version 1.29.8+, Apache in mod_http2 v2.0.41, while IIS, Envoy, and Pingora currently have no fix available.

telegram · zaihuapd · Jun 3, 15:00

**Background**: HPACK is a header compression format used in HTTP/2 to reduce overhead, but it can be abused to amplify small inputs into large memory allocations. Slowloris is a classic slow DoS attack that keeps many connections open by sending partial requests. The HTTP/2 Bomb combines these techniques: it sends compressed headers that expand greatly in memory while holding connections open slowly, exhausting server resources.

<details><summary>References</summary>
<ul>
<li><a href="https://httpwg.org/specs/rfc7541.html">RFC 7541 - HPACK: Header Compression for HTTP/2</a></li>
<li><a href="https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/">HPACK: the silent killer (feature) of HTTP/2</a></li>
<li><a href="https://en.wikipedia.org/wiki/Slowloris_(cyber_attack)">Slowloris (cyber attack) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#HTTP/2`, `#DoS`, `#vulnerability`, `#web server`

---

<a id="item-5"></a>
## [Google's Gemma 4 12B: Encoder-Free Multimodal Model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) ⭐️ 8.0/10

Google DeepMind released Gemma 4 12B, a dense multimodal model that replaces traditional vision and audio encoders with a lightweight embedding module, enabling native multimodal processing on a 16 GB laptop. This encoder-free design reduces latency and memory usage, making multimodal AI more accessible for local deployment and agentic workflows on consumer hardware. The embedding module consists of a single matrix multiplication, positional embedding, and normalizations, with only 35M parameters, yet the model achieves competitive performance on multimodal benchmarks.

hackernews · rvz · Jun 3, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48385906)

**Background**: Traditional multimodal models use separate encoders (e.g., SigLIP for vision) to convert images and audio into tokens before feeding them into the language model. This adds latency and memory overhead. Gemma 4 12B bypasses this by feeding raw multimodal data directly into the LLM backbone.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12B: a unified, encoder-free multimodal model</a></li>
<li><a href="https://developers.googleblog.com/gemma-4-12b-the-developer-guide/">Gemma 4 12B: The Developer Guide - Google Developers Blog</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b">A Visual Guide to Gemma 4 12B - Exploring Language Models</a></li>

</ul>
</details>

**Discussion**: Community members tested the Q4 quantized version and reported decent results but noted occasional syntax errors like extra brackets. Some questioned whether the lightweight embedding module is robust enough compared to dedicated encoders, while others praised the efficiency gains for local AI.

**Tags**: `#multimodal`, `#LLM`, `#Google`, `#vision`, `#efficiency`

---

<a id="item-6"></a>
## [DaVinci Resolve 21 Adds Photo Management, Motion Graphics](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew) ⭐️ 8.0/10

DaVinci Resolve 21 introduces a new Photo page with AI-powered photo management and editing tools, as well as enhanced motion graphics capabilities. The update also includes AI features like IntelliSearch, de-aging, and blemish removal. This update positions DaVinci Resolve as a potential competitor to Adobe Lightroom and After Effects, especially on Linux where professional photo management options are limited. It could disrupt Adobe's ecosystem by offering a unified video and photo editing solution at a one-time price of $295. The Photo page includes a large effects library with Resolve FX and Fusion FX, and supports moving fluidly between photos and video. The AI-powered IntelliSearch can analyze images and search by content, objects, people, and colors.

hackernews · pentagrama · Jun 3, 14:18 · [Discussion](https://news.ycombinator.com/item?id=48384482)

**Background**: DaVinci Resolve is a professional non-linear video editing, color correction, visual effects, and audio post-production software developed by Blackmagic Design. It runs on macOS, Windows, iPadOS, and Linux, and is known for its high-end color grading tools. The free version offers extensive features, while the Studio version costs $295.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blackmagicdesign.com/products/davinciresolve/whatsnew">DaVinci Resolve – What’s New | Blackmagic Design</a></li>
<li><a href="https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_New_Features_Guide.pdf?_v=1776322810000">DaVinci Resolve 21 New Features Guide</a></li>
<li><a href="https://en.wikipedia.org/wiki/DaVinci_Resolve">DaVinci Resolve - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members praised the update, with one user calling it 'huge' and noting it adds Lightroom-like functionality to Linux. Others expressed respect for Blackmagic Design's generous business model, while some wished for AI-driven keyframing and text-based editing workflows.

**Tags**: `#video editing`, `#photo management`, `#Linux`, `#AI`, `#Blackmagic Design`

---

<a id="item-7"></a>
## [Uber Caps AI Tool Spending at $1,500/Month per Tool](https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything) ⭐️ 8.0/10

Uber has implemented a $1,500 monthly spending cap per AI coding tool for all employees after blowing its 2026 AI budget in just four months. The policy applies to agentic coding software like Cursor and Claude Code. This highlights the real cost challenges of token-burning coding agents, which have become popular faster than companies anticipated. The cap sets a precedent for enterprise AI cost management and suggests a rational approach to balancing productivity gains with spending. The $1,500 cap is per tool, not per employee, meaning an engineer using two tools could spend up to $3,000/month. At Uber's median software engineer compensation of $330,000/year, the cap represents about 11% of that package.

rss · Simon Willison · Jun 3, 12:01 · [Discussion](https://news.ycombinator.com/item?id=48383056)

**Background**: Agentic coding tools like Claude Code and Cursor use large language models to autonomously plan, write, and test code, consuming tokens (units of AI processing) that incur API costs. These tools have seen explosive adoption in 2025-2026, leading to unexpected budget overruns at many companies. Uber's 2026 AI budget was set in 2025 before the surge in usage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the cap should be compared to fully-loaded engineer costs rather than just compensation, and whether AI providers will lower prices due to competition from Chinese models like DeepSeek. Some noted that flash models can be sufficient with careful usage, while others admitted to 'token maxxing' behaviors that inflate costs.

**Tags**: `#AI`, `#cost management`, `#software engineering`, `#Uber`, `#coding agents`

---

<a id="item-8"></a>
## [Espressif Announces ESP32-S31 RISC-V SoC with SIMD and Bitscrambler](https://www.espressif.com/en/products/socs/esp32-s31) ⭐️ 8.0/10

Espressif Systems has announced the ESP32-S31, a new system-on-chip (SoC) featuring RISC-V cores, SIMD instructions, and a Bitscrambler peripheral for flexible data transformation during DMA transfers. This release simplifies embedded development by enabling the use of modern toolchains like Rust without proprietary compilers, and the Bitscrambler offers flexibility comparable to the Raspberry Pi Pico's PIO, potentially expanding creative hardware projects. The ESP32-S31 integrates two Bitscrambler peripherals that offload bitwise operations from the CPU, and its RISC-V core supports SIMD for parallel data processing. The chip is part of Espressif's growing RISC-V family, but naming confusion persists as many variants share the 'ESP32' prefix.

hackernews · volemo · Jun 3, 16:10 · [Discussion](https://news.ycombinator.com/item?id=48385965)

**Background**: Espressif Systems is known for its ESP32 series of microcontrollers, which traditionally used Tensilica Xtensa cores. RISC-V is an open-source instruction set architecture that allows developers to use standard toolchains like GCC and Rust without vendor lock-in. SIMD (Single Instruction, Multiple Data) enables parallel processing of multiple data points, improving performance for tasks like audio or sensor data processing. The Bitscrambler is a programmable peripheral that transforms data during DMA transfers, similar to the PIO (Programmable I/O) on the Raspberry Pi Pico.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48385965">ESP 32 - S 31 | Hacker News</a></li>
<li><a href="https://docs.espressif.com/projects/esp-idf/en/stable/esp32p4/api-reference/peripherals/bitscrambler.html">BitScrambler Driver - ESP32-P4 - — ESP-IDF Programming Guide...</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed enthusiasm for the RISC-V shift, noting that it enables easy Rust development with a single command. Some users praised the Bitscrambler's flexibility, comparing it to PIO. However, several commenters criticized the naming scheme, saying that having many different chips all called 'ESP32' causes confusion.

**Tags**: `#ESP32`, `#RISC-V`, `#embedded systems`, `#hardware`, `#Espressif`

---

<a id="item-9"></a>
## [SpaceX Plans $75B Fixed-Price IPO at $135 Per Share](https://www.reuters.com/business/media-telecom/spacex-plans-raise-75-billion-ipo-135-per-share-source-says-2026-06-03/) ⭐️ 8.0/10

SpaceX plans to raise $75 billion in a fixed-price IPO at $135 per share, issuing 555.6 million shares, with trading expected on Nasdaq under ticker SPCX starting June 12, 2026. If successful, this would be the largest IPO in history, providing massive capital for AI computing and Starlink expansion, and could trigger a wave of mega-IPOs from AI companies like OpenAI and Anthropic. The fixed-price approach before roadshows is extremely rare; details may still change. SpaceX reported $18.7 billion in revenue last year but a net loss of $4.9 billion, with only Starlink being profitable.

telegram · zaihuapd · Jun 3, 09:01

**Background**: Starlink is a satellite internet constellation operated by SpaceX, providing low-latency broadband internet globally via thousands of low Earth orbit satellites. A fixed-price IPO means the offering price is set in advance and not adjusted based on investor demand during the book-building process, which is uncommon for large IPOs.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/星链">星 链 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.bbc.com/zhongwen/simp/science-62377847">什 么 是 星 链 Starlink ？ 成千上万颗低轨卫 星 布局的背后 - BBC News 中文</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#IPO`, `#finance`, `#AI`, `#Starlink`

---

<a id="item-10"></a>
## [Massive Proxy Service Blocking by GFW on March 4](https://t.me/zaihuapd/41740) ⭐️ 8.0/10

On March 4, 2025, the Great Firewall of China (GFW) began blocking IP ranges of popular proxy service providers, severely disrupting access to circumvention tools. The blocking heavily affects the VLESS protocol and the newer AnyTLS protocol, while non-TLS encryption appears less impacted. This event significantly impacts internet freedom in China, as proxy services are essential for accessing blocked global content. The targeting of newer protocols like VLESS and AnyTLS indicates the GFW's evolving detection capabilities, potentially rendering many current circumvention methods ineffective. The blocking began around noon on March 4 and targeted IP ranges of multiple popular proxy providers. While VLESS and AnyTLS protocols are heavily affected, non-TLS encryption methods remain relatively functional, though the full scope is still unclear.

telegram · zaihuapd · Jun 3, 11:15

**Background**: The Great Firewall of China (GFW) is a national-level internet censorship system that blocks access to foreign websites and slows cross-border traffic. VLESS is a lightweight, stateless transport protocol designed to evade deep packet inspection (DPI), while AnyTLS is a newer TLS camouflage protocol that aims to resist TLS-in-TLS fingerprinting. Both protocols are commonly used in proxy tools like Xray and V2Ray to bypass censorship.

<details><summary>References</summary>
<ul>
<li><a href="https://ru.wikipedia.org/wiki/VLESS">VLESS — Википедия</a></li>
<li><a href="https://portapp.app/en/about/protocols/anytls/">AnyTLS — TLS VPN protocol with simple setup</a></li>
<li><a href="https://en.wikipedia.org/wiki/Great_Firewall">Great Firewall - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#GFW`, `#proxy`, `#censorship`, `#Vless`, `#AnyTLS`

---

<a id="item-11"></a>
## [Google lets websites opt out of AI search results](https://9to5google.com/2026/06/02/google-ai-mode-overviews-opt-out/) ⭐️ 8.0/10

Google announced a new toggle in Search Console that lets website owners opt out of appearing in AI Mode and AI Overviews, without affecting their regular search rankings or Discover traffic. This gives webmasters and publishers control over how their content is used in generative AI features, addressing concerns about traffic loss and lack of attribution. It sets a precedent for AI content usage policies across the industry. The opt-out is available via Search Console and is currently being tested with a subset of UK websites before a global rollout. Google also introduced generative AI search statistics for impressions and page performance.

telegram · zaihuapd · Jun 3, 12:00

**Background**: AI Overviews is a Google Search feature that generates AI summaries from web content, often reducing click-through rates for publishers. Many website owners have sought ways to exclude their content from these summaries without harming their organic search presence.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5google.com/2026/06/02/google-ai-mode-overviews-opt-out/">Google will let websites opt-out of AI Mode & Overviews in Search</a></li>
<li><a href="https://mashable.com/tech/google-will-allow-websites-to-opt-out-of-ai-overviews">Google will allow websites to opt out of AI overviews | Mashable</a></li>
<li><a href="https://www.thekeyword.co/news/google-ai-overviews-opt-out-publishers">Google Opens AI Overviews Opt-Out for Publishers</a></li>

</ul>
</details>

**Tags**: `#Google`, `#AI search`, `#SEO`, `#Search Console`, `#webmaster tools`

---