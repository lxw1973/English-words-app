<template>
  <div class="vocab-container">
    <h2 class="text-3xl font-bold mb-6">📖 词库浏览</h2>

    <div class="flex gap-4 mb-6 flex-wrap">
      <button
        v-for="level in ['CET4', 'CET6', 'BEC', 'TOEFL', 'IELTS']"
        :key="level"
        @click="selectedLevel = level; loadVocab()"
        :class="selectedLevel === level ? 'bg-indigo-600 text-white' : 'bg-white text-gray-700'"
        class="px-4 py-2 rounded-lg shadow hover:shadow-md transition-all"
      >
        {{ level }}
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="word in words"
        :key="word.id"
        class="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow"
      >
        <h3 class="text-xl font-bold text-indigo-600">{{ word.word }}</h3>
        <p class="text-gray-600 text-sm">{{ word.phonetic }}</p>
        <p class="mt-2 text-gray-700">{{ word.meaning }}</p>
        <p class="text-gray-600 text-sm mt-2 italic">{{ word.example }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { wordAPI } from '../api/client'

const selectedLevel = ref('CET4')
const words = ref([])

const loadVocab = async () => {
  try {
    const response = await wordAPI.getWords(selectedLevel.value, 0, 30)
    words.value = response.data.words
  } catch (error) {
    console.error('加载词库失败:', error)
  }
}

onMounted(() => {
  loadVocab()
})
</script>