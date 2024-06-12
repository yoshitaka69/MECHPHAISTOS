<template>
  <div id="app">
    <Header />
    <div class="main">
      <Sidebar @itemDragged="addItemToCanvas"/>
      <Canvas ref="canvasRef" :items="canvasItems" @lineAdded="addLineToCanvas"/>
    </div>
    <Footer @toggleGrid="toggleGridLines"/>
  </div>
</template>

<script>
import Header from './Header.vue'
import Sidebar from './Sidebar.vue'
import Canvas from './Canvas.vue'
import Footer from './Footer.vue'
import { ref } from 'vue'

export default {
  name: 'App',
  components: {
    Header,
    Sidebar,
    Canvas,
    Footer,
  },
  setup() {
    const canvasItems = ref([])
    const canvasRef = ref(null)

    const addItemToCanvas = (item) => {
      canvasItems.value.push(item)
    }

    const addLineToCanvas = (line) => {
      canvasItems.value.push(line)
    }

    const toggleGridLines = () => {
      canvasRef.value.toggleGrid()
    }

    return {
      canvasItems,
      canvasRef,
      addItemToCanvas,
      addLineToCanvas,
      toggleGridLines
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
