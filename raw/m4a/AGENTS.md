<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-07-09 | Updated: 2026-07-09 -->

# raw/m4a（手机录音 · 转写工序）

## 目的
视频/音频→文本管线中的**录音中转站**。手机录音（m4a，噪音较多、电平偏低）在此用 faster-whisper large-v3 直转为带时间戳文本，输出到 `raw/notes/video-transcripts/`。

## ⚠️ 重要：不要对录音做神经降噪前置（实测纠错）

2026-07-09 实测结论：**对 faster-whisper 转写，原始直转质量最佳，去噪反而有害。**

A/B 测试（同一 4 分钟片段 × 4 变体，无 VAD 隔离音频处理变量）：

| 变体 | 关键实体「来天美的成都」 | 「在腾讯」 | 「为什么是游戏科学」 | 评价 |
|------|---|---|---|---|
| **A 原始直转** | ✅ 来天美的成都 | ✅ 在腾讯 | ✅ 游戏科学 | **最佳** |
| B dns64 神经降噪(无 loudnorm) | ❌ 根本没给大家做 | ❌ 在重新 | ❌ | 差 |
| C afftdn 轻度谱减法 | ⚠️ 天美的**杭州**(错) | ✅ | — | 无提升 |
| D dns64+loudnorm(激进) | ❌ 我来感受/好的气息 | ❌ | ❌ | 最差 |

**原因**：whisper large-v3 训练时已见过各种噪声，能自行处理背景噪声；神经降噪（dns64）会把语音当噪声压掉，引入的**失真比噪声更伤转写**。这些录音 SNR≈10dB（有噪声但可懂），属 whisper 能处理的范围。之前犯的错：只盯着「底噪=-inf」指标，没验证语音是否被损伤（Crest factor 18→6 已是损伤信号，被忽略）。

## 关键文件

| 文件 | 说明 |
|------|------|
| `transcribe.py` | **转写脚本**（可复用）：原始 m4a → large-v3 → 带时间戳文本，保守 VAD（min_silence_duration_ms=2000）避免切碎句子 |
| `merge_sentences.py` | **句子合并后处理**：碎片段 → 可读整句（30字/句末标点断），产出 `.readable.txt` |
| `*.m4a` | 手机原始录音（5 个，共 ~493MB，gitignore 本地保留） |

## 子目录

| 目录 | 用途 |
|------|------|
| `digest/` | 内部分享知识包（INDEX + 5 个结构化 digest，供 agent 使用，见 `digest/INDEX.md`） |

## 转写管线（transcribe.py）

`原始 m4a → faster-whisper large-v3 (language=zh, beam_size=5) → 16k mono → 带时间戳 .transcript.txt + 纯文本 .full.txt`

**VAD 参数**：`vad_filter=True, min_silence_duration_ms=2000, speech_pad_ms=200, threshold=0.5`。只过滤 >2s 长静音，不切自然停顿（之前用 500ms 把句子切碎成单字）。

**用法**：`python transcribe.py` 转文件1 / `python transcribe.py all` 转全部 / `python transcribe.py "文件.m4a"` 指定。

## 给 AI Agent

### 在此目录工作
- 转写**直接用原始 m4a**，不要做神经降噪前置（已实测有害，详见上方 A/B 表）。
- 产出在 `raw/notes/video-transcripts/{文件名}.transcript.txt`（带时间戳）和 `.full.txt`（纯文本）。
- 依赖：`faster-whisper`(large-v3，首次自动下载 ~3GB)、GPU(torch+RTX 5080)、`ffmpeg`。
- 新增录音：把 m4a 丢进本目录，跑 `transcribe.py all`。
- **m4a 已 gitignore**：仓库只提交转写文本、digest 与脚本，音视频本地保留。
- ASR 小错（如"回长州"应为"回杭州"、"残战人士"应为"残障人士"）属正常，可在摘要/digest 阶段校对，不要回改转写原文。

### 校验要求
- 转写后抽查开头+中段+结尾，确认实体（人名/公司/项目）是否保留——这是判断质量的硬标准，不是看通顺度。
- 若出现大量 0 秒碎片段（`[00:12:43-00:12:43] 单字`），是 VAD 切太碎，调大 `min_silence_duration_ms`。
- 复原版转写 vs 原始直写的对比基准：见本文件 A/B 表，不要重复踩坑。

### 常见模式
- 长文件（4 小时）GPU 转写约 14 分钟（17.8x 实时）；8.8 小时音频共约 35 分钟。
- 大模型随机性：同一段多次转写会有细微差异，但实体应稳定。

## 依赖

### 内部
- 上游：手机录音 m4a（source of truth）。
- 下游：转写文本 → `raw/notes/video-transcripts/` → ingest/digest → `wiki/` 知识层。

### 外部
- `faster-whisper`(large-v3)、`torch`+CUDA、`ffmpeg`。

<!-- MANUAL: -->
