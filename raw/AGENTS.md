<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-07-09 | Updated: 2026-07-09 -->

# raw（原始素材层）

## 目的
Karpathy LLM Wiki 三层架构中的 **第一层：原始素材层（source of truth）**。这里保存视频转写、网页文章、公众号、推文、小红书、知乎、PDF、开源项目要点副本等不可变原始材料。`wiki/` 层的一切结论都要能回溯到这里。

## 关键文件
本目录不直接放文件，所有素材按媒介进入下面的子目录。

## 子目录

| 目录 | 用途 | 状态 |
|------|------|------|
| `notes/` | 手写笔记、转写、外部 Markdown（含 `video-notes/`、`video-transcripts/`，见 `notes/AGENTS.md`） | 有内容 |
| `articles/` | 网页文章原始副本（见 `articles/AGENTS.md`） | 有内容 |
| `repos/` | GitHub/开源项目要点副本（README、关键说明、要点摘抄；代码不入库，见 `repos/AGENTS.md`） | 有内容 |
| `pdfs/` | PDF 文件 | 当前为空（schema 预留桶） |
| `tweets/` | X/Twitter 内容 | 当前为空（schema 预留桶） |
| `wechat/` | 微信公众号文章 | 当前为空（schema 预留桶） |
| `xiaohongshu/` | 小红书内容 | 当前为空（schema 预留桶） |
| `zhihu/` | 知乎内容 | 当前为空（schema 预留桶） |
| `assets/` | 图片等附件 | 当前为空（schema 预留桶） |

## 给 AI Agent

### 在此目录工作
- **默认只读**：原始素材是事实来源，LLM 可以读取但默认不修改。需要纠错时，优先在 `03-核验/待核验事实.md` 和对应 `wiki/sources/` 页里记录，而不是改写原始素材。
- **新素材按媒介入对应子目录**，不要直接丢在根目录或 `raw/` 顶层。微信文章进 `wechat/`，推文进 `tweets/`，以此类推。
- 历史视频笔记的不可变副本在 `notes/video-notes/`；完整转写在 `notes/video-transcripts/`。
- 顶部应标注抓取日期、来源 URL 和「不可作为已核验结论」性质声明（参考 `articles/` 现有文件的头部格式）。

### 校验要求
- 原始素材是否被 `wiki/sources/` 摘要覆盖。
- 高风险事实（数字、融资、论文结论）是否已分流到 `03-核验/待核验事实.md`，而不是停在原始素材里当定论。

### 常见模式
- 每份原始素材对应（或应该对应）一页 `wiki/sources/` 摘要。
- `intel-gather` 类采集件在 `notes/` 下，是多 agent 并行汇总的情报副本，引用时注明归因边界。

## 依赖

### 内部
- 上游被 `wiki/sources/` 摘要引用，是知识网络的根。
- `02-视频笔记/` 的内容已复制到 `notes/video-notes/` 作为副本。

### 外部
- 无（纯 Markdown / 文本素材）。

<!-- MANUAL: -->
