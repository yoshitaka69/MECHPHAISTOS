import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

//vue-router
import router from './router';


//primeVue関係
import PrimeVue from 'primevue/config';
//以下はprimeVueのscss primeVueのglobal scss assetsフォルダ内にある。
import '@/assets/styles.scss';





const app = createApp(App);
app.use(router);
app.use(PrimeVue, { ripple: true });
app.mount('#app')
