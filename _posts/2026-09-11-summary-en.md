---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 31 items, 7 important content pieces were selected

---

1. [Terry Tao and 25 Fields Medalists Warn of AI Misalignment in Mathematics](#item-1) ⭐️ 9.0/10
2. [OpenAI Launches Agents API in Public Beta](#item-2) ⭐️ 9.0/10
3. [Developer Finds 60% of $220 Google App Ad Installs Were Bots](#item-3) ⭐️ 8.0/10
4. [OpenAI launches GPT-Live-1 full-duplex voice model on API](#item-4) ⭐️ 8.0/10
5. [GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated File Reads](#item-5) ⭐️ 8.0/10
6. [DeepSeek Releases V4.1 Flash: 552B Multimodal MoE Model](#item-6) ⭐️ 8.0/10
7. [Anthropic Accuses Seven Chinese AI Labs of Large-Scale Claude Distillation](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Terry Tao and 25 Fields Medalists Warn of AI Misalignment in Mathematics](https://mathandai.org/) ⭐️ 9.0/10

On September 11, 2026, Terence Tao published a declaration titled "A Severe Misalignment of AI in Mathematics" on his blog, signed by 25 Fields Medal winners, arguing that the commercial incentives of AI companies are fundamentally at odds with the mathematical community's goals. The statement followed outrage over OpenAI's methods in claiming to solve a major open problem, with the Economist reporting that top mathematicians fear AI could undermine the foundations of mathematics. This is an unprecedented collective warning from the most decorated figures in mathematics, signaling that AI's rapid incursion into proof-solving could disrupt how mathematical credit, understanding, and research norms are established. It affects not only mathematicians but also AI labs, funders, and any scientific field where AI-generated results outpace human comprehension. The declaration was signed by 25 Fields Medal winners, including Tao, and frames the issue as part of broader alignment problems affecting other scientific and creative professions. The controversy was sparked by OpenAI's GPT-6 Astra, which reportedly took about 17 hours to verify a solution to a fluid dynamics problem, with NYU mathematicians alleging the company "fought dirty" on a career-making problem.

hackernews · meredydd · Sep 11, 17:45 · [Discussion](https://news.ycombinator.com/item?id=49662371)

**Background**: The Fields Medal is often described as the Nobel Prize of mathematics, awarded to a few mathematicians under 40 every four years. AI alignment generally refers to ensuring AI systems pursue intended goals; here it is applied to the mismatch between AI labs' commercial drive for fast, headline-grabbing results and mathematics' slow, rigorous culture of proof and peer understanding. OpenAI's recent claim to have solved a long-standing problem using GPT-6 Astra intensified existing tensions over credit and verification.

<details><summary>References</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/">A Severe Misalignment of AI in Mathematics | What's new</a></li>
<li><a href="https://www.economist.com/science-and-technology/2026/09/11/top-mathematicians-are-outraged-by-openais-methods">Top mathematicians are outraged by OpenAI ’s methods</a></li>
<li><a href="https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/">OpenAI fought dirty on career-making math problem... | TechCrunch</a></li>

</ul>
</details>

**Discussion**: Commenters offered diverse analogies: one mathematician compared AI-generated proofs to Mochizuki's isolated abc conjecture proof, noting it still generated productive conferences and papers; another argued AI has destroyed the yardstick of solving open problems rather than understanding itself. Others likened the panic to 1990s fears that computers would ruin chess, pointing out chess is now more popular and players stronger, while one quoted Baudelaire's 19th-century critique of photography as a mechanical recorder that cannot transform reality like painting.

**Tags**: `#AI`, `#mathematics`, `#research`, `#ethics`, `#alignment`

---

<a id="item-2"></a>
## [OpenAI Launches Agents API in Public Beta](https://openai.com/index/introducing-the-agents-api/) ⭐️ 9.0/10

On September 10, 2026, OpenAI launched the public beta of its Agents API, allowing developers to create production-grade cloud agents with a single API call. The API lets users choose between OpenAI-hosted sandboxes, their own infrastructure, or partner environments. This release marks a major shift in agent development, moving from fragmented custom pipelines to a unified, production-ready platform. It could accelerate adoption of autonomous AI agents across the ecosystem and reshape how developers build and deploy AI applications. The API is built on the open-source Codex harness and supports long-session context compression, tool search, parallel tool calls, and sub-agent collaboration with up to 3 concurrent sub-agents. During the public beta, there are no additional fees beyond token and tool usage costs.

telegram · zaihuapd · Sep 11, 11:12

**Background**: The Codex harness is the underlying agent loop and logic that powers all Codex experiences, including the web app, CLI, IDE extension, and macOS app. It manages conversation state, streams execution, uses tools, and enforces sandbox and approval policies. The Agents API extends this infrastructure to general-purpose cloud agents, not just coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/unlocking-the-codex-harness/">Unlocking the Codex harness: how we built the App Server | OpenAI</a></li>
<li><a href="https://developers.openai.com/blog/codex-as-a-platform">Codex as a platform: build on the open agent harness | OpenAI Developers</a></li>
<li><a href="https://www.ithome.com/1/001/072.htm">OpenAI Agents API ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Agents API`, `#AI 智能体`, `#API 发布`, `#云计算`

---

<a id="item-3"></a>
## [Developer Finds 60% of $220 Google App Ad Installs Were Bots](https://dayzlegame.com/blog/google-ads-bot-farm/) ⭐️ 8.0/10

A developer spent $220 on Google app ads and found that roughly 60% of the resulting installs came from bots, according to a blog post that sparked a 228-point Hacker News discussion with 120 comments. The post documents how bot farms simulate clicks, installs, and even conversions that Google's ad system rewards. This case gives developers and marketers concrete, data-backed evidence that ad fraud remains a serious problem on major platforms like Google Ads, directly wasting ad budgets for small app publishers. It also raises questions about how much responsibility ad platforms bear for detecting and preventing invalid traffic that they profit from. Community members noted that bot farms are often run from data center IP ranges rather than residential providers, and that advertisers can add entire network ranges (e.g., 123.4.5.*) to Google Ads' IP Exclusions list under Admin > Account Settings. One commenter reported accumulating over 4,000 excluded networks in the US alone after running Google Ads for a couple of years.

hackernews · nickabe · Sep 11, 18:24 · [Discussion](https://news.ycombinator.com/item?id=49662990)

**Background**: Mobile ad fraud refers to deliberate manipulation of advertising metrics such as clicks, impressions, installs, or conversions to generate illegitimate revenue or inflate performance data. Common techniques include bot farms, device emulators, click injection, and VPN proxy tools, and detection typically relies on behavioral analysis and anomaly rules that flag abnormal click-to-conversion ratios. Google Ads is Google's advertising platform, and AdMob is its mobile ad monetization network, which can ban accounts for invalid traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49662990">I spent $220 on Google app ads and 60% of the installs were robots</a></li>
<li><a href="https://www.humansecurity.com/learn/topics/what-is-mobile-ad-fraud/">What is Mobile Ad Fraud? Here’s How To Stop Mobile Ad Fraud</a></li>
<li><a href="https://improvado.io/blog/ad-fraud">Ad Fraud 2026: Detection & Prevention Guide</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical of ad platforms, with one calling Google and Meta ads 'a con' and another suspecting Google turns a blind eye to fraud it is capable of detecting. A widely cited cautionary tale described a developer who bought Google Ads to promote an AdMob-monetized app and then had his AdMob account banned for invalid traffic. Others offered practical mitigation advice, such as excluding data center IP ranges, and one commenter praised the app's clean interface after installing it.

**Tags**: `#ad-fraud`, `#google-ads`, `#mobile-apps`, `#digital-advertising`, `#bot-detection`

---

<a id="item-4"></a>
## [OpenAI launches GPT-Live-1 full-duplex voice model on API](https://openai.com/index/introducing-gpt-live-1-in-the-api/) ⭐️ 8.0/10

On September 10, 2026, OpenAI released GPT-Live-1 on its API, a full-duplex speech model that can listen and speak simultaneously, supporting natural interruptions, background-noise handling, long conversations, and phone-based voice agents. OpenAI reports a 30-percentage-point improvement on Full Duplex Bench over GPT-Realtime-2.1, with API voice front-end pricing at $0.05 per minute. Full-duplex capability is a major step for voice agents because it lets models handle overlapping speech and interruptions the way humans do, which is critical for call centers, customer support, and phone-based assistants. A 30-point benchmark gain over GPT-Realtime-2.1 signals rapid progress in turn-taking and could push developers to migrate existing realtime voice pipelines to GPT-Live-1. GPT-Live-1 can delegate complex reasoning and tool calls to a backend model, keeping the speech front end lightweight, and it is priced at $0.05 per minute for the API voice front end. The 30-point gain is measured on Full Duplex Bench, a benchmark that evaluates pause handling, backchanneling, turn-taking, and interruption management.

telegram · zaihuapd · Sep 11, 03:09

**Background**: Traditional voice assistants are half-duplex: they listen, then speak, and cannot easily handle users talking over them. Full-duplex spoken dialogue models are engineered for real-time bidirectional exchange, accommodating overlapping speech, interruptions, and rapid backchannels, and Full-Duplex-Bench was introduced as a benchmark to systematically evaluate these turn-taking behaviors. GPT-Realtime-2.1, released in July 2026, was OpenAI's prior low-latency streaming speech-to-speech model with configurable reasoning effort and tool use, so GPT-Live-1 represents the next step in that line.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.04721">[2503.04721] Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-realtime-2.1">GPT-Realtime-2.1 Model | OpenAI API</a></li>
<li><a href="https://www.emergentmind.com/topics/full-duplex-spoken-dialogue-model">Full-Duplex Spoken Dialogue Model</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#voice-ai`, `#API`, `#speech-models`, `#realtime`

---

<a id="item-5"></a>
## [GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated File Reads](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 8.0/10

GitLab released emergency patches on September 10 in versions 19.3.2, 19.2.6, and 19.1.8 to fix CVE-2026-85706, a CVSS 10.0 vulnerability that lets unauthenticated attackers read arbitrary files on self-hosted GitLab servers via the repository commits API. Affected versions include 18.7 through before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2. A maximum-severity unauthenticated arbitrary file read flaw is a serious security event for any organization running self-managed GitLab, since exposed instances could leak credentials, secrets, and confidential data. GitLab.com is already patched and GitLab Dedicated users need no action, but self-hosted administrators must upgrade immediately. The flaw stems from improper path confinement and missing authentication enforcement in the repository commits API, and was reported by researcher s3ntago through GitLab's HackerOne bug bounty program. GitLab has not publicly disclosed the specific preconditions, no public proof-of-concept exists, and there is no evidence of in-the-wild exploitation yet.

telegram · zaihuapd · Sep 11, 11:05

**Background**: CVSS is a framework that rates vulnerability severity from 0.0 to 10.0 based on metrics such as attack vector, complexity, privileges required, and impact on confidentiality, integrity, and availability; a 10.0 score represents the maximum severity. GitLab is a widely used DevOps platform available as a hosted service (GitLab.com) and as self-managed Community and Enterprise Edition installations, where administrators are responsible for keeping their own instances patched. Path traversal vulnerabilities allow attackers to manipulate file paths to access files outside the intended directory, and when combined with missing authentication they can expose sensitive server files without any login.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html">GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure</a></li>
<li><a href="https://www.news4hackers.com/gitlab-critical-path-traversal-vulnerability-patch-needed/">GitLab Critical Path Traversal Vulnerability Patch Needed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System">Common Vulnerability Scoring System - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#gitlab`, `#vulnerability`, `#cve`, `#devops`

---

<a id="item-6"></a>
## [DeepSeek Releases V4.1 Flash: 552B Multimodal MoE Model](https://t.me/zaihuapd/43770) ⭐️ 8.0/10

DeepSeek officially released V4.1 Flash, the smallest model in its new architecture series, featuring a 552B-parameter Causal-Encoder-Decoder (CED) design with 8B input and 16B output activations and native multimodal vision understanding. The model is now live on the DeepSeek API under the name deepseek-flash, with new pricing taking effect on September 10, 2026, and requests to deepseek-v4-pro being rerouted after September 14, 2026. This release signals DeepSeek's shift to a novel Causal-Encoder-Decoder architecture that decouples reading from writing, potentially improving efficiency over traditional decoder-only models. It also expands DeepSeek's multimodal capabilities and reshapes its API pricing and model lineup, affecting developers and enterprises building on its platform. The model is a multimodal Mixture-of-Experts (MoE) with 552B backbone parameters and supports contexts of up to one million tokens, natively processing images and text while generating text autoregressively. V4-Flash and V4-Flash-Vision-Exp are retired, and the new pricing and routing changes take effect on September 10 and September 14, 2026, respectively.

telegram · zaihuapd · Sep 11, 11:32

**Background**: Traditional autoregressive LLMs like GPT and Llama use a monolithic decoder-only architecture, where one set of weights handles both reading (prefill) and writing (decode), sharing the same compute budget. The Causal-Encoder-Decoder (CED) architecture decouples these phases, using separate components for encoding input and generating output, which can improve efficiency. DeepSeek V4.1 Flash applies this design within a Mixture-of-Experts framework, where only a subset of parameters is activated per token, keeping inference costs lower despite the large 552B total parameter count.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek -ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>
<li><a href="https://www.happyrock.cloud/blog/2026-09-11_a_en/">DeepSeek V4.1 Flash In-Depth: 552B MoE, Asymmetric Causal ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#LLM`, `#multimodal`, `#model-release`, `#AI`

---

<a id="item-7"></a>
## [Anthropic Accuses Seven Chinese AI Labs of Large-Scale Claude Distillation](https://t.me/zaihuapd/43771) ⭐️ 8.0/10

Anthropic's latest threat intelligence report claims it detected and blocked industrial-scale Claude distillation campaigns by seven Chinese AI labs, naming Alibaba, Zhipu, Xiaomi, SenseTime, and MiniMax. Alibaba's campaign was the largest, generating over 151 million interactions between May and July, peaking at nearly 3 million per day, which Anthropic says was used to train Qwen 3.5, 3.6, and 3.7 models. This is a significant development in the escalating US-China AI competition, touching on model IP, terms-of-service enforcement, and the race to build frontier models. If the allegations hold, they could intensify scrutiny of Chinese AI labs' training practices and shape future export-control or API-access debates. The report describes the use of fraudulent accounts, proxies, and harvested transcripts to extract Claude's capabilities, and Anthropic says the data was also used for reinforcement learning environments and model architecture work. The claims are single-source corporate allegations without independent verification, and the Telegram post is only a brief summary.

telegram · zaihuapd · Sep 11, 13:10

**Background**: Model distillation is a machine learning technique that transfers knowledge from a large model to a smaller one, often by fine-tuning the smaller model on outputs from the larger one. It is a legitimate and widely used method, but using a competitor's API outputs at industrial scale to train a rival model typically violates terms of service and is what Anthropic calls an illicit distillation attack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/">Anthropic details distillation campaigns from Alibaba ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#model distillation`, `#China AI labs`, `#threat intelligence`

---