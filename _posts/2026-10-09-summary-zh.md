---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> From 28 items, 7 important content pieces were selected

---

1. [OpenAI 为 GPT-6.1 Sol API 新增 Ultrafast 模式](#item-1) ⭐️ 9.0/10
2. [中国科学家研制成功世界首台核光钟](#item-2) ⭐️ 8.0/10
3. [Stripe 同意收购 OpenRouter，覆盖 400 多个模型的 AI 网关](#item-3) ⭐️ 8.0/10
4. [Manus 2.0 正式发布，推出自研 Cascade 框架与全新应用 Cue](#item-4) ⭐️ 8.0/10
5. [Mistral 发布 1 万亿参数开源模型 Mistral Large 4](#item-5) ⭐️ 8.0/10
6. [美政府以欺诈为由暂停微软绿卡申请资格](#item-6) ⭐️ 8.0/10
7. [SpaceX 拟收购全美低频段频谱许可证](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 为 GPT-6.1 Sol API 新增 Ultrafast 模式](https://developers.openai.com/api/docs/changelog) ⭐️ 9.0/10

OpenAI 在 Responses API（v1/responses）中为 GPT-6.1 Sol 推出了 Ultrafast 服务层级，生成速度相比 Standard 最高约提升 8 倍。该模式面向所有 API 用户开放，价格为 Standard 的 6 倍，短上下文定价约为每百万 token 输入 12 美元、缓存输入 0.60 美元、输出 60 美元。 这为构建延迟敏感型或智能体（agentic）应用的开发者提供了一种无需更换模型、以成本换速度的途径，有望显著提升实时交互和多次工具调用工作流的响应速度。不过 6 倍的价格溢价可能会把采用范围限制在那些确实值得为降低延迟付费的场景中。 Ultrafast 被描述为 OpenAI API 中最快的服务层级，已广泛适用于 GPT-6 Astra 和 GPT-6.1 Sol，并对 GPT-5.6 Sol 提供预览访问。OpenAI 强烈建议使用 WebSockets，尤其是对需要快速连续发起大量工具调用的智能体应用，因为若没有持久连接，网络开销可能会削弱延迟收益。

telegram · zaihuapd · Oct 9, 00:00

**背景**: Responses API（v1/responses）是 OpenAI 较新的模型调用端点，支持内置工具、状态管理和流式输出，被视为对旧版 Chat Completions 接口的演进。Flex、Standard、Priority、Batch 等服务层级让开发者可以根据成本与延迟之间的权衡来调度流量。Ultrafast 是最新且最快的层级，面向把生成速度放在首位的工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/ultrafast-mode">Ultrafast mode | OpenAI API</a></li>
<li><a href="https://www.latent.space/p/ainews-openai-devday-2026-dots-61">[AINews] OpenAI DevDay 2026: Dots, 6 . 1 Sol , Ultrafast , Decisions...</a></li>
<li><a href="https://apidog.com/blog/openai-responses-api/">How to use the OpenAI Responses API</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API`, `#GPT-6.1`, `#Ultrafast`, `#LLM`

---

<a id="item-2"></a>
## [中国科学家研制成功世界首台核光钟](https://www.nature.com/articles/s41586-026-11122-1) ⭐️ 8.0/10

清华大学研究团队利用自主研制的 148 纳米连续波真空紫外激光和掺钍-229 氟化钙晶体，在国际上率先研制出核光钟并实现稳定运行，成果发表于《自然》。 这是核光钟的首次成功实现，有望成为新一代时间频率基准，并服务于卫星导航、深空探测等高精度计时场景，同时为检验基本物理常数是否变化等基础物理研究开辟新前沿。 该时钟以钍-229 原子核中能量极低、寿命极长的同质异能态作为计时基准，需要波长约 148 纳米的真空紫外光来激发。团队通过将连续波激光稳定到该核跃迁上实现了稳定运行，而掺钍氟化钙晶体为这种光谱学提供了固态平台。

telegram · zaihuapd · Oct 8, 05:19

**背景**: 支撑 GPS 和全球授时的原子钟，以原子中电子能级之间的跃迁作为计时基准。核光钟则改用原子核内部的量子态作为基准，这些核态对外界干扰的敏感度远低于电子态，因此有望实现更高的精度和稳定性。钍-229 之所以特别适合，是因为它拥有一个能量异常低的激发态，可以用真空紫外激光来激发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11084-4">A thorium-229 optical nuclear clock with feedback loop | Nature</a></li>
<li><a href="https://thoriumclock.eu/">Webpage of the Thorium Nuclear clock research project</a></li>
<li><a href="https://physics.aps.org/articles/v19/19">Physics - A Laser Built for Nuclear Timekeeping</a></li>

</ul>
</details>

**标签**: `#nuclear clock`, `#thorium-229`, `#timekeeping`, `#physics`, `#Nature`

---

<a id="item-3"></a>
## [Stripe 同意收购 OpenRouter，覆盖 400 多个模型的 AI 网关](https://t.me/zaihuapd/44275) ⭐️ 8.0/10

Stripe 于 2026 年 8 月 19 日宣布已同意收购 AI 模型网关与路由平台 OpenRouter，该平台可根据任务复杂度、价格、速度和可靠性，在 80 多家提供商的 400 多个模型之间动态分配请求。有报道称这笔交易金额约为 75 亿美元，但 Stripe 官方并未披露具体价格。 这笔收购让一家大型支付公司站到了 AI 模型访问与计费的核心位置，可能重塑开发者和企业在多个提供商之间路由、计量和支付推理费用的方式。这也表明 AI 基础设施层的整合仍在继续，网关正成为控制成本和供应商管理的关键战略节点。 OpenRouter 的核心价值在于提供统一的 API 端点，屏蔽了数十家提供商的集成差异，从而实现故障转移、成本优化和基于质量的路由。据报道约 75 亿美元的收购价对一家路由层公司而言相当高，且交易仍需满足交割条件，因此目前尚未公布任何技术或产品层面的变动。

telegram · zaihuapd · Oct 8, 05:52

**背景**: OpenRouter 是一个 AI 模型网关，有时也被称为 LLM 路由器，位于应用程序与众多模型提供商之间。开发者无需分别对接各家厂商的 API，只需向一个端点发送请求，由 OpenRouter 决定使用哪个底层模型。Stripe 以可编程支付服务闻名，收购 OpenRouter 将其基础设施版图延伸到了 AI 用量的计量与计费环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter">Stripe agrees to acquire OpenRouter to help businesses ...</a></li>
<li><a href="https://techcrunch.com/2026/08/19/stripe-didnt-really-buy-openrouter-because-of-the-singularity/">Stripe didn't really buy OpenRouter because of the ...</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Acquisition`, `#OpenRouter`, `#Stripe`, `#Model Routing`

---

<a id="item-4"></a>
## [Manus 2.0 正式发布，推出自研 Cascade 框架与全新应用 Cue](https://t.me/zaihuapd/44276) ⭐️ 8.0/10

Manus 2.0 于 2026 年 9 月 28 日正式发布，带来自研 Agent 框架 Cascade、云电脑以及事件触发自动化。据官方测试，其 Token 消耗减少 23.2%，任务完成时间缩短 28.2%，运行成本降低 32%。 这是广受欢迎的 AI Agent 平台的一次重大版本更新，显著的效率提升可能重塑开发者和企业部署自主智能体的方式。全新的 Cascade 框架和 Cue 应用有望加速从单一任务 AI Agent 向持续运行、多能力工作空间的转变。 桌面应用升级为 Manus Studio，新增视频编辑器、游戏开发工具和 Computer Use 功能。独立应用 Cue 可为个人 Agent 配置邮箱、电话、钱包和电脑，目前凭邀请码免费体验。

telegram · zaihuapd · Oct 8, 06:43

**背景**: Manus 是由 Butterfly Effect 开发的自主 AI Agent，该公司在中国创立、总部位于新加坡。它能处理构建自定义网页工具、内容本地化、数据清洗和自动化工作流等任务，并采用积分制收费。Cascade 是 Manus 自研的 Agent 框架，能让项目保持轻量，仅在需要时引入专门能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://manus.im/blog/introducing-manus-2-0">Introducing Manus 2.0</a></li>
<li><a href="https://letsdatascience.com/news/manus-introduces-manus-20-with-cascade-architecture-and-new-53ecf751">Manus Introduces Manus 2.0 With Cascade Architecture and New ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent)</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Manus`, `#agent framework`, `#automation`, `#cloud computing`

---

<a id="item-5"></a>
## [Mistral 发布 1 万亿参数开源模型 Mistral Large 4](https://t.me/zaihuapd/44279) ⭐️ 8.0/10

10 月 6 日，法国 AI 公司 Mistral 发布了 Mistral Large 4（昵称“le Chonk”），这是一个拥有 1 万亿参数的模型，被其称为全球最强开源模型之一。该模型目前面向开发者、网络安全负责人及政府机构开放预览，计划于本月晚些时候扩大开放范围。 一家欧洲实验室推出 1 万亿参数的开源权重模型，将加剧与美国和中国前沿实验室的竞争，而其聚焦网络安全、编程、制造和金融领域，也显示 Mistral 正进军企业和政府市场。如果开源权重如期发布，它可能成为可公开下载的最大模型之一。 Mistral 称该模型使用 4000 个英伟达 Grace Blackwell GPU 训练了两个月，它原生支持多模态，并采用总参数达 1 万亿的混合专家（MoE）架构。Mistral 承认其在编程等领域仍落后于前沿模型，开源权重预计于 10 月底发布。

telegram · zaihuapd · Oct 8, 10:08

**背景**: Mistral AI 是一家法国初创公司，以发布任何人都能下载运行的开源权重大型语言模型而闻名，这与 OpenAI 的 GPT-4 等闭源模型形成对比。参数规模大致衡量模型的体量和能力，而万亿参数模型属于迄今最大的模型之列。英伟达的 Grace Blackwell 是其最新 GPU 平台，将 Blackwell GPU 与基于 Arm 架构的 Grace CPU 结合，专为大规模 AI 训练和推理设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/mistral-large-4/">Introducing Mistral Large 4 | Mistral</a></li>
<li><a href="https://officechai.com/ai/mistral-large-4-le-chonk/">Mistral Releases Mistral Large 4 ( Le Chonk ), Says It's The Top Open...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Mistral`, `#large language models`, `#open source`, `#AI`, `#model release`

---

<a id="item-6"></a>
## [美政府以欺诈为由暂停微软绿卡申请资格](https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea) ⭐️ 8.0/10

特朗普政府宣布暂停微软参与外籍劳工绿卡申请项目，指控其存在欺诈行为。副总统万斯在新闻发布会上表示，微软去年裁掉 6000 名美国员工，却获得了 6300 份 H-1B 签证和近 3000 张绿卡，称其为“利用该系统最多的公司”。 此举标志着特朗普政府对企业移民行为的打击显著升级，可能为其他科技巨头树立先例，影响它们雇佣外籍人才的方式。这可能会打乱微软为现有及未来员工申请绿卡的能力，并促使其他科技公司重新评估其移民策略。 万斯指责微软先发布虚假招聘广告以证明招不到美国工人，然后用外籍劳工替换美国员工，还点名哈佛、耶鲁、MIT 等九所大学涉嫌滥用 J-1 签证项目。微软尚未对这些指控作出回应。

telegram · zaihuapd · Oct 9, 00:00

**背景**: H-1B 签证是一种临时非移民签证，允许美国公司雇佣从事专业职业的高技能外籍员工。绿卡劳工证（PERM）流程要求雇主在担保外籍员工申请 EB-2 或 EB-3 就业类绿卡前，必须证明没有合格的美国工人可胜任该永久职位。J-1 签证是用于工作与学习相结合的文化交流项目的交流访问学者签证。此次暂停意味着微软不能再提交 PERM 申请，而这是为员工担保绿卡的第一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dol.gov/agencies/eta/foreign-labor/programs/permanent">Permanent Labor Certification - U.S. Department of Labor</a></li>
<li><a href="https://greencardtracker.com/articles/perm-labor-certification">PERM Labor Certification: Step-by-Step Employer Guide (2026)</a></li>
<li><a href="https://www.aljazeera.com/economy/2025/1/16/bannon-vs-musk-how-trumps-u-turn-on-h-1b-visas-has-split-maga">Bannon vs Musk: How Trump’s U-turn on H - 1 B visas has... | Al Jazeera</a></li>

</ul>
</details>

**标签**: `#immigration`, `#H-1B`, `#Microsoft`, `#policy`, `#tech industry`

---

<a id="item-7"></a>
## [SpaceX 拟收购全美低频段频谱许可证](https://x.com/SpaceX/status/2108291133025698301) ⭐️ 8.0/10

SpaceX 宣布达成协议，拟收购一套覆盖全美的低频段频谱许可证组合，公司称这将为 Starlink 成为美国主要移动运营商铺平道路。结合其 Gen2 星座，SpaceX 声称 Starlink Mobile 可以让美国民众无论身处何地都能获得高速移动宽带。 这是一项重大战略举措，可能颠覆美国电信行业，使 Starlink 从卫星互联网提供商转变为与 AT&T、Verizon 和 T-Mobile 竞争的全方位移动运营商。低频段频谱因覆盖广、穿透力强而备受青睐，是实现全国性手机直连卫星服务的关键。 低频段频谱传输距离远、穿透建筑能力强，但容量低于中频段或高频段，因此通常用于广覆盖而非峰值速率。SpaceX 规划的 Gen2 星座包含近 3 万颗卫星，其中三分之二位于 450 公里以下的超低地球轨道，将支撑手机直连卫星服务。

telegram · zaihuapd · Oct 9, 01:04

**背景**: 低频段频谱通常指 1 GHz 以下的无线电频率，运营商用它实现大范围移动覆盖，因为信号传输远且能穿透墙壁。Starlink 是 SpaceX 的卫星互联网服务，其手机直连卫星技术让普通智能手机连接充当太空基站的卫星。收购全国性低频段许可证将使 SpaceX 获得作为完整移动运营商所需的频谱权利，而不再仅依赖合作伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/technology/last-critical-piece-spacex-secures-spectrum-deal-challenge-big-telecom">"Last Critical Piece": SpaceX Secures Spectrum Deal To... | ZeroHedge</a></li>
<li><a href="https://www.telecomreview.com/index.php/articles/reports-and-coverage/4938-over-500-operators-now-hold-spectrum-licenses-for-low-band-lte-and-5g">Over 500 operators now hold spectrum licenses for low - band LTE...</a></li>
<li><a href="https://www.researchgate.net/figure/hr-mean-Starlink-Gen2-satellites-visible-by-latitude-in-line-of-sight-but-not_fig1_395437535">Figure 1. 24 hr mean Starlink Gen 2 satellites visible by latitude in...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#spectrum`, `#telecom`, `#satellite-internet`

---