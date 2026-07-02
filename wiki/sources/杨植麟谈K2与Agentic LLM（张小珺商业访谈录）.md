---
tags: [素材, 视频, 访谈, 基础模型, Agentic LLM, Kimi, 张小珺商业访谈录]
created: 2026-07-01
updated: 2026-07-01
sources: [raw/notes/video-transcripts/对话Kimi创始人杨植麟：K2、Agentic LLM、缸中之脑、艰难的泛化、用L4解决L3、长文本影响智商、“站在无限的开端”.transcript.txt, https://www.bilibili.com/video/BV1hFe1zSEXp]
---

# 杨植麟谈K2与Agentic LLM（张小珺商业访谈录）

> 月之暗面创始人杨植麟深度访谈。核心：2025 已完成从对话到 Agent 的范式转变；Agent 泛化不足是最大瓶颈，需「用 L4（模型自我迭代）解决 L3（Agent 泛化）」；哲学内核是 David Deutsch「问题不可避免，但问题可解决」（Beginning of Infinity）。

## 来源

- 视频：《对话 Kimi 创始人杨植麟：K2、Agentic LLM、缸中之脑、艰难的泛化、用 L4 解决 L3、长文本影响智商、"站在无限的开端"》
- UP 主：张小珺商业访谈录 | 嘉宾：杨植麟（月之暗面 / Kimi 创始人）
- BV1hFe1zSEXp | 时长 99:39 | 中文 | 抓取 2026-07-01｜faster-whisper large-v3
- 原始转写：`raw/notes/video-transcripts/对话Kimi创始人杨植麟….transcript.txt`

## 核心内容

归因边界：创始人对技术路线的判断，含技术信仰；模型参数/效率/ARR 等数字为口播，需核验。

### 核心论点

1. **站在无限的开端**：AI 研发如爬无限高的雪山，问题不可避免但可被解决，每解一题生新题也解锁新场景。2025 已完成从基础对话到 Agent 的范式转变。
2. **Test Time Scaling 双轨制**：强思考推理（「缸中之脑」型，纯推理长 CoT，如 o1）与多轮 Agent（与外界交互、多轮工具调用）都是 test-time scaling，但路线不同。
3. **用 L4 解决 L3**：Agent 泛化不足是最大瓶颈，需用「innovation（模型自我建设/迭代）」赋能 Agent，而非反向依赖；Agent 能力上限须与 reasoning 同步提升。
4. **Token Efficiency > Compute Efficiency**：高质量数据已成常数，关键是提升单位数据价值；Muon 优化器（非 Adam）据称提升学习效率约 2 倍。
5. **泛化困境与 benchmark 失效**：RL 面临「种瓜得瓜」——优化 benchmark 后 OOD 任务崩塌；需更 AI-native 的 evaluation。
6. **长文本 = 更大智商压力**：长 context 架构易损短 context 表现，需模型足够大（压缩率够高）才能兼顾长度与智能。
7. **AGI 是方向非终点**：不迷恋「登月时刻」，很多领域已超 99% 人类，但难宣称「此刻实现 AGI」。
8. **开源是博弈 + 技术信仰的混合**：领先者不开源、落后者才开源是客观事实；K2 开源同时借社区加速技术。
9. **模型级产品论仍成立**：Agent 的工具/环境/context 应在训练时设计，「模型训好时产品基本做完」。
10. **组织管理的 RL 视角**：科研/训练/团队管理都是强化学习——定义奖励、防 reward hacking、平衡 RL（激发创新）与 SFT（防偏离）。

### 关键概念

K2（Kimi 第二代 base model，融合 Muon + RL 基建 + Agent 训练，首个开源的高质量模型）、Agentic LLM（「多轮 + 工具」是最重要特征）、缸中之脑（纯推理型强思考）、用 L4 解决 L3、长文本影响智商、Muon 优化器、Post-train、泛化。

## 对天美/知识库的价值

- **基础模型主线的一线判断**：补强 [[基础模型]]——Agentic LLM 的本质、泛化瓶颈、test-time scaling 双轨。
- **与 Agent 主线呼应**：「Agent = 多轮 + 工具」「模型内化应用创新」与 [[Agent Harness：模型是脑Harness是手（十字路口×MiniMax×Hermes）]]（应用层创新被模型吸收）、[[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]] 互证；与库内 [[对姚顺宇的4小时访谈：请允许我小疯一下！在Anthropic和Gemini训模型、技术预测、英雄主义已过去]] 同属大模型一线判断，可交叉。
- **model-native 产品论**：呼应 [[AI原生公司]]、[[企业AI产品案例]]——能力在训练时内建，而非事后包壳。

## 待核验事实

见 [[03-核验/待核验事实]]：Muon 比 Adam 效率提升约 2 倍、高质量数据约 30T tokens 量级、K2 「首个开源泛化 Agent 能力模型」、模型连续工作数小时完成代码任务、头部公司 ARR 每 1-2 季度翻 2-3 倍等。

## 相关页面

- [[基础模型]]
- [[Agent Harness：模型是脑Harness是手（十字路口×MiniMax×Hermes）]]
- [[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]]
- [[对姚顺宇的4小时访谈：请允许我小疯一下！在Anthropic和Gemini训模型、技术预测、英雄主义已过去]]
- [[AI原生公司]]
- [[张小珺商业访谈录]]
