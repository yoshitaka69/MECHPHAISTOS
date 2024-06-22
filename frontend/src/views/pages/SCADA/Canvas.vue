<template>
  <div class="container">
    <!-- サイドバー -->
    <div class="sidebar">
      <img :src="pumpIconSrc" @click="addPumpIcon" class="icon" alt="Pump Icon" />
    </div>
    <!-- 描画ツールのボタン -->
    <div class="toolbar">
      <button @click="setDrawingMode('line')">Draw Line</button>
      <button @click="setDrawingMode('spline')">Draw Spline</button>
      <button @click="setDrawingMode('circle')">Draw Circle</button>
      <button @click="setDrawingMode('rect')">Draw Rectangle</button>
      <button @click="setDrawingMode('text')">Draw Text</button>
      <button @click="zoomIn">Zoom In</button>
      <button @click="zoomOut">Zoom Out</button>
    </div>
    <!-- キャンバス -->
    <div class="canvas-container">
      <v-stage ref="stage" :config="stageConfig">
        <v-layer ref="layer">
          <!-- 背景用の白い矩形 -->
          <v-rect :config="backgroundConfig" />
          <!-- 描画した図形を表示 -->
          <v-line v-for="(line, index) in lines" :key="index" :config="line" @dragend="onDragEnd(index, 'line')" draggable />
          <v-rect v-for="(rect, index) in rects" :key="index" :config="rect" @dragend="onDragEnd(index, 'rect')" draggable />
          <v-circle v-for="(circle, index) in circles" :key="index" :config="circle" @dragend="onDragEnd(index, 'circle')" draggable />
          <v-text v-for="(text, index) in texts" :key="index" :config="text" @dragend="onDragEnd(index, 'text')" draggable />
          <v-image v-for="(pump, index) in pumps" :key="index" :config="pump.config" @dragend="onDragEnd(index, 'pump')" />
        </v-layer>
      </v-stage>
    </div>
  </div>
</template>

<script>
import pumpIcon from '@/assets/pump_icon.png'

export default {
  data() {
    return {
      stageConfig: {
        width: window.innerWidth - 100,
        height: window.innerHeight - 50,
        scaleX: 1,
        scaleY: 1,
      },
      backgroundConfig: {
        x: 0,
        y: 0,
        width: window.innerWidth - 100,
        height: window.innerHeight - 50,
        fill: 'white',
      },
      drawingMode: 'none',
      isDrawing: false,
      lines: [],
      rects: [],
      circles: [],
      texts: [],
      pumps: [],
      currentShape: null,
      pumpIconSrc: pumpIcon,
    }
  },
  methods: {
    setDrawingMode(mode) {
      this.drawingMode = mode;
    },
    startDrawing(e) {
      if (this.drawingMode === 'none') return;
      this.isDrawing = true;
      const stage = this.$refs.stage.getStage();
      const pointerPosition = stage.getPointerPosition();
      if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
        this.currentShape = [{ x: pointerPosition.x, y: pointerPosition.y }];
      } else if (this.drawingMode === 'rect') {
        this.currentShape = {
          x: pointerPosition.x,
          y: pointerPosition.y,
          width: 0,
          height: 0,
          fill: 'transparent',
          stroke: 'black',
          strokeWidth: 2,
        };
        this.rects.push(this.currentShape);
      } else if (this.drawingMode === 'circle') {
        this.currentShape = {
          x: pointerPosition.x,
          y: pointerPosition.y,
          radius: 0,
          fill: 'transparent',
          stroke: 'black',
          strokeWidth: 2,
        };
        this.circles.push(this.currentShape);
      } else if (this.drawingMode === 'text') {
        this.currentShape = {
          x: pointerPosition.x,
          y: pointerPosition.y,
          text: 'Sample Text',
          fontSize: 20,
          fill: 'black',
        };
        this.texts.push(this.currentShape);
      }
    },
    draw(e) {
      if (!this.isDrawing) return;
      const stage = this.$refs.stage.getStage();
      const pointerPosition = stage.getPointerPosition();
      if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
        this.currentShape = [
          ...this.currentShape,
          { x: pointerPosition.x, y: pointerPosition.y },
        ];
        this.lines = [
          ...this.lines.slice(0, -1),
          {
            points: this.currentShape.flatMap(point => [point.x, point.y]),
            stroke: 'black',
            strokeWidth: 2,
            lineCap: 'round',
            lineJoin: this.drawingMode === 'spline' ? 'round' : 'miter',
          },
        ];
      } else if (this.drawingMode === 'rect') {
        const rect = this.currentShape;
        rect.width = pointerPosition.x - rect.x;
        rect.height = pointerPosition.y - rect.y;
      } else if (this.drawingMode === 'circle') {
        const circle = this.currentShape;
        const dx = pointerPosition.x - circle.x;
        const dy = pointerPosition.y - circle.y;
        circle.radius = Math.sqrt(dx * dx + dy * dy);
      }
    },
    endDrawing() {
      if (!this.isDrawing) return;
      this.isDrawing = false;
      if (this.drawingMode === 'line' || this.drawingMode === 'spline') {
        this.lines.push({
          points: this.currentShape.flatMap(point => [point.x, point.y]),
          stroke: 'black',
          strokeWidth: 2,
          lineCap: 'round',
          lineJoin: this.drawingMode === 'spline' ? 'round' : 'miter',
        });
      }
      this.currentShape = null;
      this.drawingMode = 'none';
    },
    addPumpIcon() {
      const stage = this.$refs.stage.getStage();
      const pointerPosition = stage.getPointerPosition();
      const img = new window.Image();
      img.src = this.pumpIconSrc;
      img.onload = () => {
        this.pumps.push({
          config: {
            x: pointerPosition.x,
            y: pointerPosition.y,
            image: img,
            width: 50,
            height: 50,
            draggable: true,
          },
        });
      }
    },
    onDragEnd(index, type) {
      const shape = this[type + 's'][index].config;
      const stage = this.$refs.stage.getStage();
      const pointerPosition = stage.getPointerPosition();
      shape.x = pointerPosition.x;
      shape.y = pointerPosition.y;
    },
    zoomIn() {
      this.stageConfig.scaleX *= 1.2;
      this.stageConfig.scaleY *= 1.2;
    },
    zoomOut() {
      this.stageConfig.scaleX /= 1.2;
      this.stageConfig.scaleY /= 1.2;
    },
    handleKeyDown(e) {
      if (e.key === 'Escape' || e.key === 'Backspace') {
        this.deleteSelectedShape();
      }
    },
    deleteSelectedShape() {
      // 選択された図形を削除する処理
      // ここでは仮に最後に追加された図形を削除する実装例を示します
      if (this.lines.length) {
        this.lines.pop();
      } else if (this.rects.length) {
        this.rects.pop();
      } else if (this.circles.length) {
        this.circles.pop();
      } else if (this.texts.length) {
        this.texts.pop();
      } else if (this.pumps.length) {
        this.pumps.pop();
      }
    },
  },
  mounted() {
    const stage = this.$refs.stage.getStage();
    stage.on('mousedown touchstart', this.startDrawing);
    stage.on('mousemove touchmove', this.draw);
    stage.on('mouseup touchend', this.endDrawing);
    window.addEventListener('keydown', this.handleKeyDown);
  },
  beforeDestroy() {
    window.removeEventListener('keydown', this.handleKeyDown);
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  display: flex;
}

.container {
  display: flex;
  width: 100vw;
  height: 100vh;
}

.sidebar {
  width: 100px;
  background-color: #f0f0f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

.icon {
  width: 50px;
  height: 50px;
  margin-bottom: 20px;
  cursor: pointer;
}

.toolbar {
  width: calc(100% - 100px);
  height: 50px;
  background-color: #ccc;
  display: flex;
  align-items: center;
  padding: 0 10px;
}

.canvas-container {
  flex-grow: 1;
}
</style>
