Title: 使用supervisor-Nginx部署savemylink线上测试环境
Date: 2017-06-06 10:13:06
Modified: 2017-08-26 13:05:51
Slug: Deploying_savemylink_online_test_environments_using_supervisor-Nginx
Tags: supervisor, nginx
Author: Xiaojie Luo

* * *

经过了一个多月断断续续地开发，savemylink这个项目终于到了可以初步运行的地步，线上环境选择的方案就是使用
Nginx 来做反向代理，使用 Supervisord 来作为进程管理工具

## 技术选择

-   [Supervisor](http://supervisord.org)
-   [Nginx](http://nginx.org/)

## 服务器

服务器一开始使用的是 [banwagong](https://bwh1.net/) 的vps，但是搭建了之后发现速度跟不上，后来就换到了 Linode ,现在线上测试环境是[Linode](linode.com) 的 Forment 节点. 内存2G，用来测试应该足够了。

操作系统选择了 Centos 7

## Nginx

### 安装 Nginx

运行下面命令安装nginx

```shell
    sudo yum update -y
    sudo yum install epel-release
    sudo yum install nginx
```

### 配置 Nginx

Nginx 的配置文件可以参考 Tornado [文档最后的例子](http://tornadocn.readthedocs.io/zh/latest/guide/running.html) ,基本就是那样，只有一些地方按照自己的目录修改下就可以了
修改完成之后启动Nginx并添加到开机启动列表中

```shell
    sudo systemctl restart nginx
    sudo systemctl enable nginx
```

Nginx 配置结束了，下面来配置supervisor

## supervisor

[Supervisor](http://supervisord.org) 是一个用 Python
编写的进程管理工具，可以很方便的用来启动、重启、关闭进程（不仅仅是 Python 进程）。除了对单个进程的控制，还可以同时启动、关闭多个进程，比如很不幸的服务器出问题导致所有应用程序都被杀死，此时可以用
supervisor 同时启动所有应用程序而不是一个一个地敲命令启动。

### 安装

Supervisor 可以运行在 Linux、Mac OS X 上。如前所述，supervisor 是 Python
编写的，所以安装起来也很方便，可以直接用 pip (若使用python3，需运行pip3
来安装):

```shell
    sudo pip install supervisor
```

### 配置

在上面的 `nginx.conf` 中，我们开了四个 Tornado 进程，端口号分别是 8000, 8001, 8002, 8003，现在来看 supervisor 的配置，其他配置可以自行 Google ,这里来看下与端口有关的配置

开了四个 Tornado 进程，需要使用来 supervisor 来管理，于是和端口有关的配置如下：

先将默认的 supervisor 配置写入 /etc/supervisor.conf 中，运行下面命令：

```shell
    supervisor
```

然后我们要新建几个配置文件，用来启动 Tornado 进程，
在 `/etc/supervisor.d/` 目录下新建五个文件(注意最后的 redis-6379，因为我项目中用到了 Redis ,所以要加上 Redis 配置文件)：

```shell
    tornado-8000.supervisor
    tornado-8001.supervisor
    tornado-8002.supervisor
    tornado-8003.supervisor
    redis-6379.supervisor
```

文件内容如下：

**tornado-8000.supervisor**

```shel
    [program:tornado-8000]
    command=python3 /home/blog/app/app.py --port=8000
    autostart=true                ; supervisord守护程序启动时自动启动tornado
    autorestart=true              ; supervisord守护程序重启时自动重启tornado
    redirect_stderr=true          ; 将stderr重定向到stdout
    stdout_logfile = /home/blog/blog-8000.log
```

**tornado-8001.supervisor**

```shell
    [program:tornado-8001]
    command=python3 /home/blog/app/app.py --port=8001
    autostart=true                ; supervisord守护程序启动时自动启动tornado
    autorestart=true              ; supervisord守护程序重启时自动重启tornado
    redirect_stderr=true          ; 将stderr重定向到stdout
    stdout_logfile = /home/blog/blog-8001.log
```

**tornado-8002.supervisor**

```shell
    [program:tornado-8002]
    command=python3 /home/blog/app/app.py --port=8002
    autostart=true                ; supervisord守护程序启动时自动启动tornado
    autorestart=true              ; supervisord守护程序重启时自动重启tornado
    redirect_stderr=true          ; 将stderr重定向到stdout
    stdout_logfile = /home/blog/blog-8002.log
```

**tornado-8003.supervisor**

```shell
    [program:tornado-8003]
    command=python3 /home/blog/app/app.py --port=8003
    autostart=true                ; supervisord守护程序启动时自动启动tornado
    autorestart=true              ; supervisord守护程序重启时自动重启tornado
    redirect_stderr=true          ; 将stderr重定向到stdout
    stdout_logfile = /home/blog/blog-8003.log
```

**redis-6379.supervisord**

```shell
    [program:redis-6379]
    command = /usr/local/bin/redis-server /var/www/savemylink/redis.conf  ; 启动命令，可以看出与手动在命令行启动的命令是一样的
    autostart = true     ; 在 supervisord 启动的时候也自动启动
    autorestart = true   ; 程序异常退出后自动重启
    startsecs = 5        ; 启动 5 秒后没有异常退出，就当作已经正常启动了
    startretries = 3     ; 启动失败自动重试次数，默认是 3
    redirect_stderr = true  ; 把 stderr 重定向到 stdout，默认 false
    stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
    stdout_logfile_backups = 20     ; stdout 日志文件备份数
    ; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
    stdout_logfile = /var/www/savemylink/redis-6379-stdout.log
```

配置文件写入完成之后，还需要在 `/etc/supervisor.conf` 中 include
打开 `/etc/supervisor.conf` ,在最后添加下面代码：

```shell
    [include]
    files=/etc/supervisor.d/*.supervisor
```

### supervisorctl 操作

Supervisorctl 是 supervisord 的一个命令行客户端工具，启动时需要指定与 supervisord 使用同一份配置文件，否则与 supervisord 一样按照顺序查找配置文件。

在命令后运行 `supervisorctl` ，可以进入 supervisor 的命令行模式，在此模式中支持以下几种操作命令：

-   status : 查看被管理的进程的状态
-   start : 启动指定进程
-   stop : 停止指定进程
-   restart : 重启指定进程
-   update : 启动新配置或有改动的进程
-   reload : 重新启动supervisor

### supervisor 运行

直接在命令行输入 `supervisord` 即可启动，可进入 supervisorctl` 检查各进程是否启动成功。

## 结束

使用浏览器访问地址就发现Nginx已经反向代理了Tornado进程，线上测试环境部署完成。
