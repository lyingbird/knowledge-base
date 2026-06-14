---
tags: [素材, GitHub, 项目学习, LLM编码原则, Claude Code, AI原生工作流]
created: 2026-06-14
updated: 2026-06-14
sources: [raw/repos/multica-ai-andrej-karpathy-skills.md, https://github.com/multica-ai/andrej-karpathy-skills]
---

# Karpathy 编码原则与 Claude Code Skills

> 把 Andrej Karpathy 关于「LLM 写代码常见坑」的观察，提炼成一份可直接装进 Claude Code / Cursor 的开发准则（一个 `CLAUDE.md`），核心是四条原则：先想后写、简单优先、外科手术式改动、目标驱动执行。

## 来源

- 仓库：`multica-ai/andrej-karpathy-skills`
- 内容类型：准则/原则文件（非可执行代码），可作为 Claude Code 插件或按项目的 `CLAUDE.md`
- 抓取日期：2026-06-14
- 关键金句：「Don't tell it what to do, give it success criteria and watch it go.」

## 项目定位与问题

LLM 编码 agent 有几类稳定的失败模式：默默假设、过度工程、顺手改无关代码、把模糊指令当成可执行目标。这个仓库不写新框架，而是把这些坑反过来写成**约束 agent 行为的规则**，落成一份可复用的 [[LLM编码原则]]。它和本库已有的工程实践素材（[[Anthropic团队：如何构建运行 数小时的Agent]]、[[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]]）互补：那两条讲「怎么搭 harness / operating model」，这条讲「给 agent 的单文件行为准则该写什么」。

## 核心方法与架构

四条原则（出自 `CLAUDE.md`）：

1. **Think Before Coding** —「Don't assume. Don't hide confusion. Surface tradeoffs.」显式说明假设、不确定就问；给出多种解释而非默默选一个；该反对时提更简单方案；遇困惑停下点明。
2. **Simplicity First** —「Minimum code that solves the problem. Nothing speculative.」不加没要求的功能；不为一次性代码造抽象；不加没人要的灵活性；不处理不可能的错误分支；200 行能写成 50 行就重写。自检：「资深工程师会不会觉得这过度复杂？」
3. **Surgical Changes** —「Touch only what you must. Clean up only your own mess.」不改无关代码/注释/格式；不重构能跑的代码；匹配现有风格；无关死代码只提示不删。规则：「每一行改动都能直接追溯到用户请求。」
4. **Goal-Driven Execution** —「Define success criteria. Loop until verified.」把模糊任务转成可验证目标和具体检查；复杂工作先给简短多步计划；用强成功标准让 agent 自主迭代。

## 技术栈与关键组件

- `CLAUDE.md`：核心准则（按项目安装）
- `CURSOR.md` / `.cursor/rules/`：Cursor 集成
- `.claude-plugin/`：Claude Code 插件市场配置
- `EXAMPLES.md`：用法示例

## 可复用知识

- **「给标准，而不是给指令」**：第 4 条与本库 [[生成器-评估器架构]]、[[Evals]] 同源——LLM 擅长「朝着可验证目标循环」，所以把判断写成成功标准/rubric 比堆命令更有效。
- **过度工程是 LLM 默认倾向，要靠规则压住**：第 2、3 条正好对冲 agent「顺手加抽象、顺手重构」的惯性，可直接抄进任意项目的 `CLAUDE.md` / `AGENTS.md`（包括本工作区的）。
- **行为准则是一种可移植资产**：同一套原则能以 Claude Code 插件、项目 `CLAUDE.md`、Cursor 规则三种形态复用，呼应 [[AI原生工作流]] 里「把经验沉淀成可被工具加载的规则」。

## 动手清单（安装 / 复现）

- 装成 Claude Code 插件（插件市场），或把其 `CLAUDE.md` 内容并入目标项目根目录的 `CLAUDE.md`；Cursor 用户用 `.cursor/rules/`。
- 验证方式：在一个真实改动任务里观察 agent 是否更少做无关改动、更少过度抽象、更主动先确认假设。

## 局限与适用边界

- 是「行为准则」而非能力增强，效果取决于底层模型是否遵循；不同模型/版本服从度不同。
- 第 3 条「外科手术式改动」与某些需要大范围重构的任务存在张力，需按任务放宽。

## 待核验事实

- 仓库与 Andrej Karpathy 本人的关系（是第三方整理，作者为 multica-ai，非 Karpathy 官方）。
- 各条原则的具体措辞以仓库 `CLAUDE.md` 最新版本为准。

## 相关页面

- [[LLM编码原则]]
- [[Claude Code]]
- [[AI原生工作流]]
- [[生成器-评估器架构]]
- [[Spec-driven development]]
- [[Evals]]
- [[AI技术与开源学习]]
- [[Karpathy开源学习路线]]
