import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import RulesView from '../views/RulesView.vue'
import AccueilView from '../views/AccueilView.vue'
import ClassementView from "@/views/ClassementView.vue";
import InfoClubView from "@/views/InfoClubView.vue";

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
    {
      path: "/classement",
      name: "classement",
      component: ClassementView
    },
    {
      path: "/clubs",
      name: "clubs",
      component: InfoClubView
    },
  ],
})

export default router
