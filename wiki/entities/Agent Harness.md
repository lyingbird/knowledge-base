---
tags: [实体, Agent, AI研发提效, Claude Code]
created: 2026-06-07
updated: 2026-06-07
sources: [Anthropic团队：如何构建运行 数小时的Agent, Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]
---

# Agent Harness

> Agent Harness 是包在模型外部的工程运行框架，用来组织工具、权限、上下文、状态、评价、循环和人类接管点。

## 核心内容

[[Anthropic团队：如何构建运行 数小时的Agent]] 中的 harness 不是单一工具，而是一组可演化的 scaffold。早期长程 agent 使用 initializer、`featurelist.json`、progress file、fresh context window、smoke test、Puppeteer 验证和 per-feature commit。后续模型变强后，一些机制可以被删减，转为 single continuous session + compaction，再在生成结束后用 evaluator 批评。

Harness 的职责随模型能力移动。模型不能可靠规划时，harness 负责拆 sprint；模型有 context anxiety 时，harness 负责 reset 和外部状态；模型会 rubber stamp 自己时，harness 负责引入独立 evaluator；模型升级后，harness 要通过 eval 判断哪些旧结构可以 strip out。

## 关键模块

- Planner：给高层产品方向和 sprint，不提前写死所有细节。
- Generator：实现功能、写代码、构建产物。
- Evaluator：用真实环境验证，提出 critique。
- Completion contract：编码前协商完成定义。
- Trace logging：记录模型行为、工具调用、失败路径和修复。
- Hooks：在需要人类介入时暂停并接收 developer message。

## 工程原则

Harness 不应被当成永久教条。每次模型发布后，都要用 [[Evals]] 判断旧 scaffold 是否仍补模型短板。真正可复用的是“发现 spiky behavior -> 用 harness 补 -> 让模型或 workflow 吸收 -> 删除不再必要的结构”这个循环。

## 相关页面

- [[长程智能体]]
- [[生成器-评估器架构]]
- [[Claude Code]]
- [[Evals]]
- [[文件系统共享状态]]
- [[AI研发提效]]
