---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> From 46 items, 8 important content pieces were selected

---

1. [Karpathy 发布 NanoChat：100 美元的 ChatGPT 克隆版](#item-1) ⭐️ 8.0/10
2. [欧盟议会间谍软件调查员遭飞马间谍软件攻击](#item-2) ⭐️ 8.0/10
3. [Current AI 发布开源 AI 差距地图](#item-3) ⭐️ 8.0/10
4. [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](#item-4) ⭐️ 8.0/10
5. [华为 Atlas 350 搭载昇腾 950PR，性能达 H20 的 2.87 倍](#item-5) ⭐️ 8.0/10
6. [阿里下令全员卸载 Claude，7 月 10 日生效](#item-6) ⭐️ 8.0/10
7. [NASA 发射救援卫星拯救老化雨燕望远镜](#item-7) ⭐️ 8.0/10
8. [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Karpathy 发布 NanoChat：100 美元的 ChatGPT 克隆版](https://github.com/karpathy/nanochat) ⭐️ 8.0/10

Andrej Karpathy 发布了 nanochat，这是一个从头构建的、极简的全栈训练和推理管道，用于类似 ChatGPT 的聊天机器人，代码库单一且依赖极少。 该项目通过展示仅需 100 美元即可构建功能性的 ChatGPT 替代品，从而普及了对话式 AI 的访问，可能推动该领域更广泛的实验和教育。 NanoChat 基于 Karpathy 之前的 nanoGPT，但将其从预训练扩展到完整的聊天机器人管道，包括一个 Rust 分词器和大约 8000 行代码。

github · karpathy · Jul 3, 17:47

**背景**: 三年前发布的 nanoGPT 仅专注于语言模型的预训练。NanoChat 通过添加微调和推理完善了这一图景，使其成为一个实用的聊天机器人。该项目旨在易于修改且依赖轻量，吸引开发者和研究人员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can buy. · GitHub</a></li>
<li><a href="https://x.com/karpathy/status/1977755427569111362?lang=en">Excited to release new repo: nanochat! (it's ...</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1o5qo0r/it_has_been_4_hrs_since_the_release_of_nanochat/">r/LocalLLaMA on Reddit: It has been 4 hrs since the release of nanochat from Karpathy and no sign of it here! A new full-stack implementation of an LLM like ChatGPT in a single, clean, minimal, hackable, dependency-lite codebase</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对 nanochat 表现出兴趣，注意到其 8000 行代码和 Rust 分词器，部分人质疑其与 nanoGPT 相比的新颖性。总体情绪积极，许多人计划探索代码。

**标签**: `#LLM`, `#ChatGPT`, `#open-source`, `#cost-effective`, `#AI`

---

<a id="item-2"></a>
## [欧盟议会间谍软件调查员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室确认，一名参与调查间谍软件的欧洲议会委员会成员在 2022 年和 2023 年多次被飞马间谍软件成功感染，导致包括个人医疗信息和政府文件在内的敏感数据泄露。 此次攻击直接损害了民主机构调查过程的完整性，并凸显了商业间谍软件对民选官员和公共问责制的持续威胁。 感染发生在 2022 年 10 月 21 日和 2023 年 3 月 6 日至 7 日，目标是欧洲议会调查飞马及同类监控间谍软件使用情况的调查委员会（PEGA 委员会）的一名成员。

hackernews · ledoge · Jul 3, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的一款强大的间谍软件，能够远程入侵移动设备并窃取数据。公民实验室是多伦多大学的一家领先研究机构，致力于调查数字威胁，并已曝光全球多起飞马感染事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出间谍软件调查员被黑具有讽刺意味，一些人提到希腊和意大利更广泛的涉及国家滥用飞马的丑闻。其他人讨论了设备加固措施，认为使用 GrapheneOS 或启用锁定模式本可以提高攻击成本。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-3"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI 是一家在 2025 年 2 月巴黎 AI 行动峰会上成立的非营利组织，发布了开源 AI 差距地图 v0.1，索引了开源 AI 栈中的 421 个产品，包括 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目。 该地图提供了一个结构化、可公开访问的资源，有助于理解开源 AI 生态系统，帮助开发者、研究人员和政策制定者识别差距和机会。底层数据以 MIT 许可证发布，支持进一步分析和社区贡献。 该地图将产品组织为 3 层（模型组件、产品/用户体验和基础设施）共 14 个类别，并追踪了超过 16,000 个 GitHub 仓库。数据以 YAML 文件和 CSV 格式在 GitHub 上提供，可通过 Datasette Lite 进行探索。

rss · Simon Willison · Jul 3, 22:04

**背景**: Current AI 是一个全球合作伙伴关系，已承诺投入 4 亿美元，旨在构建 AI 的公共选项。差距地图试图系统性地编录开源 AI 领域，该领域发展迅速但缺乏全面的索引。该项目获得了大量资金支持，旨在支持开源 AI 社区。

**标签**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

---

<a id="item-4"></a>
## [Anthropic 指控阿里巴巴对 Claude 发动大规模蒸馏攻击](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴利用近 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，非法提取 Claude 的能力，这是已知最大规模的蒸馏攻击。 这一指控凸显了 AI 行业面临的严重安全和知识产权威胁，因为蒸馏攻击可能破坏出口管制，使外国竞争对手在未经授权的情况下复制专有模型，从而削弱美国 AI 公司的竞争优势。 Anthropic 声称阿里巴巴及其 Qwen AI 实验室参与了此次攻击，通过重复查询 Claude 来训练竞争模型。攻击持续了 45 天，涉及数百万次交互，是 Anthropic 迄今检测到的最大规模此类攻击。

telegram · zaihuapd · Jul 3, 06:21

**背景**: 模型蒸馏是一种让较弱模型通过学习较强模型的输出来复制其能力的技术。虽然合法用于内部开发，但未经许可使用其他公司的专有模型被视为知识产权盗窃。Anthropic 一直强调蒸馏攻击的风险，这种攻击可能绕过出口管制，使先进的 AI 能力在全球扩散。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks: What They Are and Why They Matter | MindStudio</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#model distillation`, `#Anthropic`, `#Alibaba`

---

<a id="item-5"></a>
## [华为 Atlas 350 搭载昇腾 950PR，性能达 H20 的 2.87 倍](https://t.me/zaihuapd/42329) ⭐️ 8.0/10

在 2026 年华为中国合作伙伴大会上，华为正式发布并上市了搭载全新昇腾 950PR 处理器的 Atlas 350 AI 加速卡，声称单卡算力达到英伟达 H20 的 2.87 倍，并支持 FP4 低精度推理。 此次发布标志着华为在 AI 硬件竞赛中迈出重要一步，可能减少中国在 AI 推理领域对英伟达芯片的依赖。FP4 支持和高内存容量（112GB HBM）可降低 70B 参数等大模型的推理成本和延迟。 Atlas 350 据称是国内唯一支持 FP4 推理的加速卡，拥有 112GB HBM 容量，可单卡加载 70B 参数模型。与前代相比，在向量算力、互联带宽和自研 HBM 等方面均有提升。

telegram · zaihuapd · Jul 3, 08:35

**背景**: 英伟达 H20 GPU 是为中国市场设计的 H100 修改版，以符合美国出口限制。FP4 是一种 4 位浮点格式，英伟达已将其用于高效 AI 推理，华为采用 FP4 表明其与行业趋势一致。昇腾 950PR 是华为最新的 AI 芯片，据部分报道可提供 1.56 petaflops 算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/">Ascend 950PR AI Chip: Everything you need to know</a></li>
<li><a href="https://nerdleveltech.com/huawei-ascend-950pr-atlas-350-ai-chip-challenges-nvidia">Huawei Ascend 950PR Beats NVIDIA H20: 2.8× FP8, CUDA-Ready</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AI hardware`, `#Ascend`, `#Atlas 350`, `#FP4`

---

<a id="item-6"></a>
## [阿里下令全员卸载 Claude，7 月 10 日生效](https://t.me/zaihuapd/42334) ⭐️ 8.0/10

阿里巴巴内部下令要求全体员工卸载 Anthropic 相关产品，包括 Claude 模型（Sonnet、Opus、Fable）和 Claude Code agent，禁令于 7 月 10 日生效。此前 Anthropic 指控阿里在 4 月 22 日至 6 月 5 日期间使用约 2.5 万个虚假账号与 Claude 交互超过 2800 万次。 这一事件凸显了大型科技公司在 AI 模型安全和知识产权方面的紧张关系。它可能为企业在面对模型蒸馏指控时如何执行使用政策树立先例，从而影响更广泛的 AI 生态系统。 禁令涵盖所有 Anthropic 产品，包括 Claude 模型（Sonnet、Opus、Fable）和 Claude Code agent。此前，阿里曾报销员工使用 Claude、GPT、Gemini 等外部模型的费用。Anthropic 随后收紧了风控策略。

telegram · zaihuapd · Jul 3, 13:00

**背景**: Claude 是 Anthropic 公司开发的一系列大型语言模型，Anthropic 是一家 AI 安全公司。Claude Code 是一种代理式编码工具，可以读取代码库并执行命令。模型蒸馏是一种技术，通过使用大型模型的输出来训练较小的模型模仿其行为。未经授权的蒸馏指控可能导致法律和政策纠纷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html">Anthropic accuses Alibaba of campaign to extract AI capabilities</a></li>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://www.explainx.ai/blog/anthropic-alibaba-claude-distillation-25000-fake-accounts-2026">Anthropic vs Alibaba — 25K Fake Claude Accounts, Distillation ...</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#Claude`, `#Anthropic`, `#AI policy`, `#corporate security`

---

<a id="item-7"></a>
## [NASA 发射救援卫星拯救老化雨燕望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

2026 年 7 月 3 日，NASA 发射了由 Katalyst Space 建造的 LINK 航天器，与运行 20 年的雨燕空间望远镜会合，并将其轨道抬升约 240 公里，防止其即将发生的大气层再入。 此次任务是私人航天器首次尝试抓取并服务美国政府卫星，展示了一种延长老化太空资产寿命、减少太空碎片的新方法。 LINK 航天器将使用机械臂抓住雨燕，然后启动推进器抬升轨道。如果成功，雨燕最快可在 2026 年 9 月恢复科学观测。

telegram · zaihuapd · Jul 3, 15:43

**背景**: 雨燕天文台于 2004 年发射，研究伽马射线暴及其他宇宙现象。由于太阳活动增加，其轨道持续衰减，若不干预，将在 2026 年底前坠入大气层烧毁。在轨卫星服务是一个新兴领域，此前有 1984 年修复太阳极大期任务等先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_rescue_mission">Swift Boost Mission - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift Observatory - NASA</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/nasa-to-launch-ambitious-mission-to-save-a-space-telescope-from-burning-up-in-earths-atmosphere">NASA launches rescue mission to save Swift space telescope from burning up in Earth's atmosphere | Space</a></li>

</ul>
</details>

**标签**: `#NASA`, `#space telescope`, `#satellite servicing`, `#space technology`

---

<a id="item-8"></a>
## [腾讯阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室的阿图因 AI 在 CyberGym 网络安全基准测试中获得 84.0%的得分，超过 Anthropic 的 Claude Mythos Preview，并以不到 Mythos 0.1%的成本在多个开源项目中发现了高危漏洞。 这表明开源、可本地部署的 AI 模型能够以极低的成本在网络安全任务中超越专有系统，可能推动高级漏洞检测的普及，并减少对昂贵商业 AI 服务的依赖。 阿图因 AI 基于开源模型 GLM-5.1 构建，在 curl、gnark、OpenSSL、Python cryptography 和 Java bc-java 中发现了此前未被检测到的高危逻辑漏洞，严重性评分最高达 9.3。在伯克利 BVI 真实世界漏洞榜单中，其严重漏洞严重程度排名第 1，总数排名第 5。

telegram · zaihuapd · Jul 3, 16:12

**背景**: CyberGym 是加州大学伯克利分校主导的大规模网络安全评估框架，利用来自 188 个软件项目的 1507 个历史漏洞测试 AI 代理的真实漏洞分析能力。GLM-5.1 是 Z.AI 推出的开源旗舰模型，专为长周期代理任务设计。Anthropic 的“玻璃翼计划”使用 Claude Mythos Preview 在攻击者利用之前主动修复漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities ...</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.1">zai-org/GLM-5.1 · Hugging Face</a></li>
<li><a href="https://news.aibase.com/zh/news/26923">27年老漏洞被AI识破!苹果谷歌联手 Anthropic 开启“ 玻 璃 翼 ”护航</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#benchmark`, `#vulnerability detection`, `#open-source`

---