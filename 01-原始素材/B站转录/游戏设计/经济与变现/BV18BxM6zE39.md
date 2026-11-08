---
title: "GDC26|Steam增长战略内幕：每日特惠、用户评论和开发者工具详解——Inside Steam's Growth Strategy: Daily Deals"
platform: bilibili
bvid: BV18BxM6zE39
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-10-27 14:15:24
duration_sec: 1910
view: 242
like: 11
coin: 1
favorite: 7
reply: 1
danmaku: 0
share: 1
url: https://www.bilibili.com/video/BV18BxM6zE39
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 49747
crawl_time: 2026-11-08 21:20:01


# GDC26|Steam增长战略内幕：每日特惠、用户评论和开发者工具详解——Inside Steam's Growth Strategy: Daily Deals

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-10-27 14:15:24
- **时长**: 31分50秒
- **播放**: 242 | 赞: 11 | 币: 1 | 藏: 7
- **链接**: https://www.bilibili.com/video/BV18BxM6zE39

## 视频描述

原视频：https://www.youtube.com/watch?v=h1ivZzEyNFY
（2026年9月9日）来自平台官方团队的分享，带你掌握面向业内顶级平台开发游戏的前沿见解。
在这场 2026 年 GDC 游戏盛典演讲中，Valve 公司 Steam 团队传播负责人凯西・艾奇逊・博伊尔（Kaci Aitchison Boyle）与 Steam 商务负责人汤姆・贾尔迪诺（Tom Giar

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV18BxM6zE39
# 语言=en 时长=00:31:49 模型=large-v3

[00:00:02-00:00:08] We should start by saying thanks for taking time out of a busy GDC to come and talk with us.
[00:00:09-00:00:15] Really appreciate you guys showing up. My name is Tom Giardino, and I started working at Valve in 2012.
[00:00:15-00:00:22] I'm on the Steam business team, so that means almost my whole job revolves around talking to developers and publishers,
[00:00:22-00:00:27] like all of you, and then talking to the engineers and developers and designers at Valve
[00:00:27-00:00:32] who are making and shipping Steam features and tools, and this is my colleague Casey.
[00:00:32-00:00:37] What's up? Wow, I made it two seconds. My name is Casey.
[00:00:37-00:00:40] We have a strict no dancing rule for Casey, and she's not.
[00:00:40-00:00:44] When I told my colleagues I wanted to do this talk, they were like, can you not dance?
[00:00:44-00:00:47] I was like, yeah, I can not dance, and I just made it not even a minute.
[00:00:47-00:00:52] So my name is Casey, as I mentioned. I work in communications on the Steam business team
[00:00:52-00:00:57] and then across Valve on a bunch of other teams from Steam hardware to the gaming teams,
[00:00:57-00:01:01] anything that deals with communicating with developers, with players, and everywhere.
[00:01:02-00:01:05] We're in between, and I know that we're going to be talking a lot about documentation
[00:01:05-00:01:10] and mentioning different resources, and we kind of wanted to reassure you you don't have to write all of it down.
[00:01:11-00:01:17] We have a QR code at the end so that you can click on that and get all the information that you need from there.
[00:01:17-00:01:22] Yeah, we'll start with kind of a brief outline, just a little bit of what we're going to be going over today.
[00:01:22-00:01:27] We have a little bit of data and updates about Steam in 2026, and then we want to spend a little bit of time
[00:01:27-00:01:32] talking about our approach to solving problems and what that means for devs,
[00:01:32-00:01:36] and players. To pause on that for a second, I think a lot of our talks and presentations,
[00:01:36-00:01:39] we've been very like, here's what we shipped, here's when it happened, here's the next thing.
[00:01:40-00:01:44] And we got some feedback and suggestions that we should pause a little bit and really break into
[00:01:44-00:01:49] some of the trade-offs we're making, how we thought about something, or the process we went through.
[00:01:49-00:01:54] So we'll spend a little extra time on that. We have a little bit of advice and guidance throughout the talk,
[00:01:54-00:01:59] but I think the final quarter is really just specific, like things you can do for your game,
[00:01:59-00:02:01] or your publisher, or your developer studio.
[00:02:02-00:02:05] In the short term, to make the most of the opportunity on Steam.
[00:02:05-00:02:10] And even though the title of this talk and everything about it is Steam and how Steam is doing,
[00:02:10-00:02:15] the real measure of how Steam is doing is how developers are doing, how you are all doing,
[00:02:15-00:02:19] as well as how players, your customers on Steam, are doing.
[00:02:20-00:02:22] As developers, you're the ones who have the hard job, right?
[00:02:23-00:02:25] You're the ones that have to manage the success of your game.
[00:02:25-00:02:28] You have a lot of different work to do to make that happen.
[00:02:28-00:02:30] And for everybody in the room, that's going to look different.
[00:02:30-00:02:31] Everybody's making a different game.
[00:02:32-00:02:34] You're making a different game for different people.
[00:02:34-00:02:37] So the measure of that success is going to vary among everyone.
[00:02:37-00:02:42] But it's our job, as members of the Steam team, to help connect your games with players.
[00:02:42-00:02:48] Which means every decision that we make is all about balancing what you care about as developers
[00:02:48-00:02:52] with what players, the ones you want buying your games, care about.
[00:02:52-00:02:56] Yeah, and that's gotten, I think, a lot more important as the years go by,
[00:02:56-00:03:00] because there are just so many more games coming out on Steam.
[00:03:00-00:03:02] It's more important than ever that we do that.
[00:03:02-00:03:04] This is sometimes kind of the elephant in the room.
[00:03:04-00:03:09] I hear this all the time from devs as a cause of consternation or stress or anxiety.
[00:03:09-00:03:12] Hey, there's so many games coming out every day on Steam.
[00:03:12-00:03:13] Like, how do I break through?
[00:03:13-00:03:15] We want to talk about some of that stuff.
[00:03:15-00:03:21] But the number of games rising also corresponds with a really healthy increase in the number of players on Steam as well.
[00:03:21-00:03:25] There are way more people on Steam buying and playing games now than ever before.
[00:03:25-00:03:28] Here's what that looks like in raw numbers.
[00:03:28-00:03:31] Just a few weeks ago, we passed the 42 million mark.
[00:03:31-00:03:37] For peak concurrent users, that's just the count of people who have the Steam client running.
[00:03:37-00:03:43] If you're like me, sometimes the Steam client is running on your PC even if you're not shopping for a game or buying a game.
[00:03:43-00:03:46] So we also track the in-game concurrence.
[00:03:46-00:03:50] That just hit a new record recently of 13.9 million users.
[00:03:50-00:03:56] And just to put those numbers into context, if you go back about five years to the 2020 phase,
[00:03:56-00:04:00] this is about double the number of peak concurrence and in-game users from five years ago.
[00:04:00-00:04:03] That growth is good news, right?
[00:04:03-00:04:09] It's our job to try to make the opportunity bigger on Steam and make the opportunity for your next game bigger.
[00:04:09-00:04:12] And this is kind of where we want to pause a little bit.
[00:04:12-00:04:19] There's something really important to frame about that growth and those numbers and how our team at Valve thinks about the platform.
[00:04:19-00:04:26] A lot of companies are structured in a way where the numbers and the growth and number go up is kind of the driving force, right?
[00:04:26-00:04:30] To be really direct, decisions that are made around a quarterly or a monthly basis,
[00:04:30-00:04:35] whether it's an earnings call or a stock price or whatever is trending on Wall Street at the moment, line go up.
[00:04:35-00:04:41] That structure of problem solving creates a lot of short-term thinking and a lot of short-term incentives,
[00:04:41-00:04:48] sometimes incentivizes decisions that aren't necessarily great for players or for long-term sustainability of a platform.
[00:04:48-00:04:50] Valve is pretty different.
[00:04:50-00:04:52] We're a relatively small company in terms of headcount.
[00:04:52-00:04:53] We are private.
[00:04:53-00:04:54] We don't have investors.
[00:04:54-00:04:56] We don't have a stock price.
[00:04:56-00:04:59] And we don't have impossible expectations around infinite growth.
[00:05:00-00:05:04] So, if you're one of the people you might know, that was the worst transition ever.
[00:05:04-00:05:05] It's you!
[00:05:05-00:05:06] You guys.
[00:05:06-00:05:10] We really only answer to developers and players and that's it.
[00:05:10-00:05:16] So, that means we're much more interested in investing in our relationships with you and your relationships with Steam in the long term.
[00:05:16-00:05:23] And on Steam, that means we're freed up to make decisions based on exactly what your happiness is looking like.
[00:05:23-00:05:28] If you tell us you're not happy, we're incentivized to try to fix that and work on it.
[00:05:28-00:05:30] And we don't have to balance any of that at all.
[00:05:30-00:05:32] So, we work with the agenda of advertisers.
[00:05:32-00:05:34] We don't have advertisers.
[00:05:34-00:05:36] We don't have paid placements of any kind.
[00:05:36-00:05:38] And we do that on purpose.
[00:05:38-00:05:46] We think that we can actually provide a much better experience for customers on Steam if we're showing them games that we think they're likeliest to be interested in.
[00:05:46-00:05:54] Which means, I mean, let's just say it seems kind of weird if you're trying to compare us to a traditional business model because it's not.
[00:05:54-00:05:59] We literally only exist if we can continue to be a place that both developers and players want to be.
[00:05:59-00:06:01] Yeah, exactly.
[00:06:01-00:06:09] And I think at this point, Steam has gotten so broad and so global that it's really hard to balance kind of the needs and interests of all those people at once.
[00:06:09-00:06:12] This is a satellite map of our users.
[00:06:12-00:06:20] So, every green dot on this map represents somebody connecting to Steam servers to buy and play games, upload builds, and so on and so forth.
[00:06:20-00:06:23] We shared maps just like this over the years.
[00:06:23-00:06:27] And this is a public map you can see in our Steam hardware survey if you're ever curious.
[00:06:27-00:06:29] You'll watch it, you know, change.
[00:06:29-00:06:31] It's a map you can see season by season.
[00:06:31-00:06:36] And if you go back five or even ten years, there's a lot of green on this map that didn't used to be there, right?
[00:06:36-00:06:46] I don't think a lot of PC devs typically think of territories like India or Japan or Indonesia or Brazil or Peru as big opportunities for PC games a decade ago.
[00:06:46-00:06:49] But a ton of growth on Steam has happened there.
[00:06:49-00:06:55] Meanwhile, I think North America, Western Europe, sort of traditionally incumbent stronger markets have continued to grow, which is really interesting.
[00:06:55-00:06:58] So, when you're talking to 42 million people at the same time,
[00:06:58-00:07:06] there's a huge variety of tastes and preferences and expectations and a huge range of games that are actually finding success, which is really exciting.
[00:07:06-00:07:11] Which is fine for us to say, but we thought it would be helpful if we showed you what we mean by this with an example.
[00:07:11-00:07:16] So, what you're looking at here on the screen, this is the top new releases on Steam in January.
[00:07:16-00:07:27] So, in one single month, you're seeing everything from zombies and base building cults to funny RPG escapes, stylized indie adventures, casual walking sims,
[00:07:27-00:07:29] and everything in between.
[00:07:29-00:07:32] And by the way, this is all transparent, easily available.
[00:07:32-00:07:38] We want you as developers to have access to this information because we feel like the more you can be informed,
[00:07:38-00:07:44] the better you're able to be successful in making a great game and chatting with your customers on what they want.
[00:07:44-00:07:52] Yeah, and that, I think, kind of creates an opportunity for us to just like directly address the thing that stresses a lot of devs out.
[00:07:52-00:07:56] They're looking at the increase of games on Steam and naturally wondering, like, does this mean a small amount?
[00:07:56-00:07:57] Yeah.
[00:07:57-00:07:58] Am I a smaller piece of the pie?
[00:07:58-00:08:03] Am I fighting for, you know, what are all those 42 million people buying and playing?
[00:08:03-00:08:09] By bringing more people into the ecosystem and doing a good job promoting the right games to the right people at the right time,
[00:08:09-00:08:12] we've been able to make the pie substantially bigger.
[00:08:12-00:08:15] And here's kind of what that looks like in terms of raw numbers.
[00:08:15-00:08:23] So, this chart shows the number of products on Steam able to achieve $100,000 or more in revenue per calendar year.
[00:08:23-00:08:26] And if you go back to 2020, that number is about 3%.
[00:08:26-00:08:29] That number is about 3,000 games.
[00:08:29-00:08:33] In 2025, five years later, it's close to double with 5,800 games.
[00:08:33-00:08:39] And $100,000 could be wildly successful for one dev in this room and a total disaster for another dev.
[00:08:39-00:08:40] We realize that.
[00:08:40-00:08:45] So, we also look at these numbers for other thresholds like $500,000 a year, $1 million a year.
[00:08:45-00:08:48] And the trend lines stay really consistent there.
[00:08:48-00:08:52] There's dramatically more games finding success every single year.
[00:08:52-00:08:55] And the other nice thing is thinking back to some of those user numbers we shared,
[00:08:55-00:08:59] the number of games finding success on Steam is generally keeping pace with user growth.
[00:08:59-00:09:06] Both the number of concurrent users and in-game users and the numbers of games finding success is about double over the last five years,
[00:09:06-00:09:08] which we're really proud of.
[00:09:08-00:09:09] Okay.
[00:09:09-00:09:14] So, let's take it for granted that there's more games on Steam, there's more players, more games are finding success.
[00:09:14-00:09:15] That's great.
[00:09:15-00:09:18] We wanted to dig in next a little bit on, like, how do we make that happen?
[00:09:18-00:09:20] What does our process look like?
[00:09:20-00:09:24] Partially to be transparent for you folks and also so that, you know, the next idea you have
[00:09:24-00:09:29] or the next piece of feedback you want to give us, you have a little template to keep in mind.
[00:09:29-00:09:34] We think Steam is going to keep getting better when we keep solving problems for devs and players.
[00:09:34-00:09:37] Some, you know, of those solutions are really dev-focused.
[00:09:37-00:09:38] Others are more player-focused.
[00:09:38-00:09:45] But typically, if we're doing our jobs well, making Steam means both of those groups of people are better off.
[00:09:45-00:09:52] The result of a model like this where we ship a solution, we get a bunch of feedback and data, we iterate, we improve, and the cycle repeats
[00:09:52-00:09:58] is that players have a lot more trust in our platform and they get more out of their PC games.
[00:09:58-00:10:00] Steam Labs is like a really visible version of this.
[00:10:00-00:10:03] This is a public website that you can visit any time.
[00:10:03-00:10:08] When we introduce small features or updates or new tools, often we'll put them into Steam Labs.
[00:10:08-00:10:10] Customers can start trying them out.
[00:10:10-00:10:11] Developers can poke at them.
[00:10:11-00:10:15] Sometimes they grow and get better and become a full-fledged Steam feature.
[00:10:15-00:10:19] Other times they're not as successful as we hoped and we set them aside, and that's okay.
[00:10:19-00:10:20] So, we've been talking a lot about problems.
[00:10:20-00:10:21] And when we are talking about problems, what do we do?
[00:10:21-00:10:27] When we are talking about problems that Steam is attempting to solve, we understand that there are some problems super easy to tackle.
[00:10:27-00:10:28] And we love those.
[00:10:28-00:10:29] Who doesn't?
[00:10:29-00:10:34] But we really prefer to tackle some of the more interesting problems that seem simple at first.
[00:10:34-00:10:40] And then as you kind of start peeling back the layers, you realize, oh, this is a lot more complex than we thought.
[00:10:40-00:10:47] These are problems that we feel like we're in a unique position to solve, mostly because of how we're built and how we're structured,
[00:10:47-00:10:50] but also because our goal, again, is on the long-term growth of the platform
[00:10:50-00:10:53] and the long-term happiness of developers and players.
[00:10:53-00:11:00] So, we thought we could show you some examples of how this model has helped us decide what to work on most recently when it comes to Steam.
[00:11:00-00:11:09] Every gorgeous blue blob that you see up here is something that we worked on because you as developers told us to work on it
[00:11:09-00:11:12] or players told us to work on it or, in some cases, both.
[00:11:12-00:11:19] And this is just a small sample of some of the things that we either launched or improved on Steam in just the last year.
[00:11:19-00:11:20] Yeah.
[00:11:20-00:11:25] So, we're not going to try to tackle every single one of these bubbles, but just last week we published the Steam Year in Review.
[00:11:25-00:11:27] This is kind of our annual report.
[00:11:27-00:11:33] There's a bunch of interesting data and backstory there, but we also try to go kind of literally one by one.
[00:11:33-00:11:34] Here's a feature we shipped.
[00:11:34-00:11:35] Here's the details behind it.
[00:11:35-00:11:38] Here's how it might benefit your company or your studio.
[00:11:38-00:11:41] But today we wanted to pick a couple to do a deep dive.
[00:11:41-00:11:45] I mentioned at the start of the talk kind of talking through our process, talking through the tradeoffs we made.
[00:11:45-00:11:49] So, we'll talk about user reviews by language, which was a big change in 2025,
[00:11:49-00:11:52] and a bunch of improvements we've made to daily deals.
[00:11:52-00:11:58] So, starting with user reviews, this is something we shipped last year that responded to a problem that we didn't really identify.
[00:11:58-00:12:02] Honestly, developers came to us and brought it to our attention.
[00:12:02-00:12:08] A handful of dev studios told us they were noticing this inconsistent user review score and feedback
[00:12:08-00:12:15] where a small subset of users would significantly alter their percent positive user review score on Steam
[00:12:15-00:12:18] with feedback that was perfectly valid but maybe not relevant
[00:12:18-00:12:21] to 90% of their audience.
[00:12:21-00:12:26] So, one small set of players was having a bad experience, dragging down a user review score that everybody sees,
[00:12:26-00:12:29] even though the issue didn't really impact most of those users.
[00:12:29-00:12:31] So, our first job was investigation, right?
[00:12:31-00:12:36] We know players have a huge amount of trust in the Steam user review system,
[00:12:36-00:12:43] and developers can get a bunch of data just by reading the feedback or using our API to download the raw data of their user reviews.
[00:12:43-00:12:47] But most important, players are using user review scores not just as a percentage gauge
[00:12:47-00:12:50] of game quality, because what does that even mean,
[00:12:50-00:12:54] but they're looking at the text from other people to have predictive value.
[00:12:54-00:12:57] Will I enjoy this game? Is it worth spending my time and money on?
[00:12:57-00:13:05] And if we can make those decisions better for players, we're going to make PC gaming in general a better place.
[00:13:05-00:13:07] So, that creates this really interesting challenge.
[00:13:07-00:13:09] We want to improve user reviews for players.
[00:13:09-00:13:15] We want to address this problem devs has brought us about, you know, localized issues dragging down the score.
[00:13:15-00:13:17] So, we dug into the hard data across a bunch of data.
[00:13:17-00:13:18] We looked at different games.
[00:13:18-00:13:23] We found this kind of common theme emerging where user reviews were kind of region specific.
[00:13:23-00:13:27] Customers would be struggling with an issue that might only impact a small set of the market.
[00:13:27-00:13:30] You can probably imagine what those things might be, right?
[00:13:30-00:13:33] Bad server connection in one country that doesn't affect another,
[00:13:33-00:13:37] or a localization issue that's really important to me if I play the game in that language,
[00:13:37-00:13:39] but that no other customers are noticing.
[00:13:39-00:13:41] Even cultural references that could be problematic.
[00:13:41-00:13:45] All of that is really valuable feedback for you as developers, right?
[00:13:45-00:13:47] You want to know that that's a potential problem.
[00:13:47-00:13:49] For you to invest in or address.
[00:13:49-00:13:52] It's also super useful info for the players in that region.
[00:13:52-00:13:55] We don't, you know, there's a lot of ways you could approach a problem like that.
[00:13:55-00:13:59] And I'll hand the mic back to Casey to talk about kind of what we chose not to do.
[00:13:59-00:14:03] Yeah, this is kind of what we mean when we say interesting, complex problems
[00:14:03-00:14:06] that are much more difficult to solve than we initially thought.
[00:14:06-00:14:09] There were lots of different ways we could tackle this problem, right?
[00:14:09-00:14:11] We could consider hiding reviews.
[00:14:11-00:14:14] We could let developers delete reviews.
[00:14:14-00:14:17] Or we could simply make reviews a thing.
[00:14:17-00:14:19] A thumbs up, thumbs down kind of a situation.
[00:14:19-00:14:24] And these could be valuable options in certain contexts, in certain situations.
[00:14:24-00:14:27] But they don't quite get us where we're trying to go.
[00:14:27-00:14:29] Both as a platform with the goals we've talked about,
[00:14:29-00:14:33] which are super long-term, long-term happiness of players and developers.
[00:14:33-00:14:39] And also, we want the user reviews to provide as much accurate information to players as possible.
[00:14:39-00:14:42] As well as accurate information to you as developers.
[00:14:42-00:14:46] So instead, instead of taking information away from either group,
[00:14:46-00:14:49] we started categorizing user reviews by language.
[00:14:49-00:14:53] Doing this gave us a way to communicate the context of those reviews.
[00:14:53-00:14:56] Not just to fellow players who were having those issues in those regions,
[00:14:56-00:14:59] but to players outside of those regions as a way to let them know,
[00:14:59-00:15:03] this might not be something that you need to worry about based on where you're playing.
[00:15:03-00:15:07] And this is kind of how that's communicated to a player on a store page.
[00:15:07-00:15:09] Many of you have probably seen this.
[00:15:09-00:15:14] If a game has a large total number of user reviews and hits a certain threshold of user feedback,
[00:15:14-00:15:16] then we'll show this language balance.
[00:15:16-00:15:18] This is a language by language breakdown.
[00:15:18-00:15:22] Users default to seeing the user review score for their own language,
[00:15:22-00:15:25] but then they can kind of dig in and see the variance in feedback
[00:15:25-00:15:28] and explore user reviews in other languages if they want.
[00:15:28-00:15:31] Look, in a lot of cases, this made no difference, right?
[00:15:31-00:15:36] Frankly, there's a ton of games on Steam where they're 90% in one language and 91% in another,
[00:15:36-00:15:38] and it really didn't make a big difference.
[00:15:38-00:15:41] But for those games that brought the problem to us originally,
[00:15:41-00:15:43] it made a really meaningful difference.
[00:15:43-00:15:45] And it also made them give a useful framework
[00:15:45-00:15:48] to kind of understand the problem and dig in easily.
[00:15:48-00:15:49] So with a layout like this,
[00:15:49-00:15:52] we can kind of preserve the transparency and trust that we need
[00:15:52-00:15:55] for customers to be able to make good decisions.
[00:15:55-00:15:58] We can also address this stressful thing that developers were worried about
[00:15:58-00:16:01] around their user review scores being dragged down by a narrow, specific thing.
[00:16:01-00:16:04] So that's how we tackle user reviews.
[00:16:04-00:16:06] Another problem that we tackled...
[00:16:06-00:16:08] OK, daily deals, not a problem.
[00:16:08-00:16:10] We love daily deals. They're great.
[00:16:10-00:16:12] But we needed to make some improvements.
[00:16:12-00:16:14] So we wanted to kind of share this as an example of how,
[00:16:14-00:16:17] hopefully, improved this for both developers and players.
[00:16:17-00:16:20] We'd been receiving a lot of feedback from both groups about,
[00:16:20-00:16:21] this needs to be better.
[00:16:21-00:16:23] It's not working for me the way that it was intended.
[00:16:23-00:16:25] A lot of you might know this.
[00:16:25-00:16:29] Daily deals have been a part of Steam's front page forever,
[00:16:29-00:16:32] for years and years and years, since before we were born.
[00:16:32-00:16:34] We're very young. Who cares?
[00:16:34-00:16:37] And we wondered, as Steam continued to grow,
[00:16:37-00:16:41] was there going to be a way that daily deals could continue to increase in value,
[00:16:41-00:16:43] not just for the developers who were used to using them,
[00:16:43-00:16:46] but for developers who hadn't had a chance to use daily deals?
[00:16:46-00:16:50] And then also, is there a way that we can increase the value of these
[00:16:50-00:16:52] to players as well at the same time?
[00:16:52-00:16:54] Yeah, and this is another one of those questions that, like,
[00:16:54-00:16:56] there are easier solutions, right?
[00:16:56-00:17:00] And there's a bunch of stores and websites, in games and otherwise,
[00:17:00-00:17:02] that solve this in a bunch of different ways, right?
[00:17:02-00:17:06] So there are plenty of stores or platforms where there's a preplanned program.
[00:17:06-00:17:10] You negotiate with an account manager or a business person or a lawyer,
[00:17:10-00:17:12] and you get a special spot in accounting,
[00:17:12-00:17:14] a special spot in a calendar that's predetermined.
[00:17:14-00:17:17] A lot of stores and platforms just charge money for this stuff.
[00:17:17-00:17:20] So if you've got the deepest pockets, you can secure a front page placement,
[00:17:20-00:17:22] or whatever the case may be.
[00:17:22-00:17:24] There's also the curatorial aspect, right?
[00:17:24-00:17:28] Casey and myself and other people at Valve could be sitting and deciding
[00:17:28-00:17:30] what games we think are most likely to be successful,
[00:17:30-00:17:32] which games are our favorite.
[00:17:32-00:17:36] It would just be Slay the Spire every day if I was in charge of the store.
[00:17:36-00:17:40] And all of those plans kind of fall short of our underlying goals, right?
[00:17:40-00:17:42] They take choice and power away.
[00:17:42-00:17:45] Away from game developers, they take the focus off of end users,
[00:17:45-00:17:49] and they end up reflecting kind of the preferences or the needs of the storefront
[00:17:49-00:17:52] instead of the needs of the game developers.
[00:17:52-00:17:55] It introduces all kinds of tradeoffs,
[00:17:55-00:17:58] all kinds of negative externalities that distract from the core solution,
[00:17:58-00:18:02] which is, hey, we just want to put the right game in front of the right customer.
[00:18:02-00:18:06] We don't want game discoverability on Steam to be based on who has deep pockets
[00:18:06-00:18:10] or the best deal makers or the best relationship with a sales guy.
[00:18:10-00:18:12] So instead of those alternatives,
[00:18:12-00:18:15] we leaned really hard into personalization.
[00:18:15-00:18:17] We added a bunch more daily deals.
[00:18:17-00:18:20] We used to have just one a day, then two, then four.
[00:18:20-00:18:24] And in 2025, we bumped up to six daily deals together.
[00:18:24-00:18:26] And anybody who's doing some math in their head thinks,
[00:18:26-00:18:31] okay, that sounds like a smaller slice of the pie if you're doing fewer and fewer of these.
[00:18:31-00:18:36] But we paired that increase with a big increase in smarter personalization.
[00:18:36-00:18:38] So a bunch of that is common sense stuff, right?
[00:18:38-00:18:39] Like you already own a game.
[00:18:39-00:18:42] Maybe we won't show it to you in the daily deal spot first.
[00:18:42-00:18:44] What games do your friends play?
[00:18:44-00:18:45] What language does the game support?
[00:18:45-00:18:48] And does that match up with the language you play games in?
[00:18:48-00:18:49] What are your friends playing right now?
[00:18:49-00:18:51] What developers do you follow on Steam?
[00:18:51-00:18:52] All that sort of thing.
[00:18:52-00:18:54] With that kind of personalization,
[00:18:54-00:18:57] we made the daily deal experience a lot better for customers
[00:18:57-00:19:01] and also just showed off way more games from a much wider array of devs.
[00:19:01-00:19:06] And that paired with a big improvement for scheduling and planning for all of you developers
[00:19:06-00:19:08] so that you have a little bit more flexibility.
[00:19:08-00:19:10] This is like maybe weird, but out of curiosity,
[00:19:10-00:19:12] who has gotten one of these games?
[00:19:12-00:19:13] These emails.
[00:19:13-00:19:14] Okay, yeah.
[00:19:14-00:19:17] So if a game is eligible for a daily deal,
[00:19:17-00:19:19] we proactively invite it.
[00:19:19-00:19:22] You get a message like this that has a register now button.
[00:19:22-00:19:24] And if you press that register now button,
[00:19:24-00:19:27] you get taken here to our internal planning calendar.
[00:19:27-00:19:31] So instead of emailing back and forth or being assigned a slot that works for us,
[00:19:31-00:19:34] you, the game dev, have direct access to the calendar
[00:19:34-00:19:36] and you can claim the open spot that works for you.
[00:19:36-00:19:38] And the things we hear from devs are things like,
[00:19:38-00:19:41] hey, you know, I'm announcing my sequel on March 29th.
[00:19:41-00:19:42] I'd love to play it.
[00:19:42-00:19:44] I want to promote my old game on that day.
[00:19:44-00:19:45] Or I'm launching a DLC.
[00:19:45-00:19:47] I'm supporting new languages in my game.
[00:19:47-00:19:48] Whatever the case may be.
[00:19:48-00:19:50] Now, a lot of people have not received an email like this.
[00:19:50-00:19:53] You may be wondering how do I get in on this action.
[00:19:53-00:19:56] We built a dedicated flow right into Steamworks
[00:19:56-00:19:58] where devs can read all the nitty-gritty details
[00:19:58-00:20:00] and submit your game for a daily deal.
[00:20:00-00:20:02] This flow is kind of simple enough.
[00:20:02-00:20:03] It's designed to be really quick.
[00:20:03-00:20:06] You could probably open up the Steamworks website on your phone right now
[00:20:06-00:20:09] and request a daily deal before we're done with our slides.
[00:20:09-00:20:11] Please don't do that because Casey has lots more good stuff to tell you.
[00:20:11-00:20:13] There's lots more good stuff to tell you first.
[00:20:13-00:20:16] And we will include on that QR code at the end.
[00:20:16-00:20:18] You can scan that, and one of the links in that list
[00:20:18-00:20:21] is a direct link to daily deal eligibility and submission.
[00:20:21-00:20:23] So take advantage of it, please.
[00:20:23-00:20:25] Okay, so we've added more games.
[00:20:25-00:20:27] We showed them off in a better way.
[00:20:27-00:20:30] Now time to answer that with data and what actually happened.
[00:20:30-00:20:33] The result of these changes is really exciting for us.
[00:20:33-00:20:36] So first off, way more games featured in daily deals.
[00:20:36-00:20:40] In 2025, we featured 1,500 individual titles,
[00:20:40-00:20:43] and that does not include all the additional games
[00:20:43-00:20:46] that were featured as part of like a studio sale or a franchise sale.
[00:20:46-00:20:49] So that 1,500 is just individual games.
[00:20:49-00:20:53] 69% of those games had never been in a daily deal spot before.
[00:20:53-00:20:56] So a bunch of people who had never been able to take advantage
[00:20:56-00:20:58] of this Steam feature were invited to join it.
[00:20:58-00:21:01] And this is kind of what we mean by making the pie bigger.
[00:21:01-00:21:05] Thanks to those improvements, developer revenue from daily deal spots
[00:21:05-00:21:09] increased 274% year over year.
[00:21:09-00:21:12] That substantially outpaced our revenue growth and user growth
[00:21:12-00:21:16] and literally just a lot more devs making a lot more money from daily deals
[00:21:16-00:21:18] because we invested in this new system.
[00:21:18-00:21:20] And as we mentioned at the beginning,
[00:21:20-00:21:22] we wanted to be able to add that value to you as developers,
[00:21:22-00:21:26] but we also wanted to make sure we were doing something for players also.
[00:21:26-00:21:29] It's kind of a practical impact when we're talking about the way
[00:21:29-00:21:31] that it affected players.
[00:21:31-00:21:33] More relevant placement on Steam,
[00:21:33-00:21:36] and that means the first daily deals that I see are going to be different
[00:21:36-00:21:38] than the first daily deals that Tom sees.
[00:21:39-00:21:41] And we present all of this in a carousel
[00:21:41-00:21:43] so players are still able to kind of tab through
[00:21:43-00:21:46] and see all of the ones that are on the deals as well.
[00:21:46-00:21:49] And we have numbers to support this.
[00:21:49-00:21:55] 8.2 million customers bought at least one game from a daily deal in 2025.
[00:21:55-00:21:58] And users buying games from the daily deal spot
[00:21:58-00:22:03] increased about 125% as a result of this change.
[00:22:03-00:22:07] So we take this feedback to mean the store is doing a better job
[00:22:07-00:22:08] at meeting a player's needs.
[00:22:09-00:22:11] We've been talking a lot about tools and features,
[00:22:11-00:22:15] so you might assume that we're not going to be touching on hardware today.
[00:22:15-00:22:17] But we are.
[00:22:17-00:22:19] This is not a hardware announcement.
[00:22:19-00:22:21] We are not making any announcements,
[00:22:21-00:22:24] but we are mentioning hardware
[00:22:24-00:22:28] because Steam hardware to us is an extension of Steam.
[00:22:28-00:22:31] We view these as Steam features.
[00:22:31-00:22:35] Our goals are to help players get games as quickly as they can.
[00:22:35-00:22:37] We want them to get them reliably
[00:22:37-00:22:39] and to get your games in front of players
[00:22:39-00:22:41] in whatever form they want to play those games in.
[00:22:41-00:22:43] And that's where hardware comes in.
[00:22:43-00:22:45] Players have told us time and time again
[00:22:45-00:22:47] how much they value the option of playing their games
[00:22:47-00:22:50] in different ways and in different rooms.
[00:22:50-00:22:53] Our first big push into the living room was in 2013
[00:22:53-00:22:56] with Big Picture Mode and the OG Steam Controller,
[00:22:56-00:23:00] the OG Steam Machine, and Steam Link.
[00:23:00-00:23:02] And Steam hardware has evolved since then
[00:23:02-00:23:05] with feedback over the years from developers, from players,
[00:23:05-00:23:07] and every product that we've made since
[00:23:07-00:23:09] is building off of what we've learned
[00:23:09-00:23:11] from the things that we've made before it.
[00:23:11-00:23:14] So Steam Deck and the soon-to-come Steam Controller,
[00:23:14-00:23:16] Steam Machine, and Steam Frame,
[00:23:16-00:23:19] those are all additional ways for players to play your games.
[00:23:19-00:23:22] And again, each of these represents the culmination
[00:23:22-00:23:24] of what we've learned up until then.
[00:23:24-00:23:26] Bottom line, give customers multiple options
[00:23:26-00:23:28] for playing their Steam library.
[00:23:28-00:23:32] And again, no announcement here unless anyone has RAM.
[00:23:32-00:23:35] Yeah, if you have line on like a bunch of RAM,
[00:23:35-00:23:36] we are in the market.
[00:23:36-00:23:38] We would love to buy it from you.
[00:23:38-00:23:39] Yeah.
[00:23:39-00:23:42] This piece of advice that we're talking about with hardware
[00:23:42-00:23:44] does go way beyond just Steam hardware,
[00:23:44-00:23:46] which kind of gets into the last part
[00:23:46-00:23:47] that Tom was going to start with here.
[00:23:47-00:23:48] Yeah, exactly.
[00:23:48-00:23:50] So we always have advice.
[00:23:50-00:23:51] Oh, man, I really, by the way,
[00:23:51-00:23:53] I just really like these little marching guys.
[00:23:53-00:23:54] We always have advice.
[00:23:54-00:23:56] There's always things that we can share
[00:23:56-00:23:58] that you can be doing to make your game better.
[00:23:58-00:24:01] That advice often doesn't change very much over the years, right?
[00:24:01-00:24:03] We're always talking about localize your game,
[00:24:03-00:24:05] listen to your players, et cetera.
[00:24:05-00:24:07] But the first one is kind of hardware related
[00:24:07-00:24:08] because it's all about controllers.
[00:24:08-00:24:11] Millions of players use controllers on Steam every day.
[00:24:11-00:24:14] In 2025, there were nearly 5 billion,
[00:24:14-00:24:16] that's billion with a B,
[00:24:16-00:24:19] gameplay sessions on Steam using a gamepad.
[00:24:19-00:24:21] So this includes all kinds of gamepads, right?
[00:24:21-00:24:23] It's the Steam Deck and the Steam controller, sure,
[00:24:23-00:24:26] but it's the Xbox gamepad and the PlayStation DualShock
[00:24:26-00:24:29] and Nintendo Switch Pro and flight sticks and wheels,
[00:24:29-00:24:30] you name it.
[00:24:30-00:24:32] It's also a stat that we find developers
[00:24:32-00:24:34] kind of consistently underestimating
[00:24:34-00:24:36] where they feel like, okay, controller support,
[00:24:36-00:24:37] that's something I'll add after early on.
[00:24:37-00:24:39] That's something I'll add after early access or like,
[00:24:39-00:24:41] ah, I didn't have to get that into the demo.
[00:24:41-00:24:44] It is such a popular way for people to play games on PC
[00:24:44-00:24:46] and it's only going to get more popular.
[00:24:46-00:24:48] So keep that in mind.
[00:24:48-00:24:50] We have a Steam input API.
[00:24:50-00:24:52] That's an easy way to make sure that your game supports
[00:24:52-00:24:54] all kinds of controller configurations,
[00:24:54-00:24:55] even touchscreens,
[00:24:55-00:24:57] and can kind of show the right glyphs
[00:24:57-00:24:59] so that somebody can tell the difference between,
[00:24:59-00:25:01] you know, triangle, square, A, B, X, Y,
[00:25:01-00:25:03] whatever the case may be.
[00:25:03-00:25:06] And this is also a great thing for non-Steam platforms too, right?
[00:25:06-00:25:07] Everywhere else that you ship your game,
[00:25:07-00:25:09] on PC, on console,
[00:25:09-00:25:10] usually investing in controller support
[00:25:10-00:25:12] is just going to create a better user experience
[00:25:12-00:25:14] everywhere that people enjoy your game.
[00:25:14-00:25:16] And when we're talking about player behavior,
[00:25:16-00:25:17] that relates to another piece of advice
[00:25:17-00:25:19] that we like to give often,
[00:25:19-00:25:21] which is that Steam users enjoy playing their games
[00:25:21-00:25:22] on multiple devices.
[00:25:22-00:25:26] In fact, over 50% of active Steam users in 2025
[00:25:26-00:25:28] played on more than one machine.
[00:25:28-00:25:31] And so this makes Steam Cloud a no-brainer.
[00:25:31-00:25:34] Turn it on so that your players can carry their progress
[00:25:34-00:25:36] and their save files with them from one machine
[00:25:36-00:25:37] to another.
[00:25:37-00:25:39] We even built something called Auto Cloud,
[00:25:39-00:25:41] which means all you have to do is tell us
[00:25:41-00:25:43] what directory your save files are in.
[00:25:43-00:25:44] We'll make sure it's in the right place
[00:25:44-00:25:45] so that the players can find it
[00:25:45-00:25:47] and pick it back up with their progress.
[00:25:47-00:25:49] And I hate to put Tom on the spot,
[00:25:49-00:25:51] but he had something like this happen
[00:25:51-00:25:53] with his own playing experience.
[00:25:53-00:25:55] Yeah, I was complaining about this
[00:25:55-00:25:56] the other day in the office.
[00:25:56-00:25:59] So I tried out a demo in Steam Next Fest.
[00:25:59-00:26:00] I loved it.
[00:26:00-00:26:02] I played through the tutorial,
[00:26:02-00:26:04] maybe like an hour of play time.
[00:26:04-00:26:05] That night, I installed the same demo
[00:26:05-00:26:07] on my Steam Deck to keep playing.
[00:26:07-00:26:09] And instead of picking up where I left off,
[00:26:09-00:26:11] I started right back at the tutorial again.
[00:26:11-00:26:13] It's not the end of the world.
[00:26:13-00:26:14] I hate to be nitpicky.
[00:26:14-00:26:16] But also, it was a reason for me to bounce out of that demo.
[00:26:16-00:26:17] I kind of said,
[00:26:17-00:26:19] yeah, I don't think I'm going to play the tutorial again,
[00:26:19-00:26:21] but I would have loved to pick up where I left off.
[00:26:21-00:26:23] So again, even if you're at that stage of your development
[00:26:23-00:26:25] where you're just putting a demo in Next Fest
[00:26:25-00:26:27] or you're just shipping in Steam Early Access,
[00:26:27-00:26:29] those little quality-of-life improvements
[00:26:29-00:26:31] can be a big difference in retaining users
[00:26:31-00:26:34] and keeping them happy with your product.
[00:26:34-00:26:37] Another thing we're always encouraging is localization.
[00:26:37-00:26:39] Two-thirds of players on Steam are not playing
[00:26:39-00:26:41] and viewing the store in English,
[00:26:41-00:26:44] and so localize your game and your store page.
[00:26:44-00:26:46] In 2025, we shipped this big update
[00:26:46-00:26:49] to the way you can add localized text and images
[00:26:49-00:26:51] to your store page,
[00:26:51-00:26:53] but also to your Steam events and blog posts.
[00:26:53-00:26:55] So we realized that can be time-consuming,
[00:26:55-00:26:58] and we tried to make our tools a little bit smoother
[00:26:58-00:27:00] to save you some time and effort
[00:27:00-00:27:02] when you localize your messaging to players.
[00:27:02-00:27:04] Another thing that we just hear over and over
[00:27:04-00:27:06] from folks is that they really like looking
[00:27:06-00:27:08] at their wishlist data and even their sales data
[00:27:08-00:27:11] to prioritize what languages to localize, right?
[00:27:11-00:27:13] So if you've got a bunch of wishlisters in Brazil,
[00:27:13-00:27:16] then maybe Brazilian Portuguese makes sense to localize.
[00:27:16-00:27:19] So localization is probably one of the top pieces of advice
[00:27:19-00:27:22] we find ourselves sharing with developers all over the place,
[00:27:22-00:27:25] but this one is a close second, and it's all about playtesting.
[00:27:25-00:27:28] Launching your game is such an important moment
[00:27:28-00:27:31] in the development cycle of what you're making,
[00:27:31-00:27:33] which means it's very stressful, it's very risky,
[00:27:33-00:27:36] and you have a lot of things that you're trying to keep track of.
[00:27:36-00:27:38] So playtest your game well in advance
[00:27:38-00:27:40] so that you can find things that maybe
[00:27:40-00:27:43] you hadn't anticipated budgeting time for at launch
[00:27:43-00:27:46] and take care of them in those weeks and months
[00:27:46-00:27:48] leading up to that important moment.
[00:27:48-00:27:50] On Steam, that means you can take advantage of it
[00:27:50-00:27:53] in multiple ways, including the Steam playtest feature.
[00:27:53-00:27:56] You can look for rounds of feedback in lots of different ways.
[00:27:56-00:27:58] But again, as with much of what we're saying,
[00:27:58-00:28:00] this advice applies to off of Steam, too.
[00:28:00-00:28:02] Playtest your game in as many different ways
[00:28:02-00:28:03] and as many different platforms
[00:28:03-00:28:05] as you're planning to have your game on.
[00:28:05-00:28:07] Now, this was the place we were going to
[00:28:07-00:28:09] just gracefully transition on out of here,
[00:28:09-00:28:11] but right before we got on the plane to come to San Francisco,
[00:28:11-00:28:14] one of the features that the team had been working on for a while
[00:28:14-00:28:16] shipped, and we thought, can we squeeze it in?
[00:28:16-00:28:17] May as well.
[00:28:17-00:28:19] Yeah, so a few years ago,
[00:28:19-00:28:22] we introduced developer and publisher homepages on Steam.
[00:28:22-00:28:26] Players really get attached to a studio or a team.
[00:28:26-00:28:28] They find out that they love the kind of games that you make.
[00:28:28-00:28:30] You build an audience over time.
[00:28:30-00:28:32] And homepages make it really easy
[00:28:32-00:28:34] for you to build that audience
[00:28:34-00:28:36] and for customers to kind of follow you directly in Steam.
[00:28:36-00:28:38] If a customer follows you,
[00:28:38-00:28:40] they automatically get notified
[00:28:40-00:28:42] when a game you release comes out.
[00:28:42-00:28:44] They also see your games more in places like,
[00:28:44-00:28:46] you know, they open up the Steam Summer Sale
[00:28:46-00:28:48] and we show games from developers and publishers
[00:28:48-00:28:50] you follow in a bunch of places.
[00:28:50-00:28:52] So that feature has slowly been getting better.
[00:28:52-00:28:54] In 2025, we made a big fix
[00:28:54-00:28:57] specifically from complaints devs gave to us at GDC.
[00:28:57-00:28:59] It used to be a little bit painful
[00:28:59-00:29:01] and annoying to link your games
[00:29:01-00:29:03] to your creator homepage.
[00:29:03-00:29:05] I'm seeing some nodding heads.
[00:29:05-00:29:07] We made that process a lot easier,
[00:29:07-00:29:09] so it's just less time consuming to maintain.
[00:29:09-00:29:10] And then like Casey said,
[00:29:10-00:29:12] right before we left for GDC,
[00:29:12-00:29:14] the team rolled out a big personalization
[00:29:14-00:29:17] and customization option for homepages.
[00:29:17-00:29:19] So you now have a lot more control
[00:29:19-00:29:21] to put your best foot forward,
[00:29:21-00:29:23] make your publisher homepage on Steam
[00:29:23-00:29:25] or your developer homepage kind of your own space.
[00:29:25-00:29:27] If you already have one of these pages,
[00:29:27-00:29:29] keep it up to date.
[00:29:29-00:29:31] It's really worth even just the minimal effort
[00:29:31-00:29:32] you put in every six months
[00:29:32-00:29:34] to make sure your new coming soon game
[00:29:34-00:29:36] is showing up on your homepage.
[00:29:36-00:29:37] If you haven't made one yet,
[00:29:37-00:29:39] even if you only have one game on Steam,
[00:29:39-00:29:41] the best time to make one is yesterday.
[00:29:41-00:29:43] The next best time is today.
[00:29:43-00:29:45] Future you will be very appreciative
[00:29:45-00:29:47] that you started building followers
[00:29:47-00:29:49] so that when that second or third game comes out
[00:29:49-00:29:51] or when you announce that expansion,
[00:29:51-00:29:54] a bunch of fans of yours can follow it.
[00:29:54-00:29:56] We could keep talking for hours.
[00:29:56-00:29:58] I promise you we won't
[00:29:58-00:30:00] because this is our third to last slide.
[00:30:00-00:30:03] But I think it's important that we call out the fact
[00:30:03-00:30:05] that this is not meant to be
[00:30:05-00:30:07] an entirely contextualized talk
[00:30:07-00:30:09] where this is all that you need to know
[00:30:09-00:30:11] when it comes to Steam.
[00:30:11-00:30:13] This is something that we work on constantly.
[00:30:13-00:30:15] We don't mean for it to be a,
[00:30:15-00:30:17] we're perfect, you're welcome, Earth.
[00:30:17-00:30:19] We mean for it to be the kind of place
[00:30:19-00:30:21] where you tell us what you need from us,
[00:30:21-00:30:22] we work on it,
[00:30:22-00:30:24] you tell us again what you need from us,
[00:30:24-00:30:26] we work on it, and so on.
[00:30:26-00:30:27] So we're really invested,
[00:30:27-00:30:28] as we mentioned in the beginning,
[00:30:28-00:30:29] in the long-term success
[00:30:29-00:30:31] of everyone on Steam,
[00:30:31-00:30:33] and that includes both developers and players.
[00:30:33-00:30:35] Steam really only works
[00:30:35-00:30:37] if we do our job to keep everybody happy.
[00:30:37-00:30:39] Yeah, and that includes improving
[00:30:39-00:30:41] on a bunch of stuff that we've talked about today, right?
[00:30:41-00:30:43] These features aren't done being developed.
[00:30:43-00:30:45] These tools aren't done being finished.
[00:30:45-00:30:48] Sometimes I feel like Steam is an early access game
[00:30:48-00:30:50] where we're constantly refining things
[00:30:50-00:30:52] and improving things.
[00:30:52-00:30:54] There's a lot of work left to do.
[00:30:54-00:30:56] In some cases, devs aren't satisfied
[00:30:56-00:30:58] with solutions or trade-offs we've made
[00:30:58-00:31:00] or they want us to invest in something new
[00:31:00-00:31:01] that maybe is a blind spot
[00:31:01-00:31:03] or that we haven't considered yet.
[00:31:03-00:31:05] That's why we're here at GDC.
[00:31:05-00:31:07] We spend a little bit of time talking,
[00:31:07-00:31:09] and then the whole rest of the week is listening, right?
[00:31:09-00:31:11] Hearing what game devs and game publishers
[00:31:11-00:31:13] are worried about or concerned about
[00:31:13-00:31:15] and how we can help you make your business better
[00:31:15-00:31:17] or make your customers happier.
[00:31:17-00:31:19] After the talk, I'll hang around.
[00:31:19-00:31:21] Casey will, too, not in this room.
[00:31:21-00:31:23] We'll try to go kind of out beyond.
[00:31:23-00:31:25] So if you do want to ask follow-up questions
[00:31:25-00:31:27] or just chat or give feedback, come find us.
[00:31:27-00:31:30] And if you didn't already, scan that QR code.
[00:31:30-00:31:31] Oh, sorry.
[00:31:31-00:31:32] No, no.
[00:31:32-00:31:33] I should have said that.
[00:31:33-00:31:34] I think everybody got it.
[00:31:34-00:31:36] But we also just should close by saying thank you.
[00:31:36-00:31:38] We know GDC is really busy.
[00:31:38-00:31:40] It means a lot that you folks spent a little bit of time
[00:31:40-00:31:41] talking with us.
[00:31:41-00:31:43] So thanks for coming, and have a great GDC.
[00:31:43-00:31:44] Thank you.
[00:31:44-00:31:46] That was great.
