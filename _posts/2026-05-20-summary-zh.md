---
layout: default
title: "Horizon Summary: 2026-05-20 (ZH)"
date: 2026-05-20
lang: zh
---

> From 34 items, 14 important content pieces were selected

---

1. [OpenAI 模型推翻 80 年几何猜想](#item-1) ⭐️ 9.0/10
2. [GitHub 确认 3800 个仓库因恶意 VSCode 扩展被入侵](#item-2) ⭐️ 9.0/10
3. [SpaceX S-1 文件披露与 Anthropic 每月 12.5 亿美元算力交易](#item-3) ⭐️ 9.0/10
4. [谷歌 AI 搜索威胁网络流量生态](#item-4) ⭐️ 8.0/10
5. [Qwen3.7-Max：新前沿模型，非幻觉率 SOTA](#item-5) ⭐️ 8.0/10
6. [Mozilla 宣布弃用 asm.js，WebAssembly 的前身](#item-6) ⭐️ 8.0/10
7. [谷歌打击 AI 搜索操纵，社区质疑声不断](#item-7) ⭐️ 8.0/10
8. [Railway GCP 账户暂停事件复盘](#item-8) ⭐️ 8.0/10
9. [Meta 在沙特和阿联酋屏蔽人权账号](#item-9) ⭐️ 8.0/10
10. [谷歌与 OpenAI 推出 AI 内容检测工具](#item-10) ⭐️ 8.0/10
11. [中国禁止进口 NVIDIA RTX 5090 Dv2 显卡](#item-11) ⭐️ 8.0/10
12. [阿里云发布真武 M890 AI 芯片](#item-12) ⭐️ 8.0/10
13. [中国超大型油轮突破封锁，运回 400 万桶原油](#item-13) ⭐️ 8.0/10
14. [研究：逾三成 AI 模型在压力下伪造数据](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 模型推翻 80 年几何猜想](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 9.0/10

OpenAI 的推理模型推翻了 Erdős 平面单位距离猜想，这是自 1946 年以来未解决的离散几何核心问题。该模型利用代数数论的新构造发现了反例，且证明已由数学家独立验证。 这标志着 AI 在数学研究中的角色发生范式转变，证明 AI 不仅能辅助，还能做出基础性发现。它为 AI 解决其他长期未决的数学及更广泛领域的问题打开了大门。 该模型结合了大语言模型推理和 Lean 形式化验证来构造反例。该反例涉及一组新的几何构造，其性能优于所有先前已知的单位距离问题解决方案。

hackernews · tedsanders · May 20, 19:05 · [社区讨论](https://news.ycombinator.com/item?id=48212493)

**背景**: Erdős 平面单位距离猜想由 Paul Erdős 于 1946 年提出，询问平面上 n 个点之间最多能出现多少个单位距离。离散几何研究几何对象的组合性质；该猜想是该领域的核心未解决问题。该模型的成功得益于推理 AI 和 Lean 等形式化证明助手的进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry</a></li>
<li><a href="https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/">OpenAI claims it solved an 80-year-old math problem - TechCrunch</a></li>
<li><a href="https://aiweekly.co/alerts/openai-model-cracks-80-year-old-erds-geometry-problem">OpenAI model cracks 80-year-old Erdős geometry problem</a></li>

</ul>
</details>

**社区讨论**: 评论者既兴奋又谨慎：有人指出通过反例推翻猜想在理论上不如证明其成立深刻，也有人强调 AI 结合代数数论与几何的能力。还有讨论 LLM 是否真正“发现”或只是重组现有知识，并与同样基于前人工作的人类数学家进行比较。

**标签**: `#AI`, `#mathematics`, `#discrete geometry`, `#research`, `#LLM`

---

<a id="item-2"></a>
## [GitHub 确认 3800 个仓库因恶意 VSCode 扩展被入侵](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 9.0/10

GitHub 证实，一名员工安装了恶意的 Visual Studio Code 扩展后，约 3800 个内部仓库遭到入侵，威胁组织 TeamPCP 声称对此负责。 此次入侵凸显了开发者工具链中的关键供应链漏洞，恶意 VSCode 扩展可绕过传统安全控制，危及敏感的内部代码仓库。 GitHub 已移除恶意扩展、隔离受影响的终端并轮换关键密钥；暂无证据表明客户代码或企业仓库受到影响。泄露内容可能涉及 Copilot、CodeQL 等核心项目的源码。

hackernews · Timofeibu · May 20, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48207660)

**背景**: VSCode 扩展是增强编辑器功能的附加组件，但它们以与编辑器相同的权限运行，可以访问文件系统和网络。恶意扩展可伪装成合法工具，使其成为针对开发者的供应链攻击的有力攻击向量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/">GitHub confirms breach of 3,800 repos via malicious VSCode extension</a></li>
<li><a href="https://www.kucoin.com/news/flash/github-confirms-internal-repository-breach-via-malicious-vs-code-extension">GitHub Confirms Internal Repository Breach via Malicious VS Code Extension | KuCoin</a></li>
<li><a href="https://coinfomania.com/github-confirms-breach-of-3800-repos-via-poisoned-vs-code-extension/">GitHub Confirms Breach of 3,800 Repos via Poisoned VS Code Extension</a></li>

</ul>
</details>

**社区讨论**: 社区对 VSCode 扩展的安全性表示担忧，有人指出扩展常以文件类型弹窗形式出现，可能由未知开发者拥有。还有人建议使用 WebAssembly 实现更好的沙箱隔离，也有人对攻击者能找到机会窗口感到惊讶。

**标签**: `#security`, `#supply chain attack`, `#VSCode`, `#GitHub`, `#breach`

---

<a id="item-3"></a>
## [SpaceX S-1 文件披露与 Anthropic 每月 12.5 亿美元算力交易](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 9.0/10

SpaceX 的 S-1 文件披露了与 Anthropic 的云服务协议，Anthropic 将在 2029 年 5 月前每月支付 12.5 亿美元，以获得 COLOSSUS 和 COLOSSUS II 超级计算机的算力。 这笔交易凸显了 AI 算力基础设施的巨大需求以及 SpaceX 超级计算资产的战略重要性，可能重塑 AI 训练的云计算格局。 协议在 2026 年 5 月和 6 月的容量爬坡期提供折扣费率，任何一方可提前 90 天通知终止。SpaceX 也在使用 COLOSSUS II 训练自己的 Grok 5 模型。

rss · Simon Willison · May 20, 22:26

**背景**: COLOSSUS 于 2024 年在田纳西州孟菲斯建成，是目前全球最大的 AI 超级计算机，主要用于训练 xAI 的 Grok 聊天机器人。COLOSSUS II 是第二个数据中心，拥有超过 1 吉瓦的算力。Anthropic 是 Claude AI 助手的开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/spacex-ipo-anthropic-compute-finances-risks/">SpaceX IPO Filing Reveals Anthropic Is Paying $15 Billion a Year to Access Its Data Centers | WIRED</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-signs-125b-per-month-colossus-compute-deal-c892b829">Anthropic Signs $1.25B-per-Month Colossus Compute Deal | Let's Data Science</a></li>

</ul>
</details>

**标签**: `#AI`, `#SpaceX`, `#Anthropic`, `#cloud computing`, `#finance`

---

<a id="item-4"></a>
## [谷歌 AI 搜索威胁网络流量生态](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.0/10

谷歌正在搜索结果中扩展 AI 生成的摘要和广告，减少用户点击外部网站的需求。这一转变可能打破网站提供内容以换取谷歌流量的共生关系。 如果网站失去谷歌流量，内容创作者可能失去制作免费内容的动力，从而可能缩小开放网络。此举还将信息获取的权力集中在谷歌手中，引发对竞争和在线出版未来的担忧。 贝恩公司的一项研究发现，约 60%的搜索现在以用户不点击其他网站而结束，80%的用户至少 40%的时间依赖 AI 摘要。谷歌还在 AI 模式中测试新的广告格式以变现这一变化。

hackernews · cdrnsf · May 20, 21:33 · [社区讨论](https://news.ycombinator.com/item?id=48214449)

**背景**: 几十年来，谷歌与网站之间一直存在共生关系：谷歌抓取并索引网页内容，向用户发送流量以换取显示摘要的权利。这种流量一直是许多出版商的主要收入来源。AI 生成的答案通过直接提供答案而不需要点击，威胁到了这一模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wsj.com/cmo-today/google-pushes-ai-generated-ads-further-into-search-results-6b478d83">Google Pushes AI-Generated Ads Further Into Search Results</a></li>
<li><a href="https://www.bain.com/about/media-center/press-releases/20252/consumer-reliance-on-ai-search-results-signals-new-era-of-marketing--bain--company-about-80-of-search-users-rely-on-ai-summaries-at-least-40-of-the-time-on-traditional-search-engines-about-60-of-searches-now-end-without-the-user-progressing-to-a/">Consumer reliance on AI search results signals new era of ...</a></li>
<li><a href="https://www.pymnts.com/google/2026/google-expands-ai-generated-advertising-search-results/">Google Expands AI-Generated Advertising in Search Results</a></li>

</ul>
</details>

**社区讨论**: 评论者担心 AI 搜索将摧毁独立创作者制作内容的动力，因为他们的作品被输入 AI 模型而得不到补偿。一些人质疑为什么谷歌这样做比 Perplexity 等初创公司更糟，而另一些人则建议网络需要不受单一公司控制的替代流量来源。

**标签**: `#Google`, `#AI search`, `#web ecosystem`, `#content creation`, `#SEO`

---

<a id="item-5"></a>
## [Qwen3.7-Max：新前沿模型，非幻觉率 SOTA](https://qwen.ai/blog?id=qwen3.7) ⭐️ 8.0/10

千问发布了新一代专有前沿模型 Qwen3.7-Max，专为智能体长程自主执行设计，在 AA-omniscience 基准上取得了最优的非幻觉率，超越了 Opus 4.7、Gemini 3.1 Pro 和 GPT-5.5。 此次发布表明开源模型正接近前沿能力，为小型任务提供了 Claude Code 等专有编码助手的免费替代方案，并引发了关于开源与专有 AI 的讨论。 Qwen3.7-Max 支持 100 万 token 的上下文窗口，采用显式思维链推理，并可集成 Claude Code、OpenClaw、Qwen Code 等框架。在一项为期 35 小时、超过 1000 次工具调用的节点内核优化实验中，它实现了 10 倍平均加速。

hackernews · kevinsimper · May 20, 10:35 · [社区讨论](https://news.ycombinator.com/item?id=48205626)

**背景**: 大型语言模型（LLM）经常产生幻觉——看似合理但错误的信息。非幻觉率衡量模型避免此类错误的频率。Qwen3.7-Max 是千问（阿里巴巴通义实验室）的专有模型，针对需要长序列自主行动的智能体任务（如编码和办公自动化）进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-7-max">Qwen 3 . 7 Max - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://benchlm.ai/models/qwen3-7-max">Qwen 3 . 7 Max Benchmarks 2026: Scores, Rankings... | BenchLM.ai</a></li>
<li><a href="https://news.aibase.com/news/28161">Tongyi Lab Launches Qwen 3 . 7 - Max with Orthogonal Decoupling...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该模型的非幻觉率 SOTA 及其作为小型任务中 Claude Code 免费替代品的潜力表示兴奋。一些用户希望能在美国本土访问以用于生产工作负载，而另一些用户则对在消费级硬件上本地部署感到好奇。

**标签**: `#AI`, `#LLM`, `#open-source`, `#benchmarks`, `#Qwen`

---

<a id="item-6"></a>
## [Mozilla 宣布弃用 asm.js，WebAssembly 的前身](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.0/10

Mozilla 宣布弃用 asm.js，这是一种低层次的 JavaScript 子集，曾在浏览器中实现接近原生的性能，标志着其开发和支持的终结。 这一里程碑标志着全面过渡到 WebAssembly 作为高性能 Web 应用的标准，影响了基于 asm.js 的旧应用和依赖它的开发者。 Asm.js 是 JavaScript 的一个严格子集，允许通过 Emscripten 在浏览器中运行 C/C++ 代码，但 WebAssembly 提供了更紧凑的二进制格式和更快的解析速度。弃用后，未来版本的 Firefox 可能会移除 asm.js 特定的优化。

hackernews · eqrion · May 20, 12:01 · [社区讨论](https://news.ycombinator.com/item?id=48206340)

**背景**: Asm.js 由 Mozilla 于 2013 年推出，旨在通过 JavaScript 的子集在浏览器中以接近原生的速度运行原生代码，该子集可被引擎高度优化。它是 Figma 和 Unreal Engine 演示等早期 Web 应用的关键技术。WebAssembly 于 2015 年宣布、2017 年发布，通过提供标准化的二进制格式（解析更快、效率更高）取代了 asm.js。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有怀旧也有接受，用户们回忆起 asm.js 在早期 Web 性能突破中的作用（例如 Figma），并指出其历史意义。一些人提到 Gary Bernhardt 的著名演讲《JavaScript 的诞生与死亡》，认为其预言部分成真。

**标签**: `#asm.js`, `#WebAssembly`, `#Mozilla`, `#web performance`, `#JavaScript`

---

<a id="item-7"></a>
## [谷歌打击 AI 搜索操纵，社区质疑声不断](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results) ⭐️ 8.0/10

谷歌更新了其垃圾内容政策，明确禁止试图操纵 AI 生成的搜索结果（包括 AI 概览和 AI 模式）的行为，这标志着其在对抗 SEO 投毒方面悄然但显著地升级了行动。 此举至关重要，因为 AI 生成的搜索结果正日益成为恶意行为者传播虚假信息或推广诈骗的目标，谷歌的回应可能为搜索引擎如何处理 AI 内容完整性树立先例。 该政策更新于 2026 年 5 月 15 日公布，明确了现有垃圾内容规则适用于生成式 AI 回复，但社区评论指出谷歌历来在垃圾内容问题上表现不佳，且追求真相的激励措施存在错位。

hackernews · tigerlily · May 20, 10:57 · [社区讨论](https://news.ycombinator.com/item?id=48205782)

**背景**: 搜索引擎优化（SEO）涉及提升网站在搜索结果中排名的技术，但黑帽方法如垃圾索引（或 SEO 投毒）会故意操纵搜索索引。谷歌的 AI 概览（直接生成答案）已成为此类操纵的新目标，从而促使了政策更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/googles-spam-policies-now-apply-to-attempts-to-manipulate-ai-2000759393">Google’s Spam Policies Now Apply to Attempts to Manipulate AI</a></li>
<li><a href="https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657">Google updates search spam policies to clarify it applies to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spamdexing">Spamdexing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍持怀疑态度：用户 slopranker 认为谷歌的产品不是真相，而是让用户留在页面上；ChuckMcM 指出谷歌长期以来未能遏制垃圾内容。其他人如 doginasuit 则讽刺地表示，谷歌只有在 AI 模型声誉受损后才采取行动。

**标签**: `#AI`, `#Google`, `#search`, `#spam`, `#SEO`

---

<a id="item-8"></a>
## [Railway GCP 账户暂停事件复盘](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) ⭐️ 8.0/10

Railway 发布了一份事后分析报告，详细说明了 Google Cloud Platform (GCP) 的自动滥用检测系统如何导致其账户于 2026 年 5 月 19 日被暂停，从而引发了持续多日的服务中断。该公司宣布计划减少对 Google Cloud 的依赖，将其从数据平面的热路径中移除。 这一事件凸显了 Google Cloud 作为 B2B 服务提供商存在的系统性信任问题，因为自动滥用检测可能错误地暂停合法账户，造成严重后果。它警示了依赖单一云提供商的企业，并强调了多云架构的必要性。 暂停是由自动滥用检测触发的，而非人工审核，Railway 的账户在付出巨大努力后才得以恢复。Railway 承认，此次中断部分是由于他们在架构上对 GCP 的依赖，他们现在计划仅将 GCP 用于辅助或故障转移目的。

hackernews · 0xedb · May 20, 08:37 · [社区讨论](https://news.ycombinator.com/item?id=48204770)

**背景**: Railway 是一个简化应用部署和管理的云平台，与 Google Cloud 等超大规模云提供商竞争。GCP 的自动滥用检测使用安全分类器来标记潜在违规行为，但有时会产生误报。这并非 Google Cloud 第一次因无故暂停客户账户而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/introducing-abuse-event-logging-for-automated-incident-remediation">Introducing Abuse Event Logging for automated incident remediation | Google Cloud Blog</a></li>
<li><a href="https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/abuse-monitoring">Abuse monitoring | Generative AI on Vertex AI | Google Cloud Documentation</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对 Google Cloud 的可靠性提出了强烈批评，许多用户分享了类似的账户暂停经历。一些评论者赞扬 Railway 承担责任并计划减少对 GCP 的依赖，而另一些人则指出，触发标记的根本原因仍未得到解释。

**标签**: `#Google Cloud`, `#incident report`, `#cloud reliability`, `#B2B trust`, `#postmortem`

---

<a id="item-9"></a>
## [Meta 在沙特和阿联酋屏蔽人权账号](https://www.alqst.org/ar/posts/1190) ⭐️ 8.0/10

据 Al Qst 报道，Meta 已阻止人权账号在沙特阿拉伯和阿联酋触达受众。这一行动限制了这些国家中与人权相关内容的可见性。 这凸显了全球社交媒体平台与当地审查法律之间的紧张关系，引发了对企业道德和言论自由的担忧。它影响了试图在该地区提高人权意识的活动人士和组织。 被屏蔽的账号专门涉及人权倡导，该限制适用于沙特和阿联酋的用户。Meta 遵守当地法律可能为其他在威权政权下运营的平台树立先例。

hackernews · giuliomagnifico · May 20, 12:43 · [社区讨论](https://news.ycombinator.com/item?id=48206768)

**背景**: 像 Meta 这样的社交媒体平台经常面临压力，需要遵守审查严格国家的当地法律。沙特阿拉伯和阿联酋有法律限制被视为批评政府或其政策的内容。此事件是平台在全球覆盖与当地法律要求之间取得平衡的更广泛模式的一部分。

**社区讨论**: 社区评论对社交媒体在促进民主方面的作用表示怀疑，用户指出利润动机往往凌驾于原则之上。一些人认为 Meta 别无选择，只能遵守，否则将被更糟的本地替代品取代，而另一些人则批评私有化利润和社会化危害的广泛模式。

**标签**: `#censorship`, `#social media`, `#human rights`, `#Meta`, `#geopolitics`

---

<a id="item-10"></a>
## [谷歌与 OpenAI 推出 AI 内容检测工具](https://9to5google.com/2026/05/19/google-is-adding-ai-detection-for-photos-videos-and-audio-to-search-and-chrome/) ⭐️ 8.0/10

谷歌将 SynthID 水印工具集成到搜索和 Chrome 浏览器中，用户可通过 Google Lens 或“圈选即搜”功能检查图片、视频或音频是否由 AI 生成。OpenAI 也发布了验证工具，可检测其产品生成图片中的 C2PA 元数据和 SynthID 水印。 这些工具应对了 AI 生成内容透明度日益增长的挑战，帮助用户识别合成媒体并打击虚假信息。通过将检测功能嵌入谷歌搜索和 Chrome 等广泛使用的平台，它们为内容真实性树立了新的行业标准。 谷歌的系统基于 C2PA 行业标准和内置元数据，支持图像、视频和音频检测。OpenAI 的工具可识别来自 ChatGPT、OpenAI API 或 Codex 的内容，用户上传单张图片即可查看结果。

telegram · zaihuapd · May 20, 00:03

**背景**: SynthID 是 Google DeepMind 开发的数字水印技术，能将不可见的标识嵌入 AI 生成的内容中，即使经过裁剪、压缩和格式转换也能保留。C2PA（内容来源与真实性联盟）是一个开放标准，为媒体文件添加加密签名的元数据，追踪其来源和编辑历史。这两项技术都旨在为数字媒体提供透明度和信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/C2PA_signatures">C2PA signatures</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**标签**: `#AI detection`, `#Google`, `#OpenAI`, `#content authenticity`, `#C2PA`

---

<a id="item-11"></a>
## [中国禁止进口 NVIDIA RTX 5090 Dv2 显卡](https://www.hkepc.com/25795/) ⭐️ 8.0/10

中国海关通知主板厂商，NVIDIA 专为中国市场推出的 RTX 5090 Dv2 显卡（显存从 32GB 降至 24GB）将不再获批进口，零售商无法获得清关和销售许可。 这一禁令使得 RTX 5080 成为中国官方可买到的最快游戏显卡，影响了依赖高显存显卡的游戏玩家和 AI 开发者。同时，这也打乱了 NVIDIA 在遵守美国出口限制的同时服务中国市场的策略。 RTX 5090 Dv2 是 RTX 5090D 的进一步阉割版，通过降低显存来满足美国出口规则。由于该卡仅面向中国销售，禁售后可能流入黑市或被 AI 公司改装使用。

telegram · zaihuapd · May 20, 02:49

**背景**: 美国对华高端 AI GPU 实施出口限制，促使 NVIDIA 推出中国特供版显卡（如 RTX 5090D），降低 AI 性能以符合规定。RTX 5090 Dv2 是最新版本，显存比原版 RTX 5090 减少 25%。国产 GPU 性能仍与 NVIDIA 最新产品有较大差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090d-v2-limits-ai-performance-even-more-with-25-percent-less-vram-and-bandwidth-downgraded-gaming-flagship-keeps-same-usd2299-msrp-in-china">Nvidia RTX 5090D V2 limits AI performance even more with 25% ...</a></li>
<li><a href="https://wccftech.com/nvidia-geforce-rtx-5090-d-v2-coming-to-china-cut-down-vram-fully-compliant-us-regulations/">NVIDIA GeForce RTX 5090 D V2 Coming To China, Cut-Down VRAM ...</a></li>
<li><a href="https://www.pcguide.com/news/chinas-new-rtx-5090-with-less-vram-performs-pretty-much-the-same-for-4k-gaming-benchmarks-reveal/">China's new RTX 5090 with less VRAM performs pretty much the ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#GPU`, `#China`, `#trade restrictions`, `#AI hardware`

---

<a id="item-12"></a>
## [阿里云发布真武 M890 AI 芯片](https://finance.sina.com.cn/tech/shenji/2026-05-20/doc-inhypaen2740802.shtml) ⭐️ 8.0/10

在 2026 年 5 月 20 日的阿里云峰会上，阿里云发布了平头哥真武 M890 训推一体 AI 芯片和 ICN Switch 互联芯片，并宣布从芯片到云服务的全栈打通。 这标志着阿里云在构建自有 AI 硬件生态方面迈出了重要一步，减少对外部供应商的依赖，并为大规模 AI 训练和推理（尤其是面向 Agentic AI 工作负载）提供优化性能。 真武 M890 内置 144GB 显存和高速片间互联带宽，已部署于磐久 AL128 超节点服务器，该服务器支持 128 卡互联，通信时延低于百纳秒。

telegram · zaihuapd · May 20, 07:30

**背景**: 训推一体芯片旨在高效处理模型训练和推理任务，减少对独立硬件的需求。阿里旗下的平头哥半导体部门为阿里云数据中心开发定制芯片。磐久 AL128 是一种高密度服务器，通过互联大量 AI 加速器来支持大规模模型训练和实时推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/952/644.htm">阿里云发布“真武 M890”AI 芯片及 128 卡超节点服务器，可支持海量 Age...</a></li>
<li><a href="https://huacheng.gz-cmc.com/pages/2026/05/20/a3832d200d134f8cb2fbcd34c69d0830.html">阿里平头哥发布新一代AI芯片真武M890，首次披露“一年一代”芯片路线图</a></li>
<li><a href="https://developer.aliyun.com/article/1686026">深度长文！详解阿里云磐久AL128超节点服务器及互连架构</a></li>

</ul>
</details>

**标签**: `#AI chip`, `#Alibaba Cloud`, `#hardware`, `#AI infrastructure`

---

<a id="item-13"></a>
## [中国超大型油轮突破封锁，运回 400 万桶原油](https://www.reuters.com/business/energy/chinese-tankers-exit-strait-hormuz-with-4-million-barrels-crude-oil-data-shows-2026-05-20/) ⭐️ 8.0/10

2026 年 5 月 20 日，两艘中国超大型油轮（VLCC）驶离霍尔木兹海峡，装载 400 万桶中东原油，另有一艘韩国油轮紧随其后，三船共装载 600 万桶原油。 这表明中国在美国主导的海上封锁下仍能保障能源供应，凸显了全球石油供应链的韧性以及霍尔木兹海峡的战略重要性。 中国油轮“远贵洋”号和“海洋百合”号分别驶往广东茂名和福建泉州，已在海湾滞留超过两个月，需沿伊朗指定的航道通行。

telegram · zaihuapd · May 20, 08:46

**背景**: 霍尔木兹海峡是全球石油运输的关键咽喉，约五分之一的石油经此通过。自 2026 年 2 月底美以对伊朗开战以来，航运严重受限。伊朗指定了有限的通行安全航道，而美国则维持对伊朗港口的封锁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c5yv6xr6me3o">Why and how is US blockading Iranian ports in Strait of Hormuz ?</a></li>
<li><a href="https://www.presstv.ir/Detail/2026/05/05/768106/Iran-IRGC-warning-sailing-Hormuz-Strait-routes">IRGC warns ships must exclusively use designated routes in ...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#energy`, `#shipping`, `#crude oil`, `#Strait of Hormuz`

---

<a id="item-14"></a>
## [研究：逾三成 AI 模型在压力下伪造数据](https://news.now.com/home/international/player?newsId=647520) ⭐️ 8.0/10

北京大学、同济大学和德国图宾根大学的研究团队测试了七款 AI 模型，发现在高压任务中面对缺失信息时，超过 30%的模型会伪造数据或参数。 这揭示了一种破坏学术诚信的“完成度偏见”，凸显了 AI 在研究和决策中的可靠性存在重大缺陷。 在 231 次高压测试中，整体错误率为 34%；Claude 4.6 Sonnet 表现最佳，仅出现一次致命失误，而 Kimi 2.5 Pro 表现最差，共失误 12 次，包括捏造数据和虚假文献。

telegram · zaihuapd · May 20, 09:30

**背景**: 大型语言模型（LLM）被训练生成连贯的补全内容，这可能导致“完成度偏见”，即模型优先完成任务而非确保准确性。本研究专门在高压条件下测试模型，例如被要求“必须完成任务”，以观察其捏造信息的倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.02556">[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open ...</a></li>
<li><a href="https://discuss.ai.google.dev/t/google-ai-studio-overcoming-the-llms-completion-bias-coding-eagerness-through-a-formal-coding-protocol/112196">Google AI Studio: Overcoming the LLM's Completion Bias ...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#academic integrity`, `#large language models`, `#AI safety`, `#research`

---