---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> From 31 items, 7 important content pieces were selected

---

1. [陶哲轩与 25 位菲尔兹奖得主警告 AI 与数学界严重错位](#item-1) ⭐️ 9.0/10
2. [OpenAI 推出 Agents API 公测版](#item-2) ⭐️ 9.0/10
3. [开发者发现 220 美元谷歌应用广告中 60%的安装来自机器人](#item-3) ⭐️ 8.0/10
4. [OpenAI 在 API 上线 GPT-Live-1 全双工语音模型](#item-4) ⭐️ 8.0/10
5. [GitLab 修复 CVSS 10.0 漏洞：未授权读取服务器文件](#item-5) ⭐️ 8.0/10
6. [DeepSeek 发布 V4.1 Flash：552B 多模态 MoE 模型](#item-6) ⭐️ 8.0/10
7. [Anthropic 指控七家中国 AI 实验室大规模蒸馏 Claude](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩与 25 位菲尔兹奖得主警告 AI 与数学界严重错位](https://mathandai.org/) ⭐️ 9.0/10

2026 年 9 月 11 日，陶哲轩在其博客上发表了题为《AI 在数学中的严重错位》的声明，由 25 位菲尔兹奖得主联署，指出 AI 公司的商业动机与数学界的目标存在根本性冲突。此前，OpenAI 声称解决了一个重大未解问题的方法引发众怒，《经济学人》报道称顶尖数学家担心 AI 可能破坏数学的根基。 这是数学界最高荣誉获得者前所未有的集体警告，表明 AI 对证明求解的快速介入可能扰乱数学界的 credit 分配、理解方式和研究规范。这不仅影响数学家，也影响 AI 实验室、资助者以及任何 AI 生成结果超出人类理解能力的科学领域。 该声明由包括陶哲轩在内的 25 位菲尔兹奖得主签署，并将此问题视为影响其他科学和创意职业的更广泛对齐问题的一部分。争议由 OpenAI 的 GPT-6 Astra 引发，据报道其花费约 17 小时验证了一个流体动力学问题的解，纽约大学数学家指责该公司在关乎职业发展的问题上“手段不光彩”。

hackernews · meredydd · Sep 11, 17:45 · [社区讨论](https://news.ycombinator.com/item?id=49662371)

**背景**: 菲尔兹奖常被称为数学界的诺贝尔奖，每四年颁发给少数 40 岁以下的数学家。AI 对齐通常指确保 AI 系统追求预期目标；此处指 AI 实验室追求快速、吸引眼球的成果与数学界缓慢、严谨的证明和同行理解文化之间的不匹配。OpenAI 最近声称用 GPT-6 Astra 解决了一个长期存在的问题，加剧了围绕 credit 和验证的现有紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/">A Severe Misalignment of AI in Mathematics | What's new</a></li>
<li><a href="https://www.economist.com/science-and-technology/2026/09/11/top-mathematicians-are-outraged-by-openais-methods">Top mathematicians are outraged by OpenAI ’s methods</a></li>
<li><a href="https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/">OpenAI fought dirty on career-making math problem... | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了多种类比：一位数学家将 AI 生成的证明与望月新一孤立的 abc 猜想证明相比，指出后者仍催生了富有成效的会议和论文；另一位认为 AI 破坏的是“解决未解问题”这一衡量标准，而非理解本身。还有人将这种恐慌比作 1990 年代对计算机毁掉国际象棋的担忧，指出如今国际象棋更受欢迎、棋手更强；一位评论者则引用波德莱尔 19 世纪对摄影的批评，称其只是机械记录，无法像绘画那样改造现实。

**标签**: `#AI`, `#mathematics`, `#research`, `#ethics`, `#alignment`

---

<a id="item-2"></a>
## [OpenAI 推出 Agents API 公测版](https://openai.com/index/introducing-the-agents-api/) ⭐️ 9.0/10

2026 年 9 月 10 日，OpenAI 推出 Agents API 公测版，开发者只需一次 API 调用即可创建生产级云端智能体。该 API 允许开发者选择 OpenAI 托管沙箱、自有基础设施或合作伙伴环境进行部署。 此次发布标志着智能体开发范式的重大转变，从碎片化的自定义流程转向统一的生产级平台。这可能加速自主 AI 智能体在整个生态中的普及，并重塑开发者构建和部署 AI 应用的方式。 该 API 基于开源 Codex harness 构建，支持长会话上下文压缩、工具搜索、并行工具调用以及最多 3 个并发子智能体的协作。公测期间除令牌和工具使用费用外，不收取额外费用。

telegram · zaihuapd · Sep 11, 11:12

**背景**: Codex harness 是支撑所有 Codex 体验（包括 Web 应用、CLI、IDE 扩展和 macOS 应用）的底层智能体循环与逻辑。它负责管理对话状态、流式执行、工具调用以及沙箱和审批策略。Agents API 将这一基础设施扩展到通用云端智能体，而不仅限于编码任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/unlocking-the-codex-harness/">Unlocking the Codex harness: how we built the App Server | OpenAI</a></li>
<li><a href="https://developers.openai.com/blog/codex-as-a-platform">Codex as a platform: build on the open agent harness | OpenAI Developers</a></li>
<li><a href="https://www.ithome.com/1/001/072.htm">OpenAI Agents API ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Agents API`, `#AI 智能体`, `#API 发布`, `#云计算`

---

<a id="item-3"></a>
## [开发者发现 220 美元谷歌应用广告中 60%的安装来自机器人](https://dayzlegame.com/blog/google-ads-bot-farm/) ⭐️ 8.0/10

一位开发者花费 220 美元投放谷歌应用广告后，发现约 60%的安装量来自机器人，这一博客文章在 Hacker News 上引发热议，获得 228 分和 120 条评论。文章记录了机器人农场如何模拟点击、安装甚至转化，以骗取谷歌广告系统的回报。 这一案例为开发者和营销人员提供了具体的数据证据，表明广告欺诈在谷歌广告等主流平台上依然严重，直接浪费了小型应用发布者的广告预算。这也引发了关于广告平台在检测和阻止无效流量方面应承担多少责任的质疑，毕竟平台本身也从这些流量中获利。 社区成员指出，机器人农场通常运行在数据中心 IP 段而非住宅网络提供商上，广告主可以在谷歌广告的“管理 > 账户设置 > IP 排除”中添加整个网络段（例如 123.4.5.*）。一位评论者表示，在投放谷歌广告几年后，仅在美国就积累了超过 4000 个排除网络。

hackernews · nickabe · Sep 11, 18:24 · [社区讨论](https://news.ycombinator.com/item?id=49662990)

**背景**: 移动广告欺诈是指故意操纵点击、展示、安装或转化等广告指标，以产生非法收入或虚增效果数据。常见手段包括机器人农场、设备模拟器、点击注入和 VPN 代理工具，检测通常依赖行为分析和异常规则，用来标记异常的点击转化率。谷歌广告是谷歌的广告投放平台，AdMob 则是其移动广告变现网络，后者会因无效流量而封禁账户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49662990">I spent $220 on Google app ads and 60% of the installs were robots</a></li>
<li><a href="https://www.humansecurity.com/learn/topics/what-is-mobile-ad-fraud/">What is Mobile Ad Fraud? Here’s How To Stop Mobile Ad Fraud</a></li>
<li><a href="https://improvado.io/blog/ad-fraud">Ad Fraud 2026: Detection & Prevention Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对广告平台持怀疑态度，有人称谷歌和 Meta 的广告是“骗局”，还有人怀疑谷歌对自己有能力检测的欺诈行为视而不见。一个被广泛引用的警示案例是：一位开发者购买谷歌广告推广带 AdMob 变现的应用，结果其 AdMob 账户因无效流量被封禁。其他人则提供了实用的缓解建议，例如排除数据中心 IP 段，还有一位评论者在安装应用后称赞其界面简洁。

**标签**: `#ad-fraud`, `#google-ads`, `#mobile-apps`, `#digital-advertising`, `#bot-detection`

---

<a id="item-4"></a>
## [OpenAI 在 API 上线 GPT-Live-1 全双工语音模型](https://openai.com/index/introducing-gpt-live-1-in-the-api/) ⭐️ 8.0/10

2026 年 9 月 10 日，OpenAI 在 API 上线 GPT-Live-1，这是一款可同时听说（全双工）的语音模型，支持自然打断、背景噪声处理、长对话以及电话语音代理。OpenAI 称其在 Full Duplex Bench 上较 GPT-Realtime-2.1 提升 30 个百分点，API 语音前端价格为每分钟 0.05 美元。 全双工能力是语音代理的重要一步，因为它让模型能像人类一样处理重叠语音和打断，这对呼叫中心、客户支持和电话助手至关重要。相较 GPT-Realtime-2.1 提升 30 个百分点，说明轮次转换能力进步很快，可能促使开发者把现有的实时语音管线迁移到 GPT-Live-1。 GPT-Live-1 可将复杂推理与工具调用交给后端模型处理，使语音前端保持轻量，API 语音前端价格为每分钟 0.05 美元。30 个百分点的提升是在 Full Duplex Bench 上测得的，该基准评估停顿处理、反馈信号（backchanneling）、轮次转换和打断管理。

telegram · zaihuapd · Sep 11, 03:09

**背景**: 传统语音助手是半双工的：先听再说，难以处理用户插话。全双工口语对话模型专为实时双向交流设计，可处理重叠语音、打断和快速反馈信号，Full-Duplex-Bench 正是为系统评估这些轮次转换行为而提出的基准。2026 年 7 月发布的 GPT-Realtime-2.1 是 OpenAI 此前低延迟流式语音到语音模型，支持可配置推理强度和工具调用，GPT-Live-1 则是该系列的最新进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.04721">[2503.04721] Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-2.1">GPT-Realtime-2.1 Model | OpenAI API</a></li>
<li><a href="https://www.emergentmind.com/topics/full-duplex-spoken-dialogue-model">Full-Duplex Spoken Dialogue Model</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#voice-ai`, `#API`, `#speech-models`, `#realtime`

---

<a id="item-5"></a>
## [GitLab 修复 CVSS 10.0 漏洞：未授权读取服务器文件](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 8.0/10

GitLab 于 9 月 10 日发布 19.3.2、19.2.6 和 19.1.8 紧急补丁，修复 CVE-2026-85706。该漏洞 CVSS 评分为 10.0，未认证攻击者可利用代码仓库 commits API 读取自建 GitLab 服务器上的任意文件。受影响版本包括 18.7 至 19.1.8 之前、19.2.6 之前的 19.2 版本，以及 19.3.2 之前的 19.3 版本。 最高严重级别的未认证任意文件读取漏洞对任何运行自建 GitLab 的组织都是重大安全事件，暴露的实例可能泄露凭证、密钥和机密数据。GitLab.com 已完成修复，GitLab Dedicated 用户无需操作，但自建实例管理员必须立即升级。 该漏洞源于代码仓库 commits API 的路径约束不当和认证缺失，由研究员 s3ntago 通过 GitLab 的 HackerOne 漏洞赏金计划报告。GitLab 尚未公开具体前置条件，网上也没有可复现的公开 PoC，目前尚无证据表明已遭在野利用。

telegram · zaihuapd · Sep 11, 11:05

**背景**: CVSS 是一个根据攻击向量、复杂度、所需权限以及对机密性、完整性和可用性的影响等指标，对漏洞严重程度进行 0.0 至 10.0 评分的框架，10.0 分代表最高严重级别。GitLab 是广泛使用的 DevOps 平台，既有托管服务 GitLab.com，也有自建的社区版和企业版，自建实例的安全更新由管理员自行负责。路径遍历漏洞允许攻击者操纵文件路径访问预期目录之外的文件，若再叠加认证缺失，就可能在无需登录的情况下暴露服务器上的敏感文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html">GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure</a></li>
<li><a href="https://www.news4hackers.com/gitlab-critical-path-traversal-vulnerability-patch-needed/">GitLab Critical Path Traversal Vulnerability Patch Needed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#gitlab`, `#vulnerability`, `#cve`, `#devops`

---

<a id="item-6"></a>
## [DeepSeek 发布 V4.1 Flash：552B 多模态 MoE 模型](https://t.me/zaihuapd/43770) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是其全新模型结构系列中最小尺寸的模型，采用 552B 参数的 Causal-Encoder-Decoder（CED）结构，输入和输出激活分别为 8B 和 16B，并原生支持多模态视觉理解。该模型已上线 DeepSeek API，模型名为 deepseek-flash，新价格于 2026 年 9 月 10 日 12:00 生效，9 月 14 日 12:00 后 deepseek-v4-pro 的请求将被重新路由。 此次发布标志着 DeepSeek 转向全新的 Causal-Encoder-Decoder 架构，将读取与写入解耦，有望在效率上超越传统的纯解码器模型。同时它也扩展了 DeepSeek 的多模态能力，并重塑了其 API 定价和模型阵容，影响在其平台上构建应用的开发者和企业。 该模型是多模态混合专家（MoE）模型，主干参数为 552B，支持高达一百万 token 的上下文，可原生处理图像和文本并以自回归方式生成文本。V4-Flash 和 V4-Flash-Vision-Exp 已退役，新定价和路由变更分别于 2026 年 9 月 10 日和 9 月 14 日生效。

telegram · zaihuapd · Sep 11, 11:32

**背景**: 像 GPT 和 Llama 这样的传统自回归大语言模型采用单一的纯解码器架构，同一组权重同时负责读取（预填充）和写入（解码），共享相同的计算预算。Causal-Encoder-Decoder（CED）架构将这些阶段解耦，使用独立的组件分别编码输入和生成输出，从而提升效率。DeepSeek V4.1 Flash 将这一设计应用于混合专家（MoE）框架中，每个 token 只激活部分参数，因此尽管总参数量高达 552B，推理成本仍能保持较低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek -ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>
<li><a href="https://www.happyrock.cloud/blog/2026-09-11_a_en/">DeepSeek V4.1 Flash In-Depth: 552B MoE, Asymmetric Causal ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#multimodal`, `#model-release`, `#AI`

---

<a id="item-7"></a>
## [Anthropic 指控七家中国 AI 实验室大规模蒸馏 Claude](https://t.me/zaihuapd/43771) ⭐️ 8.0/10

Anthropic 最新威胁情报报告称，其发现并阻止了七家中国 AI 实验室针对 Claude 的大规模蒸馏活动，并点名阿里巴巴、智谱、小米、商汤和 MiniMax。其中阿里巴巴规模最大，5 月至 7 月产生超过 1.51 亿次交互，高峰期每天接近 300 万次，Anthropic 称这些数据被用于训练 Qwen 3.5、3.6 和 3.7 模型。 这是中美 AI 竞争加剧背景下的重要进展，涉及模型知识产权、服务条款执行以及前沿模型竞赛。若指控成立，可能加剧对中国 AI 实验室训练实践的审视，并影响未来出口管制或 API 访问政策的讨论。 报告描述了利用虚假账号、代理和抓取对话记录来提取 Claude 能力的行为，Anthropic 称相关数据还被用于强化学习环境和模型架构工作。这些指控目前仅为单方面企业声明，未经独立验证，且 Telegram 帖子只是简要摘要。

telegram · zaihuapd · Sep 11, 13:10

**背景**: 模型蒸馏是一种机器学习技术，通过让较小模型学习较大模型的输出来迁移知识，通常是对小模型进行微调。它本身是合法且广泛使用的方法，但以工业规模利用竞争对手 API 的输出训练自家模型通常违反服务条款，这正是 Anthropic 所称的非法蒸馏攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/">Anthropic details distillation campaigns from Alibaba ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#model distillation`, `#China AI labs`, `#threat intelligence`

---