---
tags: [素材摘要, B站视频, AI原生设计, Anthropic, 设计流程, 产品管理]
created: 2026-06-23
updated: 2026-06-23
sources: [raw/notes/video-transcripts/传统设计流程已死：Claude 设计负责人 Jenny Wen 谈 AI 时代设计.transcript.txt]
---

# 传统设计流程已死：Jenny Wen 谈 AI 时代设计

> 核心观点：当工程师能并行跑七个 Claude、随时把想法做成可用原型，"研究→发散→收敛→精美设计稿"的经典设计流程就被工程侧的变化倒逼着失效。设计师的价值从"产出漂亮 mock"转向"帮团队落地、收敛方向、补最后一公里的 polish，并识别那些还说不清但有能量的 illegible 想法"。

## 来源与校准

- B 站：BV1oPAZz2E4i，标题《传统设计流程已死！Claude 设计负责人道出未来趋势 | Jenny Wen》，UP 主"通用人工智障"，上传 2026-03-03，时长约 74 分钟。
- 原始英文播客：Lenny's Podcast，《The design process is dead. Here's what's replacing it.》嘉宾 Jenny Wen（YouTube 原链接 https://www.youtube.com/watch?v=eh8bcBIAAFo ）。
- 本地处理：用 faster-whisper large-v3（GPU/fp16）对 B 站音轨做英文 ASR，转写存 `raw/notes/video-transcripts/`。音频为英文原音，B 站版本仅替换中文标题。
- 归因边界：本页观点全部归属 Jenny Wen 与主持人 Lenny 的对谈；提到的 Boris、Mike Krieger、Kevin Weil、Evan Tana、Terrence Rohan 等为对谈中转述，相关数字与他人观点进待核验。
- 人物：Jenny Wen 现任 Anthropic [[Claude Code|Claude]] / Claude [[Cowork]] 设计负责人，曾任 Figma 设计总监（主导 FigJam、Figma Slides），更早在 Dropbox、Square、Shopify 任设计师。X handle 自述 `@jenny_wen`。

## 核心判断

这条素材把 [[AI原生组织]] 主线从"工程/PM 如何变"扩展到**设计职能如何变**，与 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 形成同一组织内的"PM 视角 + 设计视角"双样本。

Jenny 的主张可概括为：**不是设计行业自己想变，而是工程侧变了，倒逼设计变。** 工程师用 agentic coding 工具能"ship, ship, ship"，设计师与其当 gatekeeper 去阻塞，不如"let them cook"，转而做收敛、连接与 polish。

## 章节拆解

### 设计流程为何"已死"

- Jenny 2025 年 9 月在柏林做过一个 talk 叫《Don't trust the design process》，指那套"研究/发现 → 发散收敛反复 → 当成圣经般保留"的流程基本已死；它在 AI 之前就在衰亡，AI 只是加速。她说才过三四个月这个 talk 自己都觉得过时了，尤其是 Opus（自述"Opus 4.6"，**型号待核验**）发布、大量人在假期里发现并开始用 Claude Code 之后。
- 设计工作被"分层(stratified)"成两类：① **支持实现与执行**——工程师用工具快速做出 scrappy 版本，设计师没时间再做精美 mock；② **创造愿景/方向**——但愿景从"两年/五年/十年 + 精美 deck"收缩为"三到六个月 + 一个指向性原型"，因为技术变化太快，没人知道两年后会怎样。

### 为什么"先 ship 再迭代"在 AI 产品里更优

- AI 模型是非确定性的，无法把所有状态 mock 出来，甚至做不了能跑通的 clickable prototype；必须用真实模型、看真实用户怎么用，才能发现 use case。Cowork、早期 Claude Code 都是用户用出了设计者没预设的用法。

### Anthropic 设计师的一天

- 很大一部分时间是"catch up"：跟研究侧模型进展、各团队的 prototype 和 code name，"我们的 Slack 是金矿"，最好的 AI 新闻其实在公司内部 Slack。
- 时间分配变化（自述）：几年前 mock/prototype 占 60-70%，与工程师 jam/consult 占约 20%，协调会约 10%；现在 mock 降到 30-40%，与工程师直接结对/jam 升到 30-40%，还多出一块"自己写代码做实现与 polish"。
- AI 栈：全 Claude house——Claude chat（已基本迁到 Cowork 处理长任务）、Claude [[Cowork]]、Claude Code（在 VS Code IDE 里改前端，也试着通过 mobile / Slack 远程 @Claude 改一个图标就出 PR）。**仍在用 Figma**：Figma 擅长一次性探索 8-10 个方向、以及字体/视觉/交互的"微方向"，而 coding 工具偏线性、不适合并行铺开。有趣反转：IDE 可能正从工程师手里"过气"，反而变成设计师/PM 改 CSS 的趁手工具。

### 品味与判断：人脑还在哪里有价值

- Jenny 认为 AI 的 taste/judgment/design 会持续变好，"我们可能太执着于'设计师永远更懂'这件事了"。
- 但"决定到底该做什么、什么才重要"仍需有人 accountable——就像今天 Claude 能写全部代码，仍由工程师对"代码是否真能跑、是否在产品里讲得通"负责。她区分：审美意义的 taste 会被追上，但"在分歧中决定该做什么"的 judgment 仍落在人身上（类比放射科：AI 给判断，人负责 sign-off 担责）。

### 聊天界面会消失吗

- 结论：chat 不会消失，terminal 也不会。聊天打开了"无限方式与计算机对话"的灵活性，是之前 baked-in UI 给不了的；同时人也仍喜欢看得见、能点的 UI（Claude 近期上线 widget 让模型 elicit 提问、展示天气/股票等交互卡片，反响好）。未来很可能是**两者结合，且这些 UI 越来越多由模型实时生成**而非手工逐个编码。引 Kevin Weil 观点：talking 能优雅地适配各个智能水平（200 IQ 到 300 IQ 都能聊），所以它随模型变强一直奏效。

### 回到 IC、管理与招聘

- Jenny 这一年在 Anthropic 先做 IC、中间带过几个月团队、又回到全职 IC。理由：想贴近一线、怀疑中层管理在未来是否还稳；做 IC 让她学到一堆只有亲手做才会的硬技能，反过来增强当管理者时的同理心。她在 Figma 时团队峰值约 12-15 名设计师 + 几个 manager。
- 对设计管理的判断：只要有团队就需要 manager，但未来的 manager 不是纯 people management，而是"既给团队方向、又做部分人管理"的合体；建议设计沿用工程的做法——让 EM/总监先轮岗做几个月 IC、真正理解技术怎么变，再去管理。回到 IC 最"生疏"的是重新接受 crit（被高频批评）这种脆弱练习。
- **招聘三种 archetype**（AI 时代尤其重要）：
  1. **Strong generalists（"block 形"）**——不是泛泛的多面手，而是在几项核心技能上都到 80 分位、技能图形近似一个"方块"；因为设计角色在向 PM 形、工程形拉伸，多项强技能的人最易 flex。极难招。
  2. **Deep specialist（T 形的"深 T"）**——T 的竖笔比别人更深，处于行业 top 10%；例如技术深到接近半个软件工程师，或视觉/图标设计极强。在"人人都能做出东西"的时代，深专长帮助产品差异化。
  3. **Cracked new grad**——早慧、谦逊、极强学习欲的应届生；大多数公司只招资深，但角色变化太快，"白板 + 快学 + 没有固化流程仪式"反而极有价值。
- 给年轻设计师建议：别停在理论，**多 build 真东西、分享、找社区**（提到母校的 Socratica：像做科学项目一样造东西展示，有人造跑在 Claude 上的机器人、有人给波士顿的巴士贴 googly eyes，强调 agency）。给资深设计师：不必学到从零写代码，但要把 coding 工具纳入工具箱、知道怎么用现有工具，而非去专门学 React。当前 Claude 还不够格被当设计师"录用"——擅长出 first pass 和铺多个想法，但还没到 special & hireable。

### 管理心法与框架

- **低杠杆即高杠杆**：她不认同"低杠杆的事就别做"的两矩阵建议；恰恰是 senior leader 亲自 dogfood 死磕产品、亲自提 PR（提到 Mike Krieger 自己提 PR）、亲手给同事 vibe-code 一张周年卡，这些"看似低杠杆"的事因为是 leader 在做而变成高杠杆，建立产品熟悉度与"无人之事低于我"的团队氛围。
- **鼓励"互相 roast"**：不是强制，而是把它当心理安全(psychological safety)的信号——团队能互相打趣、也敢打趣 leader，说明不怕你、信任你。同时必须配"高标准"：先有心理安全，再施加高标准反而更容易（无惧地给）。类比"严格的家长"，呼应 Radical Candor（深切关心 + 直接挑战）。
- **Legibility framework**（来自 SPC partner Evan Tana 的二乘二）：founder 与 idea 各分 legible/illegible。两者都 legible 的点子往往不新、已被人做；真正有趣的是 **illegible idea**——在前沿、别人还没 get、或没被讲清。设计师（尤其前沿实验室）的一部分工作就是在内部 Slack 里识别这些"说不清但有能量"的想法，用 storytelling 或 UX 形态把它 transform 出来。案例：内部原型 Cloud Studio（dense、跑在某 agentic harness 上、展示 Claude 的知识/技能/输出预览）当时她"看不懂但感到有能量"——后来从中长出了 **Skills 框架**（指导 Claude 行为的 markdown 文件），其信息呈现形态也被她借鉴进 Cowork 的 plan/to-do 设计。她提出"设计师应该更像内部 VC"。
- 主持人补充其与 Terrence Rohan 的研究：早期加入后来巨大成功公司（Palantir、Stripe、Linear、Notion、OpenAI）的人，看重的信号之一是"点子疯狂到大家都在笑/觉得不可能"，以及"有人对某事异常兴奋（即便你不 get）"，再加"founder 是 top 1%"。

### Cowork 的"10 天"真相

- 网上疯传 Cowork "只用 10 天造出来"，Jenny 澄清：那 10 天只是从"内部已有的东西"打磨到"可对外发布"的时间；之前已在多个 agent harness 上做了大量探索、对 to-do 列表/多选问题/use case 引导试过很多 form factor。是"想法一直回来、总不是对的时机，直到突然时机对了、显得理所当然，但背后是很长的旅程"。她最自豪的就是"真的把它 ship 出去了"，正迭代 homepage 让它更像"你和 Claude 共享的 to-do 列表"。对 Cowork 的一句话定义认可主持人的"Claude with hands"，并补充"Claude 很擅长把你的一堆杂物变成好东西"（给它一个文件夹就能抽取价值）。

### 信任与速度（与已有页面强一致）

- 用"research preview"标签发布早期、有瑕疵但有价值的产品（Cowork 即如此，"这是它最差的时候"）；但必须兑现承诺——持续迭代、公开回应反馈、快速修复，否则"发了早期版却没下文"才会损伤品牌。她把这总结为**building trust through speed**，并强调让用户"感到被听见"。这与 [[产品品味]]、[[Claude Code]] 页中 Anthropic 的 research preview / dogfooding 机制完全一致，是设计视角的二次印证。

## 与已有判断的关系

- **强化** [[Anthropic]] / [[产品品味]] / [[Cowork]]：从设计侧再次印证 research preview、dogfooding、build trust through speed、mission-aligned 低流程，是同一组织机制的不同切面。
- **新增设计维度**：[[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 讲工程 operating model 重写、Cat Wu 讲 PM 品味，本页补上**设计职能**的重写——三者共同支撑"AI 让实现变便宜后，人类价值上移到判断、收敛与方向"。
- **呼应** [[AI超级个体与组织提效]]："七个 Claude 并行""如何跟上我们自己/我们的 agent"是个体被放大后组织协作压力的具体写照；设计师做收敛与方向正是"组织内重构"路径下的新协作角色。
- **关联** [[AI与人类独特性]]：taste 会被追上、但 accountability/judgment 仍属人，是 AI 时代人类独特性的产品化注脚。

## 待核验点（详见 03-核验/待核验事实）

- 模型型号"Opus 4.6"是否口误（ASR 听写），以及对应真实发布版本与时间。
- Cowork "10 天"、Figma 团队"12-15 设计师"、设计师时间分配"60-70%→30-40%"等均为 Jenny 自述约数。
- Boris（Claude Code 负责人）"Claude Code 帮他想点子"、Mike Krieger 亲自提 PR、Kevin Weil 关于 talking 的观点、Evan Tana legibility framework、Terrence Rohan 早期加入者研究等为对谈转述。
- "100% 代码由 AI 写""最好的工程师已不看代码"为对谈中的概括表达，非严谨统计。
- Socratica、Retro（周相册 app）、推荐书目（《The Power Broker》《Insomniac City》）等为个人推荐，非知识库结论。

## 相关页面

- [[AI原生设计]]
- [[产品品味]]
- [[Cowork]]
- [[Anthropic]]
- [[Claude Code]]
- [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]
- [[AI与人类独特性]]
- [[AI超级个体与组织提效]]
