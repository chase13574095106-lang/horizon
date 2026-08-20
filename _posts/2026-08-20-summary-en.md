---
layout: default
title: "Horizon Summary: 2026-08-20 (EN)"
date: 2026-08-20
lang: en
---

> From 31 items, 8 important content pieces were selected

---

1. [Malicious Rust crate arrayref executes build-time payload](#item-1) ⭐️ 9.0/10
2. [AliExpress Uses Silent WebAudio to Fingerprint Users and Break Bluetooth Multipoint](#item-2) ⭐️ 8.0/10
3. [Linux 7.2 Released with HDMI 2.1 Support](#item-3) ⭐️ 8.0/10
4. [125M Transformer Autocompletes Piano on iPhone](#item-4) ⭐️ 8.0/10
5. [AI Boosts Chinese Students' Homework Scores 18% but Cuts Exam Scores 20%](#item-5) ⭐️ 8.0/10
6. [Stripe to Acquire OpenRouter for Over $7 Billion](#item-6) ⭐️ 8.0/10
7. [Terence Tao Warns AI Could Trigger Mathematics' Biggest Crisis Since Gödel](#item-7) ⭐️ 8.0/10
8. [Reverse Image Search Service Exposes Millions of Facial Photos](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Malicious Rust crate arrayref executes build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 9.0/10

A malicious version of the popular Rust crate 'arrayref' (version 0.3.10) was published on crates.io and executed a build-time payload that downloaded and ran a backdoor. The Rust Security Response Team verified the attack and deleted the malicious versions, which were online for about 86 minutes. This incident highlights significant supply-chain security risks in the Rust ecosystem, as even widely-used crates can be compromised. It underscores the need for better security measures, such as sandboxing build scripts and improving crates.io's incident response. The malicious crate had a build script that downloaded a malicious payload, and the campaign's infrastructure overlaps with recent DPRK supply chain attacks. Other malicious crates (proc-macro1, proc-macro-en, aovine, arone, aronenao, tinymember) were also deleted.

hackernews · abhisek · Aug 20, 13:23 · [Discussion](https://news.ycombinator.com/item?id=49374269)

**Background**: Rust is a systems programming language known for its safety and performance, and it uses a package manager called Cargo with a central registry, crates.io. Build scripts (build.rs) are executed at compile time, which can be exploited to run arbitrary code, making them a target for supply-chain attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates with...</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref : Significant Overlap... | Wiz Blog</a></li>

</ul>
</details>

**Discussion**: Community comments express frustration with crates.io's handling of the incident, noting the lack of a security advisory and the disappearance of the malicious version without clear indication. There are calls for sandboxing build scripts and a more 'batteries included' approach to reduce dependency bloat, as well as concerns about the high number of transitive dependencies in Rust projects.

**Tags**: `#security`, `#supply-chain`, `#rust`, `#malware`, `#open-source`

---

<a id="item-2"></a>
## [AliExpress Uses Silent WebAudio to Fingerprint Users and Break Bluetooth Multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 8.0/10

AliExpress has been found to silently play WebAudio to fingerprint users' devices, which also disrupts Bluetooth multipoint connections. This technique was detailed in a blog post by laserphile, highlighting a new privacy-invasive method. This matters because it reveals a novel privacy threat that can affect both user tracking and the functionality of Bluetooth devices. It could impact millions of AliExpress users and raises concerns about the ethics of such practices in e-commerce. The silent audio playback is used for WebAudio fingerprinting, which exploits hardware and software differences to create a unique identifier. This playback can interfere with Bluetooth multipoint, causing devices like headphones to switch connections unexpectedly. The technique appears to work even when the tab is not active, and may also allow background running on mobile browsers.

hackernews · emctech · Aug 20, 10:08 · [Discussion](https://news.ycombinator.com/item?id=49372583)

**Background**: WebAudio fingerprinting is a browser identification technique that measures how a browser processes sound using the Web Audio API. Small differences in hardware, operating systems, and browser engines produce slightly different results, allowing websites to use audio processing as a fingerprint component. Bluetooth multipoint is a feature that lets a single Bluetooth headset maintain simultaneous connections to at least two source devices, such as a laptop and smartphone.

<details><summary>References</summary>
<ul>
<li><a href="https://fingerprint.com/blog/audio-fingerprinting/">Audio Fingerprinting : What It Is + How It Works with Web API</a></li>
<li><a href="https://browserinsight.net/blog/audio-fingerprinting">Audio Fingerprinting : How AudioContext Identifies Your Device</a></li>
<li><a href="https://www.bose.com/stories/bluetooth-multipoint">What Is Bluetooth Multipoint and How Do I Use It? | Bose</a></li>
<li><a href="https://www.soundguys.com/bluetooth-multipoint-explained-28601/">What is Bluetooth multipoint ? - SoundGuys</a></li>

</ul>
</details>

**Discussion**: Community members expressed concern and shared personal anecdotes. Some noted that silent audio playback does not trigger the speaker icon, and wondered if it allows background running on mobile. Others reported Bluetooth disruptions with hearing aids and car audio, linking them to AliExpress. One commenter mentioned that Firefox has largely mitigated WebAudio fingerprinting, providing a link for details. Another sarcastically questioned if Apple would remove AliExpress from the App Store given their closed-system privacy stance.

**Tags**: `#privacy`, `#WebAudio`, `#fingerprinting`, `#Bluetooth`, `#security`

---

<a id="item-3"></a>
## [Linux 7.2 Released with HDMI 2.1 Support](https://www.igalia.com/2026/08/19/Linux-72-Released.html) ⭐️ 8.0/10

Linux kernel 7.2 has been released, featuring HDMI 2.1 support and other improvements. The release is notable for its inclusion of cache-aware scheduling, a feature that has been in development for over a year. This release is significant for the open-source community as it brings long-awaited HDMI 2.1 support to the Linux kernel, potentially improving display capabilities for users with modern hardware. It also introduces performance enhancements like cache-aware scheduling, which can benefit a wide range of workloads. HDMI 2.1 support in the kernel enables higher resolutions and refresh rates, but requires certified Ultra High Speed HDMI cables to fully utilize these features. The kernel is also set to be the default in upcoming distributions like Ubuntu 26.10.

hackernews · mariuz · Aug 20, 15:46 · [Discussion](https://news.ycombinator.com/item?id=49376265)

**Background**: HDMI 2.1 is a display interface standard that supports higher bandwidth, enabling features like 4K at 120Hz and 8K at 60Hz. The Linux kernel is the core of many operating systems, and its updates bring new hardware support and performance improvements. Cache-aware scheduling is a technique that optimizes task placement based on CPU cache topology, reducing cache misses and improving performance.

<details><summary>References</summary>
<ul>
<li><a href="https://itsfoss.com/news/linux-kernel-7-2-release/">Linux 7 . 2 Arrives With Cache Aware Scheduling After More Than...</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.2-rc7-Released">Linux 7 . 2 -rc7 Released Following Another Exhausting... - Phoronix</a></li>
<li><a href="https://www.hdmi.org/spec/index">HDMI Technology: Specifications and Programs</a></li>

</ul>
</details>

**Discussion**: The community discussion shows a mix of curiosity and enthusiasm. One user asks about the resolution of the HDMI 2.1 blocker in AMD's open-source driver, while another questions the target audience for such news. Others express excitement about updating their Raspberry Pi 4 and compare HDMI with DisplayPort. Overall, the sentiment is positive, with users appreciating the context provided.

**Tags**: `#Linux`, `#kernel`, `#HDMI 2.1`, `#open source`

---

<a id="item-4"></a>
## [125M Transformer Autocompletes Piano on iPhone](https://simedw.com/2026/08/20/midi-autocomplete/) ⭐️ 8.0/10

A developer trained a 125M-parameter transformer to autocomplete piano performances in real time on an iPhone 15, achieving ~108 notes/sec, and released a free app. The model is prompted by playing a few MIDI notes and continues the performance entirely on-device. This demonstrates a novel application of transformer models to music generation with on-device performance, highlighting the feasibility of running such models on consumer hardware. It could inspire new creative tools for musicians and expand the use of on-device ML beyond text and images. The model advances music one complete note at a time, rather than generating note attributes in multiple passes. The app is free, and the developer is open to questions about the model, training, Core ML, and failed approaches.

hackernews · simedw · Aug 20, 12:04 · [Discussion](https://news.ycombinator.com/item?id=49373456)

**Background**: Transformers have been used for symbolic music generation, such as the Music Transformer, which uses relative attention for modeling musical sequences. Core ML is Apple's framework for on-device machine learning, leveraging the Apple Neural Engine (ANE) for efficient inference. This project applies the 'autocomplete' concept, similar to code completion tools like GitHub Copilot, to music.

<details><summary>References</summary>
<ul>
<li><a href="https://simedw.com/2026/08/20/midi-autocomplete/">Training a 125M-parameter Model to Autocomplete Piano - SimEdw's Blog</a></li>
<li><a href="https://openreview.net/pdf?id=rJe4ShAcF7">Published as a conference paper at ICLR 2019 MUSIC TRANSFORMER:</a></li>
<li><a href="https://hackernoon.com/why-a-fast-core-ml-model-can-still-make-your-iphone-app-feel-slow">Why a Fast Core ML Model Can Still Make Your iPhone... | HackerNoon</a></li>

</ul>
</details>

**Discussion**: Commenters noted parallels to classical composer training and AI design tools, with one pianist seeing value in exploring dead-ends faster. Others asked about data size and training details, while one user found the unexpected continuation of Für Elise disconcerting. A link to an algorithmic melody generation project was also shared.

**Tags**: `#transformer`, `#music generation`, `#on-device ML`, `#Core ML`, `#MIDI`

---

<a id="item-5"></a>
## [AI Boosts Chinese Students' Homework Scores 18% but Cuts Exam Scores 20%](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning) ⭐️ 8.0/10

A study tracking 27,000 Chinese students aged 12-18 found that using AI tools like Doubao increased average homework scores by 18% and reduced time per assignment from 64 to 45 minutes, but exam scores were 20% lower than non-AI users after six months. This highlights a critical trade-off in AI-assisted learning: while AI can improve homework efficiency and scores, it may hinder deep learning and exam performance if used to shortcut understanding. The findings have significant implications for educators, policymakers, and edtech developers in integrating AI responsibly into education. The study found that performance declines were concentrated among students who rushed through homework, while those who used AI as a personal tutor and spent similar time understanding concepts saw no impairment. Another study mentioned in the article showed that university students using chatbots scored higher on tests, with the advantage persisting a week later.

telegram · zaihuapd · Aug 20, 03:58

**Background**: Doubao is a large language model family developed by ByteDance, including capabilities for text generation, image generation, and other AI tasks. The study's results align with broader discussions about AI in education, where tools can provide personalized tutoring but also risk enabling shortcuts that undermine learning. The Economist's coverage adds credibility to these findings, which are relevant to ongoing debates about AI's role in classrooms.

<details><summary>References</summary>
<ul>
<li><a href="https://dku.wang/tool/328.html">豆 包 大 模 型 - 字节跳动推出的 AI ...</a></li>
<li><a href="https://www.sohu.com/a/877733704_121924584">AI教育助力家庭作业：技术革新与个性化学习解析_辅导_工具_孩子</a></li>
<li><a href="https://blog.csdn.net/shejizuopin/article/details/146496489">人工智能教育应用：个性化学习与智能辅导-CSDN博客</a></li>

</ul>
</details>

**Tags**: `#AI in education`, `#student performance`, `#China`, `#edtech`, `#research`

---

<a id="item-6"></a>
## [Stripe to Acquire OpenRouter for Over $7 Billion](https://t.me/zaihuapd/43290) ⭐️ 8.0/10

Stripe has reportedly reached an agreement to acquire OpenRouter for more than $7 billion, according to Bloomberg. The final price may still change, and Stripe declined to comment on the rumor. This acquisition marks a significant move by Stripe into the AI infrastructure space, potentially reshaping how developers access and pay for AI models. It could strengthen Stripe's position in the AI economy and impact the broader developer tools ecosystem. OpenRouter, founded in 2023, provides access to over 400 AI models and claims to serve 8 million developers as of May. The reported price tag is $7.5 billion, according to Banking Dive.

telegram · zaihuapd · Aug 20, 07:00

**Background**: OpenRouter is a platform that offers a unified API for accessing multiple AI models from providers like OpenAI, Anthropic, Google, and Meta, with automatic fallbacks and price/performance routing. Stripe is a major online payments company that has been expanding into AI-related services, and this acquisition would integrate AI model access with payment infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/19/stripe-openrouter-fintech-ai-model-marketplace-.html">Stripe to buy OpenRouter as fintech expands deeper into AI</a></li>
<li><a href="https://www.bankingdive.com/news/stripe-openrouter-acquisition-ai-7-billion/828357/">Stripe , OpenRouter finally strike a deal | Banking Dive</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/stripe-acquires-openrouter-7b-turning-091812340.html?fr=sycsrp_catchall">Stripe Acquires OpenRouter for $7B+, Turning Model Routing Into a...</a></li>

</ul>
</details>

**Tags**: `#acquisition`, `#AI`, `#Stripe`, `#OpenRouter`, `#developer tools`

---

<a id="item-7"></a>
## [Terence Tao Warns AI Could Trigger Mathematics' Biggest Crisis Since Gödel](https://the-decoder.com/terence-tao-says-ai-could-trigger-maths-biggest-crisis-since-godel/) ⭐️ 8.0/10

Terence Tao, in an article for the 2026 International Congress of Mathematicians, warned that AI could lead to a surplus of proofs that no one can fully understand, comparing the situation to the foundational crisis of the early 20th century. He cited the First-Proof project, where in its second round, 7 out of 10 unpublished research problems were deemed solvable by at least one of four AI systems at a cost of tens to hundreds of dollars each. This warning highlights a potential paradigm shift in mathematics, where the focus may move from producing proofs to verifying and understanding them, with implications for how mathematical knowledge is validated and trusted. It could affect mathematicians, AI developers, and the broader scientific community, as AI-generated proofs may challenge traditional notions of rigor and comprehension. The First-Proof project, organized by mathematicians including Lauren Williams, collected 10 unpublished 'lemmas' from leading mathematicians and gave AI systems a week to solve them; collectively, the LLMs solved at least six of ten. Tao argued that a proof that no one can clearly explain should be considered incomplete even if it passes formal verification, emphasizing the importance of human understanding in mathematics.

telegram · zaihuapd · Aug 20, 13:19

**Background**: The early 20th century foundational crisis in mathematics was triggered by paradoxes like Russell's paradox and Gödel's incompleteness theorems, which challenged the consistency and completeness of formal systems. Formal verification uses computational proof assistants to check proofs mechanically, but it does not necessarily provide human-understandable explanations. The First-Proof project is an initiative to evaluate AI's capabilities in research-level mathematics, using unpublished problems to prevent AI from finding solutions online.

<details><summary>References</summary>
<ul>
<li><a href="https://1stproof.org/">First Proof Project</a></li>
<li><a href="https://current.fas.harvard.edu/stories/first-proofs-second-batch-math-problems-test-ai">First Proof’s second batch of math problems test AI | Harvard FAS</a></li>
<li><a href="https://cacm.acm.org/research/formally-verified-mathematics/">Formally Verified Mathematics – Communications of the ACM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#research`, `#proof verification`, `#Terence Tao`

---

<a id="item-8"></a>
## [Reverse Image Search Service Exposes Millions of Facial Photos](https://arstechnica.com/gadgets/2026/08/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/) ⭐️ 8.0/10

A reverse image search service suffered a data breach, exposing a 450 GB database containing over 9 million images of people's faces along with associated personal information such as email addresses, phone numbers, and IP addresses. The service has restricted access to the database, but the full scope and remediation measures remain unclear. This breach is significant because facial images are immutable biometric data, unlike passwords that can be reset. The exposed data could be used for unauthorized identification, tracking, or fraud, posing serious privacy and identity security risks to millions of individuals. The leaked database is approximately 450 GB and contains over 9 million images, with some records including email addresses, phone numbers, and IP addresses. Experts warn that the data could be exploited for identity theft or surveillance, and the incident highlights the risks of storing biometric data without adequate protection.

telegram · zaihuapd · Aug 20, 15:14

**Background**: Reverse image search services allow users to find where an image appears online or identify similar images. Biometric data, such as facial images, is unique and permanent, making it particularly sensitive. Unlike passwords, biometric data cannot be changed if compromised, which is why breaches involving such data raise heightened concerns. The Forbes article notes that biometric data is immutable, and Norton highlights the risks of biometric breaches.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2025/04/25/what-happens-if-biometric-data-is-breached-and-how-to-prevent-it/">What Happens If Biometric Data Is Breached (And How To Prevent It)</a></li>
<li><a href="https://us.norton.com/blog/emerging-threats/biometric-data-breach-database-exposes-fingerprints-and-facial-recognition-data">Biometric data breach : Database exposes fingerprints and... | Norton</a></li>

</ul>
</details>

**Tags**: `#data breach`, `#privacy`, `#biometric data`, `#security`, `#cybersecurity`

---