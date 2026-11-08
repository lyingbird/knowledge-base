---
title: "NewbieIGD|《过山车大亨》中过度设计的“呕吐系统”——RollerCoaster Tycoon’s Overengineered Puking Syst"
platform: bilibili
bvid: BV1vQe76cEHb
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-09-15 15:54:49
duration_sec: 2046
view: 4030
like: 90
coin: 4
favorite: 132
reply: 13
danmaku: 3
share: 18
url: https://www.bilibili.com/video/BV1vQe76cEHb
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 23399
crawl_time: 2026-11-08 21:20:03


# NewbieIGD|《过山车大亨》中过度设计的“呕吐系统”——RollerCoaster Tycoon’s Overengineered Puking Syst

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-09-15 15:54:49
- **时长**: 34分6秒
- **播放**: 4030 | 赞: 90 | 币: 4 | 藏: 132
- **链接**: https://www.bilibili.com/video/BV1vQe76cEHb

## 视频描述

原视频：https://www.youtube.com/watch?v=tG66j1sP8gs
（2026年2月28日）
🎮 免费下载 GameMaker：https://opr.as/GM-NewbieIndie
👾 试玩我的部分游戏：https://newbie-indie-game-dev.itch.io/

感谢 ‪https://www.youtube.com/@JuniperDev‬

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1vQe76cEHb
# 语言=en 时长=00:16:04 模型=large-v3

[00:00:00-00:00:04] Guests in RollerCoaster Tycoon will start throwing up once their nausea reaches 128,
[00:00:05-00:00:07] which is about halfway through the nausea meter.
[00:00:07-00:00:09] From that point on, the chance of vomiting goes up pretty linearly,
[00:00:10-00:00:14] reaching a 25% chance every 12.8 seconds at maximum nausea.
[00:00:14-00:00:18] And they can only puke if they're walking, so they're safe if they're at a bench, for example.
[00:00:18-00:00:22] Hi guys, my name's UniperDev, and today we're talking all about throwing up
[00:00:22-00:00:27] in RollerCoaster Tycoon, the 20-year-old relic of a game that it is.
[00:00:27-00:00:29] Huge thanks to Newbie for inviting me to the channel,
[00:00:30-00:00:32] and for writing this next line that I'm about to say.
[00:00:33-00:00:38] Uh, the puddle of vomit appears on exactly frame 16 of the puking animation.
[00:00:38-00:00:39] Did you know that?
[00:00:39-00:00:42] And there's only two possible vomit sprites.
[00:00:42-00:00:46] Some sources online say that the color of the guest's vomit depends on what they ate,
[00:00:46-00:00:49] which would be awesome, but that doesn't really appear to be the case.
[00:00:50-00:00:54] The two variants are randomly assigned when a guest is born with a 50-50 chance,
[00:00:54-00:00:57] so you're kind of just genetically predisposed to one of the two colors.
[00:00:57-00:01:01] And the animation itself is also accompanied by one of four puking sounds.
[00:01:02-00:01:07] Now, the game does give you a few visual hints before the guest actually throws up.
[00:01:08-00:01:12] If you inspect a person, you'll see that they have a face icon that reflects their current mood.
[00:01:13-00:01:16] Nausea itself is tracked as a value from 0 to 255,
[00:01:16-00:01:19] and that represents how sick a guest is feeling.
[00:01:19-00:01:23] At 140, the guest starts looking a little bit worried.
[00:01:23-00:01:25] At 170, it turns completely green.
[00:01:26-00:01:29] And when it hits 200, it's over. Puking is imminent.
[00:01:29-00:01:32] That gives us three clear tiers that are exactly 30 points apart.
[00:01:33-00:01:36] Puking can technically happen even before any of these faces appear.
[00:01:36-00:01:40] The probability is already greater than zero at 128 nausea,
[00:01:40-00:01:45] so in rare cases, the guests can just throw up without any prior warning or visual indicator.
[00:01:45-00:01:48] Each tier is also tied to changes in how the guest will behave.
[00:01:49-00:01:51] At the first level, they start walking at half speed.
[00:01:51-00:01:55] They hold their hands to their mouth, and they start thinking about how sick they're getting.
[00:01:55-00:01:59] The second tier comes with a different walking animation, and their skin gets all green and funky.
[00:01:59-00:02:01] But they don't have any new thoughts.
[00:02:01-00:02:07] At the final tier, there's no new walk cycle, but they're really feeling it, and they're really thinking about it.
[00:02:07-00:02:11] The only thing that can override a sick face is when a guest is very angry,
[00:02:11-00:02:13] and they get prone to breaking things and becoming a vandal.
[00:02:14-00:02:17] The game just considers that state a little bit more important to convey to the player.
[00:02:18-00:02:21] And the sick walking animations are replaced by item animations,
[00:02:21-00:02:24] like holding a balloon or an umbrella, wearing a hat.
[00:02:24-00:02:29] But not by tiredness, or the animation when they need to go to the bathroom, for example.
[00:02:29-00:02:33] But when a guest finally throws up, their nausea is reduced in two ways.
[00:02:33-00:02:39] It immediately drops by 30 points, which is usually enough points to bring them down one tier on the visual sickness scale.
[00:02:39-00:02:43] And then it gradually continues falling until it's at about half of its original value.
[00:02:44-00:02:47] Internally, the game is tracking two nausea values.
[00:02:47-00:02:50] There's the current one, and then the one that the game is moving towards.
[00:02:50-00:02:55] Whenever something happens that increases or relieves nausea, the target is updated,
[00:02:55-00:02:58] and then the current value slowly adjusts to it over time.
[00:02:58-00:02:58] That smoothing is what makes the game so fun.
[00:02:58-00:02:58] That smoothing is what makes the game so fun.
[00:02:58-00:02:59] That smoothing is what makes the game so fun.
[00:02:59-00:02:59] That smoothing is what makes the game so fun.
[00:02:59-00:02:59] That smoothing is what makes the game so fun.
[00:02:59-00:03:02] That smoothing is what makes changes in nausea feel more natural and gradual.
[00:03:03-00:03:05] And, uh, you know what else is smooth?
[00:03:06-00:03:08] Oh, the transition into today's sponsor.
[00:03:08-00:03:10] I'll pass it off to Newbie for this one.
[00:03:10-00:03:13] This video is sponsored by GameMaker.
[00:03:13-00:03:18] GameMaker is the engine behind games like Katana Zero, recent hit The King is Watching,
[00:03:19-00:03:21] and one of my personal favorites, Archvale.
[00:03:22-00:03:27] GameMaker is known as a great entry-level engine, but it's also powered some absolute classics.
[00:03:28-00:03:29] Even Undertale was made.
[00:03:29-00:03:34] And it's one of the best-rated and best-selling games ever.
[00:03:34-00:03:40] With that level of success, it's no surprise that Toby Fox stacked with GameMaker for Deltarune 2.
[00:03:41-00:03:45] I asked our host JuniperDev what she likes most about GameMaker,
[00:03:45-00:03:48] and she wanted to give a shout-out to GML Visual.
[00:03:48-00:03:53] That's the visual coding mode where you build logic by dragging and dropping action blocks.
[00:03:53-00:03:59] It's great if you want to understand how code flows without needing to program in the traditional way.
[00:03:59-00:04:02] On top of that, there's a huge learning ecosystem around GameMaker,
[00:04:03-00:04:07] with tons of official tutorials on YouTube and a very friendly community on Discord.
[00:04:08-00:04:12] Honestly, I think it's one of the best options out there if you want to start making games,
[00:04:12-00:04:14] but feel overwhelmed or don't know where to begin.
[00:04:15-00:04:18] You can use GameMaker for free for non-commercial projects,
[00:04:18-00:04:21] and if you go commercial, it's just a one-time payment.
[00:04:21-00:04:22] Pretty rare these days.
[00:04:22-00:04:26] I encourage you to download GameMaker using the link in the description.
[00:04:26-00:04:29] And now let's get back to JuniperDev and the technical side of puking.
[00:04:29-00:04:30] Hi, I'm back.
[00:04:31-00:04:34] Now, nausea increases as a direct result of riding attractions.
[00:04:34-00:04:36] Each ride in the game has three ratings.
[00:04:36-00:04:40] There's excitement, intensity, and nausea.
[00:04:40-00:04:42] Unlike excitement, where higher is generally better,
[00:04:43-00:04:46] or intensity, where the ideal level depends on guest preferences,
[00:04:46-00:04:49] nausea is always something that you want to keep low.
[00:04:49-00:04:52] Basically, the lower the nausea, the better for the guests.
[00:04:52-00:04:56] From the player's perspective, this rating is shown in one of six categories,
[00:04:56-00:04:59] from low to ultra-exciting.
[00:04:59-00:05:04] Extreme, not just, not just extreme, no, no, no, no, no, no, ultra-extreme.
[00:05:04-00:05:08] Internally, those map to increasing ranges of 256 points each,
[00:05:08-00:05:12] which in-game are displayed as values stepping by 2.56.
[00:05:12-00:05:15] Now, all kinds of ride features can influence this value.
[00:05:16-00:05:20] Excessive lateral G-forces can add 200 to 800 points to the nausea rating.
[00:05:20-00:05:24] And yeah, this game takes physical properties like lateral Gs into account
[00:05:24-00:05:29] and how they contribute to nausea, even for roller coasters made by the player,
[00:05:29-00:05:32] which is an insane level of detail for a game made in the late 90s.
[00:05:32-00:05:38] Like, every guest is made with its own built-in tolerance to nausea, just like real life.
[00:05:38-00:05:39] There are four possible levels.
[00:05:39-00:05:42] There's none, low, average, and high,
[00:05:42-00:05:45] and each of them map to a different internal tolerance value.
[00:05:46-00:05:49] When a guest is born into the beautiful world of Roller Coaster Tycoon,
[00:05:49-00:05:51] they're given one of these tolerance levels randomly,
[00:05:52-00:05:53] but it's not with the same probability.
[00:05:54-00:05:58] Internally, this is done with a small range of numeric values that map to each category.
[00:05:59-00:06:03] Under normal conditions, only the first eight values of that range are used,
[00:06:03-00:06:06] which means most guests end up with an average tolerance.
[00:06:06-00:06:10] But in scenarios where guests are meant to prefer more intense rides,
[00:06:10-00:06:12] the game will shift that range upwards,
[00:06:12-00:06:15] which removes the lowest values from the pool completely,
[00:06:15-00:06:18] and now our new most common tolerance is high.
[00:06:18-00:06:21] When a guest is deciding whether or not they want to hit up a ride,
[00:06:21-00:06:26] the game compares that ride's nausea rating with the guest's tolerance for nausea.
[00:06:26-00:06:28] But it also takes their happiness
[00:06:28-00:06:29] into account.
[00:06:29-00:06:32] The more fun that a guest is having, the happier they're doing,
[00:06:32-00:06:34] the more that they're willing to put up with,
[00:06:34-00:06:36] and the more nausea they're willing to tolerate.
[00:06:36-00:06:38] When that happiness is maxed out,
[00:06:38-00:06:41] that can add up to 255 points to the guest's tolerance,
[00:06:41-00:06:43] which is a huge boost.
[00:06:43-00:06:46] A guest who has no natural tolerance but is having
[00:06:46-00:06:50] the time of their life can still go on some high nausea rides.
[00:06:50-00:06:52] And in contrast, a guest that has a high tolerance
[00:06:52-00:06:55] but is really sad is probably still going to accept
[00:06:55-00:06:58] going on the higher nausea rides, but they might turn down
[00:06:58-00:07:01] the most extreme ones until their mood improves.
[00:07:01-00:07:04] If a guest approaches a ride that's just too much for their tolerance,
[00:07:04-00:07:07] they won't ride it. Instead, they'll just look at the ride
[00:07:07-00:07:09] and think about how sick it makes them feel,
[00:07:09-00:07:11] and then their happiness drops eight points.
[00:07:12-00:07:17] And somehow, even with all of that, tolerance is still not the only factor.
[00:07:17-00:07:20] A guest's current nausea level also acts as a cutoff.
[00:07:21-00:07:25] Once it goes over 160, which is about 60% through the nausea meter,
[00:07:25-00:07:27] guests are only going to go on rides that have a rating
[00:07:27-00:07:29] of 140 or less.
[00:07:29-00:07:32] Interestingly enough, this threshold doesn't line up
[00:07:32-00:07:36] with any of the visual sickness tiers, and the 140 rating doesn't match
[00:07:36-00:07:40] any of the ride nausea categories that are given to the player either.
[00:07:40-00:07:44] It falls roughly in the lower half of the low range.
[00:07:44-00:07:47] Surprisingly enough, the guest's nausea tolerance doesn't
[00:07:47-00:07:52] just define a maximum, but it also defines a desired minimum level of nausea.
[00:07:53-00:07:57] That's what the game uses to really decide how satisfied a guest is after a ride.
[00:07:57-00:08:01] Whether a guest enjoyed a ride depends on a lot of things, like the price,
[00:08:01-00:08:04] how long they were waiting for, and whether or not they've ridden it before.
[00:08:04-00:08:08] But it also depends on how well the ride's intensity and nausea matches
[00:08:09-00:08:13] the guest's individual preferences. If a ride's nausea rating falls nicely
[00:08:13-00:08:16] within the minimum and the maximum preference of nausea for a guest,
[00:08:16-00:08:18] then it scores pretty high.
[00:08:18-00:08:21] If it doesn't, then the game uses that guest's happiness to stretch
[00:08:21-00:08:25] the range a little bit and make it more forgiving, especially on the less nauseating rides.
[00:08:25-00:08:27] Ride nausea ratings are not always the same.
[00:08:27-00:08:30] The nausea ratings and the guest's nausea tolerance are fixed values,
[00:08:30-00:08:33] but the nausea level itself is constantly changing.
[00:08:34-00:08:37] Nausea obviously goes up when a guest gets on a ride.
[00:08:37-00:08:39] But how much it goes up depends
[00:08:39-00:08:42] on the nausea rating of the ride and then also a bunch of other stuff.
[00:08:42-00:08:44] Happier guests build up nausea slower,
[00:08:45-00:08:49] guests with full stomachs build it faster, and a guest's natural nausea tolerance
[00:08:49-00:08:51] reduces the final impact of the ride.
[00:08:51-00:08:54] But let me give you a few examples so this is easier to understand.
[00:08:54-00:08:57] Let's say that we got two little guys with the same starting
[00:08:57-00:09:01] level of nausea. They're going on the same ride that has a medium nausea rating.
[00:09:01-00:09:03] The first one has a high tolerance.
[00:09:03-00:09:06] He's in a great mood and he's only mildly hungry.
[00:09:06-00:09:07] The second guy has a low tolerance.
[00:09:08-00:09:10] He just ate and he is not having a good time.
[00:09:10-00:09:13] Even though the ride itself and the starting points of nausea are
[00:09:13-00:09:16] the same, the outcome is completely different.
[00:09:16-00:09:19] The first guest is only a little bit more nauseous than he was before.
[00:09:19-00:09:23] But the second guy is really going through it.
[00:09:23-00:09:26] He's almost at his limit and he is on the verge of throwing up.
[00:09:27-00:09:31] Low happiness and a full stomach strongly amplify the effect of a ride,
[00:09:31-00:09:34] while a low tolerance only partially mitigates it.
[00:09:34-00:09:39] In that second example with our poor little victim, vomiting is very much expected.
[00:09:39-00:09:41] Now, when a guest does throw up,
[00:09:41-00:09:43] their nausea is cut in half like we saw earlier.
[00:09:43-00:09:46] And vomiting increases their hunger level,
[00:09:46-00:09:49] so emptying their stomach puts them in a better state for the next ride.
[00:09:49-00:09:51] Now, you might be thinking that you could
[00:09:51-00:09:55] capitalize on that increased hunger to then boost your food sales, which, you know,
[00:09:56-00:09:56] ethics aside,
[00:09:56-00:09:59] is obviously number one priority here.
[00:09:59-00:10:00] But that won't work.
[00:10:00-00:10:04] Once a guest hits over 140 nausea, they just stop buying food and drinks
[00:10:04-00:10:08] altogether, which, I mean, is really realistic, so that's cool.
[00:10:08-00:10:12] Other than throwing up, guests can reduce their nausea in a few different ways.
[00:10:12-00:10:13] Obviously, if someone's just chilling,
[00:10:14-00:10:17] doing nothing, then their nausea is going to slowly go down over time.
[00:10:17-00:10:19] Sitting down on a bench is going to reduce
[00:10:19-00:10:24] that even more, about five times faster than walking, but only down to about 50 nausea.
[00:10:24-00:10:26] And guests are actively going to hunt down
[00:10:26-00:10:30] on a bench once their nausea hits above 170, which matches the second face icon
[00:10:30-00:10:34] in walking animation. Now, if their nausea ever gets above that,
[00:10:34-00:10:37] above 200, then they go straight to first aid.
[00:10:37-00:10:41] In these shelters, which are infinite and they can house an infinite number
[00:10:41-00:10:46] of sick guests, nausea drops 40 times faster than walking and about eight times
[00:10:46-00:10:50] faster than sitting. Guests leave the first aid room at 35 nausea,
[00:10:50-00:10:54] but in practice it shows as zero because the meter is a bit funky.
[00:10:54-00:10:56] Now, if somehow none of this
[00:10:56-00:11:00] helps and a guest is just predestined to throwing up, then the handyman is going
[00:11:00-00:11:02] to pull up and he's going to clean up the mess.
[00:11:02-00:11:06] Handymen are also in charge of emptying bins, watering gardens and mowing grass.
[00:11:07-00:11:10] But their top priority is always picking up litter and sweeping vomit.
[00:11:11-00:11:15] All staff follow a shared global clock, but it's offset by their number.
[00:11:15-00:11:17] So when a guest throws up or they drop
[00:11:17-00:11:20] litter, not everyone rotates to it at the same time.
[00:11:20-00:11:24] That small desynchronization makes it a lot more natural than having the hive mind
[00:11:24-00:11:27] of handymen zoom to the nearest vomit puddle.
[00:11:27-00:11:31] Every handyman is in charge of the seven by seven tile area around them.
[00:11:31-00:11:33] Anything that's beyond that perimeter,
[00:11:33-00:11:37] outside their patrol area or is blocked in the game is completely ignored.
[00:11:38-00:11:39] They always go for the closest piece
[00:11:39-00:11:43] of litter using the Manhattan distance, which basically just means no diagonals.
[00:11:43-00:11:46] And in their brains, they weigh vertical movement as four times
[00:11:46-00:11:49] more expensive and not worth it as horizontal movement.
[00:11:50-00:11:54] In practice, that means that moving up or down as a handyman is heavily discouraged,
[00:11:54-00:11:56] but more likely to move side to side.
[00:11:56-00:12:00] So with that system, vomit directly competes with food wrappers and empty cans.
[00:12:00-00:12:03] They're all equal in the eyes of the handyman.
[00:12:03-00:12:06] If a handyman locks in on vomit, they're going to follow it about 90 percent
[00:12:06-00:12:09] of the time, the exception being when they're inside of a ride queue,
[00:12:09-00:12:12] which drops the probability to about 10 percent.
[00:12:12-00:12:16] I think that helps avoid pathfinding issues maybe and just awkward behavior.
[00:12:16-00:12:20] Once they reach their target tile, the sweeping animation begins
[00:12:20-00:12:23] and the vomit disappears on frame number nine of that animation.
[00:12:23-00:12:24] All litter
[00:12:24-00:12:27] on the tile is cleaned at once in a single sweep.
[00:12:27-00:12:30] And that could, in theory, mean hundreds of puddles at once.
[00:12:30-00:12:34] There is a global cap of 500 units of litter and vomit present on the game
[00:12:35-00:12:38] at any time, but it's pretty unlikely that that cap is
[00:12:38-00:12:40] ever going to be reached on the same tile.
[00:12:41-00:12:43] If the handyman are ever slacking and a park gets really dirty,
[00:12:44-00:12:46] then it can even get the most untidy award.
[00:12:47-00:12:48] That happens when over one sixteenth
[00:12:49-00:12:52] of the total guests are thinking about how untidy the place is.
[00:12:52-00:12:54] One of the thoughts that counts for this
[00:12:54-00:12:58] is this path is disgusting and it works like this.
[00:12:58-00:13:01] As your guests are walking through the park, the game will keep track of how many
[00:13:02-00:13:06] puddles of vomit the guests have stepped over in their last three steps.
[00:13:06-00:13:09] If that accumulated exposure ever hits more than three,
[00:13:09-00:13:13] which could mean that you have three units of vomit on the same tile.
[00:13:13-00:13:13] Yuck.
[00:13:14-00:13:16] Then the guest has a 17 percent chance
[00:13:16-00:13:19] to think about how dirty the park is and lose happiness.
[00:13:19-00:13:23] This check happens every single step as long as the condition is met.
[00:13:23-00:13:24] But if the guest gets
[00:13:24-00:13:27] onto some clean tiles quickly enough, then they don't even notice.
[00:13:27-00:13:32] These thoughts don't just enable the most untidy award, but they also block others.
[00:13:33-00:13:37] If at least five guests are thinking about how disgusting and rank and stinky
[00:13:37-00:13:40] the park is, then the park cannot get the most tidy award.
[00:13:40-00:13:43] And if over 15 guests have that thought,
[00:13:43-00:13:46] then the most beautiful award is now off the table.
[00:13:46-00:13:49] Vomit even affects the overall park rating,
[00:13:49-00:13:53] which is a really important metric for just accomplishing the objectives in the game.
[00:13:53-00:13:56] The park rating itself comes from obviously the puke,
[00:13:56-00:14:00] but then also the excitement for the rides, the total number of happy guests,
[00:14:00-00:14:03] the total casualties, you know, stuff like that.
[00:14:03-00:14:07] Puke kind of has an indirect impact just by lowering the guest happiness.
[00:14:07-00:14:09] But it does have one direct effect.
[00:14:09-00:14:13] Your rating is reduced by how much vomit exists in the park.
[00:14:13-00:14:15] Any vomit or litter that stays unclean
[00:14:16-00:14:19] for over three minutes and 12 seconds starts to count against you.
[00:14:20-00:14:22] And every puddle, every piece reduces your rating by four points.
[00:14:23-00:14:26] That's how it's supposed to work, at least.
[00:14:26-00:14:30] In the original game, there was a bug that allowed this penalty to be applied immediately.
[00:14:31-00:14:33] It skipped the three minute age check completely.
[00:14:33-00:14:36] This was later fixed in Open RCT 2,
[00:14:36-00:14:39] which is an open source reimplementation of Rollercoaster Tycoon 2.
[00:14:40-00:14:42] And that's what Newbie's been using as the main source for this video.
[00:14:43-00:14:47] Now, the penalty of vomit is capped at negative 600 points, which is huge.
[00:14:48-00:14:52] For comparison, the maximum bonus that you can get from happy guests who are having
[00:14:52-00:14:55] a great time and loving your park is only 500 points.
[00:14:56-00:14:57] Reaching that penalty means that you have
[00:14:58-00:15:02] 150 puddles of vomit or pieces of litter in your park.
[00:15:02-00:15:04] Hey, congratulations.
[00:15:04-00:15:07] Now, you might be thinking that that's super unrealistic and that it's really
[00:15:07-00:15:12] hard to get that many puddles of vomit, but there is one thing that you can do.
[00:15:12-00:15:17] If you name one of your guests Felicity Anderson, everyone around them is going
[00:15:17-00:15:21] to start projectile vomiting, regardless of their nausea status, regardless of
[00:15:21-00:15:24] everything else that we talked about in this video.
[00:15:24-00:15:26] I don't know if the creator of this game
[00:15:26-00:15:28] just had beef with someone named Felicity, maybe?
[00:15:28-00:15:31] Strange, unexplained cheat aside,
[00:15:31-00:15:34] it really is amazing how deep this puking mechanic goes.
[00:15:34-00:15:38] It's realistic, it's fun, and it was made in the 90s.
[00:15:38-00:15:42] That's why Rollercoaster Tycoon is a classic and why its one creator,
[00:15:42-00:15:44] Chris Sawyer, is a legend.
[00:15:44-00:15:46] Anyway, my name's Juniper Dev.
[00:15:46-00:15:47] Thank you so much for watching.
[00:15:47-00:15:51] You can find my channel and my information in the description below.
[00:15:51-00:15:53] But if you liked this video, then make sure you subscribe to Newbie,
[00:15:53-00:15:55] who I thank so much for having me on the channel.
[00:15:55-00:15:58] Thank you for watching, and I will see you in the next one.
[00:15:59-00:16:00] Bye bye.
