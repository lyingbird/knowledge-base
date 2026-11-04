<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-07-09 | Updated: 2026-07-09 -->

# wiki（LLM 维护层）

## 目的
Karpathy LLM Wiki 三层架构中的 **第二层：LLM 维护层**。这里的页面由 LLM 生成并持续维护：素材摘要、实体页、主题页、对比、综合和知识图谱。核心理念是「编译一次并持续维护」，新素材必须**整合进已有页面**，而不是只追加孤立摘要。

## 关键文件

| 文件 | 说明 |
|------|------|
| `overview.md` | 知识库总览：当前主线、知识结构、维护重点，两条支柱（产业 / 技术学习）的总入口 |
| `knowledge-graph.md` | 静态 Mermaid 知识图谱（日常阅读用） |
| `knowledge-graph.html` | 离线交互式知识图谱（浏览器双击即可探索，自包含查看器） |
| `graph-data.json` | 图谱节点/边数据，由 wiki Markdown 双链派生，**勿手改** |
| `graph-wash.js` / `graph-wash-helpers.js` | 交互图谱运行时逻辑，**勿手改** |
| `d3.min.js` / `marked.min.js` / `purify.min.js` / `rough.min.js` | 第三方 vendored 库，**勿手改** |
| `LICENSE-d3.txt` / `LICENSE-marked.txt` / `LICENSE-purify.txt` / `LICENSE-roughjs.txt` | vendored 库许可证 |

## 子目录

| 目录 | 用途 |
|------|------|
| `sources/` | 素材摘要页：每份素材一页（见 `sources/AGENTS.md`） |
| `entities/` | 实体页：人物、组织、概念、工具（见 `entities/AGENTS.md`） |
| `topics/` | 主题页：跨素材研究主题（见 `topics/AGENTS.md`） |
| `comparisons/` | 对比分析页（见 `comparisons/AGENTS.md`） |
| `synthesis/` | 综合分析页：阶段性结论（见 `synthesis/AGENTS.md`） |
| `queries/` | 保存的查询结果（当前为空，schema 预留桶） |

## 给 AI Agent

### 在此目录工作
- **新增素材绝不只加摘要页**：必须走 `raw → sources → entities/topics → index/log → graph`。新信息要整合进已有实体页、主题页，补交叉引用，标记矛盾或待核验点。
- **页面 front-matter** 遵循 `.wiki-schema.md`：`tags` / `created` / `updated` / `sources`。
- **双向链接**用 Obsidian 语法 `[[真实页面名]]`；新 wiki 层优先短页面名（`[[智能密度]]`），链旧笔记保留路径（`[[02-视频笔记/...]]`）。每个实体/主题页底部维护「相关页面」。
- **图谱文件不要手改**：`graph-data.json` 和 `knowledge-graph.html` 由外部 `llm-wiki-skill` 的 `build-graph-data.sh` / `build-graph-html.sh` 脚本生成（本仓库未 vendored 这些脚本）。知识网络变化时重建二者，并核对 `index.md`、`knowledge-graph.md`、`log.md` 的双链。
- vendored 的 `*.min.js` 和 `LICENSE-*.txt` 是交互图谱依赖，不要编辑。

### 校验要求（Lint，见 `.wiki-schema.md`）
- 孤立页面（无入链/出链）、断链（双链指向不存在页面）。
- 索引不一致（`index.md` 漏掉重要页面）。
- 概念重复（同一概念多个近义词页，查别名词表）。
- 待核验高风险事实未进 `03-核验/待核验事实.md`。
- 停滞综合（新素材没反映进实体/主题/综合页）。
- 素材孤岛（`sources/` 页只链原文，不链任何实体/主题）。

### 常见模式
- ingest 完整流程：`sources/` 摘要 → 抽 3-5 概念进 `entities/` → 归入 `topics/` → 检查矛盾/修正/强化 → 更新 `index.md`+`log.md` → 必要时更新 `overview.md` → 重建图谱。
- 高保真视频 ingest：保留完整转写到 `raw/notes/video-transcripts/`，按时间段拆并行 worker，严格区分原始演讲 vs 二次讲解 vs 主持人扩展。

## 依赖

### 内部
- `raw/` 是事实来源；`index.md` / `log.md`（在仓库根）是全局索引与操作日志；`03-核验/待核验事实.md` 收高风险事实。
- `overview.md` 汇总各 `topics/` 主线。

### 外部
- 交互图谱依赖 d3 / marked / DOMPurify / rough.js（均已 vendored）。
- 图谱构建依赖外部 `llm-wiki-skill` 脚本（不在本仓库）。

<!-- MANUAL: -->
