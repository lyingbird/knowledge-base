---
tags: [素材, B站, AI原生产品, Anthropic, 产品管理]
created: 2026-06-07
updated: 2026-06-07
sources: [raw/notes/video-transcripts/Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味.transcript.txt]
---

# Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味

> Cat Wu 把 AI-native 产品管理的稀缺能力定义为：在代码变便宜、模型快速变化后，仍能判断该做什么、怎样做才对、如何让当前模型发挥最大能力，并把反馈固化成 eval、harness 和组织流程。

## 来源

- Bilibili：`BV1tGVm62EGS`
- 标题：`【AI工具实战】Anthropic产品负责人：AI时代，产品经理最值钱的能力是“品味”`
- UP 主：`Gelai_AI`
- 上传日期：2026-06-03
- 视频时长：01:25:34
- 原始转写：[[raw/notes/video-transcripts/Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味.transcript.txt]]
- 英文原版转写（2026-06-23 本地 ASR 补充）：`raw/notes/video-transcripts/Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味.en-original.transcript.txt`，由 faster-whisper large-v3 对另一搬运版 B 站视频 `BV1TioVBxEKp`（《Anthropic 的产品团队如何做到比任何人都快 | Cat Wu》，UP 主"Web3天空之城"）的英文原音转写而成。两个 B 站视频是同一期 Lenny's Podcast 访谈的不同中文标题搬运，英文原版可作本页中文摘要的交叉核对件。
- 外部参照：[Listen Notes 节目页](https://www.listennotes.com/podcasts/lennys-podcast/how-anthropics-product-team-ngbd5vaDuMp/)、[Lenny's Newsletter 节目页](https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves)、[transcripts.wiki 结构化摘要](https://transcripts.wiki/transcripts/cat-wu-on-ai-product/)

## 核心判断

这条材料把 [[AI原生组织]] 的问题从“公司如何引入 AI”推进到“AI-native 产品团队如何运转”。[[Anthropic]] 的案例显示，速度不只来自更强模型，也来自发布机制、组织使命、清晰目标、低流程、工程/PM/设计角色融合、内部工具、eval 和用户反馈闭环。

Cat Wu 的主张可以概括为三层：

- 代码变便宜后，稀缺能力从 implementation 转向 [[产品品味]]：选择、排序、UX 判断和 delight。
- 模型快速变化后，AI PM 必须会做模型能力校准：知道当前模型能做什么，怎样用 harness、提示、工具和 eval 引导它走到 golden path。
- 产品从 chat-based 转向 action-based [[智能体]] 后，真正的产品价值不是“AI 给建议”，而是“AI 代表用户把事情做完，并能验证、反馈和持续改进”。

## 00:00-17:54 组织速度与 AI-native PM

Cat Wu 与 Boris Cherny 的分工体现了 AI-native 产品团队的双核心。Boris 更偏向定义 3-6 个月后的 AGI-pilled 产品愿景，Cat 把今天到愿景之间的路径拆出来，并拉齐营销、销售、财务、capacity 等跨职能团队。两人的边界很模糊，约 80% 是共同心智，剩下 20% 由更在意的人推进。

Anthropic 招 PM 时，Cat 认为很多候选人仍停留在旧 PM 模式。旧模式假设技术变化慢、代码昂贵、roadmap 可以规划 6-12 个月，PM 的价值主要是协调 partner teams。AI-native 产品中，功能周期可能从 6 个月缩短到 1 个月、1 周甚至 1 天；PM 的价值变成缩短 idea 到用户手里的路径，并定义产品开箱即用必须成功的关键任务。

Anthropic 的快来自几个机制：

- 清晰目标：例如 `Claude Code` 要服务专业开发者，解决 permission prompts 过多导致的 fatigue，让企业专业开发者安全地接近 zero permission prompts。目标越清楚，越能排除无关方案。
- research preview：大多数功能以早期预览发布，告诉用户这是用于收集反馈、持续迭代、不保证永久支持的产品形态，从而降低发布承诺。
- evergreen launch room：工程师 dogfood 后，把准备好的功能交给固定房间，文档、PMM、DevRel 可以次日完成公告和文档。
- 每周 metrics readout 和 team principles：团队共享业务指标、用户、目标、取舍标准，让成员能独立决策，不被 PM 或 stakeholder 卡住。
- 轻量 PRD：模糊功能写一页纸，包含目标、delightful use cases、failure modes；重基础设施项目仍写正式 PRD。

Cat 认为 Anthropic 的高速发布不能主要归因于某个更强模型。内部前沿模型有帮助，但主要增量来自低流程、移除发布障碍，以及让每个人都相信一周内甚至一天内可以把想法交给用户。

## 17:54-35:58 产品品味、混乱和工具边界

代码越来越便宜后，真正变贵的是“决定写什么”。[[产品品味]] 包括这个功能值不值得做、正确 UX 是什么、怎样让用户体验到 delight。[[Claude Code]] 有成千上万 GitHub issues，用户会要求几乎所有功能，团队必须用 care 和 taste 判断哪些值得做、怎么做。

工程背景仍有价值，但价值点从亲手实现转向估算成本。如果某事一小时能做，就少辩论直接做；如果很难，产品判断必须知道它会显著增加团队交付成本。

人脑短期仍有用的位置包括：

- 看懂技术版图如何变化。
- 判断团队当前最需要补哪个洞。
- 识别 highest-priority gaps。
- 把已有技能迁移到当前挑战。
- 处理 stakeholder map、偏好、沟通场域和 buy-in 维护。

Cat 描述团队倾向招聘能 lean into chaos 的人。高速环境中会出现 P0 之后又有 P00、P000 的情况，处理方式不是无限紧张，而是承认只能做这么多、睡好觉、第二天做更好决策。她接受不完美发布：只要不阻断主要 use case，就可以先发、收反馈、下一轮修。

快速发布的真实代价是产品稳定性和连贯性下降。功能可能重叠，用户不知道完成某件事的最佳路径，还会产生追新焦虑。`/powerup` 是补偿机制：把 Claude Code 的最佳用法和酷玩法收束成用户教育入口，回答“100 个功能里哪 10 个必须用”。

Claude 工具边界：

- [[Claude Code]]：最新、最强，适合一两个明确编码任务。
- Claude Desktop：适合前端工作、preview 和不舒服使用 terminal 的用户。
- Web/mobile：适合在外面、手机上或旅途中快速启动 agent。
- [[Cowork]]：适合 Slack zero、inbox zero、slide deck、客户会议后续、课程、目标功能说明、设计计划等产出格式不清晰、人人都做但做不够的知识工作。

## 35:58-51:15 Cowork、内部工具和 token 成本

Cat 认为 Cowork 上手的第一步不是学 prompt，而是连接真实工作上下文：Google Calendar、Slack、Gmail、Google Drive。Cowork 只有能访问必要上下文，才会选择合适信息和工具、提出问题、起草文档，并持续提升结果质量。

她用隔夜 slide deck 举例：为 Code with Claude 会议准备材料时，她把 Google Drive、Slack、PMM 要点、链接资料和叙事目标交给 Cowork，让它生成 slide deck outline 和详细内容。Cowork 聚合材料、展开可能性、生成初稿；PM/PMM 仍负责最终判断：什么叙事成立、哪些例子值得保留、成品是否过于 wordy。

设计系统也被接入：Anthropic 有用于外部沟通的 canonical project，包含颜色、文字、模板和约 20 个示例；若有 Figma MCP 或项目模式，也可让模型吸收样式约束。

内部工具的方向是降低 purpose-built apps 的构建门槛。一位销售人员反复做客户 deck，于是搭了一个 web app：读取核心 deck、101/201 材料、Gong、销售系统、客户是否使用 Bedrock、Vertex、Claude for Enterprise、Console、是否需要 HIPAA 或安全控制等上下文，几秒钟生成客户相关 deck。过去这种整理要 20-30 分钟，甚至导致人们干脆不做。

Slack 没被 AI 替代，反而成为 AI 工作流入口。很多公司想要自建工具，但没人真的想重新造 Slack；Slack 作为实时更新和工作流中心，适合承载 Slack bots 与 AI 协同自动化。

Applied AI team 是技术型 GTM、customer success、forward-deployed engineering 的混合角色。他们与客户相处、帮助客户采用 Anthropic API，有时为客户做 prototype。高峰日一个人可能有 5-10 个 customer engagements；前一晚用 Cowork 汇总第二天客户会议、历史问题、当前关注点、action items，生成 dossier/brief。客户问 feature X 什么时候发布，Cowork 还可以查 Slack 最新 ETA 并写入会议 notes。

token 成本随模型能力提升和委托任务增多而上升。Cat 没给具体数字，但判断工程师或知识工作者的人均 token cost 会随着重大模型和产品改进持续上升。治理原则不是重审批，而是授权构建、成本意识和不浪费文化。

## 51:15-67:22 模型校准、eval 和 harness

AI PM 的关键能力是模型能力校准：判断当前模型能做什么、一个月后可能怎样变化、如何引导用户走到 golden path。难点不是为超级 AGI 设计一个万能文本框，而是面对当前模型，设计产品和 harness 来最大化 elicitation。

Cat 的方法是大量使用模型，并让模型 introspect 自己的行为。例子：模型做了前端改动并跑了测试，却没有真正使用 UI。她会追问模型为什么这样做。模型可能指出系统提示混淆、没有意识到 UI 验证也是任务的一部分、或者把验证委托给 sub-agent 后没有检查其工作。这个过程会暴露系统提示、任务定义、验证流程和 sub-agent 监督机制中的缺口。

[[Evals]] 是定义成功的方法。Cat 说不需要几百条 eval 才有用，十条高质量 eval 就能量化目标、进展和缺口。Claude Code 团队中有小 pod 与 research 合作，精确理解行为、测量改进空间。memory 这类功能尤其适合 eval。

Claude 的 character 也是产品能力。Cat 把好 Claude 描述为像优秀同事：轻松、有趣、任务上专业、low ego、用户指出错误时真诚道歉并修复、面对大任务时拆步骤并主动开始。积极、行动导向和真诚反馈是协作体验的一部分。

新模型会迫使产品删功能。许多功能或 prompt 是旧模型的拐杖，模型能力提升后应删除或弱化。todo list 是典型例子：早期 Claude Code 被要求改 20 个 call sites 时可能改 5 个就停，团队加入 todo list 强制跟踪。后来的 Opus 4 之后，模型自然会使用 todo list 并完成全部项，todo list 的价值从“强制模型完成”转向“让用户可见”。

这就是 model eats harness：模型变聪明后，会吞掉叠在模型上的产品脚手架。每次发布新模型，团队都会重读 system prompt，判断哪些提醒不再需要。

未来愿景是从单任务成功到 multi-Claude-ing。先让单个 prompt 稳定产出可 merge、可分享、可交付的结果；随后用户会同时跑多个任务；再往后可能一次跑 50-100 个 Claude。产品基础设施要从本地转向远程运行，帮助人类管理大量任务、知道哪些需要查看、验证 agent 是否完整工作、在失败后反馈并让模型未来吸收。

## 67:22-85:34 职业建议与行动代理

Cat 的职业建议不是抽象地学习 AI，而是从重复劳动出发。每当发现自己反复做某个手工任务，就思考能否用 Claude Code、Cowork 或其他 AI 工具自动化。多数工作都有创造性部分和 tedious/manual 部分；AI 应学习你过去如何做手工任务，泛化后执行，让人把时间挪回创造性判断。

自动化必须从 cool concept 推进到真正可靠。90%-95% 不足以称为自动化，尤其当错误会导致漏邮件、误分类、错发、误删或合规风险时。Cat 自己在训练 Cowork 帮她实现 Gmail inbox zero，主持人也提到邮件分类 workflow 95% 很好但偶尔误放重要邮件，反而危险。真正自动化需要教模型偏好、给反馈、让它更新 skill，并检查 skill 是否真的吸收反馈。

她反对只做 one-shot prototype 或炫耀 setup。AI prototype 如果没有帮你每天多完成事情，就没有真正增加日常价值。真正学习来自持续使用：每天用、发现边界、修复问题、迭代体验，最后进入工作流。过度定制 skills、MCPs、workflow improvements 可能变成逃避真正产出的方式。

AI skeptic 与 believer 的分裂来自体验代际差异。2024 一代产品主要是 chat-based，Claude Code 这一代是 action-based。重要 aha moment 不是 AI 告诉你该做什么，而是 agent 在你 behalf 上 just do things。

她的工作信条是 Just do things。如果知道自己在优化什么，并有 first principles，就应该推导行动、向 stakeholders 解释、然后去做。她把 startup 训练描述为跨边界做需要被做的事，而不是只做别人指定的任务。AI 时代更奖励 agency、bias toward action 和低 ego。

结尾中，Cat 说最有帮助的产品反馈不是泛泛夸奖，而是告诉团队 Claude Code / Cowork 哪些地方不好用，提供 edge cases、errors 和 specific tasks that can be reproduced。成功故事进入 user love channel，产品问题进入 feedback channel，供团队行动。

## 可复用概念

- [[Anthropic]]
- [[Claude Code]]
- [[Cowork]]
- [[产品品味]]
- [[Evals]]
- [[智能体]]
- [[AI原生组织]]
- [[AI原生公司]]
- [[企业上下文]]
- [[业务闭环]]
- [[AI人物访谈]]
- [[企业AI产品案例]]

## ASR 校准

- `Kat Wu` 应为 Cat Wu。
- `Cloud Code`、`quad code`、`clawed code`、`框架键` 等应为 Claude Code。
- `co-work`、`合作`、`cowork` 统一为 Cowork，但正式产品命名需核验。
- `Boris` 应补全为 Boris Cherny。
- `AGI peeled` 应为 AGI-pilled。
- `RBX` 应为 RBAC。
- `SLAQ` 应为 Slack。
- `forward-to-play engineering` 应为 forward-deployed engineering。
- `multi-clotting` 应为 multi-Claude-ing。
- `fountain blue` 应为 Fontainebleau。
- `i'm underscore cat wu` 可能是 `@im_catwu`，需核验。

## 待核验事实

- Cat Wu 在 Anthropic 的准确头衔、职责边界，以及 Cowork 的正式产品命名。
- Boris Cherny 是否为 Claude Code 创建者、技术负责人，以及正式职务。
- Anthropic PM 总数约 30-40 人、Applied AI team 的正式职责、Claude Developer Platform managed agents 等组织事实。
- Mythos、OpenClaw、Claude Code 源码泄露、/powerup、Claude Chrome extension、/code review、code review merge gate 等具体事件或功能。
- Amanda、Sid、Alex 等人名全名与职责。
- Anthropic ARR/增长、token 使用成本、Cowork 增长很快等量化说法。
- Andrej Karpathy 关于 AI skeptic 与 believer 分裂的推文原文。

## 相关页面

- [[AI原生组织]]
- [[企业AI产品案例]]
- [[AI人物访谈]]
- [[AI研发提效]]
- [[团队知识库]]
