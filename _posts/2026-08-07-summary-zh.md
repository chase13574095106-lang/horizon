---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> From 26 items, 12 important content pieces were selected

---

1. [pgrust：用 Rust 重写 Postgres，实现 300 倍分析加速](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731：更快、更便宜，获用户好评](#item-2) ⭐️ 8.0/10
3. [科技从业者幻灭：信仰危机](#item-3) ⭐️ 8.0/10
4. [Oracle 禁止在 OpenJDK 中使用 AI 生成代码](#item-4) ⭐️ 8.0/10
5. [据报道，2027 年内存产能已售罄，AI 需求是主因](#item-5) ⭐️ 8.0/10
6. [在 150 万页网站上与爬虫斗争的一年](#item-6) ⭐️ 8.0/10
7. [新墨西哥州法院裁定 Meta 支付 5.67 亿美元赔偿儿童心理健康损害](#item-7) ⭐️ 8.0/10
8. [Wyzer：一种针对分布式死锁的新语言](#item-8) ⭐️ 8.0/10
9. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-9) ⭐️ 8.0/10
10. [SK 海力士确认 V10 NAND 为 375 层堆叠并采用晶圆键合技术](#item-10) ⭐️ 8.0/10
11. [sub2api 存在严重 OAuth 漏洞，仅凭邮箱即可接管账户](#item-11) ⭐️ 8.0/10
12. [据报 OpenAI 拟下周发布新模型 Astra](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [pgrust：用 Rust 重写 Postgres，实现 300 倍分析加速](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 9.0/10

文章介绍了 pgrust，一个基于 Rust 重新实现的 Postgres 查询执行和存储层，通过批处理、算子融合和 SIMD，在 Clickbench（分析基准）上比 Postgres 快 300 倍。在 OLTP 基准上，pgrust 比 Postgres 快 30%。 这展示了 Postgres 在分析工作负载上的显著性能飞跃，可能影响未来的数据库设计，并为高性能分析提供可行的替代方案。同时，它也引发了关于社区驱动的关键基础设施重写的信任和采用问题的讨论。 优化重点在于减少查询引擎的 CPU 和内存带宽使用。该项目优先保证正确性，通过形式化验证和差分模糊测试，已证明超过 1000 个面向用户的函数与 Postgres 逻辑一致。

hackernews · poly2it · Aug 7, 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: Postgres 是一个流行的开源关系型数据库，但其查询引擎在分析工作负载上不如 Clickhouse 等专用系统优化。pgrust 是用 Rust 完全重写 Postgres 核心的项目，旨在提高性能的同时保持兼容性。批处理、算子融合和 SIMD 是现代分析数据库加速查询处理的常用技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now faster than Postgres and Clickhouse · GitHub</a></li>
<li><a href="https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/">Rebuilding Postgres for 300x faster analytics: batching, operator ...</a></li>
<li><a href="https://dev.to/terminalchai/pgrust-the-open-source-project-rewriting-postgresql-in-rust-4860">pgrust: The Open-Source Project Rewriting PostgreSQL in Rust - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 作者参与了讨论，通过强调形式化验证和模糊测试来回应信任问题。一些评论者对采用表示怀疑，因为对 Postgres 团队的信任，而另一些则赞赏自适应规划，并认为 pgrust 有潜力作为 SQLite 的替代品嵌入。

**标签**: `#database`, `#postgres`, `#query-engine`, `#performance`, `#rust`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731：更快、更便宜，获用户好评](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek 发布了 V4 Flash 0731，这是其效率优化的混合专家模型的新版本，具有 1M token 上下文窗口和可调推理努力。用户报告称，与之前的预览版相比，性能显著提升，速度快且成本低。 该版本在性能和成本之间取得了令人瞩目的平衡，可能通过提供比 Claude 和 GPT-4 等专有模型更便宜的替代方案来颠覆 AI 模型市场。它可能加速开源权重模型在编码和智能体任务中的采用。 该模型总参数为 284B，激活参数为 13B，支持 1M token 上下文。尽管激活规模较小，但在基准测试上优于 DeepSeek V4 Pro（预览版），并与领先的专有模型大致相当。定价是动态的，高峰时段按中国时间定义，这可能影响亚洲以外的用户。

hackernews · tosh · Aug 7, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek 是一家中国 AI 研究公司，以发布可与专有系统相媲美的开源权重模型而闻名。V4 Flash 是 V4 系列中注重效率的变体，专为快速推理和高吞吐量工作负载而设计，适用于智能体编码和数据分析。ARC-AGI-2 基准测试抽象推理能力，该模型在此基准上的表现因其纯文本特性而引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.together.ai/models/deepseek-v4-flash-0731">DeepSeek V 4 Flash 0731 API | Together AI</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash/benchmarks">DeepSeek V4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 用户对该模型的速度和成本效益非常热情，一位用户指出它“几乎适用于所有事情”，而且便宜到成本可以忽略不计。另一位用户强调了在高端硬件上的速度，实现了约 8k tok/s 的预填充和单流约 250 tok/s。然而，也存在对账户封禁的担忧，一位用户报告称，在尝试从 JetBrains IDE 进行身份验证后，其 Claude 账户被封禁；另一位用户指出高峰时段定价基于中国时间，这可能影响非亚洲用户。

**标签**: `#AI`, `#LLM`, `#DeepSeek`, `#model release`, `#performance`

---

<a id="item-3"></a>
## [科技从业者幻灭：信仰危机](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

《Noema》杂志的一篇文章探讨了科技从业者中普遍存在的悲伤和职业信仰丧失现象，质疑该行业及其劳动力的未来。这篇文章在 Hacker News 上引发了广泛讨论，获得了 275 个点赞和 411 条评论。 这篇文章凸显了科技行业日益严重的危机，从业者对自己的职业越来越感到幻灭。高参与度表明它引起了许多人的深刻共鸣，可能影响人才留存和行业文化。 文章引用了历史类比，如印刷行业的衰落，并讨论了网络世界的毒性。评论者分享了个人倦怠经历和对更接地气职业的向往，但也有人指出离开科技行业在经济上不切实际。

hackernews · RickJWagner · Aug 7, 12:42 · [社区讨论](https://news.ycombinator.com/item?id=49209539)

**背景**: 科技行业长期以来被视为成功之路，但近年来，关于倦怠、心理健康和技术伦理影响的担忧日益增加。这篇文章触及了关于科技职业可持续性以及构建数字世界的人们福祉的更广泛讨论。

**社区讨论**: 评论者表达了各种观点，从将科技行业的衰落与印刷行业的消亡相比较，到指出网络的毒性。一些人分享了个人激情减退和幻想逃离的故事，而另一些人则指出了离开该行业的经济障碍。

**标签**: `#tech culture`, `#mental health`, `#career`, `#industry trends`, `#workforce`

---

<a id="item-4"></a>
## [Oracle 禁止在 OpenJDK 中使用 AI 生成代码](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) ⭐️ 8.0/10

Oracle 已实施一项临时政策，自 2026 年 4 月 9 日起禁止向 OpenJDK 贡献 AI 生成的代码。该政策禁止在 OpenJDK 贡献中使用由大型语言模型、扩散模型或类似深度学习系统生成的内容。 该政策影响了广泛使用的 OpenJDK 项目，该项目支撑着许多关键业务系统。它凸显了开源社区中 AI 采用与法律/审查担忧之间的紧张关系，可能为其他项目树立先例。 该临时政策适用于社区贡献，但可能不影响核心开发者。Oracle 以审查负担和版权法律不确定性为由，尽管其自身在 GraalVM 等其他产品中热衷于 AI 生成的代码。

hackernews · delduca · Aug 7, 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49213754)

**背景**: OpenJDK 是 Java 平台标准版的开源实现，由 Oracle 领导下的社区维护。该项目有法律审查的历史，包括过去的版权纠纷，这可能解释了 Oracle 的谨慎态度。该临时政策是 Oracle 律师起草最终政策之前的过渡措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openjdk.org/legal/ai">OpenJDK Interim Policy on Generative AI</a></li>
<li><a href="https://www.techzine.eu/news/devops/143395/oracle-bans-ai-generated-contributions-to-openjdk/">Oracle bans AI-generated contributions to OpenJDK - Techzine Global</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些人认为鉴于法律风险和审查负担，该禁令是明智的，而另一些人则指出 Oracle 自身 AI 投资的讽刺意味。一些评论者指出，该政策可能主要针对社区提交，而非核心开发者，并质疑此类禁令的可执行性。

**标签**: `#OpenJDK`, `#AI policy`, `#open source`, `#legal`, `#Oracle`

---

<a id="item-5"></a>
## [据报道，2027 年内存产能已售罄，AI 需求是主因](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 8.0/10

据报道，2027 年的内存产能已经售罄，内存制造商正与客户签订长期协议。这凸显了由 AI 需求和高带宽内存（HBM）生产权衡导致的严重供应限制。 这一事态发展预示着内存短缺将持续，可能影响消费电子产品的价格和供应。它强调了内存（memory）在 AI 时代中的战略重要性，影响制造商、云服务提供商和最终用户。 HBM（高带宽内存）生产每单位比特消耗的晶圆产能大约是 DDR5 的三倍，从而限制了非 HBM 产品的供应。内存制造商采用预付款押金模式，合同期限为三到五年，导致新买家没有空间。

hackernews · inigyou · Aug 7, 07:58 · [社区讨论](https://news.ycombinator.com/item?id=49207236)

**背景**: 内存产能指的是用于计算机、服务器和其他设备的 DRAM 芯片的生产产量。高带宽内存（HBM）是一种垂直堆叠的专用 DRAM，为 AI 加速器提供高速度，但其生产在晶圆使用效率上较低，导致与传统内存（如 DDR5）之间存在权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/351344/memory-makers-seal-2027-deals-no-room-for-new-buyers">Memory Makers Seal 2027 Deals: No Room for New... | TechPowerUp</a></li>
<li><a href="https://www.intelligentliving.co/hbm-ram-ai-datacenter-ddr5-supply-chain/">HBM is Coming for Your PC's RAM: AI Datacenter High-Bandwidth Memory Squeezes Global DDR5 RAM Supply Chain</a></li>
<li><a href="https://wccftech.com/aletheia-warns-hbm-prices-will-double-in-2027-as-memory-becomes-ais-most-critical-component/">Aletheia Warns HBM Prices Will Double in 2027 as Memory Becomes...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对消费价格和供应影响的担忧，一些人指出通胀效应。其他人则强调了 HBM 生产的技术权衡，并分享了个人策略，如囤积旧 RAM 或避免使用 AI 以减少内存压力。

**标签**: `#memory`, `#HBM`, `#supply chain`, `#AI hardware`, `#semiconductors`

---

<a id="item-6"></a>
## [在 150 万页网站上与爬虫斗争的一年](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) ⭐️ 8.0/10

一位网站所有者详细描述了一年多来与爬虫的斗争，报告称机器人流量占 99%，并在一个月内导致成本飙升 500%。该帖子强调了使用 Cloudflare 反机器人服务的权衡以及给小网站所有者带来的财务负担。 这个故事凸显了独立网络发布者面临的机器人流量日益严峻的挑战，他们面临成本上升，必须在开放性和保护之间做出选择。它还引发了关于网络控制权集中在 Cloudflare 等公司手中的争论，以及替代解决方案的必要性。 该网站的正常月度成本约为 90 美元，但一个糟糕的峰值月份成本上涨了 500%，部分原因是 Cloudflare 的 D1 数据库成本。作者承认自己也是爬虫，会抓取公共文档，这为反爬虫立场增添了复杂性。

hackernews · petercooper · Aug 7, 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49211386)

**背景**: 网络爬虫是从网站自动提取数据的行为，常用于价格监控、内容聚合或 AI 训练。像 Cloudflare Bot Management 这样的反机器人服务使用机器学习和行为分析来检测和阻止恶意机器人，但它们也可能阻止合法用户并增加网站所有者的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/products/bot-mitigation/">Cloudflare Bot Management - Stop Bad Bots</a></li>
<li><a href="https://finedata.ai/blog/anti-bot-detection-2026/">Anti - Bot Detection: How Cloudflare , DataDome, and PerimeterX Work</a></li>
<li><a href="https://medium.com/@mayankchandel2567/how-does-cloudflare-bot-detection-work-d77179756cdc">How does Cloudflare bot detection works | by Mayank... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对将网站访问决策外包给 Cloudflare 等大公司的担忧，认为这损害了开放网络。一些人建议使用替代解决方案，如基于工作量证明的机器人检测工具 Anubis，而另一些人则建议迁移到静态网站以降低成本。一位评论者分享说，Claude 的搜索机器人从他们的网站抓取了 20.5 万页，但只带来了一个推荐，凸显了被爬取内容缺乏补偿的问题。

**标签**: `#web scraping`, `#bots`, `#Cloudflare`, `#website costs`, `#anti-bot`

---

<a id="item-7"></a>
## [新墨西哥州法院裁定 Meta 支付 5.67 亿美元赔偿儿童心理健康损害](https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta) ⭐️ 8.0/10

2026 年 8 月 6 日，新墨西哥州法院裁定 Meta 支付 5.67 亿美元，以赔偿对儿童心理健康造成的损害，另有报道提及 9.42 亿美元的金额。该裁决还要求 Meta 为未成年用户做出改变。 这一具有里程碑意义的裁决为追究社交媒体平台在儿童安全和心理健康影响方面的责任树立了重要法律先例。它可能影响其他司法管辖区，并促使 Meta 修改其面向年轻用户的算法和政策。 法院认定 Meta 违反了新墨西哥州的公共妨害法（NMSA 1978 § 30-8-1）。考虑到新墨西哥州人口稀少（约 200 万），5.67 亿美元的金额使得人均影响相对于 Meta 的收入而言相当可观。

hackernews · boplicity · Aug 7, 00:06 · [社区讨论](https://news.ycombinator.com/item?id=49204352)

**背景**: 像 Instagram 和 TikTok 这样的社交媒体平台因其对年轻用户心理健康的影响（包括成瘾设计和有害内容）而受到越来越多的审查。此案是各州和国家监管未成年人社交媒体更广泛努力的一部分，一些司法管辖区已经实施了禁令或限制。

**社区讨论**: 评论者指出，尽管罚款相对于 Meta 的全球收入可能显得微不足道，但对于像新墨西哥州这样的小司法管辖区来说意义重大。一些人表达了对短视频平台成瘾性的担忧以及算法变革的必要性，而另一些人则争论裁决的法律依据和比例性。

**标签**: `#Meta`, `#legal`, `#child safety`, `#social media`, `#mental health`

---

<a id="item-8"></a>
## [Wyzer：一种针对分布式死锁的新语言](https://github.com/Wyzer-Lang/wyzer) ⭐️ 8.0/10

Wyzer 是一种新的静态类型、编译型、面向资源的编程语言，它集成了编排式编程和 Perceus 内存管理，以防止分布式死锁。该项目经过五个月的研究和几周的开发，即将发布 0.1.0 版本。 Wyzer 解决了主流语言（如 Rust）未覆盖的分布式系统安全关键缺口，可能为编写无死锁的分布式应用提供新途径。如果成功，它可能影响未来的语言设计，并为构建可靠分布式系统的开发者提供实用的替代方案。 Wyzer 使用线性/仿射类型和 Perceus 引用计数，而不是借用检查器和生命周期，作者声称这对 LSP 来说计算上更简单。该语言推广了编排式编程，这是一种单一程序描述多个参与者之间交互的范式，并编译为每个参与者的可执行代码。

hackernews · v0id_isgood · Aug 7, 12:28 · [社区讨论](https://news.ycombinator.com/item?id=49209385)

**背景**: 编排式编程是一种用于分布式系统的编程范式，程序被编写为多个并发参与者之间交互的组合，从构造上确保无死锁。Perceus 是一种无垃圾的引用计数内存管理技术，最初在 Koka 语言中实现，具有低内存开销和竞争力的性能。Wyzer 旨在将这些概念结合到一种高级语言中，以解决分布式死锁和协议不匹配问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Choreographic_programming">Choreographic programming</a></li>
<li><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2020/11/perceus-tr-v1.pdf">Perceus: Garbage Free Reference Counting with Reuse</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3453483.3454032">Perceus: garbage free reference counting with reuse | Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation</a></li>

</ul>
</details>

**社区讨论**: 社区对该项目的雄心和新颖性总体持积极态度，评论称赞文档清晰，并尝试将学术概念付诸实践。然而，一些评论者质疑该语言如何保证无死锁，并要求提供更多示例和澄清底层机制。

**标签**: `#programming language`, `#distributed systems`, `#choreographic programming`, `#memory management`, `#Rust alternative`

---

<a id="item-9"></a>
## [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10

美国商务部工业与安全局（BIS）已启动系统性审查，调查中国 AI 企业如何通过海外渠道（包括远程云计算）获取英伟达芯片。此前有指控称，月之暗面的 Kimi K3 模型使用了非法获取的英伟达芯片，并通过泰国远程访问。 此次审查可能导致新规出台，限制中国企业通过云服务获取先进 AI 芯片，从而重塑全球 AI 供应链。同时，这也加剧了中美科技紧张局势，影响英伟达、阿里巴巴和月之暗面等主要企业。 BIS 正在整理两份名单：涉嫌走私受限芯片的黑市所在地，以及中国企业远程租用芯片的国家。限制远程访问的合法性存疑，但美国众议院已通过两党法案拟授予该权力，预计将遭到英伟达等公司反对。据报道，阿里巴巴通过新加坡壳公司，经 Megaspeed 使用位于马来西亚的英伟达芯片。

telegram · zaihuapd · Aug 7, 11:18

**背景**: 美国对华实施先进 AI 芯片出口管制，以减缓其技术进步。然而，中国企业通过云计算和第三国中介等途径寻求替代获取方式。2026 年 1 月众议院通过的《远程访问安全法案》（H.R. 2683）旨在通过监管云端访问先进芯片来堵住这一漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://channel.cx.ms/posts/6066">#article #read...</a></li>
<li><a href="https://info.51.ca/articles/1481007">黄仁勋身边神秘样女子 是 芯 片 偷卖中国的要角？_ 无忧资讯</a></li>

</ul>
</details>

**标签**: `#US-China tech war`, `#AI chips`, `#export controls`, `#NVIDIA`, `#cloud computing`

---

<a id="item-10"></a>
## [SK 海力士确认 V10 NAND 为 375 层堆叠并采用晶圆键合技术](https://www.gelonghui.com/live/2599953) ⭐️ 8.0/10

SK 海力士已确认其下一代 V10 NAND 闪存将采用 375 层堆叠，这是该公司首次使用晶圆键合技术。该公司声称每瓦性能较上一代提升 2.5 倍，专为 AI 基础设施优化。 这一里程碑对半导体行业意义重大，因为它将 NAND 堆叠推向 300 层以上，满足了 AI 工作负载对高容量、高能效内存日益增长的需求。这也标志着晶圆键合技术成为未来 NAND 扩展的关键推动力，可能影响三星、铠侠等竞争对手。 V10 NAND 是 321 层 V9“4D NAND”的继任者，也是 SK 海力士首款采用晶圆键合技术的 NAND 产品。据行业消息人士称，SK 海力士已完成生产验证，并计划在 2026 年底前量产 375 层 NAND，且无需新建晶圆厂。

telegram · zaihuapd · Aug 7, 12:19

**背景**: NAND 闪存是一种非易失性存储技术，广泛用于固态硬盘和移动设备。增加堆叠层数可提高存储密度，但传统堆叠在性能和功耗方面面临挑战。晶圆键合（又称混合键合）技术将存储单元和外围逻辑分别制造后再键合在一起，从而提升性能并支持更高层数。三星和 SK 海力士等主要存储厂商正采用该技术以满足 AI 基础设施的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendforce.com/news/2025/12/08/news-sk-hynix-reportedly-accelerates-hybrid-bonding-for-300-layer-v10-nand-eying-2027-mass-production/">[News] SK hynix Reportedly Accelerates Hybrid Bonding for 300-Layer V10 NAND, Eying 2027 Mass Production</a></li>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=11210">SK hynix to Mass Produce 375-Layer NAND by Year-End, Introduce Molybdenum < Semiconductor < 기사본문 - The Elec Inc.</a></li>
<li><a href="https://www.trendforce.com/news/2026/06/12/news-the-race-to-400-layer-nand-roadmaps-and-key-technologies-driving-samsung-sk-hynix-and-kioxia/">[News] The Race to 400-Layer NAND: Roadmaps and Key Technologies Driving Samsung, SK hynix, and Kioxia</a></li>

</ul>
</details>

**标签**: `#NAND`, `#SK Hynix`, `#semiconductor`, `#AI infrastructure`, `#memory technology`

---

<a id="item-11"></a>
## [sub2api 存在严重 OAuth 漏洞，仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

sub2api v0.1.171 及之前版本被披露存在一个 CVSS 8.8 的严重 OAuth 账户接管漏洞。攻击者仅需知道受害者的邮箱，无需密码、验证码或用户交互，即可将自己的 OAuth 身份绑定到受害者账户。 该漏洞可导致账户被完全接管，攻击者能够控制 API 密钥、账单余额和订阅配额。这对所有 sub2api 用户（尤其是拼车共享订阅的用户）构成严重风险，也凸显了开源项目中正确实现 OAuth 的重要性。 漏洞出在 pending session 流程的 existingUser 分支，该分支未校验密码和验证码。攻击者将目标用户 ID 设为受害者后即可完成 OAuth 绑定，此后每次 OAuth 登录都会解析为受害者账户。

telegram · zaihuapd · Aug 7, 14:59

**背景**: OAuth 2.0 是一种广泛使用的授权框架，允许用户通过第三方提供商登录。账户接管漏洞通常源于 OAuth 流程在将身份链接到现有账户时处理不当，尤其是当邮箱或用户 ID 等用户可控参数未经验证时。该问题已被跟踪为 CVE-2026-27812。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-27812/">CVE-2026-27812: Sub2API Auth Bypass Vulnerability</a></li>
<li><a href="https://github.com/Wei-Shaw/sub2api">GitHub - Wei-Shaw/sub2api: Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。</a></li>
<li><a href="https://book.hacktricks.xyz/pentesting-web/oauth-to-account-takeover">OAuth to Account takeover - HackTricks</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了该漏洞的严重性，用户对利用的简便性以及对拼车订阅服务的潜在影响表示担忧。一些人呼吁立即修补，并对类似的 OAuth 实现进行彻底的安全审计。

**标签**: `#security`, `#OAuth`, `#vulnerability`, `#account takeover`, `#sub2api`

---

<a id="item-12"></a>
## [据报 OpenAI 拟下周发布新模型 Astra](https://t.me/zaihuapd/43046) ⭐️ 8.0/10

据报道，OpenAI 正准备最早于下周发布名为 Astra 的新大模型。该模型据称是一次全新的预训练，是自 GPT-4.5 以来规模最大的模型，其内部测试版本代号为“mewfour”，已被定为候选发布版本。 如果消息属实，Astra 将标志着 OpenAI 模型发展的一个重要里程碑，可能提升科学推理和复杂问题解决的能力。其发布可能对 AI 行业和竞争格局产生重大影响，影响依赖前沿 AI 模型的开发者、研究人员和企业。 据爆料，Astra 是一次全新的预训练，是 OpenAI 自 GPT-4.5 以来训练过的最大模型。最新的内部测试版本代号“mewfour”已被定为候选发布版本，表明该模型已接近完成。

telegram · zaihuapd · Aug 7, 16:44

**背景**: OpenAI 一直在开发越来越强大的大语言模型，GPT-4.5 是之前的一个重要版本。最近，OpenAI 预告了其下一个主要模型 Astra，指出一个内部版本解决了数学和理论计算机科学中的十个长期问题，表明其注重科学推理。预计该模型将是 AI 能力的一次重大进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/artificial-intelligence/openai-teases-astra-its-next-major-ai-model-after-it-solves-10-long-standing-math-problems/">OpenAI teases Astra, its next major AI model, after it solves 10 long-standing math problems</a></li>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer science | OpenAI</a></li>
<li><a href="https://garymarcus.substack.com/p/openais-amazing-but-vastly-oversold">OpenAI’s amazing — but vastly oversold — new model Astra</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI model`, `#rumor`, `#GPT-4.5`, `#large language model`

---