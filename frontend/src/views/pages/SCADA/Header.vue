<template>
  <header>
    <button @click="addLine('straight')">直線</button>
    <button @click="addLine('curve')">曲線</button>
  </header>
</template>

<script>
export default {
  emits: ['lineAdded'],
  methods: {
    addLine(type) {
      this.$emit('lineAdded', { type })
    }
  }
}
</script>

<style>
header {
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
