---
layout: default
title: "Horizon Summary: 2026-09-07 (ZH)"
date: 2026-09-07
lang: zh
---

> From 26 items, 6 important content pieces were selected

---

1. [LG 智能电视被曝录制音频并扫描网络](#item-1) ⭐️ 8.0/10
2. [Linux 内核 Git 服务器被滥用爬虫淹没](#item-2) ⭐️ 8.0/10
3. [OpenAI 揭示编码代理与递归自我改进通往 AGI 之路](#item-3) ⭐️ 8.0/10
4. [黄仁勋称 GPT-6 Astra 标志 AGI 到来，由 10 万颗 NVLink72 芯片训练](#item-4) ⭐️ 8.0/10
5. [华为时隔六年发布新款高性能芯片](#item-5) ⭐️ 8.0/10
6. [最高法发布 AI 纠纷司法解释，明确换脸与算法杀熟责任](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LG 智能电视被曝录制音频并扫描网络](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

Gamers Nexus 的一项调查发现，LG 智能电视（包括 G5 OLED 型号）会主动扫描本地网络以发现附近设备，并且即使在屏幕关闭的情况下也能捕获麦克风音频。该发现已在 YouTube 上发布，并被 Notebookcheck 等媒体报道。 这引发了约 2.16 亿 LG 智能电视用户的严重隐私担忧，因为设备可能在未经明确同意的情况下收集敏感数据。它凸显了智能电视行业在数据收集和用户监控方面的更广泛问题，可能引发监管审查和消费者抵制。 使用 Wireshark 进行的网络数据包捕获显示，电视会扫描局域网以查找手机、智能手表和其他硬件。测试还表明，在屏幕关闭时也会进行音频记录，并且 LG 的服务条款要求用户告知家庭成员和客人可能存在的窃听行为。

hackernews · treve · Sep 7, 00:22 · [社区讨论](https://news.ycombinator.com/item?id=49592375)

**背景**: 智能电视通常包含语音识别功能和互联网连接，但用户可能没有意识到数据收集的程度。LG 的 webOS 平台已知会收集观看习惯和其他数据，但这项调查揭示了更具侵入性的做法，包括本地网络扫描和在电视看似关闭时捕获音频。这些做法可能与窃听法规等隐私法律相冲突，因为家中的第三方并未同意。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/lg-smart-tvs-caught-scanning-networks/">LG Smart TVs Caught Scanning Networks and Logging Audio in ...</a></li>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with screen off and snooping on local devices - Notebookcheck News</a></li>
<li><a href="https://cybernews.com/privacy/up-to-200m-lg-smart-tvs-could-be-secretly-listening-in-on-conversations/">LG smart TVs may log voice commands and scan homes | Cybernews</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了愤怒和担忧，用户分享了各自的缓解策略，如禁用网络功能或物理拔掉 WiFi/BT 芯片。一些评论者指出这可能违反窃听法律，而另一些人则批评 LG 的服务条款将同意责任转嫁给用户。

**标签**: `#privacy`, `#smart-tv`, `#security`, `#LG`, `#surveillance`

---

<a id="item-2"></a>
## [Linux 内核 Git 服务器被滥用爬虫淹没](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 8.0/10

git.kernel.org 的维护者 Konstantin Ryabitsev 报告称，滥用爬虫在渲染提交为 HTML 上消耗的 CPU 周期超过了所有合法访问（包括 git 克隆）的总和。在 5 个地理分布节点上，任何时候都有 14 个 CPU 核心专门用于为爬虫渲染提交。 这凸显了大型开源项目和网络服务面临的一个日益严重的问题：滥用爬虫可能带来巨大的基础设施成本，并降低合法用户的性能。这强调了整个行业需要更好的机器人检测和缓解策略。 报告特别指出，爬虫的 CPU 使用量超过了所有合法访问（包括通常资源密集的 git 克隆）的总和。14 个 CPU 核心分布在 5 个地理分布节点上，表明问题的规模。作者 Simon Willison 也从 Datasette 的角度表达了担忧，Datasette 提供大量可爬取的页面。

rss · Simon Willison · Sep 7, 23:08

**背景**: git.kernel.org 是 Linux 内核的官方 Git 仓库托管服务，使用 gitweb 将提交渲染为 HTML 以供网页浏览。网络爬虫，包括 AI 公司用于抓取数据的爬虫，可能会在短时间内请求大量页面，从而使服务器不堪重负。这个问题是互联网上滥用机器人流量日益增长这一更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/docs/gitweb">Git - gitweb Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Git">Git - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论可能包括开发者和维护者分享类似遭遇滥用爬虫的经历，讨论潜在的解决方案，如速率限制、验证码和 robots.txt 合规性。有些人可能会争论 AI 抓取的伦理问题，以及 AI 公司尊重服务器资源的责任。

**标签**: `#web crawling`, `#open source`, `#infrastructure`, `#security`, `#Linux kernel`

---

<a id="item-3"></a>
## [OpenAI 揭示编码代理与递归自我改进通往 AGI 之路](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 发布了一篇题为《研究加速：OpenAI 内部视角》的文章，详细介绍了编码代理如何重塑其研究工作流程，同时首席科学家 Jakub Pachocki 发表了新文章《异类心智》，两者都讨论了递归自我改进（RSI）作为通往 AGI 的路径。报告中的图表显示，每位研究人员的每日 AI 支出从 2026 年 6 月约 150 美元急剧上升至 2026 年 8 月底约 600 美元。 这很重要，因为它罕见地揭示了领先 AI 实验室如何内部使用自己的工具，表明代理工程已成为 AI 研究的核心。将 RSI 作为 AGI 的新框架的讨论可能塑造行业话语和对 AI 进展的预期。 报告中的图表显示，2026 年 7 月下旬开始每位研究人员的 AI 支出显著加速，作者推测这可能与内部访问后来以 GPT-6 Astra 发布的模型有关。文章指出，2026 年是代理工程在 OpenAI 真正起飞的一年，反映了更广泛的行业趋势。

rss · Simon Willison · Sep 6, 23:57

**背景**: 递归自我改进（RSI）指的是一种假设情景，即 AI 系统能够改进自身能力，可能导致智能爆炸。编码代理是能够自主编写、修改和调试代码的 AI 工具，而代理工程是一门新兴学科，通过人类监督来编排此类代理以执行复杂任务。OpenAI 将 RSI 作为新的 AGI 框架进行讨论，表明该公司在概念化其长期目标方面发生了转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/research-acceleration-view-inside-openai/">Research acceleration: The view inside OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/">RSI is the new AGI — and it’s just as hard to pin down</a></li>

</ul>
</details>

**社区讨论**: 提供的内容不包含社区评论，因此无法提供讨论摘要。

**标签**: `#OpenAI`, `#AGI`, `#AI research`, `#coding agents`, `#recursive self-improvement`

---

<a id="item-4"></a>
## [黄仁勋称 GPT-6 Astra 标志 AGI 到来，由 10 万颗 NVLink72 芯片训练](https://mp.weixin.qq.com/s/PJp4LEoiZPYqz3Mclqr7xg) ⭐️ 8.0/10

英伟达 CEO 黄仁勋表示，OpenAI 上周发布的 GPT-6 Astra 标志着通用人工智能（AGI）正式到来，并透露该模型由约 10 万颗 NVIDIA Grace Blackwell NVLink72 芯片训练而成。OpenAI 称 Astra 为“代际跃迁”，在计算机操作、软件工程、网络安全和科研等领域达到最先进水平。 行业领袖的这一声明可能加速 AI 基础设施和 AGI 领域的投资与研究。同时，它也凸显了 NVLink72 等大规模训练系统的重要性，可能塑造 AI 硬件和软件的未来发展方向。 据报道，该模型由约 10 万颗 NVLink72 芯片训练，这些芯片属于 NVIDIA 的 Grace Blackwell 架构。然而，OpenAI CEO 萨姆·奥尔特曼淡化了 AGI 一词，称其“定义模糊”且是“无关紧要的营销术语”。

telegram · zaihuapd · Sep 7, 04:54

**背景**: NVLink72 是一种机架级系统，通过 NVLink 5.0 互联将 72 颗 GPU 连接成一个逻辑加速器，实现高带宽通信。GPT-6 Astra 是 OpenAI 的最新模型，被描述为迄今最智能且最对齐的模型，具备计算机操作、编程、网络安全和科学等领域的能力。AGI（通用人工智能）指在广泛任务中达到或超越人类认知能力的 AI 系统，但其定义仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nextpcb.com/blog/nvidia-gb200-nvl72-architecture">NVIDIA GB200 NVL72: PCB & System Architecture Explained</a></li>
<li><a href="https://wandb.ai/onlineinference/genai-research/reports/NVIDIA-Blackwell-GPU-architecture-Unleashing-next-gen-AI-performance--VmlldzoxMjgwODI4Mw">NVIDIA Blackwell GPU architecture : Unleashing next‑gen AI...</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#AGI`, `#GPT-6`, `#NVIDIA`, `#OpenAI`, `#AI training infrastructure`

---

<a id="item-5"></a>
## [华为时隔六年发布新款高性能芯片](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

2026 年 9 月 7 日，华为在广州发布 Mate XT 2 三折叠手机，搭载最新的麒麟 9050 Pro 芯片。这是华为时隔六年推出的首款全新高性能芯片，并首次采用逻辑折叠技术。 此次发布标志着华为在时隔六年后重返高性能芯片市场，可能重塑移动半导体的竞争格局。逻辑折叠技术的引入有望引领芯片设计新趋势，尤其是在地缘政治限制持续影响中国半导体产业的背景下。 麒麟 9050 Pro 由海思设计，中芯国际采用 N+3P 工艺代工。该芯片采用逻辑折叠技术，在单芯片内将逻辑单元分层排布，并增设垂直互联通道，从而缩短信号传输路径、降低时延并提升性能。

telegram · zaihuapd · Sep 7, 08:20

**背景**: 逻辑折叠技术是华为于 2026 年 5 月在上海举行的 ISCAS 2026 上，与“韬(τ)定律”一同提出的半导体创新技术。该技术属于三维集成电路（3D IC）与先进封装范畴，旨在通过“时间缩微”替代“几何缩微”来延续性能提升。麒麟 9050 Pro 是首款落地该技术的消费级芯片，标志着芯片设计从平面走向立体堆叠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zhihu.com/question/2080313467005939789">华为时隔六年再发高性能芯片麒麟9050 Pro，采用逻辑折叠技术，如何看...</a></li>
<li><a href="https://www.guancha.cn/economy/2026_09_07_830304.shtml">华为发布首款采用逻辑折叠技术的麒麟芯片</a></li>
<li><a href="https://baike.baidu.com/item/逻辑折叠技术/67870423">逻辑折叠技术 - 百度百科</a></li>
<li><a href="https://xueqiu.com/7227104507/408385272">华为麒麟9050 Pro芯片技术解析：架构、能效与竞品对比 本文基于公开评...</a></li>
<li><a href="https://www.eet-china.com/news/202609076952.html">华为时隔六年旗舰发布会详解麒麟芯片，麒麟9050 Pro首发“韬定律”技术</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#chip`, `#semiconductor`, `#Kirin`, `#technology`

---

<a id="item-6"></a>
## [最高法发布 AI 纠纷司法解释，明确换脸与算法杀熟责任](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 8.0/10

2026 年 9 月 7 日，最高人民法院发布关于人工智能纠纷案件的司法解释，共 24 条，涵盖 AI 换脸、算法杀熟、未经授权的 AI 冒充代言、自动驾驶和知识产权等问题。解释明确，未经同意使用 AI 制作可识别的人脸或声音可能构成人格权侵权，算法价格歧视侵害消费者权益的应承担责任。 这是中国首个关于 AI 纠纷的全面司法解释，为新兴 AI 相关损害提供了明确的法律规则，并为 AI 监管树立了先例。它将影响科技公司、平台运营者和个人，可能塑造中国乃至全球的行业实践和消费者保护标准。 该解释明确将“算法价格歧视”（大数据杀熟）和“网络开盒”（人肉搜索）列为可追责行为。它还支持对利用 AI 冒充他人诱导消费的行为适用惩罚性赔偿，并规制利用 AI 侵害隐私权的行为。

telegram · zaihuapd · Sep 7, 09:32

**背景**: AI 技术如深度伪造和算法定价引发了关于人格权、消费者保护和隐私的法律问题。在中国，民法典和个人信息保护法等法律提供了基本原则，但缺乏具体的司法指导。该解释填补了这一空白，详细规定了 AI 相关纠纷的责任规则，与全球 AI 监管努力保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.court.gov.cn/zixun/xiangqing/435431.html">“AI换脸”技术的应用风险及其规制引导 - 中华人民共和国最高人民法院</a></li>
<li><a href="https://finance.sina.com.cn/tech/roll/2025-01-22/doc-inefuhup8228832.shtml">未经同意拿他人肖像AI换脸？法院：侵权！|AI换脸_新浪科技_新浪网</a></li>
<li><a href="https://www.163.com/dy/article/L68UCBPS0519DDQ2.html">被AI换脸、遭“ 网 络 开 盒 ”？最高 法 明确裁判规则</a></li>

</ul>
</details>

**社区讨论**: 新闻中未提供社区评论，但根据搜索结果，讨论可能聚焦于该解释对 AI 公司和用户权益的影响，一些人赞赏其带来的明确性，而另一些人可能质疑执行上的挑战。

**标签**: `#AI regulation`, `#legal`, `#China`, `#deepfakes`, `#algorithmic fairness`

---