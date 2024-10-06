<template>
  <div class="gantt-container">
      <div class="gantt-title">ガントチャート</div>
            <!-- 年と月の選択ボタンを追加 -->
            <div class="date-selector">
          <label for="year-select">年</label>
          <select v-model="selectedYear" @change="updateChart">
              <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
          </select>

          <label for="month-select">月</label>
          <select v-model="selectedMonth" @change="updateChart">
              <option v-for="month in monthOptions" :key="month" :value="month">{{ month }}</option>
          </select>
      </div>

      <!-- タスク追加ボタン -->
      <div class="buttons-container">
          <button @click="addTask" class="task-add-button">タスク追加</button>
          <!-- サブタスク追加ボタンを追加 -->
          <button @click="addSubtask" class="task-subtask-button">サブタスク追加</button>
          <!-- タスク削除ボタンを追加 -->
          <button @click="deleteTask" class="task-delete-button">タスク削除</button>
          <!-- 保存ボタン -->
          <button @click="saveTasks" class="task-save-button">保存</button>
          <!-- 読み込みボタンを追加 -->
          <button @click="fetchTasks" class="task-load-button">読み込み</button>
      </div>

      <div id="gantt" class="space-y-8 flex">
          <!-- 左側に入力フォームのヘッダーを追加 -->
          <div class="task-inputs">
              <!-- ヘッダー -->
              <div class="task-input-header">
                  <div class="task-header-item task-checkbox"></div>
                  <!-- チェックボックス用 -->
                  <div class="task-header-item task-name">タスク名</div>
                  <div class="task-header-item task-plant">プラント</div>
                  <div class="task-header-item task-pm-type">PM Type</div>
                  <div class="task-header-item task-date">開始日</div>
                  <div class="task-header-item task-date">終了日</div>
              </div>

              <!-- 入力フォーム -->
              <div v-for="(task, rowIndex) in tasks" :key="task.id" class="task-input-row">
                  <input type="checkbox" v-model="task.selected" class="task-checkbox" />
                  <input type="text" v-model="task.name" placeholder="タスク名" class="task-input task-name" @keydown="moveToNextCell($event, rowIndex, 0)" />

                  <!-- サブタスク名は存在する場合のみ表示 -->
                  <input v-if="task.subtaskName" type="text" v-model="task.subtaskName" placeholder="サブタスク名" class="task-input task-subtask-name" @keydown="moveToNextCell($event, rowIndex, 1)" />

                  <input type="text" v-model="task.plant" placeholder="プラント" class="task-input task-plant" @keydown="moveToNextCell($event, rowIndex, 2)" />
                  <input type="text" v-model="task.pmType" placeholder="PM Type" class="task-input task-pm-type" @keydown="moveToNextCell($event, rowIndex, 3)" />
                  <input type="date" v-model="task.startDate" class="task-input task-date" @keydown="moveToNextCell($event, rowIndex, 4)" />
                  <input type="date" v-model="task.endDate" class="task-input task-date" @keydown="moveToNextCell($event, rowIndex, 5)" />
              </div>
          </div>

          <!-- D3.jsでタスクバーと日付を表示するコンテナ -->
          <div id="gantt-chart-container-2" class="overflow-auto w-full select-none bg-white">
              <!-- 月と日付表示エリア -->
              <div id="month-header" class="month-header"></div>
              <div id="date-header" class="date-header"></div>
              <div id="day-of-week-header" class="day-of-week-header"></div>
              <svg id="gantt-chart"></svg>
          </div>
      </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import * as d3 from 'd3';
import dayjs from 'dayjs';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaのストアをインポート


// 選択可能な年と月のオプション
const yearOptions = ref([2022, 2023, 2024, 2025]); // 必要に応じて年を追加
const monthOptions = ref([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]);

// デフォルトの年と月
const selectedYear = ref(dayjs().year());
const selectedMonth = ref(dayjs().month() + 1); // dayjsのmonthは0始まりなので+1



// 追加: 現在の日付を取得し、その前後1か月の日付範囲を計算
const today = dayjs(); // 今日の日付
// 日付範囲を表す変数を let に変更
let startDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-01`);
let endDate = startDate.endOf('month');


const tasks = ref([]); // タスクデータ

const rowHeight = 40;
const blockWidth = 30;
let totalDays = endDate.diff(startDate, 'day') + 1;


// 年と月が変更されたときにガントチャートを更新する
function updateChart() {
    startDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-01`); // 月初
    endDate = startDate.endOf('month'); // 月末
    totalDays = endDate.diff(startDate, 'day') + 1;

    // ガントチャートの日付スケールを更新
    xScale.domain([startDate.toDate(), endDate.toDate()])
          .range([0, blockWidth * totalDays]);

    // チャートを再描画
    updateChartContent();
}


// xScaleの設定
const xScale = d3.scaleTime()
  .domain([startDate.toDate(), endDate.toDate()]) 
  .range([0, blockWidth * totalDays]);



// タスクデータの取得
async function fetchTasks() {
    const userStore = useUserStore(); 
    const companyCode = userStore.companyCode;

    try {
        const response = await axios.get('http://127.0.0.1:8000/api/junctionTable/scheduleForGanttByCompany/', {
            params: { companyCode: companyCode }
        });

        const companyData = response.data.find((company) => company.companyCode === companyCode);
        tasks.value = companyData ? companyData.ScheduleForGanttList : [];

        updateChartContent(); // ガントチャートを描画
    } catch (error) {
        console.error('タスクの取得エラー:', error);
    }
}

// 保存処理
async function saveTasks() {
  try {
      const response = await axios.post('http://127.0.0.1:8000/api/schedules/save/', tasks.value);
      console.log('Response from server:', response.data);
  } catch (error) {
      console.error('Error saving tasks:', error);
  }
}

// チャートの描画内容を更新する関数
function updateChartContent() {
    d3.select('#gantt-chart').selectAll('*').remove(); // 既存のチャートをクリア
    drawGanttChart();
    drawMonthHeader();
    drawDateHeader();
    drawDayOfWeekHeader();
}

onMounted(() => {
  fetchTasks();
  drawGanttChart();
  drawMonthHeader();
  drawDateHeader();
  drawDayOfWeekHeader();
  updateChart(); // 初回描画
});

// 入力セルでEnterキーが押された場合、次のセルに移動する関数
function moveToNextCell(event: KeyboardEvent, rowIndex: number, columnIndex: number) {
  if (event.key === 'Enter') {
      // 各行のすべての入力セルを取得
      const row = document.querySelectorAll('.task-input-row')[rowIndex];
      if (row) {
          const inputs = row.querySelectorAll('input'); // 行内の全てのinput要素を取得
          if (columnIndex + 1 < inputs.length) {
              const nextInput = inputs[columnIndex + 1] as HTMLInputElement;
              nextInput.focus();
          }
      }
  }
}

// ガントチャート描画関数
function drawGanttChart() {
  // 月のヘッダー（#month-header）の幅を取得
  const monthHeaderWidth = d3.select('#month-header').node().getBoundingClientRect().width;

  // 今日の日付に基づいてずらしを計算
  const offsetDaysInMonth = today.date(); // 今日の日付（6日など）
  const offsetWidth = (offsetDaysInMonth - 1) * blockWidth; // 1日目から数えて幅を計算（1日分の補正）

  const svg = d3
      .select('#gantt-chart')
      .attr('width', monthHeaderWidth) // 月のヘッダーと同じ幅をガントチャートに設定
      .attr('height', tasks.value.length * rowHeight) // 高さはタスクの数に依存
      .attr('transform', `translate(-${offsetWidth}, 0)`); // 幅だけ左にずらす

  drawVerticalGridLines(svg); // 縦グリッド線を描画

  svg.selectAll('.row-grid-line')
      .data(tasks.value)
      .enter()
      .append('line')
      .attr('x1', 0)
      .attr('x2', monthHeaderWidth) // 月表示の幅に応じたグリッド線の幅
      .attr('y1', (d, i) => (i + 1) * rowHeight)
      .attr('y2', (d, i) => (i + 1) * rowHeight)
      .attr('stroke', 'black');

  const drag = d3.drag().on('start', dragStarted).on('drag', dragged).on('end', dragEnded);

  const resizeLeft = d3.drag().on('start', resizeStarted).on('drag', resizingLeft).on('end', resizeEnded);

  const resizeRight = d3.drag().on('start', resizeStarted).on('drag', resizingRight).on('end', resizeEnded);

  // タスクバーの描画
  const bars = svg.selectAll('g').data(tasks.value).enter().append('g');

  bars.append('rect')
      .attr('x', (d) => xScale(dayjs(d.startDate).toDate())) // タスクの開始日をx座標に設定
      .attr('y', (d, i) => i * rowHeight) // タスクの位置をy座標に設定
      .attr('width', (d) => Math.max(1, xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()))) // 開始日と終了日で幅を計算、幅が0以下にならないように調整
      .attr('height', rowHeight) // 各タスクバーの高さを設定
      .attr('fill', 'steelblue') // タスクバーの色を設定
      .attr('cursor', 'move') // ドラッグカーソル
      .call(drag); // ドラッグイベントを追加

  // 左側のリサイズハンドルを追加
  bars.append('rect')
      .attr('x', (d) => xScale(dayjs(d.startDate).toDate()) - 5) // 開始日からの位置
      .attr('y', (d, i) => i * rowHeight)
      .attr('width', 10) // ツマミの幅を調整
      .attr('height', rowHeight)
      .attr('fill', 'gray') // ツマミの色
      .attr('cursor', 'ew-resize') // リサイズカーソル
      .call(resizeLeft); // 左側リサイズイベント

  // 右側のリサイズハンドルを追加
  bars.append('rect')
      .attr('x', (d) => xScale(dayjs(d.endDate).toDate()) - 5) // 終了日からの位置
      .attr('y', (d, i) => i * rowHeight)
      .attr('width', 10) // ツマミの幅を調整
      .attr('height', rowHeight)
      .attr('fill', 'gray') // ツマミの色
      .attr('cursor', 'ew-resize') // リサイズカーソル
      .call(resizeRight); // 右側リサイズイベント

  // タスク名のテキストを表示
  svg.selectAll('text')
      .data(tasks.value)
      .enter()
      .append('text')
      .attr('x', (d) => xScale(dayjs(d.startDate).toDate()) + 5) // テキストの位置を補正
      .attr('y', (d, i) => i * rowHeight + rowHeight / 2 + 5)
      .text((d) => d.name)
      .attr('fill', 'white'); // テキスト色を設定
}




// 縦グリッド線の描画
function drawVerticalGridLines(svg) {
  const daysArray = Array.from({ length: totalDays }, (_, i) => i + 1);
  const todayDate = dayjs().format('YYYY-MM-DD'); // 今日の日付を取得

  svg.selectAll('.column-grid-line')
      .data(daysArray)
      .enter()
      .append('rect')
      .attr('x', (d) => (d - 1) * blockWidth)
      .attr('y', 0)
      .attr('width', blockWidth)
      .attr('height', tasks.value.length * rowHeight)
      .attr('fill', (d) => {
          const currentDay = startDate.clone().add(d - 1, 'day'); // cloneで日付の安全性を確保
          return currentDay.format('YYYY-MM-DD') === todayDate ? '#ffe6e6' : 'none'; // 今日ならピンクに
      })
      .attr('stroke', '#ccc');
}


//-----------------------------------------------------------------------------------

// ドラッグ開始時の処理
function dragStarted(event, d) {
  d3.select(this).raise().attr('stroke', 'black'); // バーの前面に表示
}

// ドラッグ中の処理
function dragged(event, d) {
  const newX = event.x;
  const numDaysDragged = Math.round(newX / blockWidth); // ドラッグされた日数を計算
  const newStartDate = startDate.add(numDaysDragged, 'day'); // 修正: startDateを基準に計算
  const taskDuration = dayjs(d.endDate).diff(dayjs(d.startDate), 'day'); // タスクの期間を取得
  const newEndDate = newStartDate.add(taskDuration, 'day'); // 新しい終了日を計算

  // 更新された開始日と終了日を設定
  d.startDate = newStartDate.format('YYYY-MM-DD');
  d.endDate = newEndDate.format('YYYY-MM-DD');

  // バーの位置を更新
  d3.select(this)
    .attr('x', newX) // 新しいx座標
    .attr('width', blockWidth * (taskDuration + 1)); // バーの幅を期間に応じて設定
}

// ドラッグ終了時の処理
function dragEnded(event, d) {
  d3.select(this).attr('stroke', null); // ドラッグ終了後に線をクリア
  updateTaskDates(d.id); // 日付をフォームに反映
}

// リサイズ開始時の処理
function resizeStarted(event, d) {
  d3.select(this).raise().attr('stroke', 'black'); // バーを前面に表示
}

// 左端リサイズ中の処理
function resizingLeft(event, d) {
  const newX = event.x;
  const numDaysResized = Math.round(newX / blockWidth); // リサイズされた日数を計算
  const newStartDate = startDate.add(numDaysResized, 'day'); // リサイズされた新しい開始日を計算
  d.startDate = newStartDate.format('YYYY-MM-DD');

  // バーの位置と幅を更新
  d3.select(this.parentNode)
    .select('rect')
    .attr('x', newX)
    .attr('width', xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()));
}

// 右端リサイズ中の処理
function resizingRight(event, d) {
  const newX = event.x;
  const numDaysResized = Math.round(newX / blockWidth); // リサイズされた日数を計算
  const newEndDate = startDate.add(numDaysResized, 'day'); // リサイズされた新しい終了日を計算
  d.endDate = newEndDate.format('YYYY-MM-DD');

  // バーの幅を更新
  d3.select(this.parentNode)
    .select('rect')
    .attr('width', xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()));
}

// リサイズ終了時の処理
function resizeEnded(event, d) {
  d3.select(this).attr('stroke', null); // リサイズ終了後に線をクリア
  updateTaskDates(d.id); // 日付をフォームに反映
}




//-----------------------------------------------------------------------------------




// 月のヘッダーを表示する関数
function drawMonthHeader() {
    const monthHeader = d3.select('#month-header');

    // 月ごとの区切りを描画するために使用するデータを作成
    const monthData = [];
    let currentMonth = startDate.clone(); // startDateをコピーしてcurrentMonthとして使用
    while (currentMonth.isBefore(endDate)) {
        const firstDayOfMonth = currentMonth.startOf('month'); // 各月の最初の日
        const lastDayOfMonth = currentMonth.endOf('month'); // 各月の最後の日
        const monthDays = lastDayOfMonth.diff(firstDayOfMonth, 'day') + 1; // 月の日数を計算

        // データに追加
        monthData.push({
            month: currentMonth.format('MMMM YYYY'), // 月と年をフォーマット
            daysInMonth: monthDays // 月の日数
        });

        currentMonth = currentMonth.add(1, 'month'); // 1か月進める
    }

    // 今日の日付をstartDateからの差分で計算
    const todayIndex = today.diff(startDate, 'day'); // 今日の日付までの差分（開始日から今日までの日数）

    // 月の描画
    monthHeader
        .style('width', `${blockWidth * totalDays}px`) // 全体の横幅を設定
        .style('display', 'flex')
        .style('overflow', 'hidden');

    // 境界線の調整ロジック
    const offsetDaysInFirstMonth = today.date(); // 今月の「開始」位置を調整するために使う
    let cumulativeDays = 0;

    // 各月の表示部分を作成
    monthHeader.selectAll('div')
        .data(monthData)
        .enter()
        .append('div')
        .style('width', (d, i) => {
            // 最初の月は今日の日を基準にずらす
            if (i === 0) {
                return `${(d.daysInMonth - offsetDaysInFirstMonth + 1) * blockWidth}px`;
            } else {
                return `${d.daysInMonth * blockWidth}px`; // 通常の月の幅
            }
        })
        .style('text-align', 'center')
        .style('border-right', '1px solid black') // 境界線を追加
        .style('font-weight', 'bold')
        .text((d) => d.month);

    // 今日の日付の位置を調整する
    monthHeader.style('transform', `translateX(-${offsetDaysInFirstMonth * blockWidth}px)`); // 本日の日付に基づき位置をずらす
}

// 日付のヘッダーを表示する関数
function drawDateHeader() {
    const dateHeader = d3.select('#date-header');

    // 日ごとのデータを作成
    const dateData = [];
    let currentDate = startDate.clone(); // startDateをコピーしてcurrentDateとして使用
    while (currentDate.isBefore(endDate) || currentDate.isSame(endDate, 'day')) {
        dateData.push(currentDate.format('D')); // 日付をフォーマットして追加
        currentDate = currentDate.add(1, 'day'); // 1日進める
    }

    // 日付の描画
    dateHeader
        .style('width', `${blockWidth * totalDays}px`) // ガントチャートの横幅に一致
        .style('display', 'flex')
        .style('overflow', 'hidden')
        .style('transform', `translateX(-${today.date() * blockWidth}px)`); // 本日の日付に基づき位置を調整

    // 各日付の表示部分を作成
    dateHeader.selectAll('div')
        .data(dateData)
        .enter()
        .append('div')
        .style('width', `${blockWidth}px`) // 各日の横幅を設定
        .style('text-align', 'center')
        .style('border-right', '1px solid black')
        .style('background-color', (d, i) => dayjs(startDate).add(i, 'day').isSame(dayjs(), 'day') ? '#ffe6e6' : '#f0f0f0') // 今日の日付をピンクに
        .text((d) => d); // 日付を表示
}


// 曜日ヘッダーを表示する関数
function drawDayOfWeekHeader() {
    const dayOfWeekHeader = d3.select('#day-of-week-header');

    // 日ごとの曜日データを作成
    const dayOfWeekData = [];
    let currentDate = startDate.clone(); // startDateをコピーしてcurrentDateとして使用
    while (currentDate.isBefore(endDate) || currentDate.isSame(endDate, 'day')) {
        dayOfWeekData.push(currentDate.format('dd')); // 曜日をフォーマットして追加
        currentDate = currentDate.add(1, 'day'); // 1日進める
    }

    // 曜日の描画
    dayOfWeekHeader
        .style('width', `${blockWidth * totalDays}px`) // ガントチャートの横幅に一致
        .style('display', 'flex')
        .style('overflow', 'hidden')
        .style('transform', `translateX(-${today.date() * blockWidth}px)`); // 本日の日付に基づき位置を調整

    // 各曜日の表示部分を作成
    dayOfWeekHeader.selectAll('div')
        .data(dayOfWeekData)
        .enter()
        .append('div')
        .style('width', `${blockWidth}px`) // 各曜日の横幅を設定
        .style('text-align', 'center')
        .style('border-right', '1px solid black')
        .style('color', (d, i) => getDayColor(dayjs(startDate).add(i, 'day').day())) // 曜日に応じた色付け
        .style('background-color', (d, i) => dayjs(startDate).add(i, 'day').isSame(dayjs(), 'day') ? '#ffe6e6' : '#f0f0f0') // 今日の日付をピンクに
        .text((d) => d); // 曜日を表示
}

// 曜日に応じて色を決定
function getDayColor(dayOfWeek) {
    if (dayOfWeek === 0) {
        return 'red'; // 日曜日
    } else if (dayOfWeek === 6) {
        return 'blue'; // 土曜日
    } else {
        return 'black'; // 平日
    }
}


// 日付の更新時にガントチャートを再描画
function updateTaskDates(id) {
  const task = tasks.value.find((t) => t.id === id);
  if (task) {
      task.startDate = dayjs(task.startDate).format('YYYY-MM-DD');
      task.endDate = dayjs(task.endDate).format('YYYY-MM-DD');
      updateChart();
  }
}



//-----------------------------------------------------------------------------------

//task追加関数
function addTask() {
  const newTaskId = tasks.value.length + 1;
  const newTask = {
      id: newTaskId,
      name: `Task ${newTaskId}`,
      pmType: `PM${newTaskId}`,
      startDate: startDate.format('YYYY-MM-DD'), // 修正: currentMonthではなくstartDateを使用
      endDate: startDate.add(1, 'day').format('YYYY-MM-DD') // 修正: currentMonthではなくstartDateを使用
  };
  tasks.value.push(newTask); // 新しいタスクを追加
  updateChart(); // ガントチャートを更新
}

// タスク削除の実際の処理
function deleteTask() {
  tasks.value = tasks.value.filter((task) => !task.selected); // チェックが入っていないタスクのみ残す
  updateChart(); // ガントチャートを更新
}

// サブタスク追加の実際の関数
function addSubtask() {
  // 1. チェックされた行を検出
  const selectedTaskIndex = tasks.value.findIndex((task) => task.selected);
  if (selectedTaskIndex === -1) {
      console.log('サブタスクを追加するタスクが選択されていません');
      return;
  }

  // 2. サブタスクを追加
  const newSubtask = {
      id: tasks.value.length + 1,
      name: tasks.value[selectedTaskIndex].name, // 元のタスク名をコピー
      subtaskName: '', // サブタスク名は空で追加
      plant: tasks.value[selectedTaskIndex].plant, // プラント名もコピー
      pmType: tasks.value[selectedTaskIndex].pmType,
      startDate: tasks.value[selectedTaskIndex].startDate,
      endDate: tasks.value[selectedTaskIndex].endDate,
      selected: false, // チェック状態を初期化
      isSubtask: true // サブタスクであることを示すフラグ
  };

  // チェックされた行の下にサブタスクを挿入
  tasks.value.splice(selectedTaskIndex + 1, 0, newSubtask);

  // 3. ヘッダーに「サブタスク名」を追加し、既に存在しているか確認
  const subtaskHeaderExists = document.querySelector('.task-header-item.task-subtask-name');
  if (!subtaskHeaderExists) {
      const header = document.querySelector('.task-input-header');
      if (header) {
          // ヘッダーが存在する場合にのみ処理
          const subtaskHeader = document.createElement('div');
          subtaskHeader.className = 'task-header-item task-subtask-name';
          subtaskHeader.textContent = 'サブタスク名';
          header.insertBefore(subtaskHeader, header.querySelector('.task-plant'));
      }

      // 4. 全ての既存の行に「サブタスク名」の入力フォームを追加
      document.querySelectorAll('.task-input-row').forEach((row) => {
          if (row) {
              // 各行が存在する場合にのみ処理
              const subtaskCell = document.createElement('input');
              subtaskCell.type = 'text';
              subtaskCell.placeholder = 'サブタスク名';
              subtaskCell.className = 'task-input task-subtask-name';
              row.insertBefore(subtaskCell, row.querySelector('.task-plant'));
          }
      });
  }

  // 5. 新しく追加したサブタスク行に「サブタスク名」のセルを追加
  const subtaskRow = document.querySelectorAll('.task-input-row')[selectedTaskIndex + 1]; // 新しく追加したサブタスク行
  if (subtaskRow) {
      // サブタスク行が存在する場合にのみ処理
      const subtaskCellForNewRow = document.createElement('input');
      subtaskCellForNewRow.type = 'text';
      subtaskCellForNewRow.placeholder = 'サブタスク名';
      subtaskCellForNewRow.className = 'task-input task-subtask-name';
      subtaskRow.insertBefore(subtaskCellForNewRow, subtaskRow.querySelector('.task-plant'));
  }

  // 6. チェックされた行と新しいサブタスク行の「タスク名」を結合して表示
  tasks.value[selectedTaskIndex].name = newSubtask.name;
  tasks.value[selectedTaskIndex].subtaskName = newSubtask.subtaskName;
  tasks.value[selectedTaskIndex + 1].name = newSubtask.name; // サブタスクの名前を親タスク名に統一
  tasks.value[selectedTaskIndex + 1].subtaskName = newSubtask.subtaskName; // サブタスク名を設定

  updateChart(); // ガントチャートを更新
}
</script>

<style scoped>
.gantt-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: white; /* 背景を白に変更 */
}

.gantt-title {
  font-size: 2rem; /* 文字サイズを大きく */
  font-weight: bold; /* 太字 */
  text-align: left; /* 左寄せに変更 */
  margin-bottom: 20px; /* ボタンとの間に余白を追加 */
}

/* タスク入力ヘッダーのスタイル */
.task-input-header {
  display: flex;
  font-weight: bold;
  text-align: center;
  background-color: #28a745; /* 緑色に変更 */
  border-bottom: 2px solid black;
  height: 90px; /* ヘッダーの高さ */
  align-items: center;
}

/* 各項目のスタイル */
.task-header-item,
.task-input {
  padding: 10px;
  border-right: 1px solid black;
  height: 100%; /* ヘッダーと入力フォームの高さを揃える */
}

/* 各列の幅を統一 */
.task-name,
.task-plant,
.task-pm-type,
.task-date {
  width: 150px; /* 各項目の横幅を150pxに統一 */
}

/* 入力フォームのスタイル */
.task-input-row {
  display: flex;
  height: 40px;
  margin: 0;
}

.task-input {
  margin: 0;
  padding: 5px;
  height: 100%;
  border: 1px solid black;
  border-top: none;
}

/* 月のヘッダー */
.month-header {
  display: flex;
  justify-content: flex-start;
  padding: 0px;
  background-color: #f0f0f0;
  border-bottom: 1px solid black;
  font-size: 1.2rem;
  height: 30px;
}

/* 日付ヘッダー */
.date-header {
  display: flex;
  justify-content: flex-start;
  padding: 0px;
  background-color: #f0f0f0;
  border-bottom: 1px solid black;
  height: 30px;
}

/* 曜日ヘッダー */
.day-of-week-header {
  display: flex;
  justify-content: flex-start;
  padding: 0px;
  background-color: #f0f0f0;
  border-bottom: 1px solid black;
  height: 30px;
}

/* 日付と曜日のスタイル */
.date-header div,
.day-of-week-header div {
  width: 30px;
  text-align: center;
}

/* buttons-container を横並びにするための修正 */
.buttons-container {
  display: flex; /* 横並びに配置 */
  flex-direction: row; /* 水平方向に並べる */
  gap: 10px; /* ボタン間の隙間を追加 */
  margin-bottom: 20px; /* ガントチャートの他の要素との間に余白を追加 */
}

/* タスク追加ボタンのスタイル */
.task-add-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.task-add-button:hover {
  background-color: #0056b3;
}

/* 保存ボタンのスタイル */
.task-save-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.task-save-button:hover {
  background-color: #218838;
}

/* 読み込みボタンのスタイルを追加 */
.task-load-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #17a2b8; /* ブルー系の色 */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.task-load-button:hover {
  background-color: #138496;
}

/* タスク削除ボタンのスタイル */
.task-delete-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #dc3545; /* レッド系の色 */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.task-delete-button:hover {
  background-color: #c82333;
}

/* チェックボックスのスタイルを追加 */
.task-checkbox {
  width: 30px;
  height: 30px;
  margin: 5px;
}

/* サブタスク追加ボタンのスタイルを追加 */
.task-subtask-button {
  margin-bottom: 10px;
  padding: 8px 16px;
  background-color: #ffc107; /* イエロー系の色 */
  color: black;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.task-subtask-button:hover {
  background-color: #e0a800;
}

/* サブタスク名の入力セルのスタイル */
.task-subtask-name {
  width: 150px;
  padding: 5px;
  border-right: 1px solid black;
  height: 100%;
}
</style>
