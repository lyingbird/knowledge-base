---
tags: [实体, AI原生设计, 设计流程, 产品管理]
created: 2026-06-23
updated: 2026-06-23
sources: [传统设计流程已死：Jenny Wen 谈 AI 时代设计]
---

# AI原生设计

> AI 原生设计是当工程侧能用 agentic coding 即时把想法变成可用产品后，被倒逼重写的设计工作方式：从"产出精美 mock、守流程"转向"收敛方向、补最后一公里 polish、并在真实模型与真实用户中发现 use case"。

## 核心判断

不是设计行业自己想变，而是工程变了倒逼设计变。工程师能并行跑多个编码智能体"ship, ship, ship"，设计师与其当 gatekeeper 阻塞，不如"let them cook"，转去做连接、收敛与质量把关。经典"研究→发散收敛→精美设计稿"的流程（曾被当圣经）基本失效。

## 设计工作的分层

- **支持实现与执行**：工程师快速做出 scrappy 版本，设计师补 polish、做 last-mile 实现，并直接用代码做原型，而非依赖工程师。
- **创造愿景/方向**：愿景从"两年/五年 + 精美 deck"收缩为"三到六个月 + 一个指向性原型"，因为技术变化太快。其价值是在"人人能用七个 Claude 造任意功能"时，把大家指向同一目标以保持连贯与效率。

## 为什么"先 ship 再迭代"更优

AI 模型非确定性，无法 mock 所有状态，甚至做不出能跑通的 clickable prototype；必须用真实模型 + 看真实用户用法来发现 use case。配合 research preview + [[产品品味|build trust through speed]] 的发布机制。

## 工具栈的变化

- 全 Claude 栈：[[Cowork]]（长任务）、[[Claude Code]]（IDE 内改前端、远程 @Claude 出 PR）。
- **Figma 仍不可替代**：擅长一次铺 8-10 个方向、以及字体/视觉/交互的"微方向"探索；coding 工具偏线性，不利于并行铺开。
- 反转：IDE 可能从工程师手里"过气"，反而成为设计师/PM 改 CSS 的趁手工具。

## 人类价值的落点

AI 的 taste 会持续变好甚至被追上，但"决定该做什么、什么才重要"的 judgment 与 accountability 仍属于人（类比放射科 sign-off）。设计师还要像"内部 VC"一样识别 illegible 想法（前沿、别人没 get），用 storytelling 或 UX 形态把它 transform 出来。

## 招聘三种 archetype

- Strong generalists（"block 形"）：几项核心技能都到 80 分位。
- Deep specialist（深 T）：行业 top 10% 的竖笔，如近半个软件工程师或顶级视觉。
- Cracked new grad：早慧、谦逊、极强学习欲，无固化流程包袱。

## 待核验点

- 时间分配、Figma 团队规模等为 Jenny Wen 自述约数；模型型号"Opus 4.6"疑为 ASR 误听。详见 [[03-核验/待核验事实]]。

## 相关页面

- [[传统设计流程已死：Jenny Wen 谈 AI 时代设计]]
- [[Jenny Wen]]
- [[产品品味]]
- [[Cowork]]
- [[Claude Code]]
- [[AI原生组织]]
- [[AI与人类独特性]]
