<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-07-09 | Updated: 2026-07-09 -->

# 01-原始素材/视频转写（完整视频/播客转写件）

## 目的
高保真视频 ingest 的产物：保留完整转写，不压成泛泛摘要。长视频按时间段拆并行 worker 处理，每段抽取章节、例子、数字、人名/公司/产品名、术语、推理链、ASR 疑点和待核验事实。

## 关键文件
共 58 个转写文件，覆盖张小珺商业访谈录、十字路口、硅谷101等频道。代表性文件：

| 文件 | 说明 |
|------|------|
| `Anthropic团队：如何构建运行 数小时的Agent.transcript.txt` | 长程 Agent 转写（中文） |
| `Anthropic团队：如何构建运行 数小时的Agent.youtube-en.txt` | 同上的 YouTube 英文原文 |
| `Anthropic产品负责人：AI时代，产品经理最值钱的能力是品味.en-original.transcript.txt` | 英文原始转写 |
| `Manus全球爆火，我们独家对话Manus创始人肖弘！.transcript.txt` | Manus 创始人访谈转写 |
| `【十字路口】2026 AI 游戏全景扫描...transcript.txt` | AI 游戏全景扫描转写 |

（完整列表见目录，共 58 个。）

## 子目录
无。

## 给 AI Agent

### 在此目录工作
- **只读**：转写是 source of truth，纠错走 `03-核验/待核验事实.md`，不改原文。
- `.en-original.transcript.txt` / `.youtube-en.txt` 为英文原文/原转写；`.transcript.txt` 为中文转写。归因时区分。
- 高保真 ingest 时：长视频按时间段拆 worker，每段必抽章节/例子/数字/人名公司产品名/术语/推理链/ASR 疑点/待核验事实。
- 区分原始演讲 vs B 站二次讲解 vs 主持人扩展 vs 外部案例，在 `02-知识库/素材/` 写清归因边界。
- 命名格式：`{标题}.transcript.txt`，英文原文加 `.en-original` 或 `.youtube-en`。

### 校验要求
- 转写完整性（长视频是否分段无遗漏）。
- worker 覆盖范围是否覆盖整个时间段。
- 数字/公司案例/论文引用是否分流到 `03-核验/待核验事实.md`。

### 常见模式
- 汇报时列出转写完整性、worker 覆盖范围、graph 节点/边数、validate 结果、commit/push 状态。

## 依赖

### 内部
- 被 `02-知识库/素材/` 摘要引用；待核验点汇入 `03-核验/`。
- 概念汇入 `02-知识库/概念/`，归入 `02-知识库/主题/`。

<!-- MANUAL: -->
