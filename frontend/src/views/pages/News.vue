<template>
  <div class="home-contents">
    <div class="header">
      <img src="@/assets/MECHPHAISTOS cover.jpg" />
      <h1 class="title">Welcome to MECHPHASTOS</h1>
    </div>
    <div class="content-container">
      <div class="side-container left-side">
        <MiniCalendar :events="events" @update-events="updateEvents" />
      </div>
      <div class="main-content">
        <div class="section world-clock-section">
          <WorldClock />
        </div>
        <div class="section weather-info-container">
          <Weather />
          <InformationBox message="これは管理人からのお知らせです。" />
        </div>
        <div class="section">
          <News_content />
        </div>
        <div class="section calendar-section">
          <MainCalendar :events="events" @update-events="updateEvents" />
        </div>
      </div>
      <div class="side-container right-side"></div>
    </div>
  </div>
</template>

<script>
import News_content from '@/components/News/News_content.vue';
import WorldClock from '@/components/Clock/WorldClock.vue';
import Weather from '@/components/Weather/Weather.vue';
import InformationBox from '@/components/Information_box/Information_box.vue';
import MainCalendar from '@/components/Calendar/MainCalendar.vue';
import MiniCalendar from '@/components/Calendar/MiniCalendar.vue';
import { INITIAL_EVENTS } from '@/components/Calendar/event-utils';

export default {
  components: {
    News_content,
    WorldClock,
    Weather,
    InformationBox,
    MainCalendar,
    MiniCalendar,
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
  width: 240px; /* サイドコンテナの幅を狭める */
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
  max-width: 1000px; /* 各セクションの最大幅を広げる */
}

.weather-info-container {
  display: flex;
  justify-content: space-between; /* 子要素を横並びに */
  gap: 20px; /* 子要素間のスペース */
}

.weather-info-container > * {
  flex: 1; /* 子要素が均等に幅を取る */
}

/* world-clock-section と weather-info-container の間隔を狭める */
.world-clock-section {
  margin-bottom: 1px; /* デフォルトの間隔より狭く設定 */
}
</style>
