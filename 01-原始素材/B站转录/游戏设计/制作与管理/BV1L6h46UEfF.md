---
title: "GDC25|原声|跨平台游戏开发:从手机到 PC 和主机的10个经验教训——Cross-Platform Game Development: 10 Lesson"
platform: bilibili
bvid: BV1L6h46UEfF
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-09-23 19:08:18
duration_sec: 1933
view: 188
like: 9
coin: 0
favorite: 3
reply: 1
danmaku: 0
share: 0
url: https://www.bilibili.com/video/BV1L6h46UEfF
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 48391
crawl_time: 2026-11-08 21:20:03


# GDC25|原声|跨平台游戏开发:从手机到 PC 和主机的10个经验教训——Cross-Platform Game Development: 10 Lesson

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-09-23 19:08:18
- **时长**: 32分13秒
- **播放**: 188 | 赞: 9 | 币: 0 | 藏: 3
- **链接**: https://www.bilibili.com/video/BV1L6h46UEfF

## 视频描述

原视频：https://www.youtube.com/watch?v=wUQ1hFp1_Zs
GDC演讲名：Company Building Lessons: Top Ten Learnings from Becoming a Cross-Platform Studio（公司建设经验：成为跨平台工作室的十大经验）
演讲者：Ian Fielding，Super Evil Megacorp
（202

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1L6h46UEfF
# 语言=en 时长=00:32:12 模型=large-v3

[00:00:08-00:00:13] So this is a talk for Super Evil Megacorp. My name is Ian Fielding and we're going to be talking
[00:00:13-00:00:19] about our journey from a mobile first studio to a cross-platform studio. The heart of the talk is
[00:00:19-00:00:24] really digging into 10 concrete lessons that we learned as we evolved from a mobile first to
[00:00:24-00:00:28] cross-platform studio. But ahead of that, I'm going to give a brief background about myself
[00:00:28-00:00:33] and also talk about our studio. I'll keep that short though so we can get into the 10 lessons.
[00:00:33-00:00:37] And then at the end, I'll talk about some future considerations for the industry around the
[00:00:37-00:00:41] cross-platform space. And there should be a little bit of time for Q&A as well. There should
[00:00:41-00:00:46] be about five minutes or so for that. So without further ado, I'll talk a little bit about my
[00:00:46-00:00:52] background. So I started at Super Evil in April 2021. I was the studio head for several years.
[00:00:52-00:00:58] I took on the CEO role in January of this year. My focus has stayed consistent though. I focused
[00:00:58-00:01:03] on culture, talent, strategy, and then expanding our game portfolio. I also try really, really hard
[00:01:03-00:01:07] to best our designers and our QA and play tests, but I often fail.
[00:01:07-00:01:12] But I do love our play tests, one of my favorite things about the studio. In the past, I worked on
[00:01:12-00:01:16] Valorant as a senior manager. I often call it a team of team leads. I also worked for many years
[00:01:16-00:01:21] on League of Legends. In the distant past, I worked at Insomniac Games and BuzzMonkey Software.
[00:01:21-00:01:26] I'm really passionate about company building. So hence the talk today. What I focus on is around
[00:01:26-00:01:31] company building, developing new leaders. And we try to pioneer something new with every game we
[00:01:31-00:01:36] take on, whether it's how we approach cross-platform development or something fresh with the game
[00:01:36-00:01:37] experience for our titles.
[00:01:37-00:01:43] On a personal note, I really love to spend time with my wife and our two dogs and cats. Our dogs are
[00:01:43-00:01:47] named Cloud and Aerith. I'm a huge Final Fantasy nerd. So if you're a fan of that, we can chat after
[00:01:47-00:01:48] about Final Fantasy.
[00:01:50-00:01:54] All right. And then for a brief, that's a brief overview of myself, but for a brief overview of
[00:01:54-00:01:58] Super Evil, so you can sort of contextualize the talk today, I'll talk about our mission, vision,
[00:01:58-00:01:59] and a little bit about the studio.
[00:02:01-00:02:07] So why we exist as a studio is to build amazing shared gaming moments. So all of our titles are
[00:02:07-00:02:11] co-op in nature. It's actually a big reason we wanted to expand across platform to bring more
[00:02:11-00:02:16] players together. One of my favorite moments at the studio and what really gets me up out in bed in
[00:02:16-00:02:22] the morning is helping connect players to have amazing experiences in games. Last year at the end
[00:02:22-00:02:27] of 2024, I was humbled to be able to participate in an LA independent games festival. And I worked
[00:02:27-00:02:32] the booth myself for a couple of days. And it was really amazing to be able to see players playing
[00:02:32-00:02:37] at that festival both days, connecting friends and family and our team and team splintered fate.
[00:02:37-00:02:41] And that would have been possible if we didn't expand across platform from mobile to on switch and
[00:02:41-00:02:46] PC and having those booths available. So it's really allowed us to deliver on our mission better
[00:02:46-00:02:51] to expand across platform. And then our vision as a studio is to build the best home for the best
[00:02:51-00:02:56] talent to push the boundaries of gaming for the long term. So as I mentioned earlier, every game we
[00:02:56-00:03:00] take on, we try and find something that's new and fresh with the game experience. And we really
[00:03:00-00:03:04] believe at the core of that is our talent. I always say that I work for the talent at the studio.
[00:03:04-00:03:07] I think that's really key. Even when you think about expanding,
[00:03:07-00:03:10] cross-platform is what is the talent that you're bringing in your studio. So I'll talk about that
[00:03:10-00:03:17] a little bit later in our 10 lessons. And then why did we expand to cross-platform?
[00:03:17-00:03:21] So first, a lot of people I think are focused on cross-platform right now,
[00:03:21-00:03:26] because the dollars and cents, the business aspect of it. It is true. There is a monetary
[00:03:26-00:03:29] opportunity to make more money by extending to more platforms. But I think that can be also a
[00:03:29-00:03:34] trap because if you don't start first thinking through the player experience and wanting to
[00:03:34-00:03:38] really make sure that when you expand to that new platform, you're building a game that's going to
[00:03:38-00:03:42] delight them, you can get into a trap. And then you get from players being for making a port or
[00:03:42-00:03:46] trying to make a cheap buck. So first and foremost, we actually thought through the player experience,
[00:03:46-00:03:49] what is going to delight them when we expand to these new platforms?
[00:03:50-00:03:54] We also really wanted to make sure that the experiences felt native. They felt like every
[00:03:54-00:03:58] SKU that we made felt like it was a first-class system for that platform. And as I mentioned
[00:03:58-00:04:03] earlier, we could bring more players together regardless of the platform or device they
[00:04:03-00:04:07] preferred to play on. And then for the titles we made in sort of showing our growth into cross-platform,
[00:04:08-00:04:12] the first title, and this was before my time, but a game that I really loved and played quite a bit
[00:04:12-00:04:16] myself was Vainglory. So that was the first mobile esport, really high-quality mobile title at this
[00:04:16-00:04:21] time when it came out. Still proud of that today. And then Callous Black, we evolved from that,
[00:04:21-00:04:26] which helped us create large-scale battlegrounds and also social drop-in, drop-out tech that we
[00:04:26-00:04:32] used for Teenage Mutant Ninja Turtles Splintered Fate. And this game, Splintered Fate, is going to
[00:04:32-00:04:36] be primarily the focus of the 10 learnings today. As we've expanded, this is our first time we've
[00:04:36-00:04:41] expanded from mobile to PC and then to Switch on console. And we're continuing to expand it this
[00:04:41-00:04:47] year to more platforms such as PlayStation, Xbox, and beyond. We're also working on a title with
[00:04:47-00:04:51] Netflix. That's Bloodline, a Rebel Moon game. So that's going to be launching later this year on
[00:04:51-00:04:57] the Netflix platform. And we have a cross-platform title, a prototype that's already playable,
[00:04:57-00:05:00] fully cross-platform. As of today, that's in the works as well, but that is announced.
[00:05:02-00:05:05] And then the last slide for just overviewing Super Evil, again, to contextualize the
[00:05:06-00:05:11] lessons is we're really focused on the long-term for cross-platform. We really have shifted now to
[00:05:11-00:05:15] make this our main focus from a mobile-first studio. Social play, we really believe in
[00:05:15-00:05:19] cross-play. And then transmedia, both helping players engage with our games in the core game
[00:05:19-00:05:24] and around the game as well. All right. So with that brief overview of myself and the studio,
[00:05:24-00:05:28] I'm going to dig into the 10 lessons. Hopefully, there's some concrete takeaways from you all for
[00:05:28-00:05:33] this talk. The first lesson I want to talk to you is actually being really, really mindful
[00:05:33-00:05:36] of hiring in your studio. So what I see
[00:05:36-00:05:40] a lot is that when people found new studios or even at long-lasting studios,
[00:05:40-00:05:44] people will hire a lot of their former colleagues, their friends that they've worked with,
[00:05:44-00:05:49] and similar backgrounds and similar experiences. And there can be value in that because if you
[00:05:49-00:05:52] worked with someone before, there's a good chance you know they're good, you know them well,
[00:05:52-00:05:56] that you can work well together. But it also can be a trap if you end up having the vast
[00:05:56-00:06:00] majority of your studio be your former friends or colleagues that may not bring a breadth of
[00:06:00-00:06:05] experience that you need to execute on your goals, especially if you're taking on new challenges. So
[00:06:06-00:06:10] Super Evil, having only shipped mobile games before, we were very deliberate in hiring in
[00:06:10-00:06:17] talent that actually came from AAA console and PC background, excuse me, or came from PC space as
[00:06:17-00:06:22] well. And that was really helpful for us because we were able to learn and take in learnings from
[00:06:22-00:06:27] their experience when it came to things like marketing for PC or console or building community
[00:06:27-00:06:30] or the specific controls and feel on those different platforms.
[00:06:31-00:06:36] And having that diverse experience really helped us broaden why we kept our mobile veterans as a
[00:06:36-00:06:41] well, complement them. So to get more specific in some of our hiring as an example, we brought in
[00:06:41-00:06:46] people who came from best in class studios. For example, in mobile as we were expanding cross
[00:06:46-00:06:51] platform and we wanted to improve our live ops and our telemetry and data, we went out and hired
[00:06:51-00:06:57] recently, a recent ish, a director of product that came from Zynga, who's really helped us level up
[00:06:57-00:07:03] in those spaces. We also brought in Daniel Stansons. He's someone who led design on Last Epoch,
[00:07:03-00:07:05] who I particularly saw. I played that game in fall.
[00:07:06-00:07:11] His journey as he helped drive community-oriented updates, taking learning from Discord on PC,
[00:07:11-00:07:15] which is different than sort of how you approach community-driven updates often with mobile.
[00:07:15-00:07:20] And he did a really good job building up Last Epoch. And so he's now leveled us up in how we
[00:07:20-00:07:24] engage with our Discord community and incorporate those learnings as we evolve Team T's Splinter
[00:07:24-00:07:28] Fate. He's done a great job. We have another update coming out really soon for Splinter Fate
[00:07:28-00:07:34] based on our community feedback in Discord. And then lastly, Cass Bumet. She came from Ubisoft
[00:07:34-00:07:35] and other studios where she worked. And she's a really good person. She's a really good person.
[00:07:35-00:07:39] She's worked on AAA, leading titles like Assassin's Creed. And she's really leveled
[00:07:39-00:07:44] us up in our production planning as we approach going to PlayStation and Xbox in terms of
[00:07:44-00:07:48] gotchas that we need to avoid, things we need to get ahead of for cert and working with those
[00:07:48-00:07:51] partners. So we're really deliberate. I haven't worked with any of these people before, but
[00:07:51-00:07:56] trying to take people who have worked in these areas and expand our skill set versus purely
[00:07:56-00:07:59] hiring people that we've worked with before that may not be the right fit for what we need for
[00:07:59-00:08:07] where we're going. Another lesson from a company building perspective is building into the new
[00:08:07-00:08:12] capabilities that you want to develop at your studio. So for us, something that really, really
[00:08:12-00:08:18] helped us was actually deciding to partner with Apple Arcade and Paramount as we expanded TNT
[00:08:18-00:08:24] Splinter Fate. So it was really helpful for us to be able to methodically build up, start walking
[00:08:24-00:08:29] before we were running in cross-platform development. Working with Apple Arcade, we were
[00:08:29-00:08:36] able to develop skills in launch on mobile, launch on Mac, PC essentially, and Apple TV as well. And
[00:08:37-00:08:43] we needed to develop the control scheme and feel for Apple TV. We needed to develop also the feel
[00:08:43-00:08:49] for PC and Mac on keyboard and mouse. And so we were able to start with that subset of platforms
[00:08:49-00:08:54] ahead of us actually evolving to PC and console. And so by a more focused set of experiences,
[00:08:54-00:08:58] we could really tailor it to those platforms, make sure it felt really good ahead of tackling more
[00:08:59-00:09:03] platforms. There is an alternative strategy where you can go with a big splash and launch on all
[00:09:03-00:09:07] platforms at once, but the risk is if you're trying to launch on six, seven SKUs at once,
[00:09:07-00:09:11] that you miss the mark. And then it can be challenging at launch to be able to optimize
[00:09:11-00:09:14] and respond to all that feedback. So we've been methodically growing into each platform,
[00:09:15-00:09:18] platform by platform, and that's been really helpful for us. And also really thankful,
[00:09:18-00:09:21] of course, because from a company building perspective, Arcade actually helped fund
[00:09:21-00:09:27] the base game of this ahead of us expanding and self-publishing to new platforms. They've been
[00:09:27-00:09:32] great partners. Another thing that's been really, really valuable for us, and I think it's one of
[00:09:32-00:09:37] the most important lessons from the talk, is being very, very deliberate in how you set up your play
[00:09:37-00:09:39] tests and your culture. So as I mentioned,
[00:09:39-00:09:43] earlier, I'm kind of fanatical about play tests and trying to make sure even leadership and
[00:09:43-00:09:47] everyone at the company attends play tests. And this is something we really had to up our game
[00:09:47-00:09:53] in as we evolved cross-platform. So our QA and design team works really closely together, along
[00:09:53-00:09:57] with production, to make sure there's detailed play test protocols when we have our company-wide
[00:09:57-00:10:01] play tests. And we try to run those once a week. And making sure people know that not only the
[00:10:01-00:10:06] areas of games that we're playing, but we have people who can test the game across console,
[00:10:06-00:10:09] PC, and mobile, and also with all the control schemes. So people who are playing
[00:10:09-00:10:13] with touch, people playing with a controller, keyboard and mouse, et cetera. And we even break
[00:10:13-00:10:17] people out into different Zooms based on their devices, based on their platforms that we're
[00:10:17-00:10:22] playing on. And then we will do post-play test surveys often, and we'll make sure we capture
[00:10:22-00:10:26] what platform they're playing on, what devices they're playing on, and then look at the feedback
[00:10:26-00:10:30] and see, like, are we hitting the mark across these various platforms and devices? And so
[00:10:30-00:10:34] taking this rigorous approach to play testing early in the product has really helped us catch
[00:10:34-00:10:45] issues and make sure we hit the mark when we launch. Let's give Laura one second. All right.
[00:10:46-00:10:50] Another area that's been really helpful, which relates to play testing, is de-risking your
[00:10:50-00:10:57] 3Cs early in development. So 3Cs being camera, character, and controls. So this, I think,
[00:10:57-00:11:03] is something that oftentimes studios wait really late in the game to de-risk. Oftentimes there's
[00:11:03-00:11:08] a lead platform and you wait until production to actually start testing your 3Cs. For us,
[00:11:08-00:11:11] we found it really, really valuable. Once you've found a kernel of fun and you've got your initial
[00:11:11-00:11:16] core loop in place, that you start actually ahead of your vertical slice, finalizing your vertical
[00:11:16-00:11:21] slice, test the 3Cs on the different platforms. And for us, doing this was immensely valuable
[00:11:21-00:11:26] ahead of going into full-scale production because it allowed us to uncover issues,
[00:11:26-00:11:31] how onboarding in your first-time user experience may be different per platform, how expectations
[00:11:31-00:11:36] around settings and menus, HUD, even just locomotion feel, and a lot of different UX things
[00:11:36-00:11:41] that we found by testing the 3Cs earlier ahead of production. So something I really recommend studios
[00:11:41-00:11:46] do versus waiting until you're halfway through production and then trying to retrofit those issues
[00:11:46-00:11:50] that can lead to a lot of added cost and risk to your development process.
[00:11:50-00:11:57] And the other thing is, this is how important small details are. I'll share a lesson where we
[00:11:57-00:12:01] actually really missed the mark, actually, and hopefully this can prevent some future pain
[00:12:01-00:12:06] for folks, is that the small details really can have a big impact on your initial reception. So
[00:12:07-00:12:16] apologies, bowing a little bit of a cough, so bear with me on that. This lesson about the small
[00:12:16-00:12:21] details is that we actually spent a lot of care working on controller field early on the product,
[00:12:21-00:12:22] even ahead of vertical slice. So that's one of the things that's really important.
[00:12:22-00:12:28] And even though we spent all of that effort and controller felt really like a first-class
[00:12:28-00:12:32] system, we even eventually won an award from Navigator for our control field for
[00:12:32-00:12:38] Splintered Fate, what happened is that we didn't indicate this in the HUD screen or anywhere really
[00:12:38-00:12:42] in the product, actually. We relied on the app store. And so on mobile and the app store,
[00:12:42-00:12:47] it's very easy to miss if a game actually supports controller. So when we launched Splintered Fate,
[00:12:47-00:12:52] the number one feedback point from players, most common, was we don't support controller. And
[00:12:52-00:12:52] controller is a big part of the game. It's a big part of the game. It's a big part of the game.
[00:12:52-00:12:52] And controller is a big part of the game. And controller is a big part of the game. And controller
[00:12:52-00:12:57] use on mobile and actually on PC as well has been growing over time. So it's now in the double
[00:12:57-00:13:02] digit percent, low double digit percent, but it's really meaningful. So we actually had to rush out
[00:13:02-00:13:06] a hotfix to inform players that we supported controllers. And so we put that we support
[00:13:06-00:13:11] controllers can now front and center in the home page. So it's hard to miss. We actually add it to
[00:13:11-00:13:15] the loading screen and then also tooltips. So there's three different ways we notify you that
[00:13:15-00:13:19] we support controllers. And that quickly alleviated the pain point. But that little detail actually
[00:13:19-00:13:22] was one of our biggest misses on launch. And so make sure that you have that in mind. And so
[00:13:22-00:13:27] make sure you pay attention to UX and make sure inform players that you actually did put in the
[00:13:27-00:13:33] work to support the way they may prefer to play. And then the next lesson is how important it is
[00:13:33-00:13:38] to align on your budget constraints really early on, especially if you're going cross-platform
[00:13:38-00:13:43] and you want to support older platforms. So for us, we had talked to Apple actually already at
[00:13:43-00:13:50] the beginning of supporting a phone all the way down to an iPhone 6 SE, which is a phone that's
[00:13:50-00:13:54] actually roughly 10 years old. So we had to be really mindful of this. And we had,
[00:13:54-00:13:58] we had aspirations also to extend to the Switch, which is about 8 years old at this point. So we had
[00:13:58-00:14:05] to be super, super mindful early on of our tech constraints. And so we had a lot of tricks that we
[00:14:05-00:14:10] thought about very early. And we aligned across the tech team, production, art, that we were going
[00:14:10-00:14:14] to leverage things like resolution upscaling. We actually built custom shaders and lighting very
[00:14:14-00:14:18] early on. And the other thing is it's not just about the tech constraints, but thinking through
[00:14:18-00:14:23] the player experience as well. Because we knew that we wanted to support not only touch, but we
[00:14:23-00:14:24] knew controller was becoming increasingly important. And so we had to be really mindful of that. And
[00:14:24-00:14:32] so we did things where you can actually very dynamically just with one press of a button on
[00:14:32-00:14:36] your controller Bluetooth, it will instantly recognize your controller play without having to
[00:14:36-00:14:41] restart the application. So even a lot of leading games, you actually have to go into settings,
[00:14:41-00:14:45] change the support controller and restart the application. But ours is totally fluid and dynamic
[00:14:45-00:14:49] and you can do that very easily. So these are all things that we had to think about really, really
[00:14:49-00:14:53] early to make sure we supported all these older devices. And you can save a lot of pain by doing
[00:14:53-00:14:53] so.
[00:14:54-00:15:01] And then related, quick follow-up from the last point, is just not forgetting last-gen consoles. So even for us,
[00:15:01-00:15:08] as we expand to PlayStation and Xbox later this year, we are looking at Gen 8 because recent market reports are
[00:15:08-00:15:17] showing that on PlayStation about PS4 still has about 40% of game hours versus PS5, which even though PS5 has
[00:15:17-00:15:21] been out for many years, there's still a lot of players who are choosing to play on their PlayStation 4.
[00:15:21-00:15:24] So for Xbox One, it still has a meaningful market share.
[00:15:24-00:15:29] So thinking about your budget constraints early and unless you want to be bleeding edge Triple-A, like it
[00:15:29-00:15:34] could be good to actually make sure you look at those platforms as well because they have such a
[00:15:34-00:15:35] meaningful market share.
[00:15:38-00:15:42] And then the other call which talks about earlier, a methodical approach to rolling out to new
[00:15:42-00:15:48] platforms, is we really didn't want players to just feel like it was a port. A port can kind of have good or bad
[00:15:48-00:15:51] connotations. There are good ports, but oftentimes when player referenced something that
[00:15:51-00:15:56] feels like a port, it actually is a bad connotation. That's because often when a game goes to a new platform there are
[00:15:57-00:15:59] on not only making it feel good, but does that audience
[00:15:59-00:16:01] and that platform have increased expectations
[00:16:01-00:16:02] in a certain way?
[00:16:02-00:16:06] So when we alluded to expanding Splinter Fate from Arcade
[00:16:06-00:16:09] to new platforms, players who had a Switch
[00:16:09-00:16:11] were bringing up a lot on our socials and our Discord
[00:16:11-00:16:13] that they're really hoping it had couch co-op,
[00:16:13-00:16:16] which we actually didn't have that feature for Apple Arcade.
[00:16:16-00:16:19] And so we made sure that by the time we launched on the Switch,
[00:16:19-00:16:21] we had full four-player couch co-op support.
[00:16:21-00:16:23] And I think if we didn't have that,
[00:16:23-00:16:24] we would have let down Switch players.
[00:16:24-00:16:26] So as you expand to new platforms,
[00:16:26-00:16:28] making sure, do you have the key features for that?
[00:16:28-00:16:30] And then for other platforms, there
[00:16:30-00:16:32] was things that we felt were really important.
[00:16:32-00:16:35] For example, on Apple TV, making sure we supported 4K support.
[00:16:35-00:16:38] Or on Steam, the Steam Deck continues
[00:16:38-00:16:40] to gain game hours and market shares.
[00:16:40-00:16:42] So we made sure we were fully optimized with the Steam Deck
[00:16:42-00:16:44] when we launched to Steam.
[00:16:44-00:16:46] And that's actually been over 10% of our game hours.
[00:16:46-00:16:49] And we think that will continue to go up as more people get
[00:16:49-00:16:50] gaming handhelds as well.
[00:16:50-00:16:52] So really making sure of those optimizations
[00:16:52-00:16:56] as you expand to new platforms.
[00:16:56-00:16:58] And the other things, adding on to that,
[00:16:58-00:17:01] to not overlook, is make sure you don't make
[00:17:01-00:17:02] the same mistakes twice.
[00:17:02-00:17:04] So we wanted to make sure we called out on PC,
[00:17:04-00:17:06] we support controllers, which still has a double-digit
[00:17:06-00:17:08] use percentage of players who aren't playing
[00:17:08-00:17:09] with keyboard and mouse.
[00:17:09-00:17:10] They're actually using controllers.
[00:17:10-00:17:13] So carry those learnings over from prior platforms.
[00:17:13-00:17:15] We took a lot of care when it came to the UX
[00:17:15-00:17:17] for these new platforms, including making sure
[00:17:17-00:17:19] we support Joy-Cons for the Switch.
[00:17:19-00:17:20] And also optimization.
[00:17:20-00:17:22] So especially for PC, we went really above and beyond
[00:17:22-00:17:24] to hit a low min-spec.
[00:17:24-00:17:26] We even sometimes look at the Steam community review
[00:17:26-00:17:28] and we'll fix issues for people below our min-spec
[00:17:28-00:17:30] as well, which has really helped us with our Steam rating
[00:17:30-00:17:32] and building goodwill with the community.
[00:17:32-00:17:35] And then a couple more points.
[00:17:35-00:17:38] So for point nine, one thing to call is it's not just
[00:17:38-00:17:41] about the development for your game when you expand
[00:17:41-00:17:43] cross-platform, but also marketing as well.
[00:17:43-00:17:45] And this is an area where I still feel like we're
[00:17:45-00:17:48] learning at Super Evil, but there's a never-ending
[00:17:48-00:17:50] quest to continue to level up your muscles to understand
[00:17:50-00:17:53] the different platform holders, but also channels that
[00:17:53-00:17:55] you can leverage cross-platform and how players actually
[00:17:55-00:17:58] engage with those differently, depending on the platform
[00:17:58-00:17:59] you're supporting.
[00:17:59-00:18:01] And so I really recommend that you bring in consultants
[00:18:01-00:18:02] to help in this area.
[00:18:02-00:18:04] Outside agencies can be really, really valuable.
[00:18:04-00:18:06] I'll just name a few that were really helpful for us
[00:18:06-00:18:08] as specific examples.
[00:18:08-00:18:12] Happy to talk shop after the talk as well about more
[00:18:12-00:18:13] folks that helped us out.
[00:18:13-00:18:15] But just a few to give shout-outs to that I think are
[00:18:15-00:18:16] really, really valuable.
[00:18:16-00:18:19] If you're launching on Steam or PC, the game Discover Co.
[00:18:19-00:18:22] newsletter by Simon Karras was really, really valuable.
[00:18:22-00:18:25] We got a lot of insights from their newsletter, which
[00:18:25-00:18:26] we subscribe to.
[00:18:26-00:18:28] They also have a new tool that they're just rolling out.
[00:18:28-00:18:32] Which has a lot of insights that you can use to look at
[00:18:32-00:18:34] other different competitors in your space.
[00:18:34-00:18:36] You get a lot of valuable insights from this tool.
[00:18:36-00:18:39] You can also see what tags they're using to optimize
[00:18:39-00:18:40] their Steam pages.
[00:18:40-00:18:42] And if you want to use some of those learnings to optimize
[00:18:42-00:18:44] your Steam pages, it's really, really important when you're
[00:18:44-00:18:46] launching on Steam and PC overall.
[00:18:46-00:18:49] We also worked with Caboodle, who helped us a lot with
[00:18:49-00:18:52] their short and long-term sale strategies, which becomes
[00:18:52-00:18:54] increasingly important as you launch on more and more
[00:18:54-00:18:55] storefronts.
[00:18:55-00:18:57] Even PC, it's not just Steam, but you have Epic Games
[00:18:57-00:18:58] stores.
[00:18:58-00:19:00] You have Humble Store, and you have other storefronts.
[00:19:00-00:19:02] And so they were really helpful in figuring out the right
[00:19:02-00:19:04] sales strategy per storefront.
[00:19:04-00:19:06] And then Game Dash was also really helpful for us.
[00:19:06-00:19:10] They helped us prepare for doing well in the Chinese market,
[00:19:10-00:19:12] which is really, really important.
[00:19:12-00:19:14] It's top five in terms of our audiences, at least for
[00:19:14-00:19:15] Splintered Fate.
[00:19:15-00:19:17] So they helped us with localization and marketing
[00:19:17-00:19:18] support.
[00:19:18-00:19:21] And then lastly is Neon Hive, who helped level up our Discord
[00:19:21-00:19:23] as we expanded to PC.
[00:19:23-00:19:25] And they gave us a lot of tips and tricks to get ready for
[00:19:25-00:19:30] that influx of players.
[00:19:30-00:19:33] Lastly, for the 10 lessons, when I talk to a lot of other
[00:19:33-00:19:36] independent studios, one thing that I've been surprised by is a
[00:19:36-00:19:39] lot of people actually don't take the time to build a direct
[00:19:39-00:19:42] in-person connection with the platform holders.
[00:19:42-00:19:44] Obviously, all of them have portals that you can use that
[00:19:44-00:19:46] are pretty easy to interact with, but I found it really,
[00:19:46-00:19:49] really valuable to actually go out there and talk with real
[00:19:49-00:19:53] people from Valve, Nintendo, PlayStation, Epic, Xbox, etc.
[00:19:53-00:19:55] They're really, really awesome people.
[00:19:55-00:19:58] And at conferences such as GDC, they're pretty much always
[00:19:58-00:19:59] hosting coffee hours.
[00:19:59-00:20:02] Valve has a coffee hour as an example at GDC.
[00:20:02-00:20:04] But other events that you can attend and you can meet people
[00:20:04-00:20:06] and talk through what you're trying to do.
[00:20:06-00:20:08] And I found them to be incredibly helpful at giving you
[00:20:08-00:20:11] tips on things like how to leverage their platform,
[00:20:11-00:20:13] you know, upcoming sales, even emergent opportunities
[00:20:13-00:20:16] sometimes when you talk to them directly about promotions
[00:20:16-00:20:17] for your title.
[00:20:17-00:20:19] So I really encourage, especially if you're in a studio
[00:20:19-00:20:21] leadership position or marketing, to build those in-person
[00:20:21-00:20:23] connections at these events.
[00:20:23-00:20:26] All right.
[00:20:26-00:20:27] And those are the 10 lessons.
[00:20:27-00:20:29] One more slide, then we'll have a few minutes for Q&A.
[00:20:29-00:20:34] So the last thing I wanted to call is that, you know,
[00:20:34-00:20:36] more titles are expanding cross-platform.
[00:20:36-00:20:39] Players' expectations are continuing to increase for
[00:20:39-00:20:40] titles that expand.
[00:20:40-00:20:42] But the bar is really going up.
[00:20:42-00:20:45] You do see often new games that are going either from mobile to
[00:20:45-00:20:49] PC and console or vice versa, PC console games going to mobile.
[00:20:49-00:20:52] And they end up getting flagged with being a port or they end up
[00:20:52-00:20:54] having significant challenges.
[00:20:54-00:20:57] So the hope is that these 10 lessons today give you some
[00:20:57-00:21:00] concrete takeaways that you can learn so that when you expand to
[00:21:00-00:21:02] those new platforms, players actually feel like it is truly a
[00:21:02-00:21:03] native experience.
[00:21:03-00:21:06] And just from a mindset perspective, it is easy just to
[00:21:06-00:21:09] look at the dollar and cents I know because if you're expanding
[00:21:09-00:21:12] to more platforms, obviously there's more players, bigger
[00:21:12-00:21:13] opportunity you can address.
[00:21:13-00:21:15] But try and have that mindset.
[00:21:15-00:21:17] I really encourage it of first and foremost, is this going to be
[00:21:17-00:21:19] something that really wins over players?
[00:21:19-00:21:21] And make sure in your play test and as you're developing the
[00:21:21-00:21:23] product, you're really thinking through that lens first and
[00:21:23-00:21:24] foremost.
[00:21:24-00:21:27] And I think that will lead you to commercial success in the
[00:21:27-00:21:30] long term.
[00:21:30-00:21:31] All right.
[00:21:31-00:21:32] So that's the talk for today.
[00:21:32-00:21:34] We have a little bit of time for Q&A still.
[00:21:34-00:21:35] I think seven minutes.
[00:21:35-00:21:36] So thanks, all.
[00:21:36-00:21:43] Yeah.
[00:21:43-00:21:45] So we also have a cross-platform game.
[00:21:45-00:21:47] It's on about four platforms.
[00:21:47-00:21:50] But it ended up costing us maybe more than we bargained for, I
[00:21:50-00:21:51] think.
[00:21:51-00:21:54] And I guess my question is, you know, going forward, it's hard
[00:21:54-00:21:57] for us to decide, you know, how to budget our time on all the
[00:21:57-00:21:58] different platforms.
[00:21:58-00:22:01] You know, so that's my question for you is, like, how do you
[00:22:01-00:22:03] decide where I'm going to spend this much time and money on
[00:22:03-00:22:05] mobile or PC or do you just do it equally?
[00:22:05-00:22:08] Or how do you kind of allocate resources between the different
[00:22:08-00:22:09] platforms?
[00:22:09-00:22:10] Yeah, that's a great question.
[00:22:10-00:22:13] So I'll just they asked to repeat it so other people can hear.
[00:22:13-00:22:16] So sort of, like, how do you figure out how much to allocate or
[00:22:16-00:22:17] invest per platform?
[00:22:17-00:22:20] And for me, I think that's going to depend on your studio, your
[00:22:20-00:22:21] product that you're making.
[00:22:21-00:22:24] I would say there's a lot of opportunities if you're open to as
[00:22:24-00:22:27] a studio to also do things like limited time exclusives or get
[00:22:27-00:22:30] additional funding support to help offset some of that risk.
[00:22:30-00:22:33] So as I mentioned, Arcade and Paramount were amazing partners
[00:22:33-00:22:34] for us in that.
[00:22:34-00:22:37] They actually funded our core development for launching on the
[00:22:37-00:22:38] Arcade.
[00:22:38-00:22:39] And then we expanded over time.
[00:22:39-00:22:42] And we took the risk to go to Switch and PC.
[00:22:42-00:22:44] But they offset the risk and helped cover that core development
[00:22:44-00:22:45] cost.
[00:22:45-00:22:48] There's a lot of other partners that offer deals such as Game Pass,
[00:22:48-00:22:51] you know, with Microsoft or other ways to offset the risk.
[00:22:51-00:22:54] And then for the game opportunity space, I think some of the tools I
[00:22:54-00:22:58] mentioned earlier, like Simon, Game Discover Co.
[00:22:58-00:23:01] or other can help inform how successful are similar
[00:23:01-00:23:04] products that you're making on that platform and look at that and
[00:23:04-00:23:05] just have an honest talk.
[00:23:05-00:23:08] Is it worth the effort to build new features and optimize for that?
[00:23:08-00:23:10] Versus what you forecast the return would be.
[00:23:10-00:23:11] Okay.
[00:23:11-00:23:12] Thanks.
[00:23:12-00:23:15] Gentleman over there.
[00:23:15-00:23:16] Okay.
[00:23:16-00:23:19] I want to ask how do you feel the difference of publishing and
[00:23:19-00:23:24] marketing a free-to-play mobile game versus PC console game that
[00:23:24-00:23:27] you need to convince people to buy it?
[00:23:27-00:23:28] That's a good question.
[00:23:28-00:23:31] So question was the difference between free-to-play and premium
[00:23:31-00:23:35] and then a little bit of nuance there, mobile and console.
[00:23:35-00:23:38] So I think there's some overlap that's similar and then some
[00:23:38-00:23:39] differences.
[00:23:39-00:23:43] I came from free-to-play in the past, working at Riot for many years.
[00:23:43-00:23:47] And there is a big need, I feel like, with free-to-play to keep,
[00:23:47-00:23:51] you know, ongoing engagement, large teams and players coming back.
[00:23:51-00:23:54] Whereas in retention is very, very important for that in your LTV
[00:23:54-00:23:55] career, right?
[00:23:55-00:23:58] At least our approach with TMNT has actually been more about
[00:23:58-00:24:00] regularity versus retention.
[00:24:00-00:24:04] So we tried to make a good splash when we launched the game on Switch.
[00:24:04-00:24:07] We were humbled to get support from Nintendo and also PC and Valve
[00:24:07-00:24:08] and Epic gave us some promotion.
[00:24:08-00:24:10] We did that.
[00:24:10-00:24:13] But then instead of trying to keep constant retention day-over-day
[00:24:13-00:24:15] because that's a really large team and really expensive to support that
[00:24:15-00:24:19] for live ops, we've tried to have spikes in engagement every few months.
[00:24:19-00:24:22] So to drive players to come back and then new players to buy our game
[00:24:22-00:24:23] gauging.
[00:24:23-00:24:27] So, for example, we launched last year Switch and PC.
[00:24:27-00:24:30] But then in February we launched a new DLC, which was a premium price.
[00:24:30-00:24:33] But the DLC actually helped promote the base game.
[00:24:33-00:24:35] So we increased base game sales.
[00:24:35-00:24:37] And also there was still really good attach rate.
[00:24:37-00:24:40] We actually had a little over 20% on Steam, which is really good for us
[00:24:40-00:24:41] in terms of people who bought DLC.
[00:24:41-00:24:45] So creating those moments every few months has kind of been our difference
[00:24:45-00:24:50] from free-to-play is that regularity and then marketing those beats.
[00:24:50-00:24:51] Thank you.
[00:24:51-00:24:52] Hi.
[00:24:52-00:24:54] Thanks for the presentation.
[00:24:54-00:24:55] Yeah.
[00:24:55-00:24:59] I guess my question is geared more towards the beginning of your presentation
[00:24:59-00:25:03] where you've mentioned that eventually you will end up with many SKUs across
[00:25:03-00:25:06] different platforms, generations, devices, et cetera.
[00:25:06-00:25:14] Later on you mentioned you've, let's say, customized the SKUs based on the platform's
[00:25:14-00:25:15] needs.
[00:25:15-00:25:22] So I guess my question is how do you tackle feature parity, cross-generation
[00:25:22-00:25:28] ownerships, cross-generation or cross-device progression?
[00:25:28-00:25:34] Is that something you take into account because the modern trend is to allow the player
[00:25:34-00:25:35] to continue playing World of Warcraft?
[00:25:35-00:25:37] To continue playing wherever he is.
[00:25:37-00:25:42] So at home he might play on Apple TV, then he continues on Nintendo Switch, and then
[00:25:42-00:25:46] when he gets home late at night he wants to play on Steam, for example.
[00:25:46-00:25:51] Is that something you take into account in cross-platform development?
[00:25:51-00:25:52] Yeah.
[00:25:52-00:25:54] I think there's a few questions within that.
[00:25:54-00:25:57] So I'm a big believer in one SKU for all platforms.
[00:25:57-00:26:00] There could be a reason, though, for a studio to not do that.
[00:26:00-00:26:04] So to clarify for us, even when we added new features like couch co-op for Switch,
[00:26:04-00:26:07] we actually did provide that to all platforms.
[00:26:07-00:26:10] So you can play couch co-op on arcade or you can play that on PC as well.
[00:26:10-00:26:14] It's just something we felt was particularly important to get in for that platform.
[00:26:14-00:26:16] We also support full cross-play.
[00:26:16-00:26:18] So someone on Switch could play on mobile or PC.
[00:26:18-00:26:21] And so them having the same SKU is really important for cross-play goals.
[00:26:21-00:26:23] And that aligns to our mission.
[00:26:23-00:26:27] Something I've been really fulfilled with for TMT is bringing players together across
[00:26:27-00:26:28] all the tribes.
[00:26:28-00:26:33] We don't currently support full cross-save progression across platforms.
[00:26:33-00:26:36] This time, there's sort of some platform challenges around that.
[00:26:36-00:26:41] But I would say that within ecosystems, we do support actually the cross-save capability.
[00:26:41-00:26:46] So for example, if you're on Steam, you can play at home on PC.
[00:26:46-00:26:48] But you can also take it on the go on a Steam Deck.
[00:26:48-00:26:50] Or you could play at home on your Apple TV.
[00:26:50-00:26:53] And you could take that progression on the go on your iOS or iPad.
[00:26:53-00:26:57] So within those specific ecosystems, we do have full cross-save capability as well.
[00:26:57-00:26:58] OK.
[00:26:58-00:26:59] Makes sense.
[00:26:59-00:27:03] Thank you.
[00:27:03-00:27:05] Thank you, Ian, for a very concrete and tangible talk.
[00:27:05-00:27:09] We've been investing in super small teams.
[00:27:09-00:27:13] They are super evil and super cool, but definitely not megacorps.
[00:27:13-00:27:17] Super small teams in Latin America and other emerging markets.
[00:27:17-00:27:24] How advisable and how easy is, in your vision, for them to plan with all the augmentation
[00:27:24-00:27:32] that AI tools, no-code tools, 3D asset AI generate, et cetera, et cetera.
[00:27:32-00:27:34] How realistic and advisable is that?
[00:27:34-00:27:43] And advisable is for these three, seven people teams to think cross-platform at this point?
[00:27:43-00:27:47] I think that really depends on the studio, the team, the talent.
[00:27:47-00:27:48] I'm rooting for everyone.
[00:27:48-00:27:52] So if a small team is able to extend cross-platform, there's been some examples of those.
[00:27:52-00:27:55] Maybe it takes longer if it's a smaller team to get there.
[00:27:55-00:27:58] I'm not going to comment too much on the AI trend.
[00:27:58-00:28:02] I would say just at a very high level, I think it can help accelerate progress.
[00:28:02-00:28:04] We personally don't use AI, though, for any assets.
[00:28:04-00:28:06] It's super evil for disclosure.
[00:28:06-00:28:11] But there may be ways, again, for efficiency gains through that for smaller teams as well.
[00:28:11-00:28:13] So that would be my goal.
[00:28:13-00:28:17] But the other thing I would just add on to that for a small team is the methodical growth strategy
[00:28:17-00:28:22] may be better for a small team than trying to launch on six, seven SKUs at once.
[00:28:22-00:28:24] So we were a lot smaller.
[00:28:24-00:28:27] For context, at super evil four years ago, we were actually 30 people.
[00:28:27-00:28:28] Now we're a bit bigger.
[00:28:28-00:28:29] We're around 100.
[00:28:29-00:28:33] But because we were a lot smaller back in the day and trying to support a couple products,
[00:28:33-00:28:35] that's why I felt the methodical approach was good.
[00:28:35-00:28:38] So we started arcade and just a few SKUs.
[00:28:38-00:28:40] And then now we've added Switch.
[00:28:40-00:28:41] We've added PC.
[00:28:41-00:28:43] And we're going to be adding Xbox and PlayStation.
[00:28:43-00:28:45] So for a smaller team, maybe it makes sense to go that route.
[00:28:45-00:28:46] Thank you.
[00:28:46-00:28:50] Hello.
[00:28:50-00:28:53] Thank you so much for giving such a nice, insightful talk.
[00:28:53-00:29:00] I was wondering if you could give a little bit more insight into how you pick which platforms to expand to next.
[00:29:00-00:29:04] As someone who started on mobile games, is there something that you were looking for in the next console?
[00:29:04-00:29:05] I know you said that it was mobile.
[00:29:05-00:29:09] I know you said that it was hard to launch across multiple platforms.
[00:29:09-00:29:15] So I was wondering if you could maybe give a little bit of insight on how you choose which platform to expand to next.
[00:29:15-00:29:16] Yeah, that's great.
[00:29:16-00:29:17] Well, thanks for the kind words.
[00:29:17-00:29:20] And the question was just how do we pick the platform expansion order.
[00:29:20-00:29:23] So it was a combination of a few things.
[00:29:23-00:29:28] We were looking at the game we had, the IP we have, and the opportunity size.
[00:29:28-00:29:33] So for Team Indie Splinter Fate, we really felt that playing on –
[00:29:33-00:29:35] there's just a ton of demand from our players.
[00:29:35-00:29:36] So we launched an arcade.
[00:29:36-00:29:38] We heard the Switch audience being very, very vocal.
[00:29:38-00:29:40] And they were also calling out they wanted couch co-ops.
[00:29:40-00:29:42] So we did have to add that feature for them.
[00:29:42-00:29:47] But we felt like that would probably be the biggest opportunity size for this game because it's also very family-friendly oriented,
[00:29:47-00:29:50] which we think is great for the Switch platform.
[00:29:50-00:29:52] You can play it as kids, very appropriate for that content.
[00:29:52-00:29:54] But parents also enjoy the IP.
[00:29:54-00:29:56] So we felt that was a really big opportunity.
[00:29:56-00:29:57] We talked to Nintendo.
[00:29:57-00:30:01] They were willing to give us some additional promotion support as well.
[00:30:01-00:30:03] So that was big as well to bring it to them.
[00:30:03-00:30:06] We were really excited about that partnership that we had with them.
[00:30:06-00:30:09] So that was – opportunity size, I would say, was the reason we went with Switch first.
[00:30:09-00:30:14] But then Steam, we felt, was the next most important one for us from an opportunity perspective.
[00:30:14-00:30:19] We also wanted to line it up with the winter months, really important, the winter sales, and be out before that.
[00:30:19-00:30:23] And we also are big fans of the Steam Deck, something that our engine does really well.
[00:30:23-00:30:28] I think, humbly, our talent is really good at optimizing for those more portable or constrained devices.
[00:30:28-00:30:32] And so we felt it would be a great game on the Steam Deck along with bringing it to PC.
[00:30:33-00:30:35] But we do want to get it on all platforms.
[00:30:35-00:30:41] And I don't want to make it sound like any platform won't be – we won't try to treat that like a first-class player experience.
[00:30:41-00:30:43] And so we will get it on PlayStation and Xbox later this year.
[00:30:43-00:30:44] Got it.
[00:30:44-00:30:45] Thank you so much.
[00:30:45-00:30:46] Yep.
[00:30:46-00:30:47] Thanks.
[00:30:47-00:30:48] Hello, Ian.
[00:30:48-00:30:49] Nice talk.
[00:30:49-00:30:50] Thank you.
[00:30:50-00:30:56] And then my question is, in order to launch on all these platforms, hardwares, generations, systems,
[00:30:56-00:31:02] how often do you have to, like, compromise the game features, like some cool stuff?
[00:31:02-00:31:03] In your game?
[00:31:03-00:31:06] Let me think about that.
[00:31:06-00:31:07] So the question – thanks for the question.
[00:31:07-00:31:12] The question was, do we have to compromise features for cross-platform?
[00:31:12-00:31:19] To be honest, I actually feel like expanding cross-platform had the inverse expect – inverse from that,
[00:31:19-00:31:25] where when we wanted to expand to new platforms, we actually felt like we really needed to add new features versus not have them.
[00:31:25-00:31:29] So as I mentioned, Switch, like Couch Co-op, if we didn't extend to Switch, I'm not sure if we would have done that.
[00:31:29-00:31:32] We just felt it was really, really critical for that platform.
[00:31:32-00:31:33] It pushed us in certain ways.
[00:31:33-00:31:37] It pushed us in certain ways to really care even more about mainstream controller.
[00:31:37-00:31:39] It was a first-class experience, obviously, as we expanded to console.
[00:31:39-00:31:45] So for us – and we have a great team, so there hasn't been so far a feature that I feel like when we wanted to add it for one platform,
[00:31:45-00:31:50] we were like, oh, this is really going to make us – we won't be able to add this feature for other platforms.
[00:31:50-00:31:51] Okay. Thank you.
[00:31:51-00:31:57] All right.
[00:31:57-00:31:59] I think we're a little bit over, so we're going to wrap now.
[00:31:59-00:32:01] Reminder to fill out the survey after, and thank you all for attending the talk.
[00:32:01-00:32:02] Appreciate it.
