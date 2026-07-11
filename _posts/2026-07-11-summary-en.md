---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 24 items, 9 important content pieces were selected

---

1. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [Humanoid Robot Performs World's First Live Pig Gallbladder Surgery](#item-2) ⭐️ 9.0/10
3. [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](#item-3) ⭐️ 9.0/10
4. [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](#item-4) ⭐️ 8.0/10
5. [Hotz Warns AI Regulation Threatens Freedom](#item-5) ⭐️ 8.0/10
6. [SpaceXAI and Cursor Launch Grok 4.5](#item-6) ⭐️ 8.0/10
7. [Apple sues OpenAI for trade secret theft in hardware push](#item-7) ⭐️ 8.0/10
8. [6 U-Boot Flaws Allow Code Execution Before OS Boot](#item-8) ⭐️ 8.0/10
9. [Shanghai Aims for High-Quality Brain Control by 2027](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models and removes the legacy PagedAttention implementation. The Transformers modeling backend now achieves native-level performance, and new models like LLaVA-OneVision-2 and GLM-5 are supported. This release marks a major architectural shift in vLLM, simplifying the codebase and improving performance for a wide range of models. The removal of PagedAttention and the maturity of Model Runner V2 signal a more stable and efficient inference engine for the LLM community. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers backend gained FP8 MoE support and CUDA graph fixes, achieving parity with native vLLM performance.

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source LLM inference engine that uses PagedAttention for efficient memory management of the KV cache. Model Runner V2 is a newer execution path that replaces the older V1 backend, aiming to improve performance and maintainability. This release removes the legacy PagedAttention code, relying entirely on the newer attention implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>
<li><a href="https://docs.vllm.ai/en/v0.14.1/api/vllm/multimodal/evs/">evs - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-2"></a>
## [Humanoid Robot Performs World's First Live Pig Gallbladder Surgery](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons remotely operated a Unitree G1 humanoid robot to perform the world's first laparoscopic cholecystectomy on live pigs, with results published in Nature. This breakthrough demonstrates that low-cost, general-purpose humanoid robots can perform delicate surgeries, potentially making remote surgery accessible in rural, battlefield, or space settings where specialized surgical robots are too expensive or unavailable. The Unitree G1 robot costs as low as $13,500 for the base model and about $67,000 with dexterous hands, compared to millions for da Vinci surgical robots. The robot is 1.5 meters tall and weighs 27 kg, making it compact and portable.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Laparoscopic cholecystectomy is a common minimally invasive surgery to remove the gallbladder. Specialized surgical robots like the da Vinci system are widely used but cost hundreds of thousands to millions of dollars, limiting access. Humanoid robots like Unitree G1 are general-purpose platforms designed for mobility and manipulation, and this study shows they can be adapted for surgical tasks with remote control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI has officially released the GPT-5.6 series, featuring three tiers: Sol (flagship), Terra (balanced), and Luna (cost-efficient). The update introduces max/ultra reasoning, multi-agent collaboration, and programmatic tool calling, with significant improvements in code, knowledge work, design, research, and cybersecurity capabilities. This release marks a major step in making advanced AI more accessible and cost-effective, with Sol delivering top-tier performance and Luna enabling high-volume, low-cost deployments. The new multi-agent and programmatic tool calling features could transform how complex tasks are automated across industries. GPT-5.4 will retire on July 23, while GPT-5.5 remains available. The tier names (Sol, Terra, Luna) are durable and will advance on their own cadence, independent of the generation number. Sol achieves a perfect score of 5.0 on five of eight document translation scenarios.

telegram · zaihuapd · Jul 11, 13:34

**Background**: GPT-5.6 is the latest generation of OpenAI's large language model, succeeding GPT-5.5. The series introduces a tiered model structure where the number indicates the generation and the name (Sol, Terra, Luna) indicates the capability and cost level. Multi-agent collaboration allows multiple AI agents to coordinate on complex tasks, while programmatic tool calling enables models to invoke tools via code rather than individual API calls, reducing latency and cost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna : Which Tier Should You Actually Use?</a></li>
<li><a href="https://belindoc.com/blog/gpt-5-6-translation-review-sol-terra-luna">GPT - 5 . 6 Document Translation Review: Sol vs Terra vs Luna ...</a></li>
<li><a href="https://apidog.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : which model should you use?</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#multi-agent`

---

<a id="item-4"></a>
## [SGLang v0.5.15 Boosts GLM-5.2 on Blackwell GPUs](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 delivers production-tuned NVFP4 support for GLM-5.2 on Blackwell GPUs, achieving over 500 tokens per second per user on 8x B300 and 450 on 4x GB300 at batch size 1. It also introduces Spec V2 speculative decoding by default, IndexShare MTP, TopK V2, and other optimizations. This release significantly improves serving efficiency for GLM-5.2, a model designed for long-horizon tasks, making it more practical for real-time applications. The speculative decoding and kernel optimizations also benefit other large language models, advancing the state of LLM inference on NVIDIA Blackwell hardware. Spec V2 achieves +11% end-to-end throughput via CUDA-graphable DSA draft-extend and fused metadata ops. IndexShare MTP reduces draft-step cost by up to 1.9x on long contexts. The release also adds support for new models like Hunyuan 3, Qwen3.6 NVFP4, and native web search via Exa.

github · Fridge003 · Jul 10, 22:58

**Background**: NVFP4 is NVIDIA's 4-bit floating-point quantization format introduced with Blackwell GPUs, enabling lower-bitwidth inference with better quality than traditional 4-bit integer quantization. Speculative decoding accelerates text generation by using a small draft model to predict multiple tokens, which are then verified by the main model. SGLang is an open-source LLM serving framework that optimizes inference performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.03950v1">Diagonal-Tiled Mixed- Precision Attention for Efficient Low-Bit MXFP...</a></li>
<li><a href="https://huggingface.co/JongYeop/Mistral-7B-Instruct-v0.2-FP4-W4A4">JongYeop/Mistral-7B-Instruct-v0.2-FP4-W4A4 · Hugging Face</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2 - LMSYS Org</a></li>

</ul>
</details>

**Tags**: `#LLM serving`, `#GPU optimization`, `#speculative decoding`, `#GLM`, `#Blackwell`

---

<a id="item-5"></a>
## [Hotz Warns AI Regulation Threatens Freedom](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html) ⭐️ 8.0/10

George Hotz published an essay arguing that AI regulation could lead to a dystopian future where AI systems enforce ideological compliance, drawing parallels to historical struggles for liberty. This essay sparks debate on the balance between AI safety and individual freedoms, highlighting concerns that regulation might be used to suppress dissent and enforce political agendas. Hotz specifically warns against AI systems that could deny information and log users for 'thoughtcrime,' and argues that freedom is not binary but a fundamental principle worth fighting for.

hackernews · rvz · Jul 11, 18:04 · [Discussion](https://news.ycombinator.com/item?id=48874200)

**Background**: George Hotz is a well-known hacker and entrepreneur, famous for jailbreaking the iPhone and founding comma.ai. His essay reflects a libertarian perspective on technology regulation, often critiquing overreach in AI governance.

**Discussion**: Comments show mixed reactions: some agree with Hotz's concerns about censorship and thoughtcrime, while others argue that freedom is not binary and that AI agents acting in the real world require different considerations. There is also criticism that the essay lacks a central thesis.

**Tags**: `#AI ethics`, `#regulation`, `#freedom`, `#George Hotz`, `#societal impact`

---

<a id="item-6"></a>
## [SpaceXAI and Cursor Launch Grok 4.5](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI and Cursor have jointly released Grok 4.5, a new AI model focused on coding, legal, and financial services tasks, claiming top performance on the Harvey legal benchmark and double the token efficiency of leading models. This marks the first joint model after SpaceX's $60 billion acquisition of Cursor, signaling a major push into specialized AI for professional domains. The high token efficiency and domain-specific focus could disrupt existing AI coding and legal tools. Grok 4.5 runs at 80 tokens per second and is priced at $2 per million input tokens. It also emphasizes enhanced cybersecurity capabilities alongside its core focus areas.

telegram · zaihuapd · Jul 11, 01:44

**Background**: Harvey's Legal Agent Benchmark is an open-source benchmark for evaluating AI agents on real legal work. Token efficiency refers to how many useful tokens a model generates per unit cost or time, directly impacting accuracy and cost. Cursor is an AI-powered code editor and development environment, acquired by SpaceX in June 2026 for $60 billion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey’s Legal Agent Benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company)</a></li>
<li><a href="https://www.linkedin.com/posts/sean-holdbrook-74965654_i-was-originally-just-replying-to-a-post-activity-7396573267551117313-Dty6">The Importance of Token Efficiency in LLMs | Sean Brook... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Grok`, `#SpaceXAI`, `#Cursor`

---

<a id="item-7"></a>
## [Apple sues OpenAI for trade secret theft in hardware push](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 8.0/10

On July 10, 2026, Apple filed a lawsuit in the U.S. District Court for the Northern District of California against OpenAI, two former employees, and io Products, alleging systematic theft of trade secrets related to product design, manufacturing processes, and supply chain information to accelerate OpenAI's consumer hardware development. This high-profile legal battle between two tech giants could set a precedent for how trade secret laws apply to AI companies poaching talent from established hardware makers, potentially impacting the competitive landscape of AI hardware. If Apple's allegations are proven, OpenAI's hardware business—including devices developed with Jony Ive's io Products—could face significant legal and reputational damage. Apple specifically alleges that former employee Chang Liu accessed internal networks and downloaded dozens of hardware files after leaving the company, while OpenAI's hardware head Tang Yew Tan sent supplier information to his personal email before resigning and asked job candidates to bring Apple components to interviews. Apple also claims that over 400 former Apple employees now work at OpenAI.

telegram · zaihuapd · Jul 11, 03:14

**Background**: OpenAI, best known for its AI models like GPT-4, has been expanding into hardware. In May 2025, it acquired io Products, a company founded by former Apple design chief Jony Ive, to lead its hardware development. The first device from this collaboration was expected in 2026 but has been delayed to 2027 due to a trademark dispute. Trade secrets are confidential business information that provides a competitive edge; their misappropriation can lead to legal liability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html">Apple sues OpenAI alleging trade secret theft, says scheme was 'at every level'</a></li>
<li><a href="https://www.engadget.com/2212759/apple-calls-openais-hardware-business-rotten-to-its-core-in-trade-secret-theft-lawsuit/">Apple calls OpenAI's hardware business 'rotten to its core' in trade secret theft lawsuit - Engadget</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_(company)">io (company) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI hardware`

---

<a id="item-8"></a>
## [6 U-Boot Flaws Allow Code Execution Before OS Boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Firmware security firm Binarly disclosed six vulnerabilities in U-Boot's FIT signature verification, two of which allow arbitrary code execution and four cause denial of service, affecting versions since 2013.07. These flaws enable attackers to execute malicious code before the operating system boots, bypassing security measures like Secure Boot and potentially implanting persistent firmware malware on millions of devices. The vulnerabilities (BRLY-2026-037 to BRLY-2026-042) reside in the FIT image signature verification code and can be exploited remotely on devices with remote firmware update capabilities, such as BMCs.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded devices, responsible for loading the operating system. FIT (Flattened Image Tree) is a format for packaging kernel, device tree, and other binaries with cryptographic signatures to ensure authenticity. The vulnerabilities bypass this signature verification, allowing unsigned code to run.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U - Boot FIT Signature Verification — Das U - Boot unknown version...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#bootloader`, `#firmware`, `#U-Boot`

---

<a id="item-9"></a>
## [Shanghai Aims for High-Quality Brain Control by 2027](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

The Shanghai Municipal Science and Technology Commission issued the "Shanghai Brain-Computer Interface Future Industry Cultivation Action Plan (2025-2030)", targeting high-quality brain control by 2027, with semi-invasive BCI products leading clinical applications in China and breakthroughs in invasive BCI. This government-backed plan signals strong policy support for BCI technology, potentially accelerating clinical adoption and positioning Shanghai as a global leader in the field. It could bring life-changing benefits to patients with paralysis or speech loss. The plan aims to have at least five invasive or semi-invasive BCI products complete medical device type testing and clinical trials, enabling partial restoration of language and motor functions for patients with aphasia and paralysis.

telegram · zaihuapd · Jul 11, 15:49

**Background**: Brain-computer interfaces (BCIs) are classified into three types: non-invasive (scalp electrodes), semi-invasive (electrodes placed on the brain's surface under the skull), and invasive (electrodes implanted directly into brain tissue). Semi-invasive BCIs offer a balance between signal quality and reduced tissue damage, making them a promising path for clinical applications.

<details><summary>References</summary>
<ul>
<li><a href="https://segmentfault.com/a/1190000044921513">segmentfault.com/a/1190000044921513</a></li>
<li><a href="http://paper.people.com.cn/zgjjzk/pc/content/202512/30/content_30129910.html">脑 机 接 口 治病：从科幻到现实还有多远</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=837218">视频|想象过“ 脑 控 上淘宝”和“意念对话”吗？ 上海 脑 机接口临床试验获突破</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#policy`, `#China`, `#clinical application`, `#innovation`

---