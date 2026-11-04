---
title: "GDC20|字幕|容错机制与洞察玩家意图的响应式游戏设计——Forgiveness Mechanics Reading Minds for Respo"
platform: bilibili
bvid: BV1bj9gYnEvY
author: 庸才的朽木
author_uid: 49665055
pubdate: 2025-02-28 15:08:25
duration_sec: 1727
view: 473
like: 19
coin: 3
favorite: 62
reply: 1
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV1bj9gYnEvY
subtitle_source: asr_Qwen3-ASR-1.7B
asr_model: Qwen3-ASR-1.7B
asr_elapsed_sec: 2040.2
transcript_chars: 7937
crawl_time: 2026-05-26 08:35:20
---

# GDC20|字幕|容错机制与洞察玩家意图的响应式游戏设计——Forgiveness Mechanics Reading Minds for Respo

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2025-02-28 15:08:25
- **时长**: 28分47秒
- **播放**: 473 | 赞: 19 | 币: 3 | 藏: 62
- **链接**: https://www.bilibili.com/video/BV1bj9gYnEvY

## 视频描述

原视频：https://www.youtube.com/watch?v=HCnZhs-92j0
（2020年3月19日）在这 2020 年 GDC 虚拟演讲中，Butterscotch Shenanigans 的 Seth Coster 揭开了宽恕机制的神秘面纱；这些游戏系统允许玩家在输入上“出错”，但仍能获得他们想要的结果。

## 完整文稿

> 来源: asr_Qwen3-ASR-1.7B

控制是不一致的，这些词可以是适当的，对于任何游戏。如果不一致的控制意味着无聊、挫败、玩家的困惑和挫败感，但是一致的控制，它只是意味着游戏做了玩家想要做的。如何才能实现？如何才能做到？如何才能Visualization really illustrates that pop effect from the hitbox pinching in a much more pronounced way. As you can see here, we jump around across, fall for a moment, and pops up on the next tile, and that little bit of falling is forgiving. Hitbox pinching can also be used to let the player easily jump up and out of tight spaces. So here in this GIF, we're representing collision checks with these little green dots. And as you can see, that when the players jumping upward, we pinch the hitbox down to almost nothing. I think maybe the player is about two pixels wide while jumping upward. But that squeeze generally allows the player to sometimes partially go inside of walls, and so we have to make sure that we adjust for that and adjust the jump by those little yellow dots in the center of the player's body when they jump around corners. It's like that. And you may also notice that when the players falling, we don't pinch the hitbox at all, so the player has a wide base on which they can much more easily land on narrow ledges. Hitbox pinching is a super useful tool that allows you to add a lot less precision of the player and allows them to very easily squeeze through areas of the game that would otherwise require a frustrating amount of fine motors. So when it comes to hitboxes, there are a couple other much simpler things you can do to get a lot of mileage. For example, we can play around with hitbox sizes and shapes as simple but effective tools to make the game more forgiving. For starters, when it comes to things that are bad for the player to touch, we can tuck the hitbox in at the edges, making the hitbox smaller than the visual area of the object, so it's harder for the player to hurt themselves. You can see in this GIF how these spikes on Level Head have very forgiving hitboxes, which allows the player to easily squeeze through a gap like this. So I like the thing of this as those times in movies where someone's flying a spaceship, and there's always a scene where two big doors are closing, and they have to squeeze the ship through the gap. So basically, you want to create that feeling, and that's easy to do just by tucking in those hitboxes. So you may also notice that these spikes, despite obviously being square, have circular hitboxes. By shaving off the corners, we make it so that the player can kind of pass their toe through the corner of the spike, and that's still fine. It's a close call, which feels cool and makes the player feel like they're better at the game, and it's just a lot more exciting that way. On the flip side, for anything positive, we want the hitbox to be as easy to hit as possible. So for starters, we make it a square, so that it has those corners to catch, and we also extend the hitbox beyond the visual size of the item. So in this GIF, we can see how these hitboxes of gems in Level Head extend far beyond the actual visual size. And when the game is slowed down at half speed like this, and with the hitboxes visible, the forgiveness mechanic is pretty obvious. But at full speed, without the hitbox is visible, it feels totally natural, and the player is not going to notice or be upset that these good things are being handled to them with ease. But sometimes having a big hitbox isn't enough. If you want the player to really get that good stuff, you can add magnetism to positive items. In Level Head, we only apply this to the gems, but in your game, you could technically do this to whatever you want. The rule we use is once the player has gotten pretty close to the gem, we have the gem enter magnet mode, and it's then just going to chase the player until it gets picked up. This effect is especially pronounced when the player is moving faster, like this GIF, when they're falling, or maybe if they're being shot out of a cannon. So we use this kind of magnetism to make it so the player doesn't have to backtrack and physically touch every gem just to collect it. If they just kind of like graze past one, just got close enough, then we just call it good enough, and we let the player have the win. And plus, I think it just feels really cool to go really fast and just be chased by bunch of gems they're trying to catch. The last forgiveness mechanic I want to go over is the concept of the benefit of the doubt decision tree. This is what we use when a player could have multiple possible outcomes when interacting with something, with varying degrees of goodness or badness. When one of these events occurs, we walk through a series of questions that always leads to the most favorable outcome to the player. In Level Head, enemies are the best example of this. So when you hit an enemy, there are some scenarios where you defeat the enemy, and there are some scenarios where the enemy defeats you, and the outcome totally depends on how you hit the enemy. So we can use this scrub enemy from Level Head as an example. When you collide with this scrub, we first check the green rectangular area. This is the area that is favorable to you to determine whether you're going to deal damage to the scrub by jumping on its head. So notice that this area is larger than the visual size of the scrub, and it also has corners, making it easier to hit. And as you can see in this GIF, the player doesn't have to directly land on the visual area of the scrub for this to count as a successful hit. He just needs to hit somewhere in that green rectangle, and just like with the gems, the positive hitbox extends far beyond the visual area. As before, this effect is more pronounced when the game is slowed down like this, but at full speed, this happens fast enough that you don't really, you don't really notice it that much. But when you've collided with the enemy and failed to meet that first decision criteria for dealing damage to the green rectangle, only then do we evaluate if you're going to be harmed. In that case, we use a second smaller circular collision mask represented by this red circle to determine whether you're harmed. So it's possible that you would collide with the green rectangle, fail to damage the enemy, because maybe, I don't know, maybe you're traveling up or something. But maybe you're still not inside the circle, so you don't take any you don't you're not harmed, and you live to see another day. And by using this tucked-in circle, we allow you to kind of graze past and avoid anything bad happening to you. So in all cases, our goal here is to give the player as many opportunities to win and feel like they're really good at the game, and only when they totally run out of possible ways out, that's when the player loses. All right, so that's about the time that I have. I hope you found this useful and interesting. Some of these concepts are a lot more complicated to implement than others, and not all of them will apply to all games. So how you bring these forgiveness mechanics into your game may end up looking a lot different than what I've shown here today. But that's okay, because the most important thing here is not in the specifics, it's in the broad philosophy that your players are people, and people do all kinds of wacky things. They push the wrong buttons, they squeeze the controller, they panic, they do a lot of things that they don't even know about or that they can't even explain. In other words, they're not perfect, but we shouldn't expect them to be perfect. As designers, it's our job to meet our players where they are and give them the best possible experience. And to do that, we have to forgive their inconsistencies and build rules into our games that accommodate them, and only then will you have a truly responsive game. Thank you for listening. If you have any questions or comments about this talk, feel free to shoot me an email at Seth at beastcatch. Net. Good luck out there.

## 热门评论

- **庸才的朽木** (赞0): 中配版本：https://www.bilibili.com/video/BV1bQAnezECJ?vd_source=d483cf66af2a5df6ddc75b2d8e4a99e4&amp;spm_id_from=333.788.videopod.sections