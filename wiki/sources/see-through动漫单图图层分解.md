---
tags: [素材, GitHub, 项目学习, 图层分解, 扩散模型, AI视觉, 2.5D]
created: 2026-06-14
updated: 2026-06-14
sources: [raw/repos/shitagaki-lab-see-through.md, https://github.com/shitagaki-lab/see-through, https://arxiv.org/abs/2602.03749]
---

# See-Through：动漫单图图层分解

> 输入一张静态动漫角色插画，自动分解成最多 23 个「完整补绘、语义独立、含绘制顺序」的图层并导出 PSD，得到可操作的 2.5D 模型；典型的「生成式视觉 + 分割 + 深度估计」组合管线。

## 来源

- 仓库：`shitagaki-lab/see-through`（Apache 2.0；Python ≈56% / Jupyter ≈43%）
- 论文：See-Through: Single-image Layer Decomposition for Anime Characters，arXiv:2602.03749
- 录用：有条件接收 ACM SIGGRAPH 2026（待核验）
- 机构：Saint Francis University / University of Pennsylvania / Spellbrush / Shitagaki Lab（待核验）
- 抓取日期：2026-06-14

## 项目定位与问题

动漫插画是「拍平」的单层图像：头发盖住脸、衣物盖住身体、配饰盖住头发，被遮挡部分根本没有像素。要让一张图变得可动（换表情、转头、做 Live2D / 2.5D），就必须把它拆回**语义独立、且把被遮挡区域补绘完整**的图层，并知道谁在谁前面。See-Through 把这件原本靠画师手工分层的工作自动化。

## 核心方法与架构

三类模型串成一条端到端管线，对应「分什么、补什么、谁在前」三个子问题：

- **SAM Body Parsing（分什么）**：用 SAM 系语义分割，把角色拆成身体部位/区域（头发、脸、眼、衣物、配饰等）。
- **LayerDiff 3D（补什么）**：基于 SDXL 的扩散式**透明图层生成**，对每个图层补绘出被遮挡、原图不存在的像素，输出带 alpha 的完整图层（[[扩散模型]] 在这里负责 inpainting + 透明通道生成）。
- **Marigold Depth（谁在前）**：为动漫微调的伪深度估计，提供绘制/堆叠顺序的依据；支持基于深度的分层，也支持左右分层。

最终把图层按推断顺序导出为 **PSD**，直接进 Photoshop / Live2D 等下游工具。这是 [[图层分解]] 的一个完整实现样本。

## 技术栈与关键组件

- 主管线脚本：`inference/scripts/inference_psd.py`
- 目录：`annotators/`（分割/标注）、`common/`、`inference/`、`training/`、`ui/`（数据集准备界面）
- 依赖分档：`requirements.txt` + `requirements-*.txt`（SAM2、mmdet、量化）
- 基座：SDXL（扩散）、SAM/SAM2（分割）、Marigold（深度）

## 可复用知识

- **「分割 + 扩散补绘 + 深度排序」是把 2D 图像结构化为可编辑图层的通用范式**，不限于动漫，可迁移到任何「单图 → 可操作分层」的任务，呼应 [[3D生成]] 与 [[游戏生产管线]] 里「美术资产可参数化」的诉求。
- **扩散模型不仅能生成 RGB，还能直接生成带 alpha 的透明图层**（LayerDiff），这是把生成模型嵌入生产管线的关键一步——产物是可用图层而非一张成品图。
- **显存工程同样是方法的一部分**：同一管线通过 group offload / NF4 量化 / block swap 适配 8–16GB 消费级显卡（见动手清单），说明「能不能落到消费级硬件」本身是研究价值的一部分。

## 动手清单（安装 / 运行 / 复现）

```bash
conda create -n see_through python=3.12
pip install torch==2.8.0+cu128 torchvision==0.23.0+cu128
pip install -r requirements.txt
python inference/scripts/inference_psd.py --srcp path/to/image --save_to_psd
```

- 分辨率 1280 下显存需求约 8–16GB。
- 12GB：用 group offload，峰值≈10GB。
- 8GB：用 NF4 量化管线（峰值≈8GB）或 block swap 管线（保持 bf16，峰值≈8GB）。
- 免动手试用：HuggingFace Demo（每日免费 1–2 次 PSD 提取）、ModelScope Demo（大陆可用）。
- 社区集成：ComfyUI-See-through、PachiPakuGen、StretchyStudio。

## 局限与适用边界

- 针对**动漫角色**优化（Marigold 为动漫微调、SAM 解析按角色部位），迁移到真实照片或非角色图像需重新评估。
- 补绘的被遮挡区域是模型「想象」出来的，不等于原画师意图，做严肃创作时需人工复核。
- 最多 23 层、绘制顺序为「推断」，复杂构图可能出错。

## 待核验事实

- SIGGRAPH 2026 录用状态（「有条件接收」）与论文 arXiv 编号 2602.03749。
- 作者所属机构清单。
- 「最多 23 层」「8–16GB / 1280」「12GB→10GB、8GB→NF4/block swap≈8GB」等数字。
- HuggingFace「每日免费 1–2 次」额度。

## 下游：能否做成游戏动态角色资产

see-through 只产出**静态分层 PSD**，本身不做动画；作者明确声明它 ≠ Image-to-Live2D。要「动起来」需接下游工具：StretchyStudio（免费网页，自动绑定 see-through 的 PSD 成 2D 木偶，约 30 秒手动微调关节）或 PachiPakuGen（生成眨眼/口型材料给 SpriTalk）。完整可行性与「零手动 / 游戏里好表现」的判断见 [[单图到游戏角色资产的自动化管线评估]]。

## 相关页面

- [[单图到游戏角色资产的自动化管线评估]]
- [[图层分解]]
- [[扩散模型]]
- [[AI视觉与生成式内容]]
- [[3D生成]]
- [[游戏生产管线]]
- [[AI游戏与虚拟世界]]
