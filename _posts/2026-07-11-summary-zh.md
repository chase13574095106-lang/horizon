---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> From 24 items, 9 important content pieces were selected

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 9.0/10
2. [人形机器人完成全球首例活猪胆囊手术](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三档模型](#item-3) ⭐️ 9.0/10
4. [SGLang v0.5.15 在 Blackwell GPU 上大幅提升 GLM-5.2 性能](#item-4) ⭐️ 8.0/10
5. [Hotz 警告 AI 监管威胁自由](#item-5) ⭐️ 8.0/10
6. [SpaceXAI 与 Cursor 联合发布 Grok 4.5](#item-6) ⭐️ 8.0/10
7. [苹果起诉 OpenAI 窃取商业机密以推进硬件业务](#item-7) ⭐️ 8.0/10
8. [U-Boot 六个漏洞可在系统启动前执行代码](#item-8) ⭐️ 8.0/10
9. [上海计划 2027 年前实现高质量脑控](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，并移除了传统的 PagedAttention 实现。Transformers 建模后端现在达到了原生级性能，并新增了对 LLaVA-OneVision-2 和 GLM-5 等模型的支持。 此版本标志着 vLLM 的重大架构转变，简化了代码库并提升了多种模型的性能。PagedAttention 的移除和 Model Runner V2 的成熟，意味着 LLM 社区将拥有更稳定、更高效的推理引擎。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带有完整 CUDA 图的动态推测解码。Transformers 后端获得了 FP8 MoE 支持和 CUDA 图修复，性能与原生 vLLM 持平。

github · khluu · Jul 11, 20:06

**背景**: vLLM 是一个开源的大语言模型推理引擎，使用 PagedAttention 来高效管理 KV 缓存的内存。Model Runner V2 是一个较新的执行路径，取代了旧的 V1 后端，旨在提升性能和可维护性。此版本移除了传统的 PagedAttention 代码，完全依赖新的注意力实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>
<li><a href="https://docs.vllm.ai/en/v0.14.1/api/vllm/multimodal/evs/">evs - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-2"></a>
## [人形机器人完成全球首例活猪胆囊手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生远程操控宇树 G1 人形机器人，成功在活猪身上完成了全球首例微创胆囊切除手术，研究成果已发表在《自然》期刊。 这一突破表明，低成本通用人形机器人能够执行精细手术，有望在偏远地区、战场甚至太空等资源有限的环境中实现远程手术，而专用手术机器人过于昂贵或无法部署。 宇树 G1 基础款售价低至 13,500 美元，配备灵巧手后约 67,000 美元，而达芬奇手术机器人售价高达数百万美元。该机器人高 1.5 米、重 27 公斤，体积小巧便于携带。

telegram · zaihuapd · Jul 11, 02:29

**背景**: 腹腔镜胆囊切除术是一种常见的微创手术，用于切除胆囊。达芬奇等专用手术机器人虽已广泛应用，但成本高达数十万至数百万美元，限制了可及性。宇树 G1 等通用人形机器人专为移动和操作设计，本研究证明它们可通过远程控制适应手术任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>

</ul>
</details>

**标签**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三档模型](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布 GPT-5.6 系列，包含三个档次：旗舰级 Sol、平衡型 Terra 和低成本高并发型 Luna。该更新引入了 max/ultra 推理、多智能体协作和程序化工具调用，在代码、知识工作、设计、科研和网络安全能力上有显著提升。 此次发布标志着在让先进 AI 更易获取且更具成本效益方面迈出了重要一步，Sol 提供顶级性能，Luna 支持高并发低成本部署。新的多智能体协作和程序化工具调用功能可能改变各行业复杂任务的自动化方式。 GPT-5.4 将于 7 月 23 日退役，而 GPT-5.5 仍可使用。模型档次名称（Sol、Terra、Luna）是持久的，将按自身节奏演进，与代际编号无关。Sol 在八个文档翻译场景中的五个上获得了满分 5.0。

telegram · zaihuapd · Jul 11, 13:34

**背景**: GPT-5.6 是 OpenAI 大语言模型的最新版本，接替 GPT-5.5。该系列引入了分层模型结构，数字表示代际，名称（Sol、Terra、Luna）表示能力和成本级别。多智能体协作允许多个 AI 智能体协调完成复杂任务，而程序化工具调用使模型能够通过代码调用工具，而非逐个 API 调用，从而降低延迟和成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna : Which Tier Should You Actually Use?</a></li>
<li><a href="https://belindoc.com/blog/gpt-5-6-translation-review-sol-terra-luna">GPT - 5 . 6 Document Translation Review: Sol vs Terra vs Luna ...</a></li>
<li><a href="https://apidog.com/blog/gpt-5-6-sol-vs-terra-vs-luna/">GPT - 5 . 6 Sol vs Terra vs Luna : which model should you use?</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#LLM`, `#multi-agent`

---

<a id="item-4"></a>
## [SGLang v0.5.15 在 Blackwell GPU 上大幅提升 GLM-5.2 性能](https://github.com/sgl-project/sglang/releases/tag/v0.5.15) ⭐️ 8.0/10

SGLang v0.5.15 为 Blackwell GPU 上的 GLM-5.2 提供了生产级调优的 NVFP4 支持，在 8 块 B300 上实现每用户每秒超过 500 个 token，在 4 块 GB300 上达到 450 个 token（批大小为 1）。此外，默认启用了 Spec V2 推测解码，并引入了 IndexShare MTP、TopK V2 等优化。 此版本显著提升了面向长周期任务的 GLM-5.2 模型的推理效率，使其更适用于实时应用。推测解码和内核优化也惠及其他大语言模型，推动了 NVIDIA Blackwell 硬件上 LLM 推理技术的发展。 Spec V2 通过可 CUDA 图化的 DSA 草稿扩展和融合元数据操作，实现了端到端吞吐量提升 11%。IndexShare MTP 在长上下文场景下将草稿步骤成本降低最多 1.9 倍。此版本还新增了对 Hunyuan 3、Qwen3.6 NVFP4 等模型的支持，以及通过 Exa 实现的原生网络搜索功能。

github · Fridge003 · Jul 10, 22:58

**背景**: NVFP4 是 NVIDIA 随 Blackwell GPU 推出的 4 位浮点量化格式，相比传统 4 位整数量化，能以更低比特宽度实现更好的推理质量。推测解码通过使用小型草稿模型预测多个 token，再由主模型验证，从而加速文本生成。SGLang 是一个开源的大语言模型推理框架，专注于优化推理性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.03950v1">Diagonal-Tiled Mixed- Precision Attention for Efficient Low-Bit MXFP...</a></li>
<li><a href="https://huggingface.co/JongYeop/Mistral-7B-Instruct-v0.2-FP4-W4A4">JongYeop/Mistral-7B-Instruct-v0.2-FP4-W4A4 · Hugging Face</a></li>
<li><a href="https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/">The next generation of speculative decoding: DFlash and Spec V2 - LMSYS Org</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#GPU optimization`, `#speculative decoding`, `#GLM`, `#Blackwell`

---

<a id="item-5"></a>
## [Hotz 警告 AI 监管威胁自由](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html) ⭐️ 8.0/10

George Hotz 发表了一篇文章，认为 AI 监管可能导致一个反乌托邦的未来，AI 系统强制执行意识形态合规，并与历史上的自由斗争相类比。 这篇文章引发了关于 AI 安全与个人自由之间平衡的辩论，强调了监管可能被用来压制异议和强制执行政治议程的担忧。 Hotz 特别警告 AI 系统可能拒绝提供信息并将用户记录为“思想犯罪”，并认为自由不是二元的，而是一个值得为之奋斗的基本原则。

hackernews · rvz · Jul 11, 18:04 · [社区讨论](https://news.ycombinator.com/item?id=48874200)

**背景**: George Hotz 是著名的黑客和企业家，以越狱 iPhone 和创立 comma.ai 而闻名。他的文章反映了对技术监管的自由意志主义观点，经常批评 AI 治理中的过度干预。

**社区讨论**: 评论反应不一：一些人同意 Hotz 对审查和思想犯罪的担忧，而另一些人则认为自由不是二元的，且在现实世界中行动的 AI 代理需要不同的考量。也有批评称文章缺乏中心论点。

**标签**: `#AI ethics`, `#regulation`, `#freedom`, `#George Hotz`, `#societal impact`

---

<a id="item-6"></a>
## [SpaceXAI 与 Cursor 联合发布 Grok 4.5](https://t.me/zaihuapd/42484) ⭐️ 8.0/10

SpaceXAI 与 Cursor 联合发布了新一代 AI 模型 Grok 4.5，专注于编码、法律和金融服务等任务，声称在 Harvey 法律基准测试中排名第一，且 token 效率达到同类领先模型的两倍。 这是 SpaceX 以 600 亿美元收购 Cursor 后双方推出的首个联合模型，标志着向专业领域 AI 的重大进军。高 token 效率和领域专注可能颠覆现有的 AI 编程和法律工具。 Grok 4.5 以每秒 80 token 的速度运行，定价为每百万输入 token 2 美元。除了核心专注领域外，它还强调了增强的网络安全能力。

telegram · zaihuapd · Jul 11, 01:44

**背景**: Harvey 法律代理基准是一个开源基准，用于评估 AI 代理在真实法律工作中的表现。Token 效率指模型在单位成本或时间内生成的有用 token 数量，直接影响准确性和成本。Cursor 是一个 AI 驱动的代码编辑器和开发环境，于 2026 年 6 月被 SpaceX 以 600 亿美元收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark">Introducing Harvey’s Legal Agent Benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company)</a></li>
<li><a href="https://www.linkedin.com/posts/sean-holdbrook-74965654_i-was-originally-just-replying-to-a-post-activity-7396573267551117313-Dty6">The Importance of Token Efficiency in LLMs | Sean Brook... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Grok`, `#SpaceXAI`, `#Cursor`

---

<a id="item-7"></a>
## [苹果起诉 OpenAI 窃取商业机密以推进硬件业务](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 8.0/10

2026 年 7 月 10 日，苹果在美国加州北区联邦法院起诉 OpenAI、两名前员工及 io Products，指控其系统性窃取与产品设计、制造工艺及供应链相关的商业机密，以加速 OpenAI 的消费级硬件研发。 这场两大科技巨头之间的高调法律战可能为商业秘密法如何适用于 AI 公司从成熟硬件制造商挖角树立先例，并可能影响 AI 硬件领域的竞争格局。如果苹果的指控成立，OpenAI 的硬件业务——包括与 Jony Ive 的 io Products 共同开发的设备——将面临严重的法律和声誉损害。 苹果具体指控前员工 Chang Liu 在离职后仍访问内部网络并下载数十份硬件文件，而 OpenAI 硬件负责人 Tang Yew Tan 在离职前将供应商资料发送至个人邮箱，并要求求职者携带苹果零部件参加面试。苹果还声称，目前有超过 400 名前苹果员工在 OpenAI 工作。

telegram · zaihuapd · Jul 11, 03:14

**背景**: OpenAI 以 GPT-4 等 AI 模型闻名，近年来正扩展至硬件领域。2025 年 5 月，它收购了由前苹果设计总监 Jony Ive 创立的 io Products，以主导其硬件开发。双方合作的首款设备原计划 2026 年发布，但因商标纠纷推迟至 2027 年。商业秘密是提供竞争优势的机密商业信息，其盗用可能导致法律责任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html">Apple sues OpenAI alleging trade secret theft, says scheme was 'at every level'</a></li>
<li><a href="https://www.engadget.com/2212759/apple-calls-openais-hardware-business-rotten-to-its-core-in-trade-secret-theft-lawsuit/">Apple calls OpenAI's hardware business 'rotten to its core' in trade secret theft lawsuit - Engadget</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_(company)">io (company) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI hardware`

---

<a id="item-8"></a>
## [U-Boot 六个漏洞可在系统启动前执行代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

固件安全公司 Binarly 披露了 U-Boot 的 FIT 签名验证中的六个漏洞，其中两个可导致任意代码执行，四个可造成拒绝服务，影响自 2013.07 版本以来的所有版本。 这些漏洞使攻击者能在操作系统启动前执行恶意代码，绕过 Secure Boot 等安全措施，并可能在数百万台设备上植入持久性固件恶意软件。 这些漏洞（BRLY-2026-037 至 BRLY-2026-042）位于 FIT 镜像签名验证代码中，可在支持远程固件更新的设备（如 BMC）上远程利用。

telegram · zaihuapd · Jul 11, 08:32

**背景**: U-Boot 是一种广泛用于嵌入式设备的开源引导程序，负责加载操作系统。FIT（Flattened Image Tree）是一种将内核、设备树和其他二进制文件与加密签名打包的格式，以确保真实性。这些漏洞绕过了签名验证，允许未签名代码运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/">New U-Boot flaws could enable stealthy firmware attacks</a></li>
<li><a href="https://cybersecuritynews.com/u-boot-fit-signature-verification/">Six U - Boot FIT Signature Verification Flaws Enable Code Execution...</a></li>
<li><a href="https://docs.u-boot-project.org/en/latest/usage/fit/signature.html">U - Boot FIT Signature Verification — Das U - Boot unknown version...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#bootloader`, `#firmware`, `#U-Boot`

---

<a id="item-9"></a>
## [上海计划 2027 年前实现高质量脑控](https://t.me/zaihuapd/42501) ⭐️ 8.0/10

上海市科学技术委员会印发了《上海市脑机接口未来产业培育行动方案（2025-2030 年）》，目标是在 2027 年前实现高质量脑控，半侵入式脑机接口产品在国内率先实现临床应用，侵入式脑机接口研发取得突破。 这项政府支持的计划标志着对脑机接口技术的强力政策支持，可能加速临床采用，并使上海成为该领域的全球领导者。它可能为瘫痪或失语患者带来改变生活的益处。 该计划旨在推动 5 款以上侵入式或半侵入式脑机接口产品完成医疗器械型式检验和临床试验，面向失语、瘫痪等患者实现部分语言和运动功能恢复。

telegram · zaihuapd · Jul 11, 15:49

**背景**: 脑机接口分为三类：非侵入式（头皮电极）、半侵入式（电极置于颅骨下大脑表面）和侵入式（电极直接植入脑组织）。半侵入式脑机接口在信号质量和减少组织损伤之间取得平衡，使其成为临床应用的有前途的路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://segmentfault.com/a/1190000044921513">segmentfault.com/a/1190000044921513</a></li>
<li><a href="http://paper.people.com.cn/zgjjzk/pc/content/202512/30/content_30129910.html">脑 机 接 口 治病：从科幻到现实还有多远</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=837218">视频|想象过“ 脑 控 上淘宝”和“意念对话”吗？ 上海 脑 机接口临床试验获突破</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#policy`, `#China`, `#clinical application`, `#innovation`

---