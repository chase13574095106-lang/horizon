---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> From 27 items, 8 important content pieces were selected

---

1. [Kimi 发布 2.8 万亿参数 K3 模型，支持 1M 上下文](#item-1) ⭐️ 9.0/10
2. [华为昇腾 950 超节点亮相，算力达英伟达 6.7 倍](#item-2) ⭐️ 9.0/10
3. [首次在宜居带岩石系外行星上发现大气层](#item-3) ⭐️ 8.0/10
4. [Firefox 通过 WebAssembly 在另一个浏览器中运行](#item-4) ⭐️ 8.0/10
5. [Truth Social 将向华尔街出售特朗普帖子的实时访问权限](#item-5) ⭐️ 8.0/10
6. [特朗普政府拟大幅缩短签证有效期](#item-6) ⭐️ 8.0/10
7. [美议员要求封禁中国存储芯片并阻止其进入盟友供应链](#item-7) ⭐️ 8.0/10
8. [OpenAI CFO 提出“每美元有用智能”作为 AI 投资回报率指标](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi 发布 2.8 万亿参数 K3 模型，支持 1M 上下文](https://t.me/zaihuapd/42619) ⭐️ 9.0/10

Kimi 发布了 K3 模型，这是一个 2.8 万亿参数的开源模型，支持 1M token 上下文窗口，声称综合性能仅次于 Claude Fable 5 和 GPT-5.6 Sol。该模型采用 Kimi Delta Attention 和 Attention Residuals 架构，结合稀疏 MoE 设计，在 896 个专家中激活 16 个。 这是全球首个 3 万亿参数级别的开源模型，可能使前沿 AI 能力更加普及。其新颖的注意力架构可能影响整个行业未来的模型设计。 K3 相比前代 K2 的扩展效率提升约 2.5 倍。该模型原生支持视觉理解，完整权重将在未来几天内开放。

telegram · zaihuapd · Jul 17, 00:02

**背景**: Kimi Delta Attention 是一种混合线性注意力机制，扩展了 Gated DeltaNet，具有更细粒度的门控，在各种场景下优于全注意力。Attention Residuals 允许每一层有选择地从之前层聚合信息，提升表示能力。稀疏 MoE 每个 token 只激活部分专家，从而在可控计算成本下实现大参数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-Linear">GitHub - MoonshotAI/Kimi-Linear</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**社区讨论**: 评论讨论了“Pelican 基准测试”（生成骑自行车的鹈鹕的 SVG）作为模型质量测试，有人指出 Kimi K3 的分词器异常，暗示存在隐藏的系统提示。一位用户比较了定价和速度，发现 Kimi 便宜 5 倍但慢 2 倍。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Kimi`, `#Mixture of Experts`

---

<a id="item-2"></a>
## [华为昇腾 950 超节点亮相，算力达英伟达 6.7 倍](https://www.ithome.com/0/978/019.htm) ⭐️ 9.0/10

在 2026 年世界人工智能大会上，华为首次公开展示了昇腾 950 超节点（Atlas 950 SuperPoD），声称其通过 1024 张昇腾 NPU 提供 1 EFLOPS FP8 和 2 EFLOPS FP4 算力，总算力达到英伟达 NVL144 系统的 6.7 倍。 这标志着 AI 硬件的重大里程碑，可能重塑华为与英伟达在高性能 AI 计算领域的竞争格局，尤其是在中国获取先进芯片受到地缘政治限制的背景下。 该超节点采用华为自研的灵衢互联协议和超节点架构，实现 1024 卡规模及 256 TB 全局统一内存。此外，昇腾 384 超节点已在互联网、运营商、金融等行业商用落地超过 750 套。

telegram · zaihuapd · Jul 17, 10:27

**背景**: 超节点是一种高性能计算架构，通过高速互联将多个加速器（GPU/NPU）整合为单一逻辑机器，克服传统 PCIe 瓶颈。华为的灵衢协议是五层统一互联协议，旨在替代 PCIe、NVLink 和 RDMA，支持多达 8192 卡无收敛全互联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.toutiao.com/article/7551352889764020755/">华为全联接大会 2025：发布灵衢互联协议与多系列超节点产品，引领 AI ...</a></li>
<li><a href="https://locsic.com/zh/thinking/lingqu-unifiedbus-protocol-analysis/">灵衢协议深度分析：中国算力突围的互联赌注 — Locsic</a></li>
<li><a href="https://lucaberton.com/blog/huawei-atlas-950-superpod-ai-infrastructure/">Huawei Atlas 950 AI SuperPoD : 8,192 NPUs as One Machine</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AI hardware`, `#Ascend 950`, `#supercomputing`, `#Nvidia competition`

---

<a id="item-3"></a>
## [首次在宜居带岩石系外行星上发现大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

天文学家在距离地球 48 光年的红矮星宜居带内的岩石系外行星 LHS 1140b 上探测到氦气逸出，这是首次在类似地球的宜居带行星上确认存在大气层。 这一发现挑战了红矮星周围的岩石行星因强烈恒星辐射而无法保持大气层的假设，并为 JWST 等未来望远镜寻找生物特征提供了首要目标。 该探测使用麦哲伦克莱望远镜完成，JWST 发射光谱排除了迷你海王星的解释，确认 LHS 1140b 是岩石行星。该行星被潮汐锁定，可能拥有富含氦气的大气层。

hackernews · neversaydie · Jul 17, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: 红矮星比太阳更冷更小，其宜居带非常靠近恒星，使行星暴露在强烈的恒星耀斑和辐射下。此前，人们不确定在这种恶劣环境中岩石行星能否保持大气层。LHS 1140b 是“岩石世界主任自由支配时间计划”选定的目标之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ufl.edu/2026/07/exoplanet/">New study reveals potential atmosphere on rocky planet of nearby star</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-02200-5">Found: a rocky exoplanet with an atmosphere — could it host life?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Habitability_of_red_dwarf_systems">Habitability of red dwarf systems - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对红矮星周围的岩石行星能保持大气层表示惊讶，其中一人指出 JWST 数据排除了迷你海王星的可能性。其他人讨论了未来前往该行星的推进系统，以及用太阳透镜望远镜研究此类世界的潜力。

**标签**: `#exoplanets`, `#astronomy`, `#atmosphere`, `#JWST`, `#habitable zone`

---

<a id="item-4"></a>
## [Firefox 通过 WebAssembly 在另一个浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 8.0/10

Puter 已将完整的 Firefox 浏览器（Gecko 引擎）编译为 WebAssembly，使其能够在另一个浏览器标签页中运行，并显示真实的 Firefox 界面。该项目使用 Claude Opus 和 Fable 模型进行 AI 辅助代码翻译，估计消耗了价值 25,000 美元的令牌。 这展示了浏览器隔离和可移植性的新高度，可能实现整个浏览器在另一个浏览器中的安全沙箱运行。同时，它展示了 AI 在大规模代码翻译中的实际应用，显著降低了此类工程壮举所需的工作量。 该演示使用基于 WebSocket 的 Wisp 协议，通过 Puter 的服务器代理所有网络流量，因为浏览器中的 WebAssembly 无法打开任意网络连接。该项目声称支持端到端加密，检查确认 HTTPS 流量保持加密，而 HTTP 流量为明文。

rss · Simon Willison · Jul 16, 23:34

**背景**: WebAssembly（Wasm）是一种低级二进制指令格式，可在现代浏览器中以接近原生速度运行。将 Firefox 这样的完整浏览器编译为 Wasm 极具挑战性，因为浏览器是复杂的多进程应用；Firefox 因其强大的单进程支持而被选中。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP/UDP 套接字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.puter.com/labs/firefox-wasm/">Firefox in WebAssembly - developer.puter.com</a></li>
<li><a href="https://github.com/HeyPuter/firefox-wasm">HeyPuter/firefox-wasm: Firefox in WebAssembly - GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#Firefox`, `#Browser`, `#AI-assisted development`, `#WebSocket`

---

<a id="item-5"></a>
## [Truth Social 将向华尔街出售特朗普帖子的实时访问权限](https://www.cnn.com/2026/07/16/business/truth-social-data-wall-street) ⭐️ 8.0/10

特朗普媒体科技集团宣布推出 Truth API，这是一个付费数据接口，从 2026 年 8 月 1 日起以毫秒级速度提供 Truth Social 上排名前 10 账号的帖子，目标客户为高频交易公司。 此举直接将特朗普的社交媒体帖子货币化用于算法交易，引发了关于总统利益冲突和潜在市场操纵的严重伦理担忧，因为特朗普的帖子历来会引发市场波动。 该 API 将实时提供排名前 10 账号的帖子，定价未公开。CNN 此前报道称，特朗普曾利用 Truth Social 宣传自己刚买入股票的公司。

telegram · zaihuapd · Jul 17, 01:02

**背景**: 高频交易（HFT）利用算法在毫秒级时间内执行交易，通常依赖速度优势。Truth Social 已成为特朗普宣布政策的主要渠道，其关于关税和地缘政治事件的帖子曾引发市场大幅波动。向华尔街出售此类数据模糊了总统职责与私人商业利益之间的界限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hindustantimes.com/world-news/us-news/trump-media-launches-truth-api-to-give-banks-faster-access-to-truth-social-posts-101784225959242.html">Trump Media launches Truth API to give banks... | Hindustan Times</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/20982511912">高频交易（HFT）：算法交易的闪电世界 - 知乎</a></li>

</ul>
</details>

**标签**: `#API`, `#algorithmic trading`, `#social media`, `#ethics`, `#financial markets`

---

<a id="item-6"></a>
## [特朗普政府拟大幅缩短签证有效期](https://t.me/zaihuapd/42623) ⭐️ 8.0/10

特朗普政府周三公布拟议法规，计划大幅缩短学生、交流访问者和媒体签证的最长有效期，其中中国记者签证仅限 90 天。 这项政策可能严重影响 STEM 领域（包括人工智能和软件工程）的国际学生和研究人员，他们依赖较长的签证有效期进行学习和工作。同时，对外国记者（尤其是中国记者）施加严格的时间限制，也威胁到新闻自由。 根据拟议规则，学生和交流访问者签证最长不超过四年；记者签证对大多数国家限制为 240 天，中国公民仅为 90 天。签证持有者可申请延期，但需反复提交额外申请。

telegram · zaihuapd · Jul 17, 04:41

**背景**: 美国目前约有 160 万名持 F 类签证的国际学生，2024 财年共签发约 35.5 万份交流访问签证和 1.3 万份媒体签证。特朗普政府称此举是为了更好地监督签证持有者在美停留情况，是其更广泛打击合法移民行动的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.abcdreamusa.com/f2-visa-guide/">F 2 签 证 ：美国留学陪读 签 证 大指南 - ABC Dream USA</a></li>
<li><a href="https://www.btmusa.cn/J1Project.html">J-1 交 流 访 问 者 签 证 | 美国 访 问 学者申请 - 贝特曼集团</a></li>
<li><a href="https://m.iask.sina.com.cn/b/6cK3ycOx5n3.html">美国记者和媒体签证是什么？美国记者和媒体签 – 手机爱问</a></li>

</ul>
</details>

**标签**: `#US immigration policy`, `#visa regulations`, `#international students`, `#press freedom`, `#political impact`

---

<a id="item-7"></a>
## [美议员要求封禁中国存储芯片并阻止其进入盟友供应链](https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security) ⭐️ 8.0/10

美国众议院中国委员会主席 John Moolenaar 与议员 George Whitesides 致信商务部长 Howard Lutnick，要求将长鑫存储（CXMT）列入实体清单并对长江存储（YMTC）施加额外限制，称依赖中国存储芯片对美国国家安全构成不可接受的风险。 此举可能重塑全球半导体供应链，阻止中国存储芯片进入美国及盟友市场，可能影响苹果等公司以及依赖 DRAM 和 NAND 闪存的 AI 基础设施。 议员们还敦促与日本、韩国和欧盟协调，防止中国存储制造商在供应短缺时在盟友供应链中扎根，并称采购中国存储芯片可能资助解放军的军民两用技术发展。

telegram · zaihuapd · Jul 17, 14:00

**背景**: 长鑫存储（CXMT）是中国 DRAM 制造商，长江存储（YMTC）专注于 NAND 闪存。实体清单是美国商务部限制外国实体获取美国技术的贸易黑名单。这两家公司此前已被美国出口管制针对，但这封信寻求更广泛的限制，包括盟友供应链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply chain`, `#US-China tech war`, `#memory chips`, `#geopolitics`

---

<a id="item-8"></a>
## [OpenAI CFO 提出“每美元有用智能”作为 AI 投资回报率指标](https://openai.com/index/a-scorecard-for-the-ai-age) ⭐️ 8.0/10

OpenAI 首席财务官 Sarah Friar 提出了“每美元有用智能”作为衡量 AI 投资回报的新指标，将关注点从 token 成本转向任务价值。该框架与最新发布的 GPT-5.6 系列的性能亮点一同展示，其中旗舰模型 Sol 在编码任务上创下了新纪录。 这一指标可能重塑企业评估 AI 投资的方式，强调交付的价值而非原始成本。它还凸显了 GPT-5.6 Sol 等先进模型的效率优势，该模型在编码任务中比领先竞争对手减少了 54% 的输出 token。 该框架包含四个维度：完成的有用工作量、每个成功任务的全成本、AI 输出的可靠性，以及随使用增长每美元是否产生更多价值。Friar 指出，最低 token 单价不等于最低任务成本，因为更强大的模型可能一次性给出正确答案，从而总体节省资金。

telegram · zaihuapd · Jul 17, 15:00

**背景**: 传统上，软件投资回报率通过用户数或许可证续费等采用指标来衡量。对于 AI，许多公司关注每次查询的 token 成本，但这忽略了所完成工作的价值。新指标旨在捕捉 AI 产生的实际业务价值，鼓励投资于能力更强的模型，这些模型可能每 token 成本更高，但总体任务成本更低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/zh-Hans-CN/index/previewing-gpt-5-6-sol/">预览 GPT‑5.6 Sol：新一代模型 - OpenAI</a></li>
<li><a href="https://www.chatgpt-cnblog.com/guides/chatgpt/gpt-5.6-release-guide.html">GPT-5.6 震撼发布！Sol/Terra/Luna 三档齐发，编码超越 Claude，国内 ...</a></li>

</ul>
</details>

**标签**: `#AI ROI`, `#OpenAI`, `#GPT-5.6`, `#productivity metrics`, `#cost efficiency`

---