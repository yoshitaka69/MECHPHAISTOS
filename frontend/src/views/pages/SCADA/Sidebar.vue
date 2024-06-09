<template>
  <div class="sidebar">
    <p>Sidebar Content</p>
    <div class="icon" v-for="icon in icons" :key="icon.name" @click="selectIcon(icon)">
      <img :src="icon.src" :alt="icon.name" />
    </div>
  </div>
</template>

<script>
import pumpIcon from '@/assets/icons/pump.png';
import valveIcon from '@/assets/icons/valve.png';

export default {
  name: 'Sidebar',
  data() {
    return {
      icons: [
        { name: 'Pump', src: pumpIcon },
        { name: 'Valve', src: valveIcon },
        // 他のアイコンを追加
      ],
    };
  },
  methods: {
    selectIcon(icon) {
      this.$emit('icon-selected', icon);
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
  margin-bottom: 20px; /* マージンを調整してアイコン間のスペースを広げる */
  cursor: pointer;
}

.icon img {
  width: 100px; /* アイコンの幅を大きく設定 */
  height: 100px; /* アイコンの高さを大きく設定 */
  object-fit: contain; /* 画像のアスペクト比を保持 */
}
</style>
