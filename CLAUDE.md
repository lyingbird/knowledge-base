# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project**. It is a Chinese-language personal knowledge base (an Obsidian vault) maintained according to Karpathy's **LLM Wiki** method. The core idea: don't accumulate isolated notes or treat this as a one-off RAG folder. Instead, *compile* source material once into a structured, cross-linked, traceable wiki, then keep that wiki continuously updated as new material and questions arrive.

Working directory root is `D:\工作\Wiki知识库`; the vault itself lives in `knowledge-base/` (a git repo). All work happens inside `knowledge-base/`.

Content, links, and prose are in **Chinese**. Match that when writing pages.

## Three-layer architecture

The single most important thing to understand before editing anything:

1. **`01-原始素材/` — raw source layer (source of truth).** Original material or immutable copies (articles, transcripts, tweets, wechat/zhihu/xiaohongshu, PDFs, repo notes). Claude may *read* these but by default must **not modify** them. To correct something, record it in `03-核验/待核验事实.md` and the relevant `02-知识库/素材/` page rather than rewriting the raw copy. Historical video notes live in `01-原始素材/视频笔记/` as immutable copies.
2. **`02-知识库/` — LLM-maintained layer.** Everything here is generated and continuously maintained by the LLM: source summaries, entity pages, topic pages, comparisons, synthesis, and graph data. New material must be *integrated* into existing pages here, not just appended as a new file.
3. **`知识库规范.md` + `AGENTS.md` — the spec layer.** These tell the LLM how to maintain the base. **Read both before doing substantive work** — they are the operating manual and take precedence over this file for domain rules. Evolve the schema when you discover new naming/linking/verification/graph conventions.

`00-入口/`, `04-历史主题/`, `05-历史视频笔记/`, `03-核验/` are the legacy human-reading layer. **Do not delete legacy notes** to restructure — the new `02-知识库/` layer gradually reorganizes them.

## The `02-知识库/` layer

- `02-知识库/素材/{日期}-{短标题}.md` — one summary page per source (origin, core points, to-verify points, links).
- `02-知识库/概念/{名称}.md` — reusable people, orgs, concepts, tools (e.g. `[[AI原生公司]]`, `[[企业上下文]]`, `[[智能密度]]`).
- `02-知识库/主题/{主题名}.md` — cross-source themes.
- `02-知识库/综合/`, `02-知识库/对比/` — cross-source synthesis / comparison reports.
- `02-知识库/知识库总览.md`, `总索引.md`, `操作日志.md` — global overview, master index, operation log.
- `02-知识库/知识图谱说明.md` — static Mermaid graph.
- `02-知识库/知识图谱/图谱数据.json` + `02-知识库/知识图谱/知识图谱.html` — offline interactive graph. The HTML is a self-contained viewer driven by the bundled `graph-wash.js` / `graph-wash-helpers.js` runtime (plus vendored `d3.min.js`, `marked.min.js`, `purify.min.js`, `rough.min.js`). **Do not hand-edit these vendored/generated files.** `graph-data.json` is derived from the wiki Markdown double-links; regenerate it (and the HTML) with the external `llm-wiki-skill` graph-build scripts (`build-graph-data.sh` / `build-graph-html.sh`) — they are not vendored in this repo.

## The ingest workflow (the main task)

When adding new material, **a summary page alone is never sufficient.** Follow `raw → sources → entities/topics → index/log → graph`:

1. Save/locate the raw material under the correct `01-原始素材/` subdirectory.
2. Create a `02-知识库/素材/` summary page.
3. Extract 3–5 key concepts into new/updated `02-知识库/概念/`.
4. Attach to and update relevant `02-知识库/主题/`.
5. Check whether the new info **contradicts, corrects, or strengthens** existing judgments, and mark that on the affected pages.
6. Update `总索引.md` and `操作日志.md` (log every add/migrate/synthesize/delete).
7. Update `02-知识库/知识库总览.md` if the big picture changed.
8. Regenerate `02-知识库/知识图谱/图谱数据.json` + `02-知识库/知识图谱/知识图谱.html` when the knowledge network changed, and re-check that double-links in `总索引.md`, `02-知识库/知识图谱说明.md`, and `操作日志.md` all resolve.

**High-risk facts** (numbers, company cases, research conclusions, paper citations, funding/valuation/performance metrics, acceptance status) go into `03-核验/待核验事实.md` first and stay there until independently verified — do **not** promote them into synthesis conclusions before verification.

For GitHub / open-source-project material, use the dedicated ingest spec in `知识库规范.md` ("GitHub / 开源项目学习素材 Ingest 规范" and "项目学习页结构"): copy key info to `01-原始素材/开源项目/{owner}-{repo}.md`, and every project source page must include a runnable hands-on checklist (install / run / reproduce, with hardware/dependency constraints).

There is also a **high-fidelity video ingest** path. Read `00-入口/B站视频蒸馏SOP.md` before processing Bilibili or other long videos; `AGENTS.md` contains the mandatory gates. It is triggered when the user says a video's "精华/不要省略/精校准/尽可能保留信息", and also for multi-speaker, slide/demo/gameplay, or high-risk material. Preserve immutable raw evidence, page/cid identity, timestamps, visual evidence when needed, claim-level provenance, attribution boundaries, and rollback.

## Linking & naming conventions

- Use Obsidian double-link syntax `[[真实页面名]]`. New wiki-layer links prefer short page names (`[[智能密度]]`); links to legacy notes keep the path (`[[05-历史视频笔记/...]]`).
- Every entity/topic page maintains a "相关页面" (related pages) section at the bottom.
- Page front-matter format (tags/created/updated/sources) is specified in `知识库规范.md`; follow it.
- Watch for **synonyms** — `知识库规范.md` has an alias table (e.g. `AI原生公司 = AI原生组织`, `agent = 智能体`). Don't create duplicate near-synonym pages.

## Lint (health check) — what "broken" means here

There is no test suite. Correctness is graph/link health, checked per `知识库规范.md`:

- **Orphan pages** (no in/out links), **broken links** (double-link to a nonexistent page).
- **Index inconsistency** (`总索引.md` misses important pages).
- **Duplicate concepts** (multiple near-synonym pages for one concept).
- **Unverified high-risk facts** not routed to `03-核验/待核验事实.md`.
- **Stalled synthesis** (new material not reflected into entity/topic/synthesis pages).
- **Source islands** (`02-知识库/素材/` pages that link only to raw material, not to any entity/topic).

## Reporting

When reporting after an ingest, report **against verified output**, not intentions: transcript completeness, worker coverage, graph node/edge counts, lint/validate result, and commit/push status.
