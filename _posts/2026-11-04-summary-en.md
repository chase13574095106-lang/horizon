---
layout: default
title: "Horizon Summary: 2026-11-04 (EN)"
date: 2026-11-04
lang: en
---

> From 30 items, 4 important content pieces were selected

---

1. [Qwen 3.8 27B locally interprets model weights, replicating weight-space programming](#item-1) ⭐️ 8.0/10
2. [Postman silently auto-installs AI plugins and attempts to share all API data](#item-2) ⭐️ 8.0/10
3. [US tech giants' hidden AI debt surges 90% to $3.2T in six months](#item-3) ⭐️ 8.0/10
4. [Anthropic IPO Filing Reveals $33.2B Revenue and $104B Net Loss](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 27B locally interprets model weights, replicating weight-space programming](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10

Simon Willison demonstrated that Qwen 3.8 27B, running locally on his laptop, can interpret and modify raw neural network weights, replicating a capability from a recent paper on 'weight-space programming' by Rikiya Takehi et al. The paper showed that frontier models like GPT-6 Astra can read and write weights without tools, and Willison's experiment shows a compact open model can perform a similar task. This suggests that weight-space programming may not be limited to frontier models, potentially democratizing a technique that could change how models are analyzed and edited. If smaller local models can interpret weights, it could enable new debugging, model editing, and interpretability workflows without expensive API calls. The paper's example involved GPT-6 Astra fixing Qwen3.5-0.8B's math reasoning by editing only 0.016% of weights, raising MATH-500 from 7.9% to 48.1%. However, critics like Matthew Honnibal and Sean Goedecke argue the paper conflates tool-free weight interpretation with code-assisted model editing, and question the correctness of interpretations.

rss · Simon Willison · Nov 3, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50355251)

**Background**: Weight-space programming is a term coined in November 2026 by MIT researchers for the approach where a general-purpose LLM reads, interprets, and directly writes the weights of another neural network without gradient descent or a training loop. Traditionally, neural network weights are large arrays of floating-point numbers that are not human-readable, and modifying them requires training. This new approach uses an LLM's reasoning to understand what each part of a network computes and to change weights accordingly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Weight-space_programming">Weight-space programming - Wikipedia</a></li>
<li><a href="https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/">Qwen 3.8 27B on my laptop can interpret model weights , too</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about whether interpretations are correct, with one quoting Shakespeare's 'will they come when you do call for them?' Others praised Qwen 3.8 27B as a capable local model that can match frontier results with human guidance, and raised questions about whether a model can alter its own weights and how this relates to steering vectors and LoRAs.

**Tags**: `#LLM`, `#model-interpretability`, `#weight-space-programming`, `#local-models`, `#research`

---

<a id="item-2"></a>
## [Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370) ⭐️ 8.0/10

A GitHub issue (postmanlabs/postman-app-support#14370) alleges that Postman's desktop app silently auto-installs AI plugins (Codex/Claude) and attempts to share all API request data with Postman's servers, including secrets. The issue has sparked a large Hacker News discussion with over 1,000 points and 340 comments. This raises serious privacy and security concerns for developers who use Postman to test APIs, as sensitive data like API keys and tokens could be exposed. It may accelerate the migration of teams to alternative tools like Bruno, especially in regulated industries such as healthcare. Community members claim that Postman logs detailed information on every API request, including query parameters, and that templating syntax like {{some_secret}} sends the actual secret to Postman's servers. Disabling outgoing traffic to the logging endpoint reportedly breaks the app, and Postman is not HIPAA-compliant according to one user's investigation.

hackernews · sidgarimella · Nov 3, 17:22 · [Discussion](https://news.ycombinator.com/item?id=50354960)

**Background**: Postman is a popular API development and testing tool that allows developers to send HTTP requests, manage collections, and collaborate. Bruno is an open-source, Git-native alternative that stores collections locally as plain text files, avoiding cloud syncing and data collection. The controversy highlights growing concerns about data privacy in developer tools, especially as vendors add AI features that may require sending data to external servers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/postmanlabs/postman-app-support/issues/14370">[SEVERE] Desktop auto - installs Codex/Claude plugins ; installer...</a></li>
<li><a href="https://www.usebruno.com/">Bruno - The Git-Native API Client</a></li>
<li><a href="https://github.com/usebruno/bruno/">GitHub - usebruno/bruno: Opensource IDE For Exploring and ...</a></li>

</ul>
</details>

**Discussion**: The community sentiment is largely negative towards Postman, with users expressing frustration over its bloat, forced logins, and data collection. Many have switched to Bruno, citing its Git-friendly local storage and open-source nature, and one healthcare user reported that Postman was decertified by their cyber team, leading to an overnight migration.

**Tags**: `#privacy`, `#security`, `#api-tools`, `#postman`, `#developer-tools`

---

<a id="item-3"></a>
## [US tech giants' hidden AI debt surges 90% to $3.2T in six months](https://asia.nikkei.com/business/technology/artificial-intelligence/us-tech-giants-hidden-ai-debt-swells-90-to-3.2tn-in-6-months) ⭐️ 8.0/10

A Nikkei report claims that hidden AI-related obligations at US tech giants swelled 90% to $3.2 trillion in just six months, far exceeding on-balance-sheet AI borrowing. The figure has sparked debate over whether these future spending contracts should be classified as debt. The rapid growth of off-balance-sheet AI obligations raises systemic risk concerns because it links hyperscalers to private credit and insurers in ways that are hard to monitor. If AI returns disappoint, these commitments could strain corporate balance sheets and broader market liquidity. Much of the hidden debt is structured through joint ventures and special entities so costs stay off corporate books, and the terms of these contracts—including exit clauses—are often undisclosed. The $3.2T figure compares with roughly $40T in total US government debt, underscoring the scale of the commitments.

hackernews · angry_impala · Nov 3, 21:26 · [Discussion](https://news.ycombinator.com/item?id=50358422)

**Background**: Off-balance-sheet financing allows companies to move obligations outside consolidated accounts while remaining bound to leases, guarantees, and future payments. In the AI infrastructure boom, hyperscalers are funding chips, servers, and data centers through bonds, leases, and private credit, creating what the Bank for International Settlements calls 'shadow borrowing' that is economically akin to debt.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.org/publications/qr-202603/financing-ai-infrastructure-boom-on-and-off-balance-sheet-borrowing">Financing the AI infrastructure boom: on- and off-balance ...</a></li>
<li><a href="https://aitechmodel.com/ai-off-balance-sheet-financing-where-the-obligations-go-and-who-still-owes-money/">AI Off-Balance-Sheet Financing: Where the Obligations Go and ...</a></li>
<li><a href="https://www.cnbc.com/2026/08/14/ai-infrastructure-debt-leverage-risks.html">AI infrastructure debt and leverage draw market scrutiny - CNBC</a></li>

</ul>
</details>

**Discussion**: Commenters strongly challenge the framing, arguing these are signed contracts for future spending rather than true debt, and noting that exit terms are often unknown. Others worry about systemic exposure, with some comparing the scale to US government debt and questioning whether corporate budgets can sustain such spending.

**Tags**: `#AI economics`, `#tech industry`, `#finance`, `#data centers`, `#market risk`

---

<a id="item-4"></a>
## [Anthropic IPO Filing Reveals $33.2B Revenue and $104B Net Loss](https://t.me/zaihuapd/44886) ⭐️ 8.0/10

Anthropic updated its IPO prospectus on Monday, disclosing revenue of $33.24 billion for the first three quarters of 2026 (through September 30), a roughly 1,200% year-over-year increase, with third-quarter revenue alone at about $17 billion. However, net loss for the same period reached $104 billion, far exceeding last year's $25.1 billion loss. The filing offers a rare look at the financials of a leading AI company, showing explosive revenue growth alongside massive accounting losses, which could shape investor expectations for AI IPOs and the industry's economic narrative. It highlights how AI firms are scaling revenue rapidly but remain deeply unprofitable on a GAAP basis. Anthropic stated that the net loss in the first half was primarily driven by fair value changes in convertible notes and derivative liabilities, which do not fully represent actual operating cash burn. This accounting treatment can cause large swings in reported net income as the company's valuation changes.

telegram · zaihuapd · Nov 3, 13:23

**Background**: An IPO prospectus is a formal document filed with regulators that provides detailed financial and business information for investors. Fair value accounting requires certain financial instruments, like convertible notes and derivatives, to be remeasured at current market value, with changes flowing through earnings. For high-growth companies, these non-cash adjustments can create significant reported losses even if operating cash flow is positive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/f/fairvalue.asp">investopedia.com/terms/f/ fairvalue .asp</a></li>
<li><a href="https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/fair_value_measureme/fair_value_measureme__9_US/chapter_6_applicatio_US/64_derivative_assets_US.html">6.4 Derivative assets and derivative liabilities - Viewpoint</a></li>
<li><a href="https://www.sec.gov/search-filings">Search Filings - SEC.gov</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI industry`, `#IPO`, `#financials`, `#revenue growth`

---