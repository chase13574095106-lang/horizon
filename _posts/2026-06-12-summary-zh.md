---
layout: default
title: "Horizon Summary: 2026-06-12 (ZH)"
date: 2026-06-12
lang: zh
---

> From 28 items, 8 important content pieces were selected

---

1. [CRISPR Cas12a2 选择性摧毁癌细胞](#item-1) ⭐️ 9.0/10
2. [英伟达发布 Vera Rubin 平台，预计销售额达 1 万亿美元](#item-2) ⭐️ 9.0/10
3. [对“直接上传到 ChatGPT”心态的批判](#item-3) ⭐️ 8.0/10
4. [WASI 0.3 发布，转向组件模型](#item-4) ⭐️ 8.0/10
5. [预印本指控华为盘古抄袭通义千问权重，新检测方法问世](#item-5) ⭐️ 8.0/10
6. [Kimi 开源编码模型 K2.7-Code，多项基准测试大幅提升](#item-6) ⭐️ 8.0/10
7. [Cloudflare 全球故障导致间歇性中断](#item-7) ⭐️ 8.0/10
8. [长鑫科技科创板 IPO 过会，拟募资 295 亿元](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [CRISPR Cas12a2 选择性摧毁癌细胞](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/) ⭐️ 9.0/10

由 Jennifer Doudna 领导的研究人员开发了一种新型 CRISPR-Cas12a2 方法，该方法在检测到肿瘤特异性突变后，选择性地摧毁癌细胞中的染色质，从而杀死癌细胞，同时保持健康细胞完好无损。该技术于 2026 年 6 月 8 日发表在《自然》杂志上。 该技术为先前“不可成药”的癌症提供了潜在治疗方法，因为它靶向的是突变而非蛋白质。通过使用 Cas12a2 更具破坏性的染色质摧毁机制，它代表了基于 CRISPR 的癌症疗法的重要进步。 与仅在目标位点切割 DNA 的 Cas9 不同，Cas12a2 在检测到特定 RNA 序列后被激活，进而摧毁细胞内的整个染色质。该系统是 RNA 触发的，即在 RNA 水平而非 DNA 水平识别突变。

hackernews · gmays · Jun 12, 15:15 · [社区讨论](https://news.ycombinator.com/item?id=48505231)

**背景**: CRISPR-Cas 系统是源自细菌免疫系统的基因编辑工具。Cas12a2 是一种 V 型 CRISPR 核酸酶，在结合目标 RNA 后，会非特异性地降解单链 DNA 和 RNA，导致染色质摧毁和细胞死亡。这与 Cas9 形成对比，后者在特定 DNA 位点产生双链断裂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10738-7">Targeting Cancer-Specific Mutations with RNA-Triggered ...</a></li>
<li><a href="https://cancer.ucsf.edu/news/2026/06/08/new-crispr-technique-selectively-shreds-cancer-cells-including-undruggable-cancers">New CRISPR Technique Selectively Shreds Cancer Cells ...</a></li>
<li><a href="https://healthcare.utah.edu/newsroom/news/2026/05/new-kind-of-crispr-could-treat-viral-infection-and-cancer-shredding-sick">New Kind of CRISPR Could Treat Viral Infection and Cancer by...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该方法的新颖性表示兴奋，一位用户指出之前的研究使用 Cas9，其破坏性不如 Cas12a2。然而，也有人担心潜在的肿瘤耐药性，以及 CRISPR 相对于获得更多 FDA 批准的病毒载体疗法被过度炒作的问题。

**标签**: `#CRISPR`, `#cancer research`, `#gene editing`, `#biotechnology`, `#Cas12a2`

---

<a id="item-2"></a>
## [英伟达发布 Vera Rubin 平台，预计销售额达 1 万亿美元](https://t.me/zaihuapd/41917) ⭐️ 9.0/10

在 GTC 大会上，英伟达发布了 Vera Rubin 平台，包含全新的 Vera CPU 和 Rubin GPU，并集成了 Groq 3 LPU，面向智能体 AI 基础设施。CEO 黄仁勋预计，Blackwell 与 Rubin 系列截至 2027 年的销售额至少达到 1 万亿美元。 这一公告标志着英伟达在 AI 硬件市场占据主导地位的激进路线图，其巨额营收预测凸显了 AI 基础设施的爆炸性增长。Vera Rubin 平台的性能宣称可能为 AI 训练和推理树立新标杆。 Vera CPU 据称比传统机架级 CPU 效率提升 2 倍、速度提升 50%，相关产品将于今年下半年由合作伙伴提供。Groq 3 LPU 提供 1.2 petaFLOPS 的 8 位计算能力和 150 tokens/watt 的推理效率，推理效率提升 35 倍。

telegram · zaihuapd · Jun 12, 10:17

**背景**: 英伟达此前发布的 Blackwell 架构是当前 AI 工作负载的旗舰产品，性能较上一代提升 30 倍。Vera Rubin 平台是英伟达的下一代 AI 和 HPC 平台，专为处理智能体 AI 的多步推理和长上下文工作流而设计。Groq 3 LPU 是一种专为推理优化的语言处理单元，与 GPU 互补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">NVIDIA Vera Rubin Platform</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidias-vera-rubin-platform-in-depth-inside-nvidias-most-complex-ai-and-hpc-platform-to-date">Nvidia's Vera Rubin platform in depth — Inside Nvidia's most ...</a></li>
<li><a href="https://www.cnbc.com/2026/02/25/first-look-at-nvidias-ai-system-vera-rubin-and-how-it-beats-blackwell.html">First look at Nvidia’s AI system Vera Rubin and how it beats ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI hardware`, `#GPU`, `#Vera Rubin`, `#GTC`

---

<a id="item-3"></a>
## [对“直接上传到 ChatGPT”心态的批判](https://correresmidestino.com/dont-you-just-upload-it-to-chatgpt/) ⭐️ 8.0/10

一篇论文指出，虽然像 ChatGPT 这样的 AI 对非专家来说是一大福音，但它无法取代深厚的人类专业知识，并以翻译为例说明 AI 无法匹敌细腻的人类技能。 这一批判挑战了在专业领域过度依赖 AI 的趋势，强调了质量下降和人类专业知识被低估的风险，影响了翻译和写作等专业人士。 论文以翻译为核心例子，指出 AI 翻译往往缺乏文化细微差别和风格上的精妙之处，而非专家难以察觉这些缺陷。

hackernews · speckx · Jun 12, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=48507278)

**背景**: 像 ChatGPT 这样的大型语言模型（LLM）已被广泛用于翻译、写作和编程等任务。虽然它们能为普通用户产生令人印象深刻的结果，但特定领域的专家常常发现其输出缺乏深度和准确性。这篇论文为关于 AI 在专业工作中适当角色的持续辩论做出了贡献。

**社区讨论**: 评论者大多赞同论文的观点，分享了关于 AI 翻译失败以及人类专业知识不可替代价值的个人轶事。一些人争论 AI 是否最终会将翻译工作简化为审计，而另一些人则强调 AI 对非专家的好处是真实但有限的。

**标签**: `#AI`, `#LLM`, `#translation`, `#expertise`, `#technology criticism`

---

<a id="item-4"></a>
## [WASI 0.3 发布，转向组件模型](https://bytecodealliance.org/articles/WASI-0.3) ⭐️ 8.0/10

Bytecode Alliance 发布了 WASI 0.3，这是 WebAssembly 系统接口的新版本，与 WASI 0.2 相比有重大变化，包括向组件模型的转变。 WASI 0.3 标志着 WebAssembly 在浏览器之外演进的重要一步，旨在为跨平台应用提供安全、可移植的接口。组件模型方向可能带来更好的互操作性和模块化，但也引发了社区内的争论。 WASI 0.3 包含发布说明中详述的接口级更改，以及带有示例的公告文章。该版本基于组件模型，该模型为组件而非传统的类 Unix 系统调用定义 API。

hackernews · mavdol04 · Jun 12, 13:51 · [社区讨论](https://news.ycombinator.com/item?id=48504063)

**背景**: WebAssembly (Wasm) 是一种可移植的二进制指令格式，旨在浏览器和其他环境中实现高性能执行。WASI (WebAssembly 系统接口) 为 Wasm 程序提供了一套标准化的 API 来与操作系统交互，最初以 POSIX 为模型。组件模型是一种较新的方法，它定义了软件组件之间的接口，旨在提高模块化和安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/WebAssembly/WASI">GitHub - WebAssembly/WASI: WebAssembly System Interface</a></li>
<li><a href="https://component-model.bytecodealliance.org/">Introduction - The WebAssembly Component Model</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户对开发进度缓慢和缺乏可见性表示沮丧，而另一些人则批评组件模型是不必要的复杂化。不过，也有用户对此次发布及其潜力表示赞赏，一些人指出独立 Wasm 与自定义集成可能是更实用的路径。

**标签**: `#WebAssembly`, `#WASI`, `#systems programming`, `#bytecode alliance`

---

<a id="item-5"></a>
## [预印本指控华为盘古抄袭通义千问权重，新检测方法问世](https://t.me/zaihuapd/41915) ⭐️ 8.0/10

清华大学张锐翀在预印本论文中提出了一种名为“矩阵驱动即时审查”（MDIR）的新方法，用于检测大型语言模型间的权重抄袭，并提供了极低 p 值的统计证据，表明华为盘古模型可能抄袭了阿里通义千问的权重。 此事意义重大，因为它对华为盘古这一重要中文 AI 模型提出了严重的抄袭指控，并引入了一种新的检测技术，有助于确保 AI 行业的模型完整性和公平竞争。 MDIR 方法利用矩阵分析和大偏差理论对模型嵌入和多层权重进行对齐比对，计算严格的 p 值，并可在单台个人电脑上一小时内完成分析。该方法声称即使在增量预训练、剪枝或置换后也能准确识别权重来源，同时避免假阳性。

telegram · zaihuapd · Jun 12, 08:07

**背景**: 大型语言模型（如华为盘古和阿里通义千问）依赖海量数据训练，其性能很大程度上取决于学习到的权重。权重抄袭是指一个模型的权重未经适当归属地从另一个模型复制而来，这违反了开源许可和伦理规范。MDIR 方法旨在提供一种可靠的检测手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.xugj520.cn/archives/mdir-tech-llm-plagiarism-detection.html">破解AI模型抄袭黑幕！ MDIR 技术如何精准揪出LLM剽窃者？ | 高效码农</a></li>
<li><a href="https://news.qq.com/rain/a/20250709A01WPA00">盘古大模型与通义千问，谁抄袭了谁_腾讯新闻</a></li>
<li><a href="https://www.gamersky.com/tech/202507/1956337.shtml">被指抄袭阿里通义千问 华为盘古回应 _ 游民星空 GamerSky.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#plagiarism`, `#LLM`, `#model integrity`, `#research`

---

<a id="item-6"></a>
## [Kimi 开源编码模型 K2.7-Code，多项基准测试大幅提升](https://mp.weixin.qq.com/s/NBw1VAA9MjpKv-Rirq9qDg) ⭐️ 8.0/10

月之暗面（Kimi）发布并开源了 Kimi K2.7-Code 编码模型，相比 K2.6 在多项基准测试中取得显著提升，包括 Kimi Code Bench v2 提升 21.8%、Program-Bench 提升 11%、MLS Bench Lite 提升 31.5%，同时平均 token 消耗减少 30%。 此次发布推动了开源编码模型的发展，缩小了与 GPT-5.5 等专有前沿模型的差距，并为开发者提供了更高效、可本地部署的代码生成和自主执行任务选项。 该模型采用混合专家（MoE）架构，总参数量达 1 万亿，支持 256K 上下文窗口，可通过 Kimi API、Kimi Code 使用，也支持本地部署，六倍高速模式即将上线。

telegram · zaihuapd · Jun 12, 10:55

**背景**: Kimi K2.7-Code 是一个专为编码任务设计的大型语言模型，基于 MoE 架构，每次推理仅激活部分参数以提高效率。它旨在长上下文中遵循指令，并执行复杂的编码和自主执行任务，例如自主代码执行和工具使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K2.7-Code">moonshotai/ Kimi -K2.7- Code · Hugging Face</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart">Kimi K2.7 Code - Kimi API Platform</a></li>
<li><a href="https://www.aimadetools.com/blog/kimi-k2-7-code-complete-guide/">Kimi K2.7 Code Complete Guide: 1T Coding Agent That Beats Opus...</a></li>

</ul>
</details>

**标签**: `#AI`, `#开源`, `#编码模型`, `#Kimi`, `#基准测试`

---

<a id="item-7"></a>
## [Cloudflare 全球故障导致间歇性中断](https://t.me/zaihuapd/41922) ⭐️ 8.0/10

2025 年 11 月 18 日，Cloudflare 发生间歇性全球故障，其状态页面报告了多次恢复和再次中断的循环，公司确认了问题并开始实施修复，包括在伦敦禁用 WARP 访问。 作为关键的全球互联网基础设施提供商，Cloudflare 的故障影响了数百万网站和服务，凸显了集中式网络依赖的脆弱性以及健全的事件响应和补偿机制的重要性。 Cloudflare 正在按秒赔付企业用户。该事件在一小时内经历了多次恢复和再次中断的循环，状态页面更新显示作为缓解措施的一部分，在伦敦禁用了 WARP 访问。

telegram · zaihuapd · Jun 12, 14:31

**背景**: Cloudflare 是一家主要的内容分发网络（CDN）和互联网安全公司，为数百万网站提供 DDoS 防护、DNS 解析和反向代理等服务。WARP 是 Cloudflare 提供的类似 VPN 的服务，旨在提高互联网速度和隐私保护。Cloudflare Access 是一种零信任网络访问（ZTNA）解决方案，用于控制对应用程序的访问。按秒赔付是一种罕见且慷慨的 SLA 政策，针对企业客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cloudflare_WARP">Cloudflare WARP</a></li>
<li><a href="https://www.cloudflare.com/sase/products/access/">Access | Zero Trust Network Access (ZTNA) solution | Cloudflare</a></li>
<li><a href="https://scandiweb.com/blog/ddos-attack-case-blocking-10k-requests/">DDoS Attack Case: Blocking 10,000 Requests per Second - Scandiweb</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#outage`, `#internet infrastructure`, `#reliability`, `#incident`

---

<a id="item-8"></a>
## [长鑫科技科创板 IPO 过会，拟募资 295 亿元](https://t.me/zaihuapd/41923) ⭐️ 8.0/10

长鑫科技在上海证券交易所科创板的 IPO 获得上市委会议通过，拟募资 295 亿元，用于 DRAM 制造升级和研发。 这标志着中国国产 DRAM 产业的一个重要里程碑，长鑫科技是国内领先的 DRAM 制造商。大规模融资将加速技术升级，并可能重塑全球存储芯片供应链。 资金将用于存储器晶圆制造量产线技术升级、DRAM 技术升级和前瞻技术研发。长鑫科技近期实现季度盈利，并正在开发 15nm DRAM 技术，计划明年量产。

telegram · zaihuapd · Jun 12, 15:06

**背景**: 长鑫科技成立于 2016 年，总部位于安徽合肥，是中国最大的 DRAM 芯片制造商。它于 2019 年实现首款 8Gb DDR4 芯片量产，填补了中国半导体产业的空白。科创板是中国面向科技公司的纳斯达克式板块，IPO 过会是上市前的关键一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://view.inews.qq.com/a/20260523A0413800">中国 Dram 决战时刻：长鑫科技上市，只是开始_腾讯新闻</a></li>
<li><a href="https://www.sohu.com/a/1024662261_313170">长鑫科技——国产DRAM弯道超车，一场万亿产业的突围战</a></li>
<li><a href="https://www.eet-china.com/mp/a381597.html">长鑫存储正开发15nmDRAM，明年量产-电子工程专辑</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#DRAM`, `#IPO`, `#China`, `#memory`

---