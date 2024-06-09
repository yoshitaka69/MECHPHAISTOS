<template>
  <div class="canvas-wrapper" @dragover.prevent @drop="dropIcon">
    <canvas ref="canvas" :width="width" :height="height"></canvas>
    <div v-for="icon in placedIcons" :key="icon.id" class="placed-icon" :style="{ top: icon.y + 'px', left: icon.x + 'px' }">
      <img :src="icon.src" :alt="icon.name" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Canvas',
  props: {
    width: {
      type: Number,
      default: 1000,
    },
    height: {
      type: Number,
      default: 500,
    },
    gridVisible: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      placedIcons: [],
    };
  },
  methods: {
    drawGrid() {
      const canvas = this.$refs.canvas;
      const ctx = canvas.getContext('2d');

      ctx.clearRect(0, 0, this.width, this.height); // キャンバスをクリア

      // 背景を白色に設定
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, this.width, this.height);

      if (this.gridVisible) {
        ctx.strokeStyle = '#d3d3d3'; // グリッド線を灰色に設定
        const step = 20;

        for (let x = 0; x <= this.width; x += step) {
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, this.height);
          ctx.stroke();
        }

        for (let y = 0; y <= this.height; y += step) {
          ctx.beginPath();
          ctx.moveTo(0, y);
          ctx.lineTo(this.width, y);
          ctx.stroke();
        }
      }
    },
    dropIcon(event) {
      const rect = this.$refs.canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const icon = JSON.parse(event.dataTransfer.getData('icon'));
      this.placedIcons.push({
        id: Date.now(),
        src: icon.src,
        name: icon.name,
        x: x,
        y: y,
      });
    },
  },
  mounted() {
    this.drawGrid();
  },
  watch: {
    gridVisible() {
      this.drawGrid();
    },
  },
};
</script>

<style>
.canvas-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  padding: 0; /* 上下左右の余白を0に設定 */
  margin: 0; /* 上下左右の余白を0に設定 */
  position: relative;
}

canvas {
  border: 1px solid #000;
  background-color: #ffffff; /* キャンバスの背景を白色に設定 */
  padding: 0; /* 上下左右の余白を0に設定 */
  margin: 0; /* 上下左右の余白を0に設定 */
}

.placed-icon {
  position: absolute;
  transform: translate(-50%, -50%);
}
</style>
