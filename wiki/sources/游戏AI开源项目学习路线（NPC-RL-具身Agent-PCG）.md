---
tags: [素材, GitHub, 项目学习, 游戏AI, AI技术与开源学习]
created: 2026-07-01
updated: 2026-07-01
sources: [raw/repos/game-ai-projects.md, https://github.com/joonspk-research/generative_agents, https://github.com/MineDojo/Voyager, https://github.com/linyiLYi/street-fighter-ai]
---

# 游戏AI开源项目学习路线（NPC/RL/具身Agent/PCG）

> 一句话定位：把「游戏 + AI」四条技术路线的代表性开源项目串成可动手复现的学习路线——生成式 NPC、RL 玩游戏、LLM 具身 Agent、程序化关卡生成。为知识库技术/学习支柱补上游戏 AI 的实操落点。

## 来源

- 原始副本：`raw/repos/game-ai-projects.md`（含仓库地址/star/论文/动手步骤，2026-07-01 联网抓取）
- 四个项目 URL 见各节；star 为抓取时量级约数。

## 项目定位与学习顺序

四个项目对应游戏 AI 的四条技术路线，建议按「入门→进阶」顺序：

1. **RL 玩游戏（入门）** → linyiLYi/street-fighter-ai
2. **生成式 NPC（核心）** → joonspk-research/generative_agents（斯坦福小镇）
3. **LLM 具身 Agent（进阶）** → MineDojo/Voyager
4. **程序化关卡生成（专题）** → amidos2006/gym-pcgrl

## 各项目要点

### 1. street-fighter-ai（RL 玩游戏，约 6.5k star）
- 仅凭 RGB 像素 + PPO + Gym Retro + Stable-Baselines3 训练 AI 打通街霸 II BOSS；提出「惩罚衰减」缓解过度保守。
- 作者 B 站「林亦LYi」，有中文讲解——RL 玩游戏最低门槛的第一站。
- **已在库内出现**：[[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]] 讲游戏 AI 史时提及。

### 2. generative_agents（斯坦福小镇，约 21.7k star）
- 用 LLM 驱动 25 个可信 NPC；核心认知架构：**记忆流 + 检索 + 反思 + 规划**。
- 论文《Generative Agents》(UIST '23, Joon Sung Park / Percy Liang / Michael Bernstein)。
- **是理解 AI NPC 的奠基性实现**——库内 [[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]] 与 [[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]] 反复对照的「斯坦福小镇」正是它；也印证了「记忆系统」是 NPC 灵魂（呼应 [[AI NPC]] 四维记忆、[[Agent Harness]] 多层记忆）。

### 3. Voyager（Minecraft LLM Agent，约 7k star）
- GPT-4 驱动的终身学习具身智能体，三组件：自动课程 + 技能库（可执行代码）+ 迭代提示。
- 论文 arXiv:2305.16291（NVIDIA/Caltech，Jim Fan / Anima Anandkumar 等）。
- **「LLM 作为游戏智能体大脑」代表作**——技能库/自动课程思想与 [[Agent Harness]]、[[智能体编排]] 相通。

### 4. gym-pcgrl（PCG，约 130+ star，学术向）
- 把程序化关卡生成建模为 RL 问题（PCGRL），支持推箱子/塞尔达/马里奥等。
- 论文 AIIDE 2020（NYU Game Innovation Lab, Togelius 等）——生成式关卡的权威开源起点。

## 可复用知识

- **记忆架构是 NPC 的核心**：斯坦福小镇的「记忆流+反思」→ 和平精英「四维记忆」→ Hermes/OpenClaw「多层记忆」，跨项目一致印证 [[游戏AI NPC两路线对比]] 的「记忆 > 智能」。
- **技能库 + 自动课程**：Voyager 展示 Agent 如何自主积累可复用技能，对游戏内 AI 队友/NPC 的成长设计有参考。
- **RL 玩游戏 vs LLM 做 Agent**：street-fighter-ai（像素+PPO，操作精准无情）与 Voyager（LLM 规划）代表两种 game AI 范式，对应 [[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]] 里「强化学习像 BOSS 战、很难成队友」的判断。

## 动手清单（最小复现）

- **street-fighter-ai**：Conda py3.8.10 → `pip install -r requirements.txt` → 拷配置进 gym-retro 目录 → 合法 ROM 存 rom.md → `python test.py`（跑预训练）/`train.py`。
- **generative_agents**：backend 填 OpenAI key → `pip install -r requirements.txt` → frontend `manage.py runserver` → backend `reverie.py` 输入 `run <步数>` → 浏览器 `localhost:8000/simulator_home`。
- **Voyager**：`pip install -e .` → env/mineflayer 装 Node 依赖 → 搭 Minecraft + Fabric mods → 配 OpenAI key → `voyager.learn()`。
- 依赖约束：均需 OpenAI API key（除 street-fighter-ai）；Voyager 需 Minecraft 正版 + Node 环境；street-fighter-ai 需合法 ROM。

## 局限与适用边界

- 三个 LLM 项目都强依赖 GPT API（成本/延迟），与游戏「手机端实时」需求有差距——这正是和平精英选择「小模型编排」而非大模型直连的原因（见 [[游戏AI NPC两路线对比]]）。
- 斯坦福小镇/Voyager 是研究原型，「聪明但不一定好玩」（见 [[AI无法取代的核心竞争力]]）。

## 待核验事实

见 [[03-核验/待核验事实]]：各仓库 star 数（抓取时约数，随时间变动）、论文与作者信息以仓库/arXiv 实际页面为准。

## 相关页面

- [[AI技术与开源学习]]
- [[AI游戏与虚拟世界]]
- [[AI NPC]]
- [[游戏AI NPC两路线对比]]
- [[Agent Harness]]
- [[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]]
- [[Karpathy开源学习路线]]
