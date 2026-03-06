# arXiv Papers - cs.AI
Date: 2026-03-06
Total Papers: 14

## 1. RoboPocket: Improve Robot Policies Instantly with Your Phone

**Authors**: Junjie Fang, Wendi Chen, Han Xue, Fangyuan Zhou, Tian Le et al. (10 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05504v1

**PDF**: https://arxiv.org/pdf/2603.05504v1.pdf

**Abstract**:
Scaling imitation learning is fundamentally constrained by the efficiency of data collection. While handheld interfaces have emerged as a scalable solution for in-the-wild data acquisition, they predominantly operate in an open-loop manner: operators blindly collect demonstrations without knowing the underlying policy's weaknesses, leading to inefficient coverage of critical state distributions. Conversely, interactive methods like DAgger effectively address covariate shift but rely on physical robot execution, which is costly and difficult to scale. To reconcile this trade-off, we introduce RoboPocket, a portable system that enables Robot-Free Instant Policy Iteration using single consumer smartphones. Its core innovation is a Remote Inference framework that visualizes the policy's predicted trajectory via Augmented Reality (AR) Visual Foresight. This immersive feedback allows collectors to proactively identify potential failures and focus data collection on the policy's weak regions without requiring a physical robot. Furthermore, we implement an asynchronous Online Finetuning pipeline that continuously updates the policy with incoming data, effectively closing the learning loop in minutes. Extensive experiments demonstrate that RoboPocket adheres to data scaling laws and doubles the data efficiency compared to offline scaling strategies, overcoming their long-standing efficiency bottleneck. Moreover, our instant iteration loop also boosts sample efficiency by up to 2$\times$ in distributed environments a small number of interactive corrections per person. Project page and videos: https://robo-pocket.github.io.

---

## 2. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

**Authors**: Zeju Qiu, Lixin Liu, Adrian Weller, Han Shi, Weiyang Liu

**Published**: 2026-03-05

**arXiv ID**: 2603.05500v1

**PDF**: https://arxiv.org/pdf/2603.05500v1.pdf

**Abstract**:
Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In our experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

---

## 3. The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks

**Authors**: Shangwen Sun, Alfredo Canziani, Yann LeCun, Jiachen Zhu

**Published**: 2026-03-05

**arXiv ID**: 2603.05498v1

**PDF**: https://arxiv.org/pdf/2603.05498v1.pdf

**Abstract**:
We study two recurring phenomena in Transformer language models: massive activations, in which a small number of tokens exhibit extreme outliers in a few channels, and attention sinks, in which certain tokens attract disproportionate attention mass regardless of semantic relevance. Prior work observes that these phenomena frequently co-occur and often involve the same tokens, but their functional roles and causal relationship remain unclear. Through systematic experiments, we show that the co-occurrence is largely an architectural artifact of modern Transformer design, and that the two phenomena serve related but distinct functions. Massive activations operate globally: they induce near-constant hidden representations that persist across layers, effectively functioning as implicit parameters of the model. Attention sinks operate locally: they modulate attention outputs across heads and bias individual heads toward short-range dependencies. We identify the pre-norm configuration as the key choice that enables the co-occurrence, and show that ablating it causes the two phenomena to decouple.

---

## 4. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**Authors**: Helena Casademunt, Bartosz Cywiński, Khoi Tran, Arya Jakkli, Samuel Marks et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05494v1

**PDF**: https://arxiv.org/pdf/2603.05494v1.pdf

**Abstract**:
Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

---

## 5. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

**Authors**: Siddharth Boppana, Annabel Ma, Max Loeffler, Raphael Sarfati, Eric Bigelow et al. (8 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05488v1

**PDF**: https://arxiv.org/pdf/2603.05488v1.pdf

**Abstract**:
We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, 'aha' moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned "reasoning theater." Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.

---

## 6. Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation

**Authors**: Benjamin Feuer, Lucas Rosenblatt, Oussama Elachqar

**Published**: 2026-03-05

**arXiv ID**: 2603.05485v1

**PDF**: https://arxiv.org/pdf/2603.05485v1.pdf

**Abstract**:
As AI models progress beyond simple chatbots into more complex workflows, we draw ever closer to the event horizon beyond which AI systems will be utilized in autonomous, self-maintaining feedback loops. Any autonomous AI system will depend on automated, verifiable rewards and feedback; in settings where ground truth is sparse or non-deterministic, one practical source of such rewards is an LLM-as-a-Judge. Although LLM judges continue to improve, the literature has yet to introduce systems capable of enforcing standards with strong guarantees, particularly when bias vectors are unknown or adversarially discovered. To remedy this issue, we propose average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge. Evaluating on Arena-Hard-Auto with four LLM judges, we achieve (tau=0.5, delta=0.01) bias-bounded guarantees while retaining 61-99% correlation with original rankings across formatting and schematic bias settings, with most judge-bias combinations exceeding 80%. The code to reproduce our findings is available at https://github.com/penfever/bias-bounded-evaluation.

---

## 7. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis

**Authors**: Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, George H. Chen

**Published**: 2026-03-05

**arXiv ID**: 2603.05483v1

**PDF**: https://arxiv.org/pdf/2603.05483v1.pdf

**Abstract**:
Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragmented and inconsistent. We introduce SurvHTE-Bench, the first comprehensive benchmark for HTE estimation with censored outcomes. The benchmark spans (i) a modular suite of synthetic datasets with known ground truth, systematically varying causal assumptions and survival dynamics, (ii) semi-synthetic datasets that pair real-world covariates with simulated treatments and outcomes, and (iii) real-world datasets from a twin study (with known ground truth) and from an HIV clinical trial. Across synthetic, semi-synthetic, and real-world settings, we provide the first rigorous comparison of survival HTE methods under diverse conditions and realistic assumption violations. SurvHTE-Bench establishes a foundation for fair, reproducible, and extensible evaluation of causal survival methods. The data and code of our benchmark are available at: https://github.com/Shahriarnz14/SurvHTE-Bench .

---

## 8. Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval

**Authors**: Artem Vazhentsev, Maria Marina, Daniil Moskovskiy, Sergey Pletenev, Mikhail Seleznyov et al. (11 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05471v1

**PDF**: https://arxiv.org/pdf/2603.05471v1.pdf

**Abstract**:
Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the models intrinsic fact-verification capabilities largely unused. We propose the task of fact-checking without retrieval, focusing on the verification of arbitrary natural language claims, independent of their source. To study this setting, we introduce a comprehensive evaluation framework focused on generalization, testing robustness to (i) long-tail knowledge, (ii) variation in claim sources, (iii) multilinguality, and (iv) long-form generation. Across 9 datasets, 18 methods and 3 models, our experiments indicate that logit-based approaches often underperform compared to those that leverage internal model representations. Building on this finding, we introduce INTRA, a method that exploits interactions between internal representations and achieves state-of-the-art performance with strong generalization. More broadly, our work establishes fact-checking without retrieval as a promising research direction that can complement retrieval-based frameworks, improve scalability, and enable the use of such systems as reward signals during training or as components integrated into the generation process.

---

## 9. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry

**Authors**: Yifan Zhu, Mariah Bradford, Kenneth Lai, Timothy Obiso, Videep Venkatesha et al. (7 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05450v1

**PDF**: https://arxiv.org/pdf/2603.05450v1.pdf

**Abstract**:
Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

---

## 10. RealWonder: Real-Time Physical Action-Conditioned Video Generation

**Authors**: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05449v1

**PDF**: https://arxiv.org/pdf/2603.05449v1.pdf

**Abstract**:
Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

---

## 11. Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow

**Authors**: Yanda Yang, Sambeeta Das

**Published**: 2026-03-05

**arXiv ID**: 2603.05448v1

**PDF**: https://arxiv.org/pdf/2603.05448v1.pdf

**Abstract**:
Contact-rich micromanipulation in microfluidic flow is challenging because small disturbances can break pushing contact and induce large lateral drift. We study planar cell pushing with a magnetic rolling microrobot that tracks a waypoint-sampled reference curve under time-varying Poiseuille flow. We propose a hybrid controller that augments a nominal MPC with a learned residual policy trained by SAC. The policy outputs a bounded 2D velocity correction that is contact-gated, so residual actions are applied only during robot--cell contact, preserving reliable approach behavior and stabilizing learning. All methods share the same actuation interface and speed envelope for fair comparisons. Experiments show improved robustness and tracking accuracy over pure MPC and PID under nonstationary flow, with generalization from a clover training curve to unseen circle and square trajectories. A residual-bound sweep identifies an intermediate correction limit as the best trade-off, which we use in all benchmarks.

---

## 12. Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model

**Authors**: Dongwon Kim, Gawon Seo, Jinsung Lee, Minsu Cho, Suha Kwak

**Published**: 2026-03-05

**arXiv ID**: 2603.05438v1

**PDF**: https://arxiv.org/pdf/2603.05438v1.pdf

**Abstract**:
World models provide a powerful framework for simulating environment dynamics conditioned on actions or instructions, enabling downstream tasks such as action planning or policy learning. Recent approaches leverage world models as learned simulators, but its application to decision-time planning remains computationally prohibitive for real-time control. A key bottleneck lies in latent representations: conventional tokenizers encode each observation into hundreds of tokens, making planning both slow and resource-intensive. To address this, we propose CompACT, a discrete tokenizer that compresses each observation into as few as 8 tokens, drastically reducing computational cost while preserving essential information for planning. An action-conditioned world model that occupies CompACT tokenizer achieves competitive planning performance with orders-of-magnitude faster planning, offering a practical step toward real-world deployment of world models.

---

## 13. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning

**Authors**: Ye-Chan Kim, SeungJu Cha, Si-Woo Kim, Minju Jeon, Hyungee Kim et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05437v1

**PDF**: https://arxiv.org/pdf/2603.05437v1.pdf

**Abstract**:
Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically meaningful regions. Moreover, relying solely on ground-truth captions leads to sub-optimal performance due to the inherent sparsity of existing datasets. In this work, we propose SAIL, which constructs semantically-aware masks through cross-modal alignment. Our similarity aware training objective guides masks to emphasize video regions with high similarity to their corresponding event captions. Furthermore, to guide more accurate mask generation under sparse annotation settings, we introduce an LLM-based augmentation strategy that generates synthetic captions to provide additional alignment signals. These synthetic captions are incorporated through an inter-mask mechanism, providing auxiliary guidance for precise temporal localization without degrading the main objective. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance on both captioning and localization metrics.

---

## 14. Ensembling Language Models with Sequential Monte Carlo

**Authors**: Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, Clemente Pasti, Jacob Hoover Vigly et al. (8 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05432v1

**PDF**: https://arxiv.org/pdf/2603.05432v1.pdf

**Abstract**:
Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token probabilities yields samples from a locally normalized, biased approximation of the generally intractable ensemble distribution over strings. In this work, we introduce a unified framework for composing $K$ language models into $f$-ensemble distributions for a wide range of functions $f\colon\mathbb{R}_{\geq 0}^{K}\to\mathbb{R}_{\geq 0}$. To sample from these distributions, we propose a byte-level sequential Monte Carlo (SMC) algorithm that operates in a shared character space, enabling ensembles of models with mismatching vocabularies and consistent sampling in the limit. We evaluate a family of $f$-ensembles across prompt and model combinations for various structured text generation tasks, highlighting the benefits of alternative aggregation strategies over traditional probability averaging, and showing that better posterior approximations can yield better ensemble performance.

---

