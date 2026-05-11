---
layout: default
title: "Horizon Summary: 2026-05-11 (EN)"
date: 2026-05-11
lang: en
---

> From 28 items, 8 important content pieces were selected

---

1. [TanStack NPM Packages Compromised in Supply Chain Attack](#item-1) ⭐️ 9.0/10
2. [Nvidia Releases Official Rust-to-CUDA Compiler](#item-2) ⭐️ 9.0/10
3. [Software engineering may no longer be a lifetime career](#item-3) ⭐️ 8.0/10
4. [James Shore: AI Coding Agents Must Cut Maintenance Costs](#item-4) ⭐️ 8.0/10
5. [Zombie Internet: AI Content Overwhelms Human Web](#item-5) ⭐️ 8.0/10
6. [Shopify's River AI Agent Fosters Learning Culture](#item-6) ⭐️ 8.0/10
7. [NYT Corrects AI-Hallucinated Quote in Article](#item-7) ⭐️ 8.0/10
8. [Fake OpenAI Privacy Filter Repo Tops Hugging Face Charts](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TanStack NPM Packages Compromised in Supply Chain Attack](https://github.com/TanStack/router/issues/7383) ⭐️ 9.0/10

On April 29, 2026, four malicious versions (2.0.4 to 2.0.7) of the fake 'tanstack' npm package were published, containing a token-stealing payload and a destructive dead-man's switch that wipes the home directory if the stolen token is revoked. This attack targets widely-used TanStack packages and demonstrates how supply chain attacks can bypass existing security measures, potentially compromising many downstream projects and user credentials. The payload installs a systemd user service or LaunchAgent that polls GitHub API every 60 seconds with the stolen token; if the token is revoked, it executes 'rm -rf ~/'. The malicious commit originated from a fork, exploiting GitHub's shared object storage.

hackernews · varunsharma07 · May 11, 21:08 · [Discussion](https://news.ycombinator.com/item?id=48100706)

**Background**: Supply chain attacks target software dependencies by injecting malicious code into legitimate packages. NPM packages often run install scripts automatically, which can be exploited to execute arbitrary commands. The dead-man's switch mechanism ensures the attack persists even after token revocation, causing maximum damage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/fake-tanstack-packages-steal-env-files">Four published versions of a fake " tanstack " package uploaded in 27...</a></li>
<li><a href="https://socket.dev/npm/package/tanstack">tanstack - npm Package Security Analysis - Socket</a></li>

</ul>
</details>

**Discussion**: Community members warn about the dead-man's switch and advise caution when revoking tokens. Some argue that Trusted Publishing alone is insufficient, and recommend using pnpm with strict settings to disable postinstall scripts. Others criticize GitHub for allowing malicious fork commits to be reachable via the same URI as the legitimate repo.

**Tags**: `#supply chain security`, `#npm`, `#malware`, `#open source`, `#security`

---

<a id="item-2"></a>
## [Nvidia Releases Official Rust-to-CUDA Compiler](https://nvlabs.github.io/cuda-oxide/index.html) ⭐️ 9.0/10

Nvidia Labs has released cuda-oxide 0.1, an experimental Rust-to-CUDA compiler that compiles standard Rust code directly to PTX, enabling GPU kernel development in Rust without DSLs or foreign language bindings. This marks the first official Nvidia tool for writing CUDA kernels in Rust, potentially bringing Rust's memory safety and modern language features to GPU programming while reducing reliance on C++ and complex build systems. The compiler uses a custom rustc codegen backend and supports single-source compilation where host and device code coexist in the same file, built with a single cargo oxide build command. It is currently experimental and targets SIMT GPU kernels.

hackernews · adamnemecek · May 11, 15:55 · [Discussion](https://news.ycombinator.com/item?id=48096692)

**Background**: CUDA is Nvidia's parallel computing platform for GPU programming, traditionally using C++ extensions. Rust is a systems programming language known for memory safety without garbage collection. cuda-oxide bridges these by allowing Rust code to compile to PTX, the low-level instruction set for Nvidia GPUs, without requiring separate DSLs or bindings.

<details><summary>References</summary>
<ul>
<li><a href="https://nvlabs.github.io/cuda-oxide/index.html">The cuda-oxide Book — cuda-oxide</a></li>
<li><a href="https://github.com/NVlabs/cuda-oxide">GitHub - NVlabs/cuda-oxide: cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.</a></li>
<li><a href="https://www.phoronix.com/news/NVIDIA-CUDA-Oxide-0.1">NVIDIA Releases CUDA-Oxide 0.1 For Experimental Rust-To-CUDA Compiler - Phoronix</a></li>

</ul>
</details>

**Discussion**: The community is highly engaged, with users excited about potential build time improvements compared to existing Rust CUDA crates that rely on CMake or nvcc. Some question how Rust's memory model maps to CUDA semantics and whether GPU programming can ever be truly safe, while others compare it to alternatives like Slang. There is also criticism of the project's documentation tone regarding MLIR.

**Tags**: `#CUDA`, `#Rust`, `#GPU programming`, `#compiler`, `#Nvidia`

---

<a id="item-3"></a>
## [Software engineering may no longer be a lifetime career](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/) ⭐️ 8.0/10

An article argues that AI coding assistants may reduce demand for junior engineers and cause skill atrophy, potentially making software engineering a less stable long-term career. This discussion highlights a potential shift in the software engineering profession, where reliance on AI could erode foundational skills and alter career trajectories, affecting both new and experienced engineers. The article claims that using AI tools reduces learning opportunities, leading to technical skill atrophy over time, and that economic pressures may force engineers to adopt AI despite long-term cognitive risks.

hackernews · movis · May 11, 14:34 · [Discussion](https://news.ycombinator.com/item?id=48095550)

**Background**: AI coding assistants like GitHub Copilot and ChatGPT can generate code from natural language prompts, potentially automating tasks traditionally done by junior developers. This has raised concerns about reduced demand for entry-level positions and the erosion of deep technical skills if engineers rely too heavily on AI.

<details><summary>References</summary>
<ul>
<li><a href="https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age">Avoiding Skill Atrophy in the Age of AI - Elevate | Addy Osmani</a></li>
<li><a href="https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html">Demand for junior developers softens as AI takes over | CIO</a></li>
<li><a href="https://stackoverflow.blog/2025/12/26/ai-vs-gen-z/">AI vs Gen Z: How AI has changed the career pathway for junior developers - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some agree that AI can cause skill atrophy if used to replace reasoning, while others argue that experienced engineers using AI as a tool become more productive. There is also concern about the hiring market, with many applications being AI-generated, making it harder to find genuine candidates.

**Tags**: `#AI`, `#software engineering`, `#career`, `#LLM`, `#future of work`

---

<a id="item-4"></a>
## [James Shore: AI Coding Agents Must Cut Maintenance Costs](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 8.0/10

James Shore argues that AI coding agents must reduce maintenance costs proportionally to productivity gains, otherwise they create unsustainable technical debt. This insight challenges the prevailing narrative that AI coding agents purely boost productivity, highlighting a hidden compounding cost that could trap teams in permanent maintenance burden. Shore uses a mathematical example: if you double code output, maintenance costs quadruple unless halved; tripling output requires one-third maintenance costs to break even.

rss · Simon Willison · May 11, 19:48

**Background**: Technical debt is the future cost of choosing quick-and-dirty solutions over well-designed ones, analogous to financial debt with accumulating interest. AI coding agents can generate code rapidly but often produce low-quality, hard-to-maintain code, exacerbating technical debt. Shore's argument reframes the productivity metric to include maintenance cost as a critical factor.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs">James Shore: You Need AI That Reduces Maintenance Costs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/technical-debt">What is Technical Debt? | IBM</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#software maintenance`, `#technical debt`, `#productivity`

---

<a id="item-5"></a>
## [Zombie Internet: AI Content Overwhelms Human Web](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler published an angry critique coining the term 'Zombie Internet' to describe how AI-generated content is polluting online spaces and distorting human writing styles. This concept highlights a new, insidious phase of AI's impact on internet culture, where human and AI interactions become indistinguishable, exhausting users and degrading content quality. Koebler distinguishes 'Zombie Internet' from the 'Dead Internet' theory by emphasizing complex interactions: people talking to bots, people using AI talking to non-AI users, and AI agents interacting with people.

rss · Simon Willison · May 11, 19:21

**Background**: The 'Dead Internet' theory is a conspiracy theory that most online content since 2016 is bot-generated. The 'Zombie Internet' concept updates this for the generative AI era, where AI slop is created by both bots and humans using AI, making it harder to filter.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>
<li><a href="https://www.fastcompany.com/91489308/zombie-internet-devastating-consequences-advertising-social-media-human-web-dead-internet-moltbook-ai-tbpn">The ‘zombie internet’ has arrived—and it has consequences ...</a></li>
<li><a href="https://digitalfrontier.com/articles/zombie-internet-ai-agents-deep-research">How to survive the zombie internet - Digital Frontier</a></li>

</ul>
</details>

**Tags**: `#AI`, `#internet culture`, `#content quality`, `#Zombie Internet`

---

<a id="item-6"></a>
## [Shopify's River AI Agent Fosters Learning Culture](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything) ⭐️ 8.0/10

Shopify CEO Tobias Lütke revealed that the company's internal AI coding agent, River, operates exclusively in public Slack channels, enabling all employees to observe and learn from interactions. This approach creates a 'Lehrwerkstatt' (teaching workshop) environment where learning happens through osmosis. This transparent, public-by-design approach to AI-assisted coding could transform how organizations integrate AI tools, shifting from individual productivity gains to collective learning and skill development. It sets a precedent for AI transparency in the workplace and may influence how other companies deploy internal AI agents. River does not respond to direct messages; it insists on public channels, making every conversation searchable. Over 5,938 employees used River across 4,450 channels in a 30-day period, according to a separate report.

rss · Simon Willison · May 11, 15:46

**Background**: Shopify is an e-commerce platform company that has been exploring AI to improve developer productivity. The concept of 'Lehrwerkstatt' is a German term for a teaching workshop where learning happens by observing and participating in real work. This approach contrasts with traditional training programs that require formal curricula.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zenml.io/llmops-database/building-a-public-ai-agent-workspace-for-organizational-learning">Shopify: Building a Public AI Agent Workspace for ...</a></li>
<li><a href="https://x.com/simonw/status/2053529689122328947">Shopify's River agent system lives in Slack and can only be ...</a></li>

</ul>
</details>

**Discussion**: Simon Willison, the author of the news item, compared River's public Slack approach to Midjourney's early public Discord interface, which helped users learn prompt engineering by watching others. He believes this mechanism contributed to Midjourney's early success.

**Tags**: `#AI-assisted coding`, `#software engineering`, `#learning culture`, `#Shopify`, `#internal tools`

---

<a id="item-7"></a>
## [NYT Corrects AI-Hallucinated Quote in Article](https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything) ⭐️ 8.0/10

The New York Times issued an editors' note correcting a story where an AI tool falsely attributed a quote to Canadian Conservative leader Pierre Poilievre, which was actually an AI-generated summary presented as a direct quotation. This incident underscores the critical risk of AI hallucinations in journalism, where AI-generated content can be mistaken for fact, eroding trust in media and highlighting the necessity of human oversight. The reporter failed to verify the AI tool's output, and the article was updated to accurately quote from a speech Poilievre actually delivered, which did not include the term 'turncoats' as the AI had claimed.

rss · Simon Willison · May 10, 23:58

**Background**: AI hallucination refers to when an AI model generates false or misleading information presented as fact. In journalism, AI tools are sometimes used to summarize or generate content, but they can fabricate quotes or details, requiring rigorous fact-checking.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://particlenews.medium.com/3-ways-particle-detects-and-avoids-hallucinations-in-news-summaries-c1a02d06f602">3 Ways Particle Detects and Avoids Hallucinations in News... | Medium</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#hallucinations`, `#generative-ai`, `#journalism`, `#misinformation`

---

<a id="item-8"></a>
## [Fake OpenAI Privacy Filter Repo Tops Hugging Face Charts](https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html) ⭐️ 8.0/10

A malicious Hugging Face repository named 'Open-OSS/privacy-filter' impersonated OpenAI's privacy filter and spread a Rust-based infostealer, reaching #1 on the trending list with approximately 244,000 downloads before being taken down. This incident highlights the growing risk of supply chain attacks in the machine learning ecosystem, where malicious models can reach a wide audience quickly. It also shows that threat actors are actively targeting Hugging Face, a key platform for AI model distribution. The repository used a loader script to deploy a Rust-based infostealer, and researchers at HiddenLayer identified six additional similar repositories. The same infrastructure was previously used to distribute the ValleyRAT remote access trojan, with overlaps to the Silver Fox hacker group.

telegram · zaihuapd · May 11, 12:51

**Background**: Hugging Face is a popular platform for hosting and sharing machine learning models. Supply chain attacks on such platforms involve injecting malicious code into seemingly legitimate models or repositories, which can then be downloaded by unsuspecting users. Rust-based infostealers are malware written in Rust, known for their performance and difficulty to detect.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trellix.com/blogs/research/demystifying-myth-stealer-a-rust-based-infostealer/">Demystifying Myth Stealer: A Rust Based InfoStealer - Trellix</a></li>
<li><a href="https://www.zscaler.com/blogs/security-research/technical-analysis-latest-variant-valleyrat">New Updates to ValleyRAT | ThreatLabz - Zscaler</a></li>

</ul>
</details>

**Discussion**: The community expressed concern about the ease with which malicious repositories can rise to the top of trending lists, with some calling for better vetting and automated scanning on Hugging Face. Others noted the sophistication of the attack, including the use of Rust to evade detection.

**Tags**: `#supply chain attack`, `#Hugging Face`, `#malware`, `#OpenAI`, `#infostealer`

---