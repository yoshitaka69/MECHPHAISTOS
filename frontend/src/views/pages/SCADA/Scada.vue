<template>
  <div id="app">
    <Header />
    <div class="main-content">
      <Sidebar />
      <div class="canvas-container">
        <Canvas ref="canvas" :width="canvasWidth" :height="canvasHeight" :gridVisible="gridVisible" />
      </div>
    </div>
    <Footer :gridVisible="gridVisible" @toggle-grid="toggleGrid" />
  </div>
</template>

<script>
import Header from './Header.vue';
import Sidebar from './Sidebar.vue';
import Canvas from './Canvas.vue';
import Footer from './Footer.vue';

export default {
  name: 'Scada',
  components: {
    Header,
    Sidebar,
    Canvas,
    Footer,
  },
  data() {
    return {
      canvasWidth: 1000, // キャンバスの幅
      canvasHeight: 500, // キャンバスの高さ
      gridVisible: true,
    };
  },
  methods: {
    toggleGrid() {
      this.gridVisible = !this.gridVisible;
    },
  },
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 0;
  padding: 0;
}

.header {
  flex-shrink: 0;
}

.footer {
  flex-shrink: 0;
}

.main-content {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.sidebar {
  flex-shrink: 0;
}

.canvas-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0; /* 上下左右の余白を0に設定 */
  box-sizing: border-box;
}
</style>
