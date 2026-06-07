---
tags: [素材, B站视频, Anthropic, Claude Code, 长程智能体, AgentHarness]
created: 2026-06-07
updated: 2026-06-07
sources: [raw/notes/video-transcripts/Anthropic团队：如何构建运行 数小时的Agent.transcript.txt, raw/notes/video-transcripts/Anthropic团队：如何构建运行 数小时的Agent.youtube-en.txt]
---

# Anthropic团队：如何构建运行 数小时的Agent

> Anthropic Applied AI 团队把 Claude Code 从短会话编码工具演进为长程 agent 的经验，拆成上下文管理、规划、独立评估、完成契约、文件系统共享状态和 trace 调试六个工程层。

## 来源

- Bilibili：`BV19sGH6UECj`
- B 站标题：Anthropic团队：如何构建运行 数小时的Agent
- 上传者：Easonlee的AI笔记
- B 站上传日期：2026-05-25
- 原始视频：Anthropic Workshop: Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson
- 原始场合：AI Engineer Europe 2026 London Day 1 workshop
- 原始发布时间：2026-05-18（待核验）
- 本地处理：完整 WAV 4539.66 秒，本地 ASR 3397 段；另存 YouTube 英文字幕 4397 块用于专名校准。

## 核心结论

长程 agent 不是“让同一个模型一直写下去”，而是一个围绕模型搭建的 [[Agent Harness]]。这个 harness 要解决三类相互放大的失败：上下文会腐化或焦虑，规划会过载或半途停工，自我评价会把半成品说成完成。可运行数小时的系统必须把状态外部化、把完成标准契约化、把评价者独立出来，并把每次失败写回 prompt、skills、`CLAUDE.md` 或 workflow。

模型变强后，harness 不会消失。旧 scaffold 可能被模型吸收，新的薄弱点会浮现。Ash 的判断是 frontier does not shrink, it moves。工程上应当持续评估哪些机制仍在补模型的 spiky behaviors，哪些已经可以删除。

## 00:00-17:50 模型与 harness 共演化

Anthropic Applied AI 团队讨论的是运行 5-6 小时甚至数天的 [[长程智能体]]，不是一次 prompt 做完的 one-shot demo。Andrew 用 Claude Code 一周年的变化作主线：早期 Claude 连 bash 命令和字符串转义都不稳定，只能跑约 20 分钟；现在 Claude Code 大量由 Claude Code 自身参与编写，并能连续工作数天。这个变化不是单纯模型跃迁，而是模型、Claude Code/Agent SDK、工具权限、context 注入、sub-agent、Skills、server-side compaction 等 harness primitives 的共同演化。

三类结构性失败：

- **Context**：新 session 会失忆；同一窗口跑久会 context rot；接近窗口末尾时会 context anxiety，模型为了赶在窗口耗尽前草率收尾。
- **Planning**：模型开箱不擅长长期规划，容易 one-shot 做所有事、只做半个 feature、或 context 耗尽后留下半成品。
- **Self-evaluation**：模型会对自己的半成品 sycophantic。典型例子是 UI 按钮已经出现，但后端不存在，模型仍判断“功能完成”。

早期 RALPH loop 的价值是 fresh context window、任务拆分和可预测失败。Anthropic 早期 long-running agents harness 先用 initializer 把模糊 prompt 拆成 `featurelist.json`、progress file、Git repo、init script 和 feature flags；每轮读取持久化状态、运行 smoke test、选择一个未完成 feature、实现、用 Puppeteer 验证、通过后 commit 并更新状态。一个具体经验是 JSON 比 Markdown 更不容易被模型覆盖，因此更适合保存 feature list 或 breadcrumbs。

## 17:50-31:30 生成器-评估器与完成契约

[[生成器-评估器架构]] 借鉴 GAN：Generator/Builder 负责构建，Evaluator/Critic/Discriminator 负责评分和批评。关键不是换一个 prompt，而是拆开 context window、system prompt 和 job。Evaluator 不只是读 diff，它要用 Playwright 打开 live page、点击、截图、试用，再把 critique 交还给 generator。

这个结构利用了一个非对称性：把独立 critic 调得严厉是可行的，但让 builder 在创作过程中持续可靠地自我批判很难。单个 agent 自己 review 自己的 PR，容易 rubber stamp。

前端评价被拆成四项 rubric：design、originality、craft、functionality。由于模型在 functionality 上已经较强，团队更强调 design 和 originality，用来抵抗 purple gradients、AI slop aesthetics 等审美惯性。Taste 不是不能评分；前提是把强判断写成 rubric，并用 reference sites / few-shot examples 校准 evaluator。

从漂亮页面走向完整 app 时，系统加入 Planner。Planner 只给高层 spec 和 sprint，不提前写死所有技术细节，因为早期细规划错误会在多小时任务中级联放大。真正的胶水是 completion contract：Generator 写代码前提出 feature 和验证方式，Evaluator 反驳 scope 太大、test 太弱、漏 edge cases，双方通过磁盘 Markdown 文件往返，直到形成细粒度 done contract。之后 evaluator 按 contract 而不是最初模糊 spec 评分。

## Retro Game Maker 对比

同一句 prompt：`build a retro game maker`。

无 harness 版本看起来有 sprite editor、canvas、palette、frame timeline、live preview，但 play mode 里方向键和空格键无效，score、health、entities 像是存在却无法真正玩。它是“表面完成”的典型例子。

有 harness 版本约 6 小时、约 200 美元（转写所得，待核验），产物命名为 Retro Forge。它出现 new project dialog、54 色 palette、8-bit preset、actual game scale sprite、AI-level assistant、debug HUD、可运行 physics loop、玩家移动和城堡墙碰撞。模糊的 “AI features” 被 planner 变成 app 内 AI assistant，例如用户可以要求创建一座城堡并让 sprites 守卫它。

这个例子说明游戏类任务不能只看 UI 表象，必须真实玩、真实碰撞、真实验证。它也连接到 [[AI游戏与虚拟世界]] 和 [[游戏生产管线]]：AI 生成游戏工具要进入可测试行为层，而不是停在资产或界面层。

## 31:30-45:00 细粒度标准与 trace 调试

Evaluator 抓到的不是高级 bug，而是实际使用暴露的问题：FastAPI route ordering、单元测试全绿但生产可能坏掉、delete key 的布尔逻辑 bug。Retro Forge 最终形成 27 条 contract criteria。标准越细，反馈越 actionable；“把它做得更好”只会产生模糊 critique，generator 会继续泛泛修改。

Claude 默认不是好 QA agent。Judge 常有 sycophancy / generosity bias，早期 QA agent 发现 bug 后可能说“以后再修”。调试 harness 的办法不是盲跑更多实验，而是像读 stack trace 一样读 agent traces：看 agent 做了什么，在哪里和人类判断分歧，再把这些分歧回灌到 prompt。团队还会把 transcripts 管道输出到文件，让另一个 agent grep、replay、分析 traces，作为 first pass。

模型变强后，harness 应被测试和删减。Opus 4.5 需要 context reset、sprint decomposition 等机制补 context anxiety；讲者称 Opus 4.6 已能在 single continuous session + compaction 中更久保持 coherence，有时可以等 one-shot generation 完成后再跑 evaluator。结论不是 harness design 死亡，而是每次模型升级后重新判断该保留什么。

## 45:00-75:39 Q&A 与可迁移实践

不必等 Anthropic 内部 harness 才开始。可拼装的 primitives 包括 auto mode、自定义 sub-agents、Evaluator/QA role、严厉 system prompt、详细 rubric、Playwright MCP / Chrome MCP、native app computer use、Skills 打包 grading rubrics。

五条 takeaway：

- self-evaluation 是陷阱，要用 adversarial evaluator；
- compaction 不等于 coherence，lossy summaries 会漂移；
- structured hand-offs 与 clean contexts 仍有价值；
- 主观质量可以评分，只要把判断写成标准；
- 坐下来读 traces，才能知道 scaffold 哪些该删、哪些该留。

关于 [[文件系统共享状态]]：long-lived product 不应依赖有损摘要，而应写状态 JSON、timestamped time log 和 live-updating docs。状态文件至少记录尝试了什么、如何评估、发现什么 bug、实现什么 fix、fix 是否有效、最终状态。版本控制、commits、pull requests、Git worktrees 是多人和多 agent 协作时防止覆盖同一文件系统的成熟机制。

关于 human-in-the-loop：如果确实需要人介入，可以用 hooks 设置 evaluator stop condition，把控制权交给人类，收到 developer message 后继续 loop。但团队更想把稳定性修正 bake into harness，而不是用“插入一个人”遮盖系统问题。实践上可以一次生成 10 个版本，读失败的 7 个 trace，调整 harness prompt，再重跑，直到足够放心全自主运行。

关于 brownfield：该模式更适合 greenfield。brownfield 需要为现有 codebase 建立自己的 rubrics、patterns 和 tests。更完整链路可能是 autonomous monitoring 发现问题，生成 issue 或 feature request，agent 创建 PR，进入 pull review，人类最终 merge。

关于 trace 共情：要读完整 raw trace。Claude for Chrome 的例子是，想象自己闭着眼操作网页，每 10 秒睁眼看一张静态页面，再继续点击。只有站在模型的信息处境里，才能理解 browser-use agent 为什么犯错，并把经验写回 prompt templates、`CLAUDE.md`、skills 或避免规则。

## 可复用工作流

1. 把目标拆成 planner / generator / evaluator 三个角色。
2. 写代码前先让 generator 和 evaluator 通过文件协商 completion contract。
3. Evaluator 必须操作真实产物：浏览器、控制台、network error、UI 截图、键盘交互、端到端行为。
4. 把状态写入文件系统：feature list、progress、contract、trace、评价报告、修复记录。
5. 把 agent transcripts 当 stack trace 读，定位模型判断和人类判断的偏差。
6. 每次模型升级后重新做 eval，删除已经不需要的 scaffold，保留仍能补 spiky behavior 的机制。

## 待核验事实

- Ash Prabaker、Andrew Wilson、Prithvi、Jose 的完整姓名、职务和场次信息。
- 原始视频发布时间、AI Engineer Europe 2026 场次、YouTube id `mR-WAvEPRwE`。
- Boris 一周年推文、Claude Code 自举比例、20 分钟到数天的具体表述。
- METR benchmark 的口径，以及 1h/4h/12h 对应模型版本。
- Opus/Sonnet 4.5、4.6、1M context GA、server-side compaction、Agent Teams、auto memory、hooks 等正式名称与发布时间。
- RALPH loop、Jeffrey Huntley 论文/文章、2025 年 7 月/12 月时间线。
- Retro Forge 成本、耗时、轮次、54 色 palette、27 条 contract criteria 等 demo 细节。

## 相关页面

- [[Anthropic]]
- [[Claude Code]]
- [[长程智能体]]
- [[Agent Harness]]
- [[生成器-评估器架构]]
- [[文件系统共享状态]]
- [[Evals]]
- [[智能体]]
- [[AI原生组织]]
- [[企业AI产品案例]]
- [[AI游戏与虚拟世界]]
