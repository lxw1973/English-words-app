<template>
  <div class="stats-container">
    <h2 class="text-3xl font-bold mb-8">📊 学习统计</h2>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 mb-8">
      <div
        v-for="(count, level) in stats.by_difficulty"
        :key="level"
        class="bg-white rounded-lg shadow-lg p-6 text-center hover:shadow-xl transition-shadow"
      >
        <p class="text-gray-600 text-sm mb-2">{{ level }}</p>
        <p class="text-4xl font-bold text-indigo-600">{{ count }}</p>
        <p class="text-gray-500 text-xs mt-2">个单词</p>
      </div>
    </div>

    <div class="bg-white rounded-lg shadow-lg p-8">
      <p class="text-2xl font-bold mb-4">📚 总词库数: <span class="text-indigo-600">{{ stats.total_words }}</span></p>
      <p class="text-lg text-gray-600">已学习: <span class="font-bold text-green-600">{{ learnedCount }}</span> 个</p>
      <p class="text-lg text-gray-600">学习进度:
        <span class="font-bold text-indigo-600">{{ progressPercent }}%</span>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useWordStore } from '../stores/wordStore'
import { wordAPI } from '../api/client'

const wordStore = useWordStore()
const stats = ref({ total_words: 0, by_difficulty: {} })
const learnedCount = ref(0)

const progressPercent = computed(() => {
  if (!stats.value.total_words) return 0
  return Math.round(learnedCount.value / stats.value.total_words * 100)
})

onMounted(() => {
  loadStats()
})

const loadStats = async () => {
  try {
    const response = await wordAPI.getStats()
    stats.value = response.data
    learnedCount.value = wordStore.learnedCount
  } catch (error) {
    console.error('加载统计失败:', error)
  }
}
</script>

<style scoped>

</style>
