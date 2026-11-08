---
title: "Noodle|我用一个月学关卡设计，只为证明你错了——I learned level design in a month to prove you wrong"
platform: bilibili
bvid: BV1Xv4j6qE9T
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-11-07 14:05:42
duration_sec: 4816
view: 883
like: 32
coin: 4
favorite: 56
reply: 4
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV1Xv4j6qE9T
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 49954
crawl_time: 2026-11-08 21:20:01


# Noodle|我用一个月学关卡设计，只为证明你错了——I learned level design in a month to prove you wrong

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-11-07 14:05:42
- **时长**: 1小时20分16秒
- **播放**: 883 | 赞: 32 | 币: 4 | 藏: 56
- **链接**: https://www.bilibili.com/video/BV1Xv4j6qE9T

## 视频描述

一扇门该有多大？答案比你想的大得多——而且不只是门。走廊、房间、厕所，我玩过的每一款游戏，几乎都把实体空间悄悄放大了一圈。
为了证明这件事，我花了一个月啃 Hammer 编辑器，按 1:1 比例重建了一张《半条命2》地图：混凝土储物间、窄走廊、塞满东西的电脑房、寒酸的厕所，全部按现实尺寸来。一编译就发现问题——走廊窄到门框会卡住横移，玩家根本挤不过去；想靠掩体躲一下，身后偏偏是死路。
中途我把《E

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1Xv4j6qE9T
# 语言=en 时长=00:40:07 模型=large-v3

[00:00:08-00:00:14] how big is a door? Answer in the comments. WRONG! Some years ago, I was clued into some
[00:00:14-00:00:20] insider gaming knowledge. I was told that practically every single physical space in
[00:00:20-00:00:30] every video game I've ever played is... it's too big. From buildings to hallways to walls to doors.
[00:00:30-00:00:37] What you're looking at right now is a screenshot used in a slide in a GDC talk from 2002.
[00:00:37-00:00:44] This is the real shape of the thing, whereas this one is, uh, it's built to scale. And it looks
[00:00:44-00:00:49] it looks wrong. They both look... don't they? They both look wrong. This one's got so much
[00:00:49-00:00:55] negative space, this one looks like it was made for a child! Once I saw it, I couldn't stop seeing
[00:00:55-00:01:02] it everywhere. Basically every single game, from the silliest of arcade modes to the most grounded
[00:01:02-00:01:06] and tactile... I don't know, I could think of, like, two exceptions.
[00:01:07-00:01:09] And one of them's just a level, not even a whole game!
[00:01:11-00:01:15] You don't believe me, do you? You're thinking to yourself, you've played a game that's proportioned
[00:01:15-00:01:21] totally correctly. You're thinking to yourself, surely it's not that bad. Surely not every game
[00:01:21-00:01:27] has to be so violently wide. You're wrong. I mean, there's a reason for this, right?
[00:01:27-00:01:32] Player locomotion in games is usually faster than your real life walking speed and the world
[00:01:32-00:01:37] has to accommodate for that. More space means more room to flail around. I could further my
[00:01:37-00:01:41] argument by then showing you this footage, or this footage, or this footage, and then I say, see?
[00:01:43-00:01:47] Wide. But you still don't believe me. You're trying to think of examples right now that prove
[00:01:47-00:01:50] me wrong. You're getting ready to tab off this video and dig up a Dark Souls hallway like that
[00:01:50-00:01:54] shit isn't two feet too wide and three feet too tall. Fuck you. You know what, I'm gonna prove it.
[00:01:54-00:02:00] I'm going to debase myself as an essayist by making something instead of just talking about
[00:02:00-00:02:06] it. I'm gonna make a realistically sized map just to prove how wrong it feels. And then I'm gonna
[00:02:07-00:02:13] remake it in gaming size just to really nail the point home. Shigeru Miyamoto once said,
[00:02:13-00:02:17] Get what you need and get out. That's the gameplan. That's the mission here.
[00:02:18-00:02:22] Of course, he was talking about carjacking. But I'm making a level. Step one is to decide
[00:02:22-00:02:28] I'm making the level... In. I might start from scratch with Unity or Unreal, but that'd be
[00:02:28-00:02:33] fucking stupid, in next time I'd also need to design an entire the rest of a video game.
[00:02:33-00:02:35] Better to make something for a game that already exists, that already has the
[00:02:35-00:02:35] power to kill two birds with one stone, than to make this'm石 that preratting you to life.
[00:02:35-00:02:36] butthat'd be fucking stupid because then I'd also need to design an entire the rest of Beta для
[00:02:36-00:02:36] make the video game. Better to make something for a game that already exists, that already has the power to kill two birds with three
[00:02:36-00:02:41] has all the assets, the tools, the game design in place for me to build around.
[00:02:47-00:02:47] Great.
[00:02:48-00:02:50] Valve games all come with the Hammer level editor.
[00:02:50-00:02:56] Now, the second thing any Hammer user will tell you is how much they love using the Hammer editor.
[00:02:56-00:03:00] Which is good, because the first thing any Hammer user will tell you is how much they
[00:03:00-00:03:06] fucking hate using it so bad that there's a community-updated version out there that
[00:03:06-00:03:08] aims to make it bearable.
[00:03:08-00:03:25] Opening any kind of serious program like this for the first time is like visiting your friend's
[00:03:25-00:03:26] house for the first time.
[00:03:26-00:03:27] Everything is wrong.
[00:03:27-00:03:28] I don't know what the rules are.
[00:03:29-00:03:30] Their parents are divorcing.
[00:03:30-00:03:32] Where does your mom keep the cups?
[00:03:32-00:03:33] How do I...
[00:03:33-00:03:34] Where's the floor?
[00:03:34-00:03:36] So you ask your friend where the floor is.
[00:03:37-00:03:40] Your friend is a dozen YouTube videos from 2013.
[00:03:45-00:03:47] Hi, welcome to the first Hammer tutorial.
[00:03:47-00:03:49] This is going to be setting up Hammer.
[00:03:49-00:03:54] Progress is agonizingly slow at first, but progress is happening.
[00:03:54-00:03:54] The project is...
[00:03:54-00:03:55] Is moving.
[00:03:56-00:03:57] Your friend's dad is moving.
[00:03:57-00:03:58] I'm making progress.
[00:03:58-00:03:59] I've come a long way.
[00:04:00-00:04:00] I don't...
[00:04:00-00:04:01] I don't know what I'm doing.
[00:04:01-00:04:05] I want to make a train station, but I quickly realize that that's fucking stupid.
[00:04:05-00:04:06] Train stations are large.
[00:04:06-00:04:08] This doesn't prove my point at all.
[00:04:08-00:04:09] What am I...
[00:04:09-00:04:10] The JPEG was built in our rooms.
[00:04:11-00:04:13] Those are small, and I've been in those.
[00:04:14-00:04:15] That should be my idea.
[00:04:16-00:04:16] One thing leads to another.
[00:04:17-00:04:20] I channel what I reckon an Eastern European reckons a building is.
[00:04:20-00:04:21] I get lost in the sauce.
[00:04:21-00:04:22] I start embellishing.
[00:04:22-00:04:24] I find out how to add props.
[00:04:24-00:04:24] And then...
[00:04:24-00:04:25] Now there's props everywhere.
[00:04:26-00:04:27] I add a drive-thru.
[00:04:27-00:04:30] And a couple days later, I have something that's...
[00:04:30-00:04:31] Kind of looks like a level.
[00:04:32-00:04:36] Speaking of which, actually, do you want to have a look at my awesome progress?
[00:04:36-00:04:37] Oh, sure.
[00:04:38-00:04:45] Basically, I'm just trying to think of all sorts of real places that it'd be terrible to play Half-Life 2 in and...
[00:04:45-00:04:45] Tapping in.
[00:04:46-00:04:47] Oh, fuck.
[00:04:48-00:04:51] Spawn the maintenance closet into the narrow hallway.
[00:04:51-00:04:52] Big-ass door.
[00:04:52-00:04:52] Big-ass door.
[00:04:53-00:04:54] I mean, it's not...
[00:04:57-00:05:01] To the computer room where Zombie keeps throwing shit at you the second the door opens,
[00:05:01-00:05:03] and I don't know how to stop him from doing that.
[00:05:04-00:05:07] I should be able to just compile it and show you what it looks like in-game.
[00:05:08-00:05:09] Or I could go fuck myself.
[00:05:12-00:05:13] Okay, I...
[00:05:13-00:05:13] Beautiful.
[00:05:13-00:05:15] Have some work to do with the props.
[00:05:18-00:05:21] It's interesting how still very large this space feels.
[00:05:21-00:05:22] Yeah.
[00:05:22-00:05:22] Yeah.
[00:05:23-00:05:25] I mean, it might even be a bit wide.
[00:05:25-00:05:26] Oh my god, fuck off!
[00:05:27-00:05:28] But it doesn't make sense.
[00:05:28-00:05:32] You cannot make this hallway smaller without doors.
[00:05:32-00:05:35] Scraping the seat without, like, the doors scraping the ceiling.
[00:05:35-00:05:40] Well, that's the problem, is that it looks right relative to the door, which is larger than a normal door.
[00:05:40-00:05:42] Yeah, it's very large.
[00:05:42-00:05:45] Like...
[00:05:45-00:05:46] Is it, though?
[00:05:47-00:05:48] Yeah.
[00:05:50-00:05:51] That way we surely not die.
[00:05:51-00:05:52] I mean, maybe you go up to point eight.
[00:05:52-00:05:55] If you stand in front of a door, yeah.
[00:05:55-00:06:01] I'm gonna stand in front of a door right now.
[00:06:05-00:06:08] To fix this, I'd have to change everything.
[00:06:08-00:06:13] Every room has to be reconstructed one surface at a time.
[00:06:13-00:06:14] Every object out of place has to...
[00:06:14-00:06:17] To be rescaled one by one.
[00:06:17-00:06:24] Coordinates of textures designed for walls this size have to be manually adjusted every single time.
[00:06:24-00:06:26] There's no easy way to do it.
[00:06:26-00:06:29] I'd have to line these up manually.
[00:06:30-00:06:32] For every wall!
[00:06:32-00:06:35] Damn, I'm gonna have to redo everything that I've already...
[00:06:35-00:06:37] It's too playable.
[00:06:37-00:06:39] You started learning by swimming upstream.
[00:06:39-00:06:41] Yeah, I have to go out of my way...
[00:06:41-00:06:44] Your first real hammer map is one where you're intentionally...
[00:06:44-00:06:44] Yeah. You started learning by swimming upstream. I have to go out of my way...
[00:06:44-00:06:47] Trying to do the opposite of how you should make one.
[00:06:47-00:06:47] That's cool.
[00:06:47-00:06:49] That's pretty fucking funny.
[00:06:49-00:06:51] Yeah, you built a little prison for yourself.
[00:06:51-00:06:56] Then I said that actually they say a koi fish turns into a dragon when it swims upstream.
[00:06:57-00:07:04] So at this point I decided I could use some help in streamlining the process of redoing everything.
[00:07:05-00:07:13] If you do have a specific question, there's a thing you're grappling with that you want to convey and you're not totally sure how...
[00:07:13-00:07:14] We could totally do that.
[00:07:14-00:07:17] We could totally jump into a group call with Max at some point and, like...
[00:07:17-00:07:19] That's a stupid idea.
[00:07:20-00:07:22] Sam should stick to podcasting.
[00:07:23-00:07:28] Thankfully, I know this guy, Max, who's actually the lead level designer on El Paso Elsewhere 2.
[00:07:29-00:07:32] Suffice it to say they know what they're doing and can help to get me back on track.
[00:07:32-00:07:35] Hold on, have you seen the icon for an invalid entity?
[00:07:36-00:07:36] No.
[00:07:36-00:07:41] Okay, just go to the class and just type in some bullshit in the class and hit enter.
[00:07:43-00:07:43] Yeah, apply.
[00:07:43-00:07:44] Uh...
[00:07:44-00:07:46] What was that?
[00:07:48-00:07:57] Aside from showing me cool JPEGs, my hope was that Max could just kind of check to make sure nothing that I was doing was stupid.
[00:07:57-00:08:00] You might already know about this and just don't know the term.
[00:08:01-00:08:02] Go back to that, like, door frame.
[00:08:03-00:08:04] Just as an example.
[00:08:04-00:08:05] Oh.
[00:08:05-00:08:08] Say you want that, like, concrete trim to wrap around.
[00:08:08-00:08:08] Okay.
[00:08:09-00:08:11] Say you wanted to wrap it around that door that...
[00:08:11-00:08:12] Okay.
[00:08:12-00:08:13] You wouldn't have to, like, apply it to the door frame.
[00:08:13-00:08:16] You can just grab it separately and then manually match up the UVs.
[00:08:16-00:08:19] You can just grab it there and then right-click on that wood.
[00:08:20-00:08:23] Yeah.
[00:08:25-00:08:25] Wow.
[00:08:26-00:08:27] Wow.
[00:08:27-00:08:28] Fuck me.
[00:08:29-00:08:30] Oh, my God.
[00:08:30-00:08:31] Fuck me.
[00:08:32-00:08:40] I wanted to do this thing where, like, there's a scripted sequence where a zombie spawns behind you after you grab the crowbar, which traps you in this too narrow hallway, which...
[00:08:41-00:08:43] I mean, like, it's hard to describe.
[00:08:43-00:08:45] I mean, I want to make you shit, but you can't.
[00:08:45-00:08:46] You can't strafe.
[00:08:46-00:08:48] It'll suck and not be fun.
[00:08:49-00:08:53] Max held my hand as he taught me how to do math in Hammer.
[00:08:54-00:09:01] But I learned, and now that I'm wise, I could also lock this door till the planks are broken and I can play a scary sound in the hallway.
[00:09:04-00:09:05] That's pretty good.
[00:09:05-00:09:12] So as I built out the level, I wanted to use different types of enemies to put the player in different kinds of annoying dogshit predicaments.
[00:09:12-00:09:14] Designing the bits with zombies was surprisingly easy.
[00:09:15-00:09:15] You just...
[00:09:15-00:09:18] You give the player an annoying maze to navigate and then throw rocks at it.
[00:09:18-00:09:20] At the end, though, I wanted a shootout.
[00:09:20-00:09:29] My vision was of this claustrophobic laundromat, a space that makes you want to strafe around for cover until you try it and, I don't know, cry.
[00:09:29-00:09:33] So I whipped it up, a bit of polish, way too much set dressing, and the level was ready...
[00:09:34-00:09:35] ...for playtesting.
[00:09:35-00:09:37] I gotta make sure it does what it's supposed to do.
[00:09:38-00:09:42] I had no idea how much the playtesting was gonna change things.
[00:09:42-00:09:47] But we got the concrete closet, the narrow hallway, crammed computer room, another hallway, pathetic bathroom, dark room.
[00:09:47-00:09:50] A pathetic bathroom, dark alleyway, and a dingy laundromat.
[00:09:50-00:09:53] First up, playtester number one is DJ Sprite.
[00:09:53-00:09:59] Ex-DJ and FPS gamer so cracked he almost went pro in Overwatch back when that game mattered.
[00:10:03-00:10:11] I'm sorry, my mouse acceleration's fucked up. It's off.
[00:10:12-00:10:14] So I just want you to play through this earnestly.
[00:10:14-00:10:16] I've done a little bit of setup here.
[00:10:17-00:10:19] There's still some stuff to be fixed, but yeah.
[00:10:19-00:10:29] I put the crate there specifically.
[00:10:30-00:10:31] So it would be thrown at your head.
[00:10:31-00:10:32] I thought it was funny.
[00:10:32-00:10:38] You're not gonna believe what I have to say about it so far.
[00:10:40-00:10:42] It's like playing desktop Alyx.
[00:10:42-00:10:51] Alright, so he's tripping up on the geometry, that's good.
[00:10:51-00:10:56] I'm just playing how I play Half-Life.
[00:10:56-00:10:58] Skips the maze that I set up.
[00:10:58-00:11:04] Do you take critique?
[00:11:04-00:11:05] Sure, man.
[00:11:05-00:11:07] Why is that there?
[00:11:07-00:11:10] Well, because that's wherever they put the drops.
[00:11:10-00:11:11] No, that's where you mark...
[00:11:11-00:11:13] The drops aren't right next to it.
[00:11:13-00:11:15] I just didn't want to build another room.
[00:11:15-00:11:16] No, I get it, man, but grow up.
[00:11:16-00:11:29] Damn it, the laundromat.
[00:11:29-00:11:31] Of course, of course it doesn't play right.
[00:11:31-00:11:38] I put an enemy right in front of your face and I give you no reason not to just use the doorframe as a choke point.
[00:11:38-00:11:40] Obviously, this is the right play.
[00:11:40-00:11:45] Also, we skip the computer room maze.
[00:11:46-00:11:47] I'm pissed.
[00:11:47-00:11:56] I think that's it.
[00:11:56-00:11:59] Oh, no, one more.
[00:11:59-00:12:04] What would you do in that situation?
[00:12:04-00:12:05] I don't know.
[00:12:05-00:12:13] So how do we encourage the player to push in?
[00:12:13-00:12:17] One solution could be to keep the powerful weapon inside.
[00:12:17-00:12:19] So, you know, you've got like a pea shooter.
[00:12:19-00:12:20] But, you know.
[00:12:20-00:12:22] Like, you're obviously going to want the more powerful gun.
[00:12:22-00:12:23] I'm going to try it.
[00:12:23-00:12:26] And we're going to see if programmer Sam takes the bait.
[00:12:26-00:12:27] Or my friend Ed.
[00:12:27-00:12:29] We're going to see if Ed does it either.
[00:12:29-00:12:31] Also, I've got to fix that fucking door.
[00:12:31-00:12:38] Don't rush off.
[00:12:38-00:12:39] We'll be right back with...
[00:12:39-00:12:43] Where'd it go?
[00:12:43-00:12:45] Well, it's a nice laptop.
[00:12:45-00:12:47] Some aluminum frames.
[00:12:47-00:12:48] Probably go...
[00:12:48-00:12:49] Whoa, whoa, whoa, whoa!
[00:12:49-00:12:50] What did you do?
[00:12:50-00:12:51] What is that?
[00:12:51-00:12:54] Introducing the ROG Zephyrus Duo.
[00:12:54-00:12:56] They made a laptop, but it's two.
[00:12:56-00:12:57] Two screens.
[00:12:57-00:12:58] Two screens.
[00:12:58-00:12:59] How'd they do that?
[00:12:59-00:13:06] With 2.0, entire, 3K, 120Hz, 2 milliseconds, Nebula, HDR, OLED touch panels.
[00:13:06-00:13:09] The Duo can be deployed in five distinct modes.
[00:13:09-00:13:10] Laptop.
[00:13:10-00:13:11] Which is normal.
[00:13:11-00:13:12] A book.
[00:13:12-00:13:13] Which is long.
[00:13:13-00:13:14] Duo.
[00:13:14-00:13:15] Which is my favorite.
[00:13:15-00:13:16] Sharing.
[00:13:16-00:13:17] Where the device becomes flat.
[00:13:17-00:13:18] And a tent.
[00:13:18-00:13:21] In which two people are blessed with one screen per.
[00:13:21-00:13:27] In addition to its voluptuous displays, the Duo also sports the latest Intel Core Ultra
[00:13:27-00:13:31] 10 processor, up to a 5090 laptop GPU, and ports!
[00:13:31-00:13:35] Ports!
[00:13:35-00:13:36] You can buy this!
[00:13:36-00:13:41] Go to rog.gg slash newellduo, and there you can buy this!
[00:13:41-00:13:44] Oh!
[00:13:44-00:13:46] My name is James Sosich.
[00:13:46-00:13:47] I said hi.
[00:13:47-00:14:23] One thing I can do is this.
[00:14:23-00:14:27] Is extend what should be a simple thing into a conquest.
[00:14:27-00:14:28] Yeah.
[00:14:28-00:14:33] I come back, and the place that I was is the same, but I am changed.
[00:14:33-00:14:34] You know?
[00:14:34-00:14:35] Yeah.
[00:14:35-00:14:36] How many times have you changed?
[00:14:36-00:14:37] There's gotta be, like, an upper limit.
[00:14:37-00:14:38] How many times?
[00:14:38-00:14:39] What the fuck kind of question is that?
[00:14:39-00:14:40] How many?
[00:14:40-00:14:41] What?
[00:14:41-00:14:48] What?
[00:14:48-00:14:49] What?
[00:14:49-00:14:50] You just started.
[00:14:50-00:15:18] No, it's just, it's just, uh, funny being in, playing Half-Life 2 with a wrongly, correctly
[00:15:18-00:15:19] calibrated base.
[00:15:19-00:15:24] You remember I told you about that idea of, like, oh, fucking, uh, you know, uh, levels
[00:15:24-00:15:27] are way too big and it's fucking crazy and whack.
[00:15:27-00:15:28] Levels are way too big?
[00:15:28-00:15:29] Which levels?
[00:15:29-00:15:30] All levels.
[00:15:30-00:15:31] What the fuck?
[00:15:31-00:15:40] I forgot how you play video games.
[00:15:40-00:15:42] What the fuck?
[00:15:42-00:15:46] Um.
[00:15:46-00:15:53] I thought that was the crab talking.
[00:15:53-00:15:59] I'm gonna be completely honest with you.
[00:15:59-00:16:00] Baby.
[00:16:00-00:16:05] Yes.
[00:16:05-00:16:06] Wow!
[00:16:06-00:16:10] Nice!
[00:16:10-00:16:11] Please don't do this.
[00:16:11-00:16:12] Don't do what?
[00:16:12-00:16:13] Carry the baby around.
[00:16:13-00:16:17] I'm trying to actually playtest, and if you keep doing that, it's going to take away from
[00:16:17-00:16:19] the things I'm trying to actually focus on.
[00:16:19-00:16:20] Okay.
[00:16:20-00:16:21] Julian hates player freedom.
[00:16:21-00:16:22] Yeah.
[00:16:22-00:16:23] This is nuts, man.
[00:16:23-00:16:24] My guy fat as hell.
[00:16:24-00:16:27] I feel like fucking Arthur Morgan walking into a bar.
[00:16:27-00:16:35] So is this, uh, this is like Ravenholm, huh?
[00:16:35-00:16:36] No.
[00:16:36-00:16:37] Don't do that.
[00:16:37-00:16:40] You'll actually break it.
[00:16:40-00:16:41] Fuck.
[00:16:41-00:16:42] I have to restart the level.
[00:16:42-00:16:50] I'm sorry.
[00:16:50-00:16:51] No.
[00:16:51-00:16:52] Stop.
[00:16:52-00:16:53] No.
[00:16:53-00:16:54] I do that in, like, every game.
[00:16:54-00:16:56] I'm like, ooh, this looks like something where they forget to put an invisible wall, and
[00:16:56-00:16:57] then I do this.
[00:16:57-00:16:59] Well, guess what I, guess what I forgot to put in, Ed?
[00:16:59-00:17:00] I'm so sorry.
[00:17:00-00:17:01] Hello.
[00:17:01-00:17:02] Oh.
[00:17:02-00:17:06] Asshole.
[00:17:06-00:17:07] Oh.
[00:17:07-00:17:08] Asshole.
[00:17:08-00:17:09] Holy fuck.
[00:17:09-00:17:10] That's loud.
[00:17:10-00:17:11] Better.
[00:17:11-00:17:14] Okay.
[00:17:14-00:17:15] So don't do that.
[00:17:15-00:17:16] Oh.
[00:17:16-00:17:19] Oh, my fucking shit.
[00:17:19-00:17:27] Die, bitch.
[00:17:27-00:17:28] I'm going to do this.
[00:17:28-00:17:29] I'm going to smoke, smoke the area.
[00:17:29-00:17:30] Oh.
[00:17:30-00:17:31] How many do I fucking have?
[00:17:31-00:17:32] Oh, dude.
[00:17:32-00:17:36] Why would he talk like that?
[00:17:36-00:17:37] Is he stupid?
[00:17:37-00:17:38] I like this.
[00:17:38-00:17:46] He was like, for you.
[00:17:46-00:17:47] I'm fucking stupid.
[00:17:47-00:17:48] God damn it, bro.
[00:17:48-00:17:49] Ed's feedback was annoying.
[00:17:49-00:17:50] That really wasn't that bad?
[00:17:50-00:17:54] I think that was a good thing.
[00:17:54-00:17:55] I think that was a good thing.
[00:17:55-00:17:56] I think that was a good thing.
[00:17:56-00:17:59] I think that was a good thing.
[00:17:59-00:18:00] I think that was a good thing.
[00:18:00-00:18:01] I think that was a good thing.
[00:18:01-00:18:02] I think that was a good thing.
[00:18:03-00:18:08] I only had trouble going into that one door.
[00:18:08-00:18:10] And that was for a couple seconds.
[00:18:10-00:18:15] It honestly also demonstrates the thing I was saying, which is there are games that
[00:18:15-00:18:18] do this slash try to do this as best they can.
[00:18:18-00:18:23] And those games are doing it because they're intentionally trying to make you feel claustrophobic.
[00:18:23-00:18:26] And the first thing I thought of was, oh, this immediately feels like I'm playing a
[00:18:26-00:18:27] horror game.
[00:18:27-00:18:29] I thought I was playing PT.
[00:18:29-00:18:31] But it was still very playable.
[00:18:31-00:18:32] At no point was I annoyed.
[00:18:32-00:18:33] Really?
[00:18:33-00:18:38] No, like not even not even the computer room because I because I made that obnoxious on purpose
[00:18:38-00:18:43] I walked around and I killed the crabs. That's actually crazy. I might make it a little worse on purpose
[00:18:43-00:18:44] Yeah, no, I mean go for it
[00:18:44-00:18:51] So his feedback is that the level I specifically designed to be annoying and bad was not annoying or bad
[00:18:51-00:18:55] Playtesting is like playing bingo against yourself and losing
[00:18:55-00:19:00] Aside from that same as sprite. He swears he's played games that do this
[00:19:00-00:19:03] But then when I asked him to actually list one he couldn't do it
[00:19:03-00:19:08] Like it's crazy now having this conversation with you and pulling these up as examples of cramped level design
[00:19:08-00:19:13] And I pull them up and I go, oh, we know these are huge. But when I was playing the game this felt cramped
[00:19:13-00:19:16] Yeah, isn't dude video games are fucking silly. Yeah, they're cool
[00:19:16-00:19:24] Unsurprisingly the guy who makes video games for a living has a bit more to say about the way I made the
[00:19:24-00:19:28] Game god. Yeah, this is annoying. This is annoying to navigate
[00:19:28-00:19:30] I think this being head
[00:19:30-00:19:35] Crabs only it's tough because the nav meshing issue I don't it feels like that
[00:19:35-00:19:41] This is missing a piece because in order for the spaces to be big enough to for the NPCs to navigate
[00:19:41-00:19:44] Oh, they have to be big enough for players to kind of you know what I could do
[00:19:44-00:19:50] I could put a torso in there a zombie with only its upper. Oh, that's a good idea. What if you put a
[00:19:51-00:19:54] Turret or sniper equivalent out there? Well, here's the problem
[00:19:54-00:19:57] here's the big problem with that because I've thought about that, but
[00:19:58-00:20:00] I'm trying to coax the player into the
[00:20:00-00:20:06] This space and then try to make the move around in order to avoid getting pinned down too fast
[00:20:06-00:20:11] The first problem with that is that the enemies tend to be way too aggressive and so you get pinned down anyway
[00:20:11-00:20:18] but the second more tricky problem is that in a space like this the player will want to pull back because of
[00:20:18-00:20:25] Half-life 2's design and the only way I can think to prevent them from doing that is to spawn enemies behind them or to block
[00:20:25-00:20:30] The way behind them either of which is well, what if you drop down?
[00:20:30-00:20:32] Into this space
[00:20:32-00:20:36] Why didn't I think of that fuck?
[00:20:36-00:20:40] All I really have to do is I just have to I have to cut this
[00:20:40-00:20:42] Alleyway and then turn it into
[00:20:43-00:20:44] like a
[00:20:44-00:20:46] like a maintenance hallway
[00:20:46-00:20:51] That has a big hole in the middle that you drop down into and then surprise the first level is a laundromat
[00:20:51-00:20:53] Oh and you know what I can even do. Oh, you know what I can do
[00:20:53-00:20:54] okay
[00:20:54-00:20:59] I'm gonna put the shotgun at the bottom of the hole and I'm going to hide you in like the service closet of the
[00:20:59-00:21:00] laundromat
[00:21:00-00:21:02] Somewhere that's a straight dead end.
[00:21:02-00:21:04] So whenever you come out and there's enemies,
[00:21:04-00:21:06] you aren't instinctively going to go back
[00:21:06-00:21:08] because it's a dead end and you will be cornered.
[00:21:09-00:21:11] So it brings you straight out into that area.
[00:21:11-00:21:12] Okay, that's good.
[00:21:12-00:21:12] That's good.
[00:21:13-00:21:13] Yeah.
[00:21:13-00:21:14] Also, maybe two of these guys.
[00:21:15-00:21:16] Really?
[00:21:16-00:21:17] Because when I ran up here,
[00:21:17-00:21:20] I didn't hit the close quarters issue too much
[00:21:20-00:21:21] with just one guy.
[00:21:23-00:21:25] Because I just beat this and he stays back.
[00:21:26-00:21:27] But with two,
[00:21:27-00:21:29] having to split my attention might make that more annoying.
[00:21:29-00:21:32] The main thing is you want the player to want to move
[00:21:32-00:21:33] and be unable to.
[00:21:34-00:21:35] Other thing I would say,
[00:21:35-00:21:37] no shotgun for the player on this one.
[00:21:37-00:21:38] Really?
[00:21:38-00:21:41] Because the whole point is that
[00:21:41-00:21:43] I'm encouraging you to go close quarters.
[00:21:43-00:21:44] And that's exactly my issue with it
[00:21:44-00:21:46] is that the shotgun is way too good close quarters.
[00:21:46-00:21:48] Not being able to run,
[00:21:48-00:21:49] this makes it easy.
[00:21:49-00:21:51] Oh, you're right.
[00:21:51-00:21:52] I can be agile and jump around
[00:21:52-00:21:53] and keep away from the enemies.
[00:21:54-00:21:56] But because we're in an enclosed space,
[00:21:56-00:21:58] it's like I'm constantly going to be fighting myself.
[00:21:58-00:21:59] Yeah.
[00:21:59-00:21:59] That's true.
[00:21:59-00:22:01] That's based on your feedback.
[00:22:01-00:22:02] I have some stuff to do.
[00:22:03-00:22:03] Yeah.
[00:22:07-00:22:10] Aside from the stuff that you just saw me talk to Sam about,
[00:22:11-00:22:13] I also went back to make the computer room worse
[00:22:13-00:22:14] by adding a bunch of walls
[00:22:14-00:22:16] so you couldn't jump over the tables.
[00:22:16-00:22:17] At Sam's request,
[00:22:17-00:22:18] I added a sniper to keep you moving
[00:22:18-00:22:20] as well as a couple other things
[00:22:20-00:22:20] just to make it feel,
[00:22:21-00:22:22] you know, worse.
[00:22:22-00:22:23] And I fixed the door.
[00:22:23-00:22:25] Oh, and I learned how soundscapes work
[00:22:25-00:22:27] so that whenever you go into a different area,
[00:22:27-00:22:29] the room noise actually changes
[00:22:29-00:22:31] and sounds correct.
[00:22:31-00:22:36] I got really carried away,
[00:22:36-00:22:36] but I don't care.
[00:22:37-00:22:37] It's fun.
[00:22:37-00:22:37] It was fun.
[00:22:38-00:22:39] I had fun.
[00:22:39-00:22:40] I really wanted to be sure
[00:22:40-00:22:41] that all of this had been taken care of
[00:22:41-00:22:43] before I do the next playtest
[00:22:43-00:22:44] with Max,
[00:22:45-00:22:47] the guy who makes levels,
[00:22:47-00:22:48] as his job.
[00:22:49-00:22:50] If I want good advice from him,
[00:22:50-00:22:52] I need to make sure that all of the stuff
[00:22:52-00:22:54] that other people who are less smart than him,
[00:22:54-00:22:56] their problems have been addressed.
[00:22:56-00:22:57] That makes room for him to suggest
[00:22:57-00:23:00] more specific, pointed advice
[00:23:00-00:23:01] that I want.
[00:23:02-00:23:03] So, like, immediately,
[00:23:04-00:23:05] this is just fucking small.
[00:23:06-00:23:06] Yeah.
[00:23:06-00:23:13] I mean, this is like a...
[00:23:13-00:23:16] This is like a Half-Life Alyx hallway.
[00:23:17-00:23:17] Yeah.
[00:23:18-00:23:19] The lighting is nice.
[00:23:19-00:23:20] Thank you.
[00:23:21-00:23:22] Oh, hello.
[00:23:22-00:23:22] Wait.
[00:23:24-00:23:26] Oh, I got got by the thing
[00:23:26-00:23:27] that we set up a couple days ago.
[00:23:28-00:23:30] Oh, there's two of them.
[00:23:30-00:23:32] Oh, yeah, this is pretty...
[00:23:32-00:23:36] These doorways are rough.
[00:23:39-00:23:39] Okay.
[00:23:41-00:23:42] Close the door.
[00:23:42-00:23:47] Oh, my God.
[00:23:47-00:23:49] What's going on with my control?
[00:23:50-00:23:53] Oh, yeah, I put a block there,
[00:23:53-00:23:54] a player clip, so you can't jump.
[00:23:54-00:23:55] Why did you block it?
[00:23:56-00:23:57] Because I want you to do the maze.
[00:23:57-00:23:58] I want you to do it the way that sucks.
[00:23:59-00:24:00] I don't want you skipping my shit.
[00:24:01-00:24:05] I also love...
[00:24:05-00:24:06] There's something subtle here
[00:24:06-00:24:09] about the way Source handles melee detection,
[00:24:09-00:24:11] just, like, latching to nearby objects
[00:24:11-00:24:13] instead of the zombie I'm trying to hit.
[00:24:13-00:24:14] Like, there was a moment in there
[00:24:14-00:24:16] where I was, like, backing around this table,
[00:24:16-00:24:18] and I was just looking down at him,
[00:24:18-00:24:20] and it just, like, beamed over here.
[00:24:21-00:24:24] I'm keeping the stated goal of the level in mind here,
[00:24:24-00:24:25] which is just, like,
[00:24:26-00:24:28] yes, it makes sense that you would have to
[00:24:28-00:24:29] shut the door to get through the hallway
[00:24:29-00:24:31] in, like, a real space,
[00:24:32-00:24:33] but, like, in a video game,
[00:24:33-00:24:34] this fucking sucks.
[00:24:35-00:24:38] Yeah, yeah, yeah.
[00:24:38-00:24:41] Ooh, this is terrible.
[00:24:42-00:24:44] Oh, turn collision back on, please.
[00:24:45-00:24:45] What are you doing?
[00:24:46-00:24:47] Brother, this hallway is so narrow
[00:24:47-00:24:49] that if I turned collision back on,
[00:24:49-00:24:52] you literally would not be able to walk through it.
[00:24:52-00:24:54] You'd have to duck under the pipe to the left.
[00:24:54-00:24:55] Yeah, put, like, a little...
[00:24:55-00:24:57] I love how the way I'm playtesting this,
[00:24:57-00:24:58] I'm just like, okay,
[00:24:58-00:25:00] how can we fuck this up even more?
[00:25:01-00:25:02] All right.
[00:25:02-00:25:03] Ooh, gamer den.
[00:25:04-00:25:06] Can you put, like, the poster of, like, Sakurai up here?
[00:25:06-00:25:08] Do you want to teach me how to import assets
[00:25:08-00:25:09] into a hammer?
[00:25:09-00:25:10] Oh, no.
[00:25:11-00:25:15] People are dying.
[00:25:17-00:25:18] Oh, hello.
[00:25:19-00:25:20] Yeah.
[00:25:20-00:25:21] Okay, so this is pretty bad.
[00:25:22-00:25:30] Um, I love this milk carton.
[00:25:30-00:25:31] On the ground.
[00:25:31-00:25:32] Just terrible.
[00:25:33-00:25:34] Like, I'm trying to, like...
[00:25:34-00:25:35] That's emergent dog shit.
[00:25:35-00:25:36] I didn't even put that there.
[00:25:36-00:25:37] It just fell.
[00:25:37-00:25:38] Put it down there.
[00:25:38-00:25:39] Put it...
[00:25:39-00:25:39] Oh, oh.
[00:25:40-00:25:43] Oh, I can't stand up.
[00:25:43-00:25:45] The first thing you do coming out of this door
[00:25:45-00:25:47] is, like, you want to get more central to the space,
[00:25:47-00:25:48] so you try to strafe left,
[00:25:49-00:25:50] and you don't necessarily look down here.
[00:25:51-00:25:54] So just, like, leaving that fucking carton there
[00:25:54-00:25:56] so that I'm trying to, like, shoot guys and go left,
[00:25:56-00:25:57] and I just get, like, fucking...
[00:25:57-00:25:59] Like, I literally just trip over a carton.
[00:25:59-00:25:59] Hello.
[00:26:00-00:26:01] Does he really...
[00:26:01-00:26:02] Is that how this...
[00:26:02-00:26:10] There were a lot of moments
[00:26:10-00:26:12] wherever the nature of the level
[00:26:12-00:26:15] just got him talking about level design,
[00:26:16-00:26:17] which was the point,
[00:26:18-00:26:19] and that made me smile.
[00:26:20-00:26:22] It is really funny that this...
[00:26:22-00:26:23] Multiple people have commented on this
[00:26:23-00:26:26] feeling like a Half-Life Alyx map,
[00:26:27-00:26:29] because, like, even in a first-person game,
[00:26:29-00:26:32] there's such an abstraction between you and the visuals.
[00:26:32-00:26:35] Like, you're looking at this on a flat screen, right?
[00:26:35-00:26:37] So everything needs to be a little exaggerated.
[00:26:37-00:26:39] But, like, you're making a game for VR,
[00:26:39-00:26:41] so you don't really need to do that,
[00:26:41-00:26:44] because your perspective is about as one-to-one as it can get.
[00:26:44-00:26:46] I think the thing with the milk carton,
[00:26:46-00:26:47] this bench is very nice,
[00:26:47-00:26:50] because, like, you would expect a bench to be here.
[00:26:50-00:26:52] But, like, in a firefight, fuck you.
[00:26:52-00:26:54] There's a lot of nice little touches in here,
[00:26:54-00:26:58] such as how these washing machines are not perfectly even,
[00:26:58-00:27:00] and therefore, like, you can very easily
[00:27:00-00:27:01] just get caught here strafing.
[00:27:02-00:27:03] Uh, love that.
[00:27:03-00:27:05] There's one part of Invisible Walls which is like,
[00:27:05-00:27:07] hey, you'd want to block the player
[00:27:07-00:27:07] from getting somewhere,
[00:27:07-00:27:09] but there's another part of Invisible Geometry
[00:27:09-00:27:09] which is just like,
[00:27:10-00:27:12] I want to make this space nicer to move around in,
[00:27:13-00:27:14] where, like, you will get things like,
[00:27:15-00:27:17] hey, I'm kind of expecting a player
[00:27:17-00:27:20] to be, like, strafing through here.
[00:27:20-00:27:22] So what I'm actually going to do
[00:27:22-00:27:25] is I'm going to make an invisible ramp along this wall
[00:27:25-00:27:28] that smooths out their movement as they're strafing.
[00:27:29-00:27:31] More important for multiplayer games,
[00:27:31-00:27:33] but, like, you still see that in, like,
[00:27:34-00:27:35] single-player games like Half-Life a lot,
[00:27:35-00:27:36] and especially, like,
[00:27:36-00:27:37] older games.
[00:27:38-00:27:39] I asked him for actionable advice
[00:27:39-00:27:42] specifically in regards to the level design,
[00:27:43-00:27:45] and aside from placing the beach bottle on the ground
[00:27:45-00:27:48] and just cramming everything full of props,
[00:27:49-00:27:51] he simply, he handed upon me
[00:27:51-00:27:54] the perfect solution to the problem
[00:27:54-00:27:55] of the laundromat shootout.
[00:27:56-00:27:57] I want the player to be moving around
[00:27:57-00:27:58] and dodging and weaving,
[00:27:58-00:28:00] but the combine always just flood in
[00:28:00-00:28:01] and pin you down.
[00:28:01-00:28:04] You could, like, have, like, rifle guys
[00:28:04-00:28:05] positioned out here,
[00:28:05-00:28:06] and you could just, like,
[00:28:06-00:28:07] clip this off with NPC clips
[00:28:07-00:28:08] so they stay outside
[00:28:08-00:28:10] and you're forced to do, like,
[00:28:10-00:28:11] this weird fucking firefight
[00:28:11-00:28:13] with the SMG.
[00:28:13-00:28:15] Oh, this is so smarted.
[00:28:15-00:28:18] They gave smarted advice that I took.
[00:28:19-00:28:20] With the invisible wall implemented,
[00:28:20-00:28:22] the type that only affects NPCs
[00:28:22-00:28:24] but that players can just walk straight through,
[00:28:24-00:28:26] suddenly that final shootout started to make
[00:28:26-00:28:28] a lot more sense.
[00:28:28-00:28:29] While I was in there,
[00:28:29-00:28:32] I also added a lot of props
[00:28:32-00:28:33] for you to trip on,
[00:28:33-00:28:34] reintroduced a bit of collision
[00:28:34-00:28:36] to make the tunnel,
[00:28:36-00:28:38] and, once it was all done,
[00:28:39-00:28:41] I remade the entire map,
[00:28:42-00:28:43] but bigly.
[00:28:44-00:28:46] It was annoying and tedious,
[00:28:46-00:28:48] but oh my god,
[00:28:48-00:28:49] it was so much nicer
[00:28:49-00:28:51] than making the small version.
[00:28:52-00:28:54] Like, video game maps aren't just huge
[00:28:54-00:28:56] because it makes navigation easier
[00:28:56-00:28:57] for players and NPCs.
[00:28:57-00:28:59] I, as a mapper,
[00:28:59-00:29:01] I felt like I actually had room to work
[00:29:01-00:29:02] for the first time
[00:29:02-00:29:05] now that there was so much more space everywhere.
[00:29:05-00:29:06] I didn't just say,
[00:29:06-00:29:08] just go in and make things proportionally larger.
[00:29:08-00:29:10] I adjusted rooms and halls
[00:29:10-00:29:13] based on what I felt made them feel nice to navigate,
[00:29:14-00:29:16] whether that be the 50% increase
[00:29:16-00:29:18] or 150%.
[00:29:18-00:29:21] Almost every intentionally hostile decision I made
[00:29:21-00:29:23] was declawed and smoothed out.
[00:29:23-00:29:26] And the result felt wrong.
[00:29:27-00:29:28] It felt empty,
[00:29:28-00:29:30] and not just because there were so many less props.
[00:29:30-00:29:32] All this negative space,
[00:29:32-00:29:33] it's par for the course in video games,
[00:29:33-00:29:35] but not when you've been staring at a version
[00:29:35-00:29:37] more than twice as densely populated
[00:29:37-00:29:39] for several hours.
[00:29:39-00:29:41] My concern now is that, honestly,
[00:29:41-00:29:42] like, if I got a playtester
[00:29:42-00:29:44] to try this version first, blind,
[00:29:44-00:29:46] they were gonna think it felt too big.
[00:29:46-00:29:48] Like, maybe I overcorrected here.
[00:29:48-00:29:48] I don't know.
[00:29:49-00:29:50] The only way to know for sure
[00:29:50-00:29:52] is by testing it on somebody
[00:29:52-00:29:54] who doesn't have any idea
[00:29:54-00:29:55] what I'm trying to accomplish here.
[00:29:56-00:29:56] A blind test.
[00:29:57-00:29:58] But who do I have
[00:29:58-00:30:01] who have not already shown this
[00:30:01-00:30:03] and talked to them about when?
[00:30:03-00:30:03] And then I remembered.
[00:30:05-00:30:07] I don't talk to Leon very much.
[00:30:08-00:30:09] So I had him play both,
[00:30:10-00:30:11] starting with the bigger, normal one.
[00:30:12-00:30:13] Leon is a smart man.
[00:30:13-00:30:15] He baldly makes some of the best
[00:30:15-00:30:16] game analysis videos on YouTube.
[00:30:20-00:30:21] You ever think about how we can, like,
[00:30:21-00:30:24] climb big rocks and be like,
[00:30:24-00:30:26] yeah, but if I fall, I go to the doctor.
[00:30:26-00:30:28] Whereas a bear, they look at a big rock
[00:30:28-00:30:30] and they go, well, if I fall, I die.
[00:30:33-00:30:33] It's true.
[00:30:34-00:30:36] I'm not gonna tell you
[00:30:36-00:30:37] what I'm trying to accomplish
[00:30:37-00:30:38] right off the bat.
[00:30:38-00:30:40] I'm guinea pig testing here.
[00:30:40-00:30:41] So I just want to,
[00:30:41-00:30:41] you know,
[00:30:41-00:30:43] get a live Leon reaction
[00:30:43-00:30:44] and then I'll tell you
[00:30:44-00:30:45] what I'm doing afterwards.
[00:30:47-00:30:48] It's not going to be anything.
[00:30:48-00:30:50] It's not going to be anything scary, OK?
[00:30:51-00:30:53] I'm ready for you to jump scare me.
[00:30:54-00:30:56] Oh, yeah, that's definitely not.
[00:30:56-00:30:57] Yeah, it's definitely not a horror map.
[00:30:58-00:30:59] No, it's a half-life map.
[00:31:00-00:31:01] Oh, my Jesus Christ.
[00:31:02-00:31:03] Do I have a flashlight?
[00:31:03-00:31:04] I do.
[00:31:07-00:31:08] Oh, OK.
[00:31:09-00:31:10] Forgot that it's not the grabby.
[00:31:10-00:31:11] Yeah.
[00:31:12-00:31:16] Give me.
[00:31:16-00:31:19] Whoa.
[00:31:19-00:31:23] In the silhouette of a feeble creature.
[00:31:24-00:31:28] I hate how slow these fucking things are.
[00:31:29-00:31:30] I like the one in Alex
[00:31:30-00:31:31] where they have like a bug.
[00:31:31-00:31:32] Yeah, yeah.
[00:31:33-00:31:38] Oh, shit.
[00:31:38-00:31:39] That's a shotgun.
[00:31:39-00:31:40] I shouldn't have let him get close.
[00:31:46-00:31:47] Oh, my Jesus.
[00:31:48-00:31:49] I'm leaving.
[00:31:52-00:31:54] Did he drop the shotgun?
[00:31:54-00:31:55] Is that how half-life works?
[00:31:55-00:31:57] I made sure that he didn't
[00:31:57-00:31:58] in the hammer editor.
[00:31:59-00:32:00] Motherfucker.
[00:32:02-00:32:03] Fucking, I peeked my head out.
[00:32:03-00:32:04] He's instantly.
[00:32:04-00:32:07] He's instantly shooting.
[00:32:08-00:32:09] He should look like Counter-Strike.
[00:32:10-00:32:11] What's my alt fire?
[00:32:14-00:32:14] Oh, my God.
[00:32:15-00:32:17] OK, you can choose to play again,
[00:32:17-00:32:18] but you don't have to.
[00:32:18-00:32:19] No, no, no.
[00:32:19-00:32:20] I'll play it again.
[00:32:20-00:32:20] I'll play it again.
[00:32:20-00:32:20] OK.
[00:32:22-00:32:26] So I got the things there.
[00:32:29-00:32:30] Oh, fuck.
[00:32:30-00:32:39] I did it.
[00:32:39-00:32:41] Hey.
[00:32:41-00:32:42] All right.
[00:32:43-00:32:45] So you're not actually done yet.
[00:32:45-00:32:46] OK.
[00:32:46-00:32:47] No graph out.
[00:32:47-00:32:52] This is part two of two of my studies.
[00:32:52-00:32:54] This is fair.
[00:32:54-00:32:58] OK, so now they're lower down.
[00:32:59-00:33:00] Why am I tall?
[00:33:05-00:33:07] Where's the where's the guy?
[00:33:07-00:33:08] That's a good question.
[00:33:08-00:33:09] He should be there.
[00:33:10-00:33:12] Oh, he's crawling around down here.
[00:33:13-00:33:13] Fucking.
[00:33:16-00:33:17] Graffiti.
[00:33:18-00:33:22] Why is everything?
[00:33:23-00:33:24] Why am I ever so slightly taller
[00:33:24-00:33:26] in this version or everything else
[00:33:26-00:33:27] is ever so slightly smaller?
[00:33:28-00:33:34] Everything's a little bit thinner
[00:33:34-00:33:35] and stranger.
[00:33:36-00:33:39] I've been given the grenades here.
[00:33:39-00:33:41] OK, I gave you the grenades there
[00:33:41-00:33:42] all the time.
[00:33:42-00:33:42] You didn't notice.
[00:33:43-00:33:43] Oh, OK.
[00:33:47-00:33:49] This one's so much tighter.
[00:33:49-00:33:54] Oh, I was trying to bank off that.
[00:33:54-00:33:55] Yeah.
[00:34:07-00:34:15] Oh, shit.
[00:34:19-00:34:20] I still did it.
[00:34:21-00:34:22] All right.
[00:34:23-00:34:25] What are your initial thoughts
[00:34:25-00:34:26] before I tell you what's going on?
[00:34:28-00:34:32] I think that I am just a slightly bigger version
[00:34:32-00:34:34] of myself in the last one.
[00:34:36-00:34:36] Interesting.
[00:34:37-00:34:39] Because, well, I don't even know.
[00:34:39-00:34:41] All like certain parts of the map
[00:34:41-00:34:42] have been scaled down.
[00:34:43-00:34:45] I'm finding it really hard
[00:34:45-00:34:46] to walk through these little bits.
[00:34:48-00:34:50] Like the walkways are tighter.
[00:34:50-00:34:53] The level is more claustrophobic
[00:34:53-00:34:53] ever so slightly.
[00:34:54-00:34:56] The difference between the first
[00:34:56-00:34:57] and second version of this map
[00:34:57-00:34:59] is that the first one
[00:34:59-00:35:02] was designed to play
[00:35:02-00:35:03] like a video game.
[00:35:04-00:35:05] And the second one,
[00:35:05-00:35:06] the one you're playing now,
[00:35:07-00:35:08] was built to scale.
[00:35:09-00:35:12] So everything is designed to be
[00:35:13-00:35:15] about what it would actually look like
[00:35:15-00:35:16] in the real world.
[00:35:16-00:35:19] Like, I did notice it like here,
[00:35:19-00:35:20] especially as like when you come out
[00:35:20-00:35:22] the side, it's like, oh, my God.
[00:35:22-00:35:24] Like, yeah, like just like this
[00:35:24-00:35:26] little things getting in the way.
[00:35:26-00:35:26] Yeah, yeah.
[00:35:26-00:35:29] I was worried that it was so fucking huge
[00:35:29-00:35:30] that you were going to think
[00:35:30-00:35:32] it was weirdly spacey.
[00:35:32-00:35:34] Like, it's because I'm so used
[00:35:34-00:35:35] to looking at this cramped,
[00:35:35-00:35:38] realistic version that to my eyes,
[00:35:38-00:35:39] it looks fucking ridiculous.
[00:35:40-00:35:41] You know what I think helped
[00:35:41-00:35:43] with that feeling of like,
[00:35:43-00:35:45] oh, this is really claustrophobic
[00:35:45-00:35:46] in that like,
[00:35:47-00:35:48] oh, my God, this does.
[00:35:49-00:35:51] Now that I'm drawn to it,
[00:35:51-00:35:52] I'm like, whoa, this is a massive corridor.
[00:35:53-00:35:54] Also, no, look at even the door.
[00:35:56-00:35:56] Look at the...
[00:35:56-00:35:58] Oh, my God, it's so tall.
[00:35:58-00:36:00] Yeah, and it's wide.
[00:36:00-00:36:01] I passed through it like...
[00:36:01-00:36:04] This map feels like it's designed
[00:36:04-00:36:05] for this kind of speed
[00:36:05-00:36:07] and this kind of speed.
[00:36:08-00:36:08] Yeah.
[00:36:08-00:36:09] Whereas the other map, it's like, okay,
[00:36:10-00:36:12] I can move around in this kind of speed,
[00:36:12-00:36:15] but the moment I'm starting to go like up here,
[00:36:15-00:36:17] it's like, what the fuck is going on?
[00:36:17-00:36:18] Like, I couldn't move.
[00:36:19-00:36:21] I was going to say it created
[00:36:21-00:36:24] like a sense of restriction,
[00:36:24-00:36:26] not by like what, like...
[00:36:26-00:36:28] Not by the fact that I couldn't
[00:36:28-00:36:29] physically go fast.
[00:36:29-00:36:30] It's just that it's like,
[00:36:30-00:36:31] it's just uncomfortable
[00:36:31-00:36:31] to be able to move.
[00:36:31-00:36:32] to be able to be that fast
[00:36:32-00:36:34] in that kind of space.
[00:36:34-00:36:35] This is a massive bathroom.
[00:36:36-00:36:38] I looked at you go in here
[00:36:38-00:36:39] and I was like,
[00:36:39-00:36:40] he's going to say something.
[00:36:40-00:36:41] He has to say something about this.
[00:36:42-00:36:44] No, but now that I'm here,
[00:36:44-00:36:46] I'm like, why is it so big
[00:36:46-00:36:47] for this little sink?
[00:36:48-00:36:50] This little mirror and tiny toilet?
[00:36:50-00:36:52] Because if you cast your mind
[00:36:52-00:36:53] back to the other version,
[00:36:53-00:36:54] it's really uncomfortable
[00:36:54-00:36:55] to go through there.
[00:36:55-00:36:56] Yeah, yeah.
[00:36:56-00:36:58] Well, the other one's just a toilet.
[00:36:58-00:36:59] Like, the other one's,
[00:36:59-00:36:59] that's a bathroom.
[00:36:59-00:37:00] It's a bathroom.
[00:37:00-00:37:01] This one's a bathroom
[00:37:01-00:37:01] for fucking.
[00:37:01-00:37:02] Andre the Giant.
[00:37:04-00:37:04] Jesus Christ.
[00:37:05-00:37:06] Look how much space there is.
[00:37:06-00:37:06] What?
[00:37:06-00:37:10] Look how much space there is.
[00:37:10-00:37:11] I can.
[00:37:12-00:37:12] Right?
[00:37:12-00:37:12] Like, what?
[00:37:13-00:37:14] I can't believe.
[00:37:14-00:37:16] While I was making this video,
[00:37:16-00:37:17] I came across these screenshots
[00:37:17-00:37:20] from a dev talk in 2002
[00:37:20-00:37:21] given by Remedy.
[00:37:22-00:37:23] And it felt like God
[00:37:23-00:37:24] handing me material.
[00:37:25-00:37:26] I was like, oh my God.
[00:37:26-00:37:26] Oh my God.
[00:37:27-00:37:27] What the fuck?
[00:37:28-00:37:28] Wait, is,
[00:37:29-00:37:30] is the one on the left,
[00:37:31-00:37:31] that's like,
[00:37:31-00:37:32] would it be like
[00:37:32-00:37:33] if it was accurate
[00:37:33-00:37:34] to the real world?
[00:37:34-00:37:35] Yes.
[00:37:35-00:37:35] For the purpose
[00:37:35-00:37:36] of the demonstration,
[00:37:36-00:37:37] that's what they were going for.
[00:37:38-00:37:38] And then the second one
[00:37:38-00:37:39] is that's the game.
[00:37:39-00:37:40] Like, I could fucking,
[00:37:40-00:37:41] I could fit everything in here.
[00:37:41-00:37:43] I could park three cars
[00:37:43-00:37:44] in his living room.
[00:37:44-00:37:45] The man on the right
[00:37:45-00:37:47] is 14.
[00:37:48-00:37:48] Yeah.
[00:37:49-00:37:49] So that's it.
[00:37:49-00:37:50] I've done it.
[00:37:50-00:37:51] I have successfully made a map
[00:37:51-00:37:53] that proves my point.
[00:37:53-00:37:54] But I,
[00:37:54-00:37:56] I want to go back
[00:37:56-00:37:57] and keep working on it.
[00:37:58-00:37:59] Sam had to talk me down
[00:37:59-00:38:00] from opening it back up
[00:38:00-00:38:01] and tweaking it even more.
[00:38:01-00:38:01] I am,
[00:38:01-00:38:03] I feel compelled.
[00:38:03-00:38:04] to continue to play with it.
[00:38:05-00:38:05] It's fun.
[00:38:06-00:38:07] I was correct online.
[00:38:08-00:38:09] But more importantly,
[00:38:09-00:38:10] I met someone
[00:38:10-00:38:12] who was smart online.
[00:38:13-00:38:16] Who I will never talk to again.
[00:38:16-00:38:18] As Shigeru Miyamoto once said,
[00:38:18-00:38:20] great games aren't released.
[00:38:21-00:38:21] They escape.
[00:38:22-00:38:25] And so I escaped my map
[00:38:25-00:38:27] onto the Steam Workshop.
[00:38:27-00:38:28] This feeling of
[00:38:28-00:38:29] wrapping everything up,
[00:38:29-00:38:31] this sort of definitive closure,
[00:38:31-00:38:32] it used to be something
[00:38:32-00:38:33] I only really got
[00:38:33-00:38:34] from releasing videos.
[00:38:34-00:38:36] But it's really nice
[00:38:36-00:38:37] to be able to get that feeling
[00:38:37-00:38:38] from something else now, too.
[00:38:39-00:38:39] I,
[00:38:39-00:38:41] I genuinely,
[00:38:41-00:38:42] I cannot wait
[00:38:42-00:38:44] to see how you all react
[00:38:44-00:38:44] to this,
[00:38:44-00:38:46] this new thing of mine.
[00:38:46-00:38:46] This,
[00:38:46-00:38:47] this one
[00:38:47-00:38:49] final playtest.
