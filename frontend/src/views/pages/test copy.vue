<template>
  <div id="gantt" class="space-y-4">
    <!-- 上部のガントチャート -->
    <div class="gantt-chart-wrapper top-chart">
      <div id="gantt-chart-container-1" class="overflow-auto h-56 w-full select-none bg-white">
        <div id="top-header" class="top-0 flex z-20 sticky" :style="{ width: `${topViewWidth}px` }">
          <div class="border-b border-black bg-green-100 flex sticky left-0 top-0" :style="{ minWidth: `${topTaskWidth}px` }">
            <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 100px">Plant</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">開始日</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">期限日</div>
          </div>
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
        <div id="top-contents" class="relative overflow-y-auto" :style="{ width: `${topViewWidth}px`, height: 'calc(100vh - 6rem)' }">
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
            <div class="bg-green-100 z-10 flex sticky left-0" :style="{ minWidth: `${topTaskWidth}px` }">
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
            </div>
            <div :style="task.style" class="h-10 flex py-2 will-change-transform cursor-pointer" @mousedown="onMouseDown_MoveStart($event, task, topTasks)">
              <div class="w-2 bg-yellow-200 rounded-l-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'left', topTasks)"></div>
              <div class="flex-1 bg-yellow-200 pointer-events-none"></div>
              <div class="w-2 bg-yellow-200 rounded-r-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'right', topTasks)"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 下部のガントチャート -->
    <div class="gantt-chart-wrapper bottom-chart">
      <div id="gantt-chart-container-2" class="overflow-auto h-56 w-full select-none bg-white">
        <div id="bottom-header" class="top-0 flex z-20 sticky" :style="{ width: `${bottomViewWidth}px` }">
          <div class="border-b border-black bg-blue-100 flex sticky left-0 top-0" :style="{ minWidth: `${bottomTaskWidth}px` }">
            <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 80px">タスク</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">サンプル</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">PM type</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">担当者</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">開始日</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 80px">期限日</div>
          </div>
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
        <div id="bottom-contents" class="relative overflow-y-auto" :style="{ width: `${bottomViewWidth}px`, height: 'calc(100vh - 6rem)' }">
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
            <div class="bg-blue-100 z-10 flex sticky left-0" :style="{ minWidth: `${bottomTaskWidth}px` }">
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
            </div>
            <div :style="task.style" class="h-10 flex py-2 will-change-transform cursor-pointer" @mousedown="onMouseDown_MoveStart($event, task, tasks)">
              <div class="w-2 bg-yellow-200 rounded-l-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'left', tasks)"></div>
              <div class="flex-1 bg-yellow-200 pointer-events-none"></div>
              <div class="w-2 bg-yellow-200 rounded-r-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'right', tasks)"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>






<script>
import { onMounted, onUnmounted } from "vue";
import { useGanttChart } from "./ganttChartPlugin.js";

export default {
  name: "GanttChart",
  setup() {
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
      updateTaskAssignee, // 担当者更新用関数をインポート
      makeTestData, // makeTestData をインポート
      scrollbarOffset,
      taskRowHeight,
      weekendColor,
    } = useGanttChart();

    onMounted(() => {
      initView();
      makeTestData();
    });

    onUnmounted(() => {
      resetDragState();
      resetResizeState();
    });

    return {
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
      onMouseDown_MoveStart,
      onMouseDown_ResizeStart,
      updateTaskDates,
      updateTopTaskName,
      updateTaskName,
      updateTaskPmType,
      updateTaskAssignee, // ここで使用する
      scrollbarOffset,
      taskRowHeight,
      weekendColor,
    };
  },
};
</script>

<style>
.tables-container {
  display: flex;
  justify-content: space-between;
}
#totalCostTable,
#monthlyCostTable {
  width: 48%;
}

.top-task-row {
  height: 40px; /* 上部ガントチャートのタスク行の高さ */
  border-bottom: 2px solid black; /* 黒い下線を追加 */
}

.bottom-task-row {
  height: 40px; /* 下部ガントチャートのタスク行の高さ */
  border-bottom: 2px solid black; /* 黒い下線を追加 */
}

.cursor-col-resize {
  cursor: col-resize; /* 列幅変更のカーソル */
}

.cursor-pointer {
  cursor: pointer; /* ハンドカーソル */
}

.top-chart .gantt-chart-wrapper {
  width: 100%;
}

.bottom-chart .gantt-chart-wrapper {
  width: 100%;
}
</style>
