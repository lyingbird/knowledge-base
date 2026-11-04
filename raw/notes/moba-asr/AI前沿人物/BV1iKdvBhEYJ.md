---
title: "Codex产品负责人：Codex团队如何用Codex"
platform: bilibili
bvid: BV1iKdvBhEYJ
author: Easonlee的AI笔记
pubdate: 20260416
duration_sec: 2596
view: 8492
like: 321
url: https://www.bilibili.com/video/BV1iKdvBhEYJ
subtitle_source: faster-whisper_large-v3
asr_model: large-v3
transcript_chars: 51389
crawl_time: 2026-07-12
---

# Codex产品负责人：Codex团队如何用Codex

## 视频信息

- **UP主**: Easonlee的AI笔记
- **时长**: 43min
- **链接**: https://www.bilibili.com/video/BV1iKdvBhEYJ

## 视频描述

大家好，我是Easonlee，做自己和AI的CEO。

《AI Builder》专栏，分享一线AI创始人的实践和思考。AI时代，让我们关注Builder，成为Builder。

原始视频发布时间：2026-04-05

导读：本期访谈邀请了 OpenAI Codex 团队的 Alex 和 Romain，深度拆解了全球最顶尖的 AI 编码工具团队如何利用 AI 重新定义软件开发流程。嘉宾指出，在代理化开发的未来，传统职能边界将彻底模糊，高能动性的“建设者”将取代传统的流程管理角色。

1. 职能边界模糊，设计师编写的代码已超过工程师 [10:30]
在 AI 工具加持下，人才堆栈正在崩溃。Cod

## 完整文稿

> 来源: faster-whisper large-v3 (CUDA/fp16)

We write very, very few specs on the Codex team.
We're like talking like 10 bullets or something and that's it.
The designers on the Codex team write more code now than like was written by an engineer like six months ago.
And I made a quick prompt to create a little 2D game.
Maybe add some more decorations, houses, trees and stuff.
Could you add some more decoration like trees?
And there we go.
We have already like new trees appearing.
For small change, it's like often faster to send a PR than it is to like communicate to someone and get them to prioritize that task.
When they have like 10,000 other things to do.
I don't actually view PM as a good leadership position.
I view it as a fill in the gaps position.
I think the fewer people you need in a room to do anything, just the better that thing goes, the more pure every decision is.
Okay, welcome everyone.
I'm really excited to host today Alex and Roman from OpenAI's Codex team.
They're going to demo how they build new features of Codex, what Codex is capable of, and also talk about how the Codex team ships nonstop.
So welcome guys.
Thank you.
Thank you for having us.
Yeah, excited to chat.
So do you guys want?
Just quickly show what kind of things Codex can actually build in one shot?
Yeah, for sure.
I mean, like, let me like share my screen to give you a sense.
And so like there's so much I could show, but maybe like a quick glimpse into like, for instance, here is an iOS app I've been building.
And if I want to actually create a new feature for this app, I can simply dictate and voiceover something that says, hey, can you add a new screen for NASA's Artemis mission return to the moon?
And I can send that prompt with GPT 5.4.
And sure enough, the model will like create a new screen for this particular iPhone app.
So here we have this app.
It's pretty cool.
And it's currently building this new feature.
So we should see that in a moment.
But we also have the Codex Spark model, which can really help you ideate and iterate in just a few seconds on anything.
In fact, let me show you like what it's working over here.
The difference of what it does to have a Spark model responding so quickly.
On the left.
On the left side, you have GPT 5.4, right?
I'm going to give it a head start.
And on the right side, you have Codex Spark.
And boom, you have like 1,200 seconds on average.
This is insane speed.
And so when you want to build something, let's say a game, right before we started this conversation, I actually went to the Codex app and I made a quick prompt to create behind the crossing, a little like 2D game where I can start building.
What also I love using with the Codex app when I'm in.
The flow is taking the Codex app like this and pop the conversation out on top of the screen, right?
And so this way, now what I can do is like if I'm like actually working on this game, I can keep iterating and have more ideas.
I don't know what we want to do.
Do you have an idea, Peter, for what you would like to change on this game?
Maybe add some more decorations, houses, trees and stuff, make it more lively.
Could you add some more decoration like trees?
And I'm going to send this task.
And in basically a handful of seconds, Codex Spark will be able to edit and we'll see the changes live.
And there we go.
We have already like new trees appearing and I can keep on playing.
This is insane speed, right?
And so that's why I'm so excited about Codex.
You can really have frontier models like GPT 5.4 that can take on very complex tasks like, you know, millions of lines of code to analyze or migrate.
But if you're in the flow and you're really feeling inspired, you can reach for like the.
Fast mode or even Codex Spark and you have this like insane speed of thought where you can really build anything.
So this is just a quick tour for how to build with Codex.
This episode is brought to you by Granola.
If you're in back to back meetings, you know how much work it is to take notes live and clean them up afterwards.
That's why I love Granola, the best AI meeting notes app in the market.
Here's how I use it.
Granola automatically takes notes during a meeting and I can add my own notes too.
After the meeting ends.
I use it.
I use a Granola recipe to extract clear takeaways and next steps in the exact format that I want.
Then I can just share notes directly in Slack with my colleagues or even get Granola to share notes automatically.
Honestly, of all the AI apps that I use, Granola is the one that saves me the most time.
Try it now at granola.ai slash Peter and use the code Peter to sign up and get three months free.
That's granola.ai slash Peter.
Now back to our episode.
I'm really curious how you guys.
Actually built products with Codex on the team, right?
Alex, do you even write specs anymore or like, do you get GPT write a spec?
Like which model do you use when to make this stuff work?
Yeah, I think we write very, very few specs on the Codex team.
Actually, I think a lot of the work is like, you know, let's have the people closest to the metal making as many decisions as possible.
And so the only time that we'll write a spec is if it ends up being a problem that's like kind of hard to fit in one person's brain.
Right.
And by the way, like one person can fit a lot in their brain now because they can do a lot like they're delegating most of the coding, right?
And so one person can do a lot.
But if it ends up being a thing where we're like coordinating across a few people, or maybe it's like a really thorny decision that we have to make, then maybe we'll write a spec.
But these the docs that we do right in these cases tend to be incredibly short.
You're talking like talking like ten bullets or something, and that's it.
Okay, can you guys like show me how this works?
Like you give Codex like a few bullets and then maybe it writes the actual requirements first.
Yeah.
And yeah, yeah, we could do that.
But also like one thing I want to show you also very simply imagine like going back to this iOS app I was mentioning that's like currently like finishing a task over here.
Imagine you have like ideas for new features for a net new project and you have some ideas, but you're not exactly sure where to go.
What is very exciting now with with Codex is that if I start actually talking about let's plan the next steps, you can see that like Codex has automatically understood that I'm trying to make a plan.
So I can just say like, okay, I'm going to start with a plan for what we should build next.
So I need to think about the next step.
And so if I simply do shift tab, it will enter plan mode.
And if I say like, what should we build?
Like I can use Codex as a brainstorming partner to plan.
And in this plan mode, it's going to look at the code.
It's going to look at where we are so far in the project come up with ideas.
And then I can also bring my own ideas and start steering the mall into a good plan.
And so based on that, you can see, for instance, as we speak here, that we're actually starting to get some good ideas.
that Codex has some ideas based on what it's looking for and the files.
And so here, it's going to actually prompt me for some guidance.
Like, what should we do?
Should we start working more on the Artemis idea that we were just doing?
Should we just do a pass on reliability, a dashboard?
Maybe we'll say, yeah, maybe a reliability pass is good.
Wait, who should we optimize for?
And so I can use Codex this way.
And of course, here, I gave no input.
So in the case of Alex, as a product lead, I'm sure you would give a lot more guidance up front.
But here, I'm kind of letting Codex take some ideas.
It's funny.
I do this a lot, too.
Yeah, like often I'll...
Okay, so there's like various kinds of changes, right?
There's like the super simple change.
You just go straight in.
You prompt it.
Yeah.
Right.
Then there's like sort of a medium complexity change where maybe you're like reasoning about how to do it or ask for a specific plan.
But something that I actually do is kind of...
Like similar to this, where if I have like a vague idea, I might just go into Codex and just ask it to start like thinking about how it might solve a problem.
I don't even have a feature in mind.
And then like, you know, it'll go explore and like ask me some questions.
And like, in my case, I often don't end up even using that thing because maybe this is quite a complex change that like...
So, you know, so there's a digression here, but like what code do PMs write is an interesting thing to get back to.
But like maybe a complex change.
Like I don't actually want to be on the hook for like landing and maintaining that change.
But I'll still go through the motions of like a plan.
And like exploring it.
And then I just have a better mental model of what we need to do.
And then that becomes something that like not the plan itself, but like just the thinking becomes something that I share with an engineer.
I feel like...
So like to take that digression briefly, like the designers on the Codex team, right?
Like, you know, we like to joke like more code now than like was written by an engineer like six months ago.
They're like absolutely goaded.
But obviously the tool is a massive part of this.
And, you know, the team was making fun of me for not...
Not landing that many PRs in the last year.
I'm not going to give you the number, but I'm like, yeah, it should be more.
Especially when you consider how many of those were very small tweaks.
But I feel like we're at a point now where like it's not about can you generate the code?
Like the agent is amazing.
You can delegate tasks to it.
It starts to be a point of like, what are you deciding to do?
That's actually super important.
Like, are we aligned on what this thing is becoming?
And then on the other side of it, it's like, how are we making sure the thing is really high quality?
Like, you know, like some folks will say proudly say like the entire app is vibe coded.
Like in the case of Codex, like the vast majority of code was generated by an agent.
But we still spend a lot of care and attention, like thinking about the system and making sure it's really high quality.
And so that's why, for instance, if there's a really complicated feature, I often will make sure there's like a more robust, stable owner to own it.
And I don't think you want...
Part of the value of a PM is they can be like super distracted and they go around.
And so you don't necessarily want PMs owning these systems.
Yeah, you don't want a PM to like maintain a feature code.
That doesn't sound like a good idea.
I think we'll screw it up.
Yeah.
Yeah.
Okay.
And like...
Yeah.
Some of the other products out there are like...
Like I love the other products too, but like you have to spend so much time learning them.
I almost feel like if I'm not on Twitter, I would have no idea how to use the other products.
And like one thing I really love about Codex is like how simple the app is to use.
You know, it's just like very intuitive and very simple.
But there is like some pretty advanced features like skills and automations, right?
Like do you guys use that stuff internally?
Yeah, a ton.
A ton.
In fact, like I think skills are like the most interesting thing.
Like the things that like the Codex app surface enables you to use, like for instance, like imagine you're pairing with designers that use Figma.
Well, it's amazing now to turn on the Figma skill to kind of pull details directly from the Figma files, all of the React components, the variables, and then like Codex will like implement this code accordingly.
But imagine like you're building an app, like maybe you want to share it and you want to deploy that to Vercel or Cloudflare or Render.
Those skills are like...
Right there.
And so you can just simply like tell Codex what to do and will basically connect to this ecosystem of tasks.
It's funny.
I was talking to a friend like a couple nights ago.
He was telling me that he had like a ton of ideas to improve his product.
And he told Codex, just write all of these tasks on linear so I keep track of everything as we go using that skill.
And at the end of it, he's like, well, now I'm going to bed.
Go ahead and implement all of these tasks that we just discussed and cross them off.
And sure enough, he woke up.
I think it was actually complete.
Yeah.
That's amazing.
Coming back to your point about like the simplicity of the app, I think it could be interesting to share a little bit about how we think about designing it.
I don't know if that's interesting.
Yes.
Kind of like there's something that's really interesting about building in this space is that developers love just like automating tools for themselves, like building tools for themselves, automating parts of the work.
And so I feel like a really important part of the product is that it's like super configurable.
Right.
And so like for us, Codex, like the harness is open source.
Like you can go deep in like whenever we're building a feature, we start getting complaints on Twitter that the feature, which, by the way, is like not enabled in prod is like broken because that people are going in and like changing the code themselves or forking it to like get these new features working.
But for me, that's like an awesome part of the product.
Right.
And what that means is like the cutting edge of your users are just absolutely living in the future with us and pulling us into that future.
On the other hand, though, like if you only built for that, you end up with this thing that's like nearly impossible to understand and you spend all day on Twitter, like you were saying.
And so we.
Kind of have this view of like.
We are really careful about like what the core primitives of what we're building are like.
That's the place where this stuff will be written down.
And it's not just like a vibe coded thing.
It's like we're really thought like, OK, how do we mostly let the product be almost invisible, get out of the way of the model and just let the model like and every time the model gets better, just do more and more.
Then from there, how do we package this in as configurable a way as possible for power users so they can figure out what it is?
For instance, there's an implementation of like.
Sub agents that's out in the wild right now and people are like using it and experimenting and we're learning a ton from them, even though we don't actually trigger that proactively in the product.
It's just like something that users can learn about and go use.
And then we learn from how people are using it.
And then from there we think about, OK, now how do we make that super simple for everyone else?
So like the Codex app is actually an example of this, where around the time of like.
I would say like GPT GPT 5.2 Codex in December.
Um.
All of a sudden, like it was like incremental, steady model progress, but we just kind of cleared this point where you could start delegating like way longer tasks to the model and it would just like one shot at anyways.
Yeah.
Um, and so we started to see like people were already team boxing, like, or, you know, for anyone who doesn't know what team boxing people are already like running many parallels in terminal.
Um, but we started seeing like crazy, like things on social media.
Like there's this one picture of like Peter Steinberger with like, you know, the creative open call with like, I don't know, like 18 terminals across eight, like three monitors.
So we started seeing people like using Codex in the.
This very advanced way.
We were very excited.
We kept making sure the delegation worked well in the basic product, like CLI, but then we were like, okay, like maybe the top 1% of engineers are going to work that way.
How do we make this feel really intuitive?
And so then we got to the Codex app, which you launch it.
It just feels super simple.
It's just like a chat.
It'll do work, but then you start discovering, oh, there's a sidebar.
Oh, I can run multiple tasks.
Oh, it's like really easy for me to click between them.
Okay.
Now I'm like being really effective myself.
And then it's like, ah, there's a skills tab.
Let me like go into here.
Yeah.
Yeah.
So we try to like make it so it's almost like playing a game.
You're just like discovering what's next.
Totally.
And I think like we've always had this vision, right?
From the get go that like coding will take place into this like agentic delegation fashion.
Like even when we started Codex almost a year ago, we're always thinking about this like future where as an engineer, you're working on multiple things in parallel.
But candidly, the models were not quite there yet.
Yeah.
Right.
And I think we needed to see like the inflection point with GPT 5.2 Codex and beyond that to see the model.
Being able to be like super thorough and work reliably for hours on end, if not days.
And then by that time, you're like, well, now this is a weird interface to have multiple tabs open in a terminal and just let them run for hours, you know?
And so then we needed to have this new surface.
And I think the timing for something like that became perfect.
Yeah.
There's two vibe shifts in Codex history.
The first is like August.
So we launched this Codex Cloud product.
It was a great idea.
People were super.
People are still super excited about it, but it was a little early.
So around August, we shipped GPT-5, great interactive coding model.
We were like, all right, like, let's go solve the problem that the models can solve right now.
Ship Codex CLI ID extension.
Growth started exploding then.
And, you know, I remember it was like we grew like 20 or 30x in like a few months, which is awesome.
And then the second vibe shift was around December, January, where we actually could get back to this vision of like delegating to models.
Let's go a little bit deeper into the development of the Codex app.
So, um, did you have like some sort of a, do you have sort of like any roadmap like a year ago, like, Hey, in this time, we're going to launch the Codex app or is it more like you kind of saw the market doing this stuff and then you kind of prototype a bunch of stuff.
Like how, how was this thing built?
Okay.
So it's like neither.
Um, and, uh, I got some really good advice, um, from a researcher here called Andre and, uh, his advice for me was that it opened the eye you either plan near-term or long-term, but you can never plan medium term.
Okay.
Um, it's just too difficult.
So near-term is like up to eight weeks from now, eight weeks being the absolute maximum.
What is a concrete thing that you can like motivate a team to like rally together around and get done?
And this is something that we're really good at opening eyes, like kind of like rallying a team around like a thing that we want to do.
Yeah.
Um, the other thing you can do is you can kind of have a vibe that's like, you know, like a year from now, we're going to have models that are way smarter.
They're going to be able to do like, you know, I'm rewinding back a little bit in time now.
You know, because now like what I'm about to say is like obvious and it's obviously less than a year from now, but you might be like, yeah, we're going to have models and, um, we're not going to want to lend them our computer to do work because then we can only do one thing at a time.
We're going to want like infinitely many models and they're just going to be doing work independently, like validating their own work, maybe even deploying the code themselves and monitoring it themselves.
And we shouldn't even have to prompt them necessarily.
And so you can kind of think ahead to like this kind of vibe.
Right.
Um, and the in-between thing is just kind of awkward.
So the in-between thing is like a product roadmap.
Yeah.
We basically don't really have those.
We have the combination of like a sort of a long-term direction and like things that we think bring us in that direction.
So for instance, in the case of the Codex app, like one of the strategic goals that we had was to dissociate ourselves from a specific workspace.
Okay.
So that's a bit abstract.
What I mean is that like, if you're using an IDE like VS Code, which is my favorite IDE, um, you open VS Code to a specific workspace, right?
That's a specific checkout of the code.
Yeah.
Specific.
That's a specific folder, right?
And even if you're using Git work trees, you can only open it to like one Git work tree at a time.
And so you basically can only work on one thing at a time.
Right.
And the same is true for like a CLI as well.
And like, because we know we have this vision of like, we want people to be working with agents that they've delegated to in the cloud that are just working independently.
We know we need to get to a point where it feels really natural to be talking to like multiple agents at a time, or even just one agent that's like orchestrating multiple agents for you.
However, we've also learned that if you start in cloud,
it can be quite hard for the developer to get value because, you know, your tools aren't there.
You've got to do an environment set up.
It's a little bit hard if like to get partial credit for a task, because like maybe if the model goes halfway, you need to like jump in and course correct or just poke at things.
So we're like, okay, we need a local experience that is separated from a specific folder, but yet feels super intuitive to work with folders on your computer.
And so when we started the app, we had a bunch of this like vibes thinking up here, like esoteric vibes thinking.
Yeah.
And then.
We had a bunch of like prototypes that random engineers had built that were just like, I wish we had an app and it was like this or that or the other.
And there was actually a hack week where like multiple independent people built different versions of apps.
You might've even built one.
I don't remember.
And so the project, when it got started, the only thing that really needed to be written down was why we thought it was a good idea to build an app.
Like there was no specific spec for the app.
And, you know, eventually we generated one by like through building.
But really, it was like quite contentious, actually, like, should we even be building an app like the IDE extension is super popular.
Should we just focus on that and improve the quality there?
What about CLI?
Like, it feels like CLIs are a thing.
Um, and then if we are building an app, like what is the point of building an app and where should we go?
So that's kind of how these things start.
Yeah.
And luckily we had a great solution with the IDE extension at the time, which we had polished quite heavily so that you can use it in like VS Code, Cursor, Windsurf and others.
And so we took a lot of the learnings and the code base from that IDE extension.
And we were able to have a great starting point that was already robust.
Yeah, yeah, actually, like the app shares a bunch of code with, well, it just shares code with the IDE extension and under the hood, both the app and the IDE extension talk to the same core codex harness in Rust that is open source and that the CLI also uses.
So there's a lot of like sharing and like very intentional, like layering of these primitives.
But the decision to build the app was, I mean, now it's kind of obvious because like, you know, just using the codex app is way easier than having a bunch of terminal windows open.
But the decision to build the app was basically, it's kind of like beginner friendly and it's kind of like, you just play with it.
It's like the best interface to manage multiple agents at the same time.
Yeah, I would say like the way that we think, like we're very much like, you know, we're very AGI built.
So we're thinking about like, what is the future that we're skating towards?
I see.
So I would actually flip the order.
It was more like, we know that we need to build an interface where it feels really natural to delegate to multiple agents because we know we're going to have models that are ready for it.
Or in fact, we're already seeing people delegating across.
So we need an interface where that feels really natural, that will scale really well to cloud.
And we want all of that to feel like ergonomic.
It shouldn't feel like, you know, you're crazily figuring something out to delegate to multiple agents at a time.
It should just feel like, obviously, that's how you want to work.
It appeals, by the way, not just to like, you know, junior developers at all.
It's quite the opposite.
Like even the most prolific, most senior engineers, even at OpenAI, from Peter from OpenCloud to like Greg Brockman.
They're now using.
They're now using the app as the primary way to build.
So this was very much just like agentic delegation vision coming to life.
And it's not just for like, oh, like the most sophisticated engineers will stay in the terminal.
They're actually moving to the app as well.
Yeah.
So hopefully so.
OK, we keep talking about Peter because he just joined OpenAI and we're like super excited, you know, again, creative OpenCloud.
But I don't know if I told you this, but yeah, I went for a walk with him in like October at Fort Mason, which is a place in San Francisco.
And I didn't like outright tell him that we were thinking about.
Building an app.
But I was like, you know, I was starting to like poke at this idea of like, you know, some kind of new interface that made delegation feel natural.
He basically told me he would never use such a thing.
And then like last weekend, he was like tweeting.
Actually, the app is pretty good.
Yep.
Hell is frozen over.
I now like it.
Yeah.
Yeah.
I thought the PRT, if you got him to use the app, that's like that's like a major accomplishment because he has like 20 terminal windows open.
So that's like a huge accomplishment.
Exactly.
I mean, I need to follow up with him.
He probably uses both, but yeah.
Yeah.
So Alex, you were like the only PM on Codex for a while, right?
Yeah.
Yeah.
Yeah.
Yeah.
How many people does close have like, you know, 50, a hundred people or it sounds about right.
Somewhere in that range.
Yeah.
Like we were, we were like eight people back in May.
Sorry.
Yeah.
Yeah.
Or something like that.
I, you know, I don't remember exactly, but, uh, we've just like grown really quickly since then.
Yeah.
Somewhere in the 50 to a hundred range is interesting.
So how do you like spend your time, dude?
Like, like, well, what was like a typical day?
Like, or is there no typical day?
Okay.
So, so in my case, um, I was thinking about this recently because.
Cause I realized that I don't know how to answer that question.
Um, and I think what I realized is that I have these like different modes that I operate in.
Um, and, uh, you know, this is not, this is not advice.
This is just me, but, uh, I think I have a mode like before, for example, we were shipping the app, which is just like straight up execution, you know, obsessing over quality, making sure we aren't like, we're looking around all the corners and like landing every little bit of thing.
Um, and that mode is like, uh, spending a lot of time in code.
And then like, oh, you know, you've got the like, like a 3d engine and like, you have a group that's like, I like I would also use codex a lot more.
Cause you know, you can go like, I use codex a lot to like understand what's happening.
Like I use codex a ton to understand, like, what is happening in Slack.
Like, what is the feedback we're getting?
I'll have codex just go and like summarize that follow up.
Most it's linear.
So there's like a lot of the, like just understanding the state of quality using code.
Um, then there's a lot of using codex to understand what the like, just things about the code.
And then using codex to make changes.
Because.
Nowadays.
It's like for a small change.
That's like not building a new system, which again, I try to avoid.
but like, you know, taking care of existing systems, it's like often faster to send a PR
that is good and you've tested than it is to like communicate to someone and get them to prioritize
that task when they have like 10,000 other things to do, because we're aiming to launch an app in
like two weeks. So there is that. And then, you know, obviously there's a lot of human side of
just like cheerleading, rallying, but also being a critic of what we're building. So that is one
mode that I've noticed. And actually you can tell if I'm in that mode, if I'm on Twitter a lot.
I don't know why, but like as we approach a launch, I tend to be on Twitter. And then there
is this other mode, which is like where, for example, like now it's like quite top of mind
for me that we are at a stage where we have these amazing models, like GPT 5.4 is incredible.
We also have this app experience that is like even more popular than we anticipated. And we
now have it on all platforms, including windows. Right. And so now in my mind, I'm like, okay,
it's time to like, really like get back to like cloud and like invest more in that.
Right. And so when,
when we enter these kinds of phases, I spend much more time like thinking about what to do
and like understanding, like what is the state of things. And so that's kind of like a coordination
mode where actually I am spending less time in Codex. Like I tend to be using Codex more for
communication and less for writing code. So I have at least those two modes. There are probably more.
Yeah. Like how much cross-functional alignment do you have to do?
Codex team is awesome. We do very little cross-functional alignment within Codex team.
We just kind of like view ourselves as like intentionally a bit of a like
pirate ship.
Like team, you know, we, even within Codex team, you know, now there's like there's me and now 2PM
has a very recently there's a few edge leads, although until very recently, like everyone just
reported to TiVo, but we kind of like all just like fuzz around together. And so there's not
too much alignment going on there, but increasingly you know, I think a large part of, of building
Codex is building this coding agent. And increasingly it's clear.
Or it's probably obvious to everyone now that a coding agent is a really generally useful thing
for other work. That's not just coding work. Like we see people using the Codex app for more than
just writing code. They're using it for tasks across the software development lifecycle. And
then now, like we actually like the vast majority of open AI uses the Codex app, even outside of
technical orgs. I just see the app app everywhere. And so, you know, that kind of thing,
realization where it's like, okay, how do we help Codex be like useful beyond just
people writing code that requires more cross-functional alignment? Because, you know, as open AI, we
have chat GPT, which many, many, many people use. So we have to be thoughtful about how
we do that.
And on my side, also developer experience, we're kind of like an extension of the Codex
team now, like we're spending most of our effort on Codex, but for a few different reasons,
one of course, it's like, it's an exciting product and like developers love using Codex
and want to make that better. And to Alex's point, like we have a few modes too, like
we are in the trenches with the Codex team to prepare the launches, to prepare the assets,
like how to make the most.
Yeah.
Of Codex and then post-launch, we try to educate developers on how to use Codex for this like
variety of ways. But the other lens for which it's very interesting to us is that when you
look at the broader open AI platform, we have like millions of developers today also building
on the API, the models using different modalities from Imagen to Sora, to speech to speech.
And guess what? The best way to build has become Codex as the entry point, right? Like
if we, if you rewind just a year ago,
or even last summer, when we introduced GPT-5, we had to write a lot of the guides around
like how you prompt GPT-5. Yes, it's a reasoning model. It's quite different from a GPT-4 model.
Well now what we try to do is like, even for those use cases, we try to teach developers
on using Codex and skills. Like for instance, if you had an integration you want to update,
you should probably use Codex and the skill and guess what? Codex will definitely take
care of that for you. So we are also very, very cross-functional and we are seeing Codex
as the cornerstone of everything for the future.
Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.
Yeah. So we've been developing that platform.
Got it.
One, one interesting thing about like how we work together is like, I mean, I think
the best part of your Codex is the community, just you know online, on the internet and
sometimes in real life.
Yeah. Yeah.
At events. Right? And we kind of just like anchor everything about that, you know?
So it's like, okay, launches, we're very launch oriented. Like when are we shipping something?
We're very feedback oriented. Like when is there feedback from the community and like,
let's fix that and like communicate that. And so we're all like quite online. And I
think like...
Yeah, like, even, for example, thinking towards the Codex app launch, we're working super closely with Dom and, like, Dom on Homa's team, like, on the next, we were, like, he was basically, like, helping us, like, coordinate, like, actually quite a wide alpha with, like, a bunch of users and, like, building with those users to get feedback, to build skills that, like, skills for the app to use at the same time and, you know, documentation, everything.
And so, you know, I think this is kind of this unique strength we have as a Codex team, again, because we are open source.
And so, kind of, like, because we're open source, we kind of just found ourselves being incredibly open about everything we do.
And I think it's really, the community really rewards it.
Yeah, dude, like, building with the users and the community is, like, the best part about BMPM.
Yeah, for sure.
It's the best part.
Just, like, talking to them every day.
Yeah, now we have, like, Codex ambassadors, even, like, in many, many, like, cities and countries who are kind of, like, spinning up their own events to kind of teach their own communities locally, because I would love to be in every city, but we cannot be.
But it's amazing to see, like...
Like, the energy and the enthusiasm from the community to, like, set up these events, these hackathons, and, like, build together.
This is awesome.
Yeah, make me an ambassador.
I'll throw some events.
Yeah, that sounds good.
All right, we should bet.
All right, so you've signed up.
So let's talk about Peter a little bit.
So I'm, like, an early adopter of OpenClaw, and it's a little bit janky, but, like, it's done so many things for me.
Like, the other day, because it has memory of our conversations, it gave me, like, a very vulgar pep talk for, like, three minutes.
And it was, like, the most insightful thing that I've ever heard from AI.
So, like, how are you guys integrating Peter into the team and, like, you know, this, like, personal agent vision?
Is that part of, like, what Codex is doing?
Or, yeah, how do you think about that?
Two things there.
I mean, I can only share so much here.
But the first thing is that he is a ultra, ultra power user of Codex.
And, like, you know, OpenClaw was very much built with Codex.
And so he is just, like, energizing the team with, like, feedback.
And, like, basically work to, like, help improve Codex.
That's his side job, but he is doing it, and we're really excited about it.
And the other stuff that I can't share super much about yet, but he's, like, really just, like, helping us build, like, the next generation of personal agents.
But, like, into ChatGPT.
Yeah, that makes sense, dude.
Yeah.
What I find fascinating about what Peter has done is, like, obviously, like, I've known Peter for a while.
And everybody has, like, seen this glimpse of the future when they start to play with OpenClaw.
Yeah.
But what I find amazing is, like, Peter.
I've seen this vision for quite some time.
And if you rewind all of 2025, he has built more than 40 open source projects last year.
But all of them kind of aligned with one vision, which was, I need a command line interface to access my calendar.
I need a command line interface to access my tweets and my Gmail.
And by building all of these projects, he effectively made, like, you know, this vision manifest around this idea of skills and command line tools that we use coding agents for.
And by building all of these projects, he effectively made, like, you know, this vision manifest around this idea of skills and command line tools that we use coding agents for.
And by building all of these projects, he effectively made, like, you know, this vision manifest around this idea of skills and command line tools that we use coding agents for.
And it's not going to be just coding agents.
It's going to be, like, any kind of personal agents.
And so, Peter is going to be fantastic at giving us feedback along the way for having built all of these tools that are now part of the OpenClaw ecosystem.
Yeah.
I'm, like, great.
Like, he's just one person.
He built this awesome open source community.
And, yeah, it's, like, made it, like, it's made me not want to open any other app anymore.
I just talked to my little bot.
So, it's a huge difference.
What do you have it connected to?
Do you have it connected to everything?
I have it, too.
I have it connected to many things, man.
Like, it has my bank information.
It has, like, my YouTube information.
It has, like, voices that I've activated, my calendar, my Google stuff.
And, yeah, like, yeah, like, my, you know, when I'm in bed at night, like, my wife is, like, who are you talking to?
I'm, like, I'm talking to my OpenClaw bot, you know?
Yeah, it's giving me ideas.
Yeah.
Yeah.
Yeah.
But, like, it is true that there's a lot of, like, grifters out there charging $5,000 to set up OpenClaw.
So, like, yeah, if you guys can make it, like, mass market friendly, that's going to be huge, you know?
So.
You're on it.
We'll report back.
Yeah.
Yeah.
Okay.
Well, let's wrap up and talk about, like, some of your hot takes, Alex.
Like, and maybe I'm making this shit up, but, like, I believe you said something about, like, how most teams don't need that many PMs anymore or something like that.
Well, let's make it.
Let's make it spicier.
What do you think, man?
Do we need PMs?
I think what I find amazing with these tools is that, like, it's not even just PM or no PM.
In my view, it's, like, almost, like, every career ladder is starting to blur.
You know?
It was, like, you have a designer here.
You have an engineer here.
You have a designer, like, a PM here.
And maybe you have a ratio of sorts.
It's, like, the golden ratio of all.
But, like, now if you're an engineer, sure, you're, like, more productive.
But if you're a designer, you have some superpowers to, like, become more technical.
If you're a PM and all you did before was, like, writing strategy docs, well, now you can just prototype.
It doesn't mean that you have to be responsible of that feature for billions of users.
But sure enough, you can show your team a glimpse of that vision by, like, actually, like, building it.
And so I think, like, that's what I find fascinating to me.
It's, like, all of the lines between career ladders are blurring.
And we're all builders all together.
Yeah.
That resonates.
Yeah.
Okay.
So I think I don't think I'm trying to remember, like, what have I said?
I feel like it's somewhere on the internet.
I said that I think it's a red flag if a startup has a PM when it's, like, less than, like, 20 engineers or something.
Maybe.
Maybe I said that.
I think, like, kind of like what you said, like, all these roles are blurring together.
Right.
Like, a designer can do more engineering.
An engineer can do more design.
A PM can do more building.
But, you know, also engineers.
Often they need to be focused.
Right.
So a lot of why they aren't, like, I don't know, triaging tasks or doing some other kind of, like, the project management side of PMing might be because they just need to spend time coding.
But now that that's really easy, you can just ask an agent like Codex to, like, go, like, analyze the feedback and prioritize.
You have more time.
And so I think everyone's able to do everyone else's jobs.
And, like, Scott Belsky has this idea of, like, collapsing the talent stack.
Yeah.
I like that idea.
I think it is happening.
I think the fewer people you need in a room to do anything, just the better that thing goes, the more pure every decision is.
Yeah.
So then the question is, like, well, what is left for PMs?
And I think that there are many PMs who should actually convert roles.
Right.
Like, if you're a PM who kind of just, like, always wanted to be an engineer, but maybe you were very good at managing people, but you were, like, not that good at engineering, like, maybe now you should become an engineering manager.
You know, and with a coding agent, like, that's fine.
And maybe that's just a cleaner role for you.
I think there's an analogous version where, like, a different PM might just want to be a designer.
You know, just be closer to building.
But I think ultimately what it comes down to is interest.
I think interest and agency are, like, the most fundamental qualities that remain important for humans in a world with AGI.
And so for me, that's kind of what I end up thinking about.
Like, if you fundamentally are more interested in writing code and, like, you just did PM work because it was, like, someone needed to do it, now you should be, delete yourself and become an engineer and just do the same thing from an engineering standpoint.
Same for design.
But if you are, like, fundamentally.
Like, most interested in, like, spending a lot of time with users, even if it takes you away from building, right?
Or, like, trying to look around corners and understand where the market is going, et cetera.
And if you are on a large enough team where there's already enough engineers, then I think maybe there's still room for a PM there.
But, yeah, I think it really comes down to, like, what are you most interested in?
Okay, and maybe I'll add one thing, which is, like, I still think every problem needs a human that's accountable for the problem.
But I just don't think that human has to be a PM.
Yeah, and I think it depends a ton, like, what you said on the nature of the product, right?
Because we're lucky enough here to work on Codex, which is very much like a builder-developer product.
And we are the best users ourselves, and we pair with the community thanks to this open source thing.
But even if you rewind, like, a decade, when I was at Stripe, like, Stripe reached 250 employees with zero PMs, even without any AI tool.
Why?
Well, Stripe was just an API.
And, like, we were all engineers.
And we knew.
We knew what a great, like, API would look like.
So we were building the API we always dreamed about, right?
Like, we wanted Stripe to be so elegant, just with your lines of code.
If you're working in a different field and you want to carry that customer obsession, you know, you may need more PM time to spend time with customers when the vertical or the industry, the space, the problem space is different.
We're lucky here to work on Codex and kind of, like, building the tool we've always wanted to have.
So, yeah, but, like, let's say, you know, this example where it's, like, maybe, you know, it's a it's a field or the product is serving users that engineers have less intuition for, like, PM is just a label for, like, someone who can design and code is most interested in users, is very interested in users, you know what I mean?
You can equally well have an engineer who's very interested in users.
So I think these labels are kind of losing their meaning a little bit, but but that's okay for now.
It's, like, it's just a bit messy.
Yeah.
That's what I find on my team, too.
I feel like the best engineers.
Like, like, the best engineers don't ask me, like, hey, Peter, what should we build next?
Like, they go off and talk to users and figure out what to build, like, that we have a conversation about it.
It's like, it's kind of like everyone's on the same page around the stuff, you know?
That's how the Codex team works a lot, right?
Like, so many features that are, like, that you're using today with the Codex app came from great ideas from engineers, completely bottoms up because they wanted the feature for themselves.
Yeah, but I mean, I would say, I don't know, like, I think, okay, there's a very strong profile of engineer that I love working with who just, like, loves, like, hanging out with users and thinking about what to build.
They're equally well, incredibly strong profiles of engineers who just, like, are insanely fast, insanely good at building systems and thinking them through and, like, have zero interest in hanging out with users.
And I think there's plenty of room for those people, too, right?
For sure.
Like, again, that's, like, kind of my view of, like, this world with AI is we can all just become more opinionatedly ourselves, you know what I mean?
Like, be yourself, like, AI and the team around you maybe will, like, just, like, fill in your, you know, what you don't want to do.
That's a great way to put it.
Dude, but I do think, like, the builder.
Label is very important.
Like, I feel like every PM wants to be a leader and, like, dude, the traditional career ladder is just, like, you become, like, this VP or something and then you don't have time to build anymore, man.
You're just, like, in product reviews all day, like, just, like, giving some feedback here and there.
And I feel like a lot of PMs don't want that, dude.
Like, I don't know if you want it, but, like, I want to stay close to the users as you actually ship.
Yeah. Totally.
Yeah, I mean, I don't actually view PM as a good leadership position.
I view it as a fill in the gaps position occasionally that might require leadership.
Although even then, the leadership is probably just, like, helping people get aligned and less, like, being some genius who came up with the right strategy.
Yeah.
I will say one thing for sure.
Like, the best PMs at OpenAI are incredibly in the weeds.
And I think joining OpenAI in a senior leadership position is, like, very challenging because it's actually still important to be in the weeds.
So you somehow need to find time for, like, you know, a senior leadership, but also how to get in the weeds at the same time.
So always better, I think, here to join.
Directly in the weeds.
Yeah.
Yeah.
Okay.
Cool.
Last question, man.
So you finally hire another PM.
I think his name is Rohan or something.
Right.
And, like, what kind of qualities do you guys look for when recruiting people to the Codex team?
You know, other than being Codex power users, like, what kind of qualities?
Yeah.
Let's both take this.
Yeah.
I think, I mean, look, I said it before.
I'm going to go back to agency.
Like, people who do things is, like, literally the most important thing.
Like, OpenAI.
Also, especially in the industry.
Codex team.
Like, we're intentionally not a team where, like, you're going to join and it's going to be, like, hey, here's, like, 12 tasks to do in increasing order of difficulty and, like, go for it.
It's going to be more, like, welcome.
Okay.
That's just it.
It's, like, welcome.
You know?
Yeah.
So I think people who are self-starters and do things and have, like, energy and ideas for what to be done and don't mind disagreeing with the existing ideas because they're probably wrong because we probably made those decisions by accident.
Yeah.
And who will, like, now I'm just describing, like, perfect teammate, right?
Who will, like, absorb, like, any incremental, like, scope or accountability for things that are unknown I think is ideal.
So, like, that is sort of the broad meta things.
And I think if you're trying to think about what role makes the most sense, like, anything technical, engineering.
Yeah.
Agreed.
And on my side, like, on developer experience, what I'm looking for is usually, like, people who have high agency, obviously very technical, obviously mastering the tool like Codex.
But I also have this, like, passion for, like, spending time with developers and builders and, like, sharing their knowledge, you know?
Yeah.
We just announced this week, for instance, that, like, Thomas who built the open source Codex monitor is going to join my team this month.
And it's great because someone who's, like, very creative, very prolific with Codex but also loves sharing how he's building with it, you know?
And it's kind of, like, we need to bring millions of developers to this bright future of Codex.
I think, like, agentic coding is changing everything in terms of, like, how we've been always reflecting on how we build software and build apps and products.
Yeah.
And there is so much potential to show the world, like, that anyone can build anything and, like, teach them along the way.
So, that's kind of, like, what I'm looking for.
Let me know if this is wrong.
In my head, the role description for DevEx is, like, very good engineer who is also very good at Twitter.
Yeah.
You can do that.
Okay.
I got half of that.
I got half of that.
I mean, it's basically that.
With the little asterisk I would add, which is that, like, Twitter is, like, outstanding for our communities here.
And when you travel in some parts of the world, some developers are not as much on there, like in Europe and some other places.
They use LinkedIn or they use some other places.
So, we just have to have this little asterisk of, like, thinking about the worldwide developers.
Good on socials.
Okay.
But good on socials for sure.
Yeah.
And love spending time teaching and educating.
Yeah.
And I feel like agency, you can kind of tell even before they go through the interview process, right?
Like, are they shipping stuff online?
Exactly.
Do they have, like, side projects?
So, like, when someone DMs me, like, you know, interest in, like, working together, for me, it's, like, is there a link?
If there's a link, I always click it.
Like, you know, I guess maybe I look to see if it's, like, a bad link.
I pretty much always click it.
I'm always curious.
And then if there's, like, some spiel with ideas, I usually always read that.
And then I don't know.
I don't know how bad or toxic this is going to sound.
But if it's, like, some explanation of, like, why they're interested in the role and, like, you know, their CV and stuff, like, I'm much less likely to read that than, like, their ideas and what they've built, you know?
And then I never.
Someone asked me this the other day, and I realized, like, I had no idea where, like, people went to college.
Who cares, man?
Yeah.
Who cares?
I'm so glad we live in a world where all these stupid credentials don't matter anymore.
Who cares?
Fan, college.
Just, like, show me what we built.
Yeah.
Cool, guys.
Well, thanks so much, man.
I love Codex.
And, yeah, I'm going to Viper a bunch of stuff this weekend.
It should be good.
Great.
Have fun.
Don't wait to see your feedback.
Thank you so much, Peter, for having us.
All right, guys.
Thanks.
