---
title: "Indie Game Clinic|游戏机制与系统思维——Game Mechanics & Systems Thinking"
platform: bilibili
bvid: BV1fhpt6NEi3
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-10-09 14:36:31
duration_sec: 5002
view: 1054
like: 41
coin: 4
favorite: 143
reply: 3
danmaku: 0
share: 9
url: https://www.bilibili.com/video/BV1fhpt6NEi3
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 46902
crawl_time: 2026-11-08 21:20:02


# Indie Game Clinic|游戏机制与系统思维——Game Mechanics & Systems Thinking

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-10-09 14:36:31
- **时长**: 1小时23分22秒
- **播放**: 1054 | 赞: 41 | 币: 4 | 藏: 143
- **链接**: https://www.bilibili.com/video/BV1fhpt6NEi3

## 视频描述

原视频：https://www.youtube.com/watch?v=nkLmjJK3vOw
（2026年1月30日）Joe Baxter Webb 将游戏机制定义为玩家能够执行的交互性动作，并探讨了游戏机制与底层规则及系统之间的区别。本次演讲倡导采用系统化的设计方法，强调设计者应着眼于为玩家创造特定的情感体验，而不应仅仅追求对现实的逼真模拟。

⏱️ 时间戳：
00:00 引言
00:52 规

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1fhpt6NEi3
# 语言=en 时长=00:40:48 模型=large-v3

[00:00:00-00:00:05] Most people who make games and even those who play games if they talk a lot about games and
[00:00:05-00:00:10] how they're designed have some sort of understanding of what we mean by game mechanics.
[00:00:10-00:00:16] When we talk about a game's mechanics we're talking about how it works, how the gameplay
[00:00:16-00:00:21] is produced by the game. I'm Joe Baxter-Webb. In this video I'm going to define game mechanics,
[00:00:22-00:00:27] talk about the usefulness of game mechanics as a concept. I'm just going to be telling you how I
[00:00:27-00:00:33] personally think about them and that may be useful to you if you are making games. Now this video is
[00:00:33-00:00:38] going to get a bit philosophical in places and it's probably going to be longer than some of my
[00:00:38-00:00:44] other videos so you know watch it in multiple sittings or speed it up whatever you need to do
[00:00:44-00:00:48] to get through it just don't tell me in the comments like this person did because that's
[00:00:48-00:00:54] really weird. Why would you do that? Why? So to start with let's just define what game mechanics
[00:00:54-00:00:56] are. One of the issues that I often have
[00:00:56-00:00:57] when I'm making games is that I'm not sure if I'm going to be able to make a good game
[00:00:57-00:01:04] I look for definitions of mechanics is that they jumble up mechanics rules and systems so we're
[00:01:04-00:01:07] going to come up with a definition of game mechanics which disambiguates these things a
[00:01:07-00:01:15] little bit. Let's start with rules because rules are the underlying logic of a game. Any game has
[00:01:15-00:01:20] rules whether it's ice spy or soccer or chess a game is made up of rules. Now the thing that
[00:01:20-00:01:26] differentiates a video game from other types of games is that in a video game you could hide rules
[00:01:27-00:01:31] from the player. When you play a board game with someone else the players usually need to be
[00:01:31-00:01:36] cognizant of all of the rules unless there's like a games master behind a screen with their own set
[00:01:36-00:01:40] of rules that the players don't know about. A video game allows us to hide some of the rules
[00:01:40-00:01:46] from the player. The rules are all of the logic that make up the game. Any statement where you
[00:01:46-00:01:52] could say when this happens then this happens and if this happens then this happens is a rule. It's
[00:01:52-00:01:56] the stuff that you turn into code. When you sit down with an idea for a game
[00:01:57-00:02:01] you think when the player does this I want this to happen that's the logical rule and you're just
[00:02:01-00:02:07] converting it from human language into computer language and that's what programming is. Mechanics
[00:02:07-00:02:14] are made of rules. Rules are the raw material that mechanics are made up of but mechanics are more to
[00:02:14-00:02:19] do with producing gameplay itself. Mechanics are the game's interactions, the things that the player
[00:02:19-00:02:26] can do, the player actions and their goals. In game design theory we usually talk about them in terms
[00:02:27-00:02:34] of jumping, finding, avoiding or escaping. Those are verbs that are kind of more related to the goal of
[00:02:34-00:02:38] the player. They are things that the player can do. They're also things that the game can do to the
[00:02:38-00:02:43] player which kind of gets us to thinking well is everything a game mechanic then and really I would
[00:02:43-00:02:49] say the game mechanics are the tools that the players in the game use to act on the game world
[00:02:49-00:02:56] in some way. So if you imagine that your game has a game master and that game master that is in the
[00:02:57-00:03:01] game like a difficulty system or some sort of enemy AI or something it's like another player
[00:03:01-00:03:06] pushing back against the the player in the single player game. Both of those sides are using game
[00:03:06-00:03:13] mechanics. They're using their verbs like attack or collect to change the the simulation or the
[00:03:13-00:03:19] game world that they're operating in. Mechanics are made up of sets of rules. When you do this
[00:03:19-00:03:26] this happens. If you do this but this then this happens. But not all rules are necessary mechanics
[00:03:27-00:03:32] your game is going to contain other rules that don't really relate to gameplay per se. When we're
[00:03:32-00:03:38] thinking in game design terms mechanics are not about the code of the game or every part of the
[00:03:38-00:03:43] game they're just about the gameplay the the kind of interactive element of the game. A mechanic is
[00:03:43-00:03:48] going to be defined by the rules that make it up just like you or I are defined by our genetics or
[00:03:48-00:03:53] the cells in our body but the specifics of those rules are going to change the mechanic considerably
[00:03:57-00:04:01] in the game. In one game you're going to run into them and your character just steps on them and
[00:04:01-00:04:04] then you've got the coin and it plays a sound effect. You've collected the coin. In another
[00:04:04-00:04:11] game you might press a button to pick up a little bag. In a VR game you might use a totally different
[00:04:11-00:04:18] interface so that's an example of like the same player verb to collect things but at a lower level
[00:04:18-00:04:22] the rules that make up that player verb are different and that leads to a fundamentally
[00:04:22-00:04:26] different feeling in the game and it's more or less appropriate depending on what type of game
[00:04:27-00:04:31] you're thinking and what the kind of overall creative direction of that game is right like
[00:04:31-00:04:37] running into big floating coins in the environment is gonna feel weird if you do it in like a hard
[00:04:37-00:04:43] boiled detective game. A thing I'd like to emphasize here is that how mechanics feel is
[00:04:43-00:04:48] really fundamental to the character of a game. If it's a core interaction in the game if it's one
[00:04:48-00:04:53] of the main things the player is doing all the time like a jump or it could be just clicking
[00:04:53-00:04:56] on buttons in an interface in a very interface heavy game.
[00:04:57-00:05:02] If it's the main thing the player is doing over and over again then refining that thing it's
[00:05:02-00:05:08] integral to the game so don't treat that stuff as something superfluous because if you're making a
[00:05:08-00:05:14] game about jumping then locking in the final quality of the jumping very early on is probably
[00:05:14-00:05:19] quite important. Likewise if you're making a game that is all about interacting with interfaces or
[00:05:19-00:05:26] clicking through dialogue options in a story the feel of that is part of the mechanic it's part of
[00:05:26-00:05:27] the character of the game.
[00:05:27-00:05:33] And it's important to think about it early on subtle changes in a rule can change how a mechanic
[00:05:33-00:05:40] feels quite dramatically and this is why when you are early in prototyping a game you need to be
[00:05:40-00:05:44] open to like switching things and changing them you might have heard this quote from Sid Meier
[00:05:44-00:05:49] when you are testing a variable in a game double or halve it it's basically easier to see the
[00:05:49-00:05:54] difference that a change in the rules makes if you make larger adjustments when you're making small
[00:05:57-00:06:00] changes in a game than you're making small changes in a game.
[00:06:00-00:06:06] It's like prematurely fine-tuning something when you should actually be really cranking it in
[00:06:06-00:06:12] different directions to feel the change. A system is a larger set of rules it can contain mechanics
[00:06:12-00:06:18] the mechanics are usually how the player interacts with the system right so if we imagine a progression
[00:06:18-00:06:24] system in a game like the way that you collect resources in order to level up there are elements
[00:06:24-00:06:27] of that that are player mechanics like gathering
[00:06:27-00:06:33] XP or gathering some sort of resource is a thing the player can actively try to do opening the menu
[00:06:33-00:06:38] and looking at the system and seeing like the skill tree or whatever it is they're unlocking
[00:06:38-00:06:44] their progression through is a mechanic there's like an information-based mechanic there of the
[00:06:44-00:06:48] player can go and look at the thing and understand it and then there's also the activation mechanics
[00:06:48-00:06:53] of like what does the player do to actually spend the resources to unlock another thing and again
[00:06:53-00:06:57] you can think of all the variations of that like forcing a level
[00:06:57-00:07:01] up at a specific point in the game like survivors likes do where the game pauses and it's like now
[00:07:01-00:07:06] you must choose the next thing that's a different way of approaching the same mechanic which in
[00:07:06-00:07:13] another game might say oh you're ready to level up you can do it when you want right again it's
[00:07:13-00:07:17] going to be more or less appropriate depending on the game that you're doing it now when we talk
[00:07:17-00:07:21] about systems in games we're usually talking about a feature set like progression system
[00:07:21-00:07:27] like I just mentioned traversal system how does the player move around can they jump can they fly
[00:07:27-00:07:32] can they climb on walls but we also need to factor in all of the informational aspects of that as
[00:07:32-00:07:39] well because the way something is communicated is part of that system right so the the menu with the
[00:07:39-00:07:44] information about how you level up is part of the system like any interface is part of the system in
[00:07:44-00:07:50] a traversal system the way that you decorate a wall to let the player know that it is climbable that
[00:07:50-00:07:54] is part of the climbing mechanic and it's part of the traversal system another way to think about it
[00:07:57-00:08:03] if the game mechanics are the verbs what can be done in the game then the systems are usually
[00:08:03-00:08:09] there to provide the game objects or the nouns for the player to do those verbs to so the player
[00:08:09-00:08:16] attacks and defeats a wave of enemies right so attacking and defeating are mechanics you attack
[00:08:16-00:08:22] by doing particular button presses and and so on and you defeat by attacking with the degree
[00:08:22-00:08:26] of efficiency but the wave of enemies is a an object within the game or a system so that's what we're talking about
[00:08:27-00:08:32] a set of objects within the game that comes from a system and that system might be regularly spawning
[00:08:32-00:08:37] enemies in a wave based game or it could be the way that the levels are designed right because
[00:08:37-00:08:42] your level design approach within a game if it's set levels and it's not procedural that's still a
[00:08:42-00:08:47] system it's just more of a human authored system than a procedurally generated one the example I
[00:08:47-00:08:52] gave before the player unlocks an upgrade the player is doing something they are making a
[00:08:52-00:08:56] decision they're doing some interactions by giving inputs to the game and it is
[00:08:56-00:08:57] operating
[00:08:57-00:09:02] a system that exists within the game a practical thing here about the development of systems is
[00:09:02-00:09:07] that you probably don't need to build as much of them as you think you do early on we can usually
[00:09:07-00:09:14] prototype a game by just pretending the systems there or creating a sort of mock-up of it so if
[00:09:14-00:09:20] we're making a deck builder there are certain systems that we may not need early in development
[00:09:20-00:09:26] to do that first stage of prototyping we might not actually need the player to have a different deck
[00:09:26-00:09:27] every time we might not
[00:09:27-00:09:32] the scenarios or situations they're responding to with their cards to be different each time we have
[00:09:32-00:09:37] an idea of what the system will eventually be but we don't build it prematurely because we haven't
[00:09:37-00:09:42] actually felt what it would be like in action yet now that will be counter to some good programming
[00:09:42-00:09:47] practices and there's not an easy way out of that problem it really comes down to your own priorities
[00:09:47-00:09:53] and working out at any given moment whether the good engineering is more important or whether
[00:09:53-00:09:58] the finding the fun of the game is more important another example that we see all the time is people
[00:09:58-00:10:02] who know they want to make a roguelike with procedurally generated levels and they pour
[00:10:02-00:10:08] dozens or hundreds of hours into learning procedural generation algorithms and creating
[00:10:08-00:10:12] a level generator and they don't actually have a game yet they're creating systems before they know
[00:10:12-00:10:17] what the mechanics are which will interact with those systems usually that's quite foolish there's
[00:10:17-00:10:21] probably examples you can find of games which have been developed in that order where it worked out
[00:10:21-00:10:23] generally speaking if you're doing that
[00:10:23-00:10:23] you're not going to be able to make a roguelike with procedurally generated levels
[00:10:23-00:10:29] you're not really developing a game you are using game dev as a technical hobby and you're learning
[00:10:29-00:10:33] procedural generation algorithms and that's fine if that's what you want to do but it's not how
[00:10:33-00:10:39] you would develop a game a procedural generation system is part of the machine of a game which is
[00:10:39-00:10:44] meant to respond to the problem of how do we make levels if you don't have game mechanics you don't
[00:10:44-00:10:53] have a reason to have levels yet so again it's just about thinking about the the game as a as a
[00:10:53-00:12:06] such a
[00:12:06-00:12:06] video game
[00:12:07-00:12:08] that's good isn't it
[00:12:08-00:12:12] it's good that we can do that because humans are clever and stuff one of the issues with thinking
[00:12:12-00:12:18] of video games as machines is that it's easy to make the assumption that it's because video games
[00:12:18-00:12:26] are a technology but every game or really anything that you play has game mechanics board games have
[00:12:26-00:12:31] game mechanics tabletop role-playing games have game mechanics sports have game mechanics you can
[00:12:31-00:12:37] have verbal games like i spy and those have game mechanics so the machine metaphor is not really to
[00:12:37-00:12:41] do with the fact that video games are technology and that might seem obvious to some of you but to
[00:12:41-00:12:46] others it it might not be i don't know i don't know every single one of you and what's in your
[00:12:46-00:12:52] brain if i knew that i'll be a very wealthy man people use mechanics to talk about how something
[00:12:52-00:12:57] works like political analysts will talk about the mechanics of an economy or a government people
[00:12:57-00:13:04] talk about body mechanics if they work in sports science or medicine or other body stuff talking
[00:13:04-00:13:06] about something as if it's a machine
[00:13:06-00:13:13] and that's one of the reasons why we use it in game design it encourages you to think of the
[00:13:13-00:13:17] intended outcome now you can have a useless machine that doesn't have an intended outcome
[00:13:17-00:13:23] like a rube goldberg machine or the government i'm all right but most of the time machines are
[00:13:23-00:13:29] created to do a particular thing like a car engine produces forward motion and a coffee machine
[00:13:29-00:13:36] produces coffee so applying the same thinking to games we can say okay there's a thing that we want
[00:13:36-00:13:42] to get out of this which could be being scared if it's a horror game it could be feeling clever if
[00:13:42-00:13:48] it's a puzzle game it could be feeling excited and adrenaline and all of that stuff if it's an
[00:13:48-00:13:54] action game and then we need to think about which mechanics or mechanisms are likely to lead to an
[00:13:54-00:13:59] interaction that produces that outcome those of you who are already familiar with mda theory
[00:13:59-00:14:06] will know this this is what mda theory is about you have game mechanics they interact dynamically
[00:14:06-00:14:11] when the player actually plays with them the game exists as a piece of software but the play
[00:14:11-00:14:16] produced by the game doesn't exist until the player is doing it and then that leads to an
[00:14:16-00:14:23] aesthetic experience which means the player's emotional responses to the game now mda theory
[00:14:23-00:14:32] dates back to a paper from 2004 but the idea that a game is a machine that is meant to produce a
[00:14:32-00:14:35] emotional outcome is sort of inherent to
[00:14:36-00:14:42] anyone who's ever talked about game mechanics or game mechanisms a game mechanic is a unit of
[00:14:42-00:14:49] interactivity a piece of interactivity within a game and when game mechanics are combined they
[00:14:49-00:14:55] lead to specific outcomes and that is just like your coffee machine producing coffee the horror
[00:14:55-00:15:04] game produces fear the sports game produces excitement and fiero the feeling of like triumph
[00:15:04-00:15:06] when you beat an opponent and so on
[00:15:06-00:15:12] the problems that new developers often have as well is that because video games are multimedia
[00:15:12-00:15:20] it's hard to think about the gameplay as its own thing if you don't have this broader systemic view
[00:15:20-00:15:24] of like what type of engine are we trying to build and what type of experience is it supposed to
[00:15:24-00:15:29] produce you can fall into a lot of traps one of them is the realism trap oh we're going to make
[00:15:29-00:15:34] the jump this high because that's how high a human could jump that that doesn't have anything to do
[00:15:34-00:15:36] with making a player feel good or make a player feel good or make a player feel good or make a
[00:15:36-00:15:42] player feel like a particular type of character one of the reasons why i personally really like
[00:15:42-00:15:50] stylized less realistic games like blood thief is that the fun is driving everything else in the
[00:15:50-00:15:54] game all of the decisions about the art all of the decisions about how the interaction should
[00:15:54-00:16:00] work are driven by the fun and the particular fantasy of this being like a very fast like
[00:16:00-00:16:06] medieval ninja type scenario it's all based around what feels good mechanically and generally speaking
[00:16:06-00:16:07] it's all based around what feels good mechanically and generally speaking
[00:16:07-00:16:12] that's the practical way to make a fun game make a fun set of interactions and then build a game
[00:16:12-00:16:16] around it don't create a fictional world and then try to cram it with mechanics based on
[00:16:16-00:16:21] you know simulating a life in that world because you don't know that that's going to be satisfying
[00:16:21-00:16:26] to do rather you make a few mechanics that feel good and let the art style and the setting all
[00:16:26-00:16:31] coalesce around those mechanics one small personal bugbear i have with how we speak about game
[00:16:31-00:16:36] mechanics is that we often talk about them in isolation often when we talk about mechanics in
[00:16:36-00:16:42] video games we talk about a game mechanic like a single game mechanic which is kind of detracting
[00:16:42-00:16:48] from the usefulness of the metaphor you know like a screw or a bolt or a nut is not a machine just
[00:16:48-00:16:54] because we look at it and we can see that it's a machine part it only starts to gain the kind of
[00:16:54-00:16:59] usefulness or sense of purpose that we associate with a machine by being part of a machine you
[00:16:59-00:17:04] could take a steering wheel from a factory and say this is a car part but it doesn't really become
[00:17:06-00:17:12] this is all very like minute linguistic stuff but i think it's worth thinking about in the tabletop
[00:17:12-00:17:17] and board game space it's much more common to hear designers and players talk about mechanisms
[00:17:17-00:17:22] as the individual units of gameplay and then mechanics as like the whole mechanics of a game
[00:17:22-00:17:26] it's just something to think about because it will frame your thinking some of the most common
[00:17:26-00:17:31] things that we see that sort of lead to a bad game or a game that's not interesting copying
[00:17:31-00:17:36] mechanics and not really understanding how they work or the the role they play in the system they
[00:17:36-00:17:40] are in so you could take mechanics you like from different games and put them together and you
[00:17:40-00:17:44] might end up with something really good but you have to think about the role that the mechanic
[00:17:44-00:17:50] is playing in that particular system to think of a really dumb example you have lots of systems that
[00:17:50-00:17:55] are to do with progression in games like leveling up if you take loads of them and put them in the
[00:17:55-00:18:01] same game they're all sort of fighting for their role they're all trying to occupy the same space
[00:18:01-00:18:06] in the design and they don't all need to be there just taking mechanics or systems you like from
[00:18:06-00:18:06] other games
[00:18:07-00:18:11] and mashing them together doesn't work because you haven't thought about the role that they play
[00:18:11-00:18:15] in those games and the role that they're meant to play in your game another one that i see quite
[00:18:15-00:18:23] often is people taking mechanics from other games and changing one quite arbitrarily or because
[00:18:23-00:18:27] they find it restrictive or they don't like it in the original game but they haven't really
[00:18:27-00:18:32] understood the function that it performs so one that i've seen a few times here
[00:18:32-00:18:36] would be the deck builder where you don't discard your hand
[00:18:36-00:18:42] at the end of the round now it's probably totally possible to make that design work but most of the
[00:18:42-00:18:48] cases where i've seen it implemented it seemed more like the designer didn't understand why it's
[00:18:48-00:18:53] necessary for the player to discard their hand at the end of their turn in most deck builders the
[00:18:53-00:18:59] game really depends on you getting through all of your cards very quickly one set of five cards on
[00:18:59-00:19:03] one turn and a different set of five cards on one turn and then a different set of five cards and
[00:19:03-00:19:05] then you've exhausted your deck and now all of a sudden you've exhausted your deck and now all of a
[00:19:05-00:19:10] the same cards come around but in different configurations again and then in six turns
[00:19:10-00:19:14] you've been through your deck twice and each time you've been through your deck it comes out
[00:19:14-00:19:19] in a different order. If you don't discard your hand at the end of the turn then the rest of that
[00:19:19-00:19:22] system falls apart this is kind of how genres work
[00:19:22-00:19:55] CHARACTERику
[00:19:55-00:20:01] a pre-packaged set of mechanics that we already know work together and that we know that a certain
[00:20:01-00:20:06] group of players already understand. So every time you say I'm going to make a game in this genre
[00:20:06-00:20:10] you're kind of making a promise to the audience of that genre that they are going to understand
[00:20:10-00:20:15] certain parts of the gameplay. If you take something out you need to understand the effect
[00:20:15-00:20:20] it's going to have on the whole of the rest of that machine right. You can make a first person
[00:20:20-00:20:25] shooter without shooting it but if you do that the shooting needs to be replaced with something
[00:20:25-00:20:32] of equal value like a really intriguing kind of puzzle or some sort of narrative to uncover.
[00:20:32-00:20:38] That's where I think the really practical stuff around understanding mechanics and how they fit
[00:20:38-00:20:43] into a game or how they fit into a genre really lives. It's one of the reasons why it's so important
[00:20:43-00:20:49] to play the types of game you want to make because playing them gives you the literacy
[00:20:49-00:20:50] of understanding the mechanics of the game.
[00:20:50-00:20:54] Understanding how the thing works and how it produces a particular type of experience.
[00:20:54-00:20:58] I know it sounds really simple but of all the people that I speak to they're actually actively
[00:20:58-00:21:03] making games and using game engines. Not playing enough games or not playing the type of game
[00:21:03-00:21:08] they're making is one of the most common problems. Chasing a particular type of project because
[00:21:08-00:21:14] they think it'll be easy or because they think that type of game is popular right now but they're
[00:21:14-00:21:20] not really cognizant of how that game genre works because they haven't embedded the
[00:21:20-00:21:25] themselves in it as a player. One of the things about making the transition to doing game
[00:21:25-00:21:31] development as a career is understanding that play is a big part of that. Appreciation is a big
[00:21:31-00:21:35] part of that. That's the reason why there are so many people working in the indie space who
[00:21:35-00:21:41] either were or still are games critics or journalists. Having that appreciation of being
[00:21:41-00:21:47] able to like deeply engage with a particular game or a particular genre of games and pick it apart
[00:21:47-00:21:50] and think about you know why you like this one and not the other way around. I think that's a really
[00:21:50-00:21:54] big part of this one or where the most fertile soil is in that genre for experimenting and
[00:21:54-00:22:00] innovating. You get that by playing you don't get that by hours spent in a game engine. It's a
[00:22:00-00:22:04] different set of skills. Another thing I would like to mention here which is relevant at pretty
[00:22:04-00:22:10] much every level of the games industry from like teams of 500 people to like one person working
[00:22:10-00:22:15] alone in their bedroom. Another kind of element of the machine metaphor we can think of here that
[00:22:15-00:22:19] might be useful is that different studios and different game developers are like
[00:22:20-00:22:26] factories which are attuned to making different kinds of machines just like factories in the real
[00:22:26-00:22:32] world. The reason why a game studio sets up and then makes lots of sequels of the same game or
[00:22:32-00:22:38] makes similar games that have the same genre formula but are reskins of the same idea with
[00:22:38-00:22:43] like different settings and themes is partly due to the technical debt of like building a game
[00:22:43-00:22:49] engine or adding tools to an existing game engine setting up particular asset workflows for making
[00:22:50-00:22:54] certain type of game. But it's also based on the skills and preferences of that team you know
[00:22:54-00:22:59] that the creatives that work on that particular team are going to be attuned to making a particular
[00:22:59-00:23:05] type of game. A lot of the advice aimed at indie developers on YouTube specifically about what game
[00:23:05-00:23:11] they should make based on the market is not how game development works and it's not how business
[00:23:11-00:23:17] works in most other sectors either. When you're starting a small business you don't usually just
[00:23:17-00:23:20] pluck ideas out of raw air for something that's not going to work. You don't usually just pluck
[00:23:20-00:23:22] ideas out of raw air for something that you have no experience with right. You're usually trying to
[00:23:22-00:23:28] align a perceived gap in the market with something you know that you can actually do. The thing that
[00:23:28-00:23:35] you're most capable of achieving has very little to do with like what genre seems to be trending in
[00:23:35-00:23:41] the in the slop charts right now. You're going to have a specific set of mechanics that you are
[00:23:41-00:23:49] more aware of how they work. You wouldn't hire a plumber to fix your car. Different creatives are
[00:23:50-00:23:55] creating different types of machines. That's just one other way of looking at this metaphor of a game
[00:23:55-00:24:01] being a machine is that you know different types of developer or different studio setups are built
[00:24:01-00:24:07] for making different types of engine. Hopefully this has given you some helpful stuff to think
[00:24:07-00:24:11] about. About what we mean when we talk about mechanics and why it's even useful to think
[00:24:11-00:24:18] about games in those terms in the first place. Now I want to explain gameplay which is the thing
[00:24:18-00:24:20] that our engine or machine is going to use to make a game. So I'm going to talk about the
[00:24:20-00:24:25] engine of a game is supposed to be producing and I want to explain gameplay through the metaphor of
[00:24:25-00:24:30] driving a car. Look I know we don't all drive but it's about as close as I can get to a universal
[00:24:30-00:24:35] metaphor for how this all works. Playing a game involves using controls to achieve a goal. You're
[00:24:35-00:24:39] doing a thing to try to get somewhere. When you play a game there are some things that you have
[00:24:39-00:24:44] direct control over. They're kind of player verbs in the game and there are other things that you
[00:24:44-00:24:50] respond to and the gameplay emerges out of the relationship between those things. Like
[00:24:50-00:24:55] when you drive a car there's direct control of the vehicle but you're doing it within systems
[00:24:55-00:24:59] and circumstances you don't really control. You don't control the weather, you don't control the
[00:24:59-00:25:04] layout of the town, you don't control the traffic laws of the country. If you've ever been to a
[00:25:04-00:25:09] country that drives on the other side of the road or has very different traffic laws you probably
[00:25:09-00:25:14] have had this experience. The first day you're there you're like very anxious about not being
[00:25:14-00:25:20] able to drive in this new set of rules and then driving becomes more expensive and you're like
[00:25:20-00:25:25] exciting because it's kind of harder than driving at home but you've got comfortable enough with it
[00:25:25-00:25:30] that it feels fun again. And in game design terms you can think about this in terms of like
[00:25:30-00:25:36] trying to vary the systems and content around a player so that they never get bored of it just
[00:25:36-00:25:42] being the same thing all the time which would be like driving the same route to work every day. It
[00:25:42-00:25:46] stops being a challenge, it stops being interesting, you just sort of switch off and it's automatic.
[00:25:46-00:25:48] We don't really want our games to get like that.
[00:25:50-00:25:53] We don't want it to begin and end with the verbs and inputs of the player just like it's
[00:25:53-00:25:58] insufficient to think of driving as what the driver is doing within the car. The experience
[00:25:58-00:26:04] of driving or going for a drive is modified very heavily by all of the things outside of the car,
[00:26:05-00:26:09] all of the things that are beyond the driver's control. Driving is about the thing the driver
[00:26:09-00:26:14] is doing within the car and the things that they respond to. All of those things impact what it
[00:26:14-00:26:20] means to drive or to go for a drive and what the driver is thinking or feeling about the car.
[00:26:20-00:26:26] Making something for people to play is about both the controls that you give them i.e. the
[00:26:26-00:26:32] player's inputs into the game and the context that you put that in. The levels, scenarios, stories
[00:26:32-00:26:37] or systems which the player needs to navigate and respond to and learn. When you recognize that
[00:26:37-00:26:45] gameplay is the totality of all of that stuff it starts to become clearer why it's such a challenge
[00:26:45-00:26:49] to make a good game in the first place and why it's important to start off small and
[00:26:50-00:26:55] try and make simpler machines with fewer components to start with as well. This is also probably one
[00:26:55-00:27:00] of the reasons why so many game makers start out creating content for other people's games whether
[00:27:00-00:27:07] it's like level design using level editors or making mods or homebrew adventure modules for
[00:27:07-00:27:13] a tabletop role-playing game that they play, fan fiction and lore analysis of existing games.
[00:27:13-00:27:19] It's simply much easier to practice a smaller set of skills at a time than it is to bring
[00:27:20-00:27:25] every possible skill together to bear on one solo developed video game. When you develop a game
[00:27:25-00:27:30] it's like you're designing a vehicle for a driver to control but you're also defining all of the
[00:27:30-00:27:35] surrounding laws and geography which determine how they can drive it and the destinations they
[00:27:35-00:27:41] might want to go to whether those are literal environments or emotional destinations like
[00:27:41-00:27:47] number get really really big. This is also why it's usually a bad idea to try and make a game
[00:27:47-00:27:49] which is totally new and unique.
[00:27:50-00:27:55] Players don't necessarily want to learn to do a totally new thing they want to take skills they've
[00:27:55-00:28:01] acquired in other games they've played and apply those in a slightly novel context. Take existing
[00:28:01-00:28:08] small games in genres that you understand, clone them to the best of your ability, add a twist and
[00:28:08-00:28:12] then reflect on whether or not that twist worked in the way that you might have expected it to.
[00:28:13-00:28:21] There's a little bit more to this driving a car metaphor that I'd like to explore here. Certain
[00:28:21-00:28:22] types of game mechanics which are not necessarily the same as the ones that you might have expected
[00:28:22-00:28:28] are perhaps underutilized misunderstood and I would call those expressive mechanics. There are
[00:28:28-00:28:33] mechanisms within the car that you can operate which serve the primary function of driving right
[00:28:33-00:28:38] they are to get you to the other place you can turn the wheel you can do the foot pedals you can
[00:28:38-00:28:43] turn the lights on and off all of those things are necessary in order to safely drive the car from a
[00:28:43-00:28:49] to b but you also have things on the dashboard that are more to do with just modifying how it
[00:28:49-00:28:52] feels to drive the car like turning the radio on changing the ac
[00:28:52-00:28:58] winding the window down and those are comparable to what I would call expressive mechanics in video
[00:28:58-00:29:04] games expressive mechanics are things that don't need to be in the game in order to play the game
[00:29:04-00:29:09] so they're the sort of mechanics that you might not need to include at the prototype stage but
[00:29:09-00:29:14] what they often add really boils down to the kind of and I sound a bit cheesy here but the soul of
[00:29:14-00:29:22] the game the sense of frivolity or playfulness that that game is about this is stuff like can I
[00:29:22-00:29:27] if I roll around in the environment am I going to smash boxes even if they don't have anything in
[00:29:27-00:29:32] it's not even just about game feel because game feel applies to everything in the game it applies
[00:29:32-00:29:37] to the more functional mechanics as well you know like how your jump and attack and picking
[00:29:37-00:29:42] something up feels is really important to the core of the game I'm talking about things you can do as
[00:29:42-00:29:49] a player which do not help you win the game in any shape or form being able to change your
[00:29:49-00:29:52] character's hairstyle or make them in moat or any of those things that you can do in the game
[00:29:52-00:29:59] are comparable to being able to put the radio station that you want on in a car it doesn't
[00:29:59-00:30:04] directly impact whether or not you reach your goal but it's going to massively change how you
[00:30:04-00:30:08] feel about it in all of the time I've been running this channel reviewing and critiquing
[00:30:08-00:30:13] work in progress indie games I've tended to find that these little kind of more frivolous
[00:30:13-00:30:18] expressive mechanics like can I whack the bobble head in the car tend to be the things that make
[00:30:18-00:30:21] up the difference between a game which is quite good and a game which is excellent
[00:30:22-00:30:28] in the game studies we often use the theorist carloir to steal his spectrum of play which
[00:30:28-00:30:35] ranges from ludus to paeda and ludus is types of play according to strict rules like when you're
[00:30:35-00:30:39] playing a board game or a sport there's a strict set of rules to how the game is played whereas
[00:30:39-00:30:44] paeda is more the freeform kind of play so paeda is what we're thinking about when we use phrases
[00:30:44-00:30:51] like messing about or playing around most video games contain the possibility of both of these
[00:30:52-00:30:58] probably to the point where most players expect them to so if your game feels a bit bare bones it
[00:30:58-00:31:04] might be because there's too much play and not enough playing around I'm not necessarily saying
[00:31:04-00:31:10] that you should make a a game with no goals and no rules and no challenge that is purely cosmetic
[00:31:10-00:31:15] and all dress up and has no player agency in it I also wouldn't suggest going for these expressive
[00:31:15-00:31:20] mechanics before you've worked out what the core mechanics of your game are like the main things
[00:31:22-00:31:26] small expressive elements that often make a game appealing or memorable those are the sorts of
[00:31:26-00:31:31] things that when you show your game to an audience they are going to stick out and remember your game
[00:31:31-00:31:37] by letting players be a bit goofy be a bit silly jump around on a desk those are the things that
[00:31:37-00:31:42] make one game particularly more memorable than another game anything that lets the player leave
[00:31:42-00:31:47] some sort of Mark on the world or customize something anything that lets the player role
[00:31:47-00:31:52] play or make a taste based decision or leave a mark on the world in some way
[00:31:52-00:31:57] not acknowledged by the game systems or doesn't need to be acknowledged in the game systems can
[00:31:57-00:32:00] really help to make the player feel involved and to give the game that sense of playfulness
[00:32:00-00:32:05] and frivolity which makes the player want to come back to it draws them back to it on a more
[00:32:05-00:32:11] pragmatic level thinking about marketing games it's those small things that players are likely
[00:32:11-00:32:17] to recognize as attention to detail if your game seems quite bare bones then players will look at
[00:32:17-00:32:22] that and they'll think this developer isn't very technically skilled they just did this
[00:32:22-00:32:26] because that was what they could do if they look at your Steam page and they look at your socials and
[00:32:26-00:32:32] they see that you're filling your game with delightful silly little interactions that are
[00:32:32-00:32:39] functionally meaningless in terms of the gameplay that kind of builds trust because it shows them
[00:32:39-00:32:44] that doing those little things is no big effort to you building an audience for anything is about
[00:32:44-00:32:49] the little things it's about how much effort and energy you put in to the little things that kind
[00:32:49-00:32:52] of intrigue and delight people building a relationship with
[00:32:52-00:32:57] experiences just like building any kind of human relationship and by that I mean it's about the
[00:32:57-00:33:03] little things and it's also about the big things it's about all of the things of different sizes
[00:33:03-00:33:08] maybe it's not about the medium things but it's definitely about the small things and the big
[00:33:08-00:33:20] things I hope that clears things up the last type of underrated game mechanic that I really want to
[00:33:20-00:33:25] call out quickly here would be mechanics of the mind or cognitive mechanics we have a genre now
[00:33:25-00:33:27] called walking Sims
[00:33:27-00:33:32] it's a silly name I would prefer to call them something like environmental narrative games
[00:33:32-00:33:37] you go around in a place and you learn about what happened there by picking up objects and reading
[00:33:37-00:33:42] things and so on the name sarcastically given to these games implies that they are games about
[00:33:42-00:33:48] walking as an observer you look at these games and you think that is all the player is doing here but
[00:33:48-00:33:54] what the player is doing is just a lot of it is in their own head and it doesn't translate to button
[00:33:54-00:33:57] presses or events that you can see on the screen
[00:33:57-00:34:02] it doesn't necessarily mean that nothing is happening the player is doing something it's
[00:34:02-00:34:08] just they're doing it in their head that is the experience that is coming out of the game so the
[00:34:08-00:34:13] thing that the player is doing in their head is a game mechanic because it's a thing that the game
[00:34:13-00:34:19] designer gave the player to do the player is doing something they are judging or deducing something
[00:34:19-00:34:25] about a situation presented to them in the game world they're just not doing that by like running
[00:34:25-00:34:27] up and pressing loads of buttons and trying to
[00:34:27-00:34:33] decipher a code and unlock a door which is how we normally think of video game puzzles but they
[00:34:33-00:34:40] are doing an activity given to them by the game designer and that is producing their experience so
[00:34:40-00:34:45] it's a game mechanic this is the reason why so many visual novel type games position the player
[00:34:45-00:34:50] character as a detective or a journalist or someone like that it's to prime you to observe
[00:34:50-00:34:56] investigate and to make judgments these are still game mechanics because they're the things that the
[00:34:56-00:34:57] designer gives
[00:34:57-00:35:03] the player to do so if you're making a game which is mostly or entirely about story I'd encourage you
[00:35:03-00:35:09] to still think about the player verbs that you're designing for even if they're not represented in
[00:35:09-00:35:17] in-game actions a dating Sim is about judging characters in order to ascertain which one you
[00:35:17-00:35:23] like the most and then navigating the conversations around that if you're making a very story focused
[00:35:23-00:35:27] game you still need to think about what is the player doing even if the thing that they're doing
[00:35:27-00:35:33] is predominantly a cognitive verb like noticing things remembering things judging people and
[00:35:33-00:35:39] situations the player is still doing something and how good your story game is going to be will
[00:35:39-00:35:46] be based on how well it encourages players to do that thing and the kind of interesting situations
[00:35:46-00:35:50] you throw at them which get them to do those cognitive verbs more broadly what I'm saying
[00:35:50-00:35:57] here is that some game mechanics are much more heavily weighted to what is going on in the player's
[00:35:57-00:36:02] head than what is going on in their hands or on the screen lots of puzzle and strategy games
[00:36:02-00:36:09] involve a much higher ratio of thinking to doing consider a strategy game you might look at stuff
[00:36:09-00:36:14] in the game and make loads and loads of little judgments and then that all culminates in one
[00:36:14-00:36:21] click in the interface strategy games encourage players to put a lot of thought into a single
[00:36:21-00:36:26] action that's historically why we use clocks for chess we want to limit the amount of time
[00:36:27-00:36:32] players get to think about their next move or it will just go on forever the top level game design
[00:36:32-00:36:40] thing to think about here is that some of the most powerful verbs in your game might not be
[00:36:40-00:36:47] ones which directly map onto a specific set of button presses they are going to be stuff going
[00:36:47-00:36:51] on in here I hope this has given you lots of things to think about or encourage you to think
[00:36:51-00:36:57] about things in some new ways I don't make video essays like this to give you neatly
[00:36:57-00:37:03] actionable advice on what to do with your career or how to approach your hobby projects if you're
[00:37:03-00:37:08] making an indie game that's fundamentally a an entrepreneurial activity and one that requires
[00:37:08-00:37:14] you to think like a leader and not a follower and that is precisely why a video like this is
[00:37:14-00:37:19] more a kind of set of thought exercises here's some things to think about about this topic
[00:37:19-00:37:25] rather than 10 top tips to make your mechanics more good because I know that would be better
[00:37:25-00:37:26] for the algorithm but
[00:37:27-00:37:31] it's not what I'm interested in doing and I don't think it's the sort of thing that produces good
[00:37:31-00:37:36] game design thinking YouTubers are encouraged by the algorithm and encouraged by the fact that
[00:37:36-00:37:42] the largest audience is the beginner audience to wrap game design theory up as neatly packaged
[00:37:42-00:37:48] advice on exactly what to do because that's what the largest possible audience wants it's not the
[00:37:48-00:37:52] most algorithm friendly thing I'm never going to be able to retire purely on ad revenue from
[00:37:52-00:37:57] YouTube because what I'm doing here is aimed at intermediate learners and people
[00:37:57-00:38:02] but really want to learn how a game designer thinks thanks for staying to the end I hope you
[00:38:02-00:38:07] got something useful for it and if you're new to the channel and you'd like to see or hear more of
[00:38:07-00:38:13] this kind of thing please subscribe and maybe even consider supporting us on Patreon and in the
[00:38:13-00:38:17] meantime please drive safely
