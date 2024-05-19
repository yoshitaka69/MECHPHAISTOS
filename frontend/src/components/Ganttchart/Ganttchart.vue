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
              :class="{ saturday: isSaturday(date), sunday: isSunday(date) }"
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
          </div>
        </div>
        <div class="task-bars-column" ref="taskBars" @scroll="syncScroll">
          <div class="custom-grid-lines" ref="customGridLines">
            <div
              v-for="task in tasks"
              :key="task.id"
              class="task-bar"
              :style="getTaskBarStyle(task)"
              @mousedown="selectTask(task)"
            >
              {{ task.name }}
            </div>
            <div v-for="date in dates" :key="date" class="task-bar-grid-line">
              <div :class="{ 'saturday-bg': isSaturday(date), 'sunday-bg': isSunday(date) }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <script>
  import interact from 'interactjs';
  
  export default {
    data() {
      return {
        dates: this.generateDates(new Date(2024, 3, 1), 90), // Start from April 1, 2024 for 3 months
        tasks: [
          { id: 1, name: 'Task 1', content: 'Content 1', assignee: 'User 1', progress: '0%', start: new Date(2024, 3, 1), end: new Date(2024, 3, 10) },
          { id: 2, name: 'Task 2', content: 'Content 2', assignee: 'User 2', progress: '50%', start: new Date(2024, 3, 5), end: new Date(2024, 3, 15) },
          { id: 3, name: 'Task 3', content: 'Content 3', assignee: 'User 3', progress: '100%', start: new Date(2024, 3, 12), end: new Date(2024, 3, 20) }
        ],
        gridItemWidth: 30, // グリッド項目の幅を設定
        taskHeaderWidth: 0, // タスクヘッダーの横幅を保持
        selectedTask: null // 選択されたタスクを保持
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
        this.enableDragAndResize(); // ドラッグ＆リサイズを有効にする
        window.addEventListener('resize', this.updateGridLines);
        window.addEventListener('resize', this.updateTaskFieldWidth);
      });
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.updateGridLines);
      window.removeEventListener('resize', this.updateTaskFieldWidth);
    },
    methods: {
      /**
       * 指定された日付から指定された日数分の配列を生成します。
       * @param {Date} startDate - 開始日付
       * @param {number} days - 日数
       * @returns {string[]} 日付の配列
       */
      generateDates(startDate, days) {
        let dates = [];
        for (let i = 0; i < days; i++) {
          let date = new Date(startDate);
          date.setDate(startDate.getDate() + i);
          dates.push(date);
        }
        return dates.map((date) => this.formatDate(date));
      },
  
      /**
       * 日付から日をフォーマットします。
       * @param {string} date - フォーマットする日付
       * @returns {number} 日
       */
      formatDay(date) {
        const day = new Date(date).getDate();
        return day;
      },
  
      /**
       * 日付から曜日をフォーマットします。
       * @param {string} date - フォーマットする日付
       * @returns {string} 曜日
       */
      formatWeekday(date) {
        const weekdays = ['日', '月', '火', '水', '木', '金', '土'];
        const day = new Date(date).getDay();
        return weekdays[day];
      },
  
      /**
       * 日付が土曜日かどうかをチェックします。
       * @param {string} date - チェックする日付
       * @returns {boolean} 土曜日の場合は true、そうでない場合は false
       */
      isSaturday(date) {
        return new Date(date).getDay() === 6;
      },
  
      /**
       * 日付が日曜日かどうかをチェックします。
       * @param {string} date - チェックする日付
       * @returns {boolean} 日曜日の場合は true、そうでない場合は false
       */
      isSunday(date) {
        return new Date(date).getDay() === 0;
      },
  
      /**
       * 日付をフォーマットします。
       * @param {Date} date - フォーマットする日付
       * @returns {string} フォーマットされた日付
       */
      formatDate(date) {
        return date.toISOString().split('T')[0];
      },
  
      /**
       * タスクバーとヘッダーのスクロールを同期します。
       */
      syncScroll() {
        const dateHeader = this.$refs.dateHeader;
        const taskBars = this.$refs.taskBars;
        const newTaskBars = this.$refs.newTaskBars;
        dateHeader.scrollLeft = taskBars.scrollLeft;
        newTaskBars.scrollLeft = taskBars.scrollLeft;
      },
  
      /**
       * グリッドテンプレートのカラム数を取得します。
       * @returns {string} グリッドテンプレートのカラム数
       */
      getGridTemplateColumns() {
        const columnsCount = this.dates.length;
        return `repeat(${columnsCount}, ${this.gridItemWidth}px)`;
      },
  
      /**
       * グリッドラインを更新します。
       */
      updateGridLines() {
        const taskBarsElement = this.$refs.taskBars;
        const taskBarsHeight = taskBarsElement.clientHeight;
        const gridLines = taskBarsElement.querySelectorAll('.task-bar-grid-line');
        const customGridLines = this.$refs.customGridLines;
        const numberOfDays = this.dates.length;
        const gridWidth = numberOfDays * this.gridItemWidth;
  
        gridLines.forEach((line, index) => {
          line.style.height = `${taskBarsHeight}px`;
          line.style.width = `${this.gridItemWidth}px`;
          const date = this.dates[index];
          line.classList.remove('saturday', 'sunday', 'weekday'); // 以前のクラスを削除
          if (this.isSaturday(date)) {
            line.classList.add('saturday');
          } else if (this.isSunday(date)) {
            line.classList.add('sunday');
          } else {
            line.classList.add('weekday');
          }
        });
  
        customGridLines.style.width = `${gridWidth}px`;
        customGridLines.style.gridTemplateColumns = this.getGridTemplateColumns();
      },
  
      /**
       * タスクフィールドの横幅をタスクヘッダーの横幅に合わせて更新します。
       */
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
  
      /**
       * タスクバーのスタイルを取得します。
       * @param {Object} task - タスクオブジェクト
       * @returns {Object} タスクバーのスタイル
       */
      getTaskBarStyle(task) {
        const start = new Date(task.start);
        const end = new Date(task.end);
        const startDate = new Date(this.dates[0]);
        const endDate = new Date(this.dates[this.dates.length - 1]);
  
        if (start < startDate) start = startDate;
        if (end > endDate) end = endDate;
  
        const startIndex = (start - startDate) / (1000 * 60 * 60 * 24);
        const endIndex = (end - startDate) / (1000 * 60 * 60 * 24);
  
        return {
          gridColumnStart: startIndex + 1,
          gridColumnEnd: endIndex + 2
        };
      },
  
      /**
       * interactjsを使用してドラッグ＆リサイズを有効にします。
       */
      enableDragAndResize() {
        const vm = this;
        interact('.task-bar')
          .draggable({
            onmove(event) {
              const target = event.target;
              const task = vm.tasks.find(t => t.name === target.innerText);
              if (task) {
                const dx = event.dx / vm.gridItemWidth;
                const start = new Date(task.start);
                start.setDate(start.getDate() + dx);
                const end = new Date(task.end);
                end.setDate(end.getDate() + dx);
                task.start = vm.formatDate(start);
                task.end = vm.formatDate(end);
                vm.updateGridLines();
              }
            }
          })
          .resizable({
            edges: { left: true, right: true },
            onmove(event) {
              const target = event.target;
              const task = vm.tasks.find(t => t.name === target.innerText);
              if (task) {
                const start = new Date(task.start);
                const end = new Date(task.end);
                if (event.edges.left) {
                  const dx = event.deltaRect.left / vm.gridItemWidth;
                  start.setDate(start.getDate() + dx);
                }
                if (event.edges.right) {
                  const dx = event.deltaRect.right / vm.gridItemWidth;
                  end.setDate(end.getDate() + dx);
                }
                task.start = vm.formatDate(start);
                task.end = vm.formatDate(end);
                vm.updateGridLines();
              }
            }
          });
      }
    }
  };
  </script>
  
  <style scoped>
  /* ガントチャートの全体レイアウト */
  .gantt-chart {
    display: flex;
    flex-direction: column;
    height: 100vh;
    margin: 20px; /* 上下左右に余白を設定 */
  }
  
  /* 新しいタスクバー領域のスタイル */
  .new-task-bars-column {
    width: 100%; /* 横幅を親要素に合わせて一杯にする */
    overflow-x: auto;
    overflow-y: hidden;
    position: relative;
    background-color: #ffffff; /* 背景を白色に変更 */
    left: 540px; /* date-header-columnの幅に合わせて調整 */
    height: 75px !important; /* 高さを75pxに設定 */
  }
  
  /* 新しいタスクバーコンテナのスタイル */
  .new-task-bar-container {
    position: relative;
    display: grid;
    grid-template-columns: repeat(90, 30px); /* 90日分を30pxで表示 */
    height: 100%; /* 親要素の高さに合わせる */
  }
  
  /* カスタムグリッドラインのスタイル */
  .custom-grid-lines,
  .sub-custom-grid-lines {
    position: relative;
    display: grid;
    grid-template-columns: repeat(90, 30px); /* 90日分を30pxで表示 */
    height: 100%; /* 親要素の高さに合わせる */
  }
  
  /* タスクバーのグリッドラインのスタイル */
  .task-bar-grid-line {
    border-left: 1px solid lightgray; /* 縦線のグリッド線を薄い灰色に設定 */
    border-bottom: 1px solid lightgray; /* 横線のグリッド線を薄い灰色に設定 */
    width: 30px; /* グリッド項目の幅を設定 */
  }
  
  /* サブタスクバーのグリッドラインのスタイル */
  .sub-task-bar-grid-line {
    border-left: 1px solid #ddd; /* 縦線のグリッド線を追加 */
    border-bottom: 1px solid #ddd; /* 横線のグリッド線を追加 */
    height: 40px; /* グリッドラインの高さを40pxに設定 */
  }
  
  /* スペーサーのスタイル */
  .spacer {
    height: 20px; /* 新しいガントバー領域と既存のガントチャートの間にスペースを追加 */
  }
  
  /* ヘッダーのスタイル */
  .header {
    display: flex;
    flex-shrink: 0;
  }
  
  /* タスクヘッダーのカラムスタイル */
  .task-header-column {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 4つのタスクヘッダー */
    width: 600px; /* 横幅を固定 */
    border-right: 1px solid #ddd;
    background-color: #28a745; /* 背景を緑色に変更 */
  }
  
  /* タスクヘッダーのスタイル */
  .task-header {
    text-align: center;
    padding: 10px;
    font-weight: bold;
    background-color: #28a745; /* 背景を緑色に変更 */
    color: white;
    border-right: 1px solid #ddd;
  }
  
  /* 日付ヘッダーのカラムスタイル */
  .date-header-column {
    display: grid;
    grid-template-rows: auto auto; /* 自動の高さ */
    width: 100%; /* 横幅を親要素に合わせて一杯にする */
    overflow-x: hidden; /* スクロールバーを非表示にする */
  }
  
  /* 年月行、日付行のスタイル */
  .year-month-row,
  .day-row {
    display: grid;
    grid-template-columns: repeat(90, 30px); /* 90日分を30pxで表示 */
    background-color: #ffffff; /* 背景を白色に変更 */
    text-align: center;
  }
  
  /* 年月行のスタイル */
  .year-month-row {
    border-bottom: 1px solid #ddd;
    background-color: #007bff; /* 背景を青色に変更 */
    color: black; /* 文字を黒色に変更 */
  }
  
  /* 年月項目、ヘッダー項目のスタイル */
  .year-month-item,
  .header-item {
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #ddd;
  }
  
  /* ヘッダー項目のスタイル */
  .header-item {
    text-align: center;
    padding: 5px;
    color: black; /* 日付の文字を黒字に変更 */
  }
  
  /* 平日のスタイル */
  .weekday {
    background-color: #ffffff; /* 平日の背景色を白に設定 */
  }
  
  /* 土曜日のスタイル */
  .saturday {
    background-color: #e0f7fa; /* 土曜日の背景色を薄い青に設定 */
  }
  
  /* 日曜日のスタイル */
  .sunday {
    background-color: #ffebee; /* 日曜日の背景色を薄い赤に設定 */
  }
  
  /* タスク名のカラムスタイル */
  .rows {
    display: flex;
    flex-grow: 1;
    overflow-x: hidden;
  }
  
  /* タスク名の列スタイル */
  .task-names-column {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 4つのタスク名カラム */
    grid-auto-rows: 40px; /* 各タスクの高さを一致させる */
    width: 600px; /* 横幅を固定 */
    border-right: 1px solid #ddd;
    overflow-y: auto; /* タスク領域の縦スクロールを有効にする */
    background-color: #ffffff; /* 背景を白色に変更 */
    border-bottom: 1px solid #ddd; /* 横のグリッド線を追加 */
    height: 100%; /* コンテナ全体の高さを設定 */
    position: relative;
  }
  
  /* タスク名のグリッドラインを追加 */
  .task-names-column::after {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
    background: repeating-linear-gradient(to bottom, transparent, transparent 39px, black 40px);
    pointer-events: none; /* クリックイベントを無視する */
  }
  
  /* タスク名のスタイル */
  .task-name {
    display: contents; /* 各タスクを同じ高さにするために使用 */
  }
  
  /* タスクフィールドのスタイル */
  .task-field {
    display: flex;
    align-items: center;
    padding: 10px;
    background: #ffffff; /* 背景を白色に変更 */
    border-bottom: 1px solid lightgray; /* 下線を薄い灰色に設定 */
    border-left: 1px solid lightgray; /* 縦線（左）を薄い灰色に設定 */
    width: 100%;
    outline: none;
  }
  
  /* タスク入力フィールドのスタイル */
  .task-input {
    width: 100%;
    border: 1px solid white; /* 外枠を白に設定 */
    outline: none;
    background: transparent;
    box-sizing: border-box; /* パディングを含むように設定 */
  }
  
  /* タスクバーのカラムスタイル */
  .task-bars-column {
    display: grid;
    grid-template-rows: repeat(auto-fill, 40px); /* 自動でフィル */
    width: 100%; /* 横幅を親要素に合わせて一杯にする */
    overflow-x: auto;
    overflow-y: hidden;
    position: relative;
    flex-grow: 1;
    background-color: #ffffff; /* 背景を白色に変更 */
    height: 100%; /* コンテナ全体の高さを設定 */
    border-top: 1px solid black; /* 外枠の上部分を黒に設定 */
  }
  
  /* 繰り返しグリッドラインを追加 */
  .task-bars-column::before {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: repeating-linear-gradient(to bottom, transparent, transparent 39px, black 40px);
    pointer-events: none; /* クリックイベントを無視する */
  }
  
  /* 縦線のグリッド線を薄い灰色に設定 */
  .grid-line {
    border-left: 1px solid lightgray;
    border-bottom: 1px solid black; /* 横線のグリッド線を黒に設定 */
  }
  
  /* タスクバーのスタイル */
  .task-bar {
    background-color: #007bff;
    color: white;
    text-align: center;
    border-radius: 3px;
    cursor: move;
    user-select: none;
  }
  </style>
  