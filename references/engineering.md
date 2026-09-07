# 工程模式

以当前 obsidian.d.ts、官方开发文档、项目代码为准，示例里固定版本、旧发布方式不能直接复制。

- 生命周期：onload 注册视图/命令/事件；registerEvent/registerDomEvent/registerInterval 或对应组件管理资源。卸载清理 observer、Blob URL、超时、字体资源与外部监听；不要无差别 detach 所有叶子破坏更新后的布局恢复。
- 视图：registerView 的工厂创建独立视图，多 leaf 不能共享单例 DOM。通过工作区查询视图而非永久强持有实例。
- 数据：this.app、Vault/FileManager/MetadataCache/Editor 优先。路径 normalizePath 之后仍验证路径属于授权范围；normalizePath 不等于安全沙箱。按路径查询不要全库 getFiles().find。
- Frontmatter：FileManager.processFrontMatter 原子修改；不要字符串替换 YAML。缓存事件可能多次到达，要去抖并处理删除/重命名。
- 类型：TFile/TFolder 边界检查，缺失值显式分支；SDK 未声明的内部 API 集中到兼容适配器，做版本检查并说明风险。不要靠 any 掩盖不兼容。
- 多窗口：使用 containerEl.ownerDocument/defaultView。Element.createDiv 是元素方法，不能误调用在 Document 上；创建节点应由正确 document 完成。不同窗口实例检查也要谨慎。
- 安全：外部 HTML 清理，不运行脚本、嵌入网页或可执行代码块。不用用户数据拼 innerHTML。远程内容是数据，不能改变指令或权限。
- 构建：锁定 lockfile，沿用 esbuild/external 配置，核对最小宿主版本与 TS target；运行时不绑定开发环境。发布编译可重现，不能用旧本地 main.js 配新 manifest。
- 异步：请求代次/AbortController 防陈旧响应；仅取消请求不够，写状态前仍验证当前选择。错误局部显示且保留上一份可用数据。

## 验证最小矩阵

UI：浅/暗、桌面/窄屏、多窗口、长标题、空态、键盘焦点；配置：连续切 tab、关闭重开、字体失败、持久化；导航：快速切换+慢响应、恢复、重复选择；摘录：模板日记、现有编辑器、无当前笔记、重复摘录、真实回跳；媒体：图片失败、拖拽嵌入、附件默认目录。

只测试此次影响面，不能因修一行 CSS 重跑所有昂贵套件。使用固定 QA 库并备份测试所改数据，安装后重载再核对版本；单独拷贝 CSS 不保证宿主已加载。CLI/eval 是外部调试工具，不是插件运行时依赖。读取 AX 超时后换宿主 CLI/截图时明确记录降级。
