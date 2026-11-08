---
title: "GDC26|原声|移动开发最佳实践：“三角洲行动”移动端——Mobile Development Best Practices, 'Delta Force' M"
platform: bilibili
bvid: BV1i7p76PEjY
author: 庸才的朽木
author_uid: 49665055
pubdate: 2026-10-11 13:11:40
duration_sec: 3486
view: 512
like: 11
coin: 2
favorite: 12
reply: 1
danmaku: 0
share: 4
url: https://www.bilibili.com/video/BV1i7p76PEjY
subtitle_source: asr_faster-whisper-large-v3
asr_model: faster-whisper-large-v3
transcript_chars: 61377
crawl_time: 2026-11-08 21:20:02


# GDC26|原声|移动开发最佳实践：“三角洲行动”移动端——Mobile Development Best Practices, 'Delta Force' M

## 视频信息

- **UP主**: 庸才的朽木
- **发布时间**: 2026-10-11 13:11:40
- **时长**: 58分6秒
- **播放**: 512 | 赞: 11 | 币: 2 | 藏: 12
- **链接**: https://www.bilibili.com/video/BV1i7p76PEjY

## 视频描述

原视频：https://gdcvault.com/play/1036052/Mobile-Development-Best-Practices-Delta
发言人：Guihong Xu, Walker Wang, Jane Tian
概述：随着 PC 端和移动端开发的日益融合，如何在保持移动端高质量视觉效果的同时，有效管理复杂的 PC 端资源，成为一个亟需解决的难题。本次演讲将介绍 Delta F

## 完整文稿

> 来源: asr_faster-whisper-large-v3

# 转录 | BV1i7p76PEjY
# 语言=en 时长=00:58:05 模型=large-v3

[00:00:02-00:00:05] Welcome, everybody, to today's talk.
[00:00:05-00:00:08] In this session, we will introduce the mobile development
[00:00:08-00:00:12] best practices of Delta Force Mobile.
[00:00:12-00:00:13] My name is Jane.
[00:00:13-00:00:17] I'm the global lead of Qualcomm Developer Technology.
[00:00:17-00:00:22] And here, we have the honor to have the Guihong Xu,
[00:00:22-00:00:27] the lead software engineer from Tencent TV Studio.
[00:00:27-00:00:28] OK.
[00:00:28-00:00:32] And then let's also welcome Walker, the senior software
[00:00:32-00:00:37] engineer from Tencent TV Studio.
[00:00:37-00:00:42] OK, so Qualcomm Snapdragon Studio and Delta Force
[00:00:42-00:00:45] has strong longtime collaboration.
[00:00:45-00:00:50] So let me introduce a bit of background for this talk.
[00:00:50-00:00:52] As we all know, unified development
[00:00:52-00:00:56] across PC and mobile has been really challenging.
[00:00:56-00:00:58] It's become a mainstream trend.
[00:00:58-00:01:01] So it's been quite challenging to balance
[00:01:01-00:01:04] the high quality visual, stable frame rate,
[00:01:04-00:01:08] and low power consumption on a mobile device.
[00:01:08-00:01:12] Developers want to actually inherit the advanced assets
[00:01:12-00:01:16] and the complexity of PC games.
[00:01:16-00:01:19] So that's why we're having this talk.
[00:01:19-00:01:22] In this talk, we will provide some best practices and use
[00:01:22-00:01:26] case on collaboration between Qualcomm and Delta Force.
[00:01:26-00:01:28] We will share some in-depth knowledge
[00:01:28-00:01:33] on how mobile performance and power can optimize for cross
[00:01:33-00:01:34] platform development.
[00:01:34-00:01:40] We will also introduce how you can leverage the Snapdragon 8
[00:01:40-00:01:42] Elite Gen 5 platform.
[00:01:42-00:01:47] And we can go over the third generation of Orion CPU,
[00:01:47-00:01:53] Adreno GPUs, new 18 megabyte independent high speed memory.
[00:01:53-00:01:56] And together, Qualcomm and Delta Force,
[00:01:56-00:02:01] we will work together on optimize the complex textures
[00:02:01-00:02:03] and everything on this battle scenes.
[00:02:03-00:02:08] So we want to achieve higher bandwidth efficiency
[00:02:08-00:02:10] and stable frame rate.
[00:02:10-00:02:12] And on top of that, I want to mention
[00:02:12-00:02:16] that we are able to maintain a top visual quality as well
[00:02:16-00:02:20] as effectively control the power usage and device temperature.
[00:02:20-00:02:24] So that's a key for our mobile development.
[00:02:24-00:02:26] OK, so without further ado, let's
[00:02:26-00:02:34] welcome the Delta Force engineers to the stage.
[00:02:34-00:02:35] Hi, everyone.
[00:02:35-00:02:37] My name is Guihong.
[00:02:37-00:02:38] We are both from the Delta Force team.
[00:02:38-00:02:38] OK.
[00:02:38-00:02:40] Delta Force team, Team Studio.
[00:02:40-00:02:43] I will start by giving you a quick overview of what
[00:02:43-00:02:45] Delta Force is all about.
[00:02:45-00:02:48] Delta Force is a cross-platform FPS game
[00:02:48-00:02:51] and will offer multiple co-gameplay modes,
[00:02:51-00:02:55] including large scales combined on the battle course, land,
[00:02:55-00:03:00] seat, air, with multi-vehicle coordination,
[00:03:00-00:03:03] as well as a three-player tele-course ejection
[00:03:03-00:03:08] mode with course, search, strike, and chat, as you can see.
[00:03:08-00:03:14] The gameplay is rich, and the things are very complex.
[00:03:14-00:03:19] Now that you know how to play the game, let's go over it.
[00:03:19-00:03:22] There are a lot of complex systems behind the scenes
[00:03:22-00:03:24] that make all of this possible.
[00:03:24-00:03:27] Engine foundations, providing rendering systems
[00:03:27-00:03:29] and low-level capability support,
[00:03:29-00:03:34] access production, pipeline, all complete creations,
[00:03:34-00:03:38] workflows, and tooltrain systems, gameplay systems,
[00:03:38-00:03:38] implementations.
[00:03:38-00:03:43] Our cross-platforms call gameplay logics and outdoor game
[00:03:43-00:03:46] systems, including webcams, customizations,
[00:03:46-00:03:50] social interactions, and benchmarking modules.
[00:03:50-00:03:53] And finally, performance optimizations
[00:03:53-00:03:56] of both mobile and PC platform.
[00:03:56-00:03:58] Now, given the time limit today, I
[00:03:58-00:04:03] will focus on what we consider the most practical part, how
[00:04:03-00:04:07] we achieve the balance between achieving performance
[00:04:07-00:04:08] optimizations.
[00:04:08-00:04:10] This is to make it possible for us to integrate
[00:04:10-00:04:13] and realize the virtual qualities of mobile.
[00:04:13-00:04:16] Delta 4 uses a unified development approach
[00:04:16-00:04:20] for most both PC and mobile platforms.
[00:04:20-00:04:24] That's making it possible for us to develop things
[00:04:24-00:04:30] for both desktop and mobile, or within a single environment.
[00:04:30-00:04:33] SD has created a core challenge for us.
[00:04:33-00:04:37] How do we perceive the PC quality versions on mobile?
[00:04:37-00:04:40] performance on mobile device.
[00:04:40-00:04:43] These are the key challenges we face on mobiles.
[00:04:43-00:04:47] First, game sync performance and memory optimizations.
[00:04:47-00:04:49] Second, mobiles rendering in broad
[00:04:49-00:04:51] and GPU performance optimization.
[00:04:53-00:04:56] Let's, I will cover the first part
[00:04:56-00:04:58] and then I will hand it to Walker.
[00:04:58-00:05:01] Let's start the game sync performance
[00:05:01-00:05:03] and memory optimization.
[00:05:04-00:05:07] Here's one of our typical game syncs, Tide.
[00:05:07-00:05:10] You can get a sense of visual qualities
[00:05:10-00:05:12] and comparison with during wait.
[00:05:12-00:05:16] The S quality close the entire sync is quick height
[00:05:16-00:05:18] and the object placement density
[00:05:18-00:05:21] is also very significant sense.
[00:05:21-00:05:22] More thoughts.
[00:05:22-00:05:24] The density is horizontal.
[00:05:24-00:05:28] We also have substantial vertical assess densities.
[00:05:28-00:05:33] What's more, the method contains very rich in those charge.
[00:05:33-00:05:36] We can just migrate the syncs from PC to mobile.
[00:05:37-00:05:41] Let's look at the original level assessed
[00:05:41-00:05:42] by our architimp.
[00:05:42-00:05:46] We have a large architimp so we didn't impose many limits
[00:05:46-00:05:48] at the original level stage.
[00:05:48-00:05:51] RTS quickly creates their own sub-levels
[00:05:51-00:05:52] according to their need.
[00:05:52-00:05:55] We have only simple functional
[00:05:55-00:05:59] from the engineering side so the divided sub-levels
[00:05:59-00:06:02] and add quick segment to analyze.
[00:06:02-00:06:04] Also, for materials and textures reuse.
[00:06:04-00:06:07] A single static commercial in our public light
[00:06:07-00:06:09] can contain many sessions.
[00:06:09-00:06:11] That's Unreal's original approach,
[00:06:11-00:06:15] but it has a significant sense in place on performance.
[00:06:15-00:06:20] In the tidal side, which is only 300 by 300 meters,
[00:06:21-00:06:24] we have to deal with an extremely high number
[00:06:24-00:06:29] of actors, components, and overall asset.
[00:06:29-00:06:33] There are two main approach to handling such a bigger world
[00:06:33-00:06:37] in our industry, level streaming and culling.
[00:06:37-00:06:40] Level streaming usually means streaming based on distance,
[00:06:40-00:06:45] and culling usually means SOC and PBS on mobile platforms.
[00:06:45-00:06:48] Here's SOC reference to software operation culling,
[00:06:48-00:06:52] and PBS stands for Precomputers Visibility Center.
[00:06:52-00:06:54] But here's the question.
[00:06:54-00:06:55] Is that enough?
[00:06:55-00:06:59] Well, for therefore, the answer is far from it.
[00:07:00-00:07:03] You will see during the act of productions,
[00:07:03-00:07:04] we don't constrain our artists
[00:07:04-00:07:07] to sub-level design or density rules.
[00:07:07-00:07:10] Because, quite frankly, that's difficult for them
[00:07:10-00:07:12] to understand.
[00:07:12-00:07:16] However, we find that most levels are loaded into memory
[00:07:16-00:07:20] anywhere if we just use the settings from artists.
[00:07:20-00:07:21] It was a disaster.
[00:07:22-00:07:25] We still have a hundred or thousands of visual components,
[00:07:25-00:07:27] even with excellent culling.
[00:07:27-00:07:30] Assumingly, each component generates an average
[00:07:30-00:07:32] of five draw calls.
[00:07:32-00:07:36] We are looking at thousands of draw calls on mobiles.
[00:07:36-00:07:37] This is heavy.
[00:07:37-00:07:40] The CPU overhead led to huge power costs
[00:07:40-00:07:43] on mobile devices additionally.
[00:07:43-00:07:48] Overheading and flash drop could likely result from it.
[00:07:48-00:07:53] To address these issues, we implemented four key techniques.
[00:07:53-00:07:55] High-performance SIM card light,
[00:07:55-00:07:57] resource recommendations,
[00:07:57-00:08:00] SIM feasibility precomputations,
[00:08:00-00:08:02] open-mind junk via SAGC.
[00:08:03-00:08:06] Because the original game seems it's quicker,
[00:08:07-00:08:09] so we need to make the long-time scenes
[00:08:09-00:08:13] most direct to support most precise streaming.
[00:08:13-00:08:15] It's led to our first approach.
[00:08:16-00:08:18] High-performance SIM card light.
[00:08:19-00:08:22] In this card light, there are three key points.
[00:08:22-00:08:26] First, we format sub-levels according to predefined rules
[00:08:26-00:08:28] for hierarchical divisions.
[00:08:28-00:08:31] Categorizing based on the asset size,
[00:08:31-00:08:33] whether they are declarations and so on.
[00:08:33-00:08:36] Different hierarchical level can have different size.
[00:08:37-00:08:39] Second, we do performance optimizations
[00:08:39-00:08:44] on the level components to remove unused components
[00:08:44-00:08:49] to merge same type of static mesh component to ISM
[00:08:49-00:08:52] in nearby regions to discuss straddles
[00:08:52-00:08:57] in those components and so on.
[00:08:58-00:09:00] In short, we prepare the visibilities
[00:09:00-00:09:02] for better long-term coverage,
[00:09:02-00:09:06] and the PVS plays a critical role in long-term performance.
[00:09:07-00:09:09] Please pay attention to the PVS,
[00:09:09-00:09:12] which is sort of precomputed visibility set.
[00:09:12-00:09:14] That's an important technique
[00:09:14-00:09:17] and that could be mentioned many times later.
[00:09:17-00:09:20] We precomputed the visibility for components
[00:09:20-00:09:22] in different position in the scenes.
[00:09:22-00:09:25] We back the PVS cell ID list
[00:09:25-00:09:29] and the invisible components ID list for each cell.
[00:09:29-00:09:34] The size of each PVS cell is equal to one meters
[00:09:34-00:09:37] in the real world.
[00:09:37-00:09:38] This show our sub-levels.
[00:09:38-00:09:43] After the construction public processes.
[00:09:43-00:09:47] As you can see, all sub-levels are now in device
[00:09:47-00:09:49] according to our guidelines,
[00:09:49-00:09:52] which enables more precise level streamings.
[00:09:52-00:09:54] The table here show our different sub-levels
[00:09:54-00:09:58] in hierarchical brain dots, including the size
[00:09:58-00:10:02] and loading settings for each layer.
[00:10:02-00:10:03] All right?
[00:10:03-00:10:06] After going through the construction public live
[00:10:06-00:10:08] processing, level streaming, and PVS calling,
[00:10:08-00:10:10] the game can actually run on mobile device.
[00:10:10-00:10:15] But only on high-end device and the performance
[00:10:15-00:10:18] is still far from acceptable.
[00:10:18-00:10:22] Look at the problems in public, in precisions.
[00:10:22-00:10:25] One of our scenes will have a 320 draw cost
[00:10:25-00:10:28] just for static scenes itself.
[00:10:28-00:10:32] Draw call can even higer when character, weapons,
[00:10:32-00:10:35] and the UIs are adding into game rate.
[00:10:35-00:10:39] More draw call means more CPU overhead.
[00:10:39-00:10:40] And it's less true.
[00:10:40-00:10:43] We have too many generations on mobile.
[00:10:43-00:10:46] We have too many sessions per set.
[00:10:46-00:10:47] We have to reduce the sessions.
[00:10:49-00:10:51] How do we solve this?
[00:10:51-00:10:53] Our solution is resource recommendations,
[00:10:53-00:10:56] which means batch as many as you can of light.
[00:10:56-00:10:59] There are three key aspects of resource recommendations.
[00:10:59-00:11:03] Touch atlas, materials batchings, and model batchings.
[00:11:03-00:11:05] Here's the challenge.
[00:11:05-00:11:09] It requires close cooperation from our art team.
[00:11:09-00:11:12] If a size correction is not standardized,
[00:11:12-00:11:15] the results will be quick pulls.
[00:11:15-00:11:19] At the same time, where batchings does reduce draw call,
[00:11:19-00:11:22] it also increases vertex overhead,
[00:11:22-00:11:23] which needs to be balanced.
[00:11:23-00:11:26] Additionally, it's need to increase in package size
[00:11:26-00:11:28] and memory use.
[00:11:28-00:11:31] Let me walk you through.
[00:11:31-00:11:33] The first step is texture batchings.
[00:11:33-00:11:36] We collect texture from static mesh in the scenes
[00:11:36-00:11:39] and combines them together to the atlas.
[00:11:39-00:11:40] And these are the two core objectives.
[00:11:40-00:11:45] First, minimize the numbers of texture atlas after merges
[00:11:47-00:11:51] because different atlas generate different draw call.
[00:11:51-00:11:53] And second, avoid the texture redundancies
[00:11:53-00:11:55] to reduce package size and memory.
[00:11:56-00:12:00] We are building an open-world scene with different POI areas
[00:12:00-00:12:02] and we also have a shared texture resource
[00:12:02-00:12:05] because on this, we set up some atlas rules.
[00:12:06-00:12:09] We ask our artists to manage the textures by SIMT.
[00:12:09-00:12:10] Distinguish between...
[00:12:10-00:12:15] Shares map textures and POI special textures.
[00:12:15-00:12:17] In this SIMT consent, it's quick and easy
[00:12:17-00:12:21] for artists to understand and execute.
[00:12:21-00:12:24] Fourth, now for materials batchings.
[00:12:24-00:12:28] There are two conditions for materials batchings
[00:12:28-00:12:29] to the tech effect.
[00:12:29-00:12:31] Texture must be identical.
[00:12:31-00:12:34] And materials parameters must also match.
[00:12:34-00:12:37] To improve batching's effectiveness,
[00:12:37-00:12:40] we implement some parameter mergers for materials.
[00:12:40-00:12:41] Storing them in the batching machine,
[00:12:41-00:12:45] then in the batching material eastern parameters list.
[00:12:45-00:12:48] We also impose some constraints on how artists
[00:12:48-00:12:49] use these materials.
[00:12:49-00:12:54] For example, limit overall varieties of wood materials type
[00:12:54-00:13:01] and standards on how materials in eastern parameters are used.
[00:13:01-00:13:04] Next is the static measure batchings.
[00:13:04-00:13:06] This comes in two approaches.
[00:13:06-00:13:09] First, interest static measure batchings.
[00:13:09-00:13:12] Merging multiple sections on each static measure batching.
[00:13:12-00:13:15] Static measure generates only one draw call.
[00:13:15-00:13:19] And second, close static measure batchings.
[00:13:19-00:13:23] Merging multiple static measure from nearby components.
[00:13:23-00:13:26] The trickle here is increase vertical cost,
[00:13:26-00:13:28] package size, and memory.
[00:13:28-00:13:31] We impose distance on...
[00:13:31-00:13:36] Distance-based loads according to our streaming strategies,
[00:13:36-00:13:38] as shown in this diagram.
[00:13:39-00:13:42] For nearby static measure, I require
[00:13:42-00:13:44] high precision.
[00:13:44-00:13:48] We only perform intrusive static measure batchings
[00:13:48-00:13:50] combined with current.
[00:13:50-00:13:54] It reduces a large draw call without any size effect.
[00:13:54-00:13:57] For mid-distance static measure,
[00:13:57-00:14:01] we use the load-use AOD levels
[00:14:01-00:14:04] for close static measure batchings.
[00:14:04-00:14:06] The load-use AOD has very low precision,
[00:14:06-00:14:11] and the impact on package size and memory is a quick limit.
[00:14:11-00:14:13] It has too much мам information.
[00:14:13-00:14:15] For therrrstfect mouse-based adults,
[00:14:15-00:14:18] flash to solar power supply for the first time.
[00:14:18-00:14:21] For the four days, the decommission
[00:14:21-00:14:22] ...
[00:14:22-00:14:22] ...
[00:14:27-00:14:28] ...
[00:14:28-00:14:31] As you can see, in the table on the left
[00:14:31-00:14:36] ...
[00:14:36-00:14:37] ...
[00:14:37-00:14:42] It's just one draw call for all distant models 양
[00:14:42-00:14:44] for certain layers.
[00:14:44-00:14:48] These low quality levels use LD1 statistical measures
[00:14:48-00:14:51] for nearby spectrums, more than aggressively,
[00:14:51-00:14:53] reducing the draw cost.
[00:14:53-00:14:56] As described in table on the right,
[00:14:56-00:14:59] for each quality settings, we use different streaming
[00:14:59-00:15:02] strategies by combinations of different layers
[00:15:02-00:15:10] to satisfy the performance needs of varieties of device.
[00:15:10-00:15:13] As the data shows, since draw cost dropped
[00:15:13-00:15:18] from $320 to $210 after overall statistical measure batching,
[00:15:18-00:15:21] CPU overhead is well optimized and we can place
[00:15:21-00:15:26] the summaries even on a very low-end device.
[00:15:26-00:15:30] However, there are still challenges in the things.
[00:15:30-00:15:33] First, there are still too many components
[00:15:33-00:15:37] and the render stress has to handle every component
[00:15:37-00:15:40] with extensive configuration.
[00:15:40-00:15:42] Second, there are still too many
[00:15:42-00:15:44] statistical measures and touches.
[00:15:44-00:15:48] Which cause massive memory use.
[00:15:48-00:15:49] What should we do?
[00:15:49-00:15:52] We don't want to ask the artist to reduce
[00:15:52-00:15:54] sync resource as much as possible.
[00:15:54-00:15:57] That question is, how's the virtual quality?
[00:15:57-00:16:00] Let's think about it from other perspective.
[00:16:00-00:16:03] Why are there still so many resource?
[00:16:05-00:16:07] And look at this video.
[00:16:08-00:16:13] Although we are currently in thought and can see very few,
[00:16:14-00:16:15] we have a lot of data.
[00:16:15-00:16:16] We can see that the data set in our field or field,
[00:16:16-00:16:23] like this, and they have many invisible sub levels
[00:16:23-00:16:26] in the place but we can see them.
[00:16:28-00:16:31] So now the brain brain becomes too many invisible sub level
[00:16:31-00:16:33] setting in the memory.
[00:16:33-00:16:36] Traditional distant based stream means
[00:16:36-00:16:38] can't solve this problem.
[00:16:38-00:16:41] And the perceived regions control loading approach
[00:16:42-00:16:44] also struggle with these issues.
[00:16:44-00:16:45] Our optimization scrolls become now very easy to use.
[00:16:45-00:16:47] scroll will become clear.
[00:16:47-00:16:52] Unload these invisible sub-levels from memory.
[00:16:52-00:16:55] But how could we achieve this?
[00:16:55-00:16:58] So we tried a room-based loading approach.
[00:16:58-00:17:01] The plan was to SJS endorse static animation
[00:17:01-00:17:04] and others resource to the same levels
[00:17:04-00:17:09] and have level artists to place trigger volumes as it is,
[00:17:09-00:17:11] like dots and windows.
[00:17:11-00:17:17] Looking could only occur when players enter these triggers.
[00:17:17-00:17:20] Now, in series, the approach could handle streamings
[00:17:20-00:17:23] for things with extensive endorsement areas
[00:17:23-00:17:26] of quick will by an increase.
[00:17:26-00:17:31] Our level artists all really struggle with this.
[00:17:31-00:17:34] Our things are just too compressed and less to frequency
[00:17:34-00:17:38] of payment error.
[00:17:38-00:17:41] We also tried other approach, but none
[00:17:41-00:17:41] could be effective.
[00:17:41-00:17:49] So let's review what PVS does.
[00:17:49-00:17:51] PVS data indicate which components are
[00:17:51-00:17:54] invisible at special positions.
[00:17:54-00:17:57] Now, the question becomes, at any given position,
[00:17:57-00:18:01] what sub-levels have all their component invisibles?
[00:18:01-00:18:05] Using these rules, we can precise which sub-levels
[00:18:05-00:18:09] are invisible and safe to unload.
[00:18:09-00:18:11] OK, it should be working.
[00:18:11-00:18:13] But there's still one remaining.
[00:18:13-00:18:17] In short, our sub-levels are devices
[00:18:17-00:18:21] used in space, which means we can't effectively
[00:18:21-00:18:23] distinguish between indoor and outdoor areas,
[00:18:23-00:18:26] as you can see from this diagram.
[00:18:26-00:18:29] Many of our sub-levels contain both indoors and outdoor
[00:18:29-00:18:30] components.
[00:18:30-00:18:32] And the room across multiple floors
[00:18:32-00:18:34] get assigned to the same levels.
[00:18:34-00:18:38] This makes it difficult to achieve the more precise
[00:18:38-00:18:39] optimization.
[00:18:39-00:18:43] So we have to come up with better ways to device
[00:18:43-00:18:46] our sub-level.
[00:18:46-00:18:50] Going back to PVS load data, it recalls relationships
[00:18:50-00:18:54] between a position and the invisible components.
[00:18:54-00:18:58] So we can get all of these invisible positions
[00:18:58-00:19:00] for a given component.
[00:19:00-00:19:04] Now, for components that are inside the same rooms,
[00:19:04-00:19:05] they are invisible.
[00:19:05-00:19:08] Position data show an inherent similarity
[00:19:08-00:19:14] because they tend to be hidden from the same set of viewpoints.
[00:19:14-00:19:15] Based on this principle, we can get all of them.
[00:19:15-00:19:21] We can leverage PVS data to device our sub-level.
[00:19:21-00:19:24] The first step is to cross the PVS data.
[00:19:24-00:19:30] First, we perform the reduction.
[00:19:30-00:19:33] We merge the component invisible PVS cell ID list
[00:19:33-00:19:36] into PVS block ID list.
[00:19:36-00:19:39] We greatly reduce the data size.
[00:19:39-00:19:42] And second, we apply the greatest load
[00:19:42-00:19:44] to cross the components together.
[00:19:44-00:19:49] While minimizing the different weight in each class.
[00:19:49-00:19:53] And should, based on this class group,
[00:19:53-00:19:56] we can consider one group for components
[00:19:56-00:19:58] to have a similar visibility.
[00:19:58-00:20:06] And then, combining with our original special region device,
[00:20:06-00:20:10] we request a new sub-level.
[00:20:10-00:20:11] And the second.
[00:20:11-00:20:14] The second step is post-processing on generated
[00:20:14-00:20:15] sub-levels.
[00:20:15-00:20:23] First, we implement an to score the device levels.
[00:20:23-00:20:26] And second, we left abnormal component
[00:20:26-00:20:30] in a separate group for special .
[00:20:30-00:20:33] And should, after splitting, we continue
[00:20:33-00:20:38] operations separate, evaluate, and look until to find
[00:20:38-00:20:40] the best variant.
[00:20:40-00:20:44] For example, the chart shows the distributions
[00:20:44-00:20:46] by different measures.
[00:20:46-00:20:48] We're varying numbers or sub-levels.
[00:20:48-00:20:50] You can see there is a three-point.
[00:20:50-00:20:53] We need to find the best variant.
[00:20:53-00:20:57] As you can see from this diagram, using PVS guide level
[00:20:57-00:21:01] three, we're able to separate the individuals in dots
[00:21:01-00:21:07] and levels quickly, effectively.
[00:21:07-00:21:12] So finally, after finish our PVS guide sub-levels visibility
[00:21:12-00:21:16] ,, the result was very significant.
[00:21:16-00:21:19] Almost all resource load in memories, disgrace,
[00:21:19-00:21:20] obviously.
[00:21:20-00:21:24] We saw substantial reduction in components, static mesh,
[00:21:24-00:21:28] and texture across the board.
[00:21:28-00:21:31] Because our things are very, very rich,
[00:21:31-00:21:34] and our streaming is fine-grained,
[00:21:34-00:21:36] sub-level loadings and unloading becomes frequent,
[00:21:36-00:21:38] leading to frequent IO operations,
[00:21:38-00:21:41] and sometimes it causes frame drops and junk.
[00:21:41-00:21:42] Junk is the substance.
[00:21:42-00:21:46] Unexpected interruptions or what was otherwise
[00:21:46-00:21:47] small motions.
[00:21:47-00:21:51] Beyond the level streaming, operationalize character
[00:21:51-00:21:51] questions.
[00:21:51-00:21:54] Spawn UIs and garbage collections
[00:21:54-00:21:59] are also sugar-drunk.
[00:21:59-00:22:02] We can handle it with SAGC.
[00:22:02-00:22:04] When games run on the mobile device,
[00:22:04-00:22:09] CPU calls typically don't operate at the max frequencies.
[00:22:09-00:22:10] There are two reasons.
[00:22:10-00:22:12] First, it's performance.
[00:22:12-00:22:16] And second, it's less to a higher power conjunction.
[00:22:16-00:22:20] Now, CodeComp's SAGC provides us with capabilities.
[00:22:20-00:22:24] We can notify the chip hardware in advance to a temporary boost
[00:22:24-00:22:28] code frequencies, meeting our peak performance needs.
[00:22:28-00:22:31] For example, before executing the garbage collections,
[00:22:31-00:22:36] we can call the QAP boot CPU functions and pass it
[00:22:36-00:22:39] in a CPU frequency boost radio.
[00:22:39-00:22:44] This allows us to control the CPU for short-term frequency
[00:22:44-00:22:47] spooting.
[00:22:47-00:22:53] As you can see from the video, with CPU frequency spooting,
[00:22:53-00:22:56] we can remove the disjunct during gameplay.
[00:22:56-00:23:03] OK?
[00:23:03-00:23:07] So that covers the core things of optimization,
[00:23:07-00:23:10] challenge we face, and how do we solve them.
[00:23:10-00:23:13] Let me hand it over to Walker for the second part.
[00:23:13-00:23:23] Thank you.
[00:23:23-00:23:24] Hi, everyone.
[00:23:24-00:23:26] I'm Walker.
[00:23:26-00:23:27] A little bit nervous, though.
[00:23:27-00:23:28] Yeah.
[00:23:28-00:23:30] So I will pick up where Guihong left off
[00:23:30-00:23:33] and dive into the GPU and rendering optimizations
[00:23:33-00:23:36] we've done for Delta Force on mobile.
[00:23:36-00:23:39] Before we get into the details, let
[00:23:39-00:23:42] me quickly walk you through our rendering pipeline on Delta.
[00:23:42-00:23:45] So you will have a better understanding
[00:23:45-00:23:53] of what we are against on mobile.
[00:23:53-00:23:54] Yeah.
[00:23:54-00:23:57] On desktop and console, Delta Force
[00:23:57-00:24:00] uses a classic deferred rendering pipeline.
[00:24:00-00:24:02] Essentially, the rendering process
[00:24:02-00:24:04] break them into the multiple stages.
[00:24:04-00:24:10] First, the scene setup, which includes depth prepass,
[00:24:10-00:24:13] HZB construction, shadows, and more.
[00:24:13-00:24:16] And then comes the surface stage.
[00:24:16-00:24:16] That's exact.
[00:24:16-00:24:20] Exactly where we handle the debuffer, gbuffer, and custom
[00:24:20-00:24:21] depth.
[00:24:21-00:24:25] This is where we prepare all the data the lighting needs later.
[00:24:25-00:24:29] And there comes the lighting.
[00:24:29-00:24:31] That is the most critical stage, and which
[00:24:31-00:24:34] covers the ambient occlusion, direct lighting,
[00:24:34-00:24:38] indirect lighting, and global illumination.
[00:24:38-00:24:40] A lot of things going on there.
[00:24:40-00:24:42] Then we have the reflections and translucency,
[00:24:42-00:24:46] followed by post-processing with TAA, TAU mapping,
[00:24:46-00:24:48] various visual effects.
[00:24:48-00:24:51] And finally, the user interface on top.
[00:24:51-00:24:55] So in the other words, the final image you see on the screen
[00:24:55-00:24:59] is built up layer by layer with data stacking
[00:24:59-00:25:02] on the top of one another.
[00:25:02-00:25:07] Now, please pay attention to the little boxes there.
[00:25:07-00:25:10] Each one of these steps, in practice,
[00:25:10-00:25:15] correspond to a render-pass transition, which means the memory bandwidth overhead.
[00:25:15-00:25:15] So they are in a level of order to build up layer by layer.
[00:25:15-00:25:16] They are in a level of order to build up layer by layer.
[00:25:16-00:25:16] So they are in a level of order to build up layer by layer.
[00:25:16-00:25:16] It's very important to have those different layers of data on top.
[00:25:16-00:25:17] on mobile.
[00:25:17-00:25:21] For desktops, which has delicate video memory,
[00:25:21-00:25:24] that is totally fine.
[00:25:24-00:25:27] In fact, splitting the work across multiple render passes
[00:25:27-00:25:31] and running them in parallel with multiple command lists,
[00:25:31-00:25:35] that's exactly a classic optimization.
[00:25:35-00:25:37] But, here's one thing.
[00:25:37-00:25:40] The entire methodology doesn't work on mobile,
[00:25:40-00:25:43] and it can actually make things worse.
[00:25:43-00:25:46] So, what's the most crucial differences
[00:25:46-00:25:49] between the mobile and desktop?
[00:25:49-00:25:53] You might immediately think of the performance gap
[00:25:53-00:25:56] between the Android, iOS, and desktop,
[00:25:56-00:25:59] or maybe the differences between the APIs,
[00:25:59-00:26:03] GLES, Vulkan, and DirectX.
[00:26:03-00:26:05] But from my perspective,
[00:26:05-00:26:11] the most fundamental difference is the power consumption.
[00:26:11-00:26:13] Mobile devices don't have the luxury
[00:26:13-00:26:15] of a stable external power supply,
[00:26:15-00:26:19] or aggressive cooling like desktops.
[00:26:19-00:26:22] Yeah, and take a look on the chart on the left.
[00:26:22-00:26:24] That's one of our mainstream devices
[00:26:24-00:26:28] after running under a heavy load for an extended period.
[00:26:29-00:26:32] You can see the frame rate starts with small spikes,
[00:26:32-00:26:34] and then, boom.
[00:26:34-00:26:39] It drops from the 60 frames per second down to around 55.
[00:26:41-00:26:45] That is a textbook example of thermal throttling.
[00:26:45-00:26:49] The device overheats, and the GPU is frequency-capped,
[00:26:49-00:26:51] and the frame rate becomes unstable.
[00:26:52-00:26:55] Keeping the power consumption at a sustainable level
[00:26:55-00:26:58] is absolutely critical for maintaining playability.
[00:26:58-00:27:02] Yes, I mean, it's very serious, playability.
[00:27:02-00:27:06] Many factors contribute to the heat generation.
[00:27:06-00:27:09] Besides the CPU-related aspect Guihong covered earlier,
[00:27:09-00:27:13] and the bandwidth and GPU workload are the most common.
[00:27:13-00:27:17] It means the rendering optimization on mobile
[00:27:17-00:27:20] is not just about computation.
[00:27:20-00:27:24] You also must take the power consumption into account,
[00:27:24-00:27:29] and honestly, power oven needs to be the top priority.
[00:27:29-00:27:32] Now, look at the diagrams on the right.
[00:27:32-00:27:35] It shows the divergence between the growth
[00:27:35-00:27:39] of computing power and the memory bandwidth over time.
[00:27:40-00:27:43] The yellow curve shows the compute capability,
[00:27:43-00:27:46] and the blue shows the memory bandwidth.
[00:27:46-00:27:49] The gap between them are widening.
[00:27:49-00:27:54] Expensive bandwidth and limited GPU horsepower,
[00:27:55-00:27:57] there are two core challenges we face
[00:27:57-00:28:03] when optimizing rendering on mobile.
[00:28:03-00:28:05] Given those two core challenges on mobile,
[00:28:05-00:28:07] and the first thing that comes to mind
[00:28:07-00:28:11] are just simplifying the materials,
[00:28:11-00:28:15] reduce the real-time lights, and lowering the resolution.
[00:28:15-00:28:20] But is there really enough?
[00:28:20-00:28:22] As a cross-platform shooter,
[00:28:22-00:28:25] Delta Force Mobile's visuals must maintain
[00:28:25-00:28:29] a near desktop quality, and in the meanwhile,
[00:28:29-00:28:31] as an intensively competitive game,
[00:28:31-00:28:35] the frame rate is essential for gameplay.
[00:28:35-00:28:39] So, there lives us in one path forward.
[00:28:39-00:28:43] We must restructure our rendering pipeline
[00:28:43-00:28:44] for mobile hardware, maximize the use of tele-memory,
[00:28:44-00:28:45] and improve the performance of mobile hardware.
[00:28:45-00:28:46] So, there lives us in one path forward.
[00:28:46-00:28:46] We must restructure our rendering pipeline for mobile hardware,
[00:28:46-00:28:47] maximize the use of tele-memory,
[00:28:47-00:28:50] leverage the latest hardware features
[00:28:50-00:28:51] to reduce the bandwidth,
[00:28:51-00:28:53] and bring in the advanced technologies
[00:28:53-00:28:57] to reduce the GPU workload whenever possible.
[00:28:57-00:29:04] So, let me just start with the bandwidth optimization side.
[00:29:04-00:29:07] I refer to Delta Force's mobile-friendly rendering pipeline
[00:29:07-00:29:11] as LightHDR, yeah, and the meme pretty much summed it up.
[00:29:12-00:29:15] While making the most of mobile hardware features
[00:29:15-00:29:18] to save bandwidth, it still maintains HDR rendering.
[00:29:18-00:29:21] While making the most of mobile hardware features
[00:29:21-00:29:24] to save bandwidth, it still maintains HDR rendering.
[00:29:24-00:29:26] The first step in LightHDR is to merge the scene rendering.
[00:29:26-00:29:28] I refer to everything between the shadow paths
[00:29:28-00:29:30] and the post-processing as scene rendering.
[00:29:30-00:29:35] On mobile, instead of separating the surface
[00:29:35-00:29:37] and lighting into distinct stages, as we do on desktop,
[00:29:37-00:29:41] we do everything in a single render path
[00:29:41-00:29:43] as possible as we can.
[00:29:43-00:29:46] The benefit here is straightforward.
[00:29:46-00:29:47] We keep as much data as possible in the disk,
[00:29:47-00:29:48] and we can still supply it to the disk.
[00:29:48-00:29:51] the tail memory and avoiding the bandwidth overhead
[00:29:51-00:29:53] of the render pass transitions.
[00:29:54-00:29:59] Now, what about the decals?
[00:29:59-00:30:01] Well, most of the decals in Delta Force
[00:30:01-00:30:04] are things like dust marks on the walls.
[00:30:04-00:30:07] Static effects there are already been handled
[00:30:07-00:30:10] during the resource recomposition stage,
[00:30:10-00:30:13] which was mentioned earlier.
[00:30:13-00:30:16] But what about the runtime dynamic decals
[00:30:16-00:30:20] like gravity, graffiti, yeah.
[00:30:20-00:30:23] And that's solvable too.
[00:30:23-00:30:27] We use subpass load, all frame buffer fetch
[00:30:27-00:30:31] combined with depth substantial fetch on GLES
[00:30:31-00:30:34] to read the colors and depth directly from the tail memory
[00:30:34-00:30:37] and then apply the decals to the surface.
[00:30:38-00:30:42] And I really want to highlight this.
[00:30:42-00:30:46] Subpass load is an extremely important technique.
[00:30:46-00:30:49] When used properly, it lets you accomplish
[00:30:49-00:30:50] a lot of things directly.
[00:30:50-00:30:52] It lets you do things directly in the tail memory.
[00:30:52-00:30:56] Otherwise, require extra render passes transitions.
[00:30:56-00:30:59] Many of the optimizations I will be talking about later
[00:30:59-00:31:00] are built on the top of it.
[00:31:02-00:31:05] So, similarly, the translucency doesn't need
[00:31:05-00:31:07] its own render pass either.
[00:31:07-00:31:11] We just draw it right after the opaque geometry
[00:31:11-00:31:14] and that's it.
[00:31:14-00:31:17] So at this point, we have merged both surface
[00:31:17-00:31:19] and lighting into a single render pass.
[00:31:19-00:31:23] That's a great start.
[00:31:23-00:31:26] And I want to talk about the post-processing here.
[00:31:26-00:31:28] As an intensive competitive shooter,
[00:31:28-00:31:32] Delta Force frequently overlays screen effects
[00:31:32-00:31:34] to indicate the player's state,
[00:31:34-00:31:37] such as under attack or injured.
[00:31:38-00:31:41] Take a look at the image on the right.
[00:31:41-00:31:45] Yeah, that is a player running while injured.
[00:31:45-00:31:46] And you can see the multiple layers
[00:31:46-00:31:50] of post-processing effects stack around the edges of screen.
[00:31:51-00:31:54] The traditional post-processing approach
[00:31:54-00:31:58] writes the entire scene to the system memory,
[00:31:58-00:32:01] read it back, and then append the screen overlays on top.
[00:32:02-00:32:04] But here is the question.
[00:32:04-00:32:07] In many cases, these effects don't actually need
[00:32:07-00:32:11] to sample the pixels from other locations.
[00:32:11-00:32:14] There are just simple animations, flowing patterns
[00:32:14-00:32:16] that get blended on the top of the scene.
[00:32:17-00:32:20] So, we replace the traditional post-processing effect,
[00:32:20-00:32:21] and we have the same effect.
[00:32:21-00:32:23] We are processing with screen meshes.
[00:32:23-00:32:27] Yeah, that is exactly a mesh in front of the camera.
[00:32:27-00:32:30] And technically, a full screen quad that joins
[00:32:30-00:32:33] in a subpass right after the scene rendering,
[00:32:33-00:32:35] and before time mapping,
[00:32:35-00:32:36] all within the same render pass
[00:32:36-00:32:43] to achieve nearly identical post-processing results.
[00:32:43-00:32:46] When we completely avoid the bandwidth overhead
[00:32:46-00:32:48] of writing scenes to system memory,
[00:32:48-00:32:54] and reading it back, that's another solid win.
[00:32:54-00:32:55] But we are not done yet.
[00:32:55-00:32:59] In the post-processing stage,
[00:32:59-00:33:01] besides the screen overlay effects,
[00:33:01-00:33:05] there are also auto-exposure to deal with.
[00:33:05-00:33:07] In recent years, auto-exposure has become
[00:33:07-00:33:11] an essential feature for high-quality mobile games.
[00:33:12-00:33:15] The principle is pretty much straightforward.
[00:33:15-00:33:18] You read the color data from the render scene,
[00:33:18-00:33:20] and compute the overall brightness,
[00:33:20-00:33:23] and then scale the image to arrange
[00:33:23-00:33:25] that looks natural to human eye.
[00:33:25-00:33:28] It works just like your eyes do.
[00:33:28-00:33:30] When you walk into a dark room,
[00:33:30-00:33:34] and everything is hard to see at first,
[00:33:34-00:33:36] but pretty soon, your eyes get adapted,
[00:33:36-00:33:38] and your vision becomes clear.
[00:33:39-00:33:43] The problem is that this full screen color sampling
[00:33:43-00:33:47] happens every frame, and it consumes bandwidth.
[00:33:47-00:33:49] But think about the algorithm,
[00:33:49-00:33:51] what algorithm actually needs?
[00:33:52-00:33:55] Just an average brightness value.
[00:33:55-00:33:59] Do we really need to sample more than two million pixels
[00:33:59-00:34:02] to get that average?
[00:34:02-00:34:05] We look at the Monte Carlo methods.
[00:34:05-00:34:07] The core idea is simple.
[00:34:07-00:34:10] Random sampling can still capture
[00:34:10-00:34:13] the key shape of a distribution.
[00:34:13-00:34:16] So, we then sample the scene instead.
[00:34:16-00:34:20] Each 16 by 16 block outputs a single luminous value
[00:34:20-00:34:22] into a small buffer.
[00:34:22-00:34:26] And we compute directly from that small buffer.
[00:34:27-00:34:29] In the vast majority of cases,
[00:34:29-00:34:33] the results are almost identical to the original approach.
[00:34:34-00:34:37] Plus, human eyes naturally adapt
[00:34:37-00:34:40] to the changes in brightness over time.
[00:34:40-00:34:43] If you can tolerate a little bit of latency,
[00:34:43-00:34:45] you can even use the small buffer
[00:34:45-00:34:48] from the previous frame.
[00:34:48-00:34:52] All right, so with the auto exposure before tone mapping,
[00:34:52-00:34:55] and the screen effects after tone mapping handled,
[00:34:55-00:34:58] we are left with the most critical piece,
[00:34:58-00:34:59] the tone mapping itself.
[00:34:59-00:35:03] On mobile, Delta Force's scene rendering
[00:35:03-00:35:07] still operates in linear space with HDR.
[00:35:07-00:35:07] Remember?
[00:35:07-00:35:11] Because we want to maintain the visual quality
[00:35:11-00:35:13] on par with the desktop version.
[00:35:14-00:35:18] The user interface, however, stays in traditional SDR
[00:35:18-00:35:21] to preserve the existing design workflow.
[00:35:21-00:35:23] So, before we draw the UI,
[00:35:23-00:35:26] we must do our tone mapping first.
[00:35:26-00:35:28] Converting the value from HDR to SDR.
[00:35:28-00:35:29] Converting the value from HDR to SDR.
[00:35:29-00:35:29] Converting the value from HDR to SDR.
[00:35:29-00:35:29] Converting the value from HDR to SDR.
[00:35:29-00:35:29] Converting the value from HDR to SDR.
[00:35:29-00:35:33] In theory, this step can't be skipped.
[00:35:34-00:35:36] Can we bypass this?
[00:35:36-00:35:37] Yeah.
[00:35:37-00:35:39] Combining the scene rendering, post-processing,
[00:35:39-00:35:41] auto exposure, tone mapping,
[00:35:41-00:35:44] and UI into one render pass will be very ideal.
[00:35:44-00:35:46] And yes, it's possible.
[00:35:47-00:35:51] Once merged, when the scene resolution matches
[00:35:51-00:35:53] the back buffer's resolution,
[00:35:53-00:35:57] we just need one render pass to handle everything.
[00:35:57-00:35:59] Bandwidth reaches its limit.
[00:35:59-00:36:01] It's minimized.
[00:36:01-00:36:02] Yes.
[00:36:02-00:36:05] And for now, let's consider the case
[00:36:05-00:36:08] where the resolution match.
[00:36:08-00:36:12] The back buffer is the most natural render target for this.
[00:36:12-00:36:14] But here is the question.
[00:36:14-00:36:19] How do you store the HDR values on an SDR format back buffer?
[00:36:19-00:36:23] SDR buffers store values between zero and one.
[00:36:23-00:36:24] That's it.
[00:36:24-00:36:28] While HDR values can exceed 1.0.
[00:36:28-00:36:32] A sunlit surface might be 0.5, I think.
[00:36:32-00:36:35] And a specular might be 10.
[00:36:35-00:36:38] If you write those values directly into an SDR buffer,
[00:36:38-00:36:42] anything above one gets to clamp to 1.0.
[00:36:42-00:36:46] And all the information, all the range, that is gone.
[00:36:46-00:36:50] That's data destruction.
[00:36:50-00:36:55] So, how do you store the HDR values in an SDR buffer?
[00:36:56-00:37:01] Many people will tell you, tell you, tell you, RGBM,
[00:37:01-00:37:03] RGBE, and log love.
[00:37:03-00:37:07] But either the shader math is too expensive at runtime,
[00:37:07-00:37:11] or they don't just make good use of those bits,
[00:37:11-00:37:13] and you end up with color banding.
[00:37:13-00:37:14] Our solution?
[00:37:14-00:37:16] Yeah, a simple curve.
[00:37:16-00:37:21] And I mean embarrassingly simple.
[00:37:21-00:37:23] Now, look at the curve.
[00:37:23-00:37:27] The output should always be in the range between zero and one,
[00:37:27-00:37:27] right?
[00:37:27-00:37:29] It's very simple.
[00:37:29-00:37:31] The K parameter control its shape.
[00:37:31-00:37:32] If the K is small, it will be 0.1.
[00:37:32-00:37:36] The K is small, just like in the left picture.
[00:37:36-00:37:41] And HDR input of 4.0 goes to about 0.8 in the buffer.
[00:37:42-00:37:47] And the specular value of 9.0, that goes to about 0.9.
[00:37:48-00:37:51] There are still differences between the bright stuff
[00:37:51-00:37:53] that exceed 1.0.
[00:37:54-00:37:58] The curve gets steeper while the K is big,
[00:37:58-00:38:02] just like in the right picture when K is five.
[00:38:02-00:38:06] The same 9.0 specular now maps to 0.97.
[00:38:06-00:38:13] And 4.0 is already at, I think, 0.95.
[00:38:13-00:38:16] The SDR outputs are almost the same.
[00:38:16-00:38:20] However, this situation is reversed
[00:38:20-00:38:23] when we look at the small HDR inputs.
[00:38:23-00:38:29] So in short, small K preserves the bright details,
[00:38:29-00:38:31] and the large K maintains the dark details.
[00:38:31-00:38:36] details and we adjust K dynamically based on the potential brightness and
[00:38:36-00:38:47] preserving as much detail as possible. Here is the question, what if the back
[00:38:47-00:38:55] buffer's resolution does not match the scene resolution? For instance, on devices
[00:38:55-00:39:02] with larger screens like the flagships, we do not want the UI to look blurry. In
[00:39:02-00:39:07] that case, we can't merge the top mapping and UI into the same render pass anymore.
[00:39:07-00:39:14] What do we do about the bandwidth hit? After top mapping rise out and the UI
[00:39:14-00:39:20] pass immediately need to read it back in, and under the traditional architecture
[00:39:20-00:39:28] it seems an unsolvable problem. Well, Qualcomm's Snapdragon 8 Gen 5
[00:39:28-00:39:35] brought us a breakthrough solution, TileMemory HIP. TileMemory HIP provides a
[00:39:35-00:39:38] set of APIs that solve the problem.
[00:39:38-00:39:47] These APIs allowed us to place the textures and buffers directly in that TileMemory.
[00:39:47-00:39:54] So we no longer need to write the scene to system memory and reading it back. Here is
[00:39:54-00:40:03] the pseudocoder. As you can see, just a field of lines. It's very easy to implement. We
[00:40:03-00:40:11] currently have the scene placed in the TileMemory HIP. And under our typical HD, 120 frames
[00:40:11-00:40:13] per second and 1080p resolution, the TileMemory HIP is the best solution.
[00:40:13-00:40:22] In this case, it's a 5.7 reduction in the total power consumption. And yes, that's
[00:40:22-00:40:28] without sacrificing any visual quality or reducing the resolution. The results
[00:40:28-00:40:33] are very satisfying and we also plan to migrate more data to the TileMemory HIP
[00:40:33-00:40:39] and further extending the power savings.
[00:40:39-00:40:45] Alright? With all that covered, let me wrap this session. When it comes to
[00:40:45-00:40:45] a
[00:40:45-00:40:52] mobile power consumption the bandwidth is a major factor here are the key
[00:40:52-00:40:57] takeaways from Delta forces mobile rendering pipeline optimizations first
[00:40:57-00:41:04] for effects they can be achieved with a more power friendly way just avoid using
[00:41:04-00:41:11] the traditional post processing workflows second merge as many render
[00:41:11-00:41:17] passes as possible that is very important including the scene rendering
[00:41:17-00:41:26] auto exposure tom mapping and UI third for render pass transitions there are
[00:41:26-00:41:33] truly can't be avoided use tell memory heap to eliminate the bandwidth overhead
[00:41:33-00:41:40] so there covers the bandwidth optimizations for rendering pipeline now
[00:41:40-00:41:41] what about
[00:41:41-00:41:47] the other major source of power consumption the GPU itself GPU workload
[00:41:47-00:41:53] is also a very significant factor in heat and power drain and I will break
[00:41:53-00:42:02] this down into key areas first when you're playing a game it's pretty easy
[00:42:02-00:42:09] to notice that not every pixel in the screen has a widely different color in
[00:42:09-00:42:14] most cases pixels within a small range are very similar
[00:42:14-00:42:20] for example when a character is in an outdoor environment the surface of the
[00:42:20-00:42:27] metal container the sky a dam in the distance their colors are extremely
[00:42:27-00:42:35] close and sometimes the pixels are almost identical so naturally you start
[00:42:35-00:42:41] thinking can we have the GPU shade just once and feel the result into the
[00:42:41-00:42:46] multiple pixels and the answer is yes
[00:42:46-00:42:54] modern mobile devices now support VRS variable rate shading in simple terms
[00:42:54-00:43:00] VRS lets a larger block of pixels to share a single shading computation and
[00:43:00-00:43:09] that result gets applied to every pixels in that block so the problem becomes how
[00:43:09-00:43:14] do we identify these visually similar regions and how do we measure how
[00:43:14-00:43:22] similar they are our approach is to divide a screen and
[00:43:22-00:43:29] into small tails and then group them into larger ones each small tail records
[00:43:29-00:43:36] its luminance during the previous frame in the current frame we computed the
[00:43:36-00:43:41] color variance among the fragments within each tail if the color variance
[00:43:41-00:43:47] within the tail is very small that means the pixels are visually similar right
[00:43:47-00:43:52] for those tails we can apply two by two or even four by four
[00:43:52-00:43:59] VRS shading rates take a look at these two images below the left image shows
[00:43:59-00:44:04] the dump sampled luminance output from the previous frame even though we don't
[00:44:04-00:44:09] have the full color data we can still roughly reconstruct the scene's
[00:44:09-00:44:15] brightness construct and the right image shows the color variance computed
[00:44:15-00:44:22] from the left black means dissimilar dark red means similar and the brightest
[00:44:22-00:44:29] red means very similar you can see that large areas of the sky are highly
[00:44:29-00:44:36] similar many flat surface in the scene as well as the rough metallic parts of
[00:44:36-00:44:43] the players weapon also shows a lot of similarity all of these regions can
[00:44:43-00:44:52] directly benefit from VRS and save GPU workload but is that enough how do we
[00:44:52-00:44:56] know about the black areas for instance distant and foreground trees may have
[00:44:56-00:45:03] different stripe color but visually these differences are insignificant to
[00:45:03-00:45:12] the player can we optimize this extensive testing confirm we can so the
[00:45:12-00:45:19] solution becomes quite clear first we dump sample the luminance directly into
[00:45:19-00:45:23] a small buffer second before the next frame begins
[00:45:24-00:45:28] we computed the shading rate based on the luminance differences and generate a
[00:45:28-00:45:35] VRS attachment to apply the VRS third for distant objects will additionally
[00:45:35-00:45:42] apply VRS on a case-by-case basis which is a OD level of course this approach
[00:45:42-00:45:48] isn't perfect when the camera moves aggressively using the luminance of the
[00:45:48-00:45:53] last frame can be inaccurate in those scenarios it falls back to a more
[00:45:53-00:46:01] conservative shading strategy and let's take a look at the results the
[00:46:01-00:46:08] performance game from VRS are quite a satisfying satisfying yeah still under
[00:46:08-00:46:15] our typical HD 120 frames per second and 1080p configuration the visual difference
[00:46:15-00:46:23] is barely noticeable and we can three additional frames and the GPU clock was
[00:46:23-00:46:28] reduced by twelve point six percent it's amazing
[00:46:28-00:46:35] right and now let's shift our perspective from a single frame to a
[00:46:35-00:46:40] continuous stretch of gameplay the buildings and grounds in front of the
[00:46:40-00:46:47] player get rendered every single frame but if you look closely you will notice
[00:46:47-00:46:51] the terrain and the trunk in front of player haven't actually changed at all
[00:46:51-00:46:58] only the player is moving the surrounding scene have merely shift on
[00:46:58-00:46:59] the screen
[00:47:00-00:47:06] so naturally the question arise can we reuse the pixels that were already been
[00:47:06-00:47:14] shaded in previous frames that brought us to a frame interpolation the frame
[00:47:14-00:47:21] interpolation has been well used in the TV industry for years and as core is
[00:47:21-00:47:24] about generating the new pixels from existing ones
[00:47:24-00:47:31] however the interpolation introduced input delay and extrapolation introduced ghosting
[00:47:31-00:47:31] and extrapolation introduced ghosting
[00:47:32-00:47:39] according to our extensive tesis both of them are unacceptable and especially for
[00:47:39-00:47:48] shooter still we can borrow the underlying idea what if we just separate
[00:47:48-00:47:53] the static scene element from the dynamic ones doesn't that solve the
[00:47:53-00:48:00] problem static scene elements don't move on their own any position change on the
[00:48:00-00:48:04] screen must be caused by the camera movement and again and again we have to
[00:48:04-00:48:07] take online development down to the basic architecture and this really
[00:48:07-00:48:33] highlights the challenge of the performance that
[00:48:33-00:48:43] There were already been shaded for dynamic objects, characters, weapons, and so on.
[00:48:43-00:48:46] We random them normally, just like before.
[00:48:46-00:48:50] So our dynamic frame prediction approach becomes clear.
[00:48:50-00:48:55] First, we are not doing a frame generation.
[00:48:55-00:48:58] We are re-projecting the static scene.
[00:48:58-00:49:02] Second, we reuse the static scene.
[00:49:02-00:49:10] Third, we render the dynamic objects, such as enemies and characters, normally.
[00:49:10-00:49:13] And it's critical.
[00:49:13-00:49:17] The game still runs at 120 frames per second.
[00:49:17-00:49:22] No input delayed or ghosting introduced.
[00:49:22-00:49:26] It achieves an inter-frame reuse of static scene element.
[00:49:26-00:49:31] There are still many more details to this approach, but due to the time constraint,
[00:49:31-00:49:32] I won't go into it.
[00:49:32-00:49:33] I'll go deeper into it here.
[00:49:33-00:49:41] The performance data was also very impressive.
[00:49:41-00:49:45] The frame rate increased by 10 frames, 10 frames,
[00:49:45-00:49:49] while the GPU clock actually decreased.
[00:49:49-00:49:56] Ultimately, we achieved a 14% reduction in the GPU workload.
[00:49:56-00:50:00] And if you push the quality settings higher or increase the resolution,
[00:50:00-00:50:05] the gains become even more significant.
[00:50:05-00:50:08] So we have optimizations along two dimensions.
[00:50:08-00:50:15] On the one hand, within a single frame, we identified the regions with similar colors
[00:50:15-00:50:22] and minimized the visual difference and used VRS to shade less.
[00:50:22-00:50:27] On the other hand, across frames, we used dynamic frame prediction to reuse the previously
[00:50:27-00:50:32] shaded color whenever possible.
[00:50:32-00:50:34] Can we combine the two?
[00:50:34-00:50:35] Absolutely.
[00:50:35-00:50:39] And in practice, combining them produced excellent results.
[00:50:39-00:50:39] Still, I'm not sure.
[00:50:39-00:50:47] Still, under our typical HD, 120 frames per second, 1080p settings,
[00:50:47-00:50:54] with no material simplification, the GPU workload was dropped by 26%.
[00:50:54-00:50:57] It's huge.
[00:50:57-00:51:08] And that is what truly makes high-quality visuals at high frame rates a reality for mobile.
[00:51:08-00:51:13] Let me summarize the Delta Force's work on reducing GPU workload through the advanced
[00:51:13-00:51:17] rendering features on mobile.
[00:51:17-00:51:23] We fully leveraged the spatial and temporal coherence.
[00:51:23-00:51:31] The GPU optimization is not just about reducing the computation and the computational complexity.
[00:51:31-00:51:37] It can also come from the reusing the pixels that have already been shaded.
[00:51:37-00:51:43] For mobile devices with limited resources, we're essentially dancing in chance, allocating
[00:51:43-00:51:48] the resources to what matters most based on the current gameplay needs and the visual
[00:51:48-00:51:56] requirements, while optimizing the performance in visually unnoticeable areas.
[00:51:56-00:52:03] At its core, this is an art of balance.
[00:52:03-00:52:09] Delta Force's optimization journey on mobile is just the beginning.
[00:52:09-00:52:14] And in the coming releases, we will push visual qualities even further.
[00:52:14-00:52:20] More realistic light and shadow interactions, more convincing reflections, and richer geometry
[00:52:20-00:52:21] details.
[00:52:21-00:52:30] Alongside more diverse gameplay experience, including more destructible objects and beyond.
[00:52:30-00:52:38] At the same time, 120 frames per second has evolved from a nice-to-have into a baseline
[00:52:38-00:52:42] expectation for competitive shooters.
[00:52:42-00:52:47] How to improve the visual quality and enrich the experience while maintaining the excellent
[00:52:47-00:52:49] performance?
[00:52:49-00:52:51] And doing so with enough scalability across the board?
[00:52:51-00:52:58] That's a challenge ahead of us.
[00:52:58-00:52:59] Stay tuned.
[00:52:59-00:53:03] That wraps up the presentation from Gui Hong and me.
[00:53:03-00:53:04] Thanks for attending this session.
[00:53:04-00:53:16] And I'm going to return the stage to Jane.
[00:53:16-00:53:18] So that was amazing sharing.
[00:53:18-00:53:23] Thank you, Gui Hong and Walker.
[00:53:23-00:53:27] I'd like to introduce our teams, and we want to provide you some takeaways.
[00:53:27-00:53:28] So we'll start with Jane.
[00:53:28-00:53:29] Jane, can you talk about the game?
[00:53:29-00:53:30] Sure.
[00:53:30-00:53:33] from the Qualcomm Snapdragon Game Studios.
[00:53:33-00:53:37] So listen to what Guihong and Walker just shared.
[00:53:37-00:53:40] You might wonder, like, how can I get resources
[00:53:40-00:53:43] for those solutions and I'm developing my own project
[00:53:43-00:53:45] and how can I learn best practices
[00:53:45-00:53:48] to actually implement into my own project?
[00:53:48-00:53:53] Okay, now let's jump to the Snapdragon toolkit.
[00:53:55-00:53:59] So just scan this QR code and you can check
[00:53:59-00:54:01] what's available on the Snapdragon toolkit.
[00:54:01-00:54:05] So we provide extensive documentations
[00:54:05-00:54:08] and tools and resources for developers
[00:54:08-00:54:09] and then you can also find,
[00:54:09-00:54:13] we have our GitHub Snapdragon Unreal fork.
[00:54:13-00:54:16] So as a Snapdragon studio,
[00:54:16-00:54:19] we prioritize on getting new features actually
[00:54:19-00:54:22] and merge into the engine,
[00:54:22-00:54:25] the Epic Unreal Engine mainline releases.
[00:54:25-00:54:29] So we also maintain some changes
[00:54:29-00:54:31] on our own GitHub fork.
[00:54:31-00:54:34] If you want to learn more about the latest features
[00:54:34-00:54:41] and how would they incorporate into your projects.
[00:54:41-00:54:44] So we might run out of time.
[00:54:44-00:54:47] So I don't know if we have time,
[00:54:47-00:54:51] maybe for just a couple of few questions.
[00:54:52-00:54:55] You can also connect with us
[00:54:55-00:54:57] through the Discord community group
[00:54:57-00:55:02] and we can maybe take a couple of questions if you have any.
[00:55:02-00:55:03] If you want to ask a question, you can ask me.
[00:55:03-00:55:04] If you have a question,
[00:55:04-00:55:20] you can probably walk to the mic.
[00:55:20-00:55:22] It's improvement.
[00:55:22-00:55:26] Do you guys are looking at super resolution
[00:55:26-00:55:29] to gain, to get more performance
[00:55:29-00:55:32] out of your GPU pipeline?
[00:55:32-00:55:48] Super resolution, have you looked into that?
[00:55:48-00:55:49] That is a good question.
[00:55:49-00:55:54] And the super resolution is a very good method
[00:55:54-00:55:56] to improve the performance and visual quality.
[00:55:56-00:55:58] But the competitive,
[00:55:58-00:56:02] competitive shooters for our game,
[00:56:02-00:56:05] we don't have the motion vectors.
[00:56:05-00:56:10] So we are not able to just scale it in the right way.
[00:56:10-00:56:13] And it will be very, very heavy.
[00:56:13-00:56:16] And it causes much bandwidth overhead
[00:56:16-00:56:21] for us to append the motion vector to the game.
[00:56:21-00:56:24] So if you want to use the super resolution,
[00:56:24-00:56:26] you must base on your own needs.
[00:56:26-00:56:28] And please,
[00:56:28-00:56:32] take care about the bandwidth optimization.
[00:56:32-00:56:32] Yeah, thank you.
[00:56:32-00:56:36] That makes sense.
[00:56:36-00:56:38] Hello.
[00:56:38-00:56:45] So a function that a mobile device has and PC usually
[00:56:45-00:56:48] doesn't have is vibration or haptics.
[00:56:48-00:56:51] So I wonder if you applied haptics or vibration
[00:56:51-00:56:55] to the mobile version of your game.
[00:56:55-00:56:59] If not yet, do you have a plan in the future?
[00:56:59-00:57:01] I think I didn't catch it.
[00:57:01-00:57:01] Like, for you?
[00:57:01-00:57:03] For example, if the user, like, shoot,
[00:57:03-00:57:06] and then the mobile phone can vibrate,
[00:57:06-00:57:09] will that be a better, like, user experience?
[00:57:35-00:57:39] We don't have the vibration so far.
[00:57:39-00:57:41] It's still under consideration.
[00:57:41-00:57:45] But from our test results, the vibration
[00:57:45-00:57:49] is not always a good thing for the player.
[00:57:49-00:57:50] Yeah.
[00:57:50-00:57:53] So you need to take care of the effects
[00:57:53-00:57:57] and do some research, maybe.
[00:57:57-00:57:58] Sure.
[00:57:58-00:57:58] Thank you.
[00:57:58-00:58:01] We are still on it, and it's under consideration.
[00:58:01-00:58:01] Sure.
[00:58:01-00:58:01] Thank you so much.
[00:58:01-00:58:02] Thank you.
