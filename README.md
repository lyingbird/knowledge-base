---
tags:
  - 首页
  - llm-wiki
  - 视频知识库
---

# AI 视频理解知识库

这是一个按 `llm-wiki` 方法改造后的个人知识库：目标不是保存零散笔记，而是把视频、访谈、案例和判断持续沉淀成互相链接的知识网络。

方法论参考 Karpathy 的 LLM Wiki：LLM 不只是检索原始资料，而是把资料读入后持续维护一个结构化 wiki。知识被编译一次，然后随着新素材和新问题持续更新。

## 从哪里开始

- 主索引：[[index]]
- 研究方向：[[purpose]]
- 知识库总览：[[wiki/overview|知识库总览]]
- 离线交互式图谱：`wiki/knowledge-graph.html`
- 原阅读入口：[[00-入口/开始阅读]]
- 待核验事实：[[03-核验/待核验事实]]

## 新的知识层

- `wiki/sources/`：每份素材一页摘要，保留来源、核心观点、待核验点。
- `wiki/entities/`：可复用概念、人物、组织、工具，例如 [[AI原生公司]]、[[企业上下文]]、[[智能密度]]。
- `wiki/topics/`：跨素材主题，例如 [[AI原生组织]]、[[企业AI产品案例]]、[[AI游戏与虚拟世界]]。
- `wiki/synthesis/`：跨素材综合报告、阶段性结论。
- `wiki/comparisons/`：对比分析。
- `wiki/knowledge-graph.html`：离线交互式知识图谱，双击即可在浏览器中探索。

## 三层架构

1. `raw/` 是原始素材层。历史视频笔记已复制到 `raw/notes/video-notes/`，作为不可变素材副本。
2. `wiki/` 是 LLM 维护层。这里的页面会被持续更新、互相链接、合并矛盾和沉淀综合。
3. `.wiki-schema.md` 和 `AGENTS.md` 是维护规范层。它们规定 LLM 后续如何 ingest、query、lint 和更新图谱。

## 原有内容

原来的 Obsidian vault 仍然保留：

- `00-入口/`：入口与写作规范。
- `01-主题/`：旧主题页。
- `02-视频笔记/`：历史视频学习笔记。
- `03-核验/`：待核验事实。

这些内容不会删除。新的 `wiki/` 层会逐步把它们整理成可查询、可链接、可综合的结构。

## 后续怎么添加素材

1. 把原文、转写或链接放进 `raw/` 对应目录，或直接提供给 AI。
2. 在 `wiki/sources/` 创建素材摘要。
3. 抽取实体和主题，更新 `wiki/entities/` 与 `wiki/topics/`。
4. 检查是否修正或挑战已有页面中的判断。
5. 更新 `index.md` 与 `log.md`。
6. 有阶段性洞见时，写入 `wiki/synthesis/`。
7. 需要时重新生成 `wiki/knowledge-graph.html`。

维护规则详见 [[.wiki-schema]]。
