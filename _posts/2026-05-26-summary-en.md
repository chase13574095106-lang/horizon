---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 27 items, 7 important content pieces were selected

---

1. [DynIP Launches Modern Dynamic DNS with RFC 2136 Support](#item-1) ⭐️ 8.0/10
2. [Netherlands blocks US takeover of digital ID host Solvinity](#item-2) ⭐️ 8.0/10
3. [Microsoft Copilot Cowork Vulnerability Enables Data Exfiltration](#item-3) ⭐️ 8.0/10
4. [Pope Leo XIV Issues Encyclical on AI Ethics](#item-4) ⭐️ 8.0/10
5. [Iran Plans Permanent Disconnection from Global Internet](#item-5) ⭐️ 8.0/10
6. [China Reviews Meta's Manus Acquisition, Founders Restricted](#item-6) ⭐️ 8.0/10
7. [Alipay Launches Token Pay and AI Wallet](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DynIP Launches Modern Dynamic DNS with RFC 2136 Support](https://dynip.dev/) ⭐️ 8.0/10

DynIP is a new dynamic DNS service that supports RFC 2136/TSIG updates, IPv6, DNSSEC, and native integration with FortiGate and MikroTik devices without requiring custom clients. This addresses a gap in the DDNS market where most services rely on proprietary HTTP-only protocols and lack modern features like IPv6 and DNSSEC, making it easier for network engineers to maintain reliable, secure dynamic DNS. DynIP uses RFC 2136 DNS UPDATE with TSIG authentication as its primary update method, and also provides an HTTP API for devices that cannot use DNS UPDATE. It supports end-to-end IPv6 and DNSSEC signing.

hackernews · dynip · May 26, 07:35 · [Discussion](https://news.ycombinator.com/item?id=48276363)

**Background**: Dynamic DNS (DDNS) allows devices with changing IP addresses to maintain a fixed hostname. RFC 2136 defines a standard protocol for updating DNS records dynamically, but many DDNS services use proprietary APIs instead. IPv6 and DNSSEC are increasingly important for modern networks but are often missing from legacy DDNS providers.

<details><summary>References</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2136">RFC 2136 - Dynamic Updates in the Domain Name System (DNS UPDATE)</a></li>
<li><a href="https://docs.netgate.com/pfsense/en/latest/services/dyndns/rfc2136.html">Configuring RFC 2136 Dynamic DNS updates - Netgate Documentation</a></li>
<li><a href="https://docs.fortinet.com/document/fortigate/7.6.3/administration-guide/685361/ddns">DDNS | FortiGate / FortiOS 7.6.3 | Fortinet Document Library</a></li>

</ul>
</details>

**Discussion**: The community response is positive, with users praising RFC 2136 support for easier integration with Kubernetes external-dns and network devices. Some users note that self-hosting with BIND9 is possible but less convenient, and one commenter suggests the landing page could use more personality.

**Tags**: `#DNS`, `#DDNS`, `#IPv6`, `#DNSSEC`, `#networking`

---

<a id="item-2"></a>
## [Netherlands blocks US takeover of digital ID host Solvinity](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 8.0/10

The Dutch government blocked the acquisition of Solvinity, a cloud firm hosting DigiD, the Netherlands' national digital identity system, by US-based Kyndryl, citing national security and privacy concerns. This decision underscores growing geopolitical tensions over digital sovereignty and the vulnerability of critical national infrastructure to foreign legal and intelligence pressures, especially from the US. Solvinity hosts DigiD, which handles over 550 million logins annually for Dutch government services. The acquisition by Kyndryl, an IBM spin-off, was blocked after parliament voted to end the contract with Solvinity, but the government extended it.

hackernews · vrganj · May 26, 11:46 · [Discussion](https://news.ycombinator.com/item?id=48278406)

**Background**: DigiD is the Netherlands' central digital identity system used by citizens to access government services, healthcare, taxes, and benefits. The concern is that under US ownership, Solvinity could be compelled by US law (e.g., the Patriot Act) to hand over data, undermining Dutch privacy protections.

<details><summary>References</summary>
<ul>
<li><a href="https://p4sc4l.substack.com/p/dutch-digital-identity-infrastructure">Dutch digital identity infrastructure could become vulnerable to American legal, intelligence, sanctions, and political pressure.</a></li>
<li><a href="https://thepolder.news/the-netherlands-built-its-digital-identity-on-foreign-infrastructure-now-its-paying-the-price">Digital Identity: Lessons from the DigiD Case - The Polder News</a></li>

</ul>
</details>

**Discussion**: Commenters largely support the block, with many emphasizing that privacy by architecture is superior to privacy by policy. Some question why the Netherlands cannot self-host an open-source identity solution for its 20 million users.

**Tags**: `#digital sovereignty`, `#privacy`, `#geopolitics`, `#critical infrastructure`, `#identity management`

---

<a id="item-3"></a>
## [Microsoft Copilot Cowork Vulnerability Enables Data Exfiltration](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

A prompt injection vulnerability in Microsoft Copilot Cowork allows attackers to exfiltrate files by embedding external images in agent-sent emails, which trigger network requests when opened by the user. This vulnerability highlights a critical security challenge in agentic AI systems, as it can lead to unauthorized data exfiltration in a widely used enterprise product, affecting millions of Microsoft 365 users. The attack leverages the fact that Copilot Cowork can send emails to the user's inbox without approval, and those emails can contain external images that exfiltrate data via pre-authenticated OneDrive download links.

rss · Simon Willison · May 26, 15:36

**Background**: Prompt injection is a security exploit where carefully crafted inputs cause an AI model to behave unexpectedly, bypassing safeguards. In agentic systems like Copilot Cowork, which can perform actions on behalf of users, such vulnerabilities can lead to data exfiltration. External images in emails can trigger network requests to attacker-controlled servers, enabling data theft.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed concern over the severity of the vulnerability, noting that it underscores the inherent risks of granting AI agents email-sending capabilities without proper safeguards. Some debated whether Microsoft's design choices adequately prioritize security.

**Tags**: `#security`, `#AI`, `#prompt injection`, `#Microsoft Copilot`, `#data exfiltration`

---

<a id="item-4"></a>
## [Pope Leo XIV Issues Encyclical on AI Ethics](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

On May 25, 2026, Pope Leo XIV published his first encyclical, Magnifica Humanitas, which provides ethical guidance on integrating artificial intelligence into society, drawing parallels to Pope Leo XIII's Rerum novarum on the industrial revolution. This encyclical is significant because it offers clear, authoritative ethical principles for AI from a major global institution, influencing public discourse and policy. It frames AI as a social question akin to labor rights, emphasizing human dignity and justice. The encyclical highlights the interpretability problem of AI systems, noting they are more 'cultivated' than 'built' and their internal processes remain unknown. It also stresses that true development must place people at the center and not shift costs onto others.

rss · Simon Willison · May 25, 23:58

**Background**: An encyclical is a formal papal letter addressed to bishops, providing guidance on matters of faith or morals. Rerum novarum (1891) by Pope Leo XIII addressed the condition of the working class during the industrial revolution and is a foundational text of Catholic social teaching. Pope Leo XIV chose his name to honor Leo XIII and to address AI as a new industrial revolution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Encyclical">Encyclical</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rerum_novarum">Rerum novarum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica humanitas</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#Vatican`, `#encyclical`, `#technology and society`, `#Pope Leo XIV`

---

<a id="item-5"></a>
## [Iran Plans Permanent Disconnection from Global Internet](https://t.me/zaihuapd/41574) ⭐️ 8.0/10

Iran is reportedly planning to permanently disconnect from the global internet, allowing only government-vetted individuals to access a filtered version, according to digital rights activists and a report by Filterwatch. This move could set a dangerous precedent for internet fragmentation and state-controlled digital borders, severely restricting the digital rights of Iranian citizens and isolating the country from global information flows. The plan, described as a 'government privilege,' would create a domestic parallel network (National Information Network) accessible to all, while international access requires security clearance. The current internet shutdown began on January 8 following 12 days of protests.

telegram · zaihuapd · May 26, 06:36

**Background**: Iran has long pursued a 'halal internet' or National Information Network, a walled garden intranet aimed at controlling and monitoring citizens' communications. The concept dates back to 2005, and the first phase was celebrated in 2017. Filterwatch is a research hub monitoring Iranian internet policies and infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://filter.watch/english/about-us/">About - Filterwatch</a></li>
<li><a href="https://en.wikipedia.org/wiki/National_intranet">National intranet - Wikipedia</a></li>
<li><a href="https://rsf.org/en/iran-creates-halal-internet-control-online-information">Iran creates “ Halal Internet ” to control online information | RSF</a></li>

</ul>
</details>

**Tags**: `#internet censorship`, `#digital rights`, `#geopolitics`, `#Iran`

---

<a id="item-6"></a>
## [China Reviews Meta's Manus Acquisition, Founders Restricted](https://t.me/zaihuapd/41577) ⭐️ 8.0/10

Chinese regulators are reviewing Meta's acquisition of AI startup Manus, and the founders—CEO Xiao Hong and Chief Scientist Ji Yichao—have been restricted from leaving the country during the investigation. This case highlights escalating geopolitical tensions in AI regulation, as China moves to block what it sees as a 'conspiratorial' attempt to hollow out its technology base, potentially setting a precedent for future cross-border tech acquisitions. The acquisition was announced in December 2025, with an undisclosed amount. The Chinese National Development and Reform Commission (NDRC) later blocked the deal, requiring withdrawal of the transaction.

telegram · zaihuapd · May 26, 09:56

**Background**: Manus is an AI agent startup founded by Butterfly Effect, inspired by the AI coding tool Cursor. Meta announced its acquisition in December 2025 to integrate Manus into its services. The Chinese government's review reflects concerns over technology transfer and national security amid the US-China AI rivalry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/04/28/china-meta-manus-ai-deal.html">Op-ed: In blocking Meta-Manus deal, China sent a powerful reminder to Mark Zuckerberg and U.S. market about AI race</a></li>
<li><a href="https://arstechnica.com/ai/2026/04/china-kills-metas-acquisition-of-manus-as-us-china-ai-rivalry-deepens/">China kills Meta’s acquisition of Manus as US-China AI rivalry deepens - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#AI`, `#regulation`, `#Meta`, `#acquisition`, `#geopolitics`

---

<a id="item-7"></a>
## [Alipay Launches Token Pay and AI Wallet](https://finance.sina.com.cn/jjxw/2026-05-26/doc-inhzffss1524895.shtml) ⭐️ 8.0/10

On May 26, 2026, Alipay launched Token Pay, a payment service for AI model subscriptions, and AI Wallet, a tool for managing AI agent payments. Users can search for 'AI Wallet' in Alipay to experience the service immediately. This marks a significant step in integrating AI with payment systems, enabling seamless monetization of AI models and autonomous agent transactions. It could accelerate the adoption of AI services by simplifying payment processes for both users and AI companies. Token Pay supports global user subscriptions and in-app token top-ups for large model companies. MiniMax and Stepfun have already partnered with Alipay, with multiple AI-native products adopting the payment solution.

telegram · zaihuapd · May 26, 12:31

**Background**: AI models often require users to purchase tokens or subscriptions to access their services, but existing payment systems are not optimized for such microtransactions. Alipay's Token Pay and AI Wallet aim to fill this gap by providing a dedicated payment infrastructure for AI services and autonomous agents, which can make dynamic decisions and execute payments on behalf of users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buaq.net/go-418958.html">支 付 宝 ：完成 3 亿笔 AI 付 ，发布 AI 钱包和 Token Pay</a></li>

</ul>
</details>

**Tags**: `#Alipay`, `#AI Wallet`, `#Token Pay`, `#AI payments`, `#Fintech`

---