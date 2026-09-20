---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> From 24 items, 5 important content pieces were selected

---

1. [AI 编造情报差点引发美军登临中国船只](#item-1) ⭐️ 9.0/10
2. [ChatGPT 通过 OpenAI 广告收集器跨网站追踪用户](#item-2) ⭐️ 8.0/10
3. [Qwen Image 2.1：7B 开源权重文生图模型，支持原生透明](#item-3) ⭐️ 8.0/10
4. [长鑫科技第五代 DRAM 技术平台正式量产](#item-4) ⭐️ 8.0/10
5. [斯坦福研究：大脑实为两个独立演化的器官](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 编造情报差点引发美军登临中国船只](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 9.0/10

据 CNN 2026 年 9 月 18 日报道，美国特种作战司令部一名情报分析员使用 AI 聊天机器人融合公开来源情报与机密信号情报，机器人错误识别了一艘中国船只的货物清单。该分析员随后又用 AI 将错误结论包装成正式情报报告并分发至各指挥层级，导致美军启动拦截计划，武装人员准备登船、军机已经起飞，直到行动前夕官员追查报告来源才发现整份报告由 AI 生成。 这是目前最具体的真实案例之一：AI 幻觉几乎触发了一场针对他国的实际军事行动，说明生成式 AI 的失误不再是假设性风险，而可能升级为国际事件。这也对日益依赖 AI 的国防情报流程提出了紧迫问题：如何验证、如何保留人工监督、以及由谁承担责任。 这次失误包含两个独立的 AI 环节：先是聊天机器人错误识别船上货物，随后又被用来把错误结论整理成格式规范、看似权威的正式情报报告，使其在逐级上报过程中获得了虚假的可信度。据四名知情人士透露，直到计划行动前夕官员深挖报告来源时问题才被发现，其中两人称武装人员已准备登船、军机已经起飞。

telegram · zaihuapd · Sep 20, 03:07

**背景**: AI 幻觉指大语言模型生成看似事实、实则虚假或误导性的内容，通常是因为它“看到”了并不存在的模式。在情报工作中，分析员需要把来自公开数据的公开来源情报（OSINT）与机密信号情报（SIGINT）融合，形成评估结论，而美国特种作战司令部已公开表示希望在作战的各个方面更多使用 AI 与机器学习。此次事件表明，当这类工具在缺乏充分验证的情况下被嵌入情报融合与报告流程时，会产生怎样的后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.crossroadstoday.com/news/politics/national-politics/exclusive-us-military-had-close-call-after-using-ai-for-false-intelligence-report-sources-say/article_187e430e-17f0-5435-ae27-4f768e28b126.html">Exclusive: US military had close call after using AI for false intelligence report, sources say | National Politics | crossroadstoday.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence ) - Wikipedia</a></li>
<li><a href="https://www.war.gov/News/News-Stories/Article/Article/2438076/special-operations-strives-to-use-the-power-of-artificial-intelligence/">Special Operations Strives to Use the Power of Artificial Intelligence > U.S. Department of War > Defense Department News | U.S. Department of War</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#military AI`, `#hallucination`, `#national security`, `#geopolitics`

---

<a id="item-2"></a>
## [ChatGPT 通过 OpenAI 广告收集器跨网站追踪用户](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) ⭐️ 8.0/10

一份报告披露，OpenAI 在 .openai.com 上设置了一个名为 __obi 的跨站追踪 Cookie，有效期为一年；当用户访问那些在 ChatGPT 上投放广告并安装了 OpenAI 广告像素的网站时，该 Cookie 会被回传给 OpenAI。作者在自己的手机上用两种独立的抓包方法复现了这一机制，并对照了数月流量数据，覆盖 1029 个主机名上的 936 个不同广告主像素。 这意味着 OpenAI 能够把用户在广告主网站上的浏览、搜索和购买行为直接关联到其已登录的 ChatGPT 账户，将标准的广告技术监控延伸到一个用户通常期望更高隐私保护的 AI 聊天产品中。该消息在 Hacker News 上引发激烈讨论（526 分、298 条评论），凸显出 AI 商业化与用户隐私预期之间日益加剧的矛盾。 该机制本身属于标准广告技术，与零售商早已用于 Meta 和 Google 追踪代码的模式相同，但将其应用于 AI 聊天产品尚无先例。浏览器防护情况不一：根据 MDN 的说明，Firefox、Brave 和 Safari 会阻止此类跨站追踪，而 Chrome 和 Edge 不会，导致许多用户默认处于暴露状态。

hackernews · lmbbuchodi · Sep 20, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=49776729)

**背景**: 跨站追踪 Cookie 是一种小型标识符，使公司能够在不同网站之间识别同一用户，通常用于构建广告画像。广告像素是公司放在自己网站上的代码片段，用于把访客行为回传给广告平台。OpenAI 的 __obi Cookie 与已登录的 ChatGPT 账户绑定，因此广告主网站上的活动可以关联到具体用户身份，而非匿名浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-tldr.dev/releases/openai-obi-ad-tracker/">OpenAI's __obi cookie — ChatGPT accounts tracked… | AI/TLDR</a></li>
<li><a href="https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/">ChatGPT now knows what you do on other websites via ad collector</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍谴责这一做法：有人称赞欧盟立法对此类追踪的打击，有人引用称该机制虽是标准广告技术，但用在 AI 聊天产品上史无前例，仍让人感到“恶心”。其他人指出 Firefox、Brave 和 Safari 会拦截它，而 Chrome 和 Edge 不会，还有多人强调用户对付费 AI 对话与 Facebook 这类免费服务的隐私预期截然不同。

**标签**: `#privacy`, `#adtech`, `#ChatGPT`, `#tracking`, `#AI`

---

<a id="item-3"></a>
## [Qwen Image 2.1：7B 开源权重文生图模型，支持原生透明](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen 发布了 Qwen Image 2.1，这是一个 7B 参数的开源权重文生图与图像编辑模型，改进了文字渲染并新增了原生透明（alpha 通道）支持。它比上一代 20B 的 Qwen-Image 1 小得多，并已在 Day 0 原生支持 ComfyUI，权重可在 Hugging Face 下载。 该模型强大的文字渲染能力使其特别适用于海报、横幅、UI 原型和产品标签等对叠加文字准确性要求很高的场景。更小的 7B 体积也降低了本地部署门槛，但更严格的许可证可能会限制其商业采用，相比采用宽松许可证的替代方案处于劣势。 Qwen Image 2.1 是一个统一的文生图与图像编辑模型，宣称支持原生 2K 模式和专业排版。但与早期采用 Apache 2.0 的 Qwen 模型不同，本次发布采用了严格得多的许可证，这引起了从业者的担忧。

hackernews · jmillikin · Sep 20, 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 文生图扩散模型根据文本提示生成图像，开源权重发布让用户可以在本地运行或微调。原生透明意味着模型直接生成带有 alpha 通道的图像，而无需依赖后处理抠图，这是少数开源模型才具备的能力。Qwen 是阿里巴巴的模型系列，此前的 Qwen-Image 以强大的文字渲染和宽松的 Apache 2.0 许可证著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen / Qwen - Image - 2 . 1 · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen-Image-2.1">GitHub - QwenLM/ Qwen - Image - 2 . 1 : Qwen 's most powerful...</a></li>
<li><a href="https://kie.ai/blog/what-is-qwen-image-2-1">What Is Qwen - Image - 2 . 1 ? Native 2K Editing</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者称赞该模型紧凑的 7B 体积、原生透明以及大幅改进的文字渲染，一位从业者称其为开源权重市场上文字渲染最好的模型。主要批评集中在相比早期 Apache 许可的 Qwen 模型更为严格的许可证上，也有用户询问如何在 ComfyUI 之外本地运行它。

**标签**: `#text-to-image`, `#open-weight models`, `#Qwen`, `#AI/ML`, `#licensing`

---

<a id="item-4"></a>
## [长鑫科技第五代 DRAM 技术平台正式量产](https://m.thepaper.cn/newsDetail_forward_34108116) ⭐️ 8.0/10

9 月 20 日，在 2026 世界制造业大会上，长鑫科技宣布第五代技术平台正式量产，基于该平台打造的 24GB LPDDR5X 产品已进入量产，并全面进入国产主流旗舰手机。该平台将内存阵列有源区半间距缩至 11.95 纳米，存储器电容深宽比达 45:1，核心动能区高度降至 6762 纳米，同等条件下每张晶圆产出较上一代提升 50%以上。 这是中国本土半导体产业的重大里程碑，长鑫科技将最先进的 DRAM 节点推入大规模量产，并成功进入国产旗舰手机供应链。此举增强了中国存储供应链的自主可控能力，也加剧了长期由三星、SK 海力士和美光主导的全球 DRAM 市场竞争。 11.95 纳米的有源区半间距使该平台跻身先进的“10 纳米级”DRAM 世代，45:1 的电容深宽比和 6762 纳米的核心高度则体现了工艺重新设计以及高介电常数金属栅（HKMG）的整合。每张晶圆产出提升 50%以上是关键经济指标，因为更高的每片晶圆良品数可直接降低单位比特成本。

telegram · zaihuapd · Sep 20, 05:19

**背景**: DRAM 是手机、个人电脑和服务器中用于处理工作数据的主要易失性存储器，而 LPDDR5X 是旗舰智能手机采用的增强型低功耗版本。DRAM 工艺节点以存储单元阵列有源区的半间距命名，当前芯片属于“10 纳米级”（D1x、D1y、D1z、D1α），范围约从 19 纳米到 10 纳米。存储电容的深宽比是微缩的核心挑战：随着单元缩小，深孔电容必须保持足够电容量以存储电荷，因此需要更高的深宽比和新材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/en/news/info_22.html">CXMT Announces Mass Production of 5th-Generation DRAM ... - CXMT</a></li>
<li><a href="https://www.imec-int.com/en/articles/technology-platform-thermally-stable-dram-peripheral-transistors">DRAM peripheral transistors technology platform | imec</a></li>
<li><a href="https://en.wikipedia.org/wiki/LPDDR">LPDDR - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#LPDDR5X`, `#China-tech`, `#memory`

---

<a id="item-5"></a>
## [斯坦福研究：大脑实为两个独立演化的器官](https://www.solidot.org/story?sid=85426) ⭐️ 8.0/10

斯坦福大学医学院的研究人员发现，大脑由两个截然不同、彼此互斥的祖细胞群发育而来，它们在数亿年间独立演化，推翻了长期以来认为大脑有单一共同起源的主流模型。研究团队通过观察发育中的小鼠胚胎，识别出一种表达 Otx2 基因、发育为前脑和中脑的细胞群，以及另一种表达 Gbx2 基因、发育为后脑的细胞群。 这一发现挑战了数百年来将大脑视为单一器官的观点，可能重塑神经科学家和演化生物学家对大脑发育、疾病以及人类认知起源的理解。它还可能影响研究人员对以不同方式影响不同脑区的神经系统疾病进行建模的方式。 这两个祖细胞群从不重叠，在发育的最早阶段就彼此互斥；表观基因组分析显示，前部与后部神经组织在极早期就已具有不同的染色质结构。该研究是在小鼠胚胎中进行的，因此还需要进一步工作来在人类中验证这些发现。

telegram · zaihuapd · Sep 20, 12:11

**背景**: 祖细胞是能够分化成多种成熟细胞类型的早期细胞，在大脑中它们会生成神经元和其他神经细胞类型。Otx2 和 Gbx2 是已知在发育中神经系统前后区域特化过程中起关键作用的同源盒转录因子基因。传统模型认为，单一的祖先祖细胞群产生了整个大脑，这意味着所有脑区都有共同的发育起源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medicalxpress.com/news/2026-09-human-brain.html">Human brain has a split origin, new research suggests</a></li>
<li><a href="https://neurosciencenews.com/brain-separate-organs-evolution-31219/">The Brain Is Two Separate Organs Joined by Evolution</a></li>
<li><a href="https://nautil.us/you-have-two-brains-not-one-1285111">You Have Two Brains , Not One - Nautilus</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#brain development`, `#evolutionary biology`, `#stem cells`, `#Nature`

---