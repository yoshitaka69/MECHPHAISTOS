// GanttChartPlugin.ts
import { ref, reactive, computed } from 'vue';
import dayjs from 'dayjs';  // dayjsをインポート

export default function useGanttChart() {
  const BLOCK_SIZE = 20; // 各日付ブロックの幅
  const TOP_TASK_WIDTH = 300; // 上部タスクの固定部分の幅
  const BOTTOM_TASK_WIDTH = 480; // 下部タスクの固定部分の幅

  const dragging = ref(false); // ドラッグ中のフラグ
  const leftResizing = ref(false); // 左側リサイズ中のフラグ
  const rightResizing = ref(false); // 右側リサイズ中のフラグ
  const target = reactive({
    pageX: 0,
    element: null,
    task: null,
    taskList: null,
    direction: null,
  });

  const blockWidth = ref(BLOCK_SIZE);
  const topTaskWidth = ref(TOP_TASK_WIDTH);
  const bottomTaskWidth = ref(BOTTOM_TASK_WIDTH);
  const topViewWidth = ref(0);
  const bottomViewWidth = ref(0);
  const contentWidth = ref(0);
  const totalDays = ref(0);
  const startMonth = ref(dayjs().add(0, 'month').format('YYYY-MM'));
  const endMonth = ref(dayjs().add(1, 'month').format('YYYY-MM'));
  const calendars = ref([]);
  const tasks = ref([]);
  const topTasks = ref([]);
  const calendar = ref(null);
  const taskRowHeight = 40;
  const extraColumnWidth = 100;

  const topExtraColumns = ref([]);
  const bottomExtraColumns = ref([]);

  function initView() {
    serCalendar();
    totalDays.value = calendars.value.reduce((p, c) => p + c.days.length, 0);
    contentWidth.value = totalDays.value * blockWidth.value;
    topViewWidth.value = contentWidth.value;
    bottomViewWidth.value = contentWidth.value;
    console.log('View initialized. Top View Width: ', topViewWidth.value, 'Bottom View Width: ', bottomViewWidth.value);
    if (calendar.value) {
      calendar.value.scrollLeft = bottomTodayPosition.value - BOTTOM_TASK_WIDTH;
    }
  }

  function calcMovePositionX(currentPageX) {
    const diff = target.pageX - currentPageX;
    return keepThreshold(target.task.pos.x - diff, 0, contentWidth.value - target.task.pos.width);
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
    console.log('Calendars set: ', calendars.value);
  }

  function onMouseDown_MoveStart(e, task, taskList) {
    dragging.value = true;
    target.pageX = e.pageX;
    target.element = e.target;
    target.task = task;
    target.taskList = taskList;

    document.addEventListener('mousemove', onMouseDown_Moving);
    document.addEventListener('mouseup', onMouseDown_MoveStop);
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
      const task = target.taskList.find((t) => t.id === target.task.id);
      task.startDate = dayjs(task.startDate).add(-days, 'day').format('YYYY-MM-DD');
      task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
      updateTaskDates(task);
    } else {
      target.element.style.transform = `translateX(${target.task.pos.x}px)`;
    }

    resetDragState();
  }

  function onMouseDown_ResizeStart(e, task, direction, taskList) {
    if (direction === 'left') {
      leftResizing.value = true;
    } else {
      rightResizing.value = true;
    }
    target.pageX = e.pageX;
    target.element = e.target.parentElement;
    target.task = task;
    target.direction = direction;
    target.taskList = taskList;

    document.addEventListener('mousemove', onMouseDown_Resizing);
    document.addEventListener('mouseup', onMouseDown_ResizeStop);
  }

  function onMouseDown_Resizing(e) {
    if (!leftResizing.value && !rightResizing.value) return;

    const realWidth = calcResizeWidth(e.pageX, target.direction);
    const realX = target.direction === 'left' ? calcResizePositionX(e.pageX) : target.task.pos.x;
    target.element.style.transform = `translateX(${realX}px)`;
    target.element.style.width = `${realWidth}px`;
  }

  function onMouseDown_ResizeStop(e) {
    if (!leftResizing.value && !rightResizing.value) return;

    const realWidth = calcResizeWidth(e.pageX, target.direction);
    const days = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE);

    if (days !== 0) {
      const task = target.taskList.find((t) => t.id === target.task.id);
      if (leftResizing.value) {
        task.startDate = dayjs(task.startDate).add(days, 'day').format('YYYY-MM-DD');
      } else {
        task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
      }
      updateTaskDates(task);
    } else {
      target.element.style.transform = `translateX(${target.task.pos.x}px)`;
      target.element.style.width = `${target.task.pos.width}px`;
    }

    resetResizeState();
  }

  function resetDragState() {
    dragging.value = false;
    target.element = null;
    target.task = null;
    target.pageX = 0;

    document.removeEventListener('mousemove', onMouseDown_Moving);
    document.removeEventListener('mouseup', onMouseDown_MoveStop);
  }

  function resetResizeState() {
    leftResizing.value = false;
    rightResizing.value = false;
    target.element = null;
    target.task = null;
    target.pageX = 0;

    document.removeEventListener('mousemove', onMouseDown_Resizing);
    document.removeEventListener('mouseup', onMouseDown_ResizeStop);
  }

  function calcResizeWidth(currentPageX, direction) {
    const diff = target.pageX - currentPageX;
    if (direction === 'left') {
      return keepThreshold(target.task.pos.width + diff, BLOCK_SIZE, target.task.pos.width + target.task.pos.x);
    } else {
      return keepThreshold(target.task.pos.width - diff, BLOCK_SIZE, contentWidth.value - target.task.pos.x);
    }
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
    for (let i = 1; i <= 3; i++) {
      topTasks.value.push({
        id: i,
        name: `plant - ${i}`,
        startDate: today.format('YYYY-MM-DD'),
        endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD'),
        selected: false,
      });
    }
    for (let i = 4; i <= 10; i++) {
      tasks.value.push({
        id: i,
        name: `task - ${i}`,
        pmType: `PM-${(i % 3) + 1}`,
        sample: '',
        assignee: '',
        startDate: today.format('YYYY-MM-DD'),
        endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD'),
        selected: false,
      });
    }
    console.log('Top Tasks: ', topTasks.value);
    console.log('Bottom Tasks: ', tasks.value);
  }

  function updateTaskDates(task) {
    const dateFrom = dayjs(task.startDate);
    const dateTo = dayjs(task.endDate);
    const between = dateTo.diff(dateFrom, 'day') + 1;
    const startMonthDate = dayjs(startMonth.value);
    const start = dateFrom.diff(startMonthDate, 'day');

    const pos = {
      x: start * BLOCK_SIZE,
      width: BLOCK_SIZE * between,
    };

    const taskToUpdate = tasks.value.find((t) => t.id === task.id) || topTasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.style = taskToUpdate.style || {};
      taskToUpdate.style.width = `${pos.width}px`;
      taskToUpdate.style.transform = `translateX(${pos.x}px)`;
    } else {
      console.error('Task not found for updating:', task.id);
    }
  }

  function updateTopTaskName(task) {
    const taskToUpdate = topTasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.name = task.name;
    }
  }

  function updateTaskName(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.name = task.name;
    }
  }

  function updateTaskPmType(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.pmType = task.pmType;
    }
  }

  function updateTaskAssignee(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.assignee = task.assignee;
    }
  }

  const topTodayPosition = computed(() => {
    const today = dayjs();
    const startDate = dayjs(startMonth.value);
    const diffFuture = today.diff(startDate, 'day');
    return diffFuture >= 0 ? diffFuture * BLOCK_SIZE : -1;
  });

  const bottomTodayPosition = computed(() => {
    const today = dayjs();
    const startDate = dayjs(startMonth.value);
    const diffFuture = today.diff(startDate, 'day');
    return diffFuture >= 0 ? diffFuture * BLOCK_SIZE : -1;
  });

  const topTaskRows = computed(() => {
    const startMonthDate = dayjs(startMonth.value);

    return topTasks.value.map((task) => {
      const dateFrom = dayjs(task.startDate);
      const dateTo = dayjs(task.endDate);
      const between = dateTo.diff(dateFrom, 'day') + 1;
      const start = dateFrom.diff(startMonthDate, 'day');

      const pos = {
        x: start * BLOCK_SIZE,
        width: BLOCK_SIZE * between,
      };

      const style = {
        width: `${pos.width}px`,
        transform: `translateX(${pos.x}px)`,
      };

      return {
        style,
        pos,
        ...task,
      };
    });
  });

  const bottomTaskRows = computed(() => {
    const startMonthDate = dayjs(startMonth.value);

    return tasks.value.map((task) => {
      const dateFrom = dayjs(task.startDate);
      const dateTo = dayjs(task.endDate);
      const between = dateTo.diff(dateFrom, 'day') + 1;
      const start = dateFrom.diff(startMonthDate, 'day');

      const pos = {
        x: start * BLOCK_SIZE,
        width: BLOCK_SIZE * between,
      };

      const style = {
        width: `${pos.width}px`,
        transform: `translateX(${pos.x}px)`,
      };

      return {
        style,
        pos,
        ...task,
      };
    });
  });

  const topChartHeight = computed(() => (topTaskRows.value.length + 1) * taskRowHeight);
  const bottomChartHeight = computed(() => (bottomTaskRows.value.length + 1) * taskRowHeight);

  const inputWidths = {
    name: 100,
    startDate: 90,
    endDate: 90,
    sample: 80,
    pmType: 80,
    assignee: 80,
  };

  const topTaskFormWidth = computed(() => {
    return (
      30 + // チェックボックスの幅
      inputWidths.name +
      inputWidths.startDate +
      inputWidths.endDate +
      topExtraColumns.value.length * extraColumnWidth
    );
  });

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

  function addTopTaskColumn() {
    const columnKey = `extra${topExtraColumns.value.length + 1}`;
    topExtraColumns.value.push({ key: columnKey, label: `追加${topExtraColumns.value.length + 1}` });

    topTasks.value.forEach((task) => {
      task[columnKey] = '';
    });
  }

  function addBottomTaskColumn() {
    const columnKey = `extra${bottomExtraColumns.value.length + 1}`;
    bottomExtraColumns.value.push({ key: columnKey, label: `追加${bottomExtraColumns.value.length + 1}` });

    tasks.value.forEach((task) => {
      task[columnKey] = '';
    });
  }

  function updateTopTaskAdditional(task, key) {
    const taskToUpdate = topTasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate[key] = task[key];
    }
  }

  function updateBottomTaskAdditional(task, key) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate[key] = task[key];
    }
  }

  function removeSelectedTopTasks() {
    console.log('Removing selected top tasks...');
    topTasks.value.forEach((task) => {
      console.log(`Before Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
    });

    const beforeCount = topTasks.value.length;
    topTasks.value = topTasks.value.filter((task) => !task.selected);

    topTasks.value.forEach((task) => {
      console.log(`After Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
    });

    const afterCount = topTasks.value.length;
    console.log(`Removed ${beforeCount - afterCount} top tasks.`);
    topTasks.value.forEach(updateTaskDates);
  }

  function removeSelectedBottomTasks() {
    console.log('Removing selected bottom tasks...');
    tasks.value.forEach((task) => {
      console.log(`Before Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
    });

    const beforeCount = tasks.value.length;
    tasks.value = tasks.value.filter((task) => !task.selected);

    tasks.value.forEach((task) => {
      console.log(`After Remove - Task ID: ${task.id}, Selected: ${task.selected}`);
    });

    const afterCount = tasks.value.length;
    console.log(`Removed ${beforeCount - afterCount} bottom tasks.`);
    tasks.value.forEach(updateTaskDates);
  }

  return {
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
  };
}
