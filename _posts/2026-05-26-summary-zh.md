---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 27 items, 7 important content pieces were selected

---

1. [DynIP 推出支持 RFC 2136 的现代动态 DNS 服务](#item-1) ⭐️ 8.0/10
2. [荷兰阻止美国收购数字身份服务商 Solvinity](#item-2) ⭐️ 8.0/10
3. [微软 Copilot Cowork 漏洞导致数据泄露](#item-3) ⭐️ 8.0/10
4. [教宗良十四世发布人工智能伦理通谕](#item-4) ⭐️ 8.0/10
5. [伊朗计划永久断开全球互联网](#item-5) ⭐️ 8.0/10
6. [中国审查 Meta 收购 Manus，创始人被限制离境](#item-6) ⭐️ 8.0/10
7. [支付宝发布 Token Pay 和 AI 钱包](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DynIP 推出支持 RFC 2136 的现代动态 DNS 服务](https://dynip.dev/) ⭐️ 8.0/10

DynIP 是一项新的动态 DNS 服务，支持 RFC 2136/TSIG 更新、IPv6、DNSSEC，并能原生集成 FortiGate 和 MikroTik 设备，无需自定义客户端。 这填补了 DDNS 市场的空白——大多数服务依赖专有的仅 HTTP 协议，缺乏 IPv6 和 DNSSEC 等现代特性，使网络工程师能更轻松地维护可靠、安全的动态 DNS。 DynIP 使用 RFC 2136 DNS UPDATE 和 TSIG 认证作为主要更新方式，并为无法使用 DNS UPDATE 的设备提供 HTTP API。它支持端到端 IPv6 和 DNSSEC 签名。

hackernews · dynip · May 26, 07:35 · [社区讨论](https://news.ycombinator.com/item?id=48276363)

**背景**: 动态 DNS（DDNS）允许 IP 地址变化的设备保持固定的主机名。RFC 2136 定义了动态更新 DNS 记录的标准协议，但许多 DDNS 服务使用专有 API。IPv6 和 DNSSEC 对现代网络越来越重要，但传统 DDNS 提供商通常缺乏这些功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2136">RFC 2136 - Dynamic Updates in the Domain Name System (DNS UPDATE)</a></li>
<li><a href="https://docs.netgate.com/pfsense/en/latest/services/dyndns/rfc2136.html">Configuring RFC 2136 Dynamic DNS updates - Netgate Documentation</a></li>
<li><a href="https://docs.fortinet.com/document/fortigate/7.6.3/administration-guide/685361/ddns">DDNS | FortiGate / FortiOS 7.6.3 | Fortinet Document Library</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户称赞 RFC 2136 支持使与 Kubernetes external-dns 和网络设备的集成更简单。一些用户指出使用 BIND9 自建虽然可行但不够方便，还有评论者建议着陆页可以更有特色。

**标签**: `#DNS`, `#DDNS`, `#IPv6`, `#DNSSEC`, `#networking`

---

<a id="item-2"></a>
## [荷兰阻止美国收购数字身份服务商 Solvinity](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 8.0/10

荷兰政府以国家安全和隐私为由，阻止了美国公司 Kyndryl 对 Solvinity 的收购，Solvinity 是托管荷兰国家数字身份系统 DigiD 的云服务商。 这一决定凸显了围绕数字主权的日益加剧的地缘政治紧张局势，以及关键国家基础设施面临外国法律和情报压力（尤其是来自美国）的脆弱性。 Solvinity 托管着 DigiD，该系统每年为荷兰政府服务处理超过 5.5 亿次登录。在议会投票决定终止与 Solvinity 的合同后，政府却延长了合同，随后阻止了 IBM 分拆公司 Kyndryl 的收购。

hackernews · vrganj · May 26, 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48278406)

**背景**: DigiD 是荷兰中央数字身份系统，公民用它访问政府服务、医疗、税务和福利。担忧在于，若 Solvinity 被美国公司收购，美国法律（如《爱国者法案》）可能强制其交出数据，从而破坏荷兰的隐私保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://p4sc4l.substack.com/p/dutch-digital-identity-infrastructure">Dutch digital identity infrastructure could become vulnerable to American legal, intelligence, sanctions, and political pressure.</a></li>
<li><a href="https://thepolder.news/the-netherlands-built-its-digital-identity-on-foreign-infrastructure-now-its-paying-the-price">Digital Identity: Lessons from the DigiD Case - The Polder News</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持这一阻止决定，许多人强调架构层面的隐私优于政策层面的隐私。一些人质疑荷兰为何不能为 2000 万用户自建开源身份解决方案。

**标签**: `#digital sovereignty`, `#privacy`, `#geopolitics`, `#critical infrastructure`, `#identity management`

---

<a id="item-3"></a>
## [微软 Copilot Cowork 漏洞导致数据泄露](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

微软 Copilot Cowork 存在提示注入漏洞，攻击者可通过在代理发送的邮件中嵌入外部图片，当用户打开邮件时触发网络请求，从而窃取文件。 该漏洞凸显了自主 AI 系统面临的关键安全挑战，可能导致广泛使用的企业产品中出现未经授权的数据泄露，影响数百万 Microsoft 365 用户。 该攻击利用了 Copilot Cowork 可在未经批准的情况下向用户收件箱发送邮件，且这些邮件可包含外部图片，通过预认证的 OneDrive 下载链接泄露数据。

rss · Simon Willison · May 26, 15:36

**背景**: 提示注入是一种安全漏洞，精心设计的输入会导致 AI 模型意外行为，绕过安全防护。在像 Copilot Cowork 这样的自主系统中，它可以代表用户执行操作，此类漏洞可能导致数据泄露。邮件中的外部图片可触发向攻击者控制的服务器发送网络请求，从而实现数据窃取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者对漏洞的严重性表示担忧，指出这凸显了在缺乏适当防护的情况下授予 AI 代理发送邮件能力的固有风险。一些人讨论了微软的设计选择是否充分优先考虑了安全性。

**标签**: `#security`, `#AI`, `#prompt injection`, `#Microsoft Copilot`, `#data exfiltration`

---

<a id="item-4"></a>
## [教宗良十四世发布人工智能伦理通谕](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

2026 年 5 月 25 日，教宗良十四世发布了首道通谕《Magnifica Humanitas》，为人工智能融入社会提供伦理指导，并类比教宗良十三世关于工业革命的《Rerum novarum》。 这道通谕意义重大，因为它从一个重要全球机构的角度为人工智能提供了清晰、权威的伦理原则，影响公共讨论和政策。它将人工智能视为类似劳工权利的社会问题，强调人类尊严和正义。 通谕强调了 AI 系统的可解释性问题，指出它们更多是“培育”而非“建造”，其内部过程仍未知。它还强调真正的发展必须以人为中心，而不是将成本转嫁给他人。

rss · Simon Willison · May 25, 23:58

**背景**: 通谕是教宗写给主教们的正式信函，就信仰或道德问题提供指导。教宗良十三世于 1891 年发布的《Rerum novarum》关注工业革命时期工人阶级的状况，是天主教社会训导的基础文献。教宗良十四世选择此名以纪念良十三世，并将人工智能视为新的工业革命来应对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Encyclical">Encyclical</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rerum_novarum">Rerum novarum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica humanitas</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#Vatican`, `#encyclical`, `#technology and society`, `#Pope Leo XIV`

---

<a id="item-5"></a>
## [伊朗计划永久断开全球互联网](https://t.me/zaihuapd/41574) ⭐️ 8.0/10

据数字权利活动人士和 Filterwatch 组织的报告，伊朗正计划永久断开与全球互联网的连接，仅允许通过政府审查的人员访问经过过滤的版本。 此举可能为互联网碎片化和国家控制的数字边界树立危险先例，严重限制伊朗公民的数字权利，并使该国与全球信息流隔绝。 该计划被描述为“政府特权”，将创建一个所有人都可访问的国内平行网络（国家信息网络），而国际访问需要安全审查。当前的互联网封锁始于 1 月 8 日，此前发生了 12 天的抗议活动。

telegram · zaihuapd · May 26, 06:36

**背景**: 伊朗长期推行“清真互联网”或国家信息网络，这是一个旨在控制和监控公民通信的封闭内联网。这一概念可追溯到 2005 年，第一阶段于 2017 年启动。Filterwatch 是一个监测伊朗互联网政策和基础设施的研究中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://filter.watch/english/about-us/">About - Filterwatch</a></li>
<li><a href="https://en.wikipedia.org/wiki/National_intranet">National intranet - Wikipedia</a></li>
<li><a href="https://rsf.org/en/iran-creates-halal-internet-control-online-information">Iran creates “ Halal Internet ” to control online information | RSF</a></li>

</ul>
</details>

**标签**: `#internet censorship`, `#digital rights`, `#geopolitics`, `#Iran`

---

<a id="item-6"></a>
## [中国审查 Meta 收购 Manus，创始人被限制离境](https://t.me/zaihuapd/41577) ⭐️ 8.0/10

中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 的交易，该公司首席执行官肖红和首席科学家季一超在调查期间被限制离境。 此案凸显了 AI 监管领域地缘政治紧张局势的升级，中国试图阻止其认为的“阴谋性”掏空技术基础的行为，可能为未来的跨境科技收购树立先例。 该收购于 2025 年 12 月宣布，金额未公开。中国国家发展和改革委员会随后阻止了这笔交易，要求撤回收购。

telegram · zaihuapd · May 26, 09:56

**背景**: Manus 是一家由蝴蝶效应公司创立的 AI 智能体初创公司，灵感来源于 AI 编程工具 Cursor。Meta 于 2025 年 12 月宣布收购，计划将 Manus 整合到其服务中。中国政府的审查反映了在中美 AI 竞争背景下对技术转让和国家安全的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/04/28/china-meta-manus-ai-deal.html">Op-ed: In blocking Meta-Manus deal, China sent a powerful reminder to Mark Zuckerberg and U.S. market about AI race</a></li>
<li><a href="https://arstechnica.com/ai/2026/04/china-kills-metas-acquisition-of-manus-as-us-china-ai-rivalry-deepens/">China kills Meta’s acquisition of Manus as US-China AI rivalry deepens - Ars Technica</a></li>

</ul>
</details>

**标签**: `#AI`, `#regulation`, `#Meta`, `#acquisition`, `#geopolitics`

---

<a id="item-7"></a>
## [支付宝发布 Token Pay 和 AI 钱包](https://finance.sina.com.cn/jjxw/2026-05-26/doc-inhzffss1524895.shtml) ⭐️ 8.0/10

2026 年 5 月 26 日，支付宝推出了 Token Pay 服务（用于 AI 模型订阅支付）和 AI 钱包（用于管理 AI 智能体支付）。用户即日起可在支付宝搜索“AI 钱包”体验该服务。 这标志着 AI 与支付系统深度融合的重要一步，为 AI 模型和自主智能体的交易提供了无缝的货币化途径。通过简化用户和 AI 公司的支付流程，可能加速 AI 服务的普及。 Token Pay 支持全球用户订阅和端内充 Token，面向大模型公司。MiniMax 和阶跃星辰已与支付宝合作，多个 AI 原生产品将采用该支付方案。

telegram · zaihuapd · May 26, 12:31

**背景**: AI 模型通常需要用户购买 Token 或订阅才能使用其服务，但现有支付系统并未针对这类微交易进行优化。支付宝的 Token Pay 和 AI 钱包旨在填补这一空白，为 AI 服务和自主智能体提供专用支付基础设施，使智能体能够代表用户做出动态决策并执行支付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buaq.net/go-418958.html">支 付 宝 ：完成 3 亿笔 AI 付 ，发布 AI 钱包和 Token Pay</a></li>

</ul>
</details>

**标签**: `#Alipay`, `#AI Wallet`, `#Token Pay`, `#AI payments`, `#Fintech`

---