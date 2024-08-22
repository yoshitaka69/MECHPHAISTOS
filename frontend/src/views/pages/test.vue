<template>
    <div id="gantt" class="space-y-4">
        <!-- 上部のガントチャート -->
        <div class="gantt-chart-wrapper top-chart">
            <div id="gantt-chart-container-1" class="overflow-auto w-full select-none bg-white">
                <div id="top-header" class="top-0 flex z-20 sticky" :style="{ width: `${topViewWidth + scrollbarOffset}px` }">
                    <div class="border-b border-black bg-green-100 flex sticky left-0 top-0" :style="{ minWidth: `${topTaskWidth}px` }">
                        <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px">Plant</div>
                        <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">開始日</div>
                        <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px">期限日</div>
                    </div>
                    <template v-for="month in calendars" :key="month.title">
                        <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days}px` }">
                            <div class="border-b border-r border-black px-2">{{ month.title }}</div>
                            <div class="flex">
                                <div v-for="day in month.days" :key="day.date" class="border-r border-black text-xs text-center" :class="weekendColor(day.dayOfWeek)" :style="{ minWidth: `${blockWidth}px` }">
                                    {{ day.date }}
                                </div>
                            </div>
                            <div class="flex">
                                <div v-for="day in month.days" :key="day.date" class="border-r border-black text-xs text-center" :class="weekendColor(day.dayOfWeek)" :style="{ minWidth: `${blockWidth}px` }">
                                    {{ day.dayOfWeek }}
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
                <div id="top-contents" class="relative overflow-y-auto" :style="{ width: `${topViewWidth + scrollbarOffset}px`, height: `${topTaskRows.length * taskRowHeight}px` }">
                    <!-- 縦のグリッド線を表示 -->
                    <div v-for="i in totalDays" :key="i" class="absolute bg-gray-200" :style="{ left: `${i * blockWidth + topTaskWidth}px`, top: 0, height: `${topTaskRows.length * taskRowHeight}px`, width: '1px' }"></div>
                    <!-- 今日の日付を示す赤い帯 -->
                    <div v-if="topTodayPosition >= 0" class="absolute bg-red-100" :style="{ width: `${blockWidth - 1}px`, left: `${topTodayPosition}px`, height: `${topTaskRows.length * taskRowHeight}px` }"></div>
                    <div v-for="task in topTaskRows" :key="task.id" class="task-row top-task-row flex">
                        <div class="bg-green-100 z-10 flex sticky left-0" :style="{ minWidth: `${topTaskWidth}px` }">
                            <!-- 編集可能なタスク名フィールド -->
                            <input class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px" v-model="task.name" @change="updateTopTaskName(task)" />
                            <!-- 編集可能な開始日フィールド -->
                            <input class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px" type="date" v-model="task.startDate" @change="updateTopTaskDates(task)" />
                            <!-- 編集可能な期限日フィールド -->
                            <input class="py-2 h-full text-center border-r border-black text-sm" style="width: 90px" type="date" v-model="task.endDate" @change="updateTopTaskDates(task)" />
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
            <div id="gantt-chart-container-2" class="overflow-auto w-full select-none bg-white">
                <div id="bottom-header" class="top-0 flex z-20 sticky" :style="{ width: `${bottomViewWidth + scrollbarOffset}px` }">
                    <div class="border-b border-black bg-blue-100 flex sticky left-0 top-0" :style="{ minWidth: `${bottomTaskWidth}px` }">
                        <div class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px">タスク</div>
                        <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px">PM type</div>
                        <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px">開始日</div>
                        <div class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px">期限日</div>
                    </div>
                    <template v-for="month in calendars" :key="month.title">
                        <div class="border-b border-black bg-white" :style="{ minWidth: `${blockWidth * month.days}px` }">
                            <div class="border-b border-r border-black px-2">{{ month.title }}</div>
                            <div class="flex">
                                <div v-for="day in month.days" :key="day.date" class="border-r border-black text-xs text-center" :class="weekendColor(day.dayOfWeek)" :style="{ minWidth: `${blockWidth}px` }">
                                    {{ day.date }}
                                </div>
                            </div>
                            <div class="flex">
                                <div v-for="day in month.days" :key="day.date" class="border-r border-black text-xs text-center" :class="weekendColor(day.dayOfWeek)" :style="{ minWidth: `${blockWidth}px` }">
                                    {{ day.dayOfWeek }}
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
                <div id="bottom-contents" class="relative overflow-y-auto" :style="{ width: `${bottomViewWidth + scrollbarOffset}px`, height: `${bottomTaskRows.length * taskRowHeight}px` }">
                    <!-- 縦のグリッド線を表示 -->
                    <div v-for="i in totalDays" :key="i" class="absolute bg-gray-200" :style="{ left: `${i * blockWidth + bottomTaskWidth}px`, top: 0, height: `${bottomTaskRows.length * taskRowHeight}px`, width: '1px' }"></div>
                    <!-- 今日の日付を示す赤い帯 -->
                    <div v-if="bottomTodayPosition >= 0" class="absolute bg-red-100" :style="{ width: `${blockWidth - 1}px`, left: `${bottomTodayPosition}px`, height: `${bottomTaskRows.length * taskRowHeight}px` }"></div>
                    <div v-for="task in bottomTaskRows" :key="task.id" class="task-row bottom-task-row flex">
                        <div class="bg-blue-100 z-10 flex sticky left-0" :style="{ minWidth: `${bottomTaskWidth}px` }">
                            <!-- 編集可能なタスク名フィールド -->
                            <input class="py-2 h-full px-2 border-r border-black text-sm" style="width: 120px" v-model="task.name" @change="updateTaskName(task)" />
                            <!-- 編集可能なPM typeフィールド -->
                            <input class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px" v-model="task.pmType" @change="updateTaskPmType(task)" />
                            <!-- 編集可能な開始日フィールド -->
                            <input class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px" type="date" v-model="task.startDate" @change="updateTaskDates(task)" />
                            <!-- 編集可能な期限日フィールド -->
                            <input class="py-2 h-full text-center border-r border-black text-sm" style="width: 120px" type="date" v-model="task.endDate" @change="updateTaskDates(task)" />
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

<script lang="ts" setup>
import { ref, onMounted, onUnmounted, reactive, computed } from 'vue';
import dayjs from 'dayjs';
import axios from 'axios';

const BLOCK_SIZE = 20;
const TOP_TASK_WIDTH = 300; // 上部ガントチャートのタスク幅
const BOTTOM_TASK_WIDTH = 480; // 下部ガントチャートのタスク幅

const dragging = ref(false);
const leftResizing = ref(false);
const rightResizing = ref(false);
const target = reactive({
    pageX: 0,
    element: null,
    task: null
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
const scrollbarOffset = 20; // スクロールバーのオフセット
const taskRowHeight = 40; // 各タスク行の高さ

onMounted(async () => {
    console.log('Component mounted, starting data fetch...');
    try {
        // Django APIからタスクデータを取得
        const response = await axios.get('/api/gantt-tests/');
        console.log('Data fetched successfully:', response.data);

        // 取得したデータを整形してtasksに格納
        tasks.value = response.data.map(task => ({
            id: task.id,
            name: task.name,
            startDate: task.start_date,
            endDate: task.end_date,
        }));

        console.log('Tasks initialized:', tasks.value);

        // タスクデータに基づいてガントチャートを更新
        updateTaskRows();
    } catch (error) {
        console.error("There was an error fetching the tasks:", error);
    }

    console.log('Initializing view...');
    initView();
    makeTestData();

    // イベントリスナーの登録
    document.addEventListener('mousemove', onMouseDown_Moving);
    document.addEventListener('mouseup', onMouseDown_MoveStop);
    document.addEventListener('mousemove', onMouseDown_Resizing);
    document.addEventListener('mouseup', onMouseDown_ResizeStop);
});

onUnmounted(() => {
    // イベントリスナーの解除
    console.log('Component unmounted, removing event listeners...');
    document.removeEventListener('mousemove', onMouseDown_Moving);
    document.removeEventListener('mouseup', onMouseDown_MoveStop);
    document.removeEventListener('mousemove', onMouseDown_Resizing);
    document.removeEventListener('mouseup', onMouseDown_ResizeStop);
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
            width: BLOCK_SIZE * between
        };

        const style = {
            width: `${pos.width}px`,
            transform: `translateX(${pos.x}px)`
        };

        return {
            style,
            pos,
            ...task
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
            width: BLOCK_SIZE * between
        };

        const style = {
            width: `${pos.width}px`,
            transform: `translateX(${pos.x}px)`
        };

        return {
            style,
            pos,
            ...task
        };
    });
});

const topTodayPosition = computed(() => {
    const today = dayjs();
    const startDate = dayjs(startMonth.value);
    const endDate = dayjs(endMonth.value);
    const diffFuture = today.diff(startDate, 'day');
    const diffPast = endDate.diff(today, 'day') + endDate.daysInMonth();
    return diffFuture >= 0 && diffPast > 0 ? diffFuture * BLOCK_SIZE + topTaskWidth.value : -1;
});

const bottomTodayPosition = computed(() => {
    const today = dayjs();
    const startDate = dayjs(startMonth.value);
    const endDate = dayjs(endMonth.value);
    const diffFuture = today.diff(startDate, 'day');
    const diffPast = endDate.diff(today, 'day') + endDate.daysInMonth();
    return diffFuture >= 0 && diffPast > 0 ? diffFuture * BLOCK_SIZE + bottomTaskWidth.value : -1;
});

function initView() {
    console.log('Initializing calendar and view dimensions...');
    serCalendar();
    totalDays.value = calendars.value.reduce((p, c) => p + c.days.length, 0);
    contentWidth.value = totalDays.value * blockWidth.value;
    topViewWidth.value = topTaskWidth.value + contentWidth.value;
    bottomViewWidth.value = bottomTaskWidth.value + contentWidth.value;
    if (calendar.value) {
        calendar.value.scrollLeft = bottomTodayPosition.value - BOTTOM_TASK_WIDTH;
    }
}

function updateTaskRows() {
    console.log('Updating task rows...');
    tasks.value.forEach(task => {
        updateTaskDates(task);
    });
}

function getDays(startMonth) {
    const dayOfWeek = ['日', '月', '火', '水', '木', '金', '土'];
    const days = [];
    for (let i = 0; i < startMonth.daysInMonth(); i++) {
        const targetDate = startMonth.add(i, 'day');
        days.push({
            date: targetDate.date(),
            dayOfWeek: dayOfWeek[targetDate.day()]
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
            days: getDays(targetMonth)
        });
    }
}

function onMouseDown_MoveStart(e, task, taskList) {
    dragging.value = true;
    target.pageX = e.pageX;
    target.element = e.target;
    target.task = task;
    target.taskList = taskList;
}

function onMouseDown_Moving(e) {
    if (!dragging.value) return;

    const realX = calcMovePositionX(e.pageX);
    target.element.style.transform = `translateX(${realX}px)`;
}

function onMouseDown_MoveStop(e) {
    if (!dragging.value) return;

    const realX = calcMovePositionX(e.pageX);
    const days = Math.round((target.task?.pos?.x - realX) / BLOCK_SIZE);

    if (days !== 0 && target.taskList) {
        const task = target.taskList.find((t) => t.id === target.task.id);
        if (task) {
            task.startDate = dayjs(task.startDate).add(-days, 'day').format('YYYY-MM-DD');
            task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
            updateTaskDates(task); // バーの位置と幅を更新
        }
    } else if (target.task) {
        target.element.style.transform = `translateX(${target.task.pos.x}px)`;
    }

    dragging.value = false;
    target.element = null;
    target.task = null;
    target.pageX = 0;
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
}

function onMouseDown_Resizing(e) {
    if (leftResizing.value || rightResizing.value) {
        const realWidth = calcResizeWidth(e.pageX, target.direction);
        const realX = target.direction === 'left' ? calcResizePositionX(e.pageX) : target.task.pos.x;
        target.element.style.transform = `translateX(${realX}px)`;
        target.element.style.width = `${realWidth}px`;
    }
}

function onMouseDown_ResizeStop(e) {
    if (leftResizing.value || rightResizing.value) {
        const realWidth = calcResizeWidth(e.pageX, target.direction);
        const days = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE);

        if (days !== 0) {
            const task = target.taskList.find((t) => t.id === target.task.id);
            if (leftResizing.value) {
                task.startDate = dayjs(task.startDate).add(days, 'day').format('YYYY-MM-DD');
            } else {
                task.endDate = dayjs(task.endDate).add(-days, 'day').format('YYYY-MM-DD');
            }
            updateTaskDates(task); // バーの位置と幅を更新
        } else {
            target.element.style.transform = `translateX(${target.task.pos.x}px)`;
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
    if (!target.task || !target.task.pos) {
        console.error('Task or task.pos is null in calcMovePositionX');
        return 0; // 0 で代用するか、適切なデフォルト値を返す
    }

    const diff = target.pageX - currentPageX;
    return keepThreshold(target.task.pos.x - diff, 0, contentWidth.value - target.task.pos.width);
}

function calcResizePositionX(currentPageX) {
    const diff = target.pageX - currentPageX;
    return keepThreshold(target.task.pos.x - diff, 0, target.task.pos.x + target.task.pos.width - BLOCK_SIZE);
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
    // 上部のタスク
    for (let i = 1; i <= 3; i++) {
        topTasks.value.push({
            id: i,
            name: `plant - ${i}`,
            startDate: today.format('YYYY-MM-DD'),
            endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD')
        });
    }
    // 下部のタスク
    for (let i = 4; i <= 10; i++) {
        tasks.value.push({
            id: i,
            name: `task - ${i}`,
            pmType: `PM-${(i % 3) + 1}`, // PM typeを設定
            startDate: today.format('YYYY-MM-DD'),
            endDate: today.add(Math.floor(Math.random() * 5), 'day').format('YYYY-MM-DD')
        });
    }
}

function updateTopTaskDates(task) {
    try {
        const dateFrom = dayjs(task.startDate);
        const dateTo = dayjs(task.endDate);
        const between = dateTo.diff(dateFrom, 'day') + 1;
        const startMonthDate = dayjs(startMonth.value);
        const start = dateFrom.diff(startMonthDate, 'day');
        const pos = {
            x: start * BLOCK_SIZE,
            width: BLOCK_SIZE * between
        };
        task.style.width = `${pos.width}px`;
        task.style.transform = `translateX(${pos.x}px)`;
    } catch (error) {
        console.error('Error in updateTopTaskDates:', error);
    }
}

function updateTaskDates(task) {
    try {
        if (!task) {
            console.error('Task is undefined in updateTaskDates');
            return;
        }

        const dateFrom = dayjs(task.startDate);
        const dateTo = dayjs(task.endDate);
        const between = dateTo.diff(dateFrom, 'day') + 1;
        const startMonthDate = dayjs(startMonth.value);
        const start = dateFrom.diff(startMonthDate, 'day');
        const pos = {
            x: start * BLOCK_SIZE,
            width: BLOCK_SIZE * between
        };

        if (!task.style) {
            task.style = {}; // 必要に応じて style オブジェクトを初期化
        }

        console.log(`Updating task: ${task.name}, Start Date: ${task.startDate}, End Date: ${task.endDate}`);
        console.log(`Calculated Position - X: ${pos.x}, Width: ${pos.width}px`);

        task.style.width = `${pos.width}px`;
        task.style.transform = `translateX(${pos.x}px)`;
    } catch (error) {
        console.error('Error in updateTaskDates:', error);
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

.gantt-chart-wrapper {
    margin-bottom: 50px; /* 下部のガントチャートとの間にスペースを追加 */
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

#top-contents {
    height: calc(100vh - 8rem); /* 既存のスタイルの高さを少し低く調整 */
    margin-bottom: 200; /* 下部の余白を削除 */
    padding-bottom: 200; /* 下部のパディングを削除 */
}
</style>
