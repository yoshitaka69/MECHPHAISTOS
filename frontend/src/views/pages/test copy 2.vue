<template>
  <div>
    <ScheduleXCalendar :calendar-app="calendarApp" />
  </div>
</template>

<script setup>
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewDay,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
import axios from 'axios'

// 現在の日付を取得
const today = new Date().toISOString().split('T')[0];

// カレンダーのインスタンスを作成
const calendarApp = createCalendar({
  selectedDate: today,  // デフォルト表示を「本日」に設定
  defaultView: 'monthGrid',  // デフォルト表示を月に設定
  views: [
    createViewMonthGrid(),  // 最初に月表示のビューを設定
    createViewDay(),
    createViewWeek(),
  ],
  events: [],  // 初期状態ではイベントは空
})

// Axiosを使ってイベントを取得する関数
async function fetchEvents() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/events/');
    console.log('取得したイベント:', response.data);

    // 取得したイベントデータをカレンダーに追加
    calendarApp.events = response.data.map(event => ({
      id: event.id,
      title: event.title,
      start: new Date(event.start),  // Dateオブジェクトに変換
      end: new Date(event.end),
      color: event.backgroundColor || 'blue',  // 必要に応じてデフォルト色を設定
    }));
  } catch (error) {
    console.error("イベントの取得に失敗しました:", error);
  }
}

// コンポーネントがマウントされた後にイベントを取得
fetchEvents();
</script>
