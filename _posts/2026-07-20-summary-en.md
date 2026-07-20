---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 27 items, 13 important content pieces were selected

---

1. [Claude Fable Claims Counterexample to Jacobian Conjecture](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x High-Risk RCE Vulnerability Without Gadget](#item-2) ⭐️ 9.0/10
3. [Zhipu AI Completes 1 GW Data Center with All Domestic Chips](#item-3) ⭐️ 9.0/10
4. [China's open-weights AI strategy gains ground](#item-4) ⭐️ 8.0/10
5. [Hacker wipes Romania's land registry database](#item-5) ⭐️ 8.0/10
6. [AI Writing Detection on arXiv: 39% Flagged by 2026](#item-6) ⭐️ 8.0/10
7. [Kimi K3, Qwen 3.8, and Anthropic's Potential Unraveling](#item-7) ⭐️ 8.0/10
8. [Ben Thompson Proposes US Law to Legalize AI Training Data as Fair Use](#item-8) ⭐️ 8.0/10
9. [Sam Altman's 2022 Email Reveals Open-Source Strategy](#item-9) ⭐️ 8.0/10
10. [Hugging Face Breach by AI Agent; Commercial LLMs Refuse Forensics](#item-10) ⭐️ 8.0/10
11. [Trump admin may restrict US firms from using Chinese open-weight AI models](#item-11) ⭐️ 8.0/10
12. [US Military Apps Found Embedding Chinese, Russian Code](#item-12) ⭐️ 8.0/10
13. [EU proposes sharing biometric data with US for visa-free travel](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Fable Claims Counterexample to Jacobian Conjecture](https://zh.wikipedia.org/zh-cn/%E9%9B%85%E5%8F%AF%E6%AF%94%E7%8C%9C%E6%83%B3) ⭐️ 9.0/10

On July 19, 2026, Anthropic employee and mathematician Levent Alpöge presented an explicit counterexample to the Jacobian conjecture in three-dimensional space, discovered with the help of Anthropic's large language model Claude Fable 5. If verified, this would disprove a long-standing open problem in algebraic geometry that has resisted proof for over 80 years, and it demonstrates the potential of AI-assisted mathematical research. The counterexample is for the case N > 2; the Jacobian conjecture for N = 2 remains unsolved. The discovery was made during the 2026 World Cup final, and a WolframAlpha verification link was provided.

telegram · zaihuapd · Jul 20, 05:34

**Background**: The Jacobian conjecture, first stated in 1884 for two variables and generalized in 1939, asserts that a polynomial map with a non-zero constant Jacobian determinant has a polynomial inverse. It is known for many incorrect proofs and is number 16 on Smale's list of problems for the 21st century. Claude Fable 5 is a state-of-the-art large language model released by Anthropic in June 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Discussion**: The mathematics community reacted with excitement and skepticism; many researchers are asking for the construction details and reasoning behind the counterexample. The lack of peer review has led to cautious optimism.

**Tags**: `#mathematics`, `#Jacobian Conjecture`, `#AI-assisted research`, `#breakthrough`

---

<a id="item-2"></a>
## [Fastjson 1.x High-Risk RCE Vulnerability Without Gadget](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 9.0/10

Security researcher Kirill Firsov disclosed a high-risk remote code execution vulnerability in Fastjson versions 1.2.68 to 1.2.83, exploitable without enabling autoType or relying on classpath gadgets, affecting JDK 8, 17, and 21. This vulnerability is critical because Fastjson is widely used in Java applications, and the lack of a required gadget or autoType makes exploitation easier. With Fastjson 1.x end-of-life since October 2024, no official patch is expected, forcing users to migrate to Fastjson2 or enable SafeMode. The vulnerability affects Fastjson 1.2.68 through 1.2.83 and can be triggered without autoType enabled or any specific gadget on the classpath. The only mitigations are upgrading to Fastjson2 or enabling SafeMode via JVM parameters, code, or properties file.

telegram · zaihuapd · Jul 20, 14:32

**Background**: Fastjson is a popular Java library for JSON serialization/deserialization developed by Alibaba. Its autoType feature allows specifying Java class names in JSON via @type, which has historically been a source of deserialization vulnerabilities. SafeMode disables autoType entirely, preventing such attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en">fastjson _ safemode _en · alibaba/ fastjson Wiki · GitHub</a></li>
<li><a href="https://jfrog.com/blog/cve-2022-25845-analyzing-the-fastjson-auto-type-bypass-rce-vulnerability/">CVE-2022-25845 - Fastjson RCE vulnerability analysis</a></li>
<li><a href="https://www.huaweicloud.com/intl/en-us/notice/20200530105656853.html">Remote Code Execution Vulnerability in Fastjson 1.2.68 and Earlier...</a></li>

</ul>
</details>

**Tags**: `#Fastjson`, `#RCE`, `#vulnerability`, `#security`, `#Java`

---

<a id="item-3"></a>
## [Zhipu AI Completes 1 GW Data Center with All Domestic Chips](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 9.0/10

Zhipu AI has completed a 1 GW data center powered entirely by domestically produced Chinese chips, and it has already begun partial operation to support training of its GLM AI model. This milestone demonstrates China's ability to build large-scale AI infrastructure without relying on foreign chips, which is critical for geopolitical resilience and advancing domestic AI capabilities. The 1 GW facility can power approximately 750,000 homes simultaneously and is one of the largest data centers built by a Chinese AI lab, with multiple clusters each containing over 10,000 chips.

telegram · zaihuapd · Jul 20, 15:43

**Background**: Zhipu AI, also known as Z.ai, is a leading Chinese AI company and developer of the open-source GLM family of large language models. The United States placed Zhipu AI on its Entity List in January 2025, restricting its access to advanced American chips, which has accelerated China's push for domestic chip alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zhipu_AI">Zhipu AI</a></li>
<li><a href="https://techplustrends.com/1gw-data-center-power-consumption-guide/">“1GW Data Center Power Consumption: Why 2026 Infrastructure ...</a></li>
<li><a href="https://llm-stats.com/">AI Leaderboard 2026: Compare & Rank 300+ Top AI Models by...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#data center`, `#China`, `#chips`, `#infrastructure`

---

<a id="item-4"></a>
## [China's open-weights AI strategy gains ground](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

An analysis argues that China's open-weights AI models are outperforming US proprietary models, drawing parallels to historical market shifts toward free and open software. The article claims 80% of startups are using Chinese models, though some commenters dispute this figure. This trend could reshape the global AI landscape, making advanced AI more accessible and reducing reliance on expensive proprietary models. It also highlights a strategic divergence between US and Chinese AI development approaches. Open-weights models are not fully open-source; they allow free use and fine-tuning but often require payment for hosting. The article notes that US companies like OpenAI and Anthropic charge high inference margins to recoup costs, while Chinese models are offered at lower cost.

hackernews · benwerd · Jul 20, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48979269)

**Background**: Open-weights AI models refer to models where the trained parameters (weights) are publicly released, allowing others to run, fine-tune, and deploy them. This contrasts with proprietary models like GPT-4, where only API access is provided. China has adopted an open-weights strategy for many of its leading AI models, such as those from Baidu and Kimi.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/open-source-ai-china-kimi-american-ai-industry-openai-anthropic-2026-7">Americans Are Freaking Out Over China 's Open - Source AI Strategy</a></li>
<li><a href="https://ashleydudarenok.com/china-ai-strategy/">China AI Strategy : Policy, Regulation & Global Impact in 2025</a></li>
<li><a href="https://www.uscc.gov/research/two-loops-how-chinas-open-ai-strategy-reinforces-its-industrial-dominance">Two Loops: How China ’s Open AI Strategy Reinforces Its Industrial...</a></li>

</ul>
</details>

**Discussion**: Commenters debate the validity of the 80% startup usage claim, with some noting their own experience shows US models dominate. Others argue open-weights models will eventually win due to cost and flexibility, though inference costs can still be high. Some point out that open-weights is not truly open-source, but still offers significant advantages over proprietary models.

**Tags**: `#AI`, `#open-source`, `#China`, `#market dynamics`, `#strategy`

---

<a id="item-5"></a>
## [Hacker wipes Romania's land registry database](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

A hacker wiped Romania's entire land registry database, but officials restored services using offline backups and are migrating the agency's systems to the government cloud. This attack on a critical national infrastructure could have caused massive societal disruption, including inability to prove land ownership, highlighting the importance of offline backups and secure government IT systems. The hacker, identified as Zakaria Mahdjoub from Algeria, claimed to have deleted backups, but the agency had offline copies. The migration to Romania's Government Cloud is coordinated by the Special Telecommunications Service (STS) and expected to complete by July 22.

hackernews · speckx · Jul 20, 13:28 · [Discussion](https://news.ycombinator.com/item?id=48978605)

**Background**: Land registries are critical government databases that record property ownership, mortgages, and other rights. Losing such data can paralyze real estate transactions, legal disputes, and tax collection. Offline backups are a key defense against ransomware and destructive attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.newsdirectory3.com/romania-land-registry-paralysed-by-major-cyberattack/">Romania Land Registry Paralysed by Major... - News Directory 3</a></li>
<li><a href="https://buzzverified.com/romania-land-registry-hack/">Romania Land Registry Hack - buzzverified.com</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the attack may stem from corruption in government IT contracts, where cronies fail to implement real security. Others drew parallels to a similar data loss incident in South Korea, emphasizing the need for robust backup practices.

**Tags**: `#cybersecurity`, `#infrastructure`, `#data loss`, `#Romania`, `#hacking`

---

<a id="item-6"></a>
## [AI Writing Detection on arXiv: 39% Flagged by 2026](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

An analysis of 12,750 arXiv papers from 2021 to 2026 found that by January 2026, about 39% of papers were flagged as AI-written, with computer science peaking at 65% and mathematics barely above baseline at 0.7%. This measurement highlights the rapid adoption of LLMs in academic writing, raising concerns about the integrity of scholarly publishing and the reliability of AI detection tools, which may produce false positives even on pre-LLM human-written texts. The detector was tuned to avoid false positives, achieving a pre-ChatGPT detection rate of only 0.4%. However, community tests showed that a 2015 IEEE paper was flagged as 74% machine-written, indicating potential calibration issues.

hackernews · dopamine_daddy · Jul 20, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48981206)

**Background**: arXiv is a free, open-access repository for scholarly preprints in fields like physics, mathematics, and computer science. Since the release of ChatGPT in late 2022, LLMs have been increasingly used to assist or generate academic text, prompting efforts to detect such usage. However, no detection method is 100% accurate, and distinguishing human from AI writing remains challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.01268v1">Mapping the Increasing Use of LLMs in Scientific Papers</a></li>
<li><a href="https://undetectable.ai/blog/how-to-detect-ai-writing-guide/">How to Detect AI Writing in 2025: Full Guide</a></li>

</ul>
</details>

**Discussion**: Community members expressed skepticism about detection reliability, with one user noting that their 2011 paper was flagged as 27% machine-written and a 2012 dissertation as 40%, suggesting detectors may confuse human writing with AI output. Another commenter argued that no text-based detector can reliably distinguish identical human and AI paragraphs, highlighting fundamental limitations.

**Tags**: `#AI detection`, `#arXiv`, `#academic publishing`, `#LLM impact`, `#measurement`

---

<a id="item-7"></a>
## [Kimi K3, Qwen 3.8, and Anthropic's Potential Unraveling](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

Moonshot AI released Kimi K3, a 2.8-trillion-parameter open-weight model, and Alibaba launched Qwen 3.8, a 2.4-trillion-parameter multimodal model, intensifying competition with Anthropic and OpenAI. Meanwhile, Anthropic faces internal turmoil and a conflict of interest scandal involving Figma. The rapid release of powerful open-weight models from Chinese AI labs signals a commoditization of frontier AI capabilities, potentially undermining the business models of proprietary labs like Anthropic and OpenAI. The ethical and competitive pressures on Anthropic could reshape the AI industry landscape. Kimi K3 features a 1-million-token context window and is optimized for deep reasoning and agentic workflows, with open weights promised by July 2026. Qwen 3.8 uses a sparse Mixture-of-Experts architecture and can process text, images, videos, and documents, claiming performance second only to Fable 5.

hackernews · cl42 · Jul 20, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48980019)

**Background**: Frontier AI labs like Anthropic and OpenAI have traditionally relied on proprietary models and high subscription fees. The emergence of competitive open-weight models from Chinese startups threatens to commoditize AI capabilities, forcing labs to differentiate through speed, specialization, or ethical branding.

<details><summary>References</summary>
<ul>
<li><a href="https://the-decoder.com/alibabas-qwen-takes-on-kimi-k3-with-open-weight-qwen-3-8-says-model-is-second-only-to-fable-5/">Alibaba's Qwen takes on Kimi K3 with open-weight Qwen 3.8, says model is "second only to Fable 5"</a></li>
<li><a href="https://www.youtube.com/watch?v=6-ccuwX4gCQ">Chinese AI Startup Moonshot Unveils Kimi K 3 Model - YouTube</a></li>
<li><a href="https://www.anthropic.com/economic-index">The Anthropic Economic Index \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters debate whether open-weight models will commoditize AI, with some arguing that users will pay a premium for slightly better models. Others highlight ethical concerns, such as the Figma-Anthropic conflict, and note that hype cycles are shortening, suggesting a possible plateau in AI progress.

**Tags**: `#AI`, `#LLMs`, `#economics`, `#open-source`, `#Anthropic`

---

<a id="item-8"></a>
## [Ben Thompson Proposes US Law to Legalize AI Training Data as Fair Use](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the US pass a law explicitly making AI training data collection fair use and barring terms of service that forbid model distillation, aiming to help US open models compete with Chinese counterparts. This proposal addresses the hypocrisy of AI labs outlawing distillation on their models while training on unlicensed data, and could reshape US-China AI competition by enabling US open models to leverage distillation from frontier models. Thompson also speculated that Alibaba's decision to release Qwen 3.8 Max as open weights may have been influenced by a recent Xi Jinping speech encouraging open source and collaboration.

rss · Simon Willison · Jul 20, 17:09

**Background**: Model distillation is a technique where knowledge from a large AI model is transferred to a smaller one, often by querying the larger model's API. The legality of using copyrighted data for AI training is currently disputed in US courts, with fair use being a key defense. Thompson's proposal would codify fair use for training data and prevent companies from using terms of service to block distillation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://houstonlawreview.org/article/147422-fair-use-and-the-origin-of-ai-training">Fair Use and the Origin of AI Training | Published in Houston Law Review</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open source AI`, `#copyright`, `#model distillation`, `#US-China competition`

---

<a id="item-9"></a>
## [Sam Altman's 2022 Email Reveals Open-Source Strategy](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

A 2022 email from Sam Altman to OpenAI's board, exposed in the 2026 Musk v. Altman lawsuit, outlines a plan to release an open-source GPT-3-level model to run locally on consumer hardware, aiming to discourage competitors like Stability AI. This reveals OpenAI's internal strategic thinking about using open-source releases as a competitive tactic, shedding light on the complex dynamics between open-source and proprietary AI development. The email specifically mentions releasing a model with approximate GPT-3 capability before Stability AI or others do, and argues that such a release would discourage competitors and make it harder for new efforts to get funded.

rss · Simon Willison · Jul 20, 03:47

**Background**: GPT-3 is a large language model with 175 billion parameters released by OpenAI in 2020, known for its few-shot learning abilities. Stability AI, known for Stable Diffusion, later released open-source language models like StableLM in 2023. The email predates the public release of ChatGPT and reflects OpenAI's early considerations about open-source strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-3">GPT-3 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://www.theverge.com/2023/4/19/23689883/stability-ai-open-source-large-language-model-stablelm">Stability AI announces new open-source large language model | The Verge</a></li>

</ul>
</details>

**Tags**: `#openai`, `#open-source`, `#ai-ethics`, `#sam-altman`, `#generative-ai`

---

<a id="item-10"></a>
## [Hugging Face Breach by AI Agent; Commercial LLMs Refuse Forensics](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face disclosed a July 2026 security breach where an attacker exploited two code execution vulnerabilities in dataset processing pipelines, driven by an autonomous AI agent framework, to steal internal datasets and service credentials. During incident response, commercial LLM APIs refused to analyze attack logs due to safety guardrails, forcing the team to use locally deployed GLM 5.2 to process over 17,000 attack records. This incident highlights a new class of AI-driven attacks and reveals a critical blind spot: commercial LLMs may refuse to assist in forensic analysis of AI-powered breaches, undermining incident response. It underscores the need for organizations to maintain local, unrestricted models for security operations and raises questions about reliance on proprietary AI services. The attacker exploited two code execution vulnerabilities in Hugging Face's dataset processing pipelines, similar to CVE-2026-25592 and CVE-2026-26030 disclosed in Microsoft's Semantic Kernel framework. Hugging Face confirmed that public models, datasets, and Spaces were not tampered with, and the software supply chain was clean; they have since fixed vulnerabilities, rotated affected credentials, and recommend users rotate tokens and check recent activity.

telegram · zaihuapd · Jul 20, 10:41

**Background**: Hugging Face is a major platform for hosting AI models, datasets, and demo apps (Spaces). AI agent frameworks, like Semantic Kernel, enable autonomous AI systems but can introduce code execution vulnerabilities if not properly secured. GLM 5.2 is an open-source large language model from Z.ai (formerly Zhipu AI), released under the MIT License, which can be deployed locally without restrictive safety filters.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/">When prompts become shells: RCE vulnerabilities in AI agent frameworks | Microsoft Security Blog</a></li>
<li><a href="https://z.ai/blog/glm-5.2">GLM-5.2: Built for Long-Horizon Tasks</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI safety`, `#Hugging Face`, `#LLM`, `#incident response`

---

<a id="item-11"></a>
## [Trump admin may restrict US firms from using Chinese open-weight AI models](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

Axios reports that the Trump administration is considering soft restrictions on US companies using Chinese open-weight AI models like Kimi K3, citing its strong performance and low cost. The restrictions would involve bureaucratic hurdles rather than outright bans. This could reshape the global AI competitive landscape by limiting US access to cost-effective open-weight models, potentially slowing AI adoption and innovation. It also highlights the tension between closed-source AI giants and the open-weight movement. Kimi K3 is a 2.8 trillion parameter open-weight multimodal reasoning model from Moonshot AI, priced at $3 per million input tokens. The proposed restrictions include procurement rules, entity list threats, and舆论 pressure, rather than hard bans.

telegram · zaihuapd · Jul 20, 11:49

**Background**: Open-weight models release the trained neural network weights, allowing users to host and fine-tune them, offering more control than closed APIs. Kimi K3 is the latest in a series of competitive Chinese open-weight models that have narrowed the performance gap with US counterparts at a fraction of the cost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the news item.

**Tags**: `#AI policy`, `#open-source`, `#US-China`, `#Kimi K3`, `#regulation`

---

<a id="item-12"></a>
## [US Military Apps Found Embedding Chinese, Russian Code](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

Researchers at Purdue University found that nearly two-thirds of 220+ apps marketed to US military personnel contain third-party code from China and Russia, including Huawei SDKs. This raises national security concerns because the embedded code could be remotely updated to exfiltrate sensitive data from military devices, potentially compromising operational security. Although no data has been observed flowing to Huawei servers, the SDKs can be updated remotely, posing a latent risk. 76% to 83% of 103 surveyed military personnel expressed extreme unease about apps containing code from China, Russia, Iran, or North Korea.

telegram · zaihuapd · Jul 20, 13:42

**Background**: Third-party SDKs are software libraries that apps integrate to add features like analytics or authentication. Huawei's SDKs have been flagged by the US government as national security threats due to potential data collection. The US Department of Defense has previously reported adversaries using commercial location data to surveil US troops in the Middle East.

<details><summary>References</summary>
<ul>
<li><a href="https://conzit.com/post/security-risks-foreign-code-in-military-apps-exposed">Security Risks: Foreign Code in Military Apps Exposed</a></li>

</ul>
</details>

**Tags**: `#security`, `#military`, `#supply chain`, `#privacy`, `#SDK`

---

<a id="item-13"></a>
## [EU proposes sharing biometric data with US for visa-free travel](https://edri.org/our-work/the-eu-is-about-to-sell-our-most-sensitive-data-to-the-us-for-visa-free-travel/) ⭐️ 8.0/10

The European Commission is negotiating an Enhanced Border Security Partnership (EBSP) framework agreement with the Trump administration, under which the US would gain access to EU member states' biometric databases in exchange for visa-free travel for EU citizens. This deal could set a dangerous precedent for mass surveillance and the commodification of sensitive biometric data, potentially chilling political dissent and activism across Europe. Leaked drafts show the EU has largely accepted US demands for unrestricted access to data, including biometric information and 'risk indicators' based on political views. The agreement would not give US authorities direct access to EU databases, but would require operational arrangements by the end of 2026.

telegram · zaihuapd · Jul 20, 15:08

**Background**: The US Visa Waiver Program allows citizens of certain countries to travel to the US for up to 90 days without a visa. In exchange, partner countries must meet security requirements, including sharing information on travelers. The EBSP framework is the latest iteration of these negotiations, with the US setting a December 31, 2026 deadline for concluding agreements.

<details><summary>References</summary>
<ul>
<li><a href="https://ayedo.de/en/posts/transatlantischer-zugriff-auf-biometrische-daten-uneinigkeit-unter-eu-mitgliedstaaten/">Transatlantic Access to Biometric Data: Disagreement Among EU ...</a></li>
<li><a href="https://discover.passportindex.org/policy-and-regulations/visa-free-travel-personal-data-and-esta-where-do-u-s-eu-talks-stand/">Visa-Free Travel, Personal Data and ESTA: Where Do U . S .- EU Talks...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#biometric data`, `#EU-US relations`, `#surveillance`, `#civil liberties`

---