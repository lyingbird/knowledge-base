---
tags: [素材, B站视频, AI研发提效, 后敏捷, 软件工程]
created: 2026-06-07
updated: 2026-06-07
sources: [Bilibili BV1bMq3BTEhX, Moving away from Agile]
---

# 麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率

> 这条素材把 McKinsey 的 “Moving away from Agile: What's Next” 演讲，转写成一个关于 [[后敏捷操作模型]] 的中文框架：AI 让代码生成变便宜，但组织级提效取决于 spec、角色、测试、架构约束、企业上下文和 outcome 度量是否一起重写。

## 来源与校准

- B 站：BV1bMq3BTEhX，标题为《麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率》，上传者为“碳硅同传”，视频时长约 37:44。
- 原始演讲：Martin Harrysson 与 Natasha Maniar，McKinsey & Company / Software X，题为 “Moving away from Agile: What's Next”。
- 本地 raw 副本：[[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.transcript.txt]]、[[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.youtube-en.txt]]、[[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.sozai.txt]]。
- 归因边界：McKinsey 原演讲支持“约 300 家企业、公司级提效常只有 5%-15%、AI-native workflows/roles、spec-driven development、one-pizza pods、银行案例、change management、outcome measurement”等主线；Netflix、高盛、Cursor、宝洁、Browser Company 等案例属于 B 站二次讲解或外部扩展，已放入待核验。

## 核心判断

个体 AI 编码体验和公司级生产率之间存在断层。开发者可以举出许多“几小时或几天的任务变成几分钟”的案例，但 McKinsey 调研约 300 家多为大型企业的公司后，看到整体公司级 productivity improvement 往往只有 5%、10%、15%。断层不是模型没用，而是旧的协作、审查、测试、架构和度量方式没有同步升级。

旧敏捷的很多操作层假设正在失效：过去人类写代码是瓶颈，代码贵而慢，需求变化主要来自业务，系统相对稳定，团队用 sprint、story、velocity、PR 和 review 管理节奏。AI 介入后，代码不再稀缺，原型可以即时生成，需求、实现、验证被压缩到同一条时间线，模型、数据、prompt 和工具链每天变化，产品越来越像活系统。敏捷价值观仍然有用，但围绕人类开发约束形成的 operating model 需要重写。

AI 像高压水龙头一样喷出代码，而很多团队还在用模糊 story、模糊 acceptance criteria、人工 code review、旧测试队列和旧合并流程接水。结果是局部执行变快，下游 review、返工、测试排队、跨人对齐、解释和合并反而变成新瓶颈。

## 章节拆解

### 00:00-09:30：局部快与组织慢的矛盾

McKinsey 的问题不是“AI 能不能写代码”，而是“个体效率怎样扩展到团队和公司”。原演讲先承认 AI agents 的局部冲击很强，再指出公司整体只拿到有限提升。B 站解读把矛盾落到工程现场：AI 生成更多代码，但 story 仍不清楚、验收标准仍模糊、review 仍手工、测试仍排队、PR 仍堆积。

这段还引入 [[技术债]] 风险。AI 为满足当前需求可能增加分支逻辑、配置开关和局部补丁；不同人用不同 prompt 生成不同风格和抽象层次；质量保障被推到后面。今天省下的编码时间，可能在未来重构、排障、迁移和 agent 再协作中以更高利息偿还。

### 09:30-19:00：从 Vibe Coding 到 Spec-driven development

当代码变便宜，人类价值上移到三个位置：把问题讲清楚，设计系统边界和约束，做高质量、可验证的工程判断。工程师从“执行者/代码工”变成 [[智能体]] 编排者；PM 从长 PRD 中介变成 spec 与原型迭代者。

B 站把无规范的 AI 编码称为 Vibe Coding：打开 IDE，给模型一句需求，靠 prompt 接龙生成代码。它的问题是不可观测、不可复制、不可维护。组织无法稳定知道输出满足哪些安全、性能、边界和架构条件，也无法把个人经验规模化。

对应解法是 [[Spec-driven development]]：先写清楚做什么、约束是什么、验收标准是什么，再让 AI 生成方案、测试和代码。原演讲明确说高表现企业正从 story-driven development 转向 spec-driven development，PM 与 agents 迭代 specs，而不是反复打磨长 PRD。B 站进一步把 GitHub Spec Kit、Specify / Plan / Tasks / Implement 等作为方法论扩展；这些需要另行核验来源。

### 19:00-28:30：角色、架构和质量体系重写

开发者的高价值不再是敲代码速度，而是能把 agent、工具、规范、审查流程指挥干净。第一层是把业务语言翻译成 specification、structured prompt 和边界条件；第二层是审查逻辑、性能、安全和架构对齐；第三层是系统思维，判断一个 PR 放进整体系统后会不会放大复杂度、制造技术债、让未来 agent 协作更难。

PM 的价值也上移：AI 可以把产品假设快速变成能点、能看、能测的 demo，也可以扫描评论、工单和使用轨迹提取模式、痛点和机会窗口。AI 产品 PM 还必须考虑模型偏差、公平性、可解释性、合规风险、数据策略和模型能力边界。

架构师的重要性被放大。AI 在局部实现很强，但对全局约束迟钝。架构师要把隐性规则显性化，写进 spec、模板、lint、CI/CD、复杂度阈值、依赖方向、分层边界、ModelOps、安全和合规红线。否则 AI 会让系统更快走向“能跑但不可控”。

B 站提到的新岗位包括 AI 流程设计师、AI 评估/审核员、数据策划师、AI Ops、ModelOps、AI 伦理负责人、AI-enabled Scrum Master。这些岗位共同维护的是“人 + AI + 流程”的稳定性，而不是简单把旧岗位加速。

### 28:30-37:44：从采用率到 outcome 度量

McKinsey 原始结尾的重点是企业级 change management：只 rollout AI tools 会出现用量下降或低效使用。需要重置开发者和 PM 的日常角色预期，做 hands-on upskilling、bring your own code、coaches，尤其要在最初几个 sprint 里把 AI 变成工作习惯。变革不是一个大口号，而是沟通、激励、训练、度量、认证、code labs 等二三十个小动作同时做对。

度量体系不能只看 adoption。应从 inputs 到 outcomes 建链：AI 工具投入、upskilling、change management；adoption 的广度与深度；velocity、capacity、developer NPS、开发者是否更享受 craft；代码安全、质量、韧性，priority bugs 的 mean time to resolve；最后连接到 time to revenue、客户扩展、每个 pod 成本和 greenfield / brownfield 再投资能力。

B 站结尾给出一句可复用判断：现在处于“后敏捷、前新范式”的过渡期。AI 把代码变便宜，但让描述意图、设计系统、做高质量决策变得更重要、更难。继续在旧流程里装 AI，像给马车装喷气发动机；真正的任务是重写 AI 原生规范、团队和度量体系。

## McKinsey 原演讲中应保留的细节

- 约 300 家企业调研：个体案例很强，但整体公司级提效常只有 5%-15%。
- 当前多数公司仍沿用 8-10 人团队、两周 sprint 和旧 Agile operating model。
- 任务类型和人的 AI 熟练度都高度不均匀，导致工程经理难以分配 work and resources。
- 模糊 story 与模糊 acceptance criteria 会让 agent 返回不符合真实意图的代码，人工 review 被放大。
- Top performers 将 AI-native workflows 扩展到 SDLC 中 4 个以上 use cases，而不是只做 code review 或 code dev 单点工具。
- AI-native workflows 包括 continuous planning 和 spec-driven development。
- AI-native roles 包括更小的 3-5 人 one-pizza pods，产品构建者用 full-stack fluency 和架构理解来编排 agents。
- 某国际银行案例：agent 根据 team velocity 和 delivery history 分配 sprint stories；团队与 agent 共创 prototypes；围绕 security 和 observability 迭代 acceptance criteria；按 workflow 重组 squad，例如小 bug fixes 与 greenfield development 分开；后台 agent 做跨仓影响分析。
- 该银行案例中提到 agent consumption 超过 60x、code mergers 增加 51%、交付速度和业务优先级更紧密绑定。
- 未来软件开发模型会出现 shorter sprints、smaller teams、但 larger number of teams。
- 开始要早，因为这是 human change，需要时间和路径依赖。

## B 站二次讲解中有价值但待核验的案例

- Netflix：AI 生成代码后测试成为瓶颈，需要 Shift Left，让 AI 同步生成单测/集成测试，并在 CI/CD 中前置质量门槛。
- Goldman Sachs：内部 AI 开发平台理解代码库、文档、架构规范、命名习惯、安全要求和部署脚本；B 站称周期缩短 20%-30%、人均产能提升约 15%、缺陷率稳定或略好。
- Cursor：小核心工程团队让 AI 生成大量代码，人类主攻 spec、系统设计、review 和自动化测试，用于说明规范驱动和小队形态。
- P&G：小团队配 AI 工具可接近传统大团队质量并缩短完成时间。
- The Browser Company / Arc / Dia：AI 降低战略试错和原型成本，让小团队更敢快速换轨。

## 对知识库的增量

这条素材把 [[AI研发提效]] 从“项目级人天节省”推进到“组织级 operating model 改造”：个人任务提效只有进入 spec、测试、review、架构约束、团队角色、度量和变革管理，才可能变成公司级生产率。

它也把 [[Agent Harness]] 的工程视角推进到组织视角：harness 是模型外部的任务运行框架，[[后敏捷操作模型]] 是组织外部的协作运行框架。两者都在解决同一个问题：模型能生成不代表系统能稳定交付。

## 待核验

- 约 300 家企业、5%-15% 公司级提效的调查口径和正式报告来源。
- Carnegie Mellon 关于 AI 生成代码增加 technical debt / complexity 的论文或报告标题。
- GitHub Spec Kit 与 Specify / Plan / Tasks / Implement 的官方来源。
- 银行案例中的 60x agent consumption、51% code mergers、5-6x delivery speed / time to market 的精确口径。
- Netflix、高盛、Cursor、P&G、Browser Company 案例与所有量化数字。

## 相关页面

- [[AI研发提效]]
- [[AI原生组织]]
- [[后敏捷操作模型]]
- [[Spec-driven development]]
- [[AI原生工作流]]
- [[技术债]]
- [[智能体]]
- [[企业上下文]]
- [[Agent Harness]]
- [[企业AI产品案例]]
