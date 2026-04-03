import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import RulesView from '../views/RulesView.vue'
import CircuitView from '../views/CircuitView.vue'
import EcurieView from '../views/EcurieView.vue'
import ClassementView from '../views/ClassementView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/regles',
      name: 'regles',
      component: RulesView,
    },
    {
      path: '/ecurie',
      name: 'ecurie',
      component: EcurieView,
    },
    {
      path: '/circuit',
      name: 'circuit',
      component: CircuitView,
    },
    {
      path: '/classement',
      name: 'classement',
      component: ClassementView,
    },
  ],
})

export default router
