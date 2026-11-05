---
tags: [实体, 软件工程, AI研发提效, 规范驱动]
created: 2026-06-07
updated: 2026-06-07
sources: [麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]
---

# Spec-driven development

> Spec-driven development 是把“人写模糊 story、AI 写代码”改造成“人和 AI 先对齐规格、约束和验收标准，再生成方案、测试与实现”的开发方式。

## 核心内容

[[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]] 中，McKinsey 原演讲明确指出高表现企业正在从 story-driven development 转向 spec-driven development：PM 与 agents 迭代 specs，而不是反复打磨长 PRD。B 站解读进一步把它称为 SDD，并强调从代码中心转向规范中心。

Spec 不是文档主义。它是人类意图、系统边界、质量标准和 agent 执行之间的接口。没有 spec，AI 写得越快，review 和返工越多；有 spec，AI 才能把实现、测试、影响分析和回归检查串成可复用流程。

## 最小规格内容

- 要解决的问题和不解决的问题。
- 业务规则、边界条件和失败场景。
- 数据、权限、安全、性能和合规约束。
- 可验收的行为和测试用例。
- 与既有系统、接口、依赖、架构分层的关系。
- 人类必须复核或批准的节点。

## 风险

- 只把 prompt 写长，不等于 spec-driven。
- spec 如果不连接测试、review 和 CI/CD，只会变成另一份 PRD。
- GitHub Spec Kit、Specify / Plan / Tasks / Implement 等具体方法来自 B 站扩展，引用前应独立核验。

## 相关页面

- [[后敏捷操作模型]]
- [[AI原生工作流]]
- [[AI研发提效]]
- [[企业上下文]]
- [[智能体]]
- [[麦肯锡：AI 时代，旧的敏捷开发方式正在拖累个人效率]]
