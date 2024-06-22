<template>
  <div id="world-clock">
    <div v-for="(city, index) in cities" :key="city.name" class="clock-container">
      <h2 class="city-name">{{ city.name }}</h2>
      <Clock :timezone="city.timezone"></Clock>
    </div>
  </div>
</template>

<script>
import Clock from './Clock.vue';
import moment from 'moment-timezone';

export default {
  components: {
    Clock
  },
  data() {
    return {
      cities: [
        { name: 'New York, USA', timezone: 'America/New_York' },
        { name: 'London, UK', timezone: 'Europe/London' },
        { name: 'Your Location', timezone: 'UTC' }, // ここは後で更新されます
        { name: 'Tokyo, Japan', timezone: 'Asia/Tokyo' },
        { name: 'Sydney, Australia', timezone: 'Australia/Sydney' }
      ]
    };
  },
  mounted() {
    navigator.geolocation.getCurrentPosition(async position => {
      const userTimezone = moment.tz.guess();
      this.cities[2].timezone = userTimezone;

      try {
        const response = await fetch(`https://geocode.xyz/${position.coords.latitude},${position.coords.longitude}?geoit=json`);
        const data = await response.json();
        const country = data.country || 'Your Location';
        this.cities[2].name = country;
      } catch (error) {
        console.error('Error fetching location:', error);
        this.cities[2].name = 'Your Location';
      }
    });
  }
};
</script>

<style scoped>
#world-clock {
  display: flex;
  justify-content: center; /* コンテナを中央揃え */
  align-items: flex-start; /* コンテナを上に揃える */
  flex-wrap: wrap;
  gap: 1px; /* コンテナ間の間隔を調整 */
  padding: 1px; /* 外側の余白を追加 */
}

.clock-container {
  text-align: center;
  flex: 1 0 200px; /* 各コンテナの最小幅を設定 */
  max-width: 180px; /* 最大幅を設定 */
  box-sizing: border-box; /* ボックスサイズを含む */
  position: relative; /* 相対位置を設定 */
  padding-top: 5px; /* 上部の余白を設定 */
  margin: 0; /* マージンをリセット */
}

.city-name {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%; /* 横幅をコンテナ全体に設定 */
  margin: 0;
  font-size: 1.0em;
  font-weight: bold;
  text-align: center; /* テキストを中央揃え */
}

.clock-container h2 {
  margin-bottom: 10px;
  font-size: 1.2em;
  font-weight: bold;
}
</style>
