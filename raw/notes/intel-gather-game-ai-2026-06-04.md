# /intel-gather：游戏工作室利用 AI 提效的证据汇总

采集日期：2026-06-04

本素材由 5 个并行 agent 工作包汇总而来，用作 `wiki/` 层的原始情报副本。原始 agent 输出位于外层工作台 `runs/intel-gather-game-ai-20260604/agent_outputs/`。

## 工作包

- A 量化提效：EA、King、Roblox、Unity、Layer。
- B NPC/叙事/语音：Ubisoft、KRAFTON、NVIDIA ACE、Inworld、Embark、CDPR/Respeecher。
- C 资产/美术/3D/关卡管线：Scenario、Layer、EA/Stability、Roblox、NetEase、Tencent、Capcom、Unity。
- D QA/测试/运营/内部工具：King、Square Enix、Capcom、Keywords/Helpshift、modl.ai、Unity。
- E 行业报告与方法论：GDC、Unity、Google Cloud/Harris、a16z、Perforce、CB Insights、Naavik、Steam 披露数据。

## 核心发现

1. 最硬的量化证据来自生产管线和 QA，而不是“AI 自动做完整游戏”。
   - EA 披露体育场制作从约 6 个月缩短到 6 周。
   - King/Candy Crush 的 AI playtesting bot 被披露为减少 95% 手工关卡调整，并让关卡 tweak 提速 50%。
   - Roblox Code Assist 和 agentic creator tools 提供平台级采用数据。

2. 真正进入生产的 AI 多数落在低风险、可复核、可指标化环节。
   - 研究/脑暴、代码辅助、QA、自动 playtesting、本地化首稿、客服分流、live-ops/UA 素材、2D 资产草稿最稳定。
   - 玩家可见的最终美术、开放式 LLM NPC、最终语音和运行时生成内容仍有版权、授权、质量、延迟和安全边界。

3. NPC、叙事和语音的成熟度分层明显。
   - TTS/语音修复和受限 AI 角色更接近真实落地。
   - Ubisoft Neo NPC、KRAFTON CPC/PUBG Ally 等代表方向，但不少仍是 prototype、playtest 或计划上线。
   - 可复制流程不是“AI 写剧情”，而是人类设定角色、知识、边界和安全规则，AI 生成候选或实时表达，人类复核。

4. 资产管线最可落地的是“前半段”和“子流程”。
   - 2D live-ops、营销素材、装饰资产、概念探索、变体生成、PBR 贴图、自动绑定、动画插帧、灯光烘焙、资产优化更可信。
   - 3D 不是一键成品，仍需要 DCC 工具修整、拓扑/骨骼/LOD/碰撞/性能优化和美术审核。
   - Capcom 的公开立场很有边界感：AI 可用于想法、参考、调试和测试，但不把 AI 生成资产直接放进最终游戏内容。

5. 行业采用率高度分裂。
   - GDC 2026 显示 36% 从业者使用生成式 AI，52% 认为它对行业有负面影响。
   - Google Cloud/Harris 大型公司样本显示 90% 已把生成式 AI 纳入工作流。
   - Unity 报告显示开发者使用集中在代码辅助、写作/叙事、NPC 行为、市场研究、概念美术、自动化测试等。

## 高价值证据

| 公司/机构 | 落地环节 | 证据内容 | 状态 | 可信度 |
|---|---|---|---|---|
| EA SPORTS | 体育场/环境资产 | 体育场制作从约 6 个月缩短到 6 周。 | 已落地 + 高管披露 | 高 |
| EA SPORTS College Football 25 | 体育场、球员 likeness | 150 个独特体育场、11,000+ 球员 likeness；AI/ML 被披露为关键支撑。 | 已落地 | 高 |
| King / Candy Crush | AI playtesting bot | 手工关卡调整减少 95%，关卡 tweak 提速 50%。 | 已落地 | 中高 |
| Roblox | Code Assist / creator tools | Code Assist 被采纳约 535 million characters；44% top 1,000 creators 使用 Assistant 或 MCP AI 工具参与 plan/build/test。 | 已落地 | 高 |
| Ubisoft | Ghostwriter / Neo NPC / Teammates | barks 草稿、生成式 NPC、语音驱动 AI 队友。 | 工具/原型/研究项目 | 高 |
| KRAFTON + NVIDIA ACE | PUBG Ally / Smart Zoi / CPC | AI teammate、on-device agent、生活模拟角色行为。 | playtest/计划/部分上线 | 高 |
| Embark / The Finals | AI/TTS 语音 | 游戏内语音使用 AI/TTS，引发演员授权和创作争议。 | 已上线 | 中高 |
| CDPR + Respeecher | 本地化语音修复 | 在家属授权下复现已故波兰配音演员声音。 | 已上线 | 高 |
| Layer 客户案例 | 2D/live-ops 资产 | LBC、Fortune Mine、Cosmic Lounge 等案例披露 2D 资产生产提速。 | 已落地但供应商披露 | 中低 |
| Capcom | 内部流程 | 用于想法、调研、参考、调试、测试，不把 AI 生成资产直接放进最终游戏。 | 公司级计划/实践 | 中高 |
| Square Enix | QA/debug automation | 计划与大学合作推进 QA/debug 自动化。 | 计划/合作 | 中 |
| Keywords/Helpshift | 客服自动化 | SYBO、Rovio 等移动游戏客服分流和自动化指标。 | 已落地供应商案例 | 中 |
| GDC 2026 | 开发者调查 | 36% 使用生成式 AI，52% 认为负面影响。 | 行业调查 | 高 |
| Google Cloud/Harris 2025 | 大型游戏公司调查 | 90% 使用生成式 AI 工作流。 | 行业调查，大厂样本 | 中高 |

## 主要来源 URL

- EA Q4 FY24 Transcript: https://s204.q4cdn.com/701424631/files/doc_financials/2024/q4/Q4-FY24-Transcript-FINAL.pdf
- EA Q1 FY25 Prepared Remarks: https://s204.q4cdn.com/701424631/files/doc_financials/2025/q1/Q1-FY25-Prepared-Remarks-FINAL.pdf
- GameSpot on College Football 25 AI: https://www.gamespot.com/articles/ea-says-cfb-25-would-not-have-been-as-good-without-the-developers-using-ai/1100-6525428/
- King / Candy Crush AI playtesting: https://www.gamesindustry.biz/how-king-is-using-ai-to-speed-up-development-of-new-candy-crush-levels
- AP on King AI: https://apnews.com/article/547254aaa06bf026df5b41458ac62dcc
- Roblox Code Assist: https://devforum.roblox.com/t/code-assist-full-release-ai-powered-code-completion/2848978
- Roblox Road to 4D Generative AI: https://corp.roblox.com/newsroom/2024/06/robloxs-road-to-4d-generative-ai
- Roblox Studio going agentic: https://about.roblox.com/en-nz/newsroom/2026/04/roblox-studio-going-agentic
- Ubisoft Ghostwriter: https://news.ubisoft.com/en-au/article/7Cm07zbBGy4Xml6WgYi25d/the-convergence-of-ai-and-creativity-introducing-ghostwriter
- Ubisoft Neo NPC: https://news.ubisoft.com/en-ca/article/5qXdxhshJBXoanFZApdG3L/how-ubisofts-new-generative-ai-prototype-changes-the-narrative-for-npcs
- Ubisoft Teammates: https://news.ubisoft.com/it-it/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates-an-ai-experiment-to-change-the-game
- KRAFTON PUBG Ally: https://www.krafton.com/en/news/press/krafton-reveals-playtest-plans-for-pubg-ally-built-with-nvidia-ace/
- NVIDIA ACE autonomous companions: https://www.nvidia.com/en-eu/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/
- Inworld case studies: https://inworld.ai/customers/astrobeam
- Embark / The Finals AI voice: https://www.axios.com/2023/10/31/the-finals-embark-ai-voice
- CDPR / Respeecher: https://www.respeecher.com/case-studies/how-respeecher-and-cd-projekt-red-preserved-the-voice-of-cyberpunk-2077s-viktor-vektor
- Scenario case studies: https://www.scenario.com/case-studies/mighty-bear-games
- Layer customer stories: https://www.layer.ai/success-stories/lbc-studios
- EA + Stability AI: https://www.ea.com/amp/news/ea-partners-with-stability-ai
- Roblox AI avatar/texturing: https://about.roblox.com/tr/newsroom/2024/03/roblox-introduces-ai-powered-avatar-and-texturing-technologies-to-accelerate-3d-creation
- Capcom + Google Cloud: https://cloud.google.com/blog/ja/topics/customers/capcom-generating-ideas-with-generative-ai
- Square Enix QA automation release: https://web.hd.square-enix.com/eng/news/pdf/20251106_01_en.pdf
- Keywords / SYBO Helpshift: https://www.keywordsstudios.com/en/case-studies/sybo-increase-csat-automation-rate-with-helpshift/
- Unity virtual players: https://unity.com/blog/games/automate-your-playtesting-create-virtual-players-for-game-simulation
- GDC 2026 State of the Game Industry: https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/
- Unity Gaming Report: https://unity.com/resources/gaming-report?isGated=false
- Google Cloud games report: https://cloud.google.com/resources/games-report
- Naavik: https://naavik.co/digest/the-state-of-genai-in-game-development/

## 待核验点

- EA “6 个月到 6 周”的体育场口径：样本量、资产类型、团队规模、外包比例、AI/自动化/资产复用各自贡献。
- King 95%/50% 数字的原始采访全文和是否有官方 slide。
- Layer 客户案例中的 8x、+72%、4x 等数字是否有客户二次确认。
- Google Cloud/Harris 90% 采用率来自大型公司样本，不可外推到独立工作室。
- GDC 2026 与 Google Cloud/Harris 采用率差异大，需要在引用时明确样本范围。
