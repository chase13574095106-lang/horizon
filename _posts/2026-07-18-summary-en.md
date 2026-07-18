---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 31 items, 11 important content pieces were selected

---

1. [GPT-5.6 Sol Pro Solves 30-Year Convex Optimization Conjecture](#item-1) ⭐️ 9.0/10
2. [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](#item-2) ⭐️ 9.0/10
3. [LG monitors silently install software via Windows Update](#item-3) ⭐️ 8.0/10
4. [Stack Overflow's Decline Visualized in a Graph](#item-4) ⭐️ 8.0/10
5. [PHK Reflects on Bikeshedding in Open Source](#item-5) ⭐️ 8.0/10
6. [Anthropic Reverses Course, Makes Claude Fable 5 Permanent](#item-6) ⭐️ 8.0/10
7. [Meta in Talks to Lease AI Compute to Anthropic in $10B Deal](#item-7) ⭐️ 8.0/10
8. [SpaceX in Talks with Pentagon for AI Computing Deal](#item-8) ⭐️ 8.0/10
9. [TSMC Announces A14 Process Technology for 2028 Production](#item-9) ⭐️ 8.0/10
10. [Trump Administration Plans FINRA-like AI Model Watchdog](#item-10) ⭐️ 8.0/10
11. [San Francisco Orders Apple, Google to Remove 'Nudify' Apps](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Sol Pro Solves 30-Year Convex Optimization Conjecture](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

GPT-5.6 Sol Pro, a high-capability AI model, used a single prompt to prove a long-standing conjecture in convex optimization, closing a gap that had remained open for 30 years. This marks a significant milestone in AI-assisted mathematical research, demonstrating that large language models can contribute to solving open problems in theoretical fields like convex optimization, potentially accelerating discovery in mathematics and theoretical computer science. The conjecture concerns the time complexity of solving optimization problems over convex, Lipschitz functions on a spherical domain. The proof was achieved using GPT-5.6 Sol Pro, not the more advanced Ultra tier, highlighting the capability of the Sol Pro model.

hackernews · mbustamanter · Jul 18, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48957779)

**Background**: Convex optimization is a subfield of mathematical optimization focused on minimizing convex functions over convex sets. It has broad applications in machine learning, engineering, and economics. The conjecture addressed a fundamental question about the optimal convergence rate for certain optimization algorithms, which had remained unresolved for three decades.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt">GPT - 5 . 6 in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://developer.puter.com/ai/openai/gpt-5.6-sol-pro/">GPT - 5 . 6 Sol Pro - API, Specs, Playground & Pricing - Puter Developer</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed excitement and curiosity, with users noting that this is a real contribution to the field. Some discussed the implications for junior researchers, suggesting that low-hanging fruit may no longer be viable for human mathematicians. Others compared the Sol Pro and Ultra tiers, and noted that AI can brute-force mathematical logic in certain cases.

**Tags**: `#AI`, `#mathematics`, `#convex optimization`, `#LLM`, `#research`

---

<a id="item-2"></a>
## [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](https://t.me/zaihuapd/42637) ⭐️ 9.0/10

Moonshot AI released Kimi K3, the world's first open-source 2.8 trillion parameter model, which achieved the top score of 1,679 on the Frontend Code Arena leaderboard, surpassing Claude Fable 5 and GPT-5.6 Sol. Kimi K3 demonstrates that open-source models can compete with and even surpass proprietary frontier models in specific benchmarks, potentially accelerating AI accessibility and innovation. Its novel attention architecture also represents a significant technical advancement. K3 uses a hybrid architecture with Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), featuring native vision capabilities and a 1 million token context window. It leads in 6 out of 7 evaluation domains on Frontend Code Arena, only trailing in gaming.

telegram · zaihuapd · Jul 18, 02:29

**Background**: Kimi Delta Attention is a linear attention mechanism that extends Gated DeltaNet with finer-grained gating for efficient long-context processing. Attention Residuals replace standard residual connections with learned softmax attention over depth, allowing each layer to selectively aggregate earlier representations. These innovations enable K3 to handle extremely long sequences efficiently while maintaining high performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.26692">KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE</a></li>
<li><a href="https://arxiv.org/abs/2603.15031">[2603.15031] Attention Residuals - arXiv.org Attention Residuals - arXiv.org GitHub - MoonshotAI/Attention-Residuals Attention Residuals: The Long-Overdue Upgrade to How Neural ... Attention Residuals Explained: Rethinking Transformer Depth Attention Residuals Mechanism | kyegomez/attn_res | DeepWiki GitHub - kyegomez/attn_res: A clean, single-file PyTorch ...</a></li>
<li><a href="https://officechai.com/ai/kimi-k3-beats-fable-5-gpt-5-6-sol-on-frontend-code-arena/">Kimi K3 Beats Fable 5, GPT 5.6 Sol On Frontend Code Arena</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether K3's performance stems from distillation or independent innovation, with some arguing that distillation of frontier models is inevitable and beneficial. Others expressed concerns about potential government restrictions on open-weight models, comparing it to the Napster era. A user reported that K3 consumed nearly the entire 5-hour usage limit on a task that took minutes on OpenAI's $20 plan, raising questions about efficiency.

**Tags**: `#AI`, `#LLM`, `#open-source`, `#benchmark`, `#architecture`

---

<a id="item-3"></a>
## [LG monitors silently install software via Windows Update](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 8.0/10

LG monitors automatically install software through Windows Update without user consent when plugged into a PC, as reported by multiple users and security researchers. This raises serious security and privacy concerns because the software runs with full system access, starts at boot, and can be triggered by simply plugging in an LG monitor, potentially enabling supply chain attacks. The software installs even if the monitor was previously connected, and it has internet access with no sandboxing. Workarounds include disabling automatic download of manufacturer apps via Group Policy or Device Installation Settings.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update can deliver driver and software updates from hardware vendors. However, this feature is being abused to push potentially unwanted software without user interaction, reminiscent of past autorun issues with USB drives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fingerlakes1.com/2026/07/18/lg-monitor-software-now-installs-through-windows-update-and-many-users-did-not-expect-it/">LG Monitor Software Now Installs Through Windows Update and ...</a></li>

</ul>
</details>

**Discussion**: The community is highly critical, with users pointing out that Windows is ultimately responsible for allowing this behavior. Some provide detailed workarounds, while others debate whether this constitutes a supply chain attack.

**Tags**: `#security`, `#privacy`, `#Windows`, `#LG`, `#supply chain attack`

---

<a id="item-4"></a>
## [Stack Overflow's Decline Visualized in a Graph](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

A graph from Stack Exchange Data Explorer shows a significant decline in Stack Overflow activity, with community debate attributing it to AI, poor moderation, and corporate acquisition. This matters because Stack Overflow has been a cornerstone resource for developers worldwide, and its decline signals a shift in how developers seek and share knowledge, potentially impacting the entire software development ecosystem. The graph peaked in 2014, well before the rise of AI, and the decline accelerated after the site was acquired by Prosus in 2021. Community comments highlight that the decline predates ChatGPT, suggesting multiple factors at play.

hackernews · secretslol · Jul 18, 11:12 · [Discussion](https://news.ycombinator.com/item?id=48956949)

**Background**: Stack Overflow is a Q&A platform for programmers, known for its strict moderation and reputation system. The community has long debated whether its exclusionary culture and focus on strict Q&A format drove users away, with AI tools like ChatGPT now offering an alternative for getting quick answers.

**Discussion**: Community comments express strong sentiment that Stack Overflow's decline was self-inflicted due to high barriers to participation and a culture that discouraged newcomers. Some note the decline began before AI, pointing to the Prosus acquisition and the site's exclusionary policies as key factors.

**Tags**: `#Stack Overflow`, `#AI impact`, `#community management`, `#data analysis`, `#online communities`

---

<a id="item-5"></a>
## [PHK Reflects on Bikeshedding in Open Source](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

Poul-Henning Kamp (PHK), a prominent open source developer, published an article in ACM Queue reflecting on the bikeshedding phenomenon in open source communities, sharing lessons from his long career and advocating for better decision-making processes. This article provides valuable insights from a key figure in open source, helping communities recognize and mitigate bikeshedding, which can waste time and hinder progress on important issues. The article includes historical context such as PHK's creation of MD5crypt in 1994, and discusses the concept of reversible decisions as a way to avoid bikeshedding.

hackernews · Ygg2 · Jul 18, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48960155)

**Background**: Bikeshedding, also known as Parkinson's Law of Triviality, describes the tendency for groups to spend disproportionate time on trivial issues while neglecting more important ones. This phenomenon is common in open source communities where discussions can get bogged down on minor details.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Law_of_triviality">Law of triviality - Wikipedia</a></li>
<li><a href="https://thecodersblog.com/parkinson-law-triviality-bikeshedding-art-prioritization-depth-exploration/">Parkinson's Law of Triviality, Bikeshedding ... | The Coders Blog | Home</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the article, with one noting that reversible decisions should simply go with the volunteer's instinct. Another commenter highlighted PHK's creation of MD5crypt, adding historical depth. A few expressed frustration that bikeshedding persists even with modern tools like JIRA.

**Tags**: `#open source`, `#software engineering`, `#bikeshedding`, `#governance`, `#community`

---

<a id="item-6"></a>
## [Anthropic Reverses Course, Makes Claude Fable 5 Permanent](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic announced that Claude Fable 5 will be permanently included in Max and Team Premium subscription plans at 50% of usage limits, reversing its earlier plan to remove the model from subscriptions. The change, effective July 20, 2026, comes in response to competitive pressure from OpenAI's GPT-5.6 Sol and Kimi 3. This strategic reversal ensures that Anthropic's best model remains accessible to subscribers, preventing user churn to competitors offering top-tier models in their subscriptions. It highlights the intense competition in the AI model market, where pricing and access are key battlegrounds. Pro and Team Standard users will retain access to Fable 5 via usage credits and receive a one-time $100 credit. However, users on the $20/month plan still do not get Fable 5 access; only Max ($100/$200 per month) and Team Premium plans include it.

rss · Simon Willison · Jul 18, 06:00

**Background**: Claude Fable 5 is Anthropic's most advanced large language model, part of the Claude Mythos series. Anthropic had originally planned to remove Fable 5 from subscriptions due to compute capacity concerns, making it available only via API. However, the release of GPT-5.6 Sol, which outperforms Fable 5 on coding benchmarks at lower cost, and the emergence of Kimi 3, forced a rethink.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Simon Willison's analysis notes that the competitive pressure from GPT-5.6 Sol and Kimi 3 made Anthropic's original plan untenable. He observes that many users were worried about losing access to Fable 5, and the reversal is a relief, though he questions whether Anthropic will need to reduce training efforts to free up GPUs for serving the model.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#pricing`, `#competition`

---

<a id="item-7"></a>
## [Meta in Talks to Lease AI Compute to Anthropic in $10B Deal](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta is in early negotiations to lease AI computing power from its data centers to Anthropic, with a potential deal valued at $10 billion over two years. Anthropic proposed the arrangement in June 2026, and Meta is currently evaluating it. This deal highlights the acute scarcity of AI compute resources and Meta's strategy to monetize its massive infrastructure investments. If completed, it would provide Anthropic with critical compute capacity while helping Meta offset investor concerns over its $145 billion annual capital expenditure. The deal would involve monthly payments from Anthropic to Meta, with both parties having the option to exit early. Negotiations are still in early stages and may not result in a final agreement.

telegram · zaihuapd · Jul 18, 01:14

**Background**: AI compute scarcity has become a major bottleneck for AI development, with GPU rental prices surging 48% in 60 days in early 2026. Meta plans to invest up to $145 billion in 2026, largely in AI and data centers, and has outlined $600 billion in U.S. infrastructure spending by 2028. Anthropic, founded by former OpenAI employees, develops the Claude series of large language models and focuses on AI safety.

<details><summary>References</summary>
<ul>
<li><a href="https://tomtunguz.com/ai-compute-crisis-2026/">The Beginning of Scarcity in AI | Tomasz Tunguz</a></li>
<li><a href="https://www.rcrwireless.com/20250908/ai-infrastructure/meta-infrastructure">Meta outlines $600 billion US infrastructure plan by 2028</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#Anthropic`, `#cloud computing`, `#infrastructure`

---

<a id="item-8"></a>
## [SpaceX in Talks with Pentagon for AI Computing Deal](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX is negotiating with the Pentagon to provide data center computing power for running AI models, with a potential deal worth tens of billions of dollars. The talks are ongoing and could still fall through. This deal would significantly expand SpaceX's cloud computing business and deepen its ties with the U.S. military, positioning it as a key AI infrastructure provider for national security. It also reflects the Pentagon's accelerating push to adopt AI for defense operations. The Pentagon has already approved SpaceX, Amazon, Google, Microsoft, and Oracle to use AI models in classified environments. SpaceX recently signed similar computing power agreements with Anthropic and Google, and plans to expand its cloud business significantly.

telegram · zaihuapd · Jul 18, 01:44

**Background**: SpaceX has been expanding beyond rocket launches into cloud computing, leveraging its Starlink satellite network and data centers. In 2026, it signed a $30 billion deal with Google to provide 110,000 NVIDIA GPUs for AI computing. The Pentagon is pushing AI to the battlefield edge, requiring rugged, secure computing infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/06/05/technology/spacex-google-deal.html">SpaceX Has $30 Billion Deal to Provide Google With A.I. Computing Power - The New York Times</a></li>
<li><a href="https://www.ibtimes.sg/spacexs-colossus-supercomputer-emerges-pentagons-next-ai-asset-90045">SpaceX's Colossus Supercomputer Emerges as Pentagon's Next AI Asset</a></li>
<li><a href="https://www.militaryaerospace.com/trusted-computing/article/55378097/pentagon-classified-ai-push-expected-to-drive-demand-for-rugged-embedded-computing">Pentagon classified AI push expected to drive demand for rugged embedded computing | Military Aerospace</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#AI`, `#Defense`, `#Cloud Computing`, `#Pentagon`

---

<a id="item-9"></a>
## [TSMC Announces A14 Process Technology for 2028 Production](https://t.me/zaihuapd/42643) ⭐️ 8.0/10

TSMC has announced its next-generation A14 process technology, scheduled to enter production in 2028, promising a 15% speed boost at the same power or a 30% power reduction at the same speed compared to the upcoming N2 node. This roadmap solidifies TSMC's leadership in advanced semiconductor manufacturing, crucial for powering future AI, HPC, and mobile chips. The A14 node's performance and efficiency gains will directly impact the competitiveness of products from TSMC's key customers like Apple, NVIDIA, and AMD. A14 is a full-node shrink from N2, utilizing second-generation GAAFET transistors and TSMC's NanoFlex Pro architecture. TSMC also plans to introduce the intermediate A16 node in late 2026, which offers an 8-10% speed boost or 20% power reduction over N2.

telegram · zaihuapd · Jul 18, 05:00

**Background**: TSMC's N2 node, set for volume production in late 2025, is the company's first to use Gate-All-Around (GAA) transistors, replacing FinFETs. A14 represents the next full node after N2, continuing the trend of dimensional scaling to improve transistor density, performance, and power efficiency. The A16 node, positioned between N2 and A14, introduces backside power delivery for additional performance gains.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_A14">A14 Technology - Taiwan Semiconductor Manufacturing Company ...</a></li>
<li><a href="https://semiwiki.com/wikis/industry-wikis/tsmc-a14-process-technology-wiki/">TSMC A14 Process Technology Wiki - SemiWiki</a></li>
<li><a href="https://pr.tsmc.com/english/news/3228">TSMC Unveils Next-Generation A14 Process at North America ...</a></li>

</ul>
</details>

**Tags**: `#TSMC`, `#semiconductor`, `#chip manufacturing`, `#process technology`, `#A14`

---

<a id="item-10"></a>
## [Trump Administration Plans FINRA-like AI Model Watchdog](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 8.0/10

The Trump administration is considering creating an independent AI oversight body, modeled after the Financial Industry Regulatory Authority (FINRA), to review top AI models for safety. The proposal, led by Treasury Secretary Scott Bessent, is under review by White House Chief of Staff Susie Wiles and aligns with a recent suggestion from Google DeepMind CEO Demis Hassabis. This move addresses Wall Street's cybersecurity concerns and Silicon Valley's dissatisfaction with ad hoc government restrictions, giving both industries a greater role in setting safety standards. If implemented, it would create a formal, industry-funded regulatory framework for frontier AI models, potentially shaping global AI governance. The proposed body would report to the Securities and Exchange Commission (SEC), similar to FINRA's relationship with the SEC. The plan is still in discussion and has not been reviewed by President Trump; details may change. Previously, Anthropic and OpenAI objected to U.S. government requests to modify or delay their latest models.

telegram · zaihuapd · Jul 18, 05:45

**Background**: FINRA is a self-regulatory organization (SRO) that oversees U.S. broker-dealers, operating under SEC supervision. It is funded by the industry it regulates. The proposed AI watchdog would similarly be an independent, industry-funded body with authority to review and potentially restrict high-risk AI models, drawing from the financial sector's regulatory model.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/美国证券法">美国证券法 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/美国金融业监管局/9213493">美国金融业监管局_百度百科</a></li>

</ul>
</details>

**Discussion**: The Telegram channel sharing the news did not include community comments, so no discussion summary is available.

**Tags**: `#AI监管`, `#美国政策`, `#FINRA`, `#AI安全`, `#行业动态`

---

<a id="item-11"></a>
## [San Francisco Orders Apple, Google to Remove 'Nudify' Apps](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 8.0/10

San Francisco City Attorney David Chiu sent letters to Apple and Google ordering them to remove dozens of AI-powered 'nudify' apps from their app stores, which use AI to create non-consensual deepfake nude images. The letters warn that the companies may have profited millions from these apps and face civil penalties. This action marks a significant government intervention holding major tech platforms liable for third-party apps that enable non-consensual deepfake pornography, potentially setting a precedent for platform responsibility. It highlights the growing legal and ethical challenges posed by AI-generated content and the need for stricter content moderation. The Tech Transparency Project had previously warned about these apps in January and April. Apple stated it has removed three apps and terminated related developer accounts, while Google said it has suspended the five named Play Store apps.

telegram · zaihuapd · Jul 18, 08:45

**Background**: Nudify apps use generative AI to alter photos, creating realistic nude images of individuals without their consent, a form of deepfake pornography. Such content has been used for revenge porn and harassment, leading to lawsuits and criminal investigations. Under US law, Section 230 generally protects platforms from liability for third-party content, but this order challenges that immunity by alleging the platforms knowingly profited from harmful apps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://peopleofcolorintech.com/articles/100-plus-nudify-apps-found-on-apple-store-and-google-play/">100-Plus “Nudify” Apps Found On Apple’s App Store And Google Play</a></li>
<li><a href="https://www.daeryunlaw.com/us/practices/detail/online-platform-liability">Online Platform Liability: What Platforms Must Do to Stay Protected</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#deepfakes`, `#content moderation`, `#tech regulation`, `#privacy`

---