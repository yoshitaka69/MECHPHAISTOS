<template>
  <div class="canvas" @drop="dropItem" @dragover="allowDrop">
    <div v-for="item in items" :key="item.id" class="canvas-item" :style="{ top: item.y + 'px', left: item.x + 'px' }">
      {{ item.name }}
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  props: ['items'],
  setup() {
    const canvas = ref(null)

    const allowDrop = (event) => {
      event.preventDefault()
    }

    const dropItem = (event) => {
      const item = JSON.parse(event.dataTransfer.getData('item'))
      item.x = event.offsetX
      item.y = event.offsetY
      item.id = Date.now()
      canvas.value.$emit('itemDropped', item)
    }

    const toggleGrid = () => {
      canvas.value.classList.toggle('grid')
    }

    return {
      canvas,
      allowDrop,
      dropItem,
      toggleGrid
    }
  }
}
</script>

<style>
.canvas {
  flex: 1;
  position: relative;
  background-color: white;
}
.canvas-item {
  position: absolute;
  padding: 0.5rem;
  background-color: lightgrey;
  border: 1px solid #ccc;
}
.grid {
  background-image: linear-gradient(0deg, transparent 24%, rgba(0, 0, 0, 0.1) 25%, rgba(0, 0, 0, 0.1) 26%, transparent 27%, transparent 74%, rgba(0, 0, 0, 0.1) 75%, rgba(0, 0, 0, 0.1) 76%, transparent 77%, transparent), linear-gradient(90deg, transparent 24%, rgba(0, 0, 0, 0.1) 25%, rgba(0, 0, 0, 0.1) 26%, transparent 27%, transparent 74%, rgba(0, 0, 0, 0.1) 75%, rgba(0, 0, 0, 0.1) 76%, transparent 77%, transparent);
  background-size: 20px 20px;
}
</style>
