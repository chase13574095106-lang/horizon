---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> From 28 items, 4 important content pieces were selected

---

1. [小米发布 MiMo 2.6 实时强化学习后训练仪表盘](#item-1) ⭐️ 8.0/10
2. [黑客攻破 Flock 监控摄像头，暴露硬编码凭证](#item-2) ⭐️ 8.0/10
3. [170 万个低质中文赌场网站暗藏 APT 攻击基础设施](#item-3) ⭐️ 8.0/10
4. [新浪云 SAE 永久下线，早期 B 站视频源文件全部消失](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [小米发布 MiMo 2.6 实时强化学习后训练仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

小米公开发布了一个实时仪表盘，直接从训练器日志中流式展示 MiMo-V2.6-Pro 和 MiMo-V2.6-Flash 模型的强化学习后训练指标。该仪表盘会随着后训练进程实时显示奖励曲线和评估结果。 对于一家大型 AI 实验室来说，公开实时训练仪表盘并不常见，这为外界了解前沿模型在预训练之后如何被优化提供了罕见的透明度。这可能促使其他模型厂商分享类似的训练遥测数据，并让开发者提前了解 MiMo 2.6 的能力。 该仪表盘跟踪 MiMo 2.6 的 Pro 和 Flash 两个版本的强化学习训练过程，从训练器日志中实时流式输出奖励曲线和评估指标。讨论中引用的社区基准显示，MiMo-V2.5-Pro 在 DeepSWE 1.1 上得分 19%，明显落后于 Fable（70%）、Kimi K3（69%）和 Astra（74%），但用户报告其在实际编程任务中表现强劲。

hackernews · krackers · Sep 16, 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: MiMo 是小米的大语言模型系列，于 2025 年 4 月首次以 MiMo-7B 模型发布，目前通过 API 向开发者提供。后训练是指预训练之后的阶段，此时会使用基于人类反馈的强化学习（RLHF）及其他强化学习方法来对齐和改进模型行为。训练仪表盘通常被机器学习团队在内部用于监控奖励曲线等指标，但将其公开则十分罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL - mimo.xiaomi.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://pytorch.org/blog/a-primer-on-llm-post-training/">A Primer on LLM Post-Training - PyTorch</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持正面态度：一位软件工程师表示使用 MiMo-V2.5 获得了极高的投资回报率，称其成本低得难以置信，质量可与去年底/今年初的 Anthropic 模型相媲美；另一位则把下一代模型形容为一位能力强但有些健忘的资深工程师。还有人指出这种透明度很不寻常，并质疑其他模型厂商为何不这样做，也有评论者将开源 AI 的进展视为对闭源实验室 IPO 的潜在威胁。

**标签**: `#AI`, `#machine-learning`, `#model-training`, `#Xiaomi`, `#dashboard`

---

<a id="item-2"></a>
## [黑客攻破 Flock 监控摄像头，暴露硬编码凭证](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究人员发现 Flock Safety 监控摄像头中存在硬编码 API 密钥和明文存储的凭证，攻击者只需物理接触设备即可提取敏感认证信息。Distributed Denial of Secrets 已发布被攻破摄像头的分区镜像，相关报道与 404 Media 合作完成。 此次漏洞暴露了美国执法机构和市政部门广泛部署的监控基础设施中存在的系统性安全缺陷，可能泄露敏感的自动车牌识别数据并削弱公众对这些系统的信任。这也引发了关于部署在公共场所、任何人都能轻易物理接触的物联网设备安全架构的紧迫质疑。 该漏洞涉及的是硬编码 API 密钥而非硬编码管理员密码，但该 API 密钥可用于请求以明文存储的凭证，这些凭证似乎能获取对 Flock 服务器的访问权限。Flock 的漏洞披露政策包含一项重要豁免条款，排除了研究人员必须与设备“交互”或下载其数据的情况，实际上阻碍了有意义的安全研究。

hackernews · driverdan · Sep 16, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 是一家成立于 2017 年的美国私营公司，生产自动车牌识别（ALPR）摄像头、视频监控系统和枪声检测技术，被全美执法机构和社区广泛使用。硬编码凭证（归类为 CWE-798）是企业安全评估中最常被标记的安全弱点之一，因为它们会长期存在于代码历史中，且通过固件分析很容易被发现。物联网摄像头尤其脆弱，因为它们通常不支持 802.1X 等企业安全协议，也无法运行终端合规代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard-coded Credentials (4.20)</a></li>
<li><a href="https://www.guidepointsecurity.com/blog/iot-camera-security-evolving-threats/">IoT Camera Security: The Fixable Threat You Might Not See Coming | GuidePoint Security</a></li>

</ul>
</details>

**社区讨论**: 评论者强烈批评 Flock 的安全实践，有人称硬编码凭证是“完全无能的标志”，另一位则将 Flock 的漏洞披露政策描述为旨在营造负责任安全姿态的表象，而非真正了解漏洞。其他人指出这是“纯粹的懒惰”和“缩短上市时间”的优先事项所致，并指出在公共场所部署不安全的硬件意味着威胁模型必须包含本地物理访问。一位评论者分享称 Distributed Denial of Secrets 已发布分区镜像，并链接到 404 Media 文章的平行讨论。

**标签**: `#security`, `#vulnerability`, `#surveillance`, `#IoT`, `#privacy`

---

<a id="item-3"></a>
## [170 万个低质中文赌场网站暗藏 APT 攻击基础设施](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 8.0/10

安全研究人员发现约 170 万个低质中文赌场和成人网站被用作恶意软件传播与命令控制（C2）的隐蔽基础设施。自 2023 年以来，与中国有关联的 APT 组织利用名为“PeckBirdy”的框架将 C2 域名隐藏在这些网站中，并通过虚假软件更新诱骗用户下载恶意程序。 这一发现揭示了一种新颖的规避技术：恶意流量与低质赌博网站混杂在一起，使防御者容易将相关访问误判为员工违规浏览而非入侵行为。它表明廉价、一次性的网页内容可以被改造成难以检测和清除的弹性攻击基础设施。 PeckBirdy 框架是一种基于 JScript 的 C2 框架，被与中国有关联的 APT 组织用于在多种环境中滥用 LOLBins（就地取材的合法二进制文件），并已被观察到向赌博行业和亚洲政府目标投递高级后门。由于这些恶意网站与普通赌博页面高度相似，安全团队可能将相关流量视为无害而忽略。

telegram · zaihuapd · Sep 16, 07:31

**背景**: APT（高级持续性威胁）组织是资源充足、通常与国家背景相关的攻击者，长期从事间谍活动和入侵行动。他们依赖命令控制（C2）基础设施向受感染机器发送指令并接收窃取的数据，防御者则经常尝试封锁这些域名。将 C2 域名隐藏在海量低质赌博和成人网站之中，使恶意基础设施更难被识别，因为这些域名看起来只是普通（尽管不光彩）的商业网站。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendmicro.com/en_us/research/26/a/peckbirdy-script-framework.html">PeckBirdy: A Versatile Script Framework for LOLBins Exploitation Used by China-aligned Threat Groups | Trend Micro (US)</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/peckbirdy-framework-tied-china/">PeckBirdy Framework Tied to China-Aligned Cyber Campaigns - Infosecurity Magazine</a></li>
<li><a href="https://iplogger.org/blog/peckbirdy-framework-tied-to-china-aligned-cyber-campaigns/">PeckBirdy Framework: Dissecting the China-Aligned APT Threat to Asian Sectors</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#APT`, `#malware`, `#threat-intelligence`, `#C2-infrastructure`

---

<a id="item-4"></a>
## [新浪云 SAE 永久下线，早期 B 站视频源文件全部消失](https://tracker.archiveteam.org/sinavideo/#show-all) ⭐️ 8.0/10

国内首个 PaaS 平台新浪云 SAE 于 2026 年 9 月 16 日 24 时正式永久下线，所有用户数据被彻底删除。早期 B 站 存于新浪云 S3 桶中的约 420 TB 视频源文件随之消失，而 Archive Team 的分布式归档项目已抢救约 680 TB 数据，完成度达 96.26%。 此次下线抹去了一段中国互联网历史，托管在 SAE 上的早期 B 站 视频将永久无法访问，既影响曾在该平台开发的开发者，也影响早期用户生成内容的观众。这也凸显了中心化云存储的脆弱性，以及志愿者归档行动在数字保存中日益重要的作用。 Archive Team 的分布式归档项目已抢救约 680 TB 剩余数据，完成度达 96.26%，但新浪云 S3 桶中约 420 TB 数据可能无法在删除前全部抢救完成。2014 年前的 B 站 老视频预计将彻底失效。

telegram · zaihuapd · Sep 16, 15:00

**背景**: 新浪云 SAE（Sina App Engine）于 2009 年上线，是国内首个 PaaS 平台，以低成本、免运维的特点成为大量开发者的首选。中国主要视频分享网站 B 站 早期曾依赖新浪云存储大量视频源文件。Archive Team 是一个以保存濒危在线服务（如 GeoCities、Yahoo! Video）而闻名的志愿者组织，会在服务关停前发起分布式抓取以抢救数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sinacloud.com/sae.html">云 应用 SAE - 云 服务 - 云 托管</a></li>
<li><a href="https://en.wikipedia.org/wiki/Archive_Team">Archive Team - Wikipedia</a></li>
<li><a href="https://stage1st.com/2b/thread-2289931-1-1.html">新浪云 SAE 今晚永久下线：早期 B站视频源文件全部消失 - 归墟 - Stag...</a></li>

</ul>
</details>

**标签**: `#cloud-computing`, `#data-archiving`, `#bilibili`, `#paas`, `#digital-preservation`

---