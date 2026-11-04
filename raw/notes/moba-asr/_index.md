---
tags: [索引, B站ASR, 知识库原料]
created: 2026-07-12
updated: 2026-07-12
source: 库 A ~/.claude/kb/_corpus/bilibili-transcripts/ + 2026-07-12 新抓取 7 视频
---

# B站 ASR 转录稿总索引

> 772 篇 B站视频 ASR 转录稿,按内容主题归入 7 个目录。原料来自库 A(824+ 篇,可再生)及 2026-07-12 新抓取的 7 个视频(Codex/Anthropic/OpenAI/Huberman/MiniMax 等)。

## 主题目录

| 主题 | 篇数 | 时长 | 入口 |
|---|---|---|---|
| AI前沿人物 | 13 | 15h26m | [[AI前沿人物/_index|AI前沿人物 索引]] |
| Supercell与游戏公司 | 9 | 1h13m | [[Supercell与游戏公司/_index|Supercell与游戏公司 索引]] |
| 游戏开发技术 | 11 | 3h04m | [[游戏开发技术/_index|游戏开发技术 索引]] |
| 游戏文化与历史 | 48 | 9h08m | [[游戏文化与历史/_index|游戏文化与历史 索引]] |
| 游戏设计方法 | 611 | 399h00m | [[游戏设计方法/_index|游戏设计方法 索引]] |
| 游戏试玩评测 | 65 | 70h00m | [[游戏试玩评测/_index|游戏试玩评测 索引]] |
| 超级个体与一人公司 | 15 | 5h59m | [[超级个体与一人公司/_index|超级个体与一人公司 索引]] |

**总计**: 772 篇 · 总时长 503h53m

## 使用方式

- **全文搜索**: Ctrl+Shift+F 搜任意关键词
- **DataView**: frontmatter 含 `bvid`/`author`/`duration_sec`/`title`/`url`
- **双链**: `BV号文件(如 BV1xxxxxx.md)` 可链接到具体转录稿
- **主题入口**: 每个主题目录有 `_index.md`

## 注意

- ASR 转录含同音误转,高风险事实请交叉核验(见 `03-核验/待核验事实.md`)
- 库 A 原料用 Qwen3-ASR-1.7B;2026-07-12 新抓取的 7 个用 faster-whisper large-v3(CUDA/fp16),质量更高
- 与 `raw/notes/video-transcripts/`(高保真手动转写)是不同来源
