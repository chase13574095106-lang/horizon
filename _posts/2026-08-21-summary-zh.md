---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> From 32 items, 6 important content pieces were selected

---

1. [美国公民因在边境删除手机数据面临重罪指控](#item-1) ⭐️ 8.0/10
2. [配置错误的 e164.arpa 区域暴露军事通话路由查询](#item-2) ⭐️ 8.0/10
3. [DeepSeek 推出具备视觉能力的 V4-Flash-Vision-Exp 模型](#item-3) ⭐️ 8.0/10
4. [Anthropic 扫描数百万册图书训练 AI，面临 LibGen 盗版指控](#item-4) ⭐️ 8.0/10
5. [中国收紧对外投资新规草案](#item-5) ⭐️ 8.0/10
6. [长江存储科创板 IPO 获受理，拟融资 330 亿元](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美国公民因在边境删除手机数据面临重罪指控](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) ⭐️ 8.0/10

据《纽约时报》报道，美国公民 Samuel Tunick 因在边境检查期间删除手机数据而面临重罪指控。这标志着试图在美国边境保护数字隐私的旅行者将面临更严重的法律后果。 此案引发了关于边境安全与数字隐私权之间平衡的关键问题，可能为政府如何处理边境搜查中的数据删除行为树立先例。这可能对旅行者携带敏感数据过境的意愿产生寒蝉效应，并可能引发对边境搜查原则的法律挑战。 指控源于 Tunick 在边境人员检查其手机时删除数据的事件。此案凸显了允许边境无证搜查的“边境原则”周围的法律灰色地带，以及个人试图保护数据时可能面临的妨碍司法指控。

hackernews · floathub · Aug 21, 12:10 · [社区讨论](https://news.ycombinator.com/item?id=49386895)

**背景**: “边境原则”是一个有争议的法律原则，允许美国边境对旅行者及其财物（包括电子设备）进行无证搜查。法院普遍支持这一原则，但隐私倡导者认为数字设备包含大量个人数据，应需要搜查令。第四修正案保护免受不合理搜查，但其在边境的适用受到限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2018/10/feds-agree-to-delete-data-seized-off-womans-iphone-during-border-search/">Feds took woman’s iPhone at border , she sued, now... - Ars Technica</a></li>
<li><a href="https://www.humanrightsfirst.org/library/know-your-rights-protecting-digital-privacy-at-the-border">Know Your Rights: Protecting Digital Privacy at the Border</a></li>
<li><a href="https://www.eff.org/wp/digital-privacy-us-border-2017">Digital Privacy at the U.S. Border: Protecting the Data On Your Devices | Electronic Frontier Foundation</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了愤世嫉俗和实用建议的混合情绪。一些评论者认为美国已变得越来越威权，将其比作东德或苏联时代，而另一些人则建议使用一次性手机或加密镜像等技术变通方法来保护数据。还有人对政府越权表示不满，并担忧公民自由的侵蚀。

**标签**: `#privacy`, `#border search`, `#digital rights`, `#surveillance`, `#legal`

---

<a id="item-2"></a>
## [配置错误的 e164.arpa 区域暴露军事通话路由查询](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

一名安全研究人员意外发现了一个配置错误的 e164.arpa 区域，使其能够拦截用于将电话路由到军事基地的 DNS 查询。这暴露了公共 ENUM 系统中的一个严重隐私漏洞，该系统将电话号码转换为互联网地址。 该漏洞可能允许恶意行为者拦截或重定向到敏感军事和政府号码的电话，导致潜在的间谍活动或隐私泄露。它凸显了老化的 ENUM 基础设施的脆弱性，以及加强电话路由安全措施的必要性。 作者没有设置 SIP 服务器来测试实际呼叫终止，但这一发现足以引起警觉。e164.arpa 区域由 RIPE NCC 根据 IAB 指令运营，虽然公共 ENUM 基本已死，但私有 ENUM 服务仍用于号码携带信息。

hackernews · gavide · Aug 21, 13:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**背景**: ENUM（电话号码映射）是一种使用 DNS 将电话号码映射到互联网地址的标准，支持 VoIP 和统一通信。e164.arpa 区域是 ENUM 的顶级域，由互联网架构委员会（IAB）管理，并由 RIPE NCC 运营。公共 ENUM 从未被广泛采用，但运营商使用私有 ENUM 服务进行号码携带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://www.internic.net/zones/arpa.zone">internic.net/ zones / arpa . zone</a></li>
<li><a href="https://www.voip-info.org/enum/">ENUM - The bridge between the switched telephony network and the Internet - VoIP-Info</a></li>

</ul>
</details>

**社区讨论**: 评论者对作者报告问题后未被监禁表示惊讶，有些人希望作者设置 SIP 服务器以查看呼叫是否可以被终止。其他人指出私有 ENUM 服务仍然存在并用于号码携带，一位评论者提到了 TRIP 模式作为替代方案。

**标签**: `#security`, `#telephony`, `#ENUM`, `#privacy`, `#infrastructure`

---

<a id="item-3"></a>
## [DeepSeek 推出具备视觉能力的 V4-Flash-Vision-Exp 模型](https://api-docs.deepseek.com/guides/vision/) ⭐️ 8.0/10

DeepSeek 发布了一款实验性多模态模型 DeepSeek-V4-Flash-Vision-Exp，现已在其 API 平台上可用。该变体在保留 DeepSeek-V4-Flash 文本能力的同时，新增了视觉理解功能。 此次发布解决了 DeepSeek 模型此前缺乏原生视觉能力的已知局限，使 DeepSeek 在多模态 AI 领域更具竞争力。对于开源权重 AI 实验室而言尤为重要，因为它提供了 Anthropic Claude 等专有模型的视觉能力替代方案。 该模型在文本基准测试（包括智能体、推理和世界知识）上与 DeepSeek-V4-Flash 持平，并在多模态智能体基准上表现强劲。推理前图像会被缩放至约 800×800 像素，且与文本 token 一起计费；但此分辨率可能不足以处理整页 A4/Letter 的 OCR 任务。

hackernews · dares2573 · Aug 21, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=49386163)

**背景**: DeepSeek 是一家中国 AI 研究公司，以开源权重的大型语言模型（如 DeepSeek-V4 和 DeepSeek-R1）而闻名。此前，其模型缺乏原生视觉能力，导致一些用户反映模型在要求分析图像时会虚构视觉工具。这款新的实验模型旨在通过将视觉理解直接集成到模型中，填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/updates/">Change Log | DeepSeek API Docs</a></li>
<li><a href="https://x.com/deepseek_ai/status/2090730032574631962">DeepSeek on X: "DeepSeek-V4-Flash-Vision-Exp is now live on the DeepSeek API Platform! 🚀 🔹 This experimental multimodal model matches DeepSeek-V4-Flash on text capabilities—including agents, reasoning, and world knowledge. 🔹 On multimodal agent benchmarks, V4-Flash-Vision-Exp makes a major" / X</a></li>
<li><a href="https://officechai.com/ai/deepseek-releases-v4-flash-vision-exp-matches-opus-4-8-on-some-multimodal-benchmarks/">DeepSeek Releases V4-Flash-Vision-Exp, Matches Opus 4.8 On Some Multimodal Benchmarks</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户对新视觉能力持乐观态度，认为它可以替代对其他模型进行截图分析的需求，而另一些用户则报告在简单任务（如读取时钟）上失败，而较小的模型能正确处理。还有人担心图像分辨率限制对 OCR 应用的影响，部分用户指出旧版本模型倾向于虚构视觉工具的问题。

**标签**: `#DeepSeek`, `#vision model`, `#AI`, `#LLM`, `#multimodal`

---

<a id="item-4"></a>
## [Anthropic 扫描数百万册图书训练 AI，面临 LibGen 盗版指控](https://t.me/zaihuapd/43305) ⭐️ 8.0/10

《华盛顿邮报》报道称，Anthropic 于 2024 年启动“Project Panama”，通过切掉书脊的方式“破坏性扫描”数百万本实体书，投入数千万美元用于训练 Claude 等模型。此外，集体诉讼指控 Anthropic 曾从 LibGen 等“影子图书馆”下载盗版数据，可能面临 15 亿美元罚款。 这一新闻凸显了 AI 行业在数据获取方面的争议性做法，引发了关于版权侵权的重大伦理和法律问题。它可能为 AI 公司如何获取训练数据树立先例，并影响出版商、作者和 AI 开发者等更广泛的生态系统。 该项目涉及对实体书的“破坏性扫描”，Anthropic 据称强调“不想让外界知道”。法官认为扫描用于训练可能属于合理使用，但获取方式可能构成侵权。Anthropic 已在 2025 年 8 月部分和解了诉讼。

telegram · zaihuapd · Aug 21, 04:52

**背景**: Anthropic 是一家以开发 Claude 模型系列而闻名的 AI 公司。训练大型语言模型需要海量文本数据，公司通常使用书籍、文章和网页内容。LibGen 等影子图书馆提供对受版权保护作品的免费访问，这引发了与出版商的纠纷。版权法中的“合理使用”概念是判断此类扫描是否合法的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shadow_library">Shadow library - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Library_Genesis">Library Genesis - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/books/2023/sep/15/four-large-us-publishers-sue-shadow-library-for-alleged-copyright-infringement">Four large US publishers sue ‘shadow library’ for alleged copyright infringement | Books | The Guardian</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#copyright`, `#data acquisition`, `#ethics`

---

<a id="item-5"></a>
## [中国收紧对外投资新规草案](https://yyglxxbsgw.ndrc.gov.cn/htmls/article/article.html?articleId=2c97d16c-9ff00a63-01a0-230bacc4-0001) ⭐️ 8.0/10

中国国家发展和改革委员会发布了《对外投资管理办法（修订征求意见稿）》，拟取代 2017 年版本。草案引入了更严格的资金出境管控，将安全审查范围扩大至存量资产的转让和处分，并加大了对违规行为的惩戒力度。 此次监管改革将对中国企业和金融机构的对外投资产生重大影响，可能减缓跨境资本流动并增加合规负担。这反映了中国收紧资本管制和维护国家安全的总体趋势，对在海外有业务的技术公司和投资者产生影响。 主要变化包括：（1）金融机构为不合规投资办理结算将承担连带责任；（2）安全审查范围扩大至可能影响国家安全的资产转让和处分；（3）重大不利情况（如外方要求转让资产）须强制报告；（4）穿透监管要求返程投资事前报告；（5）基于“实质重于形式”原则扩大定义，并对恶意分拆项目进行处罚；（6）QDII、港股通、跨境理财通等豁免，但获得控制权或重大股权比例时除外。

telegram · zaihuapd · Aug 21, 13:05

**背景**: 中国实体的对外投资历来需遵守 2017 年《企业境外投资管理办法》的核准和备案要求。新草案旨在加强对资本外逃和国家安全的担忧。返程投资，即境内居民在境外设立主体再投资回境内，因其可能规避监管而成为关注焦点。草案也与中国更广泛的外商投资国家安全审查框架保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.xeonlaw.com/index.php?m=home&c=View&a=index&aid=696">返程投资中的外汇管理登记及上市监管案例</a></li>
<li><a href="https://www.hkgcr.com/liangongsichangjianwenti/1541.html">境外企业与返程投资-百利来</a></li>
<li><a href="https://www.gov.cn/gongbao/content/2021/content_5582626.htm">中 华人民共和 国 国 家发展和改革委员会 中 华人民共和 国 商务部令（第37...</a></li>

</ul>
</details>

**标签**: `#regulation`, `#China`, `#investment`, `#capital controls`, `#policy`

---

<a id="item-6"></a>
## [长江存储科创板 IPO 获受理，拟融资 330 亿元](https://api3.cls.cn/share/article/2461025?os=android&amp;sv=8.8.2&amp;app=cailianpress) ⭐️ 8.0/10

长江存储的科创板 IPO 申请已获上交所受理，拟融资 330 亿元。公司 2026 年一季度营收 470.42 亿元，归母净利润 333.79 亿元；据 Counterpoint 数据，2026 年第二季度其按出货容量首次跻身全球 NAND 市场前三。 此次 IPO 是中国半导体行业的重大里程碑，因为长江存储是国内存储芯片龙头。大规模融资及其跻身全球 NAND 前三的地位，可能重塑竞争格局并推动国产替代进程。 保荐机构为中信证券和中信建投。8 月 19 日其 IPO 辅导状态刚变更为辅导验收，全程约三个月。公司强劲的财务表现和市场地位凸显了其增长轨迹。

telegram · zaihuapd · Aug 21, 14:26

**背景**: 科创板是上交所为科技创新企业设立的板块，IPO 受理是上市流程的早期步骤。NAND 闪存是一种非易失性存储，用于固态硬盘和移动设备，长江存储是该领域的重要参与者，与三星、SK 海力士等全球巨头竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.elecfans.com/article/90/155/2021/05131607826.html">积极布局功率半导体 中车电气 科 创 板 IPO 过会 - 制造新闻 - 电子发烧友网</a></li>
<li><a href="https://m.21jingji.com/article/20260705/herald/5fbd92a95686d13559c5a5aa4b956aeb.html">2天28家！ 科 创 板 IPO 受 理 数量迎高峰 - 21财经</a></li>
<li><a href="https://www.ibm.com/think/topics/nand-flash">What is NAND flash memory? - IBM</a></li>

</ul>
</details>

**标签**: `#半导体`, `#IPO`, `#存储芯片`, `#科创板`, `#长江存储`

---