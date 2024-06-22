<template>
  <header class="app-header">
    <button @click="$emit('shapeSelected', 'line')">直線</button>
    <button @click="$emit('shapeSelected', 'arrow')">矢印</button>
    <button @click="$emit('shapeSelected', 'rectangle')">四角形</button>
    <button @click="$emit('shapeSelected', 'ellipse')">楕円</button>
    <button @click="$emit('shapeSelected', 'text')">テキスト</button>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.app-header {
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
