import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia } from 'pinia'

import App from './App.vue'
import StudyView from './components/StudyView.vue'
import VocabView from './components/VocabView.vue'
import StatsView from './components/StatsView.vue'

import './style.css'

const routes = [
  { path: '/', component: StudyView },
  { path: '/vocab', component: VocabView },
  { path: '/stats', component: StatsView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.mount('#app')