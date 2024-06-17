<template>
  <div
    class="canvas"
    @drop="dropItem"
    @dragover="allowDrop"
    @mousedown="startDrawing"
    @mousemove="draw"
    @mouseup="endDrawing"
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
      <SignalLight
        :color1="item.signalColors.color1"
        :color2="item.signalColors.color2"
        :color3="item.signalColors.color3"
      />
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
      <path
        v-for="curve in curves"
        :key="curve.id"
        :d="curve.path"
        stroke="black"
        fill="none"
      />
      <rect
        v-for="rect in rectangles"
        :key="rect.id"
        :x="rect.x"
        :y="rect.y"
        :width="rect.width"
        :height="rect.height"
        stroke="black"
        fill="none"
      />
      <ellipse
        v-for="ellipse in ellipses"
        :key="ellipse.id"
        :cx="ellipse.cx"
        :cy="ellipse.cy"
        :rx="ellipse.rx"
        :ry="ellipse.ry"
        stroke="black"
        fill="none"
      />
      <polygon
        v-for="arrow in arrows"
        :key="arrow.id"
        :points="arrow.points"
        stroke="black"
        fill="none"
      />
      <text
        v-for="text in texts"
        :key="text.id"
        :x="text.x"
        :y="text.y"
        stroke="black"
      >
        {{ text.content }}
      </text>
      <line
        v-if="currentLine"
        :x1="currentLine.x1"
        :y1="currentLine.y1"
        :x2="currentLine.x2"
        :y2="currentLine.y2"
        stroke="black"
      />
      <path
        v-if="currentCurve"
        :d="currentCurve.path"
        stroke="black"
        fill="none"
      />
      <rect
        v-if="currentRectangle"
        :x="currentRectangle.x"
        :y="currentRectangle.y"
        :width="currentRectangle.width"
        :height="currentRectangle.height"
        stroke="black"
        fill="none"
      />
      <ellipse
        v-if="currentEllipse"
        :cx="currentEllipse.cx"
        :cy="currentEllipse.cy"
        :rx="currentEllipse.rx"
        :ry="currentEllipse.ry"
        stroke="black"
        fill="none"
      />
      <polygon
        v-if="currentArrow"
        :points="currentArrow.points"
        stroke="black"
        fill="none"
      />
      <text
        v-if="currentText"
        :x="currentText.x"
        :y="currentText.y"
        stroke="black"
      >
        {{ currentText.content }}
      </text>
    </svg>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import SignalLight from './SignalLight.vue'

export default {
  props: ['items', 'showGrid', 'selectedShape', 'lines', 'curves', 'rectangles', 'ellipses', 'arrows', 'texts'],
  components: { SignalLight },
  setup(props, { emit }) {
    const currentLine = ref(null)
    const currentCurve = ref(null)
    const currentRectangle = ref(null)
    const currentEllipse = ref(null)
    const currentArrow = ref(null)
    const currentText = ref(null)
    const canvasRef = ref(null)
    const dragItem = ref(null)
    const offsetX = ref(0)
    const offsetY = ref(0)
    const drawing = ref(false)

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
      drawing.value = true
      const startX = event.offsetX
      const startY = event.offsetY

      if (props.selectedShape === 'line') {
        currentLine.value = { x1: startX, y1: startY, x2: startX, y2: startY }
      } else if (props.selectedShape === 'curve') {
        currentCurve.value = { id: Date.now(), path: `M${startX},${startY} Q${startX},${startY} ${startX},${startY}` }
      } else if (props.selectedShape === 'rectangle') {
        currentRectangle.value = { x: startX, y: startY, width: 0, height: 0 }
      } else if (props.selectedShape === 'ellipse') {
        currentEllipse.value = { cx: startX, cy: startY, rx: 0, ry: 0 }
      } else if (props.selectedShape === 'arrow') {
        currentArrow.value = { id: Date.now(), points: `${startX},${startY} ${startX},${startY}` }
      } else if (props.selectedShape === 'text') {
        const textContent = prompt('Enter text:')
        if (textContent) {
          currentText.value = { x: startX, y: startY, content: textContent }
        } else {
          drawing.value = false
        }
      }
    }

    const draw = (event) => {
      if (!drawing.value) return

      const currentX = event.offsetX
      const currentY = event.offsetY

      if (currentLine.value) {
        currentLine.value.x2 = currentX
        currentLine.value.y2 = currentY
      } else if (currentCurve.value) {
        const [x1, y1] = currentCurve.value.path.match(/\d+/g).map(Number)
        currentCurve.value.path = `M${x1},${y1} Q${(x1 + currentX) / 2},${(y1 + currentY) / 2} ${currentX},${currentY}`
      } else if (currentRectangle.value) {
        currentRectangle.value.width = Math.abs(currentX - currentRectangle.value.x)
        currentRectangle.value.height = Math.abs(currentY - currentRectangle.value.y)
        if (currentX < currentRectangle.value.x) currentRectangle.value.x = currentX
        if (currentY < currentRectangle.value.y) currentRectangle.value.y = currentY
      } else if (currentEllipse.value) {
        currentEllipse.value.rx = Math.abs(currentX - currentEllipse.value.cx)
        currentEllipse.value.ry = Math.abs(currentY - currentEllipse.value.cy)
      } else if (currentArrow.value) {
        const [x1, y1] = currentArrow.value.points.match(/\d+/g).map(Number)
        currentArrow.value.points = `${x1},${y1} ${currentX},${currentY}`
      }
    }

    const endDrawing = (event) => {
      if (!drawing.value) return

      drawing.value = false

      if (currentLine.value) {
        props.lines.push({ ...currentLine.value, id: Date.now() })
        currentLine.value = null
      } else if (currentCurve.value) {
        props.curves.push({ ...currentCurve.value, id: Date.now() })
        currentCurve.value = null
      } else if (currentRectangle.value) {
        props.rectangles.push({ ...currentRectangle.value, id: Date.now() })
        currentRectangle.value = null
      } else if (currentEllipse.value) {
        props.ellipses.push({ ...currentEllipse.value, id: Date.now() })
        currentEllipse.value = null
      } else if (currentArrow.value) {
        props.arrows.push({ ...currentArrow.value, id: Date.now() })
        currentArrow.value = null
      } else if (currentText.value) {
        props.texts.push({ ...currentText.value, id: Date.now() })
        currentText.value = null
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
      currentCurve,
      currentRectangle,
      currentEllipse,
      currentArrow,
      currentText,
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
