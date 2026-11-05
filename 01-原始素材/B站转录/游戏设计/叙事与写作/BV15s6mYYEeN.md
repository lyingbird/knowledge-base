---
title: "【双语字幕|GMTK】GMTK10年的10个游戏设计经验教训——Game Design Lessons from 10 Years of GMTK"
platform: bilibili
bvid: BV15s6mYYEeN
author: 庸才的朽木
author_uid: 49665055
pubdate: 2025-01-03 14:31:54
duration_sec: 938
view: 199
like: 7
coin: 1
favorite: 9
reply: 0
danmaku: 0
share: 1
url: https://www.bilibili.com/video/BV15s6mYYEeN
subtitle_source: asr_Qwen3-ASR-1.7B
asr_model: Qwen3-ASR-1.7B
asr_elapsed_sec: 206.4
transcript_chars: 12783
crawl_time: 2026-05-21 18:48:02
---

# 【双语字幕|GMTK】GMTK10年的10个游戏设计经验教训——Game Design Lessons from 10 Years of GMTK

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2025-01-03 14:31:54
- **时长**: 15分38秒
- **播放**: 199 | 赞: 7 | 币: 1 | 藏: 9
- **链接**: https://www.bilibili.com/video/BV15s6mYYEeN

## 视频描述

原视频：https://www.youtube.com/watch?v=Cm2_drGLGbc&t=511s
Game Maker's Toolkit 刚刚诞生 10 周年！以下是我在过去十年学习游戏设计过程中学到的十大教训。

=== 展示的游戏 ===
Game Dev Story（游戏开发物语）| 2010
Persona 5 Royal（女神异闻录5皇家版）| 2019
Portal（传送门）| 2007
Neon White（霓虹白）| 2022
Rollerdrome（滚轴之王）| 2022
Overcooked! 2（胡闹厨房2）| 2018
Uncharted 2: Among Thieves（神秘海域2：盗贼末路）| 2009
Far Cry 4（孤岛惊魂4）| 2014
Far Cry 2（孤岛惊魂2）| 2008
Donkey Kong（大金刚）| 1981
Devil Daggers（恶魔之刃）| 2016
Bayonetta（贝优妮塔）| 2009
Tony Hawk's Pro Skater 1+2（托尼·霍克职业滑板1+2）| 2020
Anger Foot（愤怒之足）| 2024
Assault Android Cactus（突击安卓仙人掌）| 2015
Crash Bandicoot 4: It's About Time（古惑狼4：时机已到）| 2020
Dark Souls（黑暗之魂）| 2011
Doom（毁灭战士）| 1993
Marvel's Spider-Man（漫威蜘蛛侠）| 2018
Bionic Commando（生化奇兵）| 2009
Super Mario Odyssey（超级马里奥：奥德赛）| 2017
Pseudoregalia（伪圣域）| 2023
Super Mario Bros. Wonder（超级马里奥兄弟：奇迹）| 2023
New Super Mario Bros. U（新超级马里奥兄弟U）| 2012
Super Mario Bros.（超级马里奥兄弟）| 1985
Marvel's Spider-Man 2（漫威蜘蛛侠2）| 2023
Redfall（红落）| 2023
Celeste（蔚蓝）| 2018
Rogue Legacy（盗贼遗产）| 2013
Returnal（回归）| 2021
Rogue（Rogue）| 1980
Mario Kart 8 Deluxe（马里奥赛车8豪华版）| 2017
Nioh（仁王）| 2017
The Surge（迸发）| 2017
Salt and Sanctuary（盐与避难所）| 2016
XCOM: Enemy Unknown（幽浮：未知敌人）| 2012
Marvel's Guardians of the Galaxy（漫威银河护卫队）| 2021
The Turing Test（图灵测试）| 2016
Into the Breach（陷阵之志）| 2018
Watch Dogs: Legion（看门狗：军团）| 2020
Middle-earth: Shadow of War（中土：战争之影）| 2017
Ape Out（猿出没）| 2019
Star Wars Jedi: Survivor（星球大战绝地：幸存者）| 2023
Hollow Knight（空洞骑士）| 2017
Inside（Inside）| 2016
Hitman 3（杀手3）| 2021
Titanfall 2（泰坦陨落2）| 2016
Sackboy: A Big Adventure（麻布仔大冒险）| 2020
A Little to the Left（稍微往左一点）| 2022
Mind Over Magnet（磁力之上）| 2024

## 完整文稿

> 来源: asr_Qwen3-ASR-1.7B

On November 20th, I uploaded the first video to a YouTube channel called Game Maker Toolkit. A channel where I tell you absolutely everything I know about game design. And now, ten years, two hundred videos, eight games, and countless engine designs later, I can finally reveal the truth. I didn't really know anything about game design because despite the fancy motion graphics, the low-fi hip-hop soundtrack, and the commanding British accent, all things helped give the channel an authority and not. I am truthfully noobs, but I wanted to learn. I wanted to understand the craft and players behind my very favorite hobby, and so every video was an opportunity for me to find out more through research, interviews, analysis, and then I could pop on YouTube and share what I learned with all of you. And you know what? It worked. I learned so much about the field of game design in this last decade, and so to mark this massive milestone, I want to share with you the ten biggest lessons of them all. Basically, if I could boil down fifty hours worth of GMTK videos into a single episode, this is what I would make. So join me on a whistlestop tour of the lessons, learnings, revelations, and mistakes from the first ten years of running this channel. I'm back, and this is Game Maker Toolkit. Lesson one: One of my very first videos looked at two games, Far Cry 2 and Far Cry 4. Now, on the surface, these games are very similar. They're both about war in fictional countries, they both have charismatic villains, they both have enemies and exotic animals, and they both have the words "far" and "cry" in them. What the difference? But the similarity end there because when you actually pick up the controller and start playing, you realize that these games are completely different. One is a thrilling blockbuster action movie roller coaster, and the other is literally the worst package of day you've ever been on. And so, with this video, I learned one of the most fundamental game design lessons: the game's experience is not driven by the plot, or by the graphics, or by the setting, but by the game mechanics. Far Cry 4 is fun because you have load ammo, you can track your enemies, and you can perfectly wipe your foes off the map. And Far Cry 2 is harrowing because your weapons can jam, your jeep can break down, you have to stay far out of the area and dying sends you all the way back to the last safe station. So if you want to understand why a game makes you feel a certain way, ask yourself how do the mechanics contribute to the experience. Lesson two: In 2018, I made a video that asked the question: Are high scores and leaderboard still relevant in modern games, or are they just antiquated relics of the arcade era? If you were hoping for a definitive answer one way or the other, you'd be disappointed because the truth is, it depends. This mechanic makes sense in some games and doesn't work for others, and there are both pros and cons to including such systems in your game. And so, with this video, I learned the lesson that there's no such thing as right or wrong game mechanic, as per lesson one. It totally depends on what sort of experience you want players to have. I revisited this point a number of times. Are lives outdated game design should relate, save your progress between runs. Should the game have fixed camera effects? The answer is always the same. It depends on the type of game you're making. It's tempting to use game mechanics because it's trendy, or to ignore a mechanic entirely because it feels outdated, but the only way to judge a mechanic is to ask whether or not it can contribute to the experience you're trying to forge. Lesson three: In that same year, I made a video about in some games, first Spiderman game, and came to the conclusion that the game was pretty disappointing because the web-swing system was so simple and you can swing through an hazard just by holding down a button. The game employs dozens of hidden physics to aid your every move, and it's impossible to spot Spiderman inside a skyscraper. Now, I thought the lesson of that video was that in order to give the player a thrilling experience, you had to provide significant challenge with complex inputs and high stakes for failure. But the real lesson of this video was I was wrong because sure, the game was disappointing to me, a hardcore gamer who loves in-depth movements systems with high skills games, but never asked the question was Spiderman actually made for me? Because a game is built for a target audience, a specific type of person or player, and if you consider that a blockbuster PS4 movie tie-in is probably aimed at more casual gamer, well then, in some games, it really be praised for finding a way to give those players incredible sensation of being Spiderman, even if it didn't work for me. So when it comes to making a video game, you have to decide who this game is for, and tune your mechanics appropriately. You can't please everyone. Right. Lesson four. Well, I don't know actually, because earlier this year I made a video called Super Mario's Invisible Difficulty Settings, and in this one, I looked at how Nintendo tries to make its flagship franchise fun for everyone. Like modern Mario games are made for families and newbies, so there's always such a way that it's pretty easy to make your way to the final boss and the end of the story. But if you're seasoned playing pro, who's been stomping who since nineteen eighty-five, well, you're not going to be bored. That's because there's loads of optional harder content to sink your teeth into, tricky coins to collect, tough levels to play, secret post-game worlds to unlock, and challenges to finish. So with this video, I learned the options and bonus content can be used to make a game appealing to those who are more hardcore than the target audience. And hats off to in some games who included settings for harder swinging in Spiderman. Lesson five. But what about the other way around? What if you make a game that's really difficult and then find that certain players are unable to play or finish it? I grappled with this when asking the question should dark souls have an easy mode? I mean, from soft, hard, and fantasy epic is intentionally challenging to give players a specific experience of being scared of your limits, but then having a feeling of triumph when you finally overcome those impossible odds. Now, sure, you could provide an easy difficulty mode, but if players pick that option, wouldn't it rob them of the intended experience? Well, I learned in part lesson in the video what makes the most special. This precision platform is also crushingly difficult, but unlike Dark Souls, it features a wildly permissive option to make the game as easy as you need it to be. But here's the kicker: the developers clearly explained the point of this mode before you turned on. They make it clear how the soft is supposed to be played, but also offer a way to reduce difficulty if you need it, say if you're new to games or you live with a disability, or you're more interested in the storyline than the challenges. Options, accessibility settings, and easy modes don't have to push the right to your intended experience. You just have to find a smart way to push players into seeing the version of the game that fits their needs best. Lesson six. Okay, let's move off track and talk about something else. One of the most popular subjects in game discourse is the topic of genres. Not a game is by on Reddit without someone asking if a game truly counts as a roguelike, and we can all agree that GMTK is flawed without someone pointing out that Mario Kart is secretly a massive sandbox. But in the video, do we need this sort of genre? I learned that what's vital for players to get properly played with genres, we don't want our game designers to be so obsessed. You see, when the video released in 2017, we were inundated with games that closely copied the from soft formula, games with hastily renamed versions of souls, bonfires, and esdevs, and they all felt pretty samey. That's because if you consider genres to be a long list of must-have mechanics used in a specific game, well, you end up making the same thing over and over again. Instead, designers should think of genres in the loosest possible terms. That way, you can add and remove features, out well mix-match different genres, and make stuff that feels fresh and very, rather than predictable. And for me, lesson seven, you might think that the best way to make any AI is to craft a slightly convincing, ultralike game experience to be in. But when I did the research for the video, what makes good AI? I realized the point of AI is not to try and pass the Turing test; it's to present interesting gameplay, and again, as per lesson one, give players a specific experience. And ever since that video, I've made a habit of breaking down seemingly complex systems to see how they actually quite simple, and how the real trick is using the basic systems to create magical experiences for players. So by looking at the necessary systems and the AI of them all, and more, I learned that the best solution for a complex problem is whatever provides the most interesting experience to the player. Lesson eight. Okay, so with all this theory and analysis underbelts, you might think we have everything we need to know in order to make our own game, but we're wrong because when I started to make my own games, I quickly discovered that game idea is basically worthless until you actually build it and try it yourself. Our brains are truly bad video game simulators. Everything seems fun in my mind, but you can only spot the problems the designers and the intended issues when the game is real. Theory can get you far, but nothing beats playing the game itself. But that's not all bad, as I saw in the video, the games that designers solve sometimes the best game ideas actually come about through the process of making the game. Whether it's a bug, a happy accident, or a sudden realization amazing that occurred during the development process, ultimately a game idea is worthless until you prove its value through a prototype. Lesson nine. By the end, you're going to see that your game design is busted because as I learned many many times during the development of my own game, players are quick to find faults that you never knew your game had. They go into games not understanding controls, overthinking, and underthinking your puzzles, making assumptions you never considered, and more. So as I saw in the video, developers often it pays to get playtesting involved every stage of the process. And as I learned in the video, how game designers solve these different problems being a designer is much about solving playtesting problems as it is about coming up with cool new game ideas. Game design is about building a game for other people, so playtesting should be used to make sure your design is effectively producing the results you desire. Lesson ten. And finally, I think the biggest lesson I've learned through all of this is that any lesson you learn needs to be constantly revisited, things change, people change, your opinions change, the industry changes, trends change, and more than any of that, we can make mistakes, so it's important to always be open to everything. Basically, never take some game design lesson as gospel, especially if it's coming from YouTube. Take in as many game design lessons as you can to make sure you always figure out yourself if game design lesson is true for you and for the type of games you want to make. So there we have it, the ten biggest lessons I've learned from ten years of doing Game Maker Toolkit, and what those ten years have been aside from the videos I've made, I've been lucky enough to travel the world and give talks, lectures, and so many schools and studios, and I've been privileged enough to do consulting work on some amazing games. There's also the GMTK game jam, incredible annual celebration of the GMTK community talent, and this has led to the creation of some truly awesome games. It's crazy to think that games like a Little to the Left and Rollerdrome started life on our silly little jam. I hugely thank you to everyone who helped out with this event every year, and now I'm almost ready for the next big step with this channel. As next week, I'm launching my first proper video game, Mind Over Matter, which will be released on Steam on November 15th for PC and Mac. So what will the next ten years hold for GMTK? I can't wait to find out with you. One final thank you to the amazing patrons who support GMTK financially. Every month, you are the only reason I'm able to do this. I am forever indebted. See you soon.
