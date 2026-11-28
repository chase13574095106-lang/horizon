---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> From 27 items, 4 important content pieces were selected

---

1. [OpenSec 披露 Linux NFS 服务器严重漏洞，可未授权获取 root 权限](#item-1) ⭐️ 9.0/10
2. [蜜雪冰城 5 亿元入股 DeepSeek 千亿级融资](#item-2) ⭐️ 8.0/10
3. [Anthropic 暗中削弱 Claude 对前沿 AI 研发请求的响应，影响约 0.03% 流量](#item-3) ⭐️ 8.0/10
4. [Minecraft Java 版曝高危 RCE 漏洞，恶意字体可执行任意代码](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenSec 披露 Linux NFS 服务器严重漏洞，可未授权获取 root 权限](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 披露了 CVE-2026-99362，这是 Linux 内核 NFS 服务器（nfsd）中的一个预认证堆溢出漏洞，CVSS 评分为 9.8，允许未经身份验证的远程攻击者通过一个发往 2049 端口的 TCP 连接获取 root 权限。该漏洞自 2014 年的 Linux 3.16 起就存在，影响运行 NFSv4.1 或 4.2 的主机；修复已在内核版本 6.12.117、6.18.61、7.3.2 和 7.4-rc1 中提供。 这是一个严重的远程内核漏洞，无需认证即可利用，使文件服务器、NAS 设备和集群存储节点面临完全被攻陷的风险。该漏洞自 2014 年起就存在，意味着大量系统可能暴露，必须立即打补丁或采取防火墙缓解措施。 该溢出会向内核堆对象之外写入 61 个字节，可被链式利用以获取 root shell。在不打补丁的情况下，缓解措施包括通过防火墙限制对 tcp/2049 的访问，该 CVE 于 2026 年 11 月 20 日公开。

telegram · zaihuapd · Nov 27, 12:57

**背景**: NFS（网络文件系统）是一种广泛使用的网络文件共享协议，nfsd 是 Linux 内核的 NFS 服务器实现。NFSv4.1 和 4.2 是较新的版本，包含会话中继和服务器端复制等功能，并监听 TCP 2049 端口。预认证漏洞意味着攻击者可以在任何登录或凭证检查之前利用它，因此尤其危险。CVSS 是一种标准评分系统，9.8 分表示严重级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS2ROOT (CVE-2026-99362): pre -auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS2ROOT Linux flaw can let attackers gain root privileges</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#security`, `#vulnerability`, `#nfs`, `#cve`

---

<a id="item-2"></a>
## [蜜雪冰城 5 亿元入股 DeepSeek 千亿级融资](https://m.sohu.com/a/1107027659_115479) ⭐️ 8.0/10

DeepSeek 完成第二轮融资，规模约 1000 亿至 1055 亿元人民币，投后估值约 6155 亿元。蜜雪冰城通过砺思资本管理的天津砺思星深基金认缴 5 亿元，本轮新增 31 家出资人，包括腾讯、宁德时代、中国移动和 vivo。 这是中国规模最大的 AI 融资之一，DeepSeek 估值超过 6000 亿元，并吸引了科技、能源巨头以及出人意料的消费品牌。这表明 DeepSeek 正成为获得广泛企业支持的国家级 AI 领军者，可能加速其算力建设和商业扩张。 蜜雪的 5 亿元通过天津砺思星深基金投入，该基金备案时募资 26.4 亿元，后扩募至 75.2 亿元关账，据称是今年最大的人民币盲池 VC 募资。蜜雪集团 2025 年营收 335.6 亿元，归母净利润约 58.9 亿元。

telegram · zaihuapd · Nov 27, 06:33

**背景**: DeepSeek 是一家中国 AI 研究公司，以开源前沿大语言模型闻名，例如拥有 6710 亿参数的混合专家模型 DeepSeek-V3。盲池基金是指在确定具体投资项目之前先募集资金的 VC 基金，赋予管理人较大的自主权。蜜雪冰城是中国最大的奶茶和冰淇淋连锁品牌，以低价策略和庞大的加盟网络著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/盲池基金/67559001">盲池基金 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/623993110">对比 】专项基金 VS 盲池基金 - 知乎</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI funding`, `#venture capital`, `#China tech`, `#industry news`

---

<a id="item-3"></a>
## [Anthropic 暗中削弱 Claude 对前沿 AI 研发请求的响应，影响约 0.03% 流量](https://news.ycombinator.com/item?id=50664325) ⭐️ 8.0/10

Anthropic 今年 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡披露，公司会暗中削弱 Claude 对开发前沿 AI 模型请求的回答效果，手段包括改写提示、引导向量和参数高效微调。该干预影响约 0.03% 的流量和不到 0.1% 的组织，用户无法察觉，也不会像安全类拦截那样回退到其他模型。 这揭示了一项有争议的政策：Anthropic 对 AI 开发请求静默降低模型输出质量，引发了对未公开行为修改的透明度和伦理担忧。此举可能为 AI 实验室如何管控竞争对手研究树立先例，并影响使用 Claude 进行合法机器学习工程工作的开发者。 干预覆盖预训练流水线、分布式训练和加速器设计等任务，多数编码工作不受影响；用 Claude 开发竞品模型本就违反服务条款。这份系统卡本周因 Hacker News 上的开发者讨论而重新受到关注。

telegram · zaihuapd · Nov 27, 13:42

**背景**: 系统卡是 Anthropic 发布的文档，用于说明模型的能力、安全评估和负责任部署决策。引导向量是在推理时添加到模型内部激活上的方向，用以改变其行为；参数高效微调则通过只更新一小部分参数来适配大模型。Anthropic 的服务条款禁止使用 Claude 构建竞争性 AI 模型，而此次披露显示公司通过静默降级而非明确拒绝来执行该规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.40998">[2610.40998] Steering Vectors as a Training Signal in LLM ...</a></li>
<li><a href="https://www.lesswrong.com/posts/QQP4nq7TXg89CJGBh/a-sober-look-at-steering-vectors-for-llms">A Sober Look at Steering Vectors for LLMs — LessWrong</a></li>
<li><a href="https://grokipedia.com/page/Parameter-Efficient_Fine-Tuning_PEFT">Parameter-Efficient Fine-Tuning (PEFT)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论提供了社区验证和多元观点，评论者就静默降低输出质量的透明度和伦理问题展开辩论，不过影响范围仅限于约 0.03% 的流量。

**标签**: `#AI ethics`, `#Anthropic`, `#model transparency`, `#AI policy`, `#Hacker News`

---

<a id="item-4"></a>
## [Minecraft Java 版曝高危 RCE 漏洞，恶意字体可执行任意代码](https://t.me/zaihuapd/45413) ⭐️ 8.0/10

11 月 22 日，一个名为 minecraft2shell 的高危远程代码执行漏洞被公开，影响 Minecraft Java 版 1.20.5 至 1.21.10 以及 26.1 至 26.4 快照。该漏洞允许服务器资源包中的恶意 TrueType 字体触发 FreeType 2.14.3 及更早版本中的越界写入，从而在 Windows 客户端上执行任意代码。 这是一个严重的安全问题，因为 Minecraft 服务器可以向连接的客户端推送资源包，这意味着任何加入恶意服务器的玩家都可能在毫无警告的情况下被入侵。由于目前尚无官方补丁且玩家基数庞大，建议服务器管理员和玩家在 Mojang 发布修复前保持警惕。 该漏洞源于 FreeType 中的越界写入，这是 Minecraft 通过 LWJGL 使用的字体渲染库。Mojang 目前使用受影响的 lwjgl-freetype 3.4.3，且暂无补丁；1.20.4 及更早版本以及基岩版不受影响。

telegram · zaihuapd · Nov 27, 18:04

**背景**: FreeType 是一个广泛使用的开源字体渲染库，Minecraft Java 版依赖它来显示文本，包括来自资源包的自定义字体。资源包是服务器可以自动发送给客户端以更改纹理、声音和字体的资源集合。远程代码执行（RCE）漏洞允许攻击者在受害者机器上运行任意代码，通常会导致系统被完全控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wurst.wiki/minecraft2shell">Minecraft2Shell Vulnerability - wurst.wiki</a></li>
<li><a href="https://liquidbounce.net/blog/minecraft2shell-vulnerability-AK0X5CE6">Minecraft2Shell Vulnerability - liquidbounce.net</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/minecraft2shell-minecraft-java-rce-resource-pack.html">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，Mojang 已于 11 月 24 日为 26.3 版本修复了该问题，建议玩家重启游戏以获取更新。有人担心许多服务器仍运行易受攻击的版本，用户们正在分享缓解措施，例如避免加入不受信任的服务器。

**标签**: `#security`, `#vulnerability`, `#Minecraft`, `#RCE`, `#FreeType`

---