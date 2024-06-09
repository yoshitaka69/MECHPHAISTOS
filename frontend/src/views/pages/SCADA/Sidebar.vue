<template>
  <div class="sidebar">
    <p>Sidebar Content</p>
    <div class="icon" v-for="icon in icons" :key="icon.name" draggable="true" @dragstart="dragStart(icon)">
      <img :src="icon.src" :alt="icon.name" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sidebar',
  data() {
    return {
      icons: [
        { name: 'Pump', src: '/frontend/public/icons/pump.png' },
        { name: 'Valve', src: '/frontend/public/icons/valve.png' },
        // 他のアイコンを追加
      ],
    };
  },
  methods: {
    dragStart(icon, event) {
      event.dataTransfer.setData('icon', JSON.stringify(icon));
    },
  },
};
</script>

<style>
.sidebar {
  width: 200px;
  background-color: #f4f4f4;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.icon {
  margin-bottom: 10px;
  cursor: pointer;
}

.icon img {
  width: 100%;
  height: auto;
}
</style>
