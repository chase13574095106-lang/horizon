---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> From 24 items, 1 important content pieces were selected

---

1. [PHP 紧急修复两项严重远程代码执行漏洞](#item-1) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [PHP 紧急修复两项严重远程代码执行漏洞](https://t.me/zaihuapd/44678) ⭐️ 9.0/10

PHP 团队发布紧急安全更新，修复两个可能允许未经认证的远程代码执行的严重漏洞，并敦促用户立即升级到 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35。这两个漏洞的 CVSS 4.0 评分均为 9.2。 这些漏洞影响所有处理网页请求的 PHP 部署，包括 PHP-FPM、mod_php、php-cgi、FrankenPHP 和 LiteSpeed，可能使大量网站面临远程代码执行风险。其中 mod_php 风险最高，已有验证表明攻击可在网站业务代码运行前触发。 已有针对 Apache mod_php 的利用验证，且 PHP 安全公告还记录了其中一个漏洞（CVE-2026-109619）的 PHP-FPM 利用路径。CVSS 4.0 评分 9.2 表明严重性为 critical，强烈建议立即修补。

telegram · zaihuapd · Oct 25, 02:42

**背景**: PHP 是一种广泛使用的服务器端脚本语言，为许多网站提供支持。远程代码执行（RCE）漏洞允许攻击者在无需认证的情况下在服务器上运行任意代码，通常会导致系统完全被控制。CVSS 是评估安全漏洞严重性的标准化系统，评分从 0 到 10，4.0 版本是当前标准。PHP-FPM 是 PHP 的 FastCGI 进程管理器，mod_php 是 Apache 的 PHP 模块，FrankenPHP 是基于 Caddy 构建的现代 PHP 应用服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.circl.lu/pub/tr-102/">TR-102 Critical Remote Code Execution Vulnerabilities in PHP ...</a></li>
<li><a href="https://frankenphp.dev/docs/">FrankenPHP: the modern PHP app server</a></li>
<li><a href="https://md-5.com/blog/penetration-test-report-explained/">What's in a Penetration Test Report (and How to Read One)</a></li>

</ul>
</details>

**标签**: `#security`, `#php`, `#vulnerability`, `#remote-code-execution`, `#patching`

---