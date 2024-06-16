<template>
  <div
    class="canvas"
    @drop="dropItem"
    @dragover="allowDrop"
    ref="canvas"
    :class="{ grid: showGrid }"
  >
    <div
      v-for="item in items"
      :key="item.id"
      class="canvas-item"
      :style="{ top: item.y + 'px', left: item.x + 'px' }"
      draggable
      @dragstart="startDrag($event, item)"
      @drag="onDrag($event)"
      @dragend="endDrag($event)"
    >
      <img :src="getIcon(item.name)" alt="" />
      <p>{{ item.name }}</p>
    </div>
    <svg class="canvas-svg">
      <line
        v-for="line in lines"
        :key="line.id"
        :x1="line.x1"
        :y1="line.y1"
        :x2="line.x2"
        :y2="line.y2"
        stroke="black"
      />
      <line
        v-if="currentLine"
        :x1="currentLine.x1"
        :y1="currentLine.y1"
        :x2="currentLine.x2"
        :y2="currentLine.y2"
        stroke="black"
      />
    </svg>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  props: ['items', 'showGrid', 'selectedShape', 'lines'],
  setup(props, { emit }) {
    const currentLine = ref(null)
    const canvasRef = ref(null)
    const dragItem = ref(null)
    const offsetX = ref(0)
    const offsetY = ref(0)

    onMounted(() => {
      canvasRef.value = document.querySelector('.canvas')
    })

    const allowDrop = (event) => {
      event.preventDefault()
    }

    const startDrag = (event, item) => {
      dragItem.value = item
      offsetX.value = event.clientX - (item.x || 0)
      offsetY.value = event.clientY - (item.y || 0)
      console.log('startDrag:', item)
    }

    const onDrag = (event) => {
      if (dragItem.value) {
        let x = event.clientX - offsetX.value
        let y = event.clientY - offsetY.value

        // キャンバス内に位置を制限
        const canvas = canvasRef.value
        if (canvas) {
          x = Math.max(0, Math.min(x, canvas.clientWidth - 50))
          y = Math.max(0, Math.min(y, canvas.clientHeight - 50))
        }

        dragItem.value.x = x
        dragItem.value.y = y
        console.log('onDrag:', x, y)
      }
    }

    const endDrag = (event) => {
      if (dragItem.value) {
        let x = event.clientX - offsetX.value
        let y = event.clientY - offsetY.value

        // キャンバス内に位置を制限
        const canvas = canvasRef.value
        if (canvas) {
          x = Math.max(0, Math.min(x, canvas.clientWidth - 50))
          y = Math.max(0, Math.min(y, canvas.clientHeight - 50))
        }

        dragItem.value.x = x
        dragItem.value.y = y
        emit('updateItem', dragItem.value)
        dragItem.value = null
        console.log('endDrag:', x, y)
      }
    }

    const dropItem = (event) => {
      event.preventDefault()
      if (dragItem.value) {
        let x = event.clientX - offsetX.value
        let y = event.clientY - offsetY.value

        // キャンバス内に位置を制限
        const canvas = canvasRef.value
        if (canvas) {
          x = Math.max(0, Math.min(x, canvas.clientWidth - 50))
          y = Math.max(0, Math.min(y, canvas.clientHeight - 50))
        }

        dragItem.value.x = x
        dragItem.value.y = y
        emit('updateItem', dragItem.value)
        dragItem.value = null
        console.log('dropItem:', x, y)
      }
    }

    const startDrawing = (event) => {
      if (props.selectedShape === 'line') {
        currentLine.value = {
          x1: event.offsetX,
          y1: event.offsetY,
          x2: event.offsetX,
          y2: event.offsetY,
        }
      }
    }

    const draw = (event) => {
      if (currentLine.value) {
        currentLine.value.x2 = event.offsetX
        currentLine.value.y2 = event.offsetY
      }
    }

    const endDrawing = (event) => {
      if (currentLine.value) {
        props.lines.push({
          id: Date.now(),
          ...currentLine.value,
        })
        currentLine.value = null
      }
    }

    const getIcon = (name) => {
      switch (name) {
        case 'Pump':
          return '/icons/pump-icon.png'
        case 'Valve':
          return '/icons/valve-icon.png'
        case 'Tank':
          return '/icons/tank-icon.png'
        default:
          return ''
      }
    }

    return {
      allowDrop,
      startDrag,
      onDrag,
      endDrag,
      dropItem,
      startDrawing,
      draw,
      endDrawing,
      getIcon,
      currentLine,
      canvasRef,
    }
  }
}
</script>

<style>
.canvas {
  flex: 1;
  position: relative;
  background-color: white;
  border: 1px solid #ccc;
  overflow: hidden;
}
.canvas-item {
  position: absolute;
  padding: 0.5rem;
  text-align: center;
  cursor: move;
}
.canvas-svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
.grid {
  background-image: linear-gradient(
      0deg,
      transparent 24%,
      rgba(0, 0, 0, 0.1) 25%,
      rgba(0, 0, 0, 0.1) 26%,
      transparent 27%,
      transparent 74%,
      rgba(0, 0, 0, 0.1) 75%,
      rgba(0, 0, 0, 0.1) 76%,
      transparent 77%,
      transparent
    ),
    linear-gradient(
      90deg,
      transparent 24%,
      rgba(0, 0, 0, 0.1) 25%,
      rgba(0, 0, 0, 0.1) 26%,
      transparent 27%,
      transparent 74%,
      rgba(0, 0, 0, 0.1) 75%,
      rgba(0, 0, 0, 0.1) 76%,
      transparent 77%,
      transparent
    );
  background-size: 20px 20px;
}
</style>

