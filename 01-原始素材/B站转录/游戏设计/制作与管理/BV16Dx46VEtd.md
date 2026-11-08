---
title: "Thomas Brush|独立游戏行业真的崩溃了吗？（乔纳森・布洛）——Is The Indie Game Industry Broken? Ep. 070"
platform: bilibili
bvid: BV16Dx46VEtd
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-11-01 18:47:42
duration_sec: 7531
view: 877
like: 22
coin: 5
favorite: 47
reply: 4
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV16Dx46VEtd
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 79694
crawl_time: 2026-11-08 21:20:01


# Thomas Brush|独立游戏行业真的崩溃了吗？（乔纳森・布洛）——Is The Indie Game Industry Broken? Ep. 070

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-11-01 18:47:42
- **时长**: 2小时5分31秒
- **播放**: 877 | 赞: 22 | 币: 5 | 藏: 47
- **链接**: https://www.bilibili.com/video/BV16Dx46VEtd

## 视频描述

原视频：https://www.youtube.com/watch?v=vkOiUSSb7EY
（2026年7月10日）Thomas Brush 采访独立开发者乔纳森・布洛，围绕这款万众期待的解谜游戏《沉星之序》的最新动态展开对话。二人探讨自研引擎开发的重重难点、当前 3A 与独立游戏行业格局，以及创作者要如何在每年海量新作扎堆的市场里保持自身辨识度。

我和乔纳森・布洛对谈，聊一聊他耗时十年的项

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV16Dx46VEtd
# 语言=en 时长=01:01:23 模型=large-v3

[00:00:00-00:00:08] Imagine making a few indie viral hits. Games like, I don't know, Braid or The Witness. In fact,
[00:00:08-00:00:13] you become an indie legend and maybe you're featured in one of the most successful game
[00:00:13-00:00:19] development documentaries of all time. But then, for some reason, at the peak of your career,
[00:00:19-00:00:27] you have this urge to spend 10 years making a custom scripting language, a custom engine,
[00:00:27-00:00:33] and with those tools, you create a 10-year sprawling puzzle game called
[00:00:33-00:00:40] Order of the Sinking Star. Now imagine launching that game's demo 10 years after coming up with
[00:00:40-00:00:46] that idea. How do you feel? Would you be nervous? Would you wonder if, well, you still got it?
[00:00:46-00:00:52] I ask this question directly to my guest, Jonathan Blow. I talk about his game's demo
[00:00:52-00:00:57] launch during Next Fest in the last couple of weeks, whether the 10-year gamble was worth
[00:00:57-00:01:02] it and ultimately how he's feeling on his third commercial release. We also discuss how the
[00:01:02-00:01:08] industry has changed while he's been quietly making his third release. And yeah, we of course
[00:01:08-00:01:14] discuss friend slop and the state of the AAA and indie industries. We discuss chasing trends,
[00:01:15-00:01:21] feeling irrelevant, and how to stand out amongst the thousands of indie titles released each year.
[00:01:21-00:01:26] This is the third time Jon has come on this podcast, but this is the first time that he's
[00:01:26-00:01:27] discussed an
[00:01:27-00:01:34] actual response to his third commercial release, Order of the Sinking Star. Listen up because
[00:01:34-00:01:39] an indie legend is about to start talking and you don't want to miss it. And by the way,
[00:01:39-00:01:43] if you want to make 2D games or maybe even 3D games like I'm doing and potentially turn them
[00:01:43-00:01:48] into an actual full-time gig, I have a course called Full-Time Game Dev and it's 50% off for
[00:01:48-00:01:53] the summer sale. I've gone full-time with just a demo on three separate occasions. And by the way,
[00:01:53-00:01:57] look here, these are some students who went full-time with the help of what I,
[00:01:57-00:02:02] Jon, I'm going to teach. In this course, you're going to learn just that. How to land publishing
[00:02:02-00:02:07] deals with just a demo. How to get funded on Kickstarter with just a demo, make a 2D or a 3D
[00:02:07-00:02:12] game in Unity, Godot, or Unreal. You're going to learn how to market your game, get press coverage
[00:02:12-00:02:17] like I have, hit the steam front page, and so much more. Everything that I teach in this course is
[00:02:17-00:02:22] stuff I've done. So you're learning from an actual indie game developer, not somebody who's just
[00:02:22-00:02:27] wanting to make games. I'll also throw in my 2D and 3D art courses completely free. And as a bonus,
[00:02:27-00:02:32] I'll also throw in a private one-hour mastermind meeting with me and a handful of other developers
[00:02:32-00:02:36] where I'm going to answer any questions you have in a private setting. This summer sale ends soon,
[00:02:36-00:02:42] and I don't do many of these during the year. So be sure to click below to enroll and join 4,500
[00:02:42-00:02:51] other students. First thing I wanted to ask you was, can you give us a brief overview of,
[00:02:51-00:02:55] just because I mean, the previous episodes you mentioned, the whole episode was basically about
[00:02:55-00:02:57] the production of Order of the Sinking Star. Yeah.
[00:02:57-00:03:00] Can you give me a brief overview really quick of how long it took, how you made it,
[00:03:00-00:03:05] the engine, the code, all that stuff? And then we'll talk about the demo and how it did.
[00:03:05-00:03:14] Well, I started the game shortly after the Witness shipped, which was a long time ago now,
[00:03:14-00:03:22] in 2016. We're still doing some Witness stuff for a while, but sometime around the middle of 2016,
[00:03:22-00:03:26] like possibly around June or July, I started this game.
[00:03:27-00:03:35] And the idea was to take four games that already existed out there on the internet that you could
[00:03:35-00:03:44] play for free, but they had graphics that were not particularly appealing. And so people would
[00:03:44-00:03:49] sort of bounce off them playing. They weren't the most popular games in the world, but when I played
[00:03:49-00:03:54] them, the design was really nice. And I was like, oh, these games are under-recognized. And so why
[00:03:54-00:03:57] don't I do a fun thing where I put them together into something that, well, I'm going to play this
[00:03:57-00:04:02] thing that looks like a game anthology, but then explodes into something bigger as you play,
[00:04:02-00:04:07] because we'll do a fun thing where we combine the worlds together and do this big game design
[00:04:07-00:04:14] experiment. And so at the same time as all that, so for some reason, I was convinced that that
[00:04:14-00:04:22] would be a tiny, simple little game. I don't know why. And then at the same time is that I also
[00:04:22-00:04:26] decided to do this big technical experiment where it was like, look, let's, I don't like,
[00:04:27-00:04:31] I don't like programming in C++. Let's make a new programming language and let's rebuild
[00:04:31-00:04:35] everything in that language. And let's design a new engine for modern rendering and all that.
[00:04:35-00:04:41] And so it was a lot to do at once. And so it did take a long time to get all of it done.
[00:04:44-00:04:48] And it's been a little bit of like, at some point, like as the years go on,
[00:04:48-00:04:52] it starts to become some kind of like internet mystery. Like what happened to this guy and
[00:04:52-00:04:56] what's he been doing and oh, he's been working on stuff for a long time,
[00:04:56-00:04:56] but it can't. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.
[00:04:56-00:05:01] It can't actually be good. Cause nothing that, you know, anytime you hear about a project that
[00:05:01-00:05:06] goes forever, it's like, well, it kind of failed somehow or whatever. Yeah. And so it's been great
[00:05:06-00:05:11] to actually get to the point where the demo has come out and people can play it and it's like,
[00:05:11-00:05:15] oh, this is actually pretty cool. Yeah. Yeah. So yeah.
[00:05:15-00:05:21] So it's sitting at 91%, very positive. And you left the reviews open for the demo,
[00:05:21-00:05:26] which is a, it's a courageous move. You don't have to do that. You know, you can, you can hide
[00:05:26-00:05:38] them. Um, and I'm like, so I'm so excited for you because I know to a degree how it feels where
[00:05:38-00:05:45] you work so long on something. Maybe you start to wonder if it was worth it.
[00:05:45-00:05:50] I don't know if you think that way for me, like I'm, I'm, I'm on year five with my project and
[00:05:50-00:05:56] I'm just like, I even eat, I'll even let people on Twitter inform me of how to feel. Cause I don't
[00:05:56-00:06:01] even know how to feel anymore. Yeah. You know, I'll have people say, what were you thinking? Or
[00:06:01-00:06:07] like why you bit off way more than you could chew. And so my question for you is leading up to
[00:06:07-00:06:15] launching the demo, did you feel any sense of insecurity about this project?
[00:06:16-00:06:21] I wouldn't say insecurity. Like, I don't think I relate to these things in quite the way
[00:06:21-00:06:26] as some people do. Um, I'll try to break it down. It's complicated though.
[00:06:26-00:06:29] You know, if this becomes too much, too much detail or it's too in the weeds.
[00:06:29-00:06:32] This is what I wanted. I figured your answer wouldn't be simple. So,
[00:06:32-00:06:36] so, you know, when I'm working for something on something for this long,
[00:06:37-00:06:41] um, let's just take the design component, right? There's a design component. There's a technical
[00:06:41-00:06:45] component. There's a art direction. There's all these different categories of a game,
[00:06:45-00:06:49] but let's take design, which is the one where I had the most direct hand in the whole time,
[00:06:49-00:06:54] right? Cause there's a team working on everything. So by the time the game's gonna come out, like
[00:06:54-00:06:56] it's not an accident.
[00:06:56-00:07:00] That it took a long time. It took a long time. Cause we're not just trying to make like any old
[00:07:00-00:07:06] slop. We're trying to make something that people haven't done before. And that's good. And that
[00:07:06-00:07:11] thoroughly digs into and explores the subject matter, the mission that I had for the game
[00:07:11-00:07:18] when I started. Right. So by working on that very hard for a long time, like I know that it's good.
[00:07:18-00:07:22] I know that the design of this game is good. I know that it's really interesting.
[00:07:22-00:07:26] I know that it has succeeded in doing various things because
[00:07:26-00:07:30] if it hadn't succeeded, well, I don't know, I might've canceled the game or put it on the back
[00:07:30-00:07:36] burner until I had a different idea or something. Right. So I know that now there's a different
[00:07:36-00:07:42] question is will other people think it's good or even, you know, there's a difference between
[00:07:43-00:07:47] acknowledging that something is interesting and like a contribution and actually having
[00:07:47-00:07:51] enough fun playing it that you want to like pay for it or something. Right. So those are questions.
[00:07:51-00:07:56] And so I never know the answer to that question when I'm going to release a game. And every time
[00:07:56-00:08:01] it's always turned out better than I thought. So with this demo, you know, I would have been like,
[00:08:01-00:08:08] oh, it's a Sokoban game. So what does that mean? It means not as many people are going to play it
[00:08:08-00:08:13] as if it were like a shooter or something. And it means the reviews are probably going to be lower
[00:08:13-00:08:17] because people are gonna be like, what, what the hell is this? Right. And so that would have been
[00:08:17-00:08:23] my expectation. And you know, the demo has exceeded those expectations in multiple directions,
[00:08:23-00:08:30] which is great. And, and, you know, with, with the review scores, uh, I think they'll go up a few
[00:08:30-00:08:36] percent for the final game, just because, you know, one, usually there's one or two things
[00:08:36-00:08:40] that are like consistent issues for people. And for us, it's because it's a new engine,
[00:08:41-00:08:47] like, and we were in a super hurry to get the demo out. We just didn't quite do everything that you
[00:08:47-00:08:52] would do to run better on lower end systems, just like cutting the shaders down and all that,
[00:08:52-00:08:53] because we have like. Yeah.
[00:08:53-00:08:53] Yeah.
[00:08:54-00:08:59] You know, three and a half programmers or something. So, um, that that's already,
[00:08:59-00:09:04] you know, progressed very well and stuff, but, but, okay. So, so to that's a little bit of a
[00:09:04-00:09:12] side tangent, but, um, I guess the point is, so I wasn't insecure because I know it's good,
[00:09:12-00:09:19] but I was uncertain how this is going to go. Right. Like, is it, is nobody gonna
[00:09:19-00:09:23] buy this? And then I just have to go be off by myself.
[00:09:24-00:09:29] Making games. Right. Cause having a team is even a small team like ours. It's really expensive.
[00:09:29-00:09:33] You know, you would be, you would be shocked. I'm not going to say the numbers, but you would
[00:09:33-00:09:39] be shocked at how much it costs. Well, not you. Well, you kind of hinted at it at the previous
[00:09:39-00:09:46] podcast and I did the math. Yeah. You know, I, I, um, I was going to say something related to,
[00:09:46-00:09:53] to expectations of a demo launch versus a 1.0 launch. Yeah. And I think we may have talked about
[00:09:53-00:09:58] this in the previous podcast, but I think the review scores will go up for 1.0. Not that they
[00:09:58-00:10:03] need to, I think 91% is amazing. That's great. Yeah. But I think they're going to go up and I
[00:10:03-00:10:08] think one of them is the optimization for sure. But also I think you're only going to, you're
[00:10:08-00:10:14] going to get a more qualified players. Right. Right. Yeah. So that's a phenomenon. So if people
[00:10:14-00:10:18] I'll explain it a little bit, cause I've had the same thought, you know, when you put something
[00:10:18-00:10:23] up for free or even like, let's say you have an existing game and you do a steam sale, that's super
[00:10:23-00:10:29] you do like a humble bundle. Your review scores are generally going to go down in that case,
[00:10:29-00:10:33] even if they, they were high when you launched. And the reason is because the amount that somebody
[00:10:33-00:10:38] pays for your thing is correlated to how interested they are in it and how appreciative
[00:10:38-00:10:42] they are of that kind of thing. Right. And so if somebody gets your game, let's say your game
[00:10:42-00:10:48] launched at $30 and they're getting it for like 99 cents in a super steep sale or a bundle,
[00:10:48-00:10:53] it's probably something that they're not that into, or they would have been there earlier.
[00:10:53-00:10:53] Yeah. Right.
[00:10:54-00:10:59] And so this just has an effect on scores. And so, you know, when you have a free demo like that,
[00:11:01-00:11:06] in theory, I mean, I don't know, cause steam next rest, which is the event where all this
[00:11:06-00:11:10] was happening. It's a little bit weird. The dynamics of it are a little bit weird and I
[00:11:10-00:11:13] don't totally understand them. So I'm hesitant to like draw super firm conclusions.
[00:11:13-00:11:15] Wait, what do you mean? Why are they, why are they weird?
[00:11:16-00:11:20] Well, let's say you wanted to play some things,
[00:11:20-00:11:23] right? Like you're on steam because you want to play games.
[00:11:23-00:11:28] And you want to play interesting, good games. And these events happen multiple times per year
[00:11:28-00:11:33] when there's all this stuff that's free and it's not even out yet. Right. And so you would think
[00:11:33-00:11:40] that like more people would play that than who buy games on steam because it's free.
[00:11:40-00:11:41] Yeah.
[00:11:41-00:11:45] And it costs you enough, you know, and, and you get to see things that aren't even out yet,
[00:11:45-00:11:50] but it's, it's actually like a subset of the audience. Right. And not even that big of a
[00:11:50-00:11:53] subset. And so like, that's the dynamic. Right. And so like, that's the dynamic I'd
[00:11:53-00:11:59] kind of don't understand. Yeah. Yeah. And maybe I can come up with some reasons for that because
[00:11:59-00:12:04] like, oh, um, well, if I really like a game, I want to wait until it's done. I don't want to
[00:12:04-00:12:09] play a bad version of the game or I want to wait for other people to tell me what's good. And I
[00:12:09-00:12:14] don't want to have to dig through all this stuff. You can come up with reasons for that, but I,
[00:12:14-00:12:17] I feel like they still don't quite explain. I feel like next fest
[00:12:18-00:12:23] should be a lot better than it is. Maybe part of it is there's just so many games and you try one
[00:12:23-00:12:29] or two and they're terrible and you're like, ugh. Um, and that's not really a dig on anyone
[00:12:29-00:12:33] else's legitimate game. It's just for people who don't know, there's like 5,000 games that
[00:12:33-00:12:39] get released in one day. Yeah. And you definitely need some filtering mechanism to figure out
[00:12:40-00:12:45] what, you know, and usually that might be just the charts or something, but most people, you know,
[00:12:45-00:12:53] most gamers don't go to like steam DB to see what demo is, has a lot of plays or whatever. Right.
[00:12:53-00:12:56] Yeah. So do you feel like, do you feel like, uh,
[00:12:58-00:13:04] releasing a demo? Is that becoming more and more, uh, watered down? It's, it's definitely more
[00:13:04-00:13:10] competitive, right? So is it worth a lot of things going on? So, so in that 5,000 game number,
[00:13:11-00:13:16] the vast majority of those aren't real games that we would recognize as, as real games, right?
[00:13:16-00:13:22] They're like, someone wants to get into games. They made something in unity for like a couple weeks.
[00:13:23-00:13:28] I don't know how long, right. Right. And, and that's good. That's a positive thing, right? I,
[00:13:28-00:13:34] I don't think it's bad for people to experiment and learn, but then if you put that up alongside
[00:13:35-00:13:39] a game that somebody worked on for like four years, it's just not the same thing, right?
[00:13:39-00:13:44] It's, it's a very different situation. And so, well, okay. That's one category.
[00:13:44-00:13:52] The other category, which is maybe bigger now, uh, is just all the cynical slop games where it's like,
[00:13:53-00:13:57] oh God, there was this one, this wasn't even next dress, but I downloaded some funny game.
[00:13:58-00:14:05] You know, there's somebody who makes all these like shop simulator games. So I bought like gun
[00:14:05-00:14:11] shop simulator or something. And it was literally a, just a reskin that took like two days of like
[00:14:11-00:14:16] their 17 other really bad shop simulator games, you know? Yeah.
[00:14:16-00:14:22] Um, and that's probably a lot of the games in NextFest now as well. Um, so I don't know.
[00:14:22-00:14:26] I mean, I, I, I, that brings me to my next question, which is,
[00:14:28-00:14:35] has, you're, you're older than me, but I feel like I'm getting old. So I can, I can maybe
[00:14:36-00:14:42] by osmosis say, maybe you feel like you're getting older too. Cause I'm 36 in a couple of weeks.
[00:14:43-00:14:48] And I'm just like, I'm on, I'm on Instagram watching reels of all these games that are
[00:14:49-00:14:52] blowing up on steam. Yeah. And, and I'm not,
[00:14:52-00:15:00] I'm not against them, but they are a slop, at least in the internet slang terminology.
[00:15:01-00:15:02] There's just a lot.
[00:15:02-00:15:06] I mean, you wouldn't, you wouldn't look at Mecha Chameleon and say that's a well
[00:15:06-00:15:08] art directed game or whatever. Right.
[00:15:10-00:15:13] Yeah. Yeah. And does that make you feel confused?
[00:15:14-00:15:19] It doesn't make me feel confused actually. Um, I mean, good for that. So dude,
[00:15:19-00:15:22] there's been this phenomenon my entire time in the industry, right?
[00:15:22-00:15:23] Yeah.
[00:15:23-00:15:29] Where I work super hard. I just like bleed for years to make something
[00:15:30-00:15:34] and then, you know, something else gets played by way more people. That's like much simpler.
[00:15:34-00:15:35] Right. Yeah.
[00:15:35-00:15:40] That even going back to like when I, before I was working on stuff that anyone knew. So
[00:15:40-00:15:44] when I first started in games in the nineties, in 1996, I was like, oh,
[00:15:44-00:15:47] we're going to make a 3d engine. We have to learn how to do that. We have to drive
[00:15:47-00:15:52] every pixel on the screen ourselves. Cause there's no such thing as a GPU in 1996. And we were on the
[00:15:52-00:16:00] thing, this service called total entertainment network. We signed up with them and this was
[00:16:00-00:16:07] like a subscription service where you would play multiplayer games, uh, you know, over your modem
[00:16:07-00:16:13] and they were giving you like better modem connectivity with lower latency or whatever.
[00:16:13-00:16:17] That was, it didn't, that business didn't work out, you know, they shut down after a few years,
[00:16:17-00:16:22] but okay. So we were on there and I was working super hard to do this. Like,
[00:16:22-00:16:28] 3d engine, like hover tank war game with 32 simultaneous players and like
[00:16:28-00:16:34] good graphics and just, you know, real time collision detection back before you could like,
[00:16:34-00:16:39] just use a library to do that. And that was hard to figure out and just all this stuff,
[00:16:39-00:16:44] all this insanely hard stuff. And, you know, we launched on this service and we've got,
[00:16:44-00:16:48] you know, some people playing, but then there's this other multiplayer
[00:16:48-00:16:52] game on the service, which I think was called arc or something, but it, it was a
[00:16:52-00:16:58] very simple, um, team versus team, like get to the other team's goal or something.
[00:16:58-00:17:02] And it was 2d and everybody was like a little circular UFO sprite.
[00:17:03-00:17:06] And you just had one thing you could do, which was like, shoot the other guy.
[00:17:06-00:17:11] Yeah. Whereas ours had like, you know, a bunch of weapons and like, you could call in like
[00:17:11-00:17:17] ships to like orbital strike and like drop supply packs and stuff. And, and they had like five times
[00:17:17-00:17:22] as many players as us. Yeah. Right. Cause their game was just simpler and easier for people to get.
[00:17:22-00:17:27] And ours was like, because we were trying to do all this 3d stuff, it didn't run as well on
[00:17:27-00:17:33] everybody's system and all these things. Right. And so this has just been the story of my life
[00:17:33-00:17:39] in some way. It does seem much more that way in 2026, because you see all these games that are
[00:17:39-00:17:45] just like, you know, somebody worked on it for six months and it just blows up and it's like,
[00:17:45-00:17:52] all right, cool. But that actually is also, that's a good sign in some way. Um, it's a sign,
[00:17:52-00:17:59] that, okay, usually if one of these games blows up, it's, you know, not literally the same as a
[00:17:59-00:18:04] previous game with some changes. Right. So like Mecha Chameleon to take that example, you know,
[00:18:04-00:18:10] nobody was really making, uh, this kind of like multiplayer, you know, hide and seek game. It just
[00:18:10-00:18:15] wasn't really a thing. Right. Um, or, you know, Among Us, which is sort of in the same general
[00:18:15-00:18:21] category is a very different game blew up very similarly some years ago because that thing just
[00:18:21-00:18:22] didn't exist otherwise. Mm-hmm .
[00:18:22-00:18:27] Right. And so that's good. It's good when things that weren't being done before
[00:18:27-00:18:33] succeed, because that means we're increasing the breadth of like what games as a whole are doing.
[00:18:34-00:18:39] There's going to be like 20 Mecha Chameleon clones over the next six months. Right. There already
[00:18:39-00:18:45] are, I'm sure. I mean, would you say it created a new genre? I mean, it's a party game, but like.
[00:18:45-00:18:50] Yeah. I, I mean, I think, I think you have to wait a little bit to see
[00:18:51-00:18:52] what the genre is going to be.
[00:18:52-00:18:53] Yeah.
[00:18:53-00:18:59] Because I do think like Mecha Chameleon's a little too simple. Like if the, the, okay. If,
[00:18:59-00:19:04] if it's a new genre, the next game in that genre that is big, that people really play,
[00:19:05-00:19:09] it can't be like literally the same game with different maps. Mecha Chameleon already has
[00:19:09-00:19:10] different maps. Right.
[00:19:10-00:19:10] Right. Right.
[00:19:10-00:19:14] So it has to just be like, oh, it's the same concept, but the way you hide is a little
[00:19:14-00:19:20] different. The way you navigate is a little different. The way you paint yourself like that,
[00:19:20-00:19:22] the painting yourself seems like part of the genre.
[00:19:22-00:19:27] Right. And so maybe that's different in some way. So we'll see, we'll see what that ends up being.
[00:19:27-00:19:32] Do I, do I think it made a new genre? Quite possibly. Genres can be small or big as well.
[00:19:32-00:19:35] It's just like, do people recognize this as a separate thing?
[00:19:35-00:19:40] Do you think you could make a, do you think you could make a small game?
[00:19:41-00:19:42] Yeah.
[00:19:42-00:19:48] You could actually do it and you wouldn't, you wouldn't over-scope it and
[00:19:48-00:19:51] turn it into what you did with, uh, Order of the Sinking Star?
[00:19:51-00:19:51] Yeah. I think at this point, you know, I think it's, I think it's, I think it's, I think it's,
[00:19:51-00:19:56] I think at this point I could, it's just, it took a lot of learning to get to that point.
[00:19:56-00:20:01] Um, is that the strategy I'm going to do? I don't know. Maybe, maybe kind of like I,
[00:20:04-00:20:08] at some point things can't keep taking more years, right? If the next game takes 15 years,
[00:20:09-00:20:15] that'll be really bad. So, um, yeah, I don't know. The, the trick though is
[00:20:16-00:20:21] both to keep it scoped down and find something really cool and amazing and fun that people
[00:20:21-00:20:28] really like. Right. And that's not so easy. You know, lots of people make small games all the
[00:20:28-00:20:32] time and nobody cares about them. Right. Yeah, it's true. What's the quest? What's the, what's
[00:20:32-00:20:39] the difference? My theory about, um, my theory about like friend slop is not that friend slop
[00:20:39-00:20:46] is popular, but because there's so much of it and 5% of it succeeds. And so you just see a lot of
[00:20:46-00:20:51] it, you know? And I don't think it necessarily means that, you know, the market share is being
[00:20:51-00:20:58] taken up necessarily by friend slop and higher quality quote unquote, you know, games like yours
[00:20:58-00:21:04] that, that are just massive. And the artwork is incredible. It doesn't mean that those games
[00:21:05-00:21:09] have less of a market share because of friend slop. I mean, what do you think? Do you think
[00:21:09-00:21:13] No, I, I don't think, I don't think the market share is smaller.
[00:21:14-00:21:20] Um, I do think that it's changing over time. So really I think what happened, if you go back in
[00:21:20-00:21:26] the day to when I was getting in the game industry, right, it was mostly AAA games.
[00:21:27-00:21:32] And every month there were like five or six, this is not an exaggeration. Every month there were
[00:21:32-00:21:37] five or six AAA games that you would see in the news and they were coming out soon.
[00:21:37-00:21:43] And there was always stuff to watch for. Right. Um, and then over time,
[00:21:43-00:21:50] because those games got so expensive and so hard to make and take longer, just that decreased and
[00:21:50-00:21:57] decreased. And like now I don't even know. I mean, I guess if you're like mainly a PlayStation
[00:21:57-00:22:01] gamer or something, it's a little bit like that still where you have some number of games that,
[00:22:01-00:22:07] you know, are coming up. Yeah. But like, if you're on PC, you don't even really have that
[00:22:07-00:22:13] because there's nobody, there's nobody like curating the set of big games for you anymore.
[00:22:13-00:22:18] And so what do people know about, they know like GTA is a big game that's going to come out
[00:22:19-00:22:20] and like, that's kind of it.
[00:22:20-00:22:26] And so, and so there's all this mind space for other things to happen
[00:22:26-00:22:32] because AAA kind of gave up that territory is what I would say. Right. And, and they're,
[00:22:32-00:22:36] they're just not making the games anymore. Like they just don't come out that often.
[00:22:36-00:22:40] And then when they do, they're not that much better than an indie game anyway anymore.
[00:22:40-00:22:44] Right. I mean, they're still better in terms of like how much money they spent building the
[00:22:44-00:22:49] graphics, but like people don't really, we we've had so many good graphics that like,
[00:22:49-00:22:50] once you're above us,
[00:22:50-00:22:53] they're still going to be like, oh, this is the best game ever.
[00:22:53-00:22:56] Right. And so I think like, that's, that's what I'm looking for.
[00:22:56-00:22:59] Yeah. I mean, I think there's a, I think there's a minimum bar where it's like,
[00:22:59-00:23:03] oh, your game's ugly and stupid if it's below that. And then there's a big range of like,
[00:23:03-00:23:07] oh, it's a little better. It's a little worse, but how fun is the game?
[00:23:07-00:23:07] Yeah.
[00:23:07-00:23:12] And there's some like very, very, very top bar where you could imagine somebody making a game
[00:23:12-00:23:18] that looks like nothing you've ever seen before. Right. That almost never happens because it's
[00:23:18-00:23:20] incredibly difficult. Right. Yeah.
[00:23:20-00:23:25] And so that's, that's the playbook that they knew how to run though, was let's just
[00:23:25-00:23:30] spend a ton of money. We'll make a really impressive looking game and everybody will
[00:23:30-00:23:36] buy it for that reason. And that playbook stopped working. And so I think that created a big vacuum
[00:23:36-00:23:43] and all these other independent games have moved in to sort of fill that space. And so, you know,
[00:23:43-00:23:49] this year, so you mentioned the friend games, but there's, there's been a bunch of just regular
[00:23:49-00:23:54] single-player games that had really big hits this year or with mild multiplayer. Right. So like,
[00:23:55-00:24:03] you know, Slay the Spire 2, Mugenics, Subnautica 2 was really big for like a couple of weeks.
[00:24:03-00:24:06] I'm forgetting, cause there's been a lot, but, but you could probably keep going and name like
[00:24:06-00:24:12] seven or eight games like that, that had like unreasonably huge launches this year.
[00:24:12-00:24:13] Yep.
[00:24:13-00:24:18] And it's just because that, you know, people want to play games and if electronic arts can't
[00:24:19-00:24:25] make games anymore, right? Or if Microsoft can't make games anymore, we'll, we'll play games from
[00:24:25-00:24:28] people who are making the games. Like that's all that's happening.
[00:24:28-00:24:32] What's your, I want to talk about Order of the Stinking Star in just a sec,
[00:24:32-00:24:38] but I want to sort of wrap, end this loop with a question about the, the health of the industry.
[00:24:38-00:24:43] And, you know, you and I probably talk once a year, at least for the last three years.
[00:24:44-00:24:48] And I, I think I ask you this every year about the state of the industry. What, what, what happens,
[00:24:49-00:24:58] triple a you know we've got ai which i know you're not optimistic about yeah um we've got um i think
[00:24:58-00:25:04] it was more than 20 000 games are going to be released this year on steam yeah we've got price
[00:25:04-00:25:11] dropping and price increasing so polarization of pricing meaning like i guess triple a games what
[00:25:11-00:25:16] 70 bucks now or something and then we've got prices dropping i'm gonna have to release my game
[00:25:16-00:25:24] for five dollars less than what we planned on because we're just looking at the data and it's
[00:25:24-00:25:30] like indie games are getting cheaper i know exactly what data you're looking at yeah yeah
[00:25:30-00:25:37] so all in all what's what are jonathan blow's crystal ball thoughts about the state of the
[00:25:37-00:25:46] industry uh for triple a and and indie do you have any thoughts i mean triple a is having real
[00:25:46-00:25:47] problems
[00:25:47-00:25:53] obviously i mean even so at the day on which we're recording this they're supposed supposed
[00:25:53-00:26:00] to be according to rumor a bunch of big layoffs announced like today so we'll see if that happens
[00:26:00-00:26:07] um but it's just you know i had to deal with some of this like it just got really expensive
[00:26:07-00:26:13] to make games it got really expensive to hire people to work on games especially programmers
[00:26:13-00:26:17] because we had you know i don't remember if i talked about this last time but over in the
[00:26:17-00:26:23] general like web technology sector or whatever you had salaries going up and up and up for years
[00:26:23-00:26:27] because they had so much free money over there and you kind of have to compete with that like
[00:26:27-00:26:32] if you're a triple a game company if somebody can go to google and make like five hundred thousand
[00:26:32-00:26:40] dollars right for doing nothing like programming one button a month on a webpage and like going
[00:26:40-00:26:47] to some meetings you got to pay that person at least i don't know like 300 250 to to work on games
[00:26:47-00:26:50] Whereas traditionally that would have been a really high salary.
[00:26:50-00:26:51] I don't know.
[00:26:51-00:26:52] There's also been inflation and stuff, right?
[00:26:53-00:26:59] But like, so, so, and, and then, you know, there was this whole thing where the industry
[00:26:59-00:27:06] was thought of as, uh, or there was a lot of press, let's say that, that AAA game companies
[00:27:06-00:27:09] were exploitative and not paying people enough and making them work longer.
[00:27:09-00:27:13] And, and some of them were, some of them were doing that, but I think the industry as a
[00:27:13-00:27:18] whole reacted to that and, and said, oh, we have to be way too nice.
[00:27:18-00:27:24] And we can't make sure that anyone's actually working actually, because that's mean.
[00:27:24-00:27:29] And then COVID happened and everybody's working from home at least three days a week and everyone's
[00:27:29-00:27:30] less efficient.
[00:27:30-00:27:32] And so all these things compounded.
[00:27:32-00:27:37] And so here's, here's just some numbers I was spitballing on a forum with someone, right?
[00:27:37-00:27:43] So like, since pick some time, that's not even that long ago, like, well, not that let's
[00:27:43-00:27:43] say 20.
[00:27:43-00:27:45] It could be less.
[00:27:45-00:27:52] It could even be 10 years, but let's say 20 years from like 2005, 2006, when, um, the
[00:27:52-00:27:55] video game industry was still the AAA we're still talking about.
[00:27:55-00:27:57] Cause Indie was very small at that time.
[00:27:57-00:28:03] Um, it was still comprised of like good programmers, good artists for the most part who were a
[00:28:03-00:28:09] relatively like AAA teams, even at that time were small compared to now, they could really
[00:28:09-00:28:11] make some stuff that was really impressive.
[00:28:11-00:28:11] Right.
[00:28:11-00:28:12] And you were like, wow.
[00:28:12-00:28:12] Right.
[00:28:12-00:28:13] Since then, due to.
[00:28:13-00:28:20] Some of these dynamics, um, AAA salaries have gone up by like a factor of three, let's say,
[00:28:20-00:28:20] right.
[00:28:20-00:28:25] So whatever the dollar value was, somebody made it in 2005, they make three times that
[00:28:25-00:28:30] now also though, team sizes have gone up because games have gotten more complicated, but also
[00:28:30-00:28:32] AAA is less good at making games.
[00:28:32-00:28:37] And just, there's this general bureaucracy that set in everywhere where people can't do
[00:28:37-00:28:38] stuff and team sizes have to get bigger.
[00:28:39-00:28:43] So team sizes have gone up by a factor of three.
[00:28:43-00:28:45] Let's say just an estimate.
[00:28:45-00:28:45] Right.
[00:28:46-00:28:53] And then even though you have more people and you're paying them more, it still takes longer to make a game.
[00:28:53-00:28:55] Let's say it takes like twice as long.
[00:28:55-00:28:55] Right.
[00:28:56-00:29:04] And so since 2005, you've got three times, three times, two factor of cost increase to make a game.
[00:29:04-00:29:04] Right.
[00:29:05-00:29:13] That's an 18 times games have become 18 times more expensive to make than they used to be in AAA, in AAA.
[00:29:13-00:29:13] Okay.
[00:29:13-00:29:24] So, so indie, indie has had actually some of the same, like once you're indie and you're like, there's a big difference between I'm indie and I just make the game by myself and I'm indie, but I hire a few people to help.
[00:29:24-00:29:41] Like once you start hiring people to help, you're subject to some of these factors that I just mentioned, but some of them, like the bureaucracy and stuff, you can sort of try to keep down on, but even like how much you pay people, like it's, it's hard to, you know, you can't find a good programmer for like.
[00:29:42-00:29:43] 120.
[00:29:43-00:29:47] $20,000, which for many people in the USA would be an amazing salary.
[00:29:47-00:29:47] Right.
[00:29:47-00:29:47] Yep.
[00:29:48-00:29:48] Yep.
[00:29:48-00:29:49] Like that just doesn't really exist.
[00:29:50-00:29:54] I mean, maybe that'll start to exist since there's been all, all these crashes.
[00:29:54-00:29:56] I don't know, but it's, it's just expensive, but yeah.
[00:29:56-00:30:12] So like if you had a factor of 18 increase in the cost to produce your product, imagine you made like toothpaste and then somehow, somehow the paste became 18 times more expensive for you to put in the tube.
[00:30:12-00:30:12] Yeah.
[00:30:12-00:30:13] Like that's insane.
[00:30:13-00:30:15] Your business would never survive.
[00:30:15-00:30:15] Right.
[00:30:15-00:30:17] And so that's kind of what happened to AAA.
[00:30:18-00:30:29] This was offset by the fact that, you know, the audience did grow over that time and games were making more money for a while, but that kind of stopped.
[00:30:31-00:30:42] And so I think there's just this crunch now where all of this is finally like things that are unsustainable have to end eventually.
[00:30:42-00:30:43] Sure.
[00:30:43-00:30:45] This is that right.
[00:30:45-00:30:48] So they're more expensive to make on the AAA side.
[00:30:48-00:30:48] Yeah.
[00:30:48-00:30:55] Uh, the expectations for the quality of the game, are they higher or lower today?
[00:30:55-00:30:57] I think they're much higher.
[00:30:57-00:30:58] You think they're lower?
[00:30:58-00:30:58] Well, okay.
[00:30:58-00:31:03] They're, they're higher than in, at the beginning of the period that I was talking about.
[00:31:03-00:31:03] Right.
[00:31:03-00:31:04] Yes.
[00:31:04-00:31:12] But if you look back at, you know, there's this meme on Twitter and stuff where people say like, this is a game from 10 years ago.
[00:31:12-00:31:16] And it's, it's like footage from whatever battlefield game was current.
[00:31:16-00:31:16] Oh, I know.
[00:31:16-00:31:17] Yeah.
[00:31:17-00:31:17] Yeah.
[00:31:17-00:31:18] And like, it looks better than anything.
[00:31:18-00:31:20] It does.
[00:31:20-00:31:20] Right.
[00:31:20-00:31:22] Well, it looks more artful at bare minimum.
[00:31:22-00:31:25] It, it looks, the artistry is better.
[00:31:25-00:31:32] So I saw some of these side-by-sides where it's like, they do the remakes and the remakes just look like they, they really do look like generative AI.
[00:31:32-00:31:39] And I'm not saying that they are, but like there was one, I can't remember what game it was from, but it was one of the, it was like a character swimming underwater.
[00:31:39-00:31:42] And the modern version was bright and.
[00:31:42-00:31:45] Clear and crisp.
[00:31:45-00:31:47] And the older version was moodier as darker.
[00:31:47-00:31:50] It was tinted green.
[00:31:50-00:31:55] Now this one technically looks better, at least in terms of fidelity, but this one feels better.
[00:31:55-00:31:56] You know what I mean?
[00:31:56-00:31:57] It was artful.
[00:31:57-00:31:58] Yeah.
[00:31:58-00:31:59] Yeah.
[00:31:59-00:32:02] So, I mean, I don't know.
[00:32:02-00:32:09] I, I think, I think there was a peak of average game quality.
[00:32:09-00:32:12] That was probably around 10.
[00:32:12-00:32:34] Maybe eight years ago, 10 years ago now, now, if you're talking again about indie and like how good is something that one person could make or whatever, I don't know if that's peaked, but I just mean, you know, big names by big teams, I think we're past the peak and that's also okay.
[00:32:34-00:32:40] So add to that factor of 18, if the quality of the game is like 0.7 of what it used to be, right.
[00:32:40-00:32:42] Multiply that into the equator.
[00:32:42-00:32:46] Divide, divide that in for like, how good is the game?
[00:32:46-00:32:49] People are, are able to play per unit cost.
[00:32:49-00:32:50] Right.
[00:32:50-00:32:59] So I, you know, I've been in the games industry a while though, and I've seen a lot of cycles happen and this is just another one.
[00:32:59-00:33:08] And so I'm not like panicking about it for me, we're sort of, we're sort of always off doing our own thing in a corner.
[00:33:08-00:33:11] Um, and because it takes so long, that's the.
[00:33:12-00:33:27] Funny thing about working on games that take forever is you sort of like go into a wormhole at the start of development and then you come out of the wormhole at the end and you're like, you know, especially for business reasons, you're like not really trying to sell people anything new in the middle.
[00:33:27-00:33:31] And so you don't have to figure out any of that stuff out in the middle.
[00:33:31-00:33:32] Yeah.
[00:33:32-00:33:40] Well, in a way, in a way, um, come, I'm about to release my game and, uh, coming out of the wormhole.
[00:33:40-00:33:41] Yeah.
[00:33:41-00:33:43] I feel irrelevant.
[00:33:43-00:33:47] I feel like I've missed a lot of trends.
[00:33:47-00:33:55] Cause I just been, you know, I've just been so focused on my own thing that I feel irrelevant.
[00:33:55-00:34:00] I don't, maybe that's not the right word, but maybe, maybe Edmund McMillan feels this way.
[00:34:00-00:34:08] I mean, I need to talk to him again, but like he's making games in flash and he's making basically flash games, you know, but, but he, he's not irrelevant.
[00:34:08-00:34:09] Obviously.
[00:34:09-00:34:10] Obviously.
[00:34:10-00:34:11] Yeah.
[00:34:11-00:34:12] Yeah.
[00:34:12-00:34:18] But he didn't, he didn't listen to the noise of the industry, you know, he just made what he wanted to make and you did the same thing, you know?
[00:34:18-00:34:19] Yeah.
[00:34:19-00:34:20] Well, it's different strategies, right?
[00:34:20-00:34:25] I think it is a viable, a viable strategy.
[00:34:25-00:34:31] If you want to run a business to look at what other people are making, oh, I can make that
[00:34:31-00:34:35] in two years, 18 months, I'll catch the tail end of the trend.
[00:34:35-00:34:36] Yeah.
[00:34:36-00:34:40] And then, and then you do that and you get some players, but, um, I mean, as a creative
[00:34:40-00:34:41] person.
[00:34:41-00:34:42] I've never wanted to do that.
[00:34:42-00:34:43] Right.
[00:34:43-00:34:44] That's not what drives me.
[00:34:44-00:34:50] And I think, I think a lot of the games by a lot of the games that people really appreciate
[00:34:50-00:34:53] are driven by creative people in that way.
[00:34:53-00:34:58] And so it's like, where do you want to be once, once the grand history of video games
[00:34:58-00:35:02] has been written with all the characters and all the positions, right.
[00:35:02-00:35:04] Where do you want to be in that thing?
[00:35:04-00:35:09] Do you want to be, I mean, you know, Farmville was a really successful game that made a ton
[00:35:09-00:35:10] of money.
[00:35:10-00:35:13] Do you want to be the guy that made Farmville or do you want to be the guy that made me
[00:35:13-00:35:14] eugenics?
[00:35:14-00:35:15] Right.
[00:35:15-00:35:16] Like, yeah.
[00:35:16-00:35:17] I don't know.
[00:35:17-00:35:18] Or do you want to be, I mean, eugenics is also successful.
[00:35:18-00:35:20] You could pick something.
[00:35:20-00:35:21] I don't know.
[00:35:21-00:35:25] You could pick some game that's like respected, but doesn't make a ton of money, but you lived
[00:35:25-00:35:26] off that.
[00:35:26-00:35:27] Right.
[00:35:27-00:35:28] Where do you want to be?
[00:35:28-00:35:32] I would much rather be on the, on the creative side, I've, I've never been a money driven
[00:35:32-00:35:39] person that said, because I have to pay for this team, you know, it's, I need to think
[00:35:39-00:35:40] about it.
[00:35:40-00:35:43] But again, you know, I try to, I try to separate these things.
[00:35:43-00:35:44] Right.
[00:35:44-00:35:48] So dude, if I was trying to make money, I would never may have made like a Sokoban game,
[00:35:48-00:35:49] right.
[00:35:49-00:35:51] With your own custom engine and custom language.
[00:35:51-00:35:52] Yeah.
[00:35:52-00:35:54] None of that makes any business planning sense.
[00:35:54-00:35:55] Right.
[00:35:55-00:35:56] Yeah.
[00:35:56-00:35:58] It's just like, what do I want to do?
[00:35:58-00:35:59] How do I get it done?
[00:35:59-00:36:04] And then once, once I've got it basically together, you know, like now it's like, okay,
[00:36:04-00:36:09] let's figure out how to show people that this is actually really cool.
[00:36:09-00:36:10] Yeah.
[00:36:10-00:36:14] And they might be interested in, in buying the game and playing it.
[00:36:14-00:36:18] And that has worked out every time it's starting to look like it's going to work out this time.
[00:36:18-00:36:22] It's a little too early to tell, but like we said, the responses to the demo were very
[00:36:22-00:36:23] positive.
[00:36:23-00:36:25] And so that's a good indicator, right?
[00:36:25-00:36:29] The wishlist number is going up still, by the way, the demo.
[00:36:29-00:36:31] So we had put this demo up in next fast.
[00:36:31-00:36:33] We thought we were going to take it down.
[00:36:33-00:36:34] I thought you were too.
[00:36:34-00:36:35] Yeah.
[00:36:35-00:36:39] But so, so valve put out an email that said, here's the timeline.
[00:36:39-00:36:40] Top games in next rest.
[00:36:40-00:36:43] And they sent emails to everybody saying, we're not an email.
[00:36:43-00:36:45] They put, they put a blog on steam or whatever.
[00:36:45-00:36:50] They sent us all emails and saying, don't take your game down because we're gonna, we're
[00:36:50-00:36:51] going to link it.
[00:36:51-00:36:52] And I was like, all right, we'll take that.
[00:36:52-00:36:57] And then we just decided to keep it up for a little bit for at least a few more weeks.
[00:36:57-00:37:00] So probably when this comes out, it'll still be up.
[00:37:00-00:37:02] You could play the order of the sinking star.
[00:37:02-00:37:05] So you're going to keep the demo out in perpetuity.
[00:37:05-00:37:08] I don't think in perpetuity we, we currently have plans.
[00:37:08-00:37:12] It's on what date we're going to take it down, but I don't want to say that because
[00:37:12-00:37:18] it's already changed before and like who, who knows, but like at least a few weeks from
[00:37:18-00:37:20] today, three or four weeks, maybe.
[00:37:20-00:37:21] And then we'll see.
[00:37:21-00:37:23] I took mine down yesterday.
[00:37:23-00:37:24] So yeah.
[00:37:24-00:37:26] It's concerning hearing you say that.
[00:37:26-00:37:27] Cause I just took it down.
[00:37:27-00:37:28] Well, it did.
[00:37:28-00:37:31] I mean, you're watching your own situation, right?
[00:37:31-00:37:32] So right.
[00:37:32-00:37:33] Right.
[00:37:33-00:37:36] I mean, our, our situation is different from yours because yours went up a long time ago,
[00:37:36-00:37:37] right?
[00:37:37-00:37:38] Yeah.
[00:37:38-00:37:44] I mean, it's sort of, it sort of capped out at like 1300 or 1100 reviews.
[00:37:44-00:37:48] So it did, it did well, but it's, it's one of those things, especially with a linear
[00:37:48-00:37:53] game where it's like, you, you don't want to give too much away in the demo, you know,
[00:37:53-00:37:54] you want it.
[00:37:54-00:37:55] It's like a movie.
[00:37:55-00:37:59] It's like, if somebody got to watch 15 minutes of a movie, is that a good thing or 30 minutes
[00:37:59-00:38:00] of a movie?
[00:38:00-00:38:01] I don't know.
[00:38:01-00:38:07] Another advantage I wanted to bring up to you on top of like your, you said that being
[00:38:07-00:38:08] a time capsule.
[00:38:08-00:38:13] There's a bit of an advantage because there's the, and maybe it's nostalgia.
[00:38:13-00:38:19] Maybe it's, maybe it's bringing, uh, a genre that people loved that they thought died,
[00:38:19-00:38:23] bringing it back to the forefront and resurrecting it in a new and special way.
[00:38:23-00:38:24] There's an advantage to that.
[00:38:24-00:38:28] But I also wanted to tell you, cause you were talking about, it's not a good business decision
[00:38:28-00:38:34] to be as, uh, like you did make your own engine and code your own, write your own language.
[00:38:34-00:38:36] It's not a good business decision.
[00:38:36-00:38:37] I don't know.
[00:38:37-00:38:43] I agree in the sense that the reason why people know your name is because you do that,
[00:38:43-00:38:44] you know?
[00:38:44-00:38:46] So your name carries a lot of weight.
[00:38:46-00:38:50] Now obviously you make good games, but like, I think half of the reason people know about
[00:38:50-00:38:56] you is because you, you say a lot of things and you also do a lot of things that most
[00:38:56-00:38:59] people don't want to do, you know?
[00:38:59-00:39:00] Yeah.
[00:39:00-00:39:05] Well, that's the paradox of at least the modern day and maybe, maybe this has been true through
[00:39:05-00:39:06] all of history.
[00:39:06-00:39:07] I don't know.
[00:39:07-00:39:12] If you're just like crassly commercially driven and you're like, I just want to make
[00:39:12-00:39:15] some money or whatever, and, or it doesn't even have to be crassly commercially driven.
[00:39:15-00:39:20] If you just go into it with the attitude, like, look, I just want to make some money
[00:39:20-00:39:21] off this thing.
[00:39:21-00:39:24] Cause I want to support my family or whatever, which is fine.
[00:39:24-00:39:25] Nothing wrong with that.
[00:39:25-00:39:26] Yeah.
[00:39:26-00:39:30] Then if you're not imaginative about how to do that, you're just going to look at like,
[00:39:30-00:39:33] Oh, what, what do people buy?
[00:39:33-00:39:35] That determines what I should make.
[00:39:35-00:39:36] What should it look like?
[00:39:36-00:39:37] What should it sound like?
[00:39:37-00:39:38] Right.
[00:39:38-00:39:39] And you're going to look at what's out there.
[00:39:39-00:39:43] And the thing is, there's all these other people pursuing the same strategy and they're
[00:39:43-00:39:45] just all going to look at what's out there.
[00:39:45-00:39:51] And then all of a sudden you're competing with who knows how many people following exactly
[00:39:51-00:39:52] the same strategy as you are.
[00:39:52-00:39:57] And so you would expect those people to produce very similar things, right?
[00:39:57-00:40:05] And so the, the paradox is that you can actually be much more successful, um, by deviating
[00:40:05-00:40:06] from that strategy.
[00:40:06-00:40:07] Right.
[00:40:07-00:40:13] Because it's, it's a very crowded strategy, um, and now, and, and so I get, I get the
[00:40:13-00:40:14] benefit of that.
[00:40:14-00:40:19] I do think the optimal, like if I wanted to make money, the optimal thing would be to
[00:40:19-00:40:25] be less creative and wacky than I am, but still somewhat creative and wacky.
[00:40:25-00:40:26] Right.
[00:40:26-00:40:31] Um, that at least that statement that I said about, about that being a very crowded strategy
[00:40:31-00:40:33] and being creative is helpful.
[00:40:33-00:40:37] Um, that has been consistently true through my entire time in the game.
[00:40:37-00:40:40] I've been in the game industry for a long time, but I think I've made a lot of progress
[00:40:40-00:40:41] in the game industry.
[00:40:41-00:40:42] And so I wouldn't expect that to change anytime soon.
[00:40:42-00:40:47] Um, if anything, it's more like that as time goes on, just because there's more and more
[00:40:47-00:40:49] and more people making games.
[00:40:49-00:40:50] Right.
[00:40:50-00:40:54] And so just standing out to people, what, why, I mean, this is always the question is
[00:40:54-00:40:57] like, why are people going to play your thing?
[00:40:57-00:41:00] If you spend all this time making it, what, what about it?
[00:41:00-00:41:02] Cause there's all these other things that they could play.
[00:41:02-00:41:04] So what about this thing that you're making?
[00:41:04-00:41:05] Yeah.
[00:41:05-00:41:06] Yeah.
[00:41:06-00:41:09] How do you get people's attention or inspire them?
[00:41:09-00:41:12] Like, oh, I can have fun with this thing in a way that I'm not having with other things
[00:41:12-00:41:17] or, or this is going to give me some kind of experience that I'm not getting from other
[00:41:17-00:41:18] things.
[00:41:18-00:41:19] Right.
[00:41:19-00:41:20] Sure.
[00:41:20-00:41:21] And I think it's, um, go ahead.
[00:41:21-00:41:22] Sorry.
[00:41:22-00:41:23] Well, I that's the end of the point.
[00:41:23-00:41:28] Well, I think it's a lot like, so people, certain people, I know certain people who
[00:41:28-00:41:33] have like a certain scent, uh, you, you get near them or, or, or their house, you go in
[00:41:33-00:41:36] their house and their house has a certain smell and it's natural.
[00:41:36-00:41:39] It's just the, it's just the, the musk of a person, right.
[00:41:39-00:41:43] And dogs in particular would, would, this would be amplified.
[00:41:43-00:41:44] Yes.
[00:41:44-00:41:48] When I think about a John Blow game, it's got a scent to it.
[00:41:48-00:41:49] Okay.
[00:41:49-00:41:52] It's it, you see it and you're like, yeah, this is a John Blow game.
[00:41:52-00:41:56] And I think it's because you're just doing it naturally.
[00:41:56-00:42:01] It's like, it's in your DNA to make a cozy puzzle game that has beautiful music and a
[00:42:01-00:42:03] really interesting story.
[00:42:03-00:42:05] It doesn't seem like you really.
[00:42:05-00:42:06] Yeah.
[00:42:06-00:42:10] It doesn't seem like you were just born with that scent for a game like that.
[00:42:10-00:42:15] That smell of your games is just, it just naturally comes out.
[00:42:15-00:42:17] Well, I wouldn't say I was born with it.
[00:42:17-00:42:22] I mean, I definitely had to develop it over time, but yeah, I mean, I think, I think it's
[00:42:22-00:42:28] noticeable what somebody's aesthetic is, even if it comes out differently from game to game.
[00:42:28-00:42:32] I mean, Edmund again is a super obvious example of this, right.
[00:42:32-00:42:35] And it's, it's more obvious in his case because he.
[00:42:35-00:42:38] He draws all the characters and the stuff.
[00:42:38-00:42:39] Right.
[00:42:39-00:42:43] But, but even so you could imagine if he wasn't drawing the art himself, but he was directing
[00:42:43-00:42:46] the game, it would still have this kind of sensibility.
[00:42:46-00:42:47] Yeah.
[00:42:47-00:42:50] About like, what is his kind of, it's very recognizable.
[00:42:50-00:42:51] Right.
[00:42:51-00:42:52] Yeah.
[00:42:52-00:42:57] Um, and I think, I think that's the case for, you know, a number of people in games.
[00:42:57-00:43:03] And if you have that, then that's one thing that, that an audience could look for for,
[00:43:03-00:43:05] Oh, I like the way he did that thing.
[00:43:05-00:43:06] Last time.
[00:43:06-00:43:07] Let's see.
[00:43:07-00:43:10] Let's see if this one is at least kind of like that.
[00:43:10-00:43:11] Yeah.
[00:43:11-00:43:12] Yeah.
[00:43:12-00:43:17] Any product that is some of the most incredible products and entertainment products that,
[00:43:17-00:43:23] that like have a legacy still have hundreds, if not thousands of flaws.
[00:43:23-00:43:26] So like last night I was watching gladiator.
[00:43:26-00:43:28] I haven't watched gladiator in a long time.
[00:43:28-00:43:30] It's a great movie.
[00:43:30-00:43:31] It's so flawed.
[00:43:31-00:43:33] Like I, I saw so many issues, especially with like color grading and, and the flashbacks.
[00:43:33-00:43:34] Yeah.
[00:43:34-00:43:39] And, and the frame rates and, and the editing choices were a little strange and I was shocked
[00:43:39-00:43:43] cause like last time I watched it when I was like 14, it was amazing, but I saw all these
[00:43:43-00:43:48] flaws and I immediately thought to myself, I think it was Ridley Scott who did it.
[00:43:48-00:43:49] Right.
[00:43:49-00:43:50] Yeah.
[00:43:50-00:43:51] Yeah.
[00:43:51-00:43:57] Um, if Ridley Scott had sent this out to thousands of beta testers to play, to watch this thing
[00:43:57-00:44:01] and they had a critical eye, they would list out hundreds, if not thousands of issues and
[00:44:01-00:44:03] he would have been bogged down, fixing all of these things.
[00:44:03-00:44:09] When in reality, it's like the, the movie is great regardless of the flaws.
[00:44:09-00:44:13] And so I'm sure, and this is where I sort of a segue into my next question to you.
[00:44:13-00:44:17] I'm sure there's hundreds, if not thousands of things that people have pointed out to
[00:44:17-00:44:21] you in the demo that you feel like you need to resolve.
[00:44:21-00:44:27] So my question is, what are you going to resolve and how are you parsing that feedback?
[00:44:27-00:44:28] Yeah.
[00:44:28-00:44:32] Well, there's actually not that many things, surprisingly.
[00:44:32-00:44:33] Hmm.
[00:44:33-00:44:38] That's one of the things that I would have thought is like, oh, there's going to be all
[00:44:38-00:44:43] sorts of, you know, different problems.
[00:44:43-00:44:47] The demo actually stood up very well considering the game's not done.
[00:44:47-00:44:53] We did get a few, so like I said earlier, okay, let's make it run faster on lower end
[00:44:53-00:44:54] systems.
[00:44:54-00:44:55] Okay.
[00:44:55-00:44:56] Not that hard.
[00:44:56-00:44:57] We've already done that.
[00:44:57-00:44:58] Can I ask for the solution?
[00:44:58-00:44:59] Is that really quick?
[00:44:59-00:45:00] What is the solution?
[00:45:00-00:45:03] Well, you know, when we start the game, we auto detect your hardware.
[00:45:03-00:45:08] It was already in for the demo and we just pick the rendering level, like low, medium
[00:45:08-00:45:09] or high.
[00:45:09-00:45:10] Right.
[00:45:10-00:45:15] And our real problem is that the low and medium were still pretty close to high in terms of
[00:45:15-00:45:16] just like what the features were.
[00:45:16-00:45:18] And we just needed to, well, there's two.
[00:45:18-00:45:22] So one is you can always just go optimize your system more overall and make everything
[00:45:22-00:45:23] faster.
[00:45:23-00:45:26] And we continue to do that.
[00:45:26-00:45:32] But secondly is just like, look, if it's a low end system, find a way, well, you don't
[00:45:32-00:45:38] want to be that serious that much visual degradation, but like, so, you know, our, our shaders
[00:45:38-00:45:42] are PBR, like physically based rendering shaders.
[00:45:42-00:45:49] And that involves doing a lot of math for relatively subtle lighting gradients on surfaces
[00:45:49-00:45:50] or whatever, let's say.
[00:45:50-00:45:51] Right.
[00:45:51-00:45:57] And so often you can just cut out large chunks of that kind of shader and you get something
[00:45:57-00:45:59] pretty close, you know?
[00:45:59-00:46:00] Yeah.
[00:46:00-00:46:02] And so, so we did some stuff like that.
[00:46:02-00:46:03] Basically.
[00:46:03-00:46:05] So, so that was one category of feedback.
[00:46:05-00:46:06] There's definitely.
[00:46:06-00:46:07] Okay.
[00:46:07-00:46:09] So example of conflicting things.
[00:46:09-00:46:12] Some people are like, oh, I really like the characters.
[00:46:12-00:46:15] Some people are like, I just want to play a puzzle game.
[00:46:15-00:46:19] I don't want any storytelling, right?
[00:46:19-00:46:22] After like every game that I make, everyone's like, can you have a more traditional story?
[00:46:22-00:46:28] And then now everyone's like, not everyone, but a few people and a, a small portion of
[00:46:28-00:46:29] the audience.
[00:46:29-00:46:30] Yeah.
[00:46:30-00:46:31] Is like, just let me play without the story.
[00:46:31-00:46:34] And that's actually something that's easy to put in the menu if you want that.
[00:46:34-00:46:35] Oh, sure.
[00:46:35-00:46:37] And so we're going to let people turn that off.
[00:46:37-00:46:42] Actually, you know, there's just some small percentage of people want to tweak the graphics
[00:46:42-00:46:43] by hand.
[00:46:43-00:46:47] I think most people just want the game to run and just want to play it.
[00:46:47-00:46:53] But some people are like, why can't I select the anti-aliasing level and put it on 2X in
[00:46:53-00:46:54] the menu?
[00:46:54-00:46:56] And it's like, okay, we can give you that kind of stuff.
[00:46:56-00:47:00] And just like, we didn't have separate volume controls for like sound effects and characters,
[00:47:00-00:47:01] and whatever.
[00:47:01-00:47:08] And so those kinds of things are, that's the vast majority of the feedback.
[00:47:08-00:47:14] There's a little, actually the other, the other piece of feedback is about controls.
[00:47:14-00:47:20] And this one's really confusing because sometimes I just have no idea what people want.
[00:47:20-00:47:21] Right.
[00:47:21-00:47:27] Is it the grid-based controls that they're, they want that with this kind of game?
[00:47:27-00:47:28] You have to have that, right?
[00:47:28-00:47:30] So, so just as a background, right?
[00:47:30-00:47:37] This is a grid-based game where you walk around and your character's always in a square because
[00:47:37-00:47:44] the genre of game is like objects in positions relative to each other do very specific things.
[00:47:44-00:47:51] And so when you're solving a puzzle, you want to be able to think about, I'm here, here's
[00:47:51-00:47:56] the, the beam projector with the beam of red light, and the monster is here two squares
[00:47:56-00:47:57] away.
[00:47:57-00:47:59] And the fact that it's exactly two squares is important, right?
[00:47:59-00:48:00] Yeah.
[00:48:00-00:48:03] It's a puzzle genre of game, puzzle, puzzle game.
[00:48:03-00:48:10] So you can't like stand 20% off center of the light projector and then push it.
[00:48:10-00:48:14] Like you might in a first person game where you're walking around continuously.
[00:48:14-00:48:16] That's just not how this kind of game works.
[00:48:16-00:48:21] So I think some percentage of people are complaining about that.
[00:48:21-00:48:25] They're complaining that they can't walk around freely on a 2D grid.
[00:48:25-00:48:30] And it's like, well, but that's, that's just not what this game is.
[00:48:30-00:48:38] And so I start to wonder, should I at least make that very clear, like, so as a developer
[00:48:38-00:48:42] and as someone who's played games my whole life, I'm like, okay, obviously you start
[00:48:42-00:48:45] playing the game and you move from square to square.
[00:48:45-00:48:46] Yeah.
[00:48:46-00:48:48] People are going to understand very quickly that that's this game.
[00:48:48-00:48:52] But now I'm like, maybe some people don't like, especially if you're playing with the
[00:48:52-00:48:58] analog stick, is it possible to not notice that your character always stops on a square
[00:48:58-00:48:59] in the middle of a square?
[00:48:59-00:49:00] No.
[00:49:00-00:49:04] They just think that it's like, you know, but, but then you have to remember like, oh,
[00:49:04-00:49:05] it's the internet.
[00:49:05-00:49:11] And like what, it sounds like a significant response, but like what percentage of players
[00:49:11-00:49:12] is this?
[00:49:12-00:49:13] And, and all that.
[00:49:13-00:49:14] Right.
[00:49:14-00:49:17] So, so now that's one category of thing there is okay.
[00:49:17-00:49:20] Because the game wasn't done yet.
[00:49:20-00:49:24] There is some stuff with controls that I legitimately was not satisfied with.
[00:49:24-00:49:29] So, so a couple of weeks before this, we went and we did demo to at Summer Game Fest, which
[00:49:29-00:49:30] people might have.
[00:49:30-00:49:37] Have seen, um, people probably saw the Jeff Keighley doing the show with all the trailers,
[00:49:37-00:49:41] but accompanying that there was like a live event where press and influencers would go
[00:49:41-00:49:42] play games.
[00:49:42-00:49:46] And so Nintendo had a booth showing off a bunch of third party switch to games and we
[00:49:46-00:49:52] were in there and it was the first time that anyone could play the game hands-on outside
[00:49:52-00:49:53] the company.
[00:49:53-00:49:54] Right.
[00:49:54-00:49:58] And so that was really cool, but I realized like, oh, most people are using the analog
[00:49:58-00:49:59] stick to move.
[00:49:59-00:50:03] That's just the convenient thing when you pick up a switch to, right.
[00:50:03-00:50:09] So for, for a game like this, I tend to like the D-pad because it's crisper, right.
[00:50:09-00:50:11] Sure.
[00:50:11-00:50:12] Down here.
[00:50:12-00:50:16] But it's also a little bit more awk cause it's like below your thumbs got to sort of
[00:50:16-00:50:21] be like in, and I think people just want to use the stick.
[00:50:21-00:50:22] Right.
[00:50:22-00:50:23] Yeah.
[00:50:23-00:50:28] And it's just so, so there were some ways in which the analog stick movement was less
[00:50:28-00:50:29] responsive than I would want.
[00:50:29-00:50:33] It's still, you know, totally playable, but it's like, oh, this could be, could be better.
[00:50:33-00:50:37] Would it help to have the value tweakable?
[00:50:37-00:50:38] Like the sensitivity?
[00:50:38-00:50:40] I don't think that's the really core.
[00:50:40-00:50:45] The core problem has to do more with this thing about it being a grid based puzzle game.
[00:50:45-00:50:46] Okay.
[00:50:46-00:50:49] So, so to go back to the grid based puzzle game thing, it's not just that when you're
[00:50:49-00:50:56] solving the puzzle, you think very clearly about the positions, but also like the gameplay
[00:50:56-00:50:59] engine, which I'm putting air quotes around.
[00:50:59-00:51:03] It really is one in this game has to make sure that the puzzles don't break no matter
[00:51:03-00:51:04] what you do.
[00:51:04-00:51:09] Like puzzles are designed so that like, oh, this thing levitates this object and that
[00:51:09-00:51:10] happened.
[00:51:10-00:51:15] When you push it out from under the thing will fall and you're not allowed according
[00:51:15-00:51:20] to the puzzle rules to like sneak some move in there between those two things happening
[00:51:20-00:51:23] or else puzzles break and you can exploit them and stuff.
[00:51:23-00:51:28] And because the puzzles in this game get very complex with very disparate.
[00:51:28-00:51:36] Sets of gameplay functionality all coming together, like that has to be really solid.
[00:51:36-00:51:43] And so so there's this whole system that makes sure that puzzles don't break basically.
[00:51:43-00:51:48] And that system is kind of why the analog stick was a little bit less responsive than
[00:51:48-00:51:49] we would want.
[00:51:49-00:51:50] I actually explained it in a video.
[00:51:50-00:51:55] I don't know that it's worth going into here, but we've since tweaked that and it's like
[00:51:55-00:51:57] much more responsive actually.
[00:51:57-00:51:58] And that's that.
[00:51:58-00:52:04] I think what what is worth going into is how you decided that that was worth solving.
[00:52:04-00:52:13] Because yeah, I saw I saw maybe a few negative comments about the player movement, but I
[00:52:13-00:52:19] don't think it was worth the time of day, you know, like especially when you sell this
[00:52:19-00:52:21] game for whatever you're going to sell it for.
[00:52:21-00:52:27] You're going to get people who actually know this genre as opposed to a free a free demo
[00:52:27-00:52:28] where.
[00:52:28-00:52:33] You know, 30% of the players don't even know that a grid based a grid based system like
[00:52:33-00:52:35] this is absolutely necessary.
[00:52:35-00:52:36] You know what I mean?
[00:52:36-00:52:37] Yeah.
[00:52:37-00:52:39] I mean, I don't know.
[00:52:39-00:52:41] You got to make these judgment calls as a developer, right?
[00:52:41-00:52:46] I what it comes down to is like I just personally when I was playing on the switch to well,
[00:52:46-00:52:49] OK, so things compound, right?
[00:52:49-00:52:55] So when the frame rate is high, things are more risk games are naturally more responsive,
[00:52:55-00:52:56] right?
[00:52:56-00:52:57] Because they see the input sooner and all that.
[00:52:57-00:52:58] Yeah.
[00:52:58-00:53:03] But like if you're on a system where the frame rate is low and that's making it a little
[00:53:03-00:53:08] less responsive and the analog stick is a little less responsive and people are using
[00:53:08-00:53:12] that, those things compound and it starts to be like, yeah, I really don't like how
[00:53:12-00:53:13] this feels.
[00:53:13-00:53:14] Right.
[00:53:14-00:53:18] And just as a developer, you decide what's important and how how important is that relative
[00:53:18-00:53:20] to other things you could be working on?
[00:53:20-00:53:21] Right.
[00:53:21-00:53:22] So.
[00:53:22-00:53:24] Well, I'll I'll wrap up here, Jonathan.
[00:53:24-00:53:26] The this game.
[00:53:26-00:53:27] Is.
[00:53:27-00:53:28] I love this game.
[00:53:28-00:53:34] And I was telling I was telling Rad, Rad, who's with your publisher before we started
[00:53:34-00:53:35] the call.
[00:53:35-00:53:37] He was like, have you played the game?
[00:53:37-00:53:40] And I was like, no, but I've watched hours and hours of it.
[00:53:40-00:53:45] And I said, it's because I can't I can't play these kind of games because I can't I can't
[00:53:45-00:53:46] solve the puzzles.
[00:53:46-00:53:48] I'm just not smart enough.
[00:53:48-00:53:51] Well, this game isn't that hard most of the time is what I would say.
[00:53:51-00:53:53] Well, then I'm real dumb.
[00:53:53-00:53:54] Well, OK.
[00:53:54-00:53:55] .
[00:53:55-00:54:02] But point being, I see this game as a like a really enjoyable game to just watch.
[00:54:02-00:54:06] I put it on with my wife while we were going to bed and we just put it on the TV and watched
[00:54:06-00:54:07] it.
[00:54:07-00:54:13] And to to sort of, you know, give you a few compliments about it, the music and the sound
[00:54:13-00:54:17] and I'm sure you you you replied to my tweet about the sound, but the sound and the music
[00:54:17-00:54:18] is a master class.
[00:54:18-00:54:22] I mean, just incredible.
[00:54:22-00:54:23] And I wanted to ask you before we wrap up here with sort of one final thought.
[00:54:23-00:54:24] Yeah.
[00:54:24-00:54:26] I want to ask you sort of one final thought.
[00:54:26-00:54:29] Was that soundtrack written live?
[00:54:29-00:54:30] Composed live?
[00:54:30-00:54:32] What do you mean by comp?
[00:54:32-00:54:33] Oh, you mean like.
[00:54:33-00:54:34] Or recorded live?
[00:54:34-00:54:40] OK, so as I'm actually not sure.
[00:54:40-00:54:48] What percentage of what's in the demo is live because we're we're still doing that process.
[00:54:48-00:54:53] There's actually more recording is going to happen in two weeks and we're going to put
[00:54:53-00:54:54] more stuff in.
[00:54:54-00:54:56] So, you know, the composers work.
[00:54:56-00:54:58] So first we talk about high level stuff.
[00:54:58-00:55:01] The composers work on the music.
[00:55:01-00:55:02] We get it in the game.
[00:55:02-00:55:03] We see how it feels.
[00:55:03-00:55:04] We're like, how is this?
[00:55:04-00:55:05] How is that?
[00:55:05-00:55:07] And it's like it's all MIDI the whole time.
[00:55:07-00:55:08] Right.
[00:55:08-00:55:12] So it's like just like generated instruments like you probably hear in the vast majority
[00:55:12-00:55:13] of games now.
[00:55:13-00:55:14] Right.
[00:55:14-00:55:15] Yeah.
[00:55:15-00:55:16] Software instruments.
[00:55:16-00:55:17] You're not A.I.
[00:55:17-00:55:18] Just so everybody's clear.
[00:55:18-00:55:19] It's not A.I.
[00:55:19-00:55:23] But like classic, you know, like you've had for 30 years or whatever.
[00:55:23-00:55:25] Yeah, of course.
[00:55:25-00:55:30] And then but they were like, hey, we think this would sound a lot better if we can live
[00:55:30-00:55:31] record it.
[00:55:31-00:55:33] And I was like, I agree.
[00:55:33-00:55:36] But man, that's expensive.
[00:55:36-00:55:40] But we decided to do it because it is better.
[00:55:40-00:55:45] And dude, there's a choice of studios and there's quite a price range.
[00:55:45-00:55:48] It could have gotten super, super, super expensive.
[00:55:48-00:55:51] But I was like, no, let's just.
[00:55:51-00:55:52] We don't have that much money.
[00:55:52-00:55:53] Let's just try to go with like.
[00:55:53-00:55:56] Like good musicians who can play.
[00:55:56-00:55:59] And well, you got to you got to pay.
[00:55:59-00:56:05] I would assume you're paying each musician or are you paying a studio?
[00:56:05-00:56:06] So how does it work?
[00:56:06-00:56:11] I'm sort of letting the composers deal with this, but there's kind of a hierarchical structure
[00:56:11-00:56:16] as far as I can tell, where you sort of tell the studio we need this many musicians and
[00:56:16-00:56:17] whatever.
[00:56:17-00:56:23] And they so, you know, the studio is located somewhere that you don't live, but they know,
[00:56:23-00:56:26] all the musicians that.
[00:56:26-00:56:30] They work with frequently and they get the right people in and and, you know, well, get
[00:56:30-00:56:33] them the score ahead of time and they practice and all that.
[00:56:33-00:56:34] And so, yeah.
[00:56:34-00:56:36] And all this is happening in Europe, by the way.
[00:56:36-00:56:39] So I'm just observing the recording from afar.
[00:56:39-00:56:42] I I was not I was not live at that.
[00:56:42-00:56:48] I was I was at the voice acting recording, but it came out really well, is what I would
[00:56:48-00:56:49] say.
[00:56:49-00:56:50] And it's beautiful.
[00:56:50-00:56:51] All I'm saying is just I'm not sure.
[00:56:51-00:56:52] I'm not sure.
[00:56:52-00:56:53] I'm not sure.
[00:56:53-00:56:54] I don't know what you mean.
[00:56:54-00:56:57] But at the demo, what percentage is live and what percentage is midi?
[00:56:57-00:56:59] But in the final game, it will all be live.
[00:56:59-00:57:00] Okay.
[00:57:00-00:57:02] Last last shotgun question for you.
[00:57:02-00:57:08] Are you surprised that these four games smashed together actually worked?
[00:57:08-00:57:11] No, because I picked them for that reason.
[00:57:11-00:57:14] I knew that you didn't pick random games you liked.
[00:57:14-00:57:17] You picked four games that you knew would work together.
[00:57:17-00:57:18] Yes.
[00:57:18-00:57:19] Okay.
[00:57:19-00:57:20] Yes, we.
[00:57:20-00:57:22] Well, it does work, man.
[00:57:22-00:57:30] huge huge congratulations for the demo being as successful as it has been yeah um great game i
[00:57:30-00:57:36] see it i see it having a a long life it's one of those evergreen games that just you sit down and
[00:57:36-00:57:43] you just play for years um yeah i mean i hope i hope people really enjoy it we we're still we're
[00:57:43-00:57:50] working really hard to get it done this year um it's a big game with so much stuff in it that
[00:57:50-00:57:59] i think people will really appreciate that yeah and yeah as you know if you haven't seen the demo
[00:57:59-00:58:04] you can check it out on steam you know you can watch a video like you're saying or it's just
[00:58:04-00:58:09] simple to download it and i i think what comes across so so for developers out there
[00:58:09-00:58:17] i think it's underappreciated the you know there's a more than the sum of its parts
[00:58:17-00:58:20] feeling that you get when different ingredients
[00:58:20-00:58:20] i think it's underappreciated the you know there's a more than the sum of its parts
[00:58:20-00:58:29] of a game all come together right so like you start the game the music is good the sound effects
[00:58:29-00:58:36] are good and by good i just mean they're not grating or annoying they have a rich sonic texture
[00:58:36-00:58:41] but they also invite a little bit of mystery like this is this is obviously part of something bigger
[00:58:41-00:58:47] that i haven't seen yet and the voice acting is good and the visuals are good and when you get
[00:58:47-00:58:55] all those things um the game really comes together and feels magical and yeah that all for us that all
[00:58:55-00:58:59] happened like this year like we've been working on this game forever right but it's all super rough
[00:58:59-00:59:07] drafty and all that yeah and it's crazy how that happens you just get this exponential uh growth in
[00:59:07-00:59:12] polish yeah and and that's part of the you know we said before there's uncertainty about how people
[00:59:12-00:59:16] are going to receive it and that's part of the uncertainty because you're not getting
[00:59:17-00:59:22] you i mean meaning the developer are not getting to see the good version of it until like
[00:59:22-00:59:28] a week before the demo goes live or whatever because we're racing to get all this stuff in
[00:59:28-00:59:34] there yeah and but no you you started up and it's like okay no i see what this thing is and it
[00:59:34-00:59:39] it makes sense it's funny because in the last podcast we did you were you were showcasing it
[00:59:39-00:59:46] and a lot of stuff broke a lot of stuff was breaking uh on your computer like i think
[00:59:46-00:59:47] things were loading and
[00:59:47-00:59:53] sounds weren't playing and oh yeah yeah and some of the scenes weren't dressed and that's game
[00:59:53-00:59:59] development for you i know i know and it's crazy how you just turned it into this frankly masterpiece
[00:59:59-01:00:05] just beautiful beautiful looking game okay links in the description everybody please play order the
[01:00:05-01:00:11] sinking star demo as long as it's out for i don't know how long it's going to be sometime some amount
[01:00:11-01:00:15] of time yep that's right jonathan thanks for your time dude this was fun thanks good talking to you
[01:00:15-01:00:17] again yep appreciate you
[01:00:17-01:00:22] bud cheers and by the way if you want to make 2d games or maybe even 3d games like i'm doing
[01:00:22-01:00:27] and potentially turn them into an actual full-time gig i have a course called full-time game dev
[01:00:27-01:00:32] and it's 50 off for the summer sale i've gone full-time with just a demo on three separate
[01:00:32-01:00:37] occasions and by the way look here these are some students who went full-time with the help of what
[01:00:37-01:00:42] i teach in this course you're going to learn just that how to land publishing deals with just a demo
[01:00:42-01:00:47] how to get funded on kickstarter with just a demo make a 2d or a 3d game in
[01:00:47-01:00:52] unity godot or unreal you're going to learn how to market your game get press coverage like i have
[01:00:52-01:00:57] hit the steam front page and so much more everything that i teach in this course is stuff
[01:00:57-01:01:01] i've done so you're learning from an actual indie game developer not somebody who's just
[01:01:01-01:01:06] wanting to make games i'll also throw in my 2d and 3d art courses completely free and as a bonus
[01:01:06-01:01:12] i'll also throw in a private one hour mastermind meeting with me and a handful of other developers
[01:01:12-01:01:16] where i'm going to answer any questions you have in a private setting this summer sale ends soon
[01:01:17-01:01:23] i don't do many of these during the year so be sure to click below to enroll and join 4500 other students
