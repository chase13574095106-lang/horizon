---
layout: default
title: "Horizon Summary: 2026-10-01 (ZH)"
date: 2026-10-01
lang: zh
---

> From 26 items, 6 important content pieces were selected

---

1. [谷歌发布旗舰 AI 模型 Gemini 4 Argon](#item-1) ⭐️ 9.0/10
2. [DeepSeek 开源华为昇腾基础组件](#item-2) ⭐️ 8.0/10
3. [特朗普与六大 AI 巨头签署自愿性 AI 安全协议](#item-3) ⭐️ 8.0/10
4. [Cloudflare 宣布进军公共证书颁发机构市场](#item-4) ⭐️ 8.0/10
5. [Kimi K3 接入 OpenAI Codex 企业通道，成首个进入其付费结算体系的中国模型](#item-5) ⭐️ 8.0/10
6. [Reddit 将停用 RSS 订阅与公开 API 访问](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布旗舰 AI 模型 Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 9.0/10

谷歌发布了新一代旗舰 AI 模型 Gemini 4 Argon，在编程、推理和多模态能力方面表现出色，其介绍性定价为每百万输入 token 2 美元、每百万输出 token 10 美元。该模型目前正与早期测试者一起迭代完善，之后将尽快面向开发者、企业和消费者开放。 此次发布加剧了前沿实验室之间持续的 AI 模型交替领先竞赛，挑战了 AI 是赢家通吃领域的观点，表明竞争格局在超大规模云厂商、新型云厂商和初创公司之间更加分散。这直接影响到选择 AI 提供商的开发者和企业，强调了模型和提供商可替换策略的必要性。 Gemini 4 Argon（High）在智能水平上处于领先模型之列，与同类模型相比价格合理，缓存输入 token 的价格为输入 token 价格的 5%。在 Vals 任务集上，它比 Gemini 3.8 Flash 落后约 14 分，但这一差距不一定适用于其他任务。

hackernews · bradleyg223 · Sep 30, 20:04 · [社区讨论](https://news.ycombinator.com/item?id=49913571)

**背景**: Gemini 是谷歌的多模态 AI 模型系列，Argon 是最新的旗舰迭代版本。AI 行业已见证多个实验室的快速模型发布，性能和价格比较由 Artificial Analysis 等平台跟踪。“交替领先”一词指的是各实验室轮流发布超越彼此能力的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-argon">Gemini 4 Argon ( high ) - Intelligence , Performance & Price Analysis</a></li>
<li><a href="https://news.ycombinator.com/item?id=49914236">Gemini 4 Argon ( High ): Intelligence , Performance and Price Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者强调了 Gemini 的实际能力，一位用户描述了 Gemini 3.8 Flash 如何逆向工程 GPU 驱动以修复 ROCm 问题。其他人则讨论了竞争格局，指出交替领先仍在继续，并挑战了 Dario Amodei 的赢家通吃理论，同时一些人批评了发布延迟，并建议保持模型可替换。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Model Release`

---

<a id="item-2"></a>
## [DeepSeek 开源华为昇腾基础组件](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

2026 年 9 月 30 日，DeepSeek 开源了面向华为昇腾平台的一整套基础组件，涵盖 TileLang 高级语言编译工具链、计算库和分布式通信库，与其英伟达平台组件一一对应。此次发布包括 DeepGEMM Ascend、DeepEP Ascend、TileKernels、FlashMLA 和 DeepSelect，DeepSeek 称相关组件在多项测试中性能接近硬件上限，并确认正与华为推进昇腾 950 的 128 卡超节点方案。 这是一次全栈软件发布，直接挑战英伟达 CUDA 生态的主导地位，为昇腾用户提供了与其英伟达栈对应的生产级编译器、算子库和通信库。它降低了在国产硬件上运行 DeepSeek 系列及其他大模型的门槛，而与华为合作推进 128 卡超节点也表明华为的规模化路线正在配套严肃的软件投入。 DeepGEMM Ascend 是 DeepGEMM 向华为昇腾平台的移植版本，与原版完全 API 兼容，支持 BF16、FP8、FP4 的 GEMM 以及 MQA logits，因此基于 DeepGEMM 接口构建的现有代码可以保持相同的开发流程。TileLang 则是构建在 Apache TVM 之上的 Python 风格 DSL，让开发者能够以高层方式编写基于 tile 的算子，同时不牺牲底层控制能力。

telegram · zaihuapd · Sep 30, 03:09

**背景**: 华为昇腾 NPU 是中国领先的非英伟达 AI 加速器，昇腾 950 搭配华为的“超节点”架构，通过连接数千颗芯片（Atlas 950 超节点支持 8,192 颗昇腾 950 DT 芯片）以系统级规模弥补单卡相对英伟达 B200/B300 的差距。DeepSeek 的模型被认为运行在 Atlas 950 超节点基础设施之上，使其成为该平台最重要的软件合作伙伴之一。DeepGEMM 是 DeepSeek 面向英伟达 GPU 的高性能 GEMM 算子库，TileLang 则是用于编写高效 GPU/NPU 算子的基于 tile 的算子编程语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/ DeepGEMM - Ascend : DeepGEMM - Ascend ...</a></li>
<li><a href="https://tilelang.com/">TileLang 0.1.14 documentation</a></li>
<li><a href="https://www.spheron.network/blog/huawei-ascend-950-vs-nvidia-b300-b200-llm-inference-2026/">Huawei Ascend 950 vs NVIDIA B300 and B200 for... | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Huawei Ascend`, `#AI infrastructure`, `#open source`, `#distributed computing`

---

<a id="item-3"></a>
## [特朗普与六大 AI 巨头签署自愿性 AI 安全协议](https://t.me/zaihuapd/44123) ⭐️ 8.0/10

当地时间 9 月 29 日，美国总统特朗普与谷歌、Anthropic、Meta、OpenAI、xAI 和英伟达的掌门人共同签署了一份一页纸的 AI 协议，特朗普将其发布在 Truth Social 上，并称该文件具有“道义约束力”。协议要求企业建立四层控制机制：配合外部审计机构独立评估 AI 管控系统、设立董事会独立委员会监督，并在模型训练和部署期间围绕网络安全、生物和化学威胁监控 AI 能力与对齐情况。 这是美国主要前沿 AI 企业与白宫首次共同承诺采用统一的监督框架，标志着行业走向自愿性自我治理而非强制性监管。这可能影响全球 AI 安全的审计与治理方式，但由于缺乏法律强制力，其实际效果仍存疑问。 该协议仅一页纸，没有法律执行机制，依赖“道义约束力”和自愿遵守。它复制了金融审计的结构——内部控制、外部核查和董事会监督——但缺少使金融审计对外部有用的信息披露规则。

telegram · zaihuapd · Sep 30, 05:15

**背景**: AI 对齐是 AI 安全的一个子领域，旨在引导 AI 系统朝着预期目标、偏好或伦理原则发展，而对齐失败的系统可能追求非预期目标。随着大语言模型等先进模型能力增强，研究人员和高管警告了包括策略性欺骗和权力寻求在内的风险。新协议试图通过类似金融和航空等受监管行业采用的治理机制来应对这些风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://shattered.io/white-house-ai-accord-outside-audits-explicit-2026/">White House AI Accord Makes Outside Audits Explicit</a></li>
<li><a href="https://forklog.com/en/ai-companies-agree-to-voluntary-model-oversight/">AI Companies Agree to Voluntary Model Oversight | ForkLog</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Governance`, `#Policy`, `#Tech Industry`, `#Regulation`

---

<a id="item-4"></a>
## [Cloudflare 宣布进军公共证书颁发机构市场](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare 宣布计划成为公共证书颁发机构，已申请加入 Chrome、Apple、Microsoft 和 Mozilla 的根证书计划，并与 GlobalSign 签署协议收购一个被广泛信任的根证书。该公司目前尚未开始签发证书，但计划优先支持基于 ACME 的自动化签发和续期，并计划在 2027 年第一季度签发生产级默克尔树证书（MTC），以服务于后量子互联网。 Cloudflare 进入公共证书颁发机构市场可能会颠覆长期由 DigiCert、Sectigo 和 Let's Encrypt 等少数玩家主导的证书颁发机构格局。作为主要的 CDN 和互联网基础设施提供商，Cloudflare 处于有利地位，可以推动 ACME 优先的自动化和后量子就绪，从而可能加速全行业对更高效证书技术的采用。 Cloudflare 计划在 2027 年第一季度签发生产级默克尔树证书（MTC），这是一种利用默克尔树大幅减少 TLS 握手期间交换数据量的新型证书格式。该公司尚未开始签发证书，其从 GlobalSign 收购根证书的交易仍需获得监管批准和根证书计划的接受。

telegram · zaihuapd · Sep 30, 06:26

**背景**: 证书颁发机构（CA）是受信任的实体，负责签发用于验证身份和启用网络加密连接（HTTPS）的数字证书。要被浏览器信任，CA 必须被纳入由 Google、Apple、Microsoft 和 Mozilla 等公司维护的根证书计划。ACME（自动证书管理环境）是一种 IETF 标准协议，用于自动化域名验证证书的签发和续期，被 Let's Encrypt 等服务广泛使用。默克尔树证书（MTC）是一种提议的证书格式，利用默克尔树压缩证书数据，使其更小、更高效，这对于后量子密码学尤为重要，因为后量子证书的体积要大得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sectigo.com/blog/what-are-merkle-tree-certificates-mtcs">What are Merkle Tree Certificates (MTCs)? | Sectigo® Official</a></li>
<li><a href="https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/">What is post - quantum cryptography (PQC)?</a></li>
<li><a href="https://aawjq20.buzz/p/https/docs.aws.amazon.com/acm/latest/userguide/acm-acme.html">ACME certificate automation - AWS Certificate Manager</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Certificate Authority`, `#PKI`, `#Post-Quantum`, `#ACME`

---

<a id="item-5"></a>
## [Kimi K3 接入 OpenAI Codex 企业通道，成首个进入其付费结算体系的中国模型](https://36kr.com/newsflashes/4005691489112198) ⭐️ 8.0/10

美国 AI 基础设施公司 Baseten 宣布，企业用户现可在 OpenAI 的编程工具 Codex 中使用 Kimi K3，相关调用费用直接计入企业已有的 OpenAI 采购承诺额度，无需新增供应商采购流程。这使 Kimi K3 成为首个进入 OpenAI 企业主流付费结算通道的中国开源模型。 这是企业 AI 采购格局的一次显著变化：中国开源模型如今可通过美国厂商既有的企业结算通道触达客户，大幅降低了已承诺采购 OpenAI 的企业的采用门槛。这标志着企业 AI 技术栈中跨厂商集成趋势的增强，并可能改变企业评估非美国模型的决策方式。 Kimi K3 是月之暗面（Moonshot AI）的旗舰开源权重模型，采用 2.8 万亿参数的混合专家（MoE）架构，每个 token 仅路由至 896 个专家中的 16 个，定位于复杂编程与长周期智能体工作流。该集成由 Baseten 的推理基础设施承载，费用通过企业已有的 OpenAI 采购承诺结算，而非另签合同。

telegram · zaihuapd · Sep 30, 11:23

**背景**: OpenAI 的 Codex 是一款面向多智能体软件工程工作流的 AI 编程助手，企业通常通过预先谈定的采购承诺额度来使用此类工具。Baseten 是一家成立于 2019 年的美国 AI 基础设施公司，提供无服务器推理平台，用于在生产环境中部署和扩展模型。由月之暗面发布的 Kimi K3 是迄今规模最大的开源权重模型，并已在 Hugging Face、OpenRouter 等平台上线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baseten.co/">Inference Platform: Deploy AI models in production | Baseten</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://k3-kimi.com/">Kimi K 3 : 2.8T Open-Weight Model — Benchmarks, Pricing & Guides</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise`, `#OpenAI`, `#Kimi K3`, `#model integration`

---

<a id="item-6"></a>
## [Reddit 将停用 RSS 订阅与公开 API 访问](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit 宣布将于 11 月 13 日停止 RSS 订阅支持，并将在 2027 年 3 月前关闭公开 API 访问，理由是 RSS 已成为大规模抓取和自动化滥用（尤其是 AI 机器人）的常见渠道。第三方应用和机器人开发者必须在 2027 年 1 月 12 日前完成注册，否则将被移除 API 访问权限，同时官方建议版主改用 Discord Relay。 这是一次影响深远的平台政策变动，波及依赖 Reddit 内容开放访问的开发者、研究人员、版主和普通用户，并通过移除标准化的机器可读订阅源进一步侵蚀开放网络。此举对 AI 训练数据管道以及建立在 Reddit 公开 API 之上的第三方生态也具有重大影响。 RSS 订阅将于 11 月 13 日停止，公开 API 访问将在 2027 年 3 月前结束，第三方开发者必须在 2027 年 1 月 12 日前完成注册才能保留访问权限。Reddit 引导版主改用 Discord Relay 来替代基于订阅源的工作流，但并未提供注册流程或 Relay 功能的技术细节。

telegram · zaihuapd · Oct 1, 00:27

**背景**: RSS（Really Simple Syndication，简易信息聚合）是一种基于 XML 的标准化网络订阅格式，让用户和应用能在单一聚合器中追踪网站更新，自 2000 年代初以来一直是开放网络的核心组成部分。Reddit 的公开 API 同样允许第三方客户端、机器人和研究工具以编程方式读取帖子和评论。Reddit 约 10% 的收入来自与 Google 和 OpenAI 的数据授权协议，这些协议将于 2027 年到期，因此公司有强烈动机去控制其内容的访问与抓取方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSS_feed">RSS feed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reddit_Public_Access_Network">Reddit Public Access Network</a></li>
<li><a href="https://publicapis.io/reddit-api">Reddit API — API Key, Docs & Examples | PublicAPIs.io</a></li>

</ul>
</details>

**标签**: `#Reddit`, `#API`, `#RSS`, `#AI scraping`, `#platform policy`

---