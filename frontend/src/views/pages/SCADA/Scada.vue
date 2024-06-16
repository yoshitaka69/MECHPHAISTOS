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
        @itemDropped="addItemToCanvas"
        @updateItem="updateItemPosition"
      />
    </div>
    <Footer @toggleGrid="toggleGridLines" />
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

    return {
      canvasItems,
      selectedShape,
      showGrid,
      addItemToCanvas,
      addShapeToCanvas,
      updateItemPosition,
      toggleGridLines,
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
