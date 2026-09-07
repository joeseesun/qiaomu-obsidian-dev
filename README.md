# qiaomu-obsidian-dev

插件编译通过了，用户却还是跳错文章、看不到图片、在商店搜不到？这套 skill 把乔木的阅读体验要求和 Obsidian 发布验证串成一个可执行流程。

[![Install](https://img.shields.io/badge/skills-install-315a42)](https://github.com/joeseesun/qiaomu-obsidian-dev) [![Stars](https://img.shields.io/github/stars/joeseesun/qiaomu-obsidian-dev)](https://github.com/joeseesun/qiaomu-obsidian-dev/stargazers) [![Issues](https://img.shields.io/github/issues/joeseesun/qiaomu-obsidian-dev)](https://github.com/joeseesun/qiaomu-obsidian-dev/issues) [![License](https://img.shields.io/github/license/joeseesun/qiaomu-obsidian-dev)](LICENSE)

```bash
npx skills add joeseesun/qiaomu-obsidian-dev
```

一次任务的交付样例：

> 原因：旧文章请求覆盖新频道。修复：先切选择、再加载正文，并校验请求代次。验证：慢网快速切换、输入框键盘隔离、频道滚动恢复。发布：GitHub已发布；官方审核排队，不能称已上架。

## 你可以直接这样说

- “修复这个 Obsidian 插件的设置重复 tab，保留阅读位置。”
- “阅读器要支持选区追加到今日日记，桌面分屏打开，并测试真实回跳。”
- “审查字体打包和移动兼容，再检查官方为什么搜不到插件，先不要发布。”

## 你会得到什么

| 场景 | 产出 |
| --- | --- |
| 产品迭代 | 克制工具栏、可恢复导航、即时字体、移动原生选区 |
| 工程修复 | 原生API、资源清理、原子文件写入、过期响应隔离 |
| 发布 | 版本/产物审计、PR/CI、Release与官方审核分层证据 |

核心入口约几页，细节按需加载；不把每个RSS功能强加到所有插件。

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
python3 scripts/validate_skill.py .
```

JSON给出失败列表、每个资产字节数和SHA256。检查成功不等于可上架，官方审核和公开安装必须另外核对。预算可配置；不扫描或上传用户笔记。

## 来源与取舍

源于2026-09-06至07的乔木RSS/阅读器开发经验；结合 [cameronsjo 的 Obsidian Plugin Patterns](https://lobehub.com/zh/skills/cameronsjo-obsidian-obsidian-plugin-patterns) 的公开目录摘要、[Obsidian官方开发指南](https://github.com/obsidianmd/obsidian-developer-docs)。原始cameronsjo仓库当前404，未声称读过其完整技能源码。由 qiaomu-meta-skill 创建，吸收 skill-publisher 发布页与安装验证方法。

默认不加hover tooltip，保留无障碍；用户明确要求某个选区浮层tooltip时只在该处开启。一次项目的5MB预算、源数量与字体数值不是永久官方规则。详见 [经验](references/lessons.md) 与 [研究记录](reports/prior-art-research.md)。

## Troubleshooting

| 问题 | 处理 |
| --- | --- |
| skills找不到入口 | 检查安装仓库与root SKILL.md，运行 --list |
| 本地检查通过、市场仍旧版 | 查看当前release资产、官方扫描和目录缓存，分别记录状态 |
| 手机字体/拖放表现不同 | 系统字体不可假定相同；真机验证并保留字体/链接回退 |
| 调试读错窗口 | 核对目标库、版本和ownerDocument；重载正确测试库 |

## English

An opinionated Agent Skill for developing and reviewing Obsidian plugins: reading-first UX, native note workflows, typography budgets, lifecycle cleanup and evidence-based release verification. Install with `npx skills add joeseesun/qiaomu-obsidian-dev`. It is not an Obsidian plugin, an official certification or an automatic approval service. The bundled audit is local and read-only; it never executes the target project. Mobile behavior still needs device testing.

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
