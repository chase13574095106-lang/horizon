---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> From 24 items, 6 important content pieces were selected

---

1. [PHP 紧急修复两个严重远程代码执行漏洞](#item-1) ⭐️ 9.0/10
2. [月之暗面发布 Kimi K3.1 Pro 及高速版本](#item-2) ⭐️ 8.0/10
3. [AI 辅助破解 iPhone 引发安全研究访问权争论](#item-3) ⭐️ 8.0/10
4. [Dessa：可在 MacBook Pro 本地运行的全双工语音模型](#item-4) ⭐️ 8.0/10
5. [月之暗面发布 Kimi K3.1 Pro，以更低价格媲美顶级模型](#item-5) ⭐️ 8.0/10
6. [iPhone 18 Pro 实现自 iOS 9 以来首个公开完整越狱](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PHP 紧急修复两个严重远程代码执行漏洞](https://t.me/zaihuapd/44647) ⭐️ 9.0/10

PHP 团队发布紧急安全更新，修复两个可导致未认证远程代码执行的严重漏洞（CVE-2026-109618 和 CVE-2026-109619），CVSS 4.0 评分均为 9.2。官方敦促用户立即升级至 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35。 这些漏洞影响所有处理网页请求的 PHP 部署，包括 PHP-FPM、Apache mod_php、php-cgi、FrankenPHP 和 LiteSpeed，攻击者可能无需认证即可执行任意代码。鉴于 PHP 在 Web 基础设施中的广泛使用，立即修补对于防止大规模利用至关重要。 已在 Apache mod_php 上演示了利用，攻击可在网站业务代码运行前触发；同时记录了经过验证的 PHP-FPM 利用路径。漏洞源于 PHP 核心的内存管理缺陷，例如 longjmp()处理内存不足错误导致释放后使用（UAF）条件。

telegram · zaihuapd · Oct 23, 13:46

**背景**: PHP 是一种广泛使用的开源脚本语言，特别适合 Web 开发，驱动着大量网站。CVSS（通用漏洞评分系统）是一个用于评估安全漏洞严重性的开放框架，4.0 版本是最新规范；9.0 及以上分数表示严重级别。远程代码执行（RCE）漏洞尤其危险，因为它允许攻击者在服务器上运行任意命令，通常导致系统完全被攻陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.circl.lu/pub/tr-102/">TR-102 Critical Remote Code Execution Vulnerabilities in PHP ...</a></li>
<li><a href="https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-php-could-allow-for-remote-code-execution_2026-119">Multiple Vulnerabilities in PHP Could Allow for Remote Code ...</a></li>
<li><a href="https://nsfocusglobal.com/php-remote-code-execution-vulnerability-cve-2026-109618-cve-2026-109619-advisory/">PHP Remote Code Execution Vulnerability (CVE-2026-109618 ...</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#vulnerability`, `#remote-code-execution`, `#patching`

---

<a id="item-2"></a>
## [月之暗面发布 Kimi K3.1 Pro 及高速版本](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

月之暗面（Moonshot AI）发布了新一代旗舰大语言模型 Kimi K3.1 Pro，并通过 Kimi Code 平台提供高速版本（Highspeed）。该发布迅速在 Hacker News 上引发广泛关注，获得超过 660 分和 420 条评论。 Kimi K3.1 Pro 在性能上可与 Claude Sonnet 5.5 等领先的闭源模型媲美，但成本显著更低，使其成为竞争激烈的大语言模型市场中的有力竞争者。此次发布加剧了 AI 实验室之间的性价比竞争，并为开发者提供了更经济的编码和推理任务选择。 在 Pac-Man 基准测试中，Kimi K3.1 Pro 与 Claude Sonnet 5.5 并列获得 93 分，成本为 0.68 美元、耗时 11 分钟，而 Sonnet 的成本为 1.61 美元、耗时 14 分钟。月之暗面还表示，有意在开放权重中限制模型的攻击性网络能力，并计划在未来版本中逐步提升。

hackernews · Jowsey · Oct 23, 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**背景**: Kimi 是中国 AI 公司月之暗面（Moonshot AI）开发的一系列大语言模型。K3 系列包括开放权重的多模态推理模型，其中 K3 拥有 2.8 万亿参数。Kimi Code 是一个提供这些模型用于编码任务的平台，并提供如 Highspeed 等不同变体以实现更快的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models.html">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区讨论突出了几个方面：用户注意到该模型独特的行为，例如直率且好争辩的回复，以及推理轨迹中不一致的自我识别。其他人将其性能和定价与 Sonnet 5.5 进行有利比较，而一些用户则抱怨订阅配额严格，一位用户在 99 美元套餐下不到一小时就触及了 5 小时限制。还有关于月之暗面故意限制开放权重中网络能力的辩论。

**标签**: `#LLM`, `#Kimi`, `#Moonshot AI`, `#benchmarks`, `#AI models`

---

<a id="item-3"></a>
## [AI 辅助破解 iPhone 引发安全研究访问权争论](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

Calif 团队的一篇博客文章详细介绍了他们如何利用 AI 破解 iPhone，展示了一种新颖的漏洞利用方法。这篇题为“今天，我们攻破了我们计划攻破的目标：iPhone”的文章迅速走红，在技术论坛上获得了 713 分和 467 条评论。 这一演示凸显了 AI 如何降低发现和利用 iOS 漏洞的门槛，可能加速攻击者与苹果之间的猫鼠游戏。它还引发了关于谁能获得前沿 AI 模型进行安全研究的疑问，因为此类能力可能成为少数人的护城河。 该博客文章未披露具体技术细节或所使用的确切 AI 模型，但社区讨论表明这些漏洞利用可能绕过了某些 iOS 保护机制。评论者还好奇苹果的极端安全设置“锁定模式”是否能缓解这些攻击。

hackernews · pavel_lishin · Oct 23, 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50211474)

**背景**: iOS 越狱涉及利用漏洞移除苹果的软件限制，获取 root 权限并允许安装未经授权的应用。历史上，越狱需要高超的专业技能，且往往很快被苹果修复。近期，Anthropic Claude 和 OpenAI Codex 等 AI 工具已被用于发现 iOS 漏洞，导致补丁数量激增。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://thehackernews.com/2026/06/apple-patches-30-ios-macos-safari-flaws.html">Apple Patches 30+ iOS, macOS, Safari Flaws, Including AI ...</a></li>
<li><a href="https://security.apple.com/">Apple Security Research</a></li>

</ul>
</details>

**社区讨论**: 评论者对平台锁定表示不满，指出越狱 iPhone 可能导致无法使用 iCloud 和 iMessage，使设备沦为“iPod touch”。一些人还批评前沿 AI 实验室将“红队”访问权限限制在内部圈子公司，使安全计划变成了护城河。其他人则询问锁定模式对此类漏洞利用的实际有效性。

**标签**: `#iPhone security`, `#AI exploitation`, `#jailbreaking`, `#security research`, `#platform lock-in`

---

<a id="item-4"></a>
## [Dessa：可在 MacBook Pro 本地运行的全双工语音模型](https://block.xyz/dessa) ⭐️ 8.0/10

Dessa 是一款新的全双工语音模型，可在 MacBook Pro M4 Max 或更高配置上本地运行，并且据其在 block.xyz 上的公告，它是在单台 NVIDIA GB200 NVL72 系统上训练的。它承诺提供低延迟、富有表现力的对话，能够同时聆听和说话。 这具有重要意义，因为它表明一个高度富有表现力、低延迟的全双工语音模型可以在单台机架级系统上训练，并部署在消费级硬件上，从而可能降低独立 AI 开发者的门槛。如果演示效果经得起检验，它可能会加速从轮次式语音助手向更自然、可打断的对话式 AI 的转变。 该模型据称可在 MacBook Pro M4 Max 或更高配置上本地运行，并且训练仅在一台 NVIDIA GB200 NVL72 上完成，这是一个液冷机架级系统，包含 36 个 Grace CPU 和 72 个 Blackwell GPU。公告强调了低延迟和富有表现力的对话演示，但内容中未提供技术论文或基准细节。

hackernews · dsr12 · Oct 23, 19:09 · [社区讨论](https://news.ycombinator.com/item?id=50213925)

**背景**: 全双工语音模型连续处理音频，允许系统同时聆听和说话，而不必等待用户说完，这与传统的轮次式语音助手不同。NVIDIA GB200 NVL72 是一个机架级液冷系统，通过 NVLink-C2C 连接 36 个 Grace CPU 和 72 个 Blackwell GPU，专为大规模 AI 训练和推理设计。在 Apple Silicon（M4 Max）上本地运行此类模型值得注意，因为它避免了云延迟和隐私问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL72 | NVIDIA</a></li>
<li><a href="https://github.com/cyrta/awesome-full-duplex-speech-to-speech">GitHub - cyrta/awesome-full-duplex-speech-to-speech: A ...</a></li>
<li><a href="https://mljourney.com/mac-ai-performance-guide-2026-m4-pro-vs-m4-max-vs-m4-ultra-for-local-llms/">Mac AI Performance Guide 2026: M4 Pro vs M4 Max vs M4 Ultra ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对本地推理和单系统训练的说法印象深刻，但一些人批评“史上最真实”的标题是耸人听闻的营销。其他人认为双工演示显得做作，指出模型打断太多，第一个例子中的笑声感觉不自然，还有一位评论者开玩笑地提到了 AI 女友市场。

**标签**: `#speech-model`, `#full-duplex`, `#AI`, `#local-inference`, `#Hacker News`

---

<a id="item-5"></a>
## [月之暗面发布 Kimi K3.1 Pro，以更低价格媲美顶级模型](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) ⭐️ 8.0/10

月之暗面于 2026 年 10 月 23 日在其 API 上发布了 Kimi K3.1 Pro，声称其基准测试成绩与 Claude Opus 5.5 和 GPT-6 Astra 相当，并承诺在 2026 年 11 月 4 日前发布完整的开放权重。该模型定价为每百万输入 token 2.00 美元、每百万输出 token 10.00 美元，是 Claude Opus 5.5 价格的一半。 这是首次有即将开放权重的模型在与前沿专有模型的对比中获得如此高的分数，Artificial Analysis 为其打出 55 分，领先于 Claude Fable 5.1、GPT-6 Astra 和 Gemini 4 Argon（均为 53 分），仅次于 Claude Opus 5.5（58 分）。接近前沿的性能、更低的定价以及即将开放的权重相结合，可能显著降低获取顶级 AI 能力的门槛。 月之暗面还提供了一个“Highspeed”版本，速度提升 2-3 倍，价格翻倍，但输入 token 缓存命中的价格相同。该模型支持三个推理级别（低、中、最高），而像 Simon Willison 的鹈鹕 SVG 基准测试这样的早期实践显示结果扎实但并非完美。

rss · Simon Willison · Oct 23, 19:40

**背景**: Kimi 是中国 AI 初创公司月之暗面开发的一系列大语言模型。开放权重意味着训练好的模型参数可以公开下载，任何人都能在本地运行或微调模型，这与只能通过 API 访问的专有模型形成对比。Artificial Analysis 是一家独立的基准测试机构，通过智能指数对模型进行排名，提供超越厂商自报基准的中立比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models: Open Source vs Open Weights vs...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Kimi`, `#Moonshot`, `#AI models`, `#benchmarks`

---

<a id="item-6"></a>
## [iPhone 18 Pro 实现自 iOS 9 以来首个公开完整越狱](https://t.me/zaihuapd/44644) ⭐️ 8.0/10

据 Telegram 消息，研究人员 @calif_io 在 iPhone 18 Pro 上演示了自 iOS 9 以来首个公开的 untethered 越狱，越狱状态在重启后依然保留，且无需连接电脑。该攻击链据称涉及三个层面：cryptex 子系统、TSS 票签欺骗以及绕过 PAC 保护。 这意义重大，因为自 iOS 9 以来 untethered 越狱几乎绝迹，而在当前旗舰设备上实现可用攻击链将表明苹果的多层防御仍可被攻破。这可能重振 iOS 安全研究，并引发对苹果启动时完整性保护健壮性的担忧。 该帖子称苹果在 9 月 14 日修补了 273 个漏洞，但 Calif 的演示表明仍有未公开的攻击链有效；然而细节有限且消息仅来自单一 Telegram 来源，缺乏独立验证。使用 TSS 票签欺骗和 cryptex 操作表明攻击者利用了苹果的签名和软件分发机制。

telegram · zaihuapd · Oct 23, 11:43

**背景**: 越狱是指移除苹果对 iOS 的软件限制，而 untethered 越狱被视为圣杯，因为它能在重启后保持越狱状态而无需重新运行漏洞利用。Cryptex 是 iOS 中使用的一种经过签名和完整性验证的软件分发包，而 TSS（票签签名服务器）票签是苹果签名流程的一部分，用于验证固件真实性。PAC（指针认证码）是 ARM 的一项安全特性，通过对指针进行签名来防止内存破坏漏洞利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://ios.cfw.guide/types-of-jailbreak/">Types of Jailbreak | iOS Guide</a></li>
<li><a href="https://github.com/0xjohnnydev/cryptsn0w?v=2">GitHub - 0xjohnnydev/cryptsn0w: Obsolete iOS jailbreak ...</a></li>

</ul>
</details>

**标签**: `#iOS jailbreak`, `#security research`, `#exploit chain`, `#Apple`, `#mobile security`

---