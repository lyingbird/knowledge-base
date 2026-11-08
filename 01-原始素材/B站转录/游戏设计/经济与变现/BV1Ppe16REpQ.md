---
title: "NewbieIGD|我爬取了整个Steam商品库，数据全在这——I Scraped the Entire Steam Catalog, Here’s the D"
platform: bilibili
bvid: BV1Ppe16REpQ
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-09-18 15:29:23
duration_sec: 1417
view: 821
like: 35
coin: 5
favorite: 72
reply: 2
danmaku: 3
share: 9
url: https://www.bilibili.com/video/BV1Ppe16REpQ
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 15731
crawl_time: 2026-11-08 21:20:03


# NewbieIGD|我爬取了整个Steam商品库，数据全在这——I Scraped the Entire Steam Catalog, Here’s the D

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-09-18 15:29:23
- **时长**: 23分37秒
- **播放**: 821 | 赞: 35 | 币: 5 | 藏: 72
- **链接**: https://www.bilibili.com/video/BV1Ppe16REpQ

## 视频描述

原视频：https://www.youtube.com/watch?v=qiNv3qv-YbU
（2024年12月8日）我从 Steam 的整个游戏目录中收集了数据，分析了超过 140,000 款游戏的各种信息，涵盖了 40 多个数据维度，包括游戏类型、评分、价格以及玩家反馈。通过这项分析，我得出了了一些非常有趣的结论。这一切都是出于对数据以及游戏开发领域的好奇心和热情。

=========

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1Ppe16REpQ
# 语言=en 时长=00:11:28 模型=large-v3

[00:00:00-00:00:04] Did you know that half of the top 50 games on Steam are indie titles?
[00:00:04-00:00:07] Or that there are only four fighting games with a romantic theme?
[00:00:07-00:00:08] Here's a fun one.
[00:00:08-00:00:12] Did you know that the word life appears in more game titles than death?
[00:00:12-00:00:15] Yet, war is mentioned twice as often as love?
[00:00:15-00:00:19] Today, we're diving into the data and exploring some fun insights into the game development industry.
[00:00:20-00:00:22] Let's start with the basics.
[00:00:22-00:00:26] In 2024, an average of over 70 games were released on Steam each day.
[00:00:26-00:00:29] A huge volume, and one that's grown tremendously over the years.
[00:00:29-00:00:34] Around 28% of games released last year hold a positive rating today.
[00:00:34-00:00:38] And of those, only 2% have managed to surpass the 10,000 reviews,
[00:00:38-00:00:40] showing both popularity and a strong reception.
[00:00:41-00:00:45] For context, the fighting roguelike Sifu sits around this level.
[00:00:45-00:00:48] While there are some great tools available for analyzing metrics like these,
[00:00:48-00:00:51] they don't offer the specific data I needed for my analysis.
[00:00:51-00:00:56] So I had to collect it myself, directly from the source, Steam itself.
[00:00:56-00:00:58] And that brings us to the methodology.
[00:00:58-00:00:59] I'll explain it so you can see it.
[00:00:59-00:01:07] I started by using Steam's API to pull the full catalog of over 200,000 apps.
[00:01:07-00:01:12] I pulled this data mid-October 2024, so all insights are based on that time frame.
[00:01:13-00:01:16] Once I had the full catalog, I wrote the script to pull data for each game,
[00:01:16-00:01:22] including details like its name, price, release date, and the rating and number of reviews.
[00:01:22-00:01:27] I used two endpoints from Steam, one for basic game details, and another for the user reviews.
[00:01:27-00:01:29] I also used Steam Spy.
[00:01:29-00:01:34] A third-party tool with an API that estimates key metrics, like player counts for each game.
[00:01:34-00:01:38] To complete the picture, I used web scraping to collect game tags.
[00:01:38-00:01:42] This means I run a program that navigated the entire Steam store,
[00:01:42-00:01:45] copying the tags for each game and saving them to a file.
[00:01:45-00:01:50] I found these tags especially valuable because they reflect both the developer's input
[00:01:50-00:01:52] and the community's influence on how the game is categorized.
[00:01:53-00:01:59] These scripts run for about 150 hours, that's over 6 days, gathering all the data,
[00:01:59-00:02:01] including the data needed for the analysis.
[00:02:01-00:02:04] The data from these APIs was messy and inconsistent,
[00:02:04-00:02:07] so I went through a systematic cleanup process.
[00:02:08-00:02:12] After sorting everything out, I ended up with more than 200,000 apps,
[00:02:12-00:02:17] roughly 140,000 of which were games or demos, each with a variety of attributes.
[00:02:17-00:02:22] This added up to millions of data points, so I organized everything into a database
[00:02:22-00:02:25] to make exploring and analyzing it much more efficient.
[00:02:25-00:02:29] And with that, let's dive into some interesting insights, starting with something light and fun.
[00:02:30-00:02:33] Here are the most common words in game titles on Steam.
[00:02:34-00:02:37] It's interesting to see how often certain genre names appear.
[00:02:38-00:02:40] Adventure, Simulator, Shooter, and many others.
[00:02:41-00:02:44] There's also a lot of emphasis on fantasy themes,
[00:02:44-00:02:47] with words like dragon and monster popping up frequently.
[00:02:47-00:02:52] And certain words align with available Steam tags, like zombies and even cats.
[00:02:53-00:02:57] Both cat and cats made the top list, which I thought was pretty funny.
[00:02:57-00:02:59] Then there are some unexpected ones,
[00:02:59-00:03:04] like paper or cube. Not sure what's going on there.
[00:03:04-00:03:06] If you're aiming for a unique or memorable title for your game,
[00:03:06-00:03:09] maybe steer clear of the words on this list?
[00:03:09-00:03:14] Or maybe these words are here because they are good descriptors that resonate with players.
[00:03:14-00:03:17] Familiarity could be appealing too. I'll let you decide what you think about that.
[00:03:18-00:03:22] Next, let's dive into the data on the highest rated and lowest rated games on Steam.
[00:03:22-00:03:27] For the top games, I focused on titles with an overwhelmingly positive rating,
[00:03:27-00:03:28] sorted by the number of reviews.
[00:03:28-00:03:29] For the top games, I focused on titles with an overwhelmingly positive rating, sorted by the number of reviews.
[00:03:29-00:03:29] For the top games, I focused on titles with an overwhelmingly positive rating, sorted by the number of reviews.
[00:03:29-00:03:33] This ranking highlights the most popular games that maintain an excellent reputation.
[00:03:33-00:03:38] It's worth noting that around half of the games in the top 50 are considered indie,
[00:03:38-00:03:43] including hits like Terraria, Stardew Valley, Hollow Knight, Hades, Undertale,
[00:03:43-00:03:46] Vampire Survivors, Factorio and Slay the Spire, to name a few.
[00:03:46-00:03:50] It's inspiring to see how these small teams, or solo developers,
[00:03:50-00:03:53] have created games that resonate with so many players.
[00:03:53-00:03:57] It's also interesting that some franchises appear more than once.
[00:03:57-00:03:59] For instance, both Portal and Portal 2,
[00:03:59-00:04:03] make the cut, as well as two titles from the Resident Evil series.
[00:04:03-00:04:07] Valve itself has an impressive presence, with six games in the top 50.
[00:04:07-00:04:11] The only other developers with multiple entries are SCS Software,
[00:04:11-00:04:14] Larian Studios and Capcom, with two titles each.
[00:04:15-00:04:18] At the other end of the spectrum, we have the lowest rated games.
[00:04:18-00:04:22] Remarkably, only 12 games on Steam have an overwhelmingly negative score.
[00:04:22-00:04:25] Even the least reviewed of these has more than 500 reviews,
[00:04:25-00:04:28] meaning all of them have a substantial base of feedback.
[00:04:28-00:04:32] I reviewed each title to understand why they performed so poorly.
[00:04:32-00:04:35] The game with the lowest score, War of the Three Kingdoms,
[00:04:35-00:04:40] is a 2021 release with nearly 60,000 reviews, filled with complaints about everything from
[00:04:40-00:04:46] lack of localization to gameplay issues, lag, aggressive monetization and accusations against
[00:04:46-00:04:52] the company's integrity. In several of these low-ranked games, players felt misled or scammed
[00:04:52-00:04:57] by paying for what they perceived as unfinished or poorly executed projects. Many of these games also
[00:04:57-00:05:02] faced severe technical problems, with frequent mentions of bugs and crashes.
[00:05:02-00:05:06] Interestingly, some of these titles were spin-offs of otherwise well-regarded series,
[00:05:06-00:05:10] like Command & Conquer, Airline Tycoon and Flatouts.
[00:05:10-00:05:15] Then there's Uriel's Chasm, which earned a kind of a cool status for its bizarre,
[00:05:15-00:05:19] chaotic gameplay that most players found impossible to enjoy.
[00:05:19-00:05:23] There's much to learn from both top-rated and low-rated games alike.
[00:05:23-00:05:27] With that, let's move into discussing untapped opportunities and unique ideas.
[00:05:27-00:05:33] I was curious whether there are combinations of genres or other properties that are still
[00:05:33-00:05:37] underexplored. For instance, are there any rhythm-based shooters out there?
[00:05:37-00:05:40] What about games that combine sports with a sci-fi setting?
[00:05:40-00:05:47] To explore this, I turned to data from Steam Tags. Steam offers a total of 447 predefined tags,
[00:05:47-00:05:50] which are added by both developers and players.
[00:05:50-00:05:56] I organized these tags further, subdividing them into categories based on my own interpretation to
[00:05:57-00:06:02] the players' preferences. I first focused on combinations of two genres, to identify
[00:06:02-00:06:07] original or underexplored ideas. To keep the results meaningful, I only included games with
[00:06:07-00:06:12] more than 10 reviews, and focused on the most popular genres, excluding the extremely niche
[00:06:12-00:06:17] ones that would add unnecessary noise. Each point on the graph represents a pair of genres.
[00:06:17-00:06:21] On the horizontal axis, I plotted the number of games in at least one of the two genres.
[00:06:21-00:06:27] This gives an idea of the individual popularity of the genres. If one of them is strong, the number goes up,
[00:06:27-00:06:30] and if both are popular, the plot point will end up on the far right.
[00:06:31-00:06:35] On the vertical axis, we see how many games are tagged with both genres simultaneously,
[00:06:35-00:06:40] which shows the opportunities. The lower the point, the more novel the combination,
[00:06:40-00:06:46] as fewer games share both genres. In summary, the most interesting opportunities are the ones
[00:06:46-00:06:51] that are farther down to the right, where both genres are popular but the combination is rare.
[00:06:51-00:06:56] For example, there are only three platformer Autobattlers, and Nansim particularly well known.
[00:06:57-00:07:00] There are also card game shooters, with Friends vs. Friends being the most famous,
[00:07:00-00:07:06] which I hadn't heard of before, but it looks pretty fun. Then, there are just three rhythm-based tower
[00:07:06-00:07:10] defense games. I could probably spend hours analyzing this graph. Instead, I'll link an
[00:07:10-00:07:14] interactive version in the video description, so you can explore other combinations on your own,
[00:07:14-00:07:19] and move on to talk about themes. The most common themes in games are fairly predictable, with a
[00:07:19-00:07:25] strong focus on fantasy and sci-fi settings. This is reflected in the frequent use of words like magic,
[00:07:25-00:07:27] monsters, space, etc. This is reflected in the frequent use of words like magic, monsters, space, or
[00:07:27-00:07:33] worlds in the titles of many games. Focusing on the 20 most popular themes, I explored combinations
[00:07:33-00:07:38] of these with different genres. With the top genres, it seems nearly all themes are well
[00:07:38-00:07:43] explored. Keep in mind, though, that not all themes have tags on Steam, so there's a selection bias at
[00:07:43-00:07:49] play. A few combinations stand out. There are only four romance-fighting titles, with Troublemaker
[00:07:49-00:07:54] being the most well-known. While this pairing might not attract a typical audience, there's
[00:07:54-00:07:56] definitely a niche for players who enjoy both. While this pairing might not attract a typical audience, there's definitely a niche for players who enjoy both.
[00:07:57-00:08:02] Another interesting combination is cooking games in a sci-fi setting, with around 10 games.
[00:08:02-00:08:07] In fact, on closer inspection, not all of these are truly cooking games. Some include cooking only
[00:08:07-00:08:13] as a feature. But the idea of, say, running a hot dog stand on an alien planet has a playful charm.
[00:08:13-00:08:19] So these combinations can definitely spark new ideas. Finally, I also reviewed genre combinations
[00:08:19-00:08:26] with tags related to dimensions, like 2D and 3D, and perspectives, like first person and third person.
[00:08:26-00:08:30] person. But it's probably best if you explore the data yourself. I'll link to all of these charts.
[00:08:31-00:08:36] One trend worth noting though is the steady rise in 3D releases. New 3D titles are now being launched
[00:08:36-00:08:42] almost as frequently as 2D ones. Let's take a brief pause from discussing video game genres
[00:08:42-00:08:49] to explore female and LGBTQ plus representation within the data. Around 10% of games on Steam
[00:08:49-00:08:54] are tagged with female protagonist, a number that seems surprisingly low. I had expected this
[00:08:54-00:08:59] percentage to show a steady growth over the years, but interestingly the trend isn't so clear.
[00:09:00-00:09:05] In contrast, LGBTQ plus representation shows a much clearer upward trend, with tagged games
[00:09:05-00:09:10] tripling in proportion over the past decade. The oldest title with this tag is Secret of the Magic
[00:09:10-00:09:17] Crystals from 2010, a game about breeding horses, I think. Moving on, let's dive into a specific
[00:09:17-00:09:22] genre of games that has piqued my interest as a player over the last few years. Card games,
[00:09:22-00:09:24] particularly roguelike deck builders.
[00:09:24-00:09:30] My favorite game in this genre, and perhaps even in general, is Slay the Spire. I've always thought
[00:09:30-00:09:36] it is a well-crafted fusion of genres, and I have often wondered if it was the catalyst for the rise
[00:09:36-00:09:42] of roguelike deck builders. By the way, as a quick side note, it seems roguelikes are significantly
[00:09:42-00:09:46] more popular in the indie scene compared to the AAA catalog. Platformers show a similar pattern,
[00:09:47-00:09:52] representing a much larger portion of indie games. Now, returning to roguelike deck builders in
[00:09:52-00:09:54] particular, I structured my analysis in a way that I think is very similar to what I've seen in the
[00:09:54-00:09:58] past. This is based on a framework from a study I found, which I think is excellent. I'll link that
[00:09:58-00:10:02] study and other references in the video description if you'd like to dive deeper. This graph shows
[00:10:02-00:10:07] the proportion of games on Steam that can be classified as roguelike deck builders over the
[00:10:07-00:10:12] past 10 years. This is based on game tags. Some of them are really helpful in pinpointing this
[00:10:12-00:10:17] subgenre. It's clear that Slay the Spire had a massive influence. Its release in January 2019
[00:10:17-00:10:22] sparked a significant rise in the number of games in this category. And in less than 5 years,
[00:10:22-00:10:24] the genre's presence in the Steam catalog,
[00:10:24-00:10:30] grew by 5 times. When we examine the popularity of these games, measured by review counts,
[00:10:30-00:10:34] we see that while the genre has grown, most titles still remain relatively niche,
[00:10:34-00:10:39] accumulating fewer than 100 reviews. However, there are some standout successes,
[00:10:39-00:10:45] like Inscription and Balatro. Interestingly, the red dots in the graph represent War of the Three
[00:10:45-00:10:49] Kingdoms, the lowest rated game on Steam, which we discussed earlier. For those of you who are
[00:10:49-00:10:54] as hooked on this genre as I am, I've put together a graph showcasing some of the best
[00:10:54-00:10:59] roguelike deck builders out there. These are the 20 games that balance both user rating and
[00:10:59-00:11:04] popularity the best. I've played many of them and can confirm they are fantastic. The rest
[00:11:04-00:11:09] will likely be my next addiction. If you have suggestions for other analysis, questions about
[00:11:09-00:11:13] the methodology, or if you spot any errors, feel free to reach out on Discord or in the comments.
[00:11:13-00:11:16] I'll update the description or maybe the pinned comment with any corrections based on your
[00:11:16-00:11:21] feedback. It was really fun to dive into this data, and I hope you found it interesting. See you next time.
