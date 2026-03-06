# arXiv Papers - cs.CV
Date: 2026-03-06
Total Papers: 12

## 1. Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups

**Authors**: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko et al. (7 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05507v1

**PDF**: https://arxiv.org/pdf/2603.05507v1.pdf

**Abstract**:
High-quality 3D streaming from multiple cameras is crucial for immersive experiences in many AR/VR applications. The limited number of views - often due to real-time constraints - leads to missing information and incomplete surfaces in the rendered images. Existing approaches typically rely on simple heuristics for the hole filling, which can result in inconsistencies or visual artifacts. We propose to complete the missing textures using a novel, application-targeted inpainting method independent of the underlying representation as an image-based post-processing step after the novel view rendering. The method is designed as a standalone module compatible with any calibrated multi-camera system. For this we introduce a multi-view aware, transformer-based network architecture using spatio-temporal embeddings to ensure consistency across frames while preserving fine details. Additionally, our resolution-independent design allows adaptation to different camera setups, while an adaptive patch selection strategy balances inference speed and quality, allowing real-time performance. We evaluate our approach against state-of-the-art inpainting techniques under the same real-time constraints and demonstrate that our model achieves the best trade-off between quality and speed, outperforming competitors in both image and video-based metrics.

---

## 2. FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning

**Authors**: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu

**Published**: 2026-03-05

**arXiv ID**: 2603.05506v1

**PDF**: https://arxiv.org/pdf/2603.05506v1.pdf

**Abstract**:
We introduce FaceCam, a system that generates video under customizable camera trajectories for monocular human portrait video input. Recent camera control approaches based on large video-generation models have shown promising progress but often exhibit geometric distortions and visual artifacts on portrait videos due to scale-ambiguous camera representations or 3D reconstruction errors. To overcome these limitations, we propose a face-tailored scale-aware representation for camera transformations that provides deterministic conditioning without relying on 3D priors. We train a video generation model on both multi-view studio captures and in-the-wild monocular videos, and introduce two camera-control data generation strategies: synthetic camera motion and multi-shot stitching, to exploit stationary training cameras while generalizing to dynamic, continuous camera trajectories at inference time. Experiments on Ava-256 dataset and diverse in-the-wild videos demonstrate that FaceCam achieves superior performance in camera controllability, visual quality, identity and motion preservation.

---

## 3. Accelerating Text-to-Video Generation with Calibrated Sparse Attention

**Authors**: Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar

**Published**: 2026-03-05

**arXiv ID**: 2603.05503v1

**PDF**: https://arxiv.org/pdf/2603.05503v1.pdf

**Abstract**:
Recent diffusion models enable high-quality video generation, but suffer from slow runtimes. The large transformer-based backbones used in these models are bottlenecked by spatiotemporal attention. In this paper, we identify that a significant fraction of token-to-token connections consistently yield negligible scores across various inputs, and their patterns often repeat across queries. Thus, the attention computation in these cases can be skipped with little to no effect on the result. This observation continues to hold for connections among local token blocks. Motivated by this, we introduce CalibAtt, a training-free method that accelerates video generation via calibrated sparse attention. CalibAtt performs an offline calibration pass that identifies block-level sparsity and repetition patterns that are stable across inputs, and compiles these patterns into optimized attention operations for each layer, head, and diffusion timestep. At inference time, we compute the selected input-dependent connections densely, and skip the unselected ones in a hardware-efficient manner. Extensive experiments on Wan 2.1 14B, Mochi 1, and few-step distilled models at various resolutions show that CalibAtt achieves up to 1.58x end-to-end speedup, outperforming existing training-free methods while maintaining video generation quality and text-video alignment.

---

## 4. Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline

**Authors**: Guo Chen, Lidong Lu, Yicheng Liu, Liangrui Dong, Lidong Zou et al. (20 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05484v1

**PDF**: https://arxiv.org/pdf/2603.05484v1.pdf

**Abstract**:
While datasets for video understanding have scaled to hour-long durations, they typically consist of densely concatenated clips that differ from natural, unscripted daily life. To bridge this gap, we introduce MM-Lifelong, a dataset designed for Multimodal Lifelong Understanding. Comprising 181.1 hours of footage, it is structured across Day, Week, and Month scales to capture varying temporal densities. Extensive evaluations reveal two critical failure modes in current paradigms: end-to-end MLLMs suffer from a Working Memory Bottleneck due to context saturation, while representative agentic baselines experience Global Localization Collapse when navigating sparse, month-long timelines. To address this, we propose the Recursive Multimodal Agent (ReMA), which employs dynamic memory management to iteratively update a recursive belief state, significantly outperforming existing methods. Finally, we establish dataset splits designed to isolate temporal and domain biases, providing a rigorous foundation for future research in supervised learning and out-of-distribution generalization.

---

## 5. Towards 3D Scene Understanding of Gas Plumes in LWIR Hyperspectral Images Using Neural Radiance Fields

**Authors**: Scout Jarman, Zigfried Hampel-Arias, Adra Carr, Kevin R. Moon

**Published**: 2026-03-05

**arXiv ID**: 2603.05473v1

**PDF**: https://arxiv.org/pdf/2603.05473v1.pdf

**Abstract**:
Hyperspectral images (HSI) have many applications, ranging from environmental monitoring to national security, and can be used for material detection and identification. Longwave infrared (LWIR) HSI can be used for gas plume detection and analysis. Oftentimes, only a few images of a scene of interest are available and are analyzed individually. The ability to combine information from multiple images into a single, cohesive representation could enhance analysis by providing more context on the scene's geometry and spectral properties. Neural radiance fields (NeRFs) create a latent neural representation of volumetric scene properties that enable novel-view rendering and geometry reconstruction, offering a promising avenue for hyperspectral 3D scene reconstruction. We explore the possibility of using NeRFs to create 3D scene reconstructions from LWIR HSI and demonstrate that the model can be used for the basic downstream analysis task of gas plume detection. The physics-based DIRSIG software suite was used to generate a synthetic multi-view LWIR HSI dataset of a simple facility with a strong sulfur hexafluoride gas plume. Our method, built on the standard Mip-NeRF architecture, combines state-of-the-art methods for hyperspectral NeRFs and sparse-view NeRFs, along with a novel adaptive weighted MSE loss. Our final NeRF method requires around 50% fewer training images than the standard Mip-NeRF and achieves an average PSNR of 39.8 dB with as few as 30 training images. Gas plume detection applied to NeRF-rendered test images using the adaptive coherence estimator achieves an average AUC of 0.821 when compared with detection masks generated from ground-truth test images.

---

## 6. HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token

**Authors**: Sai Akhil Kogilathota, Sripadha Vallabha E G, Luzhe Sun, Jiawei Zhou

**Published**: 2026-03-05

**arXiv ID**: 2603.05465v1

**PDF**: https://arxiv.org/pdf/2603.05465v1.pdf

**Abstract**:
Hallucinations remain a persistent challenge for vision-language models (VLMs), which often describe nonexistent objects or fabricate facts. Existing detection methods typically operate after text generation, making intervention both costly and untimely. We investigate whether hallucination risk can instead be predicted before any token is generated by probing a model's internal representations in a single forward pass. Across a diverse set of vision-language tasks and eight modern VLMs, including Llama-3.2-Vision, Gemma-3, Phi-4-VL, and Qwen2.5-VL, we examine three families of internal representations: (i) visual-only features without multimodal fusion, (ii) vision-token representations within the text decoder, and (iii) query-token representations that integrate visual and textual information before generation. Probes trained on these representations achieve strong hallucination-detection performance without decoding, reaching up to 0.93 AUROC on Gemma-3-12B, Phi-4-VL 5.6B, and Molmo 7B. Late query-token states are the most predictive for most models, while visual or mid-layer features dominate in a few architectures (e.g., ~0.79 AUROC for Qwen2.5-VL-7B using visual-only features). These results demonstrate that (1) hallucination risk is detectable pre-generation, (2) the most informative layer and modality vary across architectures, and (3) lightweight probes have the potential to enable early abstention, selective routing, and adaptive decoding to improve both safety and efficiency.

---

## 7. EdgeDAM: Real-time Object Tracking for Mobile Devices

**Authors**: Syed Muhammad Raza, Syed Murtaza Hussain Abidi, Khawar Islam, Muhammad Ibrahim, Ajmal Saeed Mian

**Published**: 2026-03-05

**arXiv ID**: 2603.05463v1

**PDF**: https://arxiv.org/pdf/2603.05463v1.pdf

**Abstract**:
Single-object tracking (SOT) on edge devices is a critical computer vision task, requiring accurate and continuous target localization across video frames under occlusion, distractor interference, and fast motion. However, recent state-of-the-art distractor-aware memory mechanisms are largely built on segmentation-based trackers and rely on mask prediction and attention-driven memory updates, which introduce substantial computational overhead and limit real-time deployment on resource-constrained hardware; meanwhile, lightweight trackers sustain high throughput but are prone to drift when visually similar distractors appear. To address these challenges, we propose EdgeDAM, a lightweight detection-guided tracking framework that reformulates distractor-aware memory for bounding-box tracking under strict edge constraints. EdgeDAM introduces two key strategies: (1) Dual-Buffer Distractor-Aware Memory (DAM), which integrates a Recent-Aware Memory to preserve temporally consistent target hypotheses and a Distractor-Resolving Memory to explicitly store hard negative candidates and penalize their re-selection during recovery; and (2) Confidence-Driven Switching with Held-Box Stabilization, where tracker reliability and temporal consistency criteria adaptively activate detection and memory-guided re-identification during occlusion, while a held-box mechanism temporarily freezes and expands the estimate to suppress distractor contamination. Extensive experiments on five benchmarks, including the distractor-focused DiDi dataset, demonstrate improved robustness under occlusion and fast motion while maintaining real-time performance on mobile devices, achieving 88.2% accuracy on DiDi and 25 FPS on an iPhone 15. Code will be released.

---

## 8. Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes

**Authors**: Pengxiang Li, Joey Tsai, Hongwei Xue, Kunyu Shi, Shilin Yan

**Published**: 2026-03-05

**arXiv ID**: 2603.05454v1

**PDF**: https://arxiv.org/pdf/2603.05454v1.pdf

**Abstract**:
Diffusion Language Models (DLMs) promise highly parallel text generation, yet their practical inference speed is often bottlenecked by suboptimal decoding schedulers. Standard approaches rely on 'scattered acceptance'-committing high confidence tokens at disjoint positions throughout the sequence. This approach inadvertently fractures the Key-Value (KV) cache, destroys memory locality, and forces the model into costly, repeated repairs across unstable token boundaries. To resolve this, we present the Longest Stable Prefix (LSP) scheduler, a training-free and model-agnostic inference paradigm based on monolithic prefix absorption. In each denoising step, LSP evaluates token stability via a single forward pass, dynamically identifies a contiguous left-aligned block of stable predictions, and snaps its boundary to natural linguistic or structural delimiters before an atomic commitment. This prefix-first topology yields dual benefits: systemically, it converts fragmented KV cache updates into efficient, contiguous appends; algorithmically, it preserves bidirectional lookahead over a geometrically shrinking active suffix, drastically reducing token flip rates and denoiser calls. Extensive evaluations on LLaDA-8B and Dream-7B demonstrate that LSP accelerates inference by up to 3.4x across rigorous benchmarks including mathematical reasoning, code generation, multilingual (CJK) tasks, and creative writing while matching or slightly improving output quality. By fundamentally restructuring the commitment topology, LSP bridges the gap between the theoretical parallelism of DLMs and practical hardware efficiency.

---

## 9. RealWonder: Real-Time Physical Action-Conditioned Video Generation

**Authors**: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05449v1

**PDF**: https://arxiv.org/pdf/2603.05449v1.pdf

**Abstract**:
Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

---

## 10. NaiLIA: Multimodal Nail Design Retrieval Based on Dense Intent Descriptions and Palette Queries

**Authors**: Kanon Amemiya, Daichi Yashima, Kei Katsumata, Takumi Komatsu, Ryosuke Korekata et al. (7 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05446v1

**PDF**: https://arxiv.org/pdf/2603.05446v1.pdf

**Abstract**:
We focus on the task of retrieving nail design images based on dense intent descriptions, which represent multi-layered user intent for nail designs. This is challenging because such descriptions specify unconstrained painted elements and pre-manufactured embellishments as well as visual characteristics, themes, and overall impressions. In addition to these descriptions, we assume that users provide palette queries by specifying zero or more colors via a color picker, enabling the expression of subtle and continuous color nuances. Existing vision-language foundation models often struggle to incorporate such descriptions and palettes. To address this, we propose NaiLIA, a multimodal retrieval method for nail design images, which comprehensively aligns with dense intent descriptions and palette queries during retrieval. Our approach introduces a relaxed loss based on confidence scores for unlabeled images that can align with the descriptions. To evaluate NaiLIA, we constructed a benchmark consisting of 10,625 images collected from people with diverse cultural backgrounds. The images were annotated with long and dense intent descriptions given by over 200 annotators. Experimental results demonstrate that NaiLIA outperforms standard methods.

---

## 11. Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model

**Authors**: Dongwon Kim, Gawon Seo, Jinsung Lee, Minsu Cho, Suha Kwak

**Published**: 2026-03-05

**arXiv ID**: 2603.05438v1

**PDF**: https://arxiv.org/pdf/2603.05438v1.pdf

**Abstract**:
World models provide a powerful framework for simulating environment dynamics conditioned on actions or instructions, enabling downstream tasks such as action planning or policy learning. Recent approaches leverage world models as learned simulators, but its application to decision-time planning remains computationally prohibitive for real-time control. A key bottleneck lies in latent representations: conventional tokenizers encode each observation into hundreds of tokens, making planning both slow and resource-intensive. To address this, we propose CompACT, a discrete tokenizer that compresses each observation into as few as 8 tokens, drastically reducing computational cost while preserving essential information for planning. An action-conditioned world model that occupies CompACT tokenizer achieves competitive planning performance with orders-of-magnitude faster planning, offering a practical step toward real-world deployment of world models.

---

## 12. SAIL: Similarity-Aware Guidance and Inter-Caption Augmentation-based Learning for Weakly-Supervised Dense Video Captioning

**Authors**: Ye-Chan Kim, SeungJu Cha, Si-Woo Kim, Minju Jeon, Hyungee Kim et al. (6 authors)

**Published**: 2026-03-05

**arXiv ID**: 2603.05437v1

**PDF**: https://arxiv.org/pdf/2603.05437v1.pdf

**Abstract**:
Weakly-Supervised Dense Video Captioning aims to localize and describe events in videos trained only on caption annotations, without temporal boundaries. Prior work introduced an implicit supervision paradigm based on Gaussian masking and complementary captioning. However, existing method focuses merely on generating non-overlapping masks without considering their semantic relationship to corresponding events, resulting in simplistic, uniformly distributed masks that fail to capture semantically meaningful regions. Moreover, relying solely on ground-truth captions leads to sub-optimal performance due to the inherent sparsity of existing datasets. In this work, we propose SAIL, which constructs semantically-aware masks through cross-modal alignment. Our similarity aware training objective guides masks to emphasize video regions with high similarity to their corresponding event captions. Furthermore, to guide more accurate mask generation under sparse annotation settings, we introduce an LLM-based augmentation strategy that generates synthetic captions to provide additional alignment signals. These synthetic captions are incorporated through an inter-mask mechanism, providing auxiliary guidance for precise temporal localization without degrading the main objective. Experiments on ActivityNet Captions and YouCook2 demonstrate state-of-the-art performance on both captioning and localization metrics.

---

