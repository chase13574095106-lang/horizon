---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 24 items, 1 important content pieces were selected

---

1. [PHP rushes emergency patches for two critical RCE vulnerabilities](#item-1) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [PHP rushes emergency patches for two critical RCE vulnerabilities](https://t.me/zaihuapd/44678) ⭐️ 9.0/10

The PHP team released emergency security updates to fix two critical vulnerabilities that could allow unauthenticated remote code execution, urging users to upgrade immediately to PHP 8.5.12, 8.4.27, 8.3.36, or 8.2.35. Both vulnerabilities have a CVSS 4.0 score of 9.2. These vulnerabilities affect all PHP deployments that handle web requests, including PHP-FPM, mod_php, php-cgi, FrankenPHP, and LiteSpeed, potentially exposing a vast number of websites to remote code execution. The highest risk is with mod_php, where exploitation has been demonstrated before application code even runs. Exploitation has been demonstrated against Apache with mod_php, and the PHP security advisories also document a validated PHP-FPM exploitation path for one of the vulnerabilities (CVE-2026-109619). The CVSS 4.0 score of 9.2 indicates critical severity, and immediate patching is strongly recommended.

telegram · zaihuapd · Oct 25, 02:42

**Background**: PHP is a widely used server-side scripting language that powers many websites. Remote code execution (RCE) vulnerabilities allow attackers to run arbitrary code on a server without authentication, often leading to full system compromise. CVSS is a standardized system for rating the severity of security vulnerabilities, with scores from 0 to 10; version 4.0 is the current standard. PHP-FPM is a FastCGI process manager for PHP, mod_php is an Apache module for PHP, and FrankenPHP is a modern PHP application server built on Caddy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.circl.lu/pub/tr-102/">TR-102 Critical Remote Code Execution Vulnerabilities in PHP ...</a></li>
<li><a href="https://frankenphp.dev/docs/">FrankenPHP: the modern PHP app server</a></li>
<li><a href="https://md-5.com/blog/penetration-test-report-explained/">What's in a Penetration Test Report (and How to Read One)</a></li>

</ul>
</details>

**Tags**: `#security`, `#php`, `#vulnerability`, `#remote-code-execution`, `#patching`

---