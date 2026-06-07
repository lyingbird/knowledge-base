---
tags: [实体, AI产品, 编程智能体, Anthropic]
created: 2026-06-07
updated: 2026-06-07
sources: [Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]
---

# Claude Code

> Claude Code 是 Anthropic 的 agentic coding 产品，也是观察 action-based AI 产品、eval、harness 和多智能体并行的核心案例。

## 核心内容

在 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 中，Claude Code 被描述为从聊天式 AI 转向 action-based agent 的代表。它不是告诉用户该怎么做，而是能在代码库中读取上下文、执行任务、运行验证、提交可 merge 的结果。

Claude Code 的产品演进体现了 model eats harness。早期模型处理大型重构时，可能说要改 20 个 call sites，实际改 5 个就停；todo list 作为产品脚手架被加入，用来强制跟踪和完成所有项。后续模型能力提升后，todo list 从“强制模型完成”的拐杖，转为“让用户可见任务进度”的辅助。

## 产品边界

- CLI：最新、最强，适合明确编码任务。
- Desktop：适合前端预览和不舒服使用 terminal 的用户。
- Web/mobile：适合随时启动任务。
- 与 [[Cowork]] 的区别：Claude Code 偏明确 artifact 与代码任务；Cowork 偏模糊、异步、低完成率的知识工作。

## 关键机制

- research preview 降低发布承诺，加快用户反馈。
- `/powerup` 把高速发版后的最佳实践收束为用户教育。
- code review 这类功能可能要先构建 prototype，等模型能力补齐后再可靠发布。
- 未来趋势是 multi-Claude-ing：从单任务成功，到远程运行多个或几十个任务，并让人类验证、反馈、管理。

## 相关页面

- [[Anthropic]]
- [[Cowork]]
- [[产品品味]]
- [[Evals]]
- [[智能体]]
- [[业务闭环]]
