import { createApp } from 'vue'
import {createRouter, createWebHistory} from 'vue-router'
import App from './App.vue'
import ProductPage from "@/pages/ProductPage.vue";
import ChatBox from "@/pages/ChatBox.vue";
import HomePage from '@/pages/HomePage.vue'

const routes = [
    { path: '/', component: HomePage},
    { path: '/home', component: HomePage},
    { path: '/chat', component: ChatBox},
    { path: '/products', component: ProductPage}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

const app = createApp(App);

app.use(router);

app.mount('#app');
