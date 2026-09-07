---
layout: default
title: "Horizon Summary: 2026-09-07 (EN)"
date: 2026-09-07
lang: en
---

> From 26 items, 6 important content pieces were selected

---

1. [LG Smart TVs Caught Logging Audio and Scanning Networks](#item-1) ⭐️ 8.0/10
2. [Linux Kernel Git Server Overwhelmed by Abusive Crawlers](#item-2) ⭐️ 8.0/10
3. [OpenAI Reveals Coding Agents and RSI as Path to AGI](#item-3) ⭐️ 8.0/10
4. [NVIDIA CEO Declares AGI Arrived with GPT-6 Astra, Trained on 100K NVLink72 Chips](#item-4) ⭐️ 8.0/10
5. [Huawei Releases First New High-Performance Chip in Six Years](#item-5) ⭐️ 8.0/10
6. [China's Top Court Clarifies AI Liability in New Judicial Interpretation](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LG Smart TVs Caught Logging Audio and Scanning Networks](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

An investigation by Gamers Nexus revealed that LG Smart TVs, including the G5 OLED model, actively scan local networks for nearby devices and can capture microphone audio even when the screen is off. The findings were published on YouTube and covered by Notebookcheck and other outlets. This raises serious privacy concerns for the estimated 216 million LG Smart TV users, as the devices may be collecting sensitive data without explicit consent. It highlights broader issues in the smart TV industry regarding data collection and user surveillance, potentially prompting regulatory scrutiny and consumer backlash. Network packet captures using Wireshark showed the TVs scanning the local area network for phones, smartwatches, and other hardware. Tests also indicated that audio logging occurs with the screen off, and LG's terms of service require users to inform household members and guests about potential eavesdropping.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Smart TVs often include voice recognition features and internet connectivity, but users may not realize the extent of data collection. LG's webOS platform is known to collect viewing habits and other data, but this investigation reveals more invasive practices, including local network scanning and audio capture when the TV appears off. Such practices may conflict with privacy laws like wiretap statutes, as third parties in the home have not consented.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/lg-smart-tvs-caught-scanning-networks/">LG Smart TVs Caught Scanning Networks and Logging Audio in ...</a></li>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with screen off and snooping on local devices - Notebookcheck News</a></li>
<li><a href="https://cybernews.com/privacy/up-to-200m-lg-smart-tvs-could-be-secretly-listening-in-on-conversations/">LG smart TVs may log voice commands and scan homes | Cybernews</a></li>

</ul>
</details>

**Discussion**: Community comments express outrage and concern, with users sharing their own mitigation strategies such as disabling network functions or physically unplugging the WiFi/BT chip. Some commenters point out potential legal violations under wiretap laws, while others criticize LG's terms of service for shifting consent responsibility to users.

**Tags**: `#privacy`, `#smart-tv`, `#security`, `#LG`, `#surveillance`

---

<a id="item-2"></a>
## [Linux Kernel Git Server Overwhelmed by Abusive Crawlers](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 8.0/10

Konstantin Ryabitsev, the maintainer of git.kernel.org, reported that abusive crawlers consume more CPU cycles rendering commits as HTML than all legitimate access combined, including git clones. Across 5 geo-distributed nodes, 14 CPU cores are dedicated solely to rendering commits for scrapers at any given time. This highlights a growing problem for large open-source projects and web services: abusive crawlers can impose significant infrastructure costs and degrade performance for legitimate users. It underscores the need for better bot detection and mitigation strategies across the industry. The report specifically mentions that the CPU usage for scrapers exceeds that of all legitimate access, including git clones, which are typically resource-intensive. The 14 CPU cores are spread across 5 geo-distributed nodes, indicating the scale of the issue. The author, Simon Willison, also expresses concern from the perspective of Datasette, which serves many crawlable pages.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository hosting for the Linux kernel, using gitweb to render commits as HTML for web browsing. Web crawlers, including those used by AI companies to scrape data, can overwhelm servers by requesting many pages in a short time. This issue is part of a broader trend of increasing abusive bot traffic on the internet.

<details><summary>References</summary>
<ul>
<li><a href="https://git-scm.com/docs/gitweb">Git - gitweb Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Git">Git - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely includes comments from developers and maintainers sharing similar experiences with abusive crawlers, discussing potential solutions such as rate limiting, CAPTCHAs, and robots.txt compliance. Some may debate the ethics of AI scraping and the responsibility of AI companies to respect server resources.

**Tags**: `#web crawling`, `#open source`, `#infrastructure`, `#security`, `#Linux kernel`

---

<a id="item-3"></a>
## [OpenAI Reveals Coding Agents and RSI as Path to AGI](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI published a piece titled 'Research acceleration: The view inside OpenAI' detailing how coding agents are reshaping their research workflows, alongside a new essay 'An Alien Mind' by Chief Scientist Jakub Pachocki, both discussing recursive self-improvement (RSI) as a route to AGI. The report includes a chart showing a steep rise in daily AI spend per researcher from about $150 in June 2026 to roughly $600 by late August 2026. This is significant because it offers rare insight into how a leading AI lab internally uses its own tools, indicating that agentic engineering has become central to AI research. The discussion of RSI as a new framing for AGI could shape industry discourse and expectations about AI progress. The chart in the report shows a notable acceleration in AI spend per researcher starting in late July 2026, which the author speculates may coincide with internal access to the model later released as GPT-6 Astra. The article notes that 2026 has been the year agentic engineering took off at OpenAI, mirroring broader industry trends.

rss · Simon Willison · Sep 6, 23:57

**Background**: Recursive self-improvement (RSI) refers to a hypothetical scenario where an AI system can improve its own capabilities, potentially leading to an intelligence explosion. Coding agents are AI tools that autonomously write, modify, and debug code, and agentic engineering is an emerging discipline that orchestrates such agents to perform complex tasks with human oversight. OpenAI's discussion of RSI as a new AGI framing suggests a shift in how the company conceptualizes its long-term goals.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/research-acceleration-view-inside-openai/">Research acceleration: The view inside OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/">RSI is the new AGI — and it’s just as hard to pin down</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so no discussion summary is available.

**Tags**: `#OpenAI`, `#AGI`, `#AI research`, `#coding agents`, `#recursive self-improvement`

---

<a id="item-4"></a>
## [NVIDIA CEO Declares AGI Arrived with GPT-6 Astra, Trained on 100K NVLink72 Chips](https://mp.weixin.qq.com/s/PJp4LEoiZPYqz3Mclqr7xg) ⭐️ 8.0/10

NVIDIA CEO Jensen Huang stated that OpenAI's GPT-6 Astra, released last week, marks the official arrival of AGI, and revealed it was trained on approximately 100,000 NVIDIA Grace Blackwell NVLink72 chips. OpenAI describes Astra as a 'generational leap' with state-of-the-art capabilities in computer use, coding, cybersecurity, and science. This declaration from a leading industry figure could accelerate investment and research in AI infrastructure and AGI development. It also highlights the growing importance of massive-scale training systems like NVLink72, potentially shaping the future direction of AI hardware and software. The model is reportedly trained on about 100,000 NVLink72 chips, which are part of NVIDIA's Grace Blackwell architecture. OpenAI's CEO Sam Altman, however, downplayed the term AGI, calling it 'vague' and an 'irrelevant marketing term.'

telegram · zaihuapd · Sep 7, 04:54

**Background**: NVLink72 is a rack-scale system that connects 72 GPUs into a single logical accelerator using NVLink 5.0 fabric, enabling high-bandwidth communication. GPT-6 Astra is OpenAI's latest model, described as their most intelligent and aligned yet, with capabilities across computer use, coding, cybersecurity, and science. AGI (Artificial General Intelligence) refers to AI systems that match or exceed human cognitive abilities across a wide range of tasks, though its definition remains debated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nextpcb.com/blog/nvidia-gb200-nvl72-architecture">NVIDIA GB200 NVL72: PCB & System Architecture Explained</a></li>
<li><a href="https://wandb.ai/onlineinference/genai-research/reports/NVIDIA-Blackwell-GPU-architecture-Unleashing-next-gen-AI-performance--VmlldzoxMjgwODI4Mw">NVIDIA Blackwell GPU architecture : Unleashing next‑gen AI...</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AGI`, `#GPT-6`, `#NVIDIA`, `#OpenAI`, `#AI training infrastructure`

---

<a id="item-5"></a>
## [Huawei Releases First New High-Performance Chip in Six Years](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

On September 7, 2026, Huawei unveiled the Mate XT 2 trifold smartphone in Guangzhou, powered by the new Kirin 9050 Pro chip. This marks Huawei's first new high-performance chip in six years, featuring the industry's first logic folding technology. This release signals Huawei's return to the high-performance chip market after a six-year hiatus, potentially reshaping the competitive landscape in mobile semiconductors. The introduction of logic folding technology could set a new trend in chip design, especially amid ongoing geopolitical restrictions on China's semiconductor industry. The Kirin 9050 Pro is designed by HiSilicon and manufactured by SMIC using an N+3P process. It incorporates logic folding, which stacks logic units in layers within a single chip and adds vertical interconnect channels, reducing signal path length and latency while improving performance.

telegram · zaihuapd · Sep 7, 08:20

**Background**: Logic folding is a semiconductor innovation proposed by Huawei in May 2026 at ISCAS 2026, along with the 'Tao (τ) Law'. It falls under the category of 3D IC and advanced packaging, aiming to continue performance scaling by 'time scaling' instead of traditional 'geometric scaling'. The Kirin 9050 Pro is the first consumer chip to implement this technology, marking a shift from planar to stacked chip design.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zhihu.com/question/2080313467005939789">华为时隔六年再发高性能芯片麒麟9050 Pro，采用逻辑折叠技术，如何看...</a></li>
<li><a href="https://www.guancha.cn/economy/2026_09_07_830304.shtml">华为发布首款采用逻辑折叠技术的麒麟芯片</a></li>
<li><a href="https://baike.baidu.com/item/逻辑折叠技术/67870423">逻辑折叠技术 - 百度百科</a></li>
<li><a href="https://xueqiu.com/7227104507/408385272">华为麒麟9050 Pro芯片技术解析：架构、能效与竞品对比 本文基于公开评...</a></li>
<li><a href="https://www.eet-china.com/news/202609076952.html">华为时隔六年旗舰发布会详解麒麟芯片，麒麟9050 Pro首发“韬定律”技术</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#chip`, `#semiconductor`, `#Kirin`, `#technology`

---

<a id="item-6"></a>
## [China's Top Court Clarifies AI Liability in New Judicial Interpretation](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 8.0/10

On September 7, 2026, China's Supreme People's Court issued a 24-article judicial interpretation on AI-related disputes, covering deepfakes, algorithmic price discrimination, unauthorized AI impersonation, autonomous driving, and intellectual property. The interpretation clarifies that using AI to create identifiable faces or voices without consent may constitute infringement of personality rights, and algorithmic price discrimination that harms consumer rights incurs liability. This is China's first comprehensive judicial interpretation on AI disputes, providing clear legal rules for emerging AI-related harms and setting a precedent for AI regulation. It will affect tech companies, platform operators, and individuals, potentially shaping industry practices and consumer protection standards in China and beyond. The interpretation explicitly addresses 'algorithmic price discrimination' (big data-enabled price discrimination) and 'network doxxing' (人肉搜索) as actionable offenses. It also supports punitive damages for AI impersonation that induces consumption, and regulates AI misuse that infringes privacy rights.

telegram · zaihuapd · Sep 7, 09:32

**Background**: AI technologies like deepfakes and algorithmic pricing have raised legal questions about personality rights, consumer protection, and privacy. In China, existing laws such as the Civil Code and the Personal Information Protection Law provide general principles, but specific judicial guidance was lacking. This interpretation fills that gap by detailing liability rules for AI-related disputes, aligning with global efforts to regulate AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.court.gov.cn/zixun/xiangqing/435431.html">“AI换脸”技术的应用风险及其规制引导 - 中华人民共和国最高人民法院</a></li>
<li><a href="https://finance.sina.com.cn/tech/roll/2025-01-22/doc-inefuhup8228832.shtml">未经同意拿他人肖像AI换脸？法院：侵权！|AI换脸_新浪科技_新浪网</a></li>
<li><a href="https://www.163.com/dy/article/L68UCBPS0519DDQ2.html">被AI换脸、遭“ 网 络 开 盒 ”？最高 法 明确裁判规则</a></li>

</ul>
</details>

**Discussion**: Community comments were not provided in the news item, but based on the search results, discussions likely focus on the interpretation's impact on AI companies and user rights, with some praising the clarity it brings while others may question enforcement challenges.

**Tags**: `#AI regulation`, `#legal`, `#China`, `#deepfakes`, `#algorithmic fairness`

---