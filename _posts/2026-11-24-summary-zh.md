---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> From 33 items, 9 important content pieces were selected

---

1. [黎曼猜想据称通过 Lean 形式化验证](#item-1) ⭐️ 10.0/10
2. [英伟达在美国政府介入后重新任命黄仁勋为 CEO](#item-2) ⭐️ 9.0/10
3. [Ladybird 浏览器引擎进入 alpha 阶段](#item-3) ⭐️ 9.0/10
4. [Anthropic 形式数学库证明 VP ≠ VNP 在所有域上成立](#item-4) ⭐️ 9.0/10
5. [智谱 AI 发布 GLM-5.4，首款面向泛编程的循环 Transformer 模型](#item-5) ⭐️ 8.0/10
6. [Z.ai 发布 GLM-5.4，其首个循环 Transformer 模型](#item-6) ⭐️ 8.0/10
7. [Ladybird 浏览器发布首个 macOS 和 Linux 的 alpha 版本](#item-7) ⭐️ 8.0/10
8. [Codex2api 作者账号被黑，遭供应链投毒](#item-8) ⭐️ 8.0/10
9. [Meta AI 负责人警告超级智能临近，控制权堪忧](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [黎曼猜想据称通过 Lean 形式化验证](https://t.me/zaihuapd/45324) ⭐️ 10.0/10

据报道，2026 年 11 月 20 日 Levent Alpöge 发布了黎曼猜想的 Lean 形式化证明，代码库约 1700 万行；11 月 21 日，Lean FRO 与 Mathlib Initiative 联合声明认证该命题与证明均正确。 若得到确认，这将是数学史上的重大突破，也是在超大规模上展示形式化验证能力的里程碑事件，可能改变数学界验证和信任重大定理的方式。 据称社区确认其命题与 Mathlib 的 RiemannHypothesis 一致、代码库可无错编译，并且多个独立证明检查器验证了证明有效；不过 2026 年的日期和 1700 万行的规模都不同寻常，需保持谨慎。

telegram · zaihuapd · Nov 24, 01:29

**背景**: 黎曼猜想是数学中最著名的未解问题之一，它猜测黎曼 ζ 函数的所有非平凡零点的实部均为 1/2。Lean 是一个交互式定理证明器，允许数学家编写可由机器检查的形式化证明，而 Mathlib 是其由社区维护的大型形式化数学库。对重大定理进行形式化验证意味着每一步逻辑都由软件检查，从而提供极高的正确性保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leanprover.github.io/theorem_proving_in_lean/introduction.html">1. Introduction — Theorem Proving in Lean 3 (outdated)...</a></li>
<li><a href="https://leandojo.org/">AI-Driven Formal Theorem Proving in the Lean Ecosystem</a></li>

</ul>
</details>

**标签**: `#Riemann Hypothesis`, `#Lean`, `#formal verification`, `#mathematics`, `#proof assistant`

---

<a id="item-2"></a>
## [英伟达在美国政府介入后重新任命黄仁勋为 CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 9.0/10

英伟达董事会一致决定重新任命黄仁勋为总裁、CEO 兼董事会成员，此时距其离职不到两周。董事会是在收到美国高级政府官员的输入后做出这一决定的，官员们认为黄仁勋的复职不构成国家安全风险。 这一反转引发了对公司治理以及政府对私营半导体公司影响力程度的严重质疑，尤其是在美中科技紧张和出口管制背景下。它可能为芯片行业中国家安全问题与高管问责如何交织树立先例。 董事会声明明确提到，基于美国高级政府层面的输入，董事会确信黄仁勋的复职不构成国家安全风险。该决定是一致通过的，与不久前罢免他的决定完全相反，而担任临时 CEO 的 Colette Kress 将回归 CFO 职位。

hackernews · jaz · Nov 23, 14:00 · [社区讨论](https://news.ycombinator.com/item?id=50611576)

**背景**: 黄仁勋于 1993 年联合创立英伟达，并在其大部分历史中担任 CEO，将其打造为 AI 和游戏用 GPU 的主导设计商。英伟达的芯片处于美中科技竞争的核心，出口管制限制了对华销售先进 AI 处理器。该公司董事会因独立性而受到审视，许多董事任职数十年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director">NVIDIA Board Reinstates Jensen Huang as President, CEO and ...</a></li>
<li><a href="https://www.cnn.com/2026/11/23/tech/nvidia-reinstates-jensen-huang-corporate-governance">Nvidia’s $1.5 trillion boardroom blunder - CNN</a></li>
<li><a href="https://observer.com/2026/11/nvidia-jensen-huang-corporate-governance-oversight/">Nvidia Reinstates Jensen Huang: The Governance Questions ...</a></li>

</ul>
</details>

**社区讨论**: 评论者关注董事会声明中明确依赖美国政府输入的关键部分，一些人指出特拉华州 Caremark 先例对董事会责任设定了高标准，司法部的立场可能免除个人责任。其他人批评这种虚伪：强迫 ASML 和日本芯片公司遵守制裁，而英伟达却得到白宫的“个人祝福”，并将此与 2023 年 OpenAI 事件相提并论，认为名义治理结构并不总是真实的治理结构。

**标签**: `#Nvidia`, `#corporate-governance`, `#geopolitics`, `#semiconductors`, `#US-China-tech-policy`

---

<a id="item-3"></a>
## [Ladybird 浏览器引擎进入 alpha 阶段](https://ladybird.org/posts/alpha/) ⭐️ 9.0/10

从零开始构建的独立浏览器引擎 Ladybird 已正式进入 alpha 阶段，标志着该项目的一个重要里程碑。 这具有重要意义，因为它为 Chromium 主导的浏览器格局提供了一个真正独立的替代品，可能促进网络标准和隐私方面的竞争与创新。 该 alpha 版本仍处于面向开发者的 pre-alpha 质量阶段，但早期测试者报告了令人惊讶的良好渲染兼容性，不过也注意到了一些轻微的性能问题，如滚动卡顿。

hackernews · janvdberg · Nov 23, 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**背景**: Ladybird 是一个从零开始编写的新浏览器引擎，不基于 Chromium 或 Gecko，最初作为 SerenityOS 项目的一部分开发。Alpha 版本是软件测试的早期阶段，软件功能可用但不完整，旨在收集开发者和早期采用者的反馈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/LadybirdBrowser/ladybird">GitHub - LadybirdBrowser/ ladybird : Truly independent web browser</a></li>
<li><a href="https://blog.openreplay.com/ladybird-non-chromium-browser/">Exploring Ladybird , the Non-Chromium Browser Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_release_life_cycle">Software release life cycle - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对此印象深刻，用户报告许多网站渲染正确，甚至像 ProxMox 这样的复杂网络应用也能良好运行。一些人表达了对原始黑客精神的怀念，并希望 Ladybird 能认真解决指纹识别和隐私问题。

**标签**: `#browser`, `#ladybird`, `#open-source`, `#web-engines`, `#alpha-release`

---

<a id="item-4"></a>
## [Anthropic 形式数学库证明 VP ≠ VNP 在所有域上成立](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 9.0/10

Anthropic 的形式数学库中包含一篇 70 页的论文《VP ≠ VNP over every field》，声称在所有域上严格分离代数复杂性类 VP 和 VNP，部分工作由 AI 生成并在 Lean 中形式化。 这是复杂性理论的一个重大里程碑，因为 VP 与 VNP 是著名 P vs NP 问题的代数类比，该结果展示了 AI 在辅助高级数学定理证明方面的能力日益增强，可能重塑该领域的研究方式。 该论文混合了人类撰写和 AI 生成的文本，作者指出他们尚未分析该结果与相对化和代数化障碍的关系，而这些是复杂性理论中的关键障碍。

hackernews · mikeryan52 · Nov 23, 22:09 · [社区讨论](https://news.ycombinator.com/item?id=50620102)

**背景**: VP 和 VNP 是类似于 P 和 NP 的代数复杂性类：VP 包含具有多项式大小算术电路的多项式，而 VNP 是 NP 的代数类比。证明 VP ≠ VNP 是代数复杂性理论中的一个主要开放问题，常被视为通向 P vs NP 的垫脚石。Lean 是一种定理证明器和函数式编程语言，用于形式化数学和验证证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity">Arithmetic circuit complexity - Wikipedia</a></li>
<li><a href="https://lean-lang.org/learn/">Learn — Lean Lang</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/claude-proves-vp-not-vnp-valiant-conjecture">Claude claims to prove VP ≠ VNP in Valiant's 47-year-old ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（262 条评论）展现了敬畏与焦虑的混合情绪：一些人认为这是 Anthropic 在积极追求 P vs NP 的“圣杯”，另一些人担心人类数学家的未来，还有人注意到 AI 实验室之间的竞争动态。评论者也指出了诸如缺乏对相对化和代数化分析等注意事项。

**标签**: `#complexity-theory`, `#formal-verification`, `#Lean`, `#AI-for-math`, `#P-vs-NP`

---

<a id="item-5"></a>
## [智谱 AI 发布 GLM-5.4，首款面向泛编程的循环 Transformer 模型](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

智谱 AI 发布了 GLM-5.4，这是其首款采用循环 Transformer（Loop Transformer）架构的旗舰模型，旨在实现“泛编程”，将编程能力拓展到视频制作、游戏开发、3D 建模和机械设计等领域。该模型可通过 Z.ai 的 Coding Plan 获取，该计划提供的 API 密钥可访问新模型。 这标志着最先进大语言模型在架构上的一个显著转变，因为循环 Transformer 通过复用层来减少推理过程中的内存带宽瓶颈，有望实现更高效的扩展。此次发布也表明智谱致力于透明、开放的技术披露，与西方实验室更为封闭的做法形成对比。 据报道，GLM-5.4 的智能水平可与 2T-3T 参数模型相媲美，并新增了视觉理解能力，但用户指出访问该模型需要 Coding Plan 而非普通 API 计划。社区成员还提到，该模型的“马拉松式思考”会话会因过度自我检查而导致在简单任务上速度较慢。

hackernews · foohis · Nov 23, 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**背景**: 循环 Transformer（也称为循环深度 Transformer）是标准 Transformer 的一种变体，其中共享的层块会对相同的潜在表示进行多次迭代应用，而不是让 token 一次通过一叠独特的层。这种参数高效的设计可以减少每个 token 需要将整个层从内存移动到芯片的需求，从而解决内存带宽这一关键推理瓶颈。智谱 AI 是一家中国人工智能公司，以其 GLM 系列大语言模型而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM-5.4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://docs.bigmodel.cn/cn/guide/models/glm-5.4">GLM-5.4 - 智谱AI开放文档 - docs.bigmodel.cn</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了智谱的透明度和技术细节，其中一位指出循环 Transformer 尽管仍存在挑战，但是一个显而易见的方向。其他人则强调了实际问题：访问 GLM-5.4 需要切换到 Coding Plan，而且该模型的“马拉松式思考”会话因不断自我怀疑而导致在简单任务上比前沿模型更慢。

**标签**: `#LLM`, `#Transformer`, `#AI`, `#Model Release`, `#Coding`

---

<a id="item-6"></a>
## [Z.ai 发布 GLM-5.4，其首个循环 Transformer 模型](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 8.0/10

Z.ai 发布了 GLM-5.4，这是其首个采用循环 Transformer 架构的模型，该架构通过多次迭代复用权重共享层来加深推理能力，而不增加参数数量。此次发布紧随 Thinking Machines Lab 于 11 月 20 日推出另一款循环 Transformer 模型 Inkling 2 Mini 之后。 这是一周内第二次出现循环 Transformer 的发布，表明该架构正成为 LLM 设计中提升推理效率的一个显著趋势。作为中国主要 AI 实验室的旗舰模型，GLM-5.4 可能影响其他实验室在深度与参数扩展之间的取舍。 GLM-5.4 尚未开放权重，目前仅能通过 Z.ai 的 Coding Plan 订阅访问，但其位于 https://api.z.ai/api/v1 的 OpenAI 兼容 Responses API 可使用编码计划密钥。Z.ai 未发布该模型的任何基准测试结果，Simon Willison 的鹈鹕测试显示其输出质量与 GLM-5.3 相当，而非显著跃升。

rss · Simon Willison · Nov 23, 23:40

**背景**: 标准 Transformer 在前向传播中每层只运行一次，而循环 Transformer 会让一组权重共享层运行多次迭代，每次细化隐藏状态。这样在不增加参数的情况下获得了更深的有效网络，Thinking Machines Lab 的 Inkling 2 Mini 同样对每个 token 将中间层循环三次，以提升每个 token 的推理能力。Z.ai 的 GLM 系列是中国的 LLM 家族，已历经 5.1、5.2 和 5.3 版本，早期版本以独特的风格化输出著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM - 5 . 4 - Overview - Z . AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://kingy.ai/blog/glm-5-4-launch/">GLM ‑ 5 . 4 launch: How to use it, pricing and API status</a></li>

</ul>
</details>

**标签**: `#llm`, `#transformer-architecture`, `#glm`, `#ai-research`, `#model-release`

---

<a id="item-7"></a>
## [Ladybird 浏览器发布首个 macOS 和 Linux 的 alpha 版本](https://simonwillison.net/2026/Nov/23/ladybird/) ⭐️ 8.0/10

Ladybird 是一个拥有自主渲染引擎的独立浏览器项目，于 2026 年 11 月 23 日发布了首个 alpha 版本，macOS 和 Linux 用户无需自行编译即可安装。该 alpha 版本包含自研的 HTML 解析器、CSS 引擎、布局、JavaScript 和 WebAssembly 实现，但仍依赖 HarfBuzz、Skia、ffmpeg 和 SQLite 等外部库。 这是浏览器多样性方面的一个重要里程碑，因为 Ladybird 是少数从零开始构建而非基于 Chromium、Gecko 或 WebKit 分叉的新引擎之一，为占主导地位的浏览器引擎提供了潜在替代方案。其 alpha 版本使项目更易于被更广泛的用户群体使用，并可能推动开放 Web 标准的创新。 早期测试显示，Ladybird 可以运行基于 WebAssembly 的工具，如 ffmpeg 和 Pyodide，但由于缺少 `navigator.serviceWorker.startMessages` 函数，它在复杂的 service worker 和 web worker 组合（如 Datasette Lite）上会失败。该浏览器采用多进程架构，标签页在独立进程中运行，与其他现代浏览器类似。

rss · Simon Willison · Nov 23, 21:46

**背景**: Ladybird 是一个从零开始构建的新浏览器引擎，由非营利组织支持，并非 Chromium、Gecko 或 WebKit 等现有引擎的分叉。它起源于 SerenityOS 项目——一个包含自有浏览器的开源桌面操作系统，后来分离出来成为独立项目。此次 alpha 发布标志着用户首次无需自行编译即可安装该浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ladybird.org/">Ladybird is a truly independent web browser , backed by a non-profit.</a></li>
<li><a href="https://en.wikipedia.org/wiki/SerenityOS">SerenityOS - Wikipedia</a></li>
<li><a href="https://github.com/harfbuzz/harfbuzz">GitHub - harfbuzz / harfbuzz : HarfBuzz text shaping engine · GitHub</a></li>

</ul>
</details>

**标签**: `#browser`, `#open-source`, `#web-standards`, `#ladybird`, `#alpha-release`

---

<a id="item-8"></a>
## [Codex2api 作者账号被黑，遭供应链投毒](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

Codex2api 的作者账号遭到入侵，攻击者绕过 main 分支推送恶意 tag，构建出带后门的版本 v3.1.11，该版本移除了鉴权，导致无需密码即可远程执行命令。同时，一个 workflow 将仓库的 16 个 Actions secrets 外传，波及同一账号下至少 21 个仓库。 这是一起具体的供应链攻击事件，表明单个维护者账号被黑就可能在发布版本中植入后门并泄露多个项目的密钥，影响所有安装或更新该工具的用户。它凸显了开源生态中加强账号安全和发布完整性检查的必要性。 已安装或更新过 3.1.10–3.1.12 版本的用户应立即停用，回退到 3.1.9，并轮换所有相关密钥，包括 GitHub token、SSH key、数据库凭证和 DeepSeek API 密钥。攻击者通过直接推送 tag 绕过了 main 分支，触发了包含后门的发布构建。

telegram · zaihuapd · Nov 23, 11:21

**背景**: GitHub Actions 是一项 CI/CD 服务，运行仓库中定义的 workflow，通常可以访问仓库密钥。攻击者控制维护者账号后，可以推送恶意 tag 触发发布构建，从而在代码中植入后门，绕过常规分支保护。密钥外传是指 workflow 将 token 或密钥等敏感数据发送到外部服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/step-security/github-actions-goat/blob/main/docs/Vulnerabilities/ExfiltratingCICDSecrets.md">github - actions -goat/docs/Vulnerabilities/ExfiltratingCICDSecrets.md at...</a></li>
<li><a href="https://cyberreplay.com/blog/detecting-remediating-github-actions-secret-exfiltration/">Detecting and Remediating GitHub Actions Secret Exfiltration ...</a></li>
<li><a href="https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/">Disrupting supply chain attacks on npm and GitHub Actions</a></li>

</ul>
</details>

**标签**: `#supply-chain-attack`, `#security`, `#github-actions`, `#secrets-exposure`, `#incident-report`

---

<a id="item-9"></a>
## [Meta AI 负责人警告超级智能临近，控制权堪忧](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 8.0/10

Meta 首席 AI 官兼超级智能实验室负责人 Alexandr Wang 在 X 上发长文表示，超级智能已不再是遥远的未来议题。他以数学家 Levent Alpöge 借助 Anthropic 的 Claude 完成、并于周六经 Lean 与 Mathlib 社区机器校验的黎曼猜想证明为例，警告人类将难以控制可无限自我改进或智能达到人类 1000 倍的系统，并呼吁紧急投入安全、对齐与防护研究。 这一论断出自大型 AI 实验室的负责人，并将超级智能辩论与一个具体且备受关注的 AI 辅助数学发现案例联系起来，可能加速全行业对安全与对齐研究的呼吁。如果此类证明变得司空见惯，可能会重塑研究人员、政策制定者和公众对 AI 能力的认知。 该黎曼猜想证明在 Claude 的帮助下历时约六周完成，已由 Lean 与 Mathlib 社区进行机器校验，但目前尚无人类可读版本，这意味着其数学有效性和重要性仍需独立的人工审查。Wang 的论点核心在于，AI 与顶尖人类之间的差距如今仅剩具体知识、工程整合与实验三部分。

telegram · zaihuapd · Nov 23, 12:49

**背景**: 黎曼猜想由 Bernhard Riemann 于 1859 年提出，涉及素数分布，是数学中最著名的未解决问题之一。Lean 是一种用于形式化数学的证明助手和函数式编程语言，而 Mathlib 是其社区驱动的库，包含超过 23 万个定理和 11 万个定义。AI 对齐是致力于引导 AI 系统朝向预期目标和人类价值的领域，超级对齐则将这一目标扩展到假设中的超级智能系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/">Anthropic mathematician claims AI -assisted proof of the Riemann ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/21/anthropic-riemann-hypothesis-solved-claude-ai">Two groups verify mathematician’s claim that Claude ... | The Guardian</a></li>
<li><a href="https://leanprover-community.github.io/">Lean community</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#superintelligence`, `#alignment`, `#Meta AI`, `#AI research`

---