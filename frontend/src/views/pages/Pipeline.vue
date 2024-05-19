<template>
  <div class="pipeline-container">
    <svg @mousedown="startDrawing" @mouseup="stopDrawing" @mousemove="draw">
      <line v-for="(line, index) in lines" :key="index" :x1="line.x1" :y1="line.y1" :x2="line.x2" :y2="line.y2" stroke="black" />
      <line v-if="drawing" :x1="currentLine.x1" :y1="currentLine.y1" :x2="currentLine.x2" :y2="currentLine.y2" stroke="black" />
    </svg>
  </div>
</template>

<script>
export default {
  name: 'Pipeline',
  data() {
    return {
      lines: [],
      drawing: false,
      currentLine: { x1: 0, y1: 0, x2: 0, y2: 0 }
    };
  },
  methods: {
    startDrawing(event) {
      this.drawing = true;
      this.currentLine.x1 = event.offsetX;
      this.currentLine.y1 = event.offsetY;
      this.currentLine.x2 = event.offsetX;
      this.currentLine.y2 = event.offsetY;
    },
    stopDrawing() {
      if (this.drawing) {
        this.lines.push({ ...this.currentLine });
        this.drawing = false;
      }
    },
    draw(event) {
      if (this.drawing) {
        this.currentLine.x2 = event.offsetX;
        this.currentLine.y2 = event.offsetY;
      }
    }
  }
};
</script>

<style>
.pipeline-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}
svg {
  width: 100%;
  height: 100%;
}
</style>
