---
tags: [实体, 概念, LLM编码原则, Claude Code, AI原生工作流]
created: 2026-06-14
updated: 2026-06-14
sources: [wiki/sources/Karpathy编码原则与Claude-Code-Skills]
---

# LLM编码原则

> 约束 LLM 编码 agent 行为、对冲其常见失败模式的一组可移植规则，典型落地形态是项目根目录的 `CLAUDE.md` / `AGENTS.md` 或 Cursor 规则。

## 核心内容

LLM 写代码有几类稳定坏习惯：默默假设、过度工程、顺手改无关代码、把模糊指令当可执行目标。LLM 编码原则就是把这些坑反写成规则。[[Karpathy编码原则与Claude-Code-Skills]] 给出的四条是有代表性的最小集：

1. **先想后写**：显式说明假设、不确定就问、给多种解释、遇困惑停下点明。
2. **简单优先**：只写解决问题的最少代码，不投机性地加功能/抽象/灵活性。
3. **外科手术式改动**：每行改动都能追溯到用户请求，不顺手重构能跑的代码。
4. **目标驱动**：把模糊任务转成可验证的成功标准，让 agent 朝标准自主迭代——「给标准，而不是给指令」。

第 4 条与本库 [[生成器-评估器架构]]、[[Evals]] 同源：LLM 擅长「朝可验证目标循环」，所以写好成功标准比堆命令更有效。整体可直接抄进任意项目的 [[AI原生工作流]]，也适用于 [[Claude Code]] 这类长程 agent 的行为约束。

## 相关页面

- [[Karpathy编码原则与Claude-Code-Skills]]
- [[Claude Code]]
- [[AI原生工作流]]
- [[生成器-评估器架构]]
- [[Spec-driven development]]
- [[Evals]]
