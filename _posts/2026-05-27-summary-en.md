---
layout: default
title: "Horizon Summary: 2026-05-27 (EN)"
date: 2026-05-27
lang: en
---

> From 37 items, 7 important content pieces were selected

---

1. [Huawei's 'Tao's Law' Proposes Time-Domain Scaling for Semiconductors](#item-1) ⭐️ 9.0/10
2. [Anthropic and OpenAI Found Product-Market Fit](#item-2) ⭐️ 8.0/10
3. [Go to Support Generic Methods](#item-3) ⭐️ 8.0/10
4. [Private equity's takeover of essential services](#item-4) ⭐️ 8.0/10
5. [Curl Project Overwhelmed by AI-Assisted Security Reports](#item-5) ⭐️ 8.0/10
6. [Critical 7-Zip Heap Overflow Vulnerability Disclosed](#item-6) ⭐️ 8.0/10
7. [Changxin Technology's STAR Market IPO Approved, Aims to Raise 29.5B Yuan](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Huawei's 'Tao's Law' Proposes Time-Domain Scaling for Semiconductors](https://t.me/zaihuapd/41597) ⭐️ 9.0/10

At the 2026 IEEE International Symposium on Circuits and Systems (ISCAS 2026) in Shanghai, Huawei officially announced 'Tao's Law' (τ-law), a new semiconductor scaling principle that replaces traditional geometric scaling with time-domain scaling by systematically reducing the time constant τ. Huawei has already designed and mass-produced 381 chips based on this principle over the past six years, and will launch a new Kirin mobile chip this fall featuring logic folding technology. Tao's Law offers a potential path to extend Moore's Law beyond the physical limits of transistor scaling, which could reshape the semiconductor industry by enabling continued performance improvements without relying solely on advanced process nodes. This breakthrough is particularly significant for China's semiconductor self-sufficiency efforts and could impact global chip design paradigms. The Kirin 2026 chip will be the first commercial implementation of logic folding technology, transitioning from a single-layer to a dual-layer free-logic design, achieving transistor density comparable to 1.4nm-class processes by 2031. Huawei's time-domain scaling optimizes across device, circuit, chip, and system levels by reducing the characteristic time constant τ.

telegram · zaihuapd · May 27, 09:00

**Background**: For decades, the semiconductor industry has followed Moore's Law, which relies on geometric scaling—shrinking transistor dimensions to increase density and performance. However, as transistors approach atomic scales, geometric scaling faces diminishing returns and skyrocketing costs. Tao's Law proposes an alternative: instead of making transistors smaller, reduce the time it takes for signals to propagate, using techniques like logic folding to stack circuits vertically and compress signal paths.

<details><summary>References</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260525A041XU00">华为正式发表「韬（τ）定律」：用「时间缩微」替代「几何缩微」</a></li>
<li><a href="https://www.guancha.cn/economy/2026_05_25_818264.shtml">华为何庭波：今年麒麟芯片首次实施逻辑折叠技术，性能将大幅提升</a></li>
<li><a href="https://www.cnblogs.com/qiniushanghai/p/20166392">华为韬（τ）定律：用"时间缩微"重写半导体演进规则（2026）</a></li>

</ul>
</details>

**Discussion**: Community comments on platforms like Zhihu and Xueqiu show cautious optimism, with many praising the innovative approach but questioning the actual performance gains and commercial viability. Some technical users note that the reported MTR (a density metric) of the Kirin 2026 chip is 238, between TSMC N4 (170-190) and N3 (270-290), suggesting real-world performance may approach TSMC 3nm-class SoCs when combined with Huawei's architecture optimizations.

**Tags**: `#semiconductor`, `#Moore's Law`, `#Huawei`, `#chip design`, `#hardware innovation`

---

<a id="item-2"></a>
## [Anthropic and OpenAI Found Product-Market Fit](https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything) ⭐️ 8.0/10

Simon Willison argues that Anthropic and OpenAI have achieved product-market fit, citing rising enterprise API spending and rumors of Anthropic's first profitable quarter. He notes that both companies have shifted enterprise pricing to API-based usage, leading to unexpectedly high bills for some customers. This signals a major shift in the AI industry: LLM providers are moving from subsidized consumer pricing to profitable enterprise models. If sustained, it validates the economic viability of large language models and could accelerate enterprise adoption, despite concerns about cost and ROI. Anthropic's Enterprise plan now charges $20/seat/month plus API usage, while OpenAI's Codex switched to token-based pricing in April 2026. Willison estimates his personal API costs would be $2,180/month versus his $200 subscription, highlighting the price gap between consumer and enterprise tiers.

rss · Simon Willison · May 27, 16:38 · [Discussion](https://news.ycombinator.com/item?id=48296794)

**Background**: Product-market fit (PMF) is the degree to which a product satisfies strong market demand, often leading to organic growth and profitability. In the AI industry, companies like OpenAI and Anthropic have long faced questions about whether their expensive models could generate sustainable revenue beyond consumer subscriptions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Product-market_fit">Product-market fit - Wikipedia</a></li>
<li><a href="https://www.productplan.com/glossary/product-market-fit">Product-Market Fit | Glossary | ProductPlan</a></li>
<li><a href="https://www.geeksforgeeks.org/product-management/what-is-product-market-fit-definition-importance-and-example/">Product-Market Fit : Definition, Importance and Example</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some agreed that PMF for coding was reached months ago, but questioned the link to profitability. Others highlighted the massive capital expenditure required to sustain growth, and noted that open-source alternatives like GLM-5.1 could undercut the business model.

**Tags**: `#AI`, `#product-market fit`, `#LLMs`, `#enterprise`, `#economics`

---

<a id="item-3"></a>
## [Go to Support Generic Methods](https://github.com/golang/go/issues/77273) ⭐️ 8.0/10

The Go team has officially accepted the proposal to add generic methods to the language, as tracked in issue #77273 on GitHub. This feature will allow methods on structs and interfaces to have their own type parameters, separate from the type's type parameters. This addresses a long-standing gap in Go's generics implementation, enabling more expressive and reusable code patterns such as monads and generic data access methods. It brings Go closer to the expressiveness of other modern languages and will likely increase adoption among developers who previously found Go's generics too restrictive. The proposal was initially deferred in the original generics design as a 'not now, not never' item, and the implementation is expected to be incremental. The change also implies that interface methods may need to support type parameters, though the exact approach is still being discussed.

hackernews · f311a · May 27, 09:02 · [Discussion](https://news.ycombinator.com/item?id=48291575)

**Background**: Go added generics (type parameters) in version 1.18, allowing functions and types to be written to work with any of a set of types. However, methods on generic types could not introduce their own type parameters, limiting patterns like monads or fluent interfaces. This proposal removes that restriction.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/golang/go/issues/77273">spec: generic methods for Go · Issue #77273 · golang/go</a></li>
<li><a href="https://go.dev/doc/tutorial/generics">Tutorial: Getting started with generics - The Go Programming Language</a></li>
<li><a href="https://go.dev/blog/generics-proposal">A Proposal for Adding Generics to Go - The Go Programming Language</a></li>

</ul>
</details>

**Discussion**: The community is largely positive, with users like xena excited about implementing monad libraries and nasretdinov noting the surprising omission. Some commenters like h1fra express skepticism, viewing it as another feature initially deemed unnecessary, while reactordev approves it as filling a major gap for developers from other languages.

**Tags**: `#Go`, `#generics`, `#programming languages`, `#software engineering`

---

<a id="item-4"></a>
## [Private equity's takeover of essential services](https://rubbishtalk.com/economy/how-private-equity-bought-americas-essential-services/) ⭐️ 8.0/10

An analysis reveals how private equity firms have systematically acquired and degraded America's essential services, driven by pension funds' demand for high returns. This trend threatens the quality and accessibility of critical services like healthcare, housing, and utilities, transferring value from current living standards to pension payouts. The article draws parallels to historical practices like Crassus' fire brigade, highlighting how private equity profits from distressed assets while degrading social capital.

hackernews · NoRagrets · May 27, 12:00 · [Discussion](https://news.ycombinator.com/item?id=48292941)

**Background**: Private equity firms use leveraged buyouts to acquire companies, often loading them with debt and cutting costs to boost short-term returns. Pension funds invest in private equity to meet required return rates (e.g., 7%), creating a cycle that prioritizes financial engineering over service quality.

**Discussion**: Commenters note the irony that pension funds drive private equity, transferring value from current living standards to retirement checks. Some draw historical parallels to Crassus, while others lament the stripping of social capital as private equity buys up apartment complexes and other community assets.

**Tags**: `#private equity`, `#economics`, `#essential services`, `#pension funds`, `#public policy`

---

<a id="item-5"></a>
## [Curl Project Overwhelmed by AI-Assisted Security Reports](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 8.0/10

Daniel Stenberg, the maintainer of the curl project, reports that the rate of incoming AI-assisted security reports has increased 4-5 times compared to 2024, now averaging more than one report per day, putting unprecedented pressure on the team. This surge highlights a new challenge for open-source maintenance: AI tools enable high-quality, detailed vulnerability reports at scale, overwhelming small volunteer teams and threatening maintainer well-being and project sustainability. Despite the flood, most vulnerabilities found are of LOW or MEDIUM severity; the last HIGH severity CVE for curl was in October 2023. Stenberg notes that the quality of AI-assisted reports is very high, making them credible and time-consuming to triage.

rss · Simon Willison · May 26, 23:48

**Background**: curl is a widely used open-source command-line tool and library for transferring data with URLs, supporting numerous protocols. It is maintained by a small team of volunteers, with Daniel Stenberg as the lead developer. The project has a strong security track record, but the recent influx of AI-generated reports is straining resources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CURL">cURL - Wikipedia</a></li>
<li><a href="https://curl.se/">curl</a></li>

</ul>
</details>

**Discussion**: The Lobste.rs discussion likely expresses concern for maintainer burnout and debates the role of AI in security research, with some questioning the value of AI-generated reports that rarely find critical flaws.

**Tags**: `#open-source`, `#security`, `#AI`, `#curl`, `#maintenance`

---

<a id="item-6"></a>
## [Critical 7-Zip Heap Overflow Vulnerability Disclosed](https://socprime.com/blog/cve-2026-48095-7-zip-heap-overflow-flaw/) ⭐️ 8.0/10

A critical heap buffer overflow vulnerability (CVE-2026-48095) in 7-Zip's NTFS archive handler has been publicly disclosed, allowing arbitrary code execution or application crashes via crafted archives. The issue was fixed in version 26.01 released on April 27, 2026. This vulnerability significantly expands the attack surface for phishing and social engineering attacks, as 7-Zip's signature-based fallback logic can route crafted files with common extensions like .7z, .zip, or .rar to the vulnerable NTFS parser. Given 7-Zip's widespread use, this poses a serious security risk to millions of users. The vulnerability (GHSL-2026-140) is a heap buffer write overflow in the NTFS archive handler, specifically due to under-allocation of a compressed stream buffer (GetCuSize shift UB). Exploitation can lead to arbitrary code execution via vtable hijack.

telegram · zaihuapd · May 27, 08:01

**Background**: 7-Zip is a free and open-source file archiver widely used for compressing and decompressing files. A heap buffer overflow occurs when a program writes more data to a heap memory buffer than it can hold, potentially allowing an attacker to overwrite adjacent memory and execute malicious code. The NTFS archive handler in 7-Zip is responsible for parsing compressed NTFS data structures.

<details><summary>References</summary>
<ul>
<li><a href="https://securitylab.github.com/advisories/GHSL-2026-140_7-Zip/">GHSL-2026-140: Heap Buffer Write Overflow in 7-Zip</a></li>
<li><a href="https://diamatix.com/7zip-rce-archive-vulnerability/">New 7 - Zip Vulnerability Enables Code Execution Through Crafted...</a></li>
<li><a href="https://cybersecuritynews.com/7-zip-vulnerabilities-code-execution/">New 7 - Zip Vulnerabilities Let Attackers Execute Arbitrary Code and...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#7-Zip`, `#CVE`, `#exploit`

---

<a id="item-7"></a>
## [Changxin Technology's STAR Market IPO Approved, Aims to Raise 29.5B Yuan](https://static.sse.com.cn/stock/disclosure/announcement/c/202605/000001_20260527_SPLE.pdf) ⭐️ 8.0/10

Changxin Technology (CXMT) received approval from the Shanghai Stock Exchange's listing committee for its IPO on the STAR Market, planning to raise 29.5 billion yuan. The funds will be used for memory wafer manufacturing capacity upgrades, DRAM technology upgrades, and forward-looking technology R&D. This IPO is a major milestone for China's semiconductor industry, as CXMT is the only domestic mass producer of DRAM chips. The massive funding will accelerate DRAM technology development, potentially reshaping the global memory market and reducing reliance on foreign suppliers. CXMT's financial data shows a historic breakthrough in Q1 2026, with revenue of 50.8 billion yuan (up 719% YoY) and net profit of 33.012 billion yuan. The company is headquartered in Hefei, Anhui, and specializes in DRAM manufacturing.

telegram · zaihuapd · May 27, 09:12

**Background**: DRAM (Dynamic Random Access Memory) is a type of volatile memory used in computers and mobile devices. Changxin Memory Technologies (CXMT) is China's leading DRAM manufacturer, founded in 2016. The STAR Market (科创板) is China's Nasdaq-style board for tech companies, with less stringent listing requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://x.com/ogawa_tter/status/2059634750944592008">=> CXMT (长鑫科技集团)'s IPO on 上海证券交易所科创板has been ...</a></li>
<li><a href="https://www.itiger.com/news/2636014105">日赚近4亿！存储龙头长鑫科技IPO有新进展，核心受益股一览</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#IPO`, `#DRAM`, `#China`, `#technology`

---