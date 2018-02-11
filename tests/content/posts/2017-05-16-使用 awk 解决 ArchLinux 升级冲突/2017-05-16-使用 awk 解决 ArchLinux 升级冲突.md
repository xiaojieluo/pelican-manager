Title: 使用 awk 解决 ArchLinux 升级冲突
Date: 2017-05-16 15:00:40
Modified: 2017-05-16 15:00:40
Slug: Using_awk_to_resolve_ArchLinux_escalation_conflicts
Tags: Archlinux, awk
Author: Xiaojie Luo

---

今天在升级 Archlinux 时发现无法升级，按照 [Archlinux
Wiki](https://wiki.archlinux.org/index.php/Pacman#.22Failed_to_commit_transaction_.28conflicting_files.29.22_error)的说法，就是文件冲突了，而 pacman 又不会自动覆盖已存在的文件。

解决方法也很简单，重命名冲突的文件就可以了。文件少点直接手动修改就好了，不过如果有许多需要重命名的文件，就要用到 awk 来自动化处理

# 提取冲突文件

从 pacman 升级过程中提取有冲突的文件，使用下列命令将 `pacman -Syu` 的运行结果写入 error.txt 中，方便后续 awk 处理

```shell
pacman -Syu > error.txt
```

# 处理提取文件

打开 error.txt ，删除不需要的信息，只保留有冲突错误信息的部分，然后保存。

# 批量重命名冲突文件

现在在命令行执行 awk 命令，批量重命名有冲突的文件（删除也可以，不过小心为上，建议重命名，如果升级有问题，可以逆向恢复）

```shell
sudo awk '{print "mv " $2 " " $2"_bak" | "bash"}' error.txt
```

正常情况下执行上面命令是没有任何输出的，最后就可以运行 `pacman -Syu`
正常升级系统

# 参考网站

[在awk中运行shell命令](http://www.shencan.net/index.php/2012/09/03/%E5%9C%A8awk%E4%B8%AD%E8%BF%90%E8%A1%8Cshell%E5%91%BD%E4%BB%A4/)

[awk学习笔记](http://www.ttlsa.com/docs/awk/#id2809263)
