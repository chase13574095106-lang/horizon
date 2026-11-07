---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 30 items, 5 important content pieces were selected

---

1. [PwnEscape Part 2: Practical Firecracker VM Escape Walkthrough](#item-1) ⭐️ 8.0/10
2. [AI is dramatically accelerating AI research, but is it real progress?](#item-2) ⭐️ 8.0/10
3. [Oracle cancels $7B AI chip lease deal with Tencent after US pressure](#item-3) ⭐️ 8.0/10
4. [Baidu Releases ERNIE 5.0: 2.4-Trillion-Parameter Omni-Modal MoE Model](#item-4) ⭐️ 8.0/10
5. [YMTC's new Wuhan fab targets up to 70% domestic equipment](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PwnEscape Part 2: Practical Firecracker VM Escape Walkthrough](https://pwn.ai/blog/firecracker-escape) ⭐️ 8.0/10

PWN.AI published a detailed practical walkthrough (Part 2) showing how a malicious guest can exploit the PwnEscape Linux kernel networking vulnerability to cross Firecracker's microVM boundary, resolve the live VMM from inside the VM, and take control of a root-run host process. The writeup demonstrates a guest-to-host code-execution primitive, but notes the tested configuration did not use Firecracker's jailer. Firecracker underpins AWS Lambda and many multi-tenant serverless and container platforms, so a demonstrated guest-to-host escape raises serious questions about isolation assumptions in production. The writeup and discussion highlight that real-world exposure depends heavily on whether deployments use the jailer, namespaces, and seccomp, and it has renewed debate over microhypervisor alternatives. The exploit chains a Linux networking flaw (tracked as CVE-2026-99999 and nicknamed PwnEscape) into a guest-to-host primitive, but the tested setup lacked Firecracker's production containment: privilege dropping, namespaces, and seccomp filters. The authors caution that a properly jailed deployment requires a separate assessment of what privileges and resources remain available after VMM compromise.

hackernews · SerCe · Nov 6, 19:33 · [Discussion](https://news.ycombinator.com/item?id=50397219)

**Background**: Firecracker is a lightweight microVM hypervisor written in Rust, designed for fast, secure isolation of short-lived workloads and used as the backbone of AWS Lambda. Its production hardening relies on the jailer, a companion binary that drops privileges and confines the Firecracker process using namespaces and seccomp. PwnEscape is a critical Linux kernel networking vulnerability that lets code inside a guest VM read host memory, effectively erasing the guest-host boundary when unpatched.

<details><summary>References</summary>
<ul>
<li><a href="https://pwn.ai/blog/firecracker-escape">Firecracker VM Escape: PwnEscape Part 2. | PWN.AI Security ...</a></li>
<li><a href="https://cybernews.com/security/critical-linux-bug-pwnescape-allows-vm-escape/">PwnEscape Linux Vulnerability Lets VM Guests Escape to Hosts ...</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md">firecracker/docs/jailer.md at main · firecracker-microvm ...</a></li>

</ul>
</details>

**Discussion**: Commenters pushed back on the writeup's framing: one noted the tested configuration had no jailer and asked for more analysis of properly jailed deployments, while another stressed the exploit is not a new vulnerability but a practical exploitation guide for a previously disclosed flaw. Others argued for formally verified microhypervisor designs like Nova, and one operator of a Firecracker-based database playground (ClickBench) offered to host a proof-of-concept escape.

**Tags**: `#virtualization`, `#security`, `#firecracker`, `#exploitation`, `#hypervisor`

---

<a id="item-2"></a>
## [AI is dramatically accelerating AI research, but is it real progress?](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) ⭐️ 8.0/10

An article argues that AI is dramatically accelerating AI research, sparking a Hacker News discussion with 193 points and 148 comments that questions whether the observed gains reflect genuine progress or are merely benchmark overfitting and compute scaling. This debate is central to the AI industry because if AI is truly accelerating AI research, it could lead to recursive self-improvement and rapid capability gains; if not, it may signal diminishing returns and inflated expectations. Commenters highlight that benchmarks are curated and can be trained on, that much of the perceived acceleration may come from capital and compute scaling rather than model intelligence, and that training speed on trillions of tokens remains a fundamental bottleneck.

hackernews · yurivish · Nov 6, 20:27 · [Discussion](https://news.ycombinator.com/item?id=50397994)

**Background**: AI research often uses benchmarks to measure progress, but models can overfit to these benchmarks, making performance gains appear larger than real-world improvements. Scaling laws describe how model performance improves with more data, compute, and parameters, and recursive self-improvement refers to AI systems improving their own capabilities, potentially leading to rapid acceleration.

<details><summary>References</summary>
<ul>
<li><a href="https://nhimg.org/glossary/benchmark-overfitting/">What Is Benchmark Overfitting ? Definition & Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">Our progress toward recursive self - improvement , and its implications.</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is largely skeptical, with commenters arguing that benchmarks are gamed, that gains may stem from capital and compute scaling rather than smarter models, and that training speed remains a bottleneck; some also note that AI accelerates work but may not change the world faster overall.

**Tags**: `#AI research`, `#benchmarking`, `#scaling laws`, `#AI acceleration`, `#community discussion`

---

<a id="item-3"></a>
## [Oracle cancels $7B AI chip lease deal with Tencent after US pressure](https://t.me/zaihuapd/44958) ⭐️ 8.0/10

Oracle has canceled a five-year, roughly $7 billion AI chip leasing agreement with Tencent after US officials raised national security concerns with the company. The deal would have given Tencent access to about 100,000 advanced AI chips through Oracle data centers in Southeast Asia, with a down payment of roughly 30%. The cancellation signals that US export controls are increasingly being applied to cloud-based access to advanced AI chips, not just direct hardware sales, which could complicate overseas compute strategies for Chinese AI firms. It also highlights how geopolitical tensions are reshaping AI infrastructure supply chains and could deter similar cross-border leasing arrangements. The five-year lease was signed earlier this year and was intended to let Tencent use chips that are unavailable in China via multiple Oracle data centers in Southeast Asia. Tencent had reportedly made a down payment of about 30%, and the deal was valued at approximately $7 billion.

telegram · zaihuapd · Nov 6, 05:02

**Background**: The US has progressively tightened export controls on advanced semiconductors to China since 2018, aiming to restrict Chinese access to cutting-edge AI chips and related computing capabilities. In response, Chinese tech companies have sought workarounds such as leasing compute capacity in overseas data centers, which US lawmakers have been weighing how to address. Oracle is a major US cloud and data center provider with infrastructure in Southeast Asia, making it a potential conduit for such arrangements.

<details><summary>References</summary>
<ul>
<li><a href="https://aidirectory.com/news/tencent-leases-100000-ai-chips-from-oracle-southeast-asia">Tencent leases 100,000 AI chips from Oracle in south-east Asia</a></li>
<li><a href="https://www.congress.gov/crs_external_products/R/PDF/R48642/R48642.5.pdf">U.S. Export Controls and China: Advanced Semiconductors</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#US-China tech`, `#Oracle`, `#Tencent`, `#export controls`

---

<a id="item-4"></a>
## [Baidu Releases ERNIE 5.0: 2.4-Trillion-Parameter Omni-Modal MoE Model](https://t.me/zaihuapd/44959) ⭐️ 8.0/10

Baidu officially released ERNIE 5.0, a 2.4-trillion-parameter omni-modal large model that uses unified modeling to process text, images, audio, and video simultaneously. The company claims it outperforms international top models like Gemini-2.5-Pro and GPT-5-High on over 40 authoritative benchmarks, and it adopts a Mixture-of-Experts architecture with less than 3% activated parameters. This is a flagship release from a major Chinese AI player, signaling that domestic models are aiming to compete directly with the world's leading frontier systems on both scale and multimodal capabilities. If the benchmark claims hold up, it could shift perceptions of China's AI competitiveness and intensify the global race toward ever-larger omni-modal models. The model uses a Mixture-of-Experts design with under 3% of its 2.4 trillion parameters active per inference, which boosts efficiency while maintaining capability. Baidu also involved 835 experts from technology, finance, culture, and education to guide and calibrate the model, and it is now available to individual users via the ERNIE platform.

telegram · zaihuapd · Nov 6, 05:41

**Background**: Omni-modal models are designed to understand and generate content across multiple modalities—text, images, audio, and video—within a single unified architecture, unlike earlier models that handled each modality separately. Mixture-of-Experts (MoE) is a technique that scales up total parameter count while only activating a small subset of 'expert' sub-networks for each input token, enabling large models to run more efficiently. Activated parameters refer to the portion of the model actually used during inference, which is typically much smaller than the total in MoE architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters : What’s the Difference?</a></li>
<li><a href="https://www.marktechpost.com/2025/11/17/uni-moe-2-0-omni-an-open-qwen2-5-7b-based-omnimodal-moe-for-text-image-audio-and-video-understanding/">Uni-MoE-2.0- Omni : An Open Qwen2.5-7B Based... - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Baidu`, `#ERNIE`, `#MoE`, `#multimodal`

---

<a id="item-5"></a>
## [YMTC's new Wuhan fab targets up to 70% domestic equipment](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 8.0/10

Yangtze Memory Technologies (YMTC) plans to build a fourth fab in Wuhan, scheduled to break ground in 2027, aiming to raise its domestic equipment procurement ratio to at least 60% and as high as 70%, up from over 50% at its third fab. The new facility will produce advanced NAND flash with more than 300 layers, primarily for data center and AI storage demand. This marks one of the highest domestic equipment ratios attempted by a leading Chinese memory maker, signaling a significant shift in China's semiconductor supply chain under US export controls. YMTC's domestic NAND market share has already risen to 38.5%, surpassing Samsung, and full ramp-up of three new fabs could double its overall capacity, strengthening China's position in AI storage infrastructure. Cleaning, polishing, and etching equipment are expected to be the main areas of incremental domestic sourcing, while advanced tools such as lithography and inspection equipment still rely on overseas suppliers. The 300+ layer NAND targets data center and AI storage, and the plan follows YMTC's third fab, which already sources over 50% of equipment domestically.

telegram · zaihuapd · Nov 6, 08:34

**Background**: YMTC is a Chinese NAND flash manufacturer founded in Wuhan in 2016 with government investment, aiming to reduce China's dependence on foreign chips. NAND flash is non-volatile memory used in SSDs and data centers, and stacking more layers (300+) increases storage density. US export controls on advanced semiconductor equipment have pushed Chinese chipmakers to localize their supply chains, with domestic equipment rates varying by category—CMP and thinning tools have progressed fastest.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.eetimes.com/ymtc-nand-design-surprise-alongside-a-new-fab/">YMTC NAND Design Surprise Alongside a New Fab- EE Times</a></li>
<li><a href="https://www.csis.org/analysis/true-impact-allied-export-controls-us-and-chinese-semiconductor-manufacturing-equipment">The True Impact of Allied Export Controls on the U . S . and Chinese ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#NAND flash`, `#YMTC`, `#supply chain localization`, `#AI storage`

---