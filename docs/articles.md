文章类

```python
path = 'hello.md'
article = article_factory(path)

```

## 属性

名称        | 备注
--------- | -----------------------------------
path      | 文章的相对路径， 相对于 `pelican_manager` 启动目录
full_path | 文章的完整路径
meta      | 包含所有 metadata 的字典
text      | 不包含 metadata 的正文文本
content   | 直接从文件中读取出的完整内容
