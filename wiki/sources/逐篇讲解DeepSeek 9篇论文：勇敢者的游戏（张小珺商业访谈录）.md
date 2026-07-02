---
tags: [素材, 视频, 技术讲解, 基础模型, DeepSeek, 强化学习, 张小珺商业访谈录]
created: 2026-07-01
updated: 2026-07-01
sources: [raw/notes/video-transcripts/逐篇讲解DeepSeek关键9篇论文及创新点——“勇敢者的游戏”.transcript.txt, https://www.bilibili.com/video/BV1xuK5eREJi]
---

# 逐篇讲解DeepSeek 9篇论文：勇敢者的游戏（张小珺商业访谈录）

> 何俊贤（港科大助理教授）逐篇讲解 DeepSeek 关键 9 篇论文。主线：DeepSeek 的成功是「论文序列的胜利」——从基座→MoE→MLA→GRPO/R1，两大原创算法（**MLA** 注意力、**GRPO** 强化学习）+ 工程化创新（FP8/MTP），核心哲学是「成本理性 + 技术远见 + 执行力」，不跟风、敢独走。

## 来源

- 视频：《逐篇讲解 DeepSeek 关键 9 篇论文及创新点——"勇敢者的游戏"》（张小珺「技术之美」系列）
- UP 主：张小珺商业访谈录 | 讲解者：何俊贤（港科大计算机系助理教授，大模型推理/对齐/评测方向，R1 发布 5 天内做过复现）
- BV1xuK5eREJi | 时长 200:54 | 中文 | 抓取 2026-07-01｜faster-whisper large-v3
- 原始转写：`raw/notes/video-transcripts/逐篇讲解DeepSeek关键9篇论文….transcript.txt`

## 核心内容

归因边界：学者对公开论文的讲解与判断；参数/卡数/成本以论文原文为准，需核验。技术向内容，术语较多。

### 9 篇论文与创新点

1. **DeepSeek LLM（基座）**：严谨复现 Llama 2，首次系统做超参数 scaling 调查，坦诚公开刷榜方式与缺陷——奠定「诚实 + 重细节」文化。
2. **DeepSeek-MoE**：Dense→MoE，多 Expert + **Shared Expert** 机制，为降本（约降 40%），不 follow Llama/Mistral。
3. **DeepSeek-Coder**：代码专用，引入 Reward Model 做 RL（后被 R1 放弃）。
4. **DeepSeek V2**：**MLA（Multi-head Latent Attention）原创**——大幅降 KV Cache、提推理效率；用「较差的 GPU」（老 A100）训出强模型。MLA 至今是 DeepSeek 独特优势。
5. **DeepSeek-Math 7B**：数学推理，初期用过程监督奖励模型（后证明是弯路）。
6. **DeepSeek-Prover / V1.5**：定理证明推理。
7. **DeepSeek V3**：**MTP（多 token 预测）** 首次大规模成功 + **FP8 训练**极致降本 + 沿袭 MLA；用约 2000 张 H800（远少于业界上万卡）。
8. **DeepSeek-R1**：**GRPO（Group Relative Policy Optimization）原创** RL 算法——抛弃过程奖励模型的弯路，改**规则导向奖励**（数学查答案、代码跑 unit test）+ **Online RL**（边生成边更新）；发现规则奖励比 Reward Model 更 effective（简单即最优），支持长链思维，打破 OpenAI o1 垄断。
9. **DeepSeek-R1-Zero**：无监督 RL 版本，纯 RL 信号从零学会推理，展现 RL 潜力。

### 两大原创 + 工程化

- **MLA**（V2）、**GRPO**（R1）是原创算法；**FP8 训练、MTP、MoE Shared Expert、Online RL** 是「非原创但首次成功大规模应用」的工程化创新。
- **成本至上哲学**：每个创新都问「如何降本增效」，不炫技——这正是「业界复制难、难以追上」的原因。

### 「勇敢者的游戏」

不跟风（不照抄 Llama/OpenAI）、敢尝试（弱 GPU 训强模型、2000 卡 vs 上万卡、RL 先失败半年再用 Online RL 成功）、低调有实力（论文学院派、不浮夸）、敢独走（MLA/GRPO 出现时业界都还在别的路上）。

## 对知识库的价值

- **技术支柱核心素材**：补强 [[基础模型]]、[[AI技术与开源学习]]——DeepSeek 技术路线的系统拆解（MLA/GRPO/MoE/FP8）。
- **与库内大模型访谈交叉**：与 [[杨植麟谈K2与Agentic LLM（张小珺商业访谈录）]]（RL/系统工程）、[[智谱张鹏：全球大模型第一股上市访谈（张小珺商业访谈录）]]（成本工程/DeepSeek 冲击后反思）、[[罗福莉谈AI范式巨变与OpenClaw（张小珺商业访谈录）]]（罗福莉是 DeepSeek V2 核心作者之一）直接呼应。
- **成本效率路线**：与 [[MiniMax闫俊杰谈M3与10T模型（十字路口）]] 的「Scaling 失效/工程化」、[[复盘2025年AI和科技大事件（十字路口）]] 的「DeepSeek 开年冲击」形成完整叙事。

## 待核验事实

见 [[03-核验/待核验事实]]：DeepSeek 早期约 5000 张 A100 + V3 约 2000 张 H800、MoE 降本约 40%、V2 参数 200+ 亿/2.788 万亿 tokens、MoE-1.45B 激活 2.8B、MLA/GRPO 归属 DeepSeek 原创等——以论文原文为准。

## 相关页面

- [[基础模型]]
- [[AI技术与开源学习]]
- [[杨植麟谈K2与Agentic LLM（张小珺商业访谈录）]]
- [[智谱张鹏：全球大模型第一股上市访谈（张小珺商业访谈录）]]
- [[罗福莉谈AI范式巨变与OpenClaw（张小珺商业访谈录）]]
- [[MiniMax闫俊杰谈M3与10T模型（十字路口）]]
- [[张小珺商业访谈录]]
