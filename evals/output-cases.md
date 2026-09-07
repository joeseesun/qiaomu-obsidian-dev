# Output regression scenarios

These are human/agent review rubrics, not executed model tests.

1. Request: remove tooltips; preserve screen-reader labels. Pass: no title/setTooltip, accessible names and focus remain. Fail: removing all accessibility.
2. Request: popup needs tooltip. Pass: exception only for that popup. Fail: global tooltip restoration.
3. GitHub release exists, directory scan timed out. Pass: report release and failed scan separately. Fail: claim official install success.
4. Three bundled fonts inflate JS. Pass: inspect final bytes, subset/license/fallback; verify devices. Fail: gzip blobs treated as free bytes or remote executable workaround.
5. Rapid channel changes with slow fetch. Pass: immediate selected state, old responses ignored, per-channel restoration. Fail: loading blocks navigation.
6. Current-note capture while reader focused. Pass: valid recent Markdown target and safe Editor write; no target handled. Fail: arbitrary file selection.
7. Drag image inserts filename. Pass: real binary saved under configured attachment path and image embed verified. Fail: synthetic drop alone declared native success.
8. Native settings duplicate navigation. Pass: reusable row cleaned and repeated-tab behavior tested. Fail: hide extra bars with CSS only.

2026-09-08 self-review: all eight behaviors are explicitly covered in references; no independent runtime execution of the skill is claimed.

## 新增人工评审场景（尚非实测）

9. 支持旧宿主的插件迁移声明式设置：须先确认最低版本、保留兼容路径，不能静默提高版本。
10. 设置独立窗口修改字体：须更新阅读视图所属文档，不能只改 activeDocument。
11. 未加载阅读视图回跳：await revealLeaf 后验证实例，不能强制加载所有后台页签。
12. 百万行笔记高亮：不得用 DOM 当全文或每次键入全库扫描，需视口/状态方案与性能测量。
