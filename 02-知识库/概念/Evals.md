---
tags: [实体, AI评估, 产品管理]
created: 2026-06-07
updated: 2026-06-07
sources: [Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]
---

# Evals

> Evals 是把“产品成功是什么”转成可运行、可比较、可迭代测试的机制。

## 核心内容

在 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 中，Cat Wu 把 evals 视为 AI-native PM 的重要能力。她认为不需要几百条 eval 才有价值，十条高质量 eval 就能帮助团队量化目标、进展和缺口。

Evals 对 memory、code review、Claude Code 行为改进等功能尤其重要。PM 不一定每个功能都亲自写 eval，但当功能需要更多产品定义时，eval 能把模糊的“更好”变成具体的成功/失败样本。

## 与产品品味的关系

[[产品品味]] 负责判断什么值得做、什么体验才对；evals 则把这个判断固化成可测试标准。AI 产品的难点在于模型行为会变化，eval 能让团队知道新模型、新 prompt、新 harness 是否真的改善了用户任务。

## 相关页面

- [[产品品味]]
- [[Claude Code]]
- [[Anthropic]]
- [[业务闭环]]
- [[智能体]]


## 从产品 Evals 到 Agent Evaluator

[[Anthropic团队：如何构建运行 数小时的Agent]] 把 evals 从“衡量模型/产品表现”推进到“驱动 agent 构建过程”。Evaluator 不是最终打一次分，而是在 [[生成器-评估器架构]] 中用 rubric 和 contract 推动 generator hill climb。前端例子使用 design、originality、craft、functionality 四项标准，并用 reference examples 校准 taste。

更重要的是 completion contract：编码前先把 done 的定义写成可测试 criteria。Retro Forge demo 最终形成 27 条 contract criteria，说明 eval 的粒度必须足够细，才能让反馈从“做得更好”变成“修这个具体行为”。
