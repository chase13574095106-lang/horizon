---
layout: default
title: "Horizon Summary: 2026-05-31 (ZH)"
date: 2026-05-31
lang: zh
---

> From 22 items, 5 important content pieces were selected

---

1. [Cloudflare Turnstile 现在要求 WebGL 指纹识别](#item-1) ⭐️ 8.0/10
2. [Dav2d：首个开源 AV2 解码器发布](#item-2) ⭐️ 8.0/10
3. [深入解析 Linux 的 rseq()系统调用：无锁并发](#item-3) ⭐️ 8.0/10
4. [AI 编程助手：生产力福音还是多动症放大器？](#item-4) ⭐️ 8.0/10
5. [FROST 攻击利用 SSD 计时窥探用户](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Turnstile 现在要求 WebGL 指纹识别](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 8.0/10

Cloudflare Turnstile 开始要求 WebGL 指纹识别才能通过其机器人检测，导致部分浏览器无法访问并引发隐私担忧。 这一变化迫使用户暴露详细的 GPU 和驱动程序信息，削弱了隐私保护，并可能屏蔽注重隐私的浏览器。 WebGL 指纹识别通过设备的图形硬件和驱动程序创建唯一标识符，可用于跨浏览器追踪同一设备。

hackernews · HypnoticOcelot · May 31, 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48345840)

**背景**: Cloudflare Turnstile 是一种隐私保护的 CAPTCHA 替代方案，通过浏览器挑战来验证用户。WebGL 指纹识别是一种从设备 GPU 提取渲染特征以生成唯一指纹的技术，常用于无 Cookie 追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting">Cloudflare Turnstile requiring fingerprintable WebGL - lanodan's cyber-home</a></li>
<li><a href="https://news.ycombinator.com/item?id=48345840">Cloudflare Turnstile requiring fingerprintable WebGL | Hacker News</a></li>
<li><a href="https://multilogin.com/glossary/webgl-fingerprint/">What is WebGL Fingerprint ? - Multilogin</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人为指纹识别作为机器人检测的必要手段辩护，也有人批评其侵犯隐私，并指出小众浏览器因此无法使用。一位浏览器维护者报告了用户投诉，还有评论者警告这可能导致互联网变成围墙花园。

**标签**: `#privacy`, `#fingerprinting`, `#cloudflare`, `#webgl`, `#browser`

---

<a id="item-2"></a>
## [Dav2d：首个开源 AV2 解码器发布](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

VideoLAN 发布了 dav2d，这是针对 AV2 视频编码标准的首个基于 CPU 的开源解码器，AV2 标准于 2026 年 5 月 28 日最终确定。 AV2 解码的复杂度大约是 AV1 的五倍，这引发担忧：当前硬件可能难以进行软件解码，若无硬件支持，现有设备可能面临淘汰。 Dav2d 是跨平台的，优先保证解码正确性，并计划针对 x86、ARM 和 RISC-V 架构进行性能优化。AV2 编码标准在同等质量下相比 AV1 可降低约 25-30%的码率。

hackernews · captain_bender · May 31, 11:44 · [社区讨论](https://news.ycombinator.com/item?id=48344961)

**背景**: AV2 是 AV1 的继任者，由开放媒体联盟（AOM）开发，是一种免版税的视频编码标准，旨在与收费的 VVC（H.266）标准竞争。dav2d 解码器延续了 VideoLAN 广受欢迎的开源 AV1 解码器 dav1d 的传统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(codec)">AV2 (codec)</a></li>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder - Phoronix</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video codec - VideoCardz.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有用户指出 25%的体积缩减可能不足以让配备 AV1 硬件解码器的设备被淘汰，引发对硬件过时的担忧。其他人则对 AV2 解码基准测试表示兴趣，因为 AV1 的软件解码已经相当耗费资源。

**标签**: `#AV2`, `#video codec`, `#open-source`, `#decoder`, `#performance`

---

<a id="item-3"></a>
## [深入解析 Linux 的 rseq()系统调用：无锁并发](https://justine.lol/rseq/) ⭐️ 8.0/10

文章解释了 Linux 的 rseq()系统调用，它允许用户态线程通过标记临界区（内核可在被抢占时重启这些区域）来访问每 CPU 数据结构，无需互斥锁或原子操作。 该技术显著提升了多核系统上并发数据结构的性能，相比传统锁或原子操作降低了开销，并已用于 glibc 等库中。 rseq()系统调用经过五年开发后于 2018 年合入 Linux 内核 4.18。每个线程只能向内核注册一个 rseq 结构，以避免调度器开销。

hackernews · grappler · May 31, 14:38 · [社区讨论](https://news.ycombinator.com/item?id=48346019)

**背景**: 可重启序列（rseq）是一种内核-用户空间接口，允许用户态线程无锁安全地访问每 CPU 数据。如果线程被抢占或迁移到其他 CPU，内核会重启该序列以保证原子性。该概念最初由 Paul Turner 和 Andrew Hunter 于 2013 年提出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/">The 5-year journey to bring restartable sequences to Linux - EfficiOS</a></li>
<li><a href="https://lwn.net/Articles/883104/">Restartable sequences in glibc [LWN.net]</a></li>
<li><a href="https://www.tutorialpedia.org/blog/what-are-rseqs-restartable-sequences-and-how-to-use-them/">What Are RSEQs ( Restartable Sequences )? — tutorialpedia.org</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏文章的解释，但指出缺少对 librseq 库的引用，并批评了文章关于昂贵硬件的语气。一些人指出该技术在操作系统中已有数十年历史。

**标签**: `#Linux`, `#concurrency`, `#kernel`, `#systems programming`, `#lock-free`

---

<a id="item-4"></a>
## [AI 编程助手：生产力福音还是多动症放大器？](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything) ⭐️ 8.0/10

David Wilson 和 Simon Willison 反思了 AI 编程代理如何导致项目被遗弃和时间浪费，将其比作‘热核级多动症放大器’，并考虑取消订阅作为解决方案。 这一批评凸显了开发者日益增长的担忧：AI 工具虽然强大，但可能损害专注力和生产力，引发了关于负责任使用和自律必要性的讨论。 Wilson 列出了超过 16 个用 AI 启动但很快被遗弃的项目，指出该技术以最小投入提供廉价回报，使其成为一种负担。Willison 补充说，即使是可靠的代码也可能被立即抛弃，质疑其价值。

rss · Simon Willison · May 31, 16:31

**背景**: 像 Claude 和 GitHub Copilot 这样的 AI 编程助手可以从单个提示生成整个项目，大幅缩短开发时间。然而，这种易创建性可能导致大量半成品项目泛滥，尤其是对于容易分心或过度专注的人。

**社区讨论**: 在 Hacker News 上，许多患有多动症的评论者报告了相反的效果：AI 帮助他们集中注意力并首次完成副项目。一些人描述感到更投入、更高效，仿佛拥有了一个支持团队。

**标签**: `#AI`, `#productivity`, `#ADHD`, `#developer experience`, `#critical analysis`

---

<a id="item-5"></a>
## [FROST 攻击利用 SSD 计时窥探用户](https://futurism.com/future-society/websites-spying-solid-state-drive) ⭐️ 8.0/10

研究人员披露了一种名为 FROST 的无交互侧信道攻击，利用浏览器的源私有文件系统（OPFS）和 SSD 读写计时来推断用户正在访问的网站或使用的应用，对网站的预测准确率达 88.95%，对应用的预测准确率达 95.83%。 该攻击代表了一种新的隐私威胁，因为它无需用户交互或安装软件，并且利用了主流操作系统上可用的标准浏览器 API（OPFS），可能允许任何恶意网站窥探用户活动。 该攻击仅在 macOS 和 Linux 上进行了测试，但研究人员认为 Windows 并非免疫；使用后及时关闭浏览器标签页可降低风险。FROST 全称为基于 OPFS 的 SSD 计时远程指纹识别。

telegram · zaihuapd · May 31, 01:55

**背景**: 侧信道攻击利用系统无意中泄露的信息，例如时间差异。源私有文件系统（OPFS）是一种浏览器 API，允许 Web 应用在本地存储文件，但恶意网站可以通过计时其 I/O 操作来推断其他竞争同一 SSD 资源的进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/">Websites have a new way to spy on visitors: Analyzing their SSD activity</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/05/29/website-tracking-ssd-activity-research/">Websites can spy on user activity by analyzing SSD ... - Help Net Security</a></li>
<li><a href="https://hannesweissteiner.com/pdfs/frost.pdf">FROST : Fingerprinting Remotely using</a></li>

</ul>
</details>

**标签**: `#security`, `#side-channel attack`, `#SSD`, `#privacy`, `#browser`

---