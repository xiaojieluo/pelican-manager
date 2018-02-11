import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/article/Index'
import ArticleEdit from '@/components/article/Edit'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
  },
  {
      path: '/articles/',
      name: 'ArticleIndex',
      component: Index
  },
  {
      path: '/articles/edit',
      name: 'ArticleEdit',
      component: ArticleEdit
  }
  ]
})
