<script>
import { defineComponent } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

export default defineComponent({
  components: {
    FullCalendar,
  },
  props: {
    events: Array,
  },
  data() {
    return {
      calendarOptions1: {
        plugins: [
          dayGridPlugin,
          interactionPlugin // needed for dateClick
        ],
        headerToolbar: {
          left: '',
          center: 'title',
          right: 'prev,next'
        },
        initialView: 'dayGridMonth',
        initialDate: new Date(), // 今月を表示
        initialEvents: this.events,
        editable: false,
        selectable: false,
        dayMaxEvents: true,
        eventsSet: this.handleEvents
      },
      calendarOptions2: {
        plugins: [
          dayGridPlugin,
          interactionPlugin // needed for dateClick
        ],
        headerToolbar: {
          left: '',
          center: 'title',
          right: 'prev,next'
        },
        initialView: 'dayGridMonth',
        initialDate: new Date(new Date().setMonth(new Date().getMonth() + 1)), // 次の月を表示
        initialEvents: this.events,
        editable: false,
        selectable: false,
        dayMaxEvents: true,
        eventsSet: this.handleEvents
      },
      currentEvents: this.events,
    }
  },
  watch: {
    events: {
      handler(newEvents) {
        this.calendarOptions1.initialEvents = newEvents;
        this.calendarOptions2.initialEvents = newEvents;
        this.currentEvents = newEvents;
      },
      deep: true
    }
  },
  methods: {
    handleEvents(events) {
      this.currentEvents = events
      this.$emit('update-events', events)
    },
  }
})
</script>

<template>
  <div class='mini-calendar'>
    <FullCalendar
      class='mini-app-calendar'
      :options='calendarOptions1'
    />
    <FullCalendar
      class='mini-app-calendar'
      :options='calendarOptions2'
    />
  </div>
</template>

<style lang='css'>
.mini-calendar {
  max-width: 240px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.mini-app-calendar .fc {
  font-size: 12px;
}
</style>
