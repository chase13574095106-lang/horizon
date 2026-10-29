---
layout: default
title: "Horizon Summary: 2026-10-29 (ZH)"
date: 2026-10-29
lang: zh
---

> From 31 items, 8 important content pieces were selected

---

1. [谷歌发布 Gemini 4 Argon，物理推理得分 87%](#item-1) ⭐️ 9.0/10
2. [指纹识别脚本的混淆代码被误认为生物武器，导致 LLM 拒绝分析](#item-2) ⭐️ 8.0/10
3. [谷歌发布 Gemini 4 Carbon，一款受限的前沿 AI 模型](#item-3) ⭐️ 8.0/10
4. [苹果推出配备 PROLED XDR 显示屏和触摸屏的 MacBook Pro](#item-4) ⭐️ 8.0/10
5. [Apple 的 git 仍信任已泄露的 eMudhra 证书](#item-5) ⭐️ 8.0/10
6. [Google 提出睡眠框架，助大模型持续学习不遗忘](#item-6) ⭐️ 8.0/10
7. [OpenAI 发布 GPT-6.1 Terra，API 价格减半](#item-7) ⭐️ 8.0/10
8. [长鑫存储拟量产 HBM3E，良率仅两三成](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 4 Argon，物理推理得分 87%](https://t.me/zaihuapd/44764) ⭐️ 9.0/10

谷歌发布了新一代多模态推理模型 Gemini 4 Argon，强化了物理理解、代码生成与视觉语义推理能力。该模型在具身推理基准 ERQA 上凭纯推理获得 87% 的得分，领先其他前沿模型，并能操控波士顿动力 Spot 四足机器人完成取物、投掷等任务。 此次发布标志着多模态推理在机器人领域的重大飞跃，表明通用模型能够直接控制复杂机器人并生成仿真数据以提升真实世界性能。这可能加速具身智能的发展，并降低在现实场景中部署高性能机器人的门槛。 Argon 能够生成仿真数据，将真实机器人的任务成功率从 56% 提升至 75%，同时将任务用时从 35 秒缩短至 24 秒。该模型现已通过 google-genai SDK 提供，定价为每百万输入 token 2 美元，每百万输出 token 价格在来源中未完整显示。

telegram · zaihuapd · Oct 28, 17:09

**背景**: ERQA（具身推理问答）是一个用于评估多模态 AI 模型在具身推理任务上表现的基准，涵盖空间推理和真实机器人场景。波士顿动力 Spot 是一款四足机器人，以敏捷移动著称，加装机械臂后具备移动操作能力。google-genai SDK 为开发者提供统一接口，以便将 Gemini 模型集成到应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/embodiedreasoning/ERQA">GitHub - embodiedreasoning/ERQA: Embodied Reasoning Question ...</a></li>
<li><a href="https://bostondynamics.com/products/spot/">Spot | Boston Dynamics</a></li>
<li><a href="https://github.com/googleapis/python-genai">GitHub - googleapis/python-genai: Google Gen AI Python SDK ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal`, `#robotics`, `#Google`, `#Gemini`

---

<a id="item-2"></a>
## [指纹识别脚本的混淆代码被误认为生物武器，导致 LLM 拒绝分析](https://nullpt.rs/fingerprinting-bioweapons) ⭐️ 8.0/10

nullpt.rs 上的一篇博客文章调查了浏览器指纹识别脚本的混淆 JavaScript 代码如何与生物武器相关内容相似，导致大型语言模型拒绝分析。Hacker News 上的讨论（185 条评论）强调了这对 AI 安全过滤器和对抗性混淆的更广泛影响。 这一事件凸显了 LLM 安全过滤器中误报的挑战，合法的安全研究或良性代码可能被阻止，从而阻碍防御工作。它还揭示了混淆技术与 AI 审核之间正在出现的军备竞赛，对网络安全和 AI 安全都有影响。 该指纹识别脚本可能使用了字符串编码或打包等混淆技术，产生了类似危险内容的模式，从而触发安全分类器。社区成员指出，一些模型（如 GLM-5.3）遵从了分析请求，而前沿商业模型则拒绝，这表明安全过滤器的严格程度存在差异。

hackernews · hazebooth · Oct 28, 17:13 · [社区讨论](https://news.ycombinator.com/item?id=50276998)

**背景**: 浏览器指纹识别脚本收集设备和浏览器属性以唯一标识用户，通常用于机器人检测或跟踪。为了防止逆向工程，这些脚本通常被混淆，使其代码难以阅读。LLM 安全过滤器经过训练，可以阻止看似涉及生物武器等有害主题的请求，但它们可能会对混淆或安全相关的代码产生误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://klu.ai/glossary/llm-guardrails">LLM Guardrails — Klu</a></li>
<li><a href="https://community.openai.com/t/recent-safety-filter-update-causing-high-false-positives-on-legitimate-academic-ml-research/1410325">Recent Safety Filter Update Causing High False Positives on...</a></li>
<li><a href="https://arxiv.org/abs/2606.11755">[2606.11755] Acoda: Adversarial Code Obfuscation for ...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了关于水印和反 LLM 字符串导致意外阻止的轶事，并对混淆与 AI 审核之间分形般的军备竞赛表示惊讶。一些人指出，像 GLM-5.3 这样的某些模型更为宽松，而另一些人则开玩笑说这种情况很荒谬。

**标签**: `#fingerprinting`, `#LLM safety`, `#obfuscation`, `#web security`, `#AI moderation`

---

<a id="item-3"></a>
## [谷歌发布 Gemini 4 Carbon，一款受限的前沿 AI 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) ⭐️ 8.0/10

谷歌发布了其最新前沿 AI 模型 Gemini 4 Carbon，该模型在 Artificial Analysis Intelligence Index v5.0 上以 59 分排名第一，并在编程和网络安全能力方面有显著提升。该模型基于两周前推出的 Gemini 4 Argon 构建，但仅限特定网络安全专家使用，并未公开可用。 此次发布凸显了谷歌在前沿模型竞赛中的快速迭代节奏，但受限的访问权限和令人困惑的模型命名（Carbon、Argon、Pro、Ultra、Flash）引发了关于产品清晰度和基准有效性的争论。对网络安全和长周期能力的关注表明其正战略性地进军高风险的企业和政府应用领域。 Gemini 4 Carbon 在 SEC-bench 上达到 88.2%，并在内部编程环境中显示出更低的对齐错误和虚构率，但它本质上是 Argon 的稍好版本，且未公开可用。该模型的基准分数是在没有公布普遍可用日期的情况下展示的，这引发了关于其在快速发展的领域中相关性的质疑。

hackernews · acossta · Oct 28, 17:01 · [社区讨论](https://news.ycombinator.com/item?id=50276792)

**背景**: Gemini 是谷歌的旗舰大语言模型系列，提供 Ultra、Pro、Flash 和 Lite 等多个层级，以满足不同的性能和成本需求。像 Gemini 4 Carbon 这样的前沿模型是最先进且最昂贵的版本，通常用于网络安全和复杂推理等专业任务。Artificial Analysis Intelligence Index 是一个综合基准，评估模型在推理、知识、数学和编程方面的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/">Introducing Gemini 4 Carbon</a></li>
<li><a href="https://arstechnica.com/ai/2026/10/google-announces-gemini-4-carbon-its-latest-frontier-ai-model-that-you-cant-use/">Google announces Gemini 4 Carbon, its latest frontier AI ...</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-carbon">Gemini 4 Carbon (high) - Intelligence, Performance... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对谷歌令人困惑的模型命名和层级表示不满，有人开玩笑说即使给 100 美元也不知道如何向 Gemini 4 Argon 发出提示。其他人认为在快速发展的领域中，不发布模型只展示基准是没有意义的，还有人建议像 SEMVER 一样标准化 Ultra、Pro、Flash 和 Lite 等模型层级。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-4"></a>
## [苹果推出配备 PROLED XDR 显示屏和触摸屏的 MacBook Pro](https://www.apple.com/macbook-pro/proled-xdr-display/) ⭐️ 8.0/10

苹果发布了新款 MacBook Pro，配备基于串联 OLED 技术的 PROLED XDR 显示屏，并首次加入触摸屏。14 英寸和 16 英寸机型重量减轻约 15%，机身也更薄。 这是苹果首款触摸屏 Mac，标志着 Mac 交互方式的重大转变，可能重塑专业工作流程并影响整个笔记本电脑市场。新的显示技术也为笔记本电脑的视觉性能树立了新标杆。 PROLED XDR 显示屏提供高达 1000 尼特持续全屏亮度、2000 尼特峰值 HDR 亮度和 10,000,000:1 对比度。笔记本仍搭载 M5 Pro 和 M5 Max 芯片，14 英寸机型视频播放续航最长可达 22 小时。

hackernews · etothet · Oct 28, 17:10 · [社区讨论](https://news.ycombinator.com/item?id=50276940)

**背景**: XDR（极致动态范围）是苹果对高动态范围显示屏的 branding，此前用于采用 Mini-LED 背光的 Pro Display XDR 和 iPad Pro。PROLED XDR 是新的迭代，采用串联 OLED 技术，通过堆叠两层 OLED 来提升亮度和寿命。OLED 显示屏每个像素自发光，无需背光，能实现更深的黑色和更薄的面板，但长期使用可能出现烧屏现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/macbook-pro/proled-xdr-display/pdf/PROLED_XDR_Display_Technical_Paper.pdf">PROLED XDR DISPLAY Technology Overview - Apple</a></li>
<li><a href="https://support.apple.com/en-us/109039">About the Super Retina display and Super Retina XDR display ... Pro Display XDR - Tech Specs - Apple Support Apple Display Technology Explained - Retina vs Liquid Retina ... What Is XDR Display & Apple EDR on Mac? (2026 Guide) Beyond the Hype: Inside Apple’s New PROLED XDR Display Technology Apple launches PROLED XDR OLED display on MacBook Pro | The ...</a></li>
<li><a href="https://www.macrumors.com/2026/10/28/touchscreen-macbook-pro-debut-these-5-features/">Touchscreen MacBook Pro to Debut Today With These... - MacRumors</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人认为加入触摸屏会引发可用性抱怨，因为 macOS 的 UI 元素对 finger 来说太小；也有人称赞重量大幅减轻和更薄的设计。一些人对笔记本触摸的价值提出质疑，提到指纹问题和鼠标的精准性，还有人觉得苹果的设计功力在下降。

**标签**: `#Apple`, `#MacBook Pro`, `#hardware`, `#display technology`, `#touchscreen`

---

<a id="item-5"></a>
## [Apple 的 git 仍信任已泄露的 eMudhra 证书](https://emudhra.we-have-a-problem.com/apple.html) ⭐️ 8.0/10

截至 2026 年 10 月 28 日，Apple 的 macOS 及其捆绑的开发者工具（包括 git、curl 和 python3）仍然信任八个已泄露的 eMudhra 中间证书，尽管 Apple 已于 10 月 17 日收到事件通知。Apple 建议的缓解措施需要手动编辑证书链，而后续的操作系统更新可能会还原这些更改，从而重新引入漏洞。 这是一个重大的安全问题，因为它不仅影响 git，还影响许多依赖操作系统信任存储的系统工具，可能使开发者和 macOS 用户面临中间人攻击的风险。它凸显了操作系统级证书管理的混乱状态，并引发了对 Apple 安全实践的质疑。 这些已泄露的证书使用弱密钥，其私钥仅为个位数或两位数整数，而非强制要求的 384 位伪随机安全性，这使得攻击者能够冒充中间证书颁发机构。Apple 的缓解措施涉及手动编辑证书链，但操作系统更新可能会还原这些更改，这种情况至少已发生过一次。

hackernews · galadran · Oct 28, 11:03 · [社区讨论](https://news.ycombinator.com/item?id=50271640)

**背景**: eMudhra 是一家证书颁发机构，其颁发的八个中间证书使用了弱私钥，这些弱密钥于 2026 年 10 月被发现。这些证书被许多操作系统和应用程序信任，使攻击者能够拦截 TLS 流量。macOS 使用系统信任存储，而 git 和 curl 等捆绑工具会使用该存储，因此该存储中受损的证书会影响这些工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emudhra.we-have-a-problem.com/apple.html">Apple's git still trusts the compromised eMudhra certificates</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here's what you need ...</a></li>
<li><a href="https://blog.talosintelligence.com/compromised-intermediate-certificates/">Compromised eMudhra intermediate certificates</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Apple 的指导要求手动编辑证书链以及操作系统更新可能还原缓解措施表示愤怒，一些人指出该问题影响的不只是 git，还有许多系统工具。其他人批评操作系统级证书管理的混乱状态，并认为 Apple 应该可以轻松地在系统更新中移除已撤销的 CA 证书。一位评论者推测弱密钥生成可能是有意为之，但没有提供证据。

**标签**: `#security`, `#macOS`, `#TLS certificates`, `#git`, `#certificate management`

---

<a id="item-6"></a>
## [Google 提出睡眠框架，助大模型持续学习不遗忘](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research 提出了一种用于持续学习的“睡眠框架”，通过增加离线巩固阶段，在主动交互与离线睡眠之间周期切换，让大语言模型将短期上下文巩固为长期参数。该方法在 1000 万 token 长上下文、持续翻译和数学推理等任务上超过了 GPT-4 和 SFT 等基线。 这项工作针对灾难性遗忘这一持续学习中的主要障碍，有望让大模型在获取新技能的同时不丢失已有知识。如果得到验证，它可能影响未来大模型在动态环境中的训练和更新方式。 该框架在主动唤醒阶段和离线睡眠阶段之间交替，模型在睡眠阶段巩固知识；在长上下文（1000 万 token）、持续翻译和数学推理等测试中，它相比 GPT-4 和 SFT 基线表现出优势。不过，这仍是一个研究提案，计算开销和可扩展性等细节仍有待全面评估。

telegram · zaihuapd · Oct 28, 01:46

**背景**: 灾难性遗忘是指神经网络（包括大语言模型）在学习新任务或新数据时，会丢失先前学到的知识。持续学习旨在让模型能够顺序学习而不遗忘，而受生物大脑在睡眠中巩固记忆启发的离线巩固是一种有前景的方法。传统机器学习将训练和推理分离，但持续学习模糊了这一界限，要求模型不断适应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/">The sleep framework: A new way for LLMs to retain knowledge ...</a></li>
<li><a href="https://www.nerdheadz.com/blog/continual-learning-llms-offline-phase-sleep">Continual Learning in LLMs : The Sleep Problem | NerdHeadz Blog</a></li>
<li><a href="https://arxiv.org/abs/2402.01364">[2402.01364] Continual Learning for Large Language Models: A Survey</a></li>

</ul>
</details>

**标签**: `#continual learning`, `#LLM`, `#catastrophic forgetting`, `#Google Research`, `#sleep framework`

---

<a id="item-7"></a>
## [OpenAI 发布 GPT-6.1 Terra，API 价格减半](https://t.me/zaihuapd/44750) ⭐️ 8.0/10

OpenAI 发布了 GPT-6.1 Terra，该模型主打视觉推理、精准的电脑操作和更自然的写作，标准 API 价格比 GPT-5.6 Terra 低 50%。目前已向 ChatGPT Work 和 Codex 的 Plus、Pro、Enterprise 和 Edu 用户开放。 此次发布大幅降低了先进 AI 能力的成本，使视觉和电脑操作功能对开发者和企业更加可及。基准测试的大幅提升和价格减半可能迫使竞争对手以更低价格提供类似功能。 GPT-6.1 Terra 在基准测试中比 GPT-5.6 Terra 高 15 个百分点，成本约为三分之一，低推理强度下的错误率从 53.6% 降至 16.7%。标准 API 按每百万输入 token 定价，但具体价格未在来源中说明。

telegram · zaihuapd · Oct 28, 03:26

**背景**: GPT-6.1 Terra 是 OpenAI GPT-6.1 系列中的中端模型，专为日常代理场景、编程和文本任务设计，具有强大的截图理解能力。ChatGPT Work 是一个用于较长、多步骤工作和交付成果的代理，而 Codex 是 OpenAI 的 AI 编程伙伴，可在 ChatGPT、编辑器和终端中使用。该模型的电脑操作能力指其与软件界面交互（如点击和输入）以自动化任务的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/gpt-6-1-terra">GPT - 6 . 1 Terra API: Visual Reasoning & Writing | Kie.ai</a></li>
<li><a href="https://simonwillison.net/2026/Oct/26/gpt-61-terra/">GPT - 6 . 1 Terra | Simon Willison’s Weblog</a></li>
<li><a href="https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex">ChatGPT Work and Codex - OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#LLM`, `#model-release`, `#API-pricing`, `#benchmarks`

---

<a id="item-8"></a>
## [长鑫存储拟量产 HBM3E，良率仅两三成](https://www.reuters.com/world/china/chinas-cxmt-start-advanced-ai-memory-production-despite-poor-yields-sources-say-2026-10-28/) ⭐️ 8.0/10

据路透社援引两名知情人士消息，长鑫存储（CXMT）已向多家国内 AI 芯片设计公司送样 HBM3E，并计划在未来两个月内启动限量生产。但其良率仅为 20% 至 30%，远低于 SK 海力士约 70% 的水平，且测试性能更接近 SK 海力士上一代 HBM3。 这标志着在美国出口管制下，中国 AI 内存自给自足迈出重要一步，因为国内 AI 芯片设计公司目前面临高带宽内存严重短缺。尽管良率低、性能落后，长鑫的入局仍可能减少对外国供应商的依赖，并重塑中国 AI 硬件竞争格局。 长鑫的 HBM3E 预计售价将高于海外同类产品，反映出低良率和有限规模带来的成本压力。性能差距意味着它可能无法匹敌 SK 海力士、美光或三星最新的 HBM3E，后者为 AI 训练和推理提供更高带宽和能效。

telegram · zaihuapd · Oct 28, 06:19

**背景**: 高带宽内存（HBM）是一种垂直堆叠并通过先进封装连接的 DRAM，能提供远超传统内存的带宽，对 AI 加速器至关重要。HBM3E 是 HBM3 的增强版本，容量和速度更高；SK 海力士、美光、三星是主要供应商。长鑫存储成立于 2016 年，总部位于合肥，是中国最大的 DRAM 制造商，也是北京推动半导体自给自足的关键力量。良率是指制造出的芯片中符合性能规格的比例，低良率会显著推高单颗芯片成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yield_(metric)">Yield (metric) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#HBM3E`, `#CXMT`, `#semiconductor manufacturing`, `#AI memory`, `#export controls`

---