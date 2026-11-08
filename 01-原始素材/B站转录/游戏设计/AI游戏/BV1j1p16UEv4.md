---
title: "AI&G Conference|《天国:拯救2》中的全方位设计｜2025人工智能与游戏大会——Design for everything in Kingdom"
platform: bilibili
bvid: BV1j1p16UEv4
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-10-14 19:31:29
duration_sec: 4521
view: 547
like: 25
coin: 4
favorite: 28
reply: 0
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV1j1p16UEv4
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 42014
crawl_time: 2026-11-08 21:20:02


# AI&G Conference|《天国:拯救2》中的全方位设计｜2025人工智能与游戏大会——Design for everything in Kingdom

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-10-14 19:31:29
- **时长**: 1小时15分21秒
- **播放**: 547 | 赞: 25 | 币: 4 | 藏: 28
- **链接**: https://www.bilibili.com/video/BV1j1p16UEv4

## 视频描述

原视频：https://www.youtube.com/watch?v=NjGo2mBxg2M
（2026年5月6日）《天国：拯救2》中的万物设计：NPC 感知系统的设计与迭代
演讲者： Vadim Petrov
工作室： Warhorse Studios

=== 演讲简介 ===
本次演讲将以《天国：拯救》（Kingdom Come: Deliverance）及其续作为例，探讨游戏设计与迭代之

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1j1p16UEv4
# 语言=en 时长=00:37:23 模型=large-v3

[00:00:16-00:00:18] OK, let's go.
[00:00:18-00:00:19] Hello again.
[00:00:19-00:00:21] My name is Vadim Petrov, and I would
[00:00:21-00:00:23] like to talk to you about the game we
[00:00:23-00:00:27] made with Warhorse Studios and released earlier this year.
[00:00:27-00:00:30] Some further introductions.
[00:00:30-00:00:32] That's me.
[00:00:32-00:00:34] I have been programming at Warhorse for about six years
[00:00:34-00:00:35] now.
[00:00:35-00:00:38] I've started with audio, and then I focused.
[00:00:38-00:00:40] My focus changed to AI.
[00:00:40-00:00:44] In my free time, I like music, and I like to race cars.
[00:00:44-00:00:47] This is me and my friend after a race.
[00:00:47-00:00:47] We did not win.
[00:00:47-00:00:48] We didn't even finish.
[00:00:48-00:00:53] But it was a lot of fun.
[00:00:53-00:00:55] Something about the company.
[00:00:55-00:00:59] It was founded in Prague in 2011.
[00:00:59-00:01:03] And so far, we have released two games, both medieval RPGs.
[00:01:09-00:01:12] Right now, the studio is about 250 people.
[00:01:12-00:01:15] We have a new office in Brno, and the picture
[00:01:15-00:01:17] is one of our founders, Martin Klima,
[00:01:17-00:01:19] giving a speech at the release.
[00:01:19-00:01:21] This is the release party of the sequel.
[00:01:21-00:01:26] It was a fancy event, a lot of fun.
[00:01:26-00:01:28] Something about the game.
[00:01:28-00:01:32] The sequel to the game we released in 2018.
[00:01:32-00:01:36] This one was released again this year in February.
[00:01:36-00:01:41] And it's a medieval open world game, RPG game,
[00:01:41-00:01:45] role-playing game, sorry, that has these three main pillars.
[00:01:45-00:01:47] It's immersion.
[00:01:47-00:01:50] We want the player to feel as if they are really in the medieval,
[00:01:50-00:01:53] bohemian world.
[00:01:53-00:01:54] We try to be historically accurate,
[00:01:54-00:01:56] so the people wear what they should be wearing.
[00:01:56-00:02:00] They should do the jobs that they would do in this time
[00:02:00-00:02:01] period.
[00:02:01-00:02:05] And we also like to make the game spectacular
[00:02:05-00:02:09] and to make the player feel spectacular.
[00:02:09-00:02:12] It's based on two maps that are both around 16 square
[00:02:12-00:02:14] kilometers.
[00:02:14-00:02:15] There's one major city, which is going
[00:02:15-00:02:19] to be one of the focal points of this talk, the city of Kutenberg
[00:02:19-00:02:22] with over 1,500 NPCs living in there.
[00:02:22-00:02:24] And the game is pretty large.
[00:02:24-00:02:26] It's got about 50 main quests.
[00:02:26-00:02:30] We are just going to release the third DLC now in about a week.
[00:02:30-00:02:38] And you can spend well over 100 hours in the game.
[00:02:38-00:02:39] Now to the talk itself.
[00:02:39-00:02:44] I've named it very peculiar design for everything.
[00:02:44-00:02:47] But I'm not going to talk about design of everything.
[00:02:47-00:02:49] I'm going to talk about Sight Sense.
[00:02:49-00:02:53] And we tried to design it to work in all the situations
[00:02:53-00:02:53] that it could.
[00:02:53-00:02:54] Because.
[00:02:54-00:02:59] Human sense, realistically, does work like that.
[00:02:59-00:03:02] But even though we tried to strive
[00:03:02-00:03:06] for historical accuracy and realism, it's still a game.
[00:03:06-00:03:10] So the leitmotif of the presentation
[00:03:10-00:03:14] will be maybe doing such a big generic system
[00:03:14-00:03:21] is not such a good idea.
[00:03:21-00:03:25] Let's see specifically what waits for us.
[00:03:25-00:03:28] I'm going to present some design requirements for the system.
[00:03:28-00:03:28] OK.
[00:03:28-00:03:34] And then some basic components of the system itself.
[00:03:34-00:03:35] I'm not going to get too technical.
[00:03:35-00:03:39] But if you're interested, I'll be happy to describe
[00:03:39-00:03:41] all the details later.
[00:03:41-00:03:44] And then the main topic, or the main part of the talk,
[00:03:44-00:03:48] some challenges and how we face them and solve them.
[00:03:48-00:03:50] And then some problems that we did not manage to solve,
[00:03:50-00:03:52] but still kept in the game.
[00:03:52-00:03:54] So maybe if you play the next DLC,
[00:03:54-00:03:57] you can find some exploits that you can use to your advantage.
[00:03:57-00:04:02] So before we go.
[00:04:02-00:04:04] Let's go to the site itself.
[00:04:04-00:04:10] We have what I like to call three pairs of immersion
[00:04:10-00:04:11] in our game.
[00:04:11-00:04:14] That means we have fully simulated NPCs.
[00:04:14-00:04:17] This was the topic of my colleague's talk
[00:04:17-00:04:19] yesterday by Petr Smircek.
[00:04:19-00:04:22] So I'm not going to go too deep into this.
[00:04:22-00:04:28] But what it basically means is that the NPCs live their life.
[00:04:28-00:04:29] They have their own bed.
[00:04:29-00:04:31] They have their own home.
[00:04:31-00:04:33] They have a family, some friends that live on there.
[00:04:33-00:04:36] In their cottage, or in a townhouse.
[00:04:36-00:04:37] They have some job.
[00:04:37-00:04:41] They either can be a shopkeeper, bartender,
[00:04:41-00:04:44] and obviously, a lot of them work on the fields
[00:04:44-00:04:45] or in the forest.
[00:04:45-00:04:47] And in the evening, they go to have some fun,
[00:04:47-00:04:50] which in Bohemia is mostly drink beer.
[00:04:50-00:04:52] And then in the evening, they go home.
[00:04:52-00:04:54] They strip their clothes, put their clothes in their chest,
[00:04:54-00:04:57] and go to their bed where they sleep every night.
[00:04:57-00:05:00] So it's this rich, complex life the NPCs live.
[00:05:00-00:05:02] And they do it even without the player.
[00:05:02-00:05:03] The player could be on the other side, the opposite side,
[00:05:03-00:05:09] side of the map in a main quest doing something spectacular and the NPCs would still take
[00:05:09-00:05:15] off their clothes, put them in the chest next to their bed and go to sleep.
[00:05:15-00:05:25] Also while doing all this the NPCs are all reactive, they're not just charades.
[00:05:25-00:05:29] When they're doing all the things I described, you can walk up to them, you can punch them
[00:05:29-00:05:35] or maybe if you go to their home in the evening, they don't like it and they confront the player
[00:05:35-00:05:39] or when the player is maybe bloodstained or armed or scary, they can just run away, fetch
[00:05:39-00:05:43] the guard, something like that.
[00:05:43-00:05:51] This is going to be the big topic of today's talk, that's where side-sense comes in.
[00:05:51-00:05:59] And we have the last pillar, which is the consequences last, when the player does something
[00:05:59-00:06:04] bad and they leave a town, play some quest, do something else and they come back.
[00:06:05-00:06:12] The NPCs don't just forget, if something was stolen, they try to find it, if someone
[00:06:12-00:06:17] is missing, they also try to find the body, if they don't, the population gets angry and
[00:06:17-00:06:24] if they figure out that the player might have something to do with that, punishment awaits.
[00:06:24-00:06:26] And as you can see in the picture, that can be pretty harsh.
[00:06:26-00:06:32] We have some pretty game-over cutscenes for this.
[00:06:32-00:06:35] Finally, the site.
[00:06:35-00:06:37] We want the NPCs to be able to see.
[00:06:37-00:06:38] That's the basic.
[00:06:38-00:06:44] They should see each other, they should look at each other walking around the town, they
[00:06:44-00:06:47] should obviously be able to see the player.
[00:06:47-00:06:52] But they should watch them because the player is usually, maybe not in the town, but in
[00:06:52-00:06:57] the villages, they're the stranger, they're the unknown entity, so they should really
[00:06:57-00:07:05] look at the player, but it should not be creepy, like owls staring at you.
[00:07:05-00:07:10] They should be able to detect when the player is doing something that's suspicious or weird,
[00:07:10-00:07:13] sometimes it can be just something silly, when the player is throwing stones around
[00:07:13-00:07:20] a public square, they will comment on it, but if they maybe, I don't know, are throwing
[00:07:20-00:07:27] stones around an enemy encampment, then they would maybe not have fun with it, but go investigate.
[00:07:27-00:07:32] And we're getting to the last point, which basically contradicts all the previous ones.
[00:07:32-00:07:34] There should be some stealth gameplay available.
[00:07:34-00:07:38] It means the NPCs shouldn't be able to see the player right away, and the player should
[00:07:38-00:07:40] be able to.
[00:07:40-00:07:44] Sneak past them.
[00:07:44-00:07:51] Going down on this, we have this town of Gutenberg, as I mentioned already, and it's huge.
[00:07:51-00:07:55] And the NPCs are walking around, the players are walking around, they can be even riding
[00:07:55-00:08:00] on their horse, so if we want the NPCs to be able to watch the player and notice when
[00:08:00-00:08:05] they're doing something weird, it needs to be really fast.
[00:08:05-00:08:11] But we have this stealth gameplay, which can take place in different locations, it could
[00:08:11-00:08:14] be an enemy camp, such as this one.
[00:08:14-00:08:16] A really small one.
[00:08:16-00:08:21] Or a huge one, such as this one, which is a king Sigismund's army.
[00:08:21-00:08:26] Which is not entirely hostile, but the player needs to do a quest thing to get in there,
[00:08:26-00:08:30] and then some areas are forbidden.
[00:08:30-00:08:33] It's a very complex place.
[00:08:33-00:08:45] So in those two, or in such locations, the fight needs to be really slow.
[00:08:45-00:08:46] And that's this.
[00:08:46-00:08:50] You have those two opposing demands.
[00:08:50-00:09:02] Which I'll describe how we try to solve.
[00:09:02-00:09:04] What can the NPCs see?
[00:09:04-00:09:06] Obviously, the player.
[00:09:06-00:09:10] They can see each other.
[00:09:10-00:09:14] They do this mostly to greet each other.
[00:09:14-00:09:16] They can see stuff lying around.
[00:09:16-00:09:23] We call this stuff items, that could be mostly weapons, food, some herbs or potions, but
[00:09:23-00:09:26] they don't really need to see everything that's placed around the world, because it's an open
[00:09:26-00:09:30] world map, it's huge, there's stuff.
[00:09:30-00:09:31] All around.
[00:09:31-00:09:35] They don't need to see that, they mostly just see things that the player dropped, or maybe
[00:09:35-00:09:36] other NPCs dropped.
[00:09:36-00:09:39] When they're in combat, they lose, they drop their weapon, run away.
[00:09:39-00:09:42] Other NPCs can come and pick it up.
[00:09:42-00:09:48] And sometimes they keep it, and if it's clothing, they can wear it.
[00:09:48-00:09:51] We have a pretty unique thing, I would say.
[00:09:51-00:09:55] That our NPCs are able to see something that's not visible.
[00:09:55-00:10:00] And the mechanism we've used for that, we call perceptible volumes.
[00:10:00-00:10:01] Couple examples.
[00:10:01-00:10:02] Say, you are invisible.
[00:10:02-00:10:07] Say, you are in this store, and you like this hat, but as a player, you don't have money
[00:10:07-00:10:12] for it, or you don't want to pay, so maybe you wait until the shopkeeper turns around,
[00:10:12-00:10:17] and you just steal it.
[00:10:17-00:10:22] And when the shopkeeper turns back, they should be able to notice that something is missing.
[00:10:22-00:10:24] But it's hard to see something that's not there.
[00:10:24-00:10:31] So instead, we place such a thing, again, we call this volume.
[00:10:31-00:10:32] It's a cylinder.
[00:10:32-00:10:36] Originally, we planned to have maybe different shapes, but we found out we don't really need
[00:10:36-00:10:38] any other shape than a cylinder.
[00:10:38-00:10:39] The shape doesn't really matter.
[00:10:39-00:10:46] What matters are those tiny balls, the pink ones, and those are raycast points for the
[00:10:46-00:10:47] sight of the NPCs.
[00:10:47-00:10:51] So instead of the hat that they previously maybe could see or couldn't, depends on the
[00:10:51-00:10:56] setting, they can now see this, and they turn around and immediately see that something
[00:10:56-00:10:57] is missing.
[00:10:57-00:10:59] Another example.
[00:10:59-00:11:01] We have chicken in the game.
[00:11:01-00:11:02] And...
[00:11:02-00:11:08] A feature, or maybe just an easter egg we carried over from the first game, is when
[00:11:08-00:11:13] you punch them, or just harm the chicken, they explode in a bunch of feathers.
[00:11:13-00:11:15] And that's something very fast.
[00:11:15-00:11:22] And obviously, the NPCs want their chicken, they feed them, they plug them, they have
[00:11:22-00:11:25] their daytime routines, they don't want the player to harm the chicken.
[00:11:25-00:11:32] So if something like that happens, we also place short-lived perception volume instead
[00:11:32-00:11:40] of the chicken, so when the NPCs walk around, they see that the chicken has it.
[00:11:40-00:11:47] We use this for multiple other cases, but let's move on.
[00:11:47-00:11:53] We can see the player, and the NPCs can detect various, more detailed information on the
[00:11:53-00:11:54] player.
[00:11:54-00:11:55] We call it perception state.
[00:11:55-00:12:00] And here's an example, a little darker than I expected, it doesn't matter.
[00:12:00-00:12:05] The player is holding a crossbow, and the NPCs can see that the player is armed.
[00:12:05-00:12:07] The player is also wearing something that they have stolen.
[00:12:07-00:12:09] From the NPCs.
[00:12:09-00:12:14] And we don't know what it is, but the NPCs would know.
[00:12:14-00:12:19] They know, we remember the previous owner, and the NPCs would check it and see, is this
[00:12:19-00:12:23] mine, or does this belong to someone from my family, and if it does so, they can confront
[00:12:23-00:12:26] the player about it.
[00:12:26-00:12:31] The player is also crouching, so they can detect that on the player, and we cannot see
[00:12:31-00:12:35] that, but the player is also somewhere where they shouldn't be, so they have the perception
[00:12:35-00:12:36] state of trespass.
[00:12:40-00:12:50] We can ask the question, who is looking at what, in a, well, next question, who is looking
[00:12:50-00:12:51] at what?
[00:12:51-00:12:58] We, early on, we set this limit of each NPC looking only at a single perception target,
[00:12:58-00:13:01] because we are afraid of the performance hits of the raycasts.
[00:13:01-00:13:11] And this made the question, what to look at, critical, and I'm going to show you the formula
[00:13:11-00:13:12] that we devised.
[00:13:12-00:13:19] I'm not going to go through all of the terms, but we're going to also, we're going to see
[00:13:19-00:13:23] later in some more specific examples.
[00:13:23-00:13:29] But, going from the top, we have like a weight and a term, always, and some of the terms
[00:13:29-00:13:35] contain more formulas, so it's formulas inside of formulas, and this is the core of our RPG
[00:13:35-00:13:36] system.
[00:13:36-00:13:41] Just one example of, at the end, we see crime priority.
[00:13:41-00:13:42] And that's one of those formulas.
[00:13:42-00:13:45] It's a lot of formulas, hidden in formulas.
[00:13:45-00:13:49] And now we're going to, we're coming to the first major takeaway.
[00:13:49-00:13:56] We've written this formula about, I don't know, 10 years ago, 12 years ago on paper,
[00:13:56-00:13:57] and it looked great.
[00:13:57-00:14:03] It's going to model so many things in the realistic open world.
[00:14:03-00:14:04] And we just never made it work.
[00:14:04-00:14:07] It just, we could never tune it.
[00:14:07-00:14:11] So, the first key takeaway is too much complexity early on.
[00:14:11-00:14:12] It's best to start early.
[00:14:12-00:14:22] useless and it was harmful. You can also ask this question in a more
[00:14:22-00:14:27] technical way who's looking at what and again I'm touching the topic of my
[00:14:27-00:14:34] colleagues yesterday's talk and also something that's been mentioned here
[00:14:34-00:14:38] multiple times so we've seen AI LODs previously I'm not going to spend too
[00:14:38-00:14:45] much time on it but I'm just going to explain how it works in case of sight.
[00:14:45-00:14:51] All the systems such as it's described they work for the NPCs that are about
[00:14:51-00:15:00] 70 or 100 meters away. Then they switch to middle LOD where they still can see
[00:15:00-00:15:05] but they cannot see each other. NPCs at least friendly NPCs seeing each other is
[00:15:05-00:15:09] mostly used in our game for them to greet each other so if the player can't
[00:15:09-00:15:14] see them they're somewhere hidden it doesn't make sense for them to really do
[00:15:14-00:15:15] this.
[00:15:15-00:15:20] And for the NPCs that are in the most distant LOD they don't even see.
[00:15:20-00:15:26] The only thing that they need to notice is that body and for that we have a
[00:15:26-00:15:31] custom mechanism that switches them to the middle LOD so they can deal with the
[00:15:31-00:15:40] situation better. Here's just an illustration of how the LODs could be
[00:15:40-00:15:47] distributed in the game. We're looking at Suhdol Castle and we can see some green
[00:15:47-00:15:48] cones above the LOD.
[00:15:48-00:15:56] The green ones are in the close LOD the yellow ones in the village back there are in the
[00:15:56-00:16:02] middle LOD and since we are looking at the border of the map and this is also the less
[00:16:02-00:16:09] densely populated map of Trosetsko there are no NPCs in far LOD.
[00:16:09-00:16:16] But if we go to Gutenberg climb the church tower and look down we can see that we can
[00:16:16-00:16:17] see only a couple of green NPCs.
[00:16:17-00:16:18] So like.
[00:16:18-00:16:19] Close NPCs.
[00:16:19-00:16:31] All of the ones in the middle LOD and obviously most of them are in the far LOD.
[00:16:31-00:16:39] Now for the challenges and these are basically going to be stories from development and obviously
[00:16:39-00:16:46] not all the problems we faced just a selection of the ones that I find more interesting.
[00:16:46-00:16:51] The first one is that this is a really asymmetrical problem.
[00:16:51-00:16:55] The NPCs see in a very different way than the player does.
[00:16:55-00:16:56] For the NPCs.
[00:16:56-00:17:02] It's this logical symbolic world of simplified geometry, raycasts and I don't know what.
[00:17:02-00:17:10] Whereas for the player it's a rich graphical visual experience.
[00:17:10-00:17:16] I don't know how many of you noticed that but there's an NPC standing in the screenshot.
[00:17:16-00:17:20] Right here.
[00:17:20-00:17:24] And even though it's hard for us to tell the NPC can see the player.
[00:17:24-00:17:27] And since a lot of our games are based on the NPCs.
[00:17:27-00:17:29] And since a lot of our game is covered with forests.
[00:17:29-00:17:33] There's a lot of gameplay in forests, a lot of side quests.
[00:17:33-00:17:36] Enemy camps as we've seen before.
[00:17:36-00:17:37] This is a big problem.
[00:17:37-00:17:41] Like being able to detect NPCs in the forest.
[00:17:41-00:17:46] They also mostly wear brown, grey, dark clothes.
[00:17:46-00:17:49] And we have a couple of solutions for this problem.
[00:17:49-00:17:51] The first was.
[00:17:51-00:17:55] We had our extreme case of this problem was enemy dogs.
[00:17:55-00:17:57] They're also greyish.
[00:17:57-00:17:58] Darkish.
[00:17:58-00:18:01] Some dog color.
[00:18:01-00:18:04] I assume that dogs generally have better senses than humans.
[00:18:04-00:18:06] So their RPG was even stronger.
[00:18:06-00:18:08] They could see even further than the people.
[00:18:08-00:18:10] But they are so much smaller.
[00:18:10-00:18:14] And they usually would hide in the underbrush behind some stones or something.
[00:18:14-00:18:18] So we solved this problem by just removing NPC dogs from forests.
[00:18:18-00:18:26] Now for some more complex solutions.
[00:18:26-00:18:29] And this is something we call it recognition time.
[00:18:29-00:18:30] But it's really nothing unique.
[00:18:31-00:18:35] Most games with some stealth gameplay do use this.
[00:18:35-00:18:40] In our case, the NPC starts looking at the player.
[00:18:40-00:18:41] What that means.
[00:18:41-00:18:43] They have successful raycasts.
[00:18:43-00:18:49] And they need to do this for a while before they actually see the player.
[00:18:49-00:18:52] And that's really unrealistic.
[00:18:52-00:18:56] But we'll go deeper into that later.
[00:18:56-00:18:57] We can...
[00:18:57-00:18:59] Or the player can...
[00:18:59-00:19:00] They have some impact on this time.
[00:19:00-00:19:02] Or how long it is.
[00:19:02-00:19:03] By what they wear.
[00:19:03-00:19:05] How they move around.
[00:19:05-00:19:11] And of course, based on their RPG skills, perks, all of this.
[00:19:11-00:19:18] The description for the example.
[00:19:18-00:19:22] We have another...
[00:19:22-00:19:26] We brought another solution to this asymmetrical problem.
[00:19:26-00:19:33] That the vision cone, which is also a pretty common thing to use inside.
[00:19:33-00:19:35] We split it into two sectors.
[00:19:35-00:19:36] The closer one.
[00:19:36-00:19:38] And the further one.
[00:19:38-00:19:42] And the NPCs actually really see only in the closer sector.
[00:19:42-00:19:47] When they detect the player after the recognition time in the further sector.
[00:19:47-00:19:51] They start playing some animations.
[00:19:51-00:19:52] They look around.
[00:19:52-00:19:53] What's going on there.
[00:19:53-00:19:54] They say something.
[00:19:54-00:19:57] And if they can, they try to get closer.
[00:19:57-00:20:01] But not every NPC can do that.
[00:20:01-00:20:02] Maybe they're a guard.
[00:20:02-00:20:03] Standing on duty.
[00:20:03-00:20:05] So they just play an animation.
[00:20:05-00:20:09] And we thought this is going to help.
[00:20:09-00:20:12] But it's just the same problem over again.
[00:20:12-00:20:16] If you can't see the NPC, you can't see that they're playing an animation.
[00:20:16-00:20:21] So this didn't really help us.
[00:20:21-00:20:24] So we brought one more solution.
[00:20:24-00:20:26] And this was a tough one.
[00:20:26-00:20:30] We introduced a heads-up display icon.
[00:20:30-00:20:33] Is this bunny below the compass?
[00:20:33-00:20:35] You might have already seen it.
[00:20:35-00:20:38] And even though it's very popular now.
[00:20:38-00:20:39] And it's cute.
[00:20:39-00:20:43] We had a lot of trouble with this.
[00:20:43-00:20:46] It's inspired from similar icons we had in the first game.
[00:20:46-00:20:48] We had those combat icons.
[00:20:48-00:20:49] Either yellow swords.
[00:20:49-00:20:51] Which meant active combat.
[00:20:51-00:20:52] You are fighting with someone.
[00:20:52-00:20:56] Or silver swords.
[00:20:56-00:20:58] Which were further away from each other.
[00:20:58-00:21:00] That meant you are in combat danger.
[00:21:00-00:21:01] Someone is chasing you.
[00:21:01-00:21:02] Something like that.
[00:21:02-00:21:04] So that worked.
[00:21:04-00:21:06] We added seven more icons.
[00:21:07-00:21:10] And I'm not going to go through all of them.
[00:21:10-00:21:14] Partly because I don't really remember how they work.
[00:21:14-00:21:22] But the most two important ones right now are this detection.
[00:21:22-00:21:27] Basically when the NPCs are waiting, doing their active raycasts.
[00:21:27-00:21:29] The recognition time is being spent.
[00:21:29-00:21:32] The ears of the bunny rise.
[00:21:32-00:21:37] It may be strange that we use ears to represent sight.
[00:21:37-00:21:42] But that's the decision we made.
[00:21:42-00:21:44] When the ears rise.
[00:21:44-00:21:47] We show this detected icon.
[00:21:47-00:21:50] Which really should shock the player.
[00:21:50-00:21:52] And let them know something is going on.
[00:21:52-00:21:59] You have a problem.
[00:21:59-00:22:03] And the problem with the development of this icon is.
[00:22:03-00:22:09] We kind of knew we might need it.
[00:22:09-00:22:10] We saw it in the pre-production.
[00:22:10-00:22:11] Okay.
[00:22:11-00:22:12] We added.
[00:22:12-00:22:15] And then we added it way too late.
[00:22:15-00:22:21] And we didn't even know what we actually wanted.
[00:22:21-00:22:23] At first we said this Skyrim eye.
[00:22:23-00:22:25] That was the inspiration.
[00:22:25-00:22:31] But then we tried to represent the complex rich world of crime.
[00:22:31-00:22:34] That we implemented in the game.
[00:22:34-00:22:35] I touched it previously.
[00:22:35-00:22:38] But maybe the NPC is confronting the player.
[00:22:38-00:22:41] They are throwing them out of their place.
[00:22:41-00:22:42] Maybe it's a guard.
[00:22:42-00:22:44] It's a guard who wants to arrest the player.
[00:22:44-00:22:46] Maybe the NPC is running away.
[00:22:46-00:22:48] Reporting a crime.
[00:22:48-00:22:53] We used those bunnies to show all of this information.
[00:22:53-00:22:56] And we just couldn't figure out how to do it.
[00:22:56-00:22:58] So the players understand it.
[00:22:58-00:23:02] So we worked on it very intensely.
[00:23:02-00:23:04] For about six months.
[00:23:04-00:23:06] Everyone was very unhappy.
[00:23:06-00:23:09] And basically it was done when no one had any energy left.
[00:23:09-00:23:13] To push for more changes.
[00:23:13-00:23:16] But yes.
[00:23:16-00:23:23] But we mostly managed to do what we wanted to.
[00:23:23-00:23:26] And it really helps the gameplay.
[00:23:26-00:23:31] But to better explain why we didn't want to do it.
[00:23:31-00:23:34] Why we kept waiting to add the icon.
[00:23:34-00:23:37] Is we didn't fit the game.
[00:23:37-00:23:39] I'm repeating myself.
[00:23:39-00:23:42] But we are trying to do this immersive realistic game.
[00:23:43-00:23:47] And immersive realistic is not like hat icons.
[00:23:47-00:23:49] And icons everywhere.
[00:23:49-00:23:50] And I don't know.
[00:23:50-00:23:52] It feels like cheating.
[00:23:52-00:23:57] Like the player knows something that's taking place in the NPC's heads.
[00:23:57-00:23:59] And how can they know this?
[00:23:59-00:24:03] But in the end.
[00:24:03-00:24:05] It was a great success.
[00:24:05-00:24:07] We sell a ton of merch.
[00:24:07-00:24:09] In those bunnies.
[00:24:11-00:24:13] And about 20 people got tattoos.
[00:24:13-00:24:14] Including me.
[00:24:14-00:24:21] For most of us it was I guess dealing with the trauma of those meetings.
[00:24:21-00:24:24] I'm not going to show the pictures of the tattoos.
[00:24:24-00:24:26] Because I think they're usually disgusting.
[00:24:26-00:24:30] But we did it in the big meeting room.
[00:24:30-00:24:32] We invited some tattoo friends.
[00:24:32-00:24:36] And they did it right there.
[00:24:36-00:24:40] And we had some pizza.
[00:24:40-00:24:41] It was nice.
[00:24:41-00:24:43] But to close this chapter.
[00:24:43-00:24:46] Do not wait to add key gameplay elements.
[00:24:46-00:24:48] It really did not pay off for us.
[00:24:48-00:24:56] Coming back to the recognition time.
[00:24:56-00:24:59] And again.
[00:24:59-00:25:01] The game being realistic and immersive.
[00:25:01-00:25:03] It just looks dumb.
[00:25:03-00:25:05] It's not realistic.
[00:25:05-00:25:07] If you look at the screenshot.
[00:25:07-00:25:09] This is from the third person's view.
[00:25:09-00:25:11] Which is not available to the players.
[00:25:11-00:25:13] But it's available for us developers.
[00:25:13-00:25:15] The player is right there in the dark clothes.
[00:25:15-00:25:18] And there's the NPCs looking at them.
[00:25:18-00:25:20] And in such a situation.
[00:25:20-00:25:22] You're just like face to face.
[00:25:22-00:25:24] And the NPC takes some time to detect the person.
[00:25:24-00:25:25] And he's like...
[00:25:26-00:25:27] Just...
[00:25:27-00:25:28] It's off.
[00:25:28-00:25:30] It's not right.
[00:25:31-00:25:34] And we tried to tune the system.
[00:25:34-00:25:36] For a really long time.
[00:25:36-00:25:38] Basically we had this long running theme.
[00:25:38-00:25:40] For the entire development.
[00:25:40-00:25:43] From production to even after development.
[00:25:43-00:25:45] We released the game in February.
[00:25:45-00:25:47] And only in about August.
[00:25:47-00:25:51] We stopped regular meetings of this crime and stealth theme.
[00:25:51-00:25:53] This was one of the biggest problems.
[00:25:53-00:25:57] of the biggest problems we were trying to solve. Like how to tune the side sense
[00:25:57-00:26:03] so it works in the cities when it needs to be really fast and also in the stealth.
[00:26:03-00:26:10] And eventually we introduced a stealth mode which you can see on the picture
[00:26:10-00:26:16] the player is crouching you just press C and you get a massive buff to stealth.
[00:26:16-00:26:27] Super simple. Didn't again didn't feel right it's not very realistic but the
[00:26:27-00:26:38] gameplay works. Another challenge we faced was or is
[00:26:38-00:26:43] tied to the limit that we said that every single NPC is only looking at a
[00:26:43-00:26:53] single target and that makes the NPC blind to everything else. Where it turned
[00:26:53-00:26:54] out to be a really big problem
[00:26:54-00:27:00] was in the behavior of a crime guarding a dead body so that no one like takes it
[00:27:00-00:27:05] brings it away or like harms it or anything but the guard actually failed
[00:27:05-00:27:09] to see the player doing something to the body even though there was a point of the
[00:27:09-00:27:21] behavior. Let's remind ourselves of the of the systems we used inside. So we have
[00:27:21-00:27:26] a corpse and there's an NPC and they have a boost to perception priority that's
[00:27:26-00:27:26] this
[00:27:26-00:27:34] formula again we have some weight age and some constant if the NPC is dead they
[00:27:34-00:27:41] get this amount of boost the player is carrying a sword so they have a
[00:27:41-00:27:46] perception state and see it here in the debug drill they're carrying a weapon
[00:27:46-00:27:52] and when the player has the corpse with the sword they create a
[00:27:52-00:27:59] perception volume and this all happens right in front of the NPC but they are
[00:27:59-00:28:03] still looking at the corpse so they can't see the player they cannot see the volume
[00:28:03-00:28:12] even though they should. How did we solve this? We added something we call
[00:28:12-00:28:19] perception ignoring and that means that after the NPC succeeds in seeing
[00:28:19-00:28:24] something they ignore it for a while and they try to look at other things so
[00:28:24-00:28:31] again in this example well we'll come back to the example soon but this
[00:28:31-00:28:39] is a look at Kuttenberg the town market without the person ignoring we see the
[00:28:39-00:28:44] bug draw of the green and blue arrows and that basically shows us which NPC
[00:28:44-00:28:48] is looking at what. And basically everyone is looking at the one right in
[00:28:48-00:28:55] front of them. And if you add this ignoring system we see that actually no
[00:28:55-00:28:58] one is looking at anybody because they looked at each other they found out they
[00:28:58-00:29:01] have nothing to do with them and they just ignore them.
[00:29:01-00:29:07] Way more realistic at least in Prague. Coming back to the example now, the the NPC is an invisible creature.
[00:29:07-00:29:10] the
[00:29:10-00:29:13] NPC looks at the corpse that they're guarding
[00:29:13-00:29:15] and because they have nothing to do with it
[00:29:15-00:29:16] they start ignoring it
[00:29:16-00:29:18] and they can see the player
[00:29:18-00:29:21] arriving with the sword
[00:29:21-00:29:23] and when the player
[00:29:23-00:29:25] hits the corpse they can see
[00:29:25-00:29:26] the volume and they can react
[00:29:26-00:29:29] and we have even one slight improvement
[00:29:29-00:29:30] if the player approaches the
[00:29:30-00:29:32] NPC with their
[00:29:32-00:29:34] sword or weapon cheated
[00:29:34-00:29:37] and they are ignored
[00:29:37-00:29:38] when they remove
[00:29:38-00:29:40] or uncheathe the sword, the weapon
[00:29:40-00:29:42] this cancels the ignoring
[00:29:42-00:29:45] so the NPC can
[00:29:45-00:29:46] notice when the player does something
[00:29:46-00:29:47] like that
[00:29:47-00:29:50] and now to
[00:29:50-00:29:53] the secret of this story
[00:29:53-00:29:55] this isn't
[00:29:55-00:29:57] a new solution, we already had this in the
[00:29:57-00:29:58] first game and for the development
[00:29:58-00:30:00] of the second game we removed it
[00:30:00-00:30:03] because we didn't like it, we thought that's weird
[00:30:03-00:30:05] we have this system and we
[00:30:05-00:30:06] just break it by doing this
[00:30:06-00:30:09] and
[00:30:09-00:30:11] for a couple of years we tried to find
[00:30:11-00:30:12] other solutions
[00:30:12-00:30:13] a different solution to this
[00:30:13-00:30:15] and we just couldn't
[00:30:15-00:30:17] so we
[00:30:17-00:30:21] sit back
[00:30:21-00:30:23] another big challenge that we faced
[00:30:23-00:30:24] is something called
[00:30:24-00:30:26] what I call mayhem and we could
[00:30:26-00:30:31] do a massive performance optimization talk on this but
[00:30:31-00:30:33] for now I'm just going to focus on
[00:30:33-00:30:35] how it touches the topic at hand
[00:30:35-00:30:36] in a slight sense
[00:30:36-00:30:39] basically the
[00:30:39-00:30:40] the scenario is
[00:30:40-00:30:41] you go turn on the
[00:30:41-00:30:42] Kuttenberg map
[00:30:42-00:30:44] you walk up to someone and you punch them
[00:30:44-00:30:46] and all hell breaks loose
[00:30:46-00:30:48] women scream, they run away
[00:30:48-00:30:50] maybe someone carries a weapon
[00:30:50-00:30:52] so they try to solve it but you kill them because
[00:30:52-00:30:54] you're cheating and you have infinite
[00:30:54-00:30:56] health and then the guards
[00:30:56-00:30:58] start running around
[00:30:58-00:31:00] there's sort of
[00:31:00-00:31:02] chaos and the problem we faced
[00:31:02-00:31:04] inside was
[00:31:04-00:31:06] that women who couldn't fight
[00:31:06-00:31:09] in our game would just like walk right into the middle of the map
[00:31:09-00:31:11] into the middle of this fray
[00:31:11-00:31:13] and we thought okay maybe
[00:31:13-00:31:16] they don't have time to process their behavior tree
[00:31:16-00:31:17] before they
[00:31:17-00:31:19] see the fight they should maybe
[00:31:19-00:31:21] or they don't
[00:31:21-00:31:24] or they finish the movement before they start another movement
[00:31:24-00:31:26] and we met for
[00:31:26-00:31:27] a couple months again in a
[00:31:27-00:31:29] team of professionals and we brought a lot of
[00:31:29-00:31:31] performance updates
[00:31:31-00:31:34] to try to solve this timing problem
[00:31:34-00:31:36] but
[00:31:36-00:31:38] there wasn't a solution
[00:31:38-00:31:39] the solution was that in a release ban
[00:31:39-00:31:39] there wasn't a solution the solution was that in a release ban
[00:31:39-00:31:40] built
[00:31:40-00:31:43] the code was just not running
[00:31:43-00:31:45] so when we found out
[00:31:45-00:31:47] then this fix was easy
[00:31:47-00:31:52] so that's another takeaway
[00:31:52-00:31:54] the solution might not lie
[00:31:54-00:32:00] on the path you walk
[00:32:00-00:32:02] I'd like to describe a couple
[00:32:02-00:32:06] unsolved problems we've faced
[00:32:06-00:32:08] and one is again with the cones
[00:32:08-00:32:10] I hope you can see them
[00:32:10-00:32:12] when I described them first
[00:32:12-00:32:14] I already said that they didn't
[00:32:14-00:32:16] work quite right
[00:32:16-00:32:18] they didn't help us as much as we hoped
[00:32:19-00:32:21] and
[00:32:21-00:32:23] we originally tried to solve them by
[00:32:23-00:32:25] making it more complex as we do
[00:32:25-00:32:27] so we tried to move the border
[00:32:27-00:32:29] of what's the closer sector
[00:32:29-00:32:31] and the further sector by
[00:32:31-00:32:33] analyzing
[00:32:33-00:32:35] the situation of the NPC
[00:32:35-00:32:37] maybe they heard a rustle in the bush
[00:32:37-00:32:39] somewhere or maybe
[00:32:39-00:32:41] one of their friends is missing
[00:32:41-00:32:43] so they should be more alert
[00:32:43-00:32:45] and this border moves but
[00:32:45-00:32:47] it was super not transparent
[00:32:47-00:32:49] for the player it was really annoying
[00:32:49-00:32:51] you were trying to play
[00:32:51-00:32:53] sneak around
[00:32:53-00:32:55] and you just had no idea when the NPCs
[00:32:55-00:32:57] can and cannot see you
[00:32:57-00:32:59] so we just removed it
[00:32:59-00:33:01] and my favorite
[00:33:01-00:33:03] is bushes
[00:33:03-00:33:05] in the first game we obviously had bushes
[00:33:05-00:33:07] and
[00:33:07-00:33:09] they are basically made of concrete
[00:33:09-00:33:11] you couldn't enter them
[00:33:11-00:33:13] so we made them
[00:33:13-00:33:15] walkable now
[00:33:15-00:33:17] and we said okay we want the player to be able
[00:33:17-00:33:19] to hide in the bushes
[00:33:19-00:33:21] and
[00:33:21-00:33:23] with the experience of all of those complex
[00:33:23-00:33:25] systems from the first game
[00:33:25-00:33:27] we tried to make it really simple
[00:33:27-00:33:29] simple means
[00:33:29-00:33:31] it's going to work no problems
[00:33:31-00:33:33] right
[00:33:33-00:33:35] well
[00:33:35-00:33:37] the first problem was a torch
[00:33:37-00:33:39] a bush in a torch is
[00:33:39-00:33:41] for some people fire in a torch
[00:33:41-00:33:43] sorry fire in a bush
[00:33:43-00:33:45] is a good sign but for us
[00:33:45-00:33:47] it wasn't so much
[00:33:47-00:33:49] you can see the player standing
[00:33:49-00:33:51] in the bush with the torch
[00:33:51-00:33:53] and then on the right you can see the
[00:33:53-00:33:55] physical colliders and
[00:33:55-00:33:57] the bush the torch is just sticking
[00:33:57-00:33:59] around out of it but the player is
[00:33:59-00:34:01] still invisible and even if
[00:34:01-00:34:03] the torch was inside
[00:34:03-00:34:05] it would be really weird for
[00:34:05-00:34:07] the NPCs to be
[00:34:07-00:34:09] not able to detect a fire inside
[00:34:09-00:34:11] of a bush but
[00:34:11-00:34:13] they are not it just works like this
[00:34:13-00:34:15] another
[00:34:15-00:34:17] problem is based on the
[00:34:17-00:34:19] implementation of the raycast
[00:34:19-00:34:21] you can see from one bush to
[00:34:21-00:34:23] another bush
[00:34:23-00:34:25] it's basically coming down to
[00:34:25-00:34:27] the physics in CryEngine being pretty
[00:34:27-00:34:29] wild and the code that I
[00:34:29-00:34:31] wrote to deal with this is just
[00:34:31-00:34:33] a mess and I didn't want to fix it
[00:34:33-00:34:35] so
[00:34:35-00:34:37] beware of NPCs or if you're
[00:34:37-00:34:39] trying if you're playing the game and you're sneaking
[00:34:39-00:34:41] in bushes beware of NPCs that walk also
[00:34:41-00:34:43] to the bush because they can see you
[00:34:43-00:34:48] but otherwise you're invisible
[00:34:48-00:34:50] anyway we even with
[00:34:50-00:34:52] those issues we decided to keep the
[00:34:52-00:34:54] bushes because we really thought
[00:34:54-00:34:56] it helps the gameplay a lot
[00:34:56-00:34:58] you can try it
[00:34:58-00:35:02] when you buy the DLC to conclude
[00:35:02-00:35:04] we
[00:35:04-00:35:06] had this system offsite from the first game
[00:35:06-00:35:08] it was really complex and we
[00:35:08-00:35:10] liked it mostly
[00:35:10-00:35:12] but still we wanted to
[00:35:12-00:35:14] we tried to improve it and we did manage to improve it
[00:35:14-00:35:16] in some ways we failed to
[00:35:16-00:35:18] improve it in other ways but
[00:35:18-00:35:20] the biggest help we did I think is we
[00:35:20-00:35:22] finally managed to tune it all the parameters
[00:35:22-00:35:24] the formula I showed you is just
[00:35:24-00:35:26] one of many and for the
[00:35:26-00:35:28] second game we managed to tune it so
[00:35:28-00:35:30] it works more or less
[00:35:30-00:35:36] to our satisfaction and
[00:35:36-00:35:38] basically what I'm coming to the entire
[00:35:38-00:35:40] talk try to avoid one
[00:35:40-00:35:42] system for many use cases
[00:35:42-00:35:44] it's just a huge pile of work
[00:35:44-00:35:48] to remind
[00:35:48-00:35:50] you of the
[00:35:50-00:35:52] key takeaways I've listed
[00:35:52-00:35:54] over the entire
[00:35:54-00:35:56] talk too much
[00:35:56-00:35:58] complexity early on is at best useless
[00:35:58-00:36:00] and at worst harmful
[00:36:00-00:36:02] do not wait to add key gameplay
[00:36:02-00:36:04] elements
[00:36:04-00:36:06] solution might not lie on the path you walk
[00:36:06-00:36:08] and avoid one system
[00:36:08-00:36:10] for many use cases
[00:36:10-00:36:12] this might be they might seem obvious
[00:36:12-00:36:14] or simple or too generic
[00:36:14-00:36:16] but
[00:36:16-00:36:18] we really had to relearn
[00:36:18-00:36:22] them the hard way I would like to thank
[00:36:22-00:36:24] the team that was running on
[00:36:24-00:36:26] working on this for basically
[00:36:26-00:36:28] the entire development of the game is offset
[00:36:28-00:36:30] and I would mostly like to highlight the role
[00:36:30-00:36:32] of QA it was many definitions
[00:36:32-00:36:34] based on feel
[00:36:34-00:36:36] or how you wanted
[00:36:36-00:36:38] the game to play and their
[00:36:38-00:36:40] input was really super valuable
[00:36:40-00:36:42] because they were the ones playing it
[00:36:42-00:36:44] day after day after day
[00:36:44-00:36:46] and they brought the issues that this feels
[00:36:46-00:36:48] off this doesn't seem right we should
[00:36:48-00:36:50] maybe change this retune this
[00:36:50-00:36:52] and that's all
[00:36:52-00:36:54] from me thank you and I'll be happy
[00:36:54-00:36:56] to answer any questions
