<template>
    <div id="gantt" class="flex">
      <div id="gantt-chart-container" ref="calendar" class="overflow-auto h-screen w-screen select-none">
        <div id="header" class="top-0 flex z-20 sticky" :style="{ width: `${viewWidth}px` }">
          <div class="border-b border-black bg-green-100 flex sticky left-0 top-0" :style="{ minWidth: `${taskWidth}px` }">
            <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px">タスク</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">開始日</div>
            <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">期限日</div>
          </div>
          <template v-for="month in calendars" :key="month.title">
            <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days}px` }">
              <div class="border-b border-r border-black px-2">{{ month.title }}</div>
              <div class="flex">
                <div
                  v-for="day in month.days"
                  :key="day.date"
                  class="border-r border-black text-xs text-center"
                  :class="weekendColor(day.dayOfWeek)"
                  :style="{ minWidth: `${blockWidth}px` }"
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
                  :style="{ minWidth: `${blockWidth}px` }"
                >
                  {{ day.dayOfWeek }}
                </div>
              </div>
            </div>
          </template>
        </div>
        <div id="contents" class="relative" :style="{ width: `${viewWidth}px` }">
          <div v-for="i in totalDays" :key="i" class="absolute bg-gray-200 h-full w-px" :style="{ left: `${i * blockWidth + taskWidth - 1}px` }"></div>
          <div v-if="todayPosition >= 0" class="absolute bg-red-300 h-full" :style="{ width: `${blockWidth - 1}px`, left: `${todayPosition}px` }"></div>
          <div v-for="task in taskRows" :key="task.id" class="h-10 border-b border-black flex">
            <div class="bg-green-100 z-10 flex sticky left-0" :style="{ minWidth: `${taskWidth}px` }">
              <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px">{{ task.name }}</div>
              <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">{{ task.startDate }}</div>
              <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">{{ task.endDate }}</div>
            </div>
            <div :style="task.style" class="h-10 flex py-2 will-change-transform" @mousedown="onMouseDown_MoveStart($event, task)">
              <div class="w-2 bg-yellow-200 rounded-l-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'left')"></div>
              <div class="flex-1 bg-yellow-200 pointer-events-none"></div>
              <div class="w-2 bg-yellow-200 rounded-r-lg cursor-col-resize" @mousedown.stop="onMouseDown_ResizeStart($event, task, 'right')"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, onUnmounted, reactive, computed } from 'vue';
  import dayjs from 'dayjs';
  
  const BLOCK_SIZE = 20;
  const TASK_WIDTH = 300;
  
  export default {
    name: 'GanttChart',
    setup() {
      const dragging = ref(false);
      const leftResizing = ref(false);
      const rightResizing = ref(false);
      const target = reactive({
        pageX: 0,
        element: null,
        task: null,
      });
  
      const blockWidth = ref(BLOCK_SIZE);
      const taskWidth = ref(TASK_WIDTH);
      const viewWidth = ref(0);
      const contentWidth = ref(0);
      const totalDays = ref(0);
      const startMonth = ref(dayjs().add(0, 'month').format('YYYY-MM'));
      const endMonth = ref(dayjs().add(1, 'month').format('YYYY-MM'));
      const calendars = ref([]);
      const tasks = ref([]);
      const calendar = ref(null);
  
      onMounted(() => {
        initView();
        makeTestData();
        document.addEventListener('mousemove', onMouseDown_Moving);
        document.addEventListener('mouseup', onMouseDown_MoveStop);
        document.addEventListener('mousemove', onMouseDown_Resizing);
        document.addEventListener('mouseup', onMouseDown_ResizeStop);
      });
  
      onUnmounted(() => {
        document.removeEventListener('mousemove', onMouseDown_Moving);
        document.removeEventListener('mouseup', onMouseDown_MoveStop);
        document.removeEventListener('mousemove', onMouseDown_Resizing);
        document.removeEventListener('mouseup', onMouseDown_ResizeStop);
      });
  
      const taskRows = computed(() => {
        const startMonthDate = dayjs(startMonth.value);
        const endMonthDate = dayjs(endMonth.value);
  
        return tasks.value.map((task) => {
          const dateFrom = dayjs(task.startDate);
          const dateTo = dayjs(task.endDate);
          const between = dateTo.diff(dateFrom, 'day') + 1;
          const start = dateFrom.diff(startMonthDate, 'day');
          const end = endMonthDate.diff(dateTo, 'day') + endMonthDate.daysInMonth();
  
          const pos = {
            x: start * BLOCK_SIZE,
            width: BLOCK_SIZE * between,
          };
  
          const style = {
            width: `${pos.width}px`,
            transform: `translateX(${pos.x}px)`,
          };
  
          const isHidden = !(start >= 0 && end > 0);
          if (isHidden) {
            style.display = 'none';
          }
  
          return {
            style,
            pos,
            isHidden,
            ...task,
          };
        });
      });
  
      const todayPosition = computed(() => {
        const today = dayjs();
        const startDate = dayjs(startMonth.value);
        const endDate = dayjs(endMonth.value);
        const diffFuture = today.diff(startDate, 'day');
        const diffPast = endDate.diff(today, 'day') + endDate.daysInMonth();
        return diffFuture >= 0 && diffPast > 0 ? diffFuture * BLOCK_SIZE + TASK_WIDTH : -1;
      });
  
      function initView() {
        serCalendar();
        totalDays.value = calendars.value.reduce((p, c) => p + c.days.length, 0);
        contentWidth.value = totalDays.value * blockWidth.value;
        viewWidth.value = taskWidth.value + contentWidth.value;
        calendar.value.scrollLeft = todayPosition.value - TASK_WIDTH;
      }
  
      function getDays(startMonth) {
        const dayOfWeek = ['日', '月', '火', '水', '木', '金', '土'];
        const days = [];
        for (let i = 0; i < startMonth.daysInMonth(); i++) {
          const targetDate = startMonth.add(i, 'day');
          days.push({
            date: targetDate.date(),
            dayOfWeek: dayOfWeek[targetDate.day()],
          });
        }
        return days;
      }
  
      function serCalendar() {
        const startMonthDate = dayjs(startMonth.value);
        const endMonthDate = dayjs(endMonth.value);
        const betweenMonth = endMonthDate.diff(startMonthDate, 'month');
        for (let i = 0; i <= betweenMonth; i++) {
          const targetMonth = startMonthDate.add(i, 'month');
          calendars.value.push({
            title: targetMonth.format('YYYY-MM'),
            days: getDays(targetMonth),
          });
        }
      }
  
      function onMouseDown_MoveStart(e, task) {
        dragging.value = true;
        target.pageX = e.pageX;
        target.element = e.target;
        target.task = task;
      }
  
      function onMouseDown_Moving(e) {
        if (!dragging.value) return;
  
        const realX = calcMovePositionX(e.pageX);
        target.element.style.transform = `translateX(${realX}px)`;
      }
  
      function onMouseDown_MoveStop(e) {
        if (!dragging.value) return;
        const realX = calcMovePositionX(e.pageX);
        const days = Math.round((target.task.pos.x - realX) / BLOCK_SIZE);
  
        if (days !== 0) {
          const task = tasks.value.find((t) => t.id === target.task.id);
          task.startDate = dayjs(task.startDate).add(-days, 'day').format('YYYY-MM-DD');
          task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
        } else {
          target.element.style.transform = `translateX(${target.task.pos.x}px)`;
        }
  
        dragging.value = false;
        target.element = null;
        target.task = null;
        target.pageX = 0;
      }
  
      function onMouseDown_ResizeStart(e, task, direction) {
        if (direction === 'left') {
          leftResizing.value = true;
        } else {
          rightResizing.value = true;
        }
        target.pageX = e.pageX;
        target.element = e.target.parentElement;
        target.task = task;
      }
  
      function onMouseDown_Resizing(e) {
        if (leftResizing.value) {
          const realX = calcResizePositionX(e.pageX);
          const realWidth = calcLeftResizeWidth(e.pageX);
          target.element.style.transform = `translateX(${realX}px)`;
          target.element.style.width = `${realWidth}px`;
        }
  
        if (rightResizing.value) {
          const realWidth = calcRightResizeWidth(e.pageX);
          target.element.style.width = `${realWidth}px`;
        }
      }
  
      function onMouseDown_ResizeStop(e) {
        if (leftResizing.value) {
          const realX = calcResizePositionX(e.pageX);
          const days = Math.round((target.task.pos.x - realX) / BLOCK_SIZE);
  
          if (days !== 0) {
            const task = tasks.value.find((t) => t.id === target.task.id);
            task.startDate = dayjs(task.startDate).add(-days, 'day').format('YYYY-MM-DD');
          } else {
            target.element.style.transform = `translateX(${target.task.pos.x}px)`;
            target.element.style.width = `${target.task.pos.width}px`;
          }
        }
  
        if (rightResizing.value) {
          const realWidth = calcRightResizeWidth(e.pageX);
          const days = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE);
  
          if (days !== 0) {
            const task = tasks.value.find((t) => t.id === target.task.id);
            task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
          } else {
            target.element.style.width = `${target.task.pos.width}px`;
          }
        }
  
        leftResizing.value = false;
        rightResizing.value = false;
        target.element = null;
        target.task = null;
        target.pageX = 0;
      }
  
      function calcMovePositionX(currentPageX) {
        const diff = target.pageX - currentPageX;
        return keepThreshold(target.task.pos.x - diff, 0, contentWidth.value - target.task.pos.width);
      }
  
      function calcResizePositionX(currentPageX) {
        const diff = target.pageX - currentPageX;
        return keepThreshold(target.task.pos.x - diff, 0, target.task.pos.x + target.task.pos.width - BLOCK_SIZE);
      }
  
      function calcLeftResizeWidth(currentPageX) {
        const diff = target.pageX - currentPageX;
        return keepThreshold(target.task.pos.width + diff, BLOCK_SIZE, target.task.pos.width + target.task.pos.x);
      }
  
      function calcRightResizeWidth(currentPageX) {
        const diff = target.pageX - currentPageX;
        return keepThreshold(target.task.pos.width - diff, BLOCK_SIZE, contentWidth.value - target.task.pos.x);
      }
  
      function keepThreshold(value, min, max) {
        if (value <= min) return min;
        if (value >= max) return max;
        return value;
      }
  
      function weekendColor(dayOfWeek) {
        switch (dayOfWeek) {
          case '土':
            return 'bg-blue-100';
          case '日':
            return 'bg-red-100';
          default:
            return '';
        }
      }
  
      function makeTestData() {
        const today = dayjs();
        for (let i = 1; i <= 100; i++) {
          tasks.value.push({
            id: i,
            name: `task - ${i}`,
            startDate: today.format('YYYY-MM-DD'),
            endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD'),
          });
        }
      }
  
      return {
        dragging,
        leftResizing,
        rightResizing,
        target,
        blockWidth,
        taskWidth,
        viewWidth,
        contentWidth,
        totalDays,
        startMonth,
        endMonth,
        calendars,
        tasks,
        calendar,
        taskRows,
        todayPosition,
        initView,
        getDays,
        serCalendar,
        onMouseDown_MoveStart,
        onMouseDown_Moving,
        onMouseDown_MoveStop,
        onMouseDown_ResizeStart,
        onMouseDown_Resizing,
        onMouseDown_ResizeStop,
        calcMovePositionX,
        calcResizePositionX,
        calcLeftResizeWidth,
        calcRightResizeWidth,
        keepThreshold,
        weekendColor,
        makeTestData,
      };
    },
  };
  </script>
  
  <style>
  .tables-container {
    display: flex;
    justify-content: space-between;
  }
  #totalCostTable, #monthlyCostTable {
    width: 48%;
  }
  </style>
  