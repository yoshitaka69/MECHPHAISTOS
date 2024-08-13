<template>
  <div id="gantt" class="space-y-4">
    <!-- 上部のガントチャート -->
    <div class="gantt-chart-wrapper top-chart" :style="{ height: `${topChartHeight}px` }">
      <div id="gantt-chart-container-1" class="overflow-auto w-full select-none bg-white">
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
              <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days}px` }">
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
        <div id="top-contents" class="relative overflow-y-auto" :style="{ width: `${topViewWidth + topExtraColumns.length * extraColumnWidth}px` }">
          <!-- 縦のグリッド線を表示 -->
          <div
            v-for="i in totalDays"
            :key="i"
            class="absolute bg-gray-200"
            :style="{ left: `${i * blockWidth + topTaskWidth}px`, top: 0, height: `${topTaskRows.length * taskRowHeight}px`, width: '1px' }"
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
        </div>
      </div>
    </div>

    <!-- 下部のガントチャート -->
    <div class="gantt-chart-wrapper bottom-chart mt-4" :style="{ height: `${bottomChartHeight}px` }">
      <div id="gantt-chart-container-2" class="overflow-auto w-full select-none bg-white">
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
              <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days}px` }">
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
        <div id="bottom-contents" class="relative overflow-y-auto" :style="{ width: `${bottomViewWidth + bottomExtraColumns.length * extraColumnWidth}px` }">
          <!-- 縦のグリッド線を表示 -->
          <div
            v-for="i in totalDays"
            :key="i"
            class="absolute bg-gray-200"
            :style="{ left: `${i * blockWidth + bottomTaskWidth}px`, top: 0, height: `${bottomTaskRows.length * taskRowHeight}px`, width: '1px' }"
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
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, onUnmounted, computed, ref } from 'vue';
import { useGanttChart } from './GanttChartPlugin.js';
import dayjs from 'dayjs';  // dayjsをインポート

// useGanttChartから必要な関数やデータを取得
const {
  dragging,
  leftResizing,
  rightResizing,
  blockWidth,
  topTaskWidth,
  bottomTaskWidth,
  topViewWidth,
  bottomViewWidth,
  contentWidth,
  totalDays,
  startMonth,
  endMonth,
  calendars,
  tasks,
  topTasks,
  calendar,
  topTaskRows,
  bottomTaskRows,
  topTodayPosition,
  bottomTodayPosition,
  initView,
  getDays,
  serCalendar,
  onMouseDown_MoveStart,
  onMouseDown_ResizeStart,
  updateTaskDates,
  updateTopTaskName,
  updateTaskName,
  updateTaskPmType,
  updateTaskAssignee,
  makeTestData,
  scrollbarOffset,
  taskRowHeight,
  weekendColor,
  resetDragState, // 追加: ドラッグ状態のリセット関数
  resetResizeState // 追加: リサイズ状態のリセット関数
} = useGanttChart();

onMounted(() => {
  initView();
  makeTestData();
});

onUnmounted(() => {
  resetDragState(); // ドラッグ状態のリセット
  resetResizeState(); // リサイズ状態のリセット
});

// コンポーネントの高さを計算
const topChartHeight = computed(() => (topTaskRows.length + 1) * taskRowHeight);
const bottomChartHeight = computed(() => (bottomTaskRows.length + 1) * taskRowHeight);

// 追加のタスク列を保持
const topExtraColumns = ref([]);
const bottomExtraColumns = ref([]);

// 追加の列の幅
const extraColumnWidth = 100;

// 上部タスクを追加する関数
function addTopTask() {
  const today = dayjs().format("YYYY-MM-DD");
  const newTask = {
    id: topTasks.value.length + 1,
    name: `new plant ${topTasks.value.length + 1}`,
    startDate: today,
    endDate: dayjs().add(2, "days").format("YYYY-MM-DD")
  };
  topExtraColumns.value.forEach(column => {
    newTask[column.key] = '';
  });
  topTasks.value.push(newTask);
  updateTaskDates(newTask);
}

// 下部タスクを追加する関数
function addBottomTask() {
  const today = dayjs().format("YYYY-MM-DD");
  const newTask = {
    id: tasks.value.length + 1,
    name: `new task ${tasks.value.length + 1}`,
    sample: '',
    pmType: 'PM-1',
    assignee: '',
    startDate: today,
    endDate: dayjs().add(2, "days").format("YYYY-MM-DD")
  };
  bottomExtraColumns.value.forEach(column => {
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
  topTasks.value.forEach(task => {
    task[columnKey] = '';
  });
}

// 下部タスク列を追加する関数
function addBottomTaskColumn() {
  const columnKey = `extra${bottomExtraColumns.value.length + 1}`;
  bottomExtraColumns.value.push({ key: columnKey, label: `追加${bottomExtraColumns.value.length + 1}` });

  // 既存のタスクに新しい列を追加
  tasks.value.forEach(task => {
    task[columnKey] = '';
  });
}

// 上部タスクの追加プロパティを更新する関数
function updateTopTaskAdditional(task, key) {
  const taskToUpdate = topTasks.value.find(t => t.id === task.id);
  if (taskToUpdate) {
    taskToUpdate[key] = task[key];
  }
}

// 下部タスクの追加プロパティを更新する関数
function updateBottomTaskAdditional(task, key) {
  const taskToUpdate = tasks.value.find(t => t.id === task.id);
  if (taskToUpdate) {
    taskToUpdate[key] = task[key];
  }
}

</script>

<style scoped>
.tables-container {
  display: flex;
  justify-content: space-between;
}

#totalCostTable,
#monthlyCostTable {
  width: 48%;
}

.top-task-row,
.bottom-task-row {
  height: 40px; /* ガントチャートのタスク行の高さ */
  border-bottom: 2px solid black; /* 黒い下線を追加 */
}

.cursor-col-resize {
  cursor: col-resize; /* 列幅変更のカーソル */
}

.cursor-pointer {
  cursor: pointer; /* ハンドカーソル */
}

.top-chart .gantt-chart-wrapper,
.bottom-chart .gantt-chart-wrapper {
  width: 100%;
  /* ここに余白を追加 */
}

.bottom-chart {
  margin-top: 16px; /* 上下のガントチャート間に16pxの余白を追加 */
}

button {
  display: inline-block;
  margin-top: 8px; /* ボタンの上部にマージンを追加 */
  margin-right: 8px; /* ボタン間にマージンを追加 */
}
</style>
