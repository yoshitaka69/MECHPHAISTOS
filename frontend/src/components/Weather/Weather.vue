<template>
    <div class="weather-container" v-if="weatherData">
        <div class="location">
            <h1>{{ weatherData.name }}, {{ weatherData.sys.country }}</h1>
            <img :src="`http://openweathermap.org/img/w/${weatherData.weather[0].icon}.png`" alt="Weather Icon">
        </div>
        <div class="weather-details">
            <h2>現在の天気: {{ weatherData.weather[0].main }}</h2>
            <p>温度: {{ weatherData.main.temp }}°C</p>
            <p>湿度: {{ weatherData.main.humidity }}%</p>
            <p>風速: {{ weatherData.wind.speed }} m/s</p>
            <div v-if="wbgtAlert" :class="['heat-alert', wbgtAlertClass]">
                <p>熱中症アラート: {{ wbgtAlertMessage }}</p>
            </div>
        </div>
    </div>
    <div class="weather-container" v-else>
        <p>天気情報を取得中...</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            weatherData: null,
            wbgtAlert: false,
            wbgtAlertMessage: '',
            wbgtAlertClass: '',
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
                    this.checkWbgtAlert();
                })
                .catch((error) => {
                    console.error('天気情報の取得に失敗しました:', error);
                    alert('天気情報の取得に失敗しました。詳細をコンソールで確認してください。');
                });
        },
        checkWbgtAlert() {
            const temp = this.weatherData.main.temp;
            const humidity = this.weatherData.main.humidity;
            // 簡易的なWBGTの計算
            const wbgt = 0.7 * temp + 0.3 * humidity;

            if (wbgt < 25) {
                this.wbgtAlertMessage = '注意';
                this.wbgtAlertClass = 'alert-caution';
            } else if (wbgt < 28) {
                this.wbgtAlertMessage = '警戒';
                this.wbgtAlertClass = 'alert-warning';
            } else if (wbgt < 31) {
                this.wbgtAlertMessage = '厳重警戒';
                this.wbgtAlertClass = 'alert-severe';
            } else {
                this.wbgtAlertMessage = '危険';
                this.wbgtAlertClass = 'alert-danger';
            }
            this.wbgtAlert = true;
        },
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
.weather-container {
    width: 100%;
    max-width: 500px;
    height: auto;
    border: 1px solid #ccc;
    padding: 1rem;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    margin: 20px auto; /* 中央寄せ */
    display: flex;
    align-items: center;
    text-align: left; /* テキスト左寄せ */
    background: linear-gradient(to top, #e0f7fa, #0277bd); /* 青色のグラデーション */
    font-size: 1rem; /* 基本のフォントサイズ */
}
.location {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 1rem;
}
.weather-details {
    display: flex;
    flex-direction: column;
    font-size: 0.8rem; /* フォントサイズをもう一回り小さく */
}
img {
    width: 3rem; /* アイコンのサイズを調整 */
    height: auto;
}
.heat-alert {
    font-weight: bold;
    margin-top: 0.5rem;
}
.alert-caution {
    color: blue;
}
.alert-warning {
    color: orange;
}
.alert-severe {
    color: red;
}
.alert-danger {
    color: darkred;
}
</style>
