<template>
  <div class="card">
    <!-- カードのタイトルを変更 -->
    <div class="card-header">
      <h5>Precision and Accuracy</h5>
    </div>
    <!-- カードのボディにコンテンツを追加 -->
    <div class="card-body">
      <p class="highlight">Precision: {{ precision }}%</p>
      <p class="highlight">Accuracy: {{ accuracy }}%</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      precision: 95.5, // サンプルデータ
      accuracy: 98.3 // サンプルデータ
    };
  }
};
</script>

<style scoped>
.card-header {
  background-color: #f8f9fa;
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
