---
tags: [素材, 视频, AIBuilder, 英文原音, OpenAI, Harness, Agent Harness, AI原生组织]
created: 2026-07-12
updated: 2026-07-12
sources: [01-原始素材/B站转录/AI前沿人物/BV1zkdWBTEFo.md, https://www.bilibili.com/video/BV1zkdWBTEFo]
---

# OpenAI 的 Harness 工程实践（Ryan Lopopolo 访谈）

> OpenAI 的 Ryan Lopopolo 谈 Harness 工程实践：把产品/用户旅程坍缩成代码，用 Codex harness 解决，用 prompt 让模型"cook"。核心方法论：系统思维 + 持续问"agent 在哪犯错/我时间花在哪/如何不再花" + 对自动化建立信心。是 [[Agent Harness]] 范式在 OpenAI 的一手工程样本。

## 来源

- 视频：《OpenAI团队：OpenAI的 Harness工程实践》
- UP 主：Easonlee的AI笔记（AI Builder 专栏）| 嘉宾：Ryan Lopopolo（OpenAI）
- BV1zkdWBTEFo | 时长 1h17min | 英文原音 | 抓取 2026-07-12｜faster-whisper large-v3
- 原始转写：`01-原始素材/B站转录/AI前沿人物/BV1zkdWBTEFo.md`

> ⚠️ ASR 转写含同音误转（Ryan Lopopolo 姓名需核验）。高风险事实见 [[03-核验/待核验事实]]。

## 核心内容

归因边界：OpenAI 工程师本人口述，属一手来源；为公开访谈，可能简化内部细节。

### Harness 作为构建 AI 产品的核心范式

- "Harness 作为构建 AI 产品的一部分，有很有意思的探索空间。"
- 当前动量集中在让模型擅长编码——每次模型发布，任务复杂度都有大跃迁。
- 关键判断：如果能把你试图构建的产品/用户旅程**坍缩成代码**，用 Codex harness 解决就很自然——harness 做完所有接线，你只需用 prompt 通信让模型"cook"（自由发挥）。
- 这定义了 [[Agent Harness]] 的工程形态：harness 是基础设施，prompt 是接口。

### 系统思维方法论

- 必须退后一步，用**系统思维**看问题：持续问三个问题——
  1. agent 在哪犯错？
  2. 我的时间花在哪？
  3. 如何未来不再花这些时间？
- 然后对正在搭建的自动化**建立信心**，确认"我已解决了 SDLC 的这部分"。
- 这是把 [[Agent Harness]] 从"用一次"变成"可复用基础设施"的方法论。

### 把 SDLC 逐步自动化

- 不是一次性自动化整个软件开发生命周期（SDLC），而是逐步：识别时间花在哪 → 搭自动化 → 建立信心 → 标记"已解决"。
- 每解决一部分，就把注意力移到下一部分，形成持续收敛。
- 与 [[AI研发提效]] 的"44→27 人天"案例同构：都是把 SDLC 环节逐个压掉。

### Codex harness 的递归性

- OpenAI 用 Codex（自己的 harness）构建产品，harness 本身也被 harness 加速——递归式 dogfooding。
- 这与 [[Codex团队如何用Codex（Easonlee AI Builder）]] 互证：团队用自己造的工具构建工具自身。

## 与已有知识网络的连接

- 接 [[Agent Harness]]：本 source 是该 entity 的一手工程样本，补充"harness 做接线、prompt 做通信"的具体形态。
- 接 [[AI原生工作流]]：Harness 是 AI 原生工作流的基础设施层。
- 接 [[AI研发提效]]：逐步自动化 SDLC 的方法论，与"44→27 人天"案例同构。
- 与 `当我们讨论 Agent Harness 时，我们究竟在讨论什么？ _ 深度对谈_ Minimax × Hermes Agent` 形成系列：本 source 是 OpenAI 视角，那个是 Minimax × Hermes 视角。
- 接 [[AI原生组织]]：Harness 工程是 AI 原生组织的技术底座——组织扁平化的前提是 harness 接管了中间层。

## 待核验点

- 嘉宾姓名"Ryan Lopopolo"为音译，需核验真实姓名与职位（见 [[03-核验/待核验事实]]）。
- "每次模型发布任务复杂度大跃迁"为口述判断，无量化。
- "坍缩成代码"的方法论为个人经验，非 OpenAI 官方方法论。
- ASR 误转点：人名、产品名可能听错。