---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> From 35 items, 8 important content pieces were selected

---

1. [OpenAI 发布由内部前沿模型生成的 722 篇数学手稿](#item-1) ⭐️ 9.0/10
2. [谷歌发布 Gemini 4 Argon，物理推理得分 87%](#item-2) ⭐️ 9.0/10
3. [DeepMind 发布 Genie 4 世界模型，新增音频与实时操控](#item-3) ⭐️ 8.0/10
4. [Python 实验性 JIT 编译器将从 CPython 中移除](#item-4) ⭐️ 8.0/10
5. [AxiomMath 在 Lean 中形式化有限单群分类](#item-5) ⭐️ 8.0/10
6. [美国政府隐瞒关于监视美国人的秘密法庭裁决](#item-6) ⭐️ 8.0/10
7. [报道称 Anthropic 使用盗版斯坦福教授书籍训练 Claude](#item-7) ⭐️ 8.0/10
8. [中国团队称创光纤实时传输速率纪录，达 3.2 Pb/s](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布由内部前沿模型生成的 722 篇数学手稿](https://t.me/zaihuapd/44741) ⭐️ 9.0/10

OpenAI 在 GitHub 上发布了一个合集，包含由内部未公开的前沿模型生成的 722 篇数学手稿和 372 个结果系列，涉及长期未解的问题。许多证明已用 Lean 形式化验证，仓库还指出模型平均每项结果使用约 3 小时 ChatGPT Pro 思考算力，评估期间约尝试 4000 道题，并提供 10 份推理摘要。 这是 AI for Math 领域的一个重大里程碑，表明前沿模型能够为开放问题生成可形式化验证的证明，可能改变自动定理证明和数学发现的方式。这会影响数学家、证明助手开发者以及任何依赖 AI 进行严谨科学推理的人。 这些结果并非全部定稿：部分仍处于验证阶段，而且数学家称模型的自然语言写作文风 unconventional，这引发了关于可读性和同行评审标准的疑问。仓库仅为 372 个结果系列提供了 10 份推理摘要，因此对模型推理过程的透明度有限。

telegram · zaihuapd · Oct 27, 15:00

**背景**: Lean 是一个交互式定理证明器，让数学家以形式化语言编写证明，使每一步逻辑都能由计算机检查。自动定理证明是 AI 的一个长期子领域，专注于让程序发现证明；近期研究将大语言模型与 Lean 等证明助手结合，生成候选证明后再进行形式化验证。OpenAI 此次发布检验了前沿模型能否对真正开放的数学问题做出贡献，而不仅仅是解决基准测试题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/">OpenAI 's math solutions aren't meeting the... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI for Math`, `#OpenAI`, `#Formal Verification`, `#Lean`, `#Automated Theorem Proving`

---

<a id="item-2"></a>
## [谷歌发布 Gemini 4 Argon，物理推理得分 87%](https://t.me/zaihuapd/44743) ⭐️ 9.0/10

谷歌发布了新一代多模态推理模型 Gemini 4 Argon，强化了物理理解、代码生成与视觉语义推理能力。该模型在具身推理基准 ERQA 上凭借纯推理获得 87% 的得分，并能操控波士顿动力 Spot 四足机器人等完成取物、投掷等任务。 此次发布标志着谷歌在具身 AI 领域的领先推进，该领域要求模型对物理世界进行推理以控制机器人。实际机器人任务成功率从 56% 提升至 75%、任务时间从 35 秒降至 24 秒，展示了在机器人和自动化领域的切实影响。 Gemini 4 Argon 已通过 google-genai SDK 提供，定价为每百万输入 token 2 美元、每百万输出 token 2 美元（部分来源列出 4/20 美元）。它还能生成仿真数据以提升真实机器人成功率，根据第三方基准其上下文窗口为 100 万 token。

telegram · zaihuapd · Oct 27, 16:28

**背景**: ERQA（具身推理问答）是 Google DeepMind 作为 Gemini Robotics 发布的一部分而开源的基准，涵盖面向真实机器人场景的空间推理和世界知识。Gemini 4 Argon 是一个多模态模型，可处理文本、图像等模态以对物理任务进行推理，而 google-genai SDK 是谷歌用于访问 Gemini 模型的统一开发者接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/embodiedreasoning/ERQA">GitHub - embodiedreasoning/ERQA: Embodied Reasoning Question ...</a></li>
<li><a href="https://deepmind.google/models/gemini/">Gemini — Google DeepMind | Our next era of frontier intelligence</a></li>
<li><a href="https://github.com/googleapis/python-genai">GitHub - googleapis/python-genai: Google Gen AI Python SDK ...</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#multimodal models`, `#robotics`, `#Google Gemini`, `#embodied reasoning`

---

<a id="item-3"></a>
## [DeepMind 发布 Genie 4 世界模型，新增音频与实时操控](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) ⭐️ 8.0/10

Google DeepMind 发布了新一代交互式世界模拟模型 Genie 4，以研究预览形式推出。它新增了原生音频、高级物理模拟、自然人体运动，以及由 Gemini 模型驱动的实时自然语言操控功能。 Genie 4 将生成式视频推向可交互、可操控的世界模拟，这一能力在机器人、自动驾驶和游戏开发等领域具有潜在应用价值。它的发布也加剧了 Google、腾讯等公司在闭源与开源权重世界模型上的竞争。 该模型能生成逼真的实时交互世界，并允许用户在模拟过程中输入提示词来改变场景。然而，社区测试发现，当物体离开画面再返回时会出现一致性失败，还存在音频标注错误，例如提示萨克斯却生成单簧管声音。

hackernews · acossta · Oct 27, 16:06 · [社区讨论](https://news.ycombinator.com/item?id=50261319)

**背景**: 世界模型是能够根据指令和动作模拟环境未来状态的 AI 系统，理想情况下应遵循物理规律和空间一致性。它们不同于普通视频生成器，后者更注重视觉质量而非持久、因果连贯的模拟。Genie 4 建立在 DeepMind 此前的 Genie 系列之上，并使用 Gemini 模型进行操控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">Genie 4: A new generation of world simulation — Google DeepMind</a></li>
<li><a href="https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/">Google’s Genie 4 world model adds audio, more... | TechCrunch</a></li>
<li><a href="https://arxiv.org/html/2502.20694">WorldModelBench: Judging Video Generation Models As World Models</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者明显持怀疑态度，指出了具体的一致性失败，例如多出一座城堡、骑手离开画面后头盔发生变化。还有人提到音频错误，以及逼真提示词仍生成游戏化画面，同时有评论者指出腾讯的开源权重模型 HY-World 2.0 是未被充分关注的替代方案。

**标签**: `#world-models`, `#generative-ai`, `#deepmind`, `#video-generation`, `#ai-research`

---

<a id="item-4"></a>
## [Python 实验性 JIT 编译器将从 CPython 中移除](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/) ⭐️ 8.0/10

CPython 的实验性 JIT 编译器在 2024 年初被合并到主开发分支，并在 Python 3.15 中得到改进，但在新的 PEP 请求后被移除。这一决定是在 JIT 优化（如自动引用计数操作消除和基于类型的特化）取得重大进展之后做出的。 这一移除影响了 Python 的性能路线图，尤其是 JIT 有望抵消自由线程开销的希望，并将焦点转向 Cython、Numba 和 PyPy 等替代优化策略。它还引发了对 CPython 处理重大性能特性的方式以及社区治理的质疑。 该 JIT 是一个实验性特性，通过 --enable-experimental-jit 配置标志启用，其移除遵循 PEP 836，该 PEP 提议在 CPython 之外维护 JIT 或创建可插拔的 JIT 基础设施。这一决定受到官僚流程和其他性能解决方案可用性的影响。

hackernews · f311a · Oct 27, 11:17 · [社区讨论](https://news.ycombinator.com/item?id=50257419)

**背景**: JIT（即时）编译器在运行时动态将 Python 字节码转换为机器码以提高执行速度，与传统解释器形成对比。CPython 的实验性 JIT 在 Python 3.13 中引入，作为提升性能努力的一部分，同时还有自由线程（移除 GIL）。PEP 744 最初概述了 JIT 计划，但后续讨论导致了 PEP 836，重新评估其未来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0744/">PEP 744 – JIT Compilation | peps.python.org</a></li>
<li><a href="https://peps.python.org/pep-0836/">PEP 836 – JIT Go Brrr: The Path to a Supported JIT ... | peps.python.org</a></li>
<li><a href="https://realpython.com/python315-jit-compiler/">Python's JIT Compiler: What's New in Python 3.15</a></li>

</ul>
</details>

**社区讨论**: 评论者表示失望，指出 JIT 工作一直进展顺利，直到要求新的 PEP，一些人认为移除部分是由于官僚主义。其他人建议使用内联 Cython 装饰器等替代方案，或指出 Cython、Numba 和 PyPy 等现有解决方案，同时质疑为什么 Python 在 JIT 方面相比 Ruby 和 JavaScript 举步维艰。

**标签**: `#Python`, `#JIT`, `#performance`, `#CPython`, `#language design`

---

<a id="item-5"></a>
## [AxiomMath 在 Lean 中形式化有限单群分类](https://cfsg.axiommath.ai/) ⭐️ 8.0/10

AxiomMath 宣布在 Lean 证明助手中完成了有限单群分类（CFSG）的形式化，并声称发现并填补了先前公认的 1000 多页证明中的一个漏洞。 这是形式化数学的一个重大里程碑，因为它表明最大、最复杂的协作证明之一可以被机器验证，从而可能在未来实现更可靠的大规模数学协作。 据报道，形式化过程发现了原始证明中的一个漏洞，并已填补；然而，Lean 形式化的完整细节，包括其完整性和对公理的依赖，尚未从公告中完全明确。

hackernews · pfdietz · Oct 27, 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50261647)

**背景**: 有限单群分类指出，每个有限单群要么属于几个无限族之一，要么是 26 个散在群之一。其原始证明由约 100 位作者撰写，分布在数百篇期刊文章中，总计数万页，主要发表于 1955 年至 2004 年间。Lean 是一种证明助手和函数式编程语言，用于形式化数学，并拥有一个社区驱动的库 mathlib。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups">Classification of finite simple groups</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://leanprover-community.github.io/">Lean community</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一里程碑表示兴奋，一些人指出发现原始证明中的漏洞的意义以及 AI 辅助自动形式化的潜力。其他人则感叹形式化仍然在集合论基础上进行，而不是同伦基础，并讨论了使用前沿模型自动形式化所有数学教科书的可能性。

**标签**: `#Lean`, `#formal-verification`, `#mathematics`, `#group-theory`, `#autoformalization`

---

<a id="item-6"></a>
## [美国政府隐瞒关于监视美国人的秘密法庭裁决](https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/) ⭐️ 8.0/10

《连线》杂志报道称，美国政府隐瞒了一项关于如何监视美国人的秘密法庭裁决，该裁决很可能与《外国情报监视法》（FISA）第 702 条有关。该裁决仍处于保密状态，阻碍了公众和国会的监督。 这种隐瞒破坏了民主监督和透明度，因为秘密法庭裁决可以在公众不知情或未经辩论的情况下授权广泛的监视项目。它影响所有美国人的隐私和公民自由，并引发了对政府权力不受制约的担忧。 该裁决很可能是 FISA 法院对第 702 条的解释，该条款允许对外国目标进行无证监视，但会附带收集美国人的通信。参议员罗恩·怀登警告称，有多届政府依赖一项机密解释并拒绝解密。

hackernews · helterskelter2 · Oct 27, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=50259604)

**背景**: FISA 于 1978 年颁布，旨在水门事件滥用权力后规范美国境内的外国情报监视。2008 年新增的第 702 条允许政府无证收集外国目标的通信，但会附带获取美国人的数据。FISA 法院是一个秘密法庭，负责批准监视请求并发布机密裁决，批评者认为其缺乏对抗性程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foreign_Intelligence_Surveillance_Act">Foreign Intelligence Surveillance Act - Wikipedia</a></li>
<li><a href="https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page">Section 702 of the Foreign Intelligence Surveillance Act ...</a></li>
<li><a href="https://www.cnn.com/2021/11/01/politics/supreme-court-foreign-intelligence-surveillance-court">FISA : Supreme Court won’t say if secretive surveillance court must...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了两党对秘密监视的担忧，一些人称秘密法庭“与民主格格不入”，另一些人指出在监视公民的同时声称自由是虚伪的。许多人提到斯诺登和 Lavabit 等历史事件，认为此类监视从未消失，而公众已经放弃。

**标签**: `#surveillance`, `#privacy`, `#civil-liberties`, `#fisa`, `#government-transparency`

---

<a id="item-7"></a>
## [报道称 Anthropic 使用盗版斯坦福教授书籍训练 Claude](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/) ⭐️ 8.0/10

《斯坦福日报》2026 年 10 月 27 日报道称，Anthropic 非法抓取并盗用了十多位斯坦福教授的著作来训练其 Claude 模型，此前 2026 年 5 月的一项联邦法院裁决已认定相关行为违法。报道还提到，2026 年 7 月获批的 15 亿美元和解协议要求 Anthropic 向数千名作者支付每本书约 3000 美元的赔偿。 此案确立了一个重要先例：使用合法获得的书籍训练 AI 可能属于合理使用，但使用盗版副本则不然，这使 AI 公司面临重大的法律和财务风险。同时，它也加剧了关于 AI 训练伦理以及大型实验室是否应通过授权而非抓取获取内容的广泛争论。 Alsup 法官的裁决区分了受合理使用保护的购买数字书籍与仍构成法律责任的盗版书籍；15 亿美元和解协议覆盖数千名作者，每本书约赔偿 3000 美元。值得注意的是，标题所称“训练本身非法”存在争议，因为文章并未明确说明训练行为违法，只指出获取方式非法。

hackernews · car · Oct 27, 15:28 · [社区讨论](https://news.ycombinator.com/item?id=50260814)

**背景**: AI 公司使用海量文本语料（通常包括书籍）训练大语言模型，而版权法一直难以界定这是否构成合理使用。2026 年，一名联邦法官裁定，使用受版权保护的书籍进行训练具有“极强的转化性”，因而属于合理使用，但明确将盗版内容排除在外，认定其违法。Claude 的开发商 Anthropic 一直以“伦理 AI”自我标榜，这使得盗版训练数据的曝光对其声誉尤为不利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/">Anthropic illegally trained Claude with Stanford professors ...</a></li>
<li><a href="https://apnews.com/article/anthropic-copyright-authors-settlement-training-f294266bc79a16ec90d2ddccdf435164">Anthropic pays authors $1.5 billion to settle copyright ...</a></li>
<li><a href="https://opendatascience.com/federal-judge-rules-ai-training-on-copyrighted-books-is-fair-use-with-key-limitations/">Federal Judge Rules AI Training on Copyrighted Books Is Fair ...</a></li>

</ul>
</details>

**社区讨论**: 评论者就标题准确性展开争论，有人指出应写“非法获取”而非暗示训练本身非法。还有人将其与 Aaron Swartz 案对比，质疑为何 Anthropic 仅面临民事和解，而 Swartz 却依据《计算机欺诈与滥用法》被刑事起诉；也有人批评某教授“奴役劳动”的说法过于夸张。

**标签**: `#AI training data`, `#copyright`, `#Anthropic`, `#AI ethics`, `#legal`

---

<a id="item-8"></a>
## [中国团队称创光纤实时传输速率纪录，达 3.2 Pb/s](https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second) ⭐️ 8.0/10

中国研究团队利用 24 芯光纤实现了每秒 3.2 Pb 的实时传输速率，足以在一秒内传输超过 2 万部 4K 电影。这一成绩超过该团队今年早些时候创下的 2.5 Pb/s 纪录，提升近 30%。 这一里程碑展示了利用商用兼容硬件在空分复用和多波段传输方面的实际进展，可能加速高容量光网络的发展。它表明破纪录的速率正越来越接近实际部署，对电信基础设施和未来网络设计产生影响。 测试采用商用兼容的硬件架构，并验证了空分复用（SDM）及 S+C+L 多波段传输技术。尽管实验室纪录曾达到 5.29 Pb/s，但那些采用了先进或实验性设备与信号处理，而本次成果更强调实际兼容性。

telegram · zaihuapd · Oct 27, 03:45

**背景**: 空分复用（SDM）是一种利用多个空间通道（例如单根光纤中的多个纤芯）传输独立数据流以提高总容量的技术。S+C+L 波段传输是指同时使用 S 波段（短波长）、C 波段（常规）和 L 波段（长波长）来扩展可用光谱。多芯光纤和多波段传输是克服标准单模光纤容量限制的关键方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Space-division_multiplexing">Space-division multiplexing</a></li>
<li><a href="https://www.rp-photonics.com/space_division_multiplexing.html">Space Division Multiplexing – fiber division, high bit rates ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/9748664">Investigation of Long-Haul S-, C- + L-Band Transmission</a></li>

</ul>
</details>

**标签**: `#optical-fiber`, `#networking`, `#space-division-multiplexing`, `#transmission-record`, `#telecommunications`

---