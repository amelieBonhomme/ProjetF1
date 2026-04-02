import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import RulesView from '../views/RulesView.vue'
import AccueilView from '../views/AccueilView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/rules',
      name: 'rules',
      component: RulesView,
    },
    {
      path: '/accueil',
      name: 'accueil',
      component: AccueilView,
    },
  ],
})

export default router
