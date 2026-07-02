# 游戏 + AI 开源项目（raw 副本）

抓取日期：2026-07-01｜来源：GitHub（联网核实，star 为抓取时量级约数）

---

## joonspk-research/generative_agents（斯坦福小镇）
- URL: https://github.com/joonspk-research/generative_agents
- 定位：斯坦福「生成式智能体」官方代码，在沙盒小镇 Smallville 用 LLM 驱动 25 个可信 NPC 行为。
- 方法：Python 3.9 + OpenAI GPT API；核心「记忆流 memory stream + 检索 + 反思 reflection + 规划 planning」认知架构；Django 环境/前端 + Tiled 地图。
- star：约 2.1w（21.7k）。许可 Apache 2.0。
- 论文：《Generative Agents: Interactive Simulacra of Human Behavior》(UIST '23)，Joon Sung Park、Percy Liang、Michael Bernstein 等（斯坦福+Google）。
- 动手：backend 填 OpenAI key → pip install -r requirements → frontend `manage.py runserver` → backend `reverie.py` 输入 `run <步数>` → 浏览器 simulator_home。

## linyiLYi/street-fighter-ai
- URL: https://github.com/linyiLYi/street-fighter-ai
- 定位：深度强化学习、仅凭 RGB 像素训练 AI 打通《街头霸王 II》最终 BOSS。
- 方法：Python 3.8 + PPO + Gym Retro + Stable-Baselines3；「惩罚衰减」缓解过度保守。
- star：约 6.5k。作者 B 站 UP 主「林亦LYi」，有中文讲解视频。
- 动手：Conda py3.8.10 → pip install → 拷配置进 gym-retro 游戏目录 → 合法 ROM 存 rom.md → `test.py`/`train.py`。
- 备注：已在库内 [[给NPC加AI真能让游戏更好玩吗（插眼GameWard）]] 提及（林亦 street-fighter-ai）。

## MineDojo/Voyager
- URL: https://github.com/MineDojo/Voyager
- 定位：首个 LLM 驱动的终身学习具身智能体，在《我的世界》自主探索、习得技能。
- 方法：GPT-4；三组件——自动课程 automatic curriculum、可执行代码技能库 skill library、结合环境反馈的迭代提示；JS(Mineflayer)+Python。
- star：约 7k。
- 论文：《Voyager: An Open-Ended Embodied Agent with LLMs》(arXiv:2305.16291, 2023)，Guanzhi Wang、Linxi Fan、Yuke Zhu、Anima Anandkumar 等（NVIDIA/Caltech）。
- 动手：pip install -e . → env/mineflayer 装 Node 依赖 → 搭 Minecraft + Fabric mods → 配 OpenAI key → `voyager.learn()`。

## amidos2006/gym-pcgrl（PCG 备选）
- URL: https://github.com/amidos2006/gym-pcgrl
- 定位：把「程序化关卡生成」建模为强化学习问题的 Gym 环境（PCGRL）。
- 方法：Python+Gym+Stable Baselines PPO2+TF1.15；narrow/wide/turtle 多种关卡表征，覆盖推箱子/塞尔达/马里奥等 6 类。
- star：约 130+（学术小众）。
- 论文：《PCGRL: Procedural Content Generation via RL》(AIIDE 2020)，Khalifa、Earle、Togelius 等（NYU Game Innovation Lab）。
