<template>
  <div
    class="canvas"
    @drop="dropItem"
    @dragover="allowDrop"
    @mousedown="startDrawing"
    @mousemove="draw"
    @mouseup="endDrawing"
    :class="{ grid: showGrid }"
  >
    <div
      v-for="item in items"
      :key="item.id"
      class="canvas-item"
      :style="{ top: item.y + 'px', left: item.x + 'px' }"
      draggable
      @dragstart="startDrag($event, item)"
      @dragend="endDrag($event, item)"
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
import { ref, watchEffect } from 'vue'

export default {
  props: ['items', 'showGrid', 'selectedShape'],
  setup(props, { emit }) {
    const lines = ref([]) // キャンバス上の線を保持する配列
    const currentLine = ref(null) // 現在描画中の線を保持する変数
    let dragItem = null // ドラッグ中のアイテムを保持する変数
    let drawing = false // 描画中かどうかを示すフラグ
    let startX = 0 // 描画開始位置のX座標
    let startY = 0 // 描画開始位置のY座標

    watchEffect(() => {
      console.log('selectedShape:', props.selectedShape)
    })

    // ドロップを許可するメソッド
    const allowDrop = (event) => {
      event.preventDefault()
    }

    // ドラッグを開始するメソッド
    const startDrag = (event, item) => {
      dragItem = item
      console.log('startDrag:', item)
    }

    // ドラッグを終了するメソッド
    const endDrag = (event, item) => {
      if (dragItem) {
        dragItem.x = event.offsetX
        dragItem.y = event.offsetY
        emit('updateItem', dragItem)
        dragItem = null
        console.log('endDrag:', item)
      }
    }

    // ドロップされたアイテムを処理するメソッド
    const dropItem = (event) => {
      if (dragItem) {
        dragItem.x = event.offsetX
        dragItem.y = event.offsetY
        emit('updateItem', dragItem)
        console.log('dropItem:', dragItem)
      }
    }

    // 線の描画を開始するメソッド
    const startDrawing = (event) => {
      if (props.selectedShape === 'line') {
        drawing = true
        startX = event.offsetX
        startY = event.offsetY
        currentLine.value = { x1: startX, y1: startY, x2: startX, y2: startY }
        console.log('startDrawing:', currentLine.value)
      }
    }

    // 線を描画するメソッド
    const draw = (event) => {
      if (drawing && props.selectedShape === 'line') {
        const x2 = event.offsetX
        const y2 = event.offsetY
        currentLine.value = { x1: startX, y1: startY, x2, y2 }
        console.log('draw:', currentLine.value)
      }
    }

    // 線の描画を終了するメソッド
    const endDrawing = (event) => {
      if (drawing && props.selectedShape === 'line') {
        const x2 = event.offsetX
        const y2 = event.offsetY
        lines.value.push({ id: Date.now(), x1: startX, y1: startY, x2, y2 })
        drawing = false
        console.log('endDrawing:', lines.value)
        currentLine.value = null
      }
    }

    // アイテムのアイコンを取得するメソッド
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
      endDrag,
      dropItem,
      getIcon,
      startDrawing,
      draw,
      endDrawing,
      lines,
      currentLine,
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
