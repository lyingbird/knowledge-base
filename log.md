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
