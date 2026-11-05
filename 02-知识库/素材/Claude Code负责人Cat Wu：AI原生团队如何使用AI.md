---
tags: [素材, 视频, AIBuilder, 英文原音, Claude Code, Anthropic, AI原生组织, Cat Wu]
created: 2026-07-12
updated: 2026-07-12
sources: [01-原始素材/B站转录/AI前沿人物/BV1eyBgB2EbX.md, https://www.bilibili.com/video/BV1eyBgB2EbX]
---

# Claude Code 负责人 Cat Wu：AI 原生团队如何使用 AI

> Cat Wu（Claude Code 产品负责人）在 Peter 播客谈 Claude Code 团队的 AI 原生运作方式：不用 Google Docs、原型替代文档、每 10 分钟收一轮用户反馈、爱负反馈不爱奉承、SweetBench 变化要读 gnarly transcripts 追因。是 [[AI原生工作流]] 与 [[AI原生组织]] 在 Anthropic 内部的一手样本，与 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]（Lenny's Podcast 85min 版）为同一人不同主持人的两期访谈，内容互补。

## 来源

- 视频：《Claude Code负责人：AI 原生团队如何使用AI？》
- UP 主：Easonlee的AI笔记（AI Builder 专栏）| 嘉宾：Cat Wu（Claude Code 产品负责人）| 主持人：Peter
- BV1eyBgB2EbX | 时长 40分 | 英文原音 | 抓取 2026-07-12｜faster-whisper large-v3
- 原始转写：`01-原始素材/B站转录/AI前沿人物/BV1eyBgB2EbX.md`

> ⚠️ ASR 转写含同音误转（"QuadCode" = Claude Code、"Boris" = Boris Cherny 疑 Claude Code 创建者）。高风险事实见 [[03-核验/待核验事实]]。

## 核心内容

归因边界：Cat Wu 本人口述，属一手来源；为公开访谈，可能简化内部流程。

### 不用 Google Docs，原型替代文档

- "Claude Code 团队不怎么用 Google Docs。"——最好的功能往往是工程师**直接做原型** → 推到 dogfooding → 听反馈，而不是写需求文档。
- 原型即文档：用可运行的东西替代文字描述，让"用户能不能立刻理解/会不会困惑/有没有 bug/喜不喜欢"直接暴露。
- 与 [[Codex团队如何用Codex（Easonlee AI Builder）]] 的"极简 spec 10 条 bullets"互证：AI 原生团队普遍去文档化。

### 每 10 分钟收一轮反馈 + 爱负反馈

- 团队大约每 10 分钟就能收到一条新反馈——反馈频率远超传统产品周期。
- "我们爱负反馈，不要奉承（platitudes），我们想听什么不工作。"——主动求坏的信号，避免确认偏误。
- 这是 [[超级组织]]"沟通即执行"的极致形态：反馈闭环从"季度调研"压到"10 分钟一轮"。

### SweetBench 变化要读 gnarly transcripts

- 谈 evals：SweetBench 分数变化不总是能看出原因，必须**读那些很 gnarly（棘手）的 transcripts** 追因。
- 量化指标（bench 分数）+ 定性深读（transcripts）结合，不能只看数字。
- 与 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 中"写 evals 定义成功标准"一致——evals 是 PM 的核心工具。

### Claude Code 的起源：Boris 的 tinkering

- Claude Code 起源于 Boris（Cherny，疑创建者）为了理解自家 API、看能增强多少软件工程而 tinkering 的小工具。
- Cat 当时用 20% 时间加自己的环境，发现 Claude Code 让她效率大增，于是不断给 Boris 发产品反馈。
- 决定对外发布后，Cat 全职加入。被广泛采用后持续投入——更功能丰富、跨异构开发者环境、更可及。
- 判断："不是宏大战略的一部分，就是他建了个小工具，然后团队开始用。"——[[AI原生组织]] 的自下而上生长样本。

### Cat Wu 个人用 Claude Code 做产品工作 + 产品愿景

- Cat 用 Claude Code 做自己的产品工作（dogfooding 到日常）。
- 被问"一两年后产品长什么样"时回答："一两年太长了，我只能说接下来几个月。"——AI 时代产品规划从长线转向短周期迭代。
- 与 [[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 互证：长线规划在 AI 时代失效。

## 与已有知识网络的连接

- 接 [[AI原生工作流]]：不用 Google Docs、原型替代文档是 AI 原生工作流的具体形态。
- 接 [[AI原生组织]]：Claude Code 起源于 tinkering 而非战略，是 AI 原生组织自下而上生长的样本。
- 接 [[超级组织]]：每 10 分钟反馈 + 爱负反馈，是"沟通即执行"的极致闭环。
- 与 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]（85min Lenny 版）互补：本 source 聚焦团队运作机制，85min 版聚焦 PM 品味与招聘——同一人两期不同角度。
- 与 [[Codex团队如何用Codex（Easonlee AI Builder）]] 形成系列：Codex 团队（OpenAI）与 Claude Code 团队（Anthropic）的 AI 原生运作对照，都去文档化、都原型驱动、都极快迭代。
- 接 [[Agent Harness]]：Claude Code 本身是 harness，团队用它构建 Claude Code 自身（递归 dogfooding，与 OpenAI Codex 同构）。

## 待核验点

- "每 10 分钟一条反馈"——口述，无量化来源（见 [[03-核验/待核验事实]]）。
- "Boris" 全名与职位（疑 Boris Cherny，Claude Code 创建者）需核验。
- "QuadCode" 为 ASR 误听，实为 Claude Code。
- Cat Wu 头衔"产品负责人"在 Anthropic 的正式名称需核验。
- Claude Code 起源叙事为回忆性口述，可能简化。
