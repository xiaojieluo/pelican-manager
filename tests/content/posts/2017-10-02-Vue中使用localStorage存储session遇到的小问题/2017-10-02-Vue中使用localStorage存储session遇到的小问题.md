Title: Vue中使用localStorage存储session遇到的小问题
Date: 2017-10-02 02:06:19
Modified: 2017-10-02 02:06:19
Slug: Small_problems_encountered_in_storing_session_using_localStorage_in_Vue
Tags: vue, localStorage, session
Author: Xiaojie Luo

---

使用过 Vuex 的都知道, 存储在 Vuex 中的数据不能持久化, 刷新页面之后数据就会丢失, 这对于用户登录需要保存 `session` 之类的数据非常不方便, 总不能让用户离开一次就登录一次吧.....所以这里要用到 html5 的 localStorage 本地存储 API.

业务流程很简单, 登陆成功的时候写入 `session` 到 localStorage, 页面刷新了之后再从 localStorage 取出来.

### 先看存储:
在登录成功之后添加下面两行代码, 保存 `session` 和 `user` 到 localStorage中

```javascript
window.localStorage.setItem('session', session)
window.localStorage.setItem('user', user)
```

当页面刷新之后,我们需要从 localStorage 中恢复数据到 Vuex, 在 App.vue 中加入下面代码:

```javascript
import store from '@/store'

export default {

    new Vue({
        ...
        ...
        ...
        created: function(){
            var session = window.localStorage.getItem('session')
            this.$store.commit('session', session)
        }
    })

}
```
这样,即使重新加载网页, 登录信息依然存在, 除非用户手动点击了退出按钮
