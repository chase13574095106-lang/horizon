---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 30 items, 11 important content pieces were selected

---

1. [ATProto Has No Instances: A Protocol Clarification](#item-1) ⭐️ 8.0/10
2. [Project Valhalla Arrives in JDK 28: Value Types & Heap Flattening](#item-2) ⭐️ 8.0/10
3. [New JAWBONE Bill Targets Government Coercion of Online Speech](#item-3) ⭐️ 8.0/10
4. [EFF Argues Court Records Should Be Free](#item-4) ⭐️ 8.0/10
5. [Datasette Apps: Host sandboxed HTML/JS apps inside Datasette](#item-5) ⭐️ 8.0/10
6. [China Proposes Rules for Interoperable Decentralized Digital IDs](#item-6) ⭐️ 8.0/10
7. [US Pressures ASML Over Suspected EUV Machine Transfer to China](#item-7) ⭐️ 8.0/10
8. [Infant Diapers Found to Contain Reproductive Toxicant Formamide](#item-8) ⭐️ 8.0/10
9. [Apple Agrees to Open Third-Party App Stores in Brazil](#item-9) ⭐️ 8.0/10
10. [SpaceX sold shares to Chinese investors before IPO](#item-10) ⭐️ 8.0/10
11. [Beihang PhD Alum Accuses Two Professors of Data Fabrication](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ATProto Has No Instances: A Protocol Clarification](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 8.0/10

Dan Abramov published an article explaining that ATProto, the protocol behind Bluesky, does not have 'instances' like Mastodon, but instead separates roles into Personal Data Servers (PDS), Relays, and AppViews. This clarification resolves a common misconception that confuses newcomers comparing Bluesky with Mastodon, and highlights ATProto's architectural advantage of decoupling data storage, relay, and application logic for better scalability. The article uses a blog analogy: PDS is like a blog's hosting, Relay is like an RSS feed aggregator, and AppView is like a reader app. Unlike Mastodon's monolithic instances, ATProto allows users to choose different providers for each role.

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: ATProto (Authenticated Transfer Protocol) is a decentralized protocol developed by Bluesky. In Mastodon (ActivityPub), each server is an 'instance' that handles storage, federation, and user interface. ATProto separates these concerns: PDS stores user data, Relays index and distribute data, and AppViews provide the user interface. This design aims to improve scalability and user choice.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://getskyscraper.com/blog/atprotocol-federation-architecture-guide">ATProtocol Federation Architecture: PDS, Relay, AppView & How ...</a></li>
<li><a href="https://fediversereport.com/a-conceptual-model-of-atproto-and-activitypub/">A conceptual model of ATProto and ActivityPub – The Fediverse Report</a></li>

</ul>
</details>

**Discussion**: Comments on Hacker News debated the accuracy of the blog analogy, with some arguing that RSS does not depend on a central reader like Google Reader, while others praised ATProto's separation of concerns as a cleaner system design. Some commenters felt the article dismissed the moderation challenges that instances solve in ActivityPub.

**Tags**: `#ATProto`, `#decentralization`, `#protocol design`, `#Bluesky`, `#ActivityPub`

---

<a id="item-2"></a>
## [Project Valhalla Arrives in JDK 28: Value Types & Heap Flattening](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Project Valhalla's value types and heap flattening will be delivered in JDK 28, fundamentally changing JVM memory layout by allowing objects to be stored inline without headers or pointers. This is a decade-long evolution of the JVM that dramatically improves memory density and performance for data-intensive applications, but sparks debate on design trade-offs like null-safety and uniformity. Heap flattening only works for objects with representations up to 64 bits; larger objects still require indirection. The null flag adds overhead, and value classes break the principle of uniformity by making assignment behavior depend on class type.

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: Project Valhalla is an OpenJDK project announced in 2014, led by Brian Goetz, aiming to introduce value types (inline classes) to Java. Traditionally, all Java objects are reference types with headers and pointers, causing memory overhead and poor cache locality. Value types eliminate object identity, allowing the JVM to store them directly in arrays and fields without indirection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 # ...</a></li>
<li><a href="https://www.baeldung.com/java-valhalla-project">Java Valhalla Project | Baeldung</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about heap flattening limitations (only for ≤64-bit objects), null-safety trade-offs, and violation of the principle of uniformity. Some defend the JVM's evolution, noting that many critics have outdated views of Java.

**Tags**: `#Java`, `#JVM`, `#Project Valhalla`, `#performance`, `#language design`

---

<a id="item-3"></a>
## [New JAWBONE Bill Targets Government Coercion of Online Speech](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech) ⭐️ 8.0/10

Senators Ted Cruz and Ron Wyden introduced the bipartisan JAWBONE Act, which would prohibit federal agencies from coercing online platforms, broadcasters, and AI companies into censoring lawful speech. This bill addresses growing concerns over government pressure on private intermediaries to silence lawful speech, potentially strengthening First Amendment protections and platform autonomy. The bill is named the Justice Against Weaponized Bureaucratic Overreach to Networked Expression (JAWBONE) Act, and the EFF has applauded its introduction while noting the need for careful balance.

hackernews · hn_acker · Jun 19, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48600950)

**Background**: The Electronic Frontier Foundation (EFF) is a digital rights group that advocates for free speech online. Government coercion of platforms to censor content, often through informal pressure, has been criticized as a form of censorship by proxy. The JAWBONE Act aims to codify protections against such practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aclu.org/press-releases/aclu-endorses-bipartisan-jawbone-act-to-protect-free-speech">ACLU Endorses Bipartisan JAWBONE Act To Protect Free Speech | American Civil Liberties Union</a></li>
<li><a href="https://laweconcenter.org/resources/government-by-raised-eyebrow-the-jawbone-act-and-the-problem-of-censorship-by-proxy/">Government by Raised Eyebrow: The JAWBONE Act and the Problem of Censorship by Proxy - International Center for Law & Economics</a></li>

</ul>
</details>

**Discussion**: Commenters generally support the bill but note political irony, as Senator Cruz has previously targeted platforms for alleged anti-conservative bias. Some also emphasize that private platforms retain their own First Amendment rights to moderate content.

**Tags**: `#online speech`, `#government pressure`, `#First Amendment`, `#EFF`, `#bipartisan bill`

---

<a id="item-4"></a>
## [EFF Argues Court Records Should Be Free](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 8.0/10

The Electronic Frontier Foundation (EFF) published an article arguing that court records should be free to the public, criticizing the high per-page fees of PACER and state systems, and supporting legislation to modernize access. This matters because public access to court records is fundamental to transparency and justice; high fees create a barrier that undermines the principle that the law should be freely readable by those subject to it. PACER charges $1 per page for federal court records, while some state systems charge up to $10 per page. The EFF supports a bill to replace aging PACER and CM/ECF systems with a modern, unified platform to improve public access and reduce costs.

hackernews · hn_acker · Jun 19, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48600946)

**Background**: PACER (Public Access to Court Electronic Records) is the electronic public access service for U.S. federal court documents, charging per-page fees. The EFF is a nonprofit digital rights group that advocates for civil liberties in the digital world. CourtListener and the RECAP program are existing tools that help share PACER documents for free.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PACER_(law)">PACER (law) - Wikipedia</a></li>
<li><a href="https://www.eff.org/about">About EFF | Electronic Frontier Foundation</a></li>
<li><a href="https://pacer.uscourts.gov/">Public Access to Court Electronic Records | PACER: Federal Court Records</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support, with one noting the high cost of $10 per page in Idaho state court. Another highlighted CourtListener and RECAP as vital stopgap solutions, hoping they become obsolete. A commenter referenced the ancient principle that the law should be freely readable, and another linked to Joel Spolsky's essay on software design.

**Tags**: `#legal tech`, `#public access`, `#government transparency`, `#PACER`, `#EFF`

---

<a id="item-5"></a>
## [Datasette Apps: Host sandboxed HTML/JS apps inside Datasette](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 8.0/10

Simon Willison released the datasette-apps plugin, which allows users to host sandboxed HTML+JavaScript applications inside Datasette that can execute read-only and write SQL queries via stored queries. This plugin transforms Datasette from a data publishing tool into a platform for building custom interactive data applications, enabling users to create rich frontends without leaving the Datasette ecosystem. Apps run in a tightly constrained iframe sandbox with `allow-scripts allow-forms` and an injected CSP header that blocks outbound HTTP requests, preventing data exfiltration. The plugin also registers permissions for create, view, edit, delete, and manage app access.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, with a JSON API that enables custom frontends. The datasette-apps plugin builds on this by allowing those frontends to be hosted directly within Datasette, using a sandboxed iframe to isolate untrusted code.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps : Host custom HTML applications inside Datasette</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#plugin`, `#sql`, `#web-applications`, `#sandbox`

---

<a id="item-6"></a>
## [China Proposes Rules for Interoperable Decentralized Digital IDs](https://www.cac.gov.cn/2026-06/18/c_1783525605384124.htm) ⭐️ 8.0/10

On June 18, 2026, China's Cyberspace Administration (CAC) released a draft regulation titled 'Regulations on Promoting Interoperable and Mutually Recognized Decentralized Digital Identity Applications' for public comment, with a deadline of July 18, 2026. This regulation marks a significant step by China to standardize decentralized digital identity (DID) based on blockchain, potentially enabling cross-platform identity interoperability across finance, transportation, customs, taxation, and digital yuan, impacting millions of users and devices. The draft defines DID as comprising identifiers, keys, verifiable credentials, and verifiable declarations, and proposes building a national identity chain on the national blockchain network. Both domestic and foreign individuals, institutions, and industrial devices can voluntarily register, while relevant entities must fulfill data security and personal information protection obligations.

telegram · zaihuapd · Jun 19, 01:39

**Background**: Decentralized digital identity (DID) is a blockchain-based identity system that gives users self-sovereign control over their identity data, unlike traditional centralized systems. Verifiable credentials (VCs) are tamper-proof digital documents issued by authorities that can be cryptographically verified. China has been developing its national blockchain network, BSN, to support such infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wublock123.com/news/cybersecurity-administration-promotes-interoperable-digital-ids-blockchain-network-63105">网信办拟推动分布式数字身份互通，支撑国家区块链网络建设</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/689030887">【深度】DID分布式数字身份(1/5)--什么是DID - 知乎</a></li>

</ul>
</details>

**Tags**: `#decentralized identity`, `#regulation`, `#blockchain`, `#China`, `#digital identity`

---

<a id="item-7"></a>
## [US Pressures ASML Over Suspected EUV Machine Transfer to China](https://www.bloomberg.com/news/articles/2026-06-19/us-tells-asml-it-s-concerned-china-may-have-top-chip-tool) ⭐️ 8.0/10

U.S. Commerce Secretary Lutnick told ASML executives that a top EUV lithography machine may have illegally reached China, violating export controls. ASML denies the claim, stating it has never exported an EUV system to China and that none of the 314 machines in operation are located there. This incident escalates US-China chip export control tensions and could lead to stricter legislation against equipment exports to China. It also risks straining US-Europe relations, as ASML is a Dutch company critical to global semiconductor supply chains. U.S. officials claim evidence that ASML has not acted in good faith, including exports of EUV-related transport equipment to China, but have not disclosed the evidence. ASML has circulated documents to prove its compliance and argues it has never exported any EUV-specific components.

telegram · zaihuapd · Jun 19, 03:09

**Background**: Extreme ultraviolet (EUV) lithography is a cutting-edge technology used to manufacture the most advanced semiconductor chips, using 13.5 nm wavelength light. ASML is the sole global supplier of EUV lithography systems, which are subject to strict export controls to prevent China from acquiring them for military modernization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">Extreme ultraviolet lithography - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://nldaily.com/tech/asml-export-controls-china-chip-war/">ASML Export Controls And China : The Dutch Company At The...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#export controls`, `#US-China`, `#ASML`, `#geopolitics`

---

<a id="item-8"></a>
## [Infant Diapers Found to Contain Reproductive Toxicant Formamide](https://t.me/zaihuapd/42051) ⭐️ 8.0/10

A commissioned investigation by the Economic Information Daily found that several brands of infant diapers, including HUGGIES, Bebaby, and Babycare, contain formamide, a reproductive toxicant. The substance was also detected in the blood and urine of some infants, and a journalist's blood concentration nearly doubled after wearing one diaper overnight. This discovery exposes a critical regulatory gap in China's national standards for diapers, which currently do not test for formamide despite its known toxicity. It poses serious health risks to infants, who are especially vulnerable to the compound's effects on the reproductive system, liver, and kidneys. Formamide is classified as a reproductive toxicant (Category 1B) by the EU and is banned in Chinese cosmetics, but the current national diaper standard (GB/T 28004.1-2021) does not include it. Experts urge a revision of the standard to mandate testing and set safety limits.

telegram · zaihuapd · Jun 19, 06:05

**Background**: Formamide is a chemical used in the production of certain plastics and adhesives, and it can be released from diaper materials during manufacturing. It is known to be absorbed through the skin and can accumulate in the body, potentially causing reproductive harm and damage to the liver and kidneys. The current Chinese standard for infant diapers focuses on physical properties and microbial safety but lacks provisions for chemical hazards like formamide.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sohu.com/a/1038359743_539932">“好奇”、“碧芭宝贝”、“Babycare”多款知名婴儿纸尿裤检测出甲酰胺生殖...</a></li>
<li><a href="https://finance.sina.com.cn/tech/roll/2026-06-18/doc-inicvmmr3319172.shtml">多品牌纸尿裤被检出甲酰胺，动物研究表明甲酰胺具有胚胎毒性和致畸性...</a></li>
<li><a href="https://news.qq.com/rain/a/20260618A0412500">好奇、碧芭宝贝、Babycare等品牌婴幼儿纸尿裤被检出毒性物质甲酰胺，...</a></li>

</ul>
</details>

**Discussion**: Online discussions show widespread concern among parents, with many reporting that their babies experienced severe diaper rash and skin breakdown that resolved after switching brands. Some brand live streams displayed 'formamide not detected' test reports, but viewers remained skeptical, questioning the credibility of self-testing.

**Tags**: `#consumer safety`, `#toxicology`, `#regulatory gap`, `#infant health`, `#product testing`

---

<a id="item-9"></a>
## [Apple Agrees to Open Third-Party App Stores in Brazil](https://t.me/zaihuapd/42059) ⭐️ 8.0/10

Apple has reached an agreement with Brazil's antitrust regulator to allow iPhone users to purchase apps and services outside the App Store and support third-party app stores, ending an investigation into anti-competitive practices. This marks a significant regulatory victory for open app distribution, potentially setting a precedent for other countries and forcing Apple to adapt its lucrative App Store model globally. Apple must implement the changes within 105 days, and the agreement lasts three years. Developers can display external payment options and alternative purchase links, but Apple may still charge fees on those transactions.

telegram · zaihuapd · Jun 19, 11:15

**Background**: Apple's App Store has faced antitrust scrutiny worldwide for requiring developers to use its in-app payment system and charging commissions of up to 30%. Similar regulatory actions have occurred in the EU and the US, with the EU's Digital Markets Act already mandating third-party app stores.

<details><summary>References</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KHIARRBT0514R9OJ.html">m.163.com/dy/article/KHIARRBT0514R9OJ.html</a></li>
<li><a href="https://macgaga.com/苹果在巴西让步，第三方应用商店来了/">苹 果 在 巴 西 让步， 第 三 方 应 用 商 店 来了 – Mac鸭子</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#antitrust`, `#app store`, `#Brazil`, `#regulation`

---

<a id="item-10"></a>
## [SpaceX sold shares to Chinese investors before IPO](https://www.propublica.org/article/spacex-elon-musk-ipo-foreign-investors-china) ⭐️ 8.0/10

Court documents unsealed by ProPublica reveal that SpaceX sold shares to at least a dozen investors based in mainland China, Hong Kong, and Russia between 2018 and 2021 through intermediary Tomales Bay Capital, despite later barring such investors from its IPO. This raises significant regulatory and national security concerns, as SpaceX is a key U.S. defense contractor involved in sensitive military projects, and the early foreign investments may have violated export control laws. The investments ranged from $800,000 to $40 million each, and investors included individuals linked to Chinese military contractors and entities tied to the Qatari royal family. Investors were promised quarterly business updates, facility tours, and meetings with the CFO.

telegram · zaihuapd · Jun 19, 12:00

**Background**: SpaceX, founded by Elon Musk, is a leading aerospace company that provides launch services for NASA and the U.S. military. Its Starlink satellite internet service also has dual-use applications. The company went public in June 2026 with an IPO that explicitly excluded investors from China and Hong Kong due to U.S. export restrictions on defense-related technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/spacex-ipo-bans-china-hong-kong-investors/">SpaceX IPO underwriters ban Hong Kong and China investors due ...</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#IPO`, `#foreign investment`, `#national security`, `#investigative journalism`

---

<a id="item-11"></a>
## [Beihang PhD Alum Accuses Two Professors of Data Fabrication](https://www.zaobao.com.sg/news/china/story20260619-9231002) ⭐️ 8.0/10

Former Beihang University PhD student Geng Jiangtao publicly accused two professors, Chang Lingqian and Wang Jun, of fabricating data in their papers, including a Nature paper by Chang. The accusations caused a surge of visitors to Beihang's website, leading to temporary outages. This case highlights ongoing concerns about research integrity at top Chinese universities, especially involving high-profile publications like Nature. The public response underscores the growing demand for transparency and accountability in academic research. Geng, who dropped out of Beihang in 2025 and became a science communicator, has previously exposed five scholars from other universities, all of whom faced consequences. The accused professors are Chang Lingqian, deputy dean of the School of Medical Science and Engineering, and Wang Jun of the School of Aeronautic Science and Engineering.

telegram · zaihuapd · Jun 19, 16:02

**Background**: Research misconduct, including data fabrication, is a serious issue in academia that undermines trust in scientific findings. Beihang University is a prestigious institution in China, and a Nature paper is considered a major achievement. Geng's previous successful exposures have built his credibility as a whistleblower.

<details><summary>References</summary>
<ul>
<li><a href="https://news.buaa.edu.cn/info/1002/65744.htm">《 Nature ...</a></li>
<li><a href="https://www.163.com/dy/article/KQL98JTD051492T3.html?f=post1603_tab_news">同济大学一院长被质疑 Nature ...</a></li>
<li><a href="https://www.xiaoyuzhoufm.com/episode/6a26d0adb30e1571aea2d05a">E898. 耿 同 学 ：用 学 术 打 假 ，赶走实验室里的大象 - 故事FM</a></li>

</ul>
</details>

**Tags**: `#academic misconduct`, `#research integrity`, `#China`, `#Beihang University`, `#paper retraction`

---