# 发布与官方审核

## 发布账本

分别记录：本地构建、测试库安装、PR/CI、合并 SHA、GitHub tag/Release/资产、目录审核状态、公开页安装按钮。GitHub 上传成功不等于官方可搜索；没有红色错误也不等于当前版本已生效。

2026-09-07 官方 Submit your plugin 文档使用 community.obsidian.md 账户流程；首次提交后新版本从 GitHub Release 更新。旧 community-plugins.json PR 教程不能作为唯一判据。每次发布先读当前官方要求，目录指南可能变化。

## 顺序

1. 核对原创/fork、许可证/字体/目录数据授权、manifest id/minAppVersion/isDesktopOnly、隐私网络说明。fork 的开源许可与社区额外提交授权是两件事。
2. 运行项目 check，生成最终资产。脚本 audit_release.py 校验本地版本与大小、SHA256；另查依赖与实际 SDK、资源许可证。预算是项目参数。
3. 检查 staged diff 与敏感信息，feature branch → PR；读评论、reviews、checks，失败/未完成不能当通过。不能直接推 main 或复用已发布 tag。
4. 插件 tag 精确等于 manifest version（例如 1.2.3，无 v）；注意这是 Obsidian 插件规则，不强加给发布本技能的 v1.0.0。上传 main.js、manifest.json，以及实际需要的 styles.css。字体等额外资产不会自动随插件三个文件下载，要设计可安装打包策略。
5. lockfile + CI 从合并 SHA 可重现构建。支持时生成 GitHub artifact attestations；不能因此宣称功能测试通过。
6. 目录后台逐条看 error/warning/recommendation。修复错误后递增版本；扫描超时与代码违规分开诊断。推荐项如 scoped enumeration 说明用途，不用谎称完全没有扫描。
7. 核对公开页面的版本、安装链接、README、截图和说明。手动检查新版本入口有时需要触发同步；排队就是排队，不报已完成。
8. 在隔离库下载正式 release 资产测试安装，比较摘要，验证读取/升级状态。真机未测就标记未测。

## 商店与更新体验

README 首屏放官方安装 URL 与说明，GitHub About 的 website 可指同一地址；保留 BRAT/手动安装作为适当备用。描述应忠于实际支持，图片来自当前真实 UI，不把美术 mock 当功能截图。目录英文限制、截图大小与 icon 能力先读页面。

设置“关于”放当前版本、release notes、GitHub Issues 和公开作者信息。只使用宿主更新机制；不静默下载可执行代码，不替用户开启遥测。下载统计是下载次数，不等于安装用户或活跃用户。

## 成功报告示例

本地/CI 通过；GitHub 1.2.3 已发布且三个资产完整；官方审核 queued；公开页面仍为 1.2.2。下一步是等待/处理官方反馈，不能写「自动上架成功」。
