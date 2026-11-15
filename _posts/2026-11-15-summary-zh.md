---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> From 29 items, 3 important content pieces were selected

---

1. [SpaceX 在星舰第 15 次试飞中成功捕获助推器](#item-1) ⭐️ 9.0/10
2. [Lovable 应用因缺少行级安全泄露护照信息和 20 万条私人消息](#item-2) ⭐️ 8.0/10
3. [SpaceX 下月将首次尝试完整回收星舰与超级重型助推器](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SpaceX 在星舰第 15 次试飞中成功捕获助推器](https://www.spacex.com/launches/starship-flight-15) ⭐️ 9.0/10

在星舰第 15 次试飞中，SpaceX 利用发射塔的“筷子”机械臂成功捕获了超级重型助推器，这是首次完整回收助推器。星舰上面级也进入了预定轨迹，但原计划的飞船二次捕获被推迟。 捕获助推器是实现完全可重复使用的关键一步，可能大幅降低发射成本并提高飞行频率，影响从卫星部署到 NASA 阿尔忒弥斯登月计划的方方面面。这一里程碑使 SpaceX 成为可重复使用超重型火箭领域的领导者。 捕获由得克萨斯州星基地的发射塔机械臂完成，此前助推器与星舰上面级分离。助推器利用栅格翼和发动机引导自身返回发射塔，但具体的捕获机制和损伤评估仍在调查中。

hackernews · ls612 · Nov 14, 21:22 · [社区讨论](https://news.ycombinator.com/item?id=50500963)

**背景**: 星舰是 SpaceX 完全可重复使用的两级火箭，由超级重型助推器和星舰飞船组成。与采用固体助推器和侧挂轨道器的部分可重复使用航天飞机不同，星舰旨在实现两级火箭的快速复用。“筷子”捕获法避免了着陆腿，使助推器能被发射塔直接捕获，从而减轻重量并缩短周转时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-says-starship-flight-15-booster-aborted-chopsticks-landing-catch-after-launch-due-to-guidance-issue-video">SpaceX still investigating why Starship Flight 15 booster ... | Space</a></li>

</ul>
</details>

**社区讨论**: 评论者庆祝这一历史性成就，将星舰与航天飞机比较，指出其更安全的设计和流水线生产。一些人讨论了完全可重复使用与部分可重复使用的经济性，另一些人则强调热防护罩需在后续步骤中经受考验。

**标签**: `#spacex`, `#starship`, `#reusable-rockets`, `#aerospace`, `#spaceflight`

---

<a id="item-2"></a>
## [Lovable 应用因缺少行级安全泄露护照信息和 20 万条私人消息](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Crissy Field 的安全研究人员发现，使用 AI 应用构建器 Lovable 创建的应用因 Supabase 数据库中的行级安全（RLS）不足，泄露了护照信息和超过 20 万条私人消息。该问题在一篇博客文章中披露，并在 Hacker News 上引发广泛关注，文章作者和 Lovable 的安全负责人均参与了讨论。 这一事件凸显了 AI 生成应用在未正确配置安全措施的情况下部署的风险，可能大规模泄露敏感用户数据。它强调了平台需要强制执行安全默认设置，以及开发者需要理解数据库安全，尤其是当越来越多非专家使用 AI 工具构建应用时。 根本原因是行级安全不足，Lovable 表示其自动扫描旨在捕捉此类问题，并提供免费扫描和自动修复选项。然而，社区成员指出 Supabase 的 RLS 默认关闭，且 10 月 30 日推出的修复可能不适用于现有项目，导致许多应用仍然存在漏洞。

hackernews · armcat · Nov 14, 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**背景**: Lovable 是一个 AI 驱动的应用构建器，用户可以通过自然语言描述来创建全栈应用。许多此类应用使用 Supabase，这是一个基于 PostgreSQL 的后端即服务，其中行级安全（RLS）控制用户可访问哪些行。默认情况下，未启用 RLS 的 Supabase 表对任何拥有公共 API 密钥的人开放，如果开发者不知情，可能导致数据泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/postgres/row-level-security">Row Level Security - Supabase Docs</a></li>
<li><a href="https://amabrik.com/blog/supabase-row-level-security/">Supabase Row Level Security (RLS) Explained - Amabrik</a></li>
<li><a href="https://lovable.dev/">App & Website Builder | Build Software in Minutes | Lovable</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（634 分，269 条评论）包括文章作者和 Lovable 的安全负责人，他们解释了根本原因和 Lovable 的扫描功能。评论者就 Supabase 对不安全默认设置的责任展开辩论，一些人认为 Supabase 历史上选择让 RLS 可选加剧了问题。其他人强调 AI 生成的应用是容易攻击的目标，平台必须采用默认拒绝的安全策略来防止此类泄露。

**标签**: `#security`, `#AI-generated apps`, `#Supabase`, `#data leak`, `#secure defaults`

---

<a id="item-3"></a>
## [SpaceX 下月将首次尝试完整回收星舰与超级重型助推器](https://t.me/zaihuapd/45117) ⭐️ 8.0/10

马斯克在财报电话会议上宣布，SpaceX 将于下个月首次尝试在同一飞行中同时回收星舰飞船和超级重型助推器，如果成功，这将是人类首次完全回收轨道运载工具。 两级完全可重复使用是大幅降低发射成本、实现火星殖民等宏伟目标的关键，若成功将成为航空航天史上的里程碑事件。 马斯克坦言首次尝试不保证成功，但表示下次飞行成功概率更高；上个月的发射因一台发动机提前关机，任务缩短至约 3 小时，助推器和飞船均未回收。

telegram · zaihuapd · Nov 14, 03:03

**背景**: 星舰是 SpaceX 研发的下一代完全可重复使用超重型运载火箭系统，由超级重型助推器和星舰飞船组成。超级重型助推器此前已被发射塔的“筷子”机械臂捕获，但从未在同一飞行中同时回收两级。完全可重复使用是 SpaceX 降低太空进入成本、实现登月和火星任务目标的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Starship_launches">List of Starship launches - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#spaceflight`, `#reusability`, `#aerospace`

---