# raw: multica-ai/andrej-karpathy-skills

- 仓库：https://github.com/multica-ai/andrej-karpathy-skills
- 定位：把 Andrej Karpathy 关于「LLM 编码常见坑」的观察，整理成一份可直接用于 Claude Code / Cursor 的开发准则（`CLAUDE.md`）。
- 内容类型：指南/原则文件，非可执行代码。
- 抓取日期：2026-06-14

## 主要文件

- CLAUDE.md：核心准则（按项目安装）
- CURSOR.md：Cursor IDE 集成说明
- EXAMPLES.md：实际用法示例
- README.md：主文档
- .claude-plugin/：Claude Code 插件市场配置
- .cursor/rules/：Cursor 项目规则目录

## 四条原则（CLAUDE.md 摘抄）

1. Think Before Coding —「Don't assume. Don't hide confusion. Surface tradeoffs.」
   - 显式说明假设，不确定就问；给出多种解释而不是默默选一个；该反对时提出更简单的做法；遇到困惑停下来点明，而不是硬着头皮往下做。

2. Simplicity First —「Minimum code that solves the problem. Nothing speculative.」
   - 不加没要求的功能；不为一次性代码造抽象；不加没人要的灵活性/可配置；不处理不可能发生的错误分支；200 行能写成 50 行就重写。自检：「资深工程师会不会觉得这过度复杂？」

3. Surgical Changes —「Touch only what you must. Clean up only your own mess.」
   - 不顺手改无关代码/注释/格式；不重构能正常工作的代码；匹配现有风格；发现无关死代码只提示、不删除。规则：「每一行改动都能直接追溯到用户的请求。」

4. Goal-Driven Execution —「Define success criteria. Loop until verified.」
   - 把模糊任务转成可验证目标和具体检查；复杂工作先给简短的多步计划；用强成功标准让模型能自主迭代。

## 关键金句

「LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go.」

## 安装方式

Claude Code 插件市场集成 / 按项目加 `CLAUDE.md` / Cursor 规则。
