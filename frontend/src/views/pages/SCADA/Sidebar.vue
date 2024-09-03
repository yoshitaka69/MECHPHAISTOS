<template>
  <aside class="app-sidebar">
    <div @click="$emit('itemSelected', { name: 'Pump', icon: 'pump-icon.png' })">
      <img src="/icons/pump-icon.png" alt="Pump" />
      <p>Pump</p>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'Sidebar'
}
</script>

<style scoped>
.app-sidebar {
  width: 200px;
  background-color: #f4f4f4;
  padding: 1rem;
}
.app-sidebar div {
  margin-bottom: 1rem;
  cursor: pointer;
  text-align: center;
}
.app-sidebar img {
  max-width: 100%;
}
</style>
