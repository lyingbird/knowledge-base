# MOBA ASR 语料池接入计划

> 这页用于管理 `D:\工作\Crawler\MOBA_Related` 的本地视频转文字语料。它不是最终知识页，而是把“能否继续跑、如何清洗、怎样入库”的决策固定下来。

## 当前判断

这批语料值得保留和接入，但不应继续盲目扩大生产。

审计结果显示：

- 已扫描 Markdown 产物：796 篇。
- 正文初筛可用：679 篇。
- 需要编码修复：82 篇。
- 过短或疑似无效：35 篇。
- ASR 超时：13 个视频。

结论：

- `transcript/` 与 `output/` 应视为 raw source material，而不是最终笔记。
- GDC 英文演讲类材料的正文转录总体可用，适合先做知识炼化。
- 中文标题、UP 主、章节名和部分描述存在明显 mojibake，需要修复或重抓 metadata。
- 大规模继续 ASR 的边际收益暂时低于清洗和入库。

## 关键位置

- 项目目录：`D:\工作\Crawler\MOBA_Related`
- ASR 模型：`D:\工作\Crawler\MOBA_Related\models\Qwen3-ASR-1.7B`
- 音频：`D:\工作\Crawler\MOBA_Related\audio`
- 原始转录 JSON：`D:\工作\Crawler\MOBA_Related\transcript`
- Markdown 产物：`D:\工作\Crawler\MOBA_Related\output`
- 审计报告：`../workspace-audits/B站转录/moba-asr-quality-audit.md`
- 审计明细：`../workspace-audits/B站转录/moba-asr-quality-audit.csv`
- 修复预览：`../workspace-audits/B站转录/repair-preview/`
- 审计工具：`../tools/moba-asr-quality-audit.ps1`

## 第一批优先级

先处理正文长、主题价值高、metadata 完整的 GDC / 游戏设计类材料。

优先候选：

- BV166cwzoE9u
- BV19cBMBMEC5
- BV1FkL16KE8x
- BV1R9hGzXEcz
- BV1DhWtzuERe
- BV1EXDJBjEmS
- BV1BHfuBKEPL
- BV1JB5x6VENZ
- BV1KdjizzEJm
- BV19Zc4zHEdH

这些文件的优势是 transcript 较长，适合提炼为 `02-知识库/素材/` 页面，并沉淀到游戏设计、开放世界、叙事设计、扩展包设计、系统设计等实体页。

第一批 raw 副本已经放在：

- `01-原始素材/B站转录/gdc-game-design-first-batch/`
- `01-原始素材/B站转录/gdc-game-design-first-batch/manifest.csv`

后续不要直接修改 `D:\工作\Crawler\MOBA_Related\output` 里的原始产物；所有清洗、摘要和炼化都以这批 raw 副本为工作对象。

## 暂缓项

以下内容先不进入第一批：

- `too_short` 状态的 35 篇。
- `asr_timeout.log` 中的 13 个超时视频。
- `needs_encoding_repair` 状态中替换字符很多的文件。
- 只有标题/描述有价值、正文很短的短视频。

## 下一步操作

1. 用审计 CSV 选出第一批 10 篇候选。
2. 为候选生成 `01-原始素材/B站转录/` 清洗副本，不覆盖原始产物。
3. 每篇清洗副本保留 BVID、URL、ASR 模型、crawl_time、transcript_chars。
4. 生成 `02-知识库/素材/` 摘要页，每页只承载核心观点、证据片段、待核验点和相关实体链接。
5. 新增或更新实体页：`游戏叙事设计`、`开放世界叙事`、`扩展包设计`、`游戏系统设计`、`玩家反馈闭环`。
6. 更新主题页 `AI游戏与虚拟世界` 或新增 `游戏设计` 主题页。

## 继续/换方向决策

当前不换方向，但切换工作重心：

- 从“继续跑更多 ASR”切到“清洗、评分、筛选、入库”。
- 当第一批 10 篇能稳定产出高质量 source/entity/topic 页面后，再恢复增量 ASR。
- 如果第一批发现正文 ASR 错误密度过高，再评估是否换 ASR 模型或只保留 metadata。
