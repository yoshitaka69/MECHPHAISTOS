<template>
  <div class="gantt-chart">
    <!-- main gantt-chart領域 -->
    <div class="header">
      <div class="task-header-column" ref="taskHeaderColumn">
        <div class="task-header">タスク名</div>
        <div class="task-header">内容</div>
        <div class="task-header">担当</div>
        <div class="task-header">進捗</div>
        <div class="task-header">開始日</div>
        <div class="task-header">完了日</div>
      </div>
      <div class="date-header-column" ref="dateHeader">
        <div class="year-month-row" ref="yearMonthRow">
          <div
            class="year-month-item"
            v-for="(month, index) in groupedDates"
            :key="index"
            :style="{ gridColumnEnd: `span ${month.days.length}` }"
          >
            {{ month.year }}年 {{ month.month }}月
          </div>
        </div>
        <div class="day-row" ref="dayRow">
          <div
            class="header-item"
            v-for="date in dates"
            :key="date"
            :class="{ 'saturday-bg': isSaturday(date), 'sunday-bg': isSunday(date), 'weekday-bg': !isSaturday(date) && !isSunday(date) }"
          >
            <span>{{ formatDay(date) }}<br />{{ formatWeekday(date) }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="rows">
      <div class="task-names-column" ref="taskNamesColumn">
        <div class="task-name" v-for="task in tasks" :key="task.id">
          <div class="task-field">
            <input v-model="task.name" class="task-input" />
          </div>
          <div class="task-field">
            <input v-model="task.content" class="task-input" />
          </div>
          <div class="task-field">
            <input v-model="task.assignee" class="task-input" />
          </div>
          <div class="task-field">
            <input v-model="task.progress" class="task-input" />
          </div>
          <div class="task-field date-field">
            <input type="date" v-model="task.start" class="task-input" @change="updateTaskBar(task)" />
          </div>
          <div class="task-field date-field">
            <input type="date" v-model="task.end" class="task-input" @change="updateTaskBar(task)" />
          </div>
        </div>
      </div>
      <div class="task-bars-column" ref="taskBarsColumn" @scroll="syncScroll">
        <div class="task-bar-grid">
          <div
            class="task-bar-item"
            v-for="task in tasks"
            :key="task.id"
          >
            <div
              v-for="date in dates"
              :key="date"
              :class="{ 'saturday-bg': isSaturday(date), 'sunday-bg': isSunday(date), 'weekday-bg': !isSaturday(date) && !isSunday(date) }"
              class="task-bar-date"
            ></div>
          </div>
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
        { id: 1, name: 'Task 1', content: 'Content 1', assignee: 'User 1', progress: '0%', start: '2024-04-01', end: '2024-04-10' },
        { id: 2, name: 'Task 2', content: 'Content 2', assignee: 'User 2', progress: '50%', start: '2024-04-05', end: '2024-04-15' },
        { id: 3, name: 'Task 3', content: 'Content 3', assignee: 'User 3', progress: '100%', start: '2024-04-12', end: '2024-04-20' }
      ],
      gridItemWidth: 30 // グリッド項目の幅を設定
    };
  },
  computed: {
    groupedDates() {
      const grouped = [];
      let currentMonth = null;

      this.dates.forEach((date) => {
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
  mounted() {
    this.$nextTick(() => {
      this.updateTaskFieldWidth();
      this.updateHeaderHeight();
      this.updateGridHeight();
      window.addEventListener('resize', this.updateTaskFieldWidth);
      window.addEventListener('resize', this.updateHeaderHeight);
      window.addEventListener('resize', this.updateGridHeight);
      this.updateLayout();
    });
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateTaskFieldWidth);
    window.removeEventListener('resize', this.updateHeaderHeight);
    window.removeEventListener('resize', this.updateGridHeight);
  },
  methods: {
    generateDates(startDate, days) {
      let dates = [];
      for (let i = 0; i < days; i++) {
        let date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        dates.push(this.formatDate(date));
      }
      return dates;
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
    updateTaskFieldWidth() {
      const taskHeaders = this.$refs.taskHeaderColumn.querySelectorAll('.task-header');
      const taskFields = this.$refs.taskNamesColumn.querySelectorAll('.task-field');

      taskHeaders.forEach((header, index) => {
        const headerWidth = header.clientWidth;
        taskFields.forEach((field) => {
          field.style.width = `${headerWidth}px`;
        });
      });
    },
    updateHeaderHeight() {
      const yearMonthRowHeight = this.$refs.yearMonthRow.clientHeight;
      const dayRowHeight = this.$refs.dayRow.clientHeight;
      const totalHeight = yearMonthRowHeight + dayRowHeight;

      this.$refs.taskHeaderColumn.style.height = `${totalHeight}px`;
      this.$refs.dateHeader.style.height = `${totalHeight}px`;
    },
    updateGridHeight() {
      const taskFields = this.$refs.taskNamesColumn.querySelectorAll('.task-field');
      const taskFieldHeight = taskFields[0].clientHeight;
      const gridHeight = taskFieldHeight * this.tasks.length;

      this.$refs.taskBarsColumn.querySelector('.task-bar-grid').style.gridTemplateRows = `repeat(${this.tasks.length}, ${taskFieldHeight}px)`;
    },
    updateLayout() {
      const taskHeaderColumn = this.$refs.taskHeaderColumn;
      const taskNamesColumn = this.$refs.taskNamesColumn;
      const dateHeader = this.$refs.dateHeader;

      const taskHeaderColumnWidth = taskHeaderColumn.offsetWidth;

      taskNamesColumn.style.width = `${taskHeaderColumnWidth}px`;
      dateHeader.style.marginLeft = `${taskHeaderColumnWidth}px`;
      this.$refs.taskBarsColumn.style.marginLeft = `${taskHeaderColumnWidth}px`; // 左端を合わせる

      // task-header-columnを最前面に
      taskHeaderColumn.style.zIndex = 2;
      dateHeader.style.zIndex = 1;
      taskNamesColumn.style.zIndex = 1;

      // task-names-columnとtask-bars-columnを<div class="rows">の上部に揃える
      const rowsTop = this.$refs.rows.getBoundingClientRect().top;
      taskNamesColumn.style.top = `${rowsTop}px`;
      this.$refs.taskBarsColumn.style.top = `${rowsTop}px`;
    },
    syncScroll() {
      const dateHeader = this.$refs.dateHeader;
      const taskBarsColumn = this.$refs.taskBarsColumn;
      dateHeader.scrollLeft = taskBarsColumn.scrollLeft;
    },
  }
};
</script>

<style scoped>
.gantt-chart {
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 20px;
}

.header {
  display: flex;
  position: relative;
}

.task-header-column {
  display: grid;
  grid-template-columns: 100px 100px 100px 100px 150px 150px; /* 各カラムの幅を指定 */
  border-right: 1px solid #ddd;
  background-color: #28a745;
  position: absolute; /* 他の要素と重ねる */
  z-index: 2; /* 最前面に配置 */
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
  overflow-x: hidden;
  margin-left: 0; /* 左端に合わせる */
  z-index: 1; /* 後ろに配置 */
}

.year-month-row,
.day-row {
  display: grid;
  grid-template-columns: repeat(90, 30px);
  background-color: #ffffff;
  text-align: center;
}

.year-month-row {
  border-bottom: 1px solid #ddd;
  background-color: #007bff;
  color: black;
}

.year-month-item,
.header-item {
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #ddd;
}

.header-item {
  text-align: center;
  padding: 5px;
  color: black;
}

.weekday-bg {
  background-color: #ffffff;
}

.saturday-bg {
  background-color: #e0f7fa;
}

.sunday-bg {
  background-color: #ffebee;
}

.rows {
  display: flex;
  flex-grow: 1;
  overflow-x: hidden;
}

.task-names-column {
  display: grid;
  grid-template-columns: 100px 100px 100px 100px 150px 150px; /* 各カラムの幅を指定 */
  grid-auto-rows: 40px;
  border-right: 1px solid #ddd;
  overflow-y: auto;
  background-color: #ffffff;
  border-bottom: 1px solid #ddd;
  height: 100%;
  position: absolute; /* 他の要素と重ねる */
  z-index: 1; /* 後ろに配置 */
  width: 100%;
}

.task-names-column::after {
  content: '';
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
  background: repeating-linear-gradient(to bottom, transparent, transparent 39px, black 40px);
  pointer-events: none;
}

.task-name {
  display: contents;
}

.task-field {
  display: flex;
  align-items: center;
  padding: 10px;
  background: #ffffff;
  border-bottom: 1px solid lightgray;
  border-left: 1px solid lightgray;
  width: 100%;
  outline: none;
}

.task-input {
  width: 100%;
  border: 1px solid white;
  outline: none;
  background: transparent;
  box-sizing: border-box;
}

.date-field .task-input {
  width: calc(100% - 20px); /* 日付フィールドの幅を広げる */
}

.task-bars-column {
  display: grid;
  width: calc(100% - (100px * 4 + 150px * 2 + 2px)); /* 残りの幅を使用 */
  overflow-x: auto;
  overflow-y: hidden;
  top: 0; /* rowsの上部に合わせる */
  background-color: #ffffff;
  height: 100%;
  left: 0; /* task-header-columnと合わせる */
}

.task-bar-grid {
  display: grid;
  grid-template-columns: repeat(90, 30px); /* datesの幅に合わせる */
}

.task-bar-item {
  border-left: 1px solid lightgray;
  border-bottom: 1px solid lightgray;
}
</style>
