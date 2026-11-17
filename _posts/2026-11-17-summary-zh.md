---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> From 36 items, 7 important content pieces were selected

---

1. [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1，性能大幅提升](#item-1) ⭐️ 8.0/10
2. [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费提供计算机科学课程讲座](#item-2) ⭐️ 8.0/10
3. [Optimizely CDN 遭入侵，向 Zoom 和 GitLab 等网站分发恶意软件](#item-3) ⭐️ 8.0/10
4. [Jiff 1.0：Rust 的新日期时间库](#item-4) ⭐️ 8.0/10
5. [美商务部将定稿规则，封堵中国公司远程使用 AI 芯片的漏洞](#item-5) ⭐️ 8.0/10
6. [山东大学团队声称首次给出哥德巴赫猜想条件性证明](#item-6) ⭐️ 8.0/10
7. [阿里、月之暗面等中国头部 AI 公司在新模型中收紧网络攻击能力](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1，性能大幅提升](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 发布，包含来自 412 位贡献者的 1061 次提交，新增 10 个模型，默认启用可扩展 KV 缓存，移除 Model Runner V1，并在 Blackwell 和 MI355X 硬件上实现最高 1.95 倍的解码加速。 此版本显著提升了 LLM 推理的吞吐量和性能，尤其是在新硬件上，并通过使 Model Runner V2 成为唯一的 GPU 运行器简化了代码库，影响所有使用 vLLM 部署 LLM 的用户。 默认块大小现在为 64（原为 16），ROCm 7.2 构件被弃用，转而使用 ROCm 10.0，并且需要 huggingface_hub >= 2.0.0；可扩展 KV 缓存根据预热后实际空闲内存进行大小调整，在高并发下可能使某些模型的每令牌解码延迟增加 6-18%。

github · khluu · Nov 16, 23:22

**背景**: vLLM 是一个高吞吐量的 LLM 推理引擎，使用 PagedAttention 和 KV 缓存来高效服务大型语言模型。Model Runner V2 是执行核心的模块化重新实现，可扩展 KV 缓存根据可用 GPU 内存动态调整缓存大小以最大化吞吐量。Blackwell 和 MI355X 是 NVIDIA 和 AMD 最新的面向 AI 工作负载的 GPU 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V 2 : A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>
<li><a href="https://gpuadvisor.com/mi355x-vs-gb200">MI355X vs GB200 — AMD vs NVIDIA Inference Comparison 2026 ...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#performance-optimization`, `#release`

---

<a id="item-2"></a>
## [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费提供计算机科学课程讲座](https://www.cs.cmu.edu/learn/) ⭐️ 8.0/10

卡内基梅隆大学格里芬计算机科学学院推出了 CS Learn，在 YouTube 上免费发布当前 CMU 计算机科学课程整个学期的讲座视频，本周每天首播一门课程，明年一月还将推出更多课程。 这是一项重要的开放教育进展，因为它免费提供了高质量的 CMU 最新课程讲座，可能惠及全球学习者，并补充了现有的开放课程项目如 MIT OpenCourseWare。 该项目由 CMU 教学教授 Phillip Compeau 负责，一些学生构建了自动化制作工具；未来计划提供包含项目和反馈机制的课程材料。

hackernews · pcompeau · Nov 16, 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**背景**: 像 MIT OpenCourseWare 这样的开放课程项目几十年来一直在网上免费提供课程材料。CS Learn 延续了这一传统，在 YouTube 上提供 CMU 当前课程的全学期讲座，使任何有互联网接入的人都能获得高质量的计算机科学教育。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://en.wikipedia.org/wiki/MIT_OpenCourseWare">MIT OpenCourseWare - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，创作者参与讨论，评论者讨论了 AI 时代基础知识的重要性，请求特定课程，并强调需要项目和反馈来补充讲座。

**标签**: `#education`, `#computer-science`, `#open-courseware`, `#CMU`, `#YouTube`

---

<a id="item-3"></a>
## [Optimizely CDN 遭入侵，向 Zoom 和 GitLab 等网站分发恶意软件](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

广泛使用的 A/B 测试和实验平台 Optimizely 遭到入侵，导致其 CDN 向包括 Zoom 和 GitLab 在内的客户网站分发恶意 JavaScript。攻击还影响了 Optimizely 自己的网站，www.optimizely.com 和 login.optimizely.com 的代码片段也包含了恶意代码。 这起供应链事件凸显了第三方脚本的系统性风险：单个供应商被入侵就可能向数千个大型网站注入恶意软件，影响数百万用户。它强调了在第三方脚本生态系统中加强安全控制和问责的迫切需求。 Optimizely 的 CDN 只是原样分发了它收到的内容，这表明入侵发生在 Optimizely 的源端，而非通过 CDN 缓存投毒。攻击者如何获得对如此多客户项目的写入权限的确切方法仍然未知，可能是通过被入侵的 Optimizely 系统或具有跨客户访问权限的凭证。

hackernews · kristjansson · Nov 16, 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**背景**: Optimizely 是一个流行的 A/B 测试和 Web 实验平台，允许营销团队无需工程人员参与即可修改网站内容。网站通常嵌入 Optimizely 的 JavaScript 代码片段，该片段会从 Optimizely 的 CDN 加载更多脚本，形成供应链依赖。第三方脚本常用于分析、广告和个性化，但它们扩大了攻击面，因为脚本提供商的任何入侵都可能影响所有客户网站。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alickaj.eu/?read=why-unmanaged-third-party-scripts-put-your-website-at-risk">Why Unmanaged Third - Party Scripts Put Your Website at Risk — AEU</a></li>
<li><a href="https://betanews.com/article/the-rise-of-third-party-browser-script-attacks-qa/">The rise of third - party browser script attacks [Q&A] - BetaNews</a></li>
<li><a href="https://suriq.io/blog/brevo-cdn-edge-supply-chain-attack">Brevo Supply - Chain Hack: Malware Injected at the CDN Edge</a></li>

</ul>
</details>

**社区讨论**: 评论者对缺乏问责制和第三方脚本的风险表示不满，一些人指责通过 Google Tag Manager 等工具让营销部门轻松添加标签的趋势。其他人建议使用 NoScript 等缓解措施，并认为大型网站应实施更严格的控制或自行托管供应商脚本。

**标签**: `#security`, `#supply-chain`, `#web`, `#javascript`, `#optimizely`

---

<a id="item-4"></a>
## [Jiff 1.0：Rust 的新日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Andrew Gallant（burntsushi）发布了 Jiff 1.0，这是一个新的 Rust 日期时间库，旨在改进 chrono 等现有库，提供经过深思熟虑的 API，自动处理夏令时等常见问题。 Jiff 1.0 是 Rust 生态系统的一个重要里程碑，它提供了 chrono 的现代替代品，注重正确性和易用性，其作者是一位备受尊敬的开发者，以 regex 和 ripgrep 等高质量库而闻名。 Jiff 与 Time Zone Database 无缝集成，支持夏令时感知的算术和舍入，并允许对时区感知的日期时间进行无损格式化和解析；它还提到处理 TAI 等时间尺度，但 UT1 等其他尺度可能需要手动处理。

hackernews · burntsushi · Nov 16, 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**背景**: Rust 的日期时间处理长期由 chrono crate 主导，虽然稳定，但其 API 设计一直受到批评。Jiff 旨在通过将时区处理置于核心位置，提供更符合人体工程学且更安全的替代方案，使其难以被误用。该库由 Andrew Gallant 编写，他是一位知名的 Rust 开发者，以创建 regex 和 ripgrep 等广泛使用的 crate 而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant's Blog</a></li>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/chrono/latest/chrono/">chrono - Rust - Docs.rs</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常积极，一位前 chrono 维护者对 Jiff 表示感谢，并分享了对 API 稳定性和倦怠的见解。其他人赞赏 Jiff 诚实地承认其局限性，并希望它能在 chrono 之上获得更广泛的采用，同时一些人提出了关于处理 TAI 和 UT1 等各种时间尺度的技术问题。

**标签**: `#Rust`, `#datetime`, `#library`, `#API design`, `#time scales`

---

<a id="item-5"></a>
## [美商务部将定稿规则，封堵中国公司远程使用 AI 芯片的漏洞](https://t.me/zaihuapd/45161) ⭐️ 8.0/10

美国商务部正在敲定一项规则，阻止中国 AI 公司通过境外数据中心远程使用先进 AI 芯片，最早可能于本月公布。该规则将现有的半导体出口限制扩展至马来西亚、新加坡、泰国等七个东南亚国家，以封堵远程访问和芯片走私漏洞。 该规则封堵了一个重大漏洞，使中国 AI 公司无法再通过第三国托管的先进英伟达芯片绕过美国出口管制，可能颠覆全球 AI 基础设施的访问模式。此举将严重影响字节跳动和阿里巴巴等中国 AI 企业以及东南亚数据中心运营商，并重塑全球芯片供应链。 据报道，该规则是商务部工业与安全局（BIS）发布的临时最终规则，对出口至印度尼西亚、马来西亚、新加坡、泰国和巴西的先进芯片增加了基于目的地的许可证要求，并包含对混合物品的限制。英伟达曾游说反对封堵这一远程访问缺口，称美国 AI 基础设施需要在全球取胜。

telegram · zaihuapd · Nov 16, 14:44

**背景**: 美国对先进 AI 芯片（如英伟达高端 GPU）的出口管制旨在防止中国获取可能增强其军事和 AI 能力的技术。然而，中国企业一直能够远程访问位于第三国数据中心的此类芯片，从而规避限制。新规则旨在通过将管制扩展至更多国家并对数据中心运营商施加许可证要求，来封堵这一“远程访问漏洞”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/trump-admin-moves-to-strangle-chinas-remote-access-to-american-ai-chips-2000840511">Trump Admin Moves to Strangle China's Remote Access to American...</a></li>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China's Access To Advanced Chips Via Singapore ...</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2026/11/16/us-closes-loophole-that-allowed-china-to-remotely-access-nvidia-chips/">US Closes Loophole That Allowed China To Remotely Access ...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#US-China tech`, `#semiconductor policy`, `#AI infrastructure`

---

<a id="item-6"></a>
## [山东大学团队声称首次给出哥德巴赫猜想条件性证明](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 8.0/10

山东大学李嘉民、刘建亚在论文中声称，在狄利克雷 L 函数的广义黎曼猜想成立、并满足两种附加谱假设之一的条件下，首次证明了所有充分大的偶数都是两个素数之和，且这两个素数位于该偶数的三分之一至三分之二之间。 这是一项重要进展，因为它覆盖了所有充分大的偶数，而以往结果只能处理几乎所有偶数或需要更强未证假设。它可能推动解析数论的新方法，但由于依赖未证假设，这并非哥德巴赫猜想的无条件证明。 该证明是条件性的：它假设狄利克雷 L 函数的广义黎曼猜想成立，并满足两种附加谱假设之一，作者指出仅靠广义黎曼猜想不足以推出结论。所用方法新颖，不同于经典筛法和圆法，但论文尚未经过同行评审，且来源仅为简要摘要。

telegram · zaihuapd · Nov 16, 16:01

**背景**: 哥德巴赫猜想断言每个大于 2 的偶数都是两个素数之和；该猜想已被验证到 4×10^18，但仍未证明。广义黎曼猜想将黎曼猜想推广到狄利克雷 L 函数，断言其所有非平凡零点都位于临界线 Re(s)=1/2 上。谱假设是关于某些算子特征值的假设，通常源于数论与谱分析之间的联系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Goldbach's_conjecture">Goldbach's conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#number-theory`, `#Goldbach-conjecture`, `#research`, `#conditional-proof`

---

<a id="item-7"></a>
## [阿里、月之暗面等中国头部 AI 公司在新模型中收紧网络攻击能力](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 8.0/10

阿里巴巴、腾讯和月之暗面在新一代模型中刻意削弱了进攻性网络能力，同时提升了防御表现；阿里最新旗舰 Qwen 未开放权重，用户无法下载并自定义完整版本。据报道，腾讯在本月发布 Hy4 模型前已削减了网络功能。 这标志着 AI 安全、网络安全与政策的重要交汇：中国头部 AI 实验室为回应出口管制草案，主动限制具有双重用途的网络能力。这可能改变中国前沿模型的发布方式，并为模型提供方（而非仅监管机构）主动限制能力树立先例。 此举与中国商务部上月公布的出口管制草案相关，该草案拟禁止可攻击关键基础设施和政府网络的 AI 工具出口。阿里将旗舰 Qwen 保持为闭源权重，偏离了其以往开放模型的策略，不过报道未披露具体的能力评测数据。

telegram · zaihuapd · Nov 17, 02:20

**背景**: 开放权重模型指训练好的参数可被下载并在本地运行，既节省成本、便于数据掌控，也使得无限制的微调成为可能；Qwen 一直是下载量最大的开放模型系列之一。月之暗面的 Kimi 系列（如开放权重的 Kimi K3）以智能体和编程能力著称。中国的出口管制草案将 AI 技术划分为禁止、限制、自动许可和未覆盖四类，涵盖模型权重、智能体和芯片集群，据报道 API 不在管制范围内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aighten.com/en/blog/china-ai-export-controls-draft-models-agents-chips">China AI Export Controls Draft : Models, Agents and Chips</a></li>
<li><a href="https://www.swarchitect.net/en/china-ai-export-controls-2026-10/">China AI Export Draft Spares APIs, Not Foreign Installs · SW Architect</a></li>
<li><a href="https://www.secondtalent.com/resources/every-qwen-ai-model-explained-compared/">Every Qwen AI Model Explained and Compared (Nov, 2026)</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#cybersecurity`, `#AI regulation`, `#China tech`, `#export controls`

---