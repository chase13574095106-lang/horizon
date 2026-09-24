---
layout: default
title: "Horizon Summary: 2026-09-24 (EN)"
date: 2026-09-24
lang: en
---

> From 27 items, 4 important content pieces were selected

---

1. [OpenAI Adds Voice-Activated Plugins and GPT-6 Models to ChatGPT](#item-1) ⭐️ 9.0/10
2. [Anthropic says Claude autonomously discovered a novel CRISPR-like enzyme system](#item-2) ⭐️ 8.0/10
3. [Google launches Gemini 3.8 text-to-speech with voice cloning and watermarking](#item-3) ⭐️ 8.0/10
4. [ShinyHunters Claims Breach of FBI Employee and Applicant Data](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Adds Voice-Activated Plugins and GPT-6 Models to ChatGPT](https://x.com/OpenAI/status/2102808325742322002) ⭐️ 9.0/10

OpenAI announced that ChatGPT voice can now invoke plugins such as email, calendar, and Slack, and is powered by new GPT-6 models named Astra, Sol, and Luna. The new version, which also lets users create documents, presentations, websites, and spreadsheets via voice in ChatGPT Work on web and mobile, rolled out globally today. This marks a significant leap in AI assistant capabilities by combining voice control with real-world tool integrations, turning ChatGPT from a conversational chatbot into an agentic assistant that can act across platforms. It is likely to affect a broad range of users and developers who rely on ChatGPT for productivity and workflow automation. The GPT-6 family offers different balances of intelligence and cost: Astra is the flagship, Sol is the cost-efficient high-end tier, and Luna is the fast low-tier model. On the Artificial Analysis Intelligence Index, Astra scores 53, Sol 48, and Luna 37, while Anthropic's Claude Opus 5.5 records 58.

telegram · zaihuapd · Sep 24, 00:02

**Background**: ChatGPT is OpenAI's AI chatbot, and plugins are add-ons that let it connect to external services like email, calendars, and Slack to perform tasks. GPT-6 is the next generation of OpenAI's large language models, succeeding GPT-5, and ChatGPT Work is a workspace feature for creating documents, spreadsheets, and presentations. Voice integration means users can speak commands instead of typing, enabling hands-free, voice-driven workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/gpt-6-sol-and-luna">GPT - 6 Sol and Luna APIs : Bringing Frontier Intelligence to... | Kie.ai</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-sol">GPT - 6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#GPT-6`, `#voice-assistant`, `#plugins`

---

<a id="item-2"></a>
## [Anthropic says Claude autonomously discovered a novel CRISPR-like enzyme system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic announced that its AI model Claude autonomously discovered a previously undescribed enzyme system in bacteriophage DNA, where the enzyme's gene sits next to a long array of repeating DNA sequences resembling a CRISPR array. The finding came from one of Anthropic's first AI-for-science research programs, and the function of the system remains unknown. If validated, this would be a notable demonstration of AI-driven scientific discovery, showing that an LLM agent can comb through raw genomic data and surface candidate biological systems without direct human guidance. It could accelerate the search for programmable DNA-modifying tools, though experts caution that the underlying enzyme appears related to known reverse transcriptases rather than being entirely novel. The discovered system has a set of characteristics that have only been found together in a handful of other systems, all of which are programmable and perform operations such as cutting, copying, and pasting DNA. Community commenters note it appears to revolve around a known retron-like reverse transcriptase, and some question why Anthropic published a marketing whitepaper rather than a traditional journal submission or preprint.

hackernews · raahelb · Sep 23, 18:06 · [Discussion](https://news.ycombinator.com/item?id=49820134)

**Background**: CRISPR is a bacterial immune system that uses short repeating DNA sequences and associated Cas enzymes to target and cut specific DNA, and it has become a foundational gene-editing technology. Reverse transcriptases are enzymes that copy RNA into DNA, and retrons are bacterial genetic elements that use reverse transcriptase and are sometimes compared to CRISPR. Large language models like Anthropic's Claude are AI systems trained on vast text data, and this news concerns their emerging use as agents that can analyze biological sequence data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR-like repeats</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR">CRISPR - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters broadly tempered the hype, noting the system appears to be a known retron-like reverse transcriptase in a new genomic arrangement rather than a wholly novel enzyme, and that therapeutic CRISPR advances are mainly limited by delivery rather than targeting. Others found the agent transcript compelling as a new form of scientific narrative, while some questioned Anthropic's decision to publish a whitepaper instead of a peer-reviewed paper and debated whether the company is steering toward human-agent collaboration or fully autonomous discovery.

**Tags**: `#AI-for-science`, `#CRISPR`, `#genomics`, `#Anthropic`, `#AI discovery`

---

<a id="item-3"></a>
## [Google launches Gemini 3.8 text-to-speech with voice cloning and watermarking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 8.0/10

Google released Gemini 3.8 text-to-speech models, including a Gemini 3.8 Flash TTS variant built for deep creative direction and character design, that can recreate consistent vocal profiles from just a 30-second audio sample. The release is backed by built-in consent verification, SynthID watermarking, and C2PA credentials, and the models are being integrated into products such as Gemini Notebook and Google Vids. This marks Google's full entry into mainstream voice cloning, a capability it had previously been hesitant to ship, and it raises the bar for the entire TTS market by pairing expressive, multilingual synthesis with provenance safeguards. Developers, creators, and voice talent will all be affected, since cloned voices can now be produced at scale while remaining traceable via watermarks and credentials. To generate single-speaker audio, developers pass a verbatim transcript as input, attach turn-level styling via a speech_metadata annotation, and configure the voice in generation_config.speech_config. The voice replication feature requires that you own the voice or have rights to use it, and the SynthID watermarking and C2PA credentials are designed to survive as provenance signals, though watermark robustness can degrade under re-encoding.

hackernews · swolpers · Sep 23, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49817615)

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio, and recent AI models have made synthetic voices far more natural and expressive. Voice cloning goes further by learning a speaker's vocal characteristics from a short sample so the model can say anything in that voice, which raises ethical concerns about consent, impersonation, and fraud. Watermarking technologies such as SynthID and provenance standards like C2PA embed invisible or verifiable signals in generated audio so listeners and platforms can identify AI-generated content.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/">Gemini 3.8 text-to-speech says hello</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/speech-generation">Text-to-speech generation (TTS) | Gemini API | Google AI for Developers</a></li>
<li><a href="https://voxbooster.com/blog/voice-cloning-watermarking/">Voice Cloning Watermarking : How Providers Tag AI... — VoxBooster</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted Google's inconsistent rollout across its consumer, prosumer, and cloud platforms, noting that the same model can have different capabilities depending on where it runs. Others observed that voice cloning is now common enough from other providers that Google no longer hesitates to ship it, while some shared practical uses such as locally hosted audiobook creation and directing fan-fiction voice casts, praising the large voice library and fine-grained control.

**Tags**: `#AI`, `#text-to-speech`, `#voice cloning`, `#Google Gemini`, `#Hacker News`

---

<a id="item-4"></a>
## [ShinyHunters Claims Breach of FBI Employee and Applicant Data](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

The hacking group ShinyHunters claims to have breached multiple FBI-related services and stolen data on all FBI employees and job applicants, providing a sample of roughly 5,000 individuals that reportedly includes names, home addresses, phone numbers, and family member details such as spouses. The FBI has not yet confirmed the claim, and 404 Media first reported the group's assertion. If the data is authentic, the leaked personal information could be used to track, harass, or threaten FBI employees and their families, and it could pose serious security and counterintelligence risks to U.S. law enforcement and intelligence systems. The claim also highlights how prolific cybercriminal groups like ShinyHunters continue to target high-profile government institutions with large-scale data theft and extortion. The sample of about 5,000 individuals reportedly includes names, home addresses, phone numbers, and details about spouses and other family members, though the FBI has not confirmed the breach and the authenticity of the data remains unverified. ShinyHunters is known for large-scale data theft and extortion campaigns, having previously claimed responsibility for breaches involving Microsoft source code and other major organizations.

telegram · zaihuapd · Sep 23, 05:00

**Background**: ShinyHunters is a cybercriminal group that specializes in large-scale data breaches and extortion, and it has been tracked by authorities including the FBI's Internet Crime Complaint Center (IC3). The FBI has recently faced other significant cyber intrusions, including a 2026 breach of a surveillance-related system that the bureau labeled a 'major incident' with suspected China-linked hackers. 404 Media is an independent technology news outlet that frequently reports on hacking and cybersecurity incidents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/">Hacking group ShinyHunters claims it breached the FBI, stole agents' and applicants' data | TechCrunch</a></li>
<li><a href="https://www.ic3.gov/PSA/2026/PSA260515">Internet Crime Complaint Center (IC3) | ShinyHunters: Cyber Criminal Group Attacks Learning Management System</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#ShinyHunters`, `#national security`

---