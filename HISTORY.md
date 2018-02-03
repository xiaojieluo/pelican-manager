## 0.2.1
修复在后台设置 debug 值不正确的错误
当文章中不存在 Status 元数据时， 默认为 published.

## 0.2 (2018-02-03)
- 当 metadata 不存在时， 在文章中插入 metadata
- 读取 pelicanconf.py 的 ARTICLE_PATH 变量作为文章存放的位置。
- 将 pelican_manager 配置存入 pelicanconf.py 文件中， 放弃 pelican_manager.toml
- 添加 -c 参数， 用来指定 pelican 的 config 文件

## 0.1.1 (2018-02-01)
- fix some bug.

## 0.1 (2018-01-29)
- The first edition, which lists all articles, can modify their metadata
