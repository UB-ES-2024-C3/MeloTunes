import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

// Importar els fitxers CSS de Bootstrap i BootstrapVue (l'ordre és important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

// Fem que el Boostrap estigui disponible a tot el projecte
Vue.use(BootstrapVue)
// Opcionalment també podem instal·lar les icones
Vue.use(IconsPlugin)
Vue.use(Vuetify)

const vuetify = new Vuetify()
/* eslint-disable no-new */
new Vue({
  router,
  components: { App },
  template: '<App/>',
  vuetify,
  render: (h) => h(App), // Renderiza el componente raíz
}).$mount('#app'); // Esto es suficiente
