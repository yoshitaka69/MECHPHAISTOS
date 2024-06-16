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
    const canvasItems = ref([]) // キャンバス上のアイテムを保持する配列
    const canvasLines = ref([]) // キャンバス上の線を保持する配列
    const showGrid = ref(false) // グリッド線の表示状態を管理するフラグ
    const selectedShape = ref(null) // 選択された形状を保持する変数
    const canvasRef = ref(null) // キャンバスの参照を保持する変数

    // キャンバスにアイテムを追加するメソッド
    const addItemToCanvas = (item) => {
      canvasItems.value.push(item)
    }

    // 選択された形状をキャンバスに追加するメソッド
    const addShapeToCanvas = (shape) => {
      selectedShape.value = shape
      console.log('addShapeToCanvas:', shape)
    }

    // キャンバス上のアイテムの位置を更新するメソッド
    const updateItemPosition = (item) => {
      const index = canvasItems.value.findIndex((i) => i.id === item.id)
      if (index !== -1) {
        canvasItems.value[index] = item
      }
    }

    // グリッド線の表示状態を切り替えるメソッド
    const toggleGridLines = () => {
      showGrid.value = !showGrid.value
    }

    // キャンバスの状態を保存するメソッド
    const saveCanvas = async () => {
      const data = {
        items: canvasItems.value,
        lines: canvasLines.value, // キャンバスの線を取得
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

    // キャンバスの状態を読み込むメソッド
    const loadCanvas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/canvas/')
        if (response.ok) {
          const data = await response.json()
          const latestCanvas = data[0] // 最新のキャンバスデータを取得
          if (latestCanvas) {
            canvasItems.value = latestCanvas.data.items
            canvasLines.value = latestCanvas.data.lines
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
