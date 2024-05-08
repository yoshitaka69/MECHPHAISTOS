<template>
    <div id="app">
        <div id="gantt-header" class="h-12 p-2 flex items-center">
            <h1 class="text-sm font-bold">ガントチャート</h1>
            <button @click="addTask" class="bg-indigo-700 hover:bg-indigo-900 text-white py-2 px-4 rounded-lg flex items-center">
                <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                <span class="font-bold text-xs"> タスクを追加する </span>
            </button>

            <teleport to="#form">
                <div class="base" v-show="show">
                    <div class="overlay" v-show="show" @click="show = false"></div>
                    <div class="content" v-show="show">
                        <h2 class="font-bold" v-if="updateMode">タスクの更新</h2>
                        <h2 class="font-bold" v-else>タスクの追加</h2>

                        <div class="my-4">
                            <label class="text-xs">カテゴリーID:</label>
                            <select v-model="form.category_id" class="text-xs border px-4 py-2 rounded-lg">
                                <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                            </select>
                        </div>

                        <div class="my-4">
                            <label class="text-xs">ID:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model.number="form.id" />
                        </div>

                        <div class="my-4">
                            <label class="text-xs">タスク名:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model="form.name" />
                        </div>

                        <div class="my-4">
                            <label class="text-xs">担当者:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model="form.incharge_user" />
                        </div>

                        <div class="my-4">
                            <label class="text-xs">開始日:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model="form.start_date" type="date" />
                        </div>

                        <div class="my-4">
                            <label class="text-xs">完了期限日:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model="form.end_date" type="date" />
                        </div>

                        <div class="my-4">
                            <label class="text-xs">進捗度:</label>
                            <input class="text-xs border rounded-lg px-4 py-2" v-model="form.percentage" type="number" />
                        </div>

                        <div v-if="updateMode" class="flex items-center justify-between">
                            <button @click="updateTask(form.id)" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg text-xs flex items-center">
                                <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                                </svg>
                                <span class="text-xs font-bold text-white">タスクを更新</span>
                            </button>
                            <button @click="deleteTask(form.id)" class="bg-red-500 hover:bg-red-700 text-white py-2 px-4 rounded-lg flex items-center ml-2">
                                <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                </svg>
                                <span class="text-xs font-bold text-white">タスクを削除</span>
                            </button>
                        </div>
                        <div v-else>
                            <button @click="saveTask" class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg flex items-center">
                                <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                                </svg>
                                <span class="font-bold text-xs"> タスクを追加する </span>
                            </button>
                        </div>
                    </div>
                </div>
            </teleport>
        </div>
        <div id="gantt-content" class="flex">
            <div id="gantt-task">
                <div id="gantt-task-title" class="flex items-center bg-green-600 text-white h-20" ref="task">
                    <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-48 h-full">タスク</div>
                    <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-24 h-full">開始日</div>
                    <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-24 h-full">完了期限日</div>
                    <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-16 h-full">担当</div>
                    <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-12 h-full">進捗</div>
                </div>

                <div id="gantt-task-list" class="overflow-y-hidden" :style="`height:${calendarViewHeight}px`">
                    <div v-for="(task, index) in displayTasks" :key="index" class="flex h-10 border-b" @dragstart="dragTask(task)" @dragover.prevent="dragTaskOver(task)" draggable="true">
                        <template v-if="task.cat === 'category'">
                            <div class="flex items-center font-bold w-full text-sm pl-2 flex justify-between items-center bg-teal-100">
                                <span>{{ task.name }}</span>
                                <div class="pr-4" @click="toggleCategory(task.id)">
                                    <span v-if="task.collapsed">
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </span>
                                    <span v-else>
                                        <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                        </svg>
                                    </span>
                                </div>
                            </div>
                        </template>
                        <template v-else>
                            <div @click="editTask(task)" class="border-r flex items-center font-bold w-48 text-sm pl-4">
                                {{ task.name }}
                            </div>
                            <div class="border-r flex items-center justify-center w-24 text-sm">
                                {{ task.start_date }}
                            </div>
                            <div class="border-r flex items-center justify-center w-24 text-sm">
                                {{ task.end_date }}
                            </div>
                            <div class="border-r flex items-center justify-center w-16 text-sm">
                                {{ task.incharge_user }}
                            </div>
                            <div class="flex items-center justify-center w-12 text-sm">{{ task.percentage }}%</div>
                        </template>
                    </div>
                </div>
            </div>

            <div id="gantt-calendar" class="overflow-x-scroll overflow-y-hidden border-l" :style="`width:${calendarViewWidth}px`" ref="calendar">
                <div id="gantt-date" class="h-20">
                    <div id="gantt-year-month" class="relative h-8">
                        <div v-for="(calendar, index) in calendars" :key="index">
                            <div
                                class="bg-indigo-700 text-white border-b border-r border-t h-8 absolute font-bold text-sm flex items-center justify-center"
                                :style="`width:${calendar.calendar * block_size}px;left:${calendar.start_block_number * block_size}px`"
                            >
                                {{ calendar.date }}
                            </div>
                        </div>
                    </div>

                    <div id="gantt-day" class="relative h-12">
                        <div v-for="(calendar, index) in calendars" :key="index">
                            <div v-for="(day, index) in calendar.days" :key="index">
                                <div
                                    class="border-r border-b h-12 absolute flex items-center justify-center flex-col font-bold text-xs"
                                    :class="{ 'bg-blue-100': day.dayOfWeek === '土', 'bg-red-100': day.dayOfWeek === '日', 'bg-red-600 text-white': calendar.year === today.year() && calendar.month === today.month() && day.day === today.date() }"
                                    :style="`width:${block_size}px;left:${day.block_number * block_size}px`"
                                >
                                    <span>{{ day.day }}</span>
                                    <span>{{ day.dayOfWeek }}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="gantt-height" class="relative">
                        <div v-for="(calendar, index) in calendars" :key="index">
                            <div v-for="day in calendar.days" :key="index">
                                <div
                                    class="border-r border-b absolute"
                                    :class="{ 'bg-blue-100': day.dayOfWeek === '土', 'bg-red-100': day.dayOfWeek === '日' }"
                                    :style="`width:${block_size}px;left:${day.block_number * block_size}px;height:${calendarViewHeight}px`"
                                ></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div id="gantt-bar-area" class="relative" :style="`width:${calendarViewWidth}px;height:${calendarViewHeight}px`">
                    <div v-for="(bar, index) in taskBars" :key="index">
                        <div :style="bar.style" class="rounded-lg absolute h-5 bg-yellow-100" v-if="bar.task.cat === 'task'" @mousedown="mouseDownMove(bar.task)">
                            <div class="w-full h-full" style="pointer-events: none">
                                <div class="h-full bg-yellow-500 rounded-l-lg" style="pointer-events: none" :style="`width:${bar.task.percentage}%`" :class="{ 'rounded-r-lg': bar.task.percentage === 100 }"></div>
                            </div>

                            <div class="absolute w-2 h-2 bg-gray-300 border border-black" style="top: 6px; left: -6px; cursor: col-resize" @mousedown.stop="mouseDownResize(bar.task, 'left')"></div>
                            <div class="absolute w-2 h-2 bg-gray-300 border border-black" style="top: 6px; right: -6px; cursor: col-resize" @mousedown.stop="mouseDownResize(bar.task, 'right')"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, reactive, onMounted, computed } from 'vue';
import moment from 'moment';

export default {
  name: 'GanttChart',

  setup() {
    const today = ref(moment());
    const show = ref(false);
    const updateMode = ref(false);
    const form = reactive({
      category_id: '',
      id: '',
      name: '',
      start_date: '',
      end_date: '',
      incharge_user: '',
      percentage: 0
    const dragging = ref(false);
    const leftResizing = ref(false);
    const rightResizing = ref(false);
    const activeTask = ref(null);
    const pageX = ref(0);
    const elementStyle = reactive({
      left: '',
      width: ''
    const dragging = ref(false);
    const resizeInfo = reactive({
      leftResizing: false,
      rightResizing: false,
      startX: 0,
      startWidth: 0,
      element: null

    });
    const categories = ref([
      { id: 1, name: 'テストA', collapsed: false },
      { id: 2, name: 'テストB', collapsed: false }
    ]);
    const tasks = ref([
      { id: 1, category_id: 1, name: 'テスト1', start_date: '2020-11-18', end_date: '2020-11-20', incharge_user: '鈴木', percentage: 100 },
      { id: 2, category_id: 1, name: 'テスト2', start_date: '2020-11-19', end_date: '2020-11-23', incharge_user: '佐藤', percentage: 90 },
      // More tasks...
    ]);

    const calendarData = reactive({
      start_month: '2020-10',
      end_month: '2021-02',
      block_size: 30,
      calendars: [],
    });

    const deleteTask = (id) => {
      const index = tasks.value.findIndex(task => task.id === id);
      if (index !== -1) {
        tasks.value.splice(index, 1);
      }
    };

      const updateTask = (id) => {
      const task = tasks.value.find(task => task.id === id);
      if (task) {
        Object.assign(task, form);
      }
    };

    const addTask = () => {
      tasks.value.push({ ...form, id: Math.max(...tasks.value.map(t => t.id)) + 1 }); // Assign a new ID
      Object.keys(form).forEach(key => form[key] = '');
    };

    const editTask = (task) => {
      updateMode.value = true;
      show.value = true;
      Object.assign(form, task);
    };

    const saveTask = () => {
      if (updateMode.value) {
        updateTask(form.id);
      } else {
        addTask();
      }
      show.value = false;
      updateMode.value = false;
    };

    const toggleCategory = (id) => {
      const category = categories.value.find(c => c.id === id);
      if (category) {
        category.collapsed = !category.collapsed;
      }
    };

    const computedTasks = computed(() => {
      return tasks.value.filter(task => {
        const category = categories.value.find(c => c.id === task.category_id);
        return category && !category.collapsed;
      });
    });
    onMounted(() => {
      getCalendar();
    });

    const getCalendar = () => {
      let start = moment(calendarData.start_month);
      let end = moment(calendarData.end_month);
      let block_number = 0;

      while (start <= end) {
        let month = {
          start_block_number: block_number,
          date: start.format('YYYY年MM月'),
          days: Array.from({ length: start.daysInMonth() }).map((_, i) => {
            return {
              day: i + 1,
              dayOfWeek: ['日', '月', '火', '水', '木', '金', '土'][moment(start).date(i + 1).day()],
              block_number: block_number++
            };
          })
        };
        calendarData.calendars.push(month);
        start.add(1, 'month');
      }
    };



    const calendarViewHeight = computed(() => {
  const innerHeight = window.innerHeight;
  const taskHeight = 48; // 仮のタスクヘッダの高さ
  return innerHeight - taskHeight - 48 - 20; // 仮の調整値
});

const calendarViewWidth = computed(() => {
  const innerWidth = window.innerWidth;
  const taskWidth = 200; // 仮のサイドバータスク幅
  return innerWidth - taskWidth;
});

const displayTasks = computed(() => {
  let displayTaskNumber = Math.floor(calendarViewHeight.value / 40);
  return lists.value.slice(0, displayTaskNumber); // シンプルに0から計算
});

const taskBars = computed(() => {
  let top = 10;
  return displayTasks.value.map(task => {
    let style = {};
    if (task.cat === 'task') {
      let dateFrom = moment(task.start_date);
      let dateTo = moment(task.end_date);
      let between = dateTo.diff(dateFrom, 'days') + 1;
      let start = dateFrom.diff(moment(calendarData.start_month), 'days');
      let left = start * calendarData.block_size;
      style = {
        top: `${top}px`,
        left: `${left}px`,
        width: `${calendarData.block_size * between}px`
      };
    }
    top += 40;
    return { style, task };
  });
});

const scrollDistance = computed(() => {
  let startDate = moment(calendarData.start_month);
  let betweenDays = today.value.diff(startDate, 'days');
  return betweenDays * calendarData.block_size;
});

const mouseDownMove = (event, task) => {
      dragging.value = task;
      resizeInfo.startX = event.pageX;
      resizeInfo.element = event.target;
    };

    const mouseMove = (event) => {
      if (dragging.value) {
        const diff = resizeInfo.startX - event.pageX;
        resizeInfo.element.style.left = `${parseInt(resizeInfo.element.style.left) - diff}px`;
        resizeInfo.startX = event.pageX;
      }
    };

    const stopDrag = () => {
      dragging.value = false;
    };

    const mouseDownResize = (event, task, direction) => {
      dragging.value = task;
      resizeInfo.startX = event.pageX;
      resizeInfo.startWidth = parseInt(event.target.parentElement.style.width);
      resizeInfo.element = event.target.parentElement;
      resizeInfo.leftResizing = direction === 'left';
      resizeInfo.rightResizing = direction === 'right';
    };

    const mouseResize = (event) => {
      if (!dragging.value) return;
      const diff = resizeInfo.startX - event.pageX;
      if (resizeInfo.leftResizing) {
        resizeInfo.element.style.width = `${resizeInfo.startWidth + diff}px`;
      } else if (resizeInfo.rightResizing) {
        resizeInfo.element.style.width = `${resizeInfo.startWidth - diff}px`;
      }
    };

    const stopResize = () => {
      resizeInfo.leftResizing = false;
      resizeInfo.rightResizing = false;
      dragging.value = false;
    };

const lists = computed(() => {
  let allLists = [];
  categories.value.forEach(category => {
    allLists.push({ cat: 'category', ...category });
    tasks.value.forEach(task => {
      if (task.category_id === category.id && !category.collapsed) {
        allLists.push({ cat: 'task', ...task });
      }
    });
  });
  return allLists;
});

// Lifecycle and Event Listeners
onMounted(() => {
  getCalendar();
  window.addEventListener('resize', getWindowSize);
  window.addEventListener('wheel', windowSizeCheck);
  window.addEventListener('mousemove', mouseMove);
  window.addEventListener('mouseup', stopDrag);
});

const getWindowSize = () => {
  // Implement window size adjustment logic here
};

const windowSizeCheck = () => {
  // Implement scroll wheel handling logic here
};

const mouseMove = () => {
  // Handle mouse move events here
};

const stopDrag = () => {
  // Handle stopping of dragging operations here
};

return {
  today,
  show,
  updateMode,
  form,
  categories,
  tasks: computedTasks,
  deleteTask,
  updateTask,
  addTask,
  editTask,
  saveTask,
  toggleCategory,
  calendarData,
  displayTasks,
  taskBars,
  calendarViewWidth,
  calendarViewHeight,
  scrollDistance,
  lists,
      dragTaskOver,
      dragTask,
      mouseDownMove,
      mouseMove,
      stopDrag,
      mouseDownResize,
      mouseResize,
      stopResize
};
</script>
