---
layout: default
title: "Horizon Summary: 2026-07-29 (EN)"
date: 2026-07-29
lang: en
---

> From 34 items, 10 important content pieces were selected

---

1. [TurboFieldfare: Run Gemma 4 26B in 2GB RAM on M-series Mac](#item-1) ⭐️ 9.0/10
2. [Mitchell Hashimoto Launches Superlogical, Transfers Ghostty to Non-Profit](#item-2) ⭐️ 8.0/10
3. [Kimi K3-256k: Half the Quota, Same Performance](#item-3) ⭐️ 8.0/10
4. [Long Policy Documents Fail to Govern AI Agents](#item-4) ⭐️ 8.0/10
5. [AI Worms Self-Propagate Through Copilot for Word](#item-5) ⭐️ 8.0/10
6. [Matthew Green: AI Cryptanalysis Could Strengthen Post-Quantum Crypto](#item-6) ⭐️ 8.0/10
7. [Claude shared links indexed by search engines, exposing user data](#item-7) ⭐️ 8.0/10
8. [Russia charges Telegram founder Durov with aiding terrorism, issues international warrant](#item-8) ⭐️ 8.0/10
9. [Report: Hugging Face Widely Used to Generate Deepfake Nudes](#item-9) ⭐️ 8.0/10
10. [China Drafts Anti-Cyberbullying Law, Regulates AI-Generated Abuse](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TurboFieldfare: Run Gemma 4 26B in 2GB RAM on M-series Mac](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

An open-source Swift/Metal inference engine called TurboFieldfare runs the 4-bit quantized Gemma 4 26B-A4B-IT model on any M-series Mac using only about 2 GB of RAM by streaming routed experts from SSD. This breakthrough enables running large Mixture-of-Experts models on memory-constrained devices like 8GB Macs, democratizing access to frontier AI on consumer hardware and potentially influencing future on-device AI architectures. The engine achieves 5–6 tok/s on an 8GB M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro, using a small expert cache and bounded parallel pread to overlap SSD reads with GPU computation.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Mixture-of-Experts (MoE) models like Gemma 4 26B have many parameters but only activate a subset per token, making them efficient but still memory-heavy. 4-bit quantization reduces model size, but the full 14GB weights still exceed typical Mac RAM. TurboFieldfare keeps only shared layers and KV cache in RAM, streaming expert weights from SSD on demand.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/drumih/turbo-fieldfare">GitHub - drumih/ turbo - fieldfare : Gemma 4 26B-A4B inference in...</a></li>
<li><a href="https://andrew.ooo/posts/flash-moe-397b-model-macbook-local-inference/">Flash- MoE : Running a 397B Parameter Model on... — andrew.ooo</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/">Gemma 4 with quantization-aware training - The Keyword</a></li>

</ul>
</details>

**Discussion**: Commenters praised the approach, with some noting similarities to mmap-based solutions in llama.cpp but highlighting TurboFieldfare's tuned synchronization of SSD reads with inference. One user provided a workaround for older macOS versions, and another expressed interest in collaborating on related projects.

**Tags**: `#on-device AI`, `#inference engine`, `#MoE`, `#Swift`, `#Metal`

---

<a id="item-2"></a>
## [Mitchell Hashimoto Launches Superlogical, Transfers Ghostty to Non-Profit](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto announced Superlogical, a new company that will build commercial products on top of the open-source libghostty terminal library, while transferring ownership of the Ghostty terminal emulator to a non-profit organization. This move ensures Ghostty remains community-owned and open-source, while Superlogical can sustainably develop proprietary tools leveraging libghostty, potentially fostering a richer terminal ecosystem. Superlogical will use libghostty as a public building block, consuming the same MIT-licensed components available to everyone, and will continue to upstream shared terminal work for the benefit of all libghostty consumers.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: Ghostty is a fast, feature-rich, cross-platform terminal emulator using GPU acceleration and native UI. libghostty is its underlying library, a cross-platform, zero-dependency C and Zig library for building terminal emulators or handling terminal functionality like VT sequence parsing.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the transfer of Ghostty to a non-profit and the open-source dependency model, with some drawing parallels to older technologies like OLE/COM. A few expressed frustration with the enigmatic title, but overall sentiment was positive.

**Tags**: `#open-source`, `#terminal`, `#startup`, `#software-engineering`, `#community`

---

<a id="item-3"></a>
## [Kimi K3-256k: Half the Quota, Same Performance](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Kimi has released the K3-256k model, a variant of its flagship K3 model that consumes half the quota while delivering equivalent results within a 256k context window. This pricing change makes Kimi significantly more affordable for most users, as the 256k context covers the vast majority of practical use cases, potentially accelerating commoditization in the LLM market. The K3-256k model uses the same model ID 'k3-256k' for API calls, and its quota consumption is exactly half of the original K3 (1M context) model. Users who stay within 256k tokens effectively pay half the price.

hackernews · monneyboi · Jul 29, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49101852)

**Background**: Context window size determines how much text an LLM can process at once. While 1M-token context windows are impressive, most real-world tasks (e.g., code generation, document analysis) fit within 256k tokens. Kimi's K3 is a flagship model with a 1M-token context, but the new K3-256k variant offers a cost-effective alternative for typical workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>
<li><a href="https://kernelbench.com/models/kinetic-0715">Kimi K3 (256k) · kernelbench</a></li>

</ul>
</details>

**Discussion**: Community members welcomed the move, noting that 256k context is sufficient for most tasks and that the price reduction is massive. Some see this as a sign of LLMs becoming commodities, with US AI labs losing their moat as hyperscalers offer cheaper tokens.

**Tags**: `#LLM`, `#AI pricing`, `#context window`, `#Kimi`, `#commoditization`

---

<a id="item-4"></a>
## [Long Policy Documents Fail to Govern AI Agents](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

A new paper, Handbook.md, demonstrates that long policy documents fail to reliably govern AI agents due to fundamental limitations in long-context models, such as attention dilution and memory constraints. This finding challenges the assumption that long-context LLMs can effectively follow complex policies, which is critical for AI safety and agent governance in real-world applications like finance and healthcare. The paper provides empirical evidence that even state-of-the-art models struggle with long policy documents, and suggests that alternative approaches like reinforcement learning on agentic datasets may be needed.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: Long-context LLMs claim to handle up to 1 million tokens, but their performance degrades due to quantization, KV cache limitations, and poor sampling. Existing benchmarks often fail to capture real-world reasoning over long texts. The AI agent economy lacks governance infrastructure, making this research timely.

<details><summary>References</summary>
<ul>
<li><a href="https://agentgoverning.com/">The independent benchmark for AI agent governance</a></li>
<li><a href="https://github.com/agentic-control-plane/agentgovbench">GitHub - agentic-control-plane/agentgovbench: Agent governance ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight real-world issues: users report that models like Claude ignore instructions in CLAUDE.md after about 10 minutes, while in-prompt instructions work better. Some argue that humans also struggle with long policy documents, so the benchmark may reflect a general limitation rather than a model-specific flaw.

**Tags**: `#LLM`, `#long-context`, `#AI safety`, `#benchmark`, `#agent`

---

<a id="item-5"></a>
## [AI Worms Self-Propagate Through Copilot for Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 8.0/10

Researchers demonstrated a new prompt injection variant that turns Microsoft Copilot for Word into a vector for self-replicating AI worms, where malicious instructions hidden in a document can cause Copilot to alter and propagate the attack to new documents. This vulnerability represents a novel class of AI security threats where LLM-integrated applications can be exploited to autonomously spread malware, highlighting systemic risks that current mitigations cannot fully address. The worm exploits the inability of AI to separate data from instructions, using techniques like white text to hide prompts. Two mitigation attempts, including a model upgrade, failed to close the vulnerability class.

hackernews · Canopy9560 · Jul 29, 11:44 · [Discussion](https://news.ycombinator.com/item?id=49096188)

**Background**: Prompt injection is a cybersecurity attack where specially crafted inputs cause LLMs to ignore prior instructions and perform unintended actions. AI worms are autonomous, self-propagating malware that use LLM-based techniques to spread. Copilot for Word is an AI assistant that can edit documents based on user prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/">Context Collapse, Part 3 - AI Worming through Word | En Klype Salt</a></li>
<li><a href="https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html">Researchers Build Self-Replicating AI Worm That Operates Entirely on Local, Open-Weight Models</a></li>
<li><a href="https://www.theregister.com/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588">Word worm crawls into Copilot , spreads chaos</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that this class of vulnerability is fundamentally unfixable as long as AI mixes instructions with data. Some noted that granting extensive access to AI agents is risky, and that techniques like white text remain effective. One commenter shared a real-world example of tricking frontier algorithms with Unicode font tricks.

**Tags**: `#AI security`, `#prompt injection`, `#Copilot`, `#adversarial attacks`, `#LLM vulnerabilities`

---

<a id="item-6"></a>
## [Matthew Green: AI Cryptanalysis Could Strengthen Post-Quantum Crypto](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Cryptographer Matthew Green commented that the current transition to post-quantum cryptography is an ideal time for AI to advance cryptanalysis, potentially strengthening confidence in new algorithms like HAWK. This perspective highlights a unique opportunity where AI-driven cryptanalysis could either break or validate new post-quantum standards, shaping the security of future communications. Green references Anthropic's recent work where Claude Mythos found weaknesses in AES and HAWK, with each attack costing roughly $100,000 in API usage. He also invokes Impagliazzo's five worlds, noting that if AI undermines all hard problems, we might live in Minicrypt.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography (PQC) aims to develop algorithms secure against quantum computers, which could break current RSA and elliptic-curve cryptography. NIST has been standardizing PQC algorithms since 2017, with final standards released in 2024. HAWK is one such candidate standard. Impagliazzo's five worlds classify possible computational complexity scenarios, with Minicrypt being a world where public-key cryptography is impossible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://www.ai-jarvis.eu/anthropics-mythos-found-flaws-aes-and-hawk-cryptography-100000-attack">Anthropic's Mythos Found Flaws in AES and HAWK Cryptography ...</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#standards`

---

<a id="item-7"></a>
## [Claude shared links indexed by search engines, exposing user data](https://t.me/zaihuapd/42830) ⭐️ 8.0/10

Anthropic's Claude shared conversation feature has a privacy bug where public links lack noindex tags, causing them to be indexed by Google and other search engines, exposing sensitive user data such as API keys, cryptocurrency wallets, and social security numbers. This vulnerability affects a widely-used AI service and exposes highly sensitive personal and corporate data, posing serious privacy and security risks. It echoes a similar issue with ChatGPT from a year ago, highlighting systemic risks in AI chat sharing features. The shared conversations were made public by default and lacked noindex tags, allowing search engines to crawl and index them. Users are advised to manually delete sensitive chats from the 'Shared Conversations' management page in settings.

telegram · zaihuapd · Jul 29, 02:40

**Background**: The noindex tag is an HTML meta tag or HTTP header that tells search engines not to include a page in search results. Without it, any publicly accessible URL can be indexed. Claude's share feature creates a public URL for each conversation, and if not properly restricted, these URLs can be discovered by search engines. A similar issue occurred with ChatGPT about a year ago and was quickly fixed.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/">PSA: Your Claude shared chats and Artifacts may have... | TechCrunch</a></li>
<li><a href="https://newscord.org/article/claude-shared-chats-and-artifacts-indexed-on-google-search-after-anthropic-share--Story_20260727_PSAYourClaudesharedcecfd763c">Claude Shared Chats and Artifacts Indexed on Google... | NewsCord</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/block-indexing">Block Search Indexing with noindex | Google Search Central</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#AI`, `#Claude`, `#data leak`

---

<a id="item-8"></a>
## [Russia charges Telegram founder Durov with aiding terrorism, issues international warrant](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

On July 29, 2026, Russia's Federal Security Service (FSB) filed criminal charges against Telegram founder Pavel Durov under Article 205.1.1 of the Criminal Code (aiding terrorism) and placed him on an international wanted list, accusing Telegram of refusing to remove channels and bots used to coordinate attacks in Russia. This marks a significant escalation in Russia's crackdown on tech platforms, potentially setting a precedent for holding platform founders personally liable for user-generated content. It could also strain Telegram's operations globally, as Durov faces arrest risk in countries with extradition treaties with Russia. The FSB specifically cited Telegram's failure to remove channels and bots used by Ukrainian intelligence and terrorist/extremist groups to coordinate sabotage, terrorist attacks, mass killings, and fraud, resulting in casualties and billions of rubles in damages. The charges are under Article 205.1.1, which covers aiding terrorist activity.

telegram · zaihuapd · Jul 29, 05:56

**Background**: Telegram is an encrypted messaging app founded by Pavel Durov and his brother Nikolai in 2013, now with over 1 billion monthly active users. The FSB is Russia's principal security agency, successor to the KGB. Article 205.1 of the Russian Criminal Code criminalizes aiding terrorism, including providing resources or services that facilitate terrorist acts.

<details><summary>References</summary>
<ul>
<li><a href="https://meduza.io/en/news/2026/07/29/russia-s-fsb-security-service-accuses-telegram-founder-pavel-durov-of-aiding-terrorism-issues-international-arrest-warrant">Russia ’s FSB security service accuses Telegram founder... — Meduza</a></li>
<li><a href="https://tass.com/society/2166649">Russia ’s FSB charges Telegram co-founder Durov with... - TASS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pavel_Durov">Pavel Durov - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#Russia`, `#terrorism`, `#regulation`, `#Pavel Durov`

---

<a id="item-9"></a>
## [Report: Hugging Face Widely Used to Generate Deepfake Nudes](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

A report by AI Forensics, published on July 28, reveals that Hugging Face is being extensively used to generate non-consensual deepfake nude images, including child sexual abuse material. The organization found that seven out of the top nine image-editing models on the platform can easily undress women with simple prompts, and a honeypot set up by researchers received over 1,000 requests in seven days, 73% of which were sexually explicit and nearly 7% targeted children. This report highlights critical safety and ethical failures in AI model hosting platforms, as Hugging Face's weak safeguards enable widespread abuse for generating non-consensual intimate images. The findings underscore the urgent need for stronger content moderation and platform accountability to protect individuals, especially minors, from AI-powered exploitation. The report notes that Hugging Face's platform-level safeguards are nearly nonexistent, contradicting its own policies prohibiting non-consensual sexual content and child nudity. AI Forensics recommends implementing prompt filtering and output scanning mechanisms to block harmful image generation.

telegram · zaihuapd · Jul 29, 08:20

**Background**: Hugging Face is a popular platform for sharing machine learning models and datasets, widely used by the AI community. Deepfake pornography involves using AI to create fake nude images of individuals without consent, often causing severe harm to victims. The report by AI Forensics, a European nonprofit, exposes how open-source models on such platforms can be misused for malicious purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_pornography">Deepfake pornography - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#deepfake`, `#Hugging Face`, `#content moderation`, `#child safety`

---

<a id="item-10"></a>
## [China Drafts Anti-Cyberbullying Law, Regulates AI-Generated Abuse](https://mp.weixin.qq.com/s/PrzKFhbwjgFEGBPADvFD6Q) ⭐️ 8.0/10

On July 29, 2026, China's Cyberspace Administration released a draft Anti-Cyberbullying Law for public comment, which for the first time includes specific provisions regulating the use of AI to generate and spread cyberbullying content. This legislation marks a significant step in China's AI governance, imposing clear obligations on platforms to monitor and prevent AI-generated cyberbullying, and providing stronger legal protections for victims, including personality rights injunctions and mental damage compensation. The draft law consists of 7 chapters and 60 articles, defining cyberbullying as activities that infringe on reputation, privacy, portrait rights, and personal information through concentrated or sustained online attacks. It requires platforms to establish detection mechanisms and protective features, and introduces multi-department government coordination.

telegram · zaihuapd · Jul 29, 10:59

**Background**: Cyberbullying has become a serious social issue in China, with incidents like 'human-flesh search' and AI-generated deepfake abuse causing widespread harm. The draft law builds on existing regulations such as the 2023 'Guiding Opinions on Punishing Cyberbullying Crimes' and the Civil Code's personality rights injunction system, aiming to provide a comprehensive legal framework.

<details><summary>References</summary>
<ul>
<li><a href="http://www.js.xinhuanet.com/20230713/45eb9dff79b040a7a9c3aa17aeea0a88/c.html">江苏多地法院探索发出人格权侵害禁令_新华网江苏频道</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607291634950.html">多类 网 暴 行为拟被明确立 法 惩治！ 南都曾曝光“人肉开盒”乱象 | 南都N视频</a></li>
<li><a href="https://t.me/tnews365/35453">竹新社 – Telegram</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#cyberbullying`, `#China law`, `#platform governance`

---