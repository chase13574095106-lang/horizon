---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> From 23 items, 6 important content pieces were selected

---

1. [DeepSeek-V4 发布：1.6 万亿参数，混合注意力架构](#item-1) ⭐️ 9.0/10
2. [Anthropic 公开 Claude 系统提示，提升透明度](#item-2) ⭐️ 8.0/10
3. [AI 模型故意“变笨”：转向外部工具与知识检索](#item-3) ⭐️ 8.0/10
4. [Cloudflare 在切换域名服务器时静默注入分析脚本](#item-4) ⭐️ 8.0/10
5. [Qwen 3.8 27B：强大的开源模型，但默认过度思考](#item-5) ⭐️ 8.0/10
6. [Anthropic 第二季营收暴涨 14 倍超 115 亿美元，筹备 IPO](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek-V4 发布：1.6 万亿参数，混合注意力架构](https://t.me/zaihuapd/43224) ⭐️ 9.0/10

DeepSeek-V4 于 2026 年 4 月 24 日发布预览版，采用混合注意力架构（HAA），提供两个变体，总参数达 1.6 万亿。 此次发布重申了 DeepSeek 在大语言模型发展前沿的地位，提供了具有竞争力的开放权重替代方案，其价格远低于 Claude 等专有模型。这可能加速 AI 的采用并改变市场格局。 该模型采用混合专家（MoE）架构，总参数 1 万亿，激活参数 320 亿，并引入了 Engram 记忆和动态稀疏注意力等创新。模型开放权重，API 使用价格比 Claude 便宜 50 倍。

telegram · zaihuapd · Aug 16, 16:04

**背景**: DeepSeek 是一家中国 AI 公司，以开发开源大语言模型而闻名。其先前发布的模型，如 DeepSeek-V3.1 和 R1，因其性能和成本效益而获得国际关注，挑战了西方 AI 的主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://spoonai.me/posts/2026-03-19-deepseek-v4-open-weight-en">DeepSeek V 4 — 1 Trillion Parameters, Open-Weight, and... | spoonai</a></li>
<li><a href="https://faq.com.tw/en/ai-ml/2026-04-25-deepseek-v4-flagship-model-release-en/">DeepSeek V 4 Arrives: 1.6 Trillion Parameters, $0.28 Output Tokens...</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#model release`, `#machine learning`

---

<a id="item-2"></a>
## [Anthropic 公开 Claude 系统提示，提升透明度](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 已在其平台文档中正式发布了 Claude 模型的系统提示，揭示了塑造模型行为的分层指令。此次发布包括 Opus 4.8 和 Opus 5 等模型的详细提示，社区成员如 Simon Willison 还创建了 git 历史分析以追踪变化。 此举显著提升了 AI 开发的透明度，使研究人员和用户能够理解和审视指导 Claude 行为的隐藏指令。它为其他 AI 公司树立了先例，可能引发关于 AI 安全、伦理和对齐的更深入讨论。 系统提示包含具体指令，例如在危机情况下优先考虑用户福祉，以及验证图像是否存在而非仅凭提示假设。Simon Willison 的 git 仓库追踪了版本间的变化，突出了诸如“Claude Fable 5”和“Claude Mythos 5”等新增内容。

hackernews · tosh · Aug 16, 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示是在用户输入之前给语言模型的初始指令，塑造其默认行为、个性和安全规则。它们是提示工程和上下文工程的关键部分，涉及设计提示以有效引导 LLM 输出。Anthropic 公开这些提示是 AI 行业中罕见的透明度举措，因为此类细节通常保密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cache.directory/prompts/">system prompts — cache.directory</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/ system _ prompts _leaks: Extracted system prompts ...</a></li>
<li><a href="https://www.promptingguide.ai/">Prompt Engineering Guide | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，Simon Willison 提供了 git 历史以方便追踪变化。一些用户对 AI 审核和系统提示设计的影响表示担忧，而另一些用户则质疑某些指令的有效性，例如验证图像存在，认为这反映了模型智能的局限性。

**标签**: `#AI`, `#Anthropic`, `#system prompts`, `#LLM`, `#transparency`

---

<a id="item-3"></a>
## [AI 模型故意“变笨”：转向外部工具与知识检索](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

文章指出，AI 模型正有意减少参数化知识，转而依赖外部工具和检索增强生成（RAG），这一趋势可能重塑模型设计与评估方式，从参数化知识转向可插拔、基于工具的架构。 这种范式转变可能减少幻觉并提高适应性，因为模型不再需要存储快速过时的事实。同时，它挑战了当前注重事实回忆的评估基准，可能催生更强调工具使用和推理而非记忆的新指标。 文章引用 SimpleQA 基准，Gemini 2.5 Pro 仅得 53%，凸显参数化知识的局限。还提到模型卡可能不再列出知识截止日期，因为权重变得不那么时效敏感。社区评论提及 Cactus 的 Needle，一个 14 MB 的工具调用 LLM，作为这一趋势的例子。

hackernews · hruvhwe · Aug 16, 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 大型语言模型传统上在训练时将知识存储在权重中，这随时间推移会过时。检索增强生成（RAG）是一种技术，允许模型在推理时获取外部信息，减少对记忆事实的依赖。这一转变与混合 AI 系统的更广泛趋势一致，即结合本地处理与外部工具和知识库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://www.promptingguide.ai/techniques/rag">Retrieval Augmented Generation ( RAG ) | Prompt Engineering...</a></li>
<li><a href="https://progressive-os.com/ai/">AI & Knowledge Systems Engineering — Private and... | Progressive OS</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一。一些人如 kennywinker 设想可插拔知识库以实现模块化专业知识。另一些人如 COAGULOPATH 批评文章数据过时，指出 SimpleQA 未更新且 Gemini 2.5 Pro 已发布 16 个月。hypfer 警告讨论像科幻小说，而 pulkitsh1234 质疑推理与事实是否真能分离。

**标签**: `#AI`, `#LLM`, `#model design`, `#knowledge retrieval`, `#tool use`

---

<a id="item-4"></a>
## [Cloudflare 在切换域名服务器时静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 8.0/10

一位用户报告称，为了通过自己的子域名提供 R2 存储桶服务而将域名服务器切换到 Cloudflare 后，其纯 HTML、无 JavaScript 的网站被静默注入了 JavaScript 分析代码片段。用户需要通过 Analytics 仪表盘手动选择退出，认为这种做法具有侵入性。 这凸显了隐私和透明度问题：Cloudflare 在未经明确同意的情况下注入第三方脚本，影响了可能不知情的网站所有者。这可能削弱用户对 Cloudflare 服务的信任，并促使他们寻找替代方案或实施更严格的安全措施（如 CSP）。 注入的脚本来自 static.cloudflareinsights.com/beacon.min.js，带有完整性哈希和 data-cf-beacon 属性。用户可以通过 Analytics 仪表盘禁用它，但退出选项并不明显。一位社区成员建议使用 Content-Security-Policy meta 标签来阻止此类脚本。

hackernews · stagas · Aug 16, 17:49

**背景**: Cloudflare 提供 Web Analytics 作为传统分析的隐私友好替代方案，但默认情况下会在页面中注入 JavaScript 信标。当用户将域名服务器切换到 Cloudflare 时，某些功能（如 R2 存储桶服务）可能会自动启用 Web Analytics，导致意外脚本注入。内容安全策略（CSP）是一种安全标准，允许网站所有者控制哪些脚本可以执行，从而提供阻止此类注入的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://community.cloudflare.com/t/how-to-disable-the-web-analytics-from-my-domains/286189">How to disable the Web Analytics from my domains - Analytics - Cloudflare Community</a></li>
<li><a href="https://community.cloudflare.com/t/how-to-disable-cloudflare-analytics-tracking/26307">How to Disable CloudFlare analytics tracking - Analytics - Cloudflare Community</a></li>
<li><a href="https://www.ianjmacintosh.com/articles/disabling-cloudflare-web-analytics/">Disabling Cloudflare Web Analytics | Ian J MacIntosh.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论证实了该问题，并提供了技术解决方案，例如使用 CSP meta 标签限制脚本来源。一些用户质疑如果 Cloudflare 不代理流量，它如何注入脚本；另一些用户则担心这可能违反《计算机欺诈和滥用法》的法律后果。

**标签**: `#Cloudflare`, `#privacy`, `#analytics`, `#DNS`, `#security`

---

<a id="item-5"></a>
## [Qwen 3.8 27B：强大的开源模型，但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 实验室发布了 Apache 2 许可的 27B 参数视觉能力 LLM——Qwen 3.8 27B，其基准测试优于前代甚至更大的闭源模型。然而，它默认使用“xhigh”推理强度，导致过度使用 token 和生成时间过长。 此次发布意义重大，因为它提供了一个可在消费级硬件上运行的强大开源权重模型，可能使高质量 AI 的获取更加民主化。过度思考问题凸显了推理强度设置对实际部署的重要性，影响用户体验和成本。 该模型原生上下文为 262,144 个 token，可通过 RoPE 缩放扩展至 100 万。Simon Willison 在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上测试了 LM Studio 的 17GB Q4_K_M 量化版本，发现增加上下文长度可缓解过度思考问题。

rss · Simon Willison · Aug 16, 22:00

**背景**: Qwen 是阿里云开发的大型语言模型系列，以发布开源和闭源权重模型而闻名。Apache 2.0 是一种宽松的开源许可证，允许商业使用，使 Qwen 3.8 27B 对开发者具有吸引力。具备视觉能力的 LLM 可以处理图像输入，将其应用范围扩展到纯文本任务之外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lmstudio.ai/models/qwen3.8">Qwen 3 . 8</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://github.com/eugeneyan/open-llms">GitHub - eugeneyan/open-llms: 📋 A list of open LLMs available for commercial use.</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Qwen`, `#open-source`, `#AI`, `#benchmarks`

---

<a id="item-6"></a>
## [Anthropic 第二季营收暴涨 14 倍超 115 亿美元，筹备 IPO](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic 第二季初步营收超过 115 亿美元，同比增长逾 14 倍（去年同期为 7.87 亿美元），当季调整后营业利润转正。公司正筹备可能在今秋启动的 IPO。 这一营收激增表明 Anthropic 在竞争激烈的 AI 市场中具有强劲的商业吸引力，可能重塑行业格局。IPO 筹备标志着投资者信心增强，并可能为 AI 进一步发展提供大量资金。 这些数字为初步数据，仍可能调整。第二季营收与 2026 年第一季的 47.3 亿美元相比，显示出快速的环比增长。据报道，公司正筹备可能在今秋启动的大型 IPO。

telegram · zaihuapd · Aug 16, 07:26

**背景**: Anthropic 是一家以开发 Claude 系列大语言模型而闻名的 AI 安全与研究公司。在快速增长的生成式 AI 市场中，该公司与 OpenAI 和 Google 等 AI 领导者竞争。营收增长和盈利能力是衡量 AI 初创公司商业可行性的关键指标。

**标签**: `#Anthropic`, `#AI business`, `#revenue`, `#IPO`, `#industry news`

---