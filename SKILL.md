---
name: qiaomu-obsidian-dev
description: |
  Develop, debug, review, test and release Obsidian plugins with Qiaomu reading-first UX and native APIs. Use for Obsidian 插件开发、阅读器、设置、字体、摘录、日记、图片附件、移动端、回跳链接、构建和官方审核发布. Also use when fixing an existing plugin's UX, lifecycle, race conditions or release evidence. Exclude ordinary vault note writing, generic Markdown formatting, plugin recommendations, non-Obsidian app development, and skill authoring itself.
metadata:
  author: 向阳乔木
  version: "1.2.0"
---

# Qiaomu Obsidian Dev

把插件做成可持续使用、可验证发布的产品。用户当前指令和项目 AGENTS 优先于本技能；本技能不等于 Obsidian 官方政策。

## 路由与边界

- 审查/诊断请求默认只读；开发请求完成实现与验证；只有授权发布时才推送、合并、修改社区页面。不得把「修好」擅自扩大为公开发布。
- 先检查实际仓库、分支、dirty 状态、目标测试库、已安装版本、项目脚本和当前 SDK 类型。不要把另一个库、旧截图或缓存中的版本当当前证据。
- 原生 API 优先；插件运行时不依赖开发机器路径或调试全局 app。面向移动端时不打包 Node/Electron；声明兼容不等于真机验证。
- 原创项目保留已选许可证；fork 保留来源和许可，核实目录提交的额外授权要求。重命名不能消除来源义务。

## 最小工作流

1. 复述用户结果与重要假设，按下面的路由只读相关参考。优先最小改动，不给普通变更增加仪式流程。
2. 修复前复现问题，追踪状态、DOM 所属文档、异步请求、文件写入或发布链路；对症找到根因。
3. 用现有架构实现。跨渠道保存阅读上下文；异步切换立即更新选择并防止旧响应覆盖；操作完成不丢焦点、选区和滚动。
4. 按改动运行 lint/typecheck/测试/build，再安装到指定测试库并重载。验证真正的用户操作；模拟测试和实机结果分开写。
5. 授权发布时按 [发布门禁](references/release.md) 走 feature branch → PR → checks → merge → exact-tag assets → 目录审核 → 公开页核验。
6. 交付改动、测试结果、未覆盖平台、实际发布阶段和可点击产物。无法验证的部分直接标记，禁止声称「自动上架成功」。

## 按任务加载

| 任务 | 参考 |
| --- | --- |
| 工具栏、频道、列表、设置、空态、移动交互 | [阅读与设置](references/product-ux.md) |
| 字体大小、离线字库、缓存图片、拖拽附件 | [字体与媒体](references/fonts-media.md) |
| 日记、当前笔记、选区、内部回跳、本地 Markdown | [摘录与来源](references/capture-navigation.md) |
| 生命周期、Vault API、异步安全、多窗口 | [工程模式](references/engineering.md) |
| 新设置 API、延迟视图、编辑器扩展、启动性能 | [宿主与性能](references/platform-patterns.md) |
| 配置迁移、并发写入、同步、密钥、索引 | [数据可靠性](references/data-reliability.md) |
| Markdown 组件、CM6 装饰、资源释放 | [编辑器与生命周期](references/editor-lifecycle.md) |
| 回归测试、真实宿主测试、常见故障定位 | [测试与诊断](references/testing-troubleshooting.md) |
| 插件商店搜不到、审核、Release、安装 | [发布门禁](references/release.md) |
| 经验来源、偏好变化、哪些不是通则 | [经验与依据](references/lessons.md) |

## 默认产品判断

阅读优先，导航和说明按需出现。默认没有 hover tooltip，除非用户明确要求；仍保留可访问名称、焦点与键盘操作。字体调整即时保存。选区摘录按产品需求配置，RSS 已明确要求的两个 popup 图标允许 tooltip，此例不扩展到全产品。

复用 Obsidian 日记、文件选择、附件路径与分屏能力。不要把内部识别码、HTML 注释、服务地址或调试选项写进普通阅读/笔记流程。

## 验证入口

```bash
python3 scripts/audit_release.py /path/to/plugin --tag 1.2.3 --max-asset-bytes 5000000
python3 -m unittest discover -s tests -p 'test_*.py'
```

审计脚本只读，输出 JSON 与非零失败码；它检查本地产物、版本、大小与摘要，不执行项目代码，不证明官方审核、依赖安全、移动兼容或网络可用。5 MB 是本项目经验的可配置预算，不声称永久官方限制。

## 输出合同

- Diagnosis：触发条件、根因、影响、拟修复范围。
- Implementation：实际文件与用户可见行为，避免只报实现术语。
- Verification：命令/结果、测试库与版本、桌面/真机/模拟覆盖，失败或缺证。
- Distribution：local / PR / merged / GitHub release / review queued / review passed / public installable 分开记录。
- Feedback：可复用规则只在用户要求时写入外部长期记忆；无需把私有库路径、订阅令牌或原始聊天发布。

Copyright (c) 向阳乔木 · X https://x.com/vista8 · GitHub https://github.com/joeseesun/
