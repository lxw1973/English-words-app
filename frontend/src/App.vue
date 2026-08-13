<script setup>
import { useWordStore } from './stores/wordStore'
import { onMounted } from 'vue'

const wordStore = useWordStore()

onMounted(() => {
  wordStore.fetchStats()
})
</script>

<template>
  <div id="app" class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
    <!-- 顶部导航 -->
    <nav class="bg-white shadow-md">
      <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <div class="flex items-center space-x-2">
          <span class="text-2xl">📚</span>
          <h1 class="text-2xl font-bold text-indigo-600">英语单词学习</h1>
        </div>
        <div class="flex items-center space-x-4">
          <span class="text-gray-600">已学: <span class="font-bold text-green-600">{{ wordStore.learnedCount }}</span></span>
          <router-link to="/" class="px-4 py-2 rounded hover:bg-gray-100">学习</router-link>
          <router-link to="/vocab" class="px-4 py-2 rounded hover:bg-gray-100">词库</router-link>
          <router-link to="/stats" class="px-4 py-2 rounded hover:bg-gray-100">统计</router-link>
        </div>
      </div>
    </nav>

    <!-- 主内容 -->
    <main class="max-w-6xl mx-auto px-6 py-10">
      <router-view />
    </main>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>
