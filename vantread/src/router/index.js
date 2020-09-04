import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Novels from '@/components/Novels'
import Intro from '@/components/Intro'
import Rank from '@/components/Rank'
import Read from '@/components/Read'
import Login from '@/components/Login'
import All from '@/components/All'
import Chapter from '@/components/Chapter'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },{
      path: '/novels',
      name: 'novels',
      component: Novels,
      meta:{
        keepAlive:true
      }
    },{
      path: '/novels/rank',
      name: 'rank',
      component: Rank,
      meta:{
        keepAlive:true
      }
    },{
      path:'/novels/intro',
      name:'intro',
      component:Intro,
    },{
      path:'/novels/read',
      name:'read',
      component:Read
    },{
      path:'/novels/login',
      name:'login',
      component:Login
    },{
      path:'/novels/all',
      name:'all',
      component:All
    },{
      path:'/novels/chapter',
      name:'chapter',
      component:Chapter
    }
  ]
})
