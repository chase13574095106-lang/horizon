---
layout: default
title: "Horizon Summary: 2026-05-31 (EN)"
date: 2026-05-31
lang: en
---

> From 22 items, 5 important content pieces were selected

---

1. [Cloudflare Turnstile Now Requires WebGL Fingerprinting](#item-1) ⭐️ 8.0/10
2. [Dav2d: First Open-Source AV2 Decoder Released](#item-2) ⭐️ 8.0/10
3. [Deep Dive into Linux's rseq() Syscall for Lock-Free Concurrency](#item-3) ⭐️ 8.0/10
4. [AI Coding Assistants: Productivity Boon or ADHD Amplifier?](#item-4) ⭐️ 8.0/10
5. [FROST Attack Uses SSD Timing to Spy on Users](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Turnstile Now Requires WebGL Fingerprinting](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 8.0/10

Cloudflare Turnstile has started requiring WebGL fingerprinting to pass its bot detection, breaking access for some browsers and raising privacy concerns. This change forces users to expose detailed GPU and driver information, undermining privacy protections and potentially locking out privacy-focused browsers. WebGL fingerprinting creates a unique identifier from a device's graphics hardware and driver, which can be used for tracking even across different browsers on the same device.

hackernews · HypnoticOcelot · May 31, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48345840)

**Background**: Cloudflare Turnstile is a privacy-preserving alternative to CAPTCHA that uses browser challenges to verify users. WebGL fingerprinting is a technique that extracts rendering characteristics from a device's GPU to generate a unique fingerprint, often used for tracking without cookies.

<details><summary>References</summary>
<ul>
<li><a href="https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting">Cloudflare Turnstile requiring fingerprintable WebGL - lanodan's cyber-home</a></li>
<li><a href="https://news.ycombinator.com/item?id=48345840">Cloudflare Turnstile requiring fingerprintable WebGL | Hacker News</a></li>
<li><a href="https://multilogin.com/glossary/webgl-fingerprint/">What is WebGL Fingerprint ? - Multilogin</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some defended fingerprinting as necessary for bot detection, while others criticized the privacy invasion and noted that minority browsers are breaking. A browser maintainer reported user complaints, and one commenter warned this could lead to a walled-garden internet.

**Tags**: `#privacy`, `#fingerprinting`, `#cloudflare`, `#webgl`, `#browser`

---

<a id="item-2"></a>
## [Dav2d: First Open-Source AV2 Decoder Released](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

VideoLAN has released dav2d, the first open-source CPU-based decoder for the AV2 video codec, which was finalized on May 28, 2026. AV2 decoding is roughly five times more complex than AV1, raising concerns that current hardware may struggle with software decoding, potentially making existing devices obsolete without hardware support. Dav2d is cross-platform and prioritizes decoding correctness, with performance optimizations planned for x86, ARM, and RISC-V architectures. The AV2 codec offers about 25-30% bitrate reduction over AV1 at similar quality.

hackernews · captain_bender · May 31, 11:44 · [Discussion](https://news.ycombinator.com/item?id=48344961)

**Background**: AV2 is the successor to AV1, developed by the Alliance for Open Media as a royalty-free video codec. It aims to compete with the royalty-based VVC (H.266) standard. The dav2d decoder follows the tradition of dav1d, VideoLAN's popular open-source AV1 decoder.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(codec)">AV2 (codec)</a></li>
<li><a href="https://www.phoronix.com/news/Dav2d-Open-Source-AV2-Decode">VideoLAN Publishes Dav2d For Open-Source AV2 Decoder - Phoronix</a></li>
<li><a href="https://videocardz.com/newz/videolan-publishes-dav2d-an-early-cpu-decoder-for-av2-video-codec">VideoLAN publishes dav2d, an early CPU decoder for AV2 video codec - VideoCardz.com</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about hardware obsolescence, with one user noting that a 25% size reduction may not justify making devices with AV1 hardware decoders obsolete. Others express interest in seeing AV2 decoding benchmarks, as AV1 software decoding is already intensive.

**Tags**: `#AV2`, `#video codec`, `#open-source`, `#decoder`, `#performance`

---

<a id="item-3"></a>
## [Deep Dive into Linux's rseq() Syscall for Lock-Free Concurrency](https://justine.lol/rseq/) ⭐️ 8.0/10

The article explains Linux's rseq() syscall for restartable sequences, which allows user-space threads to access per-CPU data structures without mutexes or atomic operations, by marking critical sections that the kernel can restart if preempted. This technique significantly improves performance for concurrent data structures on multi-core systems, reducing overhead compared to traditional locking or atomic operations, and is already used in glibc and other libraries. The rseq() syscall was merged into Linux kernel 4.18 in 2018 after a five-year development effort. Each thread can register only one rseq structure with the kernel to avoid scheduler overhead.

hackernews · grappler · May 31, 14:38 · [Discussion](https://news.ycombinator.com/item?id=48346019)

**Background**: Restartable sequences (rseq) are a kernel-user-space interface that allows user-space threads to safely access per-CPU data without locks. The kernel ensures atomicity by restarting the sequence if the thread is preempted or migrates to another CPU. This concept was originally proposed by Paul Turner and Andrew Hunter in 2013.

<details><summary>References</summary>
<ul>
<li><a href="https://www.efficios.com/blog/2019/02/08/linux-restartable-sequences/">The 5-year journey to bring restartable sequences to Linux - EfficiOS</a></li>
<li><a href="https://lwn.net/Articles/883104/">Restartable sequences in glibc [LWN.net]</a></li>
<li><a href="https://www.tutorialpedia.org/blog/what-are-rseqs-restartable-sequences-and-how-to-use-them/">What Are RSEQs ( Restartable Sequences )? — tutorialpedia.org</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated the explanation but noted missing references to the librseq library and criticized the article's tone about expensive hardware. Some pointed out that the technique is decades old in operating systems.

**Tags**: `#Linux`, `#concurrency`, `#kernel`, `#systems programming`, `#lock-free`

---

<a id="item-4"></a>
## [AI Coding Assistants: Productivity Boon or ADHD Amplifier?](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything) ⭐️ 8.0/10

David Wilson and Simon Willison reflect on how AI coding agents can lead to abandoned projects and wasted time, likening them to a 'thermonuclear ADHD amplifier,' and consider canceling subscriptions as a solution. This critique highlights a growing concern among developers that AI tools, while powerful, may harm focus and productivity, sparking debate about responsible use and the need for discipline. Wilson lists over 16 projects started with AI but quickly abandoned, noting that the technology provides cheap rewards with minimal input, making it a liability. Willison adds that even solid code can be instantly abandoned, questioning its value.

rss · Simon Willison · May 31, 16:31

**Background**: AI coding assistants like Claude and GitHub Copilot can generate entire projects from a single prompt, dramatically reducing development time. However, this ease of creation can lead to a proliferation of half-finished projects, especially for individuals prone to distraction or hyperfocus.

**Discussion**: On Hacker News, many commenters with ADHD reported the opposite effect: AI helps them achieve focus and finish side projects for the first time. Some described feeling more engaged and productive, with a sense of having a support team.

**Tags**: `#AI`, `#productivity`, `#ADHD`, `#developer experience`, `#critical analysis`

---

<a id="item-5"></a>
## [FROST Attack Uses SSD Timing to Spy on Users](https://futurism.com/future-society/websites-spying-solid-state-drive) ⭐️ 8.0/10

Researchers disclosed FROST, a zero-interaction side-channel attack that uses the browser's Origin Private File System (OPFS) and SSD read/write timing to infer which websites or applications a user is running, achieving 88.95% accuracy for websites and 95.83% for applications. This attack represents a new privacy threat because it requires no user interaction or software installation, and it exploits a standard browser API (OPFS) that is available on major operating systems, potentially allowing any malicious website to spy on user activity. The attack was tested only on macOS and Linux, but researchers believe Windows is not immune; closing browser tabs after use can reduce risk. FROST stands for Fingerprinting Remotely using OPFS-based SSD Timing.

telegram · zaihuapd · May 31, 01:55

**Background**: A side-channel attack exploits unintended information leakage from a system, such as timing variations. The Origin Private File System (OPFS) is a browser API that allows web applications to store files locally, but its I/O operations can be timed by a malicious website to infer other processes competing for the same SSD resource.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/">Websites have a new way to spy on visitors: Analyzing their SSD activity</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/05/29/website-tracking-ssd-activity-research/">Websites can spy on user activity by analyzing SSD ... - Help Net Security</a></li>
<li><a href="https://hannesweissteiner.com/pdfs/frost.pdf">FROST : Fingerprinting Remotely using</a></li>

</ul>
</details>

**Tags**: `#security`, `#side-channel attack`, `#SSD`, `#privacy`, `#browser`

---