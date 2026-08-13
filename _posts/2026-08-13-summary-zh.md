---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> From 26 items, 9 important content pieces were selected

---

1. [OpenAI 与 Cerebras 推出 GPT-5.6 Sol Ultrafast，速度提升 7 倍](#item-1) ⭐️ 9.0/10
2. [谷歌发布 Gemini 3.7 Flash，定价具有竞争力](#item-2) ⭐️ 8.0/10
3. [DRAM 意面化：新攻击绕过内存保护](#item-3) ⭐️ 8.0/10
4. [选择无聊技术：创新代币概念](#item-4) ⭐️ 8.0/10
5. [DeepSeek 发布开源 AI 代理 Harness 开发者预览版](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Pro 0813 发布，开放权重](#item-6) ⭐️ 8.0/10
7. [DeepMind 的 SL2T 将手语 AI 带入 Pixel 11](#item-7) ⭐️ 8.0/10
8. [OpenAI 升级 ChatGPT 至 GPT-5.6 系列并扩大免费权限](#item-8) ⭐️ 8.0/10
9. [谷歌发布 Gemini 3.6 Flash，透露 Gemini 4 预训练启动](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 与 Cerebras 推出 GPT-5.6 Sol Ultrafast，速度提升 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 9.0/10

OpenAI 与 Cerebras 宣布推出 GPT-5.6 Sol Ultrafast，这是一个新的服务层级，运行速度比标准处理快 14 倍，在 HLE 基准测试中实现了 7 倍加速，且准确率相当。该服务首先在 OpenAI API 中推出。 此次合作可能大幅缩短复杂推理任务的推理时间，支持更多迭代并提高 AI 输出质量。同时，它也凸显了 Cerebras 的晶圆级引擎等专用硬件在 AI 生态系统中的重要性日益增加。 在评估中，Ultrafast 模式下的 GPT-5.6 Sol 在 11 小时 11 分钟内回答了全部 2500 道 HLE 问题，而 Claude Fable 5 需要 78 小时 27 分钟，以几乎 7 倍的速度实现了相当的准确率。在 GDP-Val（一项针对经济价值知识工作的基准测试）上，Ultrafast 实现了 5.6 倍的端到端加速，且质量无下降。

hackernews · pr337h4m · Aug 13, 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: Cerebras Systems 设计晶圆级处理器，如 WSE-3，这是有史以来最大的 AI 半导体，与 GPU 集群相比减少了延迟和互连瓶颈。HLE（人类最后的考试）是一个由 2500 道专家编写的问题组成的基准测试，旨在让当前 AI 系统无法解决，测试前沿推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed | OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>

</ul>
</details>

**社区讨论**: 评论者对此次合作以及更快推理通过迭代提升思维质量的潜力表示兴奋。一些人担心准确率是否真的与标准模型相同，指出 OpenAI 和 Cerebras 都没有明确确认性能完全一致，且未披露定价细节。

**标签**: `#AI`, `#LLM`, `#inference`, `#hardware`, `#OpenAI`

---

<a id="item-2"></a>
## [谷歌发布 Gemini 3.7 Flash，定价具有竞争力](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌推出了新的人工智能模型 Gemini 3.7 Flash，该模型增强了视觉能力，并改进了知识密集型领域的推理能力。该模型目前提供 introductory 定价，该定价将于 2026 年 12 月 31 日翻倍。 Gemini 3.7 Flash 为高容量、基于文本的任务提供了高性价比的选择，可能削弱 Luna 等竞争对手的优势。其强大的视觉性能使其成为寻求经济实惠的多模态 AI 解决方案的开发者的可行选择。 introductory 定价为每 100 万输入 token 1.50 美元，每 100 万输出 token 7.50 美元，2026 年 12 月 31 日后将翻倍。该模型在 GDP.pdf 基准测试中显著优于 3.6 Flash（34.0% 对 22.0%），并且在代理任务上比 3.6 Flash 便宜 35%。

hackernews · thisisauserid · Aug 13, 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: Gemini 3.7 Flash 是谷歌 Flash 系列的一部分，专为低成本、高容量的用例（如摘要和解析）而设计。该模型基于先前版本构建，提供了改进的推理和视觉能力，并与 Luna 和 Terra 等其他高性价比模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/latest-model">What's new in Gemini 3.7 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: 社区成员测试了该模型的视觉能力，指出虽然 Opus 5 在图像到 HTML 任务中仍是最佳，但 Gemini 3.7 在其价格下表现良好。一些人对 introductory 定价表示怀疑，质疑在 3.6 Flash 发布后这么快推出新 Flash 模型的必要性，并将其性能和成本与 Luna 进行了不利比较。

**标签**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#pricing`

---

<a id="item-3"></a>
## [DRAM 意面化：新攻击绕过内存保护](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

Christopher Domas 发布了一项名为“DRAM 意面化”的新技术，该技术利用 DRAM 寻址机制获得不受限制的内存访问权限，可能危及系统安全。该技术已在 AMD Family 16h CPU 上开发和测试，并提到 Zen 3 的内存控制器寄存器基地址不同。 这项研究展示了一种新颖的硬件级攻击，可以绕过内存保护，可能影响广泛的系统。它凸显了现代 DRAM 日益增长的复杂性和攻击面，引起了安全研究人员和游戏机制造商的担忧。 该攻击利用了 DRAM 控制器的转换寄存器，这些寄存器在 AMD Family 16h CPU 上有文档记录且无法锁定。README 指出 Zen 3 的这些寄存器基地址不同，但尚不清楚哪些其他 CPU 系列受影响。

hackernews · matt_d · Aug 13, 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 寻址涉及物理地址与 DRAM bank、行和列之间的复杂映射。现代 DRAM 控制器使用转换寄存器来管理这种映射，但如果这些寄存器未锁定，拥有 ring-0 权限的攻击者可以操纵它们，从而访问通常受保护的内存区域，例如负环区域。该技术让人联想到之前的研究，如 DRAMA，它利用 DRAM 寻址进行跨 CPU 攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spaghettification">Spaghettification - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1511.08756">DRAMA: Exploiting DRAM Addressing for Cross-CPU Attacks</a></li>

</ul>
</details>

**社区讨论**: 社区对这项研究感到兴奋，用户称赞 Christopher Domas 之前的演讲，并热切期待 Black Hat 的展示。一些用户对游戏机安全的影响表示担忧，指出一旦获得 ring-0 权限，一切都会变得开放。其他人则质疑该攻击对更新 CPU 的适用性，因为该攻击是在较旧的 AMD 架构上测试的。

**标签**: `#security`, `#DRAM`, `#hardware`, `#exploit`, `#reverse engineering`

---

<a id="item-4"></a>
## [选择无聊技术：创新代币概念](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley 在 2015 年发表的有影响力的文章《选择无聊技术》主张优先选择成熟、可靠的技术而非新颖技术，并引入了“创新代币”概念来指导工程决策。 这篇文章已成为工程文化的基石，帮助团队做出务实的技术选择并沟通权衡。其相关性在今天依然存在，尤其是在 AI 代理时代，该概念被应用于决定哪些技术应该是“无聊的”，以最大化创新焦点。 “创新代币”概念表明，每家公司拥有的创新代币数量有限，用于采用新技术；明智地使用它们至关重要。文章强调新技术带有风险，只有在潜在回报证明成本合理时才应采纳。

hackernews · tosh · Aug 13, 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49289512)

**背景**: 在软件工程中，不断有采用最新框架和工具的压力。然而，成熟技术通常更可靠、文档更完善、社区更大，从而降低了风险。“创新代币”框架帮助团队在创新需求与经过验证的解决方案的稳定性之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@mstine/how-software-engineers-succeed-by-selecting-tech-that-sucks-the-least-44dd5edac64a">How Software Engineers Succeed by Selecting Tech that Sucks the Least | by Matt Stine | Medium</a></li>
<li><a href="http://technicaldebtbook.com/tag/innovation-tokens/">innovation tokens | Technical Debt</a></li>
<li><a href="https://www.growingscrummasters.com/keywords/innovation-tokens/">Managing Innovation Tokens for Strategic Technical Change : Growing Scrum Masters</a></li>

</ul>
</details>

**社区讨论**: 社区讨论大多积极，许多人称赞“创新代币”概念是进行权衡的有用思维模型。一些人反驳说，“新颖”或“新”是弱代理，工程师应根据需求和风险来评估技术。其他人则指出该概念对 AI 代理的适用性，建议代理应使用无聊技术以最大化创新。

**标签**: `#software engineering`, `#technology strategy`, `#innovation`, `#engineering culture`, `#decision-making`

---

<a id="item-5"></a>
## [DeepSeek 发布开源 AI 代理 Harness 开发者预览版](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 已发布其 AI 代理 harness 的开源开发者预览版，名为 DeepSeek Harness，采用 MIT 许可证。该预览版包含完整的会话可追溯性、热重载和动态插件功能。 此次发布意义重大，因为它为开发者提供了一个透明、可审计的 AI 代理构建框架，而这一特性在专有的美国模型中往往缺失。它可能通过促进开放标准和社区驱动的创新来影响 AI 开发工作流。 该 harness 使用 Cordis v4，支持在不重启进程的情况下热加载和卸载插件，并在卸载时能回滚副作用。正如一位作者所指出的，开发者预览版预计会有粗糙之处和破坏兼容性的更改。

hackernews · bjin · Aug 13, 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**背景**: AI 代理 harness 是围绕大型语言模型的软件基础设施，使其能够作为 AI 代理运行，管理工具使用、记忆、状态持久化和反馈循环。会话可追溯性以追加式日志记录模型看到的所有内容，这对调试和审计至关重要。动态插件功能允许在运行时灵活扩展和修改代理的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调可追溯性功能是一个“杀手级功能”，而美国模型由于加密而不允许这样做。一位作者承认这是一个早期预览版，存在粗糙之处。一些用户将其与字节跳动的 eino 等其他库进行比较，并指出使用了 Cordis v4，该库已在 Koishi 项目中使用。

**标签**: `#AI`, `#DeepSeek`, `#developer tools`, `#open source`, `#agent harness`

---

<a id="item-6"></a>
## [DeepSeek V4 Pro 0813 发布，开放权重](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek 发布了其最新模型 DeepSeek V4 Pro 0813，现可通过 OpenRouter 的 API 使用，并在 Hugging Face 上开放权重。该模型拥有 1.7 万亿参数，文件大小为 893 GB。 此次发布对 AI 社区意义重大，因为它提供了一个高性能的开放权重模型，使研究人员和开发者能够在自己的基础设施上运行和微调。这也加剧了开放权重大语言模型领域的竞争，尤其是来自中国 AI 实验室的竞争。 该模型支持 100 万 token 的上下文窗口和最大 384,000 token 的输出，定价为每百万输入 token 0.435 美元，每百万输出 token 0.87 美元。它提供思考和非思考模式、JSON 输出、工具调用，并兼容 OpenAI 风格和 Anthropic 风格的 API。

rss · Simon Willison · Aug 12, 23:59

**背景**: 开放权重模型是指核心组件公开发布的 AI 模型，任何人都可以下载、检查、修改并在自己的基础设施上运行。DeepSeek 是一家以发布强大开放权重模型而闻名的中国 AI 研究实验室，此次发布是在 DeepSeek V4 Pro 和 V4 Flash 等先前模型之后进行的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/deepseek-v4-pro">DeepSeek V4 Pro 0813 (max) - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#Open Weights`, `#Model Release`

---

<a id="item-7"></a>
## [DeepMind 的 SL2T 将手语 AI 带入 Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 于 2026 年 8 月 12 日发布了大规模多语言手语转文字模型 SL2T。这是首个在消费产品中落地的手语 AI，首次在 Pixel 11 的 Gboard 和 Live Transcribe 中推出，初期支持美国手语（ASL）转英语。 这标志着手语 AI 向公众普及迈出了重要一步，可能改善聋人和听力障碍用户的沟通体验。它为将此类模型集成到主流设备中开创了先例，可能推动无障碍技术的进一步研究和应用。 SL2T 使用了超过 10 万小时、涵盖 50 多种语言的手语数据进行训练。它在 FLEURS-ASL 基准上的零样本得分为 70 BLEURT，远超此前纪录，并且只处理手部和身体姿态关键点，不读取原始视频，以保护隐私。

telegram · zaihuapd · Aug 13, 08:55

**背景**: 由于缺乏大规模数据集和视觉手势的复杂性，手语翻译一直是一项具有挑战性的 AI 任务。FLEURS-ASL 是将 FLORES/FLEURS 扩展到美国手语的基准，BLEURT 是用于评估文本生成质量的神经指标。DeepMind 的方法利用姿态估计来降低隐私风险，同时实现实时翻译。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datanorth.ai/news/google-deepmind-releases-sl2t">Google DeepMind releases SL 2 T sign language AI - DataNorth</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/google-sign-language-model-body-landmarks">Google's new model turns sign language into text for web searches</a></li>
<li><a href="https://www.cryptopolitan.com/google-deepmind-sign-language-on-pixel-11/">Google DeepMind ships SL 2 T sign - language model ... - Cryptopolitan</a></li>

</ul>
</details>

**标签**: `#AI`, `#sign language`, `#DeepMind`, `#accessibility`, `#machine learning`

---

<a id="item-8"></a>
## [OpenAI 升级 ChatGPT 至 GPT-5.6 系列并扩大免费权限](https://t.me/zaihuapd/43176) ⭐️ 8.0/10

OpenAI 宣布推出 GPT-5.6 系列，付费用户（Plus 和 Pro）将获得 GPT-5.6 Sol，提供更可靠的事实答案，并新增滑块控制思考深度。免费用户本周起默认升级至 GPT-5.6 Luna，下周起可享无限文本对话，并新增 Think 按钮以应对复杂推理。 此次更新显著提升了 ChatGPT 对付费和免费用户的能力，可能提高用户满意度并扩大 AI 助手的采用率。免费权限的扩大可能加剧 AI 聊天机器人市场的竞争，并迫使竞争对手提供更慷慨的免费层级。 GPT-5.6 Sol 是最高能力层级，面向困难编码、复杂代理和高风险知识工作，而 Luna 是默认免费模型。Think 按钮专为深度推理任务设计，滑块允许用户控制模型的思考深度。内部评估显示，Luna 在财经、医疗和法律查询中的事实准确性有所提高。

telegram · zaihuapd · Aug 13, 17:04

**背景**: OpenAI 定期更新其 ChatGPT 模型以提升性能和用户体验。GPT-5.6 系列引入了多个层级（Sol、Terra、Luna），以满足不同用户的需求和预算，定价随层级变化。免费层级的升级和新功能旨在让更广泛的用户群体更容易获得先进的 AI 能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emergent.sh/learn/gpt-5-6-sol-vs-terra-vs-luna">GPT - 5 . 6 Sol vs Terra vs Luna : Which Model Should You Use?</a></li>
<li><a href="https://www.u7buy.com/blog/gpt-5-6-model-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : Which Model to Choose?</a></li>
<li><a href="https://nerova.ai/news/openai-gpt-5-6-sol-vs-terra-vs-luna-differences-july-2026">OpenAI GPT - 5 . 6 Sol vs Terra vs Luna : What’s the Difference ?</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI model update`, `#free access`

---

<a id="item-9"></a>
## [谷歌发布 Gemini 3.6 Flash，透露 Gemini 4 预训练启动](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

谷歌发布了 Gemini 3.6 Flash，该模型相比 3.5 Flash 减少了 17%的输出 Token，并提升了代码生成、知识工作和计算机操作能力。同时，公司透露 Gemini 4 已启动预训练。 此次更新表明谷歌持续推动 AI 模型的效率与能力提升，直接影响依赖 Gemini 进行智能体工作流的开发者和企业。Gemini 4 预训练的启动显示了前瞻性的路线图，可能影响 AI 竞争格局。 Gemini 3.6 Flash 的知识截止日期为 2026 年 3 月，API 定价为每百万输入 Token 1.5 美元、输出 Token 7.5 美元。它支持 104.8 万 Token 的上下文窗口，并具备思考模式和函数调用等功能。

telegram · zaihuapd · Aug 13, 17:32

**背景**: Gemini 3.6 Flash 是 Gemini 3.5 Flash 的升级版，定位为面向生产级 AI 智能体和复杂工作流的主力模型。减少输出 Token 和优化推理步骤旨在降低成本、提高效率。谷歌还推出了 Gemini 3.5 Flash-Lite 和专注于网络安全的变体，表明其覆盖多种应用场景的广泛策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.php.cn/faq/2864769.html">Gemini 3 . 6 Flash 来了，但网友笑得更大声：省下了 token ...</a></li>
<li><a href="https://www.zhiding.cn/ai/2026/0722/3194170.shtml">Google Gemini 深夜“三箭齐发”： 输 出 Token 直降17...</a></li>
<li><a href="https://ai-bio.cn/gemini-3-6-flash/">Gemini 3 . 6 Flash – 谷歌 推 出的多模态智能体与代码开发模型 | AI 工 具 箱</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一；X 平台上有用户批评该模型性能，指出其在 Artificial Analysis 上与 3.5 Flash 同分，且落后于 Meta Spark1.1、GLM-5.2 等竞品。也有人强调减少 Token 输出带来的成本节省，但整体情绪偏向怀疑实际改进。

**标签**: `#Google`, `#Gemini`, `#AI模型`, `#发布`, `#预训练`

---