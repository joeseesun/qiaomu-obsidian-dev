# qiaomu-obsidian-dev

插件编译通过了，真实 Obsidian 里却重复执行、写错文件、状态过期、内存增长或发布后无法安装？这套 skill 为命令、编辑器、视图、索引、导入导出、同步、媒体和 AI 插件提供同一套架构判断与证据门禁，再按类型加载专项规则。

[![Install](https://img.shields.io/badge/skills-install-315a42)](https://github.com/joeseesun/qiaomu-obsidian-dev) [![Stars](https://img.shields.io/github/stars/joeseesun/qiaomu-obsidian-dev)](https://github.com/joeseesun/qiaomu-obsidian-dev/stargazers) [![Issues](https://img.shields.io/github/issues/joeseesun/qiaomu-obsidian-dev)](https://github.com/joeseesun/qiaomu-obsidian-dev/issues) [![License](https://img.shields.io/github/license/joeseesun/qiaomu-obsidian-dev)](LICENSE)

```bash
npx skills add joeseesun/qiaomu-obsidian-dev
```

一次网络搜索插件的交付样例：

> 原因：旧查询迟到后覆盖当前条件。修复：每次请求绑定查询快照和代次，取消或丢弃旧结果。验证：慢网快速切换、空结果、认证失败和重载恢复。发布：GitHub 已发布；官方审核排队，不能称已上架。

## 你可以直接这样说

- “开发一个把当前笔记属性同步到任务服务的插件，先调研官方 API 和相似开源项目，再给评估方案。”
- “修复这个 CM6 编辑器插件输入中文后装饰错位，并验证撤销、长文和 Live Preview。”
- “审查日历视图的索引、重载恢复和移动兼容，再检查官方为什么搜不到插件，先不要发布。”

## 你会得到什么

| 场景 | 产出 |
| --- | --- |
| 产品迭代 | 按主任务选择命令、编辑器、视图、索引、集成或媒体模式 |
| 工程修复 | 状态所有权、原生 API、资源清理、原子写入、过期任务隔离 |
| 发布 | 版本/产物审计、PR/CI、Release与官方审核分层证据 |

核心入口只保留通用判断，阅读、媒体、AI、大文件和发布细节按需加载；案例不会变成其他插件的默认功能。

## 安装与前置条件

1. 安装 Node.js LTS（https://nodejs.org/），运行 `node --version` 和 `npx --version`。
2. 执行上方安装命令，在你的 Agent 中说出示例任务。用 `npx skills add joeseesun/qiaomu-obsidian-dev --list` 核对可发现。
3. 下载本仓库后运行 `python3 -m unittest discover -s tests`。Python 可从 https://python.org/ 安装，用 `python3 --version` 检查。

- [ ] 已安装 Obsidian：https://obsidian.md/download ，在设置中确认宿主版本。
- [ ] 有明确的插件源码与独立 QA 库；不要把真实日记当测试夹具。
- [ ] 发布时安装 Git 与 GitHub CLI：https://cli.github.com/ ，运行 `gh auth status` 确认自己的账号。

## 只读产物检查

```bash
python3 scripts/audit_release.py /path/to/plugin --tag 1.2.3 --max-asset-bytes 5000000
python3 scripts/audit_release.py /path/to/plugin --tag 1.2.3 --compare-dir /tmp/downloaded-release
python3 scripts/check_public_release.py /path/to/plugin --repo owner/repo --version 1.2.3 --attempts 6
python3 scripts/validate_skill.py .
```

JSON给出失败列表、每个资产字节数和SHA256。`check_public_release.py` 不使用 GitHub 登录或 token，可发现“manifest 已指向新版，但 Release 仍为草稿导致普通客户端 404”。检查成功不等于可上架，官方审核和公开安装必须另外核对。预算可配置；不扫描或上传用户笔记。

## 来源与取舍

源于多个 Obsidian 插件的真实开发和发布故障，但已抽象为插件类型、状态所有权、副作用、生命周期、性能与证据模型；Reader/RSS/Seed/Radio 只保留为案例。结合 [cameronsjo 的 Obsidian Plugin Patterns](https://lobehub.com/zh/skills/cameronsjo-obsidian-obsidian-plugin-patterns) 的公开目录摘要、[Obsidian官方开发指南](https://github.com/obsidianmd/obsidian-developer-docs)。原始 cameronsjo 仓库当前 404，未声称读过其完整技能源码。

默认不加hover tooltip，保留无障碍；用户明确要求某个选区浮层tooltip时只在该处开启。一次项目的5MB预算、源数量与字体数值不是永久官方规则。详见 [经验](references/lessons.md) 与 [研究记录](reports/prior-art-research.md)。

## Troubleshooting

| 问题 | 处理 |
| --- | --- |
| skills找不到入口 | 检查安装仓库与root SKILL.md，运行 --list |
| 本地检查通过、市场仍旧版 | 查看当前release资产、官方扫描和目录缓存，分别记录状态 |
| manifest、Tag、Release 或构建验证报错 | 按[提交故障手册](references/submission-failures.md)核对默认分支、版本链、Tag目标和远端资产摘要 |
| 客户端显示新版本但无法安装 | 先匿名请求该版本的精确 Release 资产 URL；404 时检查是否只有 Draft，不先归因于手机网络 |
| 手机字体/拖放表现不同 | 系统字体不可假定相同；真机验证并保留字体/链接回退 |
| 调试读错窗口 | 核对目标库、版本和ownerDocument；重载正确测试库 |

## English

An Agent Skill for developing and reviewing any Obsidian plugin: plugin-type classification, state ownership, native host integration, lifecycle and data safety, scalable rendering, external capabilities and evidence-based release verification. Reading, media and AI guidance is loaded only when relevant. Install with `npx skills add joeseesun/qiaomu-obsidian-dev`. It is not an Obsidian plugin, an official certification or an automatic approval service. The bundled audit is local and read-only; it never executes the target project. Mobile behavior still needs device testing.

<!-- qiaomu-profile:start -->
## 关于向阳乔木

向阳乔木（乔向阳 / Joe）是一位实践型 AI 产品与内容创作者，长期把前沿 AI 变化转译成可复用的工作流、产品判断、AI 编程实践、AI 搜索实践和 GEO/AI 营销方法。

- 个人网站: https://qiaomu.ai
- 博客: https://blog.qiaomu.ai
- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/
- 微信公众号: 向阳乔木推荐看

### 支持与关注

| 打赏支持 | 微信公众号 |
|---|---|
| <img src="assets/qiaomu-profile/qiaomu_reward_qr.png" alt="向阳乔木打赏二维码" width="180" /> | <img src="assets/qiaomu-profile/qiaomu_wechat_public_account_qr.jpg" alt="向阳乔木推荐看公众号二维码" width="180" /> |
| 感谢支持乔木持续分享 AI 实践 | 扫码关注「向阳乔木推荐看」 |

<!-- qiaomu-profile:end -->

## License / 作者

Copyright (c) 向阳乔木. GPL-3.0-only，保留第三方各自许可；遵守GPL可商用，额外授权可联系作者，不声称开源使用必须付费。

https://qiaomu.ai · https://x.com/vista8 · https://github.com/joeseesun/

## 1.1.0 增补

联网核对三个公开开发技能与官方文档，新增[宿主兼容、性能与编辑器](references/platform-patterns.md)：声明式设置兼容、延迟视图、多窗口字体更新、长文视口与增量处理。[来源与取舍](reports/research-2026-09-08.md)。

## 1.2.0 开发技巧增补

- [数据可靠性](references/data-reliability.md)：迁移、快照冲突、同步、索引与密钥。
- [编辑器与生命周期](references/editor-lifecycle.md)：CM6、Markdown 渲染、跨窗口与释放。
- [测试与诊断](references/testing-troubleshooting.md)：隔离宿主测试、移动边界、官方检查与故障定位。

按场景取用，官方要求与工程建议分开标记；[研究记录](reports/research-v1.2.0.md)。

## 1.3.0 用户纠正增补

渐进设置、插件作用域内关闭不必要 tooltip，以及选文/AI/划线/笔记回跳的完整流程。见 [学习型阅读器](references/reader-workflows.md)；这是 Book Reader 默认值，不要求其他类型插件实现同样功能。

## 1.3.1 发布保护（本机修订）

先对最终候选 SHA 做官方 Preview Scan，再验收 Draft Release 的安装与升级。发布时先公开同一 Release，确认无 token 的精确资产 URL 全部 200 且摘要匹配，再让默认分支 manifest 暴露新版本；CI 不因推 tag 直接公开。正式审核和客户端可安装需要发布后单独验证。详细规则见 [发布门禁](references/release.md)。

## 1.4.0 提交故障诊断

新增[提交与更新故障手册](references/submission-failures.md)，覆盖默认分支读不到 manifest、版本找不到 Release、Tag 带 `v`、错误构建目录、Release 资产与源码不一致、扫描 Pending、结果分级和常见 CSS Lint。审计器新增 `package-lock.json` 版本检查与 `--compare-dir` 字节级资产比较。

## 1.4.3 匿名安装链路门禁

根据 Qiaomu Reader 4.2.14 的实际故障，发布顺序改为：候选分支预扫描与 Draft 验收 → 先公开 Release → 无 token 的三资产 200/摘要回读 → 再合并会暴露新 manifest 版本的 PR → 正式扫描与客户端回读。新增 `check_public_release.py`，防止已登录 CLI 能读草稿却误报“可安装”。

## 1.5.0 开发前调研与评估

新插件或重大能力默认先查当前 Obsidian 官方文档/API/示例，再从官方社区索引和 GitHub 检查功能相近、许可明确的开源插件源码。开发前先给出差异化机会、证据表、复用矩阵、MVP、风险、验证计划与 Go / Revise / Stop 结论；局部 bug、回归、文档和发布不强制重做完整调研。详见[前置调研与评估](references/prior-art-evaluation.md)。

## 1.6.0 最近一周开发经验

综合 Reader、RSS、Seed 与 Radio 的开发对话，新增[大文件与性能](references/performance-large-files.md)和[AI 与跨插件集成](references/ai-integrations.md)：大型文档按视口虚拟化昂贵渲染层；真实 QA 绑定 checkout/vault/版本/fixture；内容插件通过公开上下文契约连接统一 AI 层；Skill/MCP/provider 按轮最小授权并验收到真实结果；用户明确选择的资源采用有界恢复，不允许旧请求触发无限队列跳转。完整取舍见[一周复盘](reports/retrospective-2026-09-08-to-15.md)。

## 1.7.0 通用插件开发框架

Reader、RSS、Seed、Radio 现在只作为发现工程模式的案例，不再是默认产品模板。所有插件先读[插件类型与通用架构](references/plugin-architecture.md)，按命令/自动化、编辑器增强、自定义视图、数据索引、导入导出、网络同步、媒体阅读或 AI/Agent 选择状态所有权、副作用、性能预算和真实验收；再按需加载专项参考。大文件规则扩展到大型任务板、日历、图库与索引，AI 集成规则扩展到所有外部 API、同步和跨插件协议。
