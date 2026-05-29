---
layout: default
title: "Horizon Summary: 2026-05-29 (ZH)"
date: 2026-05-29
lang: zh
---

> From 27 items, 8 important content pieces were selected

---

1. [vLLM v0.22.0：DeepSeek V4 成熟、MRv2 进展、Rust 前端](#item-1) ⭐️ 8.0/10
2. [AI 是否在重蹈前端失去的十年？](#item-2) ⭐️ 8.0/10
3. [GTA 6 开发者在 Rockstar Games 成立工会](#item-3) ⭐️ 8.0/10
4. [Anthropic 年化收入达 470 亿美元](#item-4) ⭐️ 8.0/10
5. [Anthropic 估值超越 OpenAI](#item-5) ⭐️ 8.0/10
6. [研究者披露印度 CBSE 高考阅卷系统多项漏洞](#item-6) ⭐️ 8.0/10
7. [中国首次认证 9 款国产 AI 芯片纳入政府采购目录](#item-7) ⭐️ 8.0/10
8. [蓝色起源新格伦火箭静态点火测试爆炸](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0：DeepSeek V4 成熟、MRv2 进展、Rust 前端](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 8.0/10

vLLM v0.22.0 版本包含来自 230 位贡献者的 459 次提交，使 DeepSeek V4 支持趋于成熟，推动 Model Runner V2 成为默认选项，并引入了实验性的 Rust 前端。 此版本显著提升了广泛使用的 vLLM 引擎的推理性能与模型支持，惠及在生产环境中部署大语言模型的开发者。Rust 前端和 Model Runner V2 的增强标志着向更高效、更模块化的推理基础设施的转变。 DeepSeek V4 获得了 NVFP4 融合 MoE 支持、完整及分段 CUDA 图以及 MTP 推测解码。Model Runner V2 现在自动为 Qwen3 密集模型选择，并在存在 KV 连接器时回退到 MRv1。实验性 Rust 前端包含用于数据并行服务的 DP Supervisor。

github · khluu · May 29, 10:28

**背景**: vLLM 是一个高性能的大语言模型推理引擎，以其速度和灵活性被广泛使用。Model Runner V2 是对 vLLM 执行核心的彻底重写，旨在实现更清晰的代码和更好的性能。Rust 前端是一项旨在提高服务效率的实验性工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm-project.github.io/2026/03/24/mrv2.html">Model Runner V2: A Modular and Faster Core for vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek V4`, `#Model Runner V2`, `#Rust frontend`

---

<a id="item-2"></a>
## [AI 是否在重蹈前端失去的十年？](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/) ⭐️ 8.0/10

一篇博客文章和社区讨论指出，AI 工具可能正在贬低前端专业知识，类似于框架曾经使该领域去技能化，让经验不足的开发者能够产出低质量的工作。 这场辩论凸显了 Web 开发中可访问性与质量之间的关键张力，影响着行业如何评估深度专业知识与广泛参与的价值。 文章引用了 Alex Russell 的术语“前端失去的十年”来描述框架如何减少对深度专业知识的需求，而评论者反驳说，这些专业知识大多处理的是偶然复杂性，而非本质复杂性。

hackernews · xyzal · May 29, 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48321631)

**背景**: 在软件工程中，“偶然复杂性”指由工具或实现产生的问题，而非问题本身固有的。“前端失去的十年”描述了 jQuery 和 React 等框架抽象掉浏览器差异的时期，使开发更容易，但减少了对浏览器深度知识的需求。AI 工具现在类似地抽象掉编码细节，引发了关于去技能化的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/">Is AI causing a repeat of Frontend ’s Lost Decade ? | Mastro Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/No_Silver_Bullet">No Silver Bullet - Wikipedia</a></li>
<li><a href="https://aiespionage.net/tech-deep-dives/is-ai-causing-a-repeat-of-front-end-s-lost-decade/">Is AI causing a repeat of Front end 's Lost Decade ? - AI Espionage</a></li>

</ul>
</details>

**社区讨论**: kristianc 和 kangalioo 等评论者认为，失去的专业知识大多是偶然复杂性，而更广泛的构建机会是净正面。ElProlactin 指出，AI 之前的工作往往平庸，因此质量担忧可能被夸大。

**标签**: `#AI`, `#frontend`, `#web development`, `#software engineering`

---

<a id="item-3"></a>
## [GTA 6 开发者在 Rockstar Games 成立工会](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/) ⭐️ 8.0/10

在 Rockstar Games 参与《侠盗猎车手 VI》开发的员工宣布成立工会，要求薪酬透明、灵活工作安排以及结束加班文化。 这一在全球最大游戏工作室之一的工会化努力，可能为游戏及更广泛的科技行业的劳工组织树立先例，有望改善工作条件和产品质量。 工会的要求集中在三个关键问题上：解决薪酬差距的薪酬透明、灵活工作政策，以及消除加班文化——游戏开发中常见的强制加班，通常每周工作 65-80 小时。

hackernews · AndrewKemendo · May 29, 15:32 · [社区讨论](https://news.ycombinator.com/item?id=48324499)

**背景**: 加班文化是电子游戏行业中普遍存在的做法，要求开发者长时间加班（通常无薪）以赶项目截止日期。科技行业的工会化历来较低，但近期的裁员和职业倦怠重新激发了人们对集体谈判的兴趣。Rockstar Games 过去曾因加班文化受到批评，尤其是在《荒野大镖客：救赎 2》的开发期间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crunch_(video_games)">Crunch (video games) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unionization_in_the_tech_sector">Unionization in the tech sector - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对工会的强烈支持，指出游戏开发者薪酬与其他技术岗位之间的差距，并强调了加班文化的剥削性质。一些人讨论了科技行业工会化的挑战，如外包和 H-1B 签证计划，但总体情绪积极，希望工会能改善工人条件和游戏质量。

**标签**: `#labor`, `#gaming`, `#unionization`, `#tech industry`, `#crunch culture`

---

<a id="item-4"></a>
## [Anthropic 年化收入达 470 亿美元](https://simonwillison.net/2026/May/29/anthropic/#atom-everything) ⭐️ 8.0/10

Anthropic 在 H 轮融资公告中宣布，其年化收入于 2026 年 5 月突破 470 亿美元，高于 4 月的 300 亿美元和 2025 年底的 90 亿美元。 这种快速的收入增长——大约五个月内从 90 亿美元增至 470 亿美元——表明企业大规模采用 AI，并验证了 Anthropic 的商业模式，可能影响投资者信心和行业基准。 年化收入是将最近一个月的收入乘以 12 得出的年度化预测。Anthropic 在多次融资公告中分享了这些数字，对投资者撒谎将构成证券欺诈，因此这些数字具有可信度。

rss · Simon Willison · May 29, 01:23

**背景**: 年化收入是一种财务指标，将当前收入外推至全年，通常被快速增长的公司用于预测年度业绩。Anthropic 是一家以 Claude 模型闻名的 AI 公司，已进行多轮大规模融资，包括以 9650 亿美元投后估值融资 650 亿美元的 H 轮。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post-money ...</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/accounting/revenue-run-rate/">Revenue Run Rate - Definition, Calculation, Examples</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">Run Rate Explained: Benefits, Risks, and Business Insights</a></li>

</ul>
</details>

**社区讨论**: 文章作者指出，一些怀疑论者认为此前 300 亿美元的数字不可信，但作者辩称在融资公告中撒谎将构成证券欺诈。Ed Zitron 对 300 亿美元的数字极为怀疑，作者想知道他是否会针对 470 亿美元的数字更新看法。

**标签**: `#Anthropic`, `#AI industry`, `#revenue`, `#funding`, `#business metrics`

---

<a id="item-5"></a>
## [Anthropic 估值超越 OpenAI](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) ⭐️ 8.0/10

Anthropic 完成一轮 650 亿美元融资，投后估值达到 9650 亿美元，超过 OpenAI 约 8520 亿美元的估值，成为估值最高的 AI 初创公司。 这一里程碑标志着 AI 初创公司格局的重大转变，凸显了资本和人才的激烈竞争，并表明市场对 Anthropic 安全 AI 发展路径的信心。 Anthropic 旗下产品包括 Claude 系列模型，该公司持续获得大额融资。资金主要用于算力、模型训练和商业化扩张。

telegram · zaihuapd · May 29, 03:29

**背景**: Anthropic 是一家由前 OpenAI 员工创立的 AI 安全初创公司，专注于构建可靠且可解释的 AI 系统。OpenAI 是 ChatGPT 的创造者，长期以来一直是 AI 初创领域的主导者。此次估值对比反映了 AI 公司的快速增长和投资者的热情。

**标签**: `#AI`, `#funding`, `#valuation`, `#Anthropic`, `#OpenAI`

---

<a id="item-6"></a>
## [研究者披露印度 CBSE 高考阅卷系统多项漏洞](https://ni5arga.com/blog/posts/hacking-cbse/) ⭐️ 8.0/10

一名安全研究人员披露了印度 CBSE 高考网上阅卷系统的多项严重漏洞，包括硬编码主密码、OTP 绕过和 SQL 注入，可能导致未经授权的分数篡改。 这些漏洞可能危及影响数百万学生的高利害性统考的公正性，凸显了政府 IT 系统的系统性安全缺陷以及负责任披露面临的挑战。 研究人员于 2026 年 2 月 25 日向 CERT-In 报告了这些问题，但 CBSE 最初否认存在漏洞；研究人员随后提供了截图，并在网站下线前发现了 SQL 注入问题。

telegram · zaihuapd · May 29, 05:52

**背景**: CBSE（印度中央中等教育委员会）为印度数百万学生举办高利害性的统考。网上阅卷系统供阅卷员评估答卷。硬编码密码和客户端 OTP 验证等漏洞可能允许攻击者绕过身份验证并修改分数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CERT-In">CERT-In</a></li>
<li><a href="https://medium.com/@mr.nt09/how-i-discovered-and-bypassed-otp-verification-an-exciting-journey-e1203f5bb900">How I Discovered and Bypassed OTP Verification: An... | Medium</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability disclosure`, `#web application`, `#education`, `#India`

---

<a id="item-7"></a>
## [中国首次认证 9 款国产 AI 芯片纳入政府采购目录](https://www.tomshardware.com/tech-industry/semiconductors/china-certifies-nine-domestic-ai-chips-for-government-procurement) ⭐️ 8.0/10

中国信息安全测评中心首次在安全认证框架下新增“AI 训练与推理芯片”品类，共 9 款国产 AI 处理器通过认证，可用于政府采购。认证厂商包括华为、阿里平头哥、壁仞科技和海光等，而寒武纪和百度昆仑芯未出现在名单中。 这标志着重大政策转变，将直接影响政府和国有企业的 AI 采购，推动国产芯片发展，并可能重塑竞争格局。同时，在美国对先进半导体实施出口限制的背景下，此举凸显了中国推动技术自主的决心。 认证有效期为三年，依据《安全可靠测评工作指南（试行）》进行。九款认证芯片来自多家厂商，但寒武纪和百度昆仑芯的缺席表明，并非所有国产 AI 芯片都满足所需的安全可靠标准。

telegram · zaihuapd · May 29, 08:41

**背景**: “安可”安全采购目录是中国政府批准的、供政府机构和国有企业使用的安全可靠 IT 产品清单。该目录最初涵盖 CPU、操作系统和数据库，现已扩展至 AI 芯片。此举符合中国减少对外国技术依赖的总体战略，尤其是在美国对 NVIDIA A100 和 H100 等先进 AI 芯片实施制裁之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.itsec.gov.cn/aqkkcp/cpgg/202405/t20240520_172866.html">安全可靠测评结果公告（2024年第1号）</a></li>
<li><a href="https://www.cnblogs.com/Magiclala/p/19913570">2026信创目录（信创国产化入围名单）：中国信息安全测评中心安全可靠...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1954867567723258004">安可测评9月更新！国产CPU、操作系统、数据库选型全清单</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#China`, `#government procurement`, `#semiconductors`, `#policy`

---

<a id="item-8"></a>
## [蓝色起源新格伦火箭静态点火测试爆炸](https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/) ⭐️ 8.0/10

2026 年 5 月 28 日，蓝色起源公司的新格伦火箭在卡纳维拉尔角进行静态点火测试时发生爆炸，火箭完全损毁，发射台也遭到破坏。爆炸发生在点燃一级火箭的七台 BE-4 甲烷发动机过程中，导致火箭和地面基础设施全部报废。 此次爆炸对蓝色起源是一次重大打击，不仅推迟了其复飞计划，还危及 NASA 阿尔忒弥斯登月任务和亚马逊 Project Kuiper 卫星部署。该事件也引发了对 BE-4 发动机可靠性的担忧，该发动机同样用于联合发射联盟的 Vulcan 火箭。 爆炸发生在 NG-4 任务准备阶段，该任务原计划发射 48 颗亚马逊 Kuiper 卫星。发射台的闪电防护塔倒塌，地面基础设施严重受损，但无人员伤亡。蓝色起源尚未公布恢复时间表或调查结果。

telegram · zaihuapd · May 29, 11:08

**背景**: 新格伦是蓝色起源的重型轨道火箭，由七台 BE-4 发动机提供动力，使用液氧和液化天然气（甲烷）作为燃料。BE-4 是美国首款富氧分级燃烧发动机，也用于 ULA 的 Vulcan 火箭。蓝色起源此前刚获 FAA 批准复飞，此次静态点火测试旨在为下一次发射验证火箭状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/science/2026/may/29/blue-origin-rocket-explodes">Blue Origin rocket explodes during test in latest setback for Jeff Bezos-owned company | Blue Origin | The Guardian</a></li>
<li><a href="https://www.cnn.com/2026/05/28/science/blue-origin-rocket-anomaly">Blue Origin rocket explodes during ground test | CNN</a></li>
<li><a href="https://en.wikipedia.org/wiki/BE-4">BE-4 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Blue Origin`, `#New Glenn`, `#rocket explosion`, `#NASA Artemis`, `#space industry`

---