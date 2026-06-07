---
tags: [实体, AI原生组织, 工作流, AI研发提效]
created: 2026-06-07
updated: 2026-06-07
sources: [麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率, Anthropic团队：如何构建运行 数小时的Agent]
---

# AI原生工作流

> AI 原生工作流不是在旧流程上外挂聊天机器人，而是把 AI 放进计划、规格、实现、测试、评估、复盘和再投资的连续闭环。

## 核心内容

[[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 中，McKinsey 把高表现企业的共同点归纳为 AI-native workflows 和 AI-native roles。工作流层面，企业不再只做 code review 或 code development 单点工具，而是把 AI 扩展到 SDLC 的多个 use cases：continuous planning、spec-driven development、原型共创、测试生成、影响分析、回归检查和质量治理。

这与 [[Anthropic团队：如何构建运行 数小时的Agent]] 的 [[Agent Harness]] 形成内外两层：单个任务需要 harness，组织价值流需要 AI 原生工作流。工作流必须规定 agent 做什么、人类何时判断、失败如何记录、经验如何回写。

## 判断标准

- AI 是否进入 4 个以上连续环节，而不是单点写代码。
- 是否以 [[Spec-driven development]] 作为人机接口。
- 是否把测试、评估和 review 左移到生成过程。
- 是否沉淀 [[企业上下文]]，让下次任务更快更准。
- 是否用 outcome 度量，而不是只看活跃用户或调用次数。

## 相关页面

- [[AI原生组织]]
- [[后敏捷操作模型]]
- [[Spec-driven development]]
- [[Agent Harness]]
- [[Evals]]
- [[企业上下文]]
