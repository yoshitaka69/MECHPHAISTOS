<template>
  <div class="canvas">
    <draggable v-model="equipmentList" @end="onDragEnd">
      <template #item="{ element }">
        <div class="equipment" :style="{ top: element.top + 'px', left: element.left + 'px' }">
          <img :src="element.icon" alt="equipment" draggable="false" />
        </div>
      </template>
    </draggable>
  </div>
</template>

<script>
import draggable from 'vuedraggable';

export default {
  name: 'Canvas',
  components: {
    draggable
  },
  data() {
    return {
      equipmentList: [
        { id: 1, icon: 'path/to/icon1.png', top: 0, left: 0 },
        { id: 2, icon: 'path/to/icon2.png', top: 0, left: 0 }
      ]
    };
  },
  methods: {
    onDragEnd(event) {
      console.log('Drag ended', event);
    }
  }
};
</script>

<style>
.canvas {
  width: 100%;
  height: 100vh;
  border: 1px solid #ccc;
  position: relative;
}
.equipment {
  position: absolute;
  cursor: move;
}
.equipment img {
  width: 50px;
  height: 50px;
}
</style>
