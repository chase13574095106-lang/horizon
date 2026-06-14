---
layout: default
title: "Horizon Summary: 2026-06-14 (EN)"
date: 2026-06-14
lang: en
---

> From 23 items, 8 important content pieces were selected

---

1. [Pyodide 314.0 Enables Direct WASM Wheel Publishing to PyPI](#item-1) ⭐️ 9.0/10
2. [Rio's Homegrown LLM Revealed as Weighted Merge of Existing Models](#item-2) ⭐️ 8.0/10
3. [Jane Street on Formal Methods and the Future of Programming](#item-3) ⭐️ 8.0/10
4. [2014 Talk Predicted JavaScript's Rise and Fall](#item-4) ⭐️ 8.0/10
5. [75 US data center projects worth $130B blocked in Q1 2026](#item-5) ⭐️ 8.0/10
6. [Huawei Open-Sources Pangu 2.0 Models with Up to 505B Parameters](#item-6) ⭐️ 8.0/10
7. [US orders Anthropic to restrict two AI models over national security](#item-7) ⭐️ 8.0/10
8. [First Global Map of Underground Fungal Networks Revealed](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pyodide 314.0 Enables Direct WASM Wheel Publishing to PyPI](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

Pyodide 314.0 allows package maintainers to publish WebAssembly (WASM) wheels directly to PyPI, eliminating the need for manual review by Pyodide maintainers. This change is supported by a PR to PyPI's warehouse that landed on April 21st. This removes a major bottleneck for Python in the browser, enabling any package maintainer to distribute Python packages for Pyodide and other WASM-based runtimes without waiting for manual review. It significantly expands the ecosystem of Python packages available in the browser. The new platform tag 'pyemscripten' (defined in PEP 783) is used for WASM wheels. Simon Willison demonstrated the feature by publishing a 'luau-wasm' package that runs the Luau language in Pyodide via a 276KB wheel.

rss · Simon Willison · Jun 13, 23:55

**Background**: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly. Previously, the Pyodide maintainers had to build and host over 300 packages themselves, creating a significant burden. PEP 783 proposed a new platform tag for Emscripten-based Python packages, which this release implements.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.0</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 - Emscripten Packaging - peps.python.org</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (via Simon Willison's post) was highly positive, with many expressing excitement about the removal of the manual review bottleneck. Some commenters noted the potential for increased package availability and easier distribution for WASM-based Python projects.

**Tags**: `#Pyodide`, `#WASM`, `#Python`, `#PyPI`, `#WebAssembly`

---

<a id="item-2"></a>
## [Rio's Homegrown LLM Revealed as Weighted Merge of Existing Models](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

An investigation on GitHub shows that Rio de Janeiro's claimed homegrown LLM, Rio-3.5-Open-397B, is actually a weighted merge of approximately 60% Nex-N2 Pro and 40% Qwen3.5-397B-A17B, with no evidence of additional training or distillation. This controversy raises critical questions about transparency and proper attribution in AI development, especially for public sector projects, and highlights the need for clear disclosure when models are derived from existing work. The analysis found that every weight tensor in Rio-3.5-Open-397B is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen across all 60 layers and components, which cannot be explained by fine-tuning.

hackernews · unrvl22 · Jun 14, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48528371)

**Background**: Model merging is a technique that combines the weights of multiple pre-trained models into a single model, often using linear interpolation or more advanced methods like TIES-Merging. This can improve performance without additional training, but it requires proper attribution of the original models. The municipality of Rio de Janeiro released Rio-3.5-Open-397B as a homegrown fine-tune of Qwen3.5, claiming it outperforms comparable open models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/arcee-ai/mergekit">GitHub - arcee-ai/mergekit: Tools for merging pretrained ...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs - NVIDIA Developer</a></li>

</ul>
</details>

**Discussion**: The community is divided: some argue that the model likely underwent on-policy distillation that wasn't uploaded, while others criticize the lack of attribution and transparency. One commenter noted that a simple linear combination of weights enhanced performance, highlighting the robustness of deep learning models.

**Tags**: `#LLM`, `#open-source`, `#AI ethics`, `#model merging`, `#controversy`

---

<a id="item-3"></a>
## [Jane Street on Formal Methods and the Future of Programming](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street published a blog post discussing the role of formal methods in modern programming, emphasizing their practical use and future potential, especially with the rise of AI-generated code. This discussion is significant because formal methods can mathematically verify code correctness, which is becoming crucial as AI agents generate large amounts of code that need validation. It signals a shift in the industry toward integrating formal verification into everyday software development. Jane Street is establishing a new Formal Methods team and aims to make formal methods as useful as type systems for building software. The blog post is part of a series that explores how formal methods can provide feedback for agentic programming and validate agent-generated code.

hackernews · eatonphil · Jun 14, 12:35 · [Discussion](https://news.ycombinator.com/item?id=48526633)

**Background**: Formal methods are mathematical techniques used to specify, develop, and verify software and hardware systems. They allow developers to prove that a program behaves correctly under all possible inputs, going beyond what testing can achieve. Jane Street, a quantitative trading firm, has historically been skeptical of formal methods but now sees their value in ensuring reliability of complex systems.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.janestreet.com/formal-methods-at-jane-street-index/">Jane Street Blog - Formal methods and the future of programming</a></li>
<li><a href="https://consensys.io/blog/embracing-the-power-of-formal-methods-in-my-coding-journey">Embracing the Power of Formal Methods in my Coding... | Consensys</a></li>
<li><a href="https://zipcpu.com/blog/2017/10/19/formal-intro.html">My first experience with Formal Methods</a></li>

</ul>
</details>

**Discussion**: Commenters shared diverse perspectives: some recalled early proof automation tools like the Boyer-Moore prover, while others discussed using expressive types in Scala 3 for compile-time proofs. A common theme was the potential of formal methods to shift human value from writing code to verifying it, especially with AI-generated code. However, some questioned whether formal specs are just another form of testing that can suffer from the same bugs.

**Tags**: `#formal methods`, `#programming`, `#verification`, `#Jane Street`, `#software engineering`

---

<a id="item-4"></a>
## [2014 Talk Predicted JavaScript's Rise and Fall](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

A 2014 talk by Gary Bernhardt humorously predicted that JavaScript would become a universal compilation target and eventually be replaced by a new technology, a prediction that has proven remarkably accurate with the rise of WebAssembly. The talk's prescience highlights the rapid evolution of web technologies and the ongoing shift toward using JavaScript as an intermediate language, with WebAssembly now fulfilling the role of a low-level compilation target for high-performance applications. The talk specifically mentioned asm.js as an early compilation target, which has since been deprecated in favor of WebAssembly, a binary format that runs natively in browsers and is supported by all major vendors.

hackernews · subset · Jun 14, 12:38 · [Discussion](https://news.ycombinator.com/item?id=48526661)

**Background**: JavaScript was originally designed as a simple scripting language for web browsers, but over time it became the de facto language of the web. Developers began using tools like TypeScript and CoffeeScript that transpile to JavaScript, treating it as a compilation target. WebAssembly, announced in 2015 and first released in 2017, is a low-level binary format designed to be a portable compilation target for languages like C, C++, and Rust, enabling near-native performance on the web.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://www.hanselman.com/blog/javascript-is-web-assembly-language-and-thats-ok">JavaScript is Web Assembly Language and... - Scott Hanselman's Blog</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**Discussion**: Commenters noted the talk's eerie accuracy, with one pointing out that the predicted global disaster between 2020-2025 was the wrong type but still came true. Others discussed the limitations of WebAssembly, such as the lack of direct DOM access, requiring JavaScript as glue code or alternative rendering approaches like canvas.

**Tags**: `#JavaScript`, `#WebAssembly`, `#programming languages`, `#compilation target`

---

<a id="item-5"></a>
## [75 US data center projects worth $130B blocked in Q1 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs) ⭐️ 8.0/10

In the first quarter of 2026, over 75 data center construction projects in the United States, valued at approximately $130 billion, were blocked or delayed, matching the total number of blocks for all of 2025. This surge in opposition signals a major shift in US energy and infrastructure policy, potentially slowing the expansion of AI and cloud computing while raising costs for tech companies. Grassroots opposition groups grew from 396 to 833 across 49 states in three months, and bipartisan lawmakers introduced numerous regulatory bills, including a federal proposal to pause AI data center construction.

telegram · zaihuapd · Jun 14, 03:03

**Background**: Data centers consume massive amounts of electricity and water, with energy costs typically accounting for 30-60% of operational expenses. The rapid growth of AI has driven a surge in data center demand, intensifying local concerns over grid strain, rising electricity prices, and environmental impact.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/人工智能数据中心暂停法案/67555903">人工智能数据中心暂停法案_百度百科</a></li>
<li><a href="https://news.sina.cn/bignews/insight/2026-03-30/detail-inhstpia4074354.d.html?vt=4">桑德斯提案暂停AI数据中心建设，美国国会如何在监管与创新间取得平衡...</a></li>
<li><a href="https://www.winzheng.com/article/sanders-aoc-ban-data-centers">桑德斯与AOC联手提议：暂停新建数据中心，直至AI监管到位</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#energy policy`, `#AI infrastructure`, `#regulation`, `#environment`

---

<a id="item-6"></a>
## [Huawei Open-Sources Pangu 2.0 Models with Up to 505B Parameters](https://t.me/zaihuapd/41948) ⭐️ 8.0/10

At Huawei Developer Conference 2026, Huawei announced the open-source release of the openPangu 2.0 model, including a Pro version with 505 billion parameters and a Flash version with 92 billion parameters, supporting a 512K context window. The company plans to open-source seven major components starting June 30, 2026. This release positions Huawei as a major player in the open-source large language model space, challenging global leaders like Meta's Llama. By open-sourcing models optimized for its Ascend AI chips and HarmonyOS, Huawei aims to build a domestic AI ecosystem and reduce dependence on foreign hardware. The Pro version has 505 billion parameters and the Flash version has 92 billion parameters, both supporting a 512K token context window. The models are optimized for Huawei's Ascend AI computing power and are compatible with HarmonyOS, with open-source components including pre-training code to be released from June 30, 2026.

telegram · zaihuapd · Jun 14, 08:05

**Background**: Large language models (LLMs) are AI models trained on vast text data to generate human-like text. Huawei's Pangu series is its flagship LLM family, and open-sourcing it allows developers worldwide to use, modify, and build upon the models. Huawei's Ascend AI processors and HarmonyOS are key components of its computing ecosystem, competing with NVIDIA GPUs and Android/iOS respectively.

<details><summary>References</summary>
<ul>
<li><a href="https://e.huawei.com/cn/products/computing/ascend">昇腾计算-华为Ascend-AI计算-华为企业业务</a></li>
<li><a href="https://zh.wikipedia.org/wiki/鸿蒙操作系统">鸿蒙操作系统 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Large Language Model`, `#Huawei`, `#Deep Learning`

---

<a id="item-7"></a>
## [US orders Anthropic to restrict two AI models over national security](https://t.me/zaihuapd/41949) ⭐️ 8.0/10

The US Commerce Department issued an export control directive to Anthropic, ordering the company to suspend access to its Fable 5 and Mythos 5 AI models for any foreign national, both inside and outside the US. Anthropic complied by abruptly disabling access to these models for all customers, including its own foreign employees. This marks a significant escalation in government intervention in AI model distribution, setting a precedent for national security-based export controls on advanced AI. It directly impacts global access to cutting-edge AI capabilities and raises concerns about discriminatory treatment of foreign nationals. The directive was prompted by concerns that the models could be jailbroken to produce dangerous capabilities, such as identifying zero-day vulnerabilities in major operating systems and browsers. Anthropic stated that other Claude models are unaffected and that it is working to restore access as soon as possible.

telegram · zaihuapd · Jun 14, 09:06

**Background**: Fable 5 and Mythos 5 are Anthropic's most advanced AI models, with Mythos 5 being a version of Fable 5 with enhanced safeguards for cybersecurity and biology. The US government's use of export controls on AI models is a relatively new but growing trend, as concerns about national security risks from dual-use AI technologies intensify.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order">Anthropic to disable its most advanced AI models after US order...</a></li>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following... | Fortune</a></li>
<li><a href="https://www.euronews.com/my-europe/2026/06/14/us-export-controls-on-anthropic-should-not-be-discriminatory-eu-commission-warns">US export controls on Anthropic 'should not be... | Euronews</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#export controls`, `#Anthropic`, `#national security`, `#Claude`

---

<a id="item-8"></a>
## [First Global Map of Underground Fungal Networks Revealed](https://insideclimatenews.org/news/11062026/earths-massive-underground-fungal-networks/) ⭐️ 8.0/10

A new study led by the Society for the Protection of Underground Networks (SPUN) has produced the first global map of arbuscular mycorrhizal fungi networks, estimating total hyphal length at 110 quadrillion kilometers and annual carbon storage of 1 billion tons. This mapping reveals that farmland fungal density is only half that of wild ecosystems, and grasslands—which hold 40% of global fungal biomass—are being converted to farmland four times faster than forests, highlighting a critical threat to natural carbon sequestration. The total hyphal length is nearly a billion times the distance between Earth and the Sun, and the total fungal mass is about five times the weight of all humans combined. The networks associate with approximately 80% of global plant species.

telegram · zaihuapd · Jun 14, 14:58

**Background**: Arbuscular mycorrhizal fungi (AMF) form symbiotic relationships with plant roots, helping plants absorb nutrients while receiving carbon in return. These underground networks play a crucial role in soil health and carbon storage. SPUN is an organization founded specifically to map and protect these fungal networks.

<details><summary>References</summary>
<ul>
<li><a href="https://madechango.com/study-guide/view/2108">Threads of underground fungal networks are long enough to reach...</a></li>

</ul>
</details>

**Tags**: `#fungal networks`, `#carbon sequestration`, `#ecology`, `#climate change`, `#mycorrhizal fungi`

---