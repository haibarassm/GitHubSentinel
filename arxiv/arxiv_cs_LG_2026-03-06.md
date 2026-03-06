# arXiv Papers - cs.LG
Date: 2026-03-06
Total Papers: 11

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

## 3. Cheap Thrills: Effective Amortized Optimization Using Inexpensive Labels

**Authors**: Khai Nguyen, Petros Ellinas, Anvita Bhagavathula, Priya Donti

**Published**: 2026-03-05

**arXiv ID**: 2603.05495v1

**PDF**: https://arxiv.org/pdf/2603.05495v1.pdf

**Abstract**:
To scale the solution of optimization and simulation problems, prior work has explored machine-learning surrogates that inexpensively map problem parameters to corresponding solutions. Commonly used approaches, including supervised and self-supervised learning with either soft or hard feasibility enforcement, face inherent challenges such as reliance on expensive, high-quality labels or difficult optimization landscapes. To address their trade-offs, we propose a novel framework that first collects "cheap" imperfect labels, then performs supervised pretraining, and finally refines the model through self-supervised learning to improve overall performance. Our theoretical analysis and merit-based criterion show that labeled data need only place the model within a basin of attraction, confirming that only modest numbers of inexact labels and training epochs are required. We empirically validate our simple three-stage strategy across challenging domains, including nonconvex constrained optimization, power-grid operation, and stiff dynamical systems, and show that it yields faster convergence; improved accuracy, feasibility, and optimality; and up to 59x reductions in total offline cost.

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

## 6. SurvHTE-Bench: A Benchmark for Heterogeneous Treatment Effect Estimation in Survival Analysis

**Authors**: Shahriar Noroozizadeh, Xiaobin Shen, Jeremy C. Weiss, George H. Chen

**Published**: 2026-03-05

**arXiv ID**: 2603.05483v1

**PDF**: https://arxiv.org/pdf/2603.05483v1.pdf

**Abstract**:
Estimating heterogeneous treatment effects (HTEs) from right-censored survival data is critical in high-stakes applications such as precision medicine and individualized policy-making. Yet, the survival analysis setting poses unique challenges for HTE estimation due to censoring, unobserved counterfactuals, and complex identification assumptions. Despite recent advances, from Causal Survival Forests to survival meta-learners and outcome imputation approaches, evaluation practices remain fragmented and inconsistent. We introduce SurvHTE-Bench, the first comprehensive benchmark for HTE estimation with censored outcomes. The benchmark spans (i) a modular suite of synthetic datasets with known ground truth, systematically varying causal assumptions and survival dynamics, (ii) semi-synthetic datasets that pair real-world covariates with simulated treatments and outcomes, and (iii) real-world datasets from a twin study (with known ground truth) and from an HIV clinical trial. Across synthetic, semi-synthetic, and real-world settings, we provide the first rigorous comparison of survival HTE methods under diverse conditions and realistic assumption violations. SurvHTE-Bench establishes a foundation for fair, reproducible, and extensible evaluation of causal survival methods. The data and code of our benchmark are available at: https://github.com/Shahriarnz14/SurvHTE-Bench .

---

## 7. Thermodynamic Response Functions in Singular Bayesian Models

**Authors**: Sean Plummer

**Published**: 2026-03-05

**arXiv ID**: 2603.05480v1

**PDF**: https://arxiv.org/pdf/2603.05480v1.pdf

**Abstract**:
Singular statistical models-including mixtures, matrix factorization, and neural networks-violate regular asymptotics due to parameter non-identifiability and degenerate Fisher geometry. Although singular learning theory characterizes marginal likelihood behavior through invariants such as the real log canonical threshold and singular fluctuation, these quantities remain difficult to interpret operationally. At the same time, widely used criteria such as WAIC and WBIC appear disconnected from underlying singular geometry. We show that posterior tempering induces a one-parameter deformation of the posterior distribution whose associated observables generate a hierarchy of thermodynamic response functions. A universal covariance identity links derivatives of tempered expectations to posterior fluctuations, placing WAIC, WBIC, and singular fluctuation within a unified response framework. Within this framework, classical quantities from singular learning theory acquire natural thermodynamic interpretations: RLCT governs the leading free-energy slope, singular fluctuation corresponds to curvature of the tempered free energy, and WAIC measures predictive fluctuation. We formalize an observable algebra that quotients out non-identifiable directions, allowing structurally meaningful order parameters to be constructed in singular models. Across canonical singular examples-including symmetric Gaussian mixtures, reduced-rank regression, and overparameterized neural networks-we empirically demonstrate phase-transition-like behavior under tempering. Order parameters collapse, susceptibilities peak, and complexity measures align with structural reorganization in posterior geometry. Our results suggest that thermodynamic response theory provides a natural organizing framework for interpreting complexity, predictive variability, and structural reorganization in singular Bayesian learning.

---

## 8. Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement

**Authors**: Priyanshi Singh, Krishna Bhatia

**Published**: 2026-03-05

**arXiv ID**: 2603.05468v1

**PDF**: https://arxiv.org/pdf/2603.05468v1.pdf

**Abstract**:
Real-time reconstruction of conditional quantum states from continuous measurement records is a fundamental requirement for quantum feedback control, yet standard stochastic master equation (SME) solvers require exact model specification, known system parameters, and are sensitive to parameter mismatch. While neural sequence models can fit these stochastic dynamics, the unconstrained predictors can violate physicality such as positivity or trace constraints, leading to unstable rollouts and unphysical estimates. We propose a Kraus-structured output layer that converts the hidden representation of a generic sequence backbone into a completely positive trace preserving (CPTP) quantum operation, yielding physically valid state updates by construction. We instantiate this layer across diverse backbones, RNN, GRU, LSTM, TCN, ESN and Mamba; including Neural ODE as a comparative baseline, on stochastic trajectories characterized by parameter drift. Our evaluation reveals distinct trade-offs between gating mechanisms, linear recurrence, and global attention. Across all models, Kraus-LSTM achieves the strongest results, improving state estimation quality by 7% over its unconstrained counterpart while guaranteeing physically valid predictions in non-stationary regimes.

---

## 9. Latent Wasserstein Adversarial Imitation Learning

**Authors**: Siqi Yang, Kai Yan, Alexander G. Schwing, Yu-Xiong Wang

**Published**: 2026-03-05

**arXiv ID**: 2603.05440v1

**PDF**: https://arxiv.org/pdf/2603.05440v1.pdf

**Abstract**:
Imitation Learning (IL) enables agents to mimic expert behavior by learning from demonstrations. However, traditional IL methods require large amounts of medium-to-high-quality demonstrations as well as actions of expert demonstrations, both of which are often unavailable. To reduce this need, we propose Latent Wasserstein Adversarial Imitation Learning (LWAIL), a novel adversarial imitation learning framework that focuses on state-only distribution matching. It benefits from the Wasserstein distance computed in a dynamics-aware latent space. This dynamics-aware latent space differs from prior work and is obtained via a pre-training stage, where we train the Intention Conditioned Value Function (ICVF) to capture a dynamics-aware structure of the state space using a small set of randomly generated state-only data. We show that this enhances the policy's understanding of state transitions, enabling the learning process to use only one or a few state-only expert episodes to achieve expert-level performance. Through experiments on multiple MuJoCo environments, we demonstrate that our method outperforms prior Wasserstein-based IL methods and prior adversarial IL methods, achieving better results across various tasks.

---

## 10. On-Policy Self-Distillation for Reasoning Compression

**Authors**: Hejian Sang, Yuanda Xu, Zhengze Zhou, Ran He, Zhipeng Wang et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05433v1

**PDF**: https://arxiv.org/pdf/2603.05433v1.pdf

**Abstract**:
Reasoning models think out loud, but much of what they say is noise. We introduce OPSDC (On-Policy Self-Distillation for Reasoning Compression), a method that teaches models to reason more concisely by
  distilling their own concise behavior back into themselves. The entire approach reduces to one idea: condition the same model on a "be concise" instruction to obtain teacher logits, and minimize per-token
  reverse KL on the student's own rollouts. No ground-truth answers, no token budgets, no difficulty estimators. Just self-distillation. Yet this simplicity belies surprising sophistication: OPSDC automatically
  compresses easy problems aggressively while preserving the deliberation needed for hard ones. On Qwen3-8B and Qwen3-14B, we achieve 57-59% token reduction on MATH-500 while improving accuracy by 9-16 points
  absolute. On AIME 2024, the 14B model gains 10 points with 41% compression. The secret? Much of what reasoning models produce is not just redundant-it is actively harmful, compounding errors with every
  unnecessary token.

---

## 11. Ensembling Language Models with Sequential Monte Carlo

**Authors**: Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, Clemente Pasti, Jacob Hoover Vigly et al. (8 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05432v1

**PDF**: https://arxiv.org/pdf/2603.05432v1.pdf

**Abstract**:
Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token probabilities yields samples from a locally normalized, biased approximation of the generally intractable ensemble distribution over strings. In this work, we introduce a unified framework for composing $K$ language models into $f$-ensemble distributions for a wide range of functions $f\colon\mathbb{R}_{\geq 0}^{K}\to\mathbb{R}_{\geq 0}$. To sample from these distributions, we propose a byte-level sequential Monte Carlo (SMC) algorithm that operates in a shared character space, enabling ensembles of models with mismatching vocabularies and consistent sampling in the limit. We evaluate a family of $f$-ensembles across prompt and model combinations for various structured text generation tasks, highlighting the benefits of alternative aggregation strategies over traditional probability averaging, and showing that better posterior approximations can yield better ensemble performance.

---

