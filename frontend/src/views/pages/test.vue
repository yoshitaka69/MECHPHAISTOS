<template>
  <div id="calendar"></div>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue'
import { Calendar } from '@fullcalendar/core'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'  // ドラッグ＆ドロップ用のプラグイン

onMounted(() => {
  const calendarEl = document.getElementById('calendar')

  if (calendarEl) {
    const calendar = new Calendar(calendarEl, {
      plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],  // interactionPlugin を追加
      timeZone: 'UTC',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay',
      },
      editable: true,  // イベントの編集（ドラッグやリサイズ）を有効化
      droppable: true,  // ドラッグ＆ドロップを許可
      events: 'https://fullcalendar.io/api/demo-feeds/events.json?overload-day',
    })

    calendar.render()
  }
})
</script>
