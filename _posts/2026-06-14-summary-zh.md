---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 23 items, 8 important content pieces were selected

---

1. [Pyodide 314.0 支持直接向 PyPI 发布 WASM 轮子](#item-1) ⭐️ 9.0/10
2. [里约热内卢自研大语言模型被指为现有模型的加权合并](#item-2) ⭐️ 8.0/10
3. [Jane Street 谈形式化方法与编程的未来](#item-3) ⭐️ 8.0/10
4. [2014 年演讲预言 JavaScript 的兴衰](#item-4) ⭐️ 8.0/10
5. [2026 年一季度美国 75 个数据中心项目被阻，总值 1300 亿美元](#item-5) ⭐️ 8.0/10
6. [华为开源盘古 2.0 模型，参数高达 505B](#item-6) ⭐️ 8.0/10
7. [美国以国家安全为由要求 Anthropic 限制两款 AI 模型](#item-7) ⭐️ 8.0/10
8. [全球地下真菌网络首张总图绘出](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pyodide 314.0 支持直接向 PyPI 发布 WASM 轮子](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

Pyodide 314.0 允许包维护者直接将 WebAssembly (WASM) 轮子发布到 PyPI，无需 Pyodide 维护者手动审核。这一变化得益于 4 月 21 日合并到 PyPI 仓库的 PR。 这消除了 Python 在浏览器中运行的一个主要瓶颈，使任何包维护者都能为 Pyodide 和其他基于 WASM 的运行时分发 Python 包，无需等待手动审核。这极大地扩展了浏览器中可用的 Python 包生态系统。 新的平台标签 'pyemscripten'（由 PEP 783 定义）用于 WASM 轮子。Simon Willison 通过发布一个 'luau-wasm' 包演示了该功能，该包通过一个 276KB 的轮子在 Pyodide 中运行 Luau 语言。

rss · Simon Willison · Jun 13, 23:55

**背景**: Pyodide 是一个基于 WebAssembly 的浏览器和 Node.js Python 发行版。此前，Pyodide 维护者必须自行构建和托管超过 300 个包，造成了巨大负担。PEP 783 提出了一个用于基于 Emscripten 的 Python 包的新平台标签，本次发布实现了该提案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.0</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 - Emscripten Packaging - peps.python.org</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（通过 Simon Willison 的帖子）非常积极，许多人对消除手动审核瓶颈表示兴奋。一些评论者指出，这将增加包的可用性并简化基于 WASM 的 Python 项目的分发。

**标签**: `#Pyodide`, `#WASM`, `#Python`, `#PyPI`, `#WebAssembly`

---

<a id="item-2"></a>
## [里约热内卢自研大语言模型被指为现有模型的加权合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

GitHub 上的一项调查显示，里约热内卢声称自研的大语言模型 Rio-3.5-Open-397B 实际上是约 60%的 Nex-N2 Pro 和 40%的 Qwen3.5-397B-A17B 的加权合并，没有证据表明进行了额外训练或蒸馏。 这一争议引发了对 AI 开发中透明度和适当归属的关键质疑，尤其是对于公共部门项目，并凸显了当模型源自现有工作时需要明确披露的必要性。 分析发现，Rio-3.5-Open-397B 中的每个权重张量在所有 60 层和组件中，以数千个标准差的程度，都是 Nex 和 Qwen 的 0.6/0.4 混合，这无法用微调来解释。

hackernews · unrvl22 · Jun 14, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将多个预训练模型的权重组合成单个模型的技术，通常使用线性插值或更高级的方法如 TIES-Merging。这可以在不进行额外训练的情况下提升性能，但需要正确归属原始模型。里约热内卢市政府发布了 Rio-3.5-Open-397B，声称是 Qwen3.5 的自研微调版本，并宣称其性能优于同类开源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/arcee-ai/mergekit">GitHub - arcee-ai/mergekit: Tools for merging pretrained ...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs - NVIDIA Developer</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：有人认为该模型可能经过了未上传的 on-policy 蒸馏，而另一些人则批评缺乏归属和透明度。一位评论者指出，简单的权重线性组合提升了性能，凸显了深度学习模型的鲁棒性。

**标签**: `#LLM`, `#open-source`, `#AI ethics`, `#model merging`, `#controversy`

---

<a id="item-3"></a>
## [Jane Street 谈形式化方法与编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street 发布了一篇博客文章，讨论形式化方法在现代编程中的作用，强调其实际用途和未来潜力，尤其是在 AI 生成代码兴起的背景下。 这一讨论意义重大，因为形式化方法可以数学上验证代码的正确性，这在 AI 代理生成大量需要验证的代码时变得至关重要。它标志着行业向将形式化验证融入日常软件开发的转变。 Jane Street 正在组建一个新的形式化方法团队，旨在使形式化方法像类型系统一样对构建软件有用。这篇博客是一个系列的一部分，探讨形式化方法如何为代理编程提供反馈并验证代理生成的代码。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法是用于规范、开发和验证软件与硬件系统的数学技术。它们允许开发者证明程序在所有可能的输入下都能正确运行，超越了测试所能达到的范围。Jane Street 是一家量化交易公司，历史上对形式化方法持怀疑态度，但现在看到了它们在确保复杂系统可靠性方面的价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.janestreet.com/formal-methods-at-jane-street-index/">Jane Street Blog - Formal methods and the future of programming</a></li>
<li><a href="https://consensys.io/blog/embracing-the-power-of-formal-methods-in-my-coding-journey">Embracing the Power of Formal Methods in my Coding... | Consensys</a></li>
<li><a href="https://zipcpu.com/blog/2017/10/19/formal-intro.html">My first experience with Formal Methods</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了不同的观点：一些人回忆了早期的证明自动化工具，如 Boyer-Moore 证明器，而另一些人则讨论了在 Scala 3 中使用表达性类型进行编译时证明。一个共同的主题是形式化方法有可能将人类价值从编写代码转移到验证代码，尤其是在 AI 生成代码的情况下。然而，也有人质疑形式化规范是否只是另一种形式的测试，可能遭受同样的错误。

**标签**: `#formal methods`, `#programming`, `#verification`, `#Jane Street`, `#software engineering`

---

<a id="item-4"></a>
## [2014 年演讲预言 JavaScript 的兴衰](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

Gary Bernhardt 在 2014 年的一场演讲中幽默地预言 JavaScript 将成为通用编译目标，并最终被新技术取代，这一预言随着 WebAssembly 的兴起已被证明非常准确。 该演讲的先见之明凸显了 Web 技术的快速演进，以及将 JavaScript 用作中间语言的持续趋势，而 WebAssembly 现在正扮演高性能应用低级编译目标的角色。 演讲特别提到了 asm.js 作为早期编译目标，但后来已被 WebAssembly 取代；WebAssembly 是一种在浏览器中本地运行的二进制格式，并得到所有主要厂商的支持。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: JavaScript 最初被设计为一种简单的浏览器脚本语言，但随着时间的推移，它成为了 Web 的事实标准语言。开发者开始使用 TypeScript 和 CoffeeScript 等工具，这些工具将代码转译为 JavaScript，将其视为编译目标。WebAssembly 于 2015 年宣布，2017 年首次发布，是一种低级二进制格式，旨在成为 C、C++和 Rust 等语言的可移植编译目标，从而在 Web 上实现接近原生的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://www.hanselman.com/blog/javascript-is-web-assembly-language-and-thats-ok">JavaScript is Web Assembly Language and... - Scott Hanselman's Blog</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该演讲惊人的准确性，有人提到预言中 2020-2025 年间的全球灾难类型虽错但确实发生了。其他人讨论了 WebAssembly 的局限性，例如缺乏直接的 DOM 访问，需要 JavaScript 作为胶水代码，或采用 canvas 等替代渲染方式。

**标签**: `#JavaScript`, `#WebAssembly`, `#programming languages`, `#compilation target`

---

<a id="item-5"></a>
## [2026 年一季度美国 75 个数据中心项目被阻，总值 1300 亿美元](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs) ⭐️ 8.0/10

2026 年第一季度，美国超过 75 个数据中心建设项目被阻止或推迟，总价值约 1300 亿美元，数量已与 2025 年全年持平。 反对声浪激增标志着美国能源和基础设施政策的重大转变，可能减缓 AI 和云计算的扩张，同时增加科技公司的成本。 草根反对组织在三个月内从 396 个激增至 833 个，遍布 49 个州；跨党派议员提出了大量监管法案，包括一项暂停 AI 数据中心建设的联邦提案。

telegram · zaihuapd · Jun 14, 03:03

**背景**: 数据中心消耗大量电力和水资源，能源成本通常占运营费用的 30-60%。AI 的快速发展推动了数据中心需求激增，加剧了当地对电网压力、电价上涨和环境影响担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/人工智能数据中心暂停法案/67555903">人工智能数据中心暂停法案_百度百科</a></li>
<li><a href="https://news.sina.cn/bignews/insight/2026-03-30/detail-inhstpia4074354.d.html?vt=4">桑德斯提案暂停AI数据中心建设，美国国会如何在监管与创新间取得平衡...</a></li>
<li><a href="https://www.winzheng.com/article/sanders-aoc-ban-data-centers">桑德斯与AOC联手提议：暂停新建数据中心，直至AI监管到位</a></li>

</ul>
</details>

**标签**: `#data centers`, `#energy policy`, `#AI infrastructure`, `#regulation`, `#environment`

---

<a id="item-6"></a>
## [华为开源盘古 2.0 模型，参数高达 505B](https://t.me/zaihuapd/41948) ⭐️ 8.0/10

在 2026 年华为开发者大会上，华为宣布开源 openPangu 2.0 模型，包含 505B 参数的 Pro 版和 92B 参数的 Flash 版，支持 512K 上下文窗口。公司计划从 2026 年 6 月 30 日起陆续开源七大组件。 此次发布使华为成为开源大语言模型领域的重要参与者，挑战 Meta 的 Llama 等全球领先者。通过开源针对昇腾 AI 芯片和鸿蒙系统优化的模型，华为旨在构建国产 AI 生态，减少对外部硬件的依赖。 Pro 版拥有 505B 参数，Flash 版拥有 92B 参数，均支持 512K token 上下文窗口。这些模型针对华为昇腾 AI 算力进行了优化，并兼容鸿蒙系统，开源组件包括预训练代码等将从 2026 年 6 月 30 日起陆续发布。

telegram · zaihuapd · Jun 14, 08:05

**背景**: 大语言模型（LLM）是在海量文本数据上训练、能生成类人文本的 AI 模型。华为盘古系列是其旗舰 LLM 家族，开源后全球开发者可以使用、修改并基于这些模型进行开发。华为的昇腾 AI 处理器和鸿蒙系统是其计算生态的关键组成部分，分别与 NVIDIA GPU 和 Android/iOS 竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://e.huawei.com/cn/products/computing/ascend">昇腾计算-华为Ascend-AI计算-华为企业业务</a></li>
<li><a href="https://zh.wikipedia.org/wiki/鸿蒙操作系统">鸿蒙操作系统 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Large Language Model`, `#Huawei`, `#Deep Learning`

---

<a id="item-7"></a>
## [美国以国家安全为由要求 Anthropic 限制两款 AI 模型](https://t.me/zaihuapd/41949) ⭐️ 8.0/10

美国商务部向 Anthropic 发出出口管制指令，要求暂停任何外国公民在美国境内外访问 Fable 5 和 Mythos 5 AI 模型。Anthropic 已遵守指令，突然关闭了这两款模型对所有客户的访问，包括其外籍员工。 这标志着政府在 AI 模型分发方面的干预显著升级，为基于国家安全的出口管制树立了先例。它直接影响全球对尖端 AI 能力的访问，并引发对外国公民歧视性待遇的担忧。 该指令的出台是由于担心模型可能被越狱以产生危险能力，例如识别主要操作系统和浏览器中的零日漏洞。Anthropic 表示其他 Claude 模型不受影响，并正在努力尽快恢复访问。

telegram · zaihuapd · Jun 14, 09:06

**背景**: Fable 5 和 Mythos 5 是 Anthropic 最先进的 AI 模型，其中 Mythos 5 是 Fable 5 的一个版本，增强了网络安全和生物学方面的保障。美国政府将出口管制应用于 AI 模型是一个相对较新但日益增长的趋势，因为对双重用途 AI 技术带来的国家安全风险的担忧日益加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order">Anthropic to disable its most advanced AI models after US order...</a></li>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following... | Fortune</a></li>
<li><a href="https://www.euronews.com/my-europe/2026/06/14/us-export-controls-on-anthropic-should-not-be-discriminatory-eu-commission-warns">US export controls on Anthropic 'should not be... | Euronews</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#export controls`, `#Anthropic`, `#national security`, `#Claude`

---

<a id="item-8"></a>
## [全球地下真菌网络首张总图绘出](https://insideclimatenews.org/news/11062026/earths-massive-underground-fungal-networks/) ⭐️ 8.0/10

由地下网络保护协会（SPUN）领导的新研究首次绘制出全球丛枝菌根真菌网络地图，估算菌丝总长度达 110 千万亿公里，每年可封存 10 亿吨碳。 该地图显示农田真菌密度仅为野生生态系统的一半，而拥有全球 40%真菌生物量的草原正以森林 4 倍的速度转为农田，凸显了自然碳封存面临的严峻威胁。 菌丝总长度约为地球与太阳距离的近十亿倍，总质量约为全人类体重的 5 倍。这些网络与全球约 80%的植物物种共生。

telegram · zaihuapd · Jun 14, 14:58

**背景**: 丛枝菌根真菌（AMF）与植物根系形成共生关系，帮助植物吸收养分并换取碳。这些地下网络对土壤健康和碳储存至关重要。SPUN 是一个专门为绘制和保护这些真菌网络而成立的组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://madechango.com/study-guide/view/2108">Threads of underground fungal networks are long enough to reach...</a></li>

</ul>
</details>

**标签**: `#fungal networks`, `#carbon sequestration`, `#ecology`, `#climate change`, `#mycorrhizal fungi`

---