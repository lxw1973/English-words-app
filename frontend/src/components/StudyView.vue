<template>
  <div class="study-container">
    <!-- 难度选择 -->
    <div class="difficulty-selector mb-8 flex gap-3 justify-center flex-wrap">
      <button
        v-for="level in ['CET4', 'CET6', 'BEC', 'TOEFL', 'IELTS']"
        :key="level"
        @click="wordStore.setDifficulty(level)"
        :class="[
          'px-6 py-2 rounded-full font-semibold transition-all',
          wordStore.difficulty === level
            ? 'bg-indigo-600 text-white shadow-lg scale-105'
            : 'bg-white text-gray-700 hover:shadow-md'
        ]"
      >
        {{ difficultyLabel[level] }}
      </button>
    </div>

    <!-- 单词卡片 -->
    <div class="flex justify-center mb-8">
      <div
        v-if="wordStore.currentWord"
        class="study-card bg-white rounded-2xl shadow-2xl p-12 max-w-2xl w-full transform transition-all"
      >
        <!-- 单词 -->
        <div class="text-center mb-8">
          <h1 class="text-6xl font-bold text-indigo-600 mb-2">
            {{ wordStore.currentWord.word }}
          </h1>
          <p class="text-2xl text-gray-500">
            {{ wordStore.currentWord.phonetic }}
          </p>
          <span class="inline-block mt-3 px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
            {{ wordStore.currentWord.pos }}
          </span>
        </div>

        <!-- 翻译和定义（可切换显示） -->
        <div
          class="flip-card cursor-pointer mb-8 h-40 perspective"
          @click="wordStore.toggleTranslation()"
        >
          <div
            class="flip-card-inner relative w-full h-full transition-transform duration-500"
            :style="{ transform: wordStore.showTranslation ? 'rotateY(180deg)' : 'rotateY(0deg)' }"
          >
            <!-- 正面：中文 -->
            <div
              class="flip-card-front absolute w-full h-full bg-gradient-to-br from-green-100 to-green-200 rounded-xl p-6 flex items-center justify-center"
              :style="{ backfaceVisibility: 'hidden' }"
            >
              <div class="text-center">
                <p class="text-gray-600 text-sm mb-2">点击查看定义</p>
                <p class="text-3xl font-bold text-green-700">
                  {{ wordStore.currentWord.meaning }}
                </p>
              </div>
            </div>

            <!-- 背面：定义 -->
            <div
              class="flip-card-back absolute w-full h-full bg-gradient-to-br from-purple-100 to-purple-200 rounded-xl p-6 flex items-center justify-center"
              :style="{ transform: 'rotateY(180deg)', backfaceVisibility: 'hidden' }"
            >
              <div class="text-center">
                <p class="text-purple-700 text-lg">
                  {{ wordStore.currentWord.definition }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- 例句 -->
        <div class="bg-blue-50 rounded-lg p-6 mb-8">
          <p class="text-gray-600 text-sm mb-2">例句：</p>
          <p class="text-lg font-semibold text-blue-900 mb-3">
            {{ wordStore.currentWord.example }}
          </p>
          <p class="text-gray-700">{{ wordStore.currentWord.example_cn }}</p>
        </div>

        <!-- 学习进度条 -->
        <div class="mb-8">
          <div class="flex justify-between mb-2">
            <span class="text-sm font-semibold text-gray-700">熟练度</span>
            <span class="text-sm font-bold text-indigo-600">{{ Math.round(wordStore.proficiencyPercentage) }}%</span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-3">
            <div
              class="bg-gradient-to-r from-green-400 to-blue-500 h-3 rounded-full transition-all duration-500"
              :style="{ width: wordStore.proficiencyPercentage + '%' }"
            ></div>
          </div>
        </div>

        <!-- 操作按钮 -->
        <div class="flex gap-4 justify-center flex-wrap">
          <button
            @click="wordStore.getRandomWord"
            class="px-6 py-3 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition-all font-semibold"
            :disabled="wordStore.loading"
          >
            ⏭️ 下一个
          </button>
          <button
            @click="() => wordStore.markAsLearned(75)"
            class="px-6 py-3 bg-yellow-500 text-white rounded-lg hover:bg-yellow-600 transition-all font-semibold"
          >
            👍 比较熟悉
          </button>
          <button
            @click="() => wordStore.markAsLearned(100)"
            class="px-6 py-3 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-all font-semibold"
          >
            ✓ 完全掌握
          </button>
          <button
            @click="() => wordStore.generateWords(20)"
            class="px-6 py-3 bg-indigo-500 text-white rounded-lg hover:bg-indigo-600 transition-all font-semibold"
            :disabled="wordStore.loading"
          >
            🤖 生成更多词库
          </button>
        </div>
      </div>

      <!-- 加载状态 -->
      <div v-else-if="wordStore.loading" class="text-center">
        <div class="inline-block animate-spin">
          <span class="text-4xl">⚙️</span>
        </div>
        <p class="mt-4 text-lg text-gray-600">加载中...</p>
      </div>

      <!-- 无数据 -->
      <div v-else class="text-center">
        <p class="text-xl text-gray-600 mb-6">该难度还没有词库，点击生成</p>
        <button
          @click="wordStore.generateWords(20)"
          class="px-8 py-3 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 font-semibold"
        >
          🤖 生成词库 (20个)
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useWordStore } from '../stores/wordStore'
import { onMounted } from 'vue'

const wordStore = useWordStore()

const difficultyLabel = {
  CET4: '🎓 四级',
  CET6: '📚 六级',
  BEC: '💼 商务',
  TOEFL: '🌍 托福',
  IELTS: '✈️ 雅思'
}

onMounted(() => {
  wordStore.getRandomWord()
})
</script>

<style scoped>
.study-card {
  animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.flip-card {
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card-front,
.flip-card-back {
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}
</style>