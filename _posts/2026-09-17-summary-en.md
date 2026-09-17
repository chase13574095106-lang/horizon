---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 28 items, 4 important content pieces were selected

---

1. [Xiaomi launches live RL post-training dashboard for MiMo 2.6](#item-1) ⭐️ 8.0/10
2. [Hackers Breach Flock Surveillance Camera, Exposing Hardcoded Credentials](#item-2) ⭐️ 8.0/10
3. [1.7 Million Low-Quality Chinese Casino Sites Hide APT Attack Infrastructure](#item-3) ⭐️ 8.0/10
4. [Sina Cloud SAE shuts down permanently, early Bilibili source files lost](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Xiaomi launches live RL post-training dashboard for MiMo 2.6](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

Xiaomi has published a public, live dashboard that streams the reinforcement-learning post-training metrics of its MiMo-V2.6-Pro and MiMo-V2.6-Flash models directly from the trainer's logs. The dashboard shows reward curves and evaluation results in real time as the post-training run progresses. Publishing a live training dashboard is unusual for a major AI lab and offers an unusual degree of transparency into how a frontier model is refined after pre-training. It could pressure other model providers to share similar training telemetry and gives developers early insight into MiMo 2.6's capabilities. The dashboard tracks the reinforcement-learning runs of both the Pro and Flash variants of MiMo 2.6, streaming reward curves and evaluation metrics live from the trainer's logs. Community benchmarks cited in discussion show MiMo-V2.5-Pro scoring 19% on DeepSWE 1.1, well behind Fable (70%), Kimi K3 (69%), and Astra (74%), though users report strong real-world coding results.

hackernews · krackers · Sep 16, 20:09 · [Discussion](https://news.ycombinator.com/item?id=49732270)

**Background**: MiMo is Xiaomi's family of large language models, first released in April 2025 with the MiMo-7B model and now available to developers via API. Post-training refers to the phase after pre-training where techniques such as reinforcement learning from human feedback (RLHF) and other RL methods are used to align and improve a model's behavior. Training dashboards are commonly used internally by ML teams to monitor metrics like reward curves, but making one public is rare.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL - mimo.xiaomi.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training - PyTorch</a></li>

</ul>
</details>

**Discussion**: Commenters were largely positive: one software engineer reported very high ROI using MiMo-V2.5, calling the cost unbelievably low and quality comparable to Anthropic models from late last year, while another described the next model as a capable but somewhat forgetful senior engineer. Others noted the transparency is unusual and wondered why other model providers don't do the same, with one commenter framing open-source AI progress as a looming threat to closed labs' IPOs.

**Tags**: `#AI`, `#machine-learning`, `#model-training`, `#Xiaomi`, `#dashboard`

---

<a id="item-2"></a>
## [Hackers Breach Flock Surveillance Camera, Exposing Hardcoded Credentials](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

Security researchers discovered that Flock Safety surveillance cameras contain hardcoded API keys and plaintext-stored credentials, allowing attackers with physical access to extract sensitive authentication material. Distributed Denial of Secrets has published partition images of the compromised cameras, and the findings were reported in collaboration with 404 Media. This breach highlights systemic security failures in widely-deployed surveillance infrastructure used by law enforcement and municipalities across the United States, potentially exposing sensitive ALPR data and undermining public trust in these systems. It raises urgent questions about the security architecture of IoT devices deployed in public spaces where physical access is trivially available to anyone. The vulnerability involved a hardcoded API key rather than a hardcoded admin password, but the API key could be used to request credentials stored in plaintext that appear to grant access to Flock's servers. Flock's Vulnerability Disclosure Policy contains a significant carveout that excludes cases where researchers must 'interact' with the device or download its data, effectively discouraging meaningful security research.

hackernews · driverdan · Sep 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**Background**: Flock Safety is a privately held American company founded in 2017 that manufactures automated license plate recognition (ALPR) cameras, video surveillance systems, and gunfire detection technology used by law enforcement agencies and communities across the US. Hardcoded credentials (classified as CWE-798) are among the most consistently flagged security weaknesses in enterprise assessments, as they persist in code history and are easily discoverable through firmware analysis. IoT cameras are particularly vulnerable because they often lack support for enterprise security protocols like 802.1X and cannot run endpoint compliance agents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard-coded Credentials (4.20)</a></li>
<li><a href="https://www.guidepointsecurity.com/blog/iot-camera-security-evolving-threats/">IoT Camera Security: The Fixable Threat You Might Not See Coming | GuidePoint Security</a></li>

</ul>
</details>

**Discussion**: Commenters strongly criticized Flock's security practices, with one calling hardcoded credentials 'a sign of total incompetence' and another describing Flock's Vulnerability Disclosure Policy as designed to create an appearance of responsible security rather than genuinely learn about vulnerabilities. Others pointed to 'pure laziness' and 'reduced time to market' priorities, noting that deploying unsecured hardware in public spaces means the threat model must include local physical access. One commenter shared that Distributed Denial of Secrets published the partition images and linked to a parallel discussion on 404 Media's article.

**Tags**: `#security`, `#vulnerability`, `#surveillance`, `#IoT`, `#privacy`

---

<a id="item-3"></a>
## [1.7 Million Low-Quality Chinese Casino Sites Hide APT Attack Infrastructure](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

Security researchers have identified roughly 1.7 million low-quality Chinese casino and adult websites that are being used as covert infrastructure for malware distribution and command-and-control (C2) operations. Since 2023, China-aligned APT groups have hidden C2 domains inside these sites using a framework called "PeckBirdy," luring victims through fake software updates. This finding reveals a novel evasion technique in which malicious traffic is blended with low-quality gambling sites, making it easy for defenders to dismiss related activity as employee policy violations rather than an intrusion. It highlights how cheap, disposable web content can be repurposed into resilient attack infrastructure that is difficult to detect and take down. The PeckBirdy framework is a JScript-based C2 framework used by China-aligned APT groups to exploit LOLBins (living-off-the-land binaries) across multiple environments, and it has been observed delivering advanced backdoors to gambling-industry and Asian government targets. Because the malicious sites closely resemble ordinary gambling pages, security teams may overlook the associated traffic as non-threatening.

telegram · zaihuapd · Sep 16, 07:31

**Background**: APT (Advanced Persistent Threat) groups are well-resourced attackers, often state-aligned, that conduct long-term espionage and intrusion campaigns. They rely on command-and-control (C2) infrastructure to send instructions to compromised machines and receive stolen data, and defenders frequently try to block these domains. Hiding C2 domains within large volumes of low-quality gambling and adult websites makes the malicious infrastructure harder to identify, since the domains appear to belong to ordinary, if unsavory, commercial sites.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendmicro.com/en_us/research/26/a/peckbirdy-script-framework.html">PeckBirdy: A Versatile Script Framework for LOLBins Exploitation Used by China-aligned Threat Groups | Trend Micro (US)</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/peckbirdy-framework-tied-china/">PeckBirdy Framework Tied to China-Aligned Cyber Campaigns - Infosecurity Magazine</a></li>
<li><a href="https://iplogger.org/blog/peckbirdy-framework-tied-to-china-aligned-cyber-campaigns/">PeckBirdy Framework: Dissecting the China-Aligned APT Threat to Asian Sectors</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#APT`, `#malware`, `#threat-intelligence`, `#C2-infrastructure`

---

<a id="item-4"></a>
## [Sina Cloud SAE shuts down permanently, early Bilibili source files lost](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

Sina Cloud SAE, China's first PaaS platform launched in 2009, permanently shut down at midnight on September 16, 2026, deleting all user data. Roughly 420 TB of early Bilibili video source files still stored in Sina Cloud S3 buckets are being lost, while the Archive Team's distributed archiving project has rescued about 680 TB and reached 96.26% completion. The shutdown erases a piece of Chinese internet history, as early Bilibili videos hosted on SAE will become permanently inaccessible, affecting both developers who built on the platform and viewers of early user-generated content. It also highlights the fragility of centralized cloud storage and the growing role of volunteer archiving efforts in digital preservation. The Archive Team's distributed archiving effort has saved about 680 TB of the remaining data, reaching 96.26% completion, but the roughly 420 TB still in Sina Cloud S3 buckets may not be fully rescued before deletion. Bilibili videos from before 2014 are expected to become completely unavailable.

telegram · zaihuapd · Sep 16, 15:00

**Background**: Sina App Engine (SAE) was launched in 2009 as China's first PaaS platform, offering low-cost, maintenance-free hosting that made it a popular choice for developers. Bilibili, a major Chinese video-sharing site, relied on Sina Cloud to store many of its early video source files. The Archive Team is a volunteer group known for preserving at-risk online services such as GeoCities and Yahoo! Video, and it runs distributed crawls to rescue data before shutdowns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sinacloud.com/sae.html">云 应用 SAE - 云 服务 - 云 托管</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team - Wikipedia</a></li>
<li><a href="https://stage1st.com/2b/thread-2289931-1-1.html">新浪云 SAE 今晚永久下线：早期 B站视频源文件全部消失 - 归墟 - Stag...</a></li>

</ul>
</details>

**Tags**: `#cloud-computing`, `#data-archiving`, `#bilibili`, `#paas`, `#digital-preservation`

---