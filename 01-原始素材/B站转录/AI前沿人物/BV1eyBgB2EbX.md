---
title: "Claude Code负责人：AI 原生团队如何使用AI？"
platform: bilibili
bvid: BV1eyBgB2EbX
author: Easonlee的AI笔记
pubdate: 20251225
duration_sec: 2436
url: https://www.bilibili.com/video/BV1eyBgB2EbX
subtitle_source: faster-whisper_large-v3
asr_model: large-v3
transcript_chars: 39535
crawl_time: 2026-07-12
---

# Claude Code负责人：AI 原生团队如何使用AI？


## 视频信息

- **UP主**: Easonlee的AI笔记
- **时长**: 40min
- **链接**: https://www.bilibili.com/video/BV1eyBgB2EbX


## 视频描述

大家好，我是Easonlee，关注AI时代的自我成长。

《AI Builder》是我频道的第三个专栏，分享一线创始人AI的实践和思考。AI时代，让我们关注Builder，成为Builder。

今天，我想和大家分享一期 Cat Wu 的新节目。

Cat 是 Claude Code 的产品负责人，我请她分享了科技领域中最具 AI 原生性的团队之一是如何实际运作的。亮点包括每 10 分钟获取用户反馈，直接制作原型而非文档，以及设计师直接提交代码。Cat 还分享了她使用 Claude Code 的 3 个最佳技巧以及该产品的未来发展。

要点：
• 每 10 分钟获取用户反馈
• 直接制作原型而非文档
• 设计师直接提交代码
• Cat 的 3 个最佳 Claude Code 技巧
• 该产品的未来发展


## 完整文稿

> 来源: faster-whisper large-v3 (CUDA/fp16)


We don't use many Google Docs for QuadCode.
A lot of our best features was like an engineer prototyping an idea,
shipping it to dogfooding, and we just hear what the feedback is.
Like, do people immediately understand it?
Are people confused?
Is it buggy?
Or do people just like love it?
How do you guys think about evals?
If you see a change in the SweetBench score,
it's not always obvious what caused the change,
and you actually have to read through these pretty gnarly transcripts.
And a lot of them, we get a new piece of feedback every,
I want to say like 10 minutes or so.
We love negative feedback.
Like, we don't want platitudes.
We want to hear what doesn't work.
Do you have like a vision doc or something for QuadCode?
Or like, what do you think the product will look like a year or two from now?
A year or two is a really long time.
I can talk about the next few months.
Okay, welcome everyone.
My guest today is Kat, the product lead for QuadCode.
QuadCode is my favorite AI agent.
So I'm really excited to talk to Kat about
how the team ships so fast,
how she uses QuadCode personally to do product work,
and what her vision is for the product.
So welcome, Kat.
Thank you so much, Peter.
Excited to share more about QuadCode with your audience.
All right.
So why don't we start with the revision story for QuadCode
and how you kind of got involved?
Yeah, so QuadCode started as a project
that Boris was tinkering with to better understand our APIs
and to see how much of software,
engineering he could augment.
And at the time, I was spending 20% time adding our own environments.
And I found that QuadCode can make me a lot more efficient at it.
And that was really good at integrating with all the tools that we have internally.
And so I was sending him a bunch of product feedback,
things that I wanted to change in the tool.
And when we made the decision to ship it externally,
I was so, so stoked to work on it full time.
And since then, it's been pretty widely adopted externally as well,
and so we're really excited to continue to invest in it.
Make it more feature-full.
Make it work across heterogeneous developer environments
and to make it more accessible.
Awesome.
So it wasn't like some part of a grand strategy,
it's kind of, he built a little tool they tinker with and then he got involved.
So what happened?
Yeah, yeah, exactly.
Like he built the tool and other people on his team started using it,
and then the rest of the org started using it,
and then the rest of the org started using it.
And then the rest of the org started using it.
using it and then it crossed over into research and then it actually started to cross over into
tech adjacent roles like data science and product management and product design so it had a very
high viral factor internally before we launched it okay so you know when i first started playing
with clock code i started in the terminal and then i was like what is this it this is the product
and uh but as i started using it more and more i discovered more and more features
and it kind of felt like uh kind of mastering a video game it kind of felt like it doesn't
kind of explain everything to you right off the bat but like the more i got into it the more i
felt like more powerful and like you know kind of kind of power user so i i guess was this like
kind of intentional and do you and the team have any product principles in building this tool
the beauty of the terminal is that it can through the terminal cloud code can access almost
everything a developer can and this is what makes the onboarding so smooth
to the tool if you're used to calling like the github cli or the datadog cli or
literally any cli tool you immediately know that cloud code can do it and so this just makes it
really fast to get started the terminal is also a very minimalist form factor so unlike a web app
you can only use ascii so you can only fit as many characters are available on the screen you
don't have the option to add any buttons and as a result you can only fit as many characters
we've been very pragmatic and very almost like brutal about what features we decide to showcase
and what features we don't because there's such minimal screen real estate as a result of this
the app form factor is very light and so it means that you don't get overwhelmed when you first
start but it also means but because we've built it to be very extensible
there's kind of like arbitrary depth as you get started our design philosophy is to make sure the
cli is very very simple to onboard to we have this philosophy that for new features there should be no
onboarding ux it should just it should be intuitive be at the feature name via like a
one-liner description what it does and you should be able to just get started and then we also think
the clis need to be very extensible because developer environments are very different
and we want to expose tools so that every engineer every developer productivity team
can customize it for their own setup got it and so that's why we have things like hooks and custom
slash commands and sub-agents and stuff like that okay so kind of like um do a simple thing first
no no like you know crazy onboarding flows and also making it composable and extensible yeah
definitely make it very simple to get started but able to handle complexity over time got it
you guys have been shipping a lot like there's new features coming out all the time and i'm just
wondering how the cloud code team actually works like you know on a given week like like did
engineers like basically ship features end-to-end themselves if that's the case then what's your role
as the pm you know how do you guys work our team is very strong a lot of very strong product
engineers who love to have end-to-end ownership over features the the way that things normally
work is there's some like high
higher level design principles that we want to follow like we always want the tool to be
customizable but within that there's a lot that you can build and a lot of our best features
what was like an engineer prototyping an idea shipping it to dog fooding which is
so that hundreds at this point maybe like a thousand internal employees can try it out and
we just hear what the feedback is like do people immediately understand it are people confused is
it buggy or do people just like
love it and for the features that people love that that's a really strong signal that we should fast
track it to um sharing it with the public and so a lot of the features that you've seen that we have
shipped a lot of times we've gone through two or three iterations of it internally before we made
it public and there's a lot of features that we've played around with internally and just like
decided not to ship i think as a pm it's tricky to be
a developer product because at the end of the day the developer is the end user and so i see the role
of the pm as one setting like the broader direction of okay how much how much customizability do we
expose what is like what is the minimum bar or what is the like aspirational bar that we want
our product features to fall between and shepherding it through the process it also
in the age of ai tools a lot of the pm role is around pricing and packaging as well so just
making sure that uh developers can focus on making the best coding experience possible
and then the pm's role is to make sure that it's accessible for the world okay so is there like
even like a product review process or you just kind of they prototype something and then it
gets traction internally and then it's like okay let's do it it's not like worse yeah yeah
for our larger projects there's a product review process and so if you if you look back at quad4
we've released id integrations with vs code and intellij and so for those it was a very clear
decision that we wanted quad code to meet people where they worked and have more context about
their tools and so made a decision worked on it for a few months and then shipped it but for
smaller features
such as the to-do list or plan mode these are ideas that we've talked about internally
and they didn't require prd because the hard thing is actually to figure out the right form factor
it's not like an integration challenge it's a design the tool the right way with the right
prompt challenge got it okay here's a quick note from our sponsor lorikeet now one of my biggest
pet peeves is sitting on hold with customer support or mashing buttons just to get to the
real person that's why businesses are turned to lorikeet an ai customer support concierge that
works 24 7 across chat email and voice this is just point to help articles it actually resolves
issues lorikeet knows your company systems policies and workflows to solve problems end to end with
99 accuracy and when a real person is needed it knows exactly when to hand things off some of the
biggest names in fintech healthcare and energy are already using lorikeet and they've seen
customer satisfaction jump by 30 points switch by october 35th and they've seen customer satisfaction
jump by 31st and lorikeet will even buy out your existing support contract so check them out now at
lorikeetcx.ai slash peter now back to the episode i think boris three is something about well not
three he posted on threads about how he designed the to-do list and it was just like him prototyping
cloud code and trying different form factors right and then you guys all tried it so how it went yeah
yeah there's a long history for to-do list so sid actually was the first person on our we noticed
a lot of people use cloud code to refactor or to rename variables or these like other larger tasks
and these tasks often involve making 20 or 30 changes and quad code would sometimes do the
first five and then forget to do the rest and so we were we were trying to figure out how do we
force the model to actually complete these tasks and so sid came up with this great idea to actually
just force the model to write down its task kind of
like what a human does as they go about their day and we were totally blown away because actually
just by forcing the model to write down its tasks and reminding it hey you can't stop until the tasks
are done this actually forced the model to go through and do all 20 or 30 items without any
early stopping and so this was like bottoms up uh by sid and then the to-do list has now been
finished and so we've in the past it was just cloud code would write the to-do list in the
transcript and so you would see it fly past your screen but it wasn't persistent and then a lot of
people we noticed that a lot of people were actually just using a to-do list to track the
model's progress and this is actually this actually meant that you actually want it to be
stickier like you don't want it to fly off the screen because otherwise users who happen to look
at the terminal don't know what's going on and so there's a lot of work to be done to do that and an
the agent's working on they have to like scroll up a lot and so the the new form factor that
Boris was experimenting with was actually showing like having the to-do be more persistent so that
you can call slash to-do at any point yeah yeah I I use that yeah I think there's some some shortcut
key to see it see how it's doing at any point right yeah totally and we've like experimented
a lot of form factors along the way that we uh didn't end up keeping so things like we have these
cute little thinking words and at some point we put the to-do list in there and then people
weren't super happy with that and so it's been a iterative process for sure how do you uh when you
iterate you you have you have obviously the you know anthropic employees that you get feedback
from but do you have a customer community too or you just look at twitter or how do you how do you
get feedback yeah we're very lucky that anthropic employees are extremely vocal about cloud code
feedback so
we have an internal chat with about a thousand maybe more anthropic employees who've opted to
join so it's not people aren't in it by default they've just decided to join and we get a new
piece of feedback every I want to say like 10 minutes or so and it's always really high quality
so we are very very very lucky that we get such a high volume of feedback before products even
get out the door once products are shipped we
look at feedback from both our early enterprise adopters and also occasionally from twitter
um I think our enterprise adopters are probably the highest signal for me right now there's about
10 companies that we work very closely with who are who we tell hey just be just be as loud as
possible like if you run into any issue please put it in the chat we might not be able to fix
it immediately but we want to hear about it we appreciate it
please please please share negative feedback we're very insistent that we love negative feedback
like we don't want platitudes we want to hear what doesn't work and thankfully uh these users
are both very engaged with cloud code and very happy to share what's not working for them
and we've held ourselves to a pretty fast SLA for fixing a lot of um a lot of these issues so
so for issues that we decide to prioritize and decide to fix
we'll turn it around and we'll see what happens next.
you know like in a more traditional company like the PM has to maintain a bunch of artifacts right
like specs and roadmaps and maybe like the vision doc or something and and uh uh and also like keep
track of the feedback so do you have any of those stuff or like do you use cloud to summarize all
the feedback or how do you yeah yes um it's an interesting question we actually get so much
feedback that we don't have a lot of feedback so we don't have a lot of feedback so we don't have
what we should prioritize become pretty clear because you'll hear it ten times i know this
isn't an super satisfying answer i wish i could just say hey we like
rank we track every single thing and we like rank it all yeah but i think in practice what happens is
we get someone post a github issue and they say something's broken and then
there's like a hundred thumbs ups on that github issue and then our sales team deals with them?
us and says, hey, like for these three customers, this thing is broken. So normally when something's
a really high priority, it's very, very obvious. There are a few ways in which I do use cloud code
though to help me with this. So one is we've connected cloud code with Slack. So it's really
easy to synthesize feedback. So for example, if one customer asks us for the ability to customize
models by sub-agent, I'll just ask cloud code, hey, which other customers have asked for this?
That way I know when it's built, we're telling the right people that we've done it. And then I
also can ask cloud code, hey, like also look at our GitHub issues and see if there's any GitHub
issues about this. That way when it's built, we close out all the GitHub issues. We also use
cloud code to automate as much of this handling as we can. So for example, cloud code will help
us update the docs. So it'll do a lot of work. And then we can also use cloud code to automate
a first pass at docs, and then we'll clean up the remaining 10% to make sure it's very accurate.
So humans still reviews it. And then we also use cloud code to deduplicate issues on GitHub.
For a lot of issues, we see five or more cases of it being filed over and over again. And so
this helps us just maintain the backlog and make sure that our community is kept in state.
You probably have all your documents in like .md files, right? You don't have any Google Docs.
Right?
I just have one there. Yeah.
We don't use many Google Docs for cloud code. No.
Okay.
It's also nice because our code base is actually pretty small. And so even if like, I think
normally people use Google Docs to document functionality or why we built something. And
I think for a lot of cloud code features, the why we built it is sometimes it's just like
in the PR. And so...
If you ask it, hey, what was the original inspiration for to do list, search GitHub, it will be able to just find the original PR and like tell you it. And because the code base is small, if you actually want to know exactly how something's implemented, it's actually a lot faster and more accurate to ask cloud code while it's initialized in that repo, rather than read a doc that might be out of date.
Yeah, that's a really good point. Because the source of truth is the code base, right? And like, you know, this model is really good at summarizing stuff in a code base. So...
Totally. Yeah. And the code base is small. So...
Do you check code yourself? Like make some copy tweaks? Or do you check features? Yeah.
Yeah, I do. So I used to do this a lot more when I first joined as the PM. And there's always like
smaller features that are just faster for me to do than for someone else on the team to jump in on.
So like, two months ago, we had this collaboration with Rick Rubin about Vibe code.
And he, one of the ideas from our brand team is that we should have a Vibe command that referenced some of Rick Rubin's writing about the topic.
And so it was just much easier for me to add it than for someone on the team to add it. And so just like take that on.
And we've also seen this with other folks on our team, like Megan, who's our amazing designer.
She used to never commit code, which is very normal for a product designer.
And when she started...
Using quad code more, she started making PRs to console, which is our management...
It's our product for managing API keys and other API usage. And she's also made PRs to quad code itself.
And so it definitely lowers...
Quad code definitely lowers the barrier for everyone to make PRs, especially for some poor changes.
Yeah, that's amazing. I mean, like that is a dream, right? To be able to, for designers and PMs, to check in code directly,
make an impact.
Yeah, that's amazing. I mean, like that is a dream, right? To be able to, for designers and PMs, to check in code directly, make an impact.
Yeah, that's amazing. I mean, like that is a dream, right? To be able to, for designers and PMs, to check in code directly, make an impact.
on the end user experience without just writing a bunch of Google Docs.
Yeah, totally. And it also makes it easier to audit flows too, because we have a lot of branching logic.
So for example, if you're on a max plan, there's a lot of conditions where we'll like show you a rate limit warning or like show you an upgrade message or...
And this differs based on every plan that you might be on, whether you're on 1P API or 3P API or Cloud for Enterprise or Prosumer.
And this differs based on every plan that you might be on, whether you're on 1P API or 3P API or Cloud for Enterprise or Prosumer.
And this differs based on every plan that you might be on, whether you're on 1P API or 3P API or Prosumer.
And so Cloud Code also makes it really easy to audit these flows because you can just ask it, okay, trace the code for each of these and tell me exactly what happens.
And then you can feel pretty good that it's accurate if it comes back accurate.
Got it. Okay.
It's probably the entire team talks to Cloud Code the most during the day.
Yeah.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Let me ask you, there's been a lot of hot takes about evals recently on Twitter.
Some people say it's like, you have to have like super robust evals before you launch anything.
Some people are like, ah, whatever.
Like, how do you guys think about evals and run stuff before you ship?
Yeah, evals are really hard.
So there's two kinds of evals that we care about, and they're both imperfect and we're trying to get better at both.
So the first is end-to-end evals.
So you can think of this as running SweetBench on Nucleus.
You do quad-code harnesses to make sure that we're not degrading performance.
And so this is something that we regularly do, both when we're making large changes to the harness and when we're testing out new models.
This isn't that granular.
So if you, for example, see a change in the SweetBench score, it's not always obvious what caused the change,
and you actually have to read through these pretty gnarly transcripts and a lot of them to be able to figure out themes and what went wrong.
We want to make this better, but we don't have a silver bullet right now.
The other kind of eval that we think is really important to make is triggering evals.
So what that means is there's a lot of situations where Cloud Code can decide whether or not to use a tool.
And ideally, Cloud Code can make these decisions without the human.
That way, things just feel more magical to the human.
So, for example, Cloud Code supports web search.
And we want to make sure that web search isn't overly eager.
If you ask it a question, you don't want it to search the web 100% of the time.
But you want it to search it if you're saying, hey, what was the latest React release?
And what new functionality is available there?
And so actually tuning this triggering is pretty hard to do.
And so this is a situation where both is really straightforward to make an eval because you know, you can clearly articulate when web search should and shouldn't happen.
And then it's also really easy to grade whether or not web search did happen.
Got it.
The harder evals are capability ones.
Like what kind of capabilities?
Like, give me an example.
Yeah.
Yeah.
So if you want to evaluate, hey, is this harness better?
It's data science work than the last one that is actually much harder to test, because you would actually want something closer to a sweep bench like setup where the model has access to really big underlying data set has the ability to write queries against the data set, iterate on those queries.
And you have, you need to have a gold standard answer.
And you need to make sure that there's no ambiguity in what the right answer is.
Yeah, got it.
Okay.
the web search one um you just kind of look at the like maybe look at the past uh when the web
search was triggered and see if it makes sense or not and maybe have a score or something is that
kind of how it goes yeah yeah so there's for web search there's a spectrum of when web search should
never trigger and when it should always trigger and so to start i'd recommend codifying the black
and white areas in an eval there is always a gray area and i would probably just take care of those
afterwards yeah and and i mean the truth is like you have such an engaged community that like
your users are keeping you honest all the time right like so you can look at some scores but
like your users are just keeping you honest about what is working and what is not working yeah that's
true yeah like even for to-do list we spent quite a bit of time making sure that it was triggering
well because sometimes
cloud code would want to write a to-do list for one item and then check it off
and this is a clear case where a to-do list shouldn't have been used because you don't
really need this form factor to track getting done one task just do the task got it this is
a situation where an eval would have been really helpful like you can make sure that you can take
the trajectory where the agent created to-do list for one task put it into your eval suite
and then make sure that either the agent
doesn't make a to-do list item
or if it does make a to-do list item
that it's like three or five items.
Kat, can you tell me some interesting stories?
I mean, you've been on this journey of Cloud Code Team, right?
Is there any some like interesting stories
that the team laughs about?
You know, like, you know,
I think I heard a story about you guys shipping a feature
during a meeting.
Tell me some fun stories on the Cloud Code Team.
Yeah.
Yeah, when I think about the team,
I think of just like,
just people who absolutely love developers.
Some of our favorite memories are when we first launched,
we wanted to thank our earliest users.
And so if anyone accidentally mentioned the word swag
or stickers while they're using Cloud Code,
we would send them, Sid built this,
we would send them to like a sticker portal
where they could enter their address
and we would actually mail them a sticker,
a set of stickers.
And someone actually reverse engineered the code
or like looked at our source maps or something
and found this.
And as a result, we got like 500 or so inquiries
where people were like submitting their addresses.
And it was just like a cute little thing that,
a cute little Easter egg
that we wanted to embed into the product.
Like for no other reason than to just like,
thank our earliest, most engaged users.
Yeah.
We thought that it would only take an hour for,
some of us do send 500 stickers,
but instead it actually probably took us eight hours.
Wow.
Okay.
And then we just,
we were originally going to make dumplings
and we ended up just ordering takeout
and mailing stickers the whole time.
Wow.
Okay.
It's probably have to remove the feature afterwards
because you don't want to be sending stickers all day.
Yeah.
We thankfully did cap it at,
I think around 500 or so.
Well, send me a sticker after this.
I want a sticker.
Yeah.
Oh, we have a lot.
We've been iterating on them.
Now we have think harder stickers and ultra think.
And there's, there's a bunch of memes, right?
Like for example,
cloud code will be like,
they'll make,
it'll make a to-do list.
And I'd be like,
Oh, it'll take,
it'll take an engineer.
It'll take me like two weeks to do this.
And I just,
I was like in like 10 minutes.
Yeah.
I've seen that happen before.
Yeah.
Yeah.
We need to teach it a better sense of time.
I think it's quoting human hours.
And then it just does it.
Cause I think it's only seen,
human hours on the internet.
So,
I mean,
it sounds like there's some pretty good vibes on the team.
And I know you're hiring a PM for the cloud code team.
You know,
what kind of person is looking for and what does the interview process look
like?
We're looking for someone who loves developers,
just like was like,
ideally has been a developer before,
or has worked on developer tools for a while.
Ideally,
we'd love to have someone who wants to make sure the SDK,
the cloud code SDK is the best way to build agents.
We want to create more agents in the world.
And we think the cloud code SDK is the fastest way to prototype an
agent and bring it to production.
And we're also looking for someone who wants to grow the ecosystem.
So we've noticed a lot of developers are customizing their setups.
They're building custom slash commands and custom hooks and status lines.
And we want to have like a hub where people can share all of this.
Where people can review each other's customizations,
where someone can one quick install it to their own quad code instance.
So I would say we're looking for someone who's both able to steward the
SDK as the best way to build agents and to,
to grow the community,
to make it,
to make these customizations easily shareable.
So probably someone who's already pretty like into cloud code then.
Yeah.
We're definitely looking for a power user.
Yeah.
Yeah.
And do you guys maybe for cloud code,
just anthropic in general is there like a,
like during any review process,
is there like,
Hey,
can you build something here?
Or like,
you know,
can you add a fee feature using cloud code or is there some live
demonstrations involved?
Ooh,
maybe we should do that.
We do ask folks to spend a bit of time in the products and give a
critique of what they will would like to see improves.
Okay.
I think normally we can get a pretty good sense for how,
engage someone really is in the tool uh based on that but that would be fun yeah or look for people
who are like making tutorials on youtube you know that's okay yeah totally yeah okay so uh let's
kind of let's do a lightning round i want to hear kind of like uh some some tips on how to get the
most out of cloud code right and maybe how you use it personally yeah the three tips i would share
are one demos not docs cloud code makes it so easy to make prototypes that if you're thinking
about hey should we build this feature i i would actually ask hey is there a way that for quad code
to prototype that feature for you so that you can get a feel for how useful it is before writing
a multi-page doc on it the second thing is i would treat quad code as an eager
new grad software engineer
so i would think of it as something called code as a tool that's very responsive to feedback i
sometimes see people give quad code a really ambitious prompt and then when quad code makes
wrong assumptions they kind of give up but instead i would say if you notice quad code's doing
something wrong just tell it that it's doing it wrong the same way that you would give feedback to
to a human and it's really receptive and will normally
change its
direction and incorporate that feedback and then the third thing is there's a ton of value in
investing in your quad md file quad md is the equivalent of memory for quad code every time
you start a quad code instance the quad md is included in it so you can kind of think about it
as eng onboarding it's everything that you would tell someone who's new to your code base and who
you want to be productive off the bat so it's a great place to
mention your code base and who you want to be productive off the bat so it's a great place to
mention the architecture of your app any gotchas how you like to test and verify work anything
that you would tell a new hire there's kind of like two approaches to cloud md right you can
just type slash init and they'll like scan the code base for you and add a bunch of stuff but uh
i i kind of like how megan uses it she she has like a she's like i'm a prod designer you gotta
like over explain everything to me like it's kind of like a more per personal like style kind of
yeah yeah yeah totally so the whole thing is about how you can test and verify work anything that you
want to be productive off the bat so you can have a whole system is very configurable and so you can
have a quad md for the entire repo and then you can also have your fully individual quad md and
in megan's case for for a quad md that describes who you are and your role at the company and that
applies to all projects you can also have a global personal quad md so that cloud code has this
context no matter what repo it's working in got it got it okay and in terms of the
in terms of like the the second tip that you shared about treating as an over-eager engineer
i i found that like the more time you do planning actually the better the results are so like so
like actually making it right like a pretty detailed spec about what you want to build
and like looking over it and then also like asking it to like make a to-do list and then
looking over that you know that that's that's been super helpful for me yeah totally our users
love plan mode so actually yeah maybe a funny story
is we originally knew that people wanted plan mode because people kept saying
hey just like tell me what you're going to do but don't write code yet and we kept being resistant
to adding plan mode because we wanted to teach users to express what they wanted in natural
language and when you do express in natural language cod will make a plan for you even
outside of plan mode over the course of one or two months
enough users said that they just wanted to be really explicit that they wanted a shortcut to it
that we caved and said okay okay well we'll add an explicit plan mode but we were really hoping
that we could teach users to directly ask the model to plan and maybe maybe in the future when
the model is better at following these kinds of user directions we might we might remove it
uh yeah i mean
it's just like the models these days are just too eager to code like it's like even even in plan mode
when i'm like hey can you make a plan for me and then it'll make a plan they'll be like oh by the
way i can start coding right now do you want to start coding stop coding i gotta review your plan
first yeah so it's just too eager i think yeah yeah totally do you have like a vision doc or
something for cloud code or like what do you think the product will look like a year or two from now
a year or two is a really long time yeah i can talk about the next few months
so we we want to make sure that the cli continues to be the most powerful coding agent and we also
want it to be incredibly customizable so that it can work in any developer environment it can
integrate with all your existing tools and you can and that we create an ecosystem around the
customizations the second pillar is we care a lot about growing the sdk so in general we would love
to be more agents in the world not just coding agents but legal assistants ea asset like personal
assistant ais health health assistant ais financial assistance stuff like this and we hope that the
cloud code sdk actually makes it easier for all the companies building general agents to get started
and we're seeing the initial signs of this there's many companies that we're working closely with who
who are building non-coding agents on the SDK.
We want to make sure these companies are incredibly successful
and will tell their stories as their products come to market.
And the third bucket, which is the most amorphous,
is bringing Cloud Code out of the terminal
and making it more accessible to more audiences.
So right now, we primarily target professional developers.
We will continue to focus on professional developers
because that's the core market of Cloud Code.
But increasingly, we find that it adds a lot of value
to tech-adjacent folks.
So data science, product management, product design.
And we would ideally like a form factor
where these folks can get value too.
And increasingly, to expand out by another ring
to folks in marketing, folks on sales,
who we think will also benefit.
Yeah, because people in the anthropological designers,
marketers.
are all using this stuff, right?
There's a few.
We want to onboard more.
Right now, it's still really hard to explain a terminal interface
to folks who haven't used it before.
But I think the core primitives are very general.
So I'm very excited for the future.
And doesn't it require, like, you know,
I just did a recording of Alex, right?
Who basically runs his life.
Like he runs a bunch of tasks using Cloud Code.
And you don't need to have like some crazy prompting.
You just have to talk to Cloud to figure this stuff out.
Yeah.
Just be like, can't do this for me.
You just tell it.
And if you're confused, like,
I recently onboarded one of the folks in our marketing team
onto Cloud Code.
And she was like, you know, I've never written code before.
I don't even know.
I don't know what I should ask.
And I was like, okay, just ask it to build an app.
And then Cloud Code goes with like some purpose.
And Cloud Code goes off to build an app.
She's like, okay, I have no idea how to run this app.
And so I told her,
like, hey, you can just ask Cloud Code.
And she did.
And I told her how to run it.
And she was like, whoa, you mean any question I have,
I can just ask?
And I'm like, yeah.
And it's really cool because it kind of just works.
Yeah, yeah, yeah.
And I love how you guys shift explanatory style
to kind of like help people become more technical too
as they're using this stuff.
My one feature request actually is like
to be able to use Cloud Code for my phone.
Because like this stuff is very agentic, right?
Like it will work for like 10 minutes.
And I can just go like play with my kids.
So have some sort of like, you know,
thing later on the phone.
What would be really, really cool.
Totally.
I agree.
This is also why we built,
our original inspiration for Hooks
is kind of related to this.
A lot of people wanted to get Slack notifications
when Cloud Code was waiting on their response.
Yeah.
So, yeah.
So Hooks made it customizable.
So for example, if you wanted to get a text message
every time Cloud Code was waiting on you,
you could.
You could configure a hook for that.
But I also hear you on the broader request
to run it remotely.
Yeah.
I haven't, I haven't played with Hooks yet.
I still have the list of features to dive into.
But yeah.
You know, I, I love how you said like, you know,
two or three years is too long.
You know, you know, what's ironic, just to close.
Like, I feel like the most innovative teams like,
like yours are just kind of iterating.
And then some of the more traditional teams are like,
oh, we're going to have like a three-year vision.
And we're like, go there.
It's like, it feels like very, you know, that, that, that's just
kind of the feeling that I get, like, just, just put yourself
out there and like, you know, iterate with your users.
Like that's how you build innovative stuff.
I agree.
We're very pragmatic.
So we, we try to build the products that we wish we had today.
And because the models are changing so quickly, we think that it's really
hard to predict more than six months in the future, but I think it's really
important to build products for the next generation of models.
Yeah.
But generation.
Capabilities don't become obvious until a few months ahead of time.
So I don't know how people plan further than that.
Yeah.
Yeah.
Okay.
So like any closing words or advice for the PMs out there, you know, trying to
become AI PMs or like, you know, any, any kind of advice you have?
Yeah.
The hardest thing to learn about being an AI PM is having a really good
grasp of what the models are capable of.
There's.
It's hard to believe.
So I think the way that we build evals at the end of the day, a lot of it comes
down to intuition, like if you want to build a feature, you should probably
actually have a really good sense of intuition for whether or not the model
is capable of supporting that feature.
And if not, how far.
Away is the model, is the model 80% there and you can prompt the last 20% or is
the model only 10% of the way there?
In which case you should actually probably just check back in, in three months or six months.
Yeah, yeah, yeah, this is the hardest skill and the rarest skill.
And I think you have to have that curiosity to push the model, right?
To try to make something happen that, you know, can't do this or not.
Just try to make it work.
Yeah.
Yeah, exactly.
Like you have to know if the model fails, is it because the context is wrong?
Is it because you're not, you're using maybe the wrong model for the task or is
the model at the core on not capable of it?
Got it.
Okay.
That's really good advice.
Yeah.
Um, all right.
So where can people find you online or do you want people to, you know, where can people
give you feedback about Cloud Code?
Yeah.
So two places, either underscore C-A-T-W-U on Twitter, or if you have a technical feedback,
please feel free to open a GitHub issue and we'll, we'll look into it.
Okay.
All right, Kat, this is awesome.
I really learned a lot talking to you and I'll be using Cloud Code more and more.
I'm sure.
Thank you for your support.
And as you have more feature requests,
please let us know.
