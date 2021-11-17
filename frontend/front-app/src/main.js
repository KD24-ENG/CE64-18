import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

import GAuth from 'vue-google-oauth2'
const gauthOption = {
    clientId: '739362517495-enknh230ngpqhb1ub4lmpe7niodtja85.apps.googleusercontent.com',
    scope: 'profile email',
    prompt: 'consent',
    fetch_basic_profile: true
}
Vue.use(GAuth, gauthOption)

createApp(App).use(store).use(router).use(axios).use(firebase).mount('#app')
