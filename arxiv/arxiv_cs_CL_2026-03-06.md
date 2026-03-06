# arXiv Papers - cs.CL
Date: 2026-03-06
Total Papers: 10

## 1. POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation

**Authors**: Zeju Qiu, Lixin Liu, Adrian Weller, Han Shi, Weiyang Liu

**Published**: 2026-03-05

**arXiv ID**: 2603.05500v1

**PDF**: https://arxiv.org/pdf/2603.05500v1.pdf

**Abstract**:
Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In our experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

---

## 2. The Spike, the Sparse and the Sink: Anatomy of Massive Activations and Attention Sinks

**Authors**: Shangwen Sun, Alfredo Canziani, Yann LeCun, Jiachen Zhu

**Published**: 2026-03-05

**arXiv ID**: 2603.05498v1

**PDF**: https://arxiv.org/pdf/2603.05498v1.pdf

**Abstract**:
We study two recurring phenomena in Transformer language models: massive activations, in which a small number of tokens exhibit extreme outliers in a few channels, and attention sinks, in which certain tokens attract disproportionate attention mass regardless of semantic relevance. Prior work observes that these phenomena frequently co-occur and often involve the same tokens, but their functional roles and causal relationship remain unclear. Through systematic experiments, we show that the co-occurrence is largely an architectural artifact of modern Transformer design, and that the two phenomena serve related but distinct functions. Massive activations operate globally: they induce near-constant hidden representations that persist across layers, effectively functioning as implicit parameters of the model. Attention sinks operate locally: they modulate attention outputs across heads and bias individual heads toward short-range dependencies. We identify the pre-norm configuration as the key choice that enables the co-occurrence, and show that ablating it causes the two phenomena to decouple.

---

## 3. Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**Authors**: Helena Casademunt, Bartosz Cywiński, Khoi Tran, Arya Jakkli, Samuel Marks et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05494v1

**PDF**: https://arxiv.org/pdf/2603.05494v1.pdf

**Abstract**:
Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

---

## 4. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

**Authors**: Siddharth Boppana, Annabel Ma, Max Loeffler, Raphael Sarfati, Eric Bigelow et al. (8 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05488v1

**PDF**: https://arxiv.org/pdf/2603.05488v1.pdf

**Abstract**:
We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, 'aha' moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned "reasoning theater." Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.

---

## 5. Leveraging LLM Parametric Knowledge for Fact Checking without Retrieval

**Authors**: Artem Vazhentsev, Maria Marina, Daniil Moskovskiy, Sergey Pletenev, Mikhail Seleznyov et al. (11 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05471v1

**PDF**: https://arxiv.org/pdf/2603.05471v1.pdf

**Abstract**:
Trustworthiness is a core research challenge for agentic AI systems built on Large Language Models (LLMs). To enhance trust, natural language claims from diverse sources, including human-written text, web content, and model outputs, are commonly checked for factuality by retrieving external knowledge and using an LLM to verify the faithfulness of claims to the retrieved evidence. As a result, such methods are constrained by retrieval errors and external data availability, while leaving the models intrinsic fact-verification capabilities largely unused. We propose the task of fact-checking without retrieval, focusing on the verification of arbitrary natural language claims, independent of their source. To study this setting, we introduce a comprehensive evaluation framework focused on generalization, testing robustness to (i) long-tail knowledge, (ii) variation in claim sources, (iii) multilinguality, and (iv) long-form generation. Across 9 datasets, 18 methods and 3 models, our experiments indicate that logit-based approaches often underperform compared to those that leverage internal model representations. Building on this finding, we introduce INTRA, a method that exploits interactions between internal representations and achieves state-of-the-art performance with strong generalization. More broadly, our work establishes fact-checking without retrieval as a promising research direction that can complement retrieval-based frameworks, improve scalability, and enable the use of such systems as reward signals during training or as components integrated into the generation process.

---

## 6. NCTB-QA: A Large-Scale Bangla Educational Question Answering Dataset and Benchmarking Performance

**Authors**: Abrar Eyasir, Tahsin Ahmed, Muhammad Ibrahim

**Published**: 2026-03-05

**arXiv ID**: 2603.05462v1

**PDF**: https://arxiv.org/pdf/2603.05462v1.pdf

**Abstract**:
Reading comprehension systems for low-resource languages face significant challenges in handling unanswerable questions. These systems tend to produce unreliable responses when correct answers are absent from context. To solve this problem, we introduce NCTB-QA, a large-scale Bangla question answering dataset comprising 87,805 question-answer pairs extracted from 50 textbooks published by Bangladesh's National Curriculum and Textbook Board. Unlike existing Bangla datasets, NCTB-QA maintains a balanced distribution of answerable (57.25%) and unanswerable (42.75%) questions. NCTB-QA also includes adversarially designed instances containing plausible distractors. We benchmark three transformer-based models (BERT, RoBERTa, ELECTRA) and demonstrate substantial improvements through fine-tuning. BERT achieves 313% relative improvement in F1 score (0.150 to 0.620). Semantic answer quality measured by BERTScore also increases significantly across all models. Our results establish NCTB-QA as a challenging benchmark for Bangla educational question answering. This study demonstrates that domain-specific fine-tuning is critical for robust performance in low-resource settings.

---

## 7. DEBISS: a Corpus of Individual, Semi-structured and Spoken Debates

**Authors**: Klaywert Danillo Ferreira de Souza, David Eduardo Pereira, Cláudio E. C. Campelo, Larissa Lucena Vasconcelos

**Published**: 2026-03-05

**arXiv ID**: 2603.05459v1

**PDF**: https://arxiv.org/pdf/2603.05459v1.pdf

**Abstract**:
The process of debating is essential in our daily lives, whether in studying, work activities, simple everyday discussions, political debates on TV, or online discussions on social networks. The range of uses for debates is broad. Due to the diverse applications, structures, and formats of debates, developing corpora that account for these variations can be challenging, and the scarcity of debate corpora in the state of the art is notable. For this reason, the current research proposes the DEBISS corpus: a collection of spoken and individual debates with semi-structured features. With a broad range of NLP task annotations, such as speech-to-text, speaker diarization, argument mining, and debater quality assessment.

---

## 8. FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

**Authors**: Ted Zadouri, Markus Hoehnerbach, Jay Shah, Timmy Liu, Vijay Thakkar et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05451v1

**PDF**: https://arxiv.org/pdf/2603.05451v1.pdf

**Abstract**:
Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. While FlashAttention-3 optimized attention for Hopper GPUs through asynchronous execution and warp specialization, it primarily targets the H100 architecture. The AI industry has rapidly transitioned to deploying Blackwell-based systems such as the B200 and GB200, which exhibit fundamentally different performance characteristics due to asymmetric hardware scaling: tensor core throughput doubles while other functional units (shared memory bandwidth, exponential units) scale more slowly or remain unchanged. We develop several techniques to address these shifting bottlenecks on Blackwell GPUs: (1) redesigned pipelines that exploit fully asynchronous MMA operations and larger tile sizes, (2) software-emulated exponential and conditional softmax rescaling that reduces non-matmul operations, and (3) leveraging tensor memory and the 2-CTA MMA mode to reduce shared memory traffic and atomic adds in the backward pass. We demonstrate that our method, FlashAttention-4, achieves up to 1.3$\times$ speedup over cuDNN 9.13 and 2.7$\times$ over Triton on B200 GPUs with BF16, reaching up to 1613 TFLOPs/s (71% utilization). Beyond algorithmic innovations, we implement FlashAttention-4 entirely in CuTe-DSL embedded in Python, achieving 20-30$\times$ faster compile times compared to traditional C++ template-based approaches while maintaining full expressivity.

---

## 9. Distributed Partial Information Puzzles: Examining Common Ground Construction Under Epistemic Asymmetry

**Authors**: Yifan Zhu, Mariah Bradford, Kenneth Lai, Timothy Obiso, Videep Venkatesha et al. (7 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05450v1

**PDF**: https://arxiv.org/pdf/2603.05450v1.pdf

**Abstract**:
Establishing common ground, a shared set of beliefs and mutually recognized facts, is fundamental to collaboration, yet remains a challenge for current AI systems, especially in multimodal, multiparty settings, where the collaborators bring different information to the table. We introduce the Distributed Partial Information Puzzle (DPIP), a collaborative construction task that elicits rich multimodal communication under epistemic asymmetry. We present a multimodal dataset of these interactions, annotated and temporally aligned across speech, gesture, and action modalities to support reasoning over propositional content and belief dynamics. We then evaluate two paradigms for modeling common ground (CG): (1) state-of-the-art large language models (LLMs), prompted to infer shared beliefs from multimodal updates, and (2) an axiomatic pipeline grounded in Dynamic Epistemic Logic (DEL) that incrementally performs the same task. Results on the annotated DPIP data indicate that it poses a challenge to modern LLMs' abilities to track both task progression and belief state.

---

## 10. Ensembling Language Models with Sequential Monte Carlo

**Authors**: Robin Shing Moon Chan, Tianyu Liu, Samuel Kiegeland, Clemente Pasti, Jacob Hoover Vigly et al. (8 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05432v1

**PDF**: https://arxiv.org/pdf/2603.05432v1.pdf

**Abstract**:
Practitioners have access to an abundance of language models and prompting strategies for solving many language modeling tasks; yet prior work shows that modeling performance is highly sensitive to both choices. Classical machine learning ensembling techniques offer a principled approach: aggregate predictions from multiple sources to achieve better performance than any single one. However, applying ensembling to language models during decoding is challenging: naively aggregating next-token probabilities yields samples from a locally normalized, biased approximation of the generally intractable ensemble distribution over strings. In this work, we introduce a unified framework for composing $K$ language models into $f$-ensemble distributions for a wide range of functions $f\colon\mathbb{R}_{\geq 0}^{K}\to\mathbb{R}_{\geq 0}$. To sample from these distributions, we propose a byte-level sequential Monte Carlo (SMC) algorithm that operates in a shared character space, enabling ensembles of models with mismatching vocabularies and consistent sampling in the limit. We evaluate a family of $f$-ensembles across prompt and model combinations for various structured text generation tasks, highlighting the benefits of alternative aggregation strategies over traditional probability averaging, and showing that better posterior approximations can yield better ensemble performance.

---

