<template>
    <div id="world-clock">
      <div v-for="(city, index) in cities" :key="city.name" class="clock-container">
        <h2>{{ city.name }}</h2>
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
    justify-content: space-between; /* ここを変更 */
    align-items: center;
    flex-wrap: wrap;
  }
  
  .clock-container {
    text-align: center;
    margin: 1px; /* ここを調整 */
  }
  
  .clock-container h2 {
    margin-bottom: 10px;
    font-size: 1.2em;
    font-weight: bold;
  }
  </style>
  