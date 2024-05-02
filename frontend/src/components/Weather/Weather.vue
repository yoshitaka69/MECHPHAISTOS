<template>
    <div v-if="weatherData">
        <h1>{{ weatherData.name }}, {{ weatherData.sys.country }}</h1>
        <img :src="`http://openweathermap.org/img/w/${weatherData.weather[0].icon}.png`" alt="Weather Icon">
        <h2>現在の天気: {{ weatherData.weather[0].main }}</h2>
        <p>温度: {{ weatherData.main.temp }}°C</p>
        <p>湿度: {{ weatherData.main.humidity }}%</p>
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
            weatherData: null
        };
    },
    methods: {
    fetchWeather(lat, lon) {
        const apiKey = 'c9c6569d82fac05271fc48f5664ea3b0'; // ここにあなたのAPIキーを入力してください
        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`;
        axios
            .get(url)
            .then((response) => {
                console.log('APIからのレスポンスデータ:', response.data);
                this.weatherData = response.data;
            })
            .catch((error) => {
                console.error('天気情報の取得に失敗しました:', error);
                alert('天気情報の取得に失敗しました。詳細をコンソールで確認してください。');
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

<style>
/* スタイルには、画像のサイズ調整など、必要に応じて追加してください */
img {
    width: 100px; /* アイコンのサイズを調整 */
    height: auto;
}
</style>
