---
layout: default
title: "Horizon Summary: 2026-06-04 (EN)"
date: 2026-06-04
lang: en
---

> From 26 items, 9 important content pieces were selected

---

1. [Anthropic open-sources AI framework for vulnerability discovery](#item-1) ⭐️ 8.0/10
2. [Cloudflare Acquires VoidZero, Creator of Vite](#item-2) ⭐️ 8.0/10
3. [Anthropic Details Progress Toward Recursive Self-Improvement](#item-3) ⭐️ 8.0/10
4. [Meta Ships Facial Recognition on Smart Glasses](#item-4) ⭐️ 8.0/10
5. [Gaussian Point Splatting: New Rendering Technique at Siggraph 2026](#item-5) ⭐️ 8.0/10
6. [Google Asks 404 Media to Remove Human-in-the-Loop Pledge](#item-6) ⭐️ 8.0/10
7. [Tiger Brokers Halts New Positions for China Accounts from June 12](#item-7) ⭐️ 8.0/10
8. [Apple's New Siri to Use Google, Nvidia Chips for Cloud AI](#item-8) ⭐️ 8.0/10
9. [AI Agent Traffic Surpasses Human Traffic for First Time](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic open-sources AI framework for vulnerability discovery](https://github.com/anthropics/defending-code-reference-harness) ⭐️ 8.0/10

Anthropic has released an open-source framework for AI-powered vulnerability discovery, providing a reference harness for using Claude models to find security flaws in code. This framework lowers the barrier for security researchers to leverage advanced AI for vulnerability discovery, potentially accelerating the identification of software flaws. However, the community debate highlights concerns about cost, practicality, and the arms race between attackers and defenders. The framework is available on GitHub and includes guidelines for running agents, with estimated costs ranging from hundreds to thousands of dollars depending on the Claude model used (Opus or Mythos). Anthropic has also disclosed that Claude Mythos identified over 23,000 issues across 1,000 open-source projects.

hackernews · binyu · Jun 4, 20:11 · [Discussion](https://news.ycombinator.com/item?id=48403980)

**Background**: AI-driven vulnerability discovery uses large language models to analyze source code for security weaknesses. Anthropic has been developing this capability with its Claude models, and recently announced that Claude Mythos found over 10,000 software flaws. The open-source framework aims to help the community replicate and build upon these results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/coordinated-vulnerability-disclosure">Coordinated vulnerability disclosure for Claude-discovered vulnerabilities \ Anthropic</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/05/26/anthropic-project-glasswing-update/">Anthropic: Claude Mythos identified 10,000+ software flaws - Help Net Security</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some compared the framework to a 'shop jig' that researchers can customize, while others questioned its cost-effectiveness and noted that attackers have access to the same tools, making it an arms race. There was also a brief discussion about broken GitHub links.

**Tags**: `#AI`, `#security`, `#open-source`, `#vulnerability discovery`, `#Anthropic`

---

<a id="item-2"></a>
## [Cloudflare Acquires VoidZero, Creator of Vite](https://blog.cloudflare.com/voidzero-joins-cloudflare/) ⭐️ 8.0/10

Cloudflare has acquired VoidZero, the company behind the popular JavaScript build tool Vite, as announced on June 4, 2026. The acquisition aims to integrate VoidZero's Rust-based tooling into Cloudflare's Workers platform. This acquisition signals a major shift in the JavaScript tooling landscape, as Vite is used by millions of developers weekly. It also raises questions about the sustainability of open-source projects that rely on acquisition as a business model. VoidZero's tooling is built in Rust for high performance, and Cloudflare plans to make it a core part of its AI-native web development platform. The acquisition includes the entire VoidZero team, and the company's open-source projects will remain free and open-source.

hackernews · coloneltcb · Jun 4, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48398055)

**Background**: Vite is a next-generation frontend build tool that provides fast development server startup and hot module replacement. It has become a cornerstone of modern web development, with over 130 million weekly npm downloads. VoidZero was founded by Evan You, the creator of Vue.js, and focused on improving JavaScript developer productivity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-voidzero-to-build-the-future-of-the-ai-native-web/">Cloudflare Acquires VoidZero to Build the Future of the AI-Native Web</a></li>

</ul>
</details>

**Discussion**: Community comments express unease about the acquisition, with some fearing that Cloudflare's control may alter Vite's direction despite promises of continuity. Others question the business model of building popular open-source tools only to be acquired, and note that Cloudflare's platform has usability issues.

**Tags**: `#acquisition`, `#Vite`, `#Cloudflare`, `#open-source`, `#JavaScript`

---

<a id="item-3"></a>
## [Anthropic Details Progress Toward Recursive Self-Improvement](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 8.0/10

Anthropic published a blog post detailing how AI systems are increasingly taking over parts of the AI development cycle, moving toward recursive self-improvement where AI can autonomously improve its own code. This represents a significant step toward artificial general intelligence (AGI) and could accelerate AI progress dramatically, but it also raises serious safety concerns about loss of human control and unforeseen consequences. Anthropic claims AI systems now write most of their code and can continuously improve, though community comments note frequent API outages and throttling that contradict the narrative of seamless self-improvement.

hackernews · meetpateltech · Jun 4, 16:20 · [Discussion](https://news.ycombinator.com/item?id=48400842)

**Background**: Recursive self-improvement (RSI) is a concept where an AI system rewrites its own code to become more intelligent, potentially leading to an intelligence explosion. Anthropic is a leading AI safety company that has recently faced criticism for dropping some safety pledges while pursuing advanced capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/">Anthropic Drops Flagship Safety Pledge - TIME</a></li>

</ul>
</details>

**Discussion**: Community comments are skeptical, with users pointing out that Anthropic's services suffer from regular outages and high resource usage, undermining claims of autonomous improvement. Some question the compatibility of pursuing RSI at full speed with Anthropic's stated safety goals, drawing analogies to building nuclear weapons during peacetime.

**Tags**: `#AI safety`, `#recursive self-improvement`, `#Anthropic`, `#machine learning`, `#software engineering`

---

<a id="item-4"></a>
## [Meta Ships Facial Recognition on Smart Glasses](https://www.buchodi.com/meta-glasses-facial-recognition/) ⭐️ 8.0/10

Meta has deployed facial recognition technology on its Ray-Ban smart glasses, enabling real-time identification of strangers. This feature was initially demonstrated by Harvard students who modified the glasses, and Meta has now officially integrated it. This move reignites privacy and ethical debates, as always-on cameras with facial recognition pose risks for abuse, surveillance, and consent. It also highlights the tension between accessibility benefits (e.g., for prosopagnosia) and privacy rights. The glasses require the wearer to activate the AI assistant to ask questions or take photos, but the camera is always facing forward. Legal challenges are expected under laws like Illinois' Biometric Information Privacy Act (BIPA).

hackernews · buchodi · Jun 4, 19:36 · [Discussion](https://news.ycombinator.com/item?id=48403588)

**Background**: Facial recognition technology identifies individuals by analyzing facial features. Meta's smart glasses, developed with Ray-Ban, have a built-in camera and AI assistant. Previous attempts like Google Glass faced backlash over privacy concerns, leading to strict developer terms banning facial recognition apps.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gblock.app/articles/meta-smart-glasses-facial-recognition-name-tag">Meta Wants to Put Facial Recognition in Your Smart Glasses</a></li>
<li><a href="https://indianexpress.com/article/technology/tech-news-technology/meta-add-facial-recognition-technology-smart-glasses-10530784/">Meta plans to add facial recognition technology to its smart glasses</a></li>
<li><a href="https://www.wired.com/story/meta-ray-ban-oakley-smart-glasses-no-face-recognition-civil-society/">Meta Is Warned That Facial Recognition Glasses Will Arm ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some wished for an offline version for accessibility (e.g., prosopagnosia), while others proposed countermeasures like IR LEDs to block facial recognition. A user noted the legal risks under BIPA, predicting lawsuits in Chicago.

**Tags**: `#facial recognition`, `#privacy`, `#smart glasses`, `#Meta`, `#ethics`

---

<a id="item-5"></a>
## [Gaussian Point Splatting: New Rendering Technique at Siggraph 2026](https://momentsingraphics.de/Siggraph2026.html) ⭐️ 8.0/10

A new rendering technique called Gaussian Point Splatting was presented at Siggraph 2026, building on the foundation of 3D Gaussian Splatting (3DGS) introduced in 2023. This technique could offer a novel approach for real-time 3D rendering in games and other applications, potentially providing predictable performance and unique visual quality. The technique is compared to mesh splatting, with some commenters suggesting mesh splatting may produce higher quality for sharp features due to triangles, while gaussians may struggle with such details.

hackernews · ibobev · Jun 4, 10:48 · [Discussion](https://news.ycombinator.com/item?id=48396792)

**Background**: Gaussian splatting is a volume rendering technique that directly renders volume data without converting to surface primitives. 3D Gaussian Splatting (3DGS), introduced at SIGGRAPH 2023, became a faster alternative to NeRF for novel view synthesis. Gaussian Point Splatting appears to be a further evolution of this approach.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://leeyngdo.github.io/blog/computer-graphics/2024-04-09-gaussian-splatting/">[Graphics] Gaussian Splatting</a></li>
<li><a href="https://poly.cam/tools/gaussian-splatting">3D Gaussian Splatting | Polycam</a></li>

</ul>
</details>

**Discussion**: Commenters expressed interest in seeing AAA games adopt such methods, with one drawing a parallel to the 1994 game Ecstatica that used ellipsoid-based rendering. Others discussed the difficulty of finding tutorials for classic point splatting due to Gaussian Splatting dominating search results, and compared Gaussian Point Splatting to mesh splatting.

**Tags**: `#computer graphics`, `#rendering`, `#gaussian splatting`, `#Siggraph`, `#point cloud`

---

<a id="item-6"></a>
## [Google Asks 404 Media to Remove Human-in-the-Loop Pledge](https://simonwillison.net/2026/Jun/4/a-slightly-different-version/#atom-everything) ⭐️ 8.0/10

Google asked 404 Media to publish a revised version of a statement that removed the phrase "it's critical that we maintain humans in the loop" after employees internally memed about the company's AI quality. This reveals Google's internal acknowledgment of AI quality issues and a concerning shift away from human oversight, raising questions about AI ethics and transparency in the industry. The original statement was part of 404 Media's story about Google employees sharing memes criticizing the company's AI. Google's spokesperson requested the change after publication, and 404 Media complied while noting the alteration.

rss · Simon Willison · Jun 4, 16:38

**Background**: Human-in-the-loop (HITL) is a principle where humans actively participate in AI system operation, supervision, or decision-making to ensure accuracy and reliability. 404 Media is an independent, reporter-owned tech news outlet known for investigative reporting on AI, hacking, and internet culture.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/human-in-the-loop">What Is Human In The Loop (HITL)? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/404_Media">404 Media</a></li>
<li><a href="https://www.404media.co/">404 Media</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#google`, `#ai`, `#journalism`, `#accountability`

---

<a id="item-7"></a>
## [Tiger Brokers Halts New Positions for China Accounts from June 12](https://t.me/zaihuapd/41762) ⭐️ 8.0/10

Tiger Brokers announced that starting June 12, 2026, it will suspend new positions and additional deposits for existing mainland China accounts, allowing only sell and close orders. This move signals intensified regulatory enforcement on cross-border securities services, directly affecting Chinese investors using offshore brokers and potentially reshaping the industry landscape. The suspension applies to all securities types, including stocks, and also halts inbound fund transfers while outbound transfers remain unaffected. Existing assets are safe and can still be held or sold.

telegram · zaihuapd · Jun 4, 07:51

**Background**: Chinese regulators have been cracking down on illegal cross-border securities activities, requiring brokers like Tiger Brokers and Futu to comply. This follows a two-year rectification campaign and aligns with similar actions by other brokers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yicai.com/news/103212592.html">老虎国际：6月12日起，暂停存量投资者账户在中国境内所有品种的新开仓...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2045412101003510680">老虎国际：6月12日起，暂停存量投资者账户在中国境内所有品种的新开仓...</a></li>
<li><a href="https://www.21jingji.com/article/20260603/herald/03ff36ce3e6fcf953603dab83387142d.html">21jingji.com/article/20260603/herald/03ff36ce3e6fcf953603dab...</a></li>

</ul>
</details>

**Tags**: `#finance`, `#regulation`, `#cross-border securities`, `#Tiger Brokers`, `#China`

---

<a id="item-8"></a>
## [Apple's New Siri to Use Google, Nvidia Chips for Cloud AI](https://www.macrumors.com/2026/06/04/apple-siri-rely-on-google-nvidia-chips/) ⭐️ 8.0/10

Apple plans to use Google data centers with Nvidia Blackwell B200 chips to process cloud-based AI queries for the upcoming Siri revamp, expected in September 2026. This marks a departure from Apple's tradition of using in-house hardware. This strategic shift highlights Apple's need to catch up in AI, as its own servers were too slow for running Gemini models. It also strengthens the partnership between Apple, Google, and Nvidia, reshaping the AI infrastructure landscape. The Nvidia Blackwell B200 GPU delivers up to 20 petaflops of FP4 compute, and the deal reportedly costs Apple around $1 billion per year. Apple will also use Nvidia hardware encryption to protect user data during cloud processing.

telegram · zaihuapd · Jun 4, 11:37

**Background**: Apple has historically designed its own chips (e.g., A-series, M-series) and relied on on-device processing for privacy. However, advanced AI tasks require cloud computing, and Apple's in-house servers reportedly struggled with the performance demands of Google's Gemini models. The partnership with Google and Nvidia allows Apple to leverage existing high-performance AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://9to5mac.com/2026/06/03/report-details-apples-plan-to-use-nvidia-chips-for-the-gemini-powered-siri/">Report details Apple's plan to use Nvidia chips for the Gemini-powered Siri</a></li>
<li><a href="https://tech-insider.org/apple-google-gemini-siri-deal-1-billion-2026/">Apple's $1B Gemini Deal: Google AI Replaces Siri [2026]</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#AI`, `#Nvidia`, `#Google`

---

<a id="item-9"></a>
## [AI Agent Traffic Surpasses Human Traffic for First Time](https://www.tomshardware.com/tech-industry/artificial-intelligence/bots-have-now-passed-human-traffic-online-cloudflare-boss-laments-says-agentic-traffic-wasnt-expected-to-eclipse-real-people-until-next-year) ⭐️ 8.0/10

Cloudflare reported that AI agent traffic has exceeded human traffic for the first time, accounting for 57.5% of web requests, earlier than CEO Matthew Prince's 2027 prediction. This milestone marks a fundamental shift in web traffic composition, with implications for website optimization, security, and the economics of online content. The AI agents differ from traditional crawlers by performing multi-step tasks like price comparison and customer service, though humans still dominate in total usage time due to streaming and social media.

telegram · zaihuapd · Jun 4, 16:49

**Background**: Web traffic has long been dominated by human users, but the rise of AI agents—automated programs that mimic human browsing—has accelerated. Cloudflare's data provides empirical evidence of this trend, which was previously only projected.

<details><summary>References</summary>
<ul>
<li><a href="https://piunikaweb.com/2026/06/04/cloudflare-bot-traffic-overtakes-humans/">Bot traffic overtakes humans ahead of 2027 timeline Cloudflare...</a></li>
<li><a href="https://independentwp.com/blog/bot-traffic-exceeds-human-traffic/">Bot Traffic Now Exceeds Human Traffic - Here's How It Affects Your...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#web traffic`, `#Cloudflare`, `#bots`, `#automation`

---