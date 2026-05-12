---
layout: default
title: "Horizon Summary: 2026-05-12 (EN)"
date: 2026-05-12
lang: en
---

> From 32 items, 12 important content pieces were selected

---

1. [TanStack npm Supply Chain Attack via Novel GitHub Actions Exploit](#item-1) ⭐️ 9.0/10
2. [CERT Releases Six CVEs for Serious dnsmasq Vulnerabilities](#item-2) ⭐️ 8.0/10
3. [Needle: 26M Parameter Tool-Calling Model for Edge Devices](#item-3) ⭐️ 8.0/10
4. [Obsidian Launches Automated Plugin Review System](#item-4) ⭐️ 8.0/10
5. [Bambu Lab Accused of Abusing Open Source Social Contract](#item-5) ⭐️ 8.0/10
6. [Canada's Bill C-22 Revives Surveillance and Encryption Backdoor Threats](#item-6) ⭐️ 8.0/10
7. [Instructure Pays Ransom to Canvas Hackers](#item-7) ⭐️ 8.0/10
8. [OpenAI to Launch GPT-5.5-Cyber for Cybersecurity](#item-8) ⭐️ 8.0/10
9. [Unitree Launches First Mass-Produced Manned Transforming Mech GD01](#item-9) ⭐️ 8.0/10
10. [Anthropic Denies Chinese Think Tank Access to Latest AI Model](#item-10) ⭐️ 8.0/10
11. [US Commerce Dept. Quietly Deletes AI Security Test Details](#item-11) ⭐️ 8.0/10
12. [SpaceX and Google in Talks for Orbital Data Centers](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TanStack npm Supply Chain Attack via Novel GitHub Actions Exploit](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 9.0/10

On May 11, 2026, between 19:20 and 19:26 UTC, an attacker published 84 malicious versions across 42 @tanstack/* npm packages using a novel attack chain that combined pull_request_target abuse, GitHub Actions cache poisoning, and OIDC token extraction from runner memory. This incident highlights a critical supply chain vulnerability in widely-used open source libraries, demonstrating that even short-lived attacks can compromise thousands of downstream users and systems. The attack did not compromise npm tokens or the release workflow itself; instead, it exploited GitHub Actions' pull_request_target event to poison the cache, then extracted OIDC tokens from the runner's memory during a legitimate release. All malicious versions were deprecated within 20 minutes, and tarballs were removed by npm security.

telegram · zaihuapd · May 12, 03:00

**Background**: The pull_request_target event in GitHub Actions runs workflows in the context of the base repository, giving access to secrets and OIDC tokens even from untrusted forks. Cache poisoning allows attackers to inject malicious content into the build cache, which can later be executed in privileged workflows. OIDC tokens can be extracted from runner memory and used to authenticate to cloud providers or package registries like npm.

<details><summary>References</summary>
<ul>
<li><a href="https://sesamedisk.com/ci-cd-attack-patterns-2026/">GitHub Actions Cache Poisoning & pull _ request _ target Abuse...</a></li>
<li><a href="https://cloud.hacktricks.wiki/en/pentesting-ci-cd/github-security/abusing-github-actions/gh-actions-cache-poisoning.html">GH Actions - Cache Poisoning - HackTricks Cloud</a></li>
<li><a href="https://www.banandre.com/blog/supply-chain-peril-lessons-from-the-tanstack-npm-compromise">Supply Chain Peril: Lessons from the TanStack npm... - Banandre</a></li>

</ul>
</details>

**Discussion**: The Telegram community discussion emphasized the severity of the attack, noting that the novel combination of techniques made it particularly dangerous. Some users expressed concern about the difficulty of detecting such attacks and the need for better CI/CD security practices.

**Tags**: `#supply chain attack`, `#npm security`, `#GitHub Actions`, `#security incident`, `#open source`

---

<a id="item-2"></a>
## [CERT Releases Six CVEs for Serious dnsmasq Vulnerabilities](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 8.0/10

CERT has released six Common Vulnerabilities and Exposures (CVEs) for serious security vulnerabilities in dnsmasq, a widely-used lightweight DNS forwarder and DHCP server. The vulnerabilities affect multiple versions and have prompted active community discussion about patching and alternatives. dnsmasq is embedded in many home routers, IoT devices, and Linux distributions, so these vulnerabilities could expose millions of devices to remote attacks. The incident highlights the challenges of maintaining security in widely-deployed open-source software and may accelerate adoption of alternative solutions. The six CVEs cover a range of serious issues including buffer overflows and denial-of-service vectors. Community members note that Debian's stable branch ships an outdated version of dnsmasq, and OpenWRT is working on a new build to address the vulnerabilities.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: dnsmasq is a lightweight, open-source software that provides DNS caching, DHCP server, TFTP server, and network boot features for small networks. It is included in most Linux distributions, Android, and many home routers, making it one of the most widely deployed network services. Common Vulnerabilities and Exposures (CVEs) are unique identifiers for publicly known cybersecurity vulnerabilities, used to track and manage security issues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some users advocate for alternatives like MaraDNS, while others criticize Debian's slow patching approach. There is also discussion about OpenWRT's progress in releasing a fixed build, and some users express general distrust of dnsmasq's all-in-one design.

**Tags**: `#security`, `#dnsmasq`, `#CVE`, `#networking`, `#open-source`

---

<a id="item-3"></a>
## [Needle: 26M Parameter Tool-Calling Model for Edge Devices](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus has open-sourced Needle, a 26M parameter distilled model for single-shot tool calling that runs at 6000 tok/s prefill and 1200 tok/s decode on consumer devices. The model uses only attention and gating without any MLPs, based on their Simple Attention Networks architecture. This demonstrates that tiny models can effectively handle tool calling, a key capability for agentic AI, enabling on-device AI agents on phones, watches, and glasses. It challenges the assumption that large models are necessary for function calling, potentially reducing cost and latency for edge AI applications. Needle was pretrained on 200B tokens using 16 TPU v6e for 27 hours, then post-trained on 2B tokens of synthesized function-calling data generated by Gemini across 15 tool categories. It outperforms larger models like FunctionGemma-270M and Qwen-0.6B on single-shot function calling, but those models have broader conversational capabilities.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Tool calling (or function calling) allows AI models to interact with external APIs and services, enabling agentic behaviors like setting alarms or sending messages. Knowledge distillation transfers knowledge from a large teacher model (e.g., Gemini) to a smaller student model, reducing size while retaining capability. Simple Attention Networks remove feed-forward layers, relying solely on attention to process external knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md">needle/docs/ simple _ attention _ networks .md at main...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Distillation_(machine_learning)">Distillation (machine learning)</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the model's potential for on-device use, with suggestions for a live demo and comparisons to existing tools like Siri. Some asked about distillation basics and why Google doesn't produce similarly small models, while others noted the need for clearer parameter count notation (0.026B vs 26M).

**Tags**: `#tool calling`, `#distillation`, `#edge AI`, `#open source`, `#small models`

---

<a id="item-4"></a>
## [Obsidian Launches Automated Plugin Review System](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian announced a new community site and an automated plugin review system that scans every version for security and code quality, replacing the previous manual review bottleneck. This addresses a critical scaling bottleneck for Obsidian's plugin ecosystem, enabling faster plugin submissions and reducing developer frustration and team burnout. The automated system scans every plugin version, not just initial submissions, and is backed by CEO engagement and a roadmap for further improvements.

hackernews · xz18r · May 12, 15:45 · [Discussion](https://news.ycombinator.com/item?id=48109970)

**Background**: Obsidian is a popular note-taking app that supports a rich plugin ecosystem. Previously, all plugin submissions were manually reviewed by a small team, which became unsustainable as the number of plugins grew, especially with AI-assisted development accelerating submissions.

<details><summary>References</summary>
<ul>
<li><a href="https://obsidian.md/blog/future-of-plugins/">The future of Obsidian plugins - Obsidian</a></li>

</ul>
</details>

**Discussion**: The community expressed relief and excitement, with users noting the previous manual review bottleneck had become impossible. Some raised concerns about automated checks' ability to detect malicious plugins, suggesting proper sandboxing and permission systems as a better solution.

**Tags**: `#Obsidian`, `#plugin ecosystem`, `#automated review`, `#developer tools`, `#community scaling`

---

<a id="item-5"></a>
## [Bambu Lab Accused of Abusing Open Source Social Contract](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/) ⭐️ 8.0/10

Bambu Lab is accused of violating the open source social contract by restricting LAN mode on its 3D printers and using weak excuses, sparking widespread community outrage. This controversy highlights tensions between closed ecosystems and open source principles in consumer hardware, potentially eroding trust in Bambu Lab and influencing purchasing decisions among the 3D printing community. Bambu Lab restricted LAN mode to require an SD card and blocked third-party clients by checking user-agent strings, which critics argue is a weak security measure that undermines open source software like OrcaSlicer.

hackernews · rubenbe · May 12, 14:54 · [Discussion](https://news.ycombinator.com/item?id=48109224)

**Background**: The open source social contract refers to the expectation that companies using open source software will respect community norms, such as allowing local control and not imposing unnecessary restrictions. Bambu Lab's printers initially lacked LAN mode until community pressure forced its addition, and recent changes have rekindled distrust.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/">Bambu Lab is abusing the open source social contract - Jeff Geerling</a></li>
<li><a href="https://wiki.bambulab.com/en/knowledge-sharing/enable-lan-mode">How to enable LAN Mode on Bambu Lab printers | Bambu Lab Wiki</a></li>
<li><a href="https://github.com/bambulab/BambuStudio/issues/4512">Make LAN-only mode actually usable · Issue #4512 · bambulab/BambuStudio</a></li>

</ul>
</details>

**Discussion**: Commenters express strong disapproval, noting that Bambu Lab's excuse of server overload due to unauthorized traffic is implausible because they relied on user-agent strings. Some recall that LAN mode was only added after previous outrage, and suggest that customer pressure is the only way to steer the company.

**Tags**: `#3D printing`, `#open source`, `#ethics`, `#community backlash`

---

<a id="item-6"></a>
## [Canada's Bill C-22 Revives Surveillance and Encryption Backdoor Threats](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare) ⭐️ 8.0/10

Canada's Bill C-22 proposes mandatory data retention and encryption backdoors, threatening to block encrypted services like Signal and WhatsApp in Canada. This legislation could set a dangerous precedent for government surveillance, undermining privacy and security for all Canadians and potentially forcing major tech companies to exit the market. Bill C-22 is a repackaged version of last year's Bill C-26, retaining warrantless metadata access and adding encryption backdoor mandates that would weaken end-to-end encryption.

hackernews · Brajeshwar · May 12, 17:35 · [Discussion](https://news.ycombinator.com/item?id=48111531)

**Background**: Mandatory data retention laws require companies to store user data for government access, while encryption backdoors create vulnerabilities in secure systems. End-to-end encryption ensures only sender and recipient can read messages, and backdoors would compromise that security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/issues/mandatory-data-retention">Mandatory Data Retention | Electronic Frontier Foundation</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption - Wikipedia</a></li>
<li><a href="https://jakeinsight.com/tech/2026-03-16-canada-bill-c26-metadata-surveillance-warrantless-/">Canada Bill C - 22 Metadata Surveillance and Developer Privacy Risk</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, with calls to contact MPs and the Minister of Public Safety. Some see a silver lining in driving innovation for censorship-circumvention tools, while others worry about repeated legislative attempts eventually passing.

**Tags**: `#surveillance`, `#encryption`, `#privacy`, `#legislation`, `#Canada`

---

<a id="item-7"></a>
## [Instructure Pays Ransom to Canvas Hackers](https://www.insidehighered.com/news/tech-innovation/administrative-tech/2026/05/11/instructure-pays-ransom-canvas-hackers) ⭐️ 8.0/10

Instructure, the developer of the Canvas learning management system, confirmed it paid a ransom to hackers who breached its systems, receiving digital confirmation of data destruction via shred logs. This incident reignites the debate on whether paying ransomware encourages further attacks, especially given Canvas's widespread use in education. It also raises questions about the credibility of ransomware operators' promises to delete stolen data. Instructure stated it received 'digital confirmation of data destruction (shred logs)' from the attackers, but critics argue such assurances are naive. The breach affected a major educational platform serving millions of students and institutions.

hackernews · Cider9986 · May 12, 02:56 · [Discussion](https://news.ycombinator.com/item?id=48103668)

**Background**: Canvas is a cloud-based learning management system (LMS) widely used in K-12, higher education, and corporate training. Ransomware attacks involve hackers encrypting data and demanding payment for decryption or to prevent data leaks. Paying ransoms is controversial, with comparisons to kidnapping ransoms, as it may fund criminal enterprises.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Canvas_LMS">Canvas LMS</a></li>
<li><a href="https://www.techradar.com/pro/the-ransomware-payment-debate-what-it-means-for-organizations">The ransomware payment debate : what it means for... | TechRadar</a></li>

</ul>
</details>

**Discussion**: Commenters debated the ethics of ransom payments, with some comparing it to kidnapping ransoms and suggesting making payments illegal. Others noted that ransomware operators need to maintain credibility to stay in business, but many dismissed the 'shred logs' as naive. A proposal to maintain a public list of organizations that paid ransoms was also discussed.

**Tags**: `#ransomware`, `#cybersecurity`, `#education`, `#data breach`, `#policy`

---

<a id="item-8"></a>
## [OpenAI to Launch GPT-5.5-Cyber for Cybersecurity](https://t.me/zaihuapd/41332) ⭐️ 8.0/10

OpenAI plans to release GPT-5.5-Cyber, a specialized model for cybersecurity, within the next few days. Initially, access will be limited to vetted trusted defenders and not available to the general public. This marks a strategic move by OpenAI to address critical cybersecurity needs with a specialized AI model, potentially enhancing defenses for critical infrastructure. It follows a similar trusted-access approach used for GPT-Rosalind in life sciences, indicating a pattern for high-risk domain-specific releases. GPT-5.5-Cyber is based on GPT-5.5, which the UK's AISI evaluated as one of the strongest models on cyber tasks, solving a multi-step cyber-attack simulation end-to-end. OpenAI is collaborating with government and industry partners to define trusted access mechanisms.

telegram · zaihuapd · May 12, 01:30

**Background**: OpenAI previously released GPT-Rosalind, a specialized model for life sciences research, under a similar trusted-access model. The company is also working with Anthropic's Mythos (likely a reference to another safety-focused initiative) to establish safe deployment practices. GPT-5.5 itself is OpenAI's latest general-purpose model with enhanced safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/">Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber | OpenAI</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities">Our evaluation of OpenAI's GPT-5.5 cyber capabilities | AISI Work</a></li>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT-Rosalind for life sciences research | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cybersecurity`, `#OpenAI`, `#GPT-5.5`, `#Model Release`

---

<a id="item-9"></a>
## [Unitree Launches First Mass-Produced Manned Transforming Mech GD01](https://m.mydrivers.com/newsview/1121657.html) ⭐️ 8.0/10

Unitree Robotics has unveiled the GD01, the world's first mass-produced manned transforming mech, priced at 3.9 million yuan. The vehicle can walk upright with a passenger and transform into a four-legged state for travel. This marks a significant milestone in robotics and consumer tech, bringing sci-fi concepts into reality. The GD01 could revolutionize tourism, special operations, and luxury transport, though its high price limits immediate mass adoption. The GD01 weighs about 500 kg and uses high-strength alloys and precision servo drives. A demonstration showed it can smash a brick wall with a single punch.

telegram · zaihuapd · May 12, 05:25

**Background**: Unitree Robotics is known for its humanoid robots like the G1 and H1. The GD01 extends their expertise into manned vehicles, combining walking and driving modes. Transforming mechs have been a staple of science fiction, but Unitree is the first to bring a mass-produced version to market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.jiemian.com/video/AGUCMQhjB2EBOVVn.html">宇 树 突然甩高燃大招！ 发布大型 载 人 变 形 机 甲 ，定价390...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#transforming mech`, `#Unitree`, `#consumer tech`, `#manned vehicle`

---

<a id="item-10"></a>
## [Anthropic Denies Chinese Think Tank Access to Latest AI Model](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html) ⭐️ 8.0/10

At a Singapore conference last month, a Chinese think tank representative requested that Anthropic grant access to its latest AI model for Beijing, and Anthropic refused on the spot. This incident highlights growing US national security concerns over China's attempts to access cutting-edge American AI technology, potentially accelerating regulatory scrutiny and export controls on AI models. The request was made during a conference organized by the Carnegie Endowment for International Peace, and while not an official Chinese government request, it has alarmed the US National Security Council.

telegram · zaihuapd · May 12, 12:57

**Background**: Anthropic is a US-based AI company known for developing the Claude series of large language models, with a strong focus on AI safety. The US government has increasingly restricted the export of advanced AI technologies to China, citing national security risks. This incident reflects ongoing tensions in the AI race between the two countries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Carnegie_Endowment_for_International_Peace">Carnegie Endowment for International Peace</a></li>

</ul>
</details>

**Tags**: `#AI`, `#geopolitics`, `#Anthropic`, `#China`, `#national security`

---

<a id="item-11"></a>
## [US Commerce Dept. Quietly Deletes AI Security Test Details](https://www.reuters.com/legal/litigation/microsoft-google-xai-security-test-details-deleted-us-government-website-2026-05-11/) ⭐️ 8.0/10

The US Commerce Department removed a webpage detailing pre-deployment AI security testing agreements with Google, xAI, and Microsoft, which was posted on May 5, 2026. The page now redirects to the homepage of the Center for AI Standards and Innovation (CAISI). This removal raises transparency concerns about government-industry AI safety oversight, especially as frontier AI models pose potential risks. It may undermine public trust in the voluntary testing program and the government's commitment to accountability. The original agreement aimed to give government scientists early access to advanced AI models to identify risks before public deployment. The Commerce Department and the Trump White House did not immediately respond to requests for comment.

telegram · zaihuapd · May 12, 13:38

**Background**: The Center for AI Standards and Innovation (CAISI) is the renamed US AI Safety Institute, established to evaluate and ensure the safety of frontier AI models. The pre-deployment testing program began under the Biden administration in 2024, with companies voluntarily submitting models for review. The deletion of details about such agreements could signal a shift in policy or a lack of transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Center_for_AI_Standards_and_Innovation">Center for AI Standards and Innovation</a></li>
<li><a href="https://qz.com/commerce-department-deletes-ai-security-testing-google-microsoft-xai-051226">Commerce Dept . deletes Google, Microsoft, xAI AI testing page</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#government regulation`, `#transparency`, `#tech policy`

---

<a id="item-12"></a>
## [SpaceX and Google in Talks for Orbital Data Centers](https://www.wsj.com/tech/spacex-google-in-talks-to-explore-data-centers-in-orbit-7b7799e2) ⭐️ 8.0/10

SpaceX and Google are negotiating a rocket launch agreement for Google's Project Suncatcher, which aims to launch a prototype orbital data center by 2027. SpaceX is also promoting orbital data centers as a key selling point for its upcoming IPO. This collaboration could revolutionize cloud computing by enabling space-based AI infrastructure, offering lower latency and renewable solar power. It also positions SpaceX as a major player in the AI compute market, potentially attracting customers like OpenAI and Microsoft. Google's Project Suncatcher involves launching solar-powered satellites equipped with Google TPUs, and has partnered with Planet Labs for satellite development. SpaceX recently struck a deal with Anthropic to provide 300 megawatts of compute power and over 220,000 Nvidia GPUs by the end of May.

telegram · zaihuapd · May 12, 16:28

**Background**: Orbital data centers are proposed facilities in space that use solar power for energy and offer advantages like global coverage and reduced latency. However, they face challenges such as extreme temperature swings and high costs—components can be 1,000 times more expensive than terrestrial ones. Google's Project Suncatcher is part of a broader trend, with companies like Starcloud already training LLMs in space using Nvidia H100 GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2l6X2VyekR4Rmc5bjdBUXJPOXFpZ0FQAQ?hl=en-MY&gl=MY&ceid=MY:en">Google News - Google 's Project Suncatcher will put AI chips in...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/research/google-project-suncatcher/">Project Suncatcher explores powering AI in space</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Google`, `#orbital data center`, `#cloud computing`, `#space infrastructure`

---