---
layout: default
title: "Horizon Summary: 2026-06-21 (EN)"
date: 2026-06-21
lang: en
---

> From 21 items, 4 important content pieces were selected

---

1. [Prefer Duplication Over Wrong Abstraction](#item-1) ⭐️ 8.0/10
2. [Norvig's Classic Lisp Interpreter Tutorial](#item-2) ⭐️ 8.0/10
3. [Developers Don't Understand CORS (2019)](#item-3) ⭐️ 8.0/10
4. [Polymarket Hired Creators for Fake Trading Videos](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Prefer Duplication Over Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) ⭐️ 8.0/10

Sandi Metz's 2016 blog post argues that premature or incorrect abstractions are more harmful than code duplication, advocating for deferring abstraction until the correct pattern emerges. This article challenges the dogmatic application of the DRY (Don't Repeat Yourself) principle, offering a nuanced perspective that helps developers avoid over-engineering and maintain code flexibility. The article emphasizes that duplication is far cheaper than the wrong abstraction, and suggests that the best time to abstract is when you clearly see the correct pattern, not before.

hackernews · rafaepta · Jun 21, 16:08 · [Discussion](https://news.ycombinator.com/item?id=48620090)

**Background**: In software engineering, DRY is a principle that aims to reduce repetition by abstracting common code into a single place. However, premature abstraction can lead to rigid, hard-to-change code. This article addresses the tension between duplication and abstraction, a common debate in code quality discussions.

**Discussion**: Community comments highlight the importance of the 'single source of truth' principle and note that functional programming can reduce duplication issues. Many agree that over-engineering is worse than under-engineering, though some express discomfort with maintaining duplicated code.

**Tags**: `#software engineering`, `#code quality`, `#abstraction`, `#refactoring`, `#best practices`

---

<a id="item-2"></a>
## [Norvig's Classic Lisp Interpreter Tutorial](https://norvig.com/lispy.html) ⭐️ 8.0/10

Peter Norvig's 2010 tutorial 'How to Write a (Lisp) Interpreter (In Python)' is being highlighted again, demonstrating how to build a Scheme-like Lisp interpreter in Python 3. This tutorial remains one of the best introductions to writing interpreters, influencing many programmers to understand language implementation. Its enduring popularity on Hacker News shows its lasting educational value. The interpreter, named Lispy (lis.py), implements a significant subset of Scheme using Python 3. The tutorial is concise, with the core interpreter fitting in about 100 lines of code.

hackernews · tosh · Jun 21, 15:36 · [Discussion](https://news.ycombinator.com/item?id=48619831)

**Background**: An interpreter directly executes source code without prior compilation. Lisp is known for its simple syntax of nested lists, making it ideal for teaching interpreter construction. Peter Norvig is a renowned AI researcher and author.

<details><summary>References</summary>
<ul>
<li><a href="https://norvig.com/lispy.html">(How to Write a (Lisp) Interpreter (in Python)) - Peter Norvig</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lisp_(programming_language)">Lisp (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/fluentpython/lispy">GitHub - fluentpython/lispy: Learning with Peter Norvig's lis ...</a></li>

</ul>
</details>

**Discussion**: Commenters praise the tutorial as the best starting point for learning to write a programming language, with references to follow-up resources like 'Crafting Interpreters'. Some share related projects, such as Ribbit, a compact R4RS Scheme implementation.

**Tags**: `#Lisp`, `#Python`, `#interpreter`, `#tutorial`, `#programming languages`

---

<a id="item-3"></a>
## [Developers Don't Understand CORS (2019)](https://fosterelli.co/developers-dont-understand-cors) ⭐️ 8.0/10

A 2019 article highlights widespread developer misunderstandings about Cross-Origin Resource Sharing (CORS), and the comment section reveals even deeper misconceptions, with many commenters misinterpreting how CORS works. CORS is a critical web security mechanism, yet widespread confusion leads to misconfigurations and vulnerabilities. This discussion underscores the need for better developer education on web security fundamentals. The article itself may misrepresent CORS, as one commenter notes that setting Access-Control-Allow-Origin does not prevent other origins from sending requests; CORS only restricts the browser from exposing the response to the requesting origin. The comment section includes 250 comments with critical corrections and insights.

hackernews · toilet · Jun 21, 01:35 · [Discussion](https://news.ycombinator.com/item?id=48614844)

**Background**: CORS is a browser security feature that controls how web pages from one origin can request resources from another origin. It uses HTTP headers to allow servers to specify which origins are permitted to read the response. Many developers mistakenly believe CORS blocks requests entirely, but it actually prevents the browser from sharing the response with the requesting script unless the server explicitly allows it.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request">Preflight request - Glossary - MDN</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS">Cross-Origin Resource Sharing (CORS) - HTTP | MDN Code sample</a></li>

</ul>
</details>

**Discussion**: The comment section is highly engaged, with many commenters criticizing the article's inaccuracies and pointing out that even the author may not fully understand CORS. Some commenters recommend the MDN CORS documentation as a reliable resource, while others express frustration that CORS is overly complex and frequently misunderstood.

**Tags**: `#CORS`, `#web security`, `#developer education`, `#HTTP`

---

<a id="item-4"></a>
## [Polymarket Hired Creators for Fake Trading Videos](https://www.wsj.com/business/media/polymarket-social-media-bets-prediction-market-441cdeb5) ⭐️ 8.0/10

The Wall Street Journal reported that Polymarket hired dozens of young creators to produce fake trading videos on simulated websites, with 70% of 1,105 analyzed videos showing $1.9 million in fictitious bets, and 118 videos claiming nearly $900,000 in winnings that would have actually lost over $166,000. This deceptive practice violates U.S. federal advertising laws requiring disclosure of paid endorsements and undermines trust in prediction markets, potentially leading to regulatory action against Polymarket, which has been banned from offering crypto trading services in the U.S. since 2022. Polymarket responded by stating its commitment to market transparency and plans to conduct a comprehensive audit of existing promotional content. The platform used a social media army to push these videos to U.S. users despite its ban from offering crypto trading services in the country.

telegram · zaihuapd · Jun 21, 06:31

**Background**: Polymarket is a prediction market platform where users trade event-based contracts to bet on future outcomes. U.S. federal advertising law requires that paid endorsements must clearly disclose the material connection between the endorser and the advertiser. The FTC's Endorsement Guides provide guidance on these requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking">FTC's Endorsement Guides: What People Are Asking</a></li>
<li><a href="https://www.ftc.gov/news-events/topics/truth-advertising/advertisement-endorsements">Advertisement Endorsements | Federal Trade Commission</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#deception`, `#regulation`, `#cryptocurrency`, `#investigative journalism`

---