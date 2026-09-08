---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 32 items, 7 important content pieces were selected

---

1. [Mathematician Claims Navier-Stokes Progress, Accuses OpenAI of Data Theft](#item-1) ⭐️ 9.0/10
2. [Kimi K3 2.8T Runs on MacBook Pro via SSD Streaming at 1 token/s](#item-2) ⭐️ 8.0/10
3. [OpenAI Unveils ChatGPT Images 2.5 with New API Models](#item-3) ⭐️ 8.0/10
4. [US BIS Probes Chinese AI Firms' Overseas Access to Nvidia Chips](#item-4) ⭐️ 8.0/10
5. [ByteDance Plans 5-Trillion Parameter LLM, Rejects Distillation](#item-5) ⭐️ 8.0/10
6. [ASML and TSMC Push High NA EUV to 12-Inch Photomasks](#item-6) ⭐️ 8.0/10
7. [China Targets 9800 EFLOPS Intelligent Computing by 2030](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mathematician Claims Navier-Stokes Progress, Accuses OpenAI of Data Theft](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 9.0/10

Tristan Buckmaster, a mathematician at NYU's Courant Institute, announced progress on Navier-Stokes-related problems, including claims of finite-time blowup for incompressible porous media, Boussinesq, and 3D incompressible Euler equations. He also accused OpenAI of using his work without permission and attempting to pressure him into cooperating with their corporate interests. This development is significant because it touches on a major unsolved problem in mathematics (the Navier-Stokes existence and smoothness problem, a Millennium Prize problem) and raises serious ethical questions about AI companies using researchers' data without consent. The controversy could impact how academics collaborate with or trust AI companies like OpenAI. Buckmaster and Levent Alpöge claim progress on finite-time blowup for several fluid dynamics equations, but they do not have a proof for the exact Millennium Prize problem. OpenAI acknowledged that while unlikely, they cannot rule out that de-identified data from user interactions helped improve their models, leaving ambiguity about whether Buckmaster's work was used.

hackernews · procedurecall · Sep 8, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49605915)

**Background**: The Navier-Stokes equations describe the motion of viscous fluids and are fundamental to fluid mechanics. The Clay Mathematics Institute has offered a $1 million prize for a proof of existence and smoothness of solutions in 3D, which remains unsolved. Buckmaster is a well-regarded mathematician who previously won the Clay Research Award for related work on these equations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_equations">Navier-Stokes equations - Wikipedia</a></li>
<li><a href="https://cims.nyu.edu/~tristanb/">Tristan Buckmaster</a></li>
<li><a href="https://officechai.com/ai/mathematician-tristan-buckmaster-says-he-cracked-a-fluid-dynamics-problem-with-ai-accuses-openai-of-trying-to-take-credit/">Mathematician Tristan Buckmaster Says He Cracked a Fluid ...</a></li>

</ul>
</details>

**Discussion**: Community comments express strong anger and concern over OpenAI's alleged actions, with some calling it a case of corporate overreach and unethical data use. Others note the ambiguity in OpenAI's statement and question whether Buckmaster opted out of data usage, while some see this as an example of academic competition intensified by AI tools.

**Tags**: `#mathematics`, `#Navier-Stokes`, `#OpenAI`, `#research ethics`, `#AI`

---

<a id="item-2"></a>
## [Kimi K3 2.8T Runs on MacBook Pro via SSD Streaming at 1 token/s](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10

A project called DeltaFin claims to run the 2.8-trillion-parameter Kimi K3 model on a MacBook Pro at 1 token per second by streaming weights from four SSDs. This approach avoids loading the entire model into memory, enabling local inference of an extremely large model on consumer hardware. This demonstrates a novel technique that could allow individuals to run models far larger than their RAM would normally permit, potentially democratizing access to frontier-scale AI. However, the extremely low speed (1 token/s) highlights practical limitations, making it more of a proof-of-concept than a usable solution. The project streams model weights from four SSDs, likely using a technique similar to layer-wise loading or SSD caching. The reported speed of 1 token/s means generating a single word could take several seconds, and a typical response could take minutes or hours.

hackernews · Argonautlabs · Sep 8, 20:07 · [Discussion](https://news.ycombinator.com/item?id=49616257)

**Background**: Large language models (LLMs) typically require massive amounts of memory, far exceeding what consumer hardware offers. SSD streaming is an emerging technique that loads only the necessary parts of the model into memory on demand, trading speed for the ability to run models that would otherwise be impossible. Apple's unified memory architecture and fast SSDs make MacBooks a popular platform for such experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/quantumnic/ssd-llm">GitHub - quantumnic/ssd-llm: Run 70B+ LLMs on Apple Silicon by using SSD as extended memory — intelligent layer streaming and caching for Mac</a></li>
<li><a href="https://tinycomputers.io/posts/partial-llm-loading-running-models-too-big-for-vram.html">Partial LLM Loading: Running Models Too Big for VRAM | TinyComputers.io</a></li>
<li><a href="https://www.mindstudio.ai/blog/ssd-streaming-ai-models-ram-dial">SSD Streaming for AI Models: How to Turn RAM from a Wall into a Dial | MindStudio</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed, with some expressing skepticism about the feasibility and practicality, noting that a medium prompt would take 11 days. Others see it as a promising start, while one user asks for clarification on how the SSDs are connected.

**Tags**: `#LLM`, `#SSD`, `#MacBook`, `#Inference`, `#Open Source`

---

<a id="item-3"></a>
## [OpenAI Unveils ChatGPT Images 2.5 with New API Models](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 8.0/10

OpenAI has released ChatGPT Images 2.5, an upgraded image generation model that improves instruction-following across multiple turns, responds faster, and better preserves subjects in reference photos. The API now includes two new model IDs: gpt-image-2.5-sunburst and gpt-image-2.5-flare. This release is significant because OpenAI's image generation models have already been used to create over 3 billion images, and the new API models offer developers a choice between precision (Sunburst) and speed (Flare), enabling more tailored workflows. The improvements in instruction-following and subject preservation will likely enhance the quality and utility of AI-generated images across various applications. According to OpenAI's documentation, Sunburst is recommended for workflows where editing precision matters most, while Flare is suited for fast, high-quality everyday image generation. Simon Willison demonstrated the new model by upgrading his openai_image.py CLI tool to support reference images, successfully adding a raccoon scientist to an existing chart.

rss · Simon Willison · Sep 8, 22:46

**Background**: OpenAI has been developing image generation models that can create and edit images from text prompts. The GPT Image series, including gpt-image-1, has been available in the API, and the new 2.5 models build on this foundation. These models are used in ChatGPT and by developers via the API, enabling a wide range of applications from creative design to content generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst : New OpenAI Image APIs</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/image-generation">Image generation - OpenAI API</a></li>
<li><a href="https://openai.com/index/image-generation-api/">Introducing our latest image generation model in the API - OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#image generation`, `#API`, `#AI models`

---

<a id="item-4"></a>
## [US BIS Probes Chinese AI Firms' Overseas Access to Nvidia Chips](https://t.me/zaihuapd/43676) ⭐️ 8.0/10

The US Bureau of Industry and Security (BIS) has launched a systematic investigation into how Chinese AI companies obtain and use Nvidia chips overseas, including via remote access to computing resources in other countries. This follows a White House official's accusation against Moonshot AI for allegedly illegally obtaining Nvidia chips and accessing them remotely through Thailand. This investigation could tighten US export controls on AI chips, potentially restricting Chinese AI companies' access to advanced computing power and impacting the global AI supply chain. It underscores escalating US-China tech tensions and may lead to new regulations on cloud-based remote access to controlled chips. The BIS is reportedly compiling two lists of countries: one for black markets suspected of smuggling restricted chips into China, and another for countries where Chinese firms remotely rent chips. The investigation began days after a White House official publicly accused Moonshot AI, whose Kimi K3 model (released July 2026) approaches US performance, of illegal chip acquisition and remote access via Thailand.

telegram · zaihuapd · Sep 8, 03:35

**Background**: The US has imposed export controls on advanced Nvidia chips to China to limit its AI development. However, Chinese firms have sought workarounds, including accessing chips via cloud services in third countries. The BIS is the US agency responsible for enforcing export controls, and its investigation may test whether remote access to controlled chips falls within its jurisdiction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://www.dw.com/zh/中国ai公司月之暗面发布全球最大规模开源模型/a-78011216">中国AI公司月之暗面发布全球最大规模开源模型</a></li>

</ul>
</details>

**Tags**: `#US-China tech war`, `#AI chips`, `#export controls`, `#Nvidia`, `#geopolitics`

---

<a id="item-5"></a>
## [ByteDance Plans 5-Trillion Parameter LLM, Rejects Distillation](https://t.me/zaihuapd/43677) ⭐️ 8.0/10

ByteDance is reportedly discussing training a large language model with over 5 trillion parameters, led by Seed Foundation head Xiang Liang in collaboration with pre-training data lead Shen Ke. If realized, it would surpass Alibaba's Qwen 3.8-Max and Moonshot's K3 to become the largest known model in China. This signals a major strategic shift in China's AI landscape, as ByteDance aims for frontier-scale models rather than incremental improvements. CEO Zhang Yiming's opposition to distillation could reshape industry practices and intensify global competition in AI capabilities. The plan is still in early stages. At a Seed all-hands meeting two weeks ago, Zhang Yiming explicitly rejected distillation, arguing it merely replicates Claude's existing capabilities and cannot achieve breakthroughs, instead encouraging the team to pursue the upper limit of intelligence and accept short-term lag. He also recognized programming as a key direction and has integrated related efforts.

telegram · zaihuapd · Sep 8, 04:05

**Background**: ByteDance's Seed team, established in 2023, focuses on pursuing the upper limit of general intelligence, with research areas including LLMs, speech, vision, world models, and AI infrastructure. Model distillation is a technique that transfers knowledge from a large 'teacher' model to a smaller 'student' model, often used to reduce computational costs. Alibaba's Qwen 3.8-Max, with 2.4 trillion total parameters, is currently one of the largest models in China.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/zh/">字节跳动Seed</a></li>
<li><a href="https://baike.baidu.com/item/Seed/65823503">Seed（字节跳动旗下团队名称）_百度百科</a></li>
<li><a href="https://ai-bio.cn/qwen-3-8-max/">Qwen 3 . 8 - Max – 阿里云千问团队推出的旗舰大 模 型 | AI工具箱</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#large language models`, `#AI training`, `#China AI`, `#model scale`

---

<a id="item-6"></a>
## [ASML and TSMC Push High NA EUV to 12-Inch Photomasks](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 8.0/10

ASML and TSMC announced a collaboration on September 7 to transition High NA EUV lithography from 6-inch to 12-inch photomasks, aiming to establish a pilot line by 2031 and adopt the systems for advanced-node production by 2033. This move is significant because 12-inch photomasks can boost fab productivity, lower chipmaking costs, and eliminate stitching constraints, which are critical as chipmakers move to smaller and more complex process nodes. The collaboration between ASML and TSMC, along with Samsung and Intel, could accelerate the adoption of High NA EUV across the industry. The pilot line for 12-inch photomasks is targeted for 2031, with High NA EUV systems expected to enter advanced-node production by 2033. TSMC plans to use High NA EUV for large-scale manufacturing at advanced nodes starting in 2030, while initial production will continue using existing 6-inch masks.

telegram · zaihuapd · Sep 8, 06:55

**Background**: High NA EUV lithography is an advanced chipmaking technology that uses extreme ultraviolet light with a higher numerical aperture to create smaller features on chips. Currently, photomasks used in EUV are 6 inches, but moving to 12-inch masks allows for larger patterns, reducing the need for stitching and improving productivity. ASML is the leading supplier of EUV lithography systems, and TSMC is a major chip manufacturer that uses them for advanced nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://interestingengineering.com/innovation/asml-tsmc-high-na-euv-12-inch-photomask-pilot-line">High - NA EUV photomask push targets 12 - inch mask pilot line</a></li>
<li><a href="https://www.trendforce.com/news/2026/09/08/news-asml-expands-high-na-euv-push-with-tsmc-samsung-and-intel-12-inch-photomask-pilot-line-set-for-2031/">[News] ASML Expands High - NA EUV Push with TSMC , Samsung and...</a></li>
<li><a href="https://aninews.in/news/business/asml-tsmc-join-hands-for-12-inch-photomasks-target-pilot-line-by-2031-for-next-gen-chipmaking20260908181527/">ASML , TSMC join hands for 12 - inch photomasks , target pilot line by...</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#EUV lithography`, `#ASML`, `#TSMC`, `#chip manufacturing`

---

<a id="item-7"></a>
## [China Targets 9800 EFLOPS Intelligent Computing by 2030](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology (MIIT) has unveiled a five-year industrial plan targeting 9800 EFLOPS of intelligent computing capacity by 2030, with a cumulative investment of 3.8 trillion yuan in information infrastructure from 2026 to 2030. The plan also calls for the orderly deployment of computing clusters with 10,000 or more accelerator cards. This policy signals a major national push to strengthen China's AI infrastructure, potentially reshaping the global AI competitive landscape and affecting supply chains for AI chips and computing hardware. It underscores the strategic importance of domestic computing power and chip localization amid ongoing export controls. As of the end of June, China's intelligent computing capacity stood at 2185 EFLOPS, a year-on-year increase of 177%, meaning the 2030 target requires a more than fourfold expansion. The plan emphasizes adapting infrastructure to domestic AI chips, reflecting a strategic focus on self-reliance.

telegram · zaihuapd · Sep 8, 11:23

**Background**: EFLOPS (exaflops) is a unit of computing speed equal to one quintillion (10^18) floating-point operations per second, commonly used to measure the performance of supercomputers and AI training systems. A '10,000-card cluster' refers to a high-performance computing system integrating over 10,000 accelerator cards, typically used to train large AI models with hundreds of billions to trillions of parameters. China's push for domestic AI chips is driven by US export controls and the need for technological self-sufficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Floating_point_operations_per_second">Floating point operations per second - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/item/万卡集群/65379543">万卡集群 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/687404811">AI算力芯片：国产算力行业产业链深度梳理 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#China tech policy`, `#computing power`, `#EFLOPS`, `#national strategy`

---