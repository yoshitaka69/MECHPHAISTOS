<template>
  <aside>
    <div v-for="item in items" :key="item.name" draggable @dragstart="startDrag(item)">
      {{ item.name }}
    </div>
  </aside>
</template>

<script>
export default {
  emits: ['itemDragged'],
  data() {
    return {
      items: [
        { name: 'Pump' },
        { name: 'Valve' },
        { name: 'Tank' }
      ]
    }
  },
  methods: {
    startDrag(item) {
      this.$emit('itemDragged', item)
    }
  }
}
</script>

<style>
aside {
  background-color: #f4f4f4;
  width: 200px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
div[draggable] {
  cursor: grab;
  padding: 0.5rem;
  border: 1px solid #ccc;
  background-color: white;
}
</style>
