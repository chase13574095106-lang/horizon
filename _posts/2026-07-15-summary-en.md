---
layout: default
title: "Horizon Summary: 2026-07-15 (EN)"
date: 2026-07-15
lang: en
---

> From 25 items, 7 important content pieces were selected

---

1. [Stripe and Advent Jointly Bid Over $53B for PayPal](#item-1) ⭐️ 9.0/10
2. [Thinking Machines Releases Inkling, Largest Open-Weights Multimodal Model](#item-2) ⭐️ 8.0/10
3. [Gemma 4 26B Runs at 5 Tokens/sec on 13-Year-Old CPU](#item-3) ⭐️ 8.0/10
4. [Claude web_fetch tool bypass enables data exfiltration](#item-4) ⭐️ 8.0/10
5. [DeepSeek Raises Over $74B in First Round with Unique Control Structure](#item-5) ⭐️ 8.0/10
6. [Sandbox Escape Lets Filza Read iOS 27 Notes Database](#item-6) ⭐️ 8.0/10
7. [Telegram Launches Serverless Platform for Bot Backends](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe and Advent Jointly Bid Over $53B for PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

Stripe and private equity firm Advent International have made a joint offer to acquire PayPal for more than $53 billion, according to sources. The deal would combine two of the largest online payment processors. If completed, the acquisition would create a dominant payments giant controlling Stripe, PayPal, Venmo, Braintree, and Xoom, raising significant antitrust concerns. It could reshape the online payments landscape and impact millions of merchants and consumers. The offer is reportedly valued at over $53 billion, which some analysts have described as a lowball bid. PayPal owns Venmo and Braintree, while Stripe would gain access to PayPal's bank charter, potentially enabling new financial services.

hackernews · rvz · Jul 15, 03:32 · [Discussion](https://news.ycombinator.com/item?id=48915953)

**Background**: Stripe is a leading online payment processor for businesses, while PayPal is a widely used consumer payment platform with subsidiaries like Venmo. Advent International is a global private equity firm with about $100 billion in assets. The deal would face intense antitrust scrutiny due to market concentration in online payments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe , Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/07/15/business/paypal-stripe-advent-takeover-bid.html">PayPal Receives $53 Billion Takeover Offer Involving Stripe</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about reduced competition and higher fees, noting that Stripe restricts certain merchants (e.g., cannabis, adult) that PayPal allows. Some worry about consolidation risk and the loss of payment diversity, while others see strategic value in Stripe gaining PayPal's bank charter.

**Tags**: `#acquisition`, `#payments`, `#antitrust`, `#fintech`, `#Stripe`

---

<a id="item-2"></a>
## [Thinking Machines Releases Inkling, Largest Open-Weights Multimodal Model](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines has released Inkling, the largest open-weights multimodal model that supports audio, optimized for fine-tuning and local deployment. Inkling fills a gap in open-source AI by providing a strong multimodal model with audio capabilities, offering an alternative to closed models and enabling enterprises to customize and own their AI. Inkling is not the strongest overall model but combines multimodal capabilities, efficient thinking, and availability on Tinker for fine-tuning, making it a good open-weights base for customization.

hackernews · vimarsh6739 · Jul 15, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48924912)

**Background**: Open-weights models are AI models whose trained parameters are publicly released, allowing anyone to download and fine-tune them. Multimodal models integrate multiple data types like text, audio, and images, enabling richer understanding. Inkling is notable for being the largest open-weights model with audio support, a feature rare in open-source.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-ai">What is Multimodal AI? | IBM</a></li>

</ul>
</details>

**Discussion**: The community is excited about Inkling's audio capabilities and local deployment, with users sharing resources for running it locally. Some see it as a potential US alternative to Chinese open models like DeepSeek, while others praise its business model of enabling enterprise customization.

**Tags**: `#open-weights`, `#multimodal`, `#AI model`, `#audio`, `#fine-tuning`

---

<a id="item-3"></a>
## [Gemma 4 26B Runs at 5 Tokens/sec on 13-Year-Old CPU](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

A technical blog post demonstrates running Google's Gemma 4 26B A4B model at 5 tokens per second on a 13-year-old Xeon server with no GPU, using CPU-only inference with quantization. This shows that modern large language models can run on legacy hardware, making local AI inference more accessible and reducing dependency on expensive GPUs, which could democratize AI usage. The Gemma 4 26B A4B model uses a Mixture-of-Experts architecture with 26B total parameters and 4B active parameters, and supports speculative decoding for faster inference. The 5 tokens/sec speed was achieved on a dual Xeon E5-2697 v2 system with 256GB DDR3 RAM.

hackernews · neomindryan · Jul 15, 15:34 · [Discussion](https://news.ycombinator.com/item?id=48922434)

**Background**: Large language models typically require powerful GPUs for inference, but quantization techniques like GGUF reduce model size and enable CPU-only execution. Gemma 4 is Google's latest open model family, offering up to 256K context and multilingual support. CPU inference is memory-bandwidth-bound, so older multi-channel DDR3 systems can still perform reasonably.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters debate cost efficiency: some note that inference providers are cheaper than local electricity costs in high-price regions like Germany. Others share similar experiments, achieving 8-12 tokens/sec on comparable hardware. A prediction suggests that by mid-2027, >200B MoE models will run on consumer hardware.

**Tags**: `#LLM`, `#inference`, `#hardware`, `#optimization`, `#local AI`

---

<a id="item-4"></a>
## [Claude web_fetch tool bypass enables data exfiltration](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Researcher Ayush Paul discovered a loophole in Anthropic's Claude web_fetch tool that allowed data exfiltration of user memories by tricking the model into following nested URLs from a malicious honeypot site. Anthropic has since closed the hole by removing the ability for web_fetch to navigate to links within fetched content. This attack demonstrates a practical bypass of Claude's data exfiltration protections, highlighting the ongoing challenge of securing LLM agents against prompt injection and the lethal trifecta of private data, untrusted content, and external communication. It underscores the need for robust architectural boundaries in AI agent design. The attack targeted Claude's web_fetch tool, which normally only allows fetching URLs explicitly provided by the user or from web_search results. The loophole allowed fetching URLs embedded in previously fetched pages, enabling a chain of requests that exfiltrated the user's name, city, and employer.

rss · Simon Willison · Jul 15, 14:21

**Background**: LLM agents like Claude face the 'lethal trifecta' risk: they have access to private data, can communicate externally, and are exposed to untrusted content (e.g., from web pages). Prompt injection attacks exploit this by embedding malicious instructions in content that the model processes. Anthropic had designed web_fetch with restrictions to prevent dynamic URL construction, but the nested-link bypass circumvented those safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (linked in the article) likely includes commentary on the cleverness of the attack and disappointment that Anthropic did not pay a bug bounty due to prior internal discovery. Some may debate the adequacy of the fix and broader implications for AI agent security.

**Tags**: `#AI safety`, `#LLM security`, `#data exfiltration`, `#prompt injection`, `#Claude`

---

<a id="item-5"></a>
## [DeepSeek Raises Over $74B in First Round with Unique Control Structure](https://t.me/zaihuapd/42589) ⭐️ 8.0/10

DeepSeek has completed its first funding round, raising over 500 billion RMB (approximately $74 billion USD), with a valuation exceeding $50 billion. The round uses a special limited partnership structure where investors inject funds into a vehicle controlled by founder Liang Wenfeng, accepting a five-year lock-up and no voting rights. This massive funding round signals strong investor confidence in DeepSeek as a leading AI company, and the unique governance structure allows the founder to maintain control despite raising substantial capital. It could set a precedent for how AI startups balance funding needs with founder autonomy. Founder Liang Wenfeng personally invested 20 billion RMB in this round. Tencent is considering investing 10 billion RMB, and CATL plans to invest 5 billion RMB, potentially becoming the largest external investors. DeepSeek has not commented on the report.

telegram · zaihuapd · Jul 15, 12:56

**Background**: DeepSeek, founded in July 2023 by Liang Wenfeng and affiliated with High-Flyer Quant, is a Chinese AI company known for its large language models. A limited partnership structure allows a founder as general partner (GP) to control the company while investors as limited partners (LPs) provide capital without voting rights. This structure is commonly used in China to maintain founder control while raising funds.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stcn.com/article/detail/3897512.html">DeepSeek，融资大消息！估值达450亿美元？</a></li>
<li><a href="https://www.dehenglaw.com/CN/tansuocontent/0008/032873/7.aspx?MID=0902&AID=">多维度解析DeepSeek股权架构设计 - 德恒探索 - 德恒律师事务所</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#DeepSeek`, `#startup`, `#governance`

---

<a id="item-6"></a>
## [Sandbox Escape Lets Filza Read iOS 27 Notes Database](https://x.com/0xjohnny/status/2077216973256274272) ⭐️ 8.0/10

Developer johnny modified the iOS file manager Filza to exploit a sandbox escape vulnerability on iOS 27 beta 3, allowing it to access the Notes database on an iPhone 17 Pro Max. This demonstrates a practical sandbox escape on the latest iOS beta, highlighting a significant security flaw that could be exploited by malicious apps to access sensitive user data. The exploit bypasses the app's container restrictions, enabling Filza to browse external data including the Notes database. The modified Filza runs on iOS 27 beta 3, which is currently in development.

telegram · zaihuapd · Jul 15, 14:35

**Background**: iOS apps are sandboxed to prevent them from accessing data outside their own container. A sandbox escape vulnerability allows an app to break out of this restriction. Filza is a popular file manager for iOS that normally requires jailbreak or special tools to access the full filesystem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=vB7EN21sxfw">Install Filza File Manager on iOS 18-26 (No Jailbreak) - YouTube</a></li>
<li><a href="https://www.tigisoftware.com/default/?page_id=78">Filza – TIGI Software</a></li>
<li><a href="https://forums.macrumors.com/threads/ios-27-beta-3-bug-fixes-changes-and-improvements.2485019/">iOS 27 Beta 3 ― Bug Fixes, Changes, and Improvements | MacRumors Forums</a></li>

</ul>
</details>

**Tags**: `#iOS`, `#sandbox escape`, `#security`, `#vulnerability`, `#Filza`

---

<a id="item-7"></a>
## [Telegram Launches Serverless Platform for Bot Backends](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram has officially launched a serverless platform that allows developers to deploy bot and Mini App backend code directly on Telegram's infrastructure using a single command, npx tgcloud push. This eliminates the need for developers to manage servers, containers, or scaling, significantly reducing operational overhead and enabling faster, simpler bot development. The code runs in an isolated V8 sandbox adjacent to the Bot API and includes a built-in SQLite database; only JavaScript modules are supported.

telegram · zaihuapd · Jul 15, 16:00

**Background**: Serverless computing allows developers to run code without provisioning or managing servers, automatically scaling with demand. Telegram's platform extends this concept to bot development, providing a tightly integrated environment with its Bot API.

<details><summary>References</summary>
<ul>
<li><a href="https://core.telegram.org/bots/serverless">Telegram Serverless</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#serverless`, `#bots`, `#JavaScript`, `#cloud`

---