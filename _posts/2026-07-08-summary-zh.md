---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> From 29 items, 14 important content pieces were selected

---

1. [TypeScript 7.0 发布，速度提升高达 11.9 倍](#item-1) ⭐️ 9.0/10
2. [OpenAI 宣布 GPT-5.6 本周四公开发布](#item-2) ⭐️ 9.0/10
3. [Mistral 发布 Robostral Navigate 实现无地图机器人导航](#item-3) ⭐️ 8.0/10
4. [OpenAI 推出 GPT-Live，支持 GPT-5.5 委派](#item-4) ⭐️ 8.0/10
5. [OpenBSD 释放后使用漏洞可本地提权至 root](#item-5) ⭐️ 8.0/10
6. [欧盟重启私人消息扫描规则](#item-6) ⭐️ 8.0/10
7. [Cloudflare Meerkat：首个生产级异步共识算法](#item-7) ⭐️ 8.0/10
8. [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](#item-8) ⭐️ 8.0/10
9. [SpaceXAI 明日发布 Grok 4.5](#item-9) ⭐️ 8.0/10
10. [顶尖 AI 企业安全评级普遍偏低，Anthropic 以 C+居首](#item-10) ⭐️ 8.0/10
11. [华为 5G 旗舰重返海外，峰值速率超 1100 Mbps](#item-11) ⭐️ 8.0/10
12. [安卓远程 Root 漏洞链曝光](#item-12) ⭐️ 8.0/10
13. [美团 OWL（LongCat）免费测试模型疑似泄露对话数据](#item-13) ⭐️ 8.0/10
14. [通过电磁信号识别手机应用，准确率达 99%](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 发布，速度提升高达 11.9 倍](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

微软发布了 TypeScript 7.0，这是一个重大版本更新，带来了显著的性能提升，在 VS Code 等大型代码库上实现了高达 11.9 倍的加速（从 125.7 秒降至 10.6 秒）。 此版本大幅缩短了大型 TypeScript 项目的编译时间，提高了开发者的生产力，并使 TypeScript 对更大的代码库更具可行性。这也表明了微软对该语言性能的持续投入。 在多个代码库上测量了加速效果：VS Code（11.9 倍）、Sentry（8.9 倍）、Bluesky（8.7 倍）、Playwright（8.7 倍）和 tldraw（7.7 倍）。但一些用户指出与 ts-jest 等工具存在兼容性问题，需要变通方案。

hackernews · DanRosenwasser · Jul 8, 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48833715)

**背景**: TypeScript 是 JavaScript 的类型超集，编译为纯 JavaScript，广泛用于大规模 Web 开发。性能一直是长期痛点，尤其是对于数百万行代码的项目。此版本专注于优化编译器和语言服务。

**社区讨论**: 社区普遍持积极态度，庆祝性能提升和团队的努力。然而，一些用户对与 ts-jest 等常用工具的兼容性以及为混合环境（例如带有 Node.js 工具链的 Web 应用）管理多个 tsconfig 文件的复杂性表示担忧。

**标签**: `#TypeScript`, `#performance`, `#programming languages`, `#Microsoft`

---

<a id="item-2"></a>
## [OpenAI 宣布 GPT-5.6 本周四公开发布](https://x.com/OpenAI/status/2074704958419792299) ⭐️ 9.0/10

OpenAI 宣布 GPT-5.6 系列（包括 Sol、Terra 和 Luna）将于 2026 年 7 月 9 日（本周四）公开发布，并立即在全球范围内扩大预览版访问权限。 此次发布标志着 AI 能力的重大飞跃，Sol 在推理、编程和网络安全方面树立了新标杆，可能重塑企业和开发者的工作流程。 Sol 是面向前沿推理和长期代理任务的旗舰模型，Terra 以比 GPT-5.5 低 2 倍的成本提供均衡性能，Luna 则是速度最快、价格最实惠的选项。

telegram · zaihuapd · Jul 8, 04:17

**背景**: GPT-5.6 是 OpenAI 大型语言模型系列的最新版本。三个模型——Sol、Terra 和 Luna——针对不同用例设计：Sol 用于高级推理和代理工作，Terra 作为高性价比通用模型，Luna 用于高速低成本推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/gpt-5-6-release-date-features-benchmarks-2026">GPT-5.6: Public Launch July 9 — Sol, Terra, Luna - explainx.ai</a></li>
<li><a href="https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna/1384931">Introducing GPT-5.6 series: Sol, Terra and Luna</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#OpenAI`, `#AI release`, `#large language model`

---

<a id="item-3"></a>
## [Mistral 发布 Robostral Navigate 实现无地图机器人导航](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI 发布了 Robostral Navigate，这是一个 80 亿参数的模型，仅通过单个 RGB 摄像头和自然语言指令就能让机器人在复杂环境中导航，在 R2R-CE 基准测试中达到 76.6% 的准确率，无需深度传感器、激光雷达或多摄像头。 这标志着 Mistral 首次正式涉足具身 AI，将其业务从语言模型扩展到物理系统，并且通过消除对昂贵传感器和预建地图的需求，可能降低机器人导航的成本和复杂性，惠及爱好者和研究人员。 该模型并未公开可用，限制了爱好者的实验；但它通过单摄像头实现无地图导航，解决了“绑架机器人”问题，这是相对于传统基于地图的方法的重大进步。

hackernews · ottomengis · Jul 8, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48832212)

**背景**: 无地图导航允许机器人在没有预建地图的情况下穿越未知环境，利用实时传感器数据避开障碍物并到达目标。传统方法通常依赖昂贵的传感器如激光雷达或多摄像头，而 Mistral 的模型仅使用单个 RGB 摄像头，使其更易获取。“绑架机器人”问题指机器人在不知情下被移动后失去定位，无地图方法可以克服这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://alphasignal.ai/news/mistral-s-robostral-navigate-beats-sensor-heavy-robots-with-just-one-camera">Mistral's Robostral Navigate Beats Sensor-Heavy Robots With ...</a></li>
<li><a href="https://www.siliconreport.com/mistral-ai-releases-robostral-navigate-a-single-camera-robotics-model-95dac18d">Mistral AI Releases Robostral Navigate, a Single-Camera ...</a></li>

</ul>
</details>

**社区讨论**: 社区对无地图导航能力及其在农场机器人等爱好者项目中的潜力感到兴奋，但对模型未公开可用感到失望。一些评论者指出，无地图户外导航早已存在，但室内无地图导航相对较新，他们推测其底层技术与斯坦福的 PIGEON 模型类似。

**标签**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-4"></a>
## [OpenAI 推出 GPT-Live，支持 GPT-5.5 委派](https://openai.com/index/introducing-gpt-live/) ⭐️ 8.0/10

OpenAI 推出了 GPT-Live，这是 ChatGPT 的一种新语音模式，可以在后台将复杂推理任务委派给 GPT-5.5，从而实现更自然、更高效的对话。该功能现已全球可用。 GPT-Live 弥合了语音交互与前沿推理之间的差距，使用户能够进行长时间、高效的对话，而不受旧语音模型的限制。这可能会显著增强 AI 辅助工作、头脑风暴和研究。 GPT-Live 可以将需要网络搜索或更复杂推理的问题委派给 GPT-5.5，后者在后台运行，同时对话继续进行。早期测试者报告了长达一小时的对话，并进行了有效的头脑风暴，但也有人指出工具集成方面的限制和偶尔的中断错误。

hackernews · logickkk1 · Jul 8, 17:03 · [社区讨论](https://news.ycombinator.com/item?id=48834405)

**背景**: 之前的 ChatGPT 语音模式使用的模型落后前沿几代，限制了其推理能力。GPT-5.5 是 OpenAI 最新的前沿推理模型，能够进行扩展思考并在复杂任务上实现接近前沿的性能。GPT-Live 通过后台委派，将专用语音模型的响应能力与 GPT-5.5 的强大功能结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pulse2.com/openai-introduces-gpt-live-to-power-more-natural-chatgpt-voice-interactions/">OpenAI Introduces GPT-Live To Power More Natural ChatGPT ...</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-live-chatgpt-voice-full-duplex">OpenAI's GPT-Live: ChatGPT voice that listens and talks - TNW</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体持积极态度，一位用户称赞了长达一小时的头脑风暴会话。然而，也有人担心 AI 会取代人际关系，还有人指出语音模式下缺乏工具/连接器支持是一个错失的机会。

**标签**: `#AI`, `#voice mode`, `#OpenAI`, `#GPT-5.5`, `#Hacker News`

---

<a id="item-5"></a>
## [OpenBSD 释放后使用漏洞可本地提权至 root](https://nvd.nist.gov/vuln/detail/cve-2026-57589) ⭐️ 8.0/10

OpenBSD 7.9 及之前版本中存在一个释放后使用漏洞（CVE-2026-57589），允许本地攻击者将权限提升至 root。该漏洞是在 OpenAI 与 Trail of Bits 合作的“Patch The Planet”计划中发现的。 该漏洞意义重大，因为 OpenBSD 以其安全性著称，而本地提权至 root 动摇了其核心安全承诺。这一发现也凸显了 AI 辅助漏洞研究在发现即使是最坚固系统中的漏洞方面日益重要的作用。 该释放后使用漏洞发生在 tsleep 调用后的上下文切换过程中，导致内存损坏，可被利用进行权限提升。该漏洞的 CVSS 评分为 8.0，属于高危级别，但需要本地访问才能利用。

hackernews · linggen · Jul 8, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48831658)

**背景**: 释放后使用漏洞是指程序在内存被释放后仍继续使用该内存指针，可能允许攻击者执行任意代码。OpenBSD 是一个注重安全的类 Unix 操作系统，其著名宣称是二十多年来默认安装中仅有两个远程漏洞。本地权限提升意味着拥有有限用户权限的攻击者可以获得系统的完全 root 控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48831658">OpenBSD has a use-after-free allowing local privilege escalation ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应不一：一些人称赞 OpenBSD 的安全文化使得漏洞极少，而另一些人则质疑为何该漏洞未列在 OpenBSD 的安全页面上。AI 辅助发现（Patch The Planet）的参与引发了关于此类工具在寻找安全操作系统漏洞方面有效性的讨论。

**标签**: `#security`, `#OpenBSD`, `#vulnerability`, `#privilege escalation`, `#AI-assisted security`

---

<a id="item-6"></a>
## [欧盟重启私人消息扫描规则](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 8.0/10

欧洲议会批准了一项紧急程序，以快速推进立法，恢复已过期的“聊天控制 1.0”规则，允许在线平台自愿扫描私人消息以查找儿童性虐待材料（CSAM）。决定性投票定于 7 月 9 日进行。 此举通过启用客户端扫描威胁到端到端加密（E2EE），可能破坏所有欧盟公民的隐私。如果通过，可能为其他地区采取类似监控措施树立先例。 投票结果为 331 票赞成、304 票反对，差距很小。批评者警告称，“聊天控制 2.0”将强制扫描并禁止 E2EE，而当前提案仅允许自愿扫描。

hackernews · ggirelli · Jul 8, 16:53 · [社区讨论](https://news.ycombinator.com/item?id=48834296)

**背景**: 端到端加密（E2EE）确保只有发送者和预期接收者才能阅读消息，防止第三方（包括服务提供商）访问内容。政府和儿童保护组织认为 E2EE 阻碍了对 CSAM 的调查，而隐私倡导者警告称，扫描机制会创建后门，可能被用于大规模监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/">EU now one step away from reviving private message scanning rules</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption</a></li>
<li><a href="https://cybernews.com/security/chat-control-eu-scanning-messages/">Will the EU start scanning your private messages? - Cybernews</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈反对，用户指出互联网观察基金会（Internet Watch Foundation）在推动客户端扫描中的作用。一些人指出，“聊天控制 1.0”允许自愿扫描（对于 Facebook 等平台已是预期），而“聊天控制 2.0”才是真正的威胁。一则行动呼吁敦促欧盟公民通过 fightchatcontrol.eu 联系他们的代表。

**标签**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#technology policy`

---

<a id="item-7"></a>
## [Cloudflare Meerkat：首个生产级异步共识算法](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare 宣布了 Meerkat，一种基于 QuePaxa 的全球分布式共识算法，它无需依赖超时即可实现异步共识。这是异步共识算法首次在生产环境中实现。 Meerkat 可以显著提升分布式系统在恶劣网络条件下的鲁棒性，因为它不依赖超时来保证活性。这对于像 Cloudflare 这样的全球规模服务尤其有价值，因为其网络延迟可能剧烈波动。 Meerkat 基于 QuePaxa，这是一种随机化异步共识协议，通过使用对冲（hedging）而非超时，在正常条件下实现了与基于领导者的协议相当的性能。该算法要求每次操作（包括读操作）都达成全局共识，这可能会给读密集型工作负载带来更高的延迟。

hackernews · bobnamob · Jul 8, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48831565)

**背景**: 传统的共识算法如 Paxos 和 Raft 依赖超时来检测故障并确保进展，因此它们是部分同步的。异步共识算法（如 QuePaxa）不需要超时，即使在任意网络延迟下也能取得进展，但历史上在正常情况下效率较低。Meerkat 旨在通过提供异步协议的实际实现来弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bford.info/pub/os/quepaxa/">QuePaxa: Escaping the Tyranny of Timeouts in Consensus – Bryan Ford's Home Page</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Pasindu Tennage* EPFL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Consensus_(computer_science)">Consensus (computer science) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调 Meerkat 是异步共识算法的首个生产实现，这是一个重要的里程碑。一些评论者指出，要求读操作也达成全局共识可能会限制其应用于特定场景，而另一些人则认为，对于领导者协议难以应对的复杂网络环境，Meerkat 可能非常有用。

**标签**: `#distributed systems`, `#consensus algorithms`, `#Cloudflare`, `#asynchronous consensus`, `#QuePaxa`

---

<a id="item-8"></a>
## [DeepSeek 自研 AI 芯片以减少对英伟达和华为的依赖](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

三位知情人士透露，中国 AI 公司 DeepSeek 正在开发自己的 AI 芯片，专注于推理阶段，旨在减少对英伟达和华为芯片的依赖。该自研芯片项目始于约一年前，目前仍处于早期阶段，DeepSeek 已开始招募芯片设计工程师，并与芯片设计、代工和存储公司接洽。 这一战略举措可能重塑中国的 AI 硬件格局，尤其是在美国出口限制限制先进芯片获取的背景下。如果成功，DeepSeek 将减少对供应链中断的脆弱性，并可能在推理芯片市场上提供具有竞争力的替代方案，挑战英伟达和华为。 该芯片专为推理而非训练设计，推理是计算强度较低但需求量大的任务。DeepSeek 近几个月已开始大量招募芯片设计工程师，并与芯片设计、代工和存储公司进行接洽。

telegram · zaihuapd · Jul 8, 05:20

**背景**: DeepSeek 是一家中国 AI 公司，以开发高性价比的大语言模型（如 DeepSeek-R1）而闻名，其性能可与 OpenAI 的 GPT-4 媲美。该公司此前依赖英伟达 H800 和华为昇腾芯片，但美国出口管制限制了中国企业获取先进 AI 芯片，促使中国企业寻求本土替代方案。推理芯片专门用于运行已训练好的模型以生成回答，而训练芯片则用于模型开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/">Facing US export controls, China's DeepSeek plans to make its own chips - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#DeepSeek`, `#semiconductors`, `#inference`, `#export controls`

---

<a id="item-9"></a>
## [SpaceXAI 明日发布 Grok 4.5](https://x.com/elonmusk/status/2074740539874775163) ⭐️ 8.0/10

SpaceXAI 宣布将于明日向公众开放 Grok 4.5，这是一款 Opus 级别的模型，速度更快、Token 使用效率更高且成本更低。 此次发布是 SpaceXAI 上市以来首次公开推出模型，可能通过提供高性能、低成本的模型加剧前沿 AI 市场的竞争。 Grok 4.5 被描述为 'Opus 级' 模型，该级别通常与 Anthropic 的 Claude Opus 系列相关，但速度更快、效率更高。基准测试显示其在 STEM 和知识工作方面表现出色，但定价较高。

telegram · zaihuapd · Jul 8, 07:09

**背景**: Opus 级别模型指 Anthropic 的 Claude Opus 系列，以深度推理和编码能力著称。SpaceXAI 由 Elon Musk 创立，一直开发 Grok 系列以与 GPT-4 和 Claude 等模型竞争。该公司数周前上市，Grok 4.5 是上市后的首个重大发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/">SpaceXAI releases Grok 4.5, which Elon describes as an 'Opus ...</a></li>
<li><a href="https://cursor.com/blog/grok-4-5">Introducing Grok 4.5 - Cursor</a></li>
<li><a href="https://benchable.ai/models/x-ai/grok-4.5-20260708">xAI: Grok 4.5 - AI Model Details & Benchmarks</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Grok`, `#SpaceXAI`

---

<a id="item-10"></a>
## [顶尖 AI 企业安全评级普遍偏低，Anthropic 以 C+居首](http://z.ai/) ⭐️ 8.0/10

生命未来研究所于 2026 年 2 月发布的最新 AI 安全指数对九家领先 AI 公司的安全实践进行了评级，没有一家公司获得 A。Anthropic 以 C+位居榜首，OpenAI 和谷歌 DeepMind 获 C，Meta 获 D+，而 xAI、DeepSeek 和 Mistral 则获 F。 该报告揭示了最具影响力的 AI 开发商在风险管理方面的系统性失败，引发了对行业自我监管能力的担忧。这些发现可能促使政府加速制定 AI 安全法规，并增加公众对 AI 公司军事合作的审视。 该指数从六个安全领域对公司进行评估：测试、透明度、滥用控制、治理等。许多公司已调整政策，允许其 AI 用于军事目的，报告将此视为一个风险因素。

telegram · zaihuapd · Jul 8, 11:30

**背景**: 生命未来研究所是一家倡导负责任 AI 发展的非营利组织。其 AI 安全指数旨在独立评估领先 AI 实验室应对灾难性风险的能力。该报告发布之际，全球对 AI 安全及军事 AI 应用伦理的争论日益激烈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://futureoflife.org/ai-safety-index-winter-2025/">AI Safety Index: Winter 2025 - Future of Life Institute</a></li>
<li><a href="https://time.com/article/2026/07/07/ai-safety-rankings-openai-anthropic-meta/">The Latest AI Safety Rankings Are In. Nobody Gets an A - TIME</a></li>
<li><a href="https://www.latimes.com/entertainment-arts/business/story/2025-12-05/ai-artificial-intelligence-company-scorecard-ranks-safety-humanity">A safety report card ranks AI company efforts to protect ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#industry report`, `#risk management`

---

<a id="item-11"></a>
## [华为 5G 旗舰重返海外，峰值速率超 1100 Mbps](https://finance.sina.com.cn/tech/roll/2026-07-08/doc-inihapna8035781.shtml) ⭐️ 8.0/10

华为 Pura 90 Pro Max 国际版原生支持 5G 网络，海外实测峰值下载速率突破 1100 Mbps，标志着华为 5G 旗舰在受美国制裁七年后正式重返海外市场。 这标志着华为在 5G 芯片供应上取得突破，并战略性地重返全球智能手机市场，可能重塑与苹果、三星在高端市场的竞争格局。 该设备搭载 HarmonyOS 6.0.0.125，并采用 5A 通信技术。华为澄清 5A 并非新的网络制式，而是代表先进连接体验的品牌标识，包括更快接入和更低时延。

telegram · zaihuapd · Jul 8, 12:17

**背景**: 自 2019 年起，美国制裁阻止华为使用 5G 芯片和谷歌移动服务，重创其海外手机业务。2023 年，Mate 60 系列凭借国产 5G 芯片震惊市场，随后 HarmonyOS 6.0.0.125 等更新引入 5A 品牌标识，为 5G 重返海外奠定基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/901/311.htm">华为官网详解“5A”先进通信技术：不等同于 5G-A / 5.5G，不涉及额外资...</a></li>
<li><a href="https://news.qq.com/rain/a/20260107A02IIR00">华为 Mate 60 等机型获 HarmonyOS 6.0.0.125 升级，实装 5A 通信</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#5G`, `#smartphones`, `#US sanctions`, `#telecommunications`

---

<a id="item-12"></a>
## [安卓远程 Root 漏洞链曝光](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

安全公司 Nebula 披露了一个名为 IonStack 的远程 Root 漏洞链，通过点击恶意链接即可攻破安卓 17 及以下版本设备，该漏洞链结合了 Firefox 浏览器漏洞和潜伏 15 年的 Linux 内核漏洞（CVE-2026-43499，GhostLock），概念验证代码已上传 GitHub。 这是首个公开的安卓 17 Root 漏洞利用，表明即使是最新安卓版本也存在远程被攻破的风险。攻击仅需用户点击链接，无需其他交互，对所有安卓用户构成严重威胁。 该漏洞链利用 Firefox 浏览器漏洞（影响 Firefox 151.0.2 及更早版本）实现初始代码执行，再通过 GhostLock Linux 内核漏洞提升至 Root 权限。Linux 内核已修复，但安卓设备可能无法及时获得更新。

telegram · zaihuapd · Jul 8, 13:01

**背景**: 安卓安全依赖于沙箱和权限模型来隔离应用并限制漏洞利用的损害。远程 Root 漏洞完全绕过这些保护，使攻击者获得设备的完全控制权。GhostLock 漏洞是 Linux 内核 rt_mutex 代码中的释放后使用漏洞，自 2011 年以来一直存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>
<li><a href="https://cybersecuritynews.com/15-year-old-ghostlock-linux-kernel-vulnerability/">15-year-old GhostLock Linux Kernel Vulnerability Enables ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#security`, `#vulnerability`, `#root exploit`, `#Linux kernel`

---

<a id="item-13"></a>
## [美团 OWL（LongCat）免费测试模型疑似泄露对话数据](https://github.com/gumusserv/ProducerBenchV2/blob/83cad6007ef3fe8df33386e8f43738fe62337e16/parsed_source_data/data/) ⭐️ 8.0/10

美团在 OpenRouter 上提供的 OWL（LongCat）免费测试模型疑似泄露用户对话数据，相关数据曾出现在一个现已设为私有的 GitHub 仓库中。该仓库至少在 2026 年 7 月 7 日前可公开访问，随后被 Discord 机器人令牌扫描器发现。 此事件凸显了使用免费 AI 模型（尤其是来自美团等大公司的模型）时存在的重大隐私风险，用户对话可能被泄露。这提醒用户避免向大语言模型输入 API 密钥、私钥等敏感信息。 泄露的数据出现在一个 GitHub 仓库中，该仓库现已设为私有，此次泄露被一个 Discord 机器人令牌扫描器发现，该扫描器可自动检测并撤销暴露的令牌。OWL 模型是美团 LongCat-2.0 的免费测试版本，LongCat-2.0 是一个 1.6 万亿参数的 MoE 模型，此前以 Owl Alpha 的化名在 OpenRouter 排名中位居榜首。

telegram · zaihuapd · Jul 8, 13:35

**背景**: 美团 LongCat-2.0 是一个 1.6 万亿参数的混合专家（MoE）模型，采用 MIT 许可证开源，完全使用国产芯片训练。OWL 模型是 OpenRouter 上提供的免费测试模型，OpenRouter 是一个聚合多种 AI 模型的平台。类似事件也曾发生在 Google、DeepSeek 等其他提供商身上，用户数据可能被用于模型改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aitoolsrecap.com/Blog/longcat-2-meituan-open-source-chinese-chips-2026">LongCat-2.0: The 1.6T Open-Source AI That Was Secretly ...</a></li>
<li><a href="https://www.opensourceforu.com/2026/06/meituan-open-sources-longcat-2-0-under-mit-license/">Meituan Open Sources LongCat-2.0 Under MIT License</a></li>
<li><a href="https://longcat.chat/blog/longcat-2.0/">Introducing LongCat-2.0</a></li>

</ul>
</details>

**社区讨论**: 社区对此数据泄露事件表示担忧，许多用户警告他人不要向大语言模型输入敏感信息。一些人指出，这一事件再次强调了将对话日志视为敏感数据资产的重要性。

**标签**: `#data leak`, `#AI security`, `#LLM`, `#Meituan`, `#privacy`

---

<a id="item-14"></a>
## [通过电磁信号识别手机应用，准确率达 99%](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

中国研究人员开发出一种非接触式取证技术，通过分析设备运行时泄漏的低频电磁辐射来识别手机应用和用户操作，在 iPhone 15 Pro、小米 15 Pro 和 OPPO Reno 13 上实现了最高 99.07% 的准确率。 这种侧信道攻击即使在手机离线、飞行模式、加密或锁定状态下也能工作，无需访问设备的操作系统或存储数据，对隐私构成严重威胁。 该方法针对智能手机组件（如电源管理 IC 和显示屏）发出的低频电磁信号（低于 1 MHz），并使用机器学习对应用特定的模式进行分类。该研究于 5 月 22 日发表在同行评审期刊《Radioengineering》上。

telegram · zaihuapd · Jul 8, 16:05

**背景**: 侧信道攻击利用系统物理运行中无意泄漏的信息，如时序、功耗或电磁辐射。与针对软件漏洞的传统网络攻击不同，侧信道攻击通过分析物理副产品来推断敏感数据。该技术类似于 TEMPEST 攻击，后者可从电子设备中恢复信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side-channel attack</a></li>
<li><a href="https://www.nationpress.com/sciencetech/china-researchers-id-apps-via-phone-radio-leak">Chinese researchers crack smartphone app ID via radio signals</a></li>
<li><a href="https://www.newsbang.com/news/article/story_id-p008-155706">Chinese Researchers Identify Smartphone Apps via Leaked ...</a></li>

</ul>
</details>

**标签**: `#side-channel attack`, `#smartphone security`, `#electromagnetic signals`, `#privacy`, `#forensics`

---