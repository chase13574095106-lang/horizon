---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 25 items, 3 important content pieces were selected

---

1. [小米发布 OneVL 一步式潜空间推理框架并开源](#item-1) ⭐️ 9.0/10
2. [三星工会罢工致代工芯片产出骤降 58%](#item-2) ⭐️ 8.0/10
3. [OpenAI 状态：Codex 5.5 和 GPT-5.5 错误率升高](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [小米发布 OneVL 一步式潜空间推理框架并开源](https://mp.weixin.qq.com/s/7po3r6YtmuXm8Xny1bw61Q) ⭐️ 9.0/10

小米发布了 Xiaomi OneVL，这是一个一步式潜空间推理框架，首次将视觉-语言-动作（VLA）模型与世界模型统一在自动驾驶框架中，以 0.24 秒的延迟实现了最先进的结果。该框架已全面开源，包括模型权重、训练和推理代码。 OneVL 是首个在自动驾驶中统一 VLA 和世界模型的框架，延迟仅为自回归方法的 5.4%，同时超越了显式思维链推理。其全面开源可能加速高效、可解释的自动驾驶系统的研发。 OneVL 使用视觉潜空间 token 编码物理因果结构，语言潜空间 token 编码驾驶意图，并在训练中使用双辅助解码器预测未来画面和可读思维链，推理时移除这些解码器。它在 NAVSIM 上取得了 88.84 的 PDM 分数，是首个超越显式 CoT（88.29）的潜空间推理方法。

telegram · zaihuapd · May 13, 10:33

**背景**: 视觉-语言-动作（VLA）模型结合了视觉感知、语言理解和动作生成，用于自动驾驶；世界模型则预测未来状态。传统的 VLA 方法使用自回归思维链推理，速度较慢。OneVL 引入了潜空间推理，即在压缩的 token 空间中进行推理，实现一步并行生成，大幅降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xiaomi-research/onevl">GitHub - xiaomi -research/ onevl · GitHub</a></li>
<li><a href="https://xiaomi-embodied-intelligence.github.io/OneVL/">OneVL : One - Step Latent Reasoning and Planning with...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2604.18486">OneVL : One - Step Latent Reasoning and Planning with... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#VLA`, `#world model`, `#latent reasoning`, `#open source`

---

<a id="item-2"></a>
## [三星工会罢工致代工芯片产出骤降 58%](https://t.me/zaihuapd/41355) ⭐️ 8.0/10

三星电子最大工会报告称，因加薪抗议导致大量员工离岗，周四夜班时段代工芯片和存储芯片产出分别下降 58%和 18%。 作为全球半导体巨头，此次生产中断威胁到本就紧张的存储和代工芯片供应链，可能波及从智能手机到 AI 加速器等多个行业。 工会已发出最后通牒：若资方不妥协，将从 5 月 21 日起启动为期 18 天的全面罢工，这极有可能严重扰乱全球半导体供应。

telegram · zaihuapd · May 13, 01:11

**背景**: 三星是全球最大的半导体制造商之一，生产存储芯片（如 DRAM、NAND）和代工芯片（为客户定制芯片）。全国三星电子工会（NSEU）是三星五个工会中最大的一个，代表约 36,000 名员工。此次争议的核心是要求提高基本工资并取消奖金上限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Samsung_and_unions">Samsung and unions - Wikipedia</a></li>
<li><a href="https://www.techtimes.com/articles/316579/20260513/samsung-electronics-labor-management-post-mediation-talks-collapse-despite-government-intervention.htm">Samsung Electronics Labor-Management Post-Mediation Talks Collapse Despite Government Intervention</a></li>
<li><a href="https://www.upi.com/Top_News/World-News/2026/05/12/Samsung-union-demands-bigger-bonuses-after-criticizing-HBM-strategy/5791778627176/">Samsung union demands bigger bonuses after criticizing HBM strategy - UPI.com</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#supply chain`, `#labor dispute`, `#Samsung`, `#manufacturing`

---

<a id="item-3"></a>
## [OpenAI 状态：Codex 5.5 和 GPT-5.5 错误率升高](http://status.openai.com/) ⭐️ 8.0/10

OpenAI 官方状态页面显示 Codex 5.5 引擎和 GPT-5.5 模型出现高错误率，且错误率持续升高。 此次服务降级直接影响依赖 OpenAI 最新编码和通用模型的开发者和用户，可能中断工作流程和应用程序。 状态页面显示 Codex 5.5 和 GPT-5.5 均存在持续问题，但未提供具体错误率或根本原因细节，也未给出预计解决时间。

telegram · zaihuapd · May 13, 08:56

**背景**: GPT-5.5 是 OpenAI 于 2026 年 4 月 23 日发布的大型语言模型，代号 'Spud'。Codex 5.5 是由 GPT-5.5 驱动的引擎，专为自主编码和软件开发任务设计。这些模型已广泛集成到 GitHub Copilot 和 Microsoft 365 Copilot 等工具中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fastcompany.com/91531659/openai-releases-gpt-5-5-a-more-powerful-engine-for-coding-science-and-general-work">OpenAI releases GPT-5.5, a more powerful engine for coding, science, and general work - Fast Company</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT - 5 . 5 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT - 5 . 5 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#GPT`, `#service outage`, `#status`

---