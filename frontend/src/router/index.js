import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import Principal from '@/components/Principal'
import Registrarse from '@/components/Registrarse'
import IniciarSesion from '@/components/IniciarSesion'
import PerfilCancion from '@/components/PerfilCancion'
import TeamSet from '@/components/TeamSet'
import PerfilUser from '@/components/Perfil_user'

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
      path: '/perfil_user',
      name: 'PerfilUser',
      component: PerfilUser
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
    },
    {
      path: '/teams',
      name: 'Teams',
      component: TeamSet
    },
    {
      path: '/perfilcancion',
      name: 'PerfilCancion',
      component: PerfilCancion
    }
  ]
})
