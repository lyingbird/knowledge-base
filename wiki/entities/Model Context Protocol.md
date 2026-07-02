---
tags: [实体, 协议, AI接口, MCP, Anthropic]
created: 2026-06-30
updated: 2026-06-30
sources: [Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统]
---

# Model Context Protocol

> MCP（Model Context Protocol）是让 AI 模型与外部工具/数据源标准化连接的协议；在游戏开发场景下，它让 Claude Desktop 通过插件直接操作 [[Roblox Studio]] 的运行时对象。

## 核心内容

MCP 是 Anthropic 推动的开放协议，定义"MCP server（暴露能力的一方）↔ MCP client（模型一方）"的连接方式。它把"AI 能调用哪些外部工具"从一次性集成变成可复用的标准接口。

在 [[Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统]] 中，MCP 的具体形态是：

- Roblox 官方提供 **Roblox Studio MCP server 插件**（装进 Studio 的 Plugins 文件夹）。
- 把对应的 MCP server 配置写进 **Claude Desktop** 的 config JSON（仅桌面版支持 MCP）。
- 连通后，在 Claude 里发自然语言 prompt，即可让模型直接在 Studio 里创建/修改 UI 与对象（如一句话生成血条 HUD、地图、背包 GUI）。

这与 [[Script Sync]] / [[Rojo]]（同步本地文件给 [[Claude Code]]）路线不同：MCP 让模型**直接接管创作工具本身**，而非通过文件中转。

## 与已有判断的关系

[[Claude Code]] 页指出 MCP 是长程 [[Agent Harness]] scaffold 的组成部分之一。本页给出 MCP 接入第三方创作工具（Roblox Studio）的具体落地案例。

## 待核验

- ASR 在来源视频中把 "MCP" 误识别为 "NCP"。
- "MCP 仅支持 Claude Desktop、不支持网页版"为视频时点说法。

## 相关页面

- [[AI辅助游戏开发]]
- [[Roblox Studio]]
- [[Claude Code]]
- [[Anthropic]]
- [[Roblox Studio 接入 Claude MCP：自动生成游戏内 GUI 系统]]
