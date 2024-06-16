<template>
  <div class="header-bar">
    <button @click="selectShape('line')">直線</button>
    <button @click="selectShape('curve')">曲線</button>
    <button @click="selectShape('rectangle')">四角形</button>
    <button @click="selectShape('ellipse')">楕円</button>
    <button @click="selectShape('arrow')">矢印</button>
    <button @click="selectShape('text')">テキスト</button>
  </div>
</template>

<script>
export default {
  emits: ['shapeAdded'],
  methods: {
    selectShape(shape) {
      this.$emit('shapeAdded', shape)
      console.log('selectShape:', shape)
    }
  }
}
</script>


<style>
.header-bar {
  background-color: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-around;
}
.header-bar button {
  background: none;
  border: 1px solid white;
  color: white;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
.header-bar button:hover {
  background-color: white;
  color: #333;
}
</style>
