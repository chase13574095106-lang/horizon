---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> From 34 items, 12 important content pieces were selected

---

1. [FFmpeg 严重漏洞：恶意视频可致远程代码执行](#item-1) ⭐️ 9.0/10
2. [中国灵晟超算登顶 TOP500，首款纯 CPU 超 2 ExaFLOPS](#item-2) ⭐️ 9.0/10
3. [AI 的可负担性危机](#item-3) ⭐️ 8.0/10
4. [Unlimited OCR：一次性长文档解析](#item-4) ⭐️ 8.0/10
5. [即将到来的循环：AI 编程需要清晰的规范](#item-5) ⭐️ 8.0/10
6. [谷歌因非官方 CLI 工具解雇员工](#item-6) ⭐️ 8.0/10
7. [Anthropic 推出 Claude Tag，一个多玩家 AI 助手集成到 Slack](#item-7) ⭐️ 8.0/10
8. [LLM 提示注入即角色混淆](#item-8) ⭐️ 8.0/10
9. [将 Moebius 0.2B 图像修复模型移植到浏览器中运行](#item-9) ⭐️ 8.0/10
10. [近半数 LG 智能电视应用含住宅代理 SDK](#item-10) ⭐️ 8.0/10
11. [三星发布 UFS 5.0，带宽 10.8 GB/s，面向端侧 AI](#item-11) ⭐️ 8.0/10
12. [研究显示洗牌 14 次才能随机化一副牌](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [FFmpeg 严重漏洞：恶意视频可致远程代码执行](https://cybernews.com/security/critical-ffmpeg-vulnerability-enables-complete-compromise/) ⭐️ 9.0/10

FFmpeg 的 MagicYUV 解码器中发现了一个严重的堆越界写入漏洞 CVE-2026-8461（PixelSmash），攻击者可通过构造恶意的 AVI、MKV 或 MOV 文件实现远程代码执行。FFmpeg 已于 2026 年 6 月 17 日发布 8.1.2 版本修复该问题。 该漏洞 CVSS 评分 8.8，影响几乎所有使用 FFmpeg 的应用，包括 VLC、Jellyfin、Kodi、Nextcloud、OBS 以及众多 IoT 设备。攻击者只需诱使用户打开恶意视频文件，甚至通过自动生成缩略图即可控制系统。 该漏洞是 MagicYUV 解码器中的堆越界写入问题，在处理特制视频帧时触发。JFrog 研究人员于 2026 年 5 月 13 日发现并报告该漏洞，FFmpeg 于 2026 年 6 月 17 日发布 8.1.2 版本修复。

telegram · zaihuapd · Jun 23, 15:00

**背景**: FFmpeg 是一个广泛使用的开源多媒体框架，被数千个应用用于视频和音频的编码、解码和转码。MagicYUV 解码器是一种无损视频编解码器，常用于高质量视频编辑和屏幕录制。堆越界写入是指程序写入数据超出分配的内存缓冲区，可被利用来执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/">FFmpeg fixes PixelSmash flaw in widely used video decoder</a></li>
<li><a href="https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/">FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media ...</a></li>
<li><a href="https://aviatrix.ai/threat-research-center/ffmpeg-pixelsmash-vulnerability-cve-2026-8461/">FFmpeg PixelSmash Vulnerability (CVE-2026-8461) - Critical ...</a></li>

</ul>
</details>

**标签**: `#FFmpeg`, `#vulnerability`, `#remote code execution`, `#security`, `#CVE-2026-8461`

---

<a id="item-2"></a>
## [中国灵晟超算登顶 TOP500，首款纯 CPU 超 2 ExaFLOPS](https://news.mydrivers.com/1/1131/1131573.htm) ⭐️ 9.0/10

6 月 23 日公布的 TOP500 榜单中，中国“灵晟”超算以 2.198 ExaFLOPS 的 HPL 性能排名第一，成为全球首台纯 CPU 设计突破 2 ExaFLOPS 的系统。它还在 HPCG 基准测试中位居首位，并在 HPL-MxP 混合精度测试中排名第四。 这标志着中国时隔八年重返 TOP500 榜首，展示了国产 CPU 技术和国家科技自主的重大进步。这一成就凸显了纯 CPU 架构在超大规模计算中的可行性，挑战了以 GPU 为主的设计趋势。 灵晟基于国产“灵鲲”平台与 LX2 处理器，采用纯 CPU 架构。它在 HPL 基准测试中达到 2.198 ExaFLOPS（双精度浮点性能），并在测试内存带宽和通信模式的 HPCG 基准测试中也位居首位。

telegram · zaihuapd · Jun 23, 15:30

**背景**: TOP500 榜单根据 HPL 基准测试（求解稠密线性方程组）的性能对超算进行排名。ExaFLOPS（每秒 10^18 次浮点运算）是高性能计算的关键里程碑。此前达到百亿亿次级别的系统（如 Frontier 和 Fugaku）使用了 GPU 加速器或多核 CPU，因此灵晟的纯 CPU 方案格外引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TOP500">TOP500 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Exascale_computing">Exascale computing - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/HPCG_benchmark">HPCG benchmark - Wikipedia</a></li>

</ul>
</details>

**标签**: `#supercomputing`, `#HPC`, `#TOP500`, `#China`, `#CPU`

---

<a id="item-3"></a>
## [AI 的可负担性危机](https://blog.dshr.org/2026/06/ais-affordability-crisis.html) ⭐️ 8.0/10

AI 行业正面临由风险投资过度投资和不可持续定价导致的可负担性危机，许多公司可能意识到 AI 采用带来的投资回报率很低。 该分析揭示了 AI 行业根本性的财务可持续性问题，可能导致市场调整，并影响企业评估 AI 投资的方式。 文章引用 Zitron 的数据表明，Anthropic 可能对企业客户补贴高达 40 倍，OpenAI 补贴高达 70 倍，显示出严重的定价过低。

hackernews · ilreb · Jun 23, 15:11 · [社区讨论](https://news.ycombinator.com/item?id=48646276)

**背景**: 风险投资向 AI 初创公司投入了数十亿美元，往往优先考虑增长而非盈利能力。这导致 AI 服务的人为低价，掩盖了开发和部署的真实成本。当前的定价模式可能无法长期持续。

**社区讨论**: 评论者争论这是可负担性危机还是金融危机，一些人认为模型成本正在快速下降，但公司可能无法从 AI 中获得投资回报。另一些人指出，风险投资的过度投资正在制造类似安然公司的不可持续泡沫。

**标签**: `#AI`, `#economics`, `#venture capital`, `#industry analysis`

---

<a id="item-4"></a>
## [Unlimited OCR：一次性长文档解析](https://github.com/baidu/Unlimited-OCR) ⭐️ 8.0/10

百度开源了 Unlimited OCR 模型，该模型通过修改 KV 缓存来避免内存增长，从而一次性解析整个 PDF，无需逐页分块。 这解决了长文档 OCR 中的关键内存瓶颈，使得无需 VRAM 溢出即可高效处理多页文档，有利于文档数字化、RAG 流水线和无障碍工具。 该模型基于 DeepSeek-OCR 和 PaddleOCR 构建，论文可在 arXiv（2606.23050）上获取。它通过修改 KV 缓存，使得内存使用量与文档长度无关，保持恒定。

hackernews · ingve · Jun 23, 11:35 · [社区讨论](https://news.ycombinator.com/item?id=48643426)

**背景**: 在基于 Transformer 的模型中，KV 缓存存储过去的 token 表示以避免重复计算，但其内存随上下文长度线性增长，导致长文档时 VRAM 耗尽。传统解决方案是将文档分页，但这效率低下且丢失上下文。Unlimited OCR 的方法模仿人类工作记忆，选择性遗忘无关 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/baidu/Unlimited-OCR">Unlimited OCR Works - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2606.23050">[2606.23050] Unlimited OCR Works - arXiv.org</a></li>
<li><a href="https://www.explainx.ai/blog/baidu-unlimited-ocr-one-shot-long-horizon-parsing-2026">Baidu Unlimited-OCR: One-Shot Long-Horizon Document Parsing ...</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了这一巧妙的架构技巧以及对 DeepSeek-OCR 和 PaddleOCR 的致谢。一些用户指出名称参考了《Fate/stay night》，其他人则讨论了光学音乐识别等应用。

**标签**: `#OCR`, `#AI`, `#memory optimization`, `#deep learning`, `#document parsing`

---

<a id="item-5"></a>
## [即将到来的循环：AI 编程需要清晰的规范](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) ⭐️ 8.0/10

作者认为，有效使用 AI 编程代理需要清晰的前期规范，并警告不要过度依赖 LLM 来处理包含错误处理的复杂代码。 这一观点意义重大，因为它挑战了围绕 AI 编程代理的热潮，并强调了在软件开发中人类规范技能的持久重要性。 作者指出，LLM 在处理复杂的错误处理代码方面存在困难，而迭代优化的“循环”通常需要 5-6 次失败尝试才能获得清晰度。

hackernews · ingve · Jun 23, 11:06 · [社区讨论](https://news.ycombinator.com/item?id=48643180)

**背景**: 像 Claude Code 和 Cursor 这样的 AI 编程代理使用大型语言模型从自然语言提示生成代码。规范驱动开发（SDD）是一种在编码开始前编写详细规范的方法论，这些规范作为人类和 AI 的权威来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.faros.ai/blog/best-ai-coding-agents-2026">Best AI Coding Agents for 2026: Real-World Developer Reviews</a></li>
<li><a href="https://en.wikipedia.org/wiki/Specification-driven_development">Specification-driven development</a></li>
<li><a href="https://developer.microsoft.com/blog/spec-driven-development-spec-kit">Diving Into Spec-Driven Development With GitHub Spec Kit GitHub - github/spec-kit: Toolkit to help you get started ... Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl Spec-Driven Development (SDD): The Definitive 2026 Guide Specification-driven development - Wikipedia What is spec-driven development? - IBM spec-kit/spec-driven.md at main · github/spec-kit · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为清晰的规范是瓶颈，其中一位指出当规范定义良好时，代理循环的问题就少了。另一位评论者强调了说服开发者移除 LLM 生成的过多空值检查的困难。

**标签**: `#AI-assisted coding`, `#software engineering`, `#LLM limitations`, `#specification-driven development`

---

<a id="item-6"></a>
## [谷歌因非官方 CLI 工具解雇员工](https://twitter.com/JPoehnelt/status/2069482265953087602) ⭐️ 8.0/10

谷歌员工 Justin Poehnelt 因创建并发布了一个非官方的 Google Workspace CLI 工具（该工具被误认为是官方产品）而被解雇。 这一事件凸显了员工创新与企业官僚主义之间的紧张关系，尤其是在像谷歌这样曾以“20%时间”鼓励副项目的公司。 该 CLI 工具使用谷歌公共 API 构建，未经公司授权。此次解雇引发了关于谷歌当前对员工副项目和开源贡献立场的讨论。

hackernews · justinwp · Jun 23, 18:13 · [社区讨论](https://news.ycombinator.com/item?id=48649011)

**背景**: 谷歌有政策要求员工为副项目获得批准，尤其是那些可能被误认为是官方产品的项目。该公司著名的“20%时间”政策（允许员工从事个人项目）已基本被淘汰。评论中提到的“Pournelle 官僚铁律”指出，在任何官僚机构中，最致力于官僚机构本身的人最终会掌权，凌驾于那些致力于组织原始目标的人之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/googleworkspace/cli">GitHub - googleworkspace/cli: Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.</a></li>
<li><a href="https://www.infoq.com/news/2026/06/google-workspace-cli/">Google Workspace CLI: Unified Command-Line Tool Built for Humans and AI Agents - InfoQ</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一。一些人认为，发布一个可能被误认为是官方产品的工具表明判断力差，解雇是合理的。另一些人则同情该员工，引用 Pournelle 官僚铁律，批评谷歌扼杀创新。少数人指出，考虑到谷歌的政策，该员工的行为存在风险。

**标签**: `#Google`, `#CLI`, `#bureaucracy`, `#open source`, `#employment`

---

<a id="item-7"></a>
## [Anthropic 推出 Claude Tag，一个多玩家 AI 助手集成到 Slack](https://www.anthropic.com/news/introducing-claude-tag) ⭐️ 8.0/10

Anthropic 推出了 Claude Tag，这是一个协作式 AI 助手，作为团队成员集成到 Slack 中，用户可以在频道中 @Claude 来委派任务，从对话中学习，并同时与多个用户互动。 此次发布标志着企业协作中向自主工作流迈出的重要一步，实现了持久、共享的 AI 队友，能够积累组织知识并支持多玩家互动，可能改变团队在 Slack 中的工作方式。 Claude Tag 被描述为 Claude Code 的演进版本，Anthropic 内部已使用一段时间，公司声称其产品团队 65% 的代码是由内部版本的 Claude Tag 创建的。

hackernews · adocomplete · Jun 23, 17:09 · [社区讨论](https://news.ycombinator.com/item?id=48648039)

**背景**: Claude Tag 是 Anthropic 的新功能，为 Slack 带来了一个始终在线的 AI 队友，能够从频道中学习并连接到工具、数据和代码库。它专为协作式多玩家互动设计，多个用户可以在频道中与同一个 Claude 实例互动，查看其工作并继续对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/introducing-claude-tag">Introducing Claude Tag \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/">Anthropic’s Claude Tag is learning your company, one Slack ...</a></li>
<li><a href="https://9to5mac.com/2026/06/23/anthropic-launches-claude-tag-enterprise-collaborative-tool-for-agentic-workflows/">Anthropic launches Claude Tag enterprise collaborative tool ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对多玩家方面和潜在的生产力提升表示兴奋，但也提出了对 token 成本、企业安全与合规性以及 Claude 区分学习内容与忽略内容能力的担忧，一些用户指出错误的假设可能导致有缺陷的见解。

**标签**: `#AI Agents`, `#Slack`, `#Anthropic`, `#Enterprise AI`, `#Collaboration`

---

<a id="item-8"></a>
## [LLM 提示注入即角色混淆](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 8.0/10

Charles Ye、Jasmine Cui 和 Dylan Hadfield-Menell 的研究表明，LLM 无法可靠地区分特权文本（如系统指令）和不可信的用户输入，并且模型更重视文本的风格而非实际内容，从而实现了有效的越狱攻击。 这一发现削弱了当前的提示注入防御，表明基于风格的攻击成功率可达 61%，并指出如果没有真正的角色感知，注入防御将永远是一场打地鼠游戏。 研究人员发现，“去风格化”——将文本重写为看起来不像角色标签中的预期格式——将攻击成功率从 61%降至 10%，这种变化对人类几乎不可见，但对 LLM 影响巨大。他们测试了 gpt-oss-20b 等模型，观察到追加模仿模型内部思考风格的文本可以覆盖初始训练。

rss · Simon Willison · Jun 22, 23:59

**背景**: 提示注入是一种安全漏洞，攻击者通过精心构造输入，诱使 LLM 忽略其预期指令而遵循攻击者命令。该漏洞在 OWASP 2025 年 LLM 应用 Top 10 中排名第一，因为它利用了 LLM 的一个基本架构弱点：无法可靠区分可信指令和不可信数据。这项研究引入了“角色混淆”作为根本机制，即模型混淆自身的角色标签（如<system>、<think>）与用户输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://blog.cyberdesserts.com/prompt-injection-attacks/">Prompt Injection Attacks: Examples and Defences</a></li>
<li><a href="https://arxiv.org/abs/2306.05499">[2306.05499] Prompt Injection attack against LLM-integrated ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（通过 Simon Willison 的博客）对该论文的可读性总结和“去风格化”发现表现出浓厚兴趣。评论者指出，这证实了长期以来对基于角色的防御脆弱性的怀疑，并呼吁进行更根本的架构变革。

**标签**: `#LLM Security`, `#Prompt Injection`, `#AI Safety`, `#Jailbreak`

---

<a id="item-9"></a>
## [将 Moebius 0.2B 图像修复模型移植到浏览器中运行](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

Simon Willison 成功将原本需要 PyTorch 和 NVIDIA CUDA 的 Moebius 0.2B 图像修复模型，通过 ONNX Runtime Web 和 WebGPU 移植到浏览器中完全运行。他创建了一个在线演示（simonw.github.io/moebius-web/），用户可以上传图片、标记要移除的区域并本地运行修复。 这表明小型但强大的 AI 模型可以直接在浏览器中部署，无需服务器端 GPU 硬件，使任何拥有 WebGPU 兼容浏览器的用户都能使用高级图像修复功能。这也展示了 WebGPU 在机器学习推理方面的日益成熟，以及智能体辅助模型移植的潜力。 该移植使用了 ONNX Runtime Web 的 WebGPU 后端，将 PyTorch 模型转换为 ONNX 格式。Simon 使用 Claude Code 作为智能体协助移植过程，并利用 Claude.ai 生成的研究文档来指导实现。

rss · Simon Willison · Jun 22, 23:43

**背景**: 图像修复是一种用合理内容填充图像中缺失或移除区域的技术。Moebius 是一个 0.2B 参数的模型，性能可与 10B+模型媲美，同时足够轻量以实现高效部署。WebGPU 是一种现代浏览器 API，允许直接访问 GPU 计算，无需插件即可在浏览器中运行机器学习推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19195">[2606.19195] Moebius: 0.2B Lightweight Image Inpainting ...</a></li>
<li><a href="https://github.com/hustvl/Moebius">GitHub - hustvl/Moebius: [ECCV 2026] Moebius: 0.2B ...</a></li>
<li><a href="https://hustvl.github.io/Moebius/">Moebius: 0.2B Lightweight Image Inpainting Framework with 10B ...</a></li>

</ul>
</details>

**标签**: `#image inpainting`, `#WebGPU`, `#browser ML`, `#model porting`, `#AI demo`

---

<a id="item-10"></a>
## [近半数 LG 智能电视应用含住宅代理 SDK](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks) ⭐️ 8.0/10

Spur 研究人员扫描了 6038 款 LG 和三星智能电视应用，发现其中 2058 款包含住宅代理 SDK，LG 平台受影响比例接近一半。这些 SDK 可将电视变为代理节点，通过家庭网络路由第三方流量。 这带来了严重的隐私和安全风险，因为家庭 IP 地址可能在用户不知情的情况下被用于网络爬虫或僵尸网络等活动。这也凸显了 LG 和三星等电视制造商缺乏监管，而亚马逊和 Roku 已禁止此类 SDK。 受影响的应用多为屏保、时钟和小游戏；部分应用在用户关闭后仍可继续运行代理功能。Spur 指出，Bright Data 的 SDK 包含阻止连接私有 IP 范围的列表，但 Massive 和 Honeygain/Oxylabs 的 SDK 中未发现类似保护。

telegram · zaihuapd · Jun 23, 02:26

**背景**: 住宅代理 SDK 是一种软件库，允许第三方通过家庭设备的 IP 地址路由互联网流量，使流量看起来来自合法的住宅连接。该技术常用于网络爬虫、广告欺诈或绕过地理限制，但也可能被滥用于恶意目的，如 Kimwolf 僵尸网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spur.us/blog/smart-tv-apps-residential-proxy-sdks">Nearly Half of LG Smart TV Apps Contain Residential Proxy SDKs</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/06/23/tv-residential-proxy-sdk/">Residential proxy SDKs are hiding in LG and Samsung smart TV ...</a></li>
<li><a href="https://cyberinsider.com/50-of-lg-and-samsung-smart-tv-apps-embed-residential-proxies/">50% of LG and Samsung smart TV apps embed residential proxies</a></li>

</ul>
</details>

**标签**: `#smart TV`, `#security`, `#privacy`, `#residential proxy`, `#IoT`

---

<a id="item-11"></a>
## [三星发布 UFS 5.0，带宽 10.8 GB/s，面向端侧 AI](https://news.samsung.com/global/samsung-unveils-industrys-fastest-ufs-5-0-solution-for-next-gen-on-device-ai-applications) ⭐️ 8.0/10

三星宣布推出 UFS 5.0，这是业界最快的通用闪存存储解决方案，顺序读取速度高达 10.8 GB/s，顺序写入速度高达 9.5 GB/s，计划于 2025 年第四季度量产。 这一突破将速度提升至 UFS 4.1 的两倍，同时功耗效率提高 40%以上，为旗舰手机、XR 头显和 AI 可穿戴设备中的端侧 AI 应用提供了更快的数据访问能力。 UFS 5.0 基于 JEDEC 嵌入式存储接口标准，采用优化的 PAM4 信号技术，提供最高 1 TB 容量，封装尺寸比上一代缩小 16.7%。

telegram · zaihuapd · Jun 23, 09:17

**背景**: UFS（通用闪存存储）是用于移动设备的闪存存储标准，提供高速数据传输。端侧 AI 是指在设备本地而非云端运行 AI 模型，需要快速存储来加载大型模型和数据。UFS 5.0 基于 UniPro 3.0 和 M-PHY 6.0 接口实现性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.samsung.com/global/samsung-unveils-industrys-fastest-ufs-5-0-solution-for-next-gen-on-device-ai-applications">Samsung Unveils Industry’s Fastest UFS 5.0 Solution for Next ...</a></li>
<li><a href="https://semiconductor.samsung.com/estorage/ufs/ufs-5-0/">UFS 5.0 | Universal Flash Storage | Samsung Semiconductor Global</a></li>

</ul>
</details>

**标签**: `#storage`, `#Samsung`, `#UFS 5.0`, `#on-device AI`, `#flash memory`

---

<a id="item-12"></a>
## [研究显示洗牌 14 次才能随机化一副牌](https://www.quantamagazine.org/seven-perfect-shuffles-randomize-a-deck-of-cards-but-how-many-sloppy-ones-20260617/) ⭐️ 8.0/10

新研究表明，对于非专业洗牌者，大约需要 14 次鸽尾式洗牌才能将一副 52 张牌充分随机化，这扩展了 1992 年关于完美切牌需 7 次洗牌的经典结论。 这一发现将概率论中的基础结论更新到更现实的条件下，对赌场安全、纸牌游戏公平性以及理解日常生活中的随机性具有重要意义。 研究人员使用二进制“条形码”追踪卡片，检测残留有序的“冷点”区域，证明了即使在不精准洗牌中也存在截止现象。当前模型仍假设卡片一张张交错落下，而非成沓掉落。

telegram · zaihuapd · Jun 23, 16:04

**背景**: 1992 年 Bayer 和 Diaconis 的经典结果使用了 Gilbert-Shannon-Reeds 模型，该模型假设完美对半切牌。新研究放宽了这一假设，采用随机切牌位置，更贴近大多数人的洗牌方式。截止现象描述了随着洗牌次数增加，牌序从有序到随机的急剧转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riffle_shuffle_permutation">Riffle shuffle permutation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#probability`, `#card shuffling`, `#randomness`

---