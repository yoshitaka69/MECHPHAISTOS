<template>
  <div class="gantt-chart">
    <!-- sub gantt-chart領域 -->
    <div class="new-task-bars-column" ref="newTaskBars">
      <div class="new-task-bar-container">
        <div class="custom-grid-lines">
          <div v-for="date in dates" :key="date" class="sub-task-bar-grid-line"></div>
        </div>
      </div>
    </div>

    <!-- スペースを追加 -->
    <div class="spacer"></div>

    <!-- main gantt-chart領域 -->
    <div class="header">
      <div class="task-header-column">
        <div class="task-header">タスク名</div>
        <div class="task-header">内容</div>
        <div class="task-header">担当</div>
        <div class="task-header">進捗</div>
      </div>
      <div class="date-header-column" ref="dateHeader">
        <div class="year-month-row">
          <div class="year-month-item" v-for="(month, index) in groupedDates" :key="index" :style="{ gridColumnEnd: `span ${month.days.length}` }">
            {{ month.year }}年 {{ month.month }}月
          </div>
        </div>
        <div class="day-row">
          <div 
            class="header-item" 
            v-for="date in dates" 
            :key="date" 
            :class="{'saturday': isSaturday(date), 'sunday': isSunday(date)}"
          >
            <span>{{ formatDay(date) }}<br>{{ formatWeekday(date) }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="rows">
      <div class="task-names-column">
        <div class="task-name" v-for="task in tasks" :key="task.id">
          <div class="task-field"><input v-model="task.name" /></div>
          <div class="task-field"><input v-model="task.content" /></div>
          <div class="task-field"><input v-model="task.assignee" /></div>
          <div class="task-field"><input v-model="task.progress" /></div>
        </div>
      </div>
      <div class="task-bars-column" ref="taskBars" @scroll="syncScroll">
        <div class="custom-grid-lines">
          <div v-for="date in dates" :key="date" class="sub-task-bar-grid-line"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dates: this.generateDates(new Date(2024, 3, 1), 90), // Start from April 1, 2024 for 3 months
      tasks: [
        { id: 1, name: "Task 1", content: "Content 1", assignee: "User 1", progress: "0%", start: new Date(2024, 3, 1), end: new Date(2024, 3, 10) },
        { id: 2, name: "Task 2", content: "Content 2", assignee: "User 2", progress: "50%", start: new Date(2024, 3, 5), end: new Date(2024, 3, 15) },
        { id: 3, name: "Task 3", content: "Content 3", assignee: "User 3", progress: "100%", start: new Date(2024, 3, 12), end: new Date(2024, 3, 20) },
      ],
    };
  },
  computed: {
    groupedDates() {
      const grouped = [];
      let currentMonth = null;

      this.dates.forEach(date => {
        const [year, month] = date.split('-').slice(0, 2);
        if (!currentMonth || currentMonth.year !== year || currentMonth.month !== month) {
          currentMonth = { year, month, days: [] };
          grouped.push(currentMonth);
        }
        currentMonth.days.push(date);
      });

      return grouped;
    }
  },
  methods: {
    generateDates(startDate, days) {
      let dates = [];
      for (let i = 0; i < days; i++) {
        let date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        dates.push(date);
      }
      return dates.map(date => this.formatDate(date));
    },
    formatDay(date) {
      const day = new Date(date).getDate();
      return day;
    },
    formatWeekday(date) {
      const weekdays = ['日', '月', '火', '水', '木', '金', '土'];
      const day = new Date(date).getDay();
      return weekdays[day];
    },
    isSaturday(date) {
      return new Date(date).getDay() === 6;
    },
    isSunday(date) {
      return new Date(date).getDay() === 0;
    },
    formatDate(date) {
      return date.toISOString().split('T')[0];
    },
    syncScroll() {
      const dateHeader = this.$refs.dateHeader;
      const taskBars = this.$refs.taskBars;
      const newTaskBars = this.$refs.newTaskBars;
      dateHeader.scrollLeft = taskBars.scrollLeft;
      newTaskBars.scrollLeft = taskBars.scrollLeft;
    }
  },
};
</script>

<style scoped>
.gantt-chart {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.new-task-bars-column {
  display: grid;
  grid-template-rows: repeat(3, 40px); /* 高さを40pxに変更 */
  width: 1536px; /* カレンダー領域と横幅を一致させる */
  overflow-x: auto;
  overflow-y: hidden;
  position: relative;
  flex-grow: 1;
  background-color: #ffffff; /* 背景を白色に変更 */
  margin-bottom: 20px; /* 既存のガントチャートとの間にスペースを追加 */
  left: 540px; /* date-header-columnの幅に合わせて調整 */
  height: 50px; /* 自動高さ */
}

.new-task-bar-container {
  position: relative;
  display: grid;
  grid-template-columns: repeat(90, minmax(60px, 1fr)); /* 90日分を表示 */
  height: 100%; /* 親要素の高さに合わせる */
}

.custom-grid-lines {
  position: relative;
  display: grid;
  grid-template-columns: repeat(90, minmax(60px, 1fr)); /* 90日分を表示 */
}

.sub-task-bar-grid-line {
  border-left: 1px solid #ddd; /* 縦線のグリッド線を追加 */
  border-bottom: 1px solid #ddd; /* 横線のグリッド線を追加 */
  height: 40px; /* グリッドラインの高さを40pxに設定 */
}

.spacer {
  height: 20px; /* 新しいガントバー領域と既存のガントチャートの間にスペースを追加 */
}

.header {
  display: flex;
  flex-shrink: 0;
}

.task-header-column {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  width: 600px; /* 横幅を固定 */
  border-right: 1px solid #ddd;
  background-color: #28a745;
}

.task-header {
  text-align: center;
  padding: 10px;
  font-weight: bold;
  background-color: #28a745;
  color: white;
  border-right: 1px solid #ddd;
}

.date-header-column {
  display: grid;
  grid-template-rows: auto auto;
  width: 1536px; /* 横幅を固定 */
  overflow-x: hidden; /* スクロールバーを非表示にする */
}

.year-month-row {
  display: grid;
  grid-template-columns: repeat(90, minmax(60px, 1fr)); /* 90日分を表示 */
  border-bottom: 1px solid #ddd;
  background-color: #007bff; /* 背景を青色に変更 */
  color: black; /* 文字を黒色に変更 */
  text-align: center;
}

.year-month-item {
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #ddd;
}

.day-row {
  display: grid;
  grid-template-columns: repeat(90, minmax(60px, 1fr)); /* 90日分を表示 */
  background-color: #ffffff; /* 背景を白色に変更 */
}

.header-item {
  text-align: center;
  border-right: 1px solid #ddd;
  padding: 5px;
  color: black; /* 日付の文字を黒字に変更 */
}

.saturday {
  background-color: #e0f7fa; /* 薄い青色 */
}

.sunday {
  background-color: #ffebee; /* 薄い赤色 */
}

.rows {
  display: flex;
  flex-grow: 1;
  overflow-x: hidden;
}

.task-names-column {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 40px; /* 各タスクの高さを一致させる */
  width: 600px; /* 横幅を固定 */
  border-right: 1px solid #ddd;
  overflow-y: auto; /* タスク領域の縦スクロールを有効にする */
  background-color: #ffffff; /* 背景を白色に変更 */
  border-bottom: 1px solid #ddd; /* 横のグリッド線を追加 */
}

.task-name {
  display: contents; /* 各タスクを同じ高さにするために使用 */
}

.task-field {
  display: flex;
  align-items: center;
  padding: 10px;
  background: #ffffff; /* 背景を白色に変更 */
  border-bottom: 1px solid #ddd;
  border-right: 1px solid #ddd;
  width: 100%;
  border: 1px solid #ffffff; /* 枠を白色に変更 */
  outline: none;
}

.task-name > input {
  width: 100%;
  border: none;
  outline: none;
  background: transparent;
}

.task-bars-column {
  display: grid;
  grid-template-rows: repeat(auto-fill, 40px);
  width: 1536px; /* 横幅を固定 */
  overflow-x: auto;
  overflow-y: hidden;
  position: relative;
  flex-grow: 1;
  background-color: #ffffff; /* 背景を白色に変更 */
}

.grid-line {
  border-left: 1px solid #ddd; /* 縦線のグリッド線を追加 */
  border-bottom: 1px solid #ddd; /* 横線のグリッド線を追加 */
}

.saturday {
  background-color: #e0f7fa; /* 薄い青色 */
}

.sunday {
  background-color: #ffebee; /* 薄い赤色 */
}
</style>
