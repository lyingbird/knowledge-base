# raw: shitagaki-lab/see-through

- 仓库：https://github.com/shitagaki-lab/see-through
- 论文：See-Through: Single-image Layer Decomposition for Anime Characters，arXiv:2602.03749
- 录用：有条件接收 ACM SIGGRAPH 2026 Conference Proceedings（待核验）
- 作者机构：Saint Francis University、University of Pennsylvania、Spellbrush、Shitagaki Lab（待核验）
- 许可证：Apache 2.0
- 语言：Python（约 56%）+ Jupyter Notebook（约 43%）
- 抓取日期：2026-06-14

## README 要点（摘抄）

把单张静态动漫角色插画自动分解成最多 23 个「完整补绘、语义独立、含推断绘制顺序」的图层（头发、脸、眼睛、衣物、配饰等），用于生成可操作的 2.5D 模型。

核心模型：
- LayerDiff 3D：基于 SDXL 的扩散式透明图层生成。
- Marigold Depth：为动漫微调的伪深度估计。
- SAM Body Parsing：语义身体部位分割。

管线特性：端到端图层分解 + PSD 导出；支持基于深度和左右分层；为低显存优化（1280 分辨率下 8–16GB）。

显存分档：
- 12GB：group offload，峰值降到约 10GB。
- 8GB：NF4 量化管线（峰值约 8GB）；或 block swap 管线，保持 bf16 精度、峰值约 8GB。

安装/使用：
```bash
conda create -n see_through python=3.12
pip install torch==2.8.0+cu128 torchvision==0.23.0+cu128
pip install -r requirements.txt
python inference/scripts/inference_psd.py --srcp path/to/image --save_to_psd
```

目录：annotators/、common/、inference/（主管线 inference_psd.py）、training/、ui/；requirements.txt 及分档 requirements-*.txt（SAM2、mmdet、量化）。

资源：HuggingFace Demo（每日免费 1–2 次 PSD 提取）、ModelScope Demo（中国大陆可用）、社区集成 ComfyUI-See-through、PachiPakuGen、StretchyStudio。
