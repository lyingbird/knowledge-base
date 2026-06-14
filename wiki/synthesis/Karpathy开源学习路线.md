---
tags: [综合, 学习路线, 开源, Karpathy, LLM]
created: 2026-06-14
updated: 2026-06-14
sources: [https://github.com/karpathy?tab=repositories, raw/repos/multica-ai-andrej-karpathy-skills.md]
---

# Karpathy 开源学习路线

> 把 Andrej Karpathy 的代表性开源仓库排成一条由浅入深的学习路线：从标量自动微分（micrograd）一路到能从零训练并部署一个小型 ChatGPT（nanochat）。每个仓库后续单独建 source 学习页深入消化。

## 为什么按这条线学

Karpathy 的仓库共享一个理念：**用最少、最干净的代码把一个核心机制讲透**（micrograd 约百行讲反向传播，llama2.c 一个 C 文件做推理）。按「自动微分 → 语言模型基础 → Transformer/GPT → 分词 → 训练系统/底层 → 端到端 ChatGPT」的顺序学，能把现代 LLM 的每一层都亲手搭一遍，对应本库技术支柱 [[AI技术与开源学习]]。配套理论课是 `nn-zero-to-hero` 视频系列。

## 推荐学习顺序（优先级从高到低）

| 优先级 | 仓库 | 语言/星标 | 学什么 | 前置 |
|---|---|---|---|---|
| 1 | **micrograd** | Jupyter · 16k+ | 标量自动微分引擎 + 类 PyTorch 神经网络；理解反向传播的最小内核 | 无 |
| 2 | **makemore** | Python · 4k | 字符级自回归语言模型，从 bigram 到 MLP；建模/采样/loss 直觉 | micrograd |
| 3 | **minbpe** | Python · 10k+ | BPE 分词算法的最小实现；LLM tokenization 的底层 | makemore |
| 4 | **minGPT** | Python · 24k+ | 干净的 GPT 训练最小复现；Transformer 结构落地 | makemore |
| 5 | **nanoGPT** | Python · 59k+ | minGPT 的「可实战」版本，训练/微调中型 GPT 的最简最快仓库 | minGPT |
| 6 | **llama2.c** | C · 19k+ | 纯 C 单文件做 Llama 2 推理；理解推理引擎与权重布局 | nanoGPT |
| 7 | **llm.c** | CUDA · 30k+ | 用裸 C/CUDA 训练 LLM；深入训练系统与 GPU 底层 | nanoGPT + C/CUDA |
| 8 | **nanochat** | Python · 55k+ | 「100 美元能买到的最好 ChatGPT」，从零训练 + 部署端到端小型 ChatGPT | nanoGPT 全链路 |
| 旁支 | **nn-zero-to-hero** | Jupyter · 23k+ | 配套理论视频课，贯穿上面多数仓库 | 与 1–5 并行 |
| 旁支 | **char-rnn** | Lua · 12k | 历史经典：字符级 RNN/LSTM；理解 Transformer 之前的序列建模 | 选学 |
| 旁支 | **llm-council** / **autoresearch** | Python | 近期 agent/多模型协作类项目；学完核心线后再看 | nanochat |

（星标为 2026-06-14 抓取，约数；具体见 [[03-核验/待核验事实]]。）

## 学习方式

按 `.wiki-schema.md` 的「GitHub / 开源项目学习素材 Ingest 规范」逐仓库处理：每个仓库建一页 `wiki/sources/`，含项目定位、核心方法、动手清单（跑通最小示例）、可复用知识；把共性概念（如「自回归」「注意力」「BPE」「KV cache」）提为 `wiki/entities/`，逐步织成网络。

## 进度

- [ ] micrograd
- [ ] makemore
- [ ] minbpe
- [ ] minGPT
- [ ] nanoGPT
- [ ] llama2.c
- [ ] llm.c
- [ ] nanochat
- [x] 方法论旁支：[[Karpathy编码原则与Claude-Code-Skills]]（第三方整理，非 Karpathy 本人仓库）

## 相关页面

- [[AI技术与开源学习]]
- [[Karpathy编码原则与Claude-Code-Skills]]
- [[基础模型]]
- [[LLM编码原则]]
