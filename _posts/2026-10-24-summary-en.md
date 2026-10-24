---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 24 items, 6 important content pieces were selected

---

1. [PHP Releases Emergency Patches for Two Critical RCE Vulnerabilities](#item-1) ⭐️ 9.0/10
2. [Moonshot AI Releases Kimi K3.1 Pro and Highspeed Variant](#item-2) ⭐️ 8.0/10
3. [AI-Assisted iPhone Hack Sparks Debate on Security Research Access](#item-3) ⭐️ 8.0/10
4. [Dessa: Full-Duplex Speech Model Runs Locally on MacBook Pro](#item-4) ⭐️ 8.0/10
5. [Moonshot releases Kimi K3.1 Pro, rivaling top models at lower price](#item-5) ⭐️ 8.0/10
6. [First Public Untethered Jailbreak Since iOS 9 Hits iPhone 18 Pro](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PHP Releases Emergency Patches for Two Critical RCE Vulnerabilities](https://t.me/zaihuapd/44647) ⭐️ 9.0/10

The PHP team released emergency security updates to fix two critical vulnerabilities (CVE-2026-109618 and CVE-2026-109619) that allow unauthenticated remote code execution, with a CVSS 4.0 score of 9.2. Users are urged to upgrade immediately to PHP 8.5.12, 8.4.27, 8.3.36, or 8.2.35. These vulnerabilities affect all PHP deployments that serve web requests, including PHP-FPM, Apache mod_php, php-cgi, FrankenPHP, and LiteSpeed, potentially allowing attackers to execute arbitrary code without authentication. Given the widespread use of PHP in web infrastructure, immediate patching is critical to prevent large-scale exploitation. Exploitation has been demonstrated against Apache with mod_php, where the attack can be triggered before website business logic runs; a validated PHP-FPM exploitation path is also documented. The flaws stem from memory management issues in PHP Core, such as longjmp() handling of out-of-memory errors leading to use-after-free conditions.

telegram · zaihuapd · Oct 23, 13:46

**Background**: PHP is a widely-used open-source scripting language especially suited for web development, powering a large share of websites. CVSS (Common Vulnerability Scoring System) is an open framework for rating the severity of security vulnerabilities, with version 4.0 being the latest specification; scores of 9.0 and above indicate critical severity. Remote code execution (RCE) vulnerabilities are particularly dangerous because they allow attackers to run arbitrary commands on the server, often leading to full system compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.circl.lu/pub/tr-102/">TR-102 Critical Remote Code Execution Vulnerabilities in PHP ...</a></li>
<li><a href="https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-php-could-allow-for-remote-code-execution_2026-119">Multiple Vulnerabilities in PHP Could Allow for Remote Code ...</a></li>
<li><a href="https://nsfocusglobal.com/php-remote-code-execution-vulnerability-cve-2026-109618-cve-2026-109619-advisory/">PHP Remote Code Execution Vulnerability (CVE-2026-109618 ...</a></li>

</ul>
</details>

**Tags**: `#PHP`, `#security`, `#vulnerability`, `#remote-code-execution`, `#patching`

---

<a id="item-2"></a>
## [Moonshot AI Releases Kimi K3.1 Pro and Highspeed Variant](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

Moonshot AI has released Kimi K3.1 Pro, a new flagship large language model, along with a Highspeed variant available through the Kimi Code platform. The release quickly drew significant attention on Hacker News, generating over 660 points and 420 comments. Kimi K3.1 Pro offers performance comparable to leading proprietary models like Claude Sonnet 5.5 at a significantly lower cost, making it a strong contender in the competitive LLM market. Its release intensifies the price-performance race among AI labs and provides developers with a more affordable option for coding and reasoning tasks. In the Pac-Man benchmark, Kimi K3.1 Pro tied with Claude Sonnet 5.5 at a score of 93, while costing $0.68 and taking 11 minutes compared to Sonnet's $1.61 and 14 minutes. Moonshot AI also stated that it intentionally limits the model's offensive cyber capability in open weights, with plans to progressively raise it in future releases.

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**Background**: Kimi is a series of large language models developed by Moonshot AI, a Chinese AI company. The K3 family includes open-weight multimodal reasoning models, with K3 having 2.8 trillion parameters. Kimi Code is a platform that provides access to these models for coding tasks, offering different variants like Highspeed for faster inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models.html">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Community discussion highlighted several aspects: users noted the model's distinctive behavior, such as blunt and argumentative responses and inconsistent self-identification in reasoning traces. Others compared its performance and pricing favorably against Sonnet 5.5, while some complained about strict subscription quotas, with one user hitting a 5-hour limit in under an hour on a $99 plan. There was also debate about Moonshot's deliberate limitation of cyber capabilities in open weights.

**Tags**: `#LLM`, `#Kimi`, `#Moonshot AI`, `#benchmarks`, `#AI models`

---

<a id="item-3"></a>
## [AI-Assisted iPhone Hack Sparks Debate on Security Research Access](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

A blog post by a team at Calif details how they used AI to hack an iPhone, demonstrating a novel exploitation method. The post, titled 'Today, we hacked what we'd set out to hack: the iPhone,' quickly gained traction, drawing 713 points and 467 comments on a tech forum. This demonstration highlights how AI is lowering the barrier to discovering and exploiting iOS vulnerabilities, potentially accelerating the cat-and-mouse game between attackers and Apple. It also raises questions about who gets access to frontier AI models for security research, as such capabilities could become a moat for a select few. The blog post does not disclose specific technical details or the exact AI models used, but the community discussion suggests the exploits may bypass certain iOS protections. Commenters also wonder whether Lockdown Mode, Apple's extreme security setting, would mitigate these attacks.

hackernews · pavel_lishin · Oct 23, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50211474)

**Background**: iOS jailbreaking involves using exploits to remove Apple's software restrictions, granting root access and allowing installation of unauthorized apps. Historically, jailbreaks required significant expertise and were often patched quickly by Apple. Recently, AI tools like Anthropic Claude and OpenAI Codex have been used to discover iOS vulnerabilities, leading to a surge in patches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://thehackernews.com/2026/06/apple-patches-30-ios-macos-safari-flaws.html">Apple Patches 30+ iOS, macOS, Safari Flaws, Including AI ...</a></li>
<li><a href="https://security.apple.com/">Apple Security Research</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration over platform lock-in, noting that jailbreaking an iPhone can lead to being locked out of iCloud and iMessage, reducing the device to an 'iPod touch.' Some also criticized frontier AI labs for restricting 'Red Team' access to inner-circle companies, turning a safety program into a moat. Others asked about the real-life effectiveness of Lockdown Mode against such exploits.

**Tags**: `#iPhone security`, `#AI exploitation`, `#jailbreaking`, `#security research`, `#platform lock-in`

---

<a id="item-4"></a>
## [Dessa: Full-Duplex Speech Model Runs Locally on MacBook Pro](https://block.xyz/dessa) ⭐️ 8.0/10

Dessa is a new full-duplex speech model that runs locally on a MacBook Pro M4 Max or better and was trained on a single NVIDIA GB200 NVL72 system, according to its announcement on block.xyz. It promises low-latency, expressive conversation with simultaneous listening and speaking. This is significant because it demonstrates that a highly expressive, low-latency full-duplex speech model can be trained on a single rack-scale system and deployed on consumer hardware, potentially lowering the barrier for indie AI developers. If the demos hold up, it could accelerate the shift from turn-based voice assistants to more natural, interruptible conversational AI. The model is said to run locally on a MacBook Pro M4 Max or better, and training was accomplished on only one NVIDIA GB200 NVL72, a liquid-cooled rack-scale system with 36 Grace CPUs and 72 Blackwell GPUs. The announcement emphasizes low latency and expressive conversation demos, but no technical paper or benchmark details were provided in the content.

hackernews · dsr12 · Oct 23, 19:09 · [Discussion](https://news.ycombinator.com/item?id=50213925)

**Background**: Full-duplex speech models process audio continuously, allowing the system to listen and speak at the same time without waiting for the user to finish, unlike traditional turn-based voice assistants. The NVIDIA GB200 NVL72 is a rack-scale, liquid-cooled system that connects 36 Grace CPUs and 72 Blackwell GPUs with NVLink-C2C, designed for large-scale AI training and inference. Running such models locally on Apple Silicon (M4 Max) is notable because it avoids cloud latency and privacy concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL72 | NVIDIA</a></li>
<li><a href="https://github.com/cyrta/awesome-full-duplex-speech-to-speech">GitHub - cyrta/awesome-full-duplex-speech-to-speech: A ...</a></li>
<li><a href="https://mljourney.com/mac-ai-performance-guide-2026-m4-pro-vs-m4-max-vs-m4-ultra-for-local-llms/">Mac AI Performance Guide 2026: M4 Pro vs M4 Max vs M4 Ultra ...</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the local inference and single-system training claims, but some criticized the 'most authentic ever' title as sensationalist marketing. Others found the duplex demos artificial, noting the model interrupts too much and the laugh in the first example felt forced, while one commenter joked about the AI girlfriend market.

**Tags**: `#speech-model`, `#full-duplex`, `#AI`, `#local-inference`, `#Hacker News`

---

<a id="item-5"></a>
## [Moonshot releases Kimi K3.1 Pro, rivaling top models at lower price](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) ⭐️ 8.0/10

Moonshot AI released Kimi K3.1 Pro on its API on October 23, 2026, claiming benchmark parity with Claude Opus 5.5 and GPT-6 Astra, with full open weights promised by November 4, 2026. The model is priced at $2.00 per million input tokens and $10.00 per million output tokens, half the price of Claude Opus 5.5. This is the first time a soon-to-be open-weight model has scored this highly against frontier proprietary models, with Artificial Analysis giving it a score of 55—ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (all at 53) and behind only Claude Opus 5.5 (58). The combination of near-frontier performance, lower pricing, and pending open weights could significantly democratize access to top-tier AI capabilities. Moonshot also offers a "Highspeed" version that is 2-3x faster at twice the price, except for input token cache hits which are priced the same. The model supports three reasoning levels (low, medium, max), and early hands-on tests like Simon Willison's pelican SVG benchmark show solid but imperfect results.

rss · Simon Willison · Oct 23, 19:40

**Background**: Kimi is a series of large language models developed by Moonshot AI, a Chinese AI startup. Open weights means the trained model parameters are publicly downloadable, allowing anyone to run or fine-tune the model locally, in contrast to proprietary models accessible only via API. Artificial Analysis is an independent benchmarking organization that ranks models on an intelligence index, providing a neutral comparison beyond vendor-reported benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models: Open Source vs Open Weights vs...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Kimi`, `#Moonshot`, `#AI models`, `#benchmarks`

---

<a id="item-6"></a>
## [First Public Untethered Jailbreak Since iOS 9 Hits iPhone 18 Pro](https://t.me/zaihuapd/44644) ⭐️ 8.0/10

A Telegram post reports that researcher @calif_io demonstrated the first public untethered jailbreak since iOS 9 on an iPhone 18 Pro, where the jailbreak state persists after reboot without needing a computer. The attack chain reportedly involves three layers: the cryptex subsystem, TSS ticket spoofing, and bypassing PAC protection. This is significant because untethered jailbreaks have been essentially extinct since iOS 9, and a working chain on a current flagship device would demonstrate that Apple's layered defenses can still be defeated. It could reinvigorate iOS security research and raise concerns about the robustness of Apple's boot-time integrity protections. The post claims Apple patched 273 vulnerabilities on September 14, yet Calif's demo shows an undisclosed attack chain still works; however, details are limited and the claim comes from a single Telegram source, so independent verification is lacking. The use of TSS ticket spoofing and cryptex manipulation suggests abuse of Apple's signing and software distribution mechanisms.

telegram · zaihuapd · Oct 23, 11:43

**Background**: Jailbreaking removes Apple's software restrictions on iOS, and an untethered jailbreak is considered the holy grail because it persists across reboots without re-running an exploit. Cryptex is a signed, integrity-verified software distribution package used in iOS, while TSS (Ticket Signing Server) tickets are part of Apple's signing process that verifies firmware authenticity. PAC (Pointer Authentication Code) is an ARM security feature that protects against memory corruption exploits by signing pointers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://ios.cfw.guide/types-of-jailbreak/">Types of Jailbreak | iOS Guide</a></li>
<li><a href="https://github.com/0xjohnnydev/cryptsn0w?v=2">GitHub - 0xjohnnydev/cryptsn0w: Obsolete iOS jailbreak ...</a></li>

</ul>
</details>

**Tags**: `#iOS jailbreak`, `#security research`, `#exploit chain`, `#Apple`, `#mobile security`

---