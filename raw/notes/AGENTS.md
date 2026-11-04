<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-07-09 | Updated: 2026-07-09 -->

# raw/notes（手写笔记 · 转写 · 外部 Markdown）

## 目的
`raw/` 下的笔记类素材：手写笔记、外部 Markdown、intel-gather 采集汇总，以及视频笔记/转写的不可变副本。

## 关键文件

| 文件 | 说明 |
|------|------|
| `intel-gather-game-ai-2026-06-04.md` | `/intel-gather` 5 个并行 agent 汇总的游戏工作室 AI 提效证据，作为 `wiki/` 层的原始情报副本（原始 agent 输出在外层工作台） |

## 子目录

| 目录 | 用途 |
|------|------|
| `video-notes/` | 从 `02-视频笔记/` 复制来的不可变素材副本（见 `video-notes/AGENTS.md`） |
| `video-transcripts/` | 完整视频/播客转写件，高保真 ingest 产物（见 `video-transcripts/AGENTS.md`） |

## 给 AI Agent

### 在此目录工作
- `intel-gather-*.md` 是多 agent 并行采集的情报副本，引用时区分采集日期与归因边界，原始 agent 输出不在本仓库。
- `video-notes/` 与 `video-transcripts/` 都是不可变副本，只读。
- 新的外部 Markdown 素材可放本目录，并在 `wiki/sources/` 建摘要。

### 校验要求
- 采集件的数字/案例是否分流到 `03-核验/待核验事实.md`。
- 采集件是否已被 `wiki/sources/` 消化（如 `游戏工作室 AI 提效证据`）。

### 常见模式
- intel-gather 汇总件按「工作包 A/B/C/D…」组织，每个工作包覆盖一个证据切面。

## 依赖

### 内部
- `video-notes/` 内容源自 `02-视频笔记/`。
- 采集件喂给 `wiki/sources/` 与 `wiki/synthesis/`（如 `游戏工作室AI提效落地框架`）。

<!-- MANUAL: -->
