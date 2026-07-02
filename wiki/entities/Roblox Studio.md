---
tags: [实体, 工具, 游戏引擎, Roblox, UGC平台]
created: 2026-06-30
updated: 2026-06-30
sources: [不用再学代码了！零基础AI全自动做Roblox游戏教程, Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统, 【中配】用AI制作罗布乐思爆款游戏 其实很简单 - tef]
---

# Roblox Studio

> Roblox 官方的游戏创作工具（用 Luau 脚本），是当前一批"用 AI 做游戏"教程的共同落地场——AI 写的代码/生成的对象最终都要进 Studio 运行。

## 核心内容

Roblox Studio 是 UGC 游戏平台 Roblox 的开发环境，使用 **Luau** 语言（Lua 方言）。脚本按层级组织（如服务端脚本放 `ServerScriptService`、玩家端 UI 脚本放 `StarterPlayerScripts` / `StarterGui`），对象以 model/角色/script 的树形结构管理。

在 AI 辅助开发语境下，Studio 是"AI 产物的落地场"，有三条把 AI 接进来的路径：

- **Chat 型 AI + 手动粘贴**：AI 出代码，人复制进 Studio 的 script（见 [[不用再学代码了！零基础AI全自动做Roblox游戏教程]] 的 [[DeepSeek]] 演示）。
- **本地文件同步 + 桌面 agent**：用 [[Script Sync]]（官方）或 [[Rojo]]（社区）把 Studio 脚本与本地文件夹双向同步，再让 [[Claude Code]] 直接读写本地文件。
- **[[Model Context Protocol|MCP]] 桥接**：通过官方 Roblox Studio MCP 插件让 Claude Desktop 直接操作 Studio 对象树（见 [[Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统]]）。

## 平台级 AI 动向

Roblox 不只是被 AI 工具改造的开发环境，平台自己也在推"AI 实时生成可玩世界"。[[竟然已经可以游玩了？Roblox AI渲染游戏【Roblox新闻】]] 记录了其 research preview 的实测：概念上属 [[AI原生游戏]]，但体验远未成熟。Roblox 也是 [[游戏工作室AI提效落地框架]] 中被反复引用的工作室 AI 提效证据来源之一。

## 相关页面

- [[AI辅助游戏开发]]
- [[Claude Code]]
- [[Script Sync]]
- [[Rojo]]
- [[Model Context Protocol]]
- [[AI原生游戏]]
- [[AI游戏与虚拟世界]]
