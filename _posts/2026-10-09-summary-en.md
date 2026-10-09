---
layout: default
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 28 items, 7 important content pieces were selected

---

1. [OpenAI Adds Ultrafast Mode to GPT-6.1 Sol API](#item-1) ⭐️ 9.0/10
2. [Chinese Scientists Build World's First Nuclear Clock](#item-2) ⭐️ 8.0/10
3. [Stripe Agrees to Acquire OpenRouter, the 400+ Model AI Gateway](#item-3) ⭐️ 8.0/10
4. [Manus 2.0 Launches with Cascade Agent Framework and New App Cue](#item-4) ⭐️ 8.0/10
5. [Mistral Releases Mistral Large 4, a 1-Trillion-Parameter Open-Weight Model](#item-5) ⭐️ 8.0/10
6. [US Suspends Microsoft from Green Card Program Over Fraud Claims](#item-6) ⭐️ 8.0/10
7. [SpaceX to Acquire Nationwide US Low-Band Spectrum Licenses](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Adds Ultrafast Mode to GPT-6.1 Sol API](https://developers.openai.com/api/docs/changelog) ⭐️ 9.0/10

OpenAI has introduced an Ultrafast service tier for GPT-6.1 Sol in the Responses API (v1/responses), delivering up to roughly 8x faster generation than the Standard tier. It is available to all API users at 6x the Standard price, with short-context pricing of about $12 per million input tokens, $0.60 for cached input, and $60 for output. This gives developers building latency-sensitive or agentic applications a way to trade cost for speed without switching models, which could meaningfully improve responsiveness in real-time and multi-tool-call workflows. However, the 6x price premium may limit adoption to use cases where shaving latency is worth the extra spend. Ultrafast is described as the fastest service tier in the OpenAI API, broadly available for GPT-6 Astra and GPT-6.1 Sol with preview access for GPT-5.6 Sol. OpenAI strongly recommends using WebSockets, especially for agentic applications making many rapid tool calls, since without a persistent connection network overhead can erode the latency gains.

telegram · zaihuapd · Oct 9, 00:00

**Background**: The Responses API (v1/responses) is OpenAI's newer endpoint for calling models, supporting built-in tools, state management, and streaming, and positioned as an evolution beyond the older Chat Completions interface. Service tiers like Flex, Standard, Priority, and Batch let developers route traffic based on the trade-off between cost and latency. Ultrafast is the newest and fastest tier, aimed at workloads where generation speed is the top priority.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/ultrafast-mode">Ultrafast mode | OpenAI API</a></li>
<li><a href="https://www.latent.space/p/ainews-openai-devday-2026-dots-61">[AINews] OpenAI DevDay 2026: Dots, 6 . 1 Sol , Ultrafast , Decisions...</a></li>
<li><a href="https://apidog.com/blog/openai-responses-api/">How to use the OpenAI Responses API</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#API`, `#GPT-6.1`, `#Ultrafast`, `#LLM`

---

<a id="item-2"></a>
## [Chinese Scientists Build World's First Nuclear Clock](https://www.nature.com/articles/s41586-026-11122-1) ⭐️ 8.0/10

Researchers at Tsinghua University have developed the world's first nuclear clock, using a self-built 148 nm continuous-wave vacuum ultraviolet laser and a thorium-229 doped calcium fluoride crystal, and demonstrated stable operation. The results were published in Nature. This is the first successful realization of a nuclear clock, which could become a next-generation time and frequency standard and serve high-precision timing applications such as satellite navigation and deep-space exploration. It also opens a new frontier for testing fundamental physics, including possible variations of fundamental constants. The clock uses the exceptionally low-energy, long-lived isomeric state of thorium-229 as its ticking reference, which requires vacuum ultraviolet light at about 148 nm. The team achieved stable operation by stabilizing a continuous-wave laser to the nuclear excitation, and the thorium-doped calcium fluoride crystal provides a solid-state platform for this spectroscopy.

telegram · zaihuapd · Oct 8, 05:19

**Background**: Atomic clocks, which underpin GPS and global timekeeping, use transitions between electron energy levels in atoms as their reference. A nuclear clock instead uses quantum states inside the atomic nucleus, which are far less sensitive to external disturbances and could therefore be more precise and stable. Thorium-229 is uniquely suited for this because it has an unusually low-energy excited state that can be reached with vacuum ultraviolet lasers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11084-4">A thorium-229 optical nuclear clock with feedback loop | Nature</a></li>
<li><a href="https://thoriumclock.eu/">Webpage of the Thorium Nuclear clock research project</a></li>
<li><a href="https://physics.aps.org/articles/v19/19">Physics - A Laser Built for Nuclear Timekeeping</a></li>

</ul>
</details>

**Tags**: `#nuclear clock`, `#thorium-229`, `#timekeeping`, `#physics`, `#Nature`

---

<a id="item-3"></a>
## [Stripe Agrees to Acquire OpenRouter, the 400+ Model AI Gateway](https://t.me/zaihuapd/44275) ⭐️ 8.0/10

Stripe announced on August 19, 2026 that it has agreed to acquire OpenRouter, an AI model gateway and routing platform that dynamically distributes requests across more than 400 models from over 80 providers based on task complexity, price, speed, and reliability. Reports indicate the deal is worth roughly $7.5 billion, though Stripe has not officially disclosed the price. The acquisition places a major payments company at the center of AI model access and billing, potentially reshaping how developers and enterprises route, meter, and pay for inference across many providers. It also signals continued consolidation in the AI infrastructure layer, where gateways are becoming strategic control points for cost and vendor management. OpenRouter's value proposition is a single unified API endpoint that abstracts away dozens of provider integrations, enabling failover, cost optimization, and quality-based routing. The reported $7.5 billion price tag is a substantial step up for a routing layer, and the deal remains subject to closing conditions, so no technical or product changes have been announced yet.

telegram · zaihuapd · Oct 8, 05:52

**Background**: OpenRouter is an AI model gateway, sometimes called an LLM router, that sits between an application and many model providers. Instead of integrating each vendor's API separately, developers send requests to one endpoint and OpenRouter decides which underlying model to use. Stripe is best known as a programmable payments company, and buying OpenRouter extends its infrastructure reach into how AI usage is metered and billed.

<details><summary>References</summary>
<ul>
<li><a href="https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter">Stripe agrees to acquire OpenRouter to help businesses ...</a></li>
<li><a href="https://techcrunch.com/2026/08/19/stripe-didnt-really-buy-openrouter-because-of-the-singularity/">Stripe didn't really buy OpenRouter because of the ...</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Acquisition`, `#OpenRouter`, `#Stripe`, `#Model Routing`

---

<a id="item-4"></a>
## [Manus 2.0 Launches with Cascade Agent Framework and New App Cue](https://t.me/zaihuapd/44276) ⭐️ 8.0/10

Manus 2.0 was officially released on September 28, 2026, introducing the self-developed agent framework Cascade, a cloud computer, and event-triggered automation. In company-reported tests, it reduced token consumption by 23.2%, shortened task completion time by 28.2%, and lowered running costs by 32%. This is a major release from a widely-used AI agent platform, and the significant efficiency gains could reshape how developers and businesses deploy autonomous agents. The new Cascade framework and Cue app may accelerate the shift from single-task AI agents to continuously running, multi-capability workspaces. The desktop application has been upgraded to Manus Studio, adding a video editor, game development tools, and Computer Use capabilities. A separate app called Cue lets users configure email, phone, wallet, and computer access for personal agents, and is currently available for free via invitation code.

telegram · zaihuapd · Oct 8, 06:43

**Background**: Manus is an autonomous AI agent developed by Butterfly Effect, a company founded in China and based in Singapore. It handles tasks such as building custom web tools, content localization, data cleaning, and automated workflows, and uses a credit-based system for charging. Cascade is Manus's in-house agent harness that keeps a project lightweight and brings in specialized capabilities only when needed.

<details><summary>References</summary>
<ul>
<li><a href="https://manus.im/blog/introducing-manus-2-0">Introducing Manus 2.0</a></li>
<li><a href="https://letsdatascience.com/news/manus-introduces-manus-20-with-cascade-architecture-and-new-53ecf751">Manus Introduces Manus 2.0 With Cascade Architecture and New ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent)</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Manus`, `#agent framework`, `#automation`, `#cloud computing`

---

<a id="item-5"></a>
## [Mistral Releases Mistral Large 4, a 1-Trillion-Parameter Open-Weight Model](https://t.me/zaihuapd/44279) ⭐️ 8.0/10

On October 6, French AI company Mistral released Mistral Large 4, nicknamed "le Chonk," a 1-trillion-parameter model it calls one of the world's strongest open-source models. The model is currently available in public preview to developers, security leaders, and government agencies, with broader access planned for later this month. A 1-trillion-parameter open-weight model from a European lab intensifies competition with US and Chinese frontier labs, and its focus on cybersecurity, coding, manufacturing, and finance signals Mistral's push into enterprise and government markets. If the open weights arrive as promised, it could become one of the largest openly downloadable models available. Mistral says the model was trained for two months on 4,000 NVIDIA Grace Blackwell GPUs, and it is natively multimodal and uses a mixture-of-experts architecture with 1 trillion total parameters. Mistral acknowledges it still trails frontier models in areas such as coding, and the open weights are slated to follow at the end of October.

telegram · zaihuapd · Oct 8, 10:08

**Background**: Mistral AI is a French startup known for releasing open-weight large language models that anyone can download and run, in contrast to closed models like OpenAI's GPT-4. Parameter count roughly measures a model's size and capacity, and trillion-parameter models are among the largest ever built. NVIDIA's Grace Blackwell is the company's latest GPU platform, combining Blackwell GPUs with Arm-based Grace CPUs and designed specifically for large-scale AI training and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/mistral-large-4/">Introducing Mistral Large 4 | Mistral</a></li>
<li><a href="https://officechai.com/ai/mistral-large-4-le-chonk/">Mistral Releases Mistral Large 4 ( Le Chonk ), Says It's The Top Open...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Mistral`, `#large language models`, `#open source`, `#AI`, `#model release`

---

<a id="item-6"></a>
## [US Suspends Microsoft from Green Card Program Over Fraud Claims](https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea) ⭐️ 8.0/10

The Trump administration has suspended Microsoft from participating in the foreign labor green card program, alleging fraud. Vice President JD Vance said at a press conference that Microsoft laid off 6,000 American workers last year while obtaining 6,300 H-1B visas and nearly 3,000 green cards, calling it "the company that has exploited the system the most." This action signals a significant escalation in the Trump administration's crackdown on corporate immigration practices, potentially setting a precedent that could affect how major tech companies hire foreign talent. It may disrupt Microsoft's ability to sponsor green cards for current and future employees, and could prompt other tech giants to reassess their immigration strategies. Vance accused Microsoft of posting fake job ads to prove no American workers were available before replacing them with foreign labor, and also named nine universities including Harvard, Yale, and MIT for alleged abuse of the J-1 visa program. Microsoft has not yet responded to the allegations.

telegram · zaihuapd · Oct 9, 00:00

**Background**: The H-1B visa is a temporary, non-immigrant visa that allows US companies to hire highly skilled foreign workers in specialty occupations. The green card labor certification (PERM) process requires employers to prove that no qualified US workers are available for a permanent position before sponsoring a foreign national for an EB-2 or EB-3 employment-based green card. The J-1 visa is an exchange visitor program for work-and-study-based cultural exchanges. This suspension means Microsoft can no longer file PERM applications, which is the first step in sponsoring employees for green cards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dol.gov/agencies/eta/foreign-labor/programs/permanent">Permanent Labor Certification - U.S. Department of Labor</a></li>
<li><a href="https://greencardtracker.com/articles/perm-labor-certification">PERM Labor Certification: Step-by-Step Employer Guide (2026)</a></li>
<li><a href="https://www.aljazeera.com/economy/2025/1/16/bannon-vs-musk-how-trumps-u-turn-on-h-1b-visas-has-split-maga">Bannon vs Musk: How Trump’s U-turn on H - 1 B visas has... | Al Jazeera</a></li>

</ul>
</details>

**Tags**: `#immigration`, `#H-1B`, `#Microsoft`, `#policy`, `#tech industry`

---

<a id="item-7"></a>
## [SpaceX to Acquire Nationwide US Low-Band Spectrum Licenses](https://x.com/SpaceX/status/2108291133025698301) ⭐️ 8.0/10

SpaceX announced an agreement to acquire a nationwide portfolio of low-band spectrum licenses, which the company says will pave the way for Starlink to become a major US mobile carrier. Combined with its Gen2 constellation, SpaceX claims Starlink Mobile can deliver high-speed mobile broadband to Americans no matter where they are. This is a major strategic move that could disrupt the US telecom industry by turning Starlink from a satellite internet provider into a full-fledged mobile carrier competing with AT&T, Verizon, and T-Mobile. Low-band spectrum is prized for its wide coverage and wall-penetrating properties, making it the key enabler for nationwide direct-to-cell service. Low-band spectrum travels long distances and penetrates buildings well, but offers lower capacity than mid-band or high-band airwaves, so it is typically used for broad coverage rather than peak speeds. SpaceX's planned Gen2 constellation includes nearly 30,000 satellites, with two-thirds in very low Earth orbit below 450 km, which would support the direct-to-cell service.

telegram · zaihuapd · Oct 9, 01:04

**Background**: Low-band spectrum refers to radio frequencies typically below 1 GHz, which carriers use to blanket large areas with mobile coverage because signals travel far and penetrate walls. Starlink is SpaceX's satellite internet service, and its direct-to-cell technology lets ordinary smartphones connect to satellites acting like cell towers in space. Acquiring nationwide low-band licenses would give SpaceX the terrestrial spectrum rights needed to operate as a full mobile carrier rather than relying solely on partnerships.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/technology/last-critical-piece-spacex-secures-spectrum-deal-challenge-big-telecom">"Last Critical Piece": SpaceX Secures Spectrum Deal To... | ZeroHedge</a></li>
<li><a href="https://www.telecomreview.com/index.php/articles/reports-and-coverage/4938-over-500-operators-now-hold-spectrum-licenses-for-low-band-lte-and-5g">Over 500 operators now hold spectrum licenses for low - band LTE...</a></li>
<li><a href="https://www.researchgate.net/figure/hr-mean-Starlink-Gen2-satellites-visible-by-latitude-in-line-of-sight-but-not_fig1_395437535">Figure 1. 24 hr mean Starlink Gen 2 satellites visible by latitude in...</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starlink`, `#spectrum`, `#telecom`, `#satellite-internet`

---