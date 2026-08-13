import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000
})

// 词库相关
export const wordAPI = {
  // 生成词库
  generateWords: (difficulty, count = 10) =>
    api.post('/words/generate', null, { params: { difficulty, count } }),

  // 获取词库
  getWords: (difficulty, skip = 0, limit = 20) =>
    api.get('/words', { params: { difficulty, skip, limit } }),

  // 获取随机单词（可排除刚看过的词，避免连续重复）
  getRandomWord: (difficulty, excludeId = null) =>
    api.get('/study/random', { params: { difficulty, exclude_id: excludeId } }),

  // 记录学习
  recordLearning: (wordId, data) =>
    api.post('/study/record', data, { params: { word_id: wordId } }),

  // 获取统计
  getStats: () =>
    api.get('/stats')
}

export default api