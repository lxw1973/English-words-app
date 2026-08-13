import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { wordAPI } from '../api/client'

export const useWordStore = defineStore('word', () => {
  // 状态
  const currentWord = ref(null)
  const difficulty = ref('CET4')
  const showTranslation = ref(false)
  const learnedCount = ref(0)
  const stats = ref(null)
  const loading = ref(false)

  // 计算属性
  const proficiencyPercentage = computed(() => {
    if (!currentWord.value) return 0
    return currentWord.value.proficiency || 0
  })

  // 方法
  const setDifficulty = async (level) => {
    difficulty.value = level
    showTranslation.value = false
    await getRandomWord() // 切换难度后立即加载该难度单词
  }

  const getRandomWord = async () => {
    loading.value = true
    try {
      const response = await wordAPI.getRandomWord(
        difficulty.value,
        currentWord.value ? currentWord.value.id : null
      )
      currentWord.value = response.data
      showTranslation.value = false
    } catch (error) {
      // 该难度无词时清空当前单词，让界面显示"生成词库"引导
      if (error.response && error.response.status === 404) {
        currentWord.value = null
      }
      console.error('获取单词失败:', error)
    } finally {
      loading.value = false
    }
  }

  const toggleTranslation = () => {
    showTranslation.value = !showTranslation.value
  }

  const markAsLearned = async (proficiency = 100) => {
    if (!currentWord.value) return

    try {
      await wordAPI.recordLearning(currentWord.value.id, {
        proficiency,
        mark_as_learned: true
      })
      learnedCount.value++
      await getRandomWord() // 加载下一个单词
    } catch (error) {
      console.error('记录学习失败:', error)
    }
  }

  const fetchStats = async () => {
    try {
      const response = await wordAPI.getStats()
      stats.value = response.data
    } catch (error) {
      console.error('获取统计失败:', error)
    }
  }

  const generateWords = async (count = 20) => {
    loading.value = true
    try {
      await wordAPI.generateWords(difficulty.value, count)
      await getRandomWord()
    } catch (error) {
      console.error('生成词库失败:', error)
    } finally {
      loading.value = false
    }
  }

  return {
    currentWord,
    difficulty,
    showTranslation,
    learnedCount,
    stats,
    loading,
    proficiencyPercentage,
    setDifficulty,
    getRandomWord,
    toggleTranslation,
    markAsLearned,
    fetchStats,
    generateWords
  }
})