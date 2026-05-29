---
layout: default
title: "Horizon Summary: 2026-05-29 (EN)"
date: 2026-05-29
lang: en
---

> From 27 items, 8 important content pieces were selected

---

1. [vLLM v0.22.0: DeepSeek V4 Maturity, MRv2, Rust Frontend](#item-1) ⭐️ 8.0/10
2. [Is AI Repeating Frontend's Lost Decade?](#item-2) ⭐️ 8.0/10
3. [GTA 6 Developers Form Union at Rockstar Games](#item-3) ⭐️ 8.0/10
4. [Anthropic's Run-Rate Revenue Hits $47 Billion](#item-4) ⭐️ 8.0/10
5. [Anthropic surpasses OpenAI in valuation](#item-5) ⭐️ 8.0/10
6. [Researcher Reveals Multiple Flaws in India's CBSE Exam Grading System](#item-6) ⭐️ 8.0/10
7. [China Certifies 9 Domestic AI Chips for Government Procurement](#item-7) ⭐️ 8.0/10
8. [Blue Origin's New Glenn Rocket Explodes During Static Fire Test](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.22.0: DeepSeek V4 Maturity, MRv2, Rust Frontend](https://github.com/vllm-project/vllm/releases/tag/v0.22.0) ⭐️ 8.0/10

vLLM v0.22.0, released with 459 commits from 230 contributors, brings DeepSeek V4 support to maturity, advances Model Runner V2 toward becoming the default, and introduces an experimental Rust frontend. This release significantly improves inference performance and model support for the widely-used vLLM engine, benefiting developers deploying large language models in production. The Rust frontend and Model Runner V2 enhancements signal a shift toward more efficient and modular inference infrastructure. DeepSeek V4 gains NVFP4 fused MoE support, full and piecewise CUDA graphs, and MTP speculative decoding. Model Runner V2 now automatically selects for Qwen3 dense models and falls back to MRv1 when a KV connector is present. The experimental Rust frontend includes a DP Supervisor for data-parallel serving.

github · khluu · May 29, 10:28

**Background**: vLLM is a high-performance inference engine for large language models, widely used for its speed and flexibility. Model Runner V2 is a ground-up reimplementation of vLLM's execution core aiming for cleaner code and better performance. The Rust frontend is an experimental effort to improve serving efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm-project.github.io/2026/03/24/mrv2.html">Model Runner V2: A Modular and Faster Core for vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek V4`, `#Model Runner V2`, `#Rust frontend`

---

<a id="item-2"></a>
## [Is AI Repeating Frontend's Lost Decade?](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/) ⭐️ 8.0/10

A blog post and community discussion argue that AI tools may be devaluing frontend expertise, similar to how frameworks once deskilled the field, by enabling lower-quality work from less experienced developers. This debate highlights a critical tension between accessibility and quality in web development, affecting how the industry values deep expertise versus broad participation. The article references Alex Russell's term "Frontend's Lost Decade" to describe how frameworks reduced the need for deep expertise, and commenters counter that much of that expertise dealt with accidental complexity, not essential complexity.

hackernews · xyzal · May 29, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48321631)

**Background**: In software engineering, "accidental complexity" refers to problems created by the tools or implementation, not inherent to the problem itself. "Frontend's Lost Decade" describes a period when frameworks like jQuery and React abstracted away browser quirks, making development easier but reducing the need for deep browser knowledge. AI tools now similarly abstract away coding details, raising concerns about deskilling.

<details><summary>References</summary>
<ul>
<li><a href="https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/">Is AI causing a repeat of Frontend ’s Lost Decade ? | Mastro Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/No_Silver_Bullet">No Silver Bullet - Wikipedia</a></li>
<li><a href="https://aiespionage.net/tech-deep-dives/is-ai-causing-a-repeat-of-front-end-s-lost-decade/">Is AI causing a repeat of Front end 's Lost Decade ? - AI Espionage</a></li>

</ul>
</details>

**Discussion**: Commenters like kristianc and kangalioo argue that the lost expertise was largely accidental complexity, and that broader access to building is a net positive. ElProlactin notes that pre-AI work was often mediocre, so quality concerns may be overstated.

**Tags**: `#AI`, `#frontend`, `#web development`, `#software engineering`

---

<a id="item-3"></a>
## [GTA 6 Developers Form Union at Rockstar Games](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/) ⭐️ 8.0/10

Developers working on Grand Theft Auto VI at Rockstar Games have announced the formation of a union, demanding pay transparency, flexible working arrangements, and an end to crunch culture. This unionization effort at one of the world's largest game studios could set a precedent for labor organizing in the gaming and broader tech industry, potentially improving working conditions and product quality. The union's demands focus on three key issues: pay transparency to address wage disparities, flexible working policies, and eliminating crunch—the compulsory overtime common in game development that often involves 65–80 hour weeks.

hackernews · AndrewKemendo · May 29, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48324499)

**Background**: Crunch culture is a widespread practice in the video game industry where developers are required to work extensive overtime, often unpaid, to meet project deadlines. Unionization in the tech sector has historically been low, but recent layoffs and burnout have spurred renewed interest in collective bargaining. Rockstar Games has faced criticism in the past for crunch, particularly during the development of Red Dead Redemption 2.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crunch_(video_games)">Crunch (video games) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unionization_in_the_tech_sector">Unionization in the tech sector - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support for the union, noting the disparity between game developer pay and that of other tech roles, and highlighting the predatory nature of crunch culture. Some discussed challenges of unionizing in tech, such as outsourcing and H-1B visa programs, but overall sentiment was positive, with hopes that unions could improve both worker conditions and game quality.

**Tags**: `#labor`, `#gaming`, `#unionization`, `#tech industry`, `#crunch culture`

---

<a id="item-4"></a>
## [Anthropic's Run-Rate Revenue Hits $47 Billion](https://simonwillison.net/2026/May/29/anthropic/#atom-everything) ⭐️ 8.0/10

Anthropic announced in its Series H funding announcement that its run-rate revenue crossed $47 billion earlier in May 2026, up from $30 billion in April and $9 billion at the end of 2025. This rapid revenue growth—from $9B to $47B in roughly five months—signals massive enterprise adoption of AI and validates Anthropic's business model, potentially influencing investor confidence and industry benchmarks. Run-rate revenue is an annualized projection calculated by multiplying the most recent month's revenue by 12. Anthropic has shared these figures in multiple funding announcements, and lying to investors would constitute securities fraud, lending credibility to the numbers.

rss · Simon Willison · May 29, 01:23

**Background**: Run-rate revenue is a financial metric that extrapolates current revenue over a full year, often used by fast-growing companies to project annual performance. Anthropic is an AI company known for its Claude model, and it has raised massive funding rounds, including a $65B Series H at a $965B post-money valuation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post-money ...</a></li>
<li><a href="https://corporatefinanceinstitute.com/resources/accounting/revenue-run-rate/">Revenue Run Rate - Definition, Calculation, Examples</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">Run Rate Explained: Benefits, Risks, and Business Insights</a></li>

</ul>
</details>

**Discussion**: The post author notes that some skeptics dismissed earlier $30B figures as untrustworthy, but argues that lying in fundraising announcements would be securities fraud. Ed Zitron was extremely skeptical of the $30B number, and the author wonders if he will update his view for the $47B figure.

**Tags**: `#Anthropic`, `#AI industry`, `#revenue`, `#funding`, `#business metrics`

---

<a id="item-5"></a>
## [Anthropic surpasses OpenAI in valuation](https://www.nytimes.com/2026/05/28/technology/anthropic-tops-openai-valuation.html) ⭐️ 8.0/10

Anthropic completed a $65 billion funding round, achieving a post-money valuation of $965 billion, surpassing OpenAI's estimated $852 billion valuation and becoming the highest-valued AI startup. This milestone signals a major shift in the AI startup landscape, highlighting intense competition for capital and talent, and underscores the market's confidence in Anthropic's approach to safe AI development. Anthropic's products include the Claude series of models, and the company has consistently secured large funding rounds. The funds are primarily allocated to computing power, model training, and commercial expansion.

telegram · zaihuapd · May 29, 03:29

**Background**: Anthropic is an AI safety startup founded by former OpenAI employees, focusing on building reliable and interpretable AI systems. OpenAI, the creator of ChatGPT, has long been the dominant player in the AI startup space. The valuation comparison reflects the rapid growth and investor appetite for AI companies.

**Tags**: `#AI`, `#funding`, `#valuation`, `#Anthropic`, `#OpenAI`

---

<a id="item-6"></a>
## [Researcher Reveals Multiple Flaws in India's CBSE Exam Grading System](https://ni5arga.com/blog/posts/hacking-cbse/) ⭐️ 8.0/10

A security researcher disclosed severe vulnerabilities in India's CBSE online exam grading system, including hardcoded master passwords, OTP bypass, and SQL injection, potentially allowing unauthorized score manipulation. These vulnerabilities could compromise the integrity of high-stakes board exams affecting millions of students, highlighting systemic security weaknesses in government IT systems and the challenges of responsible disclosure. The researcher reported the issues to CERT-In on February 25, 2026, but CBSE initially denied the vulnerabilities; the researcher later provided screenshots and discovered an SQL injection before the site was taken offline.

telegram · zaihuapd · May 29, 05:52

**Background**: CBSE (Central Board of Secondary Education) conducts high-stakes board exams for millions of students in India. The online grading system is used by examiners to evaluate answer sheets. Vulnerabilities like hardcoded passwords and client-side OTP validation can allow attackers to bypass authentication and modify scores.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CERT-In">CERT-In</a></li>
<li><a href="https://medium.com/@mr.nt09/how-i-discovered-and-bypassed-otp-verification-an-exciting-journey-e1203f5bb900">How I Discovered and Bypassed OTP Verification: An... | Medium</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability disclosure`, `#web application`, `#education`, `#India`

---

<a id="item-7"></a>
## [China Certifies 9 Domestic AI Chips for Government Procurement](https://www.tomshardware.com/tech-industry/semiconductors/china-certifies-nine-domestic-ai-chips-for-government-procurement) ⭐️ 8.0/10

China's Information Security Evaluation Center has for the first time added an 'AI training and inference chip' category to its security certification framework, certifying nine domestic AI processors for government procurement. The certified chips include products from Huawei, Alibaba's Pingtouge, Biren Technology, and Haiguang, while notable absentees include Cambricon and Baidu's Kunlun Chip. This marks a significant policy shift that will directly influence government and state-owned enterprise AI procurement, boosting domestic chipmakers and potentially reshaping the competitive landscape. It also underscores China's push for technological self-sufficiency amid ongoing US export restrictions on advanced semiconductors. The certification is valid for three years and is based on the 'Security and Reliability Evaluation Guidelines (Trial)'. The nine certified chips span multiple vendors, but the exclusion of Cambricon and Baidu Kunlun suggests that not all domestic AI chips meet the security and reliability standards required.

telegram · zaihuapd · May 29, 08:41

**Background**: The 'Anke' (安全可靠) procurement catalog is a government-approved list of secure and reliable IT products for use by Chinese government agencies and state-owned enterprises. It was originally focused on CPUs, operating systems, and databases, and has now been expanded to include AI chips. This move aligns with China's broader strategy to reduce reliance on foreign technology, especially after US sanctions on advanced AI chips like NVIDIA's A100 and H100.

<details><summary>References</summary>
<ul>
<li><a href="https://www.itsec.gov.cn/aqkkcp/cpgg/202405/t20240520_172866.html">安全可靠测评结果公告（2024年第1号）</a></li>
<li><a href="https://www.cnblogs.com/Magiclala/p/19913570">2026信创目录（信创国产化入围名单）：中国信息安全测评中心安全可靠...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1954867567723258004">安可测评9月更新！国产CPU、操作系统、数据库选型全清单</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#China`, `#government procurement`, `#semiconductors`, `#policy`

---

<a id="item-8"></a>
## [Blue Origin's New Glenn Rocket Explodes During Static Fire Test](https://arstechnica.com/space/2026/05/blue-origins-new-glenn-rocket-just-exploded-during-a-static-fire-test/) ⭐️ 8.0/10

On May 28, 2026, Blue Origin's New Glenn rocket exploded during a static fire test at Cape Canaveral, destroying the vehicle and damaging the launch pad. The explosion occurred while igniting the seven BE-4 methane engines on the first stage, causing a total loss of the rocket and ground infrastructure. This explosion is a major setback for Blue Origin, delaying its return to flight and jeopardizing NASA's Artemis lunar missions and Amazon's Project Kuiper satellite deployment. The incident also raises concerns about the reliability of the BE-4 engine, which is also used by United Launch Alliance's Vulcan rocket. The explosion occurred during the NG-4 mission preparation, which was set to launch 48 Amazon Kuiper satellites. The launch pad's lightning protection tower collapsed, and ground infrastructure was severely damaged, though no injuries were reported. Blue Origin has not yet announced a timeline for recovery or investigation results.

telegram · zaihuapd · May 29, 11:08

**Background**: New Glenn is Blue Origin's heavy-lift orbital rocket, powered by seven BE-4 engines that burn liquid oxygen and liquefied natural gas (methane). The BE-4 is the first oxygen-rich staged combustion engine made in the U.S. and is also used on ULA's Vulcan rocket. Blue Origin had recently been cleared by the FAA to resume flights after a previous anomaly, and this static fire test was intended to validate the rocket before its next launch.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/science/2026/may/29/blue-origin-rocket-explodes">Blue Origin rocket explodes during test in latest setback for Jeff Bezos-owned company | Blue Origin | The Guardian</a></li>
<li><a href="https://www.cnn.com/2026/05/28/science/blue-origin-rocket-anomaly">Blue Origin rocket explodes during ground test | CNN</a></li>
<li><a href="https://en.wikipedia.org/wiki/BE-4">BE-4 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Blue Origin`, `#New Glenn`, `#rocket explosion`, `#NASA Artemis`, `#space industry`

---