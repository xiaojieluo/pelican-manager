Title: Github上fork项目后与原项目保持同步
Date: 2017-05-27 01:29:39
Modified: 2017-05-27 01:29:39
Slug: After_the_fork_project_on_Github_keep_in_sync_with_the_original_project
Tags: github
Author: Xiaojie Luo

---

翻译自 [Github
的解决方案](https://help.github.com/articles/syncing-a-fork/)

同步存储库的分支以使其与上游存储库保持同步.
在将分支与上游存储库同步之前,必须配置一个指向 Git 中上游存储库的 remote

在本地建立两个库的中介, 把两个远程库都 clone
到本地,然后拉取原项目更新到本地,合并更新,最后 push 代码到分支的 github

-   打开终端
-   切换工作空间到 fork 的仓库目录 (cd 命令)
-   从上游存储库获取分支及其各自的提交.
