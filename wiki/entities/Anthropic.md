---
tags: [实体, AI公司, 基础模型, AI原生组织]
created: 2026-06-07
updated: 2026-06-07
sources: [Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味, 对姚顺宇的4小时访谈：请允许我小疯一下！在Anthropic和Gemini训模型、技术预测、英雄主义已过去]
---

# Anthropic

> Anthropic 在本库中是观察 AI-native 产品组织、模型产品化和安全使命如何影响组织决策的重要样本。

## 核心内容

[[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 展示了 Anthropic 的产品组织机制：低流程、高速 research preview、每周 metrics readout、team principles、跨职能 launch room、工程/PM/设计角色融合，以及围绕 Claude Code 和 Cowork 的 dogfooding。

Cat Wu 把 Anthropic 的组织优势部分归因于 mission alignment。共同使命降低了产品线政治，使团队愿意牺牲局部产品目标来服务公司整体目标。她的表述是：如果 Claude Code 失败但 Anthropic 成功，她仍会非常高兴。

## 可观察问题

- 安全使命如何转化为产品组合决策？
- 高速发布如何与稳定性、用户教育和企业采用要求平衡？
- Anthropic 的内部 dogfooding、eval 和 feedback channel 如何影响模型与产品迭代？
- Applied AI、Claude Code、Cowork 等团队如何共同形成 [[AI原生组织]] 的反馈闭环？

## 相关页面

- [[Claude Code]]
- [[Cowork]]
- [[产品品味]]
- [[Evals]]
- [[AI原生组织]]
- [[AI原生公司]]
- [[企业AI产品案例]]


## Applied AI 的长程 Agent 实验

[[Anthropic团队：如何构建运行 数小时的Agent]] 展示了 Anthropic Applied AI 团队如何把 Claude Code 的产品经验上升为 [[长程智能体]] 方法论。Andrew 负责梳理模型与 harness 的共演化：RALPH loop、Agent SDK、Skills、server-side compaction、1M context 等能力持续改变 scaffold 的职责。Ash 负责展示实验性 [[生成器-评估器架构]]：planner 给高层方向，generator 构建，evaluator 用真实浏览器和细粒度 rubric 施加对抗压力。

这补强了 Anthropic 作为 AI-native 组织样本的另一面：它不仅通过 research preview 和 dogfooding 迭代产品，也把失败 trace、eval、completion contract、prompt/skill 更新变成组织学习循环。

## 设计组织视角（Jenny Wen）

[[传统设计流程已死：Jenny Wen 谈 AI 时代设计]] 给出 Anthropic 的设计侧样本：设计师大量时间用于在内部 Slack"catch up"（"Slack 是金矿，最好的 AI 新闻在公司内部"）；设计职能被工程倒逼重写，转向收敛/方向/polish（见 [[AI原生设计]]）；用 research preview + build trust through speed 发布；内部原型 Cloud Studio 催生了 Skills 框架。这与 Cat Wu 的 PM 视角、Applied AI 的 harness 视角共同拼出同一组织的多切面。
