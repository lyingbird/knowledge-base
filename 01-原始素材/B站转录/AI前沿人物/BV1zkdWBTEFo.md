---
title: "OpenAI团队：OpenAI的 Harness工程实践"
platform: bilibili
bvid: BV1zkdWBTEFo
author: Easonlee的AI笔记
pubdate: 20260419
duration_sec: 4673
view: 3188
like: 91
url: https://www.bilibili.com/video/BV1zkdWBTEFo
subtitle_source: faster-whisper_large-v3
asr_model: large-v3
transcript_chars: 79063
crawl_time: 2026-07-12
---

# OpenAI团队：OpenAI的 Harness工程实践

## 视频信息

- **UP主**: Easonlee的AI笔记
- **时长**: 1h17m
- **链接**: https://www.bilibili.com/video/BV1zkdWBTEFo

## 视频描述

大家好，我是Easonlee，做自己和AI的CEO。

《AI Builder》专栏，分享一线AI创始人的实践和思考。AI时代，让我们关注Builder，成为Builder。

原始视频发布时间：2026-04-08

导读：本期嘉宾是 OpenAI Frontier 团队的 Ryan Lopopolo，他分享了如何在 5 个月内通过 AI 代理构建出百万行代码的复杂产品。他提出“人类是唯一稀缺资源”的观点，主张通过构建极高密度的自动化脚手架，让 AI 彻底接管从编码、测试到运维的全生命周期。

1. 设定零人工代码的极端约束 [07:12]
Ryan 在项目初期强制要求团队不写一行代码，仅通

## 完整文稿

> 来源: faster-whisper large-v3 (CUDA/fp16)

I do think that there is an interesting space to explore here with Codex,
the harness as part of building AI products, right?
There's a ton of momentum around getting the models to be good at coding.
We've seen big leaps in the task complexity with each incremental model release,
where if you can figure out how to collapse a product that you're trying to build,
a user journey that you're trying to solve into code,
it's pretty natural to use the Codex harness to solve that problem for you.
It's done all the wiring and lets you just communicate in prompts to let the model cook.
You kind of have to step back, right?
Like, you need to take a systems thinking mindset to things
and constantly be asking, where is the agent making mistakes?
Where am I spending my time?
How can I not spend that time going forward?
And then build confidence in the automation that I'm putting in place
so I have solved this part of the SDLC.
Before we get into today's episode, I just have a small message for listeners.
Thank you.
We will not be able to bring you the AI engineering, science, and entertainment contents
that you so clearly want if you didn't choose to also click in and tune into our content.
We've been approached by sponsors on an almost daily basis,
but fortunately enough of you actually subscribe to us
to keep all this sustainable without ads.
And we want to keep it that way.
But I just have one favor to ask all of you.
The single most powerful, completely free thing you can do,
is to click that subscribe button.
It's the only thing I'll ever ask of you.
And it means absolutely everything to me and my team
that works so hard to bring the InSpace to you each and every week.
If you do it, I promise you, we'll never stop working to make the show even better.
Now let's get into it.
All right, we're in the studio with Ryan Lopopolo from OpenAI.
Welcome.
Hi.
Thanks for visiting San Francisco and thanks for spending some time with us.
Yeah, thank you. I'm super excited to be here.
You wrote a blockbuster article on harness engineering.
It's probably going to be...
It's going to be the defining piece of this emerging discipline.
Thank you.
It's been kind of fun to feel like we've defined the discourse in some sense.
Let's contextualize a little bit.
This first podcast you've ever done.
Yes.
And thank you for spending it with us.
Where is this coming from?
What team are you in?
All that jazz.
Sure, sure, sure.
So I work on Frontier product exploration,
new product development in the space of OpenAI Frontier,
which is our enterprise platform for deploying agents,
specifically at scale with good governance in any business.
And the role of me and my team has been to figure out novel ways
to deploy our models into package and products that we can sell as solutions to enterprises.
And you have a background, I'll just squeeze it in there.
Snowflake, Brex, Stripe, Citadel.
Yes, I've been building the exact kind of customer my entire life.
Yes, the exact kind of customer that you want to.
So I'll say I was actually I didn't expect the background when I looked at your Twitter.
I'm seeing the opposite.
Right.
Stuff like this.
So you've got the mindset of like full send AI coding,
stuff about slop, like buckling in your your laptop on your Waymo's.
And then I look at your profile.
I'm like, oh, you're just like you're cracked in the other room.
Perfect mix, perfect mix.
It's quite fun to be AI maximalist.
If you're going to live that persona, OpenAI is the place to do it.
And it's a token is what you say.
Yeah, it certainly helps that we have no
rate limits internally and I can go, like you said, full send at this thing.
Yeah, yeah.
So so the OpenAI Frontier and your special team within OpenAI Frontier.
We had been given some space to cook, which has been super, super exciting.
And this is kind of why I started with kind
of a out there constraint to not write any of the code myself.
I was figuring if we're trying to make
agents that can be deployed into end enterprises, they should be able to do all
the things that I do and having worked with these coding models, these coding
harnesses over six, seven, eight months.
I do feel like the models are there enough.
The harnesses are there enough where
they're isomorphic to me and capability and the ability to do the job.
So starting with this constraint of I can't write the code meant that the only
way I could do my job was to get the agent to do my job.
And like just a bit of background before that, this is basically article.
So what you guys did is five months of working on an internal tool, zero lines of
code over a million lines of code in the total code.
You say it was Cenex more like it was
Cenex faster than you would have if you had done it by hand.
So that was kind of the mindset going into this, right?
That's right.
That's right.
Started with some of the very first versions of Codex CLI with the Codex mini
model, which was obviously much less capable than the ones we have today,
which was also a very good constraint, right?
It's quite a visceral feeling to ask the model to build you a product feature and
it just not being able to assemble the pieces together.
Which kind of defined one of the mindsets we had for going into this,
which is whenever the model just cannot, you always pop open the task,
double click into it and build smaller building blocks that then you can
reassemble into the broader objective.
And it was quite painful to do this.
Honestly, the first month and a half was ten times slower than I would be.
But because we paid that cost, we ended up getting to something much more productive
than any one engine.
Year could be because we built the tools,
the assembly station for the agent to do the whole thing.
But yeah, so onward to GPT-5, 5.1, 5.2, 5.3, 5.4 to go through all these model
generations and see their kind of quirks and different working styles also meant we
had to adapt the code base to change things up when the model was revved.
One interesting thing here is 5.2, the Codex harness at the time did not have
background shells in it.
Which means we were able to rely on blocking scripts to perform long horizon
work, but with 5.3 and background shells, it became less patient, less willing to block.
So we had to retool the entire build system to complete in under a minute.
And this is not a thing I would expect
to be able to do in a code base where people have opinions.
But because the only goal was to make the agent productive over the course of a
week, we went from a bespoke make file build to Bazel to Turbo to NX and just kind
of left it there because builds were fast at that point.
Interesting. Talk about Turbo to NX.
That's interesting because that's the other direction that other people have been doing.
Ultimately, I have not a lot of experience with actual front end repo architecture.
You're talking about JavaScript builds, so I'm like, I know the NX team.
I know Turbo from Jared Palmer.
And I'm like, yeah, that's an interesting comparison.
The hill we were climbing, right?
It was make it fast.
Is there a micro front end involved?
How complex?
React, Electron, single app sort of thing.
And it must be under a minute.
That's an interesting limitation.
I'm actually not super familiar with the background shell stuff.
Probably was talked about in the 5.3 release.
It basically means that Codex is able to
spawn commands in the background and then go continue to work while it waits for
them to finish so it can spawn an expensive build and then continue.
So it's like, oh, I'm going to have to go back to reviewing the code, for example.
And this helps it be more time efficient for the user invoking the harness.
I guess, like, just to really nail this, like, what does one minute matter?
Like, why not five, you know?
We want the inner loop to be as fast as possible.
One minute was just a nice round number and we were able to hit it.
And if it doesn't complete, it kills it or something?
Oh, no, we just take that as a signal that we need to stop what we're doing.
Double click.
To get the time back under so that we can
enable the agent to continue to operate.
It's almost like it's like a ratchet.
It's like a forcing build time discipline,
because if you don't, it'll just grow and grow and grow.
That's right.
And you mentioned that the software I work on currently is at 12 minutes.
It sucks.
This has been my experience with platform teams in the past, right?
Where you have sort of an envelope of acceptable build times and you let it go
up to breach and then you spend two, three weeks to bring it back down to the lower
end to be able to load and stop.
But because tokens are so cheap and so insanely parallel with the model,
we can just constantly be gardening this thing to make sure that we maintain these
invariance, which means there's way less dispersion in the code and the SDLC,
which means we can kind of simplify in a way and rely on a lot more invariance
as we write the software.
You kind of mentioned in your article, like humans became the bottleneck, right?
You kicked off as a team of like three people.
You're putting out a million line of code, like fifteen hundred PRs.
Basically, what's the mindset there, right?
So as much as code is disposable, you're doing a lot of review.
A lot of the article talks about how you want to rephrase.
Everything is prompting.
Everything is what the agent can't see.
It's kind of garbage, right? You shouldn't have it in there.
So what's kind of like the high level of how you went about building it and then
how you address like, OK, humans are just kind of PR review.
Like, how is human in the loop for this?
You know, we've moved beyond even the humans reviewing the code as well.
Most of the human review is.
Well, post-merge at this point, but
that's not even review.
That's just like, oh, let's just make ourselves happy by giving use.
Fundamentally, the model is trivially paralyzable, right?
As many GPUs and tokens as I am willing
to spend, I can have capacity to work on the code base.
The only fundamentally scarce thing is the synchronous human attention of my team.
There's only so many hours in the day.
We have to eat lunch.
I would like to sleep, although it's quite
difficult to stop poking the machine because it makes me want to feed it.
You kind of have to step back, right?
Like you need to take a systems thinking
mindset to things and constantly be asking, where is the agent making mistakes?
Where am I spending my time?
How can I not spend that time going forward and then build confidence
in the automation that I'm putting in place?
So I have solved this part of the SDLC.
And usually what that has looked like is like we started.
You need to pay very close attention to the code because the agent did not have
the right building blocks to produce modular software that decomposed
appropriately, that was reliable and observable and actually accrued a working
front end in these things, right? So in order to not spend all of our time
sitting in front of a terminal, at most doing one or two things at a time,
invested in giving the model that observability, which is that that graph
in the post here.
Yeah.
That's true.
Which existed first?
We started with just the app and the whole rest of it from Vector through to all
these log and metrics APIs was, I don't know, half an afternoon of my time.
We have intentionally chosen very high level, fast developer tools.
There's a ton of great stuff out there now.
We use Mies a bunch, which makes it trivial
to pull down all these Go written Victoria stack binaries in our local development.
So we have a tiny little bit of Python glue to spin all these up and off you go.
One neat thing here is we have tried to invert things as much as possible,
which is instead of setting up an environment to spawn the coding agent
into, instead we spawn the coding agent like that's the entry point, just codecs.
And then we give codecs via skills
and scripts the ability to boot the stack if it chooses to and then tell it how
to set some end variables so the app and local dev points
at the stack that it has chosen to spin up.
And this, I think, is like the fundamental
difference between reasoning models and the four ones and four of the past where
these models could not think so you kind of had to put them in boxes with a
predefined set of state transitions, whereas here we have the model,
the harness, be the whole box and give it a bunch of options for how
to proceed with enough context for it to make intelligent choices.
So feels like a lot of that is around scaffolding.
Right.
Yes. Previous agents, you would define a scaffold.
It would it would operate in that loop.
Try again.
That's kind of pivoted off from when we've had reasoning models.
They're seeming to perform better when you don't have a scaffold.
And you go into like niches here to like
your spec.md and like having a very short agent.md, agent.md.
Yes. Yeah.
So you even lay out what it is here.
But I like the table of contents.
Yeah. Stuff like this, it really helps guide people
because everyone's trying to do this.
This structure also makes it super cheap to put new content into the repository
to steer both the humans and and the agents.
I mean, you kind of reinvented skills, right?
One big agent.
Skills from first principles.
Skills did not exist when we started doing this, right?
You have a short 100 line overall table
of contents and then you have little skills, right?
Core beliefs, MD, TechJet tracker.
Yeah. Yeah.
Yeah. So the skill is over there.
The TechJet tracker and the quality score are pretty interesting.
Because this is basically a tiny little
scaffold, like a Markdown table, which is a hook for Codex to review all
the business logic that we have to find in the app, assess how it matches all
these documented guardrails and propose follow up work for itself.
So, you know, before Deeds and all these
ticketing systems, we were just tracking follow up work as notes in a Markdown
file, which, you know, we could spawn an agent on a cron to kind of burn down.
There's this really neat thing that like
the models fundamentally crave text.
So a lot of what we have done here is
figure out ways to inject text into the system, right?
When we get a page because we're missing a timeout, for example, I can just add
Codex in Slack on that page and say, I'm going to fix this by adding a timeout.
Please update our reliability
documentation to require that all network calls have timeouts.
So I have not only made a point in time
fix, but also like durably encoded this process knowledge around what good looks
like and we give that to the root coding agent as it goes and does the thing.
But you can also use that to distill tests out of or a code review agent,
which is pointed out the same things to narrow the acceptable universe
of the code that's produced.
I think one of the concerns I have with that kind of stuff is like you think
you're making the right call by making it persisted for all time across everything.
Yes.
But then you didn't think about the exceptions that you need to make.
Right. And then you have to roll it back.
Part of it is also.
Sometimes you can follow instructions too well.
It's somewhat a skill, right?
So it determines when it uses the tools, right?
Like it's not it's not like it'll run every call.
It'll determine when it wants to check quality score.
Right. Yeah.
And we do kind of in the prompts we give these agents allow them to push back.
When we first started adding code review agents to the PR, it would be
Codex CLI locally writes the change and pushes up a PR on those PR
synchronizations, a review agent fires, it posts a comment.
We instruct Codex that it has to at least acknowledge and respond to that feedback.
And initially the Codex driving the code
author was willing to be bullied by the PR reviewer, which meant you could kind
of end up in a situation where things were not converging.
So we kind of had to thrash.
We kind of had to add more optionality to the prompts on both of these things.
Right. Like the reviewer agents were instructed
to bias toward merging the thing to not surface anything greater than a P2 in priority.
We didn't really define.
P2, but we we gave it to find P2.
We gave it a framework within which to score its output.
And then greater than P0 is worse.
Right. Yes.
P2 is P0 is you will like code place if you merge this thing.
Right. Yeah.
But also on the on the code authoring agent side, we also gave it the flexibility
to either defer or push back against review feedback.
Right.
This happens all the time, right?
Like I happen to notice something and leave a code review.
Which could blow up the scope by a factor of two, right?
I usually don't mean for that to be addressed exactly in the moment.
It's more of an FYI, right?
File it to the backlog, pick it up in the next fix it week sort of thing.
And without the context that this is permissible,
the coding agents are going to bias toward what they do, which is following instructions.
Yeah, I do want to check in on a couple of things, right?
Like all the coding review agent, it can merge autonomously.
Mm hmm.
I think that's something that a lot of
people are comfortable with, right?
And you have a list here of how much agents do.
They do product code and tests,
CI configuration and release tooling, internal dev tools, documentation,
eval harness, review comments, scripts that manage the repository itself,
production dashboard definition files, like everything.
Yes. And so they're just all churning at the same time.
Is there like a record that any human on the team pulls to stop everything?
So because we are building a native
application here, we're not doing continuous deployment, right?
So there is still a human in the loop for
cutting the release branch.
We require a blessed human approved smoke
test of the app before we promote it to distribution, these sorts of things.
So you're working on an app.
You're not building like infrastructure
where you have like nines of reliability, that kind of stuff.
That's correct. That's correct.
OK.
And also like full recognition here that all of this activity took in a completely
greenfield repository, like there should be no assurance that this applies generally
to like this is a production thing you're going to ship to customers.
Of course. Yeah, of course.
You know, so this is real.
And like one of the things there, as you mentioned, you started this as a repo
from scratch, the onboarding first month or so was pretty it was like working
backwards, right, and you had to work with the system.
And now you're at that point where, you know, you're very autonomous.
I'm curious, like, OK, so what how human in the loop is it?
Right. So like what are the bottlenecks that you wish you could still automate?
And part of that is also like, where do you see the model trajectory improving
and offloading more human in the loop? Right.
We just got five point four.
It's a really fantastic.
Model, by the way. Yeah.
Yeah. It's the first one that's merged
top tier coding, so it's codex level coding and reasoning.
So general reasoning both in one model.
Right. So. And computer use.
Computer use.
Now whatever. Now with 5.4, I can just have codex write the blog post.
Whereas for this one, I had to balance between chat and codex.
I might be out of a job.
Oh, my God.
I know you just gave me an idea for a completely AI newsletter that like 5.4 could do.
Yeah.
I get it now.
This sort of thing is just one example of closing the loop, right?
Like the dashboard thing you mentioned.
We have codex authoring the JSON for the Grafana dashboards and publishing them
and also responding to the pages, which means when it gets the page,
it knows exactly which dashboards are defined and what alerts,
what alert was triggered by which exact log in the code base.
Because all of this stuff is collated together.
It has to own everything. Yes.
Yes. Yeah.
Yeah.
It means that if we have an outage that did not result in a page,
it has the existing set of dashboards available to it.
It has the existing set of metrics and logs and can figure out where the gaps
in the dashboard are or in the underlying metrics and fix them in one go.
In the same way, you would kind of have a full stack engineer be able
to drive a feature from the back end all the way to the front end.
So it seems like a lot of the work you guys had to do was you as a small team are
fully working for a way that the model wants
the software to be written, right?
It's less human legible for better code legibility, agent legibility.
How do you think that affects broader teams?
So one at OpenAI, like, do you liaison like this is how software should be written?
Like I can imagine, say you join a new team with this methodology, this mindset.
There's ways that, you know, teams do code review, teams write code,
like teams are structured and a lot of it is for human legibility.
It's like, should we all swap?
Like, how does this play back one broader
into OpenAI and then like broader into the software engineering?
Like, is it like teams that pick this up?
Like, you know, it's pretty drastic, right?
You have to make a pretty big switch.
Should they just full send?
Like, yeah, the mindset is very much that I am removed from the process.
Right. I can't really have deep code level opinions about things.
It's as if I'm group tech leading a 500 person organization.
Like, yeah, like it's not appropriate for me to be in the weeds on every PR.
This is why that post merge code review thing is like a good analog here, right?
Like I have some representative
example of the code as it is written, and I have to use that to infer
what the teams are struggling with, where they could use help,
where they're already moving quickly and I can pivot my focus elsewhere.
So I don't really have too many opinions around the code as it is written.
I do, however, have like a command based class, which is like used to have
repeatable chunks of business logic that comes with tracing and metrics
and observability for free. Right.
And the thing to focus on is not,
how that business logic is structured, but that it uses this primitive because I
know that's going to give leverage by default.
Yeah. Back to that sort of systems thinking.
And you have part of that in your blog
posts, enforcing architecture and taste, how you set boundaries for what's used.
There's also a section on like redefining engineering and stuff.
But yeah, it's just it's interesting to hear, you know.
And, you know, as the models have gotten better, they have gotten better at
proposing these abstractions to unblock themselves, which again, lets me move higher
and higher up the stack to look deeper into the future on what ultimately block
the team from shipping. Yeah.
You mentioned so this is primarily is like a one million line of code code
based Electron app, but it manages its own services as well.
So it's like a back end for front end type thing.
We do have like a back end in there, but that's hosted in the cloud.
Yeah. This sort of structure is actually
within the separate main and renderer processes within the Electron.
That's just how Electron works.
Yeah, yeah, yeah.
So like like have also treated like
MVC style decomposition with the same same level of rigor, which has been very fun.
I have a fun pun.
This is a tangent, but, you know, MVC is
model view controller that any sort of full stack web dev knows that.
But my AI native version of this is model view claw.
Claws the harness.
That's right. That's right.
I do think that there is an interesting space to explore here with Codex,
the harness as part of building AI products, right?
There's a ton of momentum around getting the models to be good at coding.
We've seen big leaps in like the task
complexity with each incremental model release, where if you can figure out how
to collapse a product that you're trying to build, a user journey that you're
trying to solve into code, it's pretty natural to use the Codex
harness to solve that problem for you. It's done all the wiring and lets you
just communicate and prompts to let the model cook.
Yeah, it's been very fun.
And it's also like a very engineering legible way of increasing.
It's very plastic, right?
Yeah, just give you just give the model
scripts the same scripts you would already build for yourself.
Yeah. Yeah.
So for listeners, this is Ryan saying that software engineering or coding agents
will eat knowledge work like the non coding parts that you would normally think, oh,
you have to build a separate agent for it. No.
Start with a coding agent and go out from there, which OpenClaw has.
It's a pioneerhood.
Yes.
Basically define your task in code.
Everything is a coding agent.
By the way, since I brought it up, it's probably the only place we bring it up.
Is there any OpenClaw usage from you?
No, no, not for me.
I don't have any spare Mac minis rattling around my house.
You can report it.
No, I just I'm kind of curious if it's like
changed anything in OpenAI yet, but it's probably early days.
And then, you know, the other thing I want to pull on here is like you mentioned
ticketing systems and you mentioned PRs, and I'm wondering if both those things have
to go away or be reinvented.
But for this kind of coding, right.
So the Git itself and is like very hostile to multi-agents.
Yeah, we make we make very heavy use of work trees.
All right. But like even then, like I just did a job
to podcast yesterday with Cursor saying they said they're getting rid of work
trees because it still has too many merge conflicts.
It's still too unintuitive.
But go ahead.
The models are really great at resolving merge conflicts.
And to get to a state where I'm not
synchronously in the loop in my terminal.
I almost don't care that there are merge conflicts.
Disposable. Right.
Yeah. We invoke a dollar land skill and that
coaches Codex to push the PR, wait for human and agent reviewers,
wait for CI to be green, fix the flakes if there are any
merge upstream, if the PR comes into conflict, wait for everything to pass,
put it in the merge queue, deal with flakes until it's in main.
And this is kind of what it means to delegate fully.
Right. Like this is this is, you know,
very large model repo, probably a significant tax on humans to get PRs merged.
But the agent is more than capable of doing this.
And I really don't have to think about it other than keep my laptop open.
Yeah,
I used to be much more of a control freak, but now I'm like, actually,
you could do a better job at this than me. Yeah.
With the right context. Yes.
Anything else in HarnessEng in general, just this piece, I just want to make sure we
I think one thing that I maybe didn't make super clear in the article that I
kind of heard on Twitter as an interest that's respond to them was the chatter.
And then what's your response?
Ultimately, all the things that we have encoded in docs and tests and review
agents and all these things are ways to put all the non-functional requirements of
building high scale, high quality, reliable software into a space that prompt injects.
They should either write it down as docs.
We add links where the error messages
tell how to do the right thing.
So the whole meta of the thing is to basically tease out of the heads of all
the engineers on my team what they think good looks like, what they would do by
default or what they would coach a new hire on the team to do to get things to merge.
And that's why we pay attention to all the mistakes, mistakes that the agent makes.
Right.
This is code being written that is misaligned with some as yet not written
down.
And that's what we're trying to do in this environment.
Sorry, what did the online people misunderstand or.
No, what do you respond to?
Somebody just literally said that I was like, oh, yeah, OK, this this is this is the thing.
This is what I've been doing.
I see. I see. Interesting.
What other neat thing, which I totally did not expect, is folks were just taking the
link to the article and giving it to like Pi or Codex and say, make my repo this.
You can achieve a whole recursion.
It was wildly effective.
No way.
Just actually is something I tried with 5.4 yesterday.
I didn't have that much time.
I was like out speaking at something and this is one of my things.
I was like, OK, I have this article.
Can we can we just like scaffold out what it would be like to run this?
And I did it first as that.
And then I was like, OK, let me take another little side repo and say, like,
OK, if I was to fully automate this like this, because I haven't written a line of
code, it's like a whole set of the side thing I'm doing with like voice TTS.
I'm just like slobbing out, whatever.
It's nothing production.
I'm like, how would I make this?
Like this? And it's it's actually like a really good way.
It's like a good way to learn what could be changed.
What could be like it's just a good analyzing.
Right. You give it all the code.
You give it all the context, you give it the article and it walks you through it
very well. That's right. That's right.
I guess one more thing before we go to
Symphony is I wanted to cover Brett Taylor's response.
We had him on the on the show.
He is your chairman, which is a while.
Yeah,
that he's reading your articles as well and like getting engaged in it.
He says software dependencies are going away.
Basically, they can just be like vendored.
Yes.
Response.
A hundred percent, a hundred percent agree.
You still have PromQL, you still pay Datadog, you still pay Temporal.
Thank you.
Yep.
The level of complexity of the dependencies that we can internalize is,
I would say, low medium right now, right?
Just based on model capability.
What is medium?
I would say like a couple of thousand line dependency is a thing that we could
in-house no problem in an afternoon of time.
One neat thing about it is like probably
most of that code you don't even need, right?
Like by in-housing and abstraction, you can kind of strip away.
All the generic parts of it and only
focus on what you need to enable the specific thing you're building.
I've been calling this the end of bullshit plug ins.
Yeah, because it's so much like, you know, when I publish an open source thing,
I want to accept everything and be liberal.
I want to accept this is Postel's law.
But that means there's so much bloat, so much overhead.
One other neat thing about this, too, is
when we deploy Codex security on the repo, it is able to deeply review and change
the internalized dependencies.
In a much lower friction way than it
would be to like push patches upstream, wait for them to be released, pull them
down, make sure that's compatible with all the transitives I have in my repo and
things like that. So it's also much lower friction
to kind of internalize some of these things.
If code is free because the tokens are cheap sort of thing.
Yeah, I think like the only argument I
have against this is basically scale testing, which obviously the larger pieces
of software like Linux, MySQL, he calls that even the data does in Temporals and then
maybe security testing where classically, I think, is it Linus Torvalds who said
like security open source is the best disinfectant, right?
Many eyes, many eyes.
And if you, you know, inline your dependencies and code them up,
you're going to have to relearn mistakes from other people.
Yep, yep, yep.
And, you know, to internalize that dependency, you're back to zero and you
have to kind of start reassembling all those bits and pieces to have high confidence
in the code as it is written, right?
Yeah.
But even part of like the first intro of this, you basically mentioned like
everything was written by Codex, including internal tooling, right?
So internal tooling, like when you're visualizing what's going on, it's writing
it for it. Yeah, I built internal tooling for AI now and like I just show them off
and they're like, how long did you spend?
And I didn't spend any time, I just prompted it, you know.
Very funny story here.
Yeah, go ahead.
We had deployed our app to the first dozen users internally, had some
performance issues, so we asked them to export a trace for us,
get a tarball, gave it to our on-call engineer.
And he did a fantastic job of working with Codex to build this beautiful local dev
tool, Next.js app that you drag and drop the tarball in and it visualizes the entire
trace. It's fantastic, took an afternoon, but none of this was necessary because you
could just spin up Codex and give it the tarball and ask the same thing and get
the response immediately.
So in a way, optimizing for human legibility of that debugging process was wrong.
It kept him in the loop unnecessarily when instead he could have just like Codex
cooked for five minutes and gotten there.
Yeah, you have to fight your instincts here.
I was like, this is how we used to do it or this is how I would have used to solve it.
Yeah. In this local observability stack, like, sure, you can deploy Jaeger to
visualize the traces, but I wouldn't expect to be looking at the traces in the first
place because I'm not going to write the code to fix them.
Yeah, I mean, so basically it needs to be like this kind of house stack and owning the
whole loop. I think that that is very well established.
And it sounds like you might be sharing more about that in the future, right?
Yeah, I think we're excited to do so.
We're going to talk about Symfony in a little bit.
But like the way we distributed it as a spec, which I think folks are calling
ghost libraries on Twitter, like this is like such a cool name.
It does mean it becomes much cheaper to share software with the world, right?
You define a spec.
How you could build your own specifying as much as is required for
a coding agent to reassemble it locally.
The flow here is very, very cool.
Like we have taken all the scaffolding
that has existed in our proprietary repo, spun up a new one,
ask Codex with our repo as a reference, write the spec.
We tell it spin up a Tmux, spawn a disconnected Codex to implement the spec,
wait for it to be done, spawn another Codex and another Tmux
to review the implementation compared to upstream and update the spec.
So it diverges less.
And then you just loop over and over and over Ralph style until you get a spec
that is with high fidelity, able to reproduce the system as it is.
It's fantastic.
And you're basically you're not really
adding any of your human bias in there, right?
That's correct.
A lot of times people write a spec and be like, OK, I think it should be done this
way and you'll riff on something and it's like, no, they didn't just handle that.
Like you're still scaffolding.
In a sense, right. I want it done this way.
It can determine that spec better.
That's right. That's right.
Part of me,
you know, I've been working a lot on evals recently and part of me is wondering if
an agent can produce a spec that it cannot solve.
Like, is it always capable of things that
it can imagine or can imagine things that it is impossible to do?
I think with Symfony, we there's like this
there's this axis, right, where you have things that are easier, hard or established
or new, right?
And I think things that are hard and new is still something that the models need
humans yet drive. But I think those other quadrants are largely solved given the
right scaffold and the right thing that's going to drive the agent to completion.
It's crazy that it's solved.
But it means that the humans, the ones with limited time and attention,
get to work on the hardest stuff, right?
Like the problems where it's pure white
space out in front or like the deepest refactorings where you don't know what the
proper shape of the interface is.
And this is where I want to spend my time because it lets me set up for the next level of scale.
Yeah. Yeah. Amazing.
Let's let's introduce Symfony.
I think we've been mentioning it every now and then.
Elixir. Interesting option.
Yeah. Yeah.
Again, like the the the the Elixir manifestation here is is just a derivative.
Is it a model chosen? Yeah.
Yeah. Yeah.
And it chose that because the process supervision and the gen servers are super amenable to the type of process orchestration that we're doing here.
Right. You are essentially spinning up little daemons for every task that is in execution and driving it to completion,
which means the model gets a ton of stuff for free by using Elixir and the Beam.
I mean, I had to go do a crash course in Beam and Elixir.
And I think most people are not operating at that scale of concurrency where you need that.
But it is a good mental model for resumability and all those things.
And these are things I care about.
But tell me the story, the origin story of Symfony.
What do you use it for?
Is this how did it form?
Maybe any abandoned paths that you didn't take?
At the end of December, we were at about three and a half PRs per engineer per day.
This was before 5.2 came out.
In the beginning of January, everyone gets back from holiday.
With 5.2 and no other work on the repository, we were up in the five to ten PRs per day per engineer.
And like, I don't know about y'all, but it's very taxing to
constantly be switching like that.
Like I was pretty tapped out at the end of the day.
So again, where are the humans spending their time?
They're spending their time context switching between all these active
Tmux panes to drive the agent forward in one way or another.
So let's again build something to remove ourselves from the loop.
And this is what Frantic sprinted after here to find a way to
remove the need for the human to sit in front of their terminal.
So a lot of experimentation with dev boxes.
And, you know, automatically spinning up agents.
Like, it seems like a fantastic end state here where my life is beach.
I open live twice a day and, you know, say yes, no to these things.
And this is again a super, super interesting framing for how the work is
done because I become more latency insensitive.
I have way less attachment to the code as it is written.
Like I've had close to zero in
investment in the actual authorship experience.
So if it's garbage, I can just throw it away and not care too much about it.
In Symphony, there's this like rework state
where once the PR is proposed and it's escalated to the human for review,
it should be a cheap review, right, is either mergeable or is not.
And if it's not, you move it to rework.
The Elixir service will completely trash
the entire work tree and PR and start it again from scratch.
And this is that opportunity again to say, why was it trash?
Right. What did the agent do that was bad?
Yeah. Fix that before moving the ticket to progress again.
Yeah. Why is this not in Codex app?
I guess you guys are ahead of Codex app, I guess.
Yeah. So the way the team has been working is
basically to be as AI pilled as possible and spread the head.
And a lot of the things we have worked on
have fallen out into a lot of the products that we have.
Like we were in deep consultation with the Codex team
to have the Codex app be a thing that exists, right.
To have skills be a thing that Codex is able to use.
So we didn't have to roll our own to put automations into the product.
So all of our automatic refactoring agents
didn't have to be these hand rolled control loops.
It has been really fantastic to be in a way unanchored to the product development
of Frontier and Codex and just very quickly try to figure out what works and then later find
out the scalable thing that can be deployed widely.
It's been a very fun way to operate.
It's certainly chaotic.
I have lost track very often of what the actual state of the code looks like
because I'm not in the loop, right.
There was one point where we had wired Playwright directly up to the Electron app with MCP.
MCPs I'm pretty bearish on because the
harness forcibly injects all those tokens in the context and I don't really get a say over it.
They mess with auto compaction.
The agent can forget how to use the tool.
There's probably only like, what, three calls in Playwright that I actually ever
want to use, so I pay the cost for a ton of things.
Somebody vibed a local daemon
that boots Playwright and exposes a tiny little shim CLI to drive it.
And I had zero idea that this had occurred
because to me, I run Codex and it's able to, you know, it's better.
Yeah, like like no knowledge of this at all.
So.
We have had like in human space
to spend a lot of time doing synchronous knowledge sharing.
We have a daily stand up that's 45 minutes long because
we almost have to fan out the understanding of the current state.
I was going to say, like, this is good for a single human multi agent,
but multi human, multi agent is a whole like explosion of stuff.
Yeah. And this is fundamentally why we have such a rigid, like,
10,000 engineer level architecture in the app, because we have to find ways
to carve up the space so people are not trampling on each other.
Sorry, I don't I don't get the 10,000 thing.
Did I miss that?
The structure of the repository is like 500 MPM packages.
And it's like architecture to the access for what you would consider,
I think, normal for a seven person team.
But if every person is actually like 10 to 50, then the like numbers
on like being super, super deep into decomposition and sharding
and like proper interface boundaries make a lot more sense.
Yeah, to me, that's why I talked about
micro frontends and, you know, an access from that world.
But cool. It's just coming back to this.
Like, I don't know if you have other thoughts on orchestrating so much work
going going through this. Is this enough?
Is this like any aha moments?
It'll be interesting to see like, OK,
so right now you pick linear as your issue tracker, right?
Or is it actually linear?
This is actually linear.
Oh, that's linear. It's linear.
Oh, I never look at linear video.
The demo video I had to download to run.
Yeah, so I because I'm a Slack maxi, but like linear is also really good.
Yes, we do make a good use of Slack.
We we fire off codecs to do all these
low opacity fix ups, the things that like sync that knowledge into the repository.
It's super cheap. Do it in codecs.
My biggest ploy is OpenAI needs to build Slack, right?
You need to own Slack.
Build yours.
Turn this into Slack.
I did. I did read it is.
Yeah.
I would say that if we think that we want
these agents to do economically valuable work, which is like this is the mission,
right, we want AI to be deployed widely to do economically valuable work,
then we need to find ways for them to naturally collaborate with humans,
which means collaboration tooling, I think, is an interesting space to explore.
Yeah, totally. Yeah.
GitHub, Slack, linear.
Yeah, that was kind of my thing. Like, OK, where do we see right now?
Codecs has started codecs model, then CLI.
Now there's an app. App can let me shoot off multiple codecs in parallel.
But there's no great team collaboration for codecs, right?
And it seems like your team had some say into what comes out, right?
So you talk to them. Codecs kind of was a thing from there.
If you guys are on the bound, what stuff that like, you know,
you might not focus on, but like, what do you expect other people to be building?
Right. So people that are like 5x, 50xing,
should you build stuff that's like very niche for your workflow, for your team?
Or should it be more general so other people can adopt this or a niche there?
Like because because part of it is just like, OK, is everything just internal
tooling? Do we have everything our own way?
Like the way our team operates has our own ways that we like to communicate.
Or, you know, is there a broader way to do it?
Is it something like an issue tracker?
Just thoughts if you want to reform that.
I think TBD, like we have not figured this out in a general way.
I do think that there is leverage to be
had in making the code and the processes as much the same.
As possible.
If you think that code is context, code is prompts.
It's better from the agent behavior
perspective to be able to look in a package in directory XYZ and it not to
have to page so deeply into directory ABC because they have the same structure,
use the same language, they have the same patterns internally.
And that same like leverage comes from aligning on a single set
of skills that you're pouring every engineer's taste into to make sure
that the agent is effective.
So like in our code base, we have, I think, six skills.
That's it.
And if some part of the software development loop is not being covered,
our first attempt is to encode it in one of the existing set of skills,
which means that we can change the agent behavior
more cheaply than changing the human driver behavior.
Yeah.
Have you ever experimented with agents changing their own behavior?
We do. Yes.
Or parent agent changing a subagent.
You know, behavior or something like that.
We have some bits for skill distillation.
So, for example, there's one neat thing you can do
with Codex, which is just pointed at it's on session logs to ask it to
tell you how you can use the tool better, introspection or ask it to do things better.
How can I do this session better?
What skills should I have?
I like the modification of you can just do things to that.
You can just ask the agent to do things.
You can just codex things.
This is like a
emoji that we have. You just codex things, you can just prompt things.
It's really glorious future we live in.
But like, OK, you can do that one on one.
But like, we're actually slurping these up for the entire team into blob storage
and running agent loops over them every day to figure out where as a team can we
do better and how do we reflect that back into the repository?
Though everybody benefits from everybody else's behavior for free.
Same for like PR comments, right?
These are all
feedback that means the code as written deviated from what was good.
A PR comment, a failed build.
These are all signals that mean at some point the agent was missing context.
We've got to figure out how to slurp it up and put it back in the reboot.
By the way, I do this exactly right.
So when I use Cloud Code for knowledge work, Cloud
Code work is like a nice product.
And I think you would agree.
I always have it tell me what do I do better next time.
Right. And that's the metaprogramming reflection thing.
So I was thinking like you have six reflection extraction levels in Symfony,
almost like the zero layer.
So the six levels are policy, configuration,
coordination, execution, integration, observability.
We've talked about a couple of these, but the zero layer is like the OK, well,
are we working well? Can we improve how we work?
Yes. Can I modify my own workflow without MD or something?
I don't know. Yeah, of course.
Of course you can.
Like this thing is also able to cut its own tickets because we give it full
access. You can make a ticket to have it cut tickets.
You can put in the ticket that you expect it to file.
It's all web work. Self-modifying.
Yeah. Yeah.
Don't put the agent in a box.
Give give the agent full accessibility over its domain.
I had a mental reaction when you said don't put the agent in a box.
So I think it should put it in a box.
It's just that you're giving the box everything it needs.
Yeah. Contacts and tools. Right.
But we're like as developers, we're used to calling out to different systems.
But here you use the open source things like the Prometheus, whatever, and you run
it locally so that you can have the full loop.
Right. I assume. Yep.
Right. I think I want to minimize cloud dependencies.
You also want to make sure that you think about what the agent has access to.
Right. Like, what does it see?
Does it go back into the loop?
Like from the most basic sense of you let it see its own calls, traces.
It can determine where it went wrong. Right.
But are you feeding that back in?
So, you know, just the most basic level of like you want to see exactly what's
input output, like does the agent have access to what is being output?
Right. It can self-improve a lot of these things.
It's all text. Right.
My job is to figure out ways to funnel text from one agent to the other.
It's so strange.
Like, you know, like way back at the start of this whole AI wave, like Andre was
like, you know, English is the hottest new programming language.
Isn't it? It's here. It's here.
Yeah. The features. Yeah.
OK, like a lot of software, a lot of stuff.
There's a GUI. It's made for the human.
You know, we're seeing the evolution of CLIs for everything.
Right. All tools have CLIs.
Agents can use them well.
But, you know, do we get good vision?
Do we get good little sandboxes?
Like right now, it's a really effective way.
Right. Models love to use tools.
They love to bash. They love to read through text.
So slap a CLI, let it let it go loose.
That works for everything. It does.
Yeah, yeah, yeah. We've also been adapting
non-textual things to that shape in order to improve model behavior in some ways.
Right. Like we want the agent to be able to see the UI.
And agents do not perceive visually in the same way that we do.
Right. Like they don't see a red box.
They see red box button. Right.
They see these things in latent space.
So if we want to have a thing that goes off every time you're sitting in space.
Ding.
Anyway, if we want to actually, like, make it see the layout, it's almost easier
to rasterize that image to ASCII or and feed it in to the agent.
And there's no reason.
There's no reason you can't do both.
Right.
So like further refine how the model perceives the object it's manipulating.
Cool. Can we you want to talk about a couple
more of these layers that might bear more introspection or that you have personal
passion for? I will say that the coordination layer here was a really
tricky piece to get right. Let's do it.
Yeah, I'm all about that.
And this is temporal core core thing.
This is where when we turn the spec into elixir,
where like the model takes a shortcut, right?
It's like, oh, I have all these primitives
that I can make use of in this lovely runtime that has native process
supervision, which is, I think, kind of a neat way to have taken
the spec and like made it more achievable by making choices that naturally map the
domain right in the same way that like you would prefer to have a TypeScript
model repo if you are doing full stack web development.
Right.
Because the ability to share types across
the front end and back end reduces a lot of complexity.
And because it's what GraphQL used to be.
That's right.
And I don't know if it's still alive, but no humans in the loop here.
So like my own personal ability to write or not write elixir doesn't really have
to bias us away from using the right tool for the job, which is just wild.
Love it. I love it.
Yeah. I wonder if any languages struggle more
with servers because of this.
I feel like everyone has their own abstractions that would make sense,
but maybe it might be slower or it might be more faulty where like you'd have
to just kick the server every now and then.
I don't know.
I think observability layer is really well understood.
Integration layer, MCP is dead.
I think all these are just like a really
interesting hierarchy to travel up and down.
It's common language for people working on the system to understand.
The policy stuff is really cool, right?
Like, yeah, you don't really have
to build a bunch of code to make sure the system waits for CI to pass.
It's your institutional knowledge.
You just give it the GH CLI with some text to say, CI has to pass.
It makes the maintenance of these systems a lot easier.
Do you think that like CLI maintainers need
to do anything special for agents or just as is it's good?
Because like I don't think when people
made the GitHub CLI, they anticipated this happening.
That's correct. The GH CLI is fantastic.
It's great. It's super industry.
Everyone go try GH repo create.
Like, GH pull and then pull request number, right?
GHPR like 153, whatever, right?
And then it like pulls.
Basically, my only interaction with the GitHub web UI at this point is GHPR view
dash dash web glance at the diff and be like, sure thing, send it.
Yeah.
But the CLIs are nice because they're super token efficient and they can be
made more token efficient really easily, right?
Like I'm sure you all have seen like I
go to Buildkite or Jenkins and I could just get this massive wall of build output.
And in order to unblock the humans,
your developer productivity team is almost certainly going to write some code
that parses the actual exception out of the build logs and sticks it in a sticky
note at the top of the page and you basically want CLIs to be structured
in a similar way, right? You're going to want to pass dash dash
silent to prettier because the agent doesn't care that every file was already
scripted and just wants to know it's either formatted or not, right?
So it can then go run a write command.
Similarly, like
in our PMPM sort of distributed script runner when we had one,
when you do dash dash recursive, like it produces a absolute mountain of text.
But all of that is for passing test suites.
So we ended up wrapping all of this in another script to suppress the vibe.
And we output the failing parts of the tests.
You make a pipe errors versus the standard standard out.
I don't know. OK, whatever.
Too much, too much thinking.
I used to maintain a CLI for my company.
And like, yeah, this is this is like very close to my heart.
But you're vibing my job.
That's right.
Cool. Any other things?
I mean, this is a long spec.
I appreciate that.
Like it's it's got a lot of strong opinions in here.
Any other things that we should highlight?
I think.
I don't want to spend the whole day going through some of these, but like,
you know, I do think that some of these have a lot of care or some of this you
might you might want to tell people, hey, take this, but, you know, make it your own.
Fundamentally, software is made more
flexible when it's able to adapt to the environment in which it is deployed.
Right.
Which means that things like linear or GitHub even are
specified within the spec, but not required pieces of it.
Right. There's like a more platonic ideal
of the thing that you could swap in, like Jira or Bitbucket, for example.
Right.
But being able to tightly specify things like the ID formats or how the Ralph
loop works for the individual agents basically means you can get up and
running with a fully specified system quickly that you then evolve later on.
I think we never intended for this to be a static spec that you can never change.
Right.
It's more like a blueprint to get something up and running for you then
to vibe later till your heart's content.
You have like code and scripts in here where it's like, oh, I mean,
I think this is a really good prompt.
It's just a very, very long prompt.
Fundamentally, the agents are good at following instructions.
So give them instructions. Right.
And it will improve the reliability of the result.
Right.
Like we much like the way we use Symfony, we don't want folks to have to monitor
the agent as it is vibing the system into existence.
So being very opinionated, very strict around what the success
criteria are means that like our deployment success rate goes up.
Yeah.
It means we don't have to get tickets on this thing.
It all goes back to that like code is disposable.
Right.
Like early on when you had CLI or you'd kick off a codex run, it would take two
hours, you would kind of want to monitor like, OK, I'm in the workflow of just
using one, I don't want to go down the wrong path.
I'll cut it off.
But, you know, just shoot off four.
Like that was my favorite thing of the codex app, right?
Yeah.
Just four exit like it's OK.
One of them will probably be right.
One of them might be better. Stop.
Stop overthinking it.
Like my first example is probably like deep research when you put out deep
research and I'd ask it something like I asked it something about LLM.
It thought it was legal or something and
spent an hour, came back with a report completely off the rails.
And I was like, OK, I got to monitor this thing a bit.
No, don't monitor it.
Just you want to build it so that it goes the right way.
And you don't want to you don't want to sit there and babysit.
Right.
You don't want to babysit your agents with that deep research query that you
made looking at the bad result, you probably figured out you needed to tweak
your prompt a bit, right, like that's that guardrail that you fed back
into the code base for the ask your prompt to further align the agent's execution.
Same sort of concepts apply there, too.
When you talk, I mean, how are the customers feeling?
For Symfony, I think we have none.
Right.
This is a thing we have put out into the world.
I mean, Symfony is internal, right?
As long as you're happy, you're the customer.
That's right.
Just, you know, what's what's the external view?
I say folks are very excited about this
way of distributing software and ideas in cheap ways for us as users.
It has again pushed the productivity
5x, which means I think there's something here that's like a durable pattern around
removing the human from the loop and figuring out ways to, like, trust the output.
Right.
The video.
The video that is shared here is the same sort of video we would expect the coding
agent to attach to the PR that is created.
That's part of building trust in the system.
And that's to me, like, fundamentally what has been cool about building this is like
it more closely pushes that persona of the agent working with you to be like a teammate.
Right.
I I don't shoulder surf you like for the tickets that you work on during the week.
I would.
If I ever think that I would want to do that, I wouldn't want a screen recording
of your entire session in cursor or cloud code.
I would expect you to do what you think
you need to do to convince me that the code is good and mergeable and compress
that full trajectory in a way that is legible to me, the reviewer.
Yeah, it's stuff.
And you can just do that because Codex will absolutely sling some.
You can take around. It's great.
Oh, I mean,
FFmpeg is the OG, like God CLI, Swiss Army Chainsaw.
I used to say there's a sass, micro sass, let's call it in every flag in FFmpeg.
Oh, for sure. For sure.
Like just host it as a service, put a UI on it.
People who don't know FFmpeg will pay for it.
When we were first experimenting with this, it was a wild feeling to be at the computer
with just like windows just popping up all over the place and getting captured
and files appearing on my desktop.
It very much felt like the future to have
a thing controlling my computer for like actual productive use.
Right. Like I'm just there keeping it like
awake, jiggling the mouse every once in a while.
That's what some office workers do.
So they buy a mouse jiggler.
That's right. That's right.
One thing I'd like to ask.
So like, OK, as stuff is so code is disposable, async, shoot off a bunch of agents.
One question is like, OK, are you always like a extra high thinking guy?
And where do you see Spark?
5.3 Spark?
Like, there's a lot of me wanting to make quick changes.
I'm not going to open up ID.
I'm not going to do anything.
But I will say, OK, fix this little thing, change a line, change a color.
Spark is great for that.
But like, am I still the bottleneck?
You know, like, why don't I just let that go back and just riff on that?
You know, is there.
Spark is such a different model compared to the
the extra high level reasoning that you get in these, you know,
three or four people, it is a different model, different architecture, different.
It doesn't support it. It's incredibly fast.
Smaller model.
I have not quite figured out how to use it yet, to be honest.
It's faster. I was I was adapting it to the same sorts
of tasks I would use X high reasoning for.
And it would blow through three compactions before writing a line of code.
And I mean, that's another big thing with
5.4, right? Million coking context, which is huge in agentics, right?
Like you can just run for longer before you have to compact.
The more tokens you can spend on a task before compacting, like the better you'll
do. That's right. That's right.
I'm not sure how to deploy Spark.
I think your intuition is right, that like it's very great for spiking out
prototypes, exploring ideas quickly, doing those documentation updates.
It is fantastic for us in taking that feedback and transforming it into a lint
where we already have good infrastructure for ES lints in the code base.
These sorts of things it's great at.
And it allows us to unblock quickly doing those like antifragile healing tasks in the
code base. Yeah, that makes sense.
So you're pushed, you guys are pushing models to the fricking limit.
What can card models not do well yet?
They're definitely not there on being
able to go from new product idea to prototype one shot.
This is where I find I spend a lot of time steering is
translating end state of a mock for a net new thing, right?
Think no existing screens into product that is playable with.
Similarly, while this has gotten better with each model release, like the gnarliest
refactorings are the ones that I spend my most time with, right?
The ones where I am interrupting the most,
the ones where I am now double clicking to build tooling to help decompose
monoliths and things like that, this is a thing I only expect to get better.
Right.
Over the course of a month, we went from the low complexity tasks to like
low complexity and big tasks in both these directions.
So this is what it means to not bet against them all.
Right.
You should expect that it is going to push
itself out into these higher and higher complexity spaces.
So the things we do are robust to that.
It just basically means I'll be able to
spend my time elsewhere and figure out what the next bottleneck is.
I do think it's also a bit of a different type of task, right?
Like Codex is really good at code base understanding, working with code bases.
But companies like Lovable, Bolt, Replit,
they solve a very different problem scaffold of zero to one idea to product.
And it's like there are people working on that.
And models are also pushing like step function changes there.
It's just kind of different than the software engineering agents you see today.
Right.
Like I said, the model is isomorphic to myself.
The only thing that's different is
figuring out how to get what's in here into context for the model.
And for these white space sort of projects, I myself, I'm just not good at it.
Which means that often,
over the agent trajectory, I realize the bits that we're missing,
which is why I find I need to have the synchronous interaction.
And I expect with the right harness,
with the right scaffold that's able to tease that out of me or refine the possible
space, right, to be super opinionated around the frameworks that are deployed or
to put a template in place, right, these are ways to give the model
all those non-functional requirements, that extra context to anchor on and avoid
that wide dispersion of possible outcomes. Thank you for that.
I want to talk a little bit about Frontier.
Yeah, sure.
Overall, you guys announced it maybe like a month ago.
And there's a few charts in here.
And it's kind of like your enterprise offering is kind of what I view it.
Is there one product or is there many?
I can't speak to the full product roadmap here, but what I can say is that
Frontier is the platform by which we want to do AI transformation of every enterprise
and from big to small. And the way we want to do that is by making it
easy to deploy highly observable, safe, controlled, identifiable agents into the
workplace, right? We want it to work with your company native IAM stack.
We want it to plug into the security tooling that you have.
We want it to be able to plug into the workspace tools that you use.
So you're just going to be stripping specs, right?
We expect that there will be some
harness things there.
Agents SDK is a core part of this to enable both startup builders as well as
enterprise builders to have a works by default harness that is able to use all
the best features of our models from the shell tool down to the codex harness with
file attachments and containers and all these other things that we know go into
building highly reliable, complex agents.
We want to make that great and we want to make it easy to
compose these things together in ways that are safe.
For example, right, like the GPT OSS Safeguard model, for example.
One thing that's really cool about it is
it ships the ability to interface with a safety spec.
Safety specs are things that are bespoke to enterprises.
We owe it to these folks to figure out ways for them to instrument the agents in
their enterprise to avoid exfiltration in the ways they
specifically care about to know about their internal company code names,
these sorts of things.
So providing the right hooks to make the platform customizable, but also
mostly working by default for folks is kind of the space we are trying to explore here.
Yeah. And this is like, you know,
the snowflakes of the world just need this, right?
Brexit of the world stripes.
Yeah, it makes sense.
I was going to go back to your you know,
I think the demo videos that you guys had was pretty illustrative.
It's kind of like also to me, an example of very large scale agent management.
Yes.
Like you give people a
control dashboard that if you play any one of these like multiple agent things,
you can dig down to the individual instance and see what's going on.
Yes, of course.
Well, who's the user?
Is it like the CEO, the CTO, CIO, something like that?
So, you know, at least my personal opinion here,
the buyer that we're trying to build product for here is one and employees who
are making productive use of these agents, right?
That's going to be whatever surfaces they
appear in, the connectors they have access to, things like that.
So something like this dashboard is for
IT, your GRC and government's folks, your AI innovation office, your security team,
right, the stakeholders in your company that are responsible for
successfully deploying into the spaces where your employees work, as well as doing
so in a safe way that is consistent with all the regulatory requirements that you
have and customer attestations and things like that.
So it is kind of a
kind of an iceberg beneath the actual end.
Yeah, you jump like every, I guess,
layer in the UI is like going down the layer of extraction in terms of the agent.
Right. Yep. Yeah, I think it's good.
Yeah, the ability to dive deep into the
individual agent trajectory level is going to be super powerful, not only for like
from like a security perspective, but also from like someone who is accountable
for developing skills. One thing that was interesting that we also blogged about
for shipping was an internal data agent, which uses a lot of the frontier
technology in order to make our data ontology accessible to the agent and
things like that to understand what's actually in the data warehouse.
Yeah, semantic layer type things.
I was briefly part of that world.
Is it salt? I don't know.
It's actually really hard for humans to agree on what revenue is.
Yes. You know? Yes.
What is an active user?
There's like, what, five data scientists in the company that have to
run this golden curve.
Yeah. And like, no.
And there's also internal politics as to attribution of like, I'm marketing.
I'm responsible for this much.
And sales is responsible for this much.
And they all add up to more than 100.
And I'm like, well, you guys have different definitions.
And if you're a startup, everything is ARR.
So I think that's cool.
Oh, you guys blogged about this.
OK, I didn't I didn't see this.
Yeah. Is this the same thing?
I don't know. Is this what you're referring to?
Yes. OK, well, we'll send people to read this.
This is our data agent.
Yeah. I don't know if you have any highlights.
No, no, no. I mean, in general, from the point of view,
there's a lot of good things to read.
Yeah. Yeah. Lots of homework for people.
No, but like data as the feedback layer, you need to solve this first in order
to have the product's feedback loop closed.
That's right. So for the agents to understand.
And like, this is not something that humans have not solved this.
Like in this is how this is how you build
a business that do more than coding, right?
Yeah. To actually understand how you operate the business.
Yeah.
You have to understand.
And what revenue is what your customer segments are, right?
What your product lines are, right?
Like one thing that's in like moving back
to the code base that we described here for harnessing.
One thing that's in corebeliefs.md is like who's on the team,
what product we're building, who our end customers are, who our pilot
customers are, what the full vision of what we want to achieve over the next 12
months is like these are all bits of context that inform
how we would go about building the software.
Oh, my God.
So we have to give it to the agent, too.
I'm guessing that stuff is like pretty
dynamic and it changes over time, too, right?
Like part of it was it's not just a big spec.
You you have it as one of the things and it will iterate.
One thing that I think is going to break
your mind even more is we have skills for how to properly generate deep fried memes
and have ReactG culture and Slack, because with the Slack chat GPT app that you're
able to use in Codex.
It's like I can get the agent to shitpost on my behalf.
It's just it's part of humor.
Humor is part of AGI.
Is it is it funny? It's pretty good.
Yeah. OK.
Yeah, it's pretty good.
I mean, you know, it's a lot of like I think humor is like a really hard
intelligence test, right? Like it's like you have to get a lot
of context into like very few words.
This is this is one of the references why
five four is such a big uplift for our meme lores.
It's the memeing. Yeah, for sure.
Yeah. Yeah, it's very cool.
So five four can shitpost.
So the takeaway.
Yeah, maybe maybe when y'all are done here
today, ask Codex to go over your coding agent sessions and to roast you.
Love it. I'll give a shot.
Coming back to the final point I wanted to make is, yeah, I think that there are
multiple other like you guys are working on this, but this is a pattern that every
other company out there should adopt regardless of whether or not they work
with you. To me, this is like I saw this.
I was like, fuck, every company needs this.
I mean, this is multiple billions of what it takes to get people to.
Yes. Yeah.
Actually realize the benefits and distribute it.
And it's it's I think it sounds boring to people like, oh, you know, it's for
safeguards and whatever, but like I think you to to handle agents at scale like
you're envisioning here, I don't know if it's like a real screenshot, like a demo.
But like this is what you need is my original sort of view of what
it's supposed to be that you've built this dashboard and you basically have
every long running process in the company and one dashboard and that's it.
That's right.
I think it's pretty it's pretty like
customized towards every enterprise, like you care about different things.
There's a lot of customization. Right.
But like I mean, there'll be multiple unicorns just doing this as a service.
Like, I don't know.
I'm like very, very frontier pilled, if you can tell.
Amazing.
But it only clicked because obviously this came out first, then Harness and
then Symphony, and they only clicked for me that like this is actually kind of the
thing you ship to do that. Yeah.
Yeah. There's a set of building blocks here
that we assembled into these agents and the building blocks themselves are part
of the product, right? The ability to steer, revoke authorization.
If a model becomes misaligned, like all of this is accessible through Frontier.
And there's going to be a bunch of
stakeholders in the company that have the things they need to see
on the platform to get to yes.
So we'll build all those in the Frontier
so that we can actually do the widespread deployment.
That's the fun part. Yeah.
I'm also calling back to like there's this like levels of AGI.
Like, I don't know if OpenAI is still talking about this,
but they used to talk about five levels of AGI.
And one of it was like, oh, it's like an intern coding software agent.
At some point it was AI organization.
And this is it. That's right.
This is level four or five.
I can't remember which level, but it's somewhere along that.
Which path was this?
You know how I mentioned that my team is having fun sprinting ahead here.
Right.
And we do this thing where we're collecting all the agent trajectories
from Codex to slurp them up and distill them.
Like this is what it means to build our team level knowledge base.
We happen to reflect it back into the code base, but it doesn't have to be that way.
Right.
And it doesn't have to be bound to just Codex.
Right.
I want ChatGPT to also learn our meaning
culture and also the product we are building and how.
Right. So that when I go ask it, it also has the
full context of the way I do my work.
And I'm super excited for Frontier to enable this.
Yeah. Amazing.
What did the model people say when they see you do this?
Like you have a lot of feedback.
Obviously, you have a lot of usage.
You have a lot of trajectories.
I don't imagine a lot of it's useful to them, but some of it is.
I mean, you have this too.
You deploy a billion tokens of intelligence a day.
And this was, you know, this was at the beginning of 2096.
You're cooking.
Yeah.
There's this fundamental tension, which I think you have talked about between
whether or not we invest deeper into the harness or we invest deeper into the
training process to get the model to do more of this by default.
Yeah.
And I think success for the way we are operating here means
the model gets better taste because we can point the way there.
And none of the things we have built actively degrade Asian performance
because really all
they're doing is running tests.
And like running tests is a good part of what it means to write reliable software.
If we were building an entire separate
raw scaffold around Codex to restrict its output, that I think would be
like additional harness that would be prone to being scrapped.
But if instead we can build all the guardrails in a way that's just native
to the output that Codex is already producing, which is code, I think, one, no friction
with how the model continues to advance, but also like just good engineering.
And that's that's the whole point.
Yeah.
So I've had similar discussions with research scientists where the RL
equivalence on policy versus off policy.
Yeah.
And you're basically saying that you should build an on policy harness,
which is already like well within distribution and you modify it from there.
But if you build off policy, well, it's not that useful.
That's right. Super cool.
Well, any thoughts, any things that we haven't covered that we should get out there?
Just
I've been super excited to kind of benefit
from all the cooking that the Codex team has been doing.
They absolutely ship relentlessly.
This is one of our core engineering values,
ship relentlessly and the team there embodies it to an extreme degree.
Well, yeah, I have five, three and then Spark and five,
four come out within like what feels like a month is just a phenomenally fast.
It's exactly a month ago was five, three and yesterday was five, four.
Yeah. I mean, do we have every month now is five, five next week.
And, you know, I can't say that the poly markets would be very upset, right?
Well, I think it's interesting that like it's also correlated with the growth.
You know, they they announced it's like two million users,
but like almost don't care about Codex anymore.
Like, this is it. This is the game, man.
Like it's like coding.
Cool, soft, like knowledge work.
That's right.
This is the thing to chase after.
And, you know, this is one of the things that my team is excited to support.
Get the whole like self-hosted harness thing working, which you have done
and the rest of us are trying to figure out how to catch up.
But like then do things, you know, do things.
That's right. You can just do things.
That's the line for the episode.
That's it. Any other call to actions?
You're you're based in Seattle, your team, I'm guessing.
New Bellevue office. New Bellevue office.
We just had the grand opening yesterday as of the recording date, which was
fantastic, beautiful building, super excited to be part of the Bellevue
community building the future in Washington.
And I would say that there is lots of work to be done.
In order to successfully serve enterprise
customers here in Frontier, we are certainly hiring.
And if you haven't tried the Codex app yet, please give it a download.
We just passed two million weekly active
users growing at a phenomenally fast rate, 25 percent week over week.
Come join us.
Yes. And I think that's an interesting observation.
OpenAI is a very San Francisco centric company.
Like I know people who have been who turned down the job or didn't get the job
because they didn't want to move to SF and now they just don't have a choice.
Right. You have to open the London.
You have to open the Seattle.
And I wonder if that's going to be a shift in the culture.
Right. Obviously, you can't say, but.
I was one of the first engineering hires out of our Seattle office.
Yeah, it was very natural.
Success has been part of what I have been
building toward and it is it has grown quite well.
And you have durable products and lines of business that are built
out of their ton of zero to one work happening as well, which is kind of the
core essence of the way we do applied AI work at the company to print after it
new to figure out where we can actually successfully deploy the model.
So, yes, 100 percent.
We also have a New York office, too, that has a kind of engineering presence.
Yeah, exactly.
That's the sort of my roadmaps for AI.
Wherever people hire engineers, I will go.
That's right.
It's a cool office to New York is the old R.E.I.
building, I believe, the R.E.I. office.
It's just no, you'll never be as big, right?
New York is like you can't get the size of office that they need.
The the New York Seattle has a very like office madman sort of vibe.
It's it's beautiful.
The Bellevue one is very green.
Gold fixtures, very Pacific Northwest is very cool.
It's a bit local.
Yeah, a lot of people are like, therefore, people like New York.
They want to be in New York, right?
Yeah, yeah.
We have a fantastic workplace team that has been building out these offices.
It really is a privilege to work here.
Yeah. Excellent.
OK, well, thank you for your time.
You've been very generous and you've been cooking.
So let me let you get back to cooking.
It's been amazing chatting with you folks.
Happy Friday. Happy Friday.
