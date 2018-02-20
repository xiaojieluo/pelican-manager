import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/article/Index'
import ArticleEdit from '@/components/article/Edit'
import Dashboard from '@/components/dashboard/dashboard'
import Home from '@/components/dashboard/home'
import Option from '@/components/options/options'
import optionsGeneral from '@/components/options/general'
import optionsPublished from '@/components/options/published'

Vue.use(Router)

export default new Router({
  routes: [
      {
          path: '/dashboard',
          component: Dashboard,
          children: [
              { path: 'home', name: 'Home', component: Home}
          ]
      },
      {
          path: 'options',
          component: Option,
          children: [
              { path: 'general', name: 'options_general', component: optionsGeneral },
              { path: 'published', name: 'options_published', component: optionsPublished },
          ]
      },
      // {
      //     path: '/dashboard',
      //     component
      // }
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
  },
  {
      path: '/articles/',
      name: 'ArticleAll',
      component: Index
  },
  {
      path: '/articles/edit',
      name: 'ArticleEdit',
      component: ArticleEdit
  }
  ]
})
