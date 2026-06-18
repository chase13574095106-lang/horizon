---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> From 35 items, 9 important content pieces were selected

---

1. [发现 1 万个 GitHub 仓库分发木马恶意软件](#item-1) ⭐️ 9.0/10
2. [Transformer 论文合著者 Noam Shazeer 加入 OpenAI](#item-2) ⭐️ 9.0/10
3. [GLM-5.2：最强开源权重 LLM 发布](#item-3) ⭐️ 9.0/10
4. [强制同意投诉导致 Elkjop 被罚 180 万欧元](#item-4) ⭐️ 8.0/10
5. [康奈尔大学 CS 6120 高级编译器课程转为自学模式](#item-5) ⭐️ 8.0/10
6. [医院和大学以 90%更低成本重新利用药物](#item-6) ⭐️ 8.0/10
7. [Modos 彩色显示器推动电子纸技术再进一步](#item-7) ⭐️ 8.0/10
8. [多款婴儿纸尿裤检出生殖毒性物质甲酰胺](#item-8) ⭐️ 8.0/10
9. [苹果与英特尔达成初步芯片代工协议](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [发现 1 万个 GitHub 仓库分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

安全研究员 Orchidfiles 发现超过 1 万个 GitHub 仓库在分发木马恶意软件，目标是自动化代理和依赖系统。这些仓库不是分支，名称各异，并不断更新以逃避检测。 这种广泛的供应链攻击威胁着开源生态系统，自动化代理和开发者可能无意中将恶意软件下载到项目中。其规模（1 万个仓库）和主动规避策略使其成为一个重大的安全问题。 恶意软件通过虚假的概念验证漏洞利用和其他欺骗性仓库进行分发。攻击者每隔几小时删除并推送新提交以保持隐蔽，他们针对新仓库而非流行仓库以避免审查。

hackernews · theorchid · Jun 18, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48583928)

**背景**: 针对开源软件的供应链攻击日益增多，攻击者将恶意软件注入到构建工具自动下载的依赖中。GitHub 是一个常见载体，因为开发者经常在未彻底检查的情况下克隆仓库。此次攻击利用了搜索并包含依赖的自动化代理，使其成为一种现代、可扩展的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/orchidfiles/i-discovered-a-large-scale-malware-distribution-campaign-on-github-4m6o">I discovered a large-scale malware distribution campaign on GitHub</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/thousands-of-github-repositories-deliver-fake-poc-exploits-with-malware/">Thousands of GitHub repositories deliver fake PoC exploits with...</a></li>
<li><a href="https://arstechnica.com/security/2025/07/open-source-repositories-are-seeing-a-rash-of-supply-chain-attacks/">Supply-chain attacks on open source software are getting out of hand ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论证实了严重性，用户报告了类似经历，如他们的名字被附加到恶意仓库上。一些人讨论了针对自动化代理以及围绕重大选举的时机，另一些人则分享了自己遭遇的详细记录。

**标签**: `#security`, `#malware`, `#GitHub`, `#supply chain attack`, `#open source`

---

<a id="item-2"></a>
## [Transformer 论文合著者 Noam Shazeer 加入 OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 9.0/10

Noam Shazeer，开创性论文《Attention Is All You Need》的合著者、前 Google Gemini 联合负责人，宣布加入 OpenAI。 此举对 OpenAI 而言是一次重要的人才引进，可能加速其下一代 AI 模型的开发，同时凸显了顶级 AI 实验室之间持续的人才竞争。 Shazeer 于 2024 年通过与 Character.AI 的许可协议重返 Google（他曾在 Character.AI 担任联合创始人），并被任命为 Gemini 联合负责人，随后再次离职加入 OpenAI。

hackernews · lukasgross · Jun 18, 00:26 · [社区讨论](https://news.ycombinator.com/item?id=48578913)

**背景**: Transformer 架构在 2017 年论文《Attention Is All You Need》中提出，通过用自注意力机制取代循环层，彻底改变了深度学习，实现了更高效的训练，并成为 GPT 和 Gemini 等现代大型语言模型的基础。Noam Shazeer 是该论文的八位合著者之一，自 2000 年起在 Google 的 AI 研究中扮演关键角色，曾参与 AdSense 项目，后来共同领导 Gemini。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noam_Shazeer">Noam Shazeer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_architecture">Transformer architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>

</ul>
</details>

**社区讨论**: 社区对 Shazeer 重返 Google 后迅速离职感到惊讶，一些人猜测内部分歧或政治观点可能是原因。其他人则提供了他的职业轨迹和贡献的背景信息，指出他的跳槽对 AI 行业意义重大。

**标签**: `#AI`, `#OpenAI`, `#Google`, `#Transformers`, `#Talent`

---

<a id="item-3"></a>
## [GLM-5.2：最强开源权重 LLM 发布](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai 发布了 GLM-5.2，这是一个拥有 7530 亿参数、采用 MIT 许可证的开源权重大语言模型，在独立基准测试中取得最高分，并支持 100 万 token 的上下文窗口。 此次发布标志着开源 AI 的一个重要里程碑，GLM-5.2 在 Artificial Analysis Intelligence Index 上超越其他开源模型，并在 Code Arena WebDev 排行榜上排名第二，以极低的成本与专有模型竞争。 GLM-5.2 采用混合专家架构，激活参数为 400 亿，模型大小 1.51TB，仅支持文本输入。每个任务消耗的输出 token 数（43k）高于竞争对手（24-37k）。

rss · Simon Willison · Jun 17, 23:58

**背景**: 大语言模型（LLM）是在海量文本数据上训练的人工智能系统，能够生成类似人类的文本。开源权重模型允许开发者下载并在本地运行模型，促进透明度和定制化。混合专家（MoE）模型每个 token 仅激活部分参数，提高效率。100 万 token 的上下文窗口可以处理非常长的文档，例如整个代码仓库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/17/glm-52/">GLM-5.2 is probably the most powerful text-only open weights LLM</a></li>
<li><a href="https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost">Z.ai’s open-weights GLM-5.2 beats GPT-5.5 on multiple long-horizon coding benchmarks for 1/6th the cost | VentureBeat</a></li>
<li><a href="https://explore.n1n.ai/blog/run-glm-5-2-locally-open-weights-guide-2026-06-15">Run GLM-5.2 Locally: A Complete Guide to the Open Weights Coding Model | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai</a></li>

</ul>
</details>

**社区讨论**: 社区对 GLM-5.2 的性能和开放许可证感到兴奋，但一些人注意到其 token 消耗高且缺乏视觉能力。该模型在没有图像输入的情况下取得出色的编码结果，让许多人感到惊讶。

**标签**: `#LLM`, `#open weights`, `#GLM-5.2`, `#AI`, `#benchmarks`

---

<a id="item-4"></a>
## [强制同意投诉导致 Elkjop 被罚 180 万欧元](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

一位隐私倡导者针对 Elkjop 客户俱乐部强制同意的投诉，在五年后导致挪威数据保护局（Datatilsynet）对其处以 180 万欧元的罚款。 此案表明，GDPR 执法可以追究公司将同意作为服务条件的责任，强调同意必须自由给予。它为欧洲各地类似的强制同意做法树立了先例。 该公司辩称，加入客户俱乐部是接收营销优惠的必要条件，但数据保护局裁定这是非法的强制同意。罚款金额反映了违规的严重性和不合规的持续时间。

hackernews · speckx · Jun 18, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48589501)

**背景**: 根据 GDPR，同意必须自由给予、具体、知情且明确。强迫用户将同意数据处理作为服务条件（例如加入客户俱乐部）违反了这一原则。挪威数据保护局以用户为中心的执法而闻名。

**社区讨论**: 评论者赞扬了这一结果和挪威数据保护局以用户为中心的做法，但也指出过程漫长。一些人希望更多人能行使自己的权利，而另一些人则强调了抵制此类做法的挑战，尤其是在美国。

**标签**: `#GDPR`, `#privacy`, `#consent`, `#data protection`, `#regulation`

---

<a id="item-5"></a>
## [康奈尔大学 CS 6120 高级编译器课程转为自学模式](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 8.0/10

康奈尔大学的 CS 6120 高级编译器课程现已作为免费的在线自学资源开放，让全球学习者可以按照自己的节奏学习其内容。 这使得高质量的编译器教育免费向大众开放，可能降低高级系统主题的学习门槛，并培养新一代编译器工程师。 该课程涵盖死代码消除、数据流分析、支配者分析和 SSA 形式等主题，但一些评论者指出，并非所有主题都真正达到“高级”水平。动态编译器部分主要关注跟踪编译，一些专家认为这是一种死胡同。

hackernews · ibobev · Jun 18, 11:04 · [社区讨论](https://news.ycombinator.com/item?id=48583606)

**背景**: 编译器将高级编程语言转换为机器代码。高级编译器课程通常涵盖优化技术和运行时系统。跟踪编译是一种即时编译技术，记录并编译频繁执行的代码路径，但已被基于方法的即时编译（结合类型反馈和去优化）所取代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tracing_just-in-time_compilation">Tracing just-in-time compilation - Wikipedia</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/1852761.1852771">Trace-based compilation in execution environments without interpreters | Proceedings of the 8th International Conference on the Principles and Practice of Programming in Java</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论既赞扬了课程的可用性，也提出了批评意见：titzer 认为跟踪编译是死胡同，课程应涵盖类型反馈、推测和去优化。j2kun 质疑“高级”标签，指出许多主题属于入门编译器课程。

**标签**: `#compilers`, `#education`, `#programming languages`, `#systems`

---

<a id="item-6"></a>
## [医院和大学以 90%更低成本重新利用药物](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

医院和大学正在以极低的成本将现有药物重新用于新用途，为失明和罕见病等疾病提供可负担的治疗方案。 这挑战了传统的药品定价模式，可能大幅降低医疗成本，尤其是对于新药研发往往无利可图的罕见病。 例如，使用贝伐珠单抗（Avastin）治疗黄斑变性每剂约 50 美元，而雷珠单抗（Lucentis）每剂约 1500 美元，尽管两者分子结构相似。

hackernews · giuliomagnifico · Jun 18, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=48583386)

**背景**: 药物重新利用是指研究现有已批准药物用于新的治疗目的。它绕过了许多早期开发成本，使治疗更便宜。然而，未经制造商同意而用于标签外用途的监管途径仍然有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Drug_repurposing">Drug repurposing</a></li>
<li><a href="https://www.fda.gov/news-events/press-announcements/fda-advances-drug-repurposing-address-unmet-medical-needs">FDA Advances Drug Repurposing to Address Unmet Medical Needs</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经历，例如使用 Spravato（艾司氯胺酮）治疗抑郁症，指出艾司氯胺酮是氯胺酮的改良版，为了盈利而获得专利，尽管可能效果较差。其他人则强调了像 Cures Within Reach 这样的非营利组织，它们资助针对亨廷顿病等罕见病的药物重新利用研究。

**标签**: `#drug repurposing`, `#healthcare costs`, `#pharmaceuticals`, `#rare diseases`, `#health policy`

---

<a id="item-7"></a>
## [Modos 彩色显示器推动电子纸技术再进一步](https://spectrum.ieee.org/modos-e-paper-monitor) ⭐️ 8.0/10

两人初创公司 Modos 正在开发 Modos Flow，这是一款 13.3 英寸彩色电子纸显示器，原生分辨率 3200x2400，支持触控输入，并通过基于 FPGA 的新型显示控制器实现了 60Hz 刷新率。 这标志着电子纸技术的重大飞跃，提供了彩色、高分辨率和流畅的 60Hz 刷新率，可能使电子纸适用于通用计算，相比传统 LCD 减少眼疲劳和功耗。 Modos Flow 基于早期的 Modos Paper 开发套件，在单色面板上使用彩色滤光阵列（CFA），类似于彩色 LCD。60Hz 刷新率通过定制 FPGA 控制器实现，但由于电泳介质切换增加，可能影响面板寿命。

hackernews · Vinnl · Jun 18, 11:41 · [社区讨论](https://news.ycombinator.com/item?id=48583897)

**背景**: 电子纸显示器（如 E Ink 的产品）利用电泳技术像纸一样反射光线，仅在图像变化时消耗电力。传统电子纸刷新率低（通常低于 10Hz）且色彩有限，适合电子阅读器但不适合动态内容。Modos 旨在通过高刷新率彩色电子纸显示器克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/modos-e-paper-monitor">Modos Color Monitor Pushes E-Paper Displays Further - IEEE Spectrum</a></li>
<li><a href="https://www.cnx-software.com/2026/05/27/modos-flow-an-fpga-based-13-3-inch-usb-c-touchscreen-color-e-paper-monitor/">Modos Flow - An FPGA-based 13.3-inch USB-C touchscreen e-paper monitor (Crowdfunding) - CNX Software</a></li>
<li><a href="https://www.modos.tech/blog/modos-paper-monitor">The Modos Paper Monitor | Modos</a></li>

</ul>
</details>

**社区讨论**: 社区对 Modos Flow 的规格感到兴奋，许多人认为这是电子纸显示器的突破。一些评论者担心高刷新率下面板的寿命，而其他人则讨论潜在用例，如户外平板和低功耗辅助显示器。

**标签**: `#e-paper`, `#display technology`, `#hardware`, `#startup`

---

<a id="item-8"></a>
## [多款婴儿纸尿裤检出生殖毒性物质甲酰胺](https://www.sohu.com/a/1038121771_122014422) ⭐️ 8.0/10

《经济参考报》委托专业机构检测发现，好奇、碧芭宝贝、Babycare 等多个品牌的婴幼儿纸尿裤中检出生殖毒性物质甲酰胺。部分婴幼儿的血液和尿液中也被检出该物质，一名记者穿戴某款纸尿裤一夜后血液浓度飙升近一倍。 此事意义重大，因为甲酰胺被列为生殖毒性物质，可通过皮肤吸收，对器官尚未发育完全的婴幼儿构成严重健康风险。目前纸尿裤国家标准未将甲酰胺纳入检测，暴露出亟需修订的监管空白。 甲酰胺常用于纸尿裤生产中的胶黏剂和柔软剂。欧盟将其列为 1B 类生殖毒性物质，中国化妆品目录中已禁用。专家指出，长期蓄积可能损害生殖系统、肝脏和肾脏。

telegram · zaihuapd · Jun 18, 07:09

**背景**: 甲酰胺是一种无色液体，有轻微氨味，用作溶剂和制造助剂。动物实验表明其具有生殖和发育毒性。在中国，纸尿裤受国家标准监管，但标准主要关注物理性能和微生物安全，未涵盖甲酰胺等化学危害。此次事件引发公众担忧，呼吁更新标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1038359743_539932">“好奇”、“碧芭宝贝”、“Babycare”多款知名婴儿纸尿裤检测出甲酰胺生殖...</a></li>
<li><a href="https://www.163.com/dy/article/KVNFKETB0511T7D3.html">国标不检就不管？好奇、babycare等品牌陷入“毒纸尿裤”风波|宝宝|甲醛|...</a></li>
<li><a href="https://www.thepaper.cn/newsDetail_forward_33412554">纸尿裤“甲酰胺”风波：品牌自证“未检出”，国标无检测要求_澎湃号·媒体_...</a></li>

</ul>
</details>

**标签**: `#public health`, `#consumer safety`, `#regulatory gap`, `#toxicology`, `#infant products`

---

<a id="item-9"></a>
## [苹果与英特尔达成初步芯片代工协议](https://t.me/zaihuapd/42031) ⭐️ 8.0/10

苹果与英特尔在经过一年多谈判后，已签署初步协议，由英特尔代工生产部分苹果设备所需的芯片。该协议于近几个月敲定，但具体涉及 iPhone、iPad 还是 Mac 产品尚未披露。 该协议标志着苹果芯片供应链的重大转变，减少对台积电的依赖并加强美国本土半导体制造。同时，它提振了英特尔曾因延迟和良率问题而挣扎的代工业务，并符合美国政府推动芯片制造回流的政策方向。 该协议受到美国政府大力推动，商务部长多次游说苹果 CEO 蒂姆·库克。英特尔目前已与英伟达、SpaceX 和苹果三家建立代工合作关系，但该协议是初步的，尚未成为最终商业合同。

telegram · zaihuapd · Jun 18, 09:19

**背景**: 英特尔曾是全球最大芯片制造商，但其代工业务面临良率低和延迟等挑战。苹果长期依赖台积电生产芯片，但美国政府施压减少对亚洲供应商的依赖推动了这一潜在转变。CHIPS 法案和地缘政治紧张局势加速了将半导体制造带回美国的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel">Intel - Wikipedia</a></li>
<li><a href="https://www.gadgetreview.com/trump-claims-apple-intel-chip-deal-neither-company-confirms">Trump Claims Apple - Intel Chip Deal - Neither... - Gadget Review</a></li>
<li><a href="https://colitco.com/amd-vs-intel-stock-apple-chip-deal-ai-chips-0905202615/">One Analyst Has Picked a Clear Winner in the AMD vs Intel ... - Colitco</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Intel`, `#semiconductor`, `#chip manufacturing`, `#supply chain`

---