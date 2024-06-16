<template>
  <div class="footer-bar">
    <button @click="toggleGrid">グリッド線オン/オフ</button>
    <button @click="saveCanvas">保存</button>
    <button @click="loadCanvas">読み込み</button>
  </div>
</template>

<script>
export default {
  emits: ['toggleGrid', 'saveCanvas', 'loadCanvas'],
  methods: {
    toggleGrid() {
      this.$emit('toggleGrid')
    },
    saveCanvas() {
      this.$emit('saveCanvas')
    },
    loadCanvas() {
      this.$emit('loadCanvas')
    }
  }
}
</script>

<style>
.footer-bar {
  background-color: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}
.footer-bar button {
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
.footer-bar button:hover {
  background-color: white;
  color: #333;
}
</style>
