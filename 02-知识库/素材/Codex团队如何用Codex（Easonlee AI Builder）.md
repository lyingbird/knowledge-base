---
tags: [素材, 视频, AIBuilder, 英文原音, Codex, OpenAI, AI原生组织, 工程实践]
created: 2026-07-12
updated: 2026-07-12
sources: [01-原始素材/B站转录/AI前沿人物/BV1iKdvBhEYJ.md, https://www.bilibili.com/video/BV1iKdvBhEYJ]
---

# Codex 团队如何用 Codex（Easonlee AI Builder）

> OpenAI Codex 团队成员 Alex 和 Roman 演示团队内部如何用 Codex 构建功能、持续发布。核心判断：极简 spec（10 条 bullets）、设计师直接写代码、PR 比沟通快、PM 是"填缝"角色而非领导。是 [[AI原生工作流]] 在 OpenAI 内部的一手样本。

## 来源

- 视频：《Codex产品负责人：Codex团队如何用Codex》
- UP 主：Easonlee的AI笔记（AI Builder 专栏）| 嘉宾：Alex、Roman（OpenAI Codex 团队）
- BV1iKdvBhEYJ | 时长 43分16秒 | 英文原音 | 抓取 2026-07-12｜faster-whisper large-v3
- 原始转写：`01-原始素材/B站转录/AI前沿人物/BV1iKdvBhEYJ.md`

> ⚠️ ASR 转写含同音误转（人名 Alex/Roman 为音译，GPT 版本号需核验）。高风险事实见 [[03-核验/待核验事实]]。

## 核心内容

归因边界：Codex 团队成员本人口述，属一手来源；但为公开访谈展示，可能简化内部流程。

### 极简 spec：10 条 bullets 就够

- Codex 团队写非常少的 spec——"大概 10 条 bullets，就这样"。
- 不做长篇需求文档，把需求压成最简形式直接喂给 Codex。
- 这与 [[AI原生工作流]] 的"沟通即执行"一致：spec 越短，模型自由度越高，迭代越快。

### 设计师写代码，PM 是"填缝"角色

- "Codex 团队的设计师现在写的代码，比六个月前的工程师还多。"——AI 把代码门槛降到设计师可直接产出。
- PM 不是领导岗位，是"填缝"（fill in the gaps）岗位——补团队没覆盖的部分，而非指挥。
- "房间里需要的人越少，事情就做得越好，每个决策越纯粹。"——反会议室文化。

### PR 比沟通快

- 小改动直接发 PR，比"跟人沟通、排队等优先级"更快。
- 当别人有 10000 件事要做时，直接发 PR 让改动落地，绕过协调成本。
- 这是 [[超级组织]]（李志飞"沟通即执行"）的 OpenAI 版实践。

### 现场演示：语音→功能

- Roman 现场演示：对着 Codex 语音说"给 iOS app 加一个 NASA Artemis 返回月球任务的新屏幕"，GPT 5.4 直接生成新功能。
- Codex Spark 模型用于快速 ideate 和迭代（几秒内响应）。
- 展示了从"描述需求"到"功能落地"的端到端闭环，验证 [[AI辅助游戏开发]] 的"门槛降到会描述需求"判断。

### 持续发布的节奏

- Codex 团队"nonstop shipping"——持续发布，不做大版本囤积。
- 与 [[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 互证：个人/小团队提效后，发布节奏从"数月"压到"数天甚至数小时"。

## 与已有知识网络的连接

- 接 [[AI原生工作流]]：本 source 是"极简 spec + PR 比沟通快"的 OpenAI 内部样本。
- 接 [[超级组织]]：李志飞的"沟通即执行"在 OpenAI Codex 团队的实践形态——PM 填缝、设计师写码、PR 绕过协调。
- 接 [[Agent Harness]]：Codex 本身就是一个 harness，团队用它构建 Codex 自身（递归式 dogfooding）。
- 接 [[AI辅助游戏开发]]：语音→功能的演示，验证"会描述需求就能产出"的门槛降低。
- 与 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 形成对照：Cat Wu 强调 PM 的"品味"，Codex 团队强调 PM 是"填缝"——两者不矛盾，品味决定方向，填缝决定执行。

## 待核验点

- "设计师写的代码比六个月前的工程师还多"——口述，无量化数据（见 [[03-核验/待核验事实]]）。
- "GPT 5.4"——版本号需核验（ASR 可能误听，或为内部版本）。
- 嘉宾姓名 Alex/Roman 为音译，需核验真实姓名与职位。
- "10 条 bullets"为口述经验，非硬性规定。
