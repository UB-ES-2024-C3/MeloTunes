import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import Principal from '@/components/Principal'
import Registrarse from '@/components/Registrarse'
import IniciarSesion from '@/components/IniciarSesion'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/home',
      name: 'Home',
      component: Principal
    },
    {
      path: '/register',
      name: 'Register',
      component: Registrarse
    },
    {
      path: '/login',
      name: 'Login',
      component: IniciarSesion
    }
  ]
})
