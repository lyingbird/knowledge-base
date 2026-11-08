---
title: "AI&G Conference|在《天国:拯救2》中支持数千个模拟NPC｜2025人工智能与游戏大会——Supporting Thousands of Si"
platform: bilibili
bvid: BV1h8hq6KEyt
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-09-22 00:13:14
duration_sec: 4645
view: 988
like: 22
coin: 4
favorite: 28
reply: 3
danmaku: 0
share: 3
url: https://www.bilibili.com/video/BV1h8hq6KEyt
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 46258
crawl_time: 2026-11-08 21:20:03


# AI&G Conference|在《天国:拯救2》中支持数千个模拟NPC｜2025人工智能与游戏大会——Supporting Thousands of Si

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-09-22 00:13:14
- **时长**: 1小时17分25秒
- **播放**: 988 | 赞: 22 | 币: 4 | 藏: 28
- **链接**: https://www.bilibili.com/video/BV1h8hq6KEyt

## 视频描述

原视频：https://www.youtube.com/watch?v=yMlTT-yqdmc
原标题：Supporting Thousands of Simulated NPCs in Kingdom Come Deliverance 2 | AI and Games Conference 2025
（2026年6月19日）在《天国：拯救 2》开放世界中支撑数千个模拟 NPC
演讲人：彼得・斯姆

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1h8hq6KEyt
# 语言=en 时长=00:37:41 模型=large-v3

[00:00:15-00:00:21] Okay, hello! As already said, I'm Petr Smircek, I came from Warhorse Studios from Czech Republic
[00:00:21-00:00:26] and today I will tell you something about maybe the slightly crazy amount of people we are trying
[00:00:26-00:00:32] to simulate in our games. This talk will actually be at least a little bit about both of the games
[00:00:32-00:00:36] because some of the techniques we are using in the Kingdom Come Deliverance 2 were developed
[00:00:36-00:00:41] already for the first game. If you somehow made it to this talk and you don't know what these games
[00:00:41-00:00:48] are, don't worry, I will get you covered. Those are open world RPGs and they are maybe a little
[00:00:48-00:00:54] bit unusual by having no fantasy elements in them. They are trying to be as historically accurate as
[00:00:54-00:01:03] the central medieval Bohemia was. Also interesting property is it's kind of a medieval sandbox like a
[00:01:03-00:01:10] medieval GTA. There's a big main story but you can also roam the world and mess with NPCs the way you
[00:01:10-00:01:10] want.
[00:01:11-00:01:17] They are both running on CryEngine although we heavily modified it and it took us some time.
[00:01:17-00:01:25] We actually worked for like seven years on each of the games. The original KCD came in 2018 and the
[00:01:25-00:01:30] second one just earlier this year. First, just to see the scope of our game,
[00:01:32-00:01:40] we have two maps that are approximately 16 square kilometers and on the one that has more people
[00:01:40-00:01:41] there is 24.
[00:01:41-00:01:46] There are about 400 NPCs and 1500 of that is concentrated into a single big city.
[00:01:47-00:01:51] Those NPCs aren't just standing there. They are all simulated. They have complex behaviors
[00:01:52-00:02:00] and if you would be making this game like several years earlier or decades you would probably try to
[00:02:00-00:02:04] despawn the NPCs that are far away and simulate just the ones that are close to you. But that's
[00:02:04-00:02:09] not what we do. We're actually trying to make the game as immersive as possible so we are simulating
[00:02:10-00:02:11] all of them all the time.
[00:02:11-00:02:17] And that has a really high cost and that's what i am going to try to show you how we tackle that.
[00:02:18-00:02:24] So the content of this talk will be first the reasons why we are actually doing this,
[00:02:24-00:02:27] the reasons why we are simulating the whole world. Then I will want to
[00:02:28-00:02:34] show you maybe a naive solution we did for the first game when we weren't as experienced. Then
[00:02:34-00:02:39] I will go to the more mature solution for the Kingdom Come Deliverance 2 that we are using
[00:02:39-00:02:40] right now.
[00:02:41-00:02:41] Um.
[00:02:41-00:02:46] Also special cases for the city, which has a very high density of population.
[00:02:46-00:02:54] And finally, when we already had this tech to simulate a lot of people, we could use it to some other parts of the games as well.
[00:02:55-00:02:57] So, the immersion. First part.
[00:02:58-00:03:07] We are trying to achieve with these games an illusion of player being really there in person, living his medieval life.
[00:03:08-00:03:10] And what are we using for that?
[00:03:10-00:03:14] First is the realism. The games are trying to be as realistic as possible.
[00:03:14-00:03:19] So the people there are actually wearing the correct clothes they should have been wearing during that time.
[00:03:19-00:03:22] They are doing the correct things using the correct items.
[00:03:22-00:03:25] Even most of the vegetables are the same.
[00:03:25-00:03:27] And you as a player have chores.
[00:03:27-00:03:34] You have to sleep, you have to eat, you have to basically plan your day as we all do when we get up in the morning.
[00:03:34-00:03:36] We also have quite deep systems.
[00:03:36-00:03:39] So, for example, the NPCs are carrying items or clothes.
[00:03:39-00:03:40] We are putting them on the table.
[00:03:40-00:03:42] We are putting them in the chest before they go to bed.
[00:03:42-00:03:43] You can loot it.
[00:03:43-00:03:44] Then they don't have it.
[00:03:44-00:03:45] They have to deal with that.
[00:03:45-00:03:47] They will probably be naked or spare clothes.
[00:03:47-00:03:52] And the behaviors are also very complicated.
[00:03:52-00:03:54] Those NPCs have basically their lives.
[00:03:54-00:03:57] They have a house they live, a bed they sleep in.
[00:03:57-00:04:00] They get up in the morning, have a breakfast, then they go to work.
[00:04:00-00:04:04] In the evening they might want to go to the pub to have some fun.
[00:04:05-00:04:09] And you can interact with all of that doing small crimes.
[00:04:09-00:04:12] But very, I would say, nitpicky.
[00:04:12-00:04:21] You can even stand in front of the door of some NPC for too long and he will get suspicious of you and ask what you want.
[00:04:21-00:04:23] So, we are simulating the whole world.
[00:04:23-00:04:26] And what are the main advantages of doing that?
[00:04:26-00:04:30] First, the NPCs are actually correctly positioned at all times.
[00:04:30-00:04:38] Because we have those complicated behaviors, the NPCs might not be at the same position during the whole day.
[00:04:38-00:04:44] So, they might be living somewhere and they might go to work to a field which is quite far away.
[00:04:44-00:04:46] So, you can follow them and they will do all the correct things.
[00:04:46-00:04:51] You can even be at the field and they will arrive at the correct time and interact with you, maybe.
[00:04:52-00:04:55] Also, there are consequences that affect the world.
[00:04:55-00:05:01] If you, for example, do some crime, run away, you won't get away with that.
[00:05:01-00:05:06] The guards will simulate everything if you were there.
[00:05:08-00:05:11] If you, for example, kill an innkeeper, the NPCs won't be going to that pub.
[00:05:11-00:05:12] It won't be open.
[00:05:12-00:05:14] So, they will do some different behaviors.
[00:05:14-00:05:16] Even if you are far away.
[00:05:16-00:05:20] And the player is actually not necessary for this world to work.
[00:05:20-00:05:24] And the big advantage is that it can be also scripted this way.
[00:05:24-00:05:29] So, the scripting logic, the quest logic can count on everything being there at all times.
[00:05:29-00:05:36] Doing all the triggers at the correct times and sending all the NPCs where it's necessary.
[00:05:36-00:05:37] Of course.
[00:05:37-00:05:40] It sounds really good, but it's really heavy with performance.
[00:05:40-00:05:44] And that's why we are doing some level of detail of the AI simulation.
[00:05:45-00:05:47] So, the first game.
[00:05:48-00:05:51] And some of the things we did for the first game.
[00:05:52-00:05:56] At the very beginning, when we started to develop Kingdom Come Deliverance,
[00:05:56-00:05:59] we had the idea that the world should be deeply simulated, right?
[00:05:59-00:06:04] Everything should be as in real life and not as in the games.
[00:06:04-00:06:08] And every good developer knows the first rule of optimization.
[00:06:08-00:06:10] First make all the features.
[00:06:10-00:06:11] Then profile.
[00:06:11-00:06:12] Then optimize.
[00:06:12-00:06:13] So, we did that, right?
[00:06:13-00:06:16] We created one big level without any loading screens.
[00:06:16-00:06:18] Because we didn't want loading screens.
[00:06:18-00:06:20] We created all the behaviors, all the NPCs.
[00:06:20-00:06:24] And then we tried to turn on the console and it immediately crashed on memory, right?
[00:06:24-00:06:31] So, when we fixed it a little bit so it could run at least, not crash immediately, it ran to FPS.
[00:06:31-00:06:33] So, we had to do something.
[00:06:33-00:06:34] We had to do something.
[00:06:34-00:06:41] And the big issue was that we already had a lot of system done.
[00:06:41-00:06:42] So, we had to do something on the fly.
[00:06:42-00:06:44] We couldn't remade all of that.
[00:06:45-00:06:49] Before I show you what we did to solve that,
[00:06:49-00:06:54] I have to at least briefly introduce you to the core of our technology.
[00:06:54-00:06:56] The modular behavior trees.
[00:06:56-00:06:59] We have actually a custom implementation of modular behavior trees.
[00:06:59-00:07:00] What is it?
[00:07:00-00:07:03] It's basically a visualization.
[00:07:03-00:07:05] It's a visual scripting language.
[00:07:05-00:07:07] And our version is very low level.
[00:07:07-00:07:11] So, normally you have those nodes that you connect together.
[00:07:11-00:07:13] They are like line of instructions.
[00:07:13-00:07:14] Some of the nodes do something.
[00:07:14-00:07:16] Some of the nodes are just for branching.
[00:07:16-00:07:20] And we have even like loops, conditions, expressions.
[00:07:20-00:07:22] We even have a switch statement there.
[00:07:22-00:07:24] So, it's basically Turing complete twice over.
[00:07:24-00:07:28] And we run those trees to simulate almost everything.
[00:07:28-00:07:31] We do the behavior selection using the trees.
[00:07:31-00:07:33] We execute the behaviors using these trees.
[00:07:33-00:07:36] And we execute the reactions as well.
[00:07:37-00:07:41] So, this is an example of a little part of a behavior.
[00:07:41-00:07:44] A woman is pulling a bucket of water.
[00:07:44-00:07:46] She has an empty bucket down there.
[00:07:46-00:07:49] And when she pours the water, the bucket will now look filled.
[00:07:49-00:07:50] Right?
[00:07:50-00:07:54] So, this might be like a really simplified behavior tree for that.
[00:07:54-00:07:56] We are basically playing an animation.
[00:07:56-00:08:00] Somewhere in the middle of that animation, there is an event that will be triggered.
[00:08:00-00:08:01] We catch that event.
[00:08:01-00:08:05] And we react by setting the property of the bucket.
[00:08:05-00:08:07] So, it changes model and it looks filled.
[00:08:07-00:08:08] Okay.
[00:08:08-00:08:13] So, now you see at least a little bit of the basics of our script.
[00:08:13-00:08:15] And let's return to the place we were.
[00:08:15-00:08:17] We had all those trees.
[00:08:17-00:08:19] And the game didn't run.
[00:08:19-00:08:22] So, we tried to strip away things that were not necessary.
[00:08:22-00:08:23] Right?
[00:08:23-00:08:26] When you have far-away NPCs, you don't have to simulate a lot of things.
[00:08:26-00:08:27] They are definitely not visible.
[00:08:27-00:08:28] You don't have to render them.
[00:08:28-00:08:30] If you are not rendering them, they don't have to be visible.
[00:08:30-00:08:32] They don't have to be animated.
[00:08:32-00:08:37] And if the player doesn't interact with them, there doesn't have to be physics.
[00:08:37-00:08:44] But it turns out, if you strip the animations, it breaks the script.
[00:08:44-00:08:45] Because we are not running the animations.
[00:08:45-00:08:48] We are not getting those events.
[00:08:48-00:08:51] And the logic is not correctly simulated.
[00:08:51-00:08:59] It might seem that it's not as necessary to have a bucket filled with water for the world to work.
[00:08:59-00:09:01] We had way more complicated logic there.
[00:09:01-00:09:03] This was just a simple example.
[00:09:03-00:09:05] So, what we did to tackle that?
[00:09:05-00:09:08] We introduced the LOD branching in the script.
[00:09:08-00:09:14] We basically created another branch in the tree that handles the simplified simulation.
[00:09:14-00:09:16] So, it looked somehow like this.
[00:09:16-00:09:18] You see, this is the exact same tree.
[00:09:18-00:09:21] But we added the part in the yellow rectangle.
[00:09:21-00:09:28] Which has some LOD Guardian node that is basically just branching based on which level of detail you are at.
[00:09:29-00:09:36] And the simplified version in the yellow rectangle is basically just waiting and then doing the only consequence.
[00:09:36-00:09:40] Which is the very same node that is in the full simulation.
[00:09:40-00:09:43] Just changing the bucket to look filled.
[00:09:43-00:09:47] This looks nice, but it turned out to be actually really complicated.
[00:09:47-00:09:49] Because this is really a simple tree.
[00:09:49-00:09:51] Our trees were more complicated.
[00:09:51-00:09:54] There could be many animations in a line.
[00:09:54-00:09:58] And you must be able to switch at any time.
[00:09:58-00:10:00] In the correct consistent state.
[00:10:00-00:10:06] So, there was often a lot of nodes, a lot of logic handling just this transition to the other branch.
[00:10:08-00:10:10] Another thing we did is movement.
[00:10:10-00:10:15] It turns out, if you turn off physics and animation, the NPC can't move.
[00:10:15-00:10:17] So, what we did was...
[00:10:17-00:10:19] We were teleporting them.
[00:10:19-00:10:23] But we wanted NPCs to be at correct times at correct places.
[00:10:23-00:10:26] So, we couldn't just teleport them to the end of the road.
[00:10:26-00:10:27] So, what we did?
[00:10:27-00:10:29] We ran the normal pathfind.
[00:10:29-00:10:35] And then, along the pathfind, we executed those small, consequent teleports.
[00:10:37-00:10:44] The big advantage of this approach, or at least how we implemented it, was that we made it completely transparent through script.
[00:10:44-00:10:49] So, in the behavior tree, we have just one node, which is called move.
[00:10:49-00:10:52] And it doesn't matter in which branch you run it.
[00:10:52-00:10:55] Whether it's optimized or unoptimized, you don't have to be in any branch at all.
[00:10:55-00:10:59] The logic of the switching of the LOD is hidden within the node.
[00:10:59-00:11:09] So, when you run the node, it just looks what the current LOD is and runs the correct simulation.
[00:11:09-00:11:12] And it raises the pathfind when you switch the branch.
[00:11:14-00:11:15] Okay.
[00:11:15-00:11:17] So, we did some of these things.
[00:11:17-00:11:20] And we optimized the faraway NPCs.
[00:11:20-00:11:23] And the game actually did run way better.
[00:11:23-00:11:25] But...
[00:11:25-00:11:28] But that was mainly the engine stuff we stripped.
[00:11:28-00:11:31] We also made some script branching.
[00:11:31-00:11:33] So, our trees got smaller, right?
[00:11:33-00:11:34] So, that should be faster.
[00:11:34-00:11:36] That would be nice, but...
[00:11:36-00:11:42] No, because this is actually our behavior tree for sitting at a bench in a pub.
[00:11:45-00:11:49] And only this small part down here is the behavior execution.
[00:11:49-00:11:53] And only small parts of that were branched by the LOD branching.
[00:11:53-00:11:58] If you are wondering what most of this does, it selects the behavior.
[00:11:58-00:12:01] Then it selects the correct place you should sit at.
[00:12:01-00:12:03] There are more chairs at the bench.
[00:12:03-00:12:09] It handles, like, long-distance movements or some quest injections and stuff like that.
[00:12:10-00:12:16] So, we actually, by the LOD branching, we stripped only a very small part of this execution.
[00:12:16-00:12:21] So, it was still running with a lot of performance.
[00:12:21-00:12:22] Okay.
[00:12:22-00:12:27] It turns out, if you are running some script, some AI logic,
[00:12:27-00:12:30] it will be interacting with a lot of systems.
[00:12:30-00:12:33] It will be touching movement, animations, everything.
[00:12:33-00:12:35] So, it has to run on the main thread.
[00:12:35-00:12:38] But our AI update was above 10 milliseconds.
[00:12:38-00:12:40] Sometimes even spiking to way more.
[00:12:40-00:12:44] So, if we kept it on the main thread,
[00:12:44-00:12:49] we wouldn't have many hopes for at least reasonable frame times, right?
[00:12:49-00:12:51] So, we had to do something bold.
[00:12:51-00:12:53] We moved it to the thread completely.
[00:12:53-00:12:59] This is our brief overview of the threads.
[00:12:59-00:13:02] The top two threads are main thread and render thread.
[00:13:02-00:13:05] And the other workers, they are basically running asynchronous jobs.
[00:13:05-00:13:08] And this is what we did.
[00:13:09-00:13:17] We took the AI from the main thread and we put it kind of neatly at the second half of the frame.
[00:13:17-00:13:21] The reason for that is that the physics and animations at the first half of the frame
[00:13:21-00:13:24] are updating all the entities.
[00:13:24-00:13:28] All the positions, all the states are updated here.
[00:13:28-00:13:32] And then these informations are logged down.
[00:13:32-00:13:35] And the render on the main thread will try to prepare the next frame.
[00:13:35-00:13:36] The rendering for the next frame.
[00:13:36-00:13:38] So, the entities can't be touched anymore.
[00:13:38-00:13:46] Which has the advantage that our AI update is not racing with any other systems.
[00:13:46-00:13:49] But there is a disadvantage that the AI cannot change anything, right?
[00:13:49-00:13:50] So, what we do is...
[00:13:50-00:13:52] We actually do all the simulation.
[00:13:52-00:13:57] And we defer the results to the end of the frame.
[00:13:57-00:14:01] So, they are executed right when the render ends.
[00:14:01-00:14:02] This saved a lot of time.
[00:14:02-00:14:05] It might sound simple, but it was an extreme amount of work.
[00:14:05-00:14:07] But it worked in the end.
[00:14:07-00:14:09] So, the results for the first game.
[00:14:09-00:14:11] This was all about the first game.
[00:14:13-00:14:17] We actually managed to simulate 600 NPCs at all times.
[00:14:17-00:14:19] But the frame times weren't that good.
[00:14:20-00:14:25] I'm actually talking about the performance on consoles of the time.
[00:14:25-00:14:29] Xbox One and PS4.
[00:14:29-00:14:35] The visibility was 60 meters or 90 if you account for hysteresis.
[00:14:35-00:14:38] But we actually haven't managed to simulate all of the NPCs.
[00:14:38-00:14:44] Some of the less important NPCs in the villages were unloaded when you got far away.
[00:14:44-00:14:47] Also, our script logic was very bloated.
[00:14:47-00:14:49] I showed you the huge tree.
[00:14:50-00:14:53] And that had the branches which had to be handled.
[00:14:53-00:14:55] So, that caused a lot of bugs.
[00:14:55-00:15:01] And also, we were still simulating a lot of logic in the scripting trees.
[00:15:01-00:15:04] So, our faders or even NPC reactions were very long.
[00:15:04-00:15:09] But the game came out and it was kind of a success.
[00:15:09-00:15:12] So, we knew we could do better, right?
[00:15:12-00:15:17] We knew where our weak spots were and what we could improve.
[00:15:18-00:15:21] For the second game, we got both.
[00:15:21-00:15:24] We wanted way more NPCs and a big city.
[00:15:24-00:15:28] And we also wanted to fix the issues we had with the first game.
[00:15:28-00:15:32] So, we didn't want the branching there in the script causing all the bugs.
[00:15:32-00:15:36] And we actually wanted the scripters to be able to script the game.
[00:15:36-00:15:39] Not like the low-level systems, right?
[00:15:39-00:15:43] And we wanted all the NPCs to be there at all times.
[00:15:43-00:15:45] Like the original vision was.
[00:15:45-00:15:48] But we had a big advantage at this point.
[00:15:48-00:15:50] We were starting the development.
[00:15:50-00:15:57] And we could design the game from the very beginning with the AI LOD in mind.
[00:15:57-00:16:01] So, without further suspense, let's see the core of our current solution.
[00:16:01-00:16:05] We actually now have three main LODs.
[00:16:05-00:16:08] The close one is basically the full simulation.
[00:16:08-00:16:12] We do it only for 70 closest visible NPCs.
[00:16:12-00:16:17] And only when they are at least 150 meters far away.
[00:16:17-00:16:19] This is basically the same picture.
[00:16:20-00:16:23] Zoomed slightly out, the blue dot is player.
[00:16:23-00:16:27] And you can see that some of the NPCs that are a little bit further on the outskirts of the village
[00:16:27-00:16:30] are already in the middle LOD, our second LOD.
[00:16:30-00:16:41] And the main assignment for these NPCs is that they have to be able to quickly switch into the close LOD.
[00:16:41-00:16:46] And we can support up to 400 NPCs that are no longer than 600 meters.
[00:16:46-00:16:49] Because then it doesn't make sense to simulate.
[00:16:50-00:16:52] More of them.
[00:16:52-00:17:00] Maybe you can see that together these two numbers, 70 and 400, are quite similar to the first game.
[00:17:00-00:17:08] But we added a third LOD, which is for the NPCs that are basically at another villages.
[00:17:08-00:17:12] And that enables us to heavily optimize those.
[00:17:12-00:17:16] So this is the same picture, again zoomed out, with the player being the blue dot.
[00:17:16-00:17:20] And you can see the other villages in the camera.
[00:17:20-00:17:22] So, the middle LOD.
[00:17:22-00:17:29] As I said, the main point of this LOD is to strip some things,
[00:17:29-00:17:33] but being still able to quickly switch into the correct simulation state.
[00:17:33-00:17:36] So we actually have to simulate the whole AI.
[00:17:36-00:17:39] We need the position and the state to be precise.
[00:17:39-00:17:46] If we are playing several animations or a long animation, we still have to know exactly where we are.
[00:17:46-00:17:49] We did similar optimizations to the first game.
[00:17:49-00:17:52] So we stripped the physics, animations, rendering.
[00:17:52-00:17:55] Some small other updates that could be skipped.
[00:17:55-00:18:00] When you looked closer to CryEngine, for example, the updates of water splashes and small things like that.
[00:18:00-00:18:02] But mostly the same.
[00:18:02-00:18:04] But we did one huge change.
[00:18:04-00:18:08] And that is that we made the animation simulation transparent.
[00:18:08-00:18:13] So we did our own animation simulator that doesn't care about the bones.
[00:18:13-00:18:19] It just writes timers and triggers the correct events at correct times.
[00:18:19-00:18:21] We also made the...
[00:18:22-00:18:27] execution part of the behavior trees a little bit low level.
[00:18:27-00:18:32] But that's actually a topic for another talk, which is hopefully or luckily already existing.
[00:18:32-00:18:41] If you have access to GDC Vault, my colleague Matěj Marko actually had a great talk about the goal-oriented action planning
[00:18:41-00:18:45] and the changes we did with the model behavior trees to improve this.
[00:18:45-00:18:50] So, the middle LOD was very similar to the first game.
[00:18:50-00:18:51] But now the new technology.
[00:18:51-00:18:53] The Far LOD.
[00:18:53-00:18:55] So...
[00:18:55-00:18:58] The Far LOD is actually already quite far away.
[00:18:58-00:19:01] So the player has to travel to reach those NPCs.
[00:19:01-00:19:04] That enables us to be way less precise.
[00:19:04-00:19:08] It's enough with the position being up to 10 meters.
[00:19:08-00:19:11] And we don't actually have to simulate the correct state or item handling.
[00:19:11-00:19:15] Because there is enough time to start it up when the player gets close.
[00:19:17-00:19:20] So we actually don't execute the behaviors.
[00:19:20-00:19:23] We just run the behavior selection part of the algorithm.
[00:19:23-00:19:24] And here you can see a pub.
[00:19:24-00:19:27] The pub in our games are mostly outside, like they were.
[00:19:27-00:19:30] And those red dots are the NPCs in Far LOD.
[00:19:30-00:19:33] And they are not correctly sitting at places at the tables.
[00:19:33-00:19:34] They are just in the pub.
[00:19:34-00:19:35] Because that's enough.
[00:19:35-00:19:37] And the player approaches this village.
[00:19:37-00:19:41] They will start their behaviors and get to the correct place.
[00:19:41-00:19:43] We also have a fast behavior startup.
[00:19:43-00:19:48] That means that, for example, the items or clothes of the NPCs will get...
[00:19:48-00:19:49] will get synchronized.
[00:19:49-00:19:51] Will get synchronized right away.
[00:19:51-00:19:52] Instantly.
[00:19:52-00:19:54] Because if you were approaching the village.
[00:19:54-00:19:58] And some of the NPCs switched to the closer LOD.
[00:19:58-00:19:59] And they would realize.
[00:19:59-00:20:02] Oh, but I need this item in my hand.
[00:20:02-00:20:05] They might be forced to leave the pub.
[00:20:05-00:20:07] Go to pick the item and go back.
[00:20:07-00:20:09] And that we don't want there, right?
[00:20:11-00:20:12] So.
[00:20:12-00:20:16] This is actually one of the biggest changes we did for the second game.
[00:20:16-00:20:18] The selection of the behavior.
[00:20:19-00:20:22] We looked at the huge trees of the original game.
[00:20:22-00:20:25] And we saw some repeating patterns, actually.
[00:20:25-00:20:29] All this big tree was mostly handing the behavior selection.
[00:20:29-00:20:33] And that was time of the day when the behavior should be played.
[00:20:33-00:20:34] Or some weather.
[00:20:34-00:20:35] Also the properties of the NPC.
[00:20:35-00:20:37] Whether it's drunk, needs to sleep.
[00:20:37-00:20:40] Or whether maybe social status.
[00:20:40-00:20:41] Or whether the gender.
[00:20:41-00:20:43] There are also constraints.
[00:20:43-00:20:46] So if there is the woman pulling water from a well.
[00:20:46-00:20:49] No other NPC can be there at that time.
[00:20:49-00:20:54] And also there was some random systems.
[00:20:54-00:20:57] If you select some behavior by chance.
[00:20:57-00:20:59] Then you are locked into the behavior for a while.
[00:20:59-00:21:00] So.
[00:21:00-00:21:02] When we saw those repeating patterns.
[00:21:02-00:21:03] We actually realized.
[00:21:03-00:21:07] We could get rid of the tree and simulate everything in the code.
[00:21:07-00:21:12] And just made those patterns be parameters of code execution.
[00:21:12-00:21:16] So this huge tree got removed.
[00:21:16-00:21:19] And that helped not only with the farm.
[00:21:19-00:21:22] But for all the simulation of everything.
[00:21:22-00:21:23] So.
[00:21:23-00:21:25] It is configurable in script.
[00:21:25-00:21:28] But it's executed in code.
[00:21:28-00:21:29] So.
[00:21:29-00:21:33] What actually do we do for the NPCs in the far LOD?
[00:21:33-00:21:36] The whole execution is now in code.
[00:21:36-00:21:38] Because we have the behavior selection code.
[00:21:38-00:21:41] We can run it to find the behavior.
[00:21:41-00:21:45] Then if the behavior is different than the one run up to this point.
[00:21:45-00:21:47] We do need to do the switch.
[00:21:47-00:21:48] And the switch.
[00:21:48-00:21:50] Will change some constraints.
[00:21:50-00:21:51] For example.
[00:21:51-00:21:52] There is the innkeeper in the pub.
[00:21:52-00:21:53] If innkeeper comes to the pub.
[00:21:53-00:21:54] He opens the pub.
[00:21:54-00:22:00] And other behaviors will get opened for the visitors.
[00:22:00-00:22:01] So.
[00:22:01-00:22:04] When we do have those global consequences settled.
[00:22:04-00:22:07] Then we have to decide the position where the behavior is happening.
[00:22:07-00:22:10] And we do this automatically as well.
[00:22:10-00:22:15] Because it's enough to be 10 meters within the correct distance.
[00:22:15-00:22:19] So we can just pick any position of any animation.
[00:22:19-00:22:21] And it will be participating there.
[00:22:21-00:22:23] And just teleport the NPC there.
[00:22:23-00:22:26] And if the NPC is too far away.
[00:22:26-00:22:27] We will move it.
[00:22:27-00:22:29] And we actually simplify that as well.
[00:22:29-00:22:32] Because we have this big graph of paths.
[00:22:32-00:22:38] That's actually following the real roads.
[00:22:38-00:22:40] And we don't run the full pathfind.
[00:22:40-00:22:42] We run pathfind only along those roads.
[00:22:42-00:22:45] So the NPCs in the far LOD move only along the roads.
[00:22:45-00:22:48] And most of the time that's enough to get them close enough.
[00:22:48-00:22:51] And finally teleport them to the correct destination.
[00:22:51-00:22:54] So.
[00:22:54-00:22:58] By having those simulations being so simple.
[00:22:58-00:23:01] We could actually strip way more things in the far LOD.
[00:23:01-00:23:03] So we could actually save some memory.
[00:23:03-00:23:05] So what could we release?
[00:23:05-00:23:09] The biggest save was in character.
[00:23:09-00:23:11] Which is basically a skeleton and a mesh.
[00:23:11-00:23:13] We could completely delete that from the memory.
[00:23:13-00:23:15] We could delete the physical representation.
[00:23:15-00:23:16] We don't have just capsules.
[00:23:16-00:23:18] We have articulated physics.
[00:23:18-00:23:19] Then.
[00:23:19-00:23:23] We could remove most of the behavior trees that weren't being run.
[00:23:23-00:23:26] And some other AI components like combat.
[00:23:26-00:23:29] Or some perception stuff.
[00:23:29-00:23:35] And basically some other engine stuff that were big enough to pay off to be removed.
[00:23:35-00:23:37] What we kept.
[00:23:37-00:23:39] Is some RPG representation.
[00:23:39-00:23:41] This is the state we want to keep.
[00:23:41-00:23:43] The health and stuff.
[00:23:43-00:23:49] We had to keep some part of the AI to be able to react to things.
[00:23:49-00:23:57] And then basically we kept systems that were small enough that it wasn't worth removing them.
[00:23:57-00:24:03] Doing this we lowered the memory for each NPC under 50 kilobytes.
[00:24:03-00:24:06] Which is 25% of the original size approximately.
[00:24:06-00:24:08] So.
[00:24:08-00:24:11] I just said that we removed most of the behavior trees.
[00:24:11-00:24:13] But we kept some systems for the reactions.
[00:24:13-00:24:14] So.
[00:24:14-00:24:18] What do the far LOD NPCs do when they need to react to something?
[00:24:18-00:24:20] They don't have any perception.
[00:24:20-00:24:24] Because there's rarely something to perceive.
[00:24:24-00:24:27] Even if player does something and runs away.
[00:24:27-00:24:31] Only a very small amount of the NPCs in the world have to react to that.
[00:24:31-00:24:37] So it would be a waste of resources if we simulated that for all of the NPCs all the time.
[00:24:37-00:24:41] So what we actually do is that we have a representation for the crime itself.
[00:24:41-00:24:48] It's this thing we call perceptible volume.
[00:24:48-00:24:50] So if you for example kill somebody.
[00:24:50-00:24:51] Or kill some guards.
[00:24:51-00:24:53] And the system.
[00:24:53-00:24:56] You would run away and they would switch to the far LOD.
[00:24:56-00:25:03] There will be those perceptible volumes that are representing the crime you did.
[00:25:03-00:25:10] And those perceptible volumes are actually actively searching for NPCs around them.
[00:25:10-00:25:13] And forcing them to be switched into the middle LOD.
[00:25:13-00:25:18] So the NPCs then when they switch to the middle LOD can simulate the crime fully.
[00:25:18-00:25:20] So even if you kill someone.
[00:25:20-00:25:21] And hide the body.
[00:25:21-00:25:23] And run far away.
[00:25:23-00:25:25] It actually matters how well you hit the body.
[00:25:25-00:25:28] Because all the crime resolution will get simulated.
[00:25:28-00:25:31] If you want to know more about perception or crime.
[00:25:31-00:25:34] I can recommend talk of my colleague.
[00:25:34-00:25:35] Tomorrow.
[00:25:35-00:25:37] Design for everything in KCD 2.
[00:25:37-00:25:39] By Vadim Petrov.
[00:25:39-00:25:40] Okay.
[00:25:40-00:25:43] So the general thing to take away from this is that.
[00:25:43-00:25:46] If you can make something passive in the far LOD.
[00:25:46-00:25:48] Do it like this passively.
[00:25:48-00:25:49] Okay.
[00:25:49-00:25:52] Next part is the city of Kutenberg.
[00:25:52-00:25:56] Which was the ultimate bottleneck for everything we were doing in the game.
[00:25:56-00:26:00] So the challenge was to make the city look busy.
[00:26:00-00:26:03] We actually didn't know how many people are necessary for that.
[00:26:03-00:26:06] Or how many people we can support.
[00:26:06-00:26:07] But spoiler alert.
[00:26:07-00:26:09] It turned out to be 1500 NPCs.
[00:26:09-00:26:17] And we definitely couldn't increase the budget of the 70 closest NPCs.
[00:26:17-00:26:18] Because.
[00:26:18-00:26:22] We were actually happy that we didn't have to lower the budget.
[00:26:22-00:26:25] Because the city was such a performance heavy thing.
[00:26:27-00:26:28] But.
[00:26:28-00:26:29] As I already said.
[00:26:29-00:26:31] We could start designing the systems from the very get go.
[00:26:31-00:26:33] It was a huge help.
[00:26:33-00:26:36] Because we could make the white box of the city.
[00:26:36-00:26:38] And we filled it with double NPCs.
[00:26:38-00:26:41] So we could see how many NPCs are actually visible.
[00:26:41-00:26:44] How lively it would probably look like.
[00:26:44-00:26:46] And the city was designed in a way.
[00:26:46-00:26:47] So that.
[00:26:47-00:26:54] Not too many NPCs were necessary to be visible at the same time.
[00:26:54-00:26:56] So what we did.
[00:26:56-00:27:00] We didn't do any long streets that would be busy with too many NPCs.
[00:27:00-00:27:02] If you actually pay attention.
[00:27:02-00:27:05] You can see that we don't have any see through fences in the city.
[00:27:05-00:27:07] They are all opaque walls.
[00:27:07-00:27:10] If the player is walking the city walls.
[00:27:10-00:27:13] Which is something we wanted him to be able to do.
[00:27:13-00:27:16] He can't see into some busy squares.
[00:27:16-00:27:19] And he could see a lot of space under the walls.
[00:27:19-00:27:22] But those are the places where we put way less NPCs.
[00:27:22-00:27:25] We also added some soft vision breakers.
[00:27:25-00:27:28] Like carts of hay.
[00:27:28-00:27:30] Or some stalls with shopping.
[00:27:30-00:27:32] And of course there are speed limits.
[00:27:32-00:27:35] You can't dash with the horse in the city.
[00:27:35-00:27:38] And that is not only because of the NPCs.
[00:27:38-00:27:40] But also because of all the graphics.
[00:27:40-00:27:44] All the streaming.
[00:27:44-00:27:46] So we already had the city with this structure.
[00:27:46-00:27:49] But we still had to somehow leverage it.
[00:27:49-00:27:53] To some algorithm that would use this structure.
[00:27:53-00:27:57] So what he came up with were visibility areas.
[00:27:57-00:28:02] So we split the city into areas that were approximately 100 square meters.
[00:28:02-00:28:05] And we defined the relative visibility.
[00:28:05-00:28:08] So here you can see the player is in the yellow area.
[00:28:08-00:28:11] And he can see into all the green areas.
[00:28:14-00:28:17] We couldn't use occlusion that's used in rendering.
[00:28:17-00:28:21] Because we needed to know a little bit in advance.
[00:28:21-00:28:23] Which NPCs will be visible.
[00:28:23-00:28:25] Because the switch is still not instantaneous.
[00:28:25-00:28:28] It needs at least like one to two seconds.
[00:28:28-00:28:30] So occlusion wouldn't be sufficient.
[00:28:30-00:28:35] Also note that these areas are used only for the switch between close and middle LOD.
[00:28:35-00:28:44] Because the far LOD is so far away that the structure no longer has the same meaning.
[00:28:44-00:28:46] So we can see as the player moves.
[00:28:46-00:28:48] The areas that are containing visible NPCs actually change.
[00:28:49-00:28:52] And here you can see the border of the area.
[00:28:52-00:28:53] And when the NPCs move.
[00:28:53-00:28:57] They naturally switch into the correct level of detail.
[00:28:58-00:29:01] This is the bird view of the city.
[00:29:01-00:29:03] The player is in the middle.
[00:29:03-00:29:05] And you can see the green cross there probably.
[00:29:05-00:29:09] Because he's currently staying at the crossroads.
[00:29:09-00:29:11] So he can see into two streets.
[00:29:11-00:29:16] But many of the NPCs that are actually close can be switched to middle LOD.
[00:29:16-00:29:18] Because they can't be accessed quickly.
[00:29:19-00:29:24] You can also see that the far LOD is way closer than normally.
[00:29:24-00:29:28] And that's why we have the speed limit there.
[00:29:28-00:29:33] And also the behaviors of the people in the city are carefully selected.
[00:29:33-00:29:35] So they can start very quickly.
[00:29:36-00:29:39] And when we had those visibility areas.
[00:29:39-00:29:41] We actually used them at other locations.
[00:29:41-00:29:44] So on the left that's the Sigismund army camp.
[00:29:44-00:29:46] And on the right that's the Trotsky castle.
[00:29:46-00:29:48] There's way more areas than in the city.
[00:29:48-00:29:50] But it's still very helpful.
[00:29:50-00:29:52] Ok, so results for the city.
[00:29:52-00:29:56] We actually managed to have 1500 NPCs.
[00:29:56-00:29:58] And still run 60 FPS.
[00:29:58-00:30:02] That's because we just kept the budgets for the rest of the game.
[00:30:02-00:30:07] We just more appropriately selected which NPCs are in which LOD.
[00:30:08-00:30:11] The vision distances are actually quite low.
[00:30:11-00:30:13] They can be as low as 50 meters.
[00:30:13-00:30:16] But that's where we add some soft vision breakers.
[00:30:16-00:30:17] And we also done pop the NPCs.
[00:30:17-00:30:19] Into existence right away.
[00:30:19-00:30:20] We differ them.
[00:30:20-00:30:24] So if they are for example at the 50 meters.
[00:30:24-00:30:26] And there is some visual obstruction.
[00:30:26-00:30:28] Like the stalls.
[00:30:28-00:30:31] It's not really noticeable.
[00:30:31-00:30:35] There is a funny thing.
[00:30:35-00:30:40] That when we actually found out we can run those 1500 NPCs.
[00:30:40-00:30:44] We hit the bottleneck of the environment settling.
[00:30:44-00:30:47] Because all our NPCs have to live somewhere.
[00:30:47-00:30:48] They have to need.
[00:30:49-00:30:50] A house with bed.
[00:30:50-00:30:52] And we didn't have as many furnished houses.
[00:30:52-00:30:56] And the environment team was all restrained.
[00:30:56-00:30:57] And couldn't make more of them.
[00:30:57-00:30:59] So we actually had it cheated a little bit.
[00:30:59-00:31:01] The NPCs.
[00:31:01-00:31:05] Some of them are actually living in the inaccessible houses.
[00:31:05-00:31:07] They get close to the door.
[00:31:07-00:31:08] If the player doesn't look.
[00:31:08-00:31:09] They teleport inside.
[00:31:09-00:31:10] They pretend they are sleeping.
[00:31:10-00:31:11] And in the morning.
[00:31:11-00:31:12] When the player is not close.
[00:31:12-00:31:13] They teleport outside.
[00:31:13-00:31:14] And continue their day normally.
[00:31:15-00:31:16] Ok.
[00:31:16-00:31:18] So we have this technology.
[00:31:18-00:31:21] We could simulate 500 NPCs cheaply.
[00:31:21-00:31:27] And we apply it to more things than just the regular simulation.
[00:31:27-00:31:30] Our skip time is actually simulated.
[00:31:30-00:31:34] We don't just switch the time to correct time of day.
[00:31:34-00:31:36] We actually run the whole simulation.
[00:31:36-00:31:40] So if you for example do some crime.
[00:31:40-00:31:41] Or are in danger.
[00:31:41-00:31:43] And you try to skip time.
[00:31:43-00:31:45] You will be woken up.
[00:31:45-00:31:46] Interrupted.
[00:31:46-00:31:47] And everything will have to be resolved.
[00:31:48-00:31:50] Although the quests will progress as they should.
[00:31:50-00:31:52] If they have some time limit or some triggers.
[00:31:54-00:31:55] So what we do.
[00:31:55-00:32:00] We actually can switch way more NPCs to the more optimized LODs.
[00:32:00-00:32:01] You don't see any of them.
[00:32:01-00:32:03] So there are no enclosed LODs.
[00:32:03-00:32:07] And only a few of them are in the middle LODs.
[00:32:07-00:32:09] Only those very close to the player.
[00:32:11-00:32:15] Very similar thing actually happens during the fast travel.
[00:32:15-00:32:17] We actually run the player through the road.
[00:32:17-00:32:20] And he can meet people.
[00:32:20-00:32:24] So if there will be for example encounter.
[00:32:24-00:32:25] You would be traveling the world.
[00:32:25-00:32:26] You meet some bandits.
[00:32:26-00:32:28] They are too strong for you.
[00:32:28-00:32:29] So you run away back.
[00:32:29-00:32:31] And then you try to fast travel over them.
[00:32:31-00:32:32] You cannot.
[00:32:32-00:32:36] You will be interrupted again by the very same bandits.
[00:32:36-00:32:38] The battles are something slightly different.
[00:32:38-00:32:41] Player actually cannot leave the battle area.
[00:32:41-00:32:43] At least not without the game over.
[00:32:43-00:32:48] So we can switch almost all of the world to the far LOD.
[00:32:49-00:32:52] And it is still simulated.
[00:32:52-00:32:54] So if you do something just before a battle.
[00:32:54-00:33:00] You have to deal with it after a battle.
[00:33:00-00:33:05] For the soldiers in the battle themselves.
[00:33:05-00:33:07] They are actually optimized very differently.
[00:33:07-00:33:09] Because the use case is very different.
[00:33:09-00:33:13] They don't have any behaviors they would have to choose.
[00:33:13-00:33:18] They are just standing there waiting for their turn.
[00:33:18-00:33:20] And they are always visible.
[00:33:20-00:33:21] So what we do.
[00:33:21-00:33:22] We don't use LODs.
[00:33:22-00:33:23] We have these for them.
[00:33:23-00:33:26] We actually simplified them in a different way.
[00:33:26-00:33:29] We have sprites for the very far away NPCs.
[00:33:29-00:33:31] That can't be reached anyhow.
[00:33:31-00:33:34] And we have track view for the closer ones.
[00:33:34-00:33:35] But still unreachable.
[00:33:35-00:33:38] They are basically pre-recorded.
[00:33:38-00:33:42] And playing something like a cutscene.
[00:33:42-00:33:44] If you hit them they will switch.
[00:33:44-00:33:47] And play a death animation and die.
[00:33:47-00:33:51] And sometimes they will switch naturally.
[00:33:51-00:33:53] To the correct NPC.
[00:33:53-00:33:55] And they might get close to interact.
[00:33:55-00:33:57] So the player is now the battle man.
[00:33:57-00:34:00] This NPC now switches to the full simulation.
[00:34:00-00:34:02] And he can be fought.
[00:34:02-00:34:05] For the animals.
[00:34:05-00:34:08] I mean mainly wildlife.
[00:34:08-00:34:10] We actually don't use the LODs as well.
[00:34:10-00:34:13] Because they don't have any identity.
[00:34:13-00:34:15] If you hurt an animal it runs away.
[00:34:15-00:34:17] It won't remember anything.
[00:34:17-00:34:21] We don't use them in the global quest logic.
[00:34:21-00:34:22] They don't have to be referenced.
[00:34:22-00:34:23] They don't have to be there.
[00:34:23-00:34:27] So it would be actually completely unnecessary to simulate them.
[00:34:27-00:34:30] So that's why we are normally spawning them.
[00:34:30-00:34:32] When the player gets close.
[00:34:32-00:34:35] That actually halves the NPC number in our game.
[00:34:35-00:34:38] Approximately.
[00:34:38-00:34:39] Okay.
[00:34:39-00:34:40] So.
[00:34:40-00:34:44] The conclusion.
[00:34:44-00:34:47] It actually is possible to simulate the whole world.
[00:34:47-00:34:51] It could improve the immersion a lot.
[00:34:51-00:34:54] You can have way more detailed behaviors of the NPCs.
[00:34:54-00:34:55] And better reactions.
[00:34:55-00:34:57] But if you want to do it.
[00:34:57-00:35:00] Be prepared that it's a lot of work.
[00:35:00-00:35:02] If you want to do it.
[00:35:02-00:35:06] The good place to start is knowing the NPC position.
[00:35:06-00:35:08] And if you want to know the NPC position.
[00:35:08-00:35:10] You probably need to know the NPC behavior.
[00:35:10-00:35:11] And the constraints.
[00:35:11-00:35:13] But that's very basic.
[00:35:13-00:35:16] If you can use threats.
[00:35:16-00:35:18] It probably won't be easy.
[00:35:18-00:35:20] But today computers have a lot of threats.
[00:35:20-00:35:23] So it would be wise to run everything on a main threat.
[00:35:23-00:35:30] A huge thing we did was we found a standardized logic in script.
[00:35:30-00:35:32] And we moved it to the code.
[00:35:32-00:35:34] Which helped not only by speeding up the simulation.
[00:35:34-00:35:40] But the code also had way more knowledge about what is happening in the game.
[00:35:40-00:35:42] And could do some other optimizations.
[00:35:42-00:35:44] And last but not least.
[00:35:44-00:35:49] It's important to set early limits for the systems and environment.
[00:35:49-00:35:51] Like we did with the city.
[00:35:51-00:35:55] I know this is easier said than done.
[00:35:55-00:35:59] But when I was talking actually.
[00:35:59-00:36:01] That for the first game.
[00:36:01-00:36:02] We first did all the features.
[00:36:02-00:36:03] And then we optimized.
[00:36:03-00:36:05] I was making a little bit fun of that.
[00:36:05-00:36:08] But it's actually not a bad way to do a game.
[00:36:08-00:36:10] The important thing is.
[00:36:10-00:36:12] That you have to have a plan.
[00:36:12-00:36:14] What you will do in the future with the optimizations.
[00:36:14-00:36:16] So we actually.
[00:36:16-00:36:17] Even for the second game.
[00:36:17-00:36:18] We actually did all of that.
[00:36:18-00:36:20] We actually did all the features.
[00:36:20-00:36:22] And then implemented this LOD system.
[00:36:22-00:36:25] But we from the very beginning of the development.
[00:36:25-00:36:27] Knew this system will be there.
[00:36:27-00:36:30] And what are the limitations.
[00:36:30-00:36:32] So a good analogy would be.
[00:36:32-00:36:34] If you are borrowing a lot of money.
[00:36:34-00:36:39] You have to have a plan how you are going to pay them back.
[00:36:39-00:36:44] This is actually our 10 years worth of work almost.
[00:36:44-00:36:46] So I couldn't write all the people there.
[00:36:46-00:36:47] If you want to see.
[00:36:47-00:36:49] All the people that work on this.
[00:36:49-00:36:50] Play the game.
[00:36:50-00:36:51] Run the credits.
[00:36:51-00:36:52] They are there.
[00:36:52-00:36:55] But just the ones that did most of the work.
[00:36:55-00:36:57] On these very things I was talking about.
[00:36:57-00:36:58] Some people from the code.
[00:36:58-00:37:00] And some people from the script.
[00:37:00-00:37:02] And that's actually it.
[00:37:02-00:37:05] So feel free to ask any questions.
[00:37:05-00:37:10] Here or during the rest of the event.
[00:37:10-00:37:12] Or you can even shoot me an email.
