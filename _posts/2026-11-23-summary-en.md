---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 24 items, 3 important content pieces were selected

---

1. [Lean formalization progress map for Masullo's Riemann proof sparks debate](#item-1) ⭐️ 8.0/10
2. [OpenAI Proposes Perplexity as a Shared Metric for Model Intelligence](#item-2) ⭐️ 8.0/10
3. [US Commerce Department to finalize rule blocking Chinese AI firms' remote chip access](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Lean formalization progress map for Masullo's Riemann proof sparks debate](https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3) ⭐️ 8.0/10

A progress map has been published for the Lean formalization of Alessandro Masullo's 940-page manuscript claiming a proof of the Generalized Riemann Hypothesis, accompanied by a Hacker News discussion with 131 comments questioning the proof's correctness and the endorsements it has received. This case highlights the tension between traditional peer review and emerging formal verification methods, and raises questions about how mathematical proofs are validated and endorsed in the AI era. The progress map tracks the Lean formalization effort, but community members caution that a high completion percentage does not imply correctness, as a single gap can invalidate the entire proof; the manuscript is noted as 'all human, with no AI' and has not been peer-reviewed.

hackernews · Qision · Nov 22, 23:12 · [Discussion](https://news.ycombinator.com/item?id=50605045)

**Background**: Lean is a proof assistant and functional programming language used to formalize mathematics, with a comprehensive library called Mathlib. Formalization involves writing definitions and proofs in a machine-checkable language, which can verify correctness but is extremely labor-intensive. The Generalized Riemann Hypothesis is a major unsolved problem in number theory, and Masullo's manuscript is a proposed proof released as an unfinished draft.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://www.arpaia.io/files/mathematics/riemann-hypothesis-masullo.pdf">Alessandro Masullo’s Proof of the Riemann Hypothesis</a></li>
<li><a href="https://riemannhypothesisclaude.org/alessandro-masullo">Alessandro Masullo's GRH Proof: What Vakil Announced</a></li>

</ul>
</details>

**Discussion**: Commenters expressed serious doubts: one mathematician contributing to the repo noted it's too early to tell if there's a major hole, while others pointed out that Ravi Vakil claims he hasn't even looked at the document and Brian Conrad says it needs 'major revision'. Some also voiced concern about AI and corporate influence in mathematics.

**Tags**: `#Lean`, `#formalization`, `#mathematics`, `#proof-verification`, `#academic-discourse`

---

<a id="item-2"></a>
## [OpenAI Proposes Perplexity as a Shared Metric for Model Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI published a post arguing that perplexity (equivalently, cross-entropy loss) should be established as a metric to compare model developers and inform shared safety standards, while providing more transparency into its own pretraining progress. The article sparked a large Hacker News discussion (485 points, 334 comments) about why this simple next-token prediction loss correlates so strongly with model capability. If adopted, perplexity could become a simple, standardized benchmark for comparing models across developers, replacing the increasingly convoluted benchmarks that are spun up every day. This would affect model developers, safety researchers, and anyone who needs to evaluate or trust LLM capabilities, as it could enable shared safety standards and more transparent pretraining progress reporting. Perplexity is the degree of surprise the model has in predicting the next token over a sequence; at worst it equals the vocabulary size, and at best it is 1. Commenters noted that Microsoft has reportedly signed on to this effort, with Mustafa Suleyman sharing that MAI-2 Base has a log-perplexity of 0.819 on OpenAI's evaluation set, though low perplexity does not guarantee high-quality generation, factual accuracy, or aligned behavior.

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**Background**: Perplexity is an information-theoretic measure of how well a probability model predicts a sample, and in language modeling it is equivalent to the exponentiated cross-entropy loss used as the training signal for next-token prediction. A lower perplexity means the model assigns higher probabilities to actual tokens, indicating better predictive performance. The idea that prediction equals compression, and that compression rate on raw data captures intelligence, has been argued in earlier work, and the community discussion connects this to the broader trend of using reinforcement learning and reasoning models.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cross-entropy">Cross-entropy - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters found the strong correlation between perplexity and intelligence surprising given the rise of RL, but many agreed it makes sense in retrospect as prediction equals compression. One commenter linked to a 2008 paper arguing this point, while another highlighted Microsoft's reported participation and shared MAI-2 Base results. Overall sentiment was positive, with appreciation for a simple benchmark amid increasingly convoluted evaluations.

**Tags**: `#llm`, `#perplexity`, `#machine-learning`, `#model-evaluation`, `#information-theory`

---

<a id="item-3"></a>
## [US Commerce Department to finalize rule blocking Chinese AI firms' remote chip access](https://t.me/zaihuapd/45289) ⭐️ 8.0/10

The US Commerce Department is finalizing a rule that would prevent Chinese AI companies from remotely accessing advanced AI chips through overseas data centers, with an announcement possibly as early as this month. The rule extends existing semiconductor export restrictions to seven Southeast Asian countries, including Malaysia, Singapore, and Thailand, to close remote access and chip smuggling loopholes. This rule significantly expands the scope of US export controls beyond physical chip shipments to remote access, potentially reshaping global AI compute access for Chinese firms. It directly affects major companies like Nvidia, which has lobbied against the measure, and could alter data center strategies across Southeast Asia. The rule is being finalized after consultation with other government agencies, and the White House has previously asked Congress to legislate the requirement. Nvidia argued that US AI infrastructure needs to win globally, but the administration is proceeding to close the remote access gap.

telegram · zaihuapd · Nov 22, 04:34

**Background**: US export controls on advanced AI chips, such as Nvidia's GPUs, have traditionally focused on restricting physical shipments to certain countries, particularly China. However, Chinese companies could bypass these restrictions by accessing chips remotely through data centers located in third countries. This new rule aims to close that loophole by extending controls to additional countries and regulating remote access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.freemalaysiatoday.com/category/nation/2025/07/04/us-to-restrict-ai-chip-shipments-to-malaysia-thailand">US to restrict AI chip shipments to Malaysia , Thailand | FMT</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-lobbies-white-house-and-wins-loosened-ai-gpu-export-control-to-china-u-s-lawmakers-reportedly-reject-gain-ai-act">Nvidia lobbies White House and wins loosened AI GPU export control...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#AI chips`, `#US-China tech`, `#semiconductor policy`, `#Nvidia`

---