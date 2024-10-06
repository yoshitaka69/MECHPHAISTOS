<template>
  <div class="main-calendar">
    <Toast /> <!-- Toast コンポーネントの追加 -->
    <FullCalendar
      class="demo-app-calendar"
      :options="calendarOptions"
      ref="calendar"
    />

    <!-- イベントフォーム (ダイアログ) -->
    <Dialog v-model:visible="showEventDialog" header="Event Form" :closable="false" style="width: 400px">
      <div class="p-fluid">
        <div class="field">
          <label for="title">Event Title</label>
          <InputText id="title" v-model="eventTitle" placeholder="Enter event title" />
          <small v-if="!eventTitle" class="p-error">Event title is required</small>
        </div>
        <div class="field">
          <label for="type">Event Type</label>
          <Dropdown
            id="type"
            v-model="eventType"
            :options="eventTypes"
            optionLabel="label"
            placeholder="Select event type"
          />
        </div>
        <div class="field">
          <label for="start">Start Date & Time</label>
          <Calendar id="start" v-model="eventStartDate" dateFormat="yy-mm-dd" showTime showIcon />
        </div>
        <div class="field">
          <label for="end">End Date & Time</label>
          <Calendar id="end" v-model="eventEndDate" dateFormat="yy-mm-dd" showTime showIcon />
        </div>

        <!-- 横並びのボタン -->
        <div class="button-row">
          <Button label="Save" icon="pi pi-check" class="save-button" @click="saveEvent" />
          <Button label="Cancel" icon="pi pi-times" class="cancel-button" @click="showEventDialog = false" />
        </div>
      </div>
    </Dialog>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import axios from 'axios';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Dropdown from 'primevue/dropdown';
import Button from 'primevue/button';
import Calendar from 'primevue/calendar';
import Toast from 'primevue/toast';  // Toastのインポート
import { useToast } from 'primevue/usetoast';  // Toastを使うためのフックをインポート
import { useUserStore } from '@/stores/userStore';

export default defineComponent({
  components: {
    FullCalendar,
    Dialog,
    InputText,
    Dropdown,
    Button,
    Calendar,
    Toast  // Toastの追加
  },
  setup() {
    const toast = useToast();  // Toastの初期化
    return { toast };
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        initialView: 'dayGridMonth',
        editable: true,
        eventResizableFromStart: true,
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: true,
        events: [],
        select: this.handleDateSelect,
        eventClick: this.handleEventClick // イベントクリックで編集モードに入る
      },
      currentEvents: [],
      showEventDialog: false,
      isEditing: false,
      selectedEvent: null,
      eventTitle: '',
      eventType: null,  // 初期値をnullに設定
      eventStartDate: '',
      eventEndDate: '',
      eventTypes: [
        { label: 'Work Order', value: 'work order' },
        { label: 'Daily Report', value: 'daily report' },
        { label: 'Task', value: 'task' },
        { label: 'Failure Date', value: 'failure date' }
      ]
    };
  },
  mounted() {
    this.fetchEventsFromBackend(); // 初期化時にデータを取得
  },
  methods: {
    // APIからイベントデータを取得
    async fetchEventsFromBackend() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/scheduleForCalendarByCompany/?companyCode=${companyCode}`);
        const scheduleData = response.data.find((company) => company.companyCode === companyCode)?.ScheduleForCalendarList || [];

        const events = scheduleData.map((event) => ({
          id: event.id,
          title: event.title,
          start: event.startDatetime,
          end: event.endDatetime,
          description: event.description,
          backgroundColor: this.getEventColor(event.eventType),
          borderColor: this.getEventColor(event.eventType),
          extendedProps: { type: event.eventType }
        }));

        this.calendarOptions.events = events; // 取得したイベントをカレンダーに設定
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    },
    // カレンダーをクリックした際にフォームを表示する処理
    handleDateSelect(selectInfo) {
      this.isEditing = false;
      this.eventTitle = '';
      this.eventType = null; // 初期値をnullに設定
      this.eventStartDate = selectInfo.startStr;
      this.eventEndDate = selectInfo.endStr || selectInfo.startStr;
      this.showEventDialog = true;
    },
    // イベントをクリックした際に編集フォームを表示
    handleEventClick(clickInfo) {
      this.isEditing = true;
      this.selectedEvent = clickInfo.event;
      this.eventTitle = clickInfo.event.title;
      this.eventType = this.eventTypes.find(et => et.value === clickInfo.event.extendedProps.type) || null;
      this.eventStartDate = clickInfo.event.startStr;
      this.eventEndDate = clickInfo.event.endStr || clickInfo.event.startStr;
      this.showEventDialog = true;
    },
    // イベントを保存する処理 (新規: POST, 編集: PUT)
    async saveEvent() {
      if (!this.eventTitle) {
        this.toast.add({ severity: 'error', summary: 'Error', detail: 'Event title is required.', life: 3000 });
        return; // タイトルが空の場合は送信しない
      }

      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      const eventData = {
        title: this.eventTitle,
        eventType: this.eventType ? this.eventType.value : null,  // 未選択の場合はnullを送信
        startDatetime: this.eventStartDate,
        endDatetime: this.eventEndDate,
        description: '', // 任意の説明フィールド
        companyCode: companyCode
      };

      try {
        if (this.isEditing) {
          await axios.put(`http://127.0.0.1:8000/api/junctionTable/scheduleForCalendar/${this.selectedEvent.id}/`, eventData);
          this.toast.add({ severity: 'success', summary: 'Success', detail: 'Event updated successfully!', life: 3000 });
        } else {
          await axios.post('http://127.0.0.1:8000/api/junctionTable/scheduleForCalendar/', eventData);
          this.toast.add({ severity: 'success', summary: 'Success', detail: 'Event created successfully!', life: 3000 });
        }
        this.fetchEventsFromBackend(); // イベントのリストを再取得してカレンダーを更新
      } catch (error) {
        this.toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to save event.', life: 3000 });
        console.error('Error saving event:', error.response?.data || error.message); // エラーメッセージを表示
      }

      this.showEventDialog = false; // フォームを閉じる
    },
    getEventColor(type) {
      switch (type) {
        case 'work order':
          return 'blue';
        case 'daily report':
          return 'green';
        case 'task':
          return 'orange';
        case 'failure date':
          return 'red';
        default:
          return 'gray';
      }
    }
  }
});
</script>

<style lang="css">
.main-calendar {
  width: 100%;
}
.demo-app-calendar .fc {
  font-size: 14px;
}
.p-fluid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* 横並びのボタン */
.button-row {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

/* Saveボタンの色を強調 */
.save-button {
  background-color: #4caf50;
  color: white;
}

/* Cancelボタンの色を強調 */
.cancel-button {
  background-color: #f44336;
  color: white;
}
</style>
