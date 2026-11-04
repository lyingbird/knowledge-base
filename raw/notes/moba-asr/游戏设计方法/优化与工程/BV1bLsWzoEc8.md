---
title: "原声|GMTK|游戏如何实现破坏——How Games Do Destruction"
platform: bilibili
bvid: BV1bLsWzoEc8
author: 庸才的朽木
author_uid: 49665055
pubdate: 2025-10-24 22:18:12
duration_sec: 1148
view: 750
like: 40
coin: 7
favorite: 65
reply: 5
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV1bLsWzoEc8
subtitle_source: asr_Qwen3-ASR-1.7B
asr_model: Qwen3-ASR-1.7B
asr_elapsed_sec: 372.4
transcript_chars: 15425
crawl_time: 2026-05-26 11:25:40
---

# 原声|GMTK|游戏如何实现破坏——How Games Do Destruction

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2025-10-24 22:18:12
- **时长**: 19分8秒
- **播放**: 750 | 赞: 40 | 币: 7 | 藏: 65
- **链接**: https://www.bilibili.com/video/BV1bLsWzoEc8

## 视频描述

原视频：https://www.youtube.com/watch?v=JZ9GRFD-mSc
2025年10月3日
让我们来谈谈视频游戏中的破坏，并分析用于损坏汽车、打破箱子、穿越场景和炸毁建筑的技巧。

=== 展示的游戏 ===
火爆狂飙：天堂 重制版 | Burnout Paradise Remastered|2018
马克思・佩恩 3|Max Payne 3|2012
大金刚狂欢节 | Donkey Kong Bananza|2025
孤岛惊魂 2|Far Cry 2|2008
毁灭工具 | Instruments of Destruction|2024
汤姆・克兰西：彩虹六号 围攻 | Tom Clancy’s Rainbow Six Siege|2015
神秘海域：盗贼遗产合集 | Uncharted: Legacy of Thieves Collection|2022
使命召唤：黑色行动 6|Call of Duty: Black Ops 6|2024
红色派系：游击战 | Red Faction: Guerilla|2009
终极淘汰赛 | The Finals|2023
正当防卫 3|Just Cause 3|2015
战地风云 1|Battlefield 1|2016
魔法洞穴 2|Noita|2020
控制 | Control|2019
BeamNG 赛车 | BeamNG.drive|2015
战地风云：叛逆连队 2|Battlefield: Bad Company 2|2010
战地风云 4|Battlefield 4|2013
枪神 | Stranglehold|2007
半条命 2|Half-Life 2|2004
硬核空间：拆船模拟器 | Hardspace: Shipbreaker|2022
红色派系 | Red Faction|2001
粘粘世界 2|World of Goo 2|2024
果冻车世界 | Jelly Car Worlds|2022
撞车嘉年华 2|Wreckfest 2|2025
拆迁 | Teardown|2022
洞穴探险 | Spelunky|2012
我的世界 | Minecraft|2011
异星探险家 | Astroneer|2019
七日杀 | 7 Days to Die|2024
一款关于挖洞的游戏 | A Game About Digging a Hole|2025

## 完整文稿

> 来源: asr_Qwen3-ASR-1.7B

Hey, I'm Mark. Let's talk about destruction. Let's talk about smashing cars and leveling buildings. Let's talk about terrain deformation and fire propagation. Let's talk about games where things bend and break and blow. But I'm not talking about fancy pre-canection that play as part of a cutscene or a scripted moment. I'm not talking about buildings that fall down in the exact same way every single time. I'm talking about doing destruction in real time, in response to player actions, as part of the gameplay. That's a whole other thing. That's really hard, and it's hard because you're dealing with unpredictable physics and partials and bits of debris. And if you're not careful, you'll tank the frame rate. And so that's what I find so interesting about this: doing dynamic destruction games is about being clever. It's about using cost-cutting algorithms and out-of-magic tricks to blow the world without blowing your memory budget. So in this video, I want to look at six games that have destruction in wildly different ways and reveal the techniques that they use to make the world fall apart. I'm Mark Brown. This is game makers talking, and here's how games do destruction. Okay, let's start with control. This is a game where the environment just falls to pieces as you play. Your bullets rip through tables and chairs, and you can use just telekinetic powers to rip chunks of concrete out of the wall. Now, this is perhaps the most common kind of destruction in games. Almost every shooter is filled with props and objects that can be broken apart, and they all use basically the same technique: use two versions of the object in memory and attack one and break one, and then when the object is attacked, you replace A with B. It's simple, but it totally works. And control uses the same idea. It just takes a lot further. For one, objects made up of loads of individual pieces can all be destroyed independently. That means objects can break almost the exact point way you attack them, and because those broken pieces are distinct physics objects that are connected with joints, well, if you break a table in half, then the table will fall into two parts and collapse in a realistic way. The game will also play a hard effect when the object breaks to cover up the transition. Props are tagged with material like metal, concrete, and wood, and will then play a specific effect on impact. And finally, decals are used to release all the impact. Decals are basically stickers that you can slap on the environment like bullets, holes, and crates. And control has a really good one: the tricky technique that you just made actual damage in the wall. Put all of this together, and you get an environment that is technically crumbling around you in a truly satisfying way. Next, let's talk about ashtray. So I just said that the way to destruction is to secretly prepare a broken version of whatever object you want to destroy, but it turns out that you don't have to fake the fracture. So in ashtray, there are these logs that you can cut with your laser to see to make smaller logs, and they seem to cut exactly where you damage them. What's going on there? Does the game just have thousands of possible variants of this log tucked away in memory ready to blow? Turns out no. The game actually projects a flat 2D plane under ashtray, and it's a very 3D model. And the place where you cut it, it then adds new edges and surfaces, creates new collision shapes, and then splits two models to represent the logs all in a single frame. This is also how Rainbow Six lets you shoot walls. It slices the model in real time. It's the tech behind hard space ship break. A game where you use a big-ass cutting laser to slice bits of space, and it was even being used in reflection back on the PlayStation 2 to dynamically cut spheres out of the walls. Now this turns out to be expensive on the hardware, so it comes with limitations. It only works on simple shapes, and the games will typically hide the broken pieces after some time to avoid clogging up your memory. But still, in certain circumstances, you can do the destruction in real time instead of preparing it in advance. Next up, BMG. Okay, so physics objects in games typically use simple rigid body physics, which means they always retain exact rigid shape. But other games use soft body physics to create more malleable and fancy. It's the technology behind switch games like World of Gu and Jakal Worlds, and this idea can be scaled up to create a realistic vehicle as seen in BMG driving, which can lead to extremely detailed and realistic deformation. Here's how it works. Every car in BMG is made up of a bunch of nodes just floating points in space, and then they're held together with beams, which act like stiff springs that try not to stretch. So when one of those nodes is moved by a collision, it will cause all of the connected beams which pull in all of their nodes creating realistic crumpled effect. And so, when most racing games just use shaders and textures to represent damage in a purely visual way, soft body games like BMG and RFS can literally squish and squash the model of the car to fundamentally change how the object moves and interacts with the environment. Now there's much more to BMG like aerodynamics, fuel consumption, and so on, but most people just use it to recreate one scene from fire destruction. Okay, let's go to Far Cry 2. This game is famous for fire propagation systems. In this game, a multitude of objects set fire to a patch of grass, and it will spread into raging inferno that will engulf nearby trees and buildings. How was that work? Well, basically, the game world is represented by an invisible grid that stretches over the floor, and each cell has a certain number of hit points. If the cell is flammable and loses all of its points, say when you shoot a rocket at it, it will set on fire. Then a burning cell will start to damage its neighboring cells, and when there is a breach, the cells set on fire too, creating a chain reaction where the fire spreads from zone to zone. There are other bits of new stuff to this system. Each cell has a firelight time, so it will eventually stop. Different environments will have more or fewer hit points to represent say a dry patch of grass versus a wet jungle. The more hit points it has, the harder it is to set alight, and burning cells will deal more damage to neighbors that are in the direction of the wind to capture the effect of a fire being curled by stronger gusts. It's a deceptively simple system, but creates a really strong effect. Next up, tear. But first, let's start by looking at two games. So in games like Splunky, we can see that the world is divided into grid of tiles. Then we can create simple destructions by removing those tiles to create tunnels, pathways, and shoots. The devs can just swap out the sprites of the neighboring tiles to hide the wreckage. And if you want more depth in your destruction, you can just reduce the size of the grid. You can go all the way down to destroying individual pixels, as seen in Noita. In this game, every single pixel can be removed in order to break walls and floors with practically infinite granularity. And so, if we take that grid of tiles and extend it into an extra dimension, we get, well, Minecraft. Minecraft is built out of cubes called voxels, which can be independently added and subtracted from the world to allow for completely freeform destruction. And in fact, a lot of games use this voxel approach for destruction including No Man's Sky and Days of Dying, Ashtray, and the Terrain Smashing Donkey Kong. But where every layer is made up of hundreds of cubes that pack together, most of these games use some kind of smoothing technique or algorithm to avoid that superbloody Minecraft style in favor of something more naturalistic. Check out this video on matching cubes for more info if you're feeling technical. And then, just like we went from Splunky to Noita by reducing the size of the blocks, we can do the same in 3D to get a game like Tear. Tear is basically Minecraft, but with way higher resolution. Where Minecraft represents a piece of furniture as a single cube, Tear represents it as hundreds or thousands of tiny blocks all of which allow for much more precise destruction. Though the difference with the voxel-based games is that Tear has physics that are floating platforms. Basically, the game makes objects from a cluster of voxels, but if some of those voxels get loose from the cluster, they instantly turn into new rigid body physics objects separate from the original. This means it can fall down into other objects and roll around. And then finally, it's the reigning champion of video game destruction: reflection. This is a game where almost every structure on the Martian surface can be brought down with explosives or just a big swing of your trusty hammer. This is a game where buildings react realistically when you remove foundations and even fall down and crush other structures in the process. Now there are other games where you can destroy buildings. We just saw it in Tear. There are small structures in the just-for-games that you can topple, and there's my favorite battle for bad company too. In this game, buildings are made out of a large number of prefabricated pieces, each with two versions and attacked one and destroyed one. And when you do enough damage, well, you know the trick: swap the pieces out for its destroyed variant. So that's all about all of these game struggles with fundamental question: when does the building fall down? Because Tear does it when an object is completely detached from the ground, but that means massive buildings can be held up by single strands of voxels. And bad company does it after a certain number of those prefab pieces are destroyed, which points to play a pre-canection destruction that feels kind of arbitrary. Ideally, we want to perform some kind of structural analysis to see if the building should stand in or whether it should fall, and that is exactly what reflection does with this system. The level of variation caused stress. Here's how it works. So a building in reflection is made up of hundreds of individual parts that you can destroy. Let's think of them like bricks, and then each brick has two stats: its force, which forces it to shake. Let's just think of it as how heavy that part is, and its strength, how much mass it can hold up. We can then group all of the bricks into individual layers for a simple building that will be a bunch of horizontal tiers like a big stack of pancakes, but can be more complicated for horizontal structures like bridges and overhangs. Then we can tally up the stats on those bricks to get each layer combined and strength. Keep in mind the weight must also include everything above it. And now we can do stress calculation by simply asking is the strength of one layer greater than the weight of all layers above it? Now a building is designed by vision to be architecturally sound and hold up its own weight with different values for different materials. So each joint supporting concrete pillars is much higher strength value than the panels. But as we start destroying bricks, we're reducing the strength of that layer, and we can keep going until the strength is now less than the force of everything above it, which means the layer will fail, and everything above it will turn into a bunch of physics objects that can come crashing down. In fact, if you go frame by frame, you can see the exact moment where the upper layers change from static stuff to floppy physics bits, and because those physics objects can inflict damage themselves, we can get a situation where the top layer of the building will fall down and crush the layers beneath it, or even fall to the side and make a big hole in the building next to it. Super satisfying. Now there are plenty of limitations to this system. The game takes a while to actually do the stress calculation with just buildings, sometimes taking a while to fall down. But still, this technique allows for unimaginable levels of destruction. Every building can be busted, blown up, bifurcated, and turned into bits over the course of match. The game world will crumble to pieces in reaction to rockets, mines, and explosive barrels, and even possible level-terrain plays. And the thing is, the system is basically identical to reflection. The developers were directly inspired by reflection's work, and so they made a very similar setup. The buildings are made up of hundreds of fractured parts. The game calculates stress in real time, and if layers force exceed its strength, then the whole thing comes down. Except it's now running on Unreal Engine 5 with NVIDIA FX and mins packs for 20 times more memory than you find on Xbox 360. So those are some of the most effective techniques used for adding destruction to games, swapping props, splitting the world into breakable cubes, and performing quick stress tests on buildings. All of which can make for impressive iterations of real-world destruction. And now you know the tricks. You might be wondering why we don't see this level of deformation in every game we play. And I think it's because well, each one of these techniques has some big knock-on effects for the rest of the game. Not just for performance and memory, but also stuff like art and lighting and sound and AI pathfinding. All of which must be able to adapt to world constantly changing and moving. And then on top of all of that, the game design tear designers the idea of a fully destructible environment is compelling for the player, but not for the game design. And no one can make another says it's easy to think that having a complex or highly realistic simulation will automatically result in interesting gameplay. Often that's not the case, and that's because well, game design is usually about settings and restrictions about rules and constraints and destruction can throw all of that out of the window. Donkey Kong Direct has yet to take a hashie says in most games level design is a bit like designing a course. You've got a menu you want players to follow, and you build paths to guide them along it. But in this game, even those paths can be destroyed if instead they get torn and split into gravel and jammed from behind. That's incredible. This level's with that kind of flexibility in mind was huge change. So it's like absolutely anything else that can be added to a game. It must be done for a reason. Perhaps it's for new combat gameplay, like denying enemy cover, creating new kinds of sight or collapsing structures on enemies. Maybe it's that players be crafty by making tunnels, traps, or slides. Perhaps it's for creativity or immersion, or replayability, or the sense of simulation. Whatever the case, and however you implement it, destruction should be there to support your game design goals, not blow them to bits. I'm Mark Brown. Thanks for watching. Hey, so obviously gloss over a lot of the nuances and technical implementation of this stuff. After all, according to recent YouTube most of my audience never made a video game. But if you do want to learn more, then as always with GTA videos, please check the description where you will find dozens of links to videos, talks, and slides with way more detail. Thanks. I'm seeing the next one.

## 热门评论

- **庸才的朽木** (赞4): === 章节列表 ===
00:00 - 简介
01:29 - 控制
03:17 - 天体机器人
04:52 - BeamNG.drive
06:31 - 狂野飙车 2
07:55 - 拆卸
10:23 - 红色警戒：游击战
15:49 - 结论
- **火燎菊** (赞1): 大宝加油