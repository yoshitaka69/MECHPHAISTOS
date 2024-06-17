<template>
  <div id="app">
    <Header @shapeAdded="addShapeToCanvas" />
    <div class="main">
      <Sidebar @itemDragged="addItemToCanvas" />
      <Canvas
        ref="canvasRef"
        :items="canvasItems"
        :selectedShape="selectedShape"
        :showGrid="showGrid"
        :lines="canvasLines"
        :curves="canvasCurves"
        :rectangles="canvasRectangles"
        :ellipses="canvasEllipses"
        :arrows="canvasArrows"
        :texts="canvasTexts"
        @itemDropped="addItemToCanvas"
        @updateItem="updateItemPosition"
      />
    </div>
    <Footer
      @toggleGrid="toggleGridLines"
      @saveCanvas="saveCanvas"
      @loadCanvas="loadCanvas"
    />
  </div>
</template>

<script>
import Header from './Header.vue'
import Sidebar from './Sidebar.vue'
import Canvas from './Canvas.vue'
import Footer from './Footer.vue'
import { ref } from 'vue'

export default {
  name: 'Scada',
  components: {
    Header,
    Sidebar,
    Canvas,
    Footer,
  },
  setup() {
    const canvasItems = ref([])
    const canvasLines = ref([])
    const canvasCurves = ref([])
    const canvasRectangles = ref([])
    const canvasEllipses = ref([])
    const canvasArrows = ref([])
    const canvasTexts = ref([])
    const showGrid = ref(false)
    const selectedShape = ref(null)
    const canvasRef = ref(null)

    const addItemToCanvas = (item) => {
      item.signalColors = { color1: 'gray', color2: 'gray', color3: 'gray' }
      canvasItems.value.push(item)
    }

    const addShapeToCanvas = (shape) => {
      selectedShape.value = shape
      console.log('addShapeToCanvas:', shape)
    }

    const updateItemPosition = (item) => {
      const index = canvasItems.value.findIndex((i) => i.id === item.id)
      if (index !== -1) {
        canvasItems.value[index] = item
      }
    }

    const toggleGridLines = () => {
      showGrid.value = !showGrid.value
    }

    const saveCanvas = async () => {
      const data = {
        items: canvasItems.value,
        lines: canvasLines.value,
        curves: canvasCurves.value,
        rectangles: canvasRectangles.value,
        ellipses: canvasEllipses.value,
        arrows: canvasArrows.value,
        texts: canvasTexts.value,
      }

      try {
        const response = await fetch('http://127.0.0.1:8000/api/canvas/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ data }),
        })

        if (response.ok) {
          alert('Canvas saved!')
        } else {
          alert('Failed to save canvas.')
        }
      } catch (error) {
        console.error('Error saving canvas:', error)
        alert('Error saving canvas.')
      }
    }

    const loadCanvas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/canvas/')
        if (response.ok) {
          const data = await response.json()
          const latestCanvas = data[0]
          if (latestCanvas) {
            canvasItems.value = latestCanvas.data.items
            canvasLines.value = latestCanvas.data.lines
            canvasCurves.value = latestCanvas.data.curves
            canvasRectangles.value = latestCanvas.data.rectangles
            canvasEllipses.value = latestCanvas.data.ellipses
            canvasArrows.value = latestCanvas.data.arrows
            canvasTexts.value = latestCanvas.data.texts
          }
        } else {
          alert('Failed to load canvas.')
        }
      } catch (error) {
        console.error('Error loading canvas:', error)
        alert('Error loading canvas.')
      }
    }

    return {
      canvasItems,
      canvasLines,
      canvasCurves,
      canvasRectangles,
      canvasEllipses,
      canvasArrows,
      canvasTexts,
      selectedShape,
      showGrid,
      addItemToCanvas,
      addShapeToCanvas,
      updateItemPosition,
      toggleGridLines,
      saveCanvas,
      loadCanvas,
      canvasRef,
    }
  }
}
</script>




<style>
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.main {
  display: flex;
  flex: 1;
}
</style>
