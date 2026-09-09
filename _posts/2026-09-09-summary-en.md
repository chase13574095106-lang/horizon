---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 36 items, 9 important content pieces were selected

---

1. [OpenAI Claims Navier-Stokes Solution, Sparks Priority Dispute](#item-1) ⭐️ 9.0/10
2. [OpenAI Unveils GPT-6 Astra, Tops Benchmarks with Math Breakthrough](#item-2) ⭐️ 9.0/10
3. [vLLM v0.29.0: Model Runner V2 Default, New Models, Performance Gains](#item-3) ⭐️ 8.0/10
4. [Apple Unveils Foldable iPhone Duo](#item-4) ⭐️ 8.0/10
5. [Shopify acquires Tailwind CSS framework](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 May Mimic GPT-5.5 Pro Reasoning Traces](#item-6) ⭐️ 8.0/10
7. [Researcher Details Google Ads Malware Abuse, Sparks Debate](#item-7) ⭐️ 8.0/10
8. [Terence Tao Warns AI Could Deplete Open Math Problems](#item-8) ⭐️ 8.0/10
9. [DeepSeek V4.1 Flash Beta: Native Multimodal, Faster and Cheaper](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Claims Navier-Stokes Solution, Sparks Priority Dispute](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

On September 8, 2026, OpenAI announced that an unreleased internal model, using a swarm of about 10,000 AI agents, produced a resolution to the Navier-Stokes existence and smoothness problem, one of the Millennium Prize Problems. The result, formalized in Lean, has not yet been verified by external mathematicians. If verified, this would be a paradigm-shifting achievement in mathematics and AI, demonstrating AI's capability to solve one of the hardest open problems. It also raises serious concerns about research ethics, priority disputes, and the competitive dynamics between AI companies. OpenAI stated that the agents sent 4.9 million messages and used about 300 billion output tokens across all attempted problems, with 2.7 million messages and 130 billion tokens for Navier-Stokes alone. The method built upon a 2023 approach by Diego Córdoba and Luis Martínez-Zoroa for blowup phenomena in fluid equations. OpenAI said it would decline the $1 million Clay Millennium Prize if offered.

rss · Simon Willison · Sep 8, 23:55

**Background**: The Navier-Stokes existence and smoothness problem asks whether solutions to the Navier-Stokes equations, which describe fluid motion, always remain smooth in three dimensions. It is one of seven Millennium Prize Problems established by the Clay Mathematics Institute in 2000, each with a $1 million prize. As of 2026, only the Poincaré conjecture has been officially solved. The announcement is accompanied by a priority dispute with Tristan Buckmaster and Levent Alpöge, who claim to have derived closely related results earlier.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided in the news item, but based on the controversy, sentiment is likely divided, with concerns about OpenAI's alleged use of leaked information and the ethics of AI-driven research. Some may question the validity of the unverified result, while others may see it as a milestone for AI.

**Tags**: `#AI`, `#mathematics`, `#OpenAI`, `#Navier-Stokes`, `#Millennium Prize`

---

<a id="item-2"></a>
## [OpenAI Unveils GPT-6 Astra, Tops Benchmarks with Math Breakthrough](https://t.me/zaihuapd/43707) ⭐️ 9.0/10

OpenAI has released GPT-6 Astra, claiming it is their most intelligent and aligned model to date. It achieved top scores on multiple benchmarks, including 98% on FrontierMath Tier 4, 99.9% on ARC-AGI-3, and 100% on ExploitBench, and helped improve the upper bound on prime gaps to 186. This release marks a significant leap in AI capabilities, particularly in mathematical reasoning and agentic tasks, which could accelerate research and applications in fields like cybersecurity and scientific discovery. The high benchmark scores suggest GPT-6 Astra may set a new standard for AI performance, influencing the competitive landscape among AI developers. GPT-6 Astra is priced at $10 per million input tokens and $50 per million output tokens under OpenAI's standard API, with additional charges for cache reads and writes. The API offers a fast mode for GPT-6 Astra, with processing speeds up to 2.5 times the standard mode. OpenAI also disclosed a notable decrease in chain-of-thought (CoT) monitorability, as the model can control its reasoning process and complete complex tasks with less or no verbalized reasoning.

telegram · zaihuapd · Sep 9, 07:10

**Background**: FrontierMath is a benchmark of exceptionally challenging mathematics problems crafted by expert mathematicians, with Tier 4 being the hardest, close to research-level problems. ARC-AGI-3 is an interactive reasoning benchmark that tests AI agents' ability to explore novel environments and infer goals, while ExploitBench measures AI's capability in real-world exploitation tasks, from reaching vulnerable code to arbitrary code execution. These benchmarks are designed to push AI beyond simple pattern recognition and into more complex, agentic reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://epoch.ai/benchmarks/frontiermath-tier-4-v2">FrontierMath Tier 4 (v2) | Epoch AI</a></li>
<li><a href="https://arcprize.org/blog/astra">OpenAI's GPT-6 Astra on ARC-AGI-3 | ARC Prize</a></li>
<li><a href="https://exploitbench.ai/">ExploitBench</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed reactions: some users express amazement at GPT-6 Astra's capabilities, such as the MSPAINT computer use demo, while others report performance inconsistencies, noting that Astra felt 'insane' until a recent update made it seem like Sol. There is also discussion about the implications of hidden reasoning in transformer models and concerns about the decrease in chain-of-thought monitorability, with some users linking to relevant research on computational limits and CoT requirements.

**Tags**: `#OpenAI`, `#GPT-6`, `#AI model release`, `#benchmarks`, `#mathematics`

---

<a id="item-3"></a>
## [vLLM v0.29.0: Model Runner V2 Default, New Models, Performance Gains](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 is a major release with 594 commits from 277 contributors, making Model Runner V2 the default for all models and adding support for new models like Hy4-preview, Qwen3.8-Flash-Next, and Kimi K3. It also introduces significant performance optimizations for Kimi-K3 and DeepSeek V4, along with new features for speculative decoding and RL weight sync. This release solidifies vLLM's position as a leading open-source LLM inference engine by adopting a more efficient default execution path and supporting the latest state-of-the-art models. The performance optimizations for models like DeepSeek V4 and Kimi K3 will directly benefit developers deploying these models in production, reducing latency and cost. Model Runner V2 (MRV2) is now default for all models, completing a rollout that began with pooling models, and includes CUDA graph memory profiling for KV cache auto-sizing and batch-sharded sampling. Breaking changes include removal of ten deprecated model architectures and deprecation of `python -m vllm.entrypoints.openai.api_server` in favor of `vllm serve`.

github · khluu · Sep 9, 08:54

**Background**: vLLM is a high-throughput, memory-efficient inference and serving engine for large language models (LLMs). Model Runner V2 is an internal execution framework that improves performance and flexibility compared to its predecessor. The release also supports advanced features like Multi-Token Prediction (MTP) and DeepSeek Sparse Attention (DSA), which are techniques to speed up inference and handle long contexts efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://arxiv.org/abs/2512.02556">DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#AI/ML`, `#open source`

---

<a id="item-4"></a>
## [Apple Unveils Foldable iPhone Duo](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

Apple has announced the iPhone Duo, a foldable iPhone, marking the company's entry into the foldable smartphone market. The announcement has generated significant community discussion, with 794 points and 1555 comments on the news platform. This is Apple's first foldable iPhone, a major product release that could reshape consumer expectations for foldable devices. The community's critical analysis of design and presentation indicates substantial interest and debate, potentially influencing future Apple product decisions. The iPhone Duo is described as wider than previous iPhones even before unfolding, and community members note the absence of a crease based on hands-on videos. The presentation style, led by John Ternus, has been criticized for being rehearsed and emotionally flat.

hackernews · thecosmicfrog · Sep 9, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49630931)

**Background**: Foldable smartphones use flexible displays to allow devices to fold, offering larger screens in a compact form. Apple's entry into this market follows competitors like Samsung, which have offered foldable devices for years. The iPhone Duo's design aims to provide a tablet-like experience that can fold to fit in a pocket.

**Discussion**: Community comments show mixed reactions: some praise the Duo's design and lack of crease, while others criticize the presentation style and the trend toward larger phones. One commenter notes the ISO 216 paper standard as a design inspiration, and another expresses a desire for smaller phones, highlighting a divide in consumer preferences.

**Tags**: `#Apple`, `#iPhone`, `#foldable`, `#consumer tech`, `#product launch`

---

<a id="item-5"></a>
## [Shopify acquires Tailwind CSS framework](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify has acquired Tailwind, the popular open-source CSS framework, as announced on the Tailwind blog. The acquisition comes amid a significant decline in template sales attributed to AI's impact on the business. This acquisition highlights the growing influence of AI on traditional web development business models, as even major open-source tools face revenue challenges. It also signals Shopify's interest in strengthening its developer ecosystem and design tooling. Tailwind Labs, the company behind Tailwind CSS, had previously reported a 40% drop in documentation traffic and a 75% reduction in engineering staff due to AI's impact on template sales. The acquisition includes the Tailwind brand and its team, with no immediate plans for new template releases.

hackernews · EdwinHoksberg · Sep 9, 13:27 · [Discussion](https://news.ycombinator.com/item?id=49626190)

**Background**: Tailwind CSS is a utility-first CSS framework that allows developers to style websites directly within HTML, differing from traditional frameworks like Bootstrap. Shopify is a leading e-commerce platform that has made numerous acquisitions to expand its services, and this move likely aims to integrate Tailwind's design capabilities into its ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shopify">Shopify - Wikipedia</a></li>
<li><a href="https://tracxn.com/d/acquisitions/acquisitions-by-shopify/__NNWgXlWtRBr7FVe-BI1BiwMHs246IPF8HlqlcE5kZno">List of 19 Acquisitions by Shopify (Aug 2026) - Tracxn</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of sadness and understanding, with users noting the inevitability of AI's impact on template sales. Some question the need for Tailwind in new projects given modern CSS features, while others express hope for the team's well-being and acknowledge Tailwind's educational value.

**Tags**: `#acquisition`, `#Tailwind`, `#Shopify`, `#CSS`, `#AI impact`

---

<a id="item-6"></a>
## [Qwen 3.8 May Mimic GPT-5.5 Pro Reasoning Traces](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

A gist claims that Qwen 3.8's reasoning prefills closely follow those of GPT-5.5 Pro, suggesting possible distillation from the proprietary model. The analysis uses a technique to recover hidden chain-of-thought from OpenAI models and compares the initial reasoning steps. This finding raises significant questions about training practices in the AI industry, particularly regarding the use of proprietary model outputs to train open-source models. It could impact trust and regulatory scrutiny around model development and distillation methods. The technique involves running a benchmark with a state-of-the-art model, recovering its chain-of-thought, and then using the first 1% of that reasoning as a prefix for the open-source model. Qwen 3.8 0902 was trained after the release of the relevant paper on August 10, so it could have seen those specific thoughts.

hackernews · wsxiaoys · Sep 9, 17:24 · [Discussion](https://news.ycombinator.com/item?id=49630026)

**Background**: Reasoning prefills refer to the initial chain-of-thought tokens generated by a model before producing a final answer. Distillation is a technique where a smaller model is trained to mimic a larger teacher model's outputs. The 'stolen thoughts' method, referenced in the discussion, is a known exploit to recover hidden reasoning from models like OpenAI's, which normally do not expose their full chain-of-thought.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49630026">Qwen 3.8 follows GPT-5.5 Pro reasoning prefills | Hacker News</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/qwen-3-8-9b-distilled-qwen-3-8-is-here-6dcbca16a319">Qwen 3.8–9B: Distilled Qwen 3.8 is here !! | by Mehul Gupta | Data Science in Your Pocket | Aug, 2026 | Medium</a></li>
<li><a href="https://www.mindstudio.ai/blog/qwen3-8-9b-distillation-local">Qwen3.8-9B: Running the Community-Distilled Model Locally | MindStudio</a></li>

</ul>
</details>

**Discussion**: Community comments debate the validity of the distillation claim, with some noting that both models may have been trained on the same benchmark solutions. Others question the availability of raw reasoning tokens and whether the overlap is conclusive evidence of distillation.

**Tags**: `#AI`, `#LLM`, `#distillation`, `#Qwen`, `#GPT`

---

<a id="item-7"></a>
## [Researcher Details Google Ads Malware Abuse, Sparks Debate](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

A security researcher published a detailed account of how they successfully advertised malicious software through Google Ads, exposing a critical vulnerability in the platform's ad review process. The article, titled 'How I advertise malicious software on Google Ads,' quickly gained traction on Hacker News with 342 points and 207 comments. This revelation underscores the ongoing threat of malvertising, where cybercriminals exploit trusted advertising platforms to distribute malware, potentially reaching millions of users. It highlights the need for stronger human oversight and more robust automated detection systems in online advertising, as current measures appear insufficient. The researcher's account was initially rejected but later reinstated after the issue gained visibility on Hacker News, suggesting that Google's automated systems may have flagged the content only after public attention. Community comments reveal widespread frustration with Google's reliance on automated systems and lack of human contact points for resolving such issues.

hackernews · xlii · Sep 9, 11:43 · [Discussion](https://news.ycombinator.com/item?id=49624856)

**Background**: Malvertising is a growing cybersecurity threat where attackers place malicious ads on legitimate platforms like Google Ads to trick users into downloading malware or visiting phishing sites. Google has explicit policies prohibiting malware distribution, but enforcement often relies on automated systems that can be bypassed. Recent research from Zscaler and Microsoft has documented malvertising campaigns leading to info stealers and ransomware, highlighting the scale of the problem.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/adspolicy/answer/15939580?hl=en">Malicious Software - Advertising Policies Help - Google Help</a></li>
<li><a href="https://www.csoonline.com/article/4186813/attackers-abuse-google-ads-gitlab-and-claude-to-deliver-malware.html">Attackers abuse Google Ads, GitLab, and Claude to deliver malware</a></li>
<li><a href="https://www.zscaler.com/blogs/security-research/malvertising-campaign-leading-zemot">Malvertising Campaign Leading To Zemot | Zscaler</a></li>

</ul>
</details>

**Discussion**: Community comments express strong criticism of Google's automated moderation, with users sharing personal experiences of being ignored or unfairly treated. Some note that Google is not alone, as many companies hide behind automated systems, and suggest regulatory requirements for human contact points. The researcher's update about account reinstatement was met with mixed feelings, acknowledging the power of public pressure but lamenting that it took such amplification to get a fix.

**Tags**: `#security`, `#google ads`, `#malware`, `#online advertising`, `#cybersecurity`

---

<a id="item-8"></a>
## [Terence Tao Warns AI Could Deplete Open Math Problems](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 8.0/10

Terence Tao, a renowned mathematician, has publicly warned that AI-driven research efforts may rapidly deplete the pool of fruitful open problems in mathematics, potentially discouraging researchers from sharing promising directions. His comments, posted on Mathstodon, highlight a shift in incentives that could undermine centuries of open science traditions. This warning is significant because it addresses a potential unintended consequence of AI in research: the erosion of collaborative, open science practices that have been fundamental to mathematical progress. If researchers hoard problems to avoid AI-driven competition, it could slow innovation and damage the long-term health of the field, affecting mathematicians, AI developers, and the broader scientific community. Tao specifically notes that even the rumor of someone working on a problem can trigger massive AI-powered efforts to solve it before the original researcher can fully develop their work. This creates a 'non-renewable' mining of open problems, where promising directions become scarce, and the incentive to share them diminishes.

rss · Simon Willison · Sep 9, 00:20

**Background**: Open science is a movement that promotes transparency and collaboration in research, allowing scientists to share findings, data, and ideas openly. In mathematics, sharing open problems has been a tradition that fosters collective progress. Recent advances in AI, such as solving the Navier-Stokes problem, have demonstrated AI's capability to tackle complex mathematical challenges, but also raise concerns about fairness and the pace of research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/">AI Has Solved One of Math ’s $1 Million Millennium Prize Problems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_science">Open science - Wikipedia</a></li>
<li><a href="https://theoutpost.ai/news-story/ai-achieves-major-breakthrough-on-1-million-navier-stokes-problem-transforming-mathematics-forever-30584/">OpenAI Solves Navier-Stokes Millennium Problem Amid Scandal</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#open science`, `#mathematics`, `#research incentives`

---

<a id="item-9"></a>
## [DeepSeek V4.1 Flash Beta: Native Multimodal, Faster and Cheaper](https://t.me/zaihuapd/43708) ⭐️ 8.0/10

DeepSeek has begun limited-time internal testing of V4.1 Flash, an interim model that introduces native multimodal support, improved performance, faster generation, and lower costs. The model is accessed via the same base_url with the model name 'deepseek-v4.1-flash-expires-on-0910' and is priced identically to deepseek-v4-flash. This release is significant because it marks DeepSeek's push into native multimodal AI with a new architecture, potentially boosting its competitiveness in the global AI race. The combination of faster speed and lower cost could make advanced multimodal capabilities more accessible to developers and businesses. The model uses a new model structure and is a complete retraining rather than a fine-tune of the previous version. During the beta, each account is limited to 20 concurrent requests, and the model name includes an expiration date of 0910, indicating a temporary availability.

telegram · zaihuapd · Sep 9, 07:18

**Background**: DeepSeek is a Chinese AI lab known for its open-weight large language models. V4.1 Flash is an interim update in the V4 series, which includes models like V4-Pro (1.6T parameters) and V4-Flash (284B parameters), both using Mixture-of-Experts (MoE) architecture. Native multimodal support means the model can directly process and understand multiple types of data, such as text and images, without separate components.

<details><summary>References</summary>
<ul>
<li><a href="https://technode.com/2026/09/09/deepseek-v4-1-flash-multimodal-limited-beta/">DeepSeek begins limited-time beta of V4.1 Flash multimodal model · TechNode</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-1-flash-leak">DeepSeek V 4 . 1 Flash Beta: Flash Prices Just Got Cheaper</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 Explained: V 4 -Pro 1.6T vs V 4 - Flash 284B (2026)</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI model`, `#multimodal`, `#LLM`, `#release`

---