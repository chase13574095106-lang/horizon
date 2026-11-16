---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 30 items, 1 important content pieces were selected

---

1. [Telegram Widgets RCE Vulnerability Warning](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Telegram Widgets RCE Vulnerability Warning](https://t.me/zaihuapd/45139) ⭐️ 8.0/10

Telegram's Widgets feature, introduced in Bot API 10.4 on November 9, 2026, has a sandbox escape vulnerability that allows remote code execution. Security researchers have published exploit code, and Telegram has released an urgent Android update (version 13.2.2) to patch the flaw. This is a high-severity security issue affecting a widely-used messaging platform, potentially allowing attackers to execute arbitrary code on users' devices via malicious bots. Users are advised to avoid untrusted bots and delay upgrading until patches are confirmed. The vulnerability resides in the QuickJS sandbox used by Telegram Widgets, which allows JavaScript to run inside chat messages. Exploits were demonstrated within 72 hours of the feature's release, and a second bypass was later claimed by security firm NebuSec.

telegram · zaihuapd · Nov 15, 10:51

**Background**: Telegram Widgets is a new feature in Bot API 10.4 that lets bots embed interactive HTML, CSS, and JavaScript interfaces directly into chat messages. To prevent malicious code from compromising the client, Telegram runs widget JavaScript inside a QuickJS sandbox. A sandbox escape allows code to break out of this isolated environment and execute on the host system, leading to remote code execution.

<details><summary>References</summary>
<ul>
<li><a href="https://thecybersecguru.com/exploits/telegram-widget-rce-zero-click/">Telegram Widget RCE: Zero-Click Exploit Chains Explained ...</a></li>
<li><a href="https://www.worldcybernews.com/articles/1987">Telegram Patches Critical QuickJS Sandbox Escape ...</a></li>
<li><a href="https://core.telegram.org/bots/widgets">Telegram Widgets</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#Telegram`, `#RCE`, `#sandbox`

---