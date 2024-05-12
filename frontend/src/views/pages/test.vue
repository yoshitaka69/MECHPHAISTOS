<template>
  <div v-if="weatherData">
      <h1>{{ weatherData.name }}, {{ weatherData.sys.country }}</h1>
      <img :src="`http://openweathermap.org/img/w/${weatherData.weather[0].icon}.png`" alt="Weather Icon">
      <h2>現在の天気: {{ weatherData.weather[0].main }}</h2>
      <p>温度: {{ weatherData.main.temp }}°C</p>
      <p>湿度: {{ weatherData.main.humidity }}%</p>
      <p>風速: {{ weatherData.wind.speed }} m/s</p>
      <div>
          <h3>週間天気予報:</h3>
          <ul>
              <li v-for="(item, index) in forecastData" :key="index">
                  {{ new Date(item.dt * 1000).toLocaleString() }}: {{ item.weather[0].main }}, 温度: {{ item.main.temp }} °C
              </li>
          </ul>
      </div>
  </div>
  <div v-else>
      <p>天気情報を取得中...</p>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
        weatherData: null,
        forecastData: []  // 週間天気予報データ用
    };
},

  methods: {
    fetchWeather(lat, lon) {
      const apiKey = 'c9c6569d82fac05271fc48f5664ea3b0'; // APIキー
      const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`;
      const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`;

      // 現在の天気データの取得
      axios.get(currentWeatherUrl).then((response) => {
          this.weatherData = response.data;
      }).catch((error) => {
          console.error('現在の天気情報の取得に失敗しました:', error);
      });

      // 週間天気予報データの取得
      axios.get(forecastUrl).then((response) => {
          this.forecastData = response.data.list; // 予報データ
      }).catch((error) => {
          console.error('週間天気予報の取得に失敗しました:', error);
      });
  }
},

  mounted() {
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(
              (position) => {
                  this.fetchWeather(position.coords.latitude, position.coords.longitude);
              },
              () => {
                  alert('位置情報の取得に失敗しました。');
              }
          );
      } else {
          alert('このブラウザは地理位置情報をサポートしていません。');
      }
  }
};
</script>
