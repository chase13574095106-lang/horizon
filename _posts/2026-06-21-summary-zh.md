---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> From 21 items, 4 important content pieces were selected

---

1. [宁要重复，不要错误的抽象](#item-1) ⭐️ 8.0/10
2. [Norvig 的经典 Lisp 解释器教程](#item-2) ⭐️ 8.0/10
3. [开发者不理解 CORS（2019）](#item-3) ⭐️ 8.0/10
4. [Polymarket 被曝雇人制作虚假交易视频](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [宁要重复，不要错误的抽象](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) ⭐️ 8.0/10

Sandi Metz 在 2016 年的博客文章中提出，过早或错误的抽象比代码重复更有害，主张推迟抽象直到正确的模式出现。 这篇文章挑战了 DRY（不要重复自己）原则的教条式应用，提供了细致的视角，帮助开发者避免过度工程化并保持代码灵活性。 文章强调重复的成本远低于错误的抽象，并建议最佳的抽象时机是当你清楚看到正确模式时，而不是在此之前。

hackernews · rafaepta · Jun 21, 16:08 · [社区讨论](https://news.ycombinator.com/item?id=48620090)

**背景**: 在软件工程中，DRY 是一条旨在通过将通用代码抽象到单一位置来减少重复的原则。然而，过早的抽象可能导致代码僵化、难以修改。这篇文章讨论了重复与抽象之间的张力，这是代码质量讨论中常见的辩论。

**社区讨论**: 社区评论强调了“单一真相来源”原则的重要性，并指出函数式编程可以减少重复问题。许多人同意过度工程化比欠工程化更糟糕，尽管有些人对维护重复代码感到不适。

**标签**: `#software engineering`, `#code quality`, `#abstraction`, `#refactoring`, `#best practices`

---

<a id="item-2"></a>
## [Norvig 的经典 Lisp 解释器教程](https://norvig.com/lispy.html) ⭐️ 8.0/10

Peter Norvig 在 2010 年发布的教程《如何用 Python 编写一个(Lisp)解释器》再次被推荐，展示了如何用 Python 3 构建一个类似 Scheme 的 Lisp 解释器。 该教程仍然是编写解释器的最佳入门材料之一，影响了许多程序员理解语言实现。它在 Hacker News 上的持续热度证明了其长久的教学价值。 该解释器名为 Lispy（lis.py），使用 Python 3 实现了 Scheme 的一个主要子集。教程非常简洁，核心解释器代码仅约 100 行。

hackernews · tosh · Jun 21, 15:36 · [社区讨论](https://news.ycombinator.com/item?id=48619831)

**背景**: 解释器直接执行源代码而无需预先编译。Lisp 以其嵌套列表的简单语法而闻名，非常适合用于教学解释器构建。Peter Norvig 是著名的 AI 研究者和作家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://norvig.com/lispy.html">(How to Write a (Lisp) Interpreter (in Python)) - Peter Norvig</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lisp_(programming_language)">Lisp (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/fluentpython/lispy">GitHub - fluentpython/lispy: Learning with Peter Norvig's lis ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该教程是学习编写编程语言的最佳起点，并提到了后续资源如《Crafting Interpreters》。有人分享了相关项目，如 Ribbit，一个紧凑的 R4RS Scheme 实现。

**标签**: `#Lisp`, `#Python`, `#interpreter`, `#tutorial`, `#programming languages`

---

<a id="item-3"></a>
## [开发者不理解 CORS（2019）](https://fosterelli.co/developers-dont-understand-cors) ⭐️ 8.0/10

一篇 2019 年的文章指出开发者普遍对跨域资源共享（CORS）存在误解，而评论区则揭示了更深层次的错误认识，许多评论者误解了 CORS 的工作原理。 CORS 是关键的网络安全机制，但普遍的误解会导致配置错误和安全漏洞。这场讨论凸显了加强开发者网络安全基础教育的必要性。 文章本身可能对 CORS 的描述有误，有评论者指出设置 Access-Control-Allow-Origin 并不能阻止其他源发送请求；CORS 仅限制浏览器将响应暴露给请求源。评论区包含 250 条评论，其中有重要的纠正和见解。

hackernews · toilet · Jun 21, 01:35 · [社区讨论](https://news.ycombinator.com/item?id=48614844)

**背景**: CORS 是一种浏览器安全机制，用于控制来自一个源的网页如何请求另一个源的资源。它通过 HTTP 头允许服务器指定哪些源可以读取响应。许多开发者错误地认为 CORS 会完全阻止请求，但实际上它只是阻止浏览器将响应共享给请求脚本，除非服务器明确允许。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request">Preflight request - Glossary - MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS">Cross-Origin Resource Sharing (CORS) - HTTP | MDN Code sample</a></li>

</ul>
</details>

**社区讨论**: 评论区讨论热烈，许多评论者批评文章的不准确之处，并指出作者本人可能也未完全理解 CORS。一些评论者推荐 MDN 的 CORS 文档作为可靠资源，而另一些人则对 CORS 过于复杂且常被误解表示沮丧。

**标签**: `#CORS`, `#web security`, `#developer education`, `#HTTP`

---

<a id="item-4"></a>
## [Polymarket 被曝雇人制作虚假交易视频](https://www.wsj.com/business/media/polymarket-social-media-bets-prediction-market-441cdeb5) ⭐️ 8.0/10

《华尔街日报》报道称，Polymarket 雇佣数十名年轻创作者在模拟网站上制作虚假交易视频，在分析的 1,105 个视频中，七成展示了总计 190 万美元的虚假下注，其中 118 个视频宣称赢得近 90 万美元，实际上这些交易本会亏损超过 16.6 万美元。 这种欺骗性行为违反了美国联邦广告法关于披露付费代言关系的规定，破坏了公众对预测市场的信任，可能导致监管机构对 Polymarket 采取行动——该平台自 2022 年起已被禁止在美国提供加密交易服务。 Polymarket 回应称致力于市场透明，计划全面审计现有推广内容。该平台通过社交媒体大军向美国用户推送这些视频，尽管其已被禁止在美国提供加密交易服务。

telegram · zaihuapd · Jun 21, 06:31

**背景**: Polymarket 是一个预测市场平台，用户通过交易基于事件的合约来押注未来结果。美国联邦广告法要求付费代言必须明确披露代言人与广告主之间的实质性关系。FTC 的《代言指南》对这些要求提供了指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking">FTC's Endorsement Guides: What People Are Asking</a></li>
<li><a href="https://www.ftc.gov/news-events/topics/truth-advertising/advertisement-endorsements">Advertisement Endorsements | Federal Trade Commission</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#deception`, `#regulation`, `#cryptocurrency`, `#investigative journalism`

---