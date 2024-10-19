<template>
  <div class="background-container">
    <div class="home-contents">
      <div class="header">
        <img src="@/assets/MECHPHAISTOS cover.jpg" />
        <h1 class="title">Welcome to MECHPHAISTOS</h1>
      </div>
      <div class="content-container">
        <div class="side-container left-side">
          <MiniCalendar :events="events" @update-events="updateEvents" />
        </div>
        <div class="main-content">
          <div class="section world-clock-section">
            <WorldClock />
          </div>
          <div class="section mechphaistos-ai-section">
            <Mechphaistos />
          </div>
          <div class="section news-and-weather">
            <News_content class="news-content" />
            <Weather class="weather-content" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import News_content from '@/components/News/News_content.vue';
import WorldClock from '@/components/Clock/WorldClock.vue';
import Weather from '@/components/Weather/Weather.vue';
import MainCalendar from '@/components/Calendar/MainCalendar.vue';
import MiniCalendar from '@/components/Calendar/MiniCalendar.vue';
import { INITIAL_EVENTS } from '@/components/Calendar/event-utils';
import Mechphaistos from '@/components/Mechphaistos_Ai/Mechphaistos.vue';

export default {
  components: {
    News_content,
    WorldClock,
    Weather,
    MainCalendar,
    MiniCalendar,
    Mechphaistos,
  },
  data() {
    return {
      events: INITIAL_EVENTS,
    };
  },
  methods: {
    updateEvents(events) {
      this.events = events;
    },
  },
};
</script>

<style scoped>
.background-container {
  background-color: #f5f5f5; /* 背景色を追加 */
  padding: 20px; /* コンテナ全体に余白を追加 */
  border-radius: 10px; /* コンテナの角を丸める */
  max-width: 1600px; /* 背景コンテナの最大幅を拡大 */
  margin: 0 auto; /* コンテナを中央揃えに */
}

.home-contents {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px; /* セクション間のデフォルトスペース */
}

.header {
  position: relative;
  width: 100%;
}

.header img {
  object-fit: cover;
  width: 100%;
  height: 130px;
}

/* 背景画像を暗くしても welcome to… を目立たせる */
.header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
}

.title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 0;
  margin: 0;
  font-size: 30px;
  color: #fff;
}

.content-container {
  display: flex;
  width: 100%;
}

.side-container {
  width: 240px; /* サイドコンテナの幅 */
  background-color: #f0f0f0; /* サイドコンテナの背景色 */
  height: 100vh; /* 縦に伸ばす */
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px; /* セクション間のデフォルトスペース */
  flex: 1; /* メインコンテンツが余ったスペースを取る */
  margin: 0 5px; /* 両側のマージンを狭める */
}

.section {
  width: 100%;
  max-width: 1200px; /* 各セクションの最大幅を調整 */
}

.mechphaistos-ai-section {
  width: 100%;
  max-width: 1200px;
  margin-bottom: 20px;
}

.news-and-weather {
  display: flex;
  gap: 20px; /* News_content と Weather の間のスペース */
  align-items: flex-start; /* 上端を揃える */
  width: 100%; /* 背景コンテナに合わせる */
}

.news-content {
  flex: 2; /* News_content を Weather より大きくする */
}

.weather-content {
  flex: 1; /* Weather の幅を調整 */
}
</style>
