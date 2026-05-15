---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 32 items, 8 important content pieces were selected

---

1. [Project Zero 披露 Pixel 10 零点击漏洞利用链](#item-1) ⭐️ 9.0/10
2. [AI 协助 5 天内完成首个公开 Apple M5 内核利用](#item-2) ⭐️ 9.0/10
3. [vLLM v0.21.0：重大变更、KV 卸载与推测解码](#item-3) ⭐️ 8.0/10
4. [AI 精神病：公司将思考外包给 AI](#item-4) ⭐️ 8.0/10
5. [美国司法部要求苹果和谷歌披露 10 万应用用户信息](#item-5) ⭐️ 8.0/10
6. [OCaml 在太空中的栈注解应用](#item-6) ⭐️ 8.0/10
7. [arXiv 对未核查的 LLM 内容作者禁投一年](#item-7) ⭐️ 8.0/10
8. [特朗普与习近平讨论 AI 护栏及英伟达 H200 芯片](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Project Zero 披露 Pixel 10 零点击漏洞利用链](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero 披露了针对 Pixel 10 的零点击漏洞利用链，攻击者无需任何用户交互即可获得 root 权限，该漏洞利用了 AI 驱动的消息分析功能中的缺陷。 该漏洞利用链凸显了移动设备中的 AI 功能如何扩大攻击面，使零点击攻击更加可行，并强调了整个 Android 生态系统及时打补丁的重要性。 该漏洞利用链仅需两个软件缺陷即可在零点击上下文中获得内核权限，且供应商在 90 天内修补了漏洞，这对于 Android 驱动程序漏洞来说非常迅速。

hackernews · happyhardcore · May 15, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48148460)

**背景**: 零点击漏洞利用允许攻击者在无需用户任何操作（如打开消息或点击链接）的情况下入侵设备。AI 驱动的消息分析会在用户打开消息前解码媒体，从而增加了此类漏洞利用的攻击面。Project Zero 是 Google 的安全研究团队，负责发现并披露漏洞以提升平台安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/01/pixel-0-click-part-3.html">A 0 - click exploit chain for the Pixel 9 Part 3: Where do... - Project Zero</a></li>
<li><a href="https://oxo.is/blog/2026/05/13/news-2026-05-13-a-0-click-exploit-chain-for-the-pixel-10-when-a-door-closes/">A 0 - click exploit chain for the Pixel 10: When a Door Closes...</a></li>
<li><a href="https://projectzero.google/2020/01/policy-and-disclosure-2020-edition.html">Policy and Disclosure : 2020 Edition - Project Zero</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 功能增加攻击面表示担忧，有人指出未经用户同意读取短信是一个反复出现的问题。另一个人称赞 Google 的补丁速度很快，但对 Android 其他部分感到担忧。一些人争论 AI 是否加速了漏洞发现，还是仅仅增加了媒体关注度。

**标签**: `#security`, `#exploit`, `#Android`, `#Pixel`, `#Project Zero`

---

<a id="item-2"></a>
## [AI 协助 5 天内完成首个公开 Apple M5 内核利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

安全研究员 Calif 与 Anthropic 的 Mythos Preview AI 系统合作，在 5 天内完成了首个公开的 Apple M5 macOS 内核内存破坏利用，绕过了 Apple 的 MIE 硬件内存保护。 这表明即使 Apple 最先进的硬件内存保护（MIE）也能通过专家技能与尖端 AI 的结合被攻破，对硬件级安全措施的长期有效性提出了严峻质疑。 该利用链针对 M5 硬件上的 macOS 26.4.1，使用两个漏洞和多项技术，仅通过正常系统调用即可从非特权用户提权至 root shell。完整的 55 页技术报告将在 Apple 修复后发布。

telegram · zaihuapd · May 15, 02:15

**背景**: Apple 的 Memory Integrity Enforcement（MIE）是 2025 年引入的硬件级内存安全保护，旨在防止针对内核的内存破坏攻击。它代表了五年的工程努力，被认为是业界首个始终开启的保护。内核内存破坏利用是操作系统中常见的提权手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory safety in Apple devices - Apple Security Research</a></li>
<li><a href="https://9to5mac.com/2026/05/14/calif-team-details-how-anthropic-mythos-helped-build-a-working-macos-exploit-in-five-days/">Anthropic Mythos helped Calif build a macOS exploit in five... - 9to5Mac</a></li>

</ul>
</details>

**标签**: `#Apple M5`, `#kernel exploit`, `#macOS security`, `#AI-assisted hacking`, `#MIE bypass`

---

<a id="item-3"></a>
## [vLLM v0.21.0：重大变更、KV 卸载与推测解码](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 弃用了 transformers v4，要求 C++20，将 KV 卸载与混合内存分配器 (HMA) 集成，增加了对推理模型的推测解码支持，并为 Blackwell GPU 引入了 TOKENSPEED_MLA 后端。 此版本强制要求迁移到 transformers v5 和 C++20 编译器，对生产级 LLM 推理系统产生重大影响，同时通过 KV 卸载和推理模型的推测解码提高了内存效率和推理速度。 带 HMA 的 KV 卸载包括调度器端滑动窗口组和完整的 HMA 启用。推测解码现在遵循推理/思考预算，使得 DeepSeek-R1 等模型能够正确进行推测解码。TOKENSPEED_MLA 后端针对 Blackwell GPU 上的 DeepSeek-R1/Kimi-K25 预填充和解码。

github · khluu · May 15, 08:44

**背景**: vLLM 是一个高吞吐量、内存高效的大语言模型推理引擎。KV 缓存卸载将键值缓存数据从 GPU 移动到 CPU 内存，以减少 GPU 内存压力；推测解码则使用较小的草稿模型来加速生成。混合内存分配器 (HMA) 优化了混合注意力类型模型的内存分配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm-project/vllm</a></li>
<li><a href="https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html">Inside vLLM’s New KV Offloading Connector: Smarter Memory Transfer for Maximizing Inference Throughput | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/tokenspeed_mla/">tokenspeed _ mla - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#transformers`, `#GPU`, `#speculative decoding`

---

<a id="item-4"></a>
## [AI 精神病：公司将思考外包给 AI](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto 批评公司将决策和代码编写外包给 AI 而缺乏人工监督，警告这会导致系统不稳定和“AI 精神病”。 这凸显了 AI 采用中的一个关键风险：在没有人类判断的情况下过度依赖 AI 可能会创建脆弱、不可维护的系统，尤其是在软件工程和金融领域。 “AI 精神病”一词最初指个体因与 AI 互动而产生妄想，但此处被隐喻地用于描述组织盲目信任 AI 输出的现象。

hackernews · reasonableklout · May 15, 20:26 · [社区讨论](https://news.ycombinator.com/item?id=48153379)

**背景**: AI 精神病是一种现象，指与 AI 的互动会引发或加剧易感个体的妄想和偏执。在软件工程中，代码生成器等 AI 工具的使用日益增多，但若缺乏适当审查，它们可能会引入随时间累积的漏洞和安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chatbot_psychosis">Chatbot psychosis - Wikipedia</a></li>
<li><a href="https://www.news-medical.net/health/AI-Psychosis-How-Artificial-Intelligence-May-Trigger-Delusions-and-Paranoia.aspx">AI Psychosis : How Artificial Intelligence May Trigger Delusions and...</a></li>
<li><a href="https://www.groovyweb.co/blog/outsource-ai-development-risks-benefits-right-partner-2026">Outsource AI Development: Risks , Benefits & Partner Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者同意这一批评，指出纯 AI 编写的系统可能变得过于复杂，人类无法理解，从而导致不稳定。一些人认为使用 AI 作为工具没问题，但盲目信任其输出才是真正的问题。

**标签**: `#AI`, `#software engineering`, `#risk management`, `#AI adoption`

---

<a id="item-5"></a>
## [美国司法部要求苹果和谷歌披露 10 万应用用户信息](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

美国司法部已向苹果和谷歌发出传票，要求它们披露一款热门汽车改装应用的超过 10 万名用户信息，作为排放打击行动的一部分。 此案引发了重大的隐私和中心化担忧，因为它为政府通过应用商店进行监控开创了先例，并可能抑制合法的车辆改装和研究。 涉事应用用于修改车辆软件，包括禁用排放控制，这可能违反《清洁空气法》。司法部寻求用户身份以识别潜在证人，但批评者认为这是钓鱼执法。

hackernews · tencentshill · May 15, 17:28 · [社区讨论](https://news.ycombinator.com/item?id=48151383)

**背景**: 车辆软件改装一直是一个有争议的问题，DMCA 下的豁免允许为安全研究进行某些修改。然而，根据《清洁空气法》，禁用排放控制是非法的。苹果 App Store 和 Google Play 等应用商店的中心化特性使其成为政府传票的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/">U.S. DOJ demands Apple and Google unmask over 100,000 users of popular car-tinkering app in emissions crackdown</a></li>
<li><a href="https://www.bbc.com/news/technology-34656699">Smart car software tinkering legal - US ruling - BBC News</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：一些人批评政府的做法越界且侵犯隐私，而另一些人则认为禁用排放控制的用户理应受到审查。人们担心这会为未来的监控开创先例，并质疑中心化应用分发的作用。

**标签**: `#privacy`, `#government surveillance`, `#app stores`, `#legal`, `#automotive`

---

<a id="item-6"></a>
## [OCaml 在太空中的栈注解应用](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

一个名为 OxCaml 的项目在 OCaml 中使用栈注解来消除 GC 压力，在太空应用的包分发中实现了低于 10 纳秒的 p99.9 延迟。 这表明通过使用类型注解将分配移至栈，垃圾收集语言也能实现适用于太空和高频交易的超低延迟。 切换到带有 exclave 栈注解的 OxCaml 后，每包 p99.9 延迟从 29 纳秒降至 9 纳秒，在 2500 万个包中，次要 GC 次数从 394 次降为零。

hackernews · yminsky · May 15, 10:55 · [社区讨论](https://news.ycombinator.com/item?id=48147058)

**背景**: OCaml 是一种常用于系统编程的垃圾收集语言。栈注解允许开发者显式地在栈上而非堆上分配数据，从而减少 GC 压力并提高延迟可预测性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oxcaml.org/documentation/stack-allocation/intro/">OxCaml | Stack allocation | Intro</a></li>
<li><a href="https://ocamlpro.com/blog/2020_03_23_in_depth_look_at_best_fit_gc/">An in-depth Look at OCaml’s new “Best-fit” Garbage Collector Strategy | OCamlPro</a></li>
<li><a href="https://dev.realworldocaml.org/garbage-collector.html">Understanding the Garbage Collector - Real World OCaml</a></li>

</ul>
</details>

**社区讨论**: 评论者提到 OCaml 在太空中的先前应用（例如 2016 年的 GHGSat-D），并讨论了为低延迟场景改造 GC 语言的难度。有人质疑重新发明 CCSDS 等协议的安全性。

**标签**: `#OCaml`, `#garbage collection`, `#space software`, `#low-latency`, `#systems programming`

---

<a id="item-7"></a>
## [arXiv 对未核查的 LLM 内容作者禁投一年](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 宣布，对提交含有未核查 LLM 生成内容（如幻觉引用、遗留的元注释或占位数据）的论文作者，实施为期一年的禁投处罚。 该政策为 AI 研究领域的学术诚信树立了明确先例，要求作者对所有内容负责（无论生成方式），并旨在遏制学术出版物中日益严重的 LLM 幻觉问题。 禁投期结束后，作者后续投稿必须先被可信的同行评审会议或期刊接收，才能再次提交到 arXiv。该政策特别针对幻觉引用、LLM 生成的元注释以及“请替换为真实实验数据”等占位数据。

telegram · zaihuapd · May 15, 04:30

**背景**: arXiv 是一个广泛使用的科学论文预印本仓库，尤其在物理、数学和计算机科学领域。像 GPT-4 这样的 LLM 可能生成看似合理但实际错误的引用（即幻觉），这已成为学术出版中日益严重的问题。arXiv 的行为准则规定，作者署名即代表对论文全部内容负责，不论内容由何种方式生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.07723">LLM hallucinations in the wild</a></li>
<li><a href="https://www.factors.ai/blog/llm-hallucination-detection-examples">LLM Hallucination Examples: What They Are and How to Detect Them</a></li>

</ul>
</details>

**社区讨论**: Telegram 频道的讨论验证了该政策的重要性，社区成员对 arXiv 针对未核查 LLM 内容的明确立场表示支持，但也有人指出执行和检测方面存在挑战。

**标签**: `#arXiv`, `#LLM`, `#academic integrity`, `#AI policy`, `#publishing`

---

<a id="item-8"></a>
## [特朗普与习近平讨论 AI 护栏及英伟达 H200 芯片](https://www.bloomberg.com/news/articles/2026-05-15/trump-says-he-discussed-ai-guardrails-nvidia-s-chips-with-xi) ⭐️ 8.0/10

特朗普总统透露，他在访华期间与习近平主席讨论了 AI 护栏及英伟达 H200 芯片出口问题，并指出中国选择不购买 H200，转而自主研发芯片。 此次高层讨论凸显了美中在 AI 芯片出口管制上的持续紧张关系，直接影响全球 AI 供应链及两国的技术主权。 美国已允许英伟达向中国供应 H200 芯片，但北京尚未批准任何采购，目前无一交付。此前中国也曾拒绝进口性能较低的 H20 芯片。

telegram · zaihuapd · May 15, 15:13

**背景**: AI 护栏是指确保 AI 系统在可接受范围内运行的安全机制。H200 是英伟达先进的 AI 芯片，受美国出口管制。中国推动自主研发芯片旨在减少对外国技术的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/AI_guardrails">AI guardrails</a></li>
<li><a href="https://grokipedia.com/page/2026_Chinese_restrictions_on_Nvidia_H200_chips">2026 Chinese restrictions on Nvidia H200 chips</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#US-China trade`, `#export controls`, `#geopolitics`

---