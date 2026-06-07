# 知识图谱

> 自动整理初版 | 2026-06-03 | 先覆盖核心主题、实体和第一批素材摘要

```mermaid
graph LR
  AIOrg[AI原生组织] --> AINative[AI原生公司]
  AIOrg --> Context[企业上下文]
  AIOrg --> Loop[业务闭环]
  AIOrg --> Density[智能密度]
  AINative --> Context
  AINative --> Loop
  Loop --> Agent[智能体]
  Loop --> Governance[AI安全治理]
  Density --> AINative

  Enterprise[企业AI产品案例] --> Agent
  Enterprise --> Loop
  Enterprise --> Context
  Enterprise --> Anthropic[Anthropic]
  Anthropic --> ClaudeCode[Claude Code]
  Anthropic --> Cowork[Cowork]
  ClaudeCode --> Taste[产品品味]
  ClaudeCode --> Evals[Evals]
  Cowork --> Context
  Agent --> ClaudeCode

  GameTopic[AI游戏与虚拟世界] --> AIGame[AI游戏]
  GameTopic --> Agent
  GameTopic --> GamePipeline[游戏生产管线]
  GameTopic --> GameIntel[游戏工作室AI提效证据]
  GameIntel --> GameFramework[游戏工作室AI提效落地框架]
  GameFramework --> GameQA[AI辅助QA]
  GameFramework --> AINPC[AI NPC]
  GameFramework --> GamePipeline
  AIGame --> Governance
  GamePipeline --> GameQA
  GamePipeline --> AINPC

  Safety[AI安全与治理] --> Governance
  Safety --> Agent
  Human[AI与人类独特性] --> Safety

  Tom[Tom Blomfield] --> AINative
  Tom --> Context
  Tom --> Loop
  Tom --> Density
  YC[YC AI原生公司] --> AINative
  YC --> Agent
  Micro[微型巨头] --> Density
  Gumloop[Gumloop] --> Enterprise
  Gumloop --> Loop
  Data[主动式数据分析] --> Context
  Headhunt[AI猎头] --> Context
  Altman[奥特曼访谈] --> AINative
  Schmidt[谷歌前CEO警告] --> Governance
  LiFeifei[李飞飞访谈] --> Human
  EA[EA/King/Roblox量化证据] --> GameIntel
  Ubisoft[Ubisoft/KRAFTON/Inworld] --> AINPC
  Capcom[Capcom/Square Enix/Unity] --> GamePipeline
  CatWu[Cat Wu访谈] --> Anthropic
  CatWu --> Taste
  CatWu --> Evals
```

## 查看方式

- Obsidian、GitHub、Typora 或 VS Code Markdown Preview Enhanced 均可渲染上面的 Mermaid 图。
- 后续可以按 `.wiki-schema.md` 的 graph 工作流生成交互式 `knowledge-graph.html`。

## 相关页面

- [[index]]
- [[wiki/overview]]
- [[AI原生组织]]
- [[AI原生公司]]
- [[企业上下文]]
- [[业务闭环]]
- [[智能密度]]
- [[游戏工作室 AI 提效证据]]
- [[游戏工作室AI提效落地框架]]
- [[AI辅助QA]]
- [[AI NPC]]
- [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]
- [[Anthropic]]
- [[Claude Code]]
- [[Cowork]]
- [[产品品味]]
- [[Evals]]


## 2026-06-07 新增长程 Agent Harness 子图

- [[Anthropic团队：如何构建运行 数小时的Agent]] --> [[长程智能体]]
- [[Anthropic团队：如何构建运行 数小时的Agent]] --> [[Agent Harness]]
- [[Agent Harness]] --> [[生成器-评估器架构]]
- [[Agent Harness]] --> [[文件系统共享状态]]
- [[生成器-评估器架构]] --> [[Evals]]
- [[生成器-评估器架构]] --> [[AI辅助QA]]
- [[文件系统共享状态]] --> [[企业上下文]]
- [[Claude Code]] --> [[Agent Harness]]
- [[长程智能体]] --> [[智能体]]
- [[Anthropic]] --> [[Claude Code]]
