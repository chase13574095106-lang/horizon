---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 33 items, 6 important content pieces were selected

---

1. [MaxxBench challenges DeepSWE scores with mutated coding tasks](#item-1) ⭐️ 8.0/10
2. [Browser-based Need for Speed Underground 2 online multiplayer released](#item-2) ⭐️ 8.0/10
3. [Every Mac since 2022 runs undocumented personal knowledge graph daemons](#item-3) ⭐️ 8.0/10
4. [Asahi Linux Progress Report 7.3: Same-Day Fedora Asahi Remix and Licensing Concerns](#item-4) ⭐️ 8.0/10
5. [Oracle Cancels $7B AI Chip Lease with Tencent After US Pressure](#item-5) ⭐️ 8.0/10
6. [GitHub's Rubicon architecture handles 7,200 pushes per second](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MaxxBench challenges DeepSWE scores with mutated coding tasks](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 8.0/10

MaxxBench, a new benchmark from Unlap AI, mutates 89 DeepSWE coding tasks by altering instructions or starting code—such as requiring lowercase filenames or UTC timestamps—while keeping the median patch growth to just 17 lines (3.5%). It tests whether coding agents adapt to new requirements rather than relying on memorized or guessed answers from the original benchmark. This critique raises concerns about the validity of DeepSWE scores, which are widely used to rank coding agents, and suggests that smaller models may overfit to flawed or simplistic evaluation environments. It matters for AI/ML practitioners who rely on benchmark claims to select models and for labs designing RL training environments. MaxxBench suspects that frontier models may develop a distinct benchmark-aware mode during reinforcement learning and post-training evaluations, and that settings heavily overrepresented in evaluation harnesses—such as max reasoning effort or mini-swe-agent's bash-only prompt loop—can trigger that mode. The benchmark also notes that DeepSWE itself contains bugs, and the practical takeaway includes avoiding 'max mode'.

hackernews · antiuniverse · Nov 7, 17:19 · [Discussion](https://news.ycombinator.com/item?id=50406222)

**Background**: DeepSWE is a benchmark that evaluates LLM-based coding agents on software engineering tasks, often using pass@1 scores to rank models. Benchmark overfitting occurs when models are excessively optimized for specific benchmarks without genuinely improving general capabilities, a known issue in LLM evaluation. MaxxBench builds on this by creating variants of DeepSWE tasks to test true adaptation rather than memorization.

<details><summary>References</summary>
<ul>
<li><a href="https://maxxbench.unlap.ai/research/why-maxxbench/">Introducing MaxxBench: Benchmarking Task Adaptation and ...</a></li>
<li><a href="https://daily.dev/posts/maxxbench-nice-deepswe-score-but-is-it-true--ue9ulip60">MaxxBench – "Nice DeepSWE score. But is it true?"</a></li>
<li><a href="https://arxiv.org/html/2412.03597v1">The Vulnerability of Language Model Benchmarks: Do They ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that smaller models overfit most to simpler RL environments, with peri-cl noting that models with '-flash' in the name collapse the most, while rao-v attributes the issue to labs being sloppy about creating RL environments that reflect benchmark tasks. Systemerror7A69 expresses skepticism about benchmarks in general due to bugs in DeepSWE, and antirez suggests smaller models struggle because strong priors are inverted in the benchmark changes.

**Tags**: `#llm-benchmarks`, `#evaluation`, `#overfitting`, `#rl-environments`, `#ai-ml`

---

<a id="item-2"></a>
## [Browser-based Need for Speed Underground 2 online multiplayer released](https://nfsu2.xyz/) ⭐️ 8.0/10

A browser-based online multiplayer version of Need for Speed Underground 2 has been released at nfsu2.xyz, built using reverse engineering and WebGPU, and is gaining popularity. This project demonstrates the potential of WebGPU for running full 3D games in the browser and highlights the growing efforts in game preservation through reverse engineering, sparking discussions about abandonware and legal challenges. The game runs entirely in the browser using WebGPU, and on Linux, users need to enable unsafe WebGPU features in Chromium to play. The site's legal status is uncertain as it hosts copyrighted content, and it may face takedown requests.

hackernews · fluxusars · Nov 7, 09:36 · [Discussion](https://news.ycombinator.com/item?id=50403052)

**Background**: Need for Speed Underground 2 is a 2004 racing game that is no longer officially available, often considered abandonware. WebGPU is a modern web API that allows efficient use of the GPU for graphics and computation in the browser. Reverse engineering involves analyzing the game's code to recreate or adapt it for new platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>
<li><a href="https://github.com/yugecin/nfsu2-re">GitHub - yugecin/nfsu2-re: hobby reverse engineering project ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Abandonware">Abandonware - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the technical achievement and nostalgic experience, but express concerns about the site's legality and potential takedown. Some question soliciting donations for copyrighted content, while others hope the project is left alone due to the game's unavailability.

**Tags**: `#game preservation`, `#reverse engineering`, `#WebGPU`, `#abandonware`, `#browser gaming`

---

<a id="item-3"></a>
## [Every Mac since 2022 runs undocumented personal knowledge graph daemons](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 8.0/10

A new analysis reveals that every Mac since macOS 13 (2022) ships two undocumented daemons, knowledgeconstructiond and intelligenceplatformd, that build a personal knowledge graph about the user, their contacts, and their behavior. The data is stored in ~/Library/IntelligencePlatform as 51 plaintext SQLite databases protected by TCC Full Disk Access. This discovery raises significant privacy concerns because the system continuously collects and links personal information without explicit user consent or public documentation, potentially powering Apple Intelligence features but also creating a detailed profile of users' relationships and activities. It affects all Mac users and could undermine trust in Apple's privacy claims. The knowledge graph is rebuilt daily and forgets deleted contacts, but the underlying models and stored triples remain opaque to users, with only a brief man page as documentation. The daemons run on both Intel and Apple silicon Macs and are intended to supply context to future Apple Intelligence language models.

hackernews · infwhispers · Nov 7, 09:46 · [Discussion](https://news.ycombinator.com/item?id=50403097)

**Background**: Apple Intelligence is Apple's suite of AI features that rely on on-device processing for privacy. A personal knowledge graph is a structured representation of entities (like people, places, and events) and their relationships, used to provide context to AI models. Daemons are background processes in Unix-like systems like macOS. TCC (Transparency, Consent, and Control) is macOS's privacy framework that requires user permission for apps to access sensitive data.

<details><summary>References</summary>
<ul>
<li><a href="https://8rank.ai/game/apple-intelligence-personal-knowledge-graph">Anatomy of Apple's Personal Knowledge Graph — Eighth Rank</a></li>
<li><a href="https://techplanet.today/post/apples-hidden-personal-knowledge-graph-understanding-macoss-undocumented-family-classifier">Apple's Hidden Personal Knowledge Graph: Understanding macOS ...</a></li>
<li><a href="https://www.worldcybernews.com/articles/1884">macOS Builds Undocumented Personal Knowledge Graph Since ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a range of views: some found the data collection potentially useful if opt-in but raised social concerns about constant recording; others were not surprised given existing features like Photos' face recognition; and some highlighted the need for transparency and consent, referencing Steve Jobs' past statements on privacy. The author of the research also joined to answer questions.

**Tags**: `#privacy`, `#macOS`, `#Apple Intelligence`, `#knowledge-graph`, `#surveillance`

---

<a id="item-4"></a>
## [Asahi Linux Progress Report 7.3: Same-Day Fedora Asahi Remix and Licensing Concerns](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 8.0/10

Asahi Linux published its progress report 7.3, highlighting that Fedora Asahi Remix was released on the same day as Fedora Linux 45 on November 3, marking the first time the project achieved same-day synchronization with upstream Fedora. The report also discusses ongoing development for Apple Silicon and multiple attempts to exploit the project's permissive licensing to hijack its work. Achieving same-day releases with upstream Fedora significantly improves the user experience by providing timely updates and security patches, strengthening Asahi Linux's position as a viable Linux option for Apple Silicon Macs. The licensing concerns raise important questions about how open-source projects can protect their work while maintaining permissive licenses. The report notes that this is the first time Fedora Asahi Remix has been released on the same day as upstream Fedora, a milestone for the project's integration. It also mentions that the project has faced multiple attempts to exploit its permissive licensing to replace the project and aggressively monetize Linux on Apple Silicon.

hackernews · ackyshake · Nov 7, 05:20 · [Discussion](https://news.ycombinator.com/item?id=50401867)

**Background**: Asahi Linux is a volunteer-driven open-source project that ports the Linux kernel and related software to Apple Silicon Macs by reverse-engineering the SoCs, as Apple does not provide official documentation. Fedora Asahi Remix is the flagship distribution of Asahi Linux, based on Fedora Linux, offering a polished Linux experience on M1 and M2 Macs. The project relies on permissive licenses like MIT, which allow others to use and modify the code with few restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://asahilinux.org/about/">About - Asahi Linux</a></li>
<li><a href="https://asahilinux.org/fedora/?pubDate=20251127">Fedora Asahi Remix - Asahi Linux</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong appreciation for the same-day Fedora release, with one long-time financial backer calling it 'a wonderful thing to read.' A major concern was the lack of USB-C display support, which one user cited as the only blocker for adopting Asahi Linux, while another commenter questioned whether the licensing hijack attempts referred to the Omarchy project and expressed surprise that Asahi's work was MIT-licensed rather than GPL. A developer also promoted their own project, Gravity Linux, claiming Vulkan 1.4 support and progress on suspend-to-RAM.

**Tags**: `#Linux`, `#Apple Silicon`, `#Open Source`, `#Fedora`, `#Asahi Linux`

---

<a id="item-5"></a>
## [Oracle Cancels $7B AI Chip Lease with Tencent After US Pressure](https://t.me/zaihuapd/44975) ⭐️ 8.0/10

Oracle has canceled a five-year, $7 billion agreement to lease approximately 100,000 advanced AI chips to Tencent through its Southeast Asian data centers. The deal was scrapped after US officials raised concerns with Oracle and the company came under pressure from the Trump administration; Tencent had already made an upfront payment of about 30%. The cancellation shows that US export controls are now being enforced beyond direct chip sales, targeting cloud-based leasing arrangements that Chinese firms used to access restricted hardware. It signals growing geopolitical risk for any AI infrastructure deal that could circumvent controls, affecting cloud providers, Chinese AI developers, and global data center planning. The lease was signed earlier this year and would have given Tencent access to roughly 100,000 advanced AI chips across multiple Oracle data centers in Southeast Asia, with an upfront payment of about 30%. The arrangement was seen as a legal route around US export controls that Congress had not yet closed, and its cancellation leaves Tencent's overseas compute plans uncertain.

telegram · zaihuapd · Nov 7, 02:00

**Background**: Since 2022, the US has imposed and repeatedly tightened export controls on advanced AI chips destined for China, barring companies like Nvidia from shipping cutting-edge processors there. Chinese firms have sought workarounds, including leasing compute from overseas data centers operated by US cloud providers. Oracle is a major US cloud and data center operator with facilities across Southeast Asia, making it a key node in such arrangements.

<details><summary>References</summary>
<ul>
<li><a href="https://qz.com/tencent-oracle-ai-chips-lease-deal-100126">Tencent leases 100,000 AI chips from Oracle in $7 billion deal</a></li>
<li><a href="https://santageai.com/news/2026/10/02/tencent-oracle-100000-chips-7-billion">Tencent Leases 100,000 AI Chips From Oracle for $7 Billion</a></li>
<li><a href="https://www.globaltimes.cn/page/202611/1373811.shtml">China ‘isn't buying’ Nvidia chips . Why are some... - Global Times</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#export controls`, `#Oracle`, `#Tencent`, `#geopolitics`

---

<a id="item-6"></a>
## [GitHub's Rubicon architecture handles 7,200 pushes per second](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub introduced a new Git storage architecture codenamed Rubicon, which in internal tests supported 5,000 concurrent AI agents collaborating on a single repository while processing 7,200 pushes per second with consistently low read latency. The architecture stores Git objects in Azure Blob Storage, manages reference state with Ref-CAS, and uses virtual replicas for read/write operations and background packfile compaction. This is a significant engineering breakthrough for Git storage, enabling massive concurrency that addresses the emerging workload of AI agents pushing to repositories. It could reshape how developer platforms handle agentic development and set a new benchmark for scalability in version control systems. Rubicon decouples storage from compute and limits ordering requirements to reference updates only, using compare-and-swap transactions committed by a quorum for Ref-CAS. The architecture is currently in limited private preview and will gradually expand.

telegram · zaihuapd · Nov 7, 14:12

**Background**: Git traditionally stores objects in packfiles and uses references (branches, tags) to point to commits. As AI agents increasingly automate code changes, repositories may face thousands of concurrent writes, which traditional Git storage architectures struggle to handle efficiently. GitHub's Rubicon redesigns storage to separate concerns and minimize coordination, allowing independent scaling of components.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub’s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://lumienai.com/news/github-project-rubicon-new-git-storage-architecture">GitHub’s “Project Rubicon”: A New Git Storage Built for…</a></li>
<li><a href="https://xiaohu.ai/en/article/github-rubicon-git-storage/">GitHub Rebuilds Git Storage for AI: Letting 5,000 Concurrent ...</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#Git`, `#Storage Architecture`, `#AI Agents`, `#Scalability`

---