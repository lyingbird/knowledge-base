---
tags: [素材摘要, B站视频, AI辅助游戏开发, Roblox, Claude Code, vibe coding]
created: 2026-06-30
updated: 2026-06-30
sources: [raw/notes/video-transcripts/不用再学代码了！零基础AI全自动做Roblox游戏教程.transcript.txt]
---

# 不用再学代码了！零基础AI全自动做Roblox游戏教程

> 核心观点：有了 AI 之后，做 Roblox 游戏（尤其写代码部分）不再需要从零学代码；萌新只要会描述需求、大致懂引擎操作，就能用 AI 把功能做出来。开发者的角色从"写代码"转向"产品经理 / 策划 / 设计师"式地和 AI 对话。

## 来源与校准

- B 站：BV15J786XEfk，标题《不用再学代码了！零基础AI全自动做Roblox游戏教程》，UP 主"麦天天天天天"，时长约 26 分 34 秒（1594s）。
- 本地处理：用 faster-whisper large-v3（CUDA/fp16）对 B 站音轨做 ASR（语种=中文，p=0.99），转写存 `raw/notes/video-transcripts/不用再学代码了！零基础AI全自动做Roblox游戏教程.transcript.txt`，段尾对齐视频总时长（差约 0.6s，无截断）。
- 归因边界：本页内容为 UP 主"麦天"的中文原创教学，全部演示由其本人在 [[Roblox Studio]] 中实操；涉及的 [[DeepSeek]]、[[Claude Code]]、Script Sync 评价为其个人使用体验。

## 核心判断

这条素材把 [[AI辅助游戏开发]] 主题落到**最入门的个人实操层**：它不讲行业、不讲工作室提效，而是手把手演示"一个不会写 Luau 的人，如何靠 AI 做出能跑的 Roblox 小功能"。它和 [[游戏工作室AI提效落地框架]]（大厂/工作室视角）、[[AI游戏与虚拟世界]]（行业/试验场视角）形成"个人开发者视角"的补充样本。

麦天的核心主张：**过去"先学引擎 → 再学代码语法/接口"的游戏开发教学已过时**；AI 加持下萌新不必从零学代码，连和代码相关的 UI 也不必专门学。他给出一个对比（个人经验，非统计）：过去开发一个功能要花约 3 天，现在 1-2 小时搞定，"快了一个量级"。

## 两种 AI 接管开发的方式

视频把"让 AI 接管开发"分成两类，并各做一遍同一个 demo（一个会追杀玩家、碰到即死的怪物）来对比。

### 方式一：Chat 型 AI（顾问/向导，手动复制粘贴）

- 适用：几乎所有大模型——国内 [[DeepSeek]]、豆包，海外 ChatGPT、Gemini、Claude。本质上 AI 只是"向导和顾问"，告诉你代码怎么写、怎么贴，但**不直接操控你的项目**。
- 演示流程：在 [[Roblox Studio]] 新建项目 → 用虚拟形象建一个 R6 砖块角色 → 改全黑、删脸、把名字从 rig 改成 monster → 在 model 下新建 script → 把"我在做 Roblox 游戏、用 Luau、场景里有个 model 角色、script 放在 model 下、想让它追玩家且碰到即死"这段需求用自然语言发给 DeepSeek → AI 生成完整脚本 → 复制粘贴回 Studio 的 script → 运行测试。
- 关键经验：① 要先告诉 AI "用什么引擎/什么语言"（Roblox 用 Luau，换 Unity/Unreal 语言不同）；② 不懂脚本放哪、报错怎么办，直接把问题/报错贴回去问 AI；③ 遇到怪物"有 animate 脚本但不播放动画"的问题，反复让 DeepSeek 给"完整脚本"仍报错——作者判断 DeepSeek 在中文环境下"对 Roblox 代码以前还不太到位"，最后**人工**把脚本里错误的 animation id 换成角色自带 run 动画的 id 才修好（待核验：DeepSeek 对 Luau 的能力短板为作者主观判断）。
- 局限：一直在手动复制粘贴，项目一复杂就效率低、手动操作太多。

### 方式二：桌面型 AI（[[Claude Code]] 直接读写本地文件）

- 关键前置——[[Script Sync]]：Roblox Studio 官方新功能（作者称录制时"刚从 beta 正式发布"，**发布时间待核验**），把 Studio 里的脚本双向同步到本地文件夹。演示：右键 ServerScriptService → Script Sync → Sync to 选本地文件夹 → 本地 `.luau` 文件与 Studio 脚本实时互改（改 `print 你好`→`再见`两边同步）。
- 接入：把 Claude Code 的工作目录指到该同步文件夹 → trust workspace → Claude Code 即可读/写/新建/删除该文件夹里的脚本。
- 演示流程：删掉手建 script，只对 Claude Code 发指令（同样告知 Roblox 项目 + Luau + workspace 下有 monster 角色 + 追玩家碰到即死）→ Claude Code 自动创建 `monster ai` 脚本并解释设计 → 测试。再用"产品经理/测试员"口吻反馈"怪物跑起来没动画"→ Claude Code 反问想用哪种行走动画（作者选 Roblox 默认）→ 自动改脚本，动画正常。作者评价 **Claude Code 比 DeepSeek 聪明**（用对了 180 默认行走动画 id）。
- 进阶 demo：让 Claude Code 用**代码方式生成 UI**（"死亡后弹 Game Over UI + 重新开始按钮，点击重生"）。这里暴露一个路径坑：UI 脚本要放 StarterPlayerScripts，得把该路径也用 Script Sync 同步；且 Claude Code 在本地建好脚本后需反向同步回 Studio（出现版本不一致提示，选保留磁盘/本地版本）。最终 GameOver UI 功能跑通。

## 结论与归因

- 作者结论：从需求描述到能跑能玩的小功能，几乎没涉及传统意义的"写代码"，更多是和 AI 沟通、确认需求、调整细节——"做 Roblox 开发的门槛被 AI 拉低了很多"，把想法说清楚，剩下大部分 AI 能搞定。
- 自陈局限：本期只是最基础 demo；多人联机同步、数据存储、复杂 UI 等留待后续视频。
- 提示词心法：把自己当**产品经理/策划/设计师**，描述"要什么效果、哪里有问题"，而不是去想"代码怎么写"。

## 与已有判断的关系

- **落地** [[Claude Code]]：本页是 Claude Code 在 Roblox 游戏开发场景的"桌面型 file-editing agent"用法实例，印证其"直接读写代码库、自动新建/修改文件"的 action-based 特性。
- **对比** Chat 型 AI vs 桌面型 agent：与 [[AI原生工作流]] 中"从复制粘贴到 agent 接管文件"的演进方向一致。
- **补充** [[AI游戏与虚拟世界]]：为"个人/独立开发者用 AI 做游戏"补一个最入门样本，区别于大厂工作室提效。

## 待核验点（详见 03-核验/待核验事实）

- "过去 3 天 → 现在 1-2 小时""快一个量级"为作者个人经验，非统计。
- DeepSeek 对 Roblox/Luau 代码"不太到位"为作者主观判断，且与具体版本/时间相关。
- Roblox Script Sync 从 beta 转正式发布的确切时间需核验。
- Claude Code "比 DeepSeek 聪明"为单次 demo 观察，非基准测试。

## 相关页面

- [[AI辅助游戏开发]]
- [[Roblox Studio]]
- [[Claude Code]]
- [[DeepSeek]]
- [[Script Sync]]
- [[AI游戏与虚拟世界]]
- [[AI原生工作流]]
