Title: 在函数中if,return,else的问题
Date: 2017-02-05 15:27:15
Modified: 2017-02-05 15:27:15
Slug: The_problem_of_if_return_else_in_functions
Tags: think
Author: Xiaojie Luo

---

首先有这么一个函数：

```python
    def parity(x = 10):
        """
        判断奇偶性
        奇数返回false
        偶数返回true
        """
        if x%2 == 0:
            return true
        else:
            return false
```

实际运行，上面函数能很好的完成想要实现的功能，但是如果把 if 之后的程序修改下：

```python
    def parity(x = 10):
        """
        判断奇偶性
        奇数返回false
        偶数返回true
        """
        if x%2 == 0:
            return true
        return false
```

应该也是可以的，函数在返回 `true` 后就会抛弃掉后面的程序,阻断了 `false` 的 `return`.
