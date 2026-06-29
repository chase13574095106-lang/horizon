---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> From 30 items, 8 important content pieces were selected

---

1. [最高法院裁定地理围栏搜查令需受第四修正案保护](#item-1) ⭐️ 9.0/10
2. [vLLM v0.24.0 新增 MiniMax-M3 支持，深度优化 DeepSeek-V4](#item-2) ⭐️ 8.0/10
3. [火箭实验室以 80 亿美元收购铱星](#item-3) ⭐️ 8.0/10
4. [WATaBoy：将 Game Boy 指令 JIT 编译为 WASM，性能超越原生解释器](#item-4) ⭐️ 8.0/10
5. [深度解析：CUDA 内核启动的完整路径](#item-5) ⭐️ 8.0/10
6. [Ornith-1.0：开源自脚手架大模型用于智能体编程](#item-6) ⭐️ 8.0/10
7. [三星与 SK 海力士宣布大规模 AI 投资计划](#item-7) ⭐️ 8.0/10
8. [长鑫存储与腾讯签署近 30 亿美元 DRAM 供应协议](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [最高法院裁定地理围栏搜查令需受第四修正案保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，要求科技公司识别特定区域内所有移动设备的地理围栏搜查令，必须遵守第四修正案关于禁止不合理搜查和扣押的保护。 这一里程碑式的裁决极大地限制了无证获取位置数据的行为，加强了数百万智能手机用户的数字隐私权，并为未来的监控技术树立了先例。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米内 19 个账户的位置数据；法院要求搜查令必须具体且范围有限，驳回了宽泛的地理围栏请求。

hackernews · cdrnsf · Jun 29, 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令，也称为反向位置搜查令，允许执法机构在特定时间内搜索数据库，以查找特定区域内的所有活跃移动设备。第四修正案保护公民免受不合理搜查，但法院一直难以将其应用于数字位置数据。最高法院 2018 年 Carpenter 诉美国案的判决确立了获取历史基站位置数据需要搜查令，而本次裁决将类似保护扩展到了地理围栏搜查令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant - Wikipedia</a></li>
<li><a href="https://www.congress.gov/crs-product/LSB11274">Geofence Warrants and the Fourth Amendment | Congress.gov | Library of Congress</a></li>
<li><a href="https://www.nacdl.org/Content/Geofence-Warrants">NACDL - Geofence Warrants</a></li>

</ul>
</details>

**社区讨论**: 评论者引用了 Paula Broadwell 案等历史案例，表明即使没有手机，位置追踪也能识别嫌疑人。一些人担心搜查令常常被轻易批准，而另一些人则指出该裁决对总统权力和单一行政理论有更广泛的影响。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#fourth amendment`, `#digital rights`

---

<a id="item-2"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持，深度优化 DeepSeek-V4](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充分块规划改进。该版本还扩展了 Model Runner V2，默认支持量化模型，并新增了用于工具调用和推理解析的流式解析引擎。 此版本通过支持 MiniMax-M3 和 DeepSeek-V4 等前沿模型，显著扩展了 vLLM 的模型生态系统，使高性能推理更加易用。优化提升了吞吐量和延迟，有利于在生产环境中部署大语言模型的开发者。 该版本包含来自 256 位贡献者的 571 次提交，其中 77 位是新贡献者。关键技术新增包括 MiniMax-M3 的 MXFP4 支持、DeepSeek-V4 的集群协作 topK 内核，以及集成 DeepEP v2 用于专家并行。

github · khluu · Jun 29, 19:41

**背景**: vLLM 是一个高吞吐量、内存高效的大语言模型推理引擎，最初由加州大学伯克利分校开发。它使用 PagedAttention 技术高效管理 KV-cache 内存。MiniMax-M3 是一个具有 100 万上下文窗口的多模态 MoE 模型，而 DeepSeek-V4 是一个 1 万亿参数的 MoE 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M3">MiniMaxAI/ MiniMax - M 3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#MiniMax`, `#open source`

---

<a id="item-3"></a>
## [火箭实验室以 80 亿美元收购铱星](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

火箭实验室于 2025 年 6 月 29 日宣布，将以现金加股票方式收购铱星通信公司，交易价值约 80 亿美元，每股作价 54 美元。该交易已获双方董事会一致批准，预计于 2027 年年中完成，尚需股东和监管批准。 此次收购打造了一家完全整合的航天公司，将火箭实验室的发射和航天器制造能力与铱星盈利的低轨卫星星座、L 波段频谱及 500 多家合作伙伴生态相结合。它使火箭实验室能够在卫星物联网、直连设备和 PNT 应用等领域更广泛地竞争，同时为其不断增长的发射业务确保基础发射量。 铱星运营着 66 颗活跃的低轨卫星，轨道高度约 781 公里，采用近极地轨道，提供全球语音和数据覆盖。该公司 2025 年营收为 8.717 亿美元，EBITDA 为 4.95 亿美元（利润率 57%），拥有超过 255 万活跃订阅者。火箭实验室已获得 36 亿美元过桥贷款承诺以支持该交易。

hackernews · everfrustrated · Jun 29, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: 火箭实验室是一家公开上市的航空航天制造商和发射服务提供商，以其 Electron 火箭闻名，截至 2026 年初已完成超过 75 次任务。铱星通信公司拥有并运营铱星星座，这是一个最初由摩托罗拉开发、自 1998 年起投入运营的全球低轨卫星网络。该星座利用星间链路提供覆盖极地和海洋的服务，无需地面站。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab">Rocket Lab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Iridium_Communications">Iridium Communications - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：一些人认为这是一项明智的战略举措，可确保发射需求并扩展卫星服务，类似于 SpaceX 利用 Starlink 的做法。另一些人则对太空垃圾和低轨道的商业化表示担忧。少数评论者注意到火箭实验室从新西兰的骄傲转变为一家美国公司。

**标签**: `#space`, `#acquisition`, `#satellite`, `#Rocket Lab`, `#Iridium`

---

<a id="item-4"></a>
## [WATaBoy：将 Game Boy 指令 JIT 编译为 WASM，性能超越原生解释器](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

WATaBoy 是一款 Game Boy 模拟器，它通过即时编译将 SM83 指令转换为 WebAssembly（WASM），利用浏览器的 JIT 引擎实现了超越原生解释器的性能。 这种方法巧妙地绕过了 iOS 的 JIT 限制，通过在浏览器内运行，在禁止原生 JIT 的设备上实现了高性能模拟。它还证明了 WASM 可以作为模拟 JIT 的有效中间表示。 该模拟器在运行时将 Game Boy 的 SM83 操作码编译为 WASM 模块，然后由浏览器的 WASM 引擎进一步 JIT 编译为原生代码。基准测试显示其性能优于原生解释器，但 Firefox 比 Chrome/Safari 慢约 25%。

hackernews · energeticbark · Jun 29, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48720190)

**背景**: JIT 编译是一种在运行时编译代码以提高性能的技术，但苹果在 iOS 上限制 JIT，除了浏览器的 JavaScript 和 WebAssembly 引擎。WebAssembly 是一种低级二进制格式，旨在在浏览器中实现接近原生的性能，现代浏览器会进一步将 WASM JIT 编译为机器码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EnergeticBark/WATaBoy">GitHub - EnergeticBark/ WATaBoy : A Game Boy emulator with an...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目是令人印象深刻的本科作品，并指出其巧妙绕过了 iOS 的 JIT 限制。有人质疑为什么 Firefox 较慢，一位评论者指出 WASM 开销（约 20%）远小于解释器开销（约 1000%），因此结果虽在意料之中但仍很酷。

**标签**: `#JIT compilation`, `#WebAssembly`, `#emulation`, `#Game Boy`, `#iOS`

---

<a id="item-5"></a>
## [深度解析：CUDA 内核启动的完整路径](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10

一篇详细的技术博客文章解释了启动 CUDA 内核时从 CPU 到 GPU 的完整路径，涵盖了驱动交互、通过门铃寄存器的命令提交以及队列管理描述符（QMD）的作用。 这篇深度文章弥合了高级 CUDA 语法与底层硬件机制之间的差距，帮助开发者理解性能影响并调试内核启动开销。它还突显了库和框架所抽象化的复杂性。 文章解释了 CPU 将 QMD 写入环形缓冲区并触发门铃寄存器以通知 GPU，GPU 随后获取并执行内核。社区评论指出控制码涉及表查找，而不仅仅是控制字中的位。

hackernews · mezark · Jun 29, 13:11 · [社区讨论](https://news.ycombinator.com/item?id=48718863)

**背景**: CUDA 内核是在 NVIDIA GPU 上运行的函数。启动内核涉及 CPU 通过 CUDA 驱动程序和硬件机制（如门铃寄存器和命令队列）向 GPU 发送命令。大多数教程关注内核代码本身，但从 CPU 到 GPU 的启动路径对于理解性能和系统行为同样重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html">2.3. Writing SIMT Kernels — CUDA Programming Guide</a></li>
<li><a href="https://dev.to/dianejwilliams/part-4-command-stream-and-rendering-pipeline-command-submission-26am">Part 4: Command Stream and Rendering Pipeline... - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该文章阐明了门铃和 QMD 机制，将 CUDA 语法与实际 GPU 提交联系起来。有人指出控制码更复杂（表查找），其他人则欣赏对默认流信号量的解释，将 CUDA 的隐式同步与 Vulkan 的显式方法进行了对比。

**标签**: `#CUDA`, `#GPU`, `#systems programming`, `#NVIDIA`, `#kernel launch`

---

<a id="item-6"></a>
## [Ornith-1.0：开源自脚手架大模型用于智能体编程](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一系列 MIT 许可的开源大模型，专为智能体编程设计，参数规模从 9B 到 397B，基于 Gemma 4 和 Qwen 3.5（均为 Apache 2.0 许可）。在编程基准测试中，它达到了同类开源模型中的最佳性能。 Ornith-1.0 引入了自脚手架训练框架，模型学习同时生成代码解决方案和任务特定的脚手架，从而实现更自主、更高效的编程智能体。这可能会显著推动开源 AI 辅助软件开发。 模型系列包括 9B Dense、31B Dense、35B MoE 和 397B MoE 变体。早期用户报告显示，它在智能体编程任务上表现强劲，例如导航代码库和执行多步工具调用，在消费级硬件上推理速度可达 103 tokens/秒。

rss · Simon Willison · Jun 29, 16:17

**背景**: 智能体编程是指 AI 智能体在最少人工干预下自主规划、编写、测试和修改代码。传统基于大模型的编程助手依赖固定、人工设计的脚手架来引导智能体工作流。Ornith-1.0 的自脚手架方法将脚手架视为可学习组件，在强化学习过程中与模型策略联合优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://essamamdani.com/blog/ornith-1-0-self-scaffolding-llm-coding-2026">Ornith-1.0: The Self-Scaffolding LLM That Teaches Itself to Code Better | Essa Mamdani | Essa Mamdani</a></li>
<li><a href="https://github.com/deepreinforce-ai/Ornith-1">GitHub - deepreinforce -ai/ Ornith - 1 · GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#coding`, `#AI agents`, `#model release`

---

<a id="item-7"></a>
## [三星与 SK 海力士宣布大规模 AI 投资计划](https://t.me/zaihuapd/42235) ⭐️ 8.0/10

三星和 SK 海力士将于 6 月 29 日的国家简报会上宣布大规模 AI 投资计划，其中三星拟公布 1000 万亿韩元（约 6480 亿美元）的十年支出方案，为韩国史上最大规模。 这标志着主要半导体公司向 AI 基础设施的战略转移，可能重塑全球 AI 硬件格局，并加剧与其他芯片制造商的竞争。 SK 海力士计划五年内将产能翻倍，并通过在美国上市筹资 290 亿美元。简报会还将聚焦半导体、AI 数据中心和物理 AI。

telegram · zaihuapd · Jun 29, 07:00

**背景**: 物理 AI 是一种使自主机器（如机器人、自动驾驶汽车等）在真实物理世界中感知、理解并执行复杂操作的技术。AI 数据中心是训练和部署大型 AI 模型的关键基础设施，能耗巨大。三星和 SK 海力士是领先的存储芯片制造商，其 HBM（高带宽内存）对 AI 加速器至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/Odaily_News/158245">Odaily资讯速递 – Telegram</a></li>
<li><a href="https://m.pedaily.cn/news/564774">就因为会「搬砖」了， 物 理 AI 一夜爆火|投资界</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#AI investment`, `#Samsung`, `#SK Hynix`, `#hardware`

---

<a id="item-8"></a>
## [长鑫存储与腾讯签署近 30 亿美元 DRAM 供应协议](https://www.reuters.com/world/china/chinas-cxmt-wins-3-billion-memory-supply-deal-with-tencent-sources-say-2026-06-29/) ⭐️ 8.0/10

长鑫存储（CXMT）与腾讯签署了一项价值超过 200 亿元人民币（约 29.4 亿美元）的长期 DRAM 供应协议，涵盖数年服务器内存芯片供货。 该协议标志着中国内存供应链的重大转变，减少对外国 DRAM 供应商的依赖，并强化国内半导体生态系统。同时，这也凸显了腾讯在全球内存短缺背景下确保关键组件的战略举措。 据消息人士称，协议期限为三到五年。长鑫存储据称还在与其他中国主要互联网公司（包括阿里云、字节跳动和小米）就类似合作进行谈判。

telegram · zaihuapd · Jun 29, 09:31

**背景**: 长鑫存储是一家中国 DRAM 制造商，成立于 2016 年，总部位于安徽合肥。DRAM 芯片是用于云计算、数据库和人工智能工作负载的服务器中的关键组件。全球内存短缺使得长期供应合同成为许多公司的优先事项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://m.ithome.com/html/970041.htm">消息称腾讯与长鑫 存 储签署 200 多亿元 内 存 芯 片 供应协议 - IT之家</a></li>
<li><a href="https://f5.pm/go-425897.html">腾讯与长鑫 存 储签署 内 存 芯 片 供应协议</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#semiconductors`, `#China`, `#Tencent`, `#supply chain`

---