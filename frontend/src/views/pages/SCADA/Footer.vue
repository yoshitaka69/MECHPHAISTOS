<template>
  <footer class="app-footer">
    <button @click="$emit('toggleGrid')">グリッド線オン/オフ</button>
    <button @click="$emit('saveCanvas')">保存</button>
    <button @click="$emit('loadCanvas')">読み込み</button>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.app-footer {
  background-color: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-around;
}
button {
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
button:hover {
  background-color: white;
  color: #333;
}
</style>
