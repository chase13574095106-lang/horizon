---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 31 items, 8 important content pieces were selected

---

1. [Microsoft Designates Rust as a Tier-1 Language](#item-1) ⭐️ 9.0/10
2. [Calif Research Unveils WeWorm, First Zero-Click Worm via WeChat Calls](#item-2) ⭐️ 9.0/10
3. [DeepSeek Releases Open-Source Harness and Opens V4-Pro-0813 Weights](#item-3) ⭐️ 9.0/10
4. [Shopify moves from React Native back to native Swift and Kotlin](#item-4) ⭐️ 8.0/10
5. [Researchers question whether OpenAI can be trusted with unpublished math](#item-5) ⭐️ 8.0/10
6. [Ant International, Visa and Mastercard Team Up on AI Agent Payment Standards](#item-6) ⭐️ 8.0/10
7. [DeepSeek Releases V4.1 Flash: 552B Multimodal Model With New Architecture](#item-7) ⭐️ 8.0/10
8. [Moonshot AI (Kimi) Confidentially Files for Hong Kong IPO at $50B Pre-Money Valuation](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft Designates Rust as a Tier-1 Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Microsoft has officially designated Rust as a tier-1 programming language, giving internal teams a paved path from local development to production with secure toolchain builds, developer tooling, quality workflows, deep platform integration, and compliance support. The announcement, published as a guest post on the Rust Foundation's website, also confirms that Microsoft has replaced LLVM with MSVC's backend for Rust. This marks a major strategic shift for one of the world's largest software companies, signaling that Rust is now a mature, serious competitor to C++ and C# for systems programming. It could accelerate industry-wide adoption of memory-safe languages, especially given that roughly 70% of Microsoft's CVEs are memory safety issues. The tier-1 status means Rust gets first-class engineering support at Microsoft, including secure toolchain builds and compliance workflows, and the switch to MSVC's backend is a notable technical change. Community discussion also references Microsoft's stated goal of converting 1 billion lines of code to Rust by 2030 using automated tooling, though official details remain limited.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a general-purpose systems programming language created by Graydon Hoare at Mozilla in 2006, with its first stable release in 2015 and sponsorship by the Rust Foundation since 2021. It enforces memory safety without a garbage collector via its 'borrow checker', which tracks reference lifetimes at compile time, preventing bugs like null pointer dereferences and data races. Memory safety is a property of languages that prevents certain memory-related bugs, many of which become security vulnerabilities in languages like C and C++.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>
<li><a href="https://www.memorysafety.org/docs/memory-safety/">What is memory safety and why does it matter? - Prossimo</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (579 points, 317 comments) was largely positive, with commenters noting Rust is now a mature competitor to C++ and C# rather than a fledgling language, and highlighting that all major OS vendors have diversified their systems programming options. A key point of excitement was the replacement of LLVM with MSVC's backend, and some linked Microsoft's 1B LOC conversion goal and DARPA's automated C-to-Rust translation efforts as supporting context.

**Tags**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Programming Languages`

---

<a id="item-2"></a>
## [Calif Research Unveils WeWorm, First Zero-Click Worm via WeChat Calls](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, described as the first zero-click worm that spreads through WeChat calls on both iOS and Android, hijacking accounts without any victim interaction. The team says it found the bug and wrote the first remote code execution (RCE) exploit in about two days with AI assistance, then built the worm in one more week. This marks a paradigm shift in AI-assisted vulnerability discovery and exploit development, showing that a small team can now build a self-spreading mobile worm that once required months of work by a larger team. It raises urgent questions for mobile security, WeChat's massive user base, and AI safety, since the same capabilities could be abused by attackers. The vulnerability is a memory corruption issue in WeChat's VoIP stack, and the exploit succeeds even if the victim answers the call and hears nothing. Calif Research emphasizes that AI did most of the work while humans provided judgment about targeting and safe testing.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit compromises a device without any user action, making it far more dangerous than attacks that require a click or download. A worm is malware that self-replicates and spreads automatically, and remote code execution (RCE) means an attacker can run arbitrary code on a victim's device. WeChat is one of the world's most widely used messaging apps, so a worm spreading through its call feature could reach an enormous number of users.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberinsider.com/zero-click-worm-spreads-on-iphones-and-android-via-wechat-calls/">Zero-click worm spreads on iPhones and Android via WeChat calls</a></li>
<li><a href="https://www.1950.ai/post/wechat-zero-click-worm-how-ai-turned-a-voip-vulnerability-into-a-self-spreading-account-hijacking-t">WeChat Zero-Click Worm: How AI Turned a VoIP Vulnerability Into...</a></li>
<li><a href="https://iplogger.org/blog/researchers-build-wechat-zero-click-worm-hijacking-phones-via-calls/">WeChat Zero-Click Worm: AI-Powered Call Hijacks Threaten Android...</a></li>

</ul>
</details>

**Tags**: `#ai-security`, `#mobile-security`, `#zero-click-exploit`, `#worm`, `#rce`

---

<a id="item-3"></a>
## [DeepSeek Releases Open-Source Harness and Opens V4-Pro-0813 Weights](https://t.me/zaihuapd/43738) ⭐️ 9.0/10

DeepSeek has launched DeepSeek Harness, an open-source agent harness released under the MIT license, and simultaneously opened the weights for DeepSeek-V4-Pro-0813 on Hugging Face. The Harness treats models, tools, skills, sessions, sandboxes, storage, scheduling, and UI as swappable plugins, and offers four runtime modes: Standard, PTC, Minimal, and Creative. This is a significant move for the AI agent ecosystem, as DeepSeek is offering both a fully open orchestration framework and open model weights, giving developers a free alternative to proprietary agent tools like Claude Code. The plugin-based architecture could lower the barrier to building and customizing agent workflows, and the permissive MIT license encourages broad commercial and community adoption. DeepSeek Harness is built on the Cordis plugin system and is currently in developer preview, with source code available on GitHub and npm. PTC mode keeps the full Standard-mode toolset but exposes tools through a generated SDK and a reserved run_code transport, allowing nested calls and parallel execution, though side effects are not rolled back and token savings remain workload-dependent.

telegram · zaihuapd · Sep 10, 07:28

**Background**: An agent harness is the software layer that connects a large language model to external capabilities such as file editing, shell commands, web search, and tool invocation, effectively turning a raw model into a working agent. DeepSeek is a Chinese AI company known for releasing capable open-weight models, and DeepSeek-V4-Pro-0813 is its latest model, featuring a 1M-token context window and an efficient MoE (Mixture of Experts) architecture. Cordis is a plugin framework that enables the 'everything is a plugin' design, letting developers swap or recompose any agent capability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://huggingface.co/multimodalart/DeepSeek-V4-Pro-0813">multimodalart/ DeepSeek - V 4 - Pro - 0813 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#open-source`, `#AI`, `#LLM`, `#model release`

---

<a id="item-4"></a>
## [Shopify moves from React Native back to native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is migrating its mobile app from React Native back to fully native Swift (iOS) and Kotlin (Android) codebases, citing AI-assisted code porting as a key enabler that made the transition practical. The company's engineering blog post frames the move as a return to native development after years of relying on the cross-platform framework. This is a notable industry signal because Shopify is a major, high-profile adopter of React Native, and its reversal suggests that even large engineering organizations may find native development worth the cost when AI can shoulder the porting burden. It could influence how other companies weigh cross-platform frameworks against native code, and it fuels the broader debate about AI's role in managing—or multiplying—software complexity. The migration is reportedly enabled by AI coding agents that can port React Native code to Swift and Kotlin, with community members describing similar efforts where most of the porting happened overnight and only a few days were spent on polish. The decision hinges on whether a team has the native expertise to maintain the resulting code, since AI-generated Swift or Kotlin can be hard for non-native developers to review.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework from Meta that lets developers build iOS and Android apps using JavaScript and React, sharing one codebase across platforms. Swift is Apple's compiled language for iOS and macOS, while Kotlin is JetBrains' language that Google has endorsed as the preferred choice for Android development. Native development generally offers better performance and platform-specific UX, but requires separate codebases and expertise for each platform, which is why cross-platform frameworks like React Native became popular.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some warned that Shopify may be underestimating complexity by assuming AI makes it free, arguing that AI struggles with complexity just as humans do. Others shared firsthand success porting React Native to native with AI agents, while several noted that the real question is whether a team has the native expertise to maintain and review the resulting Swift and Kotlin code.

**Tags**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#AI-assisted Development`

---

<a id="item-5"></a>
## [Researchers question whether OpenAI can be trusted with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A discussion originating on Mathstodon and amplified across X and Bluesky alleges that OpenAI used collaborative chats with researchers to solve open math problems and then published results along those lines without attribution. The thread, which drew 586 comments on Hacker News, questions whether researchers can safely share unpublished mathematical work with OpenAI's models. The dispute touches on research integrity and the ethics of AI companies learning from confidential collaborations, potentially deterring mathematicians from using frontier models and prompting calls for clearer attribution and data-use policies. It also feeds a broader debate about whether AI systems are genuinely solving open problems or absorbing fresh human insight from their users. Commenters note that OpenAI has reportedly given large numbers of researchers free or subsidized access, meaning user chats could enter pretraining data, while OpenAI reportedly claims the model that produced the result was not trained on those collaborative chats. The debate distinguishes between a model memorizing chat content and reinforcement learning on verifiable math enabling genuinely novel techniques.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Mathstodon is a Mastodon server for mathematicians, part of the decentralized fediverse, while XCancel is a Nitter-based alternative front-end for viewing X/Twitter posts and Bluesky is a separate decentralized microblogging network built on the AT Protocol. The controversy centers on whether frontier AI labs can be trusted with unpublished research shared during informal collaboration, and on how credit should be assigned when a model appears to build on that input.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mastodon_(social_network)">Mastodon (social network) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bluesky">Bluesky - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely compare OpenAI to a human collaborator who took ideas from a joint project and published without credit, calling that unethical, though some argue both things can be true: chats may improve model intuition while reinforcement learning on verifiable math produces genuinely superhuman results. Others suggest the only ethical path was to offer free credits and tooling support rather than scoop collaborators, and a few express indifference, saying the researchers should have known better.

**Tags**: `#OpenAI`, `#AI ethics`, `#research integrity`, `#mathematics`, `#collaboration`

---

<a id="item-6"></a>
## [Ant International, Visa and Mastercard Team Up on AI Agent Payment Standards](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 8.0/10

On September 10, 2026, Ant International, Visa and Mastercard announced in São Paulo that they will jointly develop common standards for AI-agent payments, including a 'Know Your Agent' (KYA) mechanism that links an agent to a valid legal entity, evaluates its behavior and monitors transaction risk. The three companies cited a McKinsey projection that AI agents could handle $3 trillion to $5 trillion of global consumer commerce by 2030. This is the first time three major payment players spanning China and the West have agreed to work on a shared trust framework for agentic commerce, which could prevent a fragmented patchwork of proprietary agent-verification schemes. If adopted widely, the standard would shape how banks, merchants and wallet providers authenticate and accept AI agents that shop, book and pay on behalf of consumers. The KYA mechanism is designed to improve interoperability and security across different payment systems by verifying agent identity and continuously monitoring behavior, rather than relying on a single platform's proprietary checks. The initiative is still at the framework stage, with no published technical specification, certification process or timeline for implementation yet.

telegram · zaihuapd · Sep 10, 03:00

**Background**: AI agents are increasingly able to act autonomously on a user's behalf — comparing products, booking travel and completing checkout — but payment networks have no common way to confirm that an agent is genuinely authorized by a real person or business. 'Know Your Agent' is an emerging concept modeled on traditional Know Your Customer (KYC) rules, extending identity verification and risk controls to software agents. Mastercard has already proposed its Agent Pay Acceptance Framework, and the FIDO Alliance has taken up the Agent Payments Protocol (AP2) to keep agentic payment standards open and platform-agnostic.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html">Ant International, Visa and Mastercard team up on AI payment ...</a></li>
<li><a href="https://www.reuters.com/technology/payment-firms-visa-mastercard-ant-international-team-up-ai-agent-trust-framework-2026-09-10/">Payment firms Visa, Mastercard and Ant International team up ...</a></li>
<li><a href="https://www.mastercard.com/us/en/news-and-trends/stories/2025/agentic-commerce-framework.html">Agentic token framework: Driving trusted AI transactions</a></li>

</ul>
</details>

**Tags**: `#AI payments`, `#fintech`, `#AI agents`, `#standards`, `#Visa/Mastercard`

---

<a id="item-7"></a>
## [DeepSeek Releases V4.1 Flash: 552B Multimodal Model With New Architecture](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek officially released V4.1 Flash, the smallest model in its new architecture series, featuring 552B parameters in a Causal-Encoder-Decoder structure with 8B input and 16B output activation, and native multimodal vision understanding. The model is now live on the DeepSeek API as deepseek-flash, with new pricing effective September 10, 2026, and deepseek-v4-pro requests routed to V4.1 Flash starting September 14, 2026. This release signals DeepSeek's push toward more efficient, cost-effective frontier models, with early third-party tests reportedly placing V4.1 Flash ahead of V4-Pro on performance, cost, speed, and total runtime. The automatic routing of deepseek-v4-pro traffic to the new model means existing API users will be migrated without code changes, potentially lowering costs across production workloads. According to vLLM Recipes, V4.1 Flash is a vision-language MoE model with 522B total parameters, 8B active per prompt token and 16B per output token, combining sliding-window plus compressed sparse attention with a two-level indexer, engram n-gram memory, hyper-connections, and a DSpark multi-token draft head. For compatibility, deepseek-v4-flash and deepseek-v4-flash-vision-exp temporarily route to V4.1 Flash.

telegram · zaihuapd · Sep 10, 05:54

**Background**: Large language models generally fall into three architecture families: encoder-decoder, causal decoder, and prefix decoder, each with distinct attention patterns. A Causal-Encoder-Decoder design combines causal (left-to-right) generation with an encoder component, which can help models handle both understanding and generation tasks. Multimodal vision understanding means the model can process images alongside text, a capability increasingly common in frontier LLMs. DeepSeek is a Chinese AI lab known for releasing competitive open and API-based models at low prices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash | vLLM Recipes</a></li>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-1-flash-pro-routing-prices-early-tests">DeepSeek V4.1 Flash: Benchmarks, Prices and Pro Cutoff</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#LLM`, `#multimodal`, `#model release`, `#API`

---

<a id="item-8"></a>
## [Moonshot AI (Kimi) Confidentially Files for Hong Kong IPO at $50B Pre-Money Valuation](https://t.me/zaihuapd/43743) ⭐️ 8.0/10

Moonshot AI (Kimi) has confidentially submitted an A1 filing to the Hong Kong Stock Exchange, formally kicking off its Hong Kong IPO process, and is simultaneously raising a new funding round at a $50 billion pre-money valuation that may be its last before listing. The company declined to comment, saying it has no information to disclose at this time. This is one of the most significant signals yet that China's large-model sector is maturing from venture-stage startups into public-market candidates, and it could set a valuation benchmark for peers such as DeepSeek, which observers expect may list in the first half of next year. A successful listing would give Moonshot access to public capital for compute and talent at a scale that private rounds alone cannot easily match. The $50 billion figure is a pre-money valuation, meaning it excludes the new capital being raised; by comparison, the company's post-money valuation was about $3.5 billion in July, up roughly 8x from about $4.3 billion at the end of 2025. Moonshot has maintained a roughly three-month release cadence, shipping K2.5, K2.6 and K3 between January and July this year.

telegram · zaihuapd · Sep 10, 10:58

**Background**: An A1 filing is the formal application form a company submits to the Hong Kong Stock Exchange to begin the listing process; a confidential filing lets a company test the waters with regulators before details become public. Pre-money valuation refers to a company's value before new investment is added, while post-money valuation includes the newly injected capital, so the two numbers are not directly comparable. Moonshot AI is the Beijing-based developer of the Kimi chatbot and the K-series of large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://hk.stockstar.com/RB2026090300005720.shtml">据媒体报道，月之暗面（Kimi）已于本周以保密形式向港交所递交 A1 文...</a></li>
<li><a href="https://news.futunn.com/post/78704914/moonshot-ai-confidentially-files-with-the-hong-kong-stock-exchange">月之暗面向港交所秘密交表，正式启动 IPO</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/369371592">股权融资中的重大误区——投前估值和投后估值不分 - 知乎 投前估值 vs 投后估值：到底有什么区别？ | EquiRound 投前VS投后估值？新股VS老股？还在傻傻分不清楚？ 投前估值 vs 投后估值（2026 指南） | Round Funded 想拿投资人的钱？创业者要分清“投前估值”与“投后估值”！</a></li>

</ul>
</details>

**Tags**: `#AI`, `#IPO`, `#Moonshot AI`, `#Kimi`, `#LLM`

---