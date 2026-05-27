# Tag Release Skill

## 触发词

打 tag、创建 tag、release、发布版本、tag release、create tag、打个 beta 版本、发个版本

## 核心流程

1. **确定版本类型**：询问用户是正式版、Beta 版还是 RC 版
2. **获取上一个 tag**：`git tag --sort=-v:refname | head -1`
3. **计算新版本号**：按语义化版本规则递增
4. **获取提交记录**：`git log <last-tag>..HEAD --oneline --no-merges`
5. **生成中文描述**：20字概括 + 要点列表
6. **创建 annotated tag**：`git tag -a <version> -m "<desc>"`

## 版本递增规则

- 包含 "BREAKING CHANGE" 或 `feat!:` → major +1
- 包含 `feat:` → minor +1
- 其他 → patch +1

## 重要限制

- **不要自动 `git push`**，除非用户明确要求
- **不要让用户确认描述**，直接执行
- **不要创建轻量 tag**，必须用 `-a` 创建 annotated tag
- Beta 版本格式：`v{major}.{minor}.{patch}-beta.{n}`
- RC 版本格式：`v{major}.{minor}.{patch}-rc.{n}`

## 输出格式

```
已创建 tag: v0.3.0-beta.1

描述：
新增阿里云 OSS 同步发布功能

- 构建产物添加平台后缀
- Release 自动同步到阿里云 OSS
- 支持 Pre-release 自动标记

运行 `git push origin v0.3.0-beta.1` 推送到远程。
```

## 执行步骤

当用户触发时：

1. 运行 `git tag --sort=-v:refname | head -1` 获取最新 tag
2. 如无 tag，默认从 v0.1.0 开始
3. 分析 `git log <last-tag>..HEAD --oneline --no-merges` 的提交信息
4. 根据提交信息自动判断版本递增类型
5. 询问用户：正式版 / Beta / RC
6. 生成 tag 描述（中文，20字概括 + 要点）
7. 执行 `git tag -a <version> -m "<desc>"`
8. 提示用户运行 `git push origin <version>` 推送
