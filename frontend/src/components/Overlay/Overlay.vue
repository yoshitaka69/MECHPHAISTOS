<template>
  <div v-if="visible" class="overlay">
    <div class="overlay-text">secret</div>
  </div>
</template>

<script>
export default {
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明の背景 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* 他の要素の上に表示するために高い値を設定 */
}

.overlay-text {
  font-size: 3em;
  color: white;
  font-weight: bold;
  transform: rotate(-45deg); /* 文字を斜めに */
  border: 5px solid white; /* □で囲む */
  padding: 20px;
}
</style>
