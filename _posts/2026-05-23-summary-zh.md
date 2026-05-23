---
layout: default
title: "Horizon Summary: 2026-05-23 (ZH)"
date: 2026-05-23
lang: zh
---

> From 23 items, 7 important content pieces were selected

---

1. [80386 微码被反汇编](#item-1) ⭐️ 9.0/10
2. [Anthropic 的 Project Glasswing：AI 发现逾万高危漏洞](#item-2) ⭐️ 9.0/10
3. [苹果开源 corecrypto 并附量子安全算法形式化验证证明](#item-3) ⭐️ 9.0/10
4. [SpaceX 星舰 v3 试飞达成关键里程碑](#item-4) ⭐️ 8.0/10
5. [微软大规模推广 Claude Code，鼓励非技术员工使用](#item-5) ⭐️ 8.0/10
6. [微软披露 OpenAI 单季度巨亏 115 亿美元](#item-6) ⭐️ 8.0/10
7. [富途被罚 18.5 亿，老虎被罚 4.11 亿](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [80386 微码被反汇编](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 9.0/10

一篇关于 Intel 80386 微处理器微码的详细反汇编和分析已发布，揭示了复杂 x86 指令在微架构层面的实现方式。 这一逆向工程成果揭开了经典处理器内部工作原理的神秘面纱，为计算机架构教育和历史保存提供了宝贵见解。 微码是通过 AI 辅助技术从高分辨率芯片图像中提取的，反汇编覆盖了 80386 的完整微码 ROM。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 微码是一层控制 CPU 内部操作的低级指令，将复杂的机器指令翻译成更简单的微操作。1985 年推出的 80386 是 Intel 首款 32 位 x86 处理器，使用微码实现其许多指令。逆向工程微码具有挑战性，因为制造商将其视为专有信息，并经常对更新进行加密或签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=48247004">80386 Microcode Disassembled | Hacker News</a></li>
<li><a href="https://www.altusintel.com/public-yyr4pw/?tt=1779562264">I386 Microcode Disassembly Results Published | Altus Intel</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对这一技术成就表示赞赏，用户指出黑盒分析的难度以及理解旧处理器的历史价值。一些评论讨论了从芯片图像中提取微码的过程，而另一些则推荐了关于微编程的资源。

**标签**: `#reverse engineering`, `#microcode`, `#80386`, `#computer architecture`, `#hardware`

---

<a id="item-2"></a>
## [Anthropic 的 Project Glasswing：AI 发现逾万高危漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 公布了 Project Glasswing 的初期成果，其 Claude Mythos Preview 模型在一个月内从关键软件中发现了超过 1 万个高危漏洞，经审查的漏洞中真阳性率达 90.6%。 这表明 AI 现在能够以远超人类验证和修补的速度和规模发现漏洞，将瓶颈从发现转移到修复，迫使软件行业加快补丁周期。 该项目扫描了数千个开源项目，发现了 6,202 个高危漏洞，Cloudflare 等合作伙伴报告漏洞发现速率提高了十倍。Anthropic 还发布了 Claude Security 工具，帮助企业修复漏洞。

telegram · zaihuapd · May 23, 03:16

**背景**: Project Glasswing 是 Anthropic 于 2026 年 4 月发起的行业网络安全计划，使用 Claude Mythos Preview 模型主动发现并修复关键开源软件中的漏洞。该模型不公开，由企业联盟使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://claude.com/product/claude-security">Claude Security | Claude by Anthropic</a></li>

</ul>
</details>

**社区讨论**: 讨论中提到了对漏洞疲劳的担忧以及开源维护者承受的压力，他们已经被大量报告压垮。一些人认为，如果没有相应的自动修补能力，AI 驱动的发现可能会使问题恶化。

**标签**: `#AI`, `#cybersecurity`, `#vulnerability discovery`, `#Anthropic`, `#open source`

---

<a id="item-3"></a>
## [苹果开源 corecrypto 并附量子安全算法形式化验证证明](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

苹果已在 GitHub 上开源其 corecrypto 密码库，包含后量子算法 ML-KEM 和 ML-DSA 的实现，并附有形式化验证证明，从数学上保证这些实现符合 NIST 标准。 这标志着密码学保障的重大进步，形式化验证提供了数学上严格的代码正确性保证，对于依赖 corecrypto 保障安全的数十亿苹果设备至关重要。同时，这也为后量子密码学部署的透明度和信任树立了新标杆。 形式化验证使用了 Isabelle 证明助手，超过 20 万行证明脚本验证了 7500 行 C 代码。苹果还发布了定制验证工具和 Isabelle 理论库供独立审查。

telegram · zaihuapd · May 23, 04:49

**背景**: 后量子密码学旨在保护系统免受未来量子计算机的攻击，因为量子计算机可能破解当前的公钥算法。ML-KEM（FIPS 203）和 ML-DSA（FIPS 204）分别是 NIST 标准化的密钥封装和数字签名算法。形式化验证通过数学证明确保软件正确实现规范，提供比单纯测试更强的保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/formal-verification-corecrypto/">A blueprint for formal verification of Apple corecrypto</a></li>
<li><a href="https://github.com/apple/corecrypto">GitHub - apple/corecrypto: Apple corecrypto</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#formal verification`, `#open source`, `#Apple`

---

<a id="item-4"></a>
## [SpaceX 星舰 v3 试飞达成关键里程碑](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 8.0/10

SpaceX 成功发射了星舰 v3 超重型火箭的首次试飞，尽管助推器在返场和着陆燃烧中出现发动机故障，仍成功实现了级间分离和星舰上面级的受控着陆。 这次试飞展示了星舰隔热罩技术的重大进步和快速迭代开发，使 SpaceX 更接近完全可重复使用的轨道发射能力，有望大幅降低进入太空的成本。 助推器在上升过程中有一台发动机失效，返场点火时所有发动机均未成功，但部分发动机在着陆时重新点燃，不过最终硬着陆且偏离目标；星舰上面级损失一台发动机，但仍实现了精确的定点着陆。

hackernews · busymom0 · May 22, 23:41 · [社区讨论](https://news.ycombinator.com/item?id=48242959)

**背景**: 星舰是 SpaceX 正在开发的两级完全可重复使用超重型运载火箭，采用燃烧液态甲烷和液氧的猛禽发动机。v3 版本进行了多项升级，尤其是隔热罩，它必须在再入过程中承受超过 1500°C 的高温。快速迭代——建造、测试、学习、改进——是 SpaceX 的核心开发理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/space/2025/08/spacex-got-good-heat-shield-data-for-starship-so-what-comes-next/">Starship’s heat shield appears to have performed quite well in test - Ars Technica</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacexs-starship-v3-megarocket-will-do-something-completely-new-on-flight-12-take-a-good-look-at-itself">SpaceX's Starship V3 megarocket will do something completely new on Flight 12 — take a good look at itself | Space</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了隔热罩的表现，指出与之前飞行相比没有可见的热点或烧穿。他们还强调了制导系统在发动机故障情况下仍成功实现飞船精确着陆，但助推器的失败被视为一个挫折。总体情绪积极，赞赏 SpaceX 的“足够好”快速迭代方法。

**标签**: `#spacex`, `#starship`, `#rocket launch`, `#space exploration`, `#engineering`

---

<a id="item-5"></a>
## [微软大规模推广 Claude Code，鼓励非技术员工使用](https://t.me/zaihuapd/41535) ⭐️ 8.0/10

微软正在其核心工程团队中广泛部署 Anthropic 的 Claude Code，包括 CoreAI 团队以及负责 Windows、Microsoft 365 和 Outlook 的体验与设备部门，并鼓励没有编程经验的员工使用它进行原型设计。软件工程师现在需要同时使用 Claude Code 和 GitHub Copilot，并提供对比反馈。 此举标志着科技巨头内部采用 AI 辅助编程工具的重大转变，可能影响整个行业的实践。通过要求工程师对比 Claude Code 和 GitHub Copilot，微软正在直接评估竞争性 AI 编程助手，这可能影响未来的产品集成和合作伙伴关系。 Claude Code 是 Anthropic 开发的 AI 编程代理，可直接在 IDE 中运行，提供代码建议和可视化差异对比。微软的推广包括非技术人员，表明该工具的原型设计门槛较低。

telegram · zaihuapd · May 23, 06:05

**背景**: Claude Code 是 Anthropic 开发的一系列大型语言模型，采用宪法 AI 训练以确保伦理合规。GitHub Copilot 由 GitHub 和 OpenAI 开发，是一款广泛使用的 AI 代码补全工具，可集成到主流 IDE 中。微软拥有 GitHub 并与 OpenAI 有紧密合作，因此其内部采用竞争对手的工具值得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/GitHub_Copilot">GitHub Copilot</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#Microsoft`, `#Claude Code`, `#GitHub Copilot`, `#software engineering`

---

<a id="item-6"></a>
## [微软披露 OpenAI 单季度巨亏 115 亿美元](https://t.me/zaihuapd/41537) ⭐️ 8.0/10

微软最新财报显示，其对 OpenAI 的权益法投资导致单季度净利润减少 31 亿美元，这意味着 OpenAI 该季度净亏损约 115 亿美元。 这一披露凸显了开发先进 AI 的巨大成本，引发了对这类投资可持续性以及 OpenAI 等领先 AI 公司财务健康状况的质疑。 基于微软持有 OpenAI 约 27%的股权，推算出的季度亏损约为 115 亿美元；若按税前损失和实际持股比例 32.5%计算，亏损可能超过 120 亿美元。这一亏损规模是 OpenAI 今年上半年 43 亿美元营收的近三倍。

telegram · zaihuapd · May 23, 07:40

**背景**: 权益法会计要求投资者在被投资企业发生利润或亏损时确认其应占份额，即使未实际分派股利。微软迄今已向 OpenAI 投入 116 亿美元，占其 130 亿美元承诺投资的绝大部分。OpenAI 的巨额亏损反映了训练和运行大型语言模型的高昂成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.mbalib.com/wiki/权益法">权益法 - MBA智库百科</a></li>
<li><a href="https://baike.baidu.com/item/长期股权投资权益法/9073814">长期股权投资权益法_百度百科</a></li>
<li><a href="https://wallstreetcn.com/articles/3769250">网传 OpenAI “ 股 权 结 构 表”：微软“130亿美元投资”已升至“2283亿美元”</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Microsoft`, `#AI Economics`, `#Financial Report`, `#Investment`

---

<a id="item-7"></a>
## [富途被罚 18.5 亿，老虎被罚 4.11 亿](https://t.me/zaihuapd/41539) ⭐️ 8.0/10

中国监管机构拟对富途控股处以 18.5 亿元人民币罚款，对老虎证券子公司罚没约 4.112 亿元人民币，原因是其未经许可在中国内地开展跨境证券业务。 这一里程碑式的处罚标志着对无牌跨境证券业务的重大打击，可能重塑金融科技格局，并影响数百万使用离岸交易平台的中国投资者。 富途 CEO 李华还面临 125 万元个人罚款。两家公司已将内地客户资产占比降至 13%以下，罚款需经后续程序最终确定。

telegram · zaihuapd · May 23, 10:58

**背景**: 富途控股和老虎证券是总部位于香港的在线券商，深受内地投资者青睐，用于交易美股和港股。中国证券法要求公司获得牌照才能招揽或服务内地客户，而这两家公司涉嫌在未获适当授权的情况下从事此类业务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.guancha.cn/GuanJinRong/2026_05_22_818074.shtml">证 监 会 拟 罚 款金额公布：富途被 罚 18.5亿，老虎被 罚 4.112亿</a></li>
<li><a href="https://www.21jingji.com/article/20260523/herald/e7eb58bb6994d891f986fd9d06c85b1d.html">中国 证 监 会拟对 富 途 罚款18.5亿， 老 虎 证 券 罚没4.112亿 - 21经济网</a></li>

</ul>
</details>

**标签**: `#regulatory`, `#fintech`, `#China`, `#securities`, `#penalty`

---