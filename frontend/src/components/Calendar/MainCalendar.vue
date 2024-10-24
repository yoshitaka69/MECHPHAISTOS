<template>
  <div class="simple-calendar">
    <FullCalendar
      :options="calendarOptions"
      ref="calendar"
    />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';

export default defineComponent({
  components: {
    FullCalendar
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
        initialView: 'dayGridMonth', // 初期ビューを月表示に設定
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek' // 月と週のビュー切り替えボタン
        },
        editable: true,  // イベントの編集を許可（ドラッグ＆ドロップ、リサイズなど）
        eventResizableFromStart: true,  // イベントの開始日からもリサイズを許可
        events: [
          {
            id: '1',
            title: 'Sample Event',
            start: '2024-10-23',
            end: '2024-10-25',
            backgroundColor: 'blue',
            borderColor: 'blue'
          },
          {
            id: '2',
            title: 'Another Event',
            start: '2024-10-26',
            backgroundColor: 'green',
            borderColor: 'green'
          }
        ],
        eventDrop: this.handleEventDrop, // ドラッグ＆ドロップ時の処理
        eventResize: this.handleEventResize // リサイズ時の処理
      }
    };
  },
  methods: {
    handleEventDrop(info) {
      // ドラッグ＆ドロップ時のイベントデータ
      console.log('Event dropped to: ', info.event.start);
    },
    handleEventResize(info) {
      // リサイズ時のイベントデータ
      console.log('Event resized to: ', info.event.end);
    }
  }
});
</script>

<style>
.simple-calendar {
  width: 100%;
  background-color: white;
}
</style>
