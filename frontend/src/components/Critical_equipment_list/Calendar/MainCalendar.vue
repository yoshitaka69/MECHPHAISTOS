<script>
import { defineComponent } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { createEventId } from '@/components/Calendar/event-utils'

export default defineComponent({
  components: {
    FullCalendar,
  },
  props: {
    events: Array,
  },
  data() {
    return {
      calendarOptions: {
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin // needed for dateClick
        ],
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        initialView: 'dayGridMonth',
        initialEvents: this.events,
        editable: true,
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: true,
        select: this.handleDateSelect,
        eventClick: this.handleEventClick,
        eventsSet: this.handleEvents
      },
      currentEvents: this.events,
    }
  },
  watch: {
    events: {
      handler(newEvents) {
        this.calendarOptions.initialEvents = newEvents;
        this.currentEvents = newEvents;
      },
      deep: true
    }
  },
  methods: {
    handleDateSelect(selectInfo) {
      let title = prompt('Please enter a new title for your event')
      let calendarApi = selectInfo.view.calendar

      calendarApi.unselect() // clear date selection

      if (title) {
        calendarApi.addEvent({
          id: createEventId(),
          title,
          start: selectInfo.startStr,
          end: selectInfo.endStr,
          allDay: selectInfo.allDay
        })
        this.$emit('update-events', calendarApi.getEvents())
      }
    },
    handleEventClick(clickInfo) {
      if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
        clickInfo.event.remove()
        this.$emit('update-events', clickInfo.view.calendar.getEvents())
      }
    },
    handleEvents(events) {
      this.currentEvents = events
      this.$emit('update-events', events)
    },
  }
})
</script>

<template>
  <div class='main-calendar'>
    <FullCalendar
      class='demo-app-calendar'
      :options='calendarOptions'
    >
      <template v-slot:eventContent='arg'>
        <b>{{ arg.timeText }}</b>
        <i>{{ arg.event.title }}</i>
      </template>
    </FullCalendar>
  </div>
</template>

<style lang='css'>
.main-calendar {
  width: 100%;
}
.demo-app-calendar .fc {
  font-size: 14px;
}
</style>
