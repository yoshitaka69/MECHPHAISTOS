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
import { onMounted, onUnmounted, computed, ref, reactive } from 'vue'; // ライフサイクルフックをインポート
import useGanttChart from './GanttChartPlugin.ts'; // プラグインをインポート
import './GanttChartStyles.css'; // スタイルをインポート

// プラグインを利用して状態と関数を取得
const {
  BLOCK_SIZE,
  dragging,
  leftResizing,
  rightResizing,
  target,
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
  taskRowHeight,
  topExtraColumns,
  bottomExtraColumns,
  extraColumnWidth,
  initView,
  calcMovePositionX,
  serCalendar,
  onMouseDown_MoveStart,
  onMouseDown_Moving,
  onMouseDown_MoveStop,
  onMouseDown_ResizeStart,
  onMouseDown_Resizing,
  onMouseDown_ResizeStop,
  resetDragState,
  resetResizeState,
  calcResizeWidth,
  keepThreshold,
  weekendColor,
  makeTestData,
  updateTaskDates,
  updateTopTaskName,
  updateTaskName,
  updateTaskPmType,
  updateTaskAssignee,
  topTodayPosition,
  bottomTodayPosition,
  topTaskRows,
  bottomTaskRows,
  topChartHeight,
  bottomChartHeight,
  inputWidths,
  topTaskFormWidth,
  bottomTaskFormWidth,
  addTopTask,
  addBottomTask,
  addTopTaskColumn,
  addBottomTaskColumn,
  updateTopTaskAdditional,
  updateBottomTaskAdditional,
  removeSelectedTopTasks,
  removeSelectedBottomTasks,
} = useGanttChart();

onMounted(() => {
  initView();
  makeTestData();
});

onUnmounted(() => {
  resetDragState();
  resetResizeState();
});

</script>
