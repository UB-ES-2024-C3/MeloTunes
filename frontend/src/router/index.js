import Vue from 'vue'
import Router from 'vue-router'
import Welcome from '@/components/Welcome'
import Principal from '@/components/Principal'
import Registrarse from '@/components/Registrarse'
import IniciarSesion from '@/components/IniciarSesion'
import PerfilCancion from '@/components/PerfilCancion'
import TeamSet from '@/components/TeamSet'
import PerfilUser from '@/components/Perfil_user'
import AddSong from '@/components/AddSong'
import ArtistProfile from '@/components/ArtistProfile'
import RecuperarContra from '@/components/RecuperarContra'

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
      path: '/artist_profile',
      name: 'ArtistProfile',
      component: ArtistProfile
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
      path: '/addsong',
      name: 'AddSong',
      component: AddSong
    },
    {
      path: '/song',
      name: 'Song',
      component: PerfilCancion
    },
    {
      path: '/change',
      name: 'Recuperar',
      component: RecuperarContra
    }
  ]
})
