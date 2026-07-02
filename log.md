# 操作日志

## 2026-06-03 init | llm-wiki 结构化改造

- 拉取并参考 `sdyckjq-lab/llm-wiki-skill`。
- 新增 `.wiki-schema.md`、`purpose.md`、`index.md` 和 `AGENTS.md`。
- 新增 `raw/` 与 `wiki/` 目录骨架。
- 保留原有 `00-入口/`、`01-主题/`、`02-视频笔记/`、`03-核验/`，作为历史笔记与人类阅读层。

## 2026-06-03 migrate | 第一批主题与实体索引

- 将既有视频笔记的主线改造为 `wiki/topics/` 与 `wiki/entities/`。
- 建立 `[[AI原生公司]]`、`[[企业上下文]]`、`[[业务闭环]]`、`[[智能密度]]` 等核心实体。
- 更新入口与 README，让后续交互默认遵循 ingest/query/digest/lint/graph 工作流。
- 新增 `wiki/knowledge-graph.md` 静态图谱初版。
- 使用 `llm-wiki-skill/scripts/build-graph-data.sh` 和 `build-graph-html.sh` 生成 `wiki/graph-data.json` 与 `wiki/knowledge-graph.html`。

## 2026-06-03 align | Karpathy LLM Wiki 方法论对齐

- 核对 Karpathy `LLM Wiki` 原文后，明确本库三层结构：`raw/` 原始素材层、`wiki/` LLM 维护层、`.wiki-schema.md` / `AGENTS.md` 规范层。
- 将 24 篇历史视频笔记复制到 `raw/notes/video-notes/`，作为不可变素材副本。
- 更新 schema、README、AGENTS 和 index，要求后续 ingest 不只生成摘要，还要更新实体页、主题页、矛盾/核验点、index、log 和图谱。

## 2026-06-03 ingest | 历史视频笔记编译为 wiki

- 为 24 篇历史视频笔记建立 `wiki/sources/` 摘要页，source 页只承载整理后的核心观点、概念链接和待核验点，不替代 `raw/` 中的原始副本。
- 扩展 `wiki/entities/`，新增 [[个人独特性]]、[[共同故事]]、[[AI意识]]、[[柔性心智]]、[[AI代理]]、[[AI原生游戏]]、[[游戏生产管线]]、[[3D生成]]、[[AI创业与投资]]、[[基础模型]]、[[具身智能]]、[[硬科技创业]]。
- 将主题页从旧视频笔记清单升级为 source/entity 网络，便于 Obsidian 双链和离线 HTML 图谱共同使用。
- 下一步每次新增素材都应按 `raw -> sources -> entities/topics -> index/log -> graph` 顺序维护。

## 2026-06-03 ux | 内容优先入口

- 新增 [[Obsidian工作台]]，明确日常阅读、维护和写作应在 Obsidian Markdown 层完成。
- 调整交互式图谱模板为内容优先布局：左侧索引，中间正文，右侧图谱导航。
- 明确 `wiki/knowledge-graph.html` 是离线全局地图，不是主要阅读界面。

## 2026-06-04 intel-gather | 游戏工作室 AI 提效证据

- 以 `/intel-gather` 方式并行拆分 5 条证据线：量化提效、NPC/叙事/语音、资产/3D/美术管线、QA/运营/内部工具、行业报告与落地方法论。
- 新增原始情报副本 [[raw/notes/intel-gather-game-ai-2026-06-04]]。
- 新增 source 页 [[游戏工作室 AI 提效证据]]，汇总 EA、King、Roblox、Ubisoft、KRAFTON、Embark、CDPR/Respeecher、Layer、Capcom、Square Enix、Unity、Google Cloud、GDC 等公开证据。
- 新增综合页 [[游戏工作室AI提效落地框架]]，按自动测试、资产生产、NPC/语音、内部工具、客服运营等环节整理可复制方法。
- 新增实体页 [[AI辅助QA]] 与 [[AI NPC]]，并更新 [[AI游戏与虚拟世界]]、[[游戏生产管线]]、[[AI游戏]]、[[wiki/overview]]、[[index]]。
- 更新静态图谱 [[wiki/knowledge-graph]]；交互式 `wiki/knowledge-graph.html` 需要下次使用原 graph build 脚本重新生成。

## 2026-06-07 graph | 重建游戏工作室 AI 提效图谱

- 重建 `wiki/graph-data.json` 与 `wiki/knowledge-graph.html`，将 [[游戏工作室 AI 提效证据]]、[[游戏工作室AI提效落地框架]]、[[AI辅助QA]]、[[AI NPC]] 纳入交互式图谱数据。
- 核对 [[index]]、[[wiki/knowledge-graph]]、[[log]] 中的 Obsidian 双链，确认三处链接均能解析到现有页面。

## 2026-06-07 ingest | 知乎侯容 AI 产研提效案例

- 导入 B 站视频 `BV1gmLz6BEse`，标题为 [[知乎侯容这段 AI 提效，讲得很实在]]。
- 下载时发现普通 DASH 音频会解码截断，改用 ffmpeg 直链流式转 WAV，完成 34:54 全量转写。
- 按精校流程派出分段代理，分别抽取 00:00-12:00、12:00-24:00、24:00-34:54 的章节、例子、数字、流程和 ASR 疑点。
- 新增原始转写副本 [[raw/notes/video-transcripts/知乎侯容这段 AI 提效，讲得很实在.transcript.txt]]。
- 新增 source 页 [[知乎侯容这段 AI 提效，讲得很实在]]，并新增实体页 [[AI研发提效]]、[[团队知识库]]。
- 更新 [[AI原生组织]]、[[企业AI产品案例]]、[[企业上下文]]、[[业务闭环]]、[[wiki/overview]] 和 [[index]]。
- 将姓名、提效口径、PE/PD 单位、知识库实验、新人上手和虚拟 Agent 接管业务等高风险点加入 [[03-核验/待核验事实]]。

## 2026-06-07 ingest | Cat Wu 谈 Anthropic AI-native 产品组织

- 导入 B 站视频 `BV1tGVm62EGS`，标题为 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]。
- 下载时发现普通 DASH/m4a 容器虽然显示 01:25:34，但 AAC 数据存在断点，先后只解出 16:45 与 27:38；改用 `yt-dlp -g` 直链加 `ffmpeg` 流式解码为 WAV，验证完整 5134.080 秒。
- 完成全量转写，字幕尾部到 01:25:32，共 4840 段；按 5 个时间段派出并行代理精读，保留产品品味、research preview、Cowork 工作流、eval、harness、multi-Claude-ing、95% 自动化不够和 Just do things 等细节。
- 新增原始转写副本 [[raw/notes/video-transcripts/Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味.transcript.txt]]。
- 新增 source 页 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]]，并新增实体页 [[Anthropic]]、[[Claude Code]]、[[Cowork]]、[[产品品味]]、[[Evals]]、[[Cat Wu]]。
- 更新 [[AI原生组织]]、[[企业AI产品案例]]、[[AI人物访谈]]、[[AI原生公司]]、[[智能体]]、[[企业上下文]]、[[wiki/overview]] 和 [[index]]。
- 将 Cowork 命名、Mythos、OpenClaw、Claude Code 泄露、/powerup、code review、Anthropic 增长数字和人物头衔等高风险点加入 [[03-核验/待核验事实]]。


## 2026-06-07 ingest | Anthropic 长程 Agent Harness 工作坊

- 导入 B 站视频 `BV19sGH6UECj`，标题为 [[Anthropic团队：如何构建运行 数小时的Agent]]。
- B 站普通 DASH 音频 30280/30216 解码截断，改用 30232 直链流式转 WAV，核对完整 4539.66 秒；本地 ASR 生成 3397 段，尾部到 01:15:23；另抓取原始 YouTube 英文字幕 4397 块用于术语校准。
- 派出 5 个并行分段代理，覆盖 00:00-17:50、17:50-31:30、31:30-45:00、45:00-62:00、62:00-75:39，保留 Claude Code 演进、RALPH loop、GAN-style harness、completion contract、Retro Forge、trace reading、文件系统共享状态、human-in-loop 和 brownfield 边界等细节。
- 新增 raw 转写副本 [[raw/notes/video-transcripts/Anthropic团队：如何构建运行 数小时的Agent.transcript.txt]] 与英文字幕校准件 [[raw/notes/video-transcripts/Anthropic团队：如何构建运行 数小时的Agent.youtube-en.txt]]。
- 新增 source 页 [[Anthropic团队：如何构建运行 数小时的Agent]]，并新增实体页 [[长程智能体]]、[[Agent Harness]]、[[生成器-评估器架构]]、[[文件系统共享状态]]。
- 更新 [[Anthropic]]、[[Claude Code]]、[[Evals]]、[[智能体]]、[[AI原生组织]]、[[企业AI产品案例]]、[[AI游戏与虚拟世界]] 和 [[wiki/overview]]，把长程 agent harness 接入既有知识网络。
- 将模型版本、METR benchmark、RALPH 来源、人物身份、Retro Forge demo 数字、hooks/auto memory 等高风险事实加入 [[03-核验/待核验事实]]。

## 2026-06-07 ingest | McKinsey 后敏捷 AI 研发 operating model

- 导入 B 站视频 BV1bMq3BTEhX，标题为 [[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]]。
- 普通 DASH 高码率音频解码存在截断，改用可完整解码的 30216 直链/导入音频，核对时长 2264.642 秒，ASR 生成 1194 段，尾部到 00:37:34。
- 另抓取原始英文演讲校准材料：YouTube SZStlIhyTCY 英文字幕与 Sozai transcript；区分 McKinsey 原演讲和 B 站二次讲解案例。
- 派出 4 个分段 agent 精读 00:00-09:30、09:30-19:00、19:00-28:30、28:30-37:44，保留 5%-15% 公司级提效、300 家企业、spec-driven development、one-pizza pods、银行案例、change management、outcome measurement、Netflix/高盛/Cursor/P&G/Browser Company 待核验案例等细节。
- 新增 raw 转写副本 [[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.transcript.txt]]、英文字幕校准件 [[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.youtube-en.txt]] 和 Sozai 校准件 [[raw/notes/video-transcripts/麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率.sozai.txt]]。
- 新增 source 页 [[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]]，并新增实体页 [[后敏捷操作模型]]、[[Spec-driven development]]、[[AI原生工作流]]、[[技术债]]。
- 更新 [[AI研发提效]]、[[AI原生组织]]、[[企业AI产品案例]]、[[智能体]]、[[企业上下文]]、[[Agent Harness]]、[[wiki/overview]] 和 [[index]]，把这条素材接入既有图谱。
- 将 McKinsey 调研口径、CMU 技术债研究、GitHub Spec Kit、银行案例数字、Netflix/高盛/Cursor/P&G/Browser Company 等高风险事实加入 [[03-核验/待核验事实]]。

## 2026-06-14 expand | 新增技术/学习支柱与 GitHub 项目录入

- 把知识库从单一「AI 组织/产品/治理」主题扩展为双支柱：新增「AI 技术与开源项目深入学习」支柱。更新 `purpose.md` 研究范围与关键问题。
- `.wiki-schema.md` 升到 1.2：新增 `raw/repos/` 目录、「GitHub / 开源项目学习素材 Ingest 规范」与「项目学习页结构」模板。
- 消化 `shitagaki-lab/see-through`：raw 副本 + source 页 [[see-through动漫单图图层分解]]，新增实体 [[图层分解]]、[[扩散模型]]，新增主题 [[AI视觉与生成式内容]]。
- 消化 `multica-ai/andrej-karpathy-skills`：raw 副本 + source 页 [[Karpathy编码原则与Claude-Code-Skills]]，新增实体 [[LLM编码原则]]，接入 [[Claude Code]]/[[AI原生工作流]]/[[生成器-评估器架构]]。
- 新增综合页 [[Karpathy开源学习路线]]（micrograd→nanochat 优先级 + 逐仓库学习计划）与主题总入口 [[AI技术与开源学习]]。
- 更新 `index.md`、`03-核验/待核验事实.md`（See-Through 数字/录用、Karpathy 仓库归属与星标待核验）。
- 待办：逐个深入 Karpathy 仓库并建 source 页；按需重建 graph-data.json / knowledge-graph.html。

## 2026-06-15 ingest | 独立开发者克隆 SaaS 月入 3.5 万美元（Starter Story 访谈）

- 导入 B 站中配视频 BV1H27X6YENj，标题《我克隆了3个成功App，现在月入3.5万美元》，上传者 EdgeAITech，时长约 13:38；原始为 Starter Story 频道对 [[Samuel Rondot]] 的访谈。基于既产出的 digest/note/entities/tags/meta 做 ingest，未重新转写。
- 新增 source 页 [[我克隆了3个成功App，现在月入3.5万美元]]，区分嘉宾口述、主持人总结与赞助插播（Mobin）三类归因。
- 开出新主题 [[独立开发与微型SaaS]]，登记为知识库第一条 indie-hacker / micro-SaaS 支线，并与 [[AI创业与投资]] 建立「单人微型 SaaS vs VC/大资本」对照（双向互链）。
- 新增实体页：[[Samuel Rondot]]、[[克隆并改进1%]]、[[公开构建]]、[[程序化SEO]]、[[无脸视频内容]]、[[StoryShort.ai]]、[[UseArtemis]]、[[Capacity.so]]，以及技术栈 [[Next.js]]、[[Node.js]]、[[Vercel]]、[[Stripe]]、[[Outrank]]。
- 更新 [[AI创业与投资]]（加对比段与链接）、[[AI人物访谈]]（加本访谈）、[[index]]、[[wiki/overview]]。
- 将三应用收入（合计 3.5 万/月，34000 vs 35000 矛盾）、单项 15k/20k/0.9k、客户数、StoryShort 月成本 4k–5k、Stripe vs SimilarWeb 流量工具矛盾、Samuel Rondot/Pat Walls/Lemlist/StoryShort/Capacity/Ahrefs/SEObot/Outrank/Vercel 等 ASR 校正点加入 [[03-核验/待核验事实]]。
- 待办：交互式 `wiki/knowledge-graph.html` 与 `wiki/graph-data.json` 需下次用原 graph build 脚本重新生成，以纳入本批新节点。

## 2026-06-14 evaluate | 单图→游戏动态角色资产链路核查

- 应「see-through 能否零手动把静态图变游戏可用动态资产」的提问，核查完整下游链路。
- 核实：see-through 仅出静态 PSD，作者声明非 Image-to-Live2D；StretchyStudio（github.com/MangoLion/stretchystudio，editor.stretchy.studio）自动绑定 PSD 但需 ~30 秒手动调关节；PachiPakuGen（github.com/kazuya-bros/PachiPakuGen）生成眨眼/口型材料给 SpriTalk，需手动配层 + DX12/CUDA。
- 新增综合页 [[单图到游戏角色资产的自动化管线评估]]：结论是 see-through 用于「自动备料」，零手动+高表现力+进引擎目前不成立；并在 [[see-through动漫单图图层分解]] 加下游章节互链。

## 2026-06-14 validate | 单图→游戏角色动画 全链路本机实测 + Godot 引擎验证

- 在本机 RTX 4070 Ti SUPER 上把 `角色图 → see-through 拆层 → 绑骨 → Godot 引擎动画` 三段全部跑通，结论写入 [[单图到游戏角色资产的自动化管线评估]]。
- see-through 本地装好（Python 3.12 venv + torch cu128，跳过 detectron2/mmcv/sam2）；实测基准 1024≈3-4min/17层、1280≈6min/18层；踩坑：16GB 卡禁用 `--group_offload`（否则 2s/step→151s/step 且解码卡死）、禁用 hf-mirror 镜像（与 hf-xet 冲突）改直连。
- StretchyStudio 浏览器实测：17/17 层匹配 + 自动骨架 + 导出 Spine(4.0+)/Live2D/PNG序列。
- Godot 4.6.3 实测：分层 PNG 程序化生成 `.tscn`（无需 MCP）→ 剪纸骨架（头部组绕颈轴旋转）→ 头转动+发摆+呼吸 idle，Vulkan 实时渲染（工程 F:\godot_rig_demo、F:\godot_seethrough_girl）。
- 关键限制：see-through 只对「标准站姿/单角色/手臂可见」效果好；对夸张展开袖+多主体的复杂 hero 立绘会崩（脸糊、手臂丢、配角丢弃），需挑图或逐主体裁切。
- 战略结论：低成本 2D 动画（待机/转头/眨眼/口型档）可行可落地，但强依赖「可绑定友好」的输入；高表现力战斗动画仍需手工绑定。

## 2026-06-23 ingest | AI 超级个体与组织提效

- 全网检索"AI 超级个体 / 组织提效"高质量内容，按 raw → sources → entities/topics → index/log → 核验 流程消化。
- 原始素材副本进 `raw/articles/`：`2026-一人独角兽-Altman赌局与超级个体编排.md`、`2026-超级个体vs超级组织-个体提效不等于组织提效.md`（含来源、抓取日期 2026-06-23、关键论断与数字）。
- 新增 source 摘要页：[[一人独角兽：Altman 赌局与超级个体的编排能力]]、[[超级个体 vs 超级组织：个体提效不等于组织提效]]。
- 新增实体页：[[AI超级个体]]、[[一人公司]]、[[智能体编排]]、[[超级组织]]、[[个人AI工作流]]。
- 新增主题页：[[AI超级个体与组织提效]]，给出"组织规模→1"（一人公司）与"组织内重构"（超级组织）两条放大路径对照表。
- 反向补链：在 [[智能密度]]、[[AI研发提效]]、[[AI原生组织]] 底部加入新页面，避免孤岛。
- 与既有 [[微型巨头：100 倍组织与智能密度]]、[[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 互证：核心判断是"个体提效 ≠ 组织提效"，瓶颈在协调成本、协作效率与组织采用率。
- 高风险事实（Altman/Amodei 预言、一人独角兽实践者收入与人数、超级组织 28 分钟上线/token 占比 15%/采用漏斗、LLM Router 降本 70%、刘世奇案例数字等）已写入 `03-核验/待核验事实.md`，核验前不升级为综合结论。
- 注：本次 source 页引用的"原始副本"改为普通路径文本（非双链），避免在图谱中产生指向 raw 的断链节点。

## 2026-06-23 ingest | Jenny Wen：AI 时代设计职能（本地 ASR）

- 用户给两个 B 站链接（BV1TioVBxEKp、BV1oPAZz2E4i），要求用本地语音转文字模型理解后入库。
- 下载受 B 站 412 风控：yt-dlp 的 bilibili 提取器在本环境网页层被拦；改写脚本走官方 API（view + WBI 签名 playurl）+ 首页 cookie jar，成功取 DASH 音轨，ffmpeg 转 16k 单声道 wav。
- 本地 ASR：faster-whisper large-v3（CUDA/fp16，cu128），两段音频均为英文原音（B 站仅换中文标题）。Jenny 1140 段、Cat Wu 1499 段，各约 5 分钟跑完。
- 去重判断：BV1TioVBxEKp（Cat Wu）= 既有页 [[Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味]] 的同期 Lenny's Podcast 另一搬运版 → 不新建页，只把英文原版转写存入 raw 并在该 source 页补"英文原版交叉核对件"。
- BV1oPAZz2E4i（Jenny Wen）为全新内容 → 新建 source 页 [[传统设计流程已死：Jenny Wen 谈 AI 时代设计]]、实体 [[AI原生设计]]、人物页 [[Jenny Wen]]。
- 反向补链：[[产品品味]]、[[Cowork]]、[[Anthropic]]、[[Cat Wu]]、[[AI与人类独特性]] 各加设计视角段落与链接。
- 核心判断入库：工程倒逼设计、流程"已死"、设计两层分化、build trust through speed、招聘三 archetype（block/深T/cracked new grad）、legibility framework、低杠杆即高杠杆、Cloud Studio→Skills 框架。
- 高风险点（"Opus 4.6"疑 ASR 误听、Cowork 10 天、时间分配比例、Boris/Mike Krieger/Kevin Weil/Evan Tana/Terrence Rohan 转述）入 03-核验/待核验事实.md。
- 转写件存 `raw/notes/video-transcripts/`：Jenny 的 `.transcript.txt` 与 Cat Wu 的 `.en-original.transcript.txt`。

## 2026-06-30 ingest | AI 辅助 Roblox 游戏开发（4 个 B 站视频，本地 ASR）

- 用户给 4 个 B 站链接（BV15J786XEfk、BV1xNRDBWEke、BV1fB7Y6TEoW、BV1CcE46wEmo），要求用本地语音模型炼化入库，跑通则落本地仓库。
- 沿用既定链路：web_fetch 4 链接均 412 风控 → 改走官方 API（nav 取 WBI img/sub key + 签名 playurl + view 取 cid/标题/时长）+ 用户 cookie jar；DASH 音轨经 ffmpeg 流式转 16k 单声道 WAV，4 个时长全部对齐（diff < 1s，无截断）。
- 本地 ASR：faster-whisper large-v3（CUDA/fp16，torch 2.11+cu128）。语种：BV1xNRDBWEke 英文原音（B 站仅换中文标题），其余 3 个中文（含 BV1fB7Y6TEoW 为 tef 英文视频的中文配音搬运）。
- 去重判断：4 个均为全新内容（既有 24 篇为访谈/行业分析，无"个人用 AI 实操做 Roblox 游戏"主题），全部新建 source 页。
- 新增 raw 转写副本 4 份于 `raw/notes/video-transcripts/`（去 BV 前缀命名）。
- 新增 source 页 4 个：[[不用再学代码了！零基础AI全自动做Roblox游戏教程]]、[[Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统]]、[[【中配】用AI制作罗布乐思爆款游戏 其实很简单 - tef]]、[[竟然已经可以游玩了？Roblox AI渲染游戏【Roblox新闻】]]。
- 新增实体页 5 个：[[Roblox Studio]]、[[Model Context Protocol]]、[[Rojo]]、[[Script Sync]]、[[DeepSeek]]；新增主题页 [[AI辅助游戏开发]]（三路径表 + 里程碑式 vibe coding 方法 + 平台级对照）。
- 反向补链：[[Claude Code]]（加"用 Claude Code 做 Roblox 游戏"段）、[[AI原生游戏]]（加平台级 AI 生成世界落差段）、[[AI游戏与虚拟世界]]（接入第三条线）、[[wiki/overview]]、[[index]]。
- 高风险事实（DeepSeek 对 Luau 能力、Script Sync 发布时间、MCP/NCP ASR 疑点、Fable 5、tef 2 小时原型、Roblox 收购 AI 公司/3% 好评率/数百万美元等）写入 [[03-核验/待核验事实]]。
- source 页引用 raw 原始副本用普通路径文本（非双链），避免图谱出现指向 raw 的断链节点。
- 重建 `wiki/graph-data.json` 与 `wiki/knowledge-graph.html`，核对 [[index]]、[[wiki/knowledge-graph]]、[[log]] 双链。
- 任务收尾清理临时下载/ASR 脚本、cookie 文件与中间 WAV（cookie 含敏感凭证）。

## 2026-07-01 intel-gather + ingest | 天美两话题：游戏商业化增量 & 游戏+AI 布局（7 个 B 站视频，本地 ASR）

- 用户提出两个天美视角调研话题：A「跨界思维 × 游戏商业化增量」（经济系统/付费/虚拟资产/IP 衍生/创作者经济/跨界灵感）、B「游戏+AI 布局」（研发提效/下一代范式/AI 无法取代的核心竞争力）。选择"检索 B 站高质量视频候选"。
- 检索：在既有 `.bili_tmp/search_bili.py` 基础上新建 `search_bili_timi.py`（两话题聚焦关键词，宽召回 1332 条→补全 80）+ 第 2 轮 `search_bili_timi2.py`（补创作者经济/皮肤/盲盒/IP 跨界 + 腾讯网易自研/世界模型/AI 美术关卡，宽召回 339）。第 2 轮话题 B 新增 0（已饱和），话题 A 有补充。人工按相关性+深度信号（投币率/收藏率/时长）分层，剔除误命中噪音，产出候选清单 `.bili_tmp/候选清单_天美两话题.md`。
- 用户确认 7 个 BV 入库：话题 A：BV1zh9jByE3y（经济系统）、BV1Af4y1Q7gS（Pay to Win，未入库见下）、BV1X54y1m79Q（王者日赚20亿）、BV1L4znYWEr5（乐高）；话题 B：BV1gjwQznEae（GDC中国位置）、BV1dLosBiExF（米哈游LPM）、BV1sAVr6bEiN（NPC加AI）。
  - 注：实际建 source 页 6 个——BV1Af4y1Q7gS（Pay to Win 氪金演变，42min）与经济系统页高度同源，其要点并入 [[游戏付费设计]] 实体与经济系统 source 页，转写副本仍保留，未单建 source 页。
- 下载：沿用官方 API + WBI 签名 playurl 链路；乐高、米哈游 2 个视频最高码率音轨落在 `mcdn.bilivideo.cn` P2P CDN 导致 ffmpeg 拉流失败，改为优先选 `upos-*` 主 CDN 音轨后成功。7 个 WAV 时长全部对齐（VAD 尾部静音差 <41s）。
- 本地 ASR：faster-whisper large-v3（CUDA/fp16），7 个全部中文，段尾时间对齐视频总时长。转写副本存 `raw/notes/video-transcripts/`（去 BV 前缀命名）。
- 新增 source 页 6 个：[[游戏设计师为什么总是搞不好经济系统（火兰杂谈）]]、[[王者荣耀日赚20亿的商业秘密（海盗Talk）]]、[[乐高的三大商业战略（小Lin说）]]、[[GDC2026观察：AI时代中国游戏在什么位置（退役编辑雨上）]]、[[米哈游LPM大型表演模型（退役编辑雨上）]]、[[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]]。
- 新增实体页 11 个：话题 A——[[游戏经济系统]]、[[游戏付费设计]]、[[游戏长线运营]]、[[IP衍生变现]]、[[创作者经济]]、[[王者荣耀]]、[[天美工作室群]]、[[乐高]]、[[AARRR模型]]、[[跨界商业案例]]；话题 B——[[游戏AI提效]]、[[AI无法取代的核心竞争力]]。更新既有实体 [[AI NPC]]（补和平精英 AI 队友、米哈游 LPM 两条路线与"聪明≠好玩"）。
- 新增主题页 1 个：[[游戏商业化与虚拟经济]]（话题 A 总入口，三层次：游戏内经济/付费、端外 IP/资产、跨界灵感）。更新主题页 [[AI游戏与虚拟世界]]（补 2026-07 大厂 AI 战略与下一代范式段、新素材、新链接）。
- 高风险事实全部写入 [[03-核验/待核验事实]]：王者日活1亿/营收20亿/留存55.9%（约2020口径）、乐高2023营收98亿/利润19亿美元、GDC 36%/106场、和平精英1.1亿用户/开麦率74.72%、米哈游LPM 170亿参数/童馨履历、OpenAI Five TAU/4.5万年、游戏AI史时间点等，核验前不升级为综合结论。
- 归因边界：6 份素材均为 UP 主对公开信息的解读/分析，非厂商官方披露；source 页均标注归因边界与时效。
- 两话题跨主题连接：[[游戏商业化与虚拟经济]]（A）与 [[AI游戏与虚拟世界]]（B）并列互链；[[王者荣耀]] 是两话题共同的天美内部案例交汇点；[[AI无法取代的核心竞争力]] 接 [[AI与人类独特性]]、[[产品品味]]。
- 待办（下一步）：重建 `wiki/graph-data.json` 与 `wiki/knowledge-graph.html`；话题 A 待补跨界案例（泡泡玛特/迪士尼/任天堂/平台经济）与网络文章/GitHub 来源（用户已勾选但本轮仅跑 B 站）；可考虑做 [[comparisons]]：乐高 vs 王者生态化、米哈游 LPM vs 和平精英 AI 队友两条 NPC 路线。


## 2026-07-01 intel-gather + ingest | 两 UP 主精选 12 访谈（张小珺 + 十字路口，本地 ASR，autopilot）

- 用户给两个 UP 主页（UID 505301413 Koji杨远骋·十字路口；280780745 张小珺商业访谈录）+ 新 cookie，要求"今晚下载"，/autopilot 模式。
- 抓取投稿列表：新建 `.bili_tmp/fetch_up_list.py`（space/wbi/arc/search 分页 + WBI 签名），得两 UP 共 82 条、约 129 小时音频（张小珺多为 3-7h 超长访谈，Koji 多为 40-90min）。去重发现张小珺的姚顺宇/Manus出售/朱啸虎/印奇/禾赛已在库。
- 因全量 82 条/129h 音频不现实，用 AskUserQuestion 确认范围 → 用户选"精选高优先级一批（约 10-15 条）今晚跑完入库"。
- 精选 12 条（清单存 `.bili_tmp/精选清单_两UP.md`）：张小珺 6（阳萌/罗福莉/杨植麟/谢赛宁/Kimi K2讲解/Manus肖弘），Koji 6（Agent Harness/前原神主创/AI游戏全景/FDE/OpenClaw/世界模型终局）。
- 下载：复用官方 API + WBI playurl + upos CDN 优选（避 mcdn P2P）链路，`dl_audio2.py`；12 个 WAV 时长全部对齐（谢赛宁 24278s=6.7h 也完整）。
- 本地 ASR：faster-whisper large-v3（CUDA），按时长升序转写，12 个全部完成、全中文、段尾对齐（谢赛宁 6.7h 转写耗时约 35min）。转写副本存 `raw/notes/video-transcripts/`。
- 入库策略：短片我通读精写 source 页；超长片用 Explore agent 并行提炼结构化要点后我据此撰写，边转写边入库以提效。
- 新增 source 页 12 个：[[2026 AI游戏全景扫描：四层图景与共识缺口（十字路口×405游局）]]、[[世界模型的终局之路：因果世界模型（十字路口×黄碧薇）]]、[[FDE：AI时代的新岗位与旧分工松动（十字路口×Rolling AI）]]、[[20个问题搞懂OpenClaw：Agent范式的爆红（十字路口）]]、[[Agent Harness：模型是脑Harness是手（十字路口×MiniMax×Hermes）]]、[[前原神主创聊AI游戏创业（十字路口×恶少）]]、[[Manus爆火时对话肖弘（张小珺商业访谈录）]]、[[杨植麟谈K2与Agentic LLM（张小珺商业访谈录）]]、[[逐段讲解Kimi K2报告：系统工程的力量（张小珺商业访谈录）]]、[[罗福莉谈AI范式巨变与OpenClaw（张小珺商业访谈录）]]、[[阳萌谈第三类公司与端侧模型（张小珺商业访谈录）]]、[[谢赛宁7小时访谈：世界模型与AMI Labs（张小珺商业访谈录）]]。
- 新增实体页 6 个：[[世界模型]]、[[端侧模型]]、[[FDE]]、[[OpenClaw]]、[[十字路口]]、[[张小珺商业访谈录]]。更新已有实体 [[Agent Harness]]（补多 Agent/记忆/人成瓶颈）、[[基础模型]]（补 Agent 范式/世界模型）、[[具身智能]]（补世界模型/端侧）。
- 更新主题页 [[AI人物访谈]]（接入两大深访频道 6+ 素材）；[[AI游戏与虚拟世界]] 已含游戏类新素材的链接。
- 三条世界模型路线在库内形成完整对照：因果世界模型（黄碧薇）vs 具身认知/JEPA（谢赛宁/杨立昆 AMI Labs）vs 生成式实时交互（米哈游 LPM）；共识 LLM 非终局，分歧在路径。多方判断"世界模型对游戏为时尚早"。
- Agent 范式主线由 OpenClaw（罗福莉/十字路口）+ Agent Harness（MiniMax×Hermes）+ 杨植麟（Agentic LLM）+ 库内 Anthropic 长程 Agent 交叉锁定：记忆>智能、框架吃 post-train、多 Agent 互检、群体开源自进化。
- 高风险事实（融资/估值/参数/用户量/benchmark/人名机构）全部写入 [[03-核验/待核验事实]]，核验前不作定论。OpenClaw 名称、罗福莉现职、AMI Labs 数字、恶少提炼数字等标注歧义/存疑。
- 待办：重建图谱、校验双链、清理临时文件；两 UP 剩余约 70 条（含张小珺李想/何小鹏/余凯/SpaceX/DeepSeek论文讲解、Koji 大量创业访谈）未处理，可后续分批。


## 2026-07-01 synthesis + verify | autopilot 收尾（核验/综合/对比/跨界/开源）

- 用户 /autopilot「都做」：自主完成此前列的后续 4 项（除需 cookie 的剩余视频下载）。
- **核验**（联网）：核对 12 项高风险事实。已核验属实：乐高财报、Aether AI 融资、AMI Labs（Yann LeCun 2025-11 离职创办、约 10.3 亿美元融资）、谢赛宁 DiT/NYU、罗福莉 DeepSeek→小米、Kimi K2/Muon。**已修正**：米哈游 LPM 实为蔡浩宇的 **Anuttacon** 发布（2026-04-10，通讯作者曾爱玲）；安克 eufy 安防份额约 6%（非全球第二）。**存疑**：王者「除夕日活破亿」（约 9535 万）、GDC「36% 使用 AI」（官方数据为 52% 认为有害/采用率约 52%）。结论写入待核验，并修正 [[米哈游LPM大型表演模型（退役编辑雨上）]]、[[GDC2026观察：AI时代中国游戏在什么位置（退役编辑雨上）]] 两页。
- **综合报告**：[[天美两话题综合报告：商业化增量与游戏AI布局]]——话题 A（存量健康化 + 增量生态化，含泡泡玛特/乐高/宝可梦/迪士尼/平台经济核实数据）+ 话题 B（研发提效/世界模型/AI NPC/核心竞争力），统一结论「AI 是商业化放大器、产业结构是护城河、产品判断不可替代」。
- **对比页**：[[世界模型三路线对比]]、[[游戏AI NPC两路线对比]]（首次使用 wiki/comparisons）。
- **跨界案例**：充实 [[跨界商业案例]]（泡泡玛特自有IP占76.5%、宝可梦周边占90%、乐高/迪士尼/平台分成，均联网核实标注年份）。
- **开源学习**：新增 [[游戏AI开源项目学习路线（NPC-RL-具身Agent-PCG）]]（斯坦福小镇/street-fighter-ai/Voyager/gym-pcgrl 四项目，raw/repos/game-ai-projects.md），接入 [[AI技术与开源学习]] + [[AI游戏与虚拟世界]]。
- 待办：重建图谱、校验双链、提交推送。仍需 cookie 的两 UP 剩余约 70 条视频未做（cookie 已按安全规范删除）。


## 2026-07-01 ingest | 两 UP 第三批 13 访谈（张小珺 + 十字路口，本地 ASR，autopilot 续）

- 用户提供新 cookie 续做剩余视频。从两 UP 剩余 65 条中精选 13 条（Koji 7 + 张小珺 6，约 20h 音频），避免 90h 全量。
- 下载：官方 API + upos CDN 优选，13 个 WAV 时长全对齐。ASR：faster-whisper large-v3，13/13 全部完成（DeepSeek 讲解 3.3h、李想 2.7h、余凯 2.6h、智谱 2.4h 等超长片），段尾对齐。
- 入库策略：超长片用 Explore agent 提炼要点后我撰写；同嘉宾上下集（课代表）、同主题三期（Claude Code/Paperboy/AirJelly）合并成页，避免碎片化。
- 新增 source 页 11 个：[[MiniMax闫俊杰谈M3与10T模型（十字路口）]]、[[Agent前沿三人谈：Harness三层-人机协作-主动式AI（十字路口）]]、[[高手怎么用AI与2026AI投资观察（十字路口×课代表立正）]]、[[复盘2025年AI和科技大事件（十字路口）]]、[[何小鹏谈人形机器人与物理AI（张小珺商业访谈录）]]、[[李想谈CEO大模型与VLA（张小珺商业访谈录）]]、[[余凯口述30年史（张小珺商业访谈录）]]、[[智谱张鹏：全球大模型第一股上市访谈（张小珺商业访谈录）]]、[[Lovart陈冕复盘AI应用创业（张小珺商业访谈录）]]、[[逐篇讲解DeepSeek 9篇论文：勇敢者的游戏（张小珺商业访谈录）]]。
- 主线补强：基础模型（MiniMax M3/10T、智谱 2B/开源、DeepSeek MLA/GRPO 九论文、Kimi）；Agent（Harness 三层框架、人机协作、主动式 AI，深化 OpenClaw 主线）；具身智能/VLA（何小鹏物理 AI、李想 VLA、余凯地平线芯片）；AI 创业方法论（Lovart 垂类 Agent、课代表方法论、2025 复盘）。
- 更新主题 [[AI人物访谈]]、频道实体 [[十字路口]]/[[张小珺商业访谈录]] 收录清单。
- 高风险事实全部写入 [[03-核验/待核验事实]]。
- 待办：重建图谱、校验双链、提交推送、清理。两 UP 仍剩约 52 条未做（up_videos.json 存清单）。


## 2026-07-01 ingest | 两 UP 第四批 13 访谈（张小珺 + 十字路口，本地 ASR，autopilot 续二）

- 用户续给 cookie。从剩余 52 条精选 13 条（Koji 8 + 张小珺 5，约 25h 音频，含多个 2.5-3h 超长片）。
- 下载 upos CDN 优选、13 个 WAV 全对齐；ASR faster-whisper large-v3 全部完成。超长片用 Explore agent 提炼后撰写；Koji 相近主题合并（AI基础设施=小宿+Zilliz；创投生态=VC复盘+具身300家庭+元理智能+3D蓝海）。
- 新增 source 页 10 个：[[范皓宇谈AI眼镜与顶级产品经理（十字路口）]]、[[AI基础设施：Agent Infra与向量数据库（十字路口）]]、[[十字路口·AI创投生态与赛道观察（VC-具身-ToB-3D）]]、[[阿里Qoder叔同谈AI Coding战场（十字路口）]]、[[杨钊谈可控核聚变（张小珺商业访谈录）]]、[[逐篇解析VLA与机器人基座模型：人是最智能的VLA（张小珺商业访谈录）]]、[[逐篇讲解注意力机制新论文：硬件上的暴力美学（张小珺商业访谈录）]]、[[机器人泡沫了吗：银河通用王鹤谈具身智能真相（张小珺商业访谈录）]]、[[星海图高继扬谈具身智能（张小珺商业访谈录）]]（Koji AI眼镜/基建/创投/Coding 4 页 + 张小珺 核聚变/VLA/注意力/机器人泡沫/星海图 5 页 + 合并页）。
- 主线补强：具身智能（银河通用王鹤「合成数据」vs 星海图高继扬「真实数据」两路线对立，+ VLA 论文讲解 + 车企 VLA，构成完整具身图谱）；基础模型（注意力机制 NSA/MOBA/线性 + DeepSeek 演进）；AI 编程（阿里 Qoder）；AI 基础设施（Agent Infra/向量数据库）；产品品味（AI 眼镜范皓宇）；硬科技/能源（可控核聚变）；创投生态（VC/ToB/3D）。
- 更新主题 [[AI人物访谈]]、频道实体收录清单；高风险事实全部入 [[03-核验/待核验事实]]。
- 待办：重建图谱、校验、提交推送、清理。两 UP 仍剩约 39 条（多为 Koji 中小体量创业访谈 + 张小珺洪乐潼/SpaceX/95后Agent/数据综述/开源论文之旅等）。
