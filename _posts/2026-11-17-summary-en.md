---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 36 items, 7 important content pieces were selected

---

1. [vLLM v0.34.0: Extensible KV Cache Default, Model Runner V1 Removed, Big Speedups](#item-1) ⭐️ 8.0/10
2. [Carnegie Mellon launches CS Learn, free CS lectures on YouTube](#item-2) ⭐️ 8.0/10
3. [Optimizely CDN Compromised, Serves Malware on Zoom and GitLab](#item-3) ⭐️ 8.0/10
4. [Jiff 1.0: A New Datetime Library for Rust](#item-4) ⭐️ 8.0/10
5. [US Commerce Department to finalize rule closing remote AI chip access loophole for Chinese firms](#item-5) ⭐️ 8.0/10
6. [Shandong University Team Claims First Conditional Proof of Goldbach's Conjecture](#item-6) ⭐️ 8.0/10
7. [Alibaba, Moonshot and other Chinese AI firms curb offensive cyber capabilities in new models](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.34.0: Extensible KV Cache Default, Model Runner V1 Removed, Big Speedups](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 was released with 1,061 commits from 412 contributors, introducing 10 new models, enabling the extensible KV cache by default, removing Model Runner V1, and delivering up to 1.95x decode speedups on Blackwell and MI355X hardware. This release significantly improves throughput and performance for LLM inference, especially on newer hardware, and simplifies the codebase by making Model Runner V2 the only GPU runner, which impacts anyone deploying LLMs with vLLM. The default block size is now 64 (was 16), ROCm 7.2 artifacts are dropped in favor of ROCm 10.0, and huggingface_hub >= 2.0.0 is required; the extensible KV cache sizes from actual free memory after warmup, which can increase per-token decode latency by 6-18% on some models at high concurrency.

github · khluu · Nov 16, 23:22

**Background**: vLLM is a high-throughput LLM inference engine that uses PagedAttention and a KV cache to efficiently serve large language models. Model Runner V2 is a modular reimplementation of the execution core, and the extensible KV cache dynamically sizes the cache based on available GPU memory to maximize throughput. Blackwell and MI355X are NVIDIA and AMD's latest GPU architectures for AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V 2 : A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>
<li><a href="https://gpuadvisor.com/mi355x-vs-gb200">MI355X vs GB200 — AMD vs NVIDIA Inference Comparison 2026 ...</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#model-serving`, `#performance-optimization`, `#release`

---

<a id="item-2"></a>
## [Carnegie Mellon launches CS Learn, free CS lectures on YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 8.0/10

Carnegie Mellon University's Griffin School of Computer Science launched CS Learn, releasing full semesters of lectures from current CMU computer science courses for free on YouTube, with one course premiering each day this week and more courses coming in January. This is a significant open-education development because it provides free access to high-quality, current CMU course lectures, potentially benefiting learners worldwide and complementing existing open courseware initiatives like MIT OpenCourseWare. The initiative is run by Phillip Compeau, a teaching professor at CMU, and some students built tools to automate production; courseware including projects and feedback mechanisms is planned for the future.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**Background**: Open courseware initiatives like MIT OpenCourseWare have made course materials freely available online for decades. CS Learn follows this tradition by offering full-semester lectures from current CMU courses on YouTube, making high-quality computer science education accessible to anyone with internet access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://en.wikipedia.org/wiki/MIT_OpenCourseWare">MIT OpenCourseWare - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community response is highly positive, with the creator participating and commenters discussing the value of fundamentals in the AI era, requesting specific courses, and emphasizing the need for projects and feedback to complement lectures.

**Tags**: `#education`, `#computer-science`, `#open-courseware`, `#CMU`, `#YouTube`

---

<a id="item-3"></a>
## [Optimizely CDN Compromised, Serves Malware on Zoom and GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely, a widely used A/B testing and experimentation platform, was compromised, causing its CDN to serve malicious JavaScript on customer websites including Zoom and GitLab. The attack affected Optimizely's own sites as well, with snippets for www.optimizely.com and login.optimizely.com carrying the malicious code. This supply-chain incident highlights the systemic risk of third-party scripts, where a single compromised vendor can inject malware into thousands of major websites, affecting millions of users. It underscores the urgent need for stronger security controls and accountability in the third-party script ecosystem. Optimizely's CDN served exactly what it was given, indicating the compromise occurred at Optimizely's origin rather than through CDN cache poisoning. The exact method by which attackers gained write access to so many customer projects remains unknown, whether via a compromised Optimizely system or a credential with cross-customer access.

hackernews · kristjansson · Nov 16, 23:00 · [Discussion](https://news.ycombinator.com/item?id=50524767)

**Background**: Optimizely is a popular platform for A/B testing and web experimentation, allowing marketing teams to modify website content without engineering involvement. Websites often embed Optimizely's JavaScript snippet, which loads further scripts from Optimizely's CDN, creating a supply-chain dependency. Third-party scripts are commonly used for analytics, advertising, and personalization, but they expand the attack surface because any compromise of the script provider can affect all customer sites.

<details><summary>References</summary>
<ul>
<li><a href="https://alickaj.eu/?read=why-unmanaged-third-party-scripts-put-your-website-at-risk">Why Unmanaged Third - Party Scripts Put Your Website at Risk — AEU</a></li>
<li><a href="https://betanews.com/article/the-rise-of-third-party-browser-script-attacks-qa/">The rise of third - party browser script attacks [Q&A] - BetaNews</a></li>
<li><a href="https://suriq.io/blog/brevo-cdn-edge-supply-chain-attack">Brevo Supply - Chain Hack: Malware Injected at the CDN Edge</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration over the lack of accountability and the risks of third-party scripts, with some blaming the trend of giving marketing departments easy tag-adding abilities via tools like Google Tag Manager. Others suggested mitigations such as NoScript and argued that large sites should implement stricter controls or self-host vendor scripts.

**Tags**: `#security`, `#supply-chain`, `#web`, `#javascript`, `#optimizely`

---

<a id="item-4"></a>
## [Jiff 1.0: A New Datetime Library for Rust](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Andrew Gallant (burntsushi) has released Jiff 1.0, a new datetime library for Rust that aims to improve upon existing libraries like chrono by providing a thoughtful API that automatically handles common problems such as daylight saving time. Jiff 1.0 is a significant milestone for the Rust ecosystem, as it offers a modern alternative to chrono with a focus on correctness and usability, and its author is a respected developer known for high-quality libraries like regex and ripgrep. Jiff integrates seamlessly with the Time Zone Database, supports DST-aware arithmetic and rounding, and allows lossless formatting and parsing of zone-aware datetimes; it also mentions handling of time scales like TAI, though other scales like UT1 may require manual handling.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**Background**: Rust's datetime handling has long been dominated by the chrono crate, which, while stable, has faced criticism for its API design. Jiff aims to provide a more ergonomic and safer alternative by putting time zone handling front and center, making it difficult to misuse. The library is authored by Andrew Gallant, a prominent Rust developer known for creating widely-used crates such as regex and ripgrep.

<details><summary>References</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant's Blog</a></li>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/chrono/latest/chrono/">chrono - Rust - Docs.rs</a></li>

</ul>
</details>

**Discussion**: The community discussion is highly positive, with a former chrono maintainer expressing gratitude for Jiff and sharing insights about API stability and burnout. Others appreciate Jiff's honest acknowledgment of its limitations and hope for wider adoption over chrono, while some raise technical questions about handling various time scales like TAI and UT1.

**Tags**: `#Rust`, `#datetime`, `#library`, `#API design`, `#time scales`

---

<a id="item-5"></a>
## [US Commerce Department to finalize rule closing remote AI chip access loophole for Chinese firms](https://t.me/zaihuapd/45161) ⭐️ 8.0/10

The U.S. Commerce Department is finalizing a rule that would block Chinese AI companies from remotely accessing advanced AI chips through overseas data centers, with publication possible as early as this month. The rule extends existing semiconductor export restrictions to seven Southeast Asian countries, including Malaysia, Singapore, and Thailand, to close remote-access and chip-smuggling loopholes. This rule closes a major loophole that allowed Chinese AI firms to bypass U.S. export controls by using advanced Nvidia chips hosted in third countries, potentially disrupting the global AI infrastructure access model. It could significantly impact Chinese AI companies like ByteDance and Alibaba, as well as data center operators in Southeast Asia, and reshape global chip supply chains. The rule, reportedly an interim final rule from the Commerce Department's Bureau of Industry and Security (BIS), adds destination-based license requirements for exports to Indonesia, Malaysia, Singapore, Thailand, and Brazil, and includes restrictions on commingled items. Nvidia had lobbied against closing the remote-access gap, arguing that U.S. AI infrastructure needs to win globally.

telegram · zaihuapd · Nov 16, 14:44

**Background**: U.S. export controls on advanced AI chips, such as Nvidia's high-end GPUs, are designed to prevent China from obtaining technology that could enhance its military and AI capabilities. However, Chinese companies have been able to remotely access such chips hosted in data centers located in third countries, circumventing the restrictions. The new rule aims to close this 'remote access loophole' by extending controls to additional countries and imposing license requirements on data center operators.

<details><summary>References</summary>
<ul>
<li><a href="https://gizmodo.com/trump-admin-moves-to-strangle-chinas-remote-access-to-american-ai-chips-2000840511">Trump Admin Moves to Strangle China's Remote Access to American...</a></li>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China's Access To Advanced Chips Via Singapore ...</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2026/11/16/us-closes-loophole-that-allowed-china-to-remotely-access-nvidia-chips/">US Closes Loophole That Allowed China To Remotely Access ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#export controls`, `#US-China tech`, `#semiconductor policy`, `#AI infrastructure`

---

<a id="item-6"></a>
## [Shandong University Team Claims First Conditional Proof of Goldbach's Conjecture](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 8.0/10

A team from Shandong University, Jia-Min Li and Jianya Liu, has posted a paper claiming the first conditional proof that every sufficiently large even number is the sum of two primes, assuming the generalized Riemann hypothesis for Dirichlet L-functions and one of two additional spectral hypotheses. The proof also asserts that the two primes lie between one-third and two-thirds of the even number. This is a significant development because it covers all sufficiently large even numbers, unlike previous results that only handled almost all even numbers or required stronger unproven assumptions. It could stimulate new approaches in analytic number theory, although the reliance on unproven hypotheses means it is not an unconditional proof of Goldbach's conjecture. The proof is conditional: it assumes the generalized Riemann hypothesis for Dirichlet L-functions plus one of two additional spectral hypotheses, and the authors note that GRH alone is insufficient. The method is novel and differs from the classical sieve and circle methods, but the paper has not yet undergone peer review and the source is a brief summary.

telegram · zaihuapd · Nov 16, 16:01

**Background**: Goldbach's conjecture states that every even integer greater than 2 is the sum of two primes; it has been verified up to 4×10^18 but remains unproven. The generalized Riemann hypothesis extends the Riemann hypothesis to Dirichlet L-functions, asserting that all their nontrivial zeros lie on the critical line Re(s)=1/2. Spectral hypotheses are assumptions about the eigenvalues of certain operators, often motivated by connections between number theory and spectral analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Goldbach's_conjecture">Goldbach's conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#number-theory`, `#Goldbach-conjecture`, `#research`, `#conditional-proof`

---

<a id="item-7"></a>
## [Alibaba, Moonshot and other Chinese AI firms curb offensive cyber capabilities in new models](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 8.0/10

Alibaba, Tencent, and Moonshot AI have deliberately reduced offensive cyber capabilities in their latest models while improving defensive performance, with Alibaba's new flagship Qwen released without open weights so users cannot download and customize the full version. Tencent reportedly trimmed cyber functions before releasing its Hy4 model this month. This marks a notable intersection of AI safety, cybersecurity, and policy, as China's top AI labs proactively limit dual-use cyber capabilities in response to draft export control rules. It could reshape how frontier models are released in China and set a precedent for capability restriction by model providers rather than regulators alone. The move is tied to a draft export control regulation published by China's Ministry of Commerce last month that would ban exports of AI tools capable of attacking critical infrastructure and government networks. Alibaba's decision to keep its flagship Qwen closed-weight is a departure from its historically open model strategy, though the report does not detail specific capability benchmarks.

telegram · zaihuapd · Nov 17, 02:20

**Background**: Open-weight models are those whose trained parameters can be downloaded and run locally, offering cost savings and data control but also enabling unrestricted fine-tuning; Qwen has been one of the most widely downloaded open model families. Moonshot AI's Kimi models, such as the open-weight Kimi K3, are known for agentic and coding capabilities. China's draft export controls sort AI technology into prohibited, restricted, automatic-licence, and uncovered categories, covering model weights, agents, and chip clusters while reportedly exempting APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aighten.com/en/blog/china-ai-export-controls-draft-models-agents-chips">China AI Export Controls Draft : Models, Agents and Chips</a></li>
<li><a href="https://www.swarchitect.net/en/china-ai-export-controls-2026-10/">China AI Export Draft Spares APIs, Not Foreign Installs · SW Architect</a></li>
<li><a href="https://www.secondtalent.com/resources/every-qwen-ai-model-explained-compared/">Every Qwen AI Model Explained and Compared (Nov, 2026)</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#cybersecurity`, `#AI regulation`, `#China tech`, `#export controls`

---