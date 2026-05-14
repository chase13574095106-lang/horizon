---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 29 items, 10 important content pieces were selected

---

1. [首个公开的苹果 M5 内核漏洞利用](#item-1) ⭐️ 9.0/10
2. [Bun 从 Zig 重写为 Rust 已合并](#item-2) ⭐️ 9.0/10
3. [NGINX 存在 18 年远程代码执行漏洞 (CVE-2026-42945)，影响数十亿服务器](#item-3) ⭐️ 9.0/10
4. [DeepSeek 会话隔离漏洞：输入 <think 可泄露他人对话](#item-4) ⭐️ 9.0/10
5. [移除 2024 款 RAV4 混动版调制解调器和 GPS](#item-5) ⭐️ 8.0/10
6. [RTX 5090 外接显卡搭配 M4 MacBook Air：游戏与 LLM 推理突破](#item-6) ⭐️ 8.0/10
7. [AI 辅助编程可能阻碍开发者学习](#item-7) ⭐️ 8.0/10
8. [Anthropic 与 SpaceX 合作获取 Colossus 算力](#item-8) ⭐️ 8.0/10
9. [美国批准向 10 家中国企业出售 H200 芯片](#item-9) ⭐️ 8.0/10
10. [京东上线 AI 硬件自营专区，上架受制裁 NVIDIA GPU](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [首个公开的苹果 M5 内核漏洞利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif 团队发布了首个针对苹果 M5 芯片的公开内核内存破坏漏洞利用，可能绕过了内存标记扩展（MTE）硬件安全特性。 这标志着一个重要的安全里程碑，因为它展示了 MTE（一种关键的内存安全硬件缓解措施）的实际绕过，并凸显了 LLM 辅助漏洞利用开发的日益增长的作用。 该漏洞由 Bruce Dang 于 4 月 25 日偶然发现，Dion Blazakis 于 4 月 27 日加入 Calif，在一周内完成了漏洞利用。团队计划发布一份 55 页的技术报告，包含完整细节。

hackernews · quadrige · May 14, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48139219)

**背景**: 苹果 M5 是苹果最新的基于 ARM 的 SoC，采用 3nm 工艺，配备下一代 GPU 和神经加速器。内存标记扩展（MTE）是 Armv9 的硬件特性，旨在检测释放后使用和缓冲区溢出等内存安全错误，已在 Android 中广泛采用，现在也出现在苹果芯片中。内核内存破坏漏洞是最严重的漏洞之一，攻击者可借此完全控制系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://developer.android.com/ndk/guides/arm-mte">Arm Memory Tagging Extension (MTE) | Android NDK | Android Developers</a></li>

</ul>
</details>

**社区讨论**: 评论者既兴奋又怀疑：一些人称赞这一成就，并指出 LLM 辅助漏洞利用的潜力，而另一些人则质疑缺乏技术细节以及漏洞如何绕过 MTE。还有讽刺性的猜测认为苹果在编造虚假漏洞来炒作 Mythos。

**标签**: `#macOS`, `#kernel exploit`, `#Apple M5`, `#security`, `#MTE`

---

<a id="item-2"></a>
## [Bun 从 Zig 重写为 Rust 已合并](https://github.com/oven-sh/bun/pull/30412) ⭐️ 9.0/10

将 Bun 从 Zig 重写为 Rust 的拉取请求已合并，产生了超过 100 万行 Rust 代码，取代了之前的 Zig 代码库。 这次重写显著提高了内存安全性，减少了在 Zig 中常见的释放后使用和双重释放等错误，使 Bun 对开发者更加可靠。 新代码库包含超过 100 万行 Rust 代码，在 736 个文件中有 10,428 个 unsafe 块，并且重写准备了从 Zig 惯用法到 Rust 的详细映射。

hackernews · Chaoses · May 14, 08:15 · [社区讨论](https://news.ycombinator.com/item?id=48132488)

**背景**: Bun 是一个 JavaScript 运行时、打包器和包管理器，旨在作为 Node.js 的直接替代品。它最初使用 Zig，一种注重安全性和性能的低级语言，但 Rust 通过其所有权系统提供了更强的内存安全保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区讨论了代码库的复杂性，有人指出 Bun 的 Rust 代码量接近 Rust 编译器本身。其他人则强调了使重写在短时间内成为可能的广泛准备和映射工作。

**标签**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript Runtime`, `#Software Engineering`

---

<a id="item-3"></a>
## [NGINX 存在 18 年远程代码执行漏洞 (CVE-2026-42945)，影响数十亿服务器](https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability) ⭐️ 9.0/10

NGINX 的 ngx_http_rewrite_module 中被披露了一个严重的堆缓冲区溢出漏洞（CVE-2026-42945，CVSS 9.2），该漏洞自 2008 年存在，允许未经身份验证的远程代码执行。已发布修复版本：NGINX Open Source 1.31.0/1.30.1 和 NGINX Plus R36 P4/R32 P6。 由于 NGINX 的广泛使用，该漏洞影响全球数十亿台生产服务器，包括 Kubernetes 集群的 Ingress 层和 API 网关。这个存在 18 年的漏洞凸显了立即打补丁的紧迫性，并暴露了长期代码库中的风险。 该漏洞源于脚本引擎两遍执行流程中的不一致：第一遍计算缓冲区大小时未考虑 URI 字符转义扩展（每个字符从 1 字节膨胀至 3 字节），导致第二遍拷贝时发生堆溢出。利用条件包括 rewrite 指令的替换字符串中含有问号，且后续有 set 指令引用未命名捕获组（如 $1）。

telegram · zaihuapd · May 14, 02:41

**背景**: NGINX 是一个广泛使用的开源 Web 服务器、反向代理和负载均衡器。ngx_http_rewrite_module 使用两遍脚本引擎处理 URL 重写：第一遍计算缓冲区大小，第二遍拷贝结果。当计算的大小过小时会发生堆缓冲区溢出，攻击者可覆盖相邻内存并可能执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rankiteo.com/f51778747583-f5-vulnerability-may-2026/">F5: Critical 18-Year-Old NGINX Vulnerability Enables Remote Code Execution Attacks</a></li>
<li><a href="https://gist.github.com/alon710/774ec5a75ca3c79658262b161d1067ad">CVE-2026-42945: CVE-2026-42945: Heap-based Buffer Overflow in NGINX ngx_http_rewrite_module - CVE Security Report · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，已发布的 PoC 假设 ASLR 被禁用，但研究人员声称存在可靠的 ASLR 绕过方法。一些人强调 ASLR 是纵深防御措施，并非完全缓解。其他人讨论了利用前提条件（rewrite 含 ? 和 set 含 $1），并建议使用命名捕获组作为临时缓解措施。

**标签**: `#NGINX`, `#CVE-2026-42945`, `#remote code execution`, `#security vulnerability`, `#heap buffer overflow`

---

<a id="item-4"></a>
## [DeepSeek 会话隔离漏洞：输入 <think 可泄露他人对话](https://github.com/deepseek-ai/DeepSeek-R1/issues/840) ⭐️ 9.0/10

DeepSeek 的 Web 和 API 对话系统中发现了一个严重的会话隔离漏洞：攻击者在全新的空对话中仅发送未闭合的 <think 字符串，即可获取其他用户的对话历史，包括代码、密钥和隐私等敏感信息。该漏洞由用户 cancat2024 于 2026 年 5 月 11 日负责任地披露，随后被公开传播。 该漏洞对所有 DeepSeek 用户构成严重的隐私风险，因为它允许未经授权访问私人对话，可能泄露专有代码、凭证和个人数据。此事件凸显了 AI 对话系统中的关键安全缺陷，并可能削弱用户对 DeepSeek 及类似平台的信任。 该漏洞通过在全新的聊天会话中发送未闭合的 <think 标记来触发，导致模型产生幻觉并返回其他用户的对话片段。该漏洞影响 DeepSeek 的 Web 界面和 API，并且在第三方部署中也被确认存在。

telegram · zaihuapd · May 14, 13:15

**背景**: DeepSeek 是一款以强大推理能力著称的热门中国 AI 模型，常用于聊天应用。会话隔离是多租户 AI 服务的基本安全要求，确保一个用户的数据对其他用户不可见。<think 标记是 DeepSeek 用于指示内部推理步骤的特殊标记，其不当处理可能导致上下文泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/AI_News_CN/36511">Telegram: View @AI_News_CN</a></li>
<li><a href="https://www.80aj.com/2026/05/15/deepseek-privacy-bug-space/">DeepSeek 疑现严重隐私漏洞：输入空格即可查看他人实时对话</a></li>

</ul>
</details>

**社区讨论**: GitHub 和 Telegram 上的社区讨论确认了该漏洞的严重性，用户指出第三方部署也受影响，表明问题源于模型幻觉而非简单的后端错误。一些评论者对漏洞的快速公开传播表示担忧，并敦促用户在修复部署前避免在 DeepSeek 上分享敏感信息。

**标签**: `#security`, `#vulnerability`, `#AI`, `#DeepSeek`, `#data leak`

---

<a id="item-5"></a>
## [移除 2024 款 RAV4 混动版调制解调器和 GPS](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

一份详细指南展示了如何物理移除 2024 款 RAV4 混动版的调制解调器和 GPS 以阻止遥测，但警告称通过蓝牙连接的手机仍会通过车辆的网络共享泄露数据。 这很重要，因为现代车辆收集大量遥测数据，该指南为注重隐私的车主提供了实用的动手解决方案，同时指出蓝牙连接可能绕过移除操作。 移除过程涉及断开数据通信模块（DCM）和 GPS 天线；然而，通过 USB 连接的 CarPlay 不会共享网络，但 CarPlay 和 Android Auto 仍会捕获各自的遥测数据。

hackernews · arkadiyt · May 14, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=48138136)

**背景**: 现代汽车如丰田 RAV4 内置蜂窝调制解调器和 GPS，用于远程服务和紧急呼叫等功能，但它们也会持续向制造商发送遥测数据。移除调制解调器可以阻止这一点，但某些功能可能会丢失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Toyota_RAV4">Toyota RAV 4 - Wikipedia</a></li>
<li><a href="https://www.youtube.com/watch?v=g7xS3uPCBJA">Disable DCM in toyota cars - YouTube</a></li>
<li><a href="https://forum.ih8mud.com/threads/permanently-disable-telemetry-data-transmission-from-16-200s.1347480/">Permanently Disable Telemetry Data Transmission from 16+ 200s</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了其他品牌（斯巴鲁、福特）的类似经验，并指出拔掉保险丝即可禁用远程信息处理且不报错。有人对蓝牙允许网络共享表示惊讶，而另一些人则指出 CarPlay/Android Auto 仍会收集数据。

**标签**: `#privacy`, `#automotive`, `#telemetry`, `#hardware hacking`, `#security`

---

<a id="item-6"></a>
## [RTX 5090 外接显卡搭配 M4 MacBook Air：游戏与 LLM 推理突破](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

一位开发者通过 Thunderbolt 的 PCIe 隧道技术，成功将 NVIDIA RTX 5090 外接显卡连接到 M4 MacBook Air，实现了此前在 Apple Silicon 上无法完成的游戏和 LLM 推理任务。 这一成就表明外接显卡可以在 Apple Silicon 上工作，有望为 Mac 解锁高性能游戏和 AI 工作负载，并凸显了 Apple 生态中对 GPU 加速日益增长的需求。 该方案通过 Thunderbolt 的 PCIe 隧道技术实现，但 Apple 的 1.5 GB DMA 窗口限制制约了性能。外接显卡显著提升了 LLM 的提示处理速度，而这是 Mac 上已知的瓶颈。

hackernews · allenleee · May 14, 15:47 · [社区讨论](https://news.ycombinator.com/item?id=48137145)

**背景**: 外接显卡（eGPU）允许笔记本电脑通过 Thunderbolt 使用桌面级显卡。Apple Silicon Mac 缺乏原生 eGPU 支持，但 PCIe 隧道技术可以绕过这一限制。Mac 上的 LLM 推理因统一内存架构而面临提示处理速度慢的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://egpu.io/forums/thunderbolt-enclosures/aoostar-ag02-egpu-not-detected-on-rog-ally-x-usb4-link-ok-no-pcie-tunnel/">AOOSTAR AG02 eGPU not detected on ROG Ally X (USB4 link OK, ...</a></li>
<li><a href="https://blog.starmorph.com/blog/apple-silicon-llm-inference-optimization-guide">Apple Silicon LLM Inference Optimization: The Complete Guide to...</a></li>
<li><a href="https://toolhalla.ai/blog/best-local-llms-mac-studio-2026">Best Local LLMs for Mac Studio in 2026 | ToolHalla</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这一技术成就，部分人指出 LLM 性能提升比游戏更有实际意义。也有人对 Apple 缺乏官方 eGPU 支持以及 1.5 GB DMA 窗口限制表示失望。

**标签**: `#eGPU`, `#Apple Silicon`, `#Gaming`, `#LLM Inference`, `#PCIe Tunneling`

---

<a id="item-7"></a>
## [AI 辅助编程可能阻碍开发者学习](https://jpain.io/god-damn-ai-is-making-me-dumb/) ⭐️ 8.0/10

一篇题为“AI 让我变笨”的开发者博客反思了依赖 AI 编程助手可能减少深度学习与技能获取，引发了超过 200 条评论的社区讨论。 这场讨论凸显了软件工程中的一个关键权衡：AI 提高了生产力，但可能损害开发者的长期成长，尤其是初级开发者。这呼应了更广泛的关于 AI 对学习和专业能力影响的担忧。 术语“vibe coding”由 Andrej Karpathy 于 2025 年 2 月提出，指不加审查地接受 AI 生成的代码。批评者警告安全风险和可维护性降低，而支持者认为它降低了业余程序员的门槛。

hackernews · Eighth · May 14, 18:19 · [社区讨论](https://news.ycombinator.com/item?id=48139148)

**背景**: Vibe coding 是一种开发者向大语言模型描述任务并接受生成代码而不深入审查的实践。它在 2025 年流行起来，被柯林斯词典评为年度词汇。争论焦点在于这种方法是有助于还是有害于技能发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：有经验的开发者感到需要持续审查 AI 输出，而其他人（尤其是初级开发者）担心入职速度变慢。少数人报告在光谱学等专业领域学习更快，表明情境很重要。

**标签**: `#AI`, `#software engineering`, `#developer experience`, `#learning`, `#vibe coding`

---

<a id="item-8"></a>
## [Anthropic 与 SpaceX 合作获取 Colossus 算力](https://t.me/zaihuapd/41371) ⭐️ 8.0/10

Anthropic 已与 SpaceX 签署协议，使用 Colossus 1 数据中心的全部算力，在一个月内获得超过 300 兆瓦的新增容量和超过 22 万块 NVIDIA GPU。因此，Claude Code 所有付费方案的 5 小时速率限制翻倍，Claude Opus 的 API 速率限制也显著提高。 此次合作为 Anthropic 提供了巨大的算力资源，能够加速模型训练和推理，并通过提高使用限制直接改善用户体验。这也表明大规模 AI 基础设施和跨行业合作的重要性日益增长。 Colossus 1 是由 xAI 开发的超级计算机，在田纳西州孟菲斯市用 122 天建成，被认为是世界上最大的 AI 超级计算机。该协议包括超过 300 兆瓦电力和 22 万块以上 NVIDIA GPU，并立即对 Claude Code 和 API 速率限制产生影响。

telegram · zaihuapd · May 14, 00:57

**背景**: Anthropic 是 Claude AI 助手的开发公司，提供包括 Pro、Max 和 API 在内的多种方案。Claude Code 是一款编码工具，其使用限制基于滚动 5 小时窗口。Colossus 1 最初为 xAI 的 Grok 聊天机器人建造，代表了 AI 算力能力的巨大飞跃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/anthropic-signs-spacex-colossus-1-data-center-to-boost-capacity/">Anthropic Signs SpaceX Colossus 1 Data Center to... - ServeTheHome</a></li>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://www.sessionwatcher.com/guides/claude-code-rate-limits-explained">Claude Code Rate Limits Explained – 5-Hour... | SessionWatcher</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SpaceX`, `#AI infrastructure`, `#Claude`, `#NVIDIA GPU`

---

<a id="item-9"></a>
## [美国批准向 10 家中国企业出售 H200 芯片](https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14/) ⭐️ 8.0/10

美国商务部已批准向约 10 家中国企业出售英伟达 H200 AI 芯片，买家包括阿里巴巴、腾讯、字节跳动和京东等，单一客户最多可购买 7.5 万颗。但截至目前尚未有任何交付完成，部分中国企业在北京方面的指导下转趋谨慎。 这一批准标志着美国对华先进 AI 芯片出口管制可能发生转变，将影响全球 AI 硬件市场和中国国产 AI 芯片产业的发展。英伟达 CEO 黄仁勋访华凸显了该公司在科技紧张局势持续之际寻求在华突破的努力。 H200 GPU 配备 141 GB HBM3e 内存，八路 HGX 配置可提供超过 32 petaflops 的 FP8 深度学习算力，性能较 H100 显著提升。许可涵盖联想和富士康等分销商，但尚未有实际出货。

telegram · zaihuapd · May 14, 08:57

**背景**: 美国对华实施先进 AI 芯片出口管制，以限制中国获取用于军事和 AI 应用的尖端技术。英伟达 H200 是专为 AI 训练和推理设计的高端 GPU，是 H100 的继任者。中国政府鼓励国产芯片发展，同时平衡进口高性能芯片的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/h200/">H200 GPU | NVIDIA</a></li>
<li><a href="https://lenovopress.lenovo.com/lp1944-nvidia-h200-141gb-gpu">ThinkSystem NVIDIA H200 141GB GPUs Product Guide > Lenovo Press</a></li>
<li><a href="https://www.runpod.io/articles/guides/nvidia-h200-gpu">Nvidia H200 GPU: Specs, VRAM, Price, and AI Performance</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#US-China trade`, `#Nvidia`, `#export controls`, `#geopolitics`

---

<a id="item-10"></a>
## [京东上线 AI 硬件自营专区，上架受制裁 NVIDIA GPU](https://u.jd.com/HaDkFMa) ⭐️ 8.0/10

京东开设了“AI 硬件京东自营专区”，上架了此前受制裁的 NVIDIA GPU，包括 H100、RTX 5090 涡轮版和 RTX PRO 6000 Blackwell 服务器版，可供购买。 此举可能意味着对华高端 AI 硬件出口限制的放松，通过提供尖端 GPU 的获取渠道，将对 AI 和机器学习行业产生重大影响。 RTX 5090 涡轮版列为全球统一无阉割规格；RTX PRO 6000 面向专业渲染和数据中心；H100 此前因制裁暂停对华出口。

telegram · zaihuapd · May 14, 15:15

**背景**: 美国以国家安全为由，对 NVIDIA H100 等先进 AI 芯片实施了对华出口限制。京东是中国主要电商平台，其自营店通常确保产品正品和可购买性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.cn/geforce/graphics-cards/50-series/rtx-5090-d-v2/">GeForce RTX 5090 D v2 显卡 | NVIDIA</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/">RTX PRO 6000 Blackwell Server Edition | NVIDIA</a></li>
<li><a href="https://www.usmart.hk/en/news-detail/7307756841394651962">英偉達GTC：聯想等 Blackwell RTX PRO ... | uSMART</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#NVIDIA`, `#export restrictions`, `#JD.com`, `#GPU`

---