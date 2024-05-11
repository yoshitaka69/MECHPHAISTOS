<template>
    <div id="app" v-if="form && calendarData.calendars">
        <div id="gantt-header" class="h-12 p-2 flex items-center">
            <h1 class="text-sm font-bold">ガントチャート</h1>
            <button @click="addTask" class="bg-indigo-700 hover:bg-indigo-900 text-white py-2 px-4 rounded-lg flex items-center">
                <svg class="w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                <span class="font-bold text-xs">タスクを追加する</span>
            </button>
            <TaskForm :show.sync="show" :updateMode="updateMode" :form="form" :categories="categories" />
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
                        <div v-for="(calendar, index) in calendarData.calendars" :key="index">
                            <div
                                class="bg-indigo-700 text-white border-b border-r border-t h-8 absolute font-bold text-sm flex items-center justify-center"
                                :style="`width:${calendar.calendar * block_size}px;left:${calendar.start_block_number * block_size}px`"
                            >
                                {{ calendar.date }}
                            </div>
                        </div>
                    </div>

                    <div id="gantt-day" class="relative h-12">
                        <div v-for="(calendar, index) in calendarData.calendars" :key="index">
                            <div v-for="(day, index) in calendarData.calendars" :key="index">
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
                        <div v-for="(calendar, index) in calendarData.calendars" :key="index">
                            <div v-for="(day, index) in calendarData.calendars" :key="index">
                                <div
                                    class="border-r border-b absolute"
                                    :class="{ 'bg-blue-100': day.dayOfWeek === '土', 'bg-red-100': day.dayOfWeek === '日' }"
                                    :style="`width:${block_size}px;left:${day.block_number * block_size}px;height:${calendarViewHeight}px`"
                                ></div>
                            </div>
                        </div>
                    </div>
                </div>

                <div id="gantt-bar-area" class="relative" :style="`width:100%; height:100%;`">
                    <div v-for="(bar, index) in taskBars" :key="index">
                        <div :style="bar.style" class="rounded-lg bg-yellow-100" v-if="bar.task.category === 'task'" @mousedown="mouseDownMove(bar.task)">
                            <div class="w-full h-full" style="pointer-events: none">
                                <div class="h-full bg-yellow-500 rounded-l-lg" :style="`width:${bar.task.percentage}%`" :class="{ 'rounded-r-lg': bar.task.percentage === 100 }"></div>
                            </div>
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
import TaskForm from '@/components/Ganttchart/Ganttchart_form.vue';

export default {
    name: 'GanttChart',
    components: {
        TaskForm
    },
    data() {
        return {
            show: false,
            updateMode: false,
            form: false,
            categories: false,
            // その他のデータプロパティ
        };
    },

    setup() {
        const today = ref(moment());
        const show = ref(false);
        const updateMode = ref(false);
        const dragging = ref(false);
        const leftResizing = ref(false);
        const rightResizing = ref(false);
        const activeTask = ref(null);
        const pageX = ref(0);

        const form = reactive({
            category_id: '',
            id: '',
            name: '',
            start_date: '',
            end_date: '',
            incharge_user: '',
            percentage: 0
        });

        // form が null または undefined でないことを確認
        if (form) {
            console.log('Form ID:', form.id);
        } else {
            console.error('Form is not initialized!');
        }
        const elementStyle = reactive({
            left: '',
            width: ''
        });

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
            { id: 2, category_id: 1, name: 'テスト2', start_date: '2020-11-19', end_date: '2020-11-23', incharge_user: '佐藤', percentage: 90 }
        ]);

        const block_size = 30; // 1日あたりのピクセル数

        // taskBars の計算されたプロパティを定義
        const taskBars = computed(() => {
            return tasks.value.map((task) => {
                const start = moment(task.start_date);
                const end = moment(task.end_date);
                const duration = end.diff(start, 'days') + 1;
                const left = start.diff(moment(tasks.value[0].start_date), 'days') * block_size;
                const width = duration * block_size;

                return {
                    task,
                    style: {
                        position: 'absolute',
                        left: `${left}px`,
                        width: `${width}px`,
                        height: '20px', // 高さは固定
                        backgroundColor: 'yellow',
                        borderRadius: '5px'
                    }
                };
            });
        });

        // displayTasks computed property
        const displayTasks = computed(() => {
            return tasks.value.filter((task) => {
                return task.percentage < 100; // 例えば、完了していないタスクだけを表示
            });
        });

        // calendarData 内で定義される calendars をテンプレートからアクセス可能にする
        const calendarData = reactive({
            start_month: '2020-10',
            end_month: '2021-02',
            block_size: 30,
            calendars: []
        });

        const getCalendar = () => {
            calendarData.calendars = []; // カレンダーデータを初期化
            let start = moment(calendarData.start_month);
            let end = moment(calendarData.end_month);
            while (start <= end) {
                const daysInMonth = start.daysInMonth();
                let days = [];
                for (let day = 1; day <= daysInMonth; day++) {
                    days.push({
                        day,
                        dayOfWeek: start.clone().date(day).format('ddd')
                    });
                }
                calendarData.calendars.push({
                    month: start.format('YYYY-MM'),
                    days
                });
                start.add(1, 'month');
            }
        };

        const updateTask = (id) => {
            const task = tasks.value.find((task) => task.id === id);
            if (task) {
                Object.assign(task, form);
            }
        };

        const addTask = () => {
            tasks.value.push({ ...form, id: Math.max(0, ...tasks.value.map((t) => t.id)) + 1 });
            Object.keys(form).forEach((key) => (form[key] = ''));
        };

        const deleteTask = (id) => {
            const index = tasks.value.findIndex((task) => task.id === id);
            if (index !== -1) {
                tasks.value.splice(index, 1);
            }
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
            const category = categories.value.find((c) => c.id === id);
            if (category) {
                category.collapsed = !category.collapsed;
            }
        };
        // 計算されたプロパティを定義
        const calendarViewWidth = computed(() => {
            const TASK_LIST_WIDTH = 200;
            return window.innerWidth - TASK_LIST_WIDTH;
        });

        const calendarViewHeight = computed(() => {
            const HEADER_HEIGHT = 50; // 仮定したヘッダーの高さ
            return window.innerHeight - HEADER_HEIGHT;
        });

        const mouseDownMove = (event, task) => {
            event.preventDefault(); // デフォルトのドラッグ動作を防止
            dragging.value = true; // ドラッグ状態を有効に
            activeTask.value = task; // アクティブなタスクを設定
            pageX.value = event.pageX; // 初期のX座標を記録
            console.log('Dragging started for task:', task.name);
        };

        onMounted(() => {
            console.log('Component mounted');
            getCalendar();
            window.addEventListener('resize', () => {});
            window.addEventListener('wheel', () => {});
            window.addEventListener('mousemove', () => {});
            window.addEventListener('mouseup', () => {});
        });

        return {
            mouseDownMove, // ここに追加
            today,
            show,
            updateMode,
            form,
            dragging,
            leftResizing,
            rightResizing,
            activeTask,
            pageX,
            elementStyle,
            resizeInfo,
            categories,
            tasks,
            taskBars,
            block_size,
            calendarViewWidth,
            calendarViewHeight,
            mouseDownMove,
            displayTasks, // ここで displayTasks を返す
            calendarData,
            getCalendar,
            updateTask,
            addTask,
            deleteTask,
            editTask,
            saveTask,
            toggleCategory
        };
    }
};
</script>
