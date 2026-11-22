---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> From 24 items, 5 important content pieces were selected

---

1. [Lean 形式化声称验证黎曼猜想](#item-1) ⭐️ 9.0/10
2. [浙江大学在超导芯片上首次真机实现量子随机存储器](#item-2) ⭐️ 9.0/10
3. [GPGME 双重释放漏洞披露，影响 2.3.0 之前版本](#item-3) ⭐️ 8.0/10
4. [微软通过 USB4 上的 RDMA 实现多台 PC 共享 AI 模型](#item-4) ⭐️ 8.0/10
5. [口服 RAS(ON)抑制剂 daraxonrasib 一线治疗胰腺癌缓解率达 60.7%](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Lean 形式化声称验证黎曼猜想](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

Anthropic 数学家 Levent Alpöge 于 11 月 20 日宣布，他借助 Claude 生成了黎曼猜想的 Lean 编码证明，并声称同时确认了广义黎曼猜想，详细证明文稿超过 25 万页。 若验证通过，这将是数学领域的范式转变，解决了一个 165 年历史的千禧年大奖难题，并证明 AI 辅助形式化验证能够攻克最深奥的未解问题。 该证明依赖 Lean 定理证明器及其内核来保证正确性，但独立验证因多个检查器可能存在漏洞以及形式化的巨大规模而变得复杂。

hackernews · g-b-r · Nov 21, 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**背景**: 黎曼猜想由 Bernhard Riemann 于 1859 年提出，涉及素数分布规律，是数学中最著名的未解难题之一。形式化验证是指用 Lean 等编程语言编码数学证明，使计算机能检查每一步逻辑，从而提供高置信度的正确性保证。广义黎曼猜想将该猜想推广到更广泛的 L-函数类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>
<li><a href="https://4m4.it/posts/when-the-proof-checker-becomes-part-of-the-experiment/index.html">When the Proof Checker Becomes Part of the Experiment – Random...</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了证明的可靠性，指出尽管多个具有一致性证明的独立检查器使得因漏洞导致错误证明的可能性极低，但过去如伪造的 Collatz 反证等事件表明检查器并非完全独立。一些人赞扬 Levent Alpöge 引导 Claude 生成证明的技巧，另一些人则强调对现代数学的大规模形式化本身就是一个重大成果。

**标签**: `#Lean`, `#Riemann Hypothesis`, `#formal verification`, `#mathematics`, `#AI-assisted proof`

---

<a id="item-2"></a>
## [浙江大学在超导芯片上首次真机实现量子随机存储器](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

浙江大学团队在自主制备的超导量子芯片「天目 2 号」上，全球首次真机实现量子随机存储器（QRAM），运行的原型能分别以 80.9%和 60.4%的准确率调取 4 位和 8 位数据。该成果发表于《自然·物理》。 QRAM 是量子计算领域长期寻求的关键组件，相当于量子计算机的「高速内存」，有望支撑量子机器学习、数据库搜索等需要快速访问大规模数据的量子算法。此次首次硬件演示将 QRAM 从理论推向实验，可能加速实用量子架构的发展。 团队报告称，优化后的线路深度较未优化方案降低 30%以上，并首次实验验证该架构具备局部抗噪特性。下一步将推进 QRAM 的规模化研究。

telegram · zaihuapd · Nov 21, 08:31

**背景**: 量子随机存储器（QRAM）是经典 RAM 的量子对应物，利用地址的量子叠加态并行访问数据，有望指数级降低内存调用需求。超导量子比特是量子计算的主流平台之一，「天目 2 号」是浙江大学研发的芯片。线路深度是关键指标，因为更浅的线路受噪声和退相干影响更小，这对近期量子设备至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2305.10310v1">QRAM : A Survey and Critique</a></li>
<li><a href="https://www.emergentmind.com/topics/quantum-random-access-memory-qram">Quantum Random Access Memory ( qRAM )</a></li>
<li><a href="https://inspirehep.net/files/a4f25eaa7405134a37080762f30e88af">Resilience of Quantum Random Access Memory to Generic Noise</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#hardware`, `#research breakthrough`

---

<a id="item-3"></a>
## [GPGME 双重释放漏洞披露，影响 2.3.0 之前版本](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

GPGME（GnuPG Made Easy）中被披露存在一个双重释放漏洞，影响所有 2.3.0 之前的版本。由于 Ruby2Shell 漏洞导致 GitLab 提前更新，协调披露日期定为 2026 年 11 月 20 日。该漏洞由 Johan Carlsson 发现，并于 2026 年 11 月 12 日通过 GitLab 报告。 GPGME 是一个广泛使用的加密库，集成于许多应用程序中，包括大多数邮件客户端、XMPP 客户端、Samba 以及 GitLab 的签名提交功能，因此内存破坏漏洞可能在这些场景中导致代码执行。此次披露凸显了上游补丁传播的重要性以及内存不安全语言在关键安全软件中的风险。 社区成员指出，该漏洞在技术上是一个双重释放缺陷，而非完整的远程代码执行链。Red Hat 五年前的一个补丁似乎已修复此问题，但未被上游采纳。所有使用 2.3.0 之前 GPGME 的软件均受影响，无论是作为共享库、DLL 还是静态链接，包括 Gpg4win、GnuPG Desktop 和许多邮件客户端。

hackernews · gdgghhhhh · Nov 21, 08:32 · [社区讨论](https://news.ycombinator.com/item?id=50587208)

**背景**: GPGME（GnuPG Made Easy）是一个 C 语言库，为应用程序提供使用 GnuPG 进行加密、解密和签名的高级 API。双重释放漏洞发生在程序两次释放同一内存地址时，可能导致内存破坏，并可能被利用进行代码执行。这类缺陷在 C/C++ 代码中很常见，通常通过现代工具和 Rust 等内存安全语言来缓解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gnupg.org/documentation/manuals/gpgme/">Top (The ‘ GnuPG Made Easy’ Reference Manual)</a></li>
<li><a href="https://github.com/gpg/gpgme">GitHub - gpg/ gpgme : GnuPG Made Easy. NOTE: Maintainers are not...</a></li>
<li><a href="https://directory.fsf.org/wiki/GPGME">GPGME - Free Software Directory</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了严重性，有人指出这是双重释放缺陷而非完整的 RCE 链，并质疑报告是否故意夸大。另有人指出 Red Hat 五年前已修复但上游遗漏，还有人强调 C/C++ 需要 Rust 级别的工具，并列出受影响的软件如邮件客户端、Samba 和 Flatpak。

**标签**: `#security`, `#gnupg`, `#vulnerability`, `#cryptography`, `#open-source`

---

<a id="item-4"></a>
## [微软通过 USB4 上的 RDMA 实现多台 PC 共享 AI 模型](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

微软发布了 Windows 的 RDMA over USB4 开发者预览，允许多台 PC 通过标准 USB4 线缆共享内存和 GPU 资源，运行同一个本地 AI 模型。在演示中，三台搭载 AMD Ryzen AI Max+ 395 的系统以 4-bit 量化运行 Qwen3-235B-A22B 模型，速度约为每秒 18.5 个 token。 这降低了在本地运行大语言模型的门槛，用户无需专用高速网卡或交换机等网络硬件，即可组合现有硬件。它可能影响边缘 AI 和分布式计算，使小团队或爱好者能够运行原本需要单台高内存机器才能运行的模型。 该技术将通过 Windows Insider 实验频道推送，目前尚未公布正式版的时间表。演示使用了 4-bit 量化的 Qwen3-235B-A22B（一个拥有 2350 亿参数的大模型），在三台机器上实现了每秒 18.5 个 token 的速度。

telegram · zaihuapd · Nov 21, 06:13

**背景**: RDMA（远程直接内存访问）允许计算机直接访问彼此的内存而无需 CPU 参与，传统上用于 InfiniBand 等高性能网络。USB4 是一种高速连接标准，支持高达 40 Gbps 的数据速率。通过将 RDMA over USB4 引入 Windows，微软使 PC 之间能够使用常见端口直接共享内存，无需专用网络硬件。AMD Ryzen AI Max+ 395 是一款较新的 APU，集成 GPU 和统一内存，适合本地 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://club.dns-shop.ru/digest/189601-windows-11-nauchili-obedinyat-pamyat-i-gpu-pk-cherez-usb4-dlya-lok/">Windows 11 научили объединять память и GPU ПК через...</a></li>
<li><a href="https://www.cozumpark.com/windows-11e-usb4-rdma-destegi-geliyor-birden-fazla-bilgisayarin-gucu-birlesecek/">Windows 11'e USB 4 RDMA Desteği Geliyor: Birden... - ÇözümPark</a></li>

</ul>
</details>

**标签**: `#RDMA`, `#USB4`, `#local AI`, `#distributed computing`, `#Windows`

---

<a id="item-5"></a>
## [口服 RAS(ON)抑制剂 daraxonrasib 一线治疗胰腺癌缓解率达 60.7%](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 8.0/10

11 月 20 日，在 EORTC-NCI-AACR（ENA 2026）大会上，研究者以 late-breaking 口头报告形式公布了 daraxonrasib（一种口服 RAS(ON)多选择性抑制剂）联合吉西他滨/白蛋白紫杉醇一线治疗 61 例既往未治疗的转移性胰腺导管腺癌患者的 I/II 期试验数据。该方案确认的客观缓解率为 60.7%，完全缓解率为 8.2%（约十二分之一），疾病控制率为 90.2%，中位无进展生存期为 12.8 个月，12 个月总生存率为 76.6%，中位随访时间为 18.3 个月。 转移性胰腺癌是最致命的癌症之一，标准化疗的历史 1 年生存率仅为 22%–48%，因此一种一线口服靶向方案显示出如此高的活性可能代表着重大的治疗进展。如果在正在进行的 III 期试验中得到证实，daraxonrasib 联合治疗可能成为 RAS 突变胰腺癌患者的新标准治疗。 该结果来自一项单臂 I/II 期研究，没有化疗对照组，主要研究者强调疗效对比需等待正在进行的 III 期试验。Daraxonrasib 是一种口服 RAS(ON)多选择性抑制剂，作用于 RAS 的活性 GTP 结合状态，覆盖多种 KRAS/NRAS 突变，而非单一的 G12C 靶向药；该药已于 8 月 26 日获 FDA 批准（商品名 RASONQUE）用于既往治疗后的患者，依据是 III 期 RMC-302 试验，其中位总生存期为 13.2 个月对 6.7 个月。

telegram · zaihuapd · Nov 21, 11:24

**背景**: 胰腺导管腺癌（PDAC）在大多数病例中由 RAS 家族基因（尤其是 KRAS）突变驱动，这些突变促进细胞不受控制地生长。传统的 RAS 抑制剂靶向失活（OFF）状态，在 PDAC 中效果有限；daraxonrasib 属于更新的一类 RAS(ON)抑制剂，结合蛋白的活性状态，设计上对依赖活跃 RAS 信号的肿瘤更有效。目前转移性胰腺癌的一线标准化疗包括吉西他滨联合白蛋白紫杉醇（MPACT 方案）或 mFOLFIRINOX，两者带来的生存获益均有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.drugs.com/rasonque.html">Rasonque ( daraxonrasib ): Uses, Dosage, Side Effects</a></li>
<li><a href="https://www.onclive.com/view/daraxonrasib-monotherapy-elicits-meaningful-responses-in-previously-treated-ras-mutated-pancreatic-cancer">Daraxonrasib Monotherapy Elicits Meaningful Responses in... | OncLive</a></li>
<li><a href="https://www.cancer.gov/types/pancreatic/research/nab-paclitaxel-gemcitabine">Nab - Paclitaxel Plus Gemcitabine for Metastatic Pancreatic Cancer</a></li>

</ul>
</details>

**标签**: `#pancreatic cancer`, `#oncology`, `#RAS inhibitor`, `#clinical trial`, `#targeted therapy`

---