---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 29 items, 9 important content pieces were selected

---

1. [哪吒监控探针存在高危路径穿越漏洞（CVSS 9.1）](#item-1) ⭐️ 9.0/10
2. [vLLM v0.23.0：DeepSeek-V4 优化与 Model Runner V2 扩展](#item-2) ⭐️ 8.0/10
3. [LinkedIn 虚假面试中的 npm 后门](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0：点对点网络库发布](#item-4) ⭐️ 8.0/10
5. [福克斯以 220 亿美元收购 Roku](#item-5) ⭐️ 8.0/10
6. [Typst 0.15.0：支持多文献列表，改进脚注](#item-6) ⭐️ 8.0/10
7. [为什么 AI 没有取代软件工程师，也不会取代](#item-7) ⭐️ 8.0/10
8. [美国下令 Anthropic 限制两款 AI 模型](#item-8) ⭐️ 8.0/10
9. [Rio 3.5 模型被曝套壳中国开源模型](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [哪吒监控探针存在高危路径穿越漏洞（CVSS 9.1）](https://github.com/nezhahq/nezha/security/advisories/GHSA-5c25-7vpj-9mqh) ⭐️ 9.0/10

哪吒监控探针 v2.0.13 以下版本被披露存在严重路径穿越漏洞（CVE-2026-53519，CVSS 9.1），未授权攻击者可通过构造 GET 请求（如 /dashboard../data/config.yaml）读取 JWT 密钥。 该漏洞非常严重，因为哪吒监控是广泛使用的开源监控工具，利用该漏洞可伪造 JWT 令牌导致系统完全沦陷。用户必须立即升级到 v2.0.13 或更高版本以防止数据泄露。 该漏洞是 dashboard 组件的路径穿越，允许攻击者读取任意文件（如包含 JWT 密钥的 config.yaml）。CVSS 评分 9.1 表明利用难度低、影响大，且无需认证。

telegram · zaihuapd · Jun 15, 09:25

**背景**: 哪吒监控是一个开源、轻量级的服务器监控和管理工具，由面板和探针组成。路径穿越漏洞发生在应用程序未能正确验证用户提供的文件路径时，允许攻击者访问预期目录之外的文件。JWT 密钥用于签名认证令牌，一旦泄露，攻击者可伪造令牌获得未授权访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://owasp.org/www-community/attacks/Path_Traversal">Path Traversal | OWASP Foundation</a></li>
<li><a href="https://blog.echosec.top/p/nezha-monitoring/">『Blog』 NeZha Monitoring 从一到无穷大 | Echosec @QIN2DIM</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#nezha`, `#path traversal`, `#CVE`

---

<a id="item-2"></a>
## [vLLM v0.23.0：DeepSeek-V4 优化与 Model Runner V2 扩展](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 为 DeepSeek-V4 引入了重大优化，包括稀疏 MLA 元数据解耦和 TRTLLM-gen 注意力内核，并将 Model Runner V2 (MRv2) 默认扩展到 Llama 和 Mistral 密集模型。 此版本显著提升了最先进的 MoE 模型 DeepSeek-V4 的推理性能，并使 MRv2 成为流行密集模型的默认选项，使大部分 vLLM 用户受益于更快、更高效的推理。 此版本包含来自 200 位贡献者的 408 次提交，增加了对 Gemma 4 Unified 和 Step-3.7-Flash 等新模型的支持，并引入了具有对象存储二级层级的多层 KV 缓存卸载。

github · khluu · Jun 15, 05:27

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。Model Runner V2 (MRv2) 是对模型运行器的彻底重写，旨在实现更清晰、更模块化、更高效的执行。DeepSeek-V4 是一个大型混合专家 (MoE) 模型，受益于专门的注意力和内存优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html">Multi-Head, Multi-Query, and Group-Query Attention — TensorRT-LLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#Model Runner V2`, `#open source`

---

<a id="item-3"></a>
## [LinkedIn 虚假面试中的 npm 后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 8.0/10

一名求职者在 LinkedIn 面试中发现，招聘人员发送的 GitHub 仓库中隐藏了一个后门，该后门利用 npm 的 prepare 脚本，在运行 npm install 时执行任意代码。 此次攻击揭示了一种针对开发者的新型社会工程学手段，利用求职面试中的信任来入侵系统，并凸显了针对此类网络犯罪缺乏报告机制的问题。 后门隐藏在注释掉的测试代码中，通过 npm 的 prepare 脚本执行，该脚本在 npm install 后自动运行。有效载荷与远程服务器通信以接收指令。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm 的 prepare 脚本是一个生命周期钩子，在 npm install 后自动运行，通常用于构建步骤。攻击者可滥用它在开发者安装依赖时执行任意代码，成为供应链攻击的载体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://stackoverflow.com/questions/44499912/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it">node.js - Why is npm running prepare script after... - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 评论者表示，这种攻击与正常的面试任务非常相似，令人不安，并呼吁建立更好的网络犯罪报告机制。有人质疑为什么 npm 的 prepare 脚本默认未被阻止。

**标签**: `#security`, `#supply chain attack`, `#npm`, `#social engineering`, `#cybercrime`

---

<a id="item-4"></a>
## [Iroh 1.0：点对点网络库发布](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 正式发布，这是一个用 Rust 编写的点对点网络库，允许应用实例之间直接连接，无需中心化基础设施，并支持可扩展的自定义传输层。 此次发布提供了一种新颖的应用层网络方案，类似于 Tailscale 但位于应用层面，可能简化分布式应用的构建并减少对中心化服务器的依赖。 Iroh 1.0 内置支持 IPv4、IPv6 和中继传输，并引入了自定义传输 API，可集成 WebRTC、BLE 或 LoRa 等协议。该库使用加密拨号密钥来确保对等节点身份安全。

hackernews · chadfowler · Jun 15, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48542480)

**背景**: 点对点网络允许设备直接通信而无需中心服务器，但 NAT 穿透和防火墙问题常使直接连接变得复杂。Iroh 通过提供一个处理这些挑战的库来简化这一过程，类似于 Tailscale 在操作系统层面创建虚拟网络，但 Iroh 在应用层运行，使应用开发者更容易嵌入 P2P 功能，无需用户账户或系统级配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iroh-computer.vercel.app/blog/iroh-0-23-welcoming-nodejs-to-the-family">iroh 0.23.0 - Welcoming Node.js to the family! - Iroh</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论将 Iroh 视为 Tailscale 的应用层替代方案，开发者称赞其自定义传输的可扩展性。一些用户质疑是否需要又一个 P2P 库，而另一些用户则欣赏其基于加密密钥的身份模型。一位开发者表示计划将 Iroh 集成到他们现有的基于 WebRTC 的 P2P 工具中。

**标签**: `#peer-to-peer`, `#networking`, `#rust`, `#open-source`, `#release`

---

<a id="item-5"></a>
## [福克斯以 220 亿美元收购 Roku](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

福克斯公司宣布以 220 亿美元收购流媒体硬件和平台领导者 Roku。该交易预计于 2026 年底完成，尚待监管批准。 此次垂直整合使福克斯直接控制约 30-50%美国家庭使用的流媒体平台，引发反垄断担忧，并可能改变流媒体内容和硬件的竞争格局。用户担心内容偏见、数据隐私和平台中立性降低。 该交易对 Roku 的估值为 220 亿美元，高于其市值。福克斯已拥有免费广告支持的流媒体服务 Tubi，并计划整合 Roku 的广告平台。Roku 的硬件业务和操作系统将保持独立，但福克斯将获得用户数据和首页位置控制权。

hackernews · thm · Jun 15, 12:50 · [社区讨论](https://news.ycombinator.com/item?id=48540499)

**背景**: Roku 是美国领先的流媒体平台，拥有超过 8000 万活跃账户，约占流媒体设备市场份额的 30%。福克斯是大型内容生产商，旗下有 Fox News、Fox Sports 和 Tubi 等网络。内容提供商与分发平台之间的垂直合并常因自我优待和市场封锁风险而面临反垄断审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fandomwire.com/biggest-concerns-after-foxs-22b-roku-acquisition/">5 Biggest Concerns After Fox's $22 Billion Roku Acquisition</a></li>
<li><a href="https://deadline.com/2026/06/fox-roku-acquisition-streaming-wall-street-1236956272/">Fox And Roku Frame Blockbuster $22B Merger As Streaming Win-Win, But Wall Street Has Questions</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户对福克斯控制 Roku 平台表示悲观。评论者担心强制集成 Fox News、广告增加以及设备中立性丧失。部分用户建议改用 Nvidia Shield 等替代方案并安装自定义启动器。

**标签**: `#acquisition`, `#streaming`, `#media`, `#hardware`, `#antitrust`

---

<a id="item-6"></a>
## [Typst 0.15.0：支持多文献列表，改进脚注](https://typst.app/docs/changelog/0.15.0/) ⭐️ 8.0/10

Typst 0.15.0 新增了在单个文档中使用多个文献列表的功能，改进了脚注处理，并增强了 HTML 导出能力，支持将数学公式自动转换为 MathML。 这些功能满足了用户长期以来的需求，使 Typst 在复杂的学术写作和出版工作流中更具可行性，巩固了其作为 LaTeX 替代方案的地位。 多文献列表功能允许用户按类别（如主要和次要来源）分隔参考文献；脚注改进包括更好的放置位置以及对包含引文的讨论性脚注的支持。

hackernews · schu · Jun 15, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=48544396)

**背景**: Typst 是一种基于标记的排版系统，旨在与 LaTeX 同样强大，但更易于学习和使用。它可编译为 PDF 和 HTML，在学术界广泛用于撰写论文、学位论文和书籍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/typst/typst">GitHub - typst / typst : A markup-based typesetting system that is...</a></li>
<li><a href="https://typst.app/docs/">Typst Documentation</a></li>
<li><a href="https://typst.app/docs/reference/model/bibliography/">Bibliography Function – Typst Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区总体反应积极，用户对新功能表示赞赏。但也有用户指出脚注仍存在局限，尤其是包含文献引用的讨论性脚注，希望未来能进一步改进。

**标签**: `#typesetting`, `#open source`, `#typst`, `#software release`

---

<a id="item-7"></a>
## [为什么 AI 没有取代软件工程师，也不会取代](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/#atom-everything) ⭐️ 8.0/10

Arvind Narayanan 和 Sayash Kapoor 发表文章，认为数据不支持 AI 将导致软件工程大规模裁员的说法，并指出纽约州新的 WARN 法案披露要求下，160 多家公司中无一报告与 AI 相关的裁员。 这篇文章为 AI 导致失业的主流叙事提供了基于数据的反驳，表明即使在一个特别容易受到 AI 影响的领域，软件工程仍然具有韧性，因为需要对代码库、业务环境和验证有深入的人类理解。 作者指出了软件工程中难以自动化的三个真正瓶颈：决定构建什么、验证并对交付物负责，以及两者所需的深入人类理解。他们指出 AI 加快了输入代码的速度，但并未加速这些核心活动。

rss · Simon Willison · Jun 14, 23:54

**背景**: WARN 法案要求雇主在发生大规模裁员前提前通知。2025 年 3 月，纽约州在其 WARN 申报中增加了 AI 披露复选框，询问裁员是否因 AI 所致。在第一个完整年度，超过 160 家公司提交了通知，但没有一家勾选 AI 选项，表明 AI 尚未成为软件工程岗位流失的主要原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hunton.com/hunton-employment-labor-perspectives/new-york-warn-act-no-ai-related-layoffs-reported-in-first-year-of-adding-ai-related-disclosure-to-the-system">New York WARN Act: No AI-Related Layoffs Reported in First Year of Adding AI-Related Disclosure to the System</a></li>
<li><a href="https://engineering.princeton.edu/news/2025/01/13/ai-snake-oil-conversation-princeton-ai-experts-arvind-narayanan-and-sayash-kapoor">‘ AI Snake Oil’: A conversation with Princeton AI experts Arvind ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#job displacement`, `#labor economics`

---

<a id="item-8"></a>
## [美国下令 Anthropic 限制两款 AI 模型](https://t.me/zaihuapd/41960) ⭐️ 8.0/10

美国商务部向 Anthropic 发出出口管制指令，要求其暂停任何外国公民在美国境内外访问 Fable 5 和 Mythos 5 AI 模型。作为回应，Anthropic 已关闭这两款模型对所有客户的访问，包括其外国籍员工。 这标志着政府对 AI 模型分发干预的显著升级，为基于国家安全的出口管制树立了先例。它可能重塑 AI 公司全球部署模型的方式，并影响国际社会对尖端 AI 能力的获取。 Fable 5 和 Mythos 5 是同一底层模型，权重相同，仅安全护栏不同。Anthropic 的其他 Claude 模型不受影响，公司正在争取尽快恢复访问。

telegram · zaihuapd · Jun 15, 08:55

**背景**: 美国政府越来越多地使用出口管制来限制被认为对国家安全至关重要的先进技术的传播。Anthropic 的 Mythos 级模型（包括 Fable 5）代表了高于其 Opus 模型的新层级，在自主知识工作和编码方面具有增强的能力。该指令是在担心模型可能被越狱并带来安全风险之后发布的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order">Anthropic to disable its most advanced AI models after US order...</a></li>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following... | Fortune</a></li>
<li><a href="https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519">Inside the whirlwind 24 hours that led the White House to slap export ...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#national security`, `#Anthropic`, `#export controls`, `#AI safety`

---

<a id="item-9"></a>
## [Rio 3.5 模型被曝套壳中国开源模型](https://mp.weixin.qq.com/s/0oYevRBT8PPxG5hudOXxug) ⭐️ 8.0/10

此前被奉为开源 SOTA 的 Rio 3.5 模型被揭露为套壳模型，实际上是 Nex 和 Qwen 的混合产物。Rio 团队随后从 Hugging Face 下架该模型并致歉，称上传的是未经最终蒸馏的错误版本。 这一事件削弱了开源 AI 社区的信任，表明声称的突破可能只是对现有工作的重新包装。它也凸显了在模型发布中加强来源验证和透明度的必要性。 Nex 团队发现，摘掉系统提示词后，Rio 3.5 有 79% 的概率自称 Nex，并能复述 Nex 独有的机构介绍。对 60 层权重的分析表明，Rio 的权重精确落在 Nex 与 Qwen 的连线上，混合比例约 0.57:0.43，共线性超过 0.98，几乎不可能为独立训练。

telegram · zaihuapd · Jun 15, 12:39

**背景**: 开源 AI 模型常声称达到 SOTA 性能，但验证其原创性颇具挑战。此前事件包括 Cursor 的 Composer 2 被曝实际为 Kimi，以及斯坦福团队的 Llama3-V 被指抄袭清华面壁的 MiniCPM-Llama3-V 2.5。这些案例凸显了开源社区中模型来源的反复问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/mitomtuna/Rio-3.5-Open-397B-NVFP4">mitomtuna/ Rio - 3 . 5 -Open-397B-NVFP4 · Hugging Face</a></li>
<li><a href="https://huggingface.co/prefeitura-rio/Rio-3.5-Open-397B">prefeitura- rio / Rio - 3 . 5 -Open-397B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#model fraud`, `#controversy`, `#machine learning`

---