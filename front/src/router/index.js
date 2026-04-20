import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '@/composables/useAuth.js'

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
      meta: { requiresAuth: true }
    },
    {
      path: '/ecurie',
      name: 'ecurie',
      component: EcurieView,
      meta: { requiresAuth: true }
    },
    {
      path: '/circuit',
      name: 'circuit',
      component: CircuitView,
      meta: { requiresAuth: true }
    },
    {
      path: '/classement',
      name: 'classement',
      component: ClassementView,
      meta: { requiresAuth: true }
    },
  ],
})
// Protection des routes
router.beforeEach((to, from, next) => {
  const { isLogged, loadUser } = useAuth()

  // Recharge l'utilisateur depuis localStorage
  loadUser()

  // Si la route nécessite une connexion et que l'utilisateur n'est pas connecté
  if (to.meta.requiresAuth && !isLogged.value) {
    return next('/') // redirection vers la page d'accueil
  }

  next()
})
export default router
