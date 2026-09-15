---
layout: default
title: "Horizon Summary: 2026-09-15 (ZH)"
date: 2026-09-15
lang: zh
---

> From 26 items, 11 important content pieces were selected

---

1. [电子墨水相框聆听鸟鸣，并以 19 世纪插画风格绘制鸟类](#item-1) ⭐️ 8.0/10
2. [互联网档案馆应对 Wayback Machine 遭 AI 爬虫大规模抓取](#item-2) ⭐️ 8.0/10
3. [谷歌发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](#item-3) ⭐️ 8.0/10
4. [Strix.ai 的 AI 代理 25 分钟内发现 Baseten 的 GitHub 管理员令牌](#item-4) ⭐️ 8.0/10
5. [US confirms for first time it has deployed space weapons](#item-5) ⭐️ 8.0/10
6. [布鲁斯·施奈尔：25 年大规模监控该结束了](#item-6) ⭐️ 8.0/10
7. [Anthropic 指控 7 家中国 AI 实验室大规模蒸馏 Claude](#item-7) ⭐️ 8.0/10
8. [中国“十五五”规划瞄准先进制程芯片与开源鸿蒙](#item-8) ⭐️ 8.0/10
9. [美英立法者推动禁止超级智能 AI 的法案](#item-9) ⭐️ 8.0/10
10. [谷歌向全体工程师开放 Anthropic 的 Claude Opus 5](#item-10) ⭐️ 8.0/10
11. [联发科发布采用台积电 2 纳米制程的天玑 9600 Pro](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [电子墨水相框聆听鸟鸣，并以 19 世纪插画风格绘制鸟类](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

开发者 Arne Munthe-Kaas 在 GitHub 上发布了 'fugleramme' 项目，这是一个由 ESP32 驱动的电子墨水相框，能够持续聆听鸟鸣，使用 BirdNET 分类器识别鸟种，并以 19 世纪野外图鉴风格的插画展示出来。该项目包含超过 800 张剪影图，覆盖 400 多个物种，并在 Hacker News 上分享，获得了 1233 个赞和 172 条评论。 该项目展示了如何将低功耗嵌入式硬件与开源机器学习相结合，创造出具有氛围感和趣味性的体验，而非纯粹实用的设备。它还凸显了 DIY 鸟类监测工具生态的不断壮大，并可能激励更多开发者探索电子墨水与边缘 AI 相结合的项目。 BirdNET 是一个传统神经网络而非大语言模型，经过训练可从声学数据中识别全球 3000 多种最常见的鸟类。该相框使用电子墨水以实现低功耗，社区成员指出，基于 BLE 的电子墨水驱动即使在每天多次刷新的情况下，单次充电（2000mAh）也可续航数年。

hackernews · arnemunthekaas · Sep 15, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49711544)

**背景**: BirdNET 是康奈尔大学的一个开源研究项目，利用人工智能和神经网络从声音录音中识别鸟类物种。电子墨水显示屏是反射式屏幕，仅在图像变化时消耗电量，因此非常适合常亮、低维护的设备。ESP32 是一款流行的低成本微控制器，支持 Wi-Fi 和蓝牙，广泛用于 DIY 物联网和硬件项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://www.hackster.io/news/this-diy-e-ink-display-brings-local-bird-sightings-to-your-wall-dd773e1558e5">This DIY E Ink Display Brings Local Bird Sightings to Your Wall</a></li>
<li><a href="https://news.ycombinator.com/item?id=49711544">Show HN: An e-ink frame that hears birds and draws them as 1800s ...</a></li>

</ul>
</details>

**社区讨论**: 评论者非常热情，称其为“HN 上最酷的东西”，并称赞它将各种想法融合成神奇的作品。一些人指出 BirdNET 是传统神经网络而非大语言模型，另一些人分享了自己的电子墨水项目，强调简单、单一用途设备带来的乐趣。还有人开玩笑说，IP over Avian Carriers 终于要实现了。

**标签**: `#e-ink`, `#ESP32`, `#bird-classification`, `#hardware`, `#creative-engineering`

---

<a id="item-2"></a>
## [互联网档案馆应对 Wayback Machine 遭 AI 爬虫大规模抓取](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

互联网档案馆发布更新称，Wayback Machine 遭遇了大量自动化流量的冲击，为维持服务运行已部署新的防护措施。档案馆认为，这些流量大多来自试图绕过原始网站封锁、转而抓取 Wayback Machine 存档副本的爬虫程序。 互联网档案馆是网页保存领域至关重要的公共基础设施，持续的抓取压力威胁到其继续提供免费、开放存档网页访问的能力。这一事件也表明，AI 训练数据的军备竞赛可能对非营利数字图书馆造成附带损害，并可能促使更多网站选择退出存档。 由于抓取行为，档案馆已经看到一些网站选择退出存档，服务访问也并非始终稳定，但仍保持了无需 Cloudflare 等中心化网关的开放访问。部分用户报告在某些网络环境下间歇性出现 429 限流错误，说明新防护措施可能同时影响正常访客与机器人。

hackernews · ChrisArchitect · Sep 15, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**背景**: 互联网档案馆是一家成立于 1996 年的美国 501(c)(3)非营利组织，以“普遍获取所有知识”为使命，最著名的服务是 Wayback Machine，它长期保存网页的历史快照。网页存档可以保留那些因网站改版或关闭而消失的文档，该馆也一直倡导自由开放的互联网。近年来，AI 公司对训练数据的需求推动了网络内容的大规模抓取，引发了关于同意与可持续性的伦理和法律争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.facebook.com/internetnetarchive/posts/publishers-have-real-questions-about-ai-but-lets-be-clear-the-wayback-machine-is/1456103409888954/">The Wayback Machine isn't a backdoor for AI scraping. For 30 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>
<li><a href="https://www.prolific.com/resources/ai-data-scraping-ethics-and-data-quality-challenges">AI data scraping : ethics and data quality challenges | Prolific</a></li>

</ul>
</details>

**社区讨论**: 评论者大多称赞互联网档案馆是不可或缺的基础设施，并谴责抓取行为；有人指出 AI 军备竞赛造成附带损害，唯有高额罚款等监管手段才可能真正解决问题。也有人分享了实际观察，例如工作网络间歇性出现 429 错误而家庭或手机访问正常，并赞赏 Tor 访问仍然可用、无需中心化网关。

**标签**: `#internet-archive`, `#web-scraping`, `#ai-ethics`, `#digital-preservation`, `#open-web`

---

<a id="item-3"></a>
## [谷歌发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，称其为迄今最先进的实时对话模型，其中 Extended Thinking 版本在实时音频会话中加入了后台推理能力。基础模型将旧的 gemini-3.1-flash-live-preview 模型字符串替换为 gemini-3.8-live，并在 Big Bench Audio 上取得 97.7% 的分数。 这是对最广泛使用的语音 AI 模型之一的重要更新，直接影响构建实时对话代理的开发者，因为他们必须更新客户端集成和模型字符串。这也加剧了前沿语音模型之间的竞争，而谷歌尽管拥有数据、TPU 硬件和广告资源，却被认为落后于竞争对手。 Extended Thinking 版本在实时音频会话中引入了后台推理，但标准的 gemini-3.8-live 模型不支持 thinking_level 参数。基础模型提供近乎实时的视觉输入处理、在 97 种支持语言之间自动进行对话中途切换，以及后台工具/API 执行，并且价格具有竞争力。

hackernews · leumon · Sep 15, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**背景**: Gemini Live 是谷歌为实时、自然的语音对话（而非纯文本聊天）设计的模型系列，通过谷歌的 Live API 访问。开发者需要指定诸如 gemini-3.8-live 这样的模型字符串来将请求路由到特定版本，因此新版本发布需要客户端更新。Big Bench Audio 是用于衡量这些实时模型音频理解与推理性能的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3.8 Live Extended Thinking - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live">Learn about the Gemini 3 . 8 Live model from Google</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持积极态度，一位用户称赞 Gemini 的南非荷兰语对话和语法课程是最令人愉快的 LLM 使用场景，另一位称此次发布很扎实，口音处理良好、声音悦耳、延迟低，并且还能在工作区账户上使用。也有人更为怀疑，质疑 Gemini 何时能超越 Fable 和 Astra 等对手，并询问 Gemini 4 何时推出；还有一位用户分享了一个用 LiveKit 和 Gemini 构建的基于电话的演示。

**标签**: `#Gemini`, `#AI`, `#LLM`, `#Google`, `#Model Release`

---

<a id="item-4"></a>
## [Strix.ai 的 AI 代理 25 分钟内发现 Baseten 的 GitHub 管理员令牌](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix.ai 的 AI 渗透测试代理在 Docker 构建历史中发现了一个有效的 Baseten GitHub 个人访问令牌（PAT），该令牌属于 'basetenbot' 账户，并在 25 分钟内获得了对 Baseten 生产仓库的管理员访问权限。该令牌拥有对 Baseten 主产品仓库、GitOps 集群仓库、Homebrew tap 的管理员和推送权限，以及对其他私有仓库的读写权限。 这一事件凸显了 CI/CD 流水线和 Docker 构建历史中凭证泄露的日益增长的风险，并展示了 AI 代理如何自动化并加速渗透测试以发现关键漏洞。它还引发了关于安全厂商将真实受害者用作营销案例的伦理和法律问题。 该令牌是在 Strix 发现 Baseten 镜像仓库后，从 Docker 构建历史中找到的；Baseten 在接到通知后将 Harbor 项目设为私有并轮换了令牌，但该事件引发了关于 Strix 是否因拉取镜像并公开点名受害者而越过道德底线的争论。

hackernews · bearsyankees · Sep 15, 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**背景**: Baseten 是一个用于在生产环境中部署和运行机器学习模型的 AI 推理平台。GitHub 个人访问令牌（PAT）是授予仓库访问权限的认证凭证，如果嵌入在 Docker 构建参数或环境变量中，可能会泄露，因为这些信息存储在镜像历史中，并可通过 'docker history' 检索。Strix.ai 是一家使用 AI 代理进行自动化渗透测试的安全公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/ise/hidden-risks-of-docker-build-time-arguments-and-how-to-secure-your-secrets/">The Hidden Risks of Docker Build Time Arguments and How to Secure Your Secrets - ISE Developer Blog</a></li>
<li><a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">Managing your personal access tokens - GitHub Docs</a></li>
<li><a href="https://www.baseten.co/">Inference Platform : Deploy AI models in production | Baseten</a></li>

</ul>
</details>

**社区讨论**: 评论者就 Strix 披露的伦理和法律问题展开辩论，一些人赞扬技术发现，另一些人则批评其营销语气和点名受害者的做法。有人对渗透测试的合法性以及其他组织中类似代理驱动攻击的可能性表示担忧。

**标签**: `#security`, `#ai-agents`, `#penetration-testing`, `#supply-chain-security`, `#github`

---

<a id="item-5"></a>
## [US confirms for first time it has deployed space weapons](https://www.bbc.com/news/articles/ck790xg41ygro) ⭐️ 8.0/10

The US has officially confirmed for the first time that it has deployed space weapons, sparking discussion on the militarization of space and its implications.

hackernews · harporoeder · Sep 15, 03:47 · [社区讨论](https://news.ycombinator.com/item?id=49707473)

**标签**: `#space weapons`, `#military technology`, `#geopolitics`, `#space policy`, `#directed energy`

---

<a id="item-6"></a>
## [布鲁斯·施奈尔：25 年大规模监控该结束了](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

布鲁斯·施奈尔发表了题为《25 年大规模监控该结束了》的文章，指出大规模监控已成为执法部门的常规工具，应当予以遏制。该文在 Hacker News 上引发热烈讨论，获得 762 分和 281 条评论，涉及隐私、政策与反抗等话题。 施奈尔是最具影响力的公共利益技术专家之一，因此他的论点在围绕《702 条款》和总统紧急状态令等监控权力的政策辩论中颇具分量。社区讨论的规模表明，人们对监控项目不断扩张而非收缩的担忧持续存在。 施奈尔在文中特别指出，ICE 将大规模监控用于移民执法，并针对行使第一修正案抗议权利的人，说明这些工具已超出反恐范畴。评论者还提到 NSPM-7 可能使大规模监控变得更加无孔不入。

hackernews · iamnothere · Sep 15, 11:26 · [社区讨论](https://news.ycombinator.com/item?id=49710883)

**背景**: 自 2001 年《爱国者法案》时代以来，美国的大规模监控不断扩张，其依据是每年签署、维持国家紧急状态的总统行政令。根据《外国情报监视法》第 702 条款授权的项目多次被曝收集美国人的数据，批评者认为监控会压制言论、助长歧视，且无法有效防止恐怖主义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html">25 Years of Mass Surveillance Is Enough - Schneier on Security</a></li>
<li><a href="https://www.lawfaremedia.org/article/25-years-of-mass-surveillance-is-enough">25 Years of Mass Surveillance Is Enough | Lawfare</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mass_surveillance_in_the_United_States">Mass surveillance in the United States - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞同施奈尔的观点，有人引用《道德经》指出限制反而滋生其欲防止的混乱，还有人警告监控"才刚刚开始"。其他人则提出实际对策：构建易于使用的自托管服务以利用第一和第四修正案的保护，并将摄像头网络限制在地方管辖范围内，以防联邦权力过度扩张。

**标签**: `#surveillance`, `#privacy`, `#security`, `#policy`, `#civil-liberties`

---

<a id="item-7"></a>
## [Anthropic 指控 7 家中国 AI 实验室大规模蒸馏 Claude](https://t.me/zaihuapd/43826) ⭐️ 8.0/10

Anthropic 发布报告称，自今年 2 月以来已发现并阻止 7 家中国 AI 实验室针对 Claude 的大规模“蒸馏”活动，并直接点名阿里巴巴、智谱、小米、商汤和 MiniMax。其中阿里巴巴规模最大，5 月至 7 月产生超过 1.51 亿次交互，高峰期每天接近 300 万次，Anthropic 称相关数据被用于训练 Qwen 3.5、3.6 和 3.7，并用于强化学习环境和模型架构研究；智谱则在 17 天内产生超过 340 万次交互，还尝试提取美国其他头部模型。 这是迄今为止最具体的跨境模型蒸馏公开指控之一，引发了关于 AI 实验室如何执行使用政策、中美模型开发者之间的竞争格局如何演变，以及企业利用竞争对手输出进行训练会面临何种法律与伦理风险的尖锐问题。具体的交互次数和被点名的模型版本让这场争议具有不同寻常的证据分量，其结果可能影响整个行业的服务条款、API 监控以及出口管制讨论。 Anthropic 将相关行为定性为有组织的蒸馏，而非普通 API 调用，并援引阿里巴巴高峰期每天约 300 万次交互、智谱 17 天内 340 万次交互等数据，称这些数据被用于 Qwen 3.5、3.6 和 3.7 以及强化学习环境和架构研究。报告并未披露完整的技术证据，也未说明另外两家未具名实验室的身份，Anthropic 也未表示是否会采取法律行动或进一步限制账户。

telegram · zaihuapd · Sep 15, 01:02

**背景**: 知识蒸馏是一种标准的机器学习技术，即让较小的模型模仿更大、更强模型的输出，使开发者无需从零训练就能构建更便宜、更快的模型。大规模调用竞争对手的商业 API 来生成这类训练数据通常被服务条款禁止，但检测难度很大，因为相关流量看起来可能与普通使用无异。Qwen 是阿里云的大语言模型系列，而强化学习环境则是模型通过试错和奖励进行学习的模拟场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>
<li><a href="https://snorkel.ai/blog/llm-distillation-demystified-a-complete-guide/">LLM distillation demystified: a complete guide - Snorkel AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#model distillation`, `#China AI`, `#Claude`

---

<a id="item-8"></a>
## [中国“十五五”规划瞄准先进制程芯片与开源鸿蒙](https://www.secrss.com/articles/93961) ⭐️ 8.0/10

中国工业和信息化部与国家发展改革委联合印发了《电子信息制造业发展“十五五”规划》，部署了 17 项重点任务。规划提出提高先进制程能力，突破高端手机核心芯片和 PC 高性能芯片，并加强开源鸿蒙等国产操作系统的搭载应用。 这一顶层政策指令表明，中国将在未来五年继续投入大量国家资源推动半导体自主可控和国产操作系统生态建设，可能重塑全球芯片供应链并减少对外国技术的依赖。这将直接影响面向中国市场的芯片制造商、设备厂商和软件开发者。 规划提出到 2030 年规模以上企业营业收入突破 30 万亿元，产业研发投入强度达到 3.5%。同时推进 RISC-V、人工智能芯片和终端、北斗等领域的发展。

telegram · zaihuapd · Sep 15, 03:10

**背景**: 五年规划是中国设定国家优先事项的中央经济计划文件，第十五个五年规划覆盖 2026 至 2030 年。先进制程指最前沿的半导体制造技术（如 7 纳米、5 纳米、3 纳米），决定芯片性能和能效。开源鸿蒙是源自华为鸿蒙的面向物联网的开源操作系统，而 RISC-V 是一种开放标准的指令集架构，允许企业免许可费设计定制处理器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenHarmony">OpenHarmony - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiconductor_device_fabrication">Semiconductor device fabrication - Wikipedia</a></li>

</ul>
</details>

**标签**: `#China tech policy`, `#semiconductors`, `#OpenHarmony`, `#RISC-V`, `#AI chips`

---

<a id="item-9"></a>
## [美英立法者推动禁止超级智能 AI 的法案](https://t.me/zaihuapd/43832) ⭐️ 8.0/10

美国参议员伯尼·桑德斯宣布将提出《禁止人工超级智能法案》，禁止开发比人类更聪明的 AI 并暂停其他先进 AI 研究；英国议员索贝尔也在下议院提出据称是 G7 议会中首份相关法案，要求赋予政府监控和限制超级智能“前体”系统的权力。 这些立法努力标志着主要西方国家政府迄今对前沿 AI 最激进的监管尝试之一，可能为全球 AI 治理树立先例，并影响美英 AI 实验室开发先进系统的方式。 两份法案还要求各自政府推动全球条约，但通过前景渺茫；伯克利教授拉塞尔警告，AI 可能造成“切尔诺贝利级灾难”，如协同破坏金融、通信或电网系统。

telegram · zaihuapd · Sep 15, 04:26

**背景**: 超级智能指的是假设中智力超越人类的软件 AI 系统，其潜在创造长期以来一直是未来学和 AI 安全领域讨论的焦点。灾难性 AI 风险通常被归为恶意使用、AI 竞赛、组织风险和失控系统等类别，这与全球研究者和政策制定者提出的担忧相呼应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-superintelligence">What Is Artificial Superintelligence? | IBM</a></li>
<li><a href="https://safe.ai/ai-risk">AI Risks that Could Lead to Catastrophe | CAIS</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#superintelligence`, `#AI safety`, `#legislation`, `#technology policy`

---

<a id="item-10"></a>
## [谷歌向全体工程师开放 Anthropic 的 Claude Opus 5](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 8.0/10

谷歌已向全公司工程师开放 Anthropic 旗下最强的编程模型 Claude（Opus 5），用于内部开发，但仅限于谷歌自家的 Antigravity 开发平台内使用。此前谷歌通常禁止大多数员工使用 Claude Code、OpenAI 的 Codex 等外部编程工具，要求他们改用自家的 Gemini。 对于一家拥有竞争性前沿模型的公司来说，这是一次明显的政策转向，说明即便是谷歌也感受到了 AI 编程工具领域的竞争压力。这也凸显了谷歌与 Anthropic 之间日益加深的战略关系——谷歌是 Anthropic 的投资方，并计划向其投入最多 400 亿美元，此举还可能影响其他大型科技公司对外部 AI 模型的采用方式。 Claude 是按每位员工配额提供的补充手段，而非替代品：谷歌发言人表示 Gemini 仍是内部开发的主要模型。此外，访问权限被限制在 Antigravity 平台内，这意味着工程师无法在该环境之外自由使用 Claude Code 等外部工具。

telegram · zaihuapd · Sep 15, 05:31

**背景**: Claude 是 Anthropic 的大语言模型系列，按能力分为 Haiku、Sonnet 和 Opus 三档，其中 Opus 能力最强，面向高难度推理、编程和长周期智能体任务。Claude Code 是 Anthropic 的智能体编程工具，可在终端、IDE 或浏览器中读取代码库、编辑文件并执行命令。Google Antigravity 则是谷歌的“智能体优先”开发平台，被视为 IDE 的演进形态，目标是编排 AI 智能体而非单纯手写代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>
<li><a href="https://mume.ai/anthropic/claude-opus-5">Claude Opus 5 by anthropic | Mume AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Anthropic`, `#Claude`, `#Software Engineering`

---

<a id="item-11"></a>
## [联发科发布采用台积电 2 纳米制程的天玑 9600 Pro](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 8.0/10

9 月 15 日，联发科推出旗舰手机芯片天玑 9600 Pro，这是该公司首款采用台积电 2 纳米制程的手机处理器，同时发布的还有采用 3 纳米制程的天玑 9600M。天玑 9600 Pro 配备专用 AI 处理器，联发科称其处理用户提示词、启动模型生成前的性能较上一代提升 51%，首批搭载手机将很快上市。 这是移动芯片领域的一个里程碑：联发科成为首批将台积电 2 纳米节点用于手机芯片的厂商之一，把半导体制造的最前沿推进到智能手机。51%的 AI 性能提升也表明，端侧 AI 能力而不仅是 CPU 原始速度，已成为旗舰安卓手机竞争的主战场。 天玑 9600 Pro 将 2 纳米制程与 4.55GHz CPU 以及融合 NPU、CPU、GPU 和 ISP 的统一“原生 AI 架构”相结合，并支持 4K/240fps 慢动作视频。相比之下，天玑 9600M 仍采用 3 纳米节点，使联发科形成双档旗舰产品线。

telegram · zaihuapd · Sep 15, 08:57

**背景**: “2 纳米”“3 纳米”等制程节点指的是制造处理器所用的工艺技术，节点越小通常意味着在相同面积内集成更多晶体管，从而带来更好的性能和能效。台积电的 N2 是其第一代纳米片（全环绕栅极）技术，该公司称相比此前的 N3E 节点，在同等功耗下性能提升约 10%至 15%，或在同等性能下功耗降低 20%至 30%。端侧 AI 指在手机本地而非云端运行大语言模型等 AI 模型，这需要强大的专用神经网络处理硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm">2nm Technology - Taiwan Semiconductor Manufacturing Company Limited</a></li>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.androidauthority.com/mediatek-dimensity-9600-pro-3711305/">The Dimensity 9600 Pro is the flagship chipset Google wishes the...</a></li>

</ul>
</details>

**标签**: `#MediaTek`, `#Dimensity 9600 Pro`, `#TSMC 2nm`, `#mobile chips`, `#on-device AI`

---