<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">


<template>
 <div id="gantt-content" class="flex">
    <div id="gantt-task">
      <div id="gantt-task-title" class="flex items-center bg-green-600 text-white h-20" ref="task">
        <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-48 h-full">タスク
        </div>
        <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-24 h-full">開始日
        </div>
        <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-24 h-full">完了期限日
        </div>
        <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-16 h-full">担当
        </div>
        <div class="border-t border-r border-b flex items-center justify-center font-bold text-xs w-12 h-full">進捗
        </div>
      </div>

      <div id="gantt-task-list" class="overflow-y-hidden" :style="`height:${calendarViewHeight}px`">
        
        <div v-for="(task, index) in displayTasks" 
             :key="index" 
             class="flex h-10 border-b"
             @dragstart="dragTask(task)"
             @dragover.prevent="dragTaskOver(task)"
             draggable=true>
  
          <template v-if="task.cat === 'category'">
            <div class="flex items-center font-bold w-full text-sm pl-2 flex justify-between items-center bg-teal-100">
              <span>{{task.name}}</span>
              <div class="pr-4" @click="toggleCategory(task.id)">
                <span v-if="task.collapsed">
                  <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                       stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                  </svg>
                </span>
                <span v-else>
                  <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                       stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </span>
              </div>
            </div>
          </template>
          <template v-else>
            <div
              @click="editTask(task)"
              class="border-r flex items-center font-bold w-48 text-sm pl-4">
              {{task.name}}
            </div>
            <div class="border-r flex items-center justify-center w-24 text-sm">
              {{task.start_date}}
            </div>
            <div class="border-r flex items-center justify-center w-24 text-sm">
              {{task.end_date}}
            </div>
            <div class="border-r flex items-center justify-center w-16 text-sm">
              {{task.incharge_user}}
            </div>
            <div class="flex items-center justify-center w-12 text-sm">
              {{task.percentage}}%
            </div>
          </template>
        </div>
      </div>
    </div>

    <div id="gantt-calendar" class="overflow-x-scroll overflow-y-hidden border-l" :style="`width:${calendarViewWidth}px`" ref="calendar">      
      <div id="gantt-date" class="h-20">
        <div id="gantt-year-month" class="relative h-8">
          <div v-for="(calendar,index) in calendars" :key="index">
            <div
              class="bg-indigo-700 text-white border-b border-r border-t h-8 absolute font-bold text-sm flex items-center justify-center"
              :style="`width:${calendar.calendar*block_size}px;left:${calendar.start_block_number*block_size}px`">
              {{calendar.date}}
            </div>
          </div>
        </div>
        
        <div id="gantt-day" class="relative h-12">
          <div v-for="(calendar,index) in calendars" :key="index">
            <div v-for="(day,index) in calendar.days" :key="index">
              <div class="border-r border-b h-12 absolute flex items-center justify-center flex-col font-bold text-xs"
                   :class="{'bg-blue-100': day.dayOfWeek === '土', 'bg-red-100': day.dayOfWeek ==='日',
                           'bg-red-600 text-white': calendar.year=== today.year() && calendar.month === today.month() && day.day === today.date()}"
                   :style="`width:${block_size}px;left:${day.block_number*block_size}px`">
                <span>{{ day.day }}</span>
                <span>{{ day.dayOfWeek }}</span>
              </div>
            </div>
          </div>
        </div>
        
        <div id="gantt-height" class="relative">
          <div v-for="(calendar,index) in calendars" :key="index">
            <div v-for="day in calendar.days" :key="index">
              <div class="border-r border-b absolute"
                   :class="{'bg-blue-100': day.dayOfWeek === '土', 'bg-red-100': day.dayOfWeek ==='日'}"
                   :style="`width:${block_size}px;left:${day.block_number*block_size}px;height:${calendarViewHeight}px`">
              </div>
            </div>
          </div>
        </div>
        
      </div>

      <div id="gantt-bar-area" class="relative" :style="`width:${calendarViewWidth}px;height:${calendarViewHeight}px`">
        <div v-for="(bar,index) in taskBars" :key="index">
          <div :style="bar.style"
               class="rounded-lg absolute h-5 bg-yellow-100"
               v-if="bar.task.cat === 'task'"
               @mousedown="mouseDownMove(bar.task)">
            
            <div class="w-full h-full" style="pointer-events: none;">
              <div class="h-full bg-yellow-500 rounded-l-lg" 
                   style="pointer-events: none;" 
                   :style="`width:${bar.task.percentage}%`"
                   :class="{'rounded-r-lg': bar.task.percentage === 100}"></div>
            </div>

            <div class="absolute w-2 h-2 bg-gray-300 border border-black" 
                 style="top:6px;left:-6px;cursor:col-resize" 
                 @mousedown.stop="mouseDownResize(bar.task,'left')">
            </div>
            <div class="absolute w-2 h-2 bg-gray-300 border border-black" 
                 style="top:6px;right:-6px;cursor:col-resize" 
                 @mousedown.stop="mouseDownResize(bar.task,'right')">
            </div>
            
          </div>
        </div>
      </div>
      
    </div>
    
  </div>
</template>
  





<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import moment from 'moment'; // moment.jsをインポート

const start_month = ref('2020-10');
const end_month = ref('2021-02');
const block_size = ref(30);
const block_number = ref(0);
const calendars = ref([]);
const inner_width = ref(window.innerWidth);
const inner_height = ref(window.innerHeight);
const task_width = ref(0);
const task_height = ref(0);
const today = ref(moment());
const position_id = ref(0);
const dragging = ref(false);
const pageX = ref('');
const element = ref(null);
const left = ref('');
const task_id = ref('');
const width = ref('');
const leftResizing = ref(false);
const rightResizing = ref(false);
const task = ref(null);
const show = ref(false);
const update_mode = ref(false);
const form = reactive({
    category_id: '',
    id: '',
    name: '',
    start_date: '',
    end_date: '',
    incharge_user: '',
    percentage: 0
});
const categories = reactive([
    {id: 1, name: 'テストA', collapsed: false},
    {id: 2, name: 'テストB', collapsed: false}
]);
const tasks = reactive([
    // タスクの配列...
]);

const deleteTask = (id) => {
    const delete_index = tasks.value.findIndex(task => task.id === id);
    if (delete_index !== -1) {
        tasks.value.splice(delete_index, 1);
        Object.assign(form, {});
        show.value = false;
    }
};

const updateTask = (id) => {
    const task = tasks.value.find(task => task.id === id);
    if (task) {
        Object.assign(task, form);
        Object.assign(form, {});
        show.value = false;
    }
};
            


onMounted(() => {
    getCalendar();
    getWindowSize();
    window.addEventListener('resize', getWindowSize);
    window.addEventListener('wheel', windowSizeCheck);
    window.addEventListener('mousemove', mouseMove);
    window.addEventListener('mousemove', mouseResize);
    window.addEventListener('mouseup', stopDrag);
});

const displayTasks = computed(() => {
    let display_task_number = Math.floor(calendarViewHeight.value / 40);
    return lists.value.slice(position_id.value, position_id.value + display_task_number);
});

const taskBars = computed(() => {
    let top = 10;
    return displayTasks.value.map(task => {
        let style = {};
        if(task.cat === 'task') {
            let date_from = moment(task.start_date);
            let date_to = moment(task.end_date);
            let between = date_to.diff(date_from, 'days') + 1;
            let start = date_from.diff(moment(start_month.value), 'days');
            let left = start * block_size.value;
            style = {
                top: `${top}px`,
                left: `${left}px`,
                width: `${block_size.value * between}px`,
            };
        }
        top += 40;
        return { style, task };
    });
});

const calendarViewWidth = computed(() => inner_width.value - task_width.value);
const calendarViewHeight = computed(() => inner_height.value - task_height.value - 48 - 20);
const scrollDistance = computed(() => {
    let start_date = moment(start_month.value);
    let between_days = today.value.diff(start_date, 'days');
    return (between_days + 1) * block_size.value - calendarViewWidth.value / 2;
});

const lists = computed(() => {
    let lists = [];
    categories.forEach(category => {
        lists.push({ cat: 'category', ...category });
        tasks.forEach(task => {
            if (task.category_id === category.id && !category.collapsed) {
                lists.push({ cat: 'task', ...task });
            }
        });
    });
    return lists;
});

</script>







<style>
.base {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    margin-top: 50px;
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: gray;
    opacity: 0.5;
}

.content {
    background-color: white;
    position: relative;
    border-radius: 10px;
    padding: 40px;
}
</style>