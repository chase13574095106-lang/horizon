---
layout: default
title: "Horizon Summary: 2026-06-24 (ZH)"
date: 2026-06-24
lang: zh
---

> From 27 items, 6 important content pieces were selected

---

1. [OpenAI 发布首款定制 AI 推理芯片 Jalapeño](#item-1) ⭐️ 9.0/10
2. [Nub：无需替换运行时，为 Node.js 提供类似 Bun 的工具集](#item-2) ⭐️ 8.0/10
3. [NSA 失去对 Anthropic 的 Mythos AI 工具的访问权限](#item-3) ⭐️ 8.0/10
4. [用生成式 AI 写作业可能降低中国学生考试成绩](#item-4) ⭐️ 8.0/10
5. [Cloudflare 联合浏览器提出 PACT 协议替代验证码](#item-5) ⭐️ 8.0/10
6. [美光 26Q3 营收暴增 346%，净利润 282 亿美元](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布首款定制 AI 推理芯片 Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与 Broadcom 合作、由 TSMC 制造，发布了其首款定制 AI 推理芯片 Jalapeño，专为大型语言模型工作负载设计。该芯片从概念到生产仅用九个月，并借助 OpenAI 自身的 AI 模型加速了开发过程。 这标志着 OpenAI 减少对 Nvidia 等 GPU 供应商依赖、优化推理成本的重要战略举措，推理成本正成为 AI 服务的主要支出。该芯片可能大幅降低运行 ChatGPT 及其他 OpenAI 产品的成本，并可能重塑 AI 硬件格局。 早期测试显示，Jalapeño 在每瓦性能上显著优于当前最先进的 AI 加速器，但详细基准尚未公布。Broadcom 首席执行官 Hock Tan 表示，该加速器相比典型 AI GPU 可节省约 50% 的成本。

hackernews · jamdesk · Jun 24, 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理是从已训练模型中生成响应的过程，与构建模型的训练相对。推理正成为 OpenAI 等 AI 公司的主要成本中心，因为服务数百万用户需要大量计算资源。定制推理芯片可通过针对特定工作负载进行优化，比通用 GPU 更高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/openai-unveils-custom-chip-it-designed-with-broadcom-boost-its-ai-infrastructure-2026-06-24/">OpenAI unveils custom chip it designed with Broadcom to boost ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 声称 AI 模型加速了芯片设计表示怀疑，认为这可能是无意义的营销。其他人讨论了推理芯片的技术优势，有人指出将模型权重固化到硅片中可带来更高效率，但会牺牲灵活性。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [Nub：无需替换运行时，为 Node.js 提供类似 Bun 的工具集](https://github.com/nubjs/nub) ⭐️ 8.0/10

Colin McDonnell 发布了 Nub，这是一个面向 Node.js 的全能工具包，通过 --require 预加载钩子添加了转译、模块解析和 polyfill，在不分叉 Node 运行时的情况下提升了开发者体验。 Nub 通过增强 Node.js 提供类似 Bun 的开发者体验改进，提供了一种务实的替代方案，可能减少 JavaScript 生态系统的碎片化，并允许团队在不切换运行时的情况下采用现代特性。 Nub 使用打包为 Node-API 插件的 oxc 转译器，注册模块解析钩子，并为 Worker 和 Temporal 等 API 注入 polyfill。它在原生 Node.js 上运行，无需修改运行时。

hackernews · colinmcd · Jun 24, 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**背景**: Bun 是一个全能 JavaScript 运行时，包含转译器、打包器和包管理器，相比 Node.js 提供了更好的开发者体验。Nub 采取了不同的方法，通过预加载钩子在 Node.js 之上叠加类似功能，而不是创建新的运行时。这使得用户可以在继续使用 Node.js 的同时获得 Bun 的部分优势。

**社区讨论**: 社区反应积极，用户称赞其实用的方法，并报告了在生产环境中的成功采用。一位评论者提到作者是 Zod 的创建者和前 Bun 员工，另一位则提出了关于通过 --require 与 --import 支持 ESM 的技术问题。

**标签**: `#Node.js`, `#developer tools`, `#JavaScript`, `#tooling`, `#open source`

---

<a id="item-3"></a>
## [NSA 失去对 Anthropic 的 Mythos AI 工具的访问权限](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html) ⭐️ 8.0/10

NSA 因合同纠纷失去了对 Anthropic 先进 AI 工具“Mythos”的访问权限，据报道，Anthropic 在围绕 2 亿美元五角大楼合同的紧张局势中拒绝续签协议。 这一事件凸显了国家安全机构与 AI 公司在获取尖端模型方面日益紧张的关系，引发了对 AI 安全、供应链风险以及 AI 治理权力平衡的担忧。 Mythos 是一款专为网络安全任务设计的强大 AI 模型，能够快速识别软件漏洞。NSA 此前通过一份未最终确定的合同使用该模型，现在一些五角大楼官员希望 NSA 探索替代模型。

hackernews · thm · Jun 24, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48658300)

**背景**: Anthropic 是 Claude AI 模型的开发商，其通过 Project Glasswing 项目开发了 Mythos，向可信组织提供早期访问权限以进行漏洞检测。2026 年 2 月，五角大楼将 Anthropic 列为供应链风险，并与七家其他公司签署了替代协议，但 NSA 继续评估 Mythos。当 Anthropic 拒绝续签 NSA 的访问权限时，争端升级，导致当前的能力丧失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html">N.S.A. Lost Access to Powerful A.I. Model Amid Anthropic Dispute</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://www.nextgov.com/artificial-intelligence/2026/06/parts-nsa-lose-mythos-5-access-amid-anthropic-supply-chain-dispute/414366/">Parts of NSA lose Mythos 5 access amid Anthropic supply chain ...</a></li>

</ul>
</details>

**社区讨论**: 评论意见不一：一些用户对 NSA 失去访问权限表示欣慰，担心监控和权力滥用；另一些人则质疑这一损失的严重性，指出政府如果需要可以没收模型权重。还有关于 Mythos 实际能力的争论，一位评论者声称它能在数小时内攻破机密系统。

**标签**: `#AI`, `#national security`, `#Anthropic`, `#NSA`, `#AI governance`

---

<a id="item-4"></a>
## [用生成式 AI 写作业可能降低中国学生考试成绩](https://cepr.org/publications/dp21577) ⭐️ 8.0/10

一项对 26,811 名中国 7 至 12 年级学生持续 30 个月的追踪研究发现，使用生成式 AI 做作业使作业成绩平均提高 18%、完成时间减少 30%，但导致闭卷考试成绩在 6 个月内平均下降约 20%，中考、高考等高风险考试成绩在约两年后下降 18%至 24%。 这项研究提供了大规模、纵向的证据，表明生成式 AI 可能削弱深度学习和考试成绩，尤其对高成就学生影响显著，为教育者和政策制定者将 AI 融入教育提出了关键警示。 研究发现约 80%的 AI 用户表现出“作业外包”特征——作业时间极短但分数高，这些学生承担了最大的考试损失；而保持与非 AI 用户相近作业时长的使用者损失较小。社科科目损失最大，其次是理工科和语言，低年级、高成就学生和男生受影响更明显。

telegram · zaihuapd · Jun 24, 05:15

**背景**: 生成式 AI（如大型语言模型）能生成类似人类的文本并解决问题，因此被用于完成作业。但闭卷考试要求学生不借助外部工具回忆和应用知识，测试真实理解。该研究揭示了一个潜在权衡：AI 提升了短期作业表现，但可能阻碍长期知识保留和考试成功。

**标签**: `#generative AI`, `#education`, `#student performance`, `#research`, `#China`

---

<a id="item-5"></a>
## [Cloudflare 联合浏览器提出 PACT 协议替代验证码](https://www.techtimes.com/articles/318891/20260623/cloudflare-chrome-firefox-plan-replace-captchas-cryptographic-tokens.htm) ⭐️ 8.0/10

Cloudflare 联合 Chrome、Firefox、Edge 及 Shopify 提出了 PACT 协议，拟用基于盲签名的匿名加密令牌替代 CAPTCHA。 如果被采纳，PACT 将消除用户解决烦人图片验证码的需要，同时保护隐私，显著提升网络用户体验和安全性。 该协议基于 IETF 的 Privacy Pass 标准，采用盲签名技术发放令牌，不泄露用户身份或浏览记录。但目前仍是提案，未确定标准组织与时间表，苹果也未加入。

telegram · zaihuapd · Jun 24, 06:30

**背景**: CAPTCHA 广泛用于区分人类和机器人，但常让用户感到烦恼，且可能被高级 AI 绕过。Privacy Pass 是 IETF 的一个工作组，致力于开发匿名认证协议。盲签名允许服务器在不查看消息内容的情况下对其进行签名，从而实现保护隐私的令牌发放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pactprotocol.io/">PACT Protocol | PACT Protocol Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/wg/privacypass/about/">Privacy Pass (privacypass) - Internet Engineering Task Force</a></li>

</ul>
</details>

**标签**: `#web security`, `#CAPTCHA replacement`, `#cryptographic tokens`, `#Privacy Pass`, `#IETF`

---

<a id="item-6"></a>
## [美光 26Q3 营收暴增 346%，净利润 282 亿美元](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

美光科技公布 2026 财年第三季度创纪录业绩，营收 414.6 亿美元，同比增长 346%，净利润 282.4 亿美元，受 AI 对高性能内存需求驱动。Non-GAAP 毛利率达 84.9%。 这一爆发式增长凸显了内存在 AI 基础设施中的关键作用，美光的 HBM4 已大规模量产，HBM4E 预计 2027 年投产。业绩表明内存制造商的需求和定价能力将持续强劲。 数据中心营收暴增 653%至 115.2 亿美元，云内存增长 306%至 137.7 亿美元。美光预计下季度营收 500 亿美元，毛利率 86%，并已签署 16 份长期战略协议锁定未来 3-5 年订单。

telegram · zaihuapd · Jun 24, 22:22

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 技术，用于 NVIDIA GPU 等 AI 加速器，带宽远高于传统 DDR 内存。HBM4 是最新一代，HBM4E 是增强版，预计 2027 年投产。Non-GAAP 毛利率排除一次性费用，更清晰反映运营盈利能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.wevolver.com/article/high-bandwidth-memory">High Bandwidth Memory : Concepts, Architecture, and Applications</a></li>
<li><a href="https://www.digitaltoday.co.kr/en/view/53615/memory-big-two-near-hbm4e-race-mass-production-timeline-becomes-key-battleground">Memory big two near HBM 4 E race as mass production timing...</a></li>

</ul>
</details>

**标签**: `#Micron`, `#semiconductors`, `#AI infrastructure`, `#HBM`, `#financial results`

---