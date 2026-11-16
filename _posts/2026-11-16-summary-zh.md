---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> From 30 items, 1 important content pieces were selected

---

1. [Telegram 小组件远程代码执行漏洞警告](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Telegram 小组件远程代码执行漏洞警告](https://t.me/zaihuapd/45139) ⭐️ 8.0/10

Telegram 在 2026 年 11 月 9 日发布的 Bot API 10.4 中引入的小组件功能存在沙箱逃逸漏洞，可导致远程代码执行。安全研究人员已发布漏洞利用代码，Telegram 已发布 Android 紧急更新（版本 13.2.2）修复该漏洞。 这是一个影响广泛使用的即时通讯平台的高危安全漏洞，攻击者可能通过恶意机器人用户在设备上执行任意代码。建议用户避免使用来路不明的机器人，并暂缓升级直至补丁确认。 该漏洞存在于 Telegram 小组件使用的 QuickJS 沙箱中，该沙箱允许 JavaScript 在聊天消息内运行。漏洞利用代码在功能发布后 72 小时内即被演示，安全公司 NebuSec 随后声称发现了第二个绕过方法。

telegram · zaihuapd · Nov 15, 10:51

**背景**: Telegram 小组件是 Bot API 10.4 中的新功能，允许机器人将交互式 HTML、CSS 和 JavaScript 界面直接嵌入聊天消息中。为防止恶意代码危害客户端，Telegram 在 QuickJS 沙箱中运行小组件的 JavaScript。沙箱逃逸可使代码突破这一隔离环境，在宿主系统上执行，从而导致远程代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thecybersecguru.com/exploits/telegram-widget-rce-zero-click/">Telegram Widget RCE: Zero-Click Exploit Chains Explained ...</a></li>
<li><a href="https://www.worldcybernews.com/articles/1987">Telegram Patches Critical QuickJS Sandbox Escape ...</a></li>
<li><a href="https://core.telegram.org/bots/widgets">Telegram Widgets</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Telegram`, `#RCE`, `#sandbox`

---