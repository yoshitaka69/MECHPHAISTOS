<template>
  <div class="bubble-comment">
    <div class="image-container">
      <img :src="imageSrc" alt="icon" class="icon" />
      <div class="image-caption">Castor</div>
    </div>
    <div class="comment-bubble">
      <!-- 吹き出しの三角を含める -->
      <div class="comment-arrow"></div>
      <!-- カードのボディにコンテンツを追加 -->
      <div class="card-body">
        <p class="highlight">Precision: {{ precision }}%</p>
        <p class="highlight">Accuracy: {{ accuracy }}%</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Viteではimportを使用して画像を読み込む
import imageSrc from '@/assets/Castor.png'; // 画像ファイル名を変更する場合、こちらも修正してください

const precision = ref(95.5); // サンプルデータ
const accuracy = ref(98.3); // サンプルデータ
</script>

<style scoped>
.bubble-comment {
  position: relative;
  display: flex;
  align-items: stretch;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
}

.image-container {
  display: inline-block;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  margin-right: 20px;
  height: 100%;
}

.icon {
  width: 220px;
  height: auto;
}

.image-caption {
  margin-top: 10px;
  font-size: 14px;
  font-weight: bold;
}

.comment-bubble {
  background-color: white;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  width: 70%;
  height: 100%;
  position: relative;
  font-size: 24px;
  font-weight: bold;
  white-space: pre-line;
}

.comment-arrow {
  position: absolute;
  left: -10px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-right: 15px solid white;
}

.card-header {
  background-color: #ffecb3; /* 薄い橙色に変更 */
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

.card-body {
  padding: 1rem;
}

.highlight {
  font-weight: bold;
  color: #ff5722; /* 色を変更 */
  font-size: 1.5rem; /* フォントサイズを大きく */
}
</style>
