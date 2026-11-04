---
tags: [实体, 游戏设计, 学院派, USC, playcentric, Fullerton]
created: 2026-11-02
updated: 2026-11-02
sources: ["Tracy Fullerton, Game Design Workshop: A Playcentric Approach to Creating Innovative Games, CRC Press, 1st ed. 2004 / 5th ed. 2024", "Fullerton, The Art of Play: Player Centric Design and the Process of Innovation, 2005"]
---

# USC游戏设计方法

> 南加大电影艺术学院的路子是「以玩家体验为目标、靠原型与试玩迭代逼近」。它把 HCI 的用户中心设计搬进游戏，主张设计师是「玩家的代言人」。

## 代表人物与文本

Tracy Fullerton，USC 电影艺术学院互动媒体与游戏系教授、USC Games 项目荣休主任、USC Game Innovation Lab 主任、EA 互动娱乐讲席教授。她的 *Game Design Workshop* 第一版 2004 年由 CRC Press 出版，第五版 2024 年，是全球采用最广的游戏设计教材之一。中文版《游戏设计梦工厂》。

实验室产出的作品包括 Cloud、flOw、Darfur is Dying、The Night Journey（与录像艺术家 Bill Viola 合作）、Walden, a game。

## 核心方法：playcentric design

Fullerton 自己给出的定义是「在设计过程中从构想到完成都让玩家参与进来」。落到操作上是六步循环：

1. 设定玩家体验目标（player experience goals）。
2. 构想一个想法或系统。
3. 做原型（纸面、实体或数字）。
4. 拿给真实玩家试玩。
5. 拿结果对照体验目标评估。
6. 排序问题、改原型、再测，直到达标。

这个循环的关键不在「迭代」这个动作，而在第 1 步和第 5 步的配对：没有体验目标，迭代就没有判据；没有试玩，体验目标就只是设计者的自我投射。

Fullerton 对设计师角色的说法是「玩家的代言人」（advocate for the player）——在团队里替玩家说话，而不是替美术、程序或发行说话。

## 三层元素

教材把游戏拆成三组元素，这是它最常被引用的结构：

| 层 | 英文 | 内容 | 性质 |
| --- | --- | --- | --- |
| 形式元素 | Formal elements | 玩家、目标、流程、规则、资源、冲突、边界、结果 | 静态，构成游戏的骨架 |
| 戏剧元素 | Dramatic elements | 挑战、玩、前提、角色、故事、世界观、戏剧弧 | 静态，提供意义与情感 |
| 动态元素 | Dynamic elements | 系统、涌现、反馈循环 | 运行后才出现 |

注意与 [[MDA框架]] 的术语错位：Fullerton 的 dynamic 指「系统动态」这个类别，MDA 的 dynamics 指「机制在玩家输入下产生的行为」。两者都叫 dynamic，指的不是同一件事。

## 她对「游戏」的定义

「一个封闭的形式系统，让玩家参与结构化的冲突，并以不等的结果化解其不确定性。」（"A closed, formal system that engages players in structured conflict and resolves its uncertainty in an unequal outcome."）

但她同时明确声明：这不提供游戏的终极定义，只是为设计实践准备的起点。这个姿态与 [[游戏定义]] 页里 Juul、Salen & Zimmerman 的处理方式一致——给可用定义，不给本质定义。

## 方法的来源

不是从游戏业内部长出来的。Fullerton 在 1995 年为微软 MSN 做休闲网游时，被指派了一位可用性专家 Kevin Keeker。她原本抗拒，结果第一轮用户测试就把她对设计的自信打碎：界面、规则清晰度、平衡、前提，全部出问题。她事后把这称为转折点——从此把用户测试当成设计流程的一部分，并把纸面原型提前到流程最前端。

所以 USC 方法论的祖先是 HCI 的用户中心设计（user-centered design），不是电影叙事学。这也解释了它在「可玩性」「可学习性」上的偏重。

## 与另外两所的分野

见 [[游戏设计流派与争论]]。简要对比：

- 对 [[CMU娱乐技术中心]]：USC 关注体验目标与试玩判据，CMU 关注跨专业团队把东西做出来。
- 对 [[NYU游戏中心]]：USC 服务商业与影视工业，NYU 服务独立与批评。

USC 的方法最像「工程化的设计流程」，这也是它被大量非 USC 团队采用的原因——它不依赖特定院校资源就能执行。

## 具体案例

### flOw：一张论文与一个可玩证明

Jenova Chen 在 USC 互动媒体部（IMD）的 MFA 论文题为《Flow in Games (and Everything Else)》，主张游戏应当适配每个玩家各自的心理状态，并提出了主动式动态难度调整（active DDA）：让玩家通过游戏内的选择自己调难度，而不是由系统暗中调整。

flOw 是这篇论文的可玩证明。它在 2006 年作为免费 Flash 游戏发布，两周内下载十万次，到七月累计下载超过六十五万次。PS3 版 2007 年 2 月上线，成为当年 PlayStation Network 下载量最高的游戏，并拿到游戏开发者选择奖的最佳下载游戏。

这个案例之所以值得写进方法页，是因为它展示了 playcentric design 的完整闭环：先有对玩家体验的假设，做成可玩的东西，让真实玩家用行为投票，再拿数据回来修假设。论文本身不构成成果，可玩证明才是。

flOw 的一个具体设计也常被引用：它没有死亡。生物输掉一场战斗不会被杀死，只会向上漂一层、掉掉体节、继续进食。取消失败状态，等于取消了通常把玩家弹出心流的那个焦虑峰值。这是把"体验优先"落到机制层的实例。

### Cloud：一次学生项目的意外外溢

Cloud 是 Chen 与 Kellee Santiago 等七名 USC 学生在 Tracy Fullerton 指导下做的团队项目，2005 年发布，讲一个住院的小男孩幻想飞出病房窗户、在天空用云朵造型。它拿下 GDC 学生展示奖，也拿到 Slamdance 与 IGF 的奖项。

Sony 的 John Hight 在学生展示上看到它，向市场部门解释这个游戏时被问"这是什么类型"，他回答"是禅"。这段对话后来被反复引用，因为它说明了一件事：当作品不属于既有类型时，分类本身会成为发行障碍。

Cloud 的成功直接催生了 thatgamecompany 与 Sony 的三款游戏合约。这条路径是 USC 方法最典型的产物：课程 -> 团队项目 -> 展示 -> 被产业接走。

### Flower：从"情感庇护所"倒推设计

Chen 说 Flower 的目标是唤起正面情绪，做一个"情感庇护所"，并把游戏描述为"一首探索城市与自然张力的互动诗"。他早期的想法很具体：每台 PlayStation 都是客厅里的一扇门，它把你带到别处，如果那是一扇让你被自然拥抱的门，会不会很好。

这个案例说明 playcentric design 里的"玩家体验目标"可以先于机制存在，而且可以是一句意象而不是一条需求。它的风险也在这里：意象无法直接验收，只能靠原型反复比对。

Flower 后来被史密森尼美国艺术博物馆的 "The Art of Video Games" 展览收录，这是游戏作为艺术形式被机构承认的一个具体节点。

### Nevermind：把生物反馈做成难度参数

Erin Reynolds（USC '06, MFA '12）的 thesis 项目 Nevermind 用生物反馈监测玩家的压力水平：玩家越焦虑，游戏的谜题越难。

这个设计在方法上是 playcentric design 的极端版本：玩家的内部状态直接成为系统输入。它同时暴露了这类设计的一个现实约束，即生物反馈信号的噪声很大，所以"越焦虑越难"必须做成可感知的、宽容的映射，否则玩家会认为系统在随机惩罚自己。

### Outer Wilds：把一个 thesis 做成商业作品

Alex Beachum（MFA '13）的 thesis 项目是 Outer Wilds，2019 年 5 月在 Xbox One 上线。玩家在一个反复重置的时间循环里解开一个太阳系的谜。

它常被当作环境叙事与知识驱动的进度的最佳案例：玩家的进度不是数值，而是"我知道了什么"。这一点与 USC 方法里"体验优先"的取向一致，也是 thesis 项目能够长成商业作品的原因：核心体验在设计之初就已经被定义清楚，剩下的工作是把它做扎实。

### The Misadventures of P.B. Winterbottom：形式先于叙事

Matthew Korba（MFA '08）的 thesis 项目，用时间操控去抢馅饼，视觉与叙事风格来自默片。2010 年由 2K Play 在 Xbox LIVE Arcade 发行。

默片风格在这里不是装饰，它是机制的解释框架：时间倒回、复制、快进这些操作在默片的物理喜剧语汇里是自洽的。这是"三层元素"里美学与机制同源的一个干净例子。

### Octobo：把屏幕装进玩偶

Yuting Su（MFA '16）的 thesis 概念是一个可拥抱的蓝色章鱼玩偶，身上有一个槽位可以插入平板，让平板成为它的眼睛和嘴。它面向幼儿，目标是训练专注力与精细动作。

这个案例的意义在于它把"游戏"的边界推到了实体玩具：屏幕不是主体，而是玩偶的一个器官。这也是 USC 与产业接口最宽的一面，它不假设交付物一定是软件。

### 一个可以照抄的流程特征

USC Games 是电影艺术学院与 Viterbi 工程学院的联合项目，MFA 每年只招约十五人。每年年末的 USC Games Expo 会展出 capstone 与 MFA thesis 项目，2026 年那一届展出了七十多个游戏。

把这几条放在一起看，方法论的特征就清楚了：小规模、跨学院、以 thesis 为强制交付、以公开 Expo 为验收。这套结构逼着学生在毕业前完成一次"从假设到可玩到公开展示"的完整循环，而不是只写文档。

## 相关页面

- [[游戏设计流派与争论]]
- [[MDA框架]]
- [[设计镜头]]
- [[玩家反馈闭环]]
- [[CMU娱乐技术中心]]
- [[NYU游戏中心]]
- [[游戏设计理论谱系]]
