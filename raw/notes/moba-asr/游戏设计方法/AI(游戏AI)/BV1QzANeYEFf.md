---
title: "GMTK|字幕|潜行学院1-潜行游戏的守卫是如何看和听的"
platform: bilibili
bvid: BV1QzANeYEFf
author: 庸才的朽木
author_uid: 49665055
pubdate: 2025-02-15 16:29:49
duration_sec: 763
view: 265
like: 16
coin: 3
favorite: 18
reply: 4
danmaku: 0
share: 2
url: https://www.bilibili.com/video/BV1QzANeYEFf
subtitle_source: asr_Qwen3-ASR-1.7B
asr_model: Qwen3-ASR-1.7B
asr_elapsed_sec: 154.6
transcript_chars: 11712
crawl_time: 2026-05-24 20:55:26
---

# GMTK|字幕|潜行学院1-潜行游戏的守卫是如何看和听的

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2025-02-15 16:29:49
- **时长**: 12分43秒
- **播放**: 265 | 赞: 16 | 币: 3 | 藏: 18
- **链接**: https://www.bilibili.com/video/BV1QzANeYEFf

## 视频描述

原视频：https://www.youtube.com/watch?v=Ay-5g36oFfc
（2020年3月26日）欢迎来到潜行学院，这是关于潜行游戏如何运作的GMTK迷你剧集。 在本中，我将解释守卫的感知和意识，守卫如何看和听，以及不同的解决方案是如何制造不同的游戏体验？ 订阅以确保您能看到后续章节。
---出现的游戏（按出现顺序）---
合金装备3：食蛇者（Konami，2004）
细胞分裂：黑名单（Ubisoft Toronto，2013）
耻辱（Arkane Studios，2012）
合金装备V：原爆点（Kojima Productions，2014）
刺客信条II（Ubisoft Montreal，2009）
蝙蝠侠：阿卡姆骑士（Rocksteady Studios，2015）
忍者之印（Klei Entertainment，2012）
漫威蜘蛛侠（Insomniac Games，2018）
隐形公司（Klei Entertainment，2015）
最后生还者（Naughty Dog，2013）
回声（Ultra Ultra，2017）
合金装备（Konami，1998）
细胞分裂：混沌理论（Ubisoft Montreal，2005）
神偷：暗黑计划（Looking Glass Studios，1998）
杀手2（IO Interactive，2018）
孤岛惊魂·新黎明（Ubisoft Montreal，2019）
荒神（Lince Works，2016）
只狼·影逝二度（FromSoftware，2019）
耻辱2（Arkane Studios，2016）
地平线·零之曙光（Guerrilla Games，2017）
蝙蝠侠：阿卡姆疯人院（Rocksteady Studios，2009）
刺客信条：起源（Ubisoft Montreal，2017）
合金装备V：幻痛（Kojima Productions，2015）
音量（Mike Bithell，2015）
影子战术:将军之刃（Mimimi，2016）
杀出重围：人类分裂（Eidos Montreal，2016）
狡狐大冒险（Sucker Punch Productions，2002）
The Marvellous Miss Take（Wonderstruck，2014）
DOOM（id Software，2020）
逃生（Red Barrels，2013）
异形：隔离（The Creative Assembly，2014）
骗局（Size Five Games，2015）
冥河:暗影碎片（Cyanide，2017）

## 完整文稿

> 来源: asr_Qwen3-ASR-1.7B

There aren't many genres with such strong fantasy as stealth games. These games are staying unseen and striking from the shadows. About spotting and tying up enemies, they are the main thing. This, these games are spies, assassins, and Batman. But making this fantasy work means balancing a number of complicated systems, from awareness to information gathering to robust detection systems. Get any of them wrong, and the whole thing can crumble in on itself. So welcome to the school of stealth. This is a short GMTK mini-series about how stealth games work. In each episode, I'm going to take one system from the stealth game formula and break down how it works. Looking at the series at the technical side of things, the design considerations and the end experience. For episode one, we need to start where most stealth games begin, with the player being hidden. And then ask ourselves, how do guards actually see and hear the player? Ultimately, guards in games are given virtual eyes and ears that are designed to simulate the two main human senses, sight and sound. To simulate vision, video game guards typically have a view cone, which is invisible, just like entering the enemy's face. If the player character enters the cone, they get detected. It's a touch more complicated than that, of course. A simple cone would allow characters to stay unseen, even if they were right next to the enemy. So more complex systems are often used. In stealth blacklists, the basic vision cone for the guard primarily sight, but the second might work to simulate peripheral vision and even a small area behind the guard to mimic that sense of knowing when someone's just over your shoulder. Developers will need to consider the height of the cone, depending on where the player should be able to hide when there are enemies. To know if the player is in cover, a game typically uses a raycast, which basically when an invisible line is drawn between two elements to see. In this case, if anything is in the way, you can make this more complex. The catchments of partial cover. So in stealth, the enemy raycasts the eight different points in sight of the player model and will only spot him if he's at a number of visible. Now, if the player enters the cone and isn't in cover, they probably don't get immediately spotted. Instead, the guards awareness of the player starts to grow. This speed with this meter fills might be slow if the character is further away or only in the guard's peripheral vision, for in light or crouching down or staying perfectly still. When the meter tops out though, the guard will know exactly where you are. It's also important to note the guards can be aware of more than just the player character, such as open doors, interesting objects, or dead bodies. This can be used to make interesting plans like traps and distractions, but it can also help give the impression of intelligence and awareness. Now, simulating hearing is a different problem. When you make a sound like firing a gun, walking on a loud floorboard, or throwing a stone, the sound will be given a distance related to the volume of noise. Any guard who is within distance can then be told to check out the source of that sound. However, a straight line between the sound and the guard won't work because we expect noises to be multiple bounces. So the typical solution is to use the game's parfying system. The same tech allows an enemy to find their way around the world without bumping into objects, make the sound travel across that, and feel more realistically capture the way sound propagates through an environment in real life. That's the gist of things then, but more complex stuff might be included in certain games. For example, in thief, guards can have second-hand information about the player based on what enemies are up to, and hinting to, in forcing characters away less perceptive agents from observing if they're facing away from them, which gives the devices more power. Links to more detailed technical information can be found in the description beneath this video. When done well, this system should create a pretty realistic representation of human visual and auditory perception. You can then make educated decisions about where you will be safe using your real world knowledge of how sight works in different conditions or how sound might be amplified. But this always going to be a certain level of ambiguity for the player to deal with, which can lead to friction and frustration. I'm sure you've played stealth games with thoughtfully visible but the guards somewhere. So to help players make sense of this stuff, there's a few ways that devs can make these perception systems more obvious. The first is helpful in development, even when back in thief, the developers knew that it was tough for players to understand how their character was from a first-person perspective. So there's a light at the bottom of the screen to show your current visibility, and in stealth, the awkward challenge of knowing how much sound you're making is helped by visual on sound heads-up display. Also, most games have some kind of detection indicator on their interface, which mimics the guards awareness meter from earlier. This helps the player know that they're about to be made, and sometimes even shows you the location of the guard who's seeing you. Next up is using animation and audio to help communicate guards to the player. A guard who is ideally lazy about, might suggest they have pretty weak perception, but a suspicious enemy with their weapon raised will be way more alert to potential threats. Audio works also helps you know that the guard is starting to become aware of you. Then there are refuge spaces. These are places in the game world where, in normal circumstances, you are ambiguously hidden. That might be the high guard hills in Batman or areas of long grass in assassins creed or crates and cubbies in Hitman. These give you at least one place where you can scout and plan for a position of total safety. Another solution is player filtering, which is the art of handicapping systems to bias the player. As stealth blacklists program Martin Walker says, it doesn't matter what the NPC can see or hear from a simulation perspective. It's what the player thinks the NPC should be able to see or hear. So in his game, a guard's hearing is reduced by half when they're off screen, because it feels unfair to be heard by someone you can't even see. And in the last verse, enemies typically raycast to just head to determine line of sight, but that changes to chest when he's crouching to let him peek over cover without being spotted. And then the biggest helpful as discussed earlier is fuzzy detection system. If you were immediately spotted when you touched the guard's vision cone, that wouldn't feel very fair. So it makes sense that guards take a few moments to become aware of your presence before being totally alerted. Now there's one final and rather bold solution to this problem, and that's simply revealing systems to the player in the excellent side scrolling neon up marker ninja. The guard's perception is about as ambiguous as you can get. The vision cone is displayed on screen. The ninja is either in shadow or light, and that shown on the character sprite. And when you make noises, you can see the emanating from the source as big round pulses. This is also shown to you before you even make the noise, which is helpful for knowing whether your noisy distraction or sneaky getaway will be successful. With the info on screen, there's no arguing about what's happening in the system. You're either in the cone or not, and that sound either reached the guard's ears or didn't. And so ninja's binary perception system can be paired with the totally binary detection system of instant awareness. Though there is a slight analog fuzziness on the very edges of the enemy view cones. So up there, for a slightly more nuanced take on this, check out Shadow Tactics Blade of the Shogun. Here, the vision cone is split into three zones. The bright green part near the enemy's face is the danger zone and leads to a pretty instant detection. In the dark green part, you can stay hidden if you're crouching down, but will be spotted if you stand up. And the dotted part is for refuge zones, places and hideouts where you will always be invisible. If you do trip the view cone, the whole cone will fill up with yellow, and if the yellow part touches your character, you're spotted. It's a very elegant way of displaying all the necessary information right there on screen. Of course, it's a lot harder to show this stuff in fully 3D game. The original Metal Gear Solid solution was to simply photocopy the game world into a top-down 2D representation on your radar, and then draw the vision cones on that. It's a sort of handwavey solution that's still being used in games like Deus Ex and divided, but it's not impossible. The light blue series has guards with torches that cast obvious pools of yellow light. If you find yourself inside the light, you get spotted, but otherwise you're safe. Caught too? Yes, but also immediately readable. The most important thing though is the experience that these different perception systems lead to. When the system is made analog and ambiguous, the player must value the environment with immersive and realistic understanding of light, shadow, distance, sound, and it also gives the game a certain level of tension. We can never be one hundred percent sure that you're safe. I think this fits quite nicely with the core stealth fantasy. These are games where you're how it doesn't come through sheer force, but only through ability to hide from the enemy. So having your sneaky status be fragile and fuzzy reminds you that you're always at risk of losing your tenuous advantage over the enemy. As thief programmers says, it's about getting the players hard pounding by holding them on the cusp of being found. And it's especially important to hide this off in final horror games, the borrowed stealth elements in a game like Alien Isolation. It would be rubbish if you could see exactly where the xenomorph was looking. A huge amount of fear and anxiety is derived from your shaky knowledge of the aliens' senses. But making the system completely obvious has its own advantages. It puts way more power in your hands and allows you to play with a huge amount of confidence. You can feel more like an operator, learning enemies and traps, sneaking in for silent kill, as ninja producer Jamie Chambers put it, as we're iterating, I found that I wasn't nearly interested in guessing whether a guard would hear you or not, and I'm more interested in creating an elaborate death trap. Of course, the predator feel can be achieved through other methods, like those aforementioned refuge zones and by giving the player a backlog of gadgets and superpowers. But the more accurately they can predict the enemy's perception, the quicker the player will get to that experience. So that's it for this one. Stealth game guards see and hear through systems of simulated eyes and ears, and developers can create very different experiences depending on how much of that system they surface to the player. Come back next time for more deep dives into sneaking up design. And if you subscribe to my channel, you'll get access to the new episodes sooner than life. Hey, thanks for watching. I hope you're all doing okay in the midst of this awful coronavirus pandemic. It's such a scary situation, so please stay safe, wash your hands, and follow the necessary guidelines. I'll do my best to keep making interesting stuff to keep you busy and entertained.

## 热门评论

- **对不起！我错了！** (赞1): 厉害👍🏻
- **庸才的朽木** (赞1): --- 资料来源 ---
在细胞分裂：黑名单中模拟AI感知和意识| GDC保管箱（免费访问） https://www.gdcvault.com/play/1020436/Modeling-AI-Perception-and-Awareness
沙箱中的空间：开放世界游戏中的策略意识| GDC保管箱（免费访问） https://www.gdcvault.com/play/1018038/Spaces
- **Ainerce** (赞1): 互相点赞赞👍[doge][星星眼][呲牙][打call][喜欢][笑哭]