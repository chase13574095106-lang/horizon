---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> From 31 items, 11 important content pieces were selected

---

1. [GPT-5.6 Sol Pro 解决凸优化领域 30 年未解猜想](#item-1) ⭐️ 9.0/10
2. [Kimi K3：开源 2.8 万亿参数模型登顶前端编程竞技场](#item-2) ⭐️ 9.0/10
3. [LG 显示器通过 Windows Update 静默安装软件](#item-3) ⭐️ 8.0/10
4. [Stack Overflow 衰退趋势图](#item-4) ⭐️ 8.0/10
5. [PHK 反思开源中的自行车棚效应](#item-5) ⭐️ 8.0/10
6. [Anthropic 改变计划，永久保留 Claude Fable 5](#item-6) ⭐️ 8.0/10
7. [Meta 拟向 Anthropic 出租 AI 算力，潜在交易达 100 亿美元](#item-7) ⭐️ 8.0/10
8. [SpaceX 与五角大楼谈判 AI 算力交易](#item-8) ⭐️ 8.0/10
9. [台积电宣布 A14 制程将于 2028 年投产](#item-9) ⭐️ 8.0/10
10. [特朗普政府拟设类似 FINRA 的 AI 模型审查机构](#item-10) ⭐️ 8.0/10
11. [旧金山责令苹果谷歌下架“脱衣”应用](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Sol Pro 解决凸优化领域 30 年未解猜想](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

GPT-5.6 Sol Pro（一种高能力 AI 模型）通过一个提示词证明了一个凸优化领域长期未解的猜想，填补了 30 年来的空白。 这标志着 AI 辅助数学研究的一个重要里程碑，表明大型语言模型能够帮助解决凸优化等理论领域的开放问题，可能加速数学和理论计算机科学的发现。 该猜想涉及在球形域上对凸 Lipschitz 函数求解优化问题的时间复杂度。证明使用的是 GPT-5.6 Sol Pro，而非更高级的 Ultra 版本，凸显了 Sol Pro 模型的能力。

hackernews · mbustamanter · Jul 18, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，专注于在凸集上最小化凸函数。它在机器学习、工程和经济学中有广泛应用。该猜想涉及某些优化算法最优收敛速度的基本问题，三十年来一直未解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt">GPT - 5 . 6 in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://developer.puter.com/ai/openai/gpt-5.6-sol-pro/">GPT - 5 . 6 Sol Pro - API, Specs, Playground & Pricing - Puter Developer</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对此表示兴奋和好奇，用户指出这是对该领域的真正贡献。一些人讨论了对初级研究者的影响，认为低垂的果实可能不再适合人类数学家。其他人比较了 Sol Pro 和 Ultra 版本，并指出 AI 在某些情况下可以暴力破解数学逻辑。

**标签**: `#AI`, `#mathematics`, `#convex optimization`, `#LLM`, `#research`

---

<a id="item-2"></a>
## [Kimi K3：开源 2.8 万亿参数模型登顶前端编程竞技场](https://t.me/zaihuapd/42637) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是全球首个开源的 2.8 万亿参数模型，在 Frontend Code Arena 排行榜上以 1679 分位居第一，超越了 Claude Fable 5 和 GPT-5.6 Sol。 Kimi K3 表明，开源模型在特定基准测试中可以与专有前沿模型竞争甚至超越，可能加速 AI 的可及性和创新。其新颖的注意力架构也代表了重大的技术进步。 K3 采用混合架构，包含 Kimi Delta Attention (KDA)和 Attention Residuals (AttnRes)，具备原生视觉能力和 100 万 token 上下文窗口。在 Frontend Code Arena 的 7 个评测领域中，它在 6 个领域领先，仅在游戏领域落后。

telegram · zaihuapd · Jul 18, 02:29

**背景**: Kimi Delta Attention 是一种线性注意力机制，通过更细粒度的门控扩展了 Gated DeltaNet，以实现高效的长上下文处理。Attention Residuals 用基于学习的深度维度 softmax 注意力替代了标准残差连接，使每一层能够有选择地聚合早期表示。这些创新使 K3 能够高效处理极长序列，同时保持高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.26692">KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE</a></li>
<li><a href="https://arxiv.org/abs/2603.15031">[2603.15031] Attention Residuals - arXiv.org Attention Residuals - arXiv.org GitHub - MoonshotAI/Attention-Residuals Attention Residuals: The Long-Overdue Upgrade to How Neural ... Attention Residuals Explained: Rethinking Transformer Depth Attention Residuals Mechanism | kyegomez/attn_res | DeepWiki GitHub - kyegomez/attn_res: A clean, single-file PyTorch ...</a></li>
<li><a href="https://officechai.com/ai/kimi-k3-beats-fable-5-gpt-5-6-sol-on-frontend-code-arena/">Kimi K3 Beats Fable 5, GPT 5.6 Sol On Frontend Code Arena</a></li>

</ul>
</details>

**社区讨论**: 评论者就 K3 的性能是源于蒸馏还是独立创新展开了辩论，有人认为对前沿模型进行蒸馏是不可避免且有益的。其他人则对政府可能限制开源权重模型表示担忧，将其比作 Napster 时代。有用户报告称，K3 在一个任务上消耗了几乎全部 5 小时的使用额度，而 OpenAI 的 20 美元套餐只需几分钟，这引发了关于效率的质疑。

**标签**: `#AI`, `#LLM`, `#open-source`, `#benchmark`, `#architecture`

---

<a id="item-3"></a>
## [LG 显示器通过 Windows Update 静默安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 8.0/10

据报道，LG 显示器在连接到电脑时会通过 Windows Update 自动安装软件，且未经用户同意，多名用户和安全研究人员已确认此问题。 这引发了严重的安全和隐私担忧，因为该软件拥有完全系统访问权限、随系统启动，且只需插入 LG 显示器即可触发，可能被用于供应链攻击。 即使之前已连接过显示器，该软件仍会安装，且拥有网络访问权限且无沙箱隔离。解决方法包括通过组策略或设备安装设置禁用自动下载制造商应用。

hackernews · baranul · Jul 18, 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 可以推送来自硬件厂商的驱动和软件更新，但此功能被滥用于在用户无交互的情况下推送可能不需要的软件，类似于过去的 USB 自动运行问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fingerlakes1.com/2026/07/18/lg-monitor-software-now-installs-through-windows-update-and-many-users-did-not-expect-it/">LG Monitor Software Now Installs Through Windows Update and ...</a></li>

</ul>
</details>

**社区讨论**: 社区对此强烈批评，用户指出 Windows 最终应对允许此行为负责。有人提供了详细解决方法，也有人争论这是否构成供应链攻击。

**标签**: `#security`, `#privacy`, `#Windows`, `#LG`, `#supply chain attack`

---

<a id="item-4"></a>
## [Stack Overflow 衰退趋势图](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

来自 Stack Exchange Data Explorer 的一张图表显示 Stack Overflow 的活动显著下降，社区讨论将其归因于 AI、糟糕的审核以及公司收购。 这很重要，因为 Stack Overflow 一直是全球开发者的基石资源，其衰退标志着开发者获取和分享知识方式的转变，可能影响整个软件开发生态系统。 该图表在 2014 年达到峰值，远在 AI 兴起之前，而衰退在 2021 年被 Prosus 收购后加速。社区评论指出衰退早于 ChatGPT，表明多种因素共同作用。

hackernews · secretslol · Jul 18, 11:12 · [社区讨论](https://news.ycombinator.com/item?id=48956949)

**背景**: Stack Overflow 是一个面向程序员的问答平台，以其严格的审核和声誉系统而闻名。社区长期争论其排他性文化和专注于严格问答格式是否赶走了用户，而像 ChatGPT 这样的 AI 工具现在提供了获取快速答案的替代方案。

**社区讨论**: 社区评论表达了强烈的观点，认为 Stack Overflow 的衰退是自作自受，原因是参与门槛高和排斥新手的文化。一些人指出衰退始于 AI 之前，并将 Prosus 收购和网站的排他性政策视为关键因素。

**标签**: `#Stack Overflow`, `#AI impact`, `#community management`, `#data analysis`, `#online communities`

---

<a id="item-5"></a>
## [PHK 反思开源中的自行车棚效应](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

著名开源开发者 Poul-Henning Kamp（PHK）在 ACM Queue 上发表文章，反思开源社区中的自行车棚效应，分享其长期职业生涯中的经验教训，并倡导更好的决策流程。 这篇文章提供了开源关键人物的宝贵见解，帮助社区识别并缓解自行车棚效应，该效应可能浪费时间并阻碍重要问题的进展。 文章包含历史背景，如 PHK 在 1994 年创建 MD5crypt，并讨论了可逆决策的概念作为避免自行车棚效应的一种方式。

hackernews · Ygg2 · Jul 18, 17:27 · [社区讨论](https://news.ycombinator.com/item?id=48960155)

**背景**: 自行车棚效应，也称为帕金森琐碎定律，描述了群体倾向于在琐碎问题上花费不成比例的时间而忽视更重要问题的现象。这种现象在开源社区中很常见，讨论可能会陷入细节的泥潭。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Law_of_triviality">Law of triviality - Wikipedia</a></li>
<li><a href="https://thecodersblog.com/parkinson-law-triviality-bikeshedding-art-prioritization-depth-exploration/">Parkinson's Law of Triviality, Bikeshedding ... | The Coders Blog | Home</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏这篇文章，其中一位指出可逆决策应直接遵循志愿者的直觉。另一位评论者强调了 PHK 创建 MD5crypt 的历史贡献。少数人表示，即使使用 JIRA 等现代工具，自行车棚效应仍然存在，令人沮丧。

**标签**: `#open source`, `#software engineering`, `#bikeshedding`, `#governance`, `#community`

---

<a id="item-6"></a>
## [Anthropic 改变计划，永久保留 Claude Fable 5](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic 宣布，Claude Fable 5 将永久包含在 Max 和 Team Premium 订阅计划中，使用额度为上限的 50%，推翻了此前将模型从订阅中移除的计划。该变更自 2026 年 7 月 20 日起生效，是对 OpenAI 的 GPT-5.6 Sol 和 Kimi 3 竞争压力的回应。 这一战略转变确保了 Anthropic 的最佳模型仍对订阅用户可用，防止用户流失到在订阅中提供顶级模型的竞争对手。这凸显了 AI 模型市场的激烈竞争，定价和访问权限是关键战场。 Pro 和 Team Standard 用户将继续通过使用额度访问 Fable 5，并获得一次性 100 美元额度。但每月 20 美元计划的用户仍无法访问 Fable 5；只有 Max（每月 100/200 美元）和 Team Premium 计划包含该模型。

rss · Simon Willison · Jul 18, 06:00

**背景**: Claude Fable 5 是 Anthropic 最先进的大语言模型，属于 Claude Mythos 系列。Anthropic 最初因计算能力问题计划将 Fable 5 从订阅中移除，仅通过 API 提供。然而，GPT-5.6 Sol 的发布（其在编码基准测试上以更低成本超越 Fable 5）以及 Kimi 3 的出现，迫使公司重新考虑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 的分析指出，GPT-5.6 Sol 和 Kimi 3 的竞争压力使 Anthropic 的原计划难以为继。他观察到许多用户曾担心失去对 Fable 5 的访问权限，这一反转令人松了一口气，但他质疑 Anthropic 是否需要减少训练工作以腾出 GPU 来服务该模型。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#pricing`, `#competition`

---

<a id="item-7"></a>
## [Meta 拟向 Anthropic 出租 AI 算力，潜在交易达 100 亿美元](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta 正与 AI 初创公司 Anthropic 进行早期谈判，拟将其 AI 数据中心算力租予后者，潜在交易规模达 100 亿美元、为期两年。Anthropic 于 2026 年 6 月提出该方案，Meta 正在评估。 这笔交易凸显了 AI 算力的极度稀缺性，以及 Meta 将其巨额基础设施投资变现的战略。若达成，将为 Anthropic 提供关键算力，同时帮助 Meta 缓解投资者对其每年 1450 亿美元资本支出的担忧。 该交易将涉及 Anthropic 按月向 Meta 付款，双方均可提前退出。谈判尚处早期阶段，未必能最终成交。

telegram · zaihuapd · Jul 18, 01:14

**背景**: AI 算力稀缺已成为 AI 发展的主要瓶颈，2026 年初 GPU 租赁价格在 60 天内飙升 48%。Meta 计划 2026 年投入高达 1450 亿美元，主要用于 AI 和数据中心建设，并已规划到 2028 年在美国基础设施上投入 6000 亿美元。Anthropic 由前 OpenAI 员工创立，开发 Claude 系列大语言模型，专注于 AI 安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tomtunguz.com/ai-compute-crisis-2026/">The Beginning of Scarcity in AI | Tomasz Tunguz</a></li>
<li><a href="https://www.rcrwireless.com/20250908/ai-infrastructure/meta-infrastructure">Meta outlines $600 billion US infrastructure plan by 2028</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#Anthropic`, `#cloud computing`, `#infrastructure`

---

<a id="item-8"></a>
## [SpaceX 与五角大楼谈判 AI 算力交易](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX 正与美国国防部谈判，拟提供用于运行 AI 模型的数据中心算力，潜在交易金额高达数十亿美元。谈判仍在进行中，存在破裂可能。 该交易将大幅扩展 SpaceX 的云计算业务，并加深其与美国军方的联系，使其成为国家安全领域的关键 AI 基础设施提供商。这也反映了五角大楼加速采用 AI 用于国防作战的趋势。 五角大楼已批准 SpaceX、亚马逊、谷歌、微软和甲骨文在机密环境中使用 AI 模型。SpaceX 近期还与 Anthropic 和谷歌签署了类似算力供应协议，并计划大幅扩展云计算业务。

telegram · zaihuapd · Jul 18, 01:44

**背景**: SpaceX 正从火箭发射扩展到云计算领域，利用其 Starlink 卫星网络和数据中心。2026 年，它与谷歌签署了价值 300 亿美元的协议，提供 11 万块 NVIDIA GPU 用于 AI 计算。五角大楼正在将 AI 推向战场边缘，需要坚固、安全的计算基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/05/technology/spacex-google-deal.html">SpaceX Has $30 Billion Deal to Provide Google With A.I. Computing Power - The New York Times</a></li>
<li><a href="https://www.ibtimes.sg/spacexs-colossus-supercomputer-emerges-pentagons-next-ai-asset-90045">SpaceX's Colossus Supercomputer Emerges as Pentagon's Next AI Asset</a></li>
<li><a href="https://www.militaryaerospace.com/trusted-computing/article/55378097/pentagon-classified-ai-push-expected-to-drive-demand-for-rugged-embedded-computing">Pentagon classified AI push expected to drive demand for rugged embedded computing | Military Aerospace</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI`, `#Defense`, `#Cloud Computing`, `#Pentagon`

---

<a id="item-9"></a>
## [台积电宣布 A14 制程将于 2028 年投产](https://t.me/zaihuapd/42643) ⭐️ 8.0/10

台积电宣布其下一代 A14 制程技术，计划于 2028 年投产，与即将推出的 N2 制程相比，在相同功耗下速度提升 15%，或在相同速度下功耗降低 30%。 这一路线图巩固了台积电在先进半导体制造领域的领导地位，对驱动未来 AI、高性能计算和移动芯片至关重要。A14 节点的性能和效率提升将直接影响苹果、英伟达和 AMD 等关键客户产品的竞争力。 A14 是 N2 的全节点缩小，采用第二代 GAAFET 晶体管和台积电的 NanoFlex Pro 架构。台积电还计划在 2026 年末推出中间的 A16 节点，相比 N2 提供 8-10%的速度提升或 20%的功耗降低。

telegram · zaihuapd · Jul 18, 05:00

**背景**: 台积电的 N2 节点计划于 2025 年底量产，是该公司首个采用环绕栅极（GAA）晶体管替代 FinFET 的节点。A14 代表 N2 之后的下一个全节点，延续尺寸缩小的趋势以提升晶体管密度、性能和功耗效率。位于 N2 和 A14 之间的 A16 节点引入了背面供电技术，以进一步提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A14">A14 Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/tsmc-a14-process-technology-wiki/">TSMC A14 Process Technology Wiki - SemiWiki</a></li>
<li><a href="https://pr.tsmc.com/english/news/3228">TSMC Unveils Next-Generation A14 Process at North America ...</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#semiconductor`, `#chip manufacturing`, `#process technology`, `#A14`

---

<a id="item-10"></a>
## [特朗普政府拟设类似 FINRA 的 AI 模型审查机构](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 8.0/10

特朗普政府正考虑设立一个类似金融业监管局（FINRA）的独立 AI 监管机构，负责审查顶尖 AI 模型的安全性。该方案由财政部长斯科特·贝森特牵头，目前正由白宫幕僚长苏茜·威尔斯审阅，并与 Google DeepMind 首席执行官德米斯·哈萨比斯近期提出的建议方向一致。 此举旨在回应华尔街对网络安全的担忧以及硅谷对政府临时性管控措施的不满，让两大行业在制定安全标准方面拥有更大发言权。如果实施，将为前沿 AI 模型建立正式的、由行业资助的监管框架，可能影响全球 AI 治理格局。 拟议中的机构将向美国证券交易委员会（SEC）汇报，类似于 FINRA 与 SEC 的关系。该方案仍在讨论中，尚未经总统特朗普审阅，内容可能调整。此前，Anthropic 和 OpenAI 均对美国要求修改或延迟发布其最新模型表示异议。

telegram · zaihuapd · Jul 18, 05:45

**背景**: FINRA 是一个自律监管组织（SRO），在美国证券交易委员会（SEC）的监督下监管美国经纪交易商，由其所监管的行业提供资金。拟议中的 AI 监管机构将类似地成为一个独立的、由行业资助的机构，有权审查并可能限制高风险 AI 模型，借鉴了金融领域的监管模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/美国证券法">美国证券法 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/美国金融业监管局/9213493">美国金融业监管局_百度百科</a></li>

</ul>
</details>

**社区讨论**: 分享该新闻的 Telegram 频道未包含社区评论，因此无法提供讨论摘要。

**标签**: `#AI监管`, `#美国政策`, `#FINRA`, `#AI安全`, `#行业动态`

---

<a id="item-11"></a>
## [旧金山责令苹果谷歌下架“脱衣”应用](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 8.0/10

旧金山市检察长邱信福致函苹果和谷歌，要求其从应用商店中下架数十款利用人工智能技术生成非自愿深度伪造裸体图像的“脱衣”应用。信件警告称，这些公司可能因此获利数百万美元，并面临民事处罚。 此举标志着政府对主要科技平台进行重大干预，要求其对促成非自愿深度伪造色情内容的第三方应用承担责任，可能为平台责任树立先例。这凸显了 AI 生成内容带来的日益增长的法律和伦理挑战，以及加强内容审核的必要性。 科技透明项目此前已在今年 1 月和 4 月就这些应用发出警告。苹果回应称已下架 3 款应用并终止相关开发者账号，谷歌则表示已暂停被点名的 5 款 Play 应用。

telegram · zaihuapd · Jul 18, 08:45

**背景**: “脱衣”应用利用生成式 AI 修改照片，在未经他人同意的情况下创建逼真的裸体图像，这是一种深度伪造色情内容。此类内容已被用于色情报复和骚扰，引发了诉讼和刑事调查。根据美国法律，第 230 条通常保护平台免于对第三方内容承担责任，但该命令通过指控平台明知有害应用仍从中获利，挑战了这一豁免权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://peopleofcolorintech.com/articles/100-plus-nudify-apps-found-on-apple-store-and-google-play/">100-Plus “Nudify” Apps Found On Apple’s App Store And Google Play</a></li>
<li><a href="https://www.daeryunlaw.com/us/practices/detail/online-platform-liability">Online Platform Liability: What Platforms Must Do to Stay Protected</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#deepfakes`, `#content moderation`, `#tech regulation`, `#privacy`

---