import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import { initializeApp } from "firebase/app";

Vue.prototype.$axios = axios;
Vue.config.productionTip = false


// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCplLmD4Lx3QuhFka0oEHhCI5nv8yJrR8c",
    authDomain: "front-app-b746e.firebaseapp.com",
    projectId: "front-app-b746e",
    storageBucket: "front-app-b746e.appspot.com",
    messagingSenderId: "214807939560",
    appId: "1:214807939560:web:c0b5e1520c0503d1d9bc5d"
};

  // Initialize Firebase
const app = initializeApp(firebaseConfig);

createApp(App).use(store).use(router).mount('#app')

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
