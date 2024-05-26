<template>
  <div class="gantt-chart">
    <!-- sub gantt-chart領域 -->
    <div class="new-task-bars-column">
      <div class="new-task-bar-container">
        <div class="sub-custom-grid-lines">
          <div v-for="date in dates" :key="date" class="sub-task-bar-grid-line"></div>
        </div>
      </div>
    </div>

    <!-- スペースを追加 -->
    <div class="spacer"></div>

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
        <div class="year-month-row">
          <div
            class="year-month-item"
            v-for="(month, index) in groupedDates"
            :key="index"
            :style="{ gridColumnEnd: `span ${month.days.length}` }"
          >
            {{ month.year }}年 {{ month.month }}月
          </div>
        </div>
        <div class="day-row">
          <div
            class="header-item"
            v-for="date in dates"
            :key="date"
            :class="{ saturday: isSaturday(date), sunday: isSunday(date), weekday: !isSaturday(date) && !isSunday(date) }"
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
      <div class="task-bars-column" ref="taskBars" @scroll="syncScroll">
        <div class="custom-grid-lines" ref="customGridLines">
          <div
            v-for="task in tasks"
            :key="task.id"
            class="task-bar"
            :style="getTaskBarStyle(task)"
            @mousedown="startDrag(task, $event)"
          >
            <div class="resize-handle left" @mousedown.stop="startResize(task, $event, 'start')"></div>
            {{ task.name }}
            <div class="resize-handle right" @mousedown.stop="startResize(task, $event, 'end')"></div>
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
      gridItemWidth: 30, // グリッド項目の幅を設定
      draggingTask: null, // ドラッグ中のタスクを保持
      initialMouseX: 0, // マウスの初期X座標
      initialTaskStart: null, // タスクの初期開始日
      resizingTask: null, // リサイズ中のタスクを保持
      resizeSide: null, // リサイズ側 (startまたはend)
      initialTaskEnd: null // タスクの初期終了日
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
      this.updateGridLines();
      this.updateTaskFieldWidth();
      window.addEventListener('resize', this.updateGridLines);
      window.addEventListener('resize', this.updateTaskFieldWidth);
      window.addEventListener('mousemove', this.onMouseMove);
      window.addEventListener('mouseup', this.onMouseUp);
      this.updateLayout();
    });
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.updateGridLines);
    window.removeEventListener('resize', this.updateTaskFieldWidth);
    window.removeEventListener('mousemove', this.onMouseMove);
    window.removeEventListener('mouseup', this.onMouseUp);
  },
  methods: {
    generateDates(startDate, days) {
      let dates = [];
      for (let i = 0; i < days; i++) {
        let date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        dates.push(date);
      }
      return dates.map((date) => this.formatDate(date));
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
      dateHeader.scrollLeft = taskBars.scrollLeft;
    },
    getGridTemplateColumns() {
      const columnsCount = this.dates.length;
      return `repeat(${columnsCount}, ${this.gridItemWidth}px)`;
    },
    updateGridLines() {
      const taskBarsElement = this.$refs.taskBars;
      const customGridLines = this.$refs.customGridLines;
      const numberOfDays = this.dates.length;
      const gridWidth = numberOfDays * this.gridItemWidth;

      customGridLines.style.width = `${gridWidth}px`;
      customGridLines.style.gridTemplateColumns = this.getGridTemplateColumns();
      customGridLines.style.gridTemplateRows = `repeat(${this.tasks.length}, 40px)`;
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
    updateLayout() {
      const taskHeaderColumn = this.$refs.taskHeaderColumn;
      const taskNamesColumn = this.$refs.taskNamesColumn;
      const dateHeader = this.$refs.dateHeader;
      const taskBars = this.$refs.taskBars;

      const taskHeaderColumnWidth = taskHeaderColumn.offsetWidth;
      const taskHeaderColumnHeight = taskHeaderColumn.offsetHeight;

      taskNamesColumn.style.width = `${taskHeaderColumnWidth}px`;
      dateHeader.style.marginLeft = `${taskHeaderColumnWidth}px`;
      taskBars.style.marginLeft = `${taskHeaderColumnWidth}px`;

      dateHeader.style.height = `${taskHeaderColumnHeight}px`;
    },
    getTaskBarStyle(task) {
      const start = new Date(task.start);
      const end = new Date(task.end);
      const startDate = new Date(this.dates[0]);
      const endDate = new Date(this.dates[this.dates.length - 1]);

      if (start < startDate) start = startDate;
      if (end > endDate) end = endDate;

      const startIndex = (start - startDate) / (1000 * 60 * 60 * 24);
      const endIndex = (end - startDate) / (1000 * 60 * 60 * 24);

      const taskIndex = this.tasks.findIndex(t => t.id === task.id) + 1;

      return {
        gridColumnStart: startIndex + 1,
        gridColumnEnd: endIndex + 2,
        gridRowStart: taskIndex,
        gridRowEnd: taskIndex + 1
      };
    },
    startDrag(task, event) {
      this.draggingTask = task;
      this.initialMouseX = event.clientX;
      this.initialTaskStart = new Date(task.start);
    },
    startResize(task, event, side) {
      this.resizingTask = task;
      this.resizeSide = side;
      this.initialMouseX = event.clientX;
      this.initialTaskStart = new Date(task.start);
      this.initialTaskEnd = new Date(task.end);
    },
    onMouseMove(event) {
      if (this.draggingTask) {
        const dx = event.clientX - this.initialMouseX;
        const daysMoved = Math.round(dx / this.gridItemWidth);
        const newStart = new Date(this.initialTaskStart);
        newStart.setDate(newStart.getDate() + daysMoved);

        const newEnd = new Date(newStart);
        const taskDuration = (new Date(this.draggingTask.end) - new Date(this.draggingTask.start)) / (1000 * 60 * 60 * 24);
        newEnd.setDate(newEnd.getDate() + taskDuration);

        this.draggingTask.start = this.formatDate(newStart);
        this.draggingTask.end = this.formatDate(newEnd);
      } else if (this.resizingTask) {
        const dx = event.clientX - this.initialMouseX;
        const daysMoved = Math.round(dx / this.gridItemWidth);

        if (this.resizeSide === 'start') {
          const newStart = new Date(this.initialTaskStart);
          newStart.setDate(newStart.getDate() + daysMoved);

          if (newStart < new Date(this.resizingTask.end)) {
            this.resizingTask.start = this.formatDate(newStart);
          }
        } else if (this.resizeSide === 'end') {
          const newEnd = new Date(this.initialTaskEnd);
          newEnd.setDate(newEnd.getDate() + daysMoved);

          if (newEnd > new Date(this.resizingTask.start)) {
            this.resizingTask.end = this.formatDate(newEnd);
          }
        }
      }
    },
    onMouseUp() {
      this.draggingTask = null;
      this.resizingTask = null;
      this.resizeSide = null;
    },
    updateTaskBar(task) {
      this.$nextTick(() => {
        this.updateGridLines();
      });
    }
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

.new-task-bars-column {
  width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
  position: relative;
  background-color: #ffffff;
  height: 75px !important;
}

.new-task-bar-container {
  position: relative;
  display: grid;
  grid-template-columns: repeat(90, 30px);
  height: 100%;
}

.custom-grid-lines,
.sub-custom-grid-lines {
  position: relative;
  display: grid;
  grid-template-columns: repeat(90, 30px);
  grid-template-rows: repeat(auto-fill, 40px);
  height: 100%;
}

.sub-task-bar-grid-line {
  border-left: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  height: 40px;
}

.spacer {
  height: 20px;
}

.header {
  display: flex;
  flex-shrink: 0;
}

.task-header-column {
  display: grid;
  grid-template-columns: 100px 100px 100px 100px 150px 150px; /* 各カラムの幅を指定 */
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
  overflow-x: hidden;
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
  position: relative;
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
  grid-template-rows: repeat(auto-fill, 40px);
  width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
  position: absolute;
  top: 0;
  left: 0; /* 左端に配置 */
  margin-left: 0;
  flex-grow: 1;
  background-color: #ffffff;
  height: 100%;
  border-top: 1px solid black;
}

.grid-line {
  border-left: 1px solid lightgray;
  border-bottom: 1px solid lightgray;
}

.task-bar {
  background-color: #28a745;
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: move;
  position: relative;
}

.resize-handle {
  width: 10px;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 0;
  cursor: ew-resize;
}

.resize-handle.left {
  left: 0;
}

.resize-handle.right {
  right: 0;
}
</style>
