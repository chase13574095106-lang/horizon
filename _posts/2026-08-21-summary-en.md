---
layout: default
title: "Horizon Summary: 2026-08-21 (EN)"
date: 2026-08-21
lang: en
---

> From 32 items, 6 important content pieces were selected

---

1. [US Citizen Faces Felony for Deleting Phone Data at Border](#item-1) ⭐️ 8.0/10
2. [Misconfigured e164.arpa Zone Exposes Military Call Routing Queries](#item-2) ⭐️ 8.0/10
3. [DeepSeek Launches Vision-Capable V4-Flash-Vision-Exp Model](#item-3) ⭐️ 8.0/10
4. [Anthropic Scanned Millions of Books for AI Training, Faced LibGen Piracy Claims](#item-4) ⭐️ 8.0/10
5. [China Tightens Outbound Investment Rules with New Draft](#item-5) ⭐️ 8.0/10
6. [YMTC STAR Market IPO Accepted, Plans to Raise 33 Billion Yuan](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [US Citizen Faces Felony for Deleting Phone Data at Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) ⭐️ 8.0/10

A US citizen, Samuel Tunick, faces felony charges for deleting data from his phone during a border search, as reported by the New York Times. This marks a significant escalation in the legal consequences for travelers who attempt to protect their digital privacy at US borders. This case raises critical questions about the balance between border security and digital privacy rights, potentially setting a precedent for how the government treats data deletion during border searches. It could have a chilling effect on travelers' willingness to carry sensitive data across borders and may prompt legal challenges to the border search doctrine. The charges stem from an incident where Tunick allegedly deleted data from his phone while it was being inspected by border agents. The case highlights the legal gray area surrounding the 'border doctrine,' which allows warrantless searches at the border, and the potential for obstruction charges when individuals attempt to protect their data.

hackernews · floathub · Aug 21, 12:10 · [Discussion](https://news.ycombinator.com/item?id=49386895)

**Background**: The 'border doctrine' is a controversial legal principle that permits warrantless searches of travelers and their belongings at US borders, including electronic devices. Courts have generally upheld this doctrine, but privacy advocates argue that digital devices contain vast amounts of personal data and should require a warrant. The Fourth Amendment protects against unreasonable searches, but its application at the border has been limited.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2018/10/feds-agree-to-delete-data-seized-off-womans-iphone-during-border-search/">Feds took woman’s iPhone at border , she sued, now... - Ars Technica</a></li>
<li><a href="https://www.humanrightsfirst.org/library/know-your-rights-protecting-digital-privacy-at-the-border">Know Your Rights: Protecting Digital Privacy at the Border</a></li>
<li><a href="https://www.eff.org/wp/digital-privacy-us-border-2017">Digital Privacy at the U.S. Border: Protecting the Data On Your Devices | Electronic Frontier Foundation</a></li>

</ul>
</details>

**Discussion**: Community comments express a mix of cynicism and practical advice. Some commenters argue that the US has become increasingly authoritarian, comparing it to East Germany or the Soviet era, while others suggest technical workarounds like using burner phones or encrypted images to protect data. There is also frustration with government overreach and concerns about the erosion of civil liberties.

**Tags**: `#privacy`, `#border search`, `#digital rights`, `#surveillance`, `#legal`

---

<a id="item-2"></a>
## [Misconfigured e164.arpa Zone Exposes Military Call Routing Queries](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

A security researcher accidentally discovered a misconfigured e164.arpa zone that allowed them to intercept DNS queries used for routing phone calls to military bases. This exposed a critical privacy vulnerability in the public ENUM system, which translates phone numbers into internet addresses. This vulnerability could allow malicious actors to intercept or redirect phone calls to sensitive military and government numbers, leading to potential espionage or privacy breaches. It highlights the fragility of the aging ENUM infrastructure and the need for better security measures in telephony routing. The author did not set up a SIP server to test actual call termination, but the discovery was enough to raise alarms. The e164.arpa zone is operated by RIPE NCC under IAB instructions, and while public ENUM is largely dead, private ENUM services still exist for number porting information.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: ENUM (Telephone Number Mapping) is a standard that uses DNS to map telephone numbers to internet addresses, enabling VoIP and unified communications. The e164.arpa zone is the top-level domain for ENUM, managed by the Internet Architecture Board (IAB) and operated by RIPE NCC. Public ENUM never gained widespread adoption, but private ENUM services are used by carriers for number portability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://www.internic.net/zones/arpa.zone">internic.net/ zones / arpa . zone</a></li>
<li><a href="https://www.voip-info.org/enum/">ENUM - The bridge between the switched telephony network and the Internet - VoIP-Info</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that the author wasn't jailed for reporting the issue, and some wished the author had set up a SIP server to see if calls could be terminated. Others noted that private ENUM services still exist and are used for number porting, and one commenter mentioned the TRIP schema as an alternative.

**Tags**: `#security`, `#telephony`, `#ENUM`, `#privacy`, `#infrastructure`

---

<a id="item-3"></a>
## [DeepSeek Launches Vision-Capable V4-Flash-Vision-Exp Model](https://api-docs.deepseek.com/guides/vision/) ⭐️ 8.0/10

DeepSeek has released an experimental multimodal model, DeepSeek-V4-Flash-Vision-Exp, now available on its API platform. This variant adds vision understanding to the existing DeepSeek-V4-Flash text model while maintaining its text capabilities. This release addresses a known limitation of DeepSeek's models, which previously lacked native vision capabilities, and positions DeepSeek as a stronger competitor in the multimodal AI space. It is particularly significant for open-weight AI labs, as it offers a vision-capable alternative to proprietary models like Anthropic's Claude. The model matches DeepSeek-V4-Flash on text benchmarks, including agents, reasoning, and world knowledge, and shows strong performance on multimodal agent benchmarks. Images are resized to roughly 800×800 pixels before inference, and tokens are billed alongside text tokens; however, this resolution may be insufficient for OCR tasks involving full A4/Letter pages.

hackernews · dares2573 · Aug 21, 10:33 · [Discussion](https://news.ycombinator.com/item?id=49386163)

**Background**: DeepSeek is a Chinese AI research company known for open-weight large language models such as DeepSeek-V4 and DeepSeek-R1. Previously, its models lacked native vision capabilities, leading some users to report that the model would hallucinate vision tools when asked to analyze images. This new experimental model aims to fill that gap by integrating vision understanding directly into the model.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/updates/">Change Log | DeepSeek API Docs</a></li>
<li><a href="https://x.com/deepseek_ai/status/2090730032574631962">DeepSeek on X: "DeepSeek-V4-Flash-Vision-Exp is now live on the DeepSeek API Platform! 🚀 🔹 This experimental multimodal model matches DeepSeek-V4-Flash on text capabilities—including agents, reasoning, and world knowledge. 🔹 On multimodal agent benchmarks, V4-Flash-Vision-Exp makes a major" / X</a></li>
<li><a href="https://officechai.com/ai/deepseek-releases-v4-flash-vision-exp-matches-opus-4-8-on-some-multimodal-benchmarks/">DeepSeek Releases V4-Flash-Vision-Exp, Matches Opus 4.8 On Some Multimodal Benchmarks</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users are optimistic about the new vision capability, noting it could replace their reliance on other models for screenshot analysis, while others report failures on simple tasks like reading a clock, which smaller models handle correctly. There are also concerns about the image resolution limit for OCR applications, and some users highlight the model's tendency to hallucinate vision tools in previous versions.

**Tags**: `#DeepSeek`, `#vision model`, `#AI`, `#LLM`, `#multimodal`

---

<a id="item-4"></a>
## [Anthropic Scanned Millions of Books for AI Training, Faced LibGen Piracy Claims](https://t.me/zaihuapd/43305) ⭐️ 8.0/10

The Washington Post reported that Anthropic launched 'Project Panama' in 2024, destructively scanning millions of physical books by cutting off their spines, spending tens of millions of dollars to train models like Claude. Additionally, class-action lawsuits allege Anthropic downloaded pirated data from shadow libraries like LibGen, with a potential $1.5 billion penalty. This news highlights the controversial data acquisition practices in the AI industry, raising significant ethical and legal questions about copyright infringement. It could set precedents for how AI companies obtain training data and impact the broader ecosystem of publishers, authors, and AI developers. The project involved 'destructive scanning' of physical books, and Anthropic reportedly emphasized that they 'didn't want outsiders to know.' A judge suggested that scanning for training could be considered fair use, but the method of acquisition might constitute infringement. Anthropic has already settled part of the lawsuit in August 2025.

telegram · zaihuapd · Aug 21, 04:52

**Background**: Anthropic is an AI company known for developing the Claude model family. Training large language models requires vast amounts of text data, and companies often use books, articles, and web content. Shadow libraries like LibGen provide free access to copyrighted works, which has led to legal disputes with publishers. The concept of 'fair use' in copyright law is central to whether such scanning is legal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shadow_library">Shadow library - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Library_Genesis">Library Genesis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/books/2023/sep/15/four-large-us-publishers-sue-shadow-library-for-alleged-copyright-infringement">Four large US publishers sue ‘shadow library’ for alleged copyright infringement | Books | The Guardian</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#copyright`, `#data acquisition`, `#ethics`

---

<a id="item-5"></a>
## [China Tightens Outbound Investment Rules with New Draft](https://yyglxxbsgw.ndrc.gov.cn/htmls/article/article.html?articleId=2c97d16c-9ff00a63-01a0-230bacc4-0001) ⭐️ 8.0/10

China's National Development and Reform Commission (NDRC) released a draft revision of the Measures for the Administration of Outbound Investment, which would replace the 2017 version. The draft introduces stricter capital outflow controls, expands security reviews to cover transfers and disposals of existing assets, and increases penalties for non-compliance. This regulatory overhaul will significantly impact Chinese companies and financial institutions engaged in outbound investment, potentially slowing cross-border capital flows and increasing compliance burdens. It reflects China's broader trend of tightening capital controls and safeguarding national security, affecting tech firms and investors with overseas operations. Key changes include: (1) financial institutions face joint liability for processing settlements for non-compliant investments; (2) security reviews now cover transfers and disposals of assets that may affect national security; (3) mandatory reporting of major adverse situations, such as foreign parties demanding asset transfers; (4) look-through supervision requiring pre-reporting for round-trip investments; (5) expanded definitions based on 'substance over form' and penalties for malicious project splitting; (6) exemptions for QDII, Stock Connect, and Cross-boundary Wealth Management Connect, with exceptions for control or significant equity stakes.

telegram · zaihuapd · Aug 21, 13:05

**Background**: Outbound investment by Chinese entities has historically been subject to approval and filing requirements under the 2017 Measures. The new draft aims to strengthen oversight amid concerns about capital flight and national security. Round-trip investment, where domestic residents invest overseas and then back into China, has been a focus of regulatory attention due to its potential for circumventing controls. The draft also aligns with China's broader national security review framework for foreign investment.

<details><summary>References</summary>
<ul>
<li><a href="http://www.xeonlaw.com/index.php?m=home&c=View&a=index&aid=696">返程投资中的外汇管理登记及上市监管案例</a></li>
<li><a href="https://www.hkgcr.com/liangongsichangjianwenti/1541.html">境外企业与返程投资-百利来</a></li>
<li><a href="https://www.gov.cn/gongbao/content/2021/content_5582626.htm">中 华人民共和 国 国 家发展和改革委员会 中 华人民共和 国 商务部令（第37...</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#China`, `#investment`, `#capital controls`, `#policy`

---

<a id="item-6"></a>
## [YMTC STAR Market IPO Accepted, Plans to Raise 33 Billion Yuan](https://api3.cls.cn/share/article/2461025?os=android&amp;sv=8.8.2&amp;app=cailianpress) ⭐️ 8.0/10

Yangtze Memory Technologies Co. (YMTC) has had its STAR Market IPO application accepted by the Shanghai Stock Exchange, with plans to raise 33 billion yuan. The company reported revenue of 47.042 billion yuan and net profit of 33.379 billion yuan for Q1 2026, and according to Counterpoint, it entered the global top three in NAND flash shipments by capacity in Q2 2026. This IPO is a major milestone for China's semiconductor industry, as YMTC is a leading domestic memory chip maker. The large fundraising and its rise to top-three global NAND status could reshape the competitive landscape and boost domestic substitution efforts. The sponsors are CITIC Securities and China Securities Co. (CSC). The IPO acceptance follows a tutoring status change to 'tutoring acceptance' on August 19, with the entire process taking about three months. The company's strong financials and market position highlight its growth trajectory.

telegram · zaihuapd · Aug 21, 14:26

**Background**: The STAR Market is a Shanghai Stock Exchange board designed for technology and innovation companies, with IPO acceptance being an early step in the listing process. NAND flash memory is a type of non-volatile storage used in SSDs and mobile devices, and YMTC is a key player in this sector, competing with global giants like Samsung and SK Hynix.

<details><summary>References</summary>
<ul>
<li><a href="https://www.elecfans.com/article/90/155/2021/05131607826.html">积极布局功率半导体 中车电气 科 创 板 IPO 过会 - 制造新闻 - 电子发烧友网</a></li>
<li><a href="https://m.21jingji.com/article/20260705/herald/5fbd92a95686d13559c5a5aa4b956aeb.html">2天28家！ 科 创 板 IPO 受 理 数量迎高峰 - 21财经</a></li>
<li><a href="https://www.ibm.com/think/topics/nand-flash">What is NAND flash memory? - IBM</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#IPO`, `#存储芯片`, `#科创板`, `#长江存储`

---