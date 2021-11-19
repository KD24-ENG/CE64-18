import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueGoogleMaps from '@fawmi/vue-google-maps'

const app = createApp(App);
app.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyC9BHsW98zpbw5vcri3eAdRfRahzpUgHGc',
    },
})

createApp(App).use(store).use(router).mount('#app')
