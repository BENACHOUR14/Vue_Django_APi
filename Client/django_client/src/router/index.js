import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'match',
      component: () => import('../views/Matche.vue')
    },
    {
      path: '/stats',
      name: 'stats',
      component: () => import('../views/Stats.vue')
    },
    {
      path: '/groupe',
      name: 'groupe',
      component: () => import('../views/Groupe.vue')
    }
  ]
})

export default router
