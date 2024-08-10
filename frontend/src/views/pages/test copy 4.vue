<template>
  <div id="gantt" class="space-y-4">
    <!-- 上部のガントチャート -->
    <div class="gantt-chart-wrapper top-chart" :style="{ height: `${topChartHeight}px` }">
      <div id="gantt-chart-container-1" class="overflow-auto w-full select-none bg-white">
        <!-- ヘッダー領域 -->
        <div id="top-header" class="top-0 flex z-20 sticky">
          <div class="border-b border-black bg-green-100 flex sticky left-0 top-0" :style="{ minWidth: `${topTaskWidth + topExtraColumns.length * extraColumnWidth}px` }">
            <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 100px">Plant</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">開始日</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">期限日</div>
            <div v-for="column in topExtraColumns" :key="column.key" class="bg-green-100 text-center border-r border-black text-sm" :style="{ width: `${extraColumnWidth}px` }">
              {{ column.label }}
            </div>
          </div>
          <div class="flex" :style="{ width: `${topViewWidth}px` }">
            <template v-for="month in calendars" :key="month.title">
              <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days.length}px` }">
                <div class="border-b border-r border-black px-2 text-xs">{{ month.title }}</div>
                <div class="flex">
                  <div
                    v-for="day in month.days"
                    :key="day.date"
                    class="border-r border-black text-xs text-center"
                    :class="weekendColor(day.dayOfWeek)"
                    :style="{ minWidth: `${blockWidth}px`, maxWidth: `${blockWidth}px` }"
                  >
                    {{ day.date }}
                  </div>
                </div>
                <div class="flex">
                  <div
                    v-for="day in month.days"
                    :key="day.date"
                    class="border-r border-black text-xs text-center"
                    :class="weekendColor(day.dayOfWeek)"
                    :style="{ minWidth: `${blockWidth}px`, maxWidth: `${blockWidth}px` }"
                  >
                    {{ day.dayOfWeek }}
                  </div>
                </div>
              </div>
            </template>
          </div>
        </div>

        <!-- タスク入力領域とガントバー -->
        <div id="top-contents" class="relative overflow-y-auto" :style="{ width: `${topViewWidth + topExtraColumns.length * extraColumnWidth}px` }">
          <!-- 縦のグリッド線を表示 -->
          <div
            v-for="i in totalDays"
            :key="i"
            class="absolute bg-gray-200"
            :style="{ left: `${i * blockWidth}px`, top: 0, height: `${topTaskRows.length * taskRowHeight}px`, width: '1px' }"
          ></div>
          <!-- 今日の日付を示す赤い帯 -->
          <div
            v-if="topTodayPosition >= 0"
            class="absolute bg-red-100"
            :style="{ width: `${blockWidth - 1}px`, left: `${topTodayPosition}px`, height: `${topTaskRows.length * taskRowHeight}px` }"
          ></div>
          <div v-for="task in topTaskRows" :key="task.id" class="task-row top-task-row flex">
            <div class="bg-green-100 z-10 flex sticky left-0" :style="{ minWidth: `${topTaskWidth + topExtraColumns.length * extraColumnWidth}px` }">
              <!-- 編集可能なタスク名フィールド -->
              <input
                class="py-2 h-full px-2 border-r border-black text-sm"
                style="width: 100px"
                v-model="task.name"
                @change="updateTopTaskName(task)"
              />
              <!-- 編集可能な開始日フィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 90px"
                type="date"
                v-model="task.startDate"
                @change="updateTaskDates(task)"
              />
              <!-- 編集可能な期限日フィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 90px"
                type="date"
                v-model="task.endDate"
                @change="updateTaskDates(task)"
              />
              <div v-for="column in topExtraColumns" :key="column.key" class="bg-green-100 text-center border-r border-black text-sm" :style="{ width: `${extraColumnWidth}px` }">
                <input
                  class="py-2 h-full text-center"
                  v-model="task[column.key]"
                  @change="updateTopTaskAdditional(task, column.key)"
                />
              </div>
            </div>
            <div :style="task.style" class="h-10 flex py-2 will-change-transform cursor-pointer" @mousedown="onMouseDown_MoveStart($event, task, topTasks)">
              <div class="w-2 bg-yellow-200 rounded-l-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'left', topTasks)"></div>
              <div class="flex-1 bg-yellow-200 pointer-events-none"></div>
              <div class="w-2 bg-yellow-200 rounded-r-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'right', topTasks)"></div>
            </div>
          </div>
          <!-- タスク追加ボタン -->
          <button class="mt-2 bg-green-200 hover:bg-green-300 text-sm py-1 px-4 rounded" @click="addTopTask">
            + タスクを追加
          </button>
          <!-- 列追加ボタン -->
          <button class="mt-2 ml-2 bg-green-300 hover:bg-green-400 text-sm py-1 px-4 rounded" @click="addTopTaskColumn">
            + 列を追加
          </button>
          <!-- タスク削除ボタン -->
          <button class="mt-2 ml-2 bg-red-200 hover:bg-red-300 text-sm py-1 px-4 rounded" @click="removeSelectedTopTasks">
            選択したタスクを削除
          </button>
        </div>
      </div>
    </div>

    <!-- 下部のガントチャート -->
    <div class="gantt-chart-wrapper bottom-chart mt-4" :style="{ height: `${bottomChartHeight}px` }">
      <div id="gantt-chart-container-2" class="overflow-auto w-full select-none bg-white">
        <!-- ヘッダー領域 -->
        <div id="bottom-header" class="top-0 flex z-20 sticky">
          <div class="border-b border-black bg-blue-100 flex sticky left-0 top-0" :style="{ minWidth: `${bottomTaskWidth + bottomExtraColumns.length * extraColumnWidth}px` }">
            <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 80px">タスク</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">サンプル</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">PM type</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">担当者</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">開始日</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">期限日</div>
            <div v-for="column in bottomExtraColumns" :key="column.key" class="bg-blue-100 text-center border-r border-black text-sm" :style="{ width: `${extraColumnWidth}px` }">
              {{ column.label }}
            </div>
          </div>
          <div class="flex" :style="{ width: `${bottomViewWidth}px` }">
            <template v-for="month in calendars" :key="month.title">
              <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days.length}px` }">
                <div class="border-b border-r border-black px-2 text-xs">{{ month.title }}</div>
                <div class="flex">
                  <div
                    v-for="day in month.days"
                    :key="day.date"
                    class="border-r border-black text-xs text-center"
                    :class="weekendColor(day.dayOfWeek)"
                    :style="{ minWidth: `${blockWidth}px`, maxWidth: `${blockWidth}px` }"
                  >
                    {{ day.date }}
                  </div>
                </div>
                <div class="flex">
                  <div
                    v-for="day in month.days"
                    :key="day.date"
                    class="border-r border-black text-xs text-center"
                    :class="weekendColor(day.dayOfWeek)"
                    :style="{ minWidth: `${blockWidth}px`, maxWidth: `${blockWidth}px` }"
                  >
                    {{ day.dayOfWeek }}
                  </div>
                </div>
              </div>
            </template>
          </div>
        </div>

        <!-- タスク入力領域とガントバー -->
        <div id="bottom-contents" class="relative overflow-y-auto" :style="{ width: `${bottomViewWidth + bottomExtraColumns.length * extraColumnWidth}px` }">
          <!-- 縦のグリッド線を表示 -->
          <div
            v-for="i in totalDays"
            :key="i"
            class="absolute bg-gray-200"
            :style="{ left: `${i * blockWidth}px`, top: 0, height: `${bottomTaskRows.length * taskRowHeight}px`, width: '1px' }"
          ></div>
          <!-- 今日の日付を示す赤い帯 -->
          <div
            v-if="bottomTodayPosition >= 0"
            class="absolute bg-red-100"
            :style="{ width: `${blockWidth - 1}px`, left: `${bottomTodayPosition}px`, height: `${bottomTaskRows.length * taskRowHeight}px` }"
          ></div>
          <div v-for="task in bottomTaskRows" :key="task.id" class="task-row bottom-task-row flex">
            <div class="bg-blue-100 z-10 flex sticky left-0" :style="{ minWidth: `${bottomTaskWidth + bottomExtraColumns.length * extraColumnWidth}px` }">
              <!-- 編集可能なタスク名フィールド -->
              <input
                class="py-2 h-full px-2 border-r border-black text-sm"
                style="width: 80px"
                v-model="task.name"
                @change="updateTaskName(task)"
              />
              <!-- 編集可能なサンプルフィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 80px"
                v-model="task.sample"
                @change="updateTaskSample(task)"
              />
              <!-- 編集可能なPM typeフィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 80px"
                v-model="task.pmType"
                @change="updateTaskPmType(task)"
              />
              <!-- 編集可能な担当者フィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 80px"
                v-model="task.assignee"
                @change="updateTaskAssignee(task)"
              />
              <!-- 編集可能な開始日フィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 80px"
                type="date"
                v-model="task.startDate"
                @change="updateTaskDates(task)"
              />
              <!-- 編集可能な期限日フィールド -->
              <input
                class="py-2 h-full text-center border-r border-black text-sm"
                style="width: 80px"
                type="date"
                v-model="task.endDate"
                @change="updateTaskDates(task)"
              />
              <div v-for="column in bottomExtraColumns" :key="column.key" class="bg-blue-100 text-center border-r border-black text-sm" :style="{ width: `${extraColumnWidth}px` }">
                <input
                  class="py-2 h-full text-center"
                  v-model="task[column.key]"
                  @change="updateBottomTaskAdditional(task, column.key)"
                />
              </div>
            </div>
            <div :style="task.style" class="h-10 flex py-2 will-change-transform cursor-pointer" @mousedown="onMouseDown_MoveStart($event, task, tasks)">
              <div class="w-2 bg-yellow-200 rounded-l-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'left', tasks)"></div>
              <div class="flex-1 bg-yellow-200 pointer-events-none"></div>
              <div class="w-2 bg-yellow-200 rounded-r-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'right', tasks)"></div>
            </div>
          </div>
          <!-- タスク追加ボタン -->
          <button class="mt-2 bg-blue-200 hover:bg-blue-300 text-sm py-1 px-4 rounded" @click="addBottomTask">
            + タスクを追加
          </button>
          <!-- 列追加ボタン -->
          <button class="mt-2 ml-2 bg-blue-300 hover:bg-blue-400 text-sm py-1 px-4 rounded" @click="addBottomTaskColumn">
            + 列を追加
          </button>
          <!-- タスク削除ボタン -->
          <button class="mt-2 ml-2 bg-red-200 hover:bg-red-300 text-sm py-1 px-4 rounded" @click="removeSelectedBottomTasks">
            選択したタスクを削除
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, onUnmounted, computed, ref, reactive } from 'vue';
import dayjs from 'dayjs';  // dayjsをインポート

// ガントチャートのロジックを管理するカスタムフック
const BLOCK_SIZE = 20; // 各日付ブロックの幅
const TOP_TASK_WIDTH = 300; // 上部タスクの固定部分の幅
const BOTTOM_TASK_WIDTH = 480; // 下部タスクの固定部分の幅

// 操作中の状態を管理するリアクティブな変数
const dragging = ref(false); // ドラッグ中のフラグ
const leftResizing = ref(false); // 左側リサイズ中のフラグ
const rightResizing = ref(false); // 右側リサイズ中のフラグ
const target = reactive({
  pageX: 0, // 現在のマウスX座標
  element: null, // 操作対象のDOM要素
  task: null, // 操作対象のタスク
  taskList: null, // 操作対象のタスクリスト
  direction: null, // リサイズの方向
});

// ガントチャートの表示に関する設定
const blockWidth = ref(BLOCK_SIZE); // 各ブロックの幅
const topTaskWidth = ref(TOP_TASK_WIDTH); // 上部タスクの幅
const bottomTaskWidth = ref(BOTTOM_TASK_WIDTH); // 下部タスクの幅
const topViewWidth = ref(0); // 上部ビューの幅
const bottomViewWidth = ref(0); // 下部ビューの幅
const contentWidth = ref(0); // コンテンツ全体の幅
const totalDays = ref(0); // 表示期間の合計日数
const startMonth = ref(dayjs().add(0, 'month').format('YYYY-MM')); // 開始月
const endMonth = ref(dayjs().add(1, 'month').format('YYYY-MM')); // 終了月
const calendars = ref([]); // 月のカレンダー情報
const tasks = ref([]); // タスク情報
const topTasks = ref([]); // 上部のタスク情報
const calendar = ref(null); // 現在のカレンダー要素
const scrollbarOffset = 20; // スクロールバーのオフセット
const taskRowHeight = 40; // タスク行の高さ

// ビューを初期化する関数
function initView() {
  serCalendar(); // カレンダー情報を設定
  totalDays.value = calendars.value.reduce((p, c) => p + c.days.length, 0); // 総日数を計算
  contentWidth.value = totalDays.value * blockWidth.value; // コンテンツ幅を設定
  topViewWidth.value = contentWidth.value; // 上部ビュー幅を設定
  bottomViewWidth.value = contentWidth.value; // 下部ビュー幅を設定
  console.log("View initialized. Top View Width: ", topViewWidth.value, "Bottom View Width: ", bottomViewWidth.value);
  if (calendar.value) {
    // カレンダーがあればスクロールを調整
    calendar.value.scrollLeft = bottomTodayPosition.value - BOTTOM_TASK_WIDTH;
  }
}

// マウス移動に基づいて新しいX座標を計算する関数
function calcMovePositionX(currentPageX) {
  const diff = target.pageX - currentPageX; // 開始位置と現在位置の差分を計算
  return keepThreshold(target.task.pos.x - diff, 0, contentWidth.value - target.task.pos.width); // 閾値を超えないように位置を調整
}

// 指定された月の日付情報を取得する関数
function getDays(startMonth) {
  const dayOfWeek = ['日', '月', '火', '水', '木', '金', '土']; // 曜日リスト
  const days = []; // 日付リスト
  for (let i = 0; i < startMonth.daysInMonth(); i++) {
    const targetDate = startMonth.add(i, 'day'); // 対象日付を計算
    days.push({
      date: targetDate.date(), // 日付を取得
      dayOfWeek: dayOfWeek[targetDate.day()], // 曜日を取得
    });
  }
  return days; // 日付情報を返す
}

// カレンダー情報を設定する関数
function serCalendar() {
  const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得
  const endMonthDate = dayjs(endMonth.value); // 終了月の日付を取得
  const betweenMonth = endMonthDate.diff(startMonthDate, 'month'); // 月の差分を計算
  for (let i = 0; i <= betweenMonth; i++) {
    const targetMonth = startMonthDate.add(i, 'month'); // 対象月を計算
    calendars.value.push({
      title: targetMonth.format('YYYY-MM'), // 月タイトルを設定
      days: getDays(targetMonth), // 日付情報を取得
    });
  }
  console.log("Calendars set: ", calendars.value);
}

// タスクを移動開始する際のマウスダウンイベントハンドラ
function onMouseDown_MoveStart(e, task, taskList) {
  dragging.value = true; // ドラッグ開始フラグをセット
  target.pageX = e.pageX; // 開始時のマウスX座標をセット
  target.element = e.target; // 対象要素をセット
  target.task = task; // 対象タスクをセット
  target.taskList = taskList; // タスクリストをセット

  document.addEventListener('mousemove', onMouseDown_Moving); // マウス移動イベントを登録
  document.addEventListener('mouseup', onMouseDown_MoveStop); // マウスアップイベントを登録
}

// タスク移動中のマウス移動イベントハンドラ
function onMouseDown_Moving(e) {
  if (!dragging.value) return; // ドラッグ中でなければ終了

  const realX = calcMovePositionX(e.pageX); // 新しいX座標を計算
  target.element.style.transform = `translateX(${realX}px)`; // 要素を移動
}

// タスク移動終了時のマウスアップイベントハンドラ
function onMouseDown_MoveStop(e) {
  if (!dragging.value) return; // ドラッグ中でなければ終了

  const realX = calcMovePositionX(e.pageX); // 新しいX座標を計算
  const days = Math.round((target.task.pos.x - realX) / BLOCK_SIZE); // 移動日数を計算

  if (days !== 0) {
    // 移動があればタスクの日付を更新
    const task = target.taskList.find((t) => t.id === target.task.id);
    task.startDate = dayjs(task.startDate).add(-days, 'day').format('YYYY-MM-DD');
    task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
    updateTaskDates(task); // タスクの日付情報を更新
  } else {
    target.element.style.transform = `translateX(${target.task.pos.x}px)`; // 元の位置に戻す
  }

  resetDragState(); // ドラッグ状態をリセット
}

// タスクリサイズ開始時のマウスダウンイベントハンドラ
function onMouseDown_ResizeStart(e, task, direction, taskList) {
  if (direction === 'left') {
    leftResizing.value = true; // 左リサイズフラグをセット
  } else {
    rightResizing.value = true; // 右リサイズフラグをセット
  }
  target.pageX = e.pageX; // 開始時のマウスX座標をセット
  target.element = e.target.parentElement; // 対象要素をセット
  target.task = task; // 対象タスクをセット
  target.direction = direction; // リサイズ方向をセット
  target.taskList = taskList; // タスクリストをセット

  document.addEventListener('mousemove', onMouseDown_Resizing); // マウス移動イベントを登録
  document.addEventListener('mouseup', onMouseDown_ResizeStop); // マウスアップイベントを登録
}

// タスクリサイズ中のマウス移動イベントハンドラ
function onMouseDown_Resizing(e) {
  if (!leftResizing.value && !rightResizing.value) return; // リサイズ中でなければ終了

  const realWidth = calcResizeWidth(e.pageX, target.direction); // 新しい幅を計算
  const realX = target.direction === 'left' ? calcResizePositionX(e.pageX) : target.task.pos.x; // 新しいX座標を計算
  target.element.style.transform = `translateX(${realX}px)`; // 要素を移動
  target.element.style.width = `${realWidth}px`; // 幅を変更
}

// タスクリサイズ終了時のマウスアップイベントハンドラ
function onMouseDown_ResizeStop(e) {
  if (!leftResizing.value && !rightResizing.value) return; // リサイズ中でなければ終了

  const realWidth = calcResizeWidth(e.pageX, target.direction); // 新しい幅を計算
  const days = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE); // リサイズ日数を計算

  if (days !== 0) {
    // リサイズがあればタスクの日付を更新
    const task = target.taskList.find((t) => t.id === target.task.id);
    if (leftResizing.value) {
      task.startDate = dayjs(task.startDate).add(days, 'day').format('YYYY-MM-DD');
    } else {
      task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
    }
    updateTaskDates(task); // タスクの日付情報を更新
  } else {
    target.element.style.transform = `translateX(${target.task.pos.x}px)`; // 元の位置に戻す
    target.element.style.width = `${target.task.pos.width}px`; // 元の幅に戻す
  }

  resetResizeState(); // リサイズ状態をリセット
}

// ドラッグ状態をリセットする関数
function resetDragState() {
  dragging.value = false; // ドラッグ中フラグを解除
  target.element = null; // 対象要素をクリア
  target.task = null; // 対象タスクをクリア
  target.pageX = 0; // マウスX座標をクリア

  document.removeEventListener('mousemove', onMouseDown_Moving); // マウス移動イベントを解除
  document.removeEventListener('mouseup', onMouseDown_MoveStop); // マウスアップイベントを解除
}

// リサイズ状態をリセットする関数
function resetResizeState() {
  leftResizing.value = false; // 左リサイズフラグを解除
  rightResizing.value = false; // 右リサイズフラグを解除
  target.element = null; // 対象要素をクリア
  target.task = null; // 対象タスクをクリア
  target.pageX = 0; // マウスX座標をクリア

  document.removeEventListener('mousemove', onMouseDown_Resizing); // マウス移動イベントを解除
  document.removeEventListener('mouseup', onMouseDown_ResizeStop); // マウスアップイベントを解除
}

// マウス移動に基づいてリサイズのための新しい幅を計算する関数
function calcResizeWidth(currentPageX, direction) {
  const diff = target.pageX - currentPageX; // 開始位置と現在位置の差分を計算
  if (direction === 'left') {
    return keepThreshold(target.task.pos.width + diff, BLOCK_SIZE, target.task.pos.width + target.task.pos.x); // 左リサイズ時の幅を調整
  } else {
    return keepThreshold(target.task.pos.width - diff, BLOCK_SIZE, contentWidth.value - target.task.pos.x); // 右リサイズ時の幅を調整
  }
}

// 値が指定の範囲内に収まるようにする関数
function keepThreshold(value, min, max) {
  if (value <= min) return min; // 最小値を下回らないように調整
  if (value >= max) return max; // 最大値を上回らないように調整
  return value; // 範囲内ならそのまま返す
}

// 曜日に応じた背景色を返す関数
function weekendColor(dayOfWeek) {
  switch (dayOfWeek) {
    case '土':
      return 'bg-blue-100'; // 土曜日の背景色
    case '日':
      return 'bg-red-100'; // 日曜日の背景色
    default:
      return ''; // 平日はデフォルトの背景色
  }
}

// テストデータを生成する関数
function makeTestData() {
  const today = dayjs(); // 今日の日付を取得
  for (let i = 1; i <= 3; i++) {
    // 上部タスクデータを生成
    topTasks.value.push({
      id: i,
      name: `plant - ${i}`,
      startDate: today.format('YYYY-MM-DD'),
      endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD'),
      selected: false, // 初期化時に selected を false に設定
    });
  }
  for (let i = 4; i <= 10; i++) {
    // 下部タスクデータを生成
    tasks.value.push({
      id: i,
      name: `task - ${i}`,
      pmType: `PM-${(i % 3) + 1}`,
      sample: '',
      assignee: '',
      startDate: today.format('YYYY-MM-DD'),
      endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD'),
      selected: false, // 初期化時に selected を false に設定
    });
  }
  console.log("Top Tasks: ", topTasks.value);
  console.log("Bottom Tasks: ", tasks.value);
}

// タスクの日付情報を更新する関数
function updateTaskDates(task) {
  const dateFrom = dayjs(task.startDate); // 開始日を取得
  const dateTo = dayjs(task.endDate); // 終了日を取得
  const between = dateTo.diff(dateFrom, 'day') + 1; // 開始日と終了日の間の日数を計算
  const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得
  const start = dateFrom.diff(startMonthDate, 'day'); // 開始月からの差分日数を計算

  const pos = {
    x: start * BLOCK_SIZE, // 開始位置を計算
    width: BLOCK_SIZE * between, // 幅を計算
  };

  // タスクが正しく見つかっているか確認
  const taskToUpdate = tasks.value.find((t) => t.id === task.id) || topTasks.value.find((t) => t.id === task.id);
  if (taskToUpdate) {
    taskToUpdate.style = taskToUpdate.style || {}; // デフォルトのスタイルオブジェクトを設定
    taskToUpdate.style.width = `${pos.width}px`; // スタイルの幅を設定
    taskToUpdate.style.transform = `translateX(${pos.x}px)`; // スタイルの位置を設定
  } else {
    console.error('Task not found for updating:', task.id); // タスクが見つからない場合にエラーログ
  }
}

// 上部タスクの名前を更新する関数
function updateTopTaskName(task) {
  const taskToUpdate = topTasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
  if (taskToUpdate) {
    taskToUpdate.name = task.name; // タスク名を更新
  }
}

// タスクの名前を更新する関数
function updateTaskName(task) {
  const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
  if (taskToUpdate) {
    taskToUpdate.name = task.name; // タスク名を更新
  }
}

// タスクのPMタイプを更新する関数
function updateTaskPmType(task) {
  const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
  if (taskToUpdate) {
    taskToUpdate.pmType = task.pmType; // PMタイプを更新
  }
}

// タスクの担当者を更新する関数
function updateTaskAssignee(task) {
  const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
  if (taskToUpdate) {
    taskToUpdate.assignee = task.assignee; // 担当者を更新
  }
}

// 今日の日付の上部位置を計算するcomputedプロパティ
const topTodayPosition = computed(() => {
  const today = dayjs(); // 今日の日付を取得
  const startDate = dayjs(startMonth.value); // 開始月の日付を取得
  const diffFuture = today.diff(startDate, 'day'); // 今日と開始日の差分を計算
  return diffFuture >= 0 ? diffFuture * BLOCK_SIZE : -1; // 今日の日付が範囲内の場合に位置を計算
});

// 今日の日付の下部位置を計算するcomputedプロパティ
const bottomTodayPosition = computed(() => {
  const today = dayjs(); // 今日の日付を取得
  const startDate = dayjs(startMonth.value); // 開始月の日付を取得
  const diffFuture = today.diff(startDate, 'day'); // 今日と開始日の差分を計算
  return diffFuture >= 0 ? diffFuture * BLOCK_SIZE : -1; // 今日の日付が範囲内の場合に位置を計算
});

// 上部タスク行を計算するcomputedプロパティ
const topTaskRows = computed(() => {
  const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得

  return topTasks.value.map((task) => {
    const dateFrom = dayjs(task.startDate); // 開始日を取得
    const dateTo = dayjs(task.endDate); // 終了日を取得
    const between = dateTo.diff(dateFrom, 'day') + 1; // 開始日と終了日の間の日数を計算
    const start = dateFrom.diff(startMonthDate, 'day'); // 開始月からの差分日数を計算

    const pos = {
      x: start * BLOCK_SIZE, // 開始位置を計算
      width: BLOCK_SIZE * between, // 幅を計算
    };

    const style = {
      width: `${pos.width}px`, // スタイルの幅を設定
      transform: `translateX(${pos.x}px)`, // スタイルの位置を設定
    };

    return {
      style, // スタイルを返す
      pos, // 位置情報を返す
      ...task, // タスク情報を返す
    };
  });
});

// 下部タスク行を計算するcomputedプロパティ
const bottomTaskRows = computed(() => {
  const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得

  return tasks.value.map((task) => {
    const dateFrom = dayjs(task.startDate); // 開始日を取得
    const dateTo = dayjs(task.endDate); // 終了日を取得
    const between = dateTo.diff(dateFrom, 'day') + 1; // 開始日と終了日の間の日数を計算
    const start = dateFrom.diff(startMonthDate, 'day'); // 開始月からの差分日数を計算

    const pos = {
      x: start * BLOCK_SIZE, // 開始位置を計算
      width: BLOCK_SIZE * between, // 幅を計算
    };

    const style = {
      width: `${pos.width}px`, // スタイルの幅を設定
      transform: `translateX(${pos.x}px)`, // スタイルの位置を設定
    };

    return {
      style, // スタイルを返す
      pos, // 位置情報を返す
      ...task, // タスク情報を返す
    };
  });
});

// コンポーネントの高さを計算
const topChartHeight = computed(() => (topTaskRows.value.length + 1) * taskRowHeight);
const bottomChartHeight = computed(() => (bottomTaskRows.value.length + 1) * taskRowHeight);

// 各入力フィールドの幅を定義
const inputWidths = {
  name: 100,
  startDate: 90,
  endDate: 90,
  sample: 80,
  pmType: 80,
  assignee: 80,
};

// 上部タスクフォームの総幅を計算
const topTaskFormWidth = computed(() => {
  return (
    30 + // チェックボックスの幅
    inputWidths.name +
    inputWidths.startDate +
    inputWidths.endDate +
    topExtraColumns.value.length * extraColumnWidth
  );
});

// 下部タスクフォームの総幅を計算
const bottomTaskFormWidth = computed(() => {
  return (
    30 + // チェックボックスの幅
    inputWidths.name +
    inputWidths.sample +
    inputWidths.pmType +
    inputWidths.assignee +
    inputWidths.startDate +
    inputWidths.endDate +
    bottomExtraColumns.value.length * extraColumnWidth
  );
});

// 追加のタスク列を保持
const topExtraColumns = ref([]);
const bottomExtraColumns = ref([]);

// 追加の列の幅
const extraColumnWidth = 100;

// 上部タスクを追加する関数
function addTopTask() {
  const today = dayjs().format('YYYY-MM-DD');
  const newTask = {
    id: topTasks.value.length + 1,
    name: `new plant ${topTasks.value.length + 1}`,
    startDate: today,
    endDate: dayjs().add(2, 'days').format('YYYY-MM-DD'),
    selected: false,
  };
  topExtraColumns.value.forEach((column) => {
    newTask[column.key] = '';
  });
  topTasks.value.push(newTask);
  updateTaskDates(newTask);
}

// 下部タスクを追加する関数
function addBottomTask() {
  const today = dayjs().format('YYYY-MM-DD');
  const newTask = {
    id: tasks.value.length + 1,
    name: `new task ${tasks.value.length + 1}`,
    sample: '',
    pmType: 'PM-1',
    assignee: '',
    startDate: today,
    endDate: dayjs().add(2, 'days').format('YYYY-MM-DD'),
    selected: false,
  };
  bottomExtraColumns.value.forEach((column) => {
    newTask[column.key] = '';
  });
  tasks.value.push(newTask);
  updateTaskDates(newTask);
}

// 上部タスク列を追加する関数
function addTopTaskColumn() {
  const columnKey = `extra${topExtraColumns.value.length + 1}`;
  topExtraColumns.value.push({ key: columnKey, label: `追加${topExtraColumns.value.length + 1}` });

  // 既存のタスクに新しい列を追加
  topTasks.value.forEach((task) => {
    task[columnKey] = '';
  });
}

// 下部タスク列を追加する関数
function addBottomTaskColumn() {
  const columnKey = `extra${bottomExtraColumns.value.length + 1}`;
  bottomExtraColumns.value.push({ key: columnKey, label: `追加${bottomExtraColumns.value.length + 1}` });

  // 既存のタスクに新しい列を追加
  tasks.value.forEach((task) => {
    task[columnKey] = '';
  });
}

// 上部タスクの追加プロパティを更新する関数
function updateTopTaskAdditional(task, key) {
  const taskToUpdate = topTasks.value.find((t) => t.id === task.id);
  if (taskToUpdate) {
    taskToUpdate[key] = task[key];
  }
}

// 下部タスクの追加プロパティを更新する関数
function updateBottomTaskAdditional(task, key) {
  const taskToUpdate = tasks.value.find((t) => t.id === task.id);
  if (taskToUpdate) {
    taskToUpdate[key] = task[key];
  }
}

// 上部タスクの削除関数
function removeSelectedTopTasks() {
  console.log('Removing selected top tasks...');
  topTasks.value.forEach((task) => {
    console.log(`Before Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
  });
  
  const beforeCount = topTasks.value.length;
  topTasks.value = topTasks.value.filter((task) => !task.selected); // selected が true のタスクを削除
  
  topTasks.value.forEach((task) => {
    console.log(`After Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
  });
  
  const afterCount = topTasks.value.length;
  console.log(`Removed ${beforeCount - afterCount} top tasks.`);
  topTasks.value.forEach(updateTaskDates); // 削除後にタスクの日付情報を更新
}

// 下部タスクの削除関数
function removeSelectedBottomTasks() {
  console.log('Removing selected bottom tasks...');
  tasks.value.forEach((task) => {
    console.log(`Before Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
  });

  const beforeCount = tasks.value.length;
  tasks.value = tasks.value.filter((task) => !task.selected); // selected が true のタスクを削除
  
  tasks.value.forEach((task) => {
    console.log(`After Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
  });

  const afterCount = tasks.value.length;
  console.log(`Removed ${beforeCount - afterCount} bottom tasks.`);
  tasks.value.forEach(updateTaskDates); // 削除後にタスクの日付情報を更新
}

onMounted(() => {
  initView();
  makeTestData();
});

onUnmounted(() => {
  resetDragState(); // ドラッグ状態のリセット
  resetResizeState(); // リサイズ状態のリセット
});
</script>










<style scoped>
/* 各タスク行の高さを固定し、余白を増やす */
.top-task-row,
.bottom-task-row {
  height: 50px; /* ガントチャートのタスク行の高さを維持 */
  border-bottom: 2px solid black; /* 黒い下線を追加 */
}

/* ガントチャート全体のサイズを調整 */
#gantt-container {
  min-width: 1200px; /* コンテナの最小幅を1200pxに設定 */
  min-height: 1000px; /* コンテナの最小高さを1000pxに設定 */
  max-width: 100%; /* コンテナの最大幅を100%に設定 */
  padding: 40px; /* 全体にパディングを追加 */
}

/* 上部ガントチャートのスタイル */
.gantt-chart-wrapper.top-chart {
  margin-bottom: 100px; /* 下部ガントチャートとの間にさらにスペースを確保 */
  background-color: #f9f9f9; /* 背景色を設定 */
  border-radius: 8px; /* 角を丸く */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 影を追加 */
  padding-bottom: 50px; /* ボタンが重ならないように下に余白を追加 */
}

/* 下部ガントチャートのスタイル */
.gantt-chart-wrapper.bottom-chart {
  background-color: #f9f9f9; /* 背景色を設定 */
  border-radius: 8px; /* 角を丸く */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 影を追加 */
  margin-top: 60px; /* 上部ガントチャートからの余白を増やす */
}

/* ボタンの間隔とスタイルを確保 */
button {
  display: inline-block;
  margin-top: 30px; /* ボタンの上部にマージンを追加 */
  margin-right: 20px; /* ボタン間にマージンを追加 */
  padding: 12px 18px; /* パディングを設定 */
  background-color: #e0e0e0; /* 背景色を設定 */
  border: none; /* ボーダーを消去 */
  border-radius: 4px; /* 角を丸く */
  cursor: pointer; /* カーソルをポインターに */
  transition: background-color 0.3s; /* 背景色のトランジション */
}

button:hover {
  background-color: #d0d0d0; /* ホバー時の背景色を変更 */
}

/* カーソルスタイル */
.cursor-col-resize {
  cursor: col-resize; /* 列幅変更のカーソル */
}

.cursor-pointer {
  cursor: pointer; /* ハンドカーソル */
}

/* ヘッダーのスタイル */
.top-header,
.bottom-header {
  background-color: #f0f0f0; /* 背景色を設定 */
  z-index: 10; /* 他の要素の上に表示 */
}

/* 入力フィールドのスタイル */
input[type="text"],
input[type="date"] {
  border: 1px solid #ccc; /* ボーダーの色を設定 */
  border-radius: 4px; /* 角を丸く */
  padding: 4px 8px; /* パディングを設定 */
  transition: border-color 0.3s; /* ボーダー色のトランジション */
}

input[type="text"]:focus,
input[type="date"]:focus {
  border-color: #007bff; /* フォーカス時のボーダー色を変更 */
}

/* スクロールバーのスタイル */
#top-calendar::-webkit-scrollbar,
#bottom-calendar::-webkit-scrollbar {
  height: 10px; /* スクロールバーの高さ */
}

#top-calendar::-webkit-scrollbar-thumb,
#bottom-calendar::-webkit-scrollbar-thumb {
  background-color: #cccccc; /* スクロールバーの色 */
  border-radius: 10px; /* スクロールバーの角を丸く */
}

#top-calendar::-webkit-scrollbar-track,
#bottom-calendar::-webkit-scrollbar-track {
  background-color: #f0f0f0; /* スクロールトラックの色 */
}
</style>
