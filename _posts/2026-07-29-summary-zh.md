---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> From 34 items, 10 important content pieces were selected

---

1. [TurboFieldfare：在 M 系列 Mac 上用 2GB 内存运行 Gemma 4 26B](#item-1) ⭐️ 9.0/10
2. [Mitchell Hashimoto 创立 Superlogical，将 Ghostty 所有权转让给非营利组织](#item-2) ⭐️ 8.0/10
3. [Kimi K3-256k：一半配额，相同性能](#item-3) ⭐️ 8.0/10
4. [长政策文档无法可靠约束 AI 智能体](#item-4) ⭐️ 8.0/10
5. [AI 蠕虫通过 Word 的 Copilot 自我传播](#item-5) ⭐️ 8.0/10
6. [Matthew Green：AI 密码分析或可增强后量子密码信心](#item-6) ⭐️ 8.0/10
7. [Claude 共享链接遭搜索引擎索引，用户数据泄露](#item-7) ⭐️ 8.0/10
8. [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动，发出国际通缉](#item-8) ⭐️ 8.0/10
9. [报告：Hugging Face 被广泛用于生成深度伪造裸照](#item-9) ⭐️ 8.0/10
10. [中国起草反网络暴力法，规制 AI 生成网暴内容](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TurboFieldfare：在 M 系列 Mac 上用 2GB 内存运行 Gemma 4 26B](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

一个名为 TurboFieldfare 的开源 Swift/Metal 推理引擎，通过从 SSD 流式传输路由专家，仅用约 2GB 内存即可在任何 M 系列 Mac 上运行 4 位量化的 Gemma 4 26B-A4B-IT 模型。 这一突破使得在 8GB Mac 等内存受限设备上运行大型混合专家模型成为可能，将前沿 AI 普及到消费级硬件，并可能影响未来的设备端 AI 架构。 该引擎在 8GB M2 MacBook Air 上达到 5-6 tok/s，在 M5 MacBook Pro 上达到 31-35 tok/s，通过小型专家缓存和有界并行 pread 将 SSD 读取与 GPU 计算重叠。

hackernews · gitpusher42 · Jul 29, 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: 像 Gemma 4 26B 这样的混合专家（MoE）模型参数众多，但每个 token 只激活一部分，效率高但内存占用仍大。4 位量化减小了模型体积，但完整的 14GB 权重仍超出典型 Mac 内存。TurboFieldfare 仅将共享层和 KV 缓存保留在 RAM 中，按需从 SSD 流式传输专家权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/drumih/turbo-fieldfare">GitHub - drumih/ turbo - fieldfare : Gemma 4 26B-A4B inference in...</a></li>
<li><a href="https://andrew.ooo/posts/flash-moe-397b-model-macbook-local-inference/">Flash- MoE : Running a 397B Parameter Model on... — andrew.ooo</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/">Gemma 4 with quantization-aware training - The Keyword</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这种方法，有人指出与 llama.cpp 中基于 mmap 的解决方案相似，但强调 TurboFieldfare 对 SSD 读取与推理的同步进行了调优。一位用户提供了旧版 macOS 的解决方法，另一人表达了在相关项目上合作的兴趣。

**标签**: `#on-device AI`, `#inference engine`, `#MoE`, `#Swift`, `#Metal`

---

<a id="item-2"></a>
## [Mitchell Hashimoto 创立 Superlogical，将 Ghostty 所有权转让给非营利组织](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto 宣布成立新公司 Superlogical，该公司将在开源 libghostty 终端库之上构建商业产品，同时将 Ghostty 终端模拟器的所有权转让给一个非营利组织。 此举确保 Ghostty 保持社区所有和开源，同时 Superlogical 可以可持续地开发利用 libghostty 的专有工具，可能促进更丰富的终端生态系统。 Superlogical 将把 libghostty 作为公共构建模块，使用与其他人相同的 MIT 许可组件，并继续向上游贡献共享终端工作，使所有 libghostty 消费者受益。

hackernews · yan · Jul 29, 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**背景**: Ghostty 是一个快速、功能丰富、跨平台的终端模拟器，使用 GPU 加速和原生 UI。libghostty 是其底层库，一个跨平台、零依赖的 C 和 Zig 库，用于构建终端模拟器或处理终端功能，如 VT 序列解析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬将 Ghostty 转让给非营利组织以及开源依赖模型，一些人将其与 OLE/COM 等旧技术相提并论。少数人对神秘的标题表示不满，但总体情绪是积极的。

**标签**: `#open-source`, `#terminal`, `#startup`, `#software-engineering`, `#community`

---

<a id="item-3"></a>
## [Kimi K3-256k：一半配额，相同性能](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Kimi 发布了 K3-256k 模型，这是其旗舰模型 K3 的变体，在 256k 上下文窗口内消耗一半的配额，同时提供相同的结果。 这一价格变化使 Kimi 对大多数用户来说更加实惠，因为 256k 上下文覆盖了绝大多数实际用例，可能加速 LLM 市场的商品化。 K3-256k 模型在 API 调用中使用相同的模型 ID 'k3-256k'，其配额消耗正好是原始 K3（1M 上下文）模型的一半。保持在 256k token 以内的用户实际上只需支付一半的价格。

hackernews · monneyboi · Jul 29, 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49101852)

**背景**: 上下文窗口大小决定了 LLM 一次可以处理的文本量。虽然 100 万 token 的上下文窗口令人印象深刻，但大多数实际任务（如代码生成、文档分析）都在 256k token 以内。Kimi 的 K3 是一款拥有 100 万 token 上下文的旗舰模型，而新的 K3-256k 变体为典型工作负载提供了经济高效的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>
<li><a href="https://kernelbench.com/models/kinetic-0715">Kimi K3 (256k) · kernelbench</a></li>

</ul>
</details>

**社区讨论**: 社区成员对此表示欢迎，指出 256k 上下文对大多数任务来说已经足够，而且降价幅度巨大。一些人认为这是 LLM 商品化的标志，随着超大规模云服务商提供更便宜的 token，美国 AI 实验室正在失去其护城河。

**标签**: `#LLM`, `#AI pricing`, `#context window`, `#Kimi`, `#commoditization`

---

<a id="item-4"></a>
## [长政策文档无法可靠约束 AI 智能体](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

一篇名为 Handbook.md 的新论文表明，由于长上下文模型的根本性限制（如注意力稀释和记忆约束），长政策文档无法可靠地约束 AI 智能体。 这一发现挑战了长上下文 LLM 能有效遵循复杂策略的假设，这对金融和医疗等实际应用中的 AI 安全与智能体治理至关重要。 该论文提供了实证证据，表明即使是最先进的模型也难以处理长政策文档，并建议可能需要采用替代方法，例如在智能体数据集上进行强化学习。

hackernews · spIrr · Jul 29, 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49096969)

**背景**: 长上下文 LLM 声称能处理多达 100 万个 token，但由于量化、KV 缓存限制和糟糕的采样，其性能会下降。现有基准测试往往无法捕捉长文本上的真实推理。AI 智能体经济缺乏治理基础设施，使这项研究具有及时性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentgoverning.com/">The independent benchmark for AI agent governance</a></li>
<li><a href="https://github.com/agentic-control-plane/agentgovbench">GitHub - agentic-control-plane/agentgovbench: Agent governance ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出了实际问题：用户报告称，像 Claude 这样的模型在约 10 分钟后会忽略 CLAUDE.md 中的指令，而提示中的指令效果更好。一些人认为人类也难以处理长政策文档，因此该基准可能反映的是普遍限制而非模型特定缺陷。

**标签**: `#LLM`, `#long-context`, `#AI safety`, `#benchmark`, `#agent`

---

<a id="item-5"></a>
## [AI 蠕虫通过 Word 的 Copilot 自我传播](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 8.0/10

研究人员展示了一种新的提示注入变体，将 Microsoft Copilot for Word 转变为自我复制 AI 蠕虫的传播媒介，隐藏在文档中的恶意指令可导致 Copilot 修改文档并将攻击传播到新文档。 此漏洞代表了一类新型 AI 安全威胁，LLM 集成的应用程序可被利用来自主传播恶意软件，突显了当前缓解措施无法完全解决的系统性风险。 该蠕虫利用了 AI 无法区分数据和指令的弱点，使用白文本等技术隐藏提示。两次缓解尝试（包括模型升级）均未能消除此类漏洞。

hackernews · Canopy9560 · Jul 29, 11:44 · [社区讨论](https://news.ycombinator.com/item?id=49096188)

**背景**: 提示注入是一种网络安全攻击，通过精心设计的输入使 LLM 忽略先前指令并执行非预期操作。AI 蠕虫是使用基于 LLM 的技术自主传播的恶意软件。Copilot for Word 是一个 AI 助手，可根据用户提示编辑文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/">Context Collapse, Part 3 - AI Worming through Word | En Klype Salt</a></li>
<li><a href="https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html">Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models</a></li>
<li><a href="https://www.theregister.com/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588">Word worm crawls into Copilot , spreads chaos</a></li>

</ul>
</details>

**社区讨论**: 评论者表示担忧，认为只要 AI 将指令与数据混合，此类漏洞从根本上就无法修复。有人指出，授予 AI 代理过多访问权限存在风险，并且白文本等技术仍然有效。一位评论者分享了使用 Unicode 字体技巧欺骗前沿算法的真实案例。

**标签**: `#AI security`, `#prompt injection`, `#Copilot`, `#adversarial attacks`, `#LLM vulnerabilities`

---

<a id="item-6"></a>
## [Matthew Green：AI 密码分析或可增强后量子密码信心](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

密码学家 Matthew Green 评论称，当前向后量子密码的过渡是 AI 推动密码分析发展的绝佳时机，可能增强对 HAWK 等新算法的信心。 这一观点凸显了 AI 驱动的密码分析可能打破或验证新后量子标准的独特机遇，从而影响未来通信的安全格局。 Green 提及 Anthropic 近期工作，其中 Claude Mythos 发现了 AES 和 HAWK 的弱点，每次攻击的 API 使用成本约 10 万美元。他还引用了 Impagliazzo 的五世界理论，指出如果 AI 破坏所有困难问题，我们可能生活在 Minicrypt 世界中。

rss · Simon Willison · Jul 29, 18:18

**背景**: 后量子密码学（PQC）旨在开发能抵御量子计算机攻击的算法，量子计算机可能破解当前的 RSA 和椭圆曲线密码。NIST 自 2017 年起一直在标准化 PQC 算法，并于 2024 年发布了最终标准。HAWK 是候选标准之一。Impagliazzo 的五世界理论对可能的计算复杂性场景进行分类，其中 Minicrypt 是一个公钥密码不可能存在的世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://www.ai-jarvis.eu/anthropics-mythos-found-flaws-aes-and-hawk-cryptography-100000-attack">Anthropic's Mythos Found Flaws in AES and HAWK Cryptography ...</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#standards`

---

<a id="item-7"></a>
## [Claude 共享链接遭搜索引擎索引，用户数据泄露](https://t.me/zaihuapd/42830) ⭐️ 8.0/10

Anthropic 的 Claude 共享对话功能存在隐私漏洞，生成的公开链接未设置 noindex 标签，导致被 Google 等搜索引擎索引，泄露了 API 密钥、加密货币钱包、社会安全号码等敏感信息。 该漏洞影响广泛使用的 AI 服务，泄露高度敏感的个人和企业数据，带来严重的隐私和安全风险。这与一年前 ChatGPT 出现的类似问题如出一辙，凸显了 AI 聊天共享功能的系统性风险。 共享对话默认公开且未设置 noindex 标签，导致搜索引擎可抓取并索引。建议用户立即进入设置中的“共享对话”管理页面，手动删除涉及隐私的聊天记录。

telegram · zaihuapd · Jul 29, 02:40

**背景**: Noindex 标签是一种 HTML 元标签或 HTTP 头，用于告知搜索引擎不要将页面纳入搜索结果。如果没有该标签，任何公开可访问的 URL 都可能被索引。Claude 的共享功能为每个对话生成公开 URL，若未适当限制，这些 URL 可能被搜索引擎发现。大约一年前 ChatGPT 曾出现类似问题并迅速修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/">PSA: Your Claude shared chats and Artifacts may have... | TechCrunch</a></li>
<li><a href="https://newscord.org/article/claude-shared-chats-and-artifacts-indexed-on-google-search-after-anthropic-share--Story_20260727_PSAYourClaudesharedcecfd763c">Claude Shared Chats and Artifacts Indexed on Google... | NewsCord</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/block-indexing">Block Search Indexing with noindex | Google Search Central</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#AI`, `#Claude`, `#data leak`

---

<a id="item-8"></a>
## [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动，发出国际通缉](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

2026 年 7 月 29 日，俄罗斯联邦安全局（FSB）依据《刑法》第 205.1 条第 1.1 款（协助恐怖活动）对 Telegram 创始人帕维尔·杜罗夫提起刑事指控，并将其列入国际通缉名单，指控 Telegram 拒绝删除用于在俄罗斯境内协调攻击的频道和机器人。 这标志着俄罗斯对科技平台打击力度的显著升级，可能开创平台创始人对用户生成内容承担个人责任的先例。这也可能影响 Telegram 的全球运营，因为杜罗夫面临与俄罗斯有引渡条约国家的逮捕风险。 FSB 特别指出 Telegram 未能删除被乌克兰情报机构及恐怖/极端组织用于协调破坏、恐怖袭击、大规模杀戮和诈骗的频道和机器人，导致人员伤亡和数十亿卢布损失。指控依据的是《刑法》第 205.1 条第 1.1 款（协助恐怖活动）。

telegram · zaihuapd · Jul 29, 05:56

**背景**: Telegram 是由帕维尔·杜罗夫及其兄弟尼古拉于 2013 年创立的加密通讯应用，目前月活跃用户超过 10 亿。FSB 是俄罗斯的主要安全机构，前身为克格勃。俄罗斯《刑法》第 205.1 条将协助恐怖活动定为犯罪，包括提供便利恐怖行为的资源或服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://meduza.io/en/news/2026/07/29/russia-s-fsb-security-service-accuses-telegram-founder-pavel-durov-of-aiding-terrorism-issues-international-arrest-warrant">Russia ’s FSB security service accuses Telegram founder... — Meduza</a></li>
<li><a href="https://tass.com/society/2166649">Russia ’s FSB charges Telegram co-founder Durov with... - TASS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pavel_Durov">Pavel Durov - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#Russia`, `#terrorism`, `#regulation`, `#Pavel Durov`

---

<a id="item-9"></a>
## [报告：Hugging Face 被广泛用于生成深度伪造裸照](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

AI Forensics 于 7 月 28 日发布的报告显示，Hugging Face 被广泛用于生成非自愿的深度伪造裸照，包括儿童性虐待内容。该组织发现，平台上排名前九的图像编辑模型中有七个能通过简单提示轻易为女性“脱衣”，研究人员设置的蜜罐空间在 7 天内收到超过 1000 条请求，其中 73%涉及性内容，近 7%针对儿童。 该报告揭示了 AI 模型托管平台在安全和伦理方面的严重缺陷，Hugging Face 薄弱的防护措施使得非自愿私密图像的生成被广泛滥用。这些发现凸显了加强内容审核和平台问责的紧迫性，以保护个人（尤其是未成年人）免受 AI 驱动的剥削。 报告指出，Hugging Face 在平台层面几乎未实施防护措施，与其禁止非自愿性内容及未成年人裸露的政策相违背。AI Forensics 建议增加提示词过滤与输出扫描机制，以阻止有害图像生成。

telegram · zaihuapd · Jul 29, 08:20

**背景**: Hugging Face 是一个流行的机器学习模型和数据集共享平台，被 AI 社区广泛使用。深度伪造色情内容是指利用 AI 在未经同意的情况下制作他人的虚假裸照，通常对受害者造成严重伤害。欧洲非营利组织 AI Forensics 的报告揭示了此类平台上的开源模型如何被滥用于恶意目的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_pornography">Deepfake pornography - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#deepfake`, `#Hugging Face`, `#content moderation`, `#child safety`

---

<a id="item-10"></a>
## [中国起草反网络暴力法，规制 AI 生成网暴内容](https://mp.weixin.qq.com/s/PrzKFhbwjgFEGBPADvFD6Q) ⭐️ 8.0/10

2026 年 7 月 29 日，国家互联网信息办公室公布《反网络暴力法（征求意见稿）》，首次将利用 AI 技术制作、传播网络暴力信息纳入专门规制。 该立法标志着中国 AI 治理的重要一步，明确了平台监测和防范 AI 生成网暴内容的义务，并为受害者提供了更强有力的法律保护，包括人格权侵害禁令和精神损害赔偿。 草案共七章六十条，明确网络暴力是指通过网络集中或持续侵害他人名誉权、隐私权、肖像权、个人信息等合法权益的活动。要求平台建立监测识别机制和防护功能，并构建多部门协同的政府治理体系。

telegram · zaihuapd · Jul 29, 10:59

**背景**: 网络暴力在中国已成为严重的社会问题，如“人肉搜索”和 AI 生成的深度伪造滥用等事件造成广泛伤害。草案基于现有法规，如 2023 年《关于依法惩治网络暴力违法犯罪的指导意见》和民法典的人格权侵害禁令制度，旨在提供全面的法律框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.js.xinhuanet.com/20230713/45eb9dff79b040a7a9c3aa17aeea0a88/c.html">江苏多地法院探索发出人格权侵害禁令_新华网江苏频道</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607291634950.html">多类 网 暴 行为拟被明确立 法 惩治！ 南都曾曝光“人肉开盒”乱象 | 南都N视频</a></li>
<li><a href="https://t.me/tnews365/35453">竹新社 – Telegram</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#cyberbullying`, `#China law`, `#platform governance`

---