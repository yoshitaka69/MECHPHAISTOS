<template>
  <aside>
    <div v-for="item in items" :key="item.name" draggable @dragstart="startDrag(item)">
      <img :src="item.icon" alt="" />
      <p>{{ item.name }}</p>
    </div>
  </aside>
</template>

<script>
export default {
  emits: ['itemDragged'],
  data() {
    return {
      items: [
        { name: 'Pump', icon: '/icons/pump-icon.png' },
        { name: 'Valve', icon: '/icons/valve-icon.png' },
        { name: 'Tank', icon: '/icons/tank-icon.png' }
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
  text-align: center;
}
img {
  max-width: 100%;
  height: auto;
}
p {
  margin: 0;
  font-size: 0.9rem;
}
</style>
