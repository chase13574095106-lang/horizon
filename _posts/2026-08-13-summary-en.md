---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 26 items, 9 important content pieces were selected

---

1. [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast with 7x Speedup](#item-1) ⭐️ 9.0/10
2. [Google Launches Gemini 3.7 Flash with Competitive Pricing](#item-2) ⭐️ 8.0/10
3. [Spaghettifying DRAM: New Attack Bypasses Memory Protections](#item-3) ⭐️ 8.0/10
4. [Choose Boring Technology: The Innovation Tokens Concept](#item-4) ⭐️ 8.0/10
5. [DeepSeek Releases Open-Source AI Agent Harness Developer Preview](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Pro 0813 Released with Open Weights](#item-6) ⭐️ 8.0/10
7. [DeepMind's SL2T Brings Sign Language AI to Pixel 11](#item-7) ⭐️ 8.0/10
8. [OpenAI Upgrades ChatGPT to GPT-5.6 Series, Expands Free Access](#item-8) ⭐️ 8.0/10
9. [Google Launches Gemini 3.6 Flash, Reveals Gemini 4 Pretraining](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast with 7x Speedup](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 9.0/10

OpenAI and Cerebras announced GPT-5.6 Sol Ultrafast, a new service tier that runs up to 14x faster than standard processing, achieving a 7x speedup on HLE benchmarks with comparable accuracy. The service is launching first in the OpenAI API. This collaboration could significantly reduce inference time for complex reasoning tasks, enabling more iterative and higher-quality AI outputs. It also highlights the growing importance of specialized hardware like Cerebras's wafer-scale engines in the AI ecosystem. In evaluations, GPT-5.6 Sol on Ultrafast answered all 2,500 HLE questions in 11 hours and 11 minutes, compared to Claude Fable 5's 78 hours and 27 minutes, achieving comparable accuracy nearly 7x faster. On GDP-Val, a benchmark for economically valuable knowledge work, Ultrafast delivered a 5.6x end-to-end speedup with no quality degradation.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**Background**: Cerebras Systems designs wafer-scale processors, such as the WSE-3, which are the largest AI semiconductors ever built, reducing latency and interconnect bottlenecks compared to GPU clusters. HLE (Humanity's Last Exam) is a benchmark consisting of 2,500 expert-written questions designed to be unsolvable by current AI systems, testing frontier reasoning capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed | OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the collaboration and the potential of faster inference to improve thought quality through iteration. Some raised concerns about whether accuracy is truly identical to the standard model, noting that neither OpenAI nor Cerebras explicitly confirmed 1:1 performance, and pricing details were not disclosed.

**Tags**: `#AI`, `#LLM`, `#inference`, `#hardware`, `#OpenAI`

---

<a id="item-2"></a>
## [Google Launches Gemini 3.7 Flash with Competitive Pricing](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google has introduced Gemini 3.7 Flash, a new AI model with enhanced vision capabilities and improved reasoning for knowledge-dense fields. The model is available with introductory pricing that is set to double on December 31, 2026. Gemini 3.7 Flash offers a cost-effective option for high-volume, text-based tasks, potentially undercutting competitors like Luna. Its strong vision performance makes it a viable choice for developers seeking affordable multimodal AI solutions. The introductory pricing is $1.50 per 1M input tokens and $7.50 per 1M output tokens, doubling after December 31, 2026. The model significantly outperforms 3.6 Flash on the GDP.pdf benchmark (34.0% vs 22.0%) and is 35% cheaper than 3.6 Flash for agentic tasks.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Background**: Gemini 3.7 Flash is part of Google's Flash series, designed for low-cost, high-volume use cases like summarization and parsing. The model builds on previous versions, offering improved reasoning and vision capabilities, and is positioned against other cost-effective models like Luna and Terra.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/latest-model">What's new in Gemini 3.7 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Community members tested the model's vision capabilities, noting that while Opus 5 remains best-in-class for image-to-HTML tasks, Gemini 3.7 performs well for its price. Some expressed skepticism about the introductory pricing, questioning the need for a new Flash model so soon after 3.6 Flash, and compared its performance and cost unfavorably to Luna.

**Tags**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#pricing`

---

<a id="item-3"></a>
## [Spaghettifying DRAM: New Attack Bypasses Memory Protections](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

Christopher Domas has released a new technique called 'Spaghettifying DRAM' that exploits DRAM addressing to gain unrestricted memory access, potentially compromising system security. The technique was developed and tested on AMD Family 16h CPUs, with notes about Zen 3 having a different base address for memory controller registers. This research demonstrates a novel hardware-level attack that can bypass memory protections, potentially affecting a wide range of systems. It highlights the growing complexity and attack surface of modern DRAM, raising concerns for security researchers and console manufacturers alike. The attack exploits the DRAM controller's translation registers, which are documented and cannot be locked on AMD Family 16h CPUs. The README notes that Zen 3 has a different base address for these registers, but it is unclear which other CPU families are affected.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: DRAM addressing involves complex mapping between physical addresses and DRAM banks, rows, and columns. Modern DRAM controllers use translation registers to manage this mapping, but if these registers are left unlocked, an attacker with ring-0 access could manipulate them to gain access to memory regions that are normally protected, such as those in negative ring territory. This technique is reminiscent of previous research like DRAMA, which exploited DRAM addressing for cross-CPU attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spaghettification">Spaghettification - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1511.08756">DRAMA: Exploiting DRAM Addressing for Cross-CPU Attacks</a></li>

</ul>
</details>

**Discussion**: The community is excited about the research, with users praising Christopher Domas's previous talks and eagerly awaiting the Black Hat presentation. Some users express concern about the implications for console security, noting that once ring-0 is achieved, everything becomes open. Others question the applicability to newer CPUs, since the attack was tested on an older AMD architecture.

**Tags**: `#security`, `#DRAM`, `#hardware`, `#exploit`, `#reverse engineering`

---

<a id="item-4"></a>
## [Choose Boring Technology: The Innovation Tokens Concept](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley's influential 2015 essay 'Choose Boring Technology' argues for prioritizing mature, reliable technologies over novel ones, introducing the 'innovation tokens' concept to guide engineering decisions. This essay has become a cornerstone of engineering culture, helping teams make pragmatic technology choices and communicate tradeoffs. Its relevance persists today, especially in the age of AI agents, where the concept is being applied to decide which technologies should be 'boring' to maximize innovation focus. The 'innovation tokens' concept suggests that each company has a limited number of innovation tokens to spend on adopting new technologies; spending them wisely is crucial. The essay emphasizes that new technologies carry risk and should be adopted only when the potential payoff justifies the cost.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**Background**: In software engineering, there is constant pressure to adopt the latest frameworks and tools. However, mature technologies are often more reliable, better documented, and have larger communities, reducing risk. The 'innovation tokens' framework helps teams balance the need for innovation with the stability of proven solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@mstine/how-software-engineers-succeed-by-selecting-tech-that-sucks-the-least-44dd5edac64a">How Software Engineers Succeed by Selecting Tech that Sucks the Least | by Matt Stine | Medium</a></li>
<li><a href="http://technicaldebtbook.com/tag/innovation-tokens/">innovation tokens | Technical Debt</a></li>
<li><a href="https://www.growingscrummasters.com/keywords/innovation-tokens/">Managing Innovation Tokens for Strategic Technical Change : Growing Scrum Masters</a></li>

</ul>
</details>

**Discussion**: The community discussion is largely positive, with many praising the 'innovation tokens' concept as a useful mental model for making tradeoffs. Some push back, arguing that 'novel' or 'new' are weak proxies and that engineers should evaluate technologies based on requirements and risks. Others note the concept's applicability to AI agents, suggesting that agents should work with boring technology to maximize innovation.

**Tags**: `#software engineering`, `#technology strategy`, `#innovation`, `#engineering culture`, `#decision-making`

---

<a id="item-5"></a>
## [DeepSeek Releases Open-Source AI Agent Harness Developer Preview](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek has released an open-source developer preview of its AI agent harness, called DeepSeek Harness, under the MIT license. The preview includes full session traceability, hot-reload, and dynamic plugin capabilities. This release is significant because it provides developers with a transparent and auditable framework for building AI agents, a feature that is often lacking in proprietary US models. It could influence AI development workflows by promoting open standards and community-driven innovation. The harness uses Cordis v4, which enables hot-loading and unloading of plugins without restarting the process, and can revert side effects when unloaded. The developer preview is expected to have rough edges and compatibility-breaking changes, as noted by one of the authors.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**Background**: An AI agent harness is the software infrastructure surrounding a large language model that enables it to operate as an AI agent, managing tool use, memory, state persistence, and feedback loops. Session traceability records everything the model sees in an append-only log, which is crucial for debugging and auditing. Dynamic plugin capabilities allow for flexible extension and modification of the agent's behavior at runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the traceability feature as a 'killer feature' that US models don't allow due to encryption. One author acknowledged it's an early preview with rough edges. Some users compared it to other libraries like bytedance's eino and noted the use of Cordis v4, which has been used in the Koishi project.

**Tags**: `#AI`, `#DeepSeek`, `#developer tools`, `#open source`, `#agent harness`

---

<a id="item-6"></a>
## [DeepSeek V4 Pro 0813 Released with Open Weights](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek has released its latest model, DeepSeek V4 Pro 0813, now available via API on OpenRouter and with open weights on Hugging Face. The model features 1.7 trillion parameters and a 893 GB file size. This release is significant for the AI community as it provides a high-capability open-weight model, enabling researchers and developers to run and fine-tune it on their own infrastructure. It also intensifies competition in the open-weight LLM space, particularly from Chinese AI labs. The model supports a 1M token context window and a maximum output of 384,000 tokens, with pricing at $0.435 per million input tokens and $0.87 per million output tokens. It offers thinking and non-thinking modes, JSON output, tool calls, and compatibility with both OpenAI-style and Anthropic-style APIs.

rss · Simon Willison · Aug 12, 23:59

**Background**: Open-weight models are AI models whose core components are publicly released, allowing anyone to download, inspect, modify, and run them on their own infrastructure. DeepSeek is a Chinese AI research lab known for releasing powerful open-weight models, and this release follows previous models like DeepSeek V4 Pro and V4 Flash.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/deepseek-v4-pro">DeepSeek V4 Pro 0813 (max) - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#Open Weights`, `#Model Release`

---

<a id="item-7"></a>
## [DeepMind's SL2T Brings Sign Language AI to Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

Google DeepMind released SL2T, a massively multilingual sign language-to-text model, on August 12, 2026. It is the first sign language AI to ship in a consumer product, debuting in Gboard and Live Transcribe on Pixel 11, initially supporting American Sign Language (ASL) to English. This marks a significant step in making sign language AI accessible to the general public, potentially improving communication for deaf and hard-of-hearing users. It sets a precedent for integrating such models into mainstream devices, which could drive further research and adoption in accessibility technology. SL2T was trained on over 100,000 hours of sign language data across more than 50 languages. It achieves a zero-shot score of 70 BLEURT on the FLEURS-ASL benchmark, far exceeding previous records, and processes only hand and body pose keypoints to protect privacy, not raw video.

telegram · zaihuapd · Aug 13, 08:55

**Background**: Sign language translation has been a challenging AI task due to the lack of large-scale datasets and the complexity of visual gestures. FLEURS-ASL is a benchmark extending FLORES/FLEURS to American Sign Language, and BLEURT is a neural metric for evaluating text generation quality. DeepMind's approach leverages pose estimation to reduce privacy risks while enabling real-time translation.

<details><summary>References</summary>
<ul>
<li><a href="https://datanorth.ai/news/google-deepmind-releases-sl2t">Google DeepMind releases SL 2 T sign language AI - DataNorth</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/google-sign-language-model-body-landmarks">Google's new model turns sign language into text for web searches</a></li>
<li><a href="https://www.cryptopolitan.com/google-deepmind-sign-language-on-pixel-11/">Google DeepMind ships SL 2 T sign - language model ... - Cryptopolitan</a></li>

</ul>
</details>

**Tags**: `#AI`, `#sign language`, `#DeepMind`, `#accessibility`, `#machine learning`

---

<a id="item-8"></a>
## [OpenAI Upgrades ChatGPT to GPT-5.6 Series, Expands Free Access](https://t.me/zaihuapd/43176) ⭐️ 8.0/10

OpenAI announced the GPT-5.6 series, with paid users (Plus and Pro) getting GPT-5.6 Sol for more reliable factual answers and a slider to control thinking depth. Free users will be upgraded to GPT-5.6 Luna by default this week, with unlimited text chat starting next week and a new Think button for complex reasoning. This update significantly enhances the capabilities of ChatGPT for both paid and free users, potentially improving user satisfaction and broadening the adoption of AI assistants. The expansion of free access could intensify competition in the AI chatbot market and pressure rivals to offer more generous free tiers. GPT-5.6 Sol is the highest-capability tier, aimed at hard coding, complex agents, and high-stakes knowledge work, while Luna is the default free model. The Think button is designed for deep reasoning tasks, and the slider allows users to control the model's thinking depth. Internal evaluations show improved factual accuracy in finance, medical, and legal queries for Luna.

telegram · zaihuapd · Aug 13, 17:04

**Background**: OpenAI regularly updates its ChatGPT models to improve performance and user experience. The GPT-5.6 series introduces multiple tiers (Sol, Terra, Luna) to cater to different user needs and budgets, with pricing scaling accordingly. The free tier upgrade and new features aim to make advanced AI capabilities more accessible to a broader audience.

<details><summary>References</summary>
<ul>
<li><a href="https://emergent.sh/learn/gpt-5-6-sol-vs-terra-vs-luna">GPT - 5 . 6 Sol vs Terra vs Luna : Which Model Should You Use?</a></li>
<li><a href="https://www.u7buy.com/blog/gpt-5-6-model-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : Which Model to Choose?</a></li>
<li><a href="https://nerova.ai/news/openai-gpt-5-6-sol-vs-terra-vs-luna-differences-july-2026">OpenAI GPT - 5 . 6 Sol vs Terra vs Luna : What’s the Difference ?</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI model update`, `#free access`

---

<a id="item-9"></a>
## [Google Launches Gemini 3.6 Flash, Reveals Gemini 4 Pretraining](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

Google has released Gemini 3.6 Flash, a new model that reduces output tokens by 17% compared to 3.5 Flash and improves code generation, knowledge work, and computer use capabilities. The company also announced that pretraining for Gemini 4 has begun. This update signals Google's continued push to improve efficiency and capability in its AI models, directly impacting developers and enterprises that rely on Gemini for agentic workflows. The announcement of Gemini 4 pretraining indicates a forward-looking roadmap that could shape the competitive landscape in AI. Gemini 3.6 Flash has a knowledge cutoff of March 2026 and is priced at $1.5 per million input tokens and $7.5 per million output tokens. It also supports a 1,048,000-token context window and includes features like thinking mode and function calling.

telegram · zaihuapd · Aug 13, 17:32

**Background**: Gemini 3.6 Flash is an upgrade to the Gemini 3.5 Flash model, designed as a workhorse model for production-grade AI agents and complex workflows. The reduction in output tokens and optimized reasoning steps aim to lower costs and improve efficiency for developers. Google also introduced other models like Gemini 3.5 Flash-Lite and a cybersecurity-focused variant, indicating a broader strategy to cover various use cases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.php.cn/faq/2864769.html">Gemini 3 . 6 Flash 来了，但网友笑得更大声：省下了 token ...</a></li>
<li><a href="https://www.zhiding.cn/ai/2026/0722/3194170.shtml">Google Gemini 深夜“三箭齐发”： 输 出 Token 直降17...</a></li>
<li><a href="https://ai-bio.cn/gemini-3-6-flash/">Gemini 3 . 6 Flash – 谷歌 推 出的多模态智能体与代码开发模型 | AI 工 具 箱</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed; some users on X criticized the model's performance, noting it scored the same as 3.5 Flash on Artificial Analysis and lagged behind competitors like Meta Spark1.1 and GLM-5.2. Others highlighted the cost savings from reduced token output, but overall sentiment leans skeptical about the actual improvements.

**Tags**: `#Google`, `#Gemini`, `#AI模型`, `#发布`, `#预训练`

---