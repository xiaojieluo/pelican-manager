Title: 使用flask-login的current_user时遇到的问题
Date: 2018-01-16 13:51:29
Modified: 2018-01-16 13:51:30
Slug: Problems_encountered_by_current_user_using_flask-login
Tags: flask-login, flask, mongodb
Author: Xiaojie Luo
---

### environment
数据库管理软件使用的是 mongoengine, 有一个 author 字段， 类型为 `ReferenceField`, 保存当前登陆的用户 objectid.
程序登陆管理使用的是 flask-login，

### bug desc
在使用时发现个问题,直接把 `current_user` 传递给 author， mongoengine 会报错：`cannot encoding <User: User objects>`。
出错代码：
```python
link(author = current_user).save()
```
但是直接使用下面代码是没有问题的：
```python
user = User().objects().first()
link = Link(author = user).save()
```

### fix bug
排查之后发现问题处在 `current_user` 这里， 查 [falsk-login 源码](https://github.com/maxcountryman/flask-login/blob/848088a9fc6e8c9c418e8820e072cde6ac81dc00/flask_login/utils.py#L26)之后， 发现 `current_user` 返回 `LocalProxy`类， 说明 `current_user` 只是一个代理类,具体实现是由 `werkzeug.local.LocalProxy` 负责的

现在跳转到 `werkzeug.local.LocalProxy` 类中， 发现了代理类中的这个方法：[_get_current_object()](https://github.com/pallets/werkzeug/blob/8393ee88aaacf7bcd3a0b1d604511f70c222df25/werkzeug/local.py#L300) ， 即返回被代理的对象。

问题找到了， 我们只要把原来的代码稍微改下即可：
```python
user = current_user._get_current_object()
link = Link(author = user).save()
```
