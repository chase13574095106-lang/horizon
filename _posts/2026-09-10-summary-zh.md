---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> From 31 items, 8 important content pieces were selected

---

1. [微软将 Rust 列为一级语言](#item-1) ⭐️ 9.0/10
2. [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](#item-2) ⭐️ 9.0/10
3. [DeepSeek 发布开源 Harness 并开放 V4-Pro-0813 权重](#item-3) ⭐️ 9.0/10
4. [Shopify 从 React Native 回归原生 Swift 与 Kotlin](#item-4) ⭐️ 8.0/10
5. [研究人员质疑 OpenAI 是否值得信任其未发表的数学成果](#item-5) ⭐️ 8.0/10
6. [蚂蚁国际携手 Visa 与 Mastercard 制定 AI 代理支付标准](#item-6) ⭐️ 8.0/10
7. [DeepSeek 发布 V4.1 Flash：552B 参数多模态新架构模型](#item-7) ⭐️ 8.0/10
8. [月之暗面（Kimi）秘密递交港股 IPO 申请，投前估值 500 亿美元](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软将 Rust 列为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

微软已正式将 Rust 列为一级编程语言，为内部团队提供从本地开发到生产环境的标准化路径，包括安全的工具链构建、开发者工具、质量工作流、深度平台集成和合规支持。该公告以客座文章形式发布在 Rust 基金会网站上，同时确认微软已将 Rust 的后端从 LLVM 替换为 MSVC 后端。 这标志着全球最大软件公司之一的重大战略转变，表明 Rust 已成为系统编程领域 C++ 和 C# 的成熟且严肃的竞争对手。这可能加速整个行业对内存安全语言的采用，尤其是考虑到微软约 70% 的 CVE 漏洞属于内存安全问题。 一级语言地位意味着 Rust 在微软获得一流的工程支持，包括安全的工具链构建和合规工作流，而切换到 MSVC 后端是一项值得注意的技术变化。社区讨论还提到微软的目标是在 2030 年前通过自动化工具将 10 亿行代码转换为 Rust，不过官方细节仍然有限。

hackernews · mmastrac · Sep 10, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是由 Graydon Hoare 于 2006 年在 Mozilla 创建的通用系统编程语言，2015 年发布首个稳定版本，自 2021 年起由 Rust 基金会赞助。它通过“借用检查器”在编译期跟踪引用生命周期，在没有垃圾回收器的情况下实现内存安全，防止空指针解引用和数据竞争等错误。内存安全是某些编程语言的一种特性，可防止特定类型的内存相关错误，而在 C 和 C++ 等语言中，许多此类错误会演变为安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>
<li><a href="https://www.memorysafety.org/docs/memory-safety/">What is memory safety and why does it matter? - Prossimo</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（579 分，317 条评论）总体积极，评论者指出 Rust 如今已是 C++ 和 C# 的成熟竞争对手，而非初出茅庐的语言，并强调所有主流操作系统厂商都已多元化其系统编程语言选择。最令人兴奋的一点是 Rust 后端从 LLVM 替换为 MSVC，还有人引用微软的 10 亿行代码转换目标和 DARPA 的 C 到 Rust 自动转换工作作为佐证。

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Programming Languages`

---

<a id="item-2"></a>
## [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，称其为首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，可在受害者毫无交互的情况下劫持账号。该团队表示，借助 AI 协助，他们在约两天内找到漏洞并写出首个远程代码执行（RCE）利用程序，随后又用一周时间构建出蠕虫。 这标志着 AI 辅助漏洞发现与利用开发的一次范式转变，表明小团队如今也能构建出过去需要更大团队耗时数月才能完成的自我传播移动蠕虫。这对移动安全、拥有庞大用户群的微信以及 AI 安全都提出了紧迫问题，因为同样的能力也可能被攻击者滥用。 该漏洞是微信 VoIP 协议栈中的内存破坏问题，即使受害者接听电话且听不到任何声音，利用仍会成功。Calif Research 强调，大部分工作由 AI 完成，人类只负责判断攻击目标和安全测试方式。

rss · Simon Willison · Sep 10, 00:56

**背景**: 零点击利用无需用户任何操作即可攻陷设备，因此比需要点击或下载的攻击危险得多。蠕虫是能自我复制并自动传播的恶意软件，而远程代码执行（RCE）意味着攻击者可在受害者设备上运行任意代码。微信是全球使用最广泛的即时通讯应用之一，因此通过其通话功能传播的蠕虫可能波及数量庞大的用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberinsider.com/zero-click-worm-spreads-on-iphones-and-android-via-wechat-calls/">Zero-click worm spreads on iPhones and Android via WeChat calls</a></li>
<li><a href="https://www.1950.ai/post/wechat-zero-click-worm-how-ai-turned-a-voip-vulnerability-into-a-self-spreading-account-hijacking-t">WeChat Zero-Click Worm: How AI Turned a VoIP Vulnerability Into...</a></li>
<li><a href="https://iplogger.org/blog/researchers-build-wechat-zero-click-worm-hijacking-phones-via-calls/">WeChat Zero-Click Worm: AI-Powered Call Hijacks Threaten Android...</a></li>

</ul>
</details>

**标签**: `#ai-security`, `#mobile-security`, `#zero-click-exploit`, `#worm`, `#rce`

---

<a id="item-3"></a>
## [DeepSeek 发布开源 Harness 并开放 V4-Pro-0813 权重](https://t.me/zaihuapd/43738) ⭐️ 9.0/10

DeepSeek 发布了以 MIT 协议开源的智能体框架 DeepSeek Harness，并同时在 Hugging Face 上开放了 DeepSeek-V4-Pro-0813 的模型权重。该 Harness 将模型、工具、技能、会话、沙箱、存储、调度和 UI 等能力设计为可替换插件，并提供标准、PTC、极简和创造四种运行模式。 这对 AI 智能体生态意义重大，因为 DeepSeek 同时提供了完全开放的编排框架和开放的模型权重，为开发者提供了可替代 Claude Code 等专有智能体工具的免费方案。基于插件的架构有望降低构建和定制智能体工作流的门槛，而宽松的 MIT 协议也有利于推动广泛的商业和社区采用。 DeepSeek Harness 基于 Cordis 插件系统构建，目前处于开发者预览阶段，源代码已在 GitHub 和 npm 上提供。PTC 模式保留了标准模式的完整工具集，但通过生成的 SDK 和保留的 run_code 传输通道来暴露工具，支持嵌套调用和并行执行，不过副作用不会回滚，token 节省效果也取决于具体工作负载。

telegram · zaihuapd · Sep 10, 07:28

**背景**: 智能体框架（agent harness）是连接大语言模型与外部能力（如文件编辑、shell 命令、网络搜索和工具调用）的软件层，实际上把原始模型变成了可工作的智能体。DeepSeek 是一家以发布高性能开放权重模型而闻名的中国 AI 公司，DeepSeek-V4-Pro-0813 是其最新模型，具备 100 万 token 的上下文窗口和高效的 MoE（混合专家）架构。Cordis 是一个插件框架，支撑了“一切皆插件”的设计，让开发者可以替换或重组任意智能体能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://huggingface.co/multimodalart/DeepSeek-V4-Pro-0813">multimodalart/ DeepSeek - V 4 - Pro - 0813 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#open-source`, `#AI`, `#LLM`, `#model release`

---

<a id="item-4"></a>
## [Shopify 从 React Native 回归原生 Swift 与 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布将其移动应用从 React Native 迁回完全原生的 Swift（iOS）和 Kotlin（Android）代码库，并将 AI 辅助代码移植作为使这一转变可行的关键因素。该公司工程博客将此举描述为在多年依赖跨平台框架之后回归原生开发。 这是一个重要的行业信号，因为 Shopify 是 React Native 的重要且高调的采用者，其逆转表明，当 AI 能够承担移植负担时，即使是大型工程组织也可能认为原生开发值得付出成本。这可能影响其他公司如何权衡跨平台框架与原生代码，并加剧了关于 AI 在管理——或倍增——软件复杂性方面作用的更广泛争论。 据报道，这一迁移得益于能够将 React Native 代码移植到 Swift 和 Kotlin 的 AI 编码代理，社区成员描述了类似经历：大部分移植在一夜之间完成，仅用几天时间打磨。该决定的关键在于团队是否具备维护生成代码的原生专业知识，因为非原生开发者很难审查 AI 生成的 Swift 或 Kotlin 代码。

hackernews · fnthawar2 · Sep 10, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源框架，允许开发者使用 JavaScript 和 React 构建 iOS 和 Android 应用，跨平台共享一套代码库。Swift 是苹果为 iOS 和 macOS 打造的编译型语言，而 Kotlin 是 JetBrains 的语言，已被谷歌推荐为 Android 开发的首选。原生开发通常能提供更好的性能和平台特有的用户体验，但需要为每个平台维护独立的代码库和专业知识，这正是 React Native 等跨平台框架流行起来的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人警告说，Shopify 可能因假设 AI 让复杂性变得免费而低估了复杂性，认为 AI 在应对复杂性方面与人类一样吃力。另一些人分享了用 AI 代理将 React Native 移植到原生的成功经验，还有几位指出真正的问题在于团队是否具备维护和审查生成的 Swift 与 Kotlin 代码的原生专业知识。

**标签**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#AI-assisted Development`

---

<a id="item-5"></a>
## [研究人员质疑 OpenAI 是否值得信任其未发表的数学成果](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

一场始于 Mathstodon、并在 X 和 Bluesky 上扩散的讨论指称，OpenAI 利用与研究人员之间的协作聊天记录来解决未解决的数学问题，随后又沿着这些思路发表成果却未给予署名。该讨论在 Hacker News 上引发 586 条评论，质疑研究人员是否还能放心地把未发表的数学工作交给 OpenAI 的模型。 这场争议涉及研究诚信以及 AI 公司从保密协作中学习的伦理问题，可能使数学家不愿使用前沿模型，并推动外界要求更清晰的署名和数据使用政策。它还加剧了一场更广泛的争论：AI 系统究竟是在真正解决未解难题，还是在从用户那里吸收新的人类洞见。 评论者指出，OpenAI 据报道已向大量研究人员提供免费或补贴访问权限，这意味着用户聊天内容可能进入预训练数据，而 OpenAI 据称又表示产出该结果的模型并未在这些协作聊天上训练。讨论区分了模型记住聊天内容与在可验证数学上进行强化学习从而产生真正新颖技巧这两种情况。

hackernews · pred_ · Sep 10, 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: Mathstodon 是面向数学家的 Mastodon 服务器，属于去中心化联邦宇宙的一部分；XCancel 是基于 Nitter 的替代前端，用于查看 X/Twitter 帖子；Bluesky 则是建立在 AT Protocol 之上的另一个去中心化微博客网络。争议的核心在于，前沿 AI 实验室是否值得信任地对待非正式协作中分享的未发表研究，以及当模型似乎基于这些输入取得成果时，荣誉应如何归属。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mastodon_(social_network)">Mastodon (social network) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bluesky">Bluesky - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者大多把 OpenAI 比作一个从合作项目中拿走想法、却不给署名就发表成果的人类合作者，认为这很不道德；但也有人认为两件事可以同时成立：聊天记录可能提升模型的直觉，而在可验证数学上的强化学习则产生了真正超人的结果。还有人表示，唯一合乎伦理的做法是提供免费额度和工具支持，而不是抢在合作者前面发表；少数人则漠不关心，认为这些研究人员本应更谨慎。

**标签**: `#OpenAI`, `#AI ethics`, `#research integrity`, `#mathematics`, `#collaboration`

---

<a id="item-6"></a>
## [蚂蚁国际携手 Visa 与 Mastercard 制定 AI 代理支付标准](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 8.0/10

2026 年 9 月 10 日，蚂蚁国际与 Visa、Mastercard 在圣保罗宣布将共同制定 AI 代理支付的通用标准，其中包括“了解你的代理”（KYA）机制，用于将代理关联到有效实体、评估其行为并监测交易风险。三方援引麦肯锡的预测称，到 2030 年 AI 代理可能处理全球消费者商业交易中的 3 万亿至 5 万亿美元。 这是首次有横跨中国与西方市场的三大支付巨头同意为代理式商务共建统一的信任框架，有望避免各家自建代理验证方案导致市场割裂。若该标准被广泛采用，将决定银行、商户和钱包服务商如何认证并受理代表消费者购物、预订和付款的 AI 代理。 KYA 机制旨在通过验证代理身份并持续监测其行为，提升不同支付系统之间的互操作性与安全性，而不是依赖单一平台的私有校验方案。该计划目前仍处于框架阶段，尚未公布技术规范、认证流程或落地时间表。

telegram · zaihuapd · Sep 10, 03:00

**背景**: AI 代理正越来越多地代替用户自主行动，例如比价、预订出行和完成结账，但支付网络目前缺乏统一方式来确认某个代理确实获得了真实个人或企业的授权。“了解你的代理”是借鉴传统 KYC（了解你的客户）规则而兴起的新概念，把身份验证与风险控制延伸到软件代理身上。Mastercard 此前已提出 Agent Pay Acceptance Framework，FIDO 联盟也接手了 Agent Payments Protocol（AP2），以保持代理支付标准的开放性和平台中立性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html">Ant International, Visa and Mastercard team up on AI payment ...</a></li>
<li><a href="https://www.reuters.com/technology/payment-firms-visa-mastercard-ant-international-team-up-ai-agent-trust-framework-2026-09-10/">Payment firms Visa, Mastercard and Ant International team up ...</a></li>
<li><a href="https://www.mastercard.com/us/en/news-and-trends/stories/2025/agentic-commerce-framework.html">Agentic token framework: Driving trusted AI transactions</a></li>

</ul>
</details>

**标签**: `#AI payments`, `#fintech`, `#AI agents`, `#standards`, `#Visa/Mastercard`

---

<a id="item-7"></a>
## [DeepSeek 发布 V4.1 Flash：552B 参数多模态新架构模型](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是其全新模型结构系列中最小尺寸的模型，采用 552B 参数的 Causal-Encoder-Decoder 结构，输入和输出激活分别为 8B 和 16B，并原生支持多模态视觉理解。该模型已上线 DeepSeek API，模型名为 deepseek-flash，新价格于 2026 年 9 月 10 日 12:00 生效，9 月 14 日 12:00 后 deepseek-v4-pro 请求将路由至 V4.1 Flash 并按新价格计费。 此次发布表明 DeepSeek 正推动更高效、更具性价比的前沿模型，多方早期测试显示 V4.1 Flash 在性能、成本、速度和总运行时间上均领先于 V4-Pro。deepseek-v4-pro 流量自动路由至新模型意味着现有 API 用户无需修改代码即可完成迁移，有望降低生产工作负载的整体成本。 根据 vLLM Recipes 的信息，V4.1 Flash 是一个视觉语言 MoE 模型，总参数约 522B，每个提示 token 激活 8B、每个输出 token 激活 16B，结合了滑动窗口与压缩稀疏注意力、两级索引器、engram n-gram 记忆、超连接以及 DSpark 多 token 草稿头。为保持兼容性，deepseek-v4-flash 和 deepseek-v4-flash-vision-exp 会临时路由至 V4.1 Flash。

telegram · zaihuapd · Sep 10, 05:54

**背景**: 大语言模型通常分为三大架构家族：编码器-解码器、因果解码器和前缀解码器，各自的注意力模式不同。Causal-Encoder-Decoder 设计将因果（从左到右）生成与编码器组件结合，有助于模型同时处理理解和生成任务。多模态视觉理解指模型能够同时处理图像和文本，这一能力在前沿大语言模型中日益普遍。DeepSeek 是一家中国 AI 实验室，以低价发布有竞争力的开放和 API 模型而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash | vLLM Recipes</a></li>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-1-flash-pro-routing-prices-early-tests">DeepSeek V4.1 Flash: Benchmarks, Prices and Pro Cutoff</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#multimodal`, `#model release`, `#API`

---

<a id="item-8"></a>
## [月之暗面（Kimi）秘密递交港股 IPO 申请，投前估值 500 亿美元](https://t.me/zaihuapd/43743) ⭐️ 8.0/10

月之暗面（Kimi）已以保密形式向港交所递交 A1 文件，正式启动港股 IPO 流程，同时正以 500 亿美元投前估值推进新一轮融资，这可能是其上市前的最后一轮。公司回应称“对于市场传闻不予置评，目前暂无可以披露的信息”。 这是中国大模型行业从创业阶段走向公开市场的重要信号之一，也可能为 DeepSeek 等同行树立估值标杆——外界预计 DeepSeek 或于明年上半年上市。若上市成功，月之暗面将获得公开市场资金，以支持远超私募融资能力的算力与人才投入。 500 亿美元是投前估值，即不包含本轮新募资金；作为对比，公司今年 7 月的投后估值约为 350 亿美元，较 2025 年底约 43 亿美元增长约 8 倍。月之暗面保持约三个月一次的迭代节奏，今年 1 至 7 月先后上线 K2.5、K2.6 和 K3。

telegram · zaihuapd · Sep 10, 10:58

**背景**: A1 文件是企业向港交所提交、正式启动上市流程的申请表；以保密形式递交意味着公司可先与监管机构沟通，细节暂不对外公开。投前估值指新投资到账前公司的价值，投后估值则包含新注入的资金，因此两个数字不能直接比较。月之暗面是一家北京公司，开发了 Kimi 聊天机器人和 K 系列大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hk.stockstar.com/RB2026090300005720.shtml">据媒体报道，月之暗面（Kimi）已于本周以保密形式向港交所递交 A1 文...</a></li>
<li><a href="https://news.futunn.com/post/78704914/moonshot-ai-confidentially-files-with-the-hong-kong-stock-exchange">月之暗面向港交所秘密交表，正式启动 IPO</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/369371592">股权融资中的重大误区——投前估值和投后估值不分 - 知乎 投前估值 vs 投后估值：到底有什么区别？ | EquiRound 投前VS投后估值？新股VS老股？还在傻傻分不清楚？ 投前估值 vs 投后估值（2026 指南） | Round Funded 想拿投资人的钱？创业者要分清“投前估值”与“投后估值”！</a></li>

</ul>
</details>

**标签**: `#AI`, `#IPO`, `#Moonshot AI`, `#Kimi`, `#LLM`

---