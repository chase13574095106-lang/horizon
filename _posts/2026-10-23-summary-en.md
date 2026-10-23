---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 37 items, 13 important content pieces were selected

---

1. [Quad9 to Exit France Over DNS Blocking Orders](#item-1) ⭐️ 8.0/10
2. [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agents](#item-2) ⭐️ 8.0/10
3. [HackiOS boots full iOS 16.5 firmware on Android phones via QEMU](#item-3) ⭐️ 8.0/10
4. [Nintendo Switch 2 Jailbroken via Software Exploit](#item-4) ⭐️ 8.0/10
5. [eMudhra to exit global SSL/TLS certificate business after weak key incident](#item-5) ⭐️ 8.0/10
6. [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](#item-6) ⭐️ 8.0/10
7. [Anthropic Releases Claude API 2026-10-21, Removes Temperature and Other Sampling Parameters](#item-7) ⭐️ 8.0/10
8. [Australian Federal Court rules Apple and Google abused market power](#item-8) ⭐️ 8.0/10
9. [Tesla begins Cybercab production in North America, a driverless robotaxi with no steering wheel](#item-9) ⭐️ 8.0/10
10. [Study: Smart TVs Still Report Data After ACR Disabled](#item-10) ⭐️ 8.0/10
11. [Oracle Issues High-Severity Security Alert for Java SE Vulnerability](#item-11) ⭐️ 8.0/10
12. [333 Backdoored Tor Exit Nodes Taken Offline](#item-12) ⭐️ 8.0/10
13. [Banned Nvidia B300 Chips Found in Chinese State Network](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Quad9 to Exit France Over DNS Blocking Orders](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 8.0/10

Quad9, a privacy-focused public DNS resolver, announced it will cease operations in France after November 24, 2024, due to court orders requiring it to block certain domain names and fines for noncompliance. The decision follows a legal battle with Sony Music Entertainment GmbH, which circumvented Quad9's geoIP blocking via VPN and successfully argued noncompliance, leading to contempt fines. This sets a precedent for holding DNS resolvers liable for content they do not host, potentially forcing other public DNS providers to implement blocking or exit markets, which could fragment the internet and undermine privacy-focused services. It highlights the growing tension between copyright enforcement and the open, global nature of internet infrastructure. Quad9 plans to use geoIP filters to block French users after November 24, though its CTO acknowledges that geoIP blocking is insufficient for selectively denying resolution of certain names. The case mirrors similar actions against Google, Cloudflare, and Cisco by French broadcasters, with Cisco having exited the market two years ago.

hackernews · farrokhi · Oct 22, 14:32 · [Discussion](https://news.ycombinator.com/item?id=50195959)

**Background**: Quad9 is a free public DNS resolver that blocks malicious domains and emphasizes user privacy. DNS resolvers translate human-readable domain names into IP addresses, acting as a directory for the internet. In France, courts have ordered DNS providers to block access to piracy sites, and failure to comply can result in fines. This case is part of a broader trend of governments and rights holders pressuring intermediaries to enforce content blocking.

<details><summary>References</summary>
<ul>
<li><a href="https://quad9.net/">Quad9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://www.unveildns.com/blog/geo-blocking-dns.html">Geo - blocking DNS by client country — UnveilDNS Blog</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with the legal outcome, comparing DNS resolvers to a phone book punished for listing a criminal's number. Some suggested that DNS resolvers should stop resolving domains of companies that sue them, while others noted the similarity to Cisco's earlier exit from France.

**Tags**: `#DNS`, `#privacy`, `#legal`, `#internet governance`, `#France`

---

<a id="item-2"></a>
## [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agents](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA has released OpenShell 0.1.0, an open-source runtime that sandboxes fleets of autonomous AI agents by enforcing declarative policies on file access, package installation, API calls, and credential use. The runtime combines sandboxed execution, controlled service access, credential management, and formal policy analysis without requiring agents to be rewritten. As organizations deploy fleets of autonomous agents that need broad access to files, APIs, and credentials, OpenShell addresses the critical security gap of preventing data exfiltration and unauthorized actions. Its adoption by companies like Cadence, Slack, and Gecko signals that runtime governance is becoming a foundational layer for enterprise AI agent deployments. OpenShell enforces policies externally so agents can read files, install packages, and call APIs without unrestricted access to data, secrets, or network; however, the community notes that balancing capability and security remains an inherent tradeoff, and preventing data exfiltration (e.g., codebase leakage) is still an open challenge even with domain-based network restrictions.

hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

**Background**: Autonomous AI agents are increasingly used to perform complex tasks like coding, research, and system administration, but their broad access to tools and data creates risks of accidental or malicious data exfiltration. Traditional containers share the host kernel and are often insufficient for isolating AI-generated code, leading to sandboxing approaches such as microVMs, gVisor, and hardware-enforced isolation. OpenShell is NVIDIA's entry into this space, providing a policy-driven runtime that governs agent execution, visibility, and inference routing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/">Add Runtime Controls to AI Agents with NVIDIA OpenShell</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor & isolation ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly agree that running agents in containers is essential, with some sharing practical alternatives like iron proxy for network restrictions and credential swapping. Skeptics argue that OpenShell's promise of full capability without security tradeoffs is an oxymoron, and others highlight that preventing data exfiltration remains unsolved; one user reports building a layer above OpenShell for team policies and safe git usage, noting that goal-seeking agents without boundaries are a real risk.

**Tags**: `#AI agents`, `#security`, `#sandboxing`, `#NVIDIA`, `#runtime`

---

<a id="item-3"></a>
## [HackiOS boots full iOS 16.5 firmware on Android phones via QEMU](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 8.0/10

A project called HackiOS has demonstrated booting the full iOS 16.5 firmware on Android devices, including the POCO X5 Pro 5G and some Xiaomi models, using QEMU and a custom XNU kernel. The project provides its own EFI loader, UEFI port, and replacements for Apple's closed drivers, allowing the unmodified iOS 16.5 user space to run from launchd through SpringBoard to apps. This is a highly novel technical achievement that pushes the boundaries of virtualization and reverse engineering, showing that Apple's proprietary iOS stack can be made to run on non-Apple hardware. It could have significant implications for security research, device repurposing, and the ongoing debate over software freedom and hardware lock-in. The project runs as a research bench rather than a daily-use ROM: a session lasts a given number of seconds, after which the kernel returns to the loader and hands over its log. It relies on QEMU for system emulation and includes a Linux Wi-Fi driver on a compatibility layer, but likely lacks full hardware acceleration and may have performance limitations.

hackernews · aghuang · Oct 22, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50196718)

**Background**: XNU is Apple's hybrid kernel that combines the Mach microkernel with BSD components, and it serves as the foundation for macOS, iOS, and other Apple operating systems. QEMU is an open-source virtualization tool that emulates hardware, allowing operating systems to run on different architectures. iOS firmware (IPSW files) contains the complete operating system image, but it is normally locked to Apple devices through hardware checks and signed components.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XNU_kernel">XNU kernel</a></li>
<li><a href="https://www.qemu.org/docs/master/system/introduction.html">Introduction — QEMU documentation</a></li>
<li><a href="https://github.com/oosexgang/hackios-xnu-kernel">GitHub - oosexgang/hackios- xnu - kernel · GitHub</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some are impressed by the technical feat of running iOS on QEMU and Android hardware, while others raise concerns about potential misuse, such as fake iPhones, and question the project's motivations. One commenter notes the website's poor design but praises the achievement, and another speculates about AI safeguards influencing the project's release.

**Tags**: `#iOS`, `#Android`, `#virtualization`, `#QEMU`, `#reverse-engineering`

---

<a id="item-4"></a>
## [Nintendo Switch 2 Jailbroken via Software Exploit](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 8.0/10

A developer has published a blog post detailing the first software-only jailbreak of the Nintendo Switch 2, which works on the latest firmware and was demonstrated with Mario Kart World mods. The exploit reportedly leverages vulnerabilities involving SmileBASIC 4 and was achieved with the assistance of LLM-driven automation tooling. This jailbreak, occurring just 16 months after the console's launch, could open the door to homebrew, game modding, and potentially game dumping, which would allow Switch 2 exclusives to be played on arbitrary hardware—a worst-case scenario for Nintendo. It also highlights how LLMs and automation are accelerating hardware security research. The exploit is software-only and works on the latest firmware, using vulnerabilities related to SmileBASIC 4. The jailbreak was demonstrated with mods for Mario Kart World, but it is still far from being a commonplace method for piracy.

hackernews · ledoge · Oct 22, 08:01 · [Discussion](https://news.ycombinator.com/item?id=50192536)

**Background**: Jailbreaking a console means bypassing its security measures to run unofficial software, such as homebrew applications, mods, or pirated games. The Nintendo Switch 2 is Nintendo's latest console, released in 2025, and its security has been a major focus for hackers. SmileBASIC 4 is a programming environment available on Nintendo platforms, and vulnerabilities in such software can sometimes be exploited to gain broader system access. LLMs are increasingly used in reverse engineering to automate tasks like decompilation and vulnerability discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://kotaku.com/nintendo-switch-2-jailbreak-hack-exploit-piracy-homebrew-emulation-modding-2000748784">The Switch 2 Has Been Jailbroken For The First Time</a></li>
<li><a href="https://www.androidauthority.com/nintendo-switch-2-software-jailbreak-3727013/">Nintendo Switch 2 jailbreak could open the door to a world of mods</a></li>
<li><a href="https://github.com/ram-elgov/awesome-llm-reverse-engineering">Awesome‑LLM‑Reverse‑Engineering - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters expressed amazement at the technical feat, with some predicting that Switch 2 game dumps could appear within hours, enabling exclusives to run on arbitrary hardware via recomps/decomps. Others highlighted the clever automation setup, including JetKVMs for controller input and HDMI capture, and a SwitchBot Bot to press the power button when the console crashes. A few questioned how Codex was used for security research given its restrictions, while others emphasized that the expertise of the human researcher remains crucial.

**Tags**: `#console hacking`, `#security research`, `#Nintendo Switch 2`, `#LLM automation`, `#reverse engineering`

---

<a id="item-5"></a>
## [eMudhra to exit global SSL/TLS certificate business after weak key incident](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 8.0/10

eMudhra, an Indian certificate authority, announced that its board decided to withdraw from its global SSL/TLS certificate business five days after a researcher demonstrated that eight of its intermediate CA private keys were weak enough to be cracked. The company will continue revocation and certificate status services until all issued certificates expire or are replaced, and will complete its remaining commitments to browser root programs, including a full root-cause report. This incident underscores the critical importance of robust key generation and transparency for certificate authorities, as weak keys can allow attackers to forge certificates for any domain and intercept traffic. eMudhra's exit affects its global customers and highlights growing scrutiny from browser root programs and the security community over CA accountability. The compromised keys were intermediate CA private keys, and the weakness allowed a researcher to crack eight of them, as detailed in Cloudflare's blog and Chrome's public questioning via Mozilla's Bugzilla. eMudhra claims its global SSL/TLS infrastructure runs separately from other operations, but critics question the statement that no end-entity certificates were issued from the affected CA, since anyone could issue certificates from it.

hackernews · bo0tzz · Oct 22, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50195110)

**Background**: A certificate authority (CA) issues digital certificates that bind public keys to domain names, enabling HTTPS and secure communication. Each CA signs certificates with its private key, and if that key is weak or compromised, attackers can create fraudulent certificates to impersonate websites. Browser root programs, such as Chrome's, set strict security requirements for CAs and can distrust them if incidents occur.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise/">8 eMudhra certificates are compromised. | Cloudflare Blog</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed strong criticism of eMudhra's security practices and transparency, with some mocking the company's response and questioning its claim that no end-entity certificates were issued. The discussion also highlighted Chrome's brutal public questioning of eMudhra, linking to a Mozilla Bugzilla comment, and overall sentiment was that the incident reveals serious accountability issues.

**Tags**: `#SSL/TLS`, `#certificate-authority`, `#security`, `#PKI`, `#industry-news`

---

<a id="item-6"></a>
## [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 8.0/10

Anthropic announced that it is donating its Agent Skills standard to the Agentic AI Foundation (AAIF) under the Linux Foundation, following its earlier donation of the Model Context Protocol (MCP). The AAIF was co-founded by Anthropic, Block, and OpenAI last year to host vendor-neutral agentic AI standards. This move signals a push toward standardization and interoperability for agent tooling, which is high-value for developers building on these protocols. By placing Agent Skills under a vendor-neutral foundation, Anthropic aims to keep the standard open and community-driven, reducing fragmentation in the agentic AI ecosystem. The AAIF was formed in December 2025 with founding contributions including Anthropic's MCP, Block's goose, and OpenAI's AGENTS.md. Simon Willison noted that he predicted this donation last December when Anthropic first declared skills an open standard, and he used his datasette-mcp plugin to have Claude find that post.

rss · Simon Willison · Oct 22, 18:09

**Background**: Agent Skills is a format developed by Anthropic that lets AI agents use modular capabilities to handle complex real-world tasks more reliably. The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems like LLMs connect to external tools and data sources. The Linux Foundation is a nonprofit that hosts many open-source projects and standards, and the AAIF is its initiative to advance open, interoperable standards for agentic AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">Donating Agent Skills to the Agentic AI Foundation \ Anthropic</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#agentic-ai`, `#open-standards`, `#anthropic`, `#ai-governance`, `#developer-tools`

---

<a id="item-7"></a>
## [Anthropic Releases Claude API 2026-10-21, Removes Temperature and Other Sampling Parameters](https://x.com/ClaudeDevs/status/2113013247209021918) ⭐️ 8.0/10

Anthropic released Claude API version 2026-10-21, its first official version update since 2023, which removes the temperature, top_p, and top_k parameters so that requests including them now return a 400 error. The SDK and ant CLI now default to the new version, and authentication headers have switched to Authorization: Bearer, while the older 2023-06-01 version remains available and not deprecated. This is a breaking change for many developers who rely on sampling parameters to control output randomness and creativity, and it signals a significant platform shift that may push teams to rethink how they tune model behavior. The switch to Bearer authentication also affects integrations that manually construct headers. The new version is available on the Claude API, Claude Platform on AWS, Microsoft Foundry, and Google Cloud, but on Amazon Bedrock it is only available for Claude 4.7 and later models. The removal of temperature, top_p, and top_k means developers can no longer directly adjust the randomness of responses through these parameters.

telegram · zaihuapd · Oct 22, 03:54

**Background**: Temperature, top_p, and top_k are common sampling parameters in large language model APIs that control the randomness and diversity of generated text. Temperature scales the probability distribution, top_p limits sampling to a cumulative probability mass, and top_k restricts sampling to the top k tokens. Bearer authentication is an HTTP authentication scheme where a token is sent in the Authorization header, widely used for API access.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/versioning">Versions - Claude Platform Docs - Anthropic</a></li>
<li><a href="https://freeacademy.ai/blog/llm-parameters-temperature-top-p-top-k-max-tokens">LLM Parameters Explained: Temperature , Top - P , Top - K</a></li>
<li><a href="https://reqbin.com/req/5k564bhv/get-request-bearer-token-authorization-header-example">How do I Send a Request with Bearer Token Authorization Header ?</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude API`, `#breaking changes`, `#LLM`, `#API design`

---

<a id="item-8"></a>
## [Australian Federal Court rules Apple and Google abused market power](https://t.me/zaihuapd/44612) ⭐️ 8.0/10

On August 12, 2025, the Federal Court of Australia issued an oral ruling that Apple and Google abused their market power in app stores and payment systems, substantially lessening competition in violation of local competition law. This ruling could force Apple and Google to open up their app store payment systems to third-party providers, potentially reshaping developer economics and setting a precedent for global antitrust actions against app store gatekeepers. The full judgment has not been published and remains sealed due to confidentiality disputes, and both Apple and Google have indicated they will contest parts of the ruling; Epic Games has hailed the decision as a victory for developers and consumers.

telegram · zaihuapd · Oct 22, 06:54

**Background**: App store antitrust scrutiny has intensified globally, with regulators arguing that Apple's App Store and Google's Play Store hold monopoly power in app distribution and in-app payments. Similar cases, such as Epic Games v. Apple in the US and various investigations by the European Union and other jurisdictions, have challenged these practices. The Australian ruling adds to the growing pressure on tech giants to alter their business models.

<details><summary>References</summary>
<ul>
<li><a href="https://m.21jingji.com/article/20210502/herald/ef0a229a83d7410c60db2cdec3f239dc_zaker.html">解读丨欧盟为何 反 垄 断 剑指苹果 应 用 商 店 ？ 指控关键点有哪些？ - 21...</a></li>
<li><a href="https://36kr.com/p/1396370413271812">Epic ...</a></li>
<li><a href="https://juejin.cn/post/7486465253817253924">Google Play 应 用 商 店 结算 系 统 被罚款2020...</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#app-store`, `#apple`, `#google`, `#regulation`

---

<a id="item-9"></a>
## [Tesla begins Cybercab production in North America, a driverless robotaxi with no steering wheel](https://t.me/zaihuapd/44614) ⭐️ 8.0/10

Tesla has announced that its Cybercab, a purpose-built autonomous electric vehicle with no steering wheel, pedals, or side mirrors, has entered production in North America. The vehicle is designed entirely around its onboard AI driving system and is positioned as the centerpiece of Tesla's Robotaxi ride-hailing business. This marks one of the first production vehicles from a major automaker built without any manual controls, a significant milestone for the autonomous vehicle industry and for Tesla's Robotaxi ambitions. If successful, it could accelerate the shift toward driverless ride-hailing and pressure regulators and competitors to adapt. The Cybercab is a two-passenger battery-electric robotaxi that uses a camera-only sensor approach and lacks a rear window as well as manual controls. Its deployment still depends on regulatory approval for vehicles without steering wheels, a process that is only now being clarified in the U.S.

telegram · zaihuapd · Oct 22, 07:54

**Background**: Tesla has been developing a Robotaxi ride-hailing service, launching an initial fleet in Texas in 2025, and the Cybercab is the purpose-built vehicle intended for that network. Traditional U.S. federal safety standards require manual controls like steering wheels and pedals, so fully driverless vehicles need regulatory exemptions or updated rules. Regulators have recently begun approving robotaxis without steering wheels, such as Amazon's Zoox, signaling that the rules are catching up to the technology.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://apnews.com/article/zoox-nhtsa-robotaxi-steering-wheel-1bdb3bb8ecc80a23721504315cfa50ce">Some robotaxis approved to operate without steering wheels ...</a></li>
<li><a href="https://www.axios.com/2026/03/18/robotaxi-autonomous-av-steering-wheel">U.S. paves road for vehicles with no steering wheel - Axios</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous vehicles`, `#Robotaxi`, `#Cybercab`, `#AI`

---

<a id="item-10"></a>
## [Study: Smart TVs Still Report Data After ACR Disabled](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 8.0/10

A study of 12 smart TVs from 10 vendors, involving 5,943 controlled experiments, found that some models continue to send content-related data even after users disable Automatic Content Recognition (ACR) in settings. Two platforms transmitted viewing information unencrypted: VIDAA OS sent data including non-resettable device IDs and audio fingerprints over plaintext MQTT, while Vizio's WatchFree+ exposed program names in unencrypted DNS queries. This research demonstrates that opting out of ACR does not reliably stop smart TVs from reporting viewing data, undermining user trust in privacy controls. The findings affect millions of smart TV owners and highlight the need for stronger enforcement and transparency around data collection in consumer devices. The study conducted 5,943 controlled experiments across 12 TVs, revealing that VIDAA OS uses plaintext MQTT to transmit non-resettable device IDs and audio fingerprints, while Vizio's WatchFree+ leaks program names via unencrypted DNS queries and TLS server-name fields associated with streaming provider Amagi. Users cannot disable these transmissions through available settings.

telegram · zaihuapd · Oct 22, 09:50

**Background**: Automatic Content Recognition (ACR) is software built into most smart TVs that captures screenshots or audio snippets of whatever is on screen—including DVDs, gaming, and cable—and sends them to a server to identify what you're watching. This data is used for targeted advertising and viewership analytics. MQTT is a lightweight messaging protocol commonly used for IoT devices, and when unencrypted, it can expose data to network observers. DNS queries, which resolve domain names to IP addresses, are typically unencrypted unless DNS-over-HTTPS is used.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/10/does-opting-out-of-smart-tv-tracking-work-research-finds-suspicious-traffic/">Does opting out of smart TV tracking work? Research... - Ars Technica</a></li>
<li><a href="https://cyberinsider.com/smart-tv-privacy-study-finds-tracking-persists-even-when-opting-out/">Smart TV privacy study finds tracking persists even when ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/MQTT">MQTT - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#smart-tv`, `#ACR`, `#data-leak`, `#security-research`

---

<a id="item-11"></a>
## [Oracle Issues High-Severity Security Alert for Java SE Vulnerability](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 8.0/10

Oracle released a security alert for CVE-2026-91403, a critical vulnerability in the JSSE component of Java SE with a CVSS score of 9.1, which can be exploited remotely without authentication. Affected versions include Java SE 8u511, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1, and multiple GraalVM editions, with patches now available. This vulnerability is remotely exploitable without authentication and affects a widely deployed platform, potentially compromising the confidentiality and integrity of data in countless Java-based applications. Organizations using affected versions should prioritize patching to prevent potential attacks. The vulnerability resides in the JSSE component, which handles secure communications, and successful exploitation could allow an attacker to compromise data confidentiality and integrity. Oracle has released patches and urges users to upgrade to supported versions immediately.

telegram · zaihuapd · Oct 22, 12:30

**Background**: JSSE (Java Secure Socket Extension) is a Java API that enables secure internet communications using SSL and TLS protocols, providing encryption and authentication for data in transit. It is a core component of the Java Runtime Environment, widely used in web servers, clients, and enterprise applications to protect sensitive information.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/alert-cve-2026-91403.html">Oracle Security Alert Advisory - CVE - 2026 - 91403</a></li>
<li><a href="https://en.wikipedia.org/wiki/Java_Secure_Socket_Extension">Java Secure Socket Extension - Wikipedia</a></li>
<li><a href="https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html">Java Secure Socket Extension ( JSSE ) Reference Guide</a></li>

</ul>
</details>

**Tags**: `#security`, `#Java`, `#vulnerability`, `#Oracle`, `#CVE`

---

<a id="item-12"></a>
## [333 Backdoored Tor Exit Nodes Taken Offline](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

A Tor operator scanned approximately 3,000 exit relays and found 333 infected with the Ebury backdoor, about 10% of all exits. These nodes were flagged as BadExit on October 4 and taken offline the next day. This incident compromised roughly a tenth of Tor's exit capacity, allowing attackers to steal SSH credentials and intercept unencrypted email traffic from users whose connections happened to route through the infected relays. It highlights the risks of relying on Tor exit nodes for sensitive traffic and underscores the importance of end-to-end encryption. The backdoor hijacked SSH connections on port 22 to 12 intercepting servers to steal credentials, and the attackers had compromised the servers since August and blocked certain ports to specifically collect unencrypted email traffic. The initial intrusion vector remains undetermined.

telegram · zaihuapd · Oct 22, 14:52

**Background**: Ebury is an OpenSSH backdoor and credential stealer targeting Linux servers, first seen in 2009 and used to maintain botnets and steal credentials. Tor exit nodes are the points where traffic leaves the Tor network, and the BadExit flag tells clients to avoid using a relay for exit connections. When an exit node is compromised, attackers can monitor or manipulate traffic that exits through it.

<details><summary>References</summary>
<ul>
<li><a href="https://attack.mitre.org/software/S0377/">Ebury, Software S0377 | MITRE ATT&CK®</a></li>
<li><a href="https://tor.stackexchange.com/questions/253/what-specifically-causes-an-exit-to-get-a-bad-exit-flag">directory - What specifically causes an Exit to get a Bad Exit flag?</a></li>

</ul>
</details>

**Tags**: `#Tor`, `#security`, `#backdoor`, `#Ebury`, `#network-security`

---

<a id="item-13"></a>
## [Banned Nvidia B300 Chips Found in Chinese State Network](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

A Chinese state-controlled semiconductor leasing group allegedly purchased 32 ASUS servers equipped with Nvidia B300 chips as part of a larger deal exceeding 3 billion yuan for over 700 servers, intended for deployment at China Mobile's Ningxia hub. After the filing drew scrutiny, the leasing group resubmitted documents with hardware descriptions redacted, prompting Nvidia to launch an investigation with its manufacturing partners. This report suggests a potential violation of U.S. export controls on the most advanced Nvidia AI chips, which could trigger stricter enforcement and escalate U.S.-China tech tensions. It also raises questions about the effectiveness of export controls and the integrity of the AI hardware supply chain, affecting policymakers, chipmakers, and cloud providers. The B300 is subject to the strictest U.S. export control tier and is essentially banned for sale to China; the servers were ASUS-branded and part of a 3 billion yuan deal for over 700 servers. Nvidia says it is investigating with manufacturing partners, while ASUS claims it complies with export controls.

telegram · zaihuapd · Oct 22, 15:22

**Background**: The Nvidia B300 is a high-end Blackwell-generation GPU designed for AI workloads, and U.S. export rules restrict its sale to China to prevent military and strategic use. China Mobile's Ningxia hub is a major data center campus in Zhongwei, leveraging cheap green power and natural cooling for AI computing. Chinese firms have increasingly turned to leasing arrangements and third-party intermediaries to acquire restricted hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://neuralwired.com/2026/06/05/nvidia-chip-export-controls-china-2026/">Nvidia & US Chip Export Controls: Complete 2026 Guide</a></li>
<li><a href="https://gpusmith.com/articles/en/nvidia-gpu-export-restrictions">NVIDIA GPU Export Restrictions: Current US Chip Controls 2026</a></li>
<li><a href="https://www.datacentermap.com/china/zhongwei/china-mobile-ningxia/">China Mobile Ningxia Data Center in Zhongwei | Fengyun Road</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export controls`, `#China`, `#AI hardware`, `#semiconductor`

---