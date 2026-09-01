---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 30 items, 6 important content pieces were selected

---

1. [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [NAT：互联网中心化的原罪](#item-2) ⭐️ 8.0/10
3. [Claude 共享链接遭搜索引擎索引，用户数据泄露](#item-3) ⭐️ 8.0/10
4. [OpenClaw 2.0：汇集逾 1.6 万拉取请求的最大更新](#item-4) ⭐️ 8.0/10
5. [苹果宣布 CEO 交接：库克卸任，特努斯接任](#item-5) ⭐️ 8.0/10
6. [小米发布三款玄戒芯片，AI 旗舰 SoC 将首搭小米 18 Fold](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已从 Chrome 网上应用店移除 Manifest V2（MV2）扩展，包括流行的广告拦截器 uBlock Origin。这标志着 MV2 弃用的最后阶段，Chrome 150 和 151 消除了允许 MV2 扩展继续运行的变通方法。 这影响了数百万依赖 uBlock Origin 进行有效广告拦截的用户，引发了对安全和浏览器垄断的担忧。这也促使用户迁移到 Firefox 等替代浏览器，后者继续支持 MV2 扩展。 Chrome 网上应用店不再接受 MV2 扩展，从 2026 年 6 月 3 日起，Chrome Beta、Dev 和 Canary 渠道会对已安装的 MV2 扩展显示警告。Chrome 150（2026 年 6 月 30 日发布）移除了恢复 MV2 安装的开关，Chrome 151（2026 年 7 月 28 日稳定版）彻底删除了 AllowLegacyMV2Extensions 代码路径。uBlock Origin 在 2026 年 8 月 31 日收到最终更新，但将不再在 Chrome 中工作。

hackernews · twapi · Aug 31, 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V3（MV3）是谷歌推出的新扩展平台，旨在提高安全性、隐私和性能，但通过限制阻塞网络请求的使用来限制广告拦截功能。uBlock Origin 是一款高效的内容拦截器，依赖 MV2 更广泛的 API，其开发者表示 MV3 版本（uBlock Origin Lite）功能较弱。谷歌于 2024 年开始逐步淘汰 MV2，到 2026 年，超过 85%的活跃维护扩展已迁移到 MV3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://blog.google/chromium/manifest-v2-phase-out-begins/">Manifest V2 phase-out begins</a></li>
<li><a href="https://appuals.com/ublock-origin-not-working-manifest-v2-shutdown/">uBlock Origin Not Working in Chrome? Fixes After ... - Appuals</a></li>

</ul>
</details>

**社区讨论**: 社区评论对谷歌的决定表示强烈不满，将广告拦截视为安全问题，尤其是对技术不熟练的用户。许多用户建议改用 Firefox，它继续有效支持 uBlock Origin，并批评谷歌对网络的单边控制。

**标签**: `#Chrome`, `#Manifest V2`, `#ad-blocking`, `#uBlock Origin`, `#browser`

---

<a id="item-2"></a>
## [NAT：互联网中心化的原罪](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

一篇评论文章认为网络地址转换（NAT）是互联网中心化的根本原因，引发了讨论，其中 Linux NAT 的原始实现者 Rusty Russell 承认自己在削弱公共端点方面所起的作用。 这场辩论凸显了为应对 IPv4 地址稀缺而采取的技术变通方案如何塑造了现代互联网的客户端-服务器模式和中心化，影响了所有运行服务器或重视去中心化网络的人。 Rusty Russell 解释说，他的实现避免了端口预留，以便将更多连接挤入一个 IP 地址，这使得来自不同地址的传入流量无法路由。讨论还将常规 NAT 与更严格的运营商级 NAT（CGNAT）进行了对比。

hackernews · robinpie · Aug 31, 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49504905)

**背景**: NAT 在 RFC 1631（1994 年）中作为 IPv4 地址枯竭和路由可扩展性的短期解决方案被引入。它将多个私有 IP 地址映射到一个公共 IP，节省了地址空间，但破坏了端到端原则，该原则原本允许任何主机充当服务器。这促进了集中式服务和客户端-服务器模式的兴起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-address-translation-nat.html">What Is Network Address Translation (NAT)? - Cisco</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-nottingham-avoiding-internet-centralization-05.html">Centralization , Decentralization, and Internet Standards</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人同意 NAT 是中心化的重要因素，而另一些人则认为这是夸大其词，指出常规 NAT 是可管理的，并且保护了不安全的设备。Rusty Russell 的承认增强了批评的分量，但一些人指出，糟糕的用户体验和 CGNAT 才是真正的问题。

**标签**: `#NAT`, `#internet architecture`, `#centralization`, `#networking`, `#history`

---

<a id="item-3"></a>
## [Claude 共享链接遭搜索引擎索引，用户数据泄露](https://t.me/zaihuapd/43511) ⭐️ 8.0/10

Anthropic 的 Claude 共享对话链接因缺少 noindex 标签而被 Google 和 Bing 等搜索引擎索引，导致敏感用户数据泄露。这一情况在 2026 年 7 月底得到了 WIRED 等媒体的确认。 这一隐私漏洞影响了数千名用户，泄露了 API 密钥、加密货币钱包、个人信息和企业机密。它凸显了 AI 聊天功能中适当隐私控制的重要性，并可能损害用户对 Anthropic 平台的信任。 共享链接缺少搜索引擎认可的'noindex'元标签，而 Anthropic 的 robots.txt 禁止规则无法移除已索引的页面。受影响的数据包括法律咨询、医疗信息和社会安全号码，Anthropic 尚未修复此问题。

telegram · zaihuapd · Aug 31, 03:22

**背景**: Claude 的共享对话功能允许用户为其聊天生成公开链接。如果没有 noindex 标签，这些链接可能被搜索引擎抓取和索引，从而被公开发现。大约一年前，ChatGPT 也出现过类似问题，但很快得到了修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/private-claude-chats-exposed-in-google-and-bing-search-results/">Private Claude Chats Exposed in Google and Bing Search Results | WIRED</a></li>
<li><a href="https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/">Indexed Claude Chats Show Why Disallow Is Not Noindex</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/private-claude-conversations-have-been-indexed-by-search-engines/">Private Claude Conversations Have Been Indexed by Search Engines - CNET</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#Claude`, `#Anthropic`, `#data leak`

---

<a id="item-4"></a>
## [OpenClaw 2.0：汇集逾 1.6 万拉取请求的最大更新](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw 于 8 月 30 日发布了史上最大更新 2.0 版本，汇集了来自 933 名贡献者（包括 569 名首次参与者）的逾 1.6 万个拉取请求。此次更新覆盖了平台的各个方面，从安装、消息到记忆、技能、模型、浏览器、插件和安全。 此次发布标志着 OpenClaw 这一广泛使用的开源项目的重要里程碑，展现了强大的社区参与度和快速的发展步伐。全面的改进，包括如私有凭据请求等增强的安全功能，可能吸引更多用户，并巩固其在 AI 代理生态系统中的地位。 此次更新包括简化的安装流程、重建的浏览器体验，以及支持多人协作的新共享云端会话。值得注意的是，它引入了私有凭据请求功能，允许用户安全地与代理共享凭据，而不会在聊天中暴露。

telegram · zaihuapd · Aug 31, 04:38

**背景**: OpenClaw 是一个开源 AI 代理平台，在去年年底发布时迅速走红。拉取请求（PR）是 GitHub 中的关键协作功能，允许开发者对代码库提出更改，由维护者审查后合并。此次更新的规模，超过 1.6 万个 PR，凸显了该项目活跃的贡献者基础和开源开发的协作性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mashable.com/tech/openclaw-2-0-released-agentic-ai">OpenClaw 2 . 0 : How to try the updated AI agent, what's new | Mashable</a></li>
<li><a href="https://docs.openclaw.ai/releases/2026.8.1">v2026.8.1 (AKA OpenClaw 2 . 0 ) - OpenClaw</a></li>
<li><a href="https://docs.github.com/articles/about-pull-requests?/">Pull requests - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#OpenClaw`, `#software release`, `#open source`, `#developer tools`, `#collaboration`

---

<a id="item-5"></a>
## [苹果宣布 CEO 交接：库克卸任，特努斯接任](https://t.me/zaihuapd/43516) ⭐️ 8.0/10

苹果宣布管理层交接：现任 CEO 蒂姆·库克将出任董事会执行董事长，硬件工程高级副总裁约翰·特努斯将于 2026 年 9 月 1 日起担任新任 CEO。董事会已一致批准该安排。 这是苹果十多年来首次更换 CEO，标志着这家全球最具价值公司进入新时代。特努斯的晋升反映了苹果对硬件创新的持续重视，此次交接将影响产品战略、投资者信心以及整个科技行业。 蒂姆·库克将在整个夏天继续担任 CEO 以确保平稳过渡，现任董事长 Arthur Levinson 将于 9 月 1 日转任首席独立董事。约翰·特努斯于 2001 年加入苹果，2013 年起领导硬件工程，他也将于同日加入董事会。

telegram · zaihuapd · Aug 31, 10:21

**背景**: 蒂姆·库克自 2011 年起担任苹果 CEO，接替史蒂夫·乔布斯，并带领公司成长为市值 3 万亿美元的巨头。约翰·特努斯是苹果硬件开发的关键人物，负责 iPhone、Mac、iPad 和 AirPods 等产品线。此次交接是计划中的继任流程的一部分，库克转任执行董事长以提供连续性。

**标签**: `#Apple`, `#CEO transition`, `#Tim Cook`, `#John Ternus`, `#tech industry`

---

<a id="item-6"></a>
## [小米发布三款玄戒芯片，AI 旗舰 SoC 将首搭小米 18 Fold](https://t.me/zaihuapd/43524) ⭐️ 8.0/10

小米于 2026 年 8 月 24 日在北京的玄戒芯片技术沟通会上发布了三款新芯片：AI 旗舰 SoC 玄戒 O3、高带宽 AI 加速芯片玄戒 O100，以及 3nm 智驾 AI 芯片玄戒 D100。三款芯片均已完成回片验证，将贯穿人车家全生态的端侧 AI 算力需求。 这标志着小米在自研芯片领域的重大扩展，覆盖移动、AI 加速和汽车领域，可能减少对外部供应商的依赖并增强设备集成度。玄戒 O3 首搭小米 18 Fold，表明小米意在高端智能手机市场以差异化 AI 能力竞争。 玄戒 O3 采用十核全大核 CPU，多核跑分突破 15000 分，GPU 为 G2-Ultra NX，性能提升 85%、功耗降低 64%。它还是全球首款支持 LPDDR6 内存的移动处理器。玄戒 O100 采用 6nm 晶圆级垂直堆叠先进封装，带宽高达 1.22 TB/s；玄戒 D100 集成 20 核 CPU 和 16 核 NPU，最高支持 160GB 统一内存，可本地部署 200B 参数大模型。

telegram · zaihuapd · Aug 31, 15:15

**背景**: 玄戒是小米自研芯片系列，旨在构建覆盖其生态的 AI 算力底座。LPDDR6 是 JEDEC 制定的低功耗内存标准，相比 LPDDR5X 提供更高带宽和效率，预计将在下一代移动处理器中采用。随着汽车制造商寻求集成先进 AI 能力用于自动驾驶，车载芯片市场正在增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/993/813.htm">构筑人车家 AI 算力底座，小米 玄 戒 发布三款自研芯片贯通全场景 - IT之家</a></li>
<li><a href="https://zhidx.com/p/587490.html">小米连发三个芯片大招！首秀3nm智驾芯片，玄戒O3搭折叠旗舰9月开卖 - 智东西</a></li>
<li><a href="https://www.163.com/dy/article/L55S5HBO051480KF.html">前瞻全球产业早报：小米发布国内首款3nm智驾高算力AI芯片|英伟达|机器人|hbm|chip|小米集团|知名企业|nvidia_网易订阅</a></li>

</ul>
</details>

**标签**: `#Xiaomi`, `#chip`, `#AI`, `#SoC`, `#hardware`

---