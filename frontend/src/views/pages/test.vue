<template>
  <div id="app">
    <div class="sidebar">
      <div class="icon" @mousedown="startDrag('pump')">
        <img src="@/assets/Scada/pump-icon.png" alt="Pump" />
      </div>
      <div class="icon" @mousedown="startDrag('blower')">
        <img src="@/assets/Scada/blower-icon.png" alt="Blower" />
      </div>

      <!-- さらに他の描画ツールを追加できます -->
    </div>
    <div 
      class="canvas" 
      ref="canvas" 
      @dragover.prevent 
      @drop="onDrop">
      <draggable-resizable
        v-for="(item, index) in items"
        :key="index"
        :class="item.type"
        class="draggable-item"
        :init-w="50"
        :init-h="50"
        :w.sync="item.width"
        :h.sync="item.height"
        :x.sync="item.x"
        :y.sync="item.y"
        @dragging="updatePosition($event, index)"
        @resizing="updateSize($event, index)"
      >
        <img 
          v-if="item.type === 'pump'" 
          src="@/assets/Scada/pump-icon.png" 
          alt="Pump" 
        />
        <img 
          v-if="item.type === 'blower'" 
          src="@/assets/Scada/blower-icon.png" 
          alt="Blower" 
        />
        <!-- 他のアイテムの描画 -->
      </draggable-resizable>
    </div>
  </div>
</template>

<script>
import DraggableResizable from 'draggable-resizable-vue3';

export default {
  components: {
    DraggableResizable
  },
  data() {
    return {
      draggingItem: null,
      items: []
    };
  },
  methods: {
    startDrag(type) {
      this.draggingItem = { type };
    },
    onDrop(event) {
      if (this.draggingItem) {
        const rect = this.$refs.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        this.items.push({ type: this.draggingItem.type, x, y, width: 50, height: 50 });
        this.draggingItem = null;
      }
    },
    updatePosition(position, index) {
      this.items[index].x = position.x;
      this.items[index].y = position.y;
    },
    updateSize(size, index) {
      this.items[index].width = size.width;
      this.items[index].height = size.height;
    }
  }
};
</script>

<style scoped>
/* 他のスタイル */
#app {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 200px;
  background: #f4f4f4;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
}

.icon {
  margin-bottom: 20px;
  cursor: grab;
}

.icon img {
  width: 100%;
}

.canvas {
  flex: 1;
  position: relative;
  border: 1px solid #ccc;
  margin-left: 10px;
  background: #fff;
}

.draggable-item {
  position: absolute;
  cursor: move;
}

.pump img,
.blower img {
  width: 100%;
  height: 100%;
}
</style>
