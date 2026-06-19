---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 30 items, 11 important content pieces were selected

---

1. [ATProto 没有实例：协议澄清](#item-1) ⭐️ 8.0/10
2. [Project Valhalla 在 JDK 28 中落地：值类型与堆扁平化](#item-2) ⭐️ 8.0/10
3. [新 JAWBONE 法案瞄准政府对在线言论的胁迫](#item-3) ⭐️ 8.0/10
4. [EFF 主张法院记录应免费公开](#item-4) ⭐️ 8.0/10
5. [Datasette Apps：在 Datasette 中托管沙盒化 HTML/JS 应用](#item-5) ⭐️ 8.0/10
6. [中国拟出台分布式数字身份互通互认规定](#item-6) ⭐️ 8.0/10
7. [美国施压 ASML，怀疑 EUV 光刻机流入中国](#item-7) ⭐️ 8.0/10
8. [多款婴儿纸尿裤检出生殖毒性物质甲酰胺](#item-8) ⭐️ 8.0/10
9. [苹果同意在巴西开放第三方应用商店](#item-9) ⭐️ 8.0/10
10. [SpaceX 在 IPO 前向中国投资者出售股份](#item-10) ⭐️ 8.0/10
11. [北航博士校友指控两名教授数据造假](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ATProto 没有实例：协议澄清](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 8.0/10

Dan Abramov 发表文章解释，Bluesky 背后的协议 ATProto 没有像 Mastodon 那样的“实例”，而是将角色分为个人数据服务器（PDS）、中继（Relay）和应用视图（AppView）。 这一澄清解决了将 Bluesky 与 Mastodon 进行比较的新手常有的误解，并突出了 ATProto 在架构上将数据存储、中继和应用逻辑解耦的优势，从而获得更好的可扩展性。 文章使用博客类比：PDS 类似于博客的托管，Relay 类似于 RSS 聚合器，AppView 类似于阅读器应用。与 Mastodon 的单体实例不同，ATProto 允许用户为每个角色选择不同的提供商。

hackernews · danabramov · Jun 19, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: ATProto（认证传输协议）是由 Bluesky 开发的去中心化协议。在 Mastodon（ActivityPub）中，每个服务器都是一个“实例”，负责存储、联邦和用户界面。ATProto 将这些关注点分离：PDS 存储用户数据，Relay 索引和分发数据，AppView 提供用户界面。这种设计旨在提高可扩展性和用户选择权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://getskyscraper.com/blog/atprotocol-federation-architecture-guide">ATProtocol Federation Architecture: PDS, Relay, AppView & How ...</a></li>
<li><a href="https://fediversereport.com/a-conceptual-model-of-atproto-and-activitypub/">A conceptual model of ATProto and ActivityPub – The Fediverse Report</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论讨论了博客类比的准确性，一些人认为 RSS 并不像 Google Reader 那样依赖中央阅读器，而另一些人则称赞 ATProto 的关注点分离是更清晰的系统设计。一些评论者认为文章忽视了 ActivityPub 中实例解决的审核挑战。

**标签**: `#ATProto`, `#decentralization`, `#protocol design`, `#Bluesky`, `#ActivityPub`

---

<a id="item-2"></a>
## [Project Valhalla 在 JDK 28 中落地：值类型与堆扁平化](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Project Valhalla 的值类型和堆扁平化功能将在 JDK 28 中交付，通过允许对象内联存储（无需对象头和指针），从根本上改变了 JVM 内存布局。 这是 JVM 长达十年的演进，大幅提升了数据密集型应用的内存密度和性能，但也引发了关于空安全、统一性等设计权衡的讨论。 堆扁平化仅对表示不超过 64 位的对象有效；更大的对象仍需间接引用。空标志会增加开销，而值类通过使赋值行为依赖于类类型，破坏了统一性原则。

hackernews · philonoist · Jun 19, 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Project Valhalla 是 2014 年宣布的 OpenJDK 项目，由 Brian Goetz 领导，旨在为 Java 引入值类型（内联类）。传统上，所有 Java 对象都是带有对象头和指针的引用类型，导致内存开销大、缓存局部性差。值类型消除了对象标识，允许 JVM 将它们直接存储在数组和字段中，无需间接引用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 # ...</a></li>
<li><a href="https://www.baeldung.com/java-valhalla-project">Java Valhalla Project | Baeldung</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出了对堆扁平化限制（仅适用于 ≤64 位对象）、空安全权衡以及违反统一性原则的担忧。也有人为 JVM 的演进辩护，认为许多批评者对 Java 的看法已经过时。

**标签**: `#Java`, `#JVM`, `#Project Valhalla`, `#performance`, `#language design`

---

<a id="item-3"></a>
## [新 JAWBONE 法案瞄准政府对在线言论的胁迫](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech) ⭐️ 8.0/10

参议员 Ted Cruz 和 Ron Wyden 提出了两党合作的 JAWBONE 法案，该法案将禁止联邦机构胁迫在线平台、广播公司和人工智能公司审查合法言论。 该法案解决了对政府施压私人中介压制合法言论日益增长的担忧，可能加强第一修正案保护和平台自主权。 该法案全称为“反对官僚武器化越权干预网络表达正义法案”（JAWBONE Act），EFF 对其提出表示赞赏，同时指出需要谨慎平衡。

hackernews · hn_acker · Jun 19, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600950)

**背景**: 电子前哨基金会（EFF）是一个倡导在线言论自由的数字权利组织。政府通过非正式压力胁迫平台审查内容的行为，常被批评为“代理审查”。JAWBONE 法案旨在将针对此类行为的保护措施写入法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aclu.org/press-releases/aclu-endorses-bipartisan-jawbone-act-to-protect-free-speech">ACLU Endorses Bipartisan JAWBONE Act To Protect Free Speech | American Civil Liberties Union</a></li>
<li><a href="https://laweconcenter.org/resources/government-by-raised-eyebrow-the-jawbone-act-and-the-problem-of-censorship-by-proxy/">Government by Raised Eyebrow: The JAWBONE Act and the Problem of Censorship by Proxy - International Center for Law & Economics</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该法案，但指出政治讽刺性，因为 Cruz 参议员此前曾以所谓的反保守派偏见为由针对平台。一些人还强调，私人平台保留其自身的第一修正案权利来管理内容。

**标签**: `#online speech`, `#government pressure`, `#First Amendment`, `#EFF`, `#bipartisan bill`

---

<a id="item-4"></a>
## [EFF 主张法院记录应免费公开](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 8.0/10

电子前哨基金会（EFF）发表文章，主张法院记录应向公众免费开放，批评 PACER 和州级系统高昂的按页收费，并支持相关立法以现代化访问方式。 此事至关重要，因为公众获取法院记录是透明度和司法公正的基础；高额费用构成了障碍，削弱了法律应被其约束者自由阅读的原则。 PACER 对联邦法院记录按页收费 1 美元，而一些州级系统收费高达每页 10 美元。EFF 支持一项法案，用现代化统一平台取代老旧的 PACER 和 CM/ECF 系统，以改善公众访问并降低长期成本。

hackernews · hn_acker · Jun 19, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600946)

**背景**: PACER（公共法院电子记录访问系统）是美国联邦法院文件的电子公共访问服务，按页收费。EFF 是一家非营利数字权利组织，倡导数字世界的公民自由。CourtListener 和 RECAP 程序是现有的免费共享 PACER 文件的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PACER_(law)">PACER (law) - Wikipedia</a></li>
<li><a href="https://www.eff.org/about">About EFF | Electronic Frontier Foundation</a></li>
<li><a href="https://pacer.uscourts.gov/">Public Access to Court Electronic Records | PACER: Federal Court Records</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈支持，有人指出爱达荷州法院每页收费 10 美元的高昂成本。另有人强调 CourtListener 和 RECAP 是重要的临时解决方案，并希望它们能很快被取代。一位评论者引用了法律应可自由阅读的古老原则，另一位则链接了 Joel Spolsky 关于软件设计的文章。

**标签**: `#legal tech`, `#public access`, `#government transparency`, `#PACER`, `#EFF`

---

<a id="item-5"></a>
## [Datasette Apps：在 Datasette 中托管沙盒化 HTML/JS 应用](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 datasette-apps 插件，允许用户在 Datasette 中托管沙盒化的 HTML+JavaScript 应用，这些应用可以通过存储查询执行只读和写入 SQL 查询。 该插件将 Datasette 从数据发布工具转变为构建自定义交互式数据应用的平台，使用户无需离开 Datasette 生态系统即可创建丰富的前端界面。 应用在严格受限的 iframe 沙盒中运行，具有 `allow-scripts allow-forms` 和注入的 CSP 标头，阻止出站 HTTP 请求，防止数据泄露。该插件还注册了创建、查看、编辑、删除和管理应用访问的权限。

rss · Simon Willison · Jun 18, 23:58

**背景**: Datasette 是一个用于探索和发布数据的开源工具，提供 JSON API 以支持自定义前端。datasette-apps 插件在此基础上允许这些前端直接托管在 Datasette 内部，并使用沙盒化 iframe 隔离不受信任的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps : Host custom HTML applications inside Datasette</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>

</ul>
</details>

**标签**: `#datasette`, `#plugin`, `#sql`, `#web-applications`, `#sandbox`

---

<a id="item-6"></a>
## [中国拟出台分布式数字身份互通互认规定](https://www.cac.gov.cn/2026-06/18/c_1783525605384124.htm) ⭐️ 8.0/10

2026 年 6 月 18 日，国家互联网信息办公室发布了《促进分布式数字身份互通互认应用规定（征求意见稿）》并向社会公开征求意见，截止日期为 2026 年 7 月 18 日。 该规定标志着中国在基于区块链的分布式数字身份标准化方面迈出了重要一步，有望实现金融、交通、海关、税务和数字人民币等领域的跨平台身份互通互认，影响数百万用户和设备。 征求意见稿将分布式数字身份定义为由标识符、密钥、可验证凭证和可验证声明构成，并提议依托国家区块链网络建设身份链。境内外个人、机构和工业设备均可自愿申请注册，相关机构需履行数据安全和个人信息保护义务。

telegram · zaihuapd · Jun 19, 01:39

**背景**: 分布式数字身份是一种基于区块链的身份系统，用户可自主控制身份数据，不同于传统的集中式系统。可验证凭证是由权威机构颁发的防篡改数字文档，可通过密码学验证。中国一直在开发其国家区块链网络 BSN，以支持此类基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wublock123.com/news/cybersecurity-administration-promotes-interoperable-digital-ids-blockchain-network-63105">网信办拟推动分布式数字身份互通，支撑国家区块链网络建设</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/689030887">【深度】DID分布式数字身份(1/5)--什么是DID - 知乎</a></li>

</ul>
</details>

**标签**: `#decentralized identity`, `#regulation`, `#blockchain`, `#China`, `#digital identity`

---

<a id="item-7"></a>
## [美国施压 ASML，怀疑 EUV 光刻机流入中国](https://www.bloomberg.com/news/articles/2026-06-19/us-tells-asml-it-s-concerned-china-may-have-top-chip-tool) ⭐️ 8.0/10

美国商务部长卢特尼克向 ASML 高管表示，一台顶级 EUV 光刻机可能已非法流入中国，违反出口管制。ASML 坚决否认，称从未向中国出口 EUV 整机，全球运行的 314 台设备均不在中国。 此事件加剧了美中芯片出口管制紧张局势，可能导致更严格的对华设备出口法案。同时可能影响美欧关系，因为 ASML 是荷兰公司，对全球半导体供应链至关重要。 美方官员声称掌握 ASML 未善意行事的证据，包括对华出口 EUV 相关运输设备，但拒绝出示。ASML 已散发文件自证清白，并反驳称从未出口任何 EUV 专用组件。

telegram · zaihuapd · Jun 19, 03:09

**背景**: 极紫外（EUV）光刻是一种尖端技术，用于制造最先进的半导体芯片，使用 13.5 纳米波长的光。ASML 是全球唯一的 EUV 光刻系统供应商，这些系统受到严格出口管制，以防止中国获取用于军事现代化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">Extreme ultraviolet lithography - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/euv-lithography-systems">EUV lithography systems – Products | ASML</a></li>
<li><a href="https://nldaily.com/tech/asml-export-controls-china-chip-war/">ASML Export Controls And China : The Dutch Company At The...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#export controls`, `#US-China`, `#ASML`, `#geopolitics`

---

<a id="item-8"></a>
## [多款婴儿纸尿裤检出生殖毒性物质甲酰胺](https://t.me/zaihuapd/42051) ⭐️ 8.0/10

《经济参考报》委托专业机构检测发现，好奇、碧芭宝贝、Babycare 等多个品牌的婴幼儿纸尿裤中含有生殖毒性物质甲酰胺。部分婴幼儿的血液和尿液中也被检出该物质，一名记者穿戴一款纸尿裤一夜后血液浓度飙升近一倍。 这一发现暴露了中国纸尿裤国家标准中的监管空白——目前国标未对甲酰胺进行检测，而该物质已知具有毒性。这对婴幼儿构成严重的健康风险，因为婴幼儿特别容易受到该化合物对生殖系统、肝脏和肾脏的损害。 甲酰胺被欧盟列为 1B 类生殖毒性物质，并在中国化妆品目录中被禁用，但现行纸尿裤国标（GB/T 28004.1-2021）未将其纳入检测。专家呼吁尽快修订国标，将甲酰胺等有毒物质纳入强制检测目录并设定安全限量。

telegram · zaihuapd · Jun 19, 06:05

**背景**: 甲酰胺是一种用于生产某些塑料和粘合剂的化学物质，在纸尿裤制造过程中可能从材料中释放。它已知可通过皮肤吸收并在体内蓄积，可能对生殖系统、肝脏和肾脏造成损害。中国现行的婴儿纸尿裤标准主要关注物理性能和微生物安全，但缺乏对甲酰胺等化学危害物的规定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1038359743_539932">“好奇”、“碧芭宝贝”、“Babycare”多款知名婴儿纸尿裤检测出甲酰胺生殖...</a></li>
<li><a href="https://finance.sina.com.cn/tech/roll/2026-06-18/doc-inicvmmr3319172.shtml">多品牌纸尿裤被检出甲酰胺，动物研究表明甲酰胺具有胚胎毒性和致畸性...</a></li>
<li><a href="https://news.qq.com/rain/a/20260618A0412500">好奇、碧芭宝贝、Babycare等品牌婴幼儿纸尿裤被检出毒性物质甲酰胺，...</a></li>

</ul>
</details>

**社区讨论**: 网上讨论显示家长普遍担忧，许多人报告称宝宝出现严重红臀和皮肤破溃，更换品牌后症状缓解。部分品牌直播间展示了“甲酰胺未检出”的检测报告，但观众仍持怀疑态度，质疑自检的可信度。

**标签**: `#consumer safety`, `#toxicology`, `#regulatory gap`, `#infant health`, `#product testing`

---

<a id="item-9"></a>
## [苹果同意在巴西开放第三方应用商店](https://t.me/zaihuapd/42059) ⭐️ 8.0/10

苹果与巴西反垄断监管机构达成协议，允许 iPhone 用户在 App Store 之外购买应用和服务，并支持第三方应用商店分发，从而结束了一项反竞争行为调查。 这标志着开放应用分发在监管方面取得重大胜利，可能为其他国家树立先例，并迫使苹果在全球范围内调整其利润丰厚的 App Store 模式。 苹果需在 105 天内落实相关改变，协议期为三年。开发者可展示外部支付方式和替代购买链接，但苹果仍可对相关交易收取费用。

telegram · zaihuapd · Jun 19, 11:15

**背景**: 苹果的 App Store 因要求开发者使用其应用内支付系统并收取高达 30%的佣金，在全球面临反垄断审查。欧盟和美国也采取了类似监管行动，欧盟的《数字市场法案》已强制要求支持第三方应用商店。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KHIARRBT0514R9OJ.html">m.163.com/dy/article/KHIARRBT0514R9OJ.html</a></li>
<li><a href="https://macgaga.com/苹果在巴西让步，第三方应用商店来了/">苹 果 在 巴 西 让步， 第 三 方 应 用 商 店 来了 – Mac鸭子</a></li>

</ul>
</details>

**标签**: `#Apple`, `#antitrust`, `#app store`, `#Brazil`, `#regulation`

---

<a id="item-10"></a>
## [SpaceX 在 IPO 前向中国投资者出售股份](https://www.propublica.org/article/spacex-elon-musk-ipo-foreign-investors-china) ⭐️ 8.0/10

ProPublica 获得的法院解密文件显示，SpaceX 在 2018 年至 2021 年间通过中间商 Tomales Bay Capital 向至少十几名位于中国大陆、香港和俄罗斯的投资者出售股份，尽管后来在 IPO 中禁止了此类投资者。 这引发了重大的监管和国家安全担忧，因为 SpaceX 是参与敏感军事项目的美国关键国防承包商，早期的外国投资可能违反了出口管制法律。 每笔投资金额从 80 万到 4000 万美元不等，投资者包括与中国军工承包商有联系的个人以及与卡塔尔王室关联的实体。投资者被承诺获得季度业务更新、参观设施以及与首席财务官会面的机会。

telegram · zaihuapd · Jun 19, 12:00

**背景**: SpaceX 由埃隆·马斯克创立，是一家领先的航空航天公司，为 NASA 和美国军方提供发射服务。其 Starlink 卫星互联网服务也具有双重用途。该公司于 2026 年 6 月上市，IPO 明确排除了来自中国和香港的投资者，原因是美国对国防相关技术的出口限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/spacex-ipo-bans-china-hong-kong-investors/">SpaceX IPO underwriters ban Hong Kong and China investors due ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#IPO`, `#foreign investment`, `#national security`, `#investigative journalism`

---

<a id="item-11"></a>
## [北航博士校友指控两名教授数据造假](https://www.zaobao.com.sg/news/china/story20260619-9231002) ⭐️ 8.0/10

前北京航空航天大学博士生耿江涛公开指控该校两名教授常凌乾和王军的论文数据造假，其中常凌乾的一篇 Nature 论文被指数据“完美到诡异”。大量网民涌入北航官网查询，导致网站一度瘫痪。 此案凸显了中国顶尖大学科研诚信方面的持续问题，尤其是涉及 Nature 等顶级期刊的论文。公众的强烈反应表明学术界对透明度和问责制的需求日益增长。 耿江涛于 2025 年从北航退学后成为科普博主，此前已曝光同济大学、南开大学等高校的五名学者，均被处置。被指控的教授包括医学科学与工程学院副院长常凌乾和航空科学与工程学院教授王军。

telegram · zaihuapd · Jun 19, 16:02

**背景**: 科研不端行为（包括数据造假）是学术界严重的问题，会削弱对科学发现的信任。北京航空航天大学是中国顶尖高校，而 Nature 论文被视为重大成就。耿江涛此前成功曝光多起造假案例，为其打假行为建立了公信力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.buaa.edu.cn/info/1002/65744.htm">《 Nature ...</a></li>
<li><a href="https://www.163.com/dy/article/KQL98JTD051492T3.html?f=post1603_tab_news">同济大学一院长被质疑 Nature ...</a></li>
<li><a href="https://www.xiaoyuzhoufm.com/episode/6a26d0adb30e1571aea2d05a">E898. 耿 同 学 ：用 学 术 打 假 ，赶走实验室里的大象 - 故事FM</a></li>

</ul>
</details>

**标签**: `#academic misconduct`, `#research integrity`, `#China`, `#Beihang University`, `#paper retraction`

---