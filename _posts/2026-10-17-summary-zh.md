---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> From 33 items, 13 important content pieces were selected

---

1. [Claude AI 破解 25 年悬案：NIST ECDSA 曲线种子来源被揭开](#item-1) ⭐️ 9.0/10
2. [特斯拉发布配备冷气推进器的飞行版 Roadster](#item-2) ⭐️ 8.0/10
3. [PS5LM 通过 llama.cpp 在越狱 PS5 上原生运行 GGUF 大模型](#item-3) ⭐️ 8.0/10
4. [Waymo 将自动驾驶网约车服务扩展至多伦多](#item-4) ⭐️ 8.0/10
5. [JPEG XL 与 AVIF：面向 Web 用例的深度对比](#item-5) ⭐️ 8.0/10
6. [苹果 MLX 在四台 Mac Studio 上运行近万亿参数 Muse Spark Open 模型](#item-6) ⭐️ 8.0/10
7. [Mercor 研究：美国 90%工作时间缺乏 AI 基准测试覆盖](#item-7) ⭐️ 8.0/10
8. [OpenBSD 37 年老内核漏洞被利用获取 root 权限](#item-8) ⭐️ 8.0/10
9. [StarSkirmish Bench v0.2 测试大模型编写星际争霸机器人](#item-9) ⭐️ 8.0/10
10. [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](#item-10) ⭐️ 8.0/10
11. [中国拟对 40 项人工智能、生物医药和光伏技术实施临时出口登记](#item-11) ⭐️ 8.0/10
12. [苹果首款折叠屏 iPhone Duo 一分钟售罄，股价盘前涨超 2%](#item-12) ⭐️ 8.0/10
13. [Anthropic IPO 估值预期下调至 1.5 万亿美元](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude AI 破解 25 年悬案：NIST ECDSA 曲线种子来源被揭开](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10

Anthropic 宣布其 Claude AI 模型在不到半小时内发现了 NIST 椭圆曲线种子（P-192、P-224、P-256、P-384 和 P-521）的来源。这些种子并非如先前假设的那样由任何哈希算法生成，而是 C 标准库中 lrand48 随机数生成器以 Unix 时间戳为种子产生的输出。 这一发现解开了一个长达 25 年的密码学谜团，并驳斥了长期以来关于 NSA 在 NIST 标准化椭圆曲线中故意植入后门的阴谋论。它恢复了人们对广泛部署于 TLS、代码签名及全球无数安全协议中的 ECDSA 曲线的信心。 Claude 发现这些种子是使用以 Unix 时间戳为种子的 lrand48 生成的，但第五个二进制种子 B-163 仍无法解释——可能是发布过程中出现了笔误。该发现并不能排除通过搜索特定时间戳来挑选具有特定属性的曲线的可能性，因为被丢弃的候选种子无法被观察到。

hackernews · ahlCVA · Oct 16, 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: NIST 于 2000 年在 FIPS 186-2 中发布了 P-192 至 P-521 椭圆曲线，规定应使用 SHA-1 对任意种子进行哈希以推导曲线参数。这些种子的来源从未被公开，引发了数十年来关于 NSA 影响力的猜测。lrand48 是 C 标准库中的伪随机数生成器，使用 48 位整数运算的线性同余算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://words.filippo.io/seeds-solved/">The NIST Elliptic Curves Seeds Bounty Has Been Claimed</a></li>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>
<li><a href="https://runtimewire.com/article/claude-traces-nist-ecdsa-seeds-to-timestamps">Claude traces NIST's ECDSA curve seeds to 1990s timestamps</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了调侃与释然，有人感叹“13 年的阴谋论就为了 srand48(time(NULL))”，另一人则称这是“对整整一代 NIST 密码学阴谋论的毁灭性消息”。但也有人提出保留意见：生成方法并不能证明这些曲线未被挑选以具备特定属性，而无法解释的 B-163 种子可能只是笔误。

**标签**: `#cryptography`, `#elliptic-curves`, `#NIST`, `#AI-discovery`, `#security`

---

<a id="item-2"></a>
## [特斯拉发布配备冷气推进器的飞行版 Roadster](https://www.tesla.com/roadster) ⭐️ 8.0/10

特斯拉发布了一款新的 Roadster 原型车，采用源自 SpaceX 的冷气推进器以及可选的火箭发动机配置，并在宣传视频中展示了车辆悬停和翻转的能力。该车分为三个版本——Performance、Thrust 以及仅限受邀用户、配备 10 个喷口推进器套件的 Rocket 版——量产时间据称定在 2028 年。 这次演示是一次重大的工程与营销事件，它模糊了超级跑车与低空飞行器之间的界限，并在社区中引发了巨大反响（在 HN 上获得超过 1100 分和 2000 条评论）。同时，它也引发了人们对火箭辅助消费级车辆经济可行性和安全性的质疑。 据报道，该推进系统使用 10000 psi 的 COPV 和冷气推进器，以帮助实现宣称的 0.81 秒 0–60 英里/小时加速，而完整的 Rocket 配置仅限受邀用户。冷气推进器是一种简单、无燃烧的推进系统，其推力低于传统火箭发动机，且车辆的压缩气体储量有限。

hackernews · shekhar101 · Oct 16, 01:32 · [社区讨论](https://news.ycombinator.com/item?id=50112657)

**背景**: 冷气推进器是一种火箭发动机，通过喷嘴释放加压气体产生推力，不涉及燃烧，因此结构简单可靠但推力相对较低；它们常用于航天器姿态控制和 CubeSat 推进。特斯拉的 Roadster 演示将这项太空技术应用于公路跑车，并有 SpaceX 参与，而该公司历来有雄心勃勃但长期延迟交付的承诺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cold_gas_thruster">Cold gas thruster</a></li>
<li><a href="https://www.motortrend.com/news/tesla-roadster-thrust-system-spacex-technology-explained">How Did the Tesla Roadster Fly? Here's How It Works - MotorTrend Tesla's Flying Roadster: What Was Shown, How Cold-Gas ... Cold Gas Thrusters - moog.com Tesla's redesigned Roadster has a cold-gas thruster option ... Cold Gas Thruster – Definition & Detailed Explanation ... How Tesla’s Roadster fan system and thrusters are built to ...</a></li>
<li><a href="https://electriccarsreport.com/2026/10/tesla-roadster-revealed-with-rocket-thrusters-and-0-60-mph-in-0-81-seconds/">Tesla Roadster Unveiled With Rocket Thrusters</a></li>

</ul>
</details>

**社区讨论**: 评论者对车辆真的能飞感到惊叹，称其为不可思议的工程成就，但许多人质疑其经济可行性和安全性——指出 COPV 驱动的推进器可能伤及旁观者。其他人批评特斯拉为一辆可能永远不会交付的车收取多年订金，还有一些人则关注车辆能够垂直行驶或吸附在天花板上的惊人能力。

**标签**: `#Tesla`, `#electric vehicles`, `#engineering`, `#rocket propulsion`, `#marketing stunt`

---

<a id="item-3"></a>
## [PS5LM 通过 llama.cpp 在越狱 PS5 上原生运行 GGUF 大模型](https://github.com/cobanov/PS5LM) ⭐️ 8.0/10

一个名为 PS5LM（cobanov/PS5LM）的 GitHub 项目通过将 llama.cpp 移植到主机上，使越狱后的 PlayStation 5 能够原生运行 GGUF 格式的大语言模型。据报道它可以在 2 比特量化下运行 Qwen 3.8 27B 等模型，把原本封闭的游戏主机变成通用的 LLM 推理设备。 这表明搭载强大 AMD APU 的消费级游戏主机可以被改造成本地 AI 推理设备，对于需要长期运行的 LLM 任务而言，可能成为专用 GPU 之外的廉价替代方案。它也进一步引发了关于硬件所有权、越狱合法性以及封闭设备是否应被视为通用计算机的广泛讨论。 该项目依赖已越狱的 PS5，也就是说需要利用主机安全漏洞，而且目前展示的性能仅限于在激进 2 比特量化下运行相对较小的模型。社区成员指出其功耗成本约为每天 70 美分，每天可产出约 200 万个输出 token，并认为 BC250 这类前挖矿 APU 主板也可能实现类似效果。

hackernews · Anon84 · Oct 16, 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50122431)

**背景**: GGUF 是 llama.cpp 使用的模型文件格式，而 llama.cpp 是一个流行的 C/C++ 推理引擎，用于在 CPU 和 GPU 上本地运行量化后的大语言模型。PlayStation 5 采用定制的 AMD APU，包含 Zen 2 CPU 核心和 RDNA 2 图形核心，越狱它需要利用软件或硬件漏洞绕过索尼的安全机制。在这样的硬件上运行 llama.cpp，意味着要把推理引擎适配到主机非标准的软件环境中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/examples/gguf/gguf.cpp">llama . cpp /examples/ gguf / gguf . cpp at master · ggml-org/ llama . cpp</a></li>
<li><a href="https://grokipedia.com/page/PlayStation_5_jailbreak">PlayStation 5 jailbreak</a></li>
<li><a href="https://huggingface.co/unsloth/Qwen3.8-27B-GGUF">unsloth/Qwen3.8-27B- GGUF · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对把封闭主机改造成通用计算机感到兴奋，有人表示此前从未考虑过购买 PS5，如今却动了心。其他人则指出这种持续、低成本 token 流的实用场景，例如监控服务器错误或安防录像，并认为同样的方法也能用在便宜的 BC250 前挖矿主板上。一个明显的担忧是项目托管在 GitHub 上可能被索尼下架，有评论者因此建议改用自建域名。

**标签**: `#llama.cpp`, `#PS5`, `#jailbreak`, `#LLM`, `#hardware`

---

<a id="item-4"></a>
## [Waymo 将自动驾驶网约车服务扩展至多伦多](https://waymo.com/blog/2026/10/waymo-in-toronto/) ⭐️ 8.0/10

Waymo 在其官方博客上宣布，将其自动驾驶网约车服务扩展至加拿大多伦多，这是其在美国现有运营之外开辟的新国际市场。公告中强调了创造就业机会，并在 Hacker News 上引发了 347 条评论的热烈讨论，内容涉及用户体验和自动驾驶汽车的未来。 此次扩展是自动驾驶汽车的一个重要里程碑，表明 Waymo 的技术已足够成熟，能够进入新的监管和地理市场。这可能加速全球自动驾驶网约车的普及，该市场在 2025 年估值 18.6 亿美元，预计到 2034 年将达到 72.3 亿美元。 Waymo 的服务已完成超过 2000 万次出行，乘客满意度达 93%，但扩展到多伦多这样的多雪城市引发了对其在恶劣冬季天气下性能的疑问。多伦多的公告还强调了创造就业机会，这可能是为了回应在其他城市（如波士顿）因担心失业而放缓采用的担忧。

hackernews · ChrisArchitect · Oct 16, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118981)

**背景**: Waymo 前身是谷歌自动驾驶汽车项目，运营着全球首个自动驾驶网约车服务，其车辆配备车顶传感器，无需人类驾驶员。自动驾驶网约车允许乘客通过应用召唤自动驾驶汽车，类似于 Uber 或 Lyft，但没有人类司机。多伦多将成为 Waymo 的新市场，目前该公司在美国多个城市运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://waymo.com/">Waymo - Self-Driving Cars - Autonomous Vehicles - Ride - Hail</a></li>
<li><a href="https://www.grandresearchstore.com/services/global-autonomous-ridehailing-service-market">Autonomous Ride - hailing Service Market Report | Size, Share 2026...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者分享了不同的体验：一些人称赞旧金山和奥斯汀的 Waymo 行程平稳且优于人类司机，而一位用户报告说 9 分钟的行程意外延长至 45 分钟，最后不得不改叫人类驾驶的 Uber。其他人对在东京看到 Waymo 表示兴奋，并提出了对失业以及波士顿等城市监管反对的担忧。

**标签**: `#autonomous vehicles`, `#Waymo`, `#transportation`, `#technology expansion`, `#Hacker News`

---

<a id="item-5"></a>
## [JPEG XL 与 AVIF：面向 Web 用例的深度对比](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

Jake Archibald 发表了一篇关于 JPEG XL 和 AVIF 在 Web 使用场景下的详细对比文章，涵盖编码速度、压缩效率和视觉质量。该文章引发了广泛的社区讨论，获得了 184 个赞和 142 条评论，探讨了实际应用中的权衡。 选择合适的图像格式直接影响 Web 性能、带宽成本和用户体验。随着 AVIF 获得浏览器支持而 JPEG XL 在采用上遇到困难，这一对比有助于开发者做出明智的格式选择。 对比指出，libjxl 的最高压缩努力极其缓慢（9–46 秒，是默认设置的 50–180 倍），而照片文件仅缩小 2–7%；AVIF 可生成小 10 倍的文件且质量良好，但可能会抹去高光等精细细节。社区成员指出，JPEG XL 编码器仍不成熟，更好的编码器可使无损文件再缩小 30–39%。

hackernews · farlight · Oct 16, 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**背景**: JPEG XL 是下一代图像格式，旨在以更高质量和更好压缩率超越 PNG、JPEG 2000、GIF 和 WebP，支持渐进式解码和无损 JPEG 重压缩。AVIF 是基于 AV1 视频编解码器的开放、免版税格式，文件比 JPEG 小 30–50%，并支持 HDR 和透明度。两者都旨在取代 Web 交付中的传统格式，但浏览器支持和编码器成熟度仍是关键差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://uploadcare.com/blog/avif-vs-jpeg-comparison/">AVIF vs JPEG XL vs JPEG : Best image format in 2026? | Uploadcare</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些人称赞 AVIF 的压缩效果并提供了最佳的 ffmpeg 设置，而另一些人则批评 AVIF 会抹去汽车高光等精细细节。多位评论者指出，JPEG XL 编码器目前并非最优，更好的编码器可实现无损文件缩小 30–39%，并且 libjxl 在高压缩努力下速度缓慢是由于 Butteraugli 感知度量优化循环所致。

**标签**: `#image-compression`, `#web-performance`, `#jpeg-xl`, `#avif`, `#frontend`

---

<a id="item-6"></a>
## [苹果 MLX 在四台 Mac Studio 上运行近万亿参数 Muse Spark Open 模型](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

苹果机器学习研究团队展示了如何使用最新版 MLX 分布式推理，在由四台 Mac Studio 组成的集群上运行 Meta 近万亿参数的 Muse Spark Open 模型，生成速度超过每秒 36 个 token。该发布显示该模型可以从单台配备最高 512GB 统一内存的 Mac Studio 扩展到多台机器协同运行。 这是一个值得注意的技术里程碑，因为它表明前沿级开源权重模型可以在消费级苹果硬件上本地提供服务，而不必依赖数据中心 GPU。这可能让注重隐私的本地推理对希望避免云成本和数据暴露的研究人员和开发者更加实用。 Muse Spark Open 是一个总参数 816B、激活参数 42B 的模型，上下文窗口为 100 万 token，而基准测试中每秒 36 token 的成绩是在 8192 token 上下文下测得的。社区成员还指出，该对比使用了 Meta 模型的 4 比特量化版本，而 Qwen 使用的是原生 BF16，这可能无法反映用户的实际配置。

hackernews · antipaul · Oct 16, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**背景**: MLX 是苹果为 Apple silicon 打造的开源机器学习数组框架，其分布式推理功能可以将单个模型的层拆分到多台 Mac 上，使它们共同参与每次前向传播。量化会降低模型权重的数值精度，从而减少内存占用并加速推理，但会以一定精度损失为代价。Muse Spark Open 是 Meta 于 2026 年 10 月根据 Muse Model License 发布的面向编码优化的开源权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/mlx-distributed-inference">Local and Distributed Large LLM Inference with MLX and RDMA ...</a></li>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta- models / Muse - Spark - Open -816B-A42B · Hugging Face</a></li>
<li><a href="https://localai.io/docs/features/mlx-distributed/">(experimental) MLX Distributed Inference - LocalAI</a></li>

</ul>
</details>

**社区讨论**: 评论者对该基准测试普遍持怀疑态度，认为将 4 比特的 Muse Spark Open 与原生 BF16 的 Qwen 对比并不公平，而且 8192 token 的上下文太短、不够实用。也有人分享了实际测试结果，例如单台 M5 Ultra 运行 DeepSeek 4.1 Flash 可达约每秒 45 token；还有评论调侃说 Meta 花数十亿美元做开源模型，而苹果则靠卖运行这些模型的硬件赚钱。

**标签**: `#Apple MLX`, `#distributed inference`, `#large language models`, `#Mac Studio`, `#model quantization`

---

<a id="item-7"></a>
## [Mercor 研究：美国 90%工作时间缺乏 AI 基准测试覆盖](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 8.0/10

Mercor 的 Labor Index 研究显示，美国 90%的工作时间花在现有 AI 基准测试几乎或完全没有覆盖的任务上，这使得人们很难判断 AI 模型在真实工作中的表现。该分析将 O*NET 职业任务与基准测试提示词进行映射，发现高薪职业的任务在基准中被显著过度代表。 这一发现挑战了“基准分数高就等于实用性强”的假设，可能推动 AI 实验室、评估机构和企业构建更能反映真实劳动分布的基准测试。如果评估持续偏向少数高薪任务，那么关于 AI 部署决策及其经济影响的判断就可能建立在不可靠的基础之上。 该研究基于 O*NET 任务数据和基准测试提示词数量，社区评论者指出，所谓“覆盖良好”有时仅意味着某个职业类别（如为父母提供育儿咨询）只有 13 条提示词。方法论还显示，即使在控制 AI 暴露度之后，与更大工资总额相关的任务在基准提示词中仍被过度代表。

hackernews · speckx · Oct 16, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**背景**: AI 基准测试是用于比较模型能力的标准化测试，例如 MMLU 或编程挑战，但它们往往依赖简化的代理任务，而非完整的真实工作流程。O*NET 是美国劳工部的数据库，收录了数百种职业的任务、技能和要求，因此常被用来研究 AI 与实际工作的对应关系。Mercor 是一家研究与数据公司，与前沿 AI 实验室合作开展人工评估和基准开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mercor.com/research/">Mercor Research | Frontier AI Training Data & Human Evaluation</a></li>
<li><a href="https://www.explainx.ai/blog/ai-benchmarks-complete-guide-2026">AI Benchmarks in 2026: The Complete Guide to MMLU... | explainx. ai</a></li>
<li><a href="https://carnegieendowment.org/research/2026/04/the-ai-labor-debate-three-views-on-the-future-of-work">The AI Labor Debate: Three Views on the Future of Work</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同这一差距确实存在，但对其解读存在分歧：有人引用“门卫谬误”指出，自动化一个显性任务可能破坏隐藏价值；也有人认为“覆盖良好”被宽松地等同于“有覆盖”。还有人批评该研究的叙事暗示 AI 正瞄准“好工作”，也有人调侃大部分工作时间其实都花在重复会议上。

**标签**: `#AI benchmarks`, `#labor economics`, `#AI evaluation`, `#future of work`, `#research`

---

<a id="item-8"></a>
## [OpenBSD 37 年老内核漏洞被利用获取 root 权限](https://calif.io/research/big-fish) ⭐️ 8.0/10

安全公司 Calif 于 2026 年 10 月 16 日发布了一个概念验证漏洞利用程序，它将 OpenBSD 内核中一个存在 37 年的整数溢出漏洞与一个释放后使用（use-after-free）漏洞串联起来，在 OpenBSD 7.9 上实现本地权限提升至 root。这两个漏洞目前均已被修补。 该漏洞利用表明，即使是被广泛认为最注重安全且经过严格审计的操作系统 OpenBSD，也可能隐藏着躲过数十年代码审查的深层内核漏洞。这凸显了以漏洞利用为导向的研究在发现自动化工具可能遗漏的漏洞类别方面的价值。 主要漏洞可追溯至约 37 年前的原始 BSD 源代码，该漏洞利用需要将其与另一个内核释放后使用（use-after-free）漏洞串联才能获取 root 权限。概念验证针对 OpenBSD 7.9，且两个漏洞均已修复，因此在已修补的系统上该漏洞利用不再有效。

hackernews · rs_rs_rs_rs_rs · Oct 16, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**背景**: OpenBSD 是由 Theo de Raadt 于 1995 年通过分叉 NetBSD 1.0 创建的一款注重安全的免费类 Unix 操作系统，以其严格的代码审计实践而闻名。内核漏洞是操作系统核心中的缺陷，可让攻击者提升权限，而整数溢出和释放后使用（use-after-free）错误是经典的漏洞类别，通常仅靠人工审查很难发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/37-year-old-kernel-openbsd-flaw/">37-Year-Old Kernel Flaw Exploited to Gain Root Access on ...</a></li>
<li><a href="https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html">Researchers Demonstrate OpenBSD Root Exploit Chaining 37-Year ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD">OpenBSD - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该漏洞在 1999 年 8 月 NetBSD 重写代码时被意外修复，还有用户称赞文章采用了 OpenBSD Release 风格的图形。一个关键讨论点是模糊测试或静态分析是否真能发现这类漏洞，言下之意是需要人类对漏洞利用原语进行推理。

**标签**: `#OpenBSD`, `#kernel`, `#security`, `#vulnerability`, `#exploit`

---

<a id="item-9"></a>
## [StarSkirmish Bench v0.2 测试大模型编写星际争霸机器人](https://starskirmish.com/bench/v0-2/) ⭐️ 8.0/10

StarSkirmish Bench 已更新至 v0.2 版本，评估来自 OpenAI、Anthropic、Google 和 Muse 的旗舰大语言模型通过编写代码来玩《星际争霸：母巢之战》的能力。每个模型在其实验室的第一方 CLI 工具中以最高推理设置运行，拥有一个小时的挂钟时间，且网络搜索和抓取工具被禁用。 该基准提供了一种新颖的方式，在复杂的长期编程任务上比较大模型智能体的能力，而非静态问答，并且其排名据称与一个独立的 9x9 围棋基准一致。这种跨领域的一致性可能强化这些评估衡量的是通用智能体技能而非特定任务特性的观点。 模型在各自的 CLI 工具中运行——Anthropic 使用 Claude Code，OpenAI 使用 Codex，Google 使用 Antigravity CLI，Meta 使用 Muse Code——除预装的 CLI 外没有互联网访问。大模型的得分反映其机器人在与一系列竞争性人类编写机器人和演示机器人对战中的胜率，不过一小时的限制可能使智能体难以匹敌最优秀的人工编写机器人。

hackernews · __cayenne__ · Oct 16, 14:18 · [社区讨论](https://news.ycombinator.com/item?id=50118688)

**背景**: 《星际争霸：母巢之战》是暴雪娱乐于 1998 年推出的即时战略资料片，玩家需要实时指挥军队、管理资源并战胜对手。StarSkirmish Bench 要求大语言模型编写控制星际争霸机器人的代码，然后让这些机器人与人类编写的对手对战以得出胜率分数。这与传统的大模型基准不同，因为它测试的是严格时间预算下的长期规划、编程和适应能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starskirmish.com/bench/">StarSkirmish Bench</a></li>
<li><a href="https://en.wikipedia.org/wiki/StarCraft:_Brood_War">StarCraft: Brood War</a></li>
<li><a href="https://ai.meta.com/muse/">Muse: Meta's personal AI agent, features & capabilities</a></li>

</ul>
</details>

**社区讨论**: 评论者认为该基准很有趣，有人指出其模型排名与一个独立的 9x9 围棋基准一致，表明智能体能力排序具有一致性。其他人则提出了更深层的问题：智能体编写的机器人是否学到了新东西，是否只是模仿人类编写的机器人代码，以及它们在多大程度上依赖固定技术而非实验反馈。

**标签**: `#LLM benchmarking`, `#StarCraft`, `#AI agents`, `#code generation`, `#game AI`

---

<a id="item-10"></a>
## [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](https://huggingface.co/stepfun-ai/Step-5-Preview) ⭐️ 8.0/10

阶跃星辰在 Hugging Face 发布旗舰模型 Step 5 Preview，采用稀疏 MoE 架构，总参数 6000 亿、激活参数 270 亿，支持最高 100 万 token 上下文，并可接收文本、图像和视频输入。该模型在软件工程、长周期智能体执行和专业知识任务上表现领先，尤其擅长金融场景。 这是阶跃星辰推出的重要智能体旗舰模型，其稀疏 MoE 设计与 100 万 token 上下文对构建长周期智能体和软件工程工具的 AI/ML 从业者高度相关。其在金融领域的突出表现也表明垂直化、面向智能体的 LLM 竞争正在加剧。 该模型可通过 OpenAI 兼容 API 配合 vLLM 或 SGLang 部署，并采用 StepFun Model License 1.0 许可。其 6000 亿总参数中仅激活 270 亿，体现了稀疏激活策略，使推理成本远低于同等规模的稠密模型。

telegram · zaihuapd · Oct 16, 06:36

**背景**: 混合专家（MoE）是一种架构，其中路由网络针对每个输入只激活部分专家，使模型能够扩展到远多于此前的参数量而计算量不会成比例增加。长周期智能体任务要求 AI 在大量相互依赖的步骤和上下文窗口中持续进行规划与目标导向执行。vLLM 和 SGLang 是流行的开源推理引擎，用于在生产环境中高效服务大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://atoms.dev/insights/long-horizon-agent-tasks-foundations-methodologies-applications-and-future-directions/ff6b00ebde5a4888a3526497667f0f89">Long - Horizon Agent Tasks : Foundations, Methodologies...</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm -project/ vllm : A high-throughput and memory-efficient...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#AI Agents`, `#Multimodal`, `#Model Release`

---

<a id="item-11"></a>
## [中国拟对 40 项人工智能、生物医药和光伏技术实施临时出口登记](https://aqygzj.mofcom.gov.cn/flzc/gzjgfxwj/art/2026/art_c99f95ca0cd043829ac9991495fc283c.html) ⭐️ 8.0/10

2026 年 10 月 16 日，中国商务部与科技部联合发布 2026 年第 48 号公告，拟将 40 项技术列入《中国禁止出口限制出口技术目录》，其中包括 23 项人工智能技术（大模型、智能体、算力集群、信息处理）、5 项生物医药技术（细胞和基因治疗、小核酸药、病原微生物）以及 12 项光伏技术（多晶硅、硅片、电池制造）。在公开征求意见期间及修订后目录正式生效前，相关技术出口须通过商务主管部门办理临时出口登记。 这是一项重大监管变化，可能重塑人工智能、生物医药和光伏行业的全球合作与供应链，影响依赖中国技术的跨国公司、研究机构和投资者。此举表明中国在全球科技竞争加剧背景下保护战略技术的意图，并可能引发其他国家的对等措施。 已通过开源发布或学术论文发表等方式进入公共领域的技术不纳入管理范围；不涉及所有权转让的对外授权模式可适用自动许可等便利措施。管理范围还涵盖承载相关技术的关键和核心设备，且临时登记要求自 2026 年 10 月 16 日起至修订后目录正式生效前持续适用。

telegram · zaihuapd · Oct 16, 09:12

**背景**: 《中国禁止出口限制出口技术目录》是根据《中华人民共和国对外贸易法》和《中华人民共和国技术进出口管理条例》维护的清单，最近一次更新是在 2023 年 12 月，列明了禁止或限制出口的技术。出口管制是中美全球科技竞争的关键工具，美国已实施自己的人工智能扩散规则和芯片出口限制。此次拟新增技术反映出对人工智能、生物医药和可再生能源领域国家安全和战略技术外流的担忧日益加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mofcom.gov.cn:8443/xwfb/xwfyrth/art/2026/art_d7661dbf62794345a221404f82a25959.html">商务部新闻发言人就修订《中国禁止出口限制出口技术目录》答记者问</a></li>
<li><a href="https://eyeon.ai/zh/f/2992">中国商务部/科技部公告2026年第48号：拟对23项人工智能技术实施出口管...</a></li>
<li><a href="https://aqygzj.mofcom.gov.cn/flzc/gzjgfxwj/art/2026/art_c99f95ca0cd043829ac9991495fc283c.html">商务部 科技部公告2026年第48号 就修订《中国禁止出口限制出口技术目...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些人认为这些措施对保护战略技术和国家安全是必要的，而另一些人则担心会对创新、国际合作和生物医药对外授权交易产生负面影响。分析人士指出，对开源和已发表研究的豁免可能会减轻对人工智能的冲击，但对合规负担和其他国家潜在报复的担忧依然存在。

**标签**: `#export controls`, `#AI policy`, `#biotech regulation`, `#solar technology`, `#China tech policy`

---

<a id="item-12"></a>
## [苹果首款折叠屏 iPhone Duo 一分钟售罄，股价盘前涨超 2%](https://api3.cls.cn/share/article/2507193?os=android&amp;sv=8.8.4&amp;app=cailianpress) ⭐️ 8.0/10

苹果首款折叠屏手机 iPhone Duo 正式开售仅一分钟，全型号库存便迅速售空，带动苹果美股盘前一度涨超 2%，开盘有望创下历史新高。 瞬间售罄表明消费者对苹果进军折叠屏品类需求强劲，这可能重塑长期由三星和中国安卓厂商主导的折叠屏市场，并为苹果带来新的高端产品增长点。 iPhone Duo 配备 7.6 英寸内屏，比 iPhone 18 Pro Max 大 50%，外屏面积超过 iPhone 18 Pro 屏幕的 90%，并采用可减少眩光的纳米纹理工艺；其起售价预计约为 2000 美元，搭载基于台积电 2nm 工艺的 A20 芯片。

telegram · zaihuapd · Oct 16, 12:45

**背景**: 折叠屏手机通过柔性屏幕和铰链让单台设备展开成平板大小的屏幕，这一品类多年来由三星和多家中国品牌主导，而苹果一直未涉足。苹果在 2026 年 9 月的发布会上正式推出 iPhone Duo，称其为自初代 iPhone 以来最具变革性的变化。盘前交易指美股正式开盘前的股票交易时段，投资者会在此时对重大新闻作出反应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/">Apple unveils iPhone Duo</a></li>
<li><a href="https://www.cnet.com/tech/mobile/who-is-iphone-duo-apple-foldable-for/">The $2,000 Duo: Who Is Apple's First Folding iPhone Actually ...</a></li>
<li><a href="https://www.appleheadlines.com/iphone-fold/">iPhone Fold: Release Date, Price, Specs & Everything We Know ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#foldable phone`, `#iPhone Duo`, `#market reaction`, `#consumer electronics`

---

<a id="item-13"></a>
## [Anthropic IPO 估值预期下调至 1.5 万亿美元](https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/) ⭐️ 8.0/10

部分投资者将 Anthropic 的 IPO 估值预期从 2 万亿美元下调至约 1.5 万亿美元，尽管该公司第三季度营收达 168 亿美元，环比增长 45%，并实现经调整后盈利和季度现金流转正。 此次下调表明公开市场投资者正在对 AI 公司的估值施加更严格的审视，更看重收入持续性、毛利率和资本效率，而非单纯的收入增长，这可能给智谱、MiniMax、Kimi 和 DeepSeek 等即将或考虑上市的 AI 公司带来估值压力。 此次估值下调反映了增速放缓、AI 模型价格竞争加剧以及算力投入成本上升；值得注意的是，Anthropic 的 IPO 招股书中近三分之一篇幅用于风险因素披露，包括警告其 AI 可能带来生存性风险，并披露了 420 亿美元的净亏损。

telegram · zaihuapd · Oct 16, 15:46

**背景**: Anthropic 是一家以 Claude 系列大语言模型闻名的 AI 公司，目前正在筹备首次公开募股（IPO）。IPO 估值反映的是投资者认为该公司在公开上市时的价值，随着新的财务和市场信息出现，这一预期可能发生变化。AI 公司需要承担训练和运行模型所需算力的高昂成本，而模型提供商之间的竞争又在压低 API 价格，使收入增长与盈利能力之间形成张力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/anthropic-ipo-2026-explained-from-965-billion-possible-2-pvgkc">Anthropic IPO 2026 Explained, From $965 Billion to a Possible...</a></li>
<li><a href="https://www.euronews.com/2026/09/29/anthropic-ipo-filing-warns-ai-may-pose-existential-risks-to-humanity">Anthropic IPO filing warns AI may pose 'existential risks to... | Euronews</a></li>
<li><a href="https://www.ibm.com/think/insights/ai-economics-compute-cost">The hidden costs of AI: How generative models are reshaping ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI valuations`, `#AI industry`, `#Reuters`

---