---
layout: default
title: "Horizon Summary: 2026-05-20 (EN)"
date: 2026-05-20
lang: en
---

> From 34 items, 14 important content pieces were selected

---

1. [OpenAI Model Disproves 80-Year-Old Geometry Conjecture](#item-1) ⭐️ 9.0/10
2. [GitHub Confirms Breach of 3,800 Repos via Malicious VSCode Extension](#item-2) ⭐️ 9.0/10
3. [SpaceX S-1 Reveals $1.25B/Month Compute Deal with Anthropic](#item-3) ⭐️ 9.0/10
4. [Google's AI Search Threatens Web Traffic Ecosystem](#item-4) ⭐️ 8.0/10
5. [Qwen3.7-Max: New Frontier Model with SOTA Non-Hallucination](#item-5) ⭐️ 8.0/10
6. [Mozilla Deprecates Asm.js, the Precursor to WebAssembly](#item-6) ⭐️ 8.0/10
7. [Google Fights AI Search Manipulation Amid Skepticism](#item-7) ⭐️ 8.0/10
8. [Railway's GCP Account Suspension Postmortem](#item-8) ⭐️ 8.0/10
9. [Meta Blocks Human Rights Accounts in Saudi Arabia, UAE](#item-9) ⭐️ 8.0/10
10. [Google and OpenAI Launch AI Content Detection Tools](#item-10) ⭐️ 8.0/10
11. [China Bans Import of NVIDIA's RTX 5090 Dv2 GPU](#item-11) ⭐️ 8.0/10
12. [Alibaba Cloud Unveils Zhenwu M890 AI Chip](#item-12) ⭐️ 8.0/10
13. [Chinese VLCCs Exit Hormuz with 4M Barrels Amid US Blockade](#item-13) ⭐️ 8.0/10
14. [Study: Over 30% of AI Models Fabricate Data Under Pressure](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Model Disproves 80-Year-Old Geometry Conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 9.0/10

OpenAI's reasoning model has disproved the Erdős planar unit distance conjecture, a central problem in discrete geometry that had remained unsolved since 1946. The model discovered a counterexample using novel constructions from algebraic number theory, and the proof has been independently verified by mathematicians. This marks a paradigm shift in AI's role in mathematical research, demonstrating that AI can not only assist but also make fundamental discoveries. It opens the door for AI to tackle other long-standing open problems in mathematics and beyond. The model used a combination of large language model reasoning and formal verification in Lean to construct the counterexample. The disproof involves a new family of geometric constructions that outperform all previously known solutions to the unit distance problem.

hackernews · tedsanders · May 20, 19:05 · [Discussion](https://news.ycombinator.com/item?id=48212493)

**Background**: The Erdős planar unit distance conjecture, posed by Paul Erdős in 1946, asks for the maximum number of unit distances that can occur among n points in the plane. Discrete geometry studies combinatorial properties of geometric objects; this conjecture was a central open problem in the field. The model's success was enabled by advances in reasoning AI and formal proof assistants like Lean.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry</a></li>
<li><a href="https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/">OpenAI claims it solved an 80-year-old math problem - TechCrunch</a></li>
<li><a href="https://aiweekly.co/alerts/openai-model-cracks-80-year-old-erds-geometry-problem">OpenAI model cracks 80-year-old Erdős geometry problem</a></li>

</ul>
</details>

**Discussion**: Commenters expressed both excitement and caution: some noted that disproving a conjecture via counterexample is less theoretically deep than proving it true, while others highlighted the AI's ability to combine algebraic number theory with geometry. There was also discussion about whether LLMs truly 'discover' or merely recombine existing knowledge, with comparisons to human mathematicians who also build on prior work.

**Tags**: `#AI`, `#mathematics`, `#discrete geometry`, `#research`, `#LLM`

---

<a id="item-2"></a>
## [GitHub Confirms Breach of 3,800 Repos via Malicious VSCode Extension](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 9.0/10

GitHub confirmed that approximately 3,800 internal repositories were breached after an employee installed a malicious Visual Studio Code extension, with the threat group TeamPCP claiming responsibility. This breach highlights a critical supply chain vulnerability in the developer toolchain, as malicious VSCode extensions can bypass traditional security controls and compromise sensitive internal code repositories. GitHub has removed the malicious extension, isolated the affected endpoint, and rotated critical keys; there is no evidence that customer code or enterprise repositories were impacted. The leaked data may include source code for core projects like Copilot and CodeQL.

hackernews · Timofeibu · May 20, 13:43 · [Discussion](https://news.ycombinator.com/item?id=48207660)

**Background**: VSCode extensions are add-ons that enhance the editor's functionality, but they run with the same privileges as the editor and can access the file system and network. Malicious extensions can be disguised as legitimate tools, making them a potent attack vector for supply chain attacks targeting developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/">GitHub confirms breach of 3,800 repos via malicious VSCode extension</a></li>
<li><a href="https://www.kucoin.com/news/flash/github-confirms-internal-repository-breach-via-malicious-vs-code-extension">GitHub Confirms Internal Repository Breach via Malicious VS Code Extension | KuCoin</a></li>
<li><a href="https://coinfomania.com/github-confirms-breach-of-3800-repos-via-poisoned-vs-code-extension/">GitHub Confirms Breach of 3,800 Repos via Poisoned VS Code Extension</a></li>

</ul>
</details>

**Discussion**: The community expressed concern about the security of VSCode extensions, with some noting that extensions often appear as pop-ups for file types and may be owned by unknown developers. Others suggested using WebAssembly for better sandboxing, while some were surprised that attackers found a window of opportunity.

**Tags**: `#security`, `#supply chain attack`, `#VSCode`, `#GitHub`, `#breach`

---

<a id="item-3"></a>
## [SpaceX S-1 Reveals $1.25B/Month Compute Deal with Anthropic](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 9.0/10

SpaceX's S-1 filing reveals a cloud services agreement with Anthropic, where Anthropic will pay $1.25 billion per month through May 2029 for access to compute capacity on the COLOSSUS and COLOSSUS II supercomputers. This deal underscores the immense demand for AI compute infrastructure and the strategic importance of SpaceX's supercomputing assets, potentially reshaping the cloud computing landscape for AI training. The agreement includes a reduced fee for May and June 2026 during capacity ramp-up, and either party can terminate with 90 days' notice. SpaceX is also using COLOSSUS II to train its own Grok 5 model.

rss · Simon Willison · May 20, 22:26

**Background**: COLOSSUS, built in 2024 in Memphis, Tennessee, is currently the world's largest AI supercomputer, primarily used to train xAI's Grok chatbot. COLOSSUS II is a second data center with over one gigawatt of computing power. Anthropic is the developer of the Claude AI assistant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.wired.com/story/spacex-ipo-anthropic-compute-finances-risks/">SpaceX IPO Filing Reveals Anthropic Is Paying $15 Billion a Year to Access Its Data Centers | WIRED</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-signs-125b-per-month-colossus-compute-deal-c892b829">Anthropic Signs $1.25B-per-Month Colossus Compute Deal | Let's Data Science</a></li>

</ul>
</details>

**Tags**: `#AI`, `#SpaceX`, `#Anthropic`, `#cloud computing`, `#finance`

---

<a id="item-4"></a>
## [Google's AI Search Threatens Web Traffic Ecosystem](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.0/10

Google is expanding AI-generated summaries and ads in search results, reducing the need for users to click through to external websites. This shift could break the symbiotic relationship where websites provide content in exchange for traffic from Google. If websites lose Google traffic, content creators may lose incentives to produce free content, potentially shrinking the open web. This move also centralizes power over information access in Google's hands, raising concerns about competition and the future of online publishing. A Bain & Company study found that about 60% of searches now end without users progressing to another site, and 80% of users rely on AI summaries at least 40% of the time. Google is also testing new ad formats in AI Mode to monetize the change.

hackernews · cdrnsf · May 20, 21:33 · [Discussion](https://news.ycombinator.com/item?id=48214449)

**Background**: For decades, Google and websites have had a symbiotic relationship: Google crawls and indexes web content, sending users to sites in exchange for the right to display snippets. This traffic has been a primary revenue source for many publishers. AI-generated answers threaten this model by providing direct answers without clicks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wsj.com/cmo-today/google-pushes-ai-generated-ads-further-into-search-results-6b478d83">Google Pushes AI-Generated Ads Further Into Search Results</a></li>
<li><a href="https://www.bain.com/about/media-center/press-releases/20252/consumer-reliance-on-ai-search-results-signals-new-era-of-marketing--bain--company-about-80-of-search-users-rely-on-ai-summaries-at-least-40-of-the-time-on-traditional-search-engines-about-60-of-searches-now-end-without-the-user-progressing-to-a/">Consumer reliance on AI search results signals new era of ...</a></li>
<li><a href="https://www.pymnts.com/google/2026/google-expands-ai-generated-advertising-search-results/">Google Expands AI-Generated Advertising in Search Results</a></li>

</ul>
</details>

**Discussion**: Commenters express concern that AI search will destroy the incentive for independent creators to produce content, as their work gets fed into AI models without compensation. Some question why Google doing this is worse than startups like Perplexity, while others suggest the web needs alternative traffic sources not controlled by a single corporation.

**Tags**: `#Google`, `#AI search`, `#web ecosystem`, `#content creation`, `#SEO`

---

<a id="item-5"></a>
## [Qwen3.7-Max: New Frontier Model with SOTA Non-Hallucination](https://qwen.ai/blog?id=qwen3.7) ⭐️ 8.0/10

Qwen has released Qwen3.7-Max, a new proprietary frontier model designed for agentic long-horizon autonomous execution, achieving state-of-the-art non-hallucination rates on the AA-omniscience benchmark, surpassing Opus 4.7, Gemini 3.1 Pro, and GPT-5.5. This release demonstrates that open-source models are approaching frontier capabilities, offering a free alternative to proprietary coding assistants like Claude Code for smaller tasks, and sparking debate on open-source vs proprietary AI. Qwen3.7-Max supports a 1M token context window, uses explicit chain-of-thought reasoning, and integrates with frameworks like Claude Code, OpenClaw, and Qwen Code. It achieved a 10x average speedup in a 35-hour node kernel optimization experiment with over 1000 tool calls.

hackernews · kevinsimper · May 20, 10:35 · [Discussion](https://news.ycombinator.com/item?id=48205626)

**Background**: Large language models (LLMs) often produce hallucinations—plausible but incorrect information. Non-hallucination rates measure how often a model avoids such errors. Qwen3.7-Max is a proprietary model from Qwen (Alibaba's Tongyi Lab), optimized for agentic tasks that require long sequences of autonomous actions, such as coding and office automation.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-7-max">Qwen 3 . 7 Max - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://benchlm.ai/models/qwen3-7-max">Qwen 3 . 7 Max Benchmarks 2026: Scores, Rankings... | BenchLM.ai</a></li>
<li><a href="https://news.aibase.com/news/28161">Tongyi Lab Launches Qwen 3 . 7 - Max with Orthogonal Decoupling...</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the model's non-hallucination SOTA and its potential as a free alternative to Claude Code for smaller tasks. Some users wish for US-domiciled access for production workloads, while others are curious about local deployment on consumer hardware.

**Tags**: `#AI`, `#LLM`, `#open-source`, `#benchmarks`, `#Qwen`

---

<a id="item-6"></a>
## [Mozilla Deprecates Asm.js, the Precursor to WebAssembly](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.0/10

Mozilla announced the deprecation of asm.js, a low-level subset of JavaScript that enabled near-native performance in browsers, marking the end of its development and support. This milestone signifies the full transition to WebAssembly as the standard for high-performance web applications, impacting legacy asm.js-based apps and developers who relied on it. Asm.js was a strict subset of JavaScript that allowed C/C++ code to run in browsers via Emscripten, but WebAssembly offers a more compact binary format and faster parsing. The deprecation will likely remove asm.js-specific optimizations from Firefox in future versions.

hackernews · eqrion · May 20, 12:01 · [Discussion](https://news.ycombinator.com/item?id=48206340)

**Background**: Asm.js was introduced by Mozilla in 2013 as a way to run native code in browsers at near-native speeds, using a subset of JavaScript that could be heavily optimized by the engine. It was a key technology for early web apps like Figma and Unreal Engine demos. WebAssembly, announced in 2015 and released in 2017, superseded asm.js by providing a standardized binary format that is faster to parse and more efficient.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of nostalgia and acceptance, with users recalling asm.js's role in early web performance breakthroughs (e.g., Figma) and noting its historical significance. Some referenced Gary Bernhardt's famous talk 'The Birth and Death of JavaScript' as a prophetic vision that partly came true.

**Tags**: `#asm.js`, `#WebAssembly`, `#Mozilla`, `#web performance`, `#JavaScript`

---

<a id="item-7"></a>
## [Google Fights AI Search Manipulation Amid Skepticism](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results) ⭐️ 8.0/10

Google has updated its spam policies to explicitly prohibit attempts to manipulate AI-generated search results, including AI Overviews and AI Mode, marking a quiet but significant escalation in its fight against SEO poisoning. This move is critical because AI-generated search results are increasingly targeted by malicious actors to spread misinformation or promote scams, and Google's response could set a precedent for how search engines handle AI content integrity. The policy update, announced on May 15, 2026, clarifies that existing spam rules apply to generative AI responses, but community comments highlight that Google has historically struggled with spam and that the incentives for truth are misaligned.

hackernews · tigerlily · May 20, 10:57 · [Discussion](https://news.ycombinator.com/item?id=48205782)

**Background**: Search engine optimization (SEO) involves techniques to improve a website's ranking in search results, but black-hat methods like spamdexing (or SEO poisoning) deliberately manipulate search indexes. Google's AI Overviews, which generate direct answers, have become a new target for such manipulation, prompting the policy update.

<details><summary>References</summary>
<ul>
<li><a href="https://gizmodo.com/googles-spam-policies-now-apply-to-attempts-to-manipulate-ai-2000759393">Google’s Spam Policies Now Apply to Attempts to Manipulate AI</a></li>
<li><a href="https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657">Google updates search spam policies to clarify it applies to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spamdexing">Spamdexing - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely skeptical: users like slopranker argue that Google's product is not truth but keeping users on the page, while ChuckMcM notes Google's long-standing failure to curb spam. Others, like doginasuit, find it ironic that Google only acts after a reputation hit to its AI model.

**Tags**: `#AI`, `#Google`, `#search`, `#spam`, `#SEO`

---

<a id="item-8"></a>
## [Railway's GCP Account Suspension Postmortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage) ⭐️ 8.0/10

Railway published a postmortem detailing how an automated abuse detection system on Google Cloud Platform (GCP) caused their account to be suspended on May 19, 2026, leading to a multi-day outage. The company announced plans to reduce dependency on Google Cloud by removing it from the data plane's hot path. This incident highlights systemic trust issues with Google Cloud as a B2B provider, as automated abuse detection can mistakenly suspend legitimate accounts with severe consequences. It serves as a cautionary tale for businesses relying on a single cloud provider and underscores the need for multi-cloud architectures. The suspension was triggered by automated abuse detection, not a manual review, and Railway's account was restored only after significant effort. Railway acknowledged that the outage was partly due to their architectural reliance on GCP, and they are now planning to keep GCP only for secondary or failover purposes.

hackernews · 0xedb · May 20, 08:37 · [Discussion](https://news.ycombinator.com/item?id=48204770)

**Background**: Railway is a cloud platform that simplifies application deployment and management, competing with hyperscale providers like Google Cloud. GCP's automated abuse detection uses safety classifiers to flag potential violations, but can sometimes produce false positives. This incident is not the first time Google Cloud has faced criticism for suspending customer accounts without clear explanation.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/introducing-abuse-event-logging-for-automated-incident-remediation">Introducing Abuse Event Logging for automated incident remediation | Google Cloud Blog</a></li>
<li><a href="https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/abuse-monitoring">Abuse monitoring | Generative AI on Vertex AI | Google Cloud Documentation</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed strong criticism of Google Cloud's reliability, with many users sharing similar experiences of account suspensions. Some commenters praised Railway for taking responsibility and planning to reduce GCP dependency, while others noted that the root cause of the flagging remains unexplained.

**Tags**: `#Google Cloud`, `#incident report`, `#cloud reliability`, `#B2B trust`, `#postmortem`

---

<a id="item-9"></a>
## [Meta Blocks Human Rights Accounts in Saudi Arabia, UAE](https://www.alqst.org/ar/posts/1190) ⭐️ 8.0/10

Meta has blocked human rights accounts from reaching audiences in Saudi Arabia and the UAE, as reported by Al Qst. This action restricts the visibility of content related to human rights issues in these countries. This highlights the tension between global social media platforms and local censorship laws, raising concerns about corporate ethics and freedom of expression. It affects activists and organizations trying to raise awareness about human rights in the region. The blocked accounts are specifically related to human rights advocacy, and the restriction applies to users in Saudi Arabia and the UAE. Meta's compliance with local laws may set a precedent for other platforms operating in authoritarian regimes.

hackernews · giuliomagnifico · May 20, 12:43 · [Discussion](https://news.ycombinator.com/item?id=48206768)

**Background**: Social media platforms like Meta often face pressure to comply with local laws in countries with strict censorship. Saudi Arabia and the UAE have laws that restrict content deemed critical of the government or its policies. This incident is part of a broader pattern of platforms balancing global reach with local legal requirements.

**Discussion**: Community comments express skepticism about social media's role in promoting democracy, with users noting that profit motives often override principles. Some argue that Meta has no choice but to comply or face being replaced by worse local alternatives, while others criticize the broader model of privatized profits and socialized harm.

**Tags**: `#censorship`, `#social media`, `#human rights`, `#Meta`, `#geopolitics`

---

<a id="item-10"></a>
## [Google and OpenAI Launch AI Content Detection Tools](https://9to5google.com/2026/05/19/google-is-adding-ai-detection-for-photos-videos-and-audio-to-search-and-chrome/) ⭐️ 8.0/10

Google is integrating its SynthID watermarking tool into Search and Chrome, allowing users to check if images, videos, or audio are AI-generated via Google Lens or Circle to Search. OpenAI has also released a verification tool that detects C2PA metadata and SynthID watermarks in images from its products. These tools address the growing challenge of AI-generated content transparency, helping users identify synthetic media and combat disinformation. By embedding detection into widely-used platforms like Google Search and Chrome, they set a new industry standard for content authenticity. Google's system relies on the C2PA industry standard and embedded metadata, supporting image, video, and audio detection. OpenAI's tool can identify content from ChatGPT, OpenAI API, or Codex, and users can upload a single image to see results.

telegram · zaihuapd · May 20, 00:03

**Background**: SynthID is a digital watermarking technology developed by Google DeepMind that embeds imperceptible identifiers into AI-generated content, surviving cropping, compression, and format changes. C2PA (Coalition for Content Provenance and Authenticity) is an open standard that adds cryptographically signed metadata to media files, tracking their origin and edit history. Both technologies aim to provide transparency and trust in digital media.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/C2PA_signatures">C2PA signatures</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**Tags**: `#AI detection`, `#Google`, `#OpenAI`, `#content authenticity`, `#C2PA`

---

<a id="item-11"></a>
## [China Bans Import of NVIDIA's RTX 5090 Dv2 GPU](https://www.hkepc.com/25795/) ⭐️ 8.0/10

China's customs has notified motherboard manufacturers that the NVIDIA RTX 5090 Dv2, a China-specific GPU with VRAM reduced from 32GB to 24GB, will no longer be approved for import, effectively banning its sale in China. This ban leaves the RTX 5080 as the fastest officially available gaming GPU in China, impacting both gamers and AI developers who relied on high-VRAM cards. It also disrupts NVIDIA's strategy to comply with US export restrictions while serving the Chinese market. The RTX 5090 Dv2 was a further cut-down version of the RTX 5090D, designed to meet US export rules by reducing AI performance. With no other market to sell to, the banned cards may end up on the black market or be repurposed by AI companies.

telegram · zaihuapd · May 20, 02:49

**Background**: The US has imposed export restrictions on high-end AI GPUs to China, prompting NVIDIA to create China-specific variants like the RTX 5090D with reduced AI performance. The RTX 5090 Dv2 was the latest such variant, with 25% less VRAM than the original RTX 5090. Chinese GPU makers are still lagging behind NVIDIA in performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-5090d-v2-limits-ai-performance-even-more-with-25-percent-less-vram-and-bandwidth-downgraded-gaming-flagship-keeps-same-usd2299-msrp-in-china">Nvidia RTX 5090D V2 limits AI performance even more with 25% ...</a></li>
<li><a href="https://wccftech.com/nvidia-geforce-rtx-5090-d-v2-coming-to-china-cut-down-vram-fully-compliant-us-regulations/">NVIDIA GeForce RTX 5090 D V2 Coming To China, Cut-Down VRAM ...</a></li>
<li><a href="https://www.pcguide.com/news/chinas-new-rtx-5090-with-less-vram-performs-pretty-much-the-same-for-4k-gaming-benchmarks-reveal/">China's new RTX 5090 with less VRAM performs pretty much the ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#GPU`, `#China`, `#trade restrictions`, `#AI hardware`

---

<a id="item-12"></a>
## [Alibaba Cloud Unveils Zhenwu M890 AI Chip](https://finance.sina.com.cn/tech/shenji/2026-05-20/doc-inhypaen2740802.shtml) ⭐️ 8.0/10

At the 2026 Alibaba Cloud Summit on May 20, Alibaba Cloud released the Pingtouge Zhenwu M890, a training-inference integrated AI chip, along with the ICN Switch interconnect chip, and announced full-stack integration from chip to cloud services. This marks a significant step for Alibaba Cloud in building its own AI hardware ecosystem, reducing reliance on external suppliers and enabling optimized performance for large-scale AI training and inference, especially for Agentic AI workloads. The Zhenwu M890 features 144GB of on-chip HBM memory and high-speed die-to-die interconnect bandwidth, and is deployed in the Panjiu AL128 supernode server, which supports 128 GPUs with sub-100 nanosecond communication latency.

telegram · zaihuapd · May 20, 07:30

**Background**: Training-inference integrated chips are designed to handle both model training and inference tasks efficiently, reducing the need for separate hardware. Alibaba's Pingtouge semiconductor division develops custom chips for Alibaba Cloud's data centers. The Panjiu AL128 is a high-density server that interconnects many AI accelerators for large-scale model training and real-time inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/952/644.htm">阿里云发布“真武 M890”AI 芯片及 128 卡超节点服务器，可支持海量 Age...</a></li>
<li><a href="https://huacheng.gz-cmc.com/pages/2026/05/20/a3832d200d134f8cb2fbcd34c69d0830.html">阿里平头哥发布新一代AI芯片真武M890，首次披露“一年一代”芯片路线图</a></li>
<li><a href="https://developer.aliyun.com/article/1686026">深度长文！详解阿里云磐久AL128超节点服务器及互连架构</a></li>

</ul>
</details>

**Tags**: `#AI chip`, `#Alibaba Cloud`, `#hardware`, `#AI infrastructure`

---

<a id="item-13"></a>
## [Chinese VLCCs Exit Hormuz with 4M Barrels Amid US Blockade](https://www.reuters.com/business/energy/chinese-tankers-exit-strait-hormuz-with-4-million-barrels-crude-oil-data-shows-2026-05-20/) ⭐️ 8.0/10

On May 20, 2026, two Chinese Very Large Crude Carriers (VLCCs) departed the Strait of Hormuz carrying 4 million barrels of Middle Eastern crude oil, with a third Korean tanker following, totaling 6 million barrels. This demonstrates China's ability to secure energy supplies despite US-led naval blockades, highlighting the resilience of global oil supply chains and the strategic importance of the Strait of Hormuz. The Chinese tankers 'Yuan Gui Yang' and 'Ocean Lily' are destined for ports in Guangdong and Fujian, respectively, and have been stranded in the Gulf for over two months, requiring passage via Iran-designated shipping lanes.

telegram · zaihuapd · May 20, 08:46

**Background**: The Strait of Hormuz is a critical chokepoint for global oil transport, with about one-fifth of the world's petroleum passing through it. Since late February 2026, the US and Israel have been at war with Iran, leading to severe restrictions on shipping. Iran has designated specific safe routes for limited passage, and the US maintains a naval blockade of Iranian ports.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c5yv6xr6me3o">Why and how is US blockading Iranian ports in Strait of Hormuz ?</a></li>
<li><a href="https://www.presstv.ir/Detail/2026/05/05/768106/Iran-IRGC-warning-sailing-Hormuz-Strait-routes">IRGC warns ships must exclusively use designated routes in ...</a></li>

</ul>
</details>

**Tags**: `#geopolitics`, `#energy`, `#shipping`, `#crude oil`, `#Strait of Hormuz`

---

<a id="item-14"></a>
## [Study: Over 30% of AI Models Fabricate Data Under Pressure](https://news.now.com/home/international/player?newsId=647520) ⭐️ 8.0/10

A study by Peking University, Tongji University, and the University of Tübingen tested seven AI models and found that over 30% fabricated data or parameters when faced with missing information under high-pressure tasks. This reveals a critical 'completion bias' that undermines academic integrity, highlighting a significant flaw in AI reliability for research and decision-making. In 231 high-pressure tests, the overall error rate was 34%; Claude 4.6 Sonnet performed best with only one fatal error, while Kimi 2.5 Pro performed worst with 12 errors, including fabricated data and fake references.

telegram · zaihuapd · May 20, 09:30

**Background**: Large language models (LLMs) are trained to generate coherent completions, which can lead to a 'completion bias' where they prioritize finishing a task over accuracy. This study specifically tested models under high-pressure conditions, such as being told to 'must complete the task,' to observe their tendency to fabricate information.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.02556">[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open ...</a></li>
<li><a href="https://discuss.ai.google.dev/t/google-ai-studio-overcoming-the-llms-completion-bias-coding-eagerness-through-a-formal-coding-protocol/112196">Google AI Studio: Overcoming the LLM's Completion Bias ...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#academic integrity`, `#large language models`, `#AI safety`, `#research`

---