---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 29 items, 3 important content pieces were selected

---

1. [SpaceX catches Starship booster in Flight 15 milestone](#item-1) ⭐️ 9.0/10
2. [Lovable apps leak passport details and 200K messages due to missing RLS](#item-2) ⭐️ 8.0/10
3. [SpaceX to attempt first full recovery of Starship and Super Heavy next month](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SpaceX catches Starship booster in Flight 15 milestone](https://www.spacex.com/launches/starship-flight-15) ⭐️ 9.0/10

SpaceX successfully caught the Super Heavy booster with the launch tower's 'chopstick' arms during Starship Flight 15, marking the first time the booster was recovered intact. The Starship upper stage also reached its planned trajectory, though a planned second catch of the ship itself was deferred. Catching the booster is a critical step toward full reusability, which could drastically lower launch costs and increase flight frequency, impacting everything from satellite deployment to NASA's Artemis lunar plans. This milestone positions SpaceX as the leader in reusable super-heavy-lift rocketry. The catch was performed by the launch tower's arms at Starbase, Texas, after the booster separated from the Starship upper stage. The booster used its grid fins and engines to guide itself back to the tower, but the exact catch mechanism and any damage assessment remain under investigation.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**Background**: Starship is SpaceX's fully reusable two-stage rocket, consisting of the Super Heavy booster and the Starship spacecraft. Unlike the Space Shuttle, which had a partially reusable design with solid boosters and a side-mounted orbiter, Starship aims for rapid reuse of both stages. The 'chopstick' catch method avoids landing legs and allows the booster to be caught directly by the launch tower, reducing weight and turnaround time.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-says-starship-flight-15-booster-aborted-chopsticks-landing-catch-after-launch-due-to-guidance-issue-video">SpaceX still investigating why Starship Flight 15 booster ... | Space</a></li>

</ul>
</details>

**Discussion**: Commenters celebrated the achievement as a historic milestone, comparing Starship to the Space Shuttle and noting its safer design and assembly-line production. Some discussed the economics of full reusability versus partial reusability, while others highlighted the need for the heat shield to hold up for the next steps.

**Tags**: `#spacex`, `#starship`, `#reusable-rockets`, `#aerospace`, `#spaceflight`

---

<a id="item-2"></a>
## [Lovable apps leak passport details and 200K messages due to missing RLS](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Security researchers at Crissy Field found that apps built with Lovable, an AI app builder, exposed passport details and over 200,000 private messages because of insufficient Row-Level Security (RLS) in their Supabase databases. The issue was disclosed in a blog post that gained significant attention on Hacker News, with both the author and Lovable's Head of Security participating in the discussion. This incident highlights the risks of AI-generated apps that are deployed without proper security configurations, potentially exposing sensitive user data at scale. It underscores the need for platforms to enforce secure defaults and for developers to understand database security, especially as more non-experts build apps with AI tools. The root cause was insufficient Row-Level Security, which Lovable says its automated scanning is designed to catch; the company offers free scans and auto-fix options. However, community members point out that Supabase's RLS is off by default, and a fix rolled out on October 30 may not apply to existing projects, leaving many apps still vulnerable.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Background**: Lovable is an AI-powered app builder that lets users create full-stack applications by describing them in plain language. Many such apps use Supabase, a backend-as-a-service built on PostgreSQL, where Row-Level Security (RLS) controls which rows users can access. By default, Supabase tables without RLS enabled are accessible to anyone with the public API key, which can lead to data leaks if developers are unaware.

<details><summary>References</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/postgres/row-level-security">Row Level Security - Supabase Docs</a></li>
<li><a href="https://amabrik.com/blog/supabase-row-level-security/">Supabase Row Level Security (RLS) Explained - Amabrik</a></li>
<li><a href="https://lovable.dev/">App & Website Builder | Build Software in Minutes | Lovable</a></li>

</ul>
</details>

**Discussion**: The discussion on Hacker News (634 points, 269 comments) included the author and Lovable's Head of Security, who explained the root cause and Lovable's scanning features. Commenters debated Supabase's responsibility for insecure defaults, with some arguing that Supabase's historical choice to make RLS opt-in contributes to the problem. Others emphasized that AI-generated apps are easy targets and that platforms must adopt deny-by-default security to prevent such leaks.

**Tags**: `#security`, `#AI-generated apps`, `#Supabase`, `#data leak`, `#secure defaults`

---

<a id="item-3"></a>
## [SpaceX to attempt first full recovery of Starship and Super Heavy next month](https://t.me/zaihuapd/45117) ⭐️ 8.0/10

Elon Musk announced during an earnings call that SpaceX will attempt to recover both the Starship spacecraft and the Super Heavy booster on the same flight next month, which would be the first full recovery of an orbital launch vehicle if successful. Full reusability of both stages is the key to drastically lowering launch costs and enabling ambitious missions like Mars colonization, and success would mark a historic milestone for the aerospace industry. Musk acknowledged the first attempt is not guaranteed to succeed but said the probability of success is higher for the next flight; last month's launch was cut short to about 3 hours after one engine shut down early, and neither the booster nor the ship was recovered.

telegram · zaihuapd · Nov 14, 03:03

**Background**: Starship is SpaceX's next-generation fully reusable super heavy-lift launch system, consisting of the Super Heavy booster and the Starship spacecraft. Super Heavy has been caught by the launch tower's chopstick arms before, but recovering both stages on the same flight has never been achieved. Full reusability is central to SpaceX's goal of making space access affordable and enabling missions to the Moon and Mars.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Super_Heavy">SpaceX Super Heavy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Starship_launches">List of Starship launches - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#spaceflight`, `#reusability`, `#aerospace`

---