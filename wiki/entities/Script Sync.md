---
tags: [实体, 工具, 同步, Roblox, 官方功能]
created: 2026-06-30
updated: 2026-06-30
sources: [不用再学代码了！零基础AI全自动做Roblox游戏教程]
---

# Script Sync

> Script Sync 是 Roblox Studio 官方提供的脚本同步功能，把 Studio 里的脚本与本地文件夹双向同步，从而让 [[Claude Code]] 这类能直接读写本地文件的桌面型 AI 介入 Roblox 开发。

## 核心内容

在 [[不用再学代码了！零基础AI全自动做Roblox游戏教程]] 中，麦天演示：右键某容器（如 `ServerScriptService`）→ Script Sync → Sync to 选定本地文件夹 → Studio 脚本与本地 `.luau` 文件实时互改（改本地"你好→再见"，Studio 端同步变化）。作者称该功能在录制时"刚从 beta 转正式发布"（**发布时间待核验**）。

有了 Script Sync，[[Claude Code]] 只要把工作目录指到该同步文件夹，即可自动新建/编辑/删除脚本，改动经同步即时反映到 Studio。注意：不同对象树路径（如 UI 用的 `StarterPlayerScripts`）需要分别同步；AI 在本地新建的脚本有时需反向同步回 Studio（会出现版本不一致提示）。

Script Sync（官方）与 [[Rojo]]（社区）是支撑"桌面型 AI agent 做 Roblox 游戏"的两条等价同步管线。

## 待核验

- Roblox Script Sync 从 beta 转正式发布的确切时间。

## 相关页面

- [[AI辅助游戏开发]]
- [[Roblox Studio]]
- [[Rojo]]
- [[Claude Code]]
- [[不用再学代码了！零基础AI全自动做Roblox游戏教程]]
