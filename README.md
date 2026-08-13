# gpt-exten

用于通过 GitHub Actions 实现间接联网下载、构建和文件中转。

下载或构建完成的文件会上传为 GitHub Actions Artifact，并通过 `ARTIFACT_CACHE.md` 记录可复用缓存、版本、Artifact 信息和过期时间。

大文件会提前分片，方便后续下载到本地或容器环境。
