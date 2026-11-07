---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07
lang: zh
---

> From 30 items, 5 important content pieces were selected

---

1. [PwnEscape 第二部分：Firecracker 虚拟机逃逸实战详解](#item-1) ⭐️ 8.0/10
2. [AI 正在大幅加速 AI 研究，但这是真正的进步吗？](#item-2) ⭐️ 8.0/10
3. [甲骨文迫于美国压力取消与腾讯 70 亿美元 AI 芯片租赁协议](#item-3) ⭐️ 8.0/10
4. [百度发布文心 5.0：2.4 万亿参数全模态 MoE 模型](#item-4) ⭐️ 8.0/10
5. [长江存储新建武汉工厂国产设备占比拟达 70%](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PwnEscape 第二部分：Firecracker 虚拟机逃逸实战详解](https://pwn.ai/blog/firecracker-escape) ⭐️ 8.0/10

PWN.AI 发布了一篇详细的实战指南（第二部分），展示恶意客户机如何利用 PwnEscape Linux 内核网络漏洞突破 Firecracker 的 microVM 边界，从虚拟机内部定位正在运行的 VMM，并控制以 root 运行的主机进程。该文章演示了从客户机到主机的代码执行原语，但指出测试配置未使用 Firecracker 的 jailer。 Firecracker 是 AWS Lambda 以及许多多租户无服务器和容器平台的基础，因此一个已演示的客户机到主机逃逸对生产环境中的隔离假设提出了严重质疑。该文章和讨论强调，实际暴露风险在很大程度上取决于部署是否使用 jailer、命名空间和 seccomp，并重新引发了关于微虚拟机监控器替代方案的辩论。 该利用链将 Linux 网络漏洞（编号 CVE-2026-99999，代号 PwnEscape）转化为客户机到主机的攻击原语，但测试环境缺少 Firecracker 的生产级防护：权限降级、命名空间和 seccomp 过滤器。作者警告，对于正确配置 jailer 的部署，需要单独评估 VMM 被攻陷后仍可用的权限和资源。

hackernews · SerCe · Nov 6, 19:33 · [社区讨论](https://news.ycombinator.com/item?id=50397219)

**背景**: Firecracker 是一个用 Rust 编写的轻量级 microVM 虚拟机监控器，专为短生命周期工作负载提供快速、安全的隔离，是 AWS Lambda 的底层支撑。其生产环境加固依赖 jailer——一个配套二进制程序，通过命名空间和 seccomp 降低权限并限制 Firecracker 进程。PwnEscape 是一个严重的 Linux 内核网络漏洞，允许客户机虚拟机内的代码读取主机内存，在未打补丁时实际上消除了客户机与主机之间的边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pwn.ai/blog/firecracker-escape">Firecracker VM Escape: PwnEscape Part 2. | PWN.AI Security ...</a></li>
<li><a href="https://cybernews.com/security/critical-linux-bug-pwnescape-allows-vm-escape/">PwnEscape Linux Vulnerability Lets VM Guests Escape to Hosts ...</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md">firecracker/docs/jailer.md at main · firecracker-microvm ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对文章的框架提出质疑：有人指出测试配置未使用 jailer，并要求对正确配置 jailer 的部署进行更多分析；另一人强调这不是新漏洞，而是针对此前已披露漏洞的实战利用指南。还有人主张采用经过形式化验证的微虚拟机监控器设计（如 Nova），而一个基于 Firecracker 的数据库游乐场（ClickBench）的运营者表示愿意托管概念验证逃逸。

**标签**: `#virtualization`, `#security`, `#firecracker`, `#exploitation`, `#hypervisor`

---

<a id="item-2"></a>
## [AI 正在大幅加速 AI 研究，但这是真正的进步吗？](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) ⭐️ 8.0/10

一篇文章认为 AI 正在大幅加速 AI 研究，引发了 Hacker News 上 193 分、148 条评论的讨论，质疑所观察到的进展是真正的进步，还是仅仅是基准过拟合和计算规模扩展。 这场辩论对 AI 行业至关重要，因为如果 AI 真正加速了 AI 研究，可能导致递归自我改进和能力快速提升；否则，可能意味着收益递减和期望膨胀。 评论者强调，基准是精心策划的，可以被训练；许多感知到的加速可能来自资本和计算规模扩展，而非模型智能；在数万亿 token 上的训练速度仍然是一个根本瓶颈。

hackernews · yurivish · Nov 6, 20:27 · [社区讨论](https://news.ycombinator.com/item?id=50397994)

**背景**: AI 研究通常使用基准来衡量进展，但模型可能会对这些基准过拟合，使性能提升看起来比实际改进更大。缩放定律描述了模型性能如何随着更多数据、计算和参数而提升，而递归自我改进指的是 AI 系统提升自身能力，可能导致快速加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nhimg.org/glossary/benchmark-overfitting/">What Is Benchmark Overfitting ? Definition & Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">Our progress toward recursive self - improvement , and its implications.</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论大多持怀疑态度，评论者认为基准被操纵，收益可能来自资本和计算规模扩展而非更智能的模型，并且训练速度仍是瓶颈；一些人还指出，AI 加速了工作，但可能并未整体上更快地改变世界。

**标签**: `#AI research`, `#benchmarking`, `#scaling laws`, `#AI acceleration`, `#community discussion`

---

<a id="item-3"></a>
## [甲骨文迫于美国压力取消与腾讯 70 亿美元 AI 芯片租赁协议](https://t.me/zaihuapd/44958) ⭐️ 8.0/10

甲骨文取消了与腾讯签署的为期五年、价值约 70 亿美元的 AI 芯片租赁协议，此前美国官员就国家安全问题向甲骨文表达了担忧。该协议原计划让腾讯通过甲骨文在东南亚的数据中心获得约 10 万枚先进 AI 芯片，首付款约占 30%。 此次取消表明，美国出口管制正越来越多地适用于通过云服务获取先进 AI 芯片的途径，而不仅仅是直接的硬件销售，这可能使中国 AI 企业的海外算力策略更加复杂。这也凸显了地缘政治紧张正在重塑 AI 基础设施供应链，并可能对类似的跨境租赁安排产生威慑作用。 这项为期五年的租赁协议于今年早些时候签署，旨在让腾讯通过甲骨文在东南亚的多个数据中心使用在中国无法获得的芯片。据报道，腾讯已支付约 30%的首付款，交易价值约为 70 亿美元。

telegram · zaihuapd · Nov 6, 05:02

**背景**: 自 2018 年以来，美国逐步收紧对华先进半导体出口管制，旨在限制中国获取尖端 AI 芯片及相关计算能力。作为回应，中国科技企业寻求变通方案，例如在海外数据中心租赁算力，而美国立法者一直在权衡如何应对这一漏洞。甲骨文是一家主要的美国云和数据中心提供商，在东南亚拥有基础设施，因而成为此类安排的潜在渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aidirectory.com/news/tencent-leases-100000-ai-chips-from-oracle-southeast-asia">Tencent leases 100,000 AI chips from Oracle in south-east Asia</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R48642/R48642.5.pdf">U.S. Export Controls and China: Advanced Semiconductors</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#US-China tech`, `#Oracle`, `#Tencent`, `#export controls`

---

<a id="item-4"></a>
## [百度发布文心 5.0：2.4 万亿参数全模态 MoE 模型](https://t.me/zaihuapd/44959) ⭐️ 8.0/10

百度今日正式发布文心 5.0 全模态大模型，参数规模达 2.4 万亿，采用全模态统一建模技术，可同时处理文本、图像、音频和视频等多种信息类型。该模型在超过 40 项权威基准测试中表现超越 Gemini-2.5-Pro 和 GPT-5-High 等国际顶尖模型，并采用混合专家结构，激活参数低于 3%。 这是中国主要 AI 厂商的旗舰级发布，表明国内模型正致力于在规模和全模态能力上与世界顶尖系统直接竞争。如果基准测试声明得到验证，可能改变外界对中国 AI 竞争力的看法，并加剧全球向更大规模全模态模型发展的竞赛。 该模型采用混合专家设计，每次推理激活的参数不到 2.4 万亿总参数的 3%，在保持能力的同时提升效率。百度还邀请了来自科技、金融、文化、教育等领域的 835 位专家参与模型指导和校准，目前个人用户可通过文心平台使用。

telegram · zaihuapd · Nov 6, 05:41

**背景**: 全模态模型旨在通过单一统一架构理解和生成跨文本、图像、音频和视频等多种模态的内容，而早期模型通常分别处理每种模态。混合专家（MoE）是一种技术，它扩大了总参数规模，但每个输入 token 只激活一小部分“专家”子网络，从而让大模型运行更高效。激活参数指的是推理时实际使用的模型部分，在 MoE 架构中通常远小于总参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference?</a></li>
<li><a href="https://www.marktechpost.com/2025/11/17/uni-moe-2-0-omni-an-open-qwen2-5-7b-based-omnimodal-moe-for-text-image-audio-and-video-understanding/">Uni-MoE-2.0- Omni : An Open Qwen2.5-7B Based... - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Baidu`, `#ERNIE`, `#MoE`, `#multimodal`

---

<a id="item-5"></a>
## [长江存储新建武汉工厂国产设备占比拟达 70%](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 8.0/10

长江存储计划在武汉建设第四座工厂，预计 2027 年开工，目标将国产设备采购比例提高至至少 60%、最高 70%，高于第三座工厂目前超过 50%的水平。新工厂将生产超过 300 层的先进 NAND 闪存，主要面向数据中心和人工智能存储需求。 这标志着中国领先存储厂商尝试的最高国产设备比例之一，反映出在美国出口管制下中国半导体供应链的重大转变。长江存储在中国 NAND 市场份额已升至 38.5%，超过三星，未来三座新厂全部投产后整体产能有望翻倍，从而增强中国在人工智能存储基础设施领域的地位。 清洗、抛光和刻蚀设备预计将成为国产化的主要增量，而光刻、检测等先进设备仍依赖海外供应商。超过 300 层的 NAND 面向数据中心和人工智能存储，该计划延续了第三座工厂国产设备占比已超过 50%的趋势。

telegram · zaihuapd · Nov 6, 08:34

**背景**: 长江存储是一家中国 NAND 闪存制造商，2016 年在武汉成立，有政府投资背景，旨在减少中国对外国芯片的依赖。NAND 闪存是用于固态硬盘和数据中心的非易失性存储器，堆叠更多层数（300 层以上）可提高存储密度。美国对先进半导体设备的出口管制推动中国芯片制造商实现供应链本地化，各类设备的国产化率差异较大，其中 CMP 和减薄设备进展最快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.eetimes.com/ymtc-nand-design-surprise-alongside-a-new-fab/">YMTC NAND Design Surprise Alongside a New Fab- EE Times</a></li>
<li><a href="https://www.csis.org/analysis/true-impact-allied-export-controls-us-and-chinese-semiconductor-manufacturing-equipment">The True Impact of Allied Export Controls on the U . S . and Chinese ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#NAND flash`, `#YMTC`, `#supply chain localization`, `#AI storage`

---