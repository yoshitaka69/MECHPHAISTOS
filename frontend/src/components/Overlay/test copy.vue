// src/App.vue
<template>
  <div id="app">
    <Overlay :visible="isRestricted" />
    <!-- 既存のHTMLコンテンツ -->
    <div>
      <!-- ここに既存のHTMLを配置 -->
      <p>Welcome to our site!</p>
    </div>
  </div>
</template>

<script>
 import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import { mapState } from 'pinia';
import Overlay from '../Overlay/Overlay.vue';

export default {
  components: {
    Overlay
  },
  computed: {
    ...mapState(useUserStore, ['companyCode']),
    isRestricted() {
      return !this.companyCode;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
