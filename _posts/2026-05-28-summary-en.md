---
layout: default
title: "Horizon Summary: 2026-05-28 (EN)"
date: 2026-05-28
lang: en
---

> From 24 items, 9 important content pieces were selected

---

1. [Anthropic raises $65B in Series H at $965B valuation](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](#item-2) ⭐️ 8.0/10
3. [Just Use Postgres for Durable Workflows](#item-3) ⭐️ 8.0/10
4. [SQLite Publishes AGENTS.md Policy on AI Code](#item-4) ⭐️ 8.0/10
5. [Nvidia CEO: We've effectively abandoned China's AI chip market](#item-5) ⭐️ 8.0/10
6. [Qualcomm and ByteDance in Deal for Custom AI ASIC Chips](#item-6) ⭐️ 8.0/10
7. [Nvidia CEO Plans $150B Annual Investment in Taiwan](#item-7) ⭐️ 8.0/10
8. [BYD Unveils 4nm Autonomous Driving Chip 'Xuanji A3'](#item-8) ⭐️ 8.0/10
9. [US DOJ Subpoenas Reddit and X for Anonymous ICE Critics](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic raises $65B in Series H at $965B valuation](https://www.anthropic.com/news/series-h) ⭐️ 9.0/10

Anthropic announced a $65 billion Series H funding round led by Altimeter Capital, Dragoneer, Greenoaks, and Sequoia Capital, achieving a $965 billion post-money valuation. The company also reported a self-calculated run-rate revenue of $47 billion as of early May 2026. This massive funding round and near-trillion-dollar valuation underscore Anthropic's rapid growth and its emergence as a leading competitor to OpenAI in the AI industry. The revenue milestone suggests strong enterprise adoption of Claude, potentially positioning Anthropic for an IPO and reshaping the competitive landscape. The $65 billion Series H round is one of the largest private funding rounds in history, bringing Anthropic's post-money valuation to $965 billion, just shy of a trillion dollars. The company's self-reported run-rate revenue of $47 billion is an annualized extrapolation of recent monthly revenue, not GAAP revenue.

hackernews · meetpateltech · May 28, 18:09 · [Discussion](https://news.ycombinator.com/item?id=48313048)

**Background**: Run-rate revenue is an annualized figure calculated by multiplying recent monthly or quarterly revenue by 12 or 4, often used by fast-growing private companies to indicate growth trajectory. Post-money valuation represents a company's value immediately after a funding round, including the new capital. Anthropic develops the Claude AI assistant and competes directly with OpenAI's ChatGPT.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post-money ...</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-money_valuation">Post-money valuation</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Anthropic's $47B run-rate revenue and $965B valuation surpass OpenAI, which appears increasingly vulnerable. Some questioned the use of run-rate revenue versus GAAP revenue, while others marveled at the near-trillion-dollar private valuation and speculated about an imminent IPO.

**Tags**: `#AI`, `#funding`, `#valuation`, `#Anthropic`, `#startups`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 8.0/10

Anthropic has released Claude Opus 4.8, a modest upgrade to its frontier model family, and announced Project Glasswing, under which a small number of organizations are using the more powerful Claude Mythos Preview for cybersecurity work. This release signals Anthropic's continued incremental improvement of its Opus line while hinting at a significant leap in capability with Mythos-class models, which have already found over 10,000 high-severity vulnerabilities in critical software through Project Glasswing. Opus 4.8 offers modest but tangible improvements in coding, agentic tasks, and professional work, and now allows users to disable adaptive thinking in the web UI. The Mythos Preview model is currently restricted to a small number of partners due to the need for stronger cyber safeguards.

hackernews · craigmart · May 28, 16:49 · [Discussion](https://news.ycombinator.com/item?id=48311647)

**Background**: Anthropic's Claude model family includes the Opus class (its most capable models) and the Sonnet class. Previous Opus versions (4.5, 4.6, 4.7) have seen incremental improvements. Project Glasswing is a collaborative cybersecurity initiative that uses advanced AI to find vulnerabilities in critical software before malicious actors can exploit them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-8">Introducing Claude Opus 4.8 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/glasswing-initial-update">Project Glasswing: An initial update \ Anthropic</a></li>
<li><a href="https://cybersecuritynews.com/anthropics-claude-mythos-preview-0-days/">Anthropic's Claude Mythos Preview Uncovers 10,000+ 0-Days in ...</a></li>

</ul>
</details>

**Discussion**: Community members noted that Opus 4.8 is the third minor version bump in the Opus 4.5 family, with each posting modest gains, and some users appreciated the ability to disable adaptive thinking. Others expressed excitement about the Mythos model, though some raised concerns about the safety implications of such powerful AI.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#frontier models`, `#cybersecurity`

---

<a id="item-3"></a>
## [Just Use Postgres for Durable Workflows](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

A blog post argues that PostgreSQL can serve as a single backend for durable workflow execution, eliminating the need for multiple specialized systems. This approach reduces system complexity and operational overhead by centralizing data in one place, potentially making durable workflows more accessible to small and medium-sized projects. The article highlights that Postgres already provides ACID transactions, triggers, and advisory locks, which can be leveraged for workflow orchestration without additional infrastructure.

hackernews · KraftyOne · May 28, 18:41 · [Discussion](https://news.ycombinator.com/item?id=48313530)

**Background**: Durable workflows are stateful processes that automatically recover from failures, ensuring that work is completed even if the system crashes. Traditionally, they require dedicated workflow engines like Temporal or Azure Durable Functions, adding complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/durable-workflow/workflow">GitHub - durable-workflow/workflow: Durable workflow engine ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared real-world experiences: one user uses Postgres for multiple purposes including workflow, vector search, and queue, noting that scaling to terabytes may require migration. Another mentioned the 'absurd' project as an alternative implementation, while others compared DBOS and Temporal, citing payload size limits as a pain point.

**Tags**: `#PostgreSQL`, `#durable workflows`, `#software architecture`, `#distributed systems`

---

<a id="item-4"></a>
## [SQLite Publishes AGENTS.md Policy on AI Code](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite has added an AGENTS.md file to its repository, explicitly stating it does not accept agentic (AI-generated) code, but welcomes bug reports and documentation patches from AI agents. The project also split AI-generated bug reports into a separate Bug Forum due to flooding. This is one of the first major open-source projects to formally define its stance on AI-generated contributions, setting a precedent for how the community handles the influx of automated code and reports. It highlights the tension between leveraging AI for productivity and maintaining code quality and legal clarity. The policy requires that any pull request be accompanied by legal paperwork placing it in the public domain, and human developers may reimplement changes from proof-of-concept PRs. The most recent commit removed the word "currently" from the statement about agentic code, strengthening the rejection.

rss · Simon Willison · May 27, 23:44

**Background**: SQLite is a widely-used embedded SQL database engine written in C, with its source code in the public domain. Agentic coding refers to AI systems that autonomously plan, write, and test code across multiple steps, as opposed to simple autocomplete or single-file rewrites. The rise of such tools has led to an influx of low-quality automated contributions in many open-source projects.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sqlite/sqlite/blob/master/AGENTS.md">sqlite/AGENTS.md at master - GitHub</a></li>
<li><a href="https://simonwillison.net/2026/May/27/sqlite-agents/">sqlite AGENTS.md - simonwillison.net</a></li>
<li><a href="https://themodelwire.com/article/sqlite-agents-md-01KSNXFG179RJA3K5FQ9TXJ1R2">sqlite AGENTS.md · Modelwire</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the news item.

**Tags**: `#SQLite`, `#AI agents`, `#open source policy`, `#software engineering`

---

<a id="item-5"></a>
## [Nvidia CEO: We've effectively abandoned China's AI chip market](https://t.me/zaihuapd/41609) ⭐️ 8.0/10

Nvidia CEO Jensen Huang stated that due to US export controls, the company has effectively abandoned the Chinese AI chip market, ceding it to local competitors like Huawei. He told investors not to expect any licenses to sell advanced chips in China. This marks a major strategic shift in the global AI chip landscape, as Nvidia—the dominant AI chip supplier—concedes a key market to Chinese rivals. It underscores the deepening impact of US-China tech decoupling and the rise of Huawei's domestic chip ecosystem. China once accounted for at least one-fifth of Nvidia's data center revenue. After the Trump administration required export licenses for chips to China in April 2025, Nvidia was effectively shut out. Huang noted that Huawei and the local chip ecosystem are very strong, while Nvidia is using its capital for supply chain expansion and an $80 billion stock buyback.

telegram · zaihuapd · May 28, 03:03

**Background**: Since 2022, the US has imposed escalating export controls on advanced AI chips and semiconductor equipment to China, aiming to limit China's AI capabilities. These restrictions have targeted Nvidia's high-end GPUs like the A100 and H100, and later the H800 and B200. In response, Chinese companies like Huawei have accelerated development of their own AI chips, such as the Ascend series, and built a domestic ecosystem to reduce reliance on foreign technology.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202505/26/WS68345586a310a04af22c1940.html">Huawei builds robust AI chip ecosystem despite US bans</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/huaweis-ascend-ai-chip-ecosystem-scales">Huawei's Ascend AI chip ecosystem scales up as China pushes ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI chips`, `#China`, `#export controls`, `#Huawei`

---

<a id="item-6"></a>
## [Qualcomm and ByteDance in Deal for Custom AI ASIC Chips](https://t.me/zaihuapd/41616) ⭐️ 8.0/10

Qualcomm has reportedly reached an agreement with ByteDance to supply millions of custom AI ASIC chips, which will support ByteDance's AI services and help convert its internal chip designs into mass-producible semiconductors. This deal signals a major investment in AI infrastructure by ByteDance and highlights Qualcomm's growing role in the custom AI chip market, potentially reshaping the AI hardware supply chain. The custom ASICs are designed specifically for AI workloads, offering higher efficiency than general-purpose chips. Qualcomm previously announced it would deliver its first ASIC to a hyperscaler cloud provider in April.

telegram · zaihuapd · May 28, 07:09

**Background**: ASICs (Application-Specific Integrated Circuits) are chips tailored for a specific use case, such as AI inference or training, offering performance and power advantages over CPUs or GPUs. Major tech companies like Google, Amazon, and Meta have increasingly turned to custom ASICs to optimize their AI operations. Qualcomm, traditionally known for mobile chips, is expanding into the AI ASIC space, competing with Broadcom and Marvell.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia">The custom AI ASIC state of play (May 2026) — Broadcom deals ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Qualcomm`, `#ByteDance`, `#ASIC`, `#hardware`

---

<a id="item-7"></a>
## [Nvidia CEO Plans $150B Annual Investment in Taiwan](https://arstechnica.com/tech-policy/2026/05/nvidia-ceo-wants-taiwan-to-be-center-of-ai-revolution-not-us/) ⭐️ 8.0/10

Nvidia CEO Jensen Huang announced plans to invest approximately $150 billion annually in Taiwan, positioning it as the center of the AI revolution. The investment covers AI chip production, system manufacturing, and supply chain partnerships, with a new headquarters in Taipei expected to start construction this year and open by 2030. This massive investment underscores Taiwan's critical role in the global AI supply chain, particularly through partnerships with TSMC, Foxconn, Wistron, and Quanta. It signals a long-term commitment that could reshape geopolitical dynamics in tech manufacturing. The annual investment of $150 billion is a significant increase from the previous $10-15 billion per year. The new Taipei headquarters will accommodate 4,000 employees, and the investment will flow into TSMC capacity reservations, advanced packaging, high-end substrates, networking equipment, and cooling products.

telegram · zaihuapd · May 28, 07:33

**Background**: Nvidia is the leading designer of AI chips, and Taiwan's semiconductor ecosystem, anchored by TSMC, is central to its production. The company's supply chain includes major Taiwanese manufacturers like Foxconn, Wistron, and Quanta for AI server assembly. This investment deepens Nvidia's reliance on Taiwan despite geopolitical tensions.

<details><summary>References</summary>
<ul>
<li><a href="https://nai500.com/zh-hans/blog/2026/05/nvidia-nvda-1500-tsm/">重金押注中国台湾，英伟达深度绑定台积电 | NAI 500</a></li>
<li><a href="https://www.sohu.com/a/897607818_121924584">深度解析：英伟达与台积电的技术领先与合作突破_芯片_黄仁_全球</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI`, `#Taiwan`, `#investment`, `#hardware`

---

<a id="item-8"></a>
## [BYD Unveils 4nm Autonomous Driving Chip 'Xuanji A3'](https://finance.sina.com.cn/roll/2026-05-28/doc-inhznenn1371824.shtml) ⭐️ 8.0/10

BYD announced the 'Xuanji A3', a 4nm autonomous driving chip, at its 'Dare to Be' intelligent strategy conference on May 28, 2026. The chip has entered mass production and supports L3 and L4 autonomous driving, with three chips delivering a total computing power exceeding 2100 TOPS. This marks China's first 4nm autonomous driving chip, showcasing BYD's vertical integration capability and reducing reliance on external suppliers. The high computing power and support for L3/L4 could accelerate the adoption of advanced autonomous driving in mass-market vehicles. BYD claims the chip achieves 100% higher computing power utilization through self-developed algorithm optimization. The company now operates five wafer fabs and has introduced over 2,000 chip products, positioning itself as the only automaker with full-chip manufacturing capabilities.

telegram · zaihuapd · May 28, 13:01

**Background**: TOPS (Tera Operations Per Second) measures a chip's performance for AI tasks, with 1 TOPS equaling one trillion operations per second. L3 autonomous driving allows the vehicle to handle most driving tasks but requires driver takeover when requested, while L4 can operate without human intervention in defined conditions. BYD's chip is built on a 4nm process, a leading-edge node for automotive chips.

<details><summary>References</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260528A099SA00">比亚迪发布自研4nm智驾芯片“璇玑A3”，整车算力超2100TOPS</a></li>
<li><a href="https://xueqiu.com/1290568231/391574806">比亚迪璇玑A3：中国首款4纳米智驾芯片深度解析</a></li>
<li><a href="https://www.ithome.com/0/956/780.htm">中国首款：比亚迪自研 4nm 智驾芯片璇玑 A3 发布，支持 L3、L4 自动驾...</a></li>

</ul>
</details>

**Tags**: `#芯片`, `#自动驾驶`, `#比亚迪`, `#4nm`

---

<a id="item-9"></a>
## [US DOJ Subpoenas Reddit and X for Anonymous ICE Critics](https://www.bloomberg.com/news/articles/2026-05-28/trump-s-doj-ramps-up-probes-of-anonymous-ice-critics-with-x-reddit-subpoenas) ⭐️ 8.0/10

The U.S. Department of Justice has escalated from administrative subpoenas to grand jury subpoenas, demanding that Reddit and X provide the names, addresses, and bank information of at least two anonymous accounts that criticized ICE enforcement actions. This move raises serious concerns about free speech, privacy, and government overreach, as it targets anonymous critics of a federal agency and could deter future whistleblowing or dissent on social media platforms. The affected users have been notified by the platforms and have retained lawyers to challenge the subpoenas in court, but they have not been told what specific crime they are suspected of. A judge is currently reviewing motions to quash the subpoenas.

telegram · zaihuapd · May 28, 14:22

**Background**: ICE (U.S. Immigration and Customs Enforcement) is a federal law enforcement agency under the Department of Homeland Security responsible for enforcing immigration laws. Grand jury subpoenas are legal orders issued as part of a criminal investigation, requiring recipients to produce evidence or testimony. This case highlights the tension between government investigative powers and the right to anonymous speech online.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ice.gov/">ICE | U.S. Immigration and Customs Enforcement</a></li>
<li><a href="https://zh.wikipedia.org/wiki/特朗普第二任期内美国移民执法人员枪击事件列表">zh.wikipedia.org/wiki/特朗普第二任期内 美 国 移 民 执 法 人员枪击事件列表</a></li>

</ul>
</details>

**Tags**: `#free speech`, `#privacy`, `#government surveillance`, `#social media`, `#legal`

---