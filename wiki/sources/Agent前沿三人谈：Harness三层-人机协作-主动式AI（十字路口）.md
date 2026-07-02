---
tags: [素材, 视频, 播客, Agent, Agent Harness, 主动式AI, 十字路口]
created: 2026-07-01
updated: 2026-07-01
sources: [raw/notes/video-transcripts/【十字路口】探秘 Claude Code，搞懂 Agent Harness｜对谈来新璐【视频播客】.transcript.txt, raw/notes/video-transcripts/【十字路口】人类和 AI Agent 的最佳配合方式，还没被发明｜对谈 Paperboy 【视频播客】.transcript.txt, raw/notes/video-transcripts/【十字路口】OpenClaw 之后，谁将定义主动式 AI 的新战场？｜对谈 AirJelly 黄柏特【视频播客】.transcript.txt, https://www.bilibili.com/video/BV1Ji9aB4Eu2, https://www.bilibili.com/video/BV1UtLP6eEgE, https://www.bilibili.com/video/BV1ZbQmBbEha]
---

# Agent前沿三人谈：Harness三层、人机协作、主动式AI（十字路口）

> 三期十字路口对谈拼出 Agent 范式的前沿全景：①**Harness 三层框架**（来新璐）——执行/状态/治理；②**人机协作最佳方式尚未被发明**（Paperboy）——session 断裂是摩擦、OS 级 context 优于聊天记录；③**OpenClaw 之后主动式 AI 新战场**（AirJelly）——意图 context > 信息 context。共同指向：模型是脑，Harness/Context/记忆是决定 Agent 上限的关键。

## 来源

- 《探秘 Claude Code，搞懂 Agent Harness｜对谈来新璐》BV1Ji9aB4Eu2 47:46
- 《人类和 AI Agent 的最佳配合方式，还没被发明｜对谈 Paperboy》BV1UtLP6eEgE 55:31
- 《OpenClaw 之后，谁将定义主动式 AI 的新战场？｜对谈 AirJelly 黄柏特》BV1ZbQmBbEha 67:58
- UP 主：Koji杨远骋at十字路口 | 中文 | 抓取 2026-07-01｜faster-whisper large-v3
- 原始转写：见上三文件。

## 核心内容

归因边界：创业者/工程者的实践与判断；融资、star、估值、时间线等为口播，需核验。

### 一、Harness 三层框架（来新璐，KKBBAI / ShareAI）

- **「模型之外都是 Harness」**：模型是大脑，Harness 给它身体手脚（「健身、舞蹈、武术、穿机甲」扩充能力）。
- **三层拆解**（本页最大增量，把 Harness 从玄学变工程）：
  1. **执行层**：文件系统、浏览器、Python/Node 解释器等工具能力。
  2. **状态层**：Context 管理、Skills、Memory、上下文压缩与卸载（预留 ~20% buffer、写交接文档）。
  3. **治理编排层**：多 Agent 协调、权限隔离、串并行编排。
- **「更多 Context，更少 Control」**：给模型充分上下文与自由度，而非预设每步（对标 Claude Code 设计哲学）；「CLI is all you need」（Unix 命令在预训练出现几十亿次，比 MCP 有效）。
- **好 Harness 标准**：自洽于模型运行原理 + 自洽于模型未来进步方向（破坏 KV Cache、过度 Prompt Node 管理就是坏 Harness）。
- **Auto Dream / 做梦机制**：后台 Agent 定期重放对话、提取更新记忆——Memory 与 Skill 边界模糊。
- 演进想象：单 Agent → Agent 编排 Agent → Agent 自主创新 → 「零人公司」；Agent 范式约 3 年红利期。

### 二、人机协作最佳方式尚未被发明（Paperboy，John Yang）

- **Session 断裂是核心摩擦**：Claude Code/Manus/OpenClaw/Codex 都是 session-based + prompt-based（开窗→输入→等待→关闭，下次从零），数百上千 session 间无连续性。
- **OS 级 Context > 聊天记录**：60 分钟电脑使用的信息密度远高于 60 分钟微信记录；Agent 应观察 OS 层活动自我学习，而非依赖反复 prompt。
- **IM 模式优于 Session 模式**：用群聊逻辑（多话题、自动归档、主动通知）组织 Agent 对话，更连续更协作。
- **竞争格局：taste vs distribution**：只有 OpenAI/Anthropic 有模型+分发优势，其他公司（Cursor/Paperboy）机会在**产品品味**——找到新交互范式后虽被复制，但先发者已建用户习惯（呼应「摩擦即机会」「moving goalpost」）。
- Pace Layers：Agent 记忆需分层（秒→分→时→天→周月），各层变化速率不同。

### 三、OpenClaw 之后的主动式 AI 新战场（AirJelly，黄柏特）

- **主动式 AI 的界分**：真正的主动式 AI 需捕获「明确意图 + 场景上下文」；多数产品只是「发散」（推荐新内容），AirJelly 是「顺延」（推进当前任务）。
- **Context 分级：意图 Context > 信息 Context**（信息可检索，意图难获取）；价值在「高光时刻/关键节点」而非全量录制。
- **Enter 键触发截图**：从周期性（15-30 秒）改为事件驱动（按 Enter 时刻——用户表达意图的最高峰，贯穿 IM/Chatbot/Web Search）。
- **OpenClaw 冲击后的调整**：Task Engineering 被 OpenClaw 吸纳后，转向深耕「Context 的获取/存储/召回」——OpenClaw 难直接涉猎的领地。壁垒三层：记忆锁定、工程细节、模型能力。
- **Vibe Coding 判断法则**：新方向若 Vibe Coding 后已达 60-80 分则无壁垒；AirJelly 的 Context 获取只到 30 分 → 有空间。
- 隐私成护城河：端加密/本地存储/自动匿名化（大厂因监管不敢做）。
- 终局想象：一人一专属 Personal Agent（一对一制），既提生产力又提供情感陪伴。

## 对知识库的价值

- **系统补强 [[Agent Harness]]**：来新璐的「三层框架」是从抽象概念到工程实践的关键跨越，与 [[Anthropic团队：如何构建运行 数小时的Agent]]、[[Agent Harness：模型是脑Harness是手（十字路口×MiniMax×Hermes）]] 三方印证。
- **深化 [[OpenClaw]] 主线**：AirJelly 展示「OpenClaw 之后」的创业调整——从执行能力转向 Context 获取；与 [[罗福莉谈AI范式巨变与OpenClaw（张小珺商业访谈录）]]、[[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]] 构成 OpenClaw 三部曲。
- **记忆/Context 是共识主线**：三期都指向「记忆 > 智能、Context 决定上限」，与和平精英四维记忆（[[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]]）、Hermes 多层记忆跨领域一致。
- **人机协作与产品品味**：Paperboy 的「taste vs distribution」呼应 [[产品品味]]、[[AI无法取代的核心竞争力]]。

## 待核验事实

见 [[03-核验/待核验事实]]：Learn Claude Code 50k+ star、KKBBAI 融资 300+ 万美元、Claude Code 源码泄露、Paperboy 融资 470 万美元/12 人、AirJelly MindContext 5000+ star/8 人/2026-03 内测、各创始人年龄履历、「Agent 3 年红利期」等。

## 相关页面

- [[Agent Harness]]
- [[OpenClaw]]
- [[智能体编排]]
- [[长程智能体]]
- [[产品品味]]
- [[Anthropic团队：如何构建运行 数小时的Agent]]
- [[Agent Harness：模型是脑Harness是手（十字路口×MiniMax×Hermes）]]
- [[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]]
- [[罗福莉谈AI范式巨变与OpenClaw（张小珺商业访谈录）]]
- [[十字路口]]
