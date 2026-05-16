---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 25 items, 6 important content pieces were selected

---

1. [SGLang v0.5.12 Adds Full Inference Support for DeepSeek V4](#item-1) ⭐️ 9.0/10
2. [δ-Mem: Fixed-Size Memory with Delta-Rule for LLMs](#item-2) ⭐️ 8.0/10
3. [Frontier AI Breaks Open CTF Competition Format](#item-3) ⭐️ 8.0/10
4. [DeepSeek-V4-Flash Revives LLM Steering Interest](#item-4) ⭐️ 8.0/10
5. [Google Bans Manipulating AI Search Results in Spam Policy](#item-5) ⭐️ 8.0/10
6. [GitHub Copilot Desktop App Enters Technical Preview](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.12 Adds Full Inference Support for DeepSeek V4](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 9.0/10

SGLang v0.5.12 has been released, adding full inference support for DeepSeek V4, including tensor parallelism, expert parallelism, context parallelism, and data parallel attention, along with optimized kernels like DeepGemm and FlashMLA for MegaMoE. This release enables efficient deployment of DeepSeek V4, a state-of-the-art 1.6 trillion parameter model, on a wide range of hardware including Nvidia B300/B200/H200/H100 and AMD MI35X, significantly lowering the barrier for running large-scale MoE models in production. Key features include HiSparse for offloading inactive KV cache to CPU memory, HiCache with UnifiedRadixTree, W4A4 MegaMoE kernels for faster speed with negligible accuracy drop, and a unified Docker tag for all Nvidia GPUs.

github · Fridge003 · May 16, 18:23

**Background**: DeepSeek V4 is a large language model with a Mixture-of-Experts (MoE) architecture, featuring 1.6 trillion total parameters and 49 billion active parameters. SGLang is an open-source inference framework designed for efficient serving of large language models, supporting advanced parallelism and kernel optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-04-10-sglang-hisparse/">HiSparse : Turbocharging Sparse Attention with... | LMSYS Org</a></li>
<li><a href="https://www.morphllm.com/deepseek-v4">DeepSeek V4: Architecture, Benchmarks, and API Guide (2026)</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#DeepSeek`, `#SGLang`, `#inference`, `#parallelism`

---

<a id="item-2"></a>
## [δ-Mem: Fixed-Size Memory with Delta-Rule for LLMs](https://arxiv.org/abs/2605.12357) ⭐️ 8.0/10

δ-Mem introduces a fixed-size state matrix updated via delta-rule learning to compress past information for efficient online memory in large language models. This method addresses the growing need for efficient long-term memory in LLMs, potentially reducing computational costs and enabling more context-aware AI agents without expanding context windows. The delta-rule learning updates the state matrix incrementally, but community comments note that capacity limits and query-association challenges remain unsolved, and the approach is similar to adding DeltaNet hypernetworks to existing LLMs.

hackernews · 44za12 · May 16, 09:30 · [Discussion](https://news.ycombinator.com/item?id=48158506)

**Background**: Large language models typically have a fixed context window, limiting their ability to remember information across long conversations or sessions. Online memory methods aim to compress past interactions into a compact representation that can be retained and queried later, but they face trade-offs between memory size, retrieval accuracy, and computational efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Learning_rule">Learning rule - Wikipedia</a></li>
<li><a href="https://supermemory.ai/blog/3-ways-to-build-llms-with-long-term-memory/">3 Ways To Build LLMs With Long-Term Memory</a></li>
<li><a href="https://machinelearningatscale.substack.com/p/deep-dive-into-memory-for-llms-architectures">Deep dive into "Memory for LLMs" architectures</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed opinions: some appreciate the approach but note it doesn't solve fundamental capacity limits, while others point out the title mangling and suggest the work is not highly novel. There is also interest in practical applications like remembering guidelines across sessions.

**Tags**: `#LLM`, `#memory`, `#compression`, `#deep learning`, `#efficiency`

---

<a id="item-3"></a>
## [Frontier AI Breaks Open CTF Competition Format](https://kabir.au/blog/the-ctf-scene-is-dead) ⭐️ 8.0/10

A blog post argues that frontier AI models have fundamentally broken the open CTF (Capture The Flag) format by enabling instant solutions, reducing the collaborative learning experience and challenging the traditional competition structure. This disruption threatens the educational value of CTFs, which are a key training ground for cybersecurity skills, and forces the community to rethink challenge design and competition rules in the age of AI. The post highlights that AI can now solve typical CTF challenges in minutes, shifting the focus from problem-solving to AI-assisted flag retrieval, and that both playing and building CTF challenges have become less rewarding.

hackernews · frays · May 16, 07:01 · [Discussion](https://news.ycombinator.com/item?id=48157559)

**Background**: Capture The Flag (CTF) competitions are cybersecurity contests where participants solve challenges to find hidden 'flags' and earn points. They are widely used for learning and skill development in areas like reverse engineering, cryptography, and web exploitation. Frontier AI models, such as advanced large language models, can now automate many of these tasks, raising questions about the future of such competitions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.paloaltonetworks.com/blog/2026/04/defenders-guide-frontier-ai-impact-cybersecurity/">Defender's Guide to the Frontier AI Impact on Cybersecurity</a></li>
<li><a href="https://www.cyber.gov.au/about-us/view-all-content/news/frontier-models-and-their-impact-on-cyber-security-update">Frontier AI models and their impact on cyber security | Cyber.gov.au</a></li>

</ul>
</details>

**Discussion**: Commenters express frustration that AI ruins both playing and building CTFs, with one noting the loss of collaborative problem-solving. Some suggest making challenges harder or banning AI, while others draw parallels to broader educational challenges posed by LLMs.

**Tags**: `#AI`, `#CTF`, `#cybersecurity`, `#education`, `#community`

---

<a id="item-4"></a>
## [DeepSeek-V4-Flash Revives LLM Steering Interest](https://www.seangoedecke.com/steering-vectors/) ⭐️ 8.0/10

DeepSeek-V4-Flash has rekindled interest in LLM steering vectors, enabling effective refusal removal and new interaction workflows as demonstrated by projects like DwarfStar 4. This development makes LLM steering practical again, allowing users to uncensor models and explore novel user interfaces, which could democratize AI customization and challenge safety alignment norms. The steering technique can completely remove refusals from DeepSeek-V4-Flash by identifying and neutralizing a single refusal direction, as noted by antirez. However, effective use requires a well-designed dataset and understanding of the steering feature.

hackernews · Brajeshwar · May 16, 14:58 · [Discussion](https://news.ycombinator.com/item?id=48160807)

**Background**: LLM steering vectors are directions in the model's latent space that control specific behaviors, such as refusal or political bias, without retraining. Earlier research found that refusal in LLMs is often mediated by a single direction, making it removable via steering. DeepSeek-V4-Flash is a recent model that has revived interest in this technique.

<details><summary>References</summary>
<ul>
<li><a href="https://bobrupakroy.medium.com/steering-large-language-models-with-activation-vectors-a-practical-guide-45866b3697ac">Steering Large Language Models with Activation Vectors ... | Medium</a></li>
<li><a href="https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction">Refusal in LLMs is mediated by a single... — AI Alignment Forum</a></li>
<li><a href="https://www.lesswrong.com/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms">A Sober Look at Steering Vectors for LLMs — LessWrong</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the potential for refusal removal (abliteration) and new UI workflows, with antirez clarifying that DwarfStar 4 is its own project, not a stripped-down llama.cpp. Some noted that steering vectors have been under-explored for practical use.

**Tags**: `#LLM`, `#steering vectors`, `#DeepSeek`, `#AI safety`, `#uncensoring`

---

<a id="item-5"></a>
## [Google Bans Manipulating AI Search Results in Spam Policy](https://www.theverge.com/tech/931416/google-ai-search-spam-policy) ⭐️ 8.0/10

Google updated its search spam policy to explicitly prohibit manipulating generative AI search responses, including AI Overviews and AI Mode, treating such tactics as equivalent to traditional search ranking manipulation. This policy directly targets the emerging practice of Generative Engine Optimization (GEO), signaling a major shift in enforcement that affects SEO professionals and content creators who rely on AI-generated search visibility. Violating sites may be demoted or removed from search results entirely. Common GEO tactics include mass-producing biased "best recommendation" content or embedding prompts to trick AI models into treating a site as an authoritative source.

telegram · zaihuapd · May 16, 06:31

**Background**: Generative Engine Optimization (GEO) is the practice of optimizing content to appear in AI-powered search engines like ChatGPT, Perplexity, and Google's AI Overviews. As users increasingly rely on AI-generated answers, businesses have sought to game these systems, leading Google to update its longstanding spam policies to cover AI-specific manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://foundingengine.com/ai-search/">AI Search Optimization ( GEO ) — Founding Engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Google`, `#AI search`, `#spam policy`, `#GEO`, `#SEO`

---

<a id="item-6"></a>
## [GitHub Copilot Desktop App Enters Technical Preview](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) ⭐️ 8.0/10

GitHub Copilot desktop app is now available in technical preview, enabling developers to start isolated development sessions from issues, pull requests, prompts, or history, view diffs, run tests, create PRs, and use Agent Merge to automatically handle review comments and merges. This app brings agent-driven development into a dedicated desktop environment, streamlining the entire PR lifecycle and reducing context switching for developers. It represents a significant step toward fully AI-assisted coding workflows. Copilot Pro and Pro+ subscribers can immediately request early access; Business and Enterprise users will get access within the week, but organization admins must enable the preview and CLI permissions in policies. The app supports multiple isolated agent sessions simultaneously, each with its own branch.

telegram · zaihuapd · May 16, 15:07

**Background**: GitHub Copilot is an AI-powered code completion and assistance tool. The new desktop app extends Copilot's capabilities beyond IDE integration, offering a standalone environment for agentic development. Agent Merge is a feature that automatically resolves merge conflicts and handles PR review comments, previously introduced as a cloud agent feature.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/">GitHub Copilot app is now available in technical preview</a></li>
<li><a href="https://docs.github.com/en/copilot/concepts/agents/github-copilot-app">About the GitHub Copilot app</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions">Working with agent sessions in the GitHub Copilot app</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#AI-assisted development`, `#developer tools`, `#technical preview`

---