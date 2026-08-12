---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 36 items, 14 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B: Massive MoE Model Released with Near-Frontier Performance](#item-1) ⭐️ 9.0/10
2. [Researchers Steal Hidden Reasoning from Proprietary LLM APIs](#item-2) ⭐️ 9.0/10
3. [Former Chinese Premier Zhu Rongji Dies at 98 in Beijing](#item-3) ⭐️ 9.0/10
4. [DeepSeek V4 Pro 0813 Launches, Rivals Opus at Lower Cost](#item-4) ⭐️ 8.0/10
5. [Zed Introduces Delta for Real-Time Collaborative AI Agent Conversations](#item-5) ⭐️ 8.0/10
6. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-6) ⭐️ 8.0/10
7. [xAI Releases Grok 4.6, a New Frontier AI Model](#item-7) ⭐️ 8.0/10
8. [uBlock Origin Stops Filtering Facebook Ads](#item-8) ⭐️ 8.0/10
9. [AI Is Hollowing Out Mid-Level Software Engineering Roles](#item-9) ⭐️ 8.0/10
10. [LLM Mathematical Strengths: Sampling and Counterexamples](#item-10) ⭐️ 8.0/10
11. [Woxi: Open-Source Rust Reimplementation of Wolfram Language](#item-11) ⭐️ 8.0/10
12. [LTX Releases Open-Source Video Model LTX-2.5, Runs on Single RTX 5090](#item-12) ⭐️ 8.0/10
13. [WeChat Releases WeLM: Resource-Efficient LLM Family with MoE](#item-13) ⭐️ 8.0/10
14. [DeepSeek V4-Flash Official API Enters Public Beta](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B: Massive MoE Model Released with Near-Frontier Performance](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released Qwen3.8-2.4T-A95B, a 2.4-trillion-parameter Mixture-of-Experts (MoE) model with 95B active parameters, available in BF16 and FP8 formats. The model is claimed to perform between Opus 4.5 and Fable 5, and the open-weight release marks the first time Qwen has open-sourced a Max-level model. This release significantly advances open-source AI by providing a model with near-frontier performance, potentially rivaling proprietary models like Opus 4.5 and Fable 5. It enables researchers and developers to deploy state-of-the-art capabilities on their own infrastructure, though the massive hardware requirements may limit accessibility. The model uses a fine-grained MoE architecture with 512 routed experts (10 active) plus one shared expert, over a 92-layer hybrid-attention backbone, supporting up to 1M context and 128K output. The BF16 version requires approximately 4.9TB of memory, while FP8 is about 2.4TB; a 1-bit quantized version (397GB) is available via Unsloth, enabling deployment on more modest hardware.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, allowing massive scale with manageable compute. Quantization reduces precision (e.g., FP8) to shrink memory footprint, enabling deployment on consumer hardware. Qwen3.8-2.4T-A95B is the open-weight base for Qwen3.8-Max, which adds features like vision input and 1M context.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72 | NVIDIA Technical Blog</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B">Qwen/Qwen3.8-2.4T-A95B — 2.4T / 95B active · MOE · 256K ctx</a></li>
<li><a href="https://x.com/FireworksAI_HQ/status/2087578149915914727">Fireworks on X: "Qwen3.8-2.4T-A95B is now live on Fireworks with Day-0 support! This 2.4T parameter MoE model is built for autonomous agents, heavy coding, large context windows, and is ideal for coding and agentic performance. Start building today: https://t.co/PJfRDyxtZ8 https://t.co/XkJU4PhokZ" / X</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some praise the model's performance and the availability of quantized versions, while others note the high hardware requirements and lack of vision support in the open-weight version. Comparisons to DeepSeek V4 and Kimi k3 highlight competitive pressure, and there is discussion about the licensing terms and the need for external quantization efforts.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Open Source`, `#Hugging Face`

---

<a id="item-2"></a>
## [Researchers Steal Hidden Reasoning from Proprietary LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

Researchers demonstrated a method to recover hidden chain-of-thought reasoning from proprietary LLM APIs (Anthropic, OpenAI, Google) by replaying encrypted traces into weaker sibling models and jailbreaking them. The attack was acknowledged by providers and subsequently fixed. This reveals a significant security vulnerability in major AI APIs, exposing hidden reasoning that providers intended to keep secret. It highlights the challenges of protecting proprietary model internals and has implications for AI safety, privacy, and competitive advantage. The attack exploited that models in the same family share encryption keys, allowing encrypted reasoning blocks to be replayed into weaker models (e.g., Claude Haiku 4.5) with a simple jailbreak prompt. The paper includes extracted reasoning traces, revealing raw chain-of-thought content not intended for human consumption, and also describes a prompt injection variant for data exfiltration.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought (CoT) reasoning is a technique where LLMs generate intermediate reasoning steps to solve complex problems. To protect proprietary reasoning, providers encrypt these traces and return them to clients as opaque blocks. This research shows that if encryption keys are shared across models, weaker models can be coerced into decrypting and revealing the hidden reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs | alphaXiv</a></li>
<li><a href="https://huggingface.co/papers/2608.09867">Paper page - Stealing Reasoning Traces from Proprietary LLM APIs</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#chain-of-thought`, `#AI privacy`, `#security research`, `#proprietary APIs`

---

<a id="item-3"></a>
## [Former Chinese Premier Zhu Rongji Dies at 98 in Beijing](https://www.news.cn/politics/20260812/4c2c72e299ef4561915d2e507393a81f/c.html) ⭐️ 9.0/10

Zhu Rongji, former Premier of China's State Council, passed away in Beijing on August 12, 2026, at the age of 98. The official announcement was made by the CPC Central Committee, the NPC Standing Committee, the State Council, and the CPPCC National Committee. Zhu Rongji was a pivotal figure in China's economic reforms, leading the country through the Asian Financial Crisis and WTO accession. His death marks the end of an era and prompts reflection on China's economic transformation and global integration. Zhu Rongji was born in October 1928 in Changsha, Hunan, and joined the CPC in October 1949. He served as Premier from March 1998, implementing proactive fiscal and prudent monetary policies, and personally participated in the final WTO negotiations with the US in 1999.

telegram · zaihuapd · Aug 12, 10:11

**Background**: Zhu Rongji was a key architect of China's socialist market economy, overseeing major reforms in fiscal, financial, state-owned enterprise, housing, and grain circulation sectors. His tenure saw China's successful accession to the WTO in 2001, which accelerated its integration into the global economy. The concept of a socialist market economy was established at the 14th CPC Congress in 1992, following Deng Xiaoping's Southern Tour.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/朱镕基">朱镕基 - 维基百科，自由的百科全书</a></li>
<li><a href="https://finance.ifeng.com/news/special/wto10/zrj/">入世十年20人：朱镕基_财经 - 凤凰网</a></li>
<li><a href="https://www.gov.cn/yaowen/liebiao/202608/content_7077937.htm">gov.cn/yaowen/liebiao/202608/content_7077937.htm</a></li>

</ul>
</details>

**Tags**: `#politics`, `#obituary`, `#China`, `#history`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813 Launches, Rivals Opus at Lower Cost](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek released V4 Pro 0813, the general-availability version of its flagship model, on OpenRouter on August 12, 2026. It is priced at $0.435 per million input tokens and $0.87 per million output tokens, with a 1,048,576-token context window and up to 384,000 output tokens. This release offers a highly competitive price-to-performance ratio, with community benchmarks showing it rivals leading models like Opus 4.8 at roughly 20x lower cost. It could significantly disrupt the AI model market by making frontier-level performance more accessible to developers and enterprises. The model is a large-scale mixture-of-experts (MoE) architecture with 1.6 trillion total parameters and 49 billion active parameters. It shows a 15.8% improvement on Terminal Bench compared to the April Preview, and is described as the best price-to-performance model currently available.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI lab known for releasing powerful open-weight models at low prices. OpenRouter is a platform that provides unified API access to hundreds of AI models, allowing developers to compare and use them easily. Mixture-of-experts (MoE) is an architecture where only a subset of parameters is activated per token, enabling large models to run efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves Preview – Unite.AI</a></li>
<li><a href="https://wccftech.com/deepseek-prices-its-new-v4-pro-0813-model-at-0-87-per-1-million-output-tokens-as-the-high-flying-chinese-ai-lab-wows-with-its-soaring-token-consumption/">DeepSeek Prices Its New V4-Pro-0813 Model At $0.87 Per 1 Million Output Tokens, As The Chinese AI Lab Comes Out Second Only To Anthropic On Token Consumption</a></li>

</ul>
</details>

**Discussion**: Community comments include practical tests and benchmark comparisons. One user found the model had issues with a docker-compose generation task, while another reported it cost $0.12 and had a bug compared to Grok 4.6's $1.41 and no bug. Overall sentiment is positive, with many praising its cost-effectiveness, though some note it is weaker than models like Sol or Fable.

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#benchmarks`, `#OpenRouter`

---

<a id="item-5"></a>
## [Zed Introduces Delta for Real-Time Collaborative AI Agent Conversations](https://zed.dev/blog/introducing-delta) ⭐️ 8.0/10

Zed has introduced Delta, a new feature that enables real-time collaborative conversations with AI agents and inline commenting on agent-generated code. This feature is built on DeltaDB, a new version control system that treats conversations and worktrees as shared artifacts. Delta could significantly improve code review and mentoring workflows by allowing teams to collaboratively interact with AI agents in real time and provide inline feedback on generated code. This represents a shift toward conversation-centric development tools, potentially changing how teams review and understand AI-generated changes. Delta is the first client application for DeltaDB, which is designed around replicated abstractions with the conversation at the center rather than the editor. The feature includes real-time multiplayer conversations and conversation-as-document, allowing inline comments within agent conversations.

hackernews · khy · Aug 12, 18:19 · [Discussion](https://news.ycombinator.com/item?id=49276574)

**Background**: Zed is a modern code editor known for its performance and collaborative features. DeltaDB is a new kind of version control system that transforms conversations with AI agents and the worktrees they edit into shared artifacts, enabling new collaborative workflows. This development comes as AI coding agents become more advanced, raising questions about the value of such features.

<details><summary>References</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Introducing Delta — Zed's Blog</a></li>
<li><a href="https://zed.dev/blog/introducing-deltadb">Software Is Made Between Commits — Zed's Blog</a></li>
<li><a href="https://github.com/zed-industries/zed/discussions/25514">How does /delta work? · zed-industries/zed · Discussion #25514</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions. Some users are intrigued by the potential for mentoring junior engineers and understanding AI-generated PRs, while others express skepticism about the value given rapid advances in AI agents. There are also critiques about the readability of AI summaries and the low contrast of the blog post design.

**Tags**: `#AI`, `#code editor`, `#collaboration`, `#Zed`, `#developer tools`

---

<a id="item-6"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale published a detailed postmortem revealing that a 16-year-old SQLite WAL-reset bug caused database corruption and outages. They funded an open-source VFS shim to help isolate the race condition, and the fix was released in SQLite 3.51.3. This highlights the importance of rigorous testing and the value of supporting open-source infrastructure. It also shows how even the most widely used software can harbor subtle bugs that only surface under specific conditions, affecting many users. The bug is a data race in SQLite's WAL checkpointing process, which can occur even with a single writer if multiple connections are involved. Tailscale experienced six months of unstable uptime, and an initial fix had to be rolled back before the final fix in 3.51.3.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a widely used embedded database that supports Write-Ahead Logging (WAL) for improved performance and concurrency. The WAL-reset bug is a race condition in the checkpointing process, which moves entries from the WAL to the main database file. Tailscale uses SQLite for its control plane, and the bug caused corruption and outages.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.theregister.com/databases/2026/08/12/tailscale-says-deeply-buried-16-year-old-sqlite-bug-caused-last-years-outages/5287004">Tailscale says deeply buried 16-year-old SQLite bug caused ...</a></li>
<li><a href="https://antithesis.com/blog/2026/wal-reset-bug/">Breaking the WAL | Antithesis</a></li>

</ul>
</details>

**Discussion**: Commenters praised the post for its clarity and the company's decision to fund open-source tooling. Some discussed the nature of the bug and the challenges of testing, while others appreciated the transparency and the support contract with SQLite.

**Tags**: `#SQLite`, `#Tailscale`, `#database`, `#bug`, `#postmortem`

---

<a id="item-7"></a>
## [xAI Releases Grok 4.6, a New Frontier AI Model](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI has released Grok 4.6, a new frontier AI model, which is now available via the SpaceXAI API and in various tools like Cursor. The model introduces four reasoning effort levels (low, medium, high, xhigh) and a 500k token context window. Grok 4.6 marks xAI's return to the frontier of AI intelligence, scoring 61 on the Artificial Analysis Intelligence Index, on par with GPT-5.6 Sol. Its competitive pricing and strong agentic performance could intensify competition among major AI labs and offer users a cost-effective alternative. Grok 4.6 costs $2.00 per 1M input tokens and $6.00 per 1M output tokens on the API, with higher effort levels providing better performance. It also debuts on the AA-Briefcase benchmark with an Elo of 1577, placing it at Fable 5-tier, behind the Claude Opus 5 family.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is a series of large language models developed by xAI, known for its integration with the X platform and its focus on truth-seeking. Frontier AI models are evaluated on benchmarks like the Artificial Analysis Intelligence Index, which measures capabilities across various tasks. The release of Grok 4.6 follows Grok 4.5 and is part of a rapid iteration cycle in the competitive AI landscape.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.x.ai/developers/grok-4-6">Grok 4 . 6 | SpaceXAI Docs</a></li>
<li><a href="https://cursor.com/docs/models/grok-4-6">Grok 4 . 6 | Cursor Docs</a></li>
<li><a href="https://artificialanalysis.ai/models/grok-4-6">Grok 4 . 6 (high) - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis">Grok 4.6 returns SpaceXAI to the intelligence frontier and ...</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4 . 6 | SpaceXAI</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about the API adding a default system prompt that overrides user instructions, and skepticism about the rapid performance gains across labs, suggesting possible benchmark hacking. Some users praise Grok's competitive pricing and strong performance in security reviews, while others note its polarizing reputation may limit adoption.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#model release`, `#LLM`

---

<a id="item-8"></a>
## [uBlock Origin Stops Filtering Facebook Ads](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 8.0/10

uBlock Origin has announced it will stop attempting to filter ads on Facebook due to the technical difficulty of doing so. This decision comes after an ongoing arms race between the ad blocker and Facebook's anti-ad-blocking measures. This marks a significant shift in the ad-blocking landscape, as Facebook is one of the largest platforms and its ads are notoriously difficult to block. It highlights the escalating arms race between platforms and ad blockers, and may influence how users and developers approach ad-blocking on other major sites. The announcement was made via a Reddit post on the r/uBlockOrigin subreddit, and was covered by Neowin. uBlock Origin's decision is likely due to Facebook's sophisticated anti-ad-blocking techniques that make filtering ineffective and resource-intensive.

hackernews · Markoff · Aug 12, 11:28 · [Discussion](https://news.ycombinator.com/item?id=49270726)

**Background**: uBlock Origin is a popular open-source browser extension for content filtering, including ad blocking. Facebook has long employed various methods to circumvent ad blockers, such as disguising ads as regular content and using dynamic code obfuscation, making it increasingly difficult for blockers to keep up.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/facebooks-ad-blocker-arm-race-escalates-hack-100-million-john-c-abell">Facebook 's ad - blocker arm race escalates; A hack for 100 million...</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed reactions. Some users support the decision, acknowledging the difficulty and suggesting that users should reconsider their Facebook usage. Others speculate about future solutions, such as computer vision-based ad blocking, while some question the effectiveness of ad-blocking on Facebook given that users with blockers are unlikely to click ads anyway.

**Tags**: `#ad-blocking`, `#Facebook`, `#uBlock Origin`, `#privacy`, `#arms race`

---

<a id="item-9"></a>
## [AI Is Hollowing Out Mid-Level Software Engineering Roles](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

A blog post argues that AI is disproportionately eliminating mid-level software engineering roles while amplifying the output of both poor and excellent engineers. The discussion highlights concerns about junior engineers losing mentorship opportunities as AI tools become more prevalent. This trend could reshape the software engineering career ladder, making it harder for junior engineers to advance and potentially leading to a 'hollowed-out' workforce. It affects hiring strategies, career development, and the overall quality of software engineering as AI tools become standard. The article notes that 'bad' engineers can now amplify their poor output tenfold across an organization, while juniors may delegate challenging tasks to AI and miss learning opportunities. The discussion also mentions the 'automation of the Stack Overflow engineer,' where seniors no longer need to hand off coding tasks to juniors.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**Background**: Software engineering has traditionally had a career ladder where juniors learn from seniors through mentorship and hands-on coding tasks. AI coding assistants and autonomous agents are now automating many routine coding tasks, which historically were the entry-level work that helped juniors build skills. This shift is pressuring the traditional career progression, as companies may reduce mid-level roles and rely more on AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/anand-butani_ai-has-flattened-the-software-engineering-activity-7427765977905577984-3dzQ">AI Has Flattened the Software Engineering Ladder — And We Are...</a></li>
<li><a href="https://www.linkedin.com/pulse/metas-ai-coding-ambitions-end-mid-level-engineers-o-connor-mis-58b3c">Meta’s AI Coding Ambitions: The End of Mid-Level Engineers?</a></li>
<li><a href="https://medium.com/@sahin.samia/the-middle-class-engineer-is-dying-how-ai-is-reshaping-software-engineering-careers-9e126a955564">The Middle-Class Engineer is Dying: How AI is ... - Medium</a></li>

</ul>
</details>

**Discussion**: The community discussion reflects a mix of agreement and concern. Some agree that AI amplifies both good and bad engineering, while others worry that juniors will miss out on mentorship and struggle to advance. There is also a viewpoint that AI automates the 'Stack Overflow engineer' role, reducing the need for mid-level coders.

**Tags**: `#AI`, `#software engineering`, `#career impact`, `#future of work`, `#productivity`

---

<a id="item-10"></a>
## [LLM Mathematical Strengths: Sampling and Counterexamples](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

The post analyzes the types of mathematics LLMs excel at, highlighting their strengths in sampling-based problem solving and counterexample search, while noting that novel, beautiful proofs would indicate human-level reasoning. This analysis provides a nuanced view of LLM capabilities in mathematics, which is crucial for guiding research directions in AI-assisted theorem proving and problem solving. It also sparks discussion on test-time scaling and the nature of AI reasoning. The post references Google's AlphaCode, which generated millions of candidate programs and filtered them down to beat the average human programmer in 2022, illustrating the power of sampling. It also suggests that a sign of human-level reasoning would be proving theorems with new, surprising, yet beautiful methods that are difficult to stumble upon by accident.

hackernews · ColinWright · Aug 12, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49270022)

**Background**: Large language models (LLMs) are increasingly used for mathematical reasoning, with benchmarks like MATH evaluating their performance on competition problems. Test-time scaling, which includes sampling multiple solutions and filtering, has been a key technique for improving LLM performance on complex tasks. Counterexample search is a natural application for LLMs, as they can generate and evaluate many candidates to find disproofs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sri.inf.ethz.ch/research/mathllm">LLMs for Mathematical Reasoning | SRI Lab</a></li>
<li><a href="https://arxiv.org/html/2506.00309v1">Evaluation of LLMs for mathematical problem solving - arXiv.org</a></li>
<li><a href="https://llmdb.com/benchmarks/math">MATH - LLM Benchmark</a></li>

</ul>
</details>

**Discussion**: The comments highlight that the post is essentially about test-time scaling, with sampling being a key strength of AI. Some commenters agree that novel and beautiful proofs would indicate human-level reasoning, while others note AI's affinity for counterexamples and the sociological aspect of focusing on prominent problems. There is also curiosity about AI's performance on temporal logic given its difficulties with concurrent code.

**Tags**: `#LLM`, `#mathematics`, `#AI research`, `#test-time scaling`, `#theorem proving`

---

<a id="item-11"></a>
## [Woxi: Open-Source Rust Reimplementation of Wolfram Language](https://woxi.ad-si.com/) ⭐️ 8.0/10

Woxi, an open-source interpreter for the Wolfram Language written in Rust, has been released with a GUI (Woxi Studio), CLI, Jupyter kernel, and WASM support. It offers fast startup and is free compared to Mathematica. This project provides a free, open-source alternative to the proprietary Wolfram Language, potentially lowering barriers for students, researchers, and developers. Its embeddability via WASM and Rust performance could expand the language's use in web and embedded contexts. Woxi is validated by ~26,000 unit tests and ~900 .wls script snapshot tests. It currently focuses on fixing edge cases and improving performance, with a detailed comparison to Mathematica available on its documentation site.

hackernews · adius · Aug 12, 10:06 · [Discussion](https://news.ycombinator.com/item?id=49270040)

**Background**: The Wolfram Language is the programming language used in Mathematica, a proprietary computational software. Woxi aims to reimplement this language in Rust, offering a free and open-source alternative that can run in various environments, including browsers via WASM.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/WolframResearch/WolframLanguageForJupyter">Wolfram Language kernel for Jupyter notebooks - GitHub</a></li>
<li><a href="https://github.com/cabralski/awesome-wolfram-language">GitHub - cabralski/awesome- wolfram - language : A curated list of...</a></li>
<li><a href="https://github.com/wasmi-labs/wasmi">GitHub - wasmi-labs/wasmi: Efficient and versatile ...</a></li>

</ul>
</details>

**Discussion**: Community members expressed interest in features like approximation methods and a control systems module, while noting the lack of out-of-order execution and the % variable. Some users shared positive experiences with Woxi's visualization capabilities, and one pointed out a previous posting of the project.

**Tags**: `#Wolfram Language`, `#Rust`, `#Open Source`, `#Interpreter`, `#Mathematica`

---

<a id="item-12"></a>
## [LTX Releases Open-Source Video Model LTX-2.5, Runs on Single RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX has released LTX-2.5, an open-source video generation foundation model with fully open weights, training code, and inference pipeline. It can run locally on a single RTX 5090 GPU and supports both text-to-video and image-to-video generation. This release significantly lowers the barrier for high-quality video generation, enabling individual developers and small studios to run state-of-the-art models locally without cloud dependencies. It also sets a new benchmark for open-source video models, as LTX-2.5 Pro ranked first among ten models in a 98-prompt text-to-video artifact evaluation. LTX-2.5 introduces a new diffusion video decoder and uses the Gemma 4 12B text encoder. It also improves multi-shot scene coherence and prompt adherence, and can generate multi-shot scenes in a single pass. Commercial use is free for companies with annual revenue under $10 million.

telegram · zaihuapd · Aug 12, 02:15

**Background**: LTX Video was originally released by Lightricks in November 2024 as a 2-billion-parameter open text-to-video model, followed by a 13-billion-parameter version in May 2025. LTX-2 arrived in October 2025 as the first DiT-based model. The new diffusion decoder is itself a small diffusion model that denoises pixels conditioned on latents, unlike traditional convolutional decoders. Gemma 4 12B is a 12-billion-parameter multimodal model from Google that processes text, images, and audio natively without separate encoders.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX's Latest AI Open-Source Foundation Model | LTX</a></li>
<li><a href="https://www.dreampixelforge.com/blog/ltx-2-5">LTX 2 . 5 : Open Weights, Specs, and How to Run It | Dream Pixel Forge</a></li>
<li><a href="https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/ltx2/pipeline_ltx2_diffusion_decode.py">diffusers/src/diffusers/pipelines/ltx2/pipeline_ltx2_ diffusion _ decode .py...</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#open source`, `#AI model`, `#LTX`

---

<a id="item-13"></a>
## [WeChat Releases WeLM: Resource-Efficient LLM Family with MoE](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 8.0/10

WeChat's team has released WeLM, a family of large language models focused on resource efficiency. The WeLM-80B (3B activated) is already deployed in WeChat's AI assistant 'Xiao Wei', while the in-development WeLM-617B (23B activated) uses a Mixture-of-Experts (MoE) architecture. This release highlights a growing trend toward sparse MoE models that balance performance with computational cost, making advanced AI more accessible. WeLM's integration into WeChat's ecosystem could bring capable AI assistance to hundreds of millions of users, and its future applications in complex tasks like mini-program development may reshape how users interact with WeChat services. WeLM-80B activates only 3B parameters per token, achieving efficiency comparable to other sparse MoE models like Qwen3-Next-80B-A3B. The larger WeLM-617B activates 23B parameters and is designed for enhanced reasoning and understanding, targeting complex tasks such as intelligent mini-program development and tool generation for 'WeChat Xiao Wei'.

telegram · zaihuapd · Aug 12, 13:58

**Background**: Large language models (LLMs) typically require massive computational resources, limiting their deployment. Mixture-of-Experts (MoE) architecture addresses this by activating only a subset of parameters per token, reducing inference cost while maintaining high capacity. WeLM follows this approach, with WeLM-80B already in production and WeLM-617B under development, reflecting a broader industry shift toward resource-efficient AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://stg-www.weex.tech/news/detail/wechat-launches-welm-large-model-series-to-drive-ai-application-implementation-irubxpo341gosi4gj8cazta0">WeChat Launches WeLM Large Model Series to Drive AI ...</a></li>
<li><a href="https://welm.weixin.qq.com/en/posts/building-effective-sparse-moe-models-with-moderate-resources/">Building Effective Sparse MoE Models with Moderate Resources</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#WeChat`, `#AI`, `#resource efficiency`

---

<a id="item-14"></a>
## [DeepSeek V4-Flash Official API Enters Public Beta](https://t.me/zaihuapd/43149) ⭐️ 8.0/10

On July 31, 2026, DeepSeek launched the public beta of its V4-Flash official API, featuring significantly enhanced agent capabilities and benchmark scores that far exceed V4-Pro-Preview. The model natively supports the Responses API format and is specifically adapted for Codex. This release marks a major step forward for DeepSeek's model lineup, with strong agentic performance that could challenge other frontier models in the AI/ML community. The enhanced agent capabilities and high benchmark scores may attract developers and enterprises looking for powerful, cost-effective AI solutions. V4-Flash achieves impressive scores on agentic benchmarks: Terminal Bench 2.1 at 82.7, Cybergym at 76.7, DSBench-FullStack at 68.7, and DSBench-Hard at 59.6. The model structure and size details are not fully disclosed in the announcement.

telegram · zaihuapd · Aug 12, 15:30

**Background**: DeepSeek is a Chinese AI company known for developing open-weight large language models. The V4-Flash is part of its V4 series, succeeding the V4-Pro-Preview. Benchmarks like Terminal Bench 2.1, Cybergym, and DSBench evaluate AI agents on tasks such as terminal use, cybersecurity, and data science, respectively, and are commonly used to gauge agentic capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://benchlm.ai/">LLM Leaderboard & AI Model Benchmarks — August... | BenchLM.ai</a></li>
<li><a href="https://www.vellum.ai/llm-leaderboard">LLM Leaderboard 2026</a></li>
<li><a href="https://llm-stats.com/benchmarks/cybergym">CyberGym Leaderboard | LLM Stats</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#API`, `#AI model`, `#benchmarks`, `#agent`

---