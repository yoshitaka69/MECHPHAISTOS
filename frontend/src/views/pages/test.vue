<template>
    <div id="app" v-if="form && calendarData.calendars">
        <div id="gantt-header" style="height: 3rem; padding: 0.5rem; display: flex; align-items: center">
            <h1 style="font-size: 0.875rem; font-weight: bold">ガントチャート</h1>
            <button @click="addTask" style="background-color: #4f46e5; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; display: flex; align-items: center; font-size: 0.75rem; font-weight: bold">
                <svg style="width: 1rem; height: 1rem" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                タスクを追加する
            </button>
            <TaskForm :show.sync="show" :updateMode="updateMode" :form="form" :categories="categories" />
        </div>

        <!--左側のタスクリスト領域-->
        <div id="gantt-content" style="display: flex">
            <div id="gantt-task">
                <div id="gantt-task-title" style="display: flex; background-color: #059669; color: white; height: 5rem" ref="task">
                    <div style="border-style: solid; border-color: black; border-width: 1px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; width: 12rem; height: 100%">タスク</div>
                    <div style="border-style: solid; border-color: black; border-width: 1px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; width: 6rem; height: 100%">開始日</div>
                    <div style="border-style: solid; border-color: black; border-width: 1px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; width: 6rem; height: 100%">完了期限日</div>
                    <div style="border-style: solid; border-color: black; border-width: 1px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; width: 4rem; height: 100%">担当</div>
                    <div style="border-style: solid; border-color: black; border-width: 1px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.75rem; width: 3rem; height: 100%">進捗</div>
                </div>

                <!--左側のタスクリストの下の領域-->
                <div id="gantt-task-list">
                    <div v-for="(lists, index) in lists" :key="index" class="task-list-item">
                        <template v-if="lists.cat === 'category'">
                            <div class="task-category">
                                {{ lists.name }}
                            </div>
                        </template>
                        <template v-else>
                            <div class="task-detail-name">
                                {{ lists.name }}
                            </div>
                            <div class="task-detail-date">
                                {{ lists.start_date }}
                            </div>
                            <div class="task-detail-date">
                                {{ lists.end_date }}
                            </div>
                            <div class="task-detail-incharge">
                                {{ lists.incharge_user }}
                            </div>
                            <div class="task-detail-percentage">{{ lists.percentage }}%</div>
                        </template>
                    </div>
                </div>
            </div>

            <!--右側のカレンダー領域-->
            <div id="gantt-calendar" class="overflow-x-scroll overflow-y-hidden border-l" :style="`width:${calendarViewWidth}px`" ref="calendar">
                <div id="gantt-date" class="h-20">
                    <!--青い帯の月の表示部分カレンダー領域-->
                    <div id="gantt-year-month" class="relative h-8">
                        <div v-for="(calendar, index) in calendarData.calendars" :key="index">
                            <div class="year-month-block" :style="`width:${calendar.calendar * block_size}px; left:${calendar.start_block_number * block_size}px`">
                                {{ calendar.date }}
                            </div>
                        </div>
                    </div>

                    <!--日付の表示部分カレンダー領域-->
                    <div v-if="calendarData.calendars && calendarViewHeight" :style="{ position: 'relative', height: calendarViewHeight + 'px' }">
                        <div v-for="(calendar, calendarIndex) in calendarData.calendars" :key="calendarIndex">
                            <div v-for="(day, dayIndex) in calendar.days" :key="dayIndex">
                                <div
                                    class="day-block"
                                    :class="{
                                        saturday: day.dayOfWeek === '土',
                                        sunday: day.dayOfWeek === '日',
                                        'today-highlight': calendar.year === today.year() && calendar.month === today.month() && day.day === today.date()
                                    }"
                                    :style="{
                                        width: `${block_size}px`,
                                        left: `${day.block_number * block_size}px`,
                                        minHeight: '20px',
                                        height: `${calendarViewHeight}px`,
                                        backgroundColor: getBackgroundColor(day, calendar),
                                        display: 'flex',
                                        flexDirection: 'column',
                                        justifyContent: 'flex-start',
                                        alignItems: 'center',
                                        borderBottom: '1px solid #ccc'
                                    }"
                                >
                                    <span>{{ day.day }}</span>
                                    <span>{{ day.dayOfWeek }}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!--タスクバー領域の表示部分カレンダー領域-->
                    <div v-if="calendarData.calendars && calendarViewHeight" :style="{ position: 'relative', height: calendarViewHeight + 'px' }">
                        <div v-for="(calendar, calendarIndex) in calendarData.calendars" :key="calendarIndex">
                            <div v-for="(day, dayIndex) in calendar.days" :key="dayIndex">
                                <div
                                    class="day-block"
                                    :class="{
                                        saturday: day.dayOfWeek === '土',
                                        sunday: day.dayOfWeek === '日',
                                        'today-highlight': calendar.year === today.year() && calendar.month === today.month() && day.day === today.date()
                                    }"
                                    :style="{
                                        width: `${block_size}px`,
                                        left: `${day.block_number * block_size}px`,
                                        height: `${calendarViewHeight}px`,
                                        backgroundColor: getBackgroundColor(day, calendar)
                                    }"
                                ></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!--ガントバー領域-->
                <div id="gantt-bar-area" style="position: relative; width: var(--calendarViewWidth); height: var(--calendarViewHeight)">
                    <div v-for="(bar, index) in taskBars" :key="index">
                        <div v-if="bar.task.cat === 'task'" :style="{ ...bar.style, backgroundColor: getBarBackgroundColor(bar.task.start_date, bar.task.end_date) }" class="gantt-bar" @mousedown="mouseDownMove(bar.task)">
                            <div class="progress-bar-container">
                                <div class="progress-bar" :style="{ width: bar.task.percentage + '%', backgroundColor: getProgressBarColor(bar.task.start_date, bar.task.end_date) }" :class="{ 'rounded-complete': bar.task.percentage === 100 }"></div>
                            </div>
                            <div class="resize-handle-left"></div>
                            <div class="resize-handle-right"></div>
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
            categories: false
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

        const categories = ref([{ id: 1, name: 'テストA', collapsed: false }]);

        const tasks = ref([
            {
                id: 1,
                category_id: 1,
                name: 'テスト1',
                start_date: '2020-11-18',
                end_date: '2020-11-20',
                incharge_user: '鈴木',
                percentage: 100
            },
            {
                id: 2,
                category_id: 1,
                name: 'テスト2',
                start_date: '2020-11-19',
                end_date: '2020-11-23',
                incharge_user: '佐藤',
                percentage: 90
            },
            {
                id: 3,
                category_id: 1,
                name: 'テスト3',
                start_date: '2020-11-19',
                end_date: '2020-12-04',
                incharge_user: '鈴木',
                percentage: 40
            },
            {
                id: 3,
                category_id: 1,
                name: 'テスト3',
                start_date: '2020-11-19',
                end_date: '2020-12-04',
                incharge_user: '鈴木',
                percentage: 40
            },
            {
                id: 3,
                category_id: 1,
                name: 'テスト3',
                start_date: '2020-11-19',
                end_date: '2020-12-04',
                incharge_user: '鈴木',
                percentage: 40
            },
            {
                id: 3,
                category_id: 1,
                name: 'テスト3',
                start_date: '2020-11-19',
                end_date: '2020-12-04',
                incharge_user: '鈴木',
                percentage: 40
            },
            {
                id: 3,
                category_id: 1,
                name: 'テスト3',
                start_date: '2020-11-19',
                end_date: '2020-12-04',
                incharge_user: '鈴木',
                percentage: 40
            }
        ]);

        const lists = computed(() => {
            let combinedLists = [];
            categories.value.forEach((category) => {
                combinedLists.push({ cat: 'category', ...category });
                tasks.value.forEach((task) => {
                    if (task.category_id === category.id) {
                        combinedLists.push({ cat: 'task', ...task });
                    }
                });
            });
            return combinedLists;
        });

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

        const getDayBackgroundColor = (day, calendar) => {
            // `today.value` を使用して、moment オブジェクトの現在の値にアクセス
            if (calendar.year === today.value.year() && calendar.month === today.value.month() + 1 && day.day === today.value.date()) {
                return '#ffd700'; // 今日の日付の背景色を黄色に
            } else if (day.dayOfWeek === '土') {
                return '#ebf8ff'; // 土曜日は薄い青
            } else if (day.dayOfWeek === '日') {
                return '#fee2e2'; // 日曜日は薄い赤
            } else {
                return 'white'; // その他の日は白色
            }
        };

        const getDayTextColor = (day, calendar) => {
            if (calendar.year === today.value.year() && calendar.month === today.value.month() + 1 && day.day === today.value.date()) {
                return 'black'; // 今日のテキスト色を黒に
            } else {
                return 'black'; // その他の日も黒
            }
        };

        // 土日に色をつけ、それ以外は白色にする関数
        const getBarBackgroundColor = (startDate, endDate) => {
            let startMoment = moment(startDate);
            let endMoment = moment(endDate);
            let isWeekend = false; // 土日かどうかのフラグ

            while (startMoment <= endMoment) {
                if (startMoment.day() === 0 || startMoment.day() === 6) {
                    isWeekend = true;
                    break;
                }
                startMoment.add(1, 'days');
            }

            if (isWeekend) {
                return startMoment.day() === 6 ? '#ebf8ff' : '#fee2e2'; // 土曜日は青、日曜日は赤
            }
            return 'white'; // 土日以外は白色
        };

        // プログレスバーの色を取得する関数
        const getProgressBarColor = (startDate, endDate) => {
            let startMoment = moment(startDate);
            let endMoment = moment(endDate);
            return startMoment.isBefore(today.value, 'day') && endMoment.isAfter(today.value, 'day') ? '#fcd34d' : '#cccccc'; // 今日を含む場合は黄色、それ以外はグレー
        };

        const getDays = (year, month, block_number) => {
            const dayOfWeek = ['日', '月', '火', '水', '木', '金', '土'];
            let days = [];
            let date = moment(`${year}-${month}-01`);
            let num = date.daysInMonth();
            for (let i = 0; i < num; i++) {
                days.push({
                    day: date.date(),
                    dayOfWeek: dayOfWeek[date.day()],
                    block_number
                });
                date.add(1, 'day');
                block_number++;
            }
            return days;
        };

        const getCalendar = () => {
            let block_number = 0;
            let start_month = moment(calendarData.start_month);
            let end_month = moment(calendarData.end_month);
            let between_month = end_month.diff(start_month, 'months');

            for (let i = 0; i <= between_month; i++) {
                let days = getDays(start_month.year(), start_month.format('MM'), block_number);
                calendarData.calendars.push({
                    date: start_month.format('YYYY年MM月'),
                    year: start_month.year(),
                    month: start_month.month(),
                    start_block_number: block_number,
                    calendar: days.length,
                    days: days
                });
                start_month.add(1, 'month');
                block_number = days[days.length - 1].block_number + 1;
            }
        };

        // calendarData 内で定義される calendars をテンプレートからアクセス可能にする
        const calendarData = reactive({
            start_month: '2020-10',
            end_month: '2021-02',
            block_size: 30,
            calendars: []
        });

        const addTask = () => {
            tasks.value.push({ ...form, id: Math.max(0, ...tasks.value.map((t) => t.id)) + 1 });
            Object.keys(form).forEach((key) => (form[key] = ''));
        };

        const toggleCategory = (id) => {
            const category = categories.value.find((c) => c.id === id);
            if (category) {
                category.collapsed = !category.collapsed;
            }
        };

        // 計算されたプロパティを定義
        const calendarViewWidth = computed(() => window.innerWidth - 200);
        const calendarViewHeight = computed(() => window.innerHeight - 50);

        const mouseDownMove = (event, task) => {
            event.preventDefault(); // デフォルトのドラッグ動作を防止
            dragging.value = true; // ドラッグ状態を有効に
            activeTask.value = task; // アクティブなタスクを設定
            pageX.value = event.pageX; // 初期のX座標を記録
            console.log('Dragging started for task:', task.name);
        };

        console.log('Calendar View Height:', calendarViewHeight.value); // Vue 3 の Refs は .value でアクセス

        onMounted(() => {
            console.log('Calendar Data:', calendarData.calendars);
            getCalendar();
            window.addEventListener('resize', () => {});
            window.addEventListener('wheel', () => {});
            window.addEventListener('mousemove', () => {});
            window.addEventListener('mouseup', () => {});
        });

        // スタイル取得関数
        const getBackgroundColor = (day, calendar) => {
            if (day.dayOfWeek === '土') {
                return '#ebf8ff'; // 土曜日は薄い青
            } else if (day.dayOfWeek === '日') {
                return '#fee2e2'; // 日曜日は薄い赤
            } else if (calendar.year === moment().year() && calendar.month === moment().month() && day.day === moment().date()) {
                return '#ff6347'; // 今日の日付
            }
            return 'white'; // それ以外の日
        };

        return {
            today,
            getDays,
            getCalendar,
            calendarData,
            categories,
            tasks,
            lists,
            getDayBackgroundColor,
            getDayTextColor,
            getBarBackgroundColor,
            getProgressBarColor,
            getBackgroundColor,

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

            taskBars,
            block_size,


            calendarViewWidth,
            calendarViewHeight,
            mouseDownMove,


            
            displayTasks,

            addTask,
            toggleCategory
        };
    }
};
</script>

<style scoped>
/* カレンダー全体のスタイル設定 */
#gantt-calendar {
    overflow-x: scroll; /* 横スクロールを有効に */
}

/* 日付表示エリアの高さ設定 */
#gantt-date {
    height: 80px; /* 必要に応じて調整 */
}

/* 年月表示エリアのスタイル */
#gantt-year-month {
    position: absolute;
    top: -0.5rem; /* gantt-task-title の高さに一致するマイナス値を設定 */
    left: 0;
    width: 100%; /* 必要に応じて調整 */
    z-index: 10; /* 必要に応じて他の要素の上に表示 */
    height: 32px;
    color: white; /* テキスト色 */
}

/* 年月表示エリアの内部divスタイル */
.year-month-block {
    background-color: #4f46e5; /* 濃い青色 */
    color: white; /* テキスト色を白に */
    border: 0.5px solid black; /* 境界線を黒で統一 */
    height: 2.8rem; /* 高さを3remに設定 */
    position: absolute; /* 絶対位置指定 */
    font-weight: bold; /* フォントの太さ */
    font-size: 0.875rem; /* フォントサイズ */
    display: flex; /* Flexboxを使用 */
    align-items: center; /* 中央揃え（垂直） */
    justify-content: center; /* 中央揃え（水平） */
    width: 100%; /* 幅を親要素に合わせて調整（必要に応じて） */
}

/* 基本的な日のブロックのスタイル */
.day-block {
    border-right: 1px solid black;
    border-bottom: 1px solid #ccc; /* 薄い灰色の下線 */
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    font-weight: bold;
    font-size: 0.875rem;
    min-height: 20px; /* 最小高さを保証 */
}

/* 土曜日と日曜日のスタイル */
.saturday {
    background-color: #ebf8ff; /* 土曜日は薄い青 */
}

.sunday {
    background-color: #fee2e2; /* 日曜日は薄い赤 */
}

/* 特定の日（今日など）をハイライトするスタイル */
.today-highlight {
    background-color: #ffd700; /* 今日の日付を黄色でハイライト */
}

/* バーエリアの位置設定 */
.gantt-bar {
    position: absolute;
    height: 20px;
    background-color: white; /* デフォルトは白色 */
    border-radius: 10px;
}

.progress-bar-container {
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.progress-bar {
    height: 100%;
    background-color: #fcd34d; /* デフォルトはダークイエロー */
    border-radius: 10px 0 0 10px;
}

.resize-handle-left,
.resize-handle-right {
    width: 4px;
    height: 4px;
    background-color: #e5e7eb;
    border: 1px solid black;
    position: absolute;
    top: 6px;
    cursor: col-resize;
}

.resize-handle-left {
    left: -6px;
}

.resize-handle-right {
    right: -6px;
}

/*gantt-task-list*/
.task-list-item {
    display: flex;
    height: 40px; /* 要素の高さ */
    border-bottom: 1px solid #e5e7eb; /* 下境界線 */
    background-color: white; /* 背景色を白に設定 */
}

.task-category {
    display: flex;
    align-items: center;
    width: 100%;
    color: black; /* 文字色を黒に設定 */
    padding-left: 0.5rem; /* 左パディング */
    font-weight: bold;
    font-size: 0.875rem; /* フォントサイズ */
    background-color: white; /* 背景色を白に設定 */
}

.task-detail-name {
    width: 12rem; /* タスクの幅を設定 */
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.75rem;
    border-right: 1px solid #e5e7eb;
}

.task-detail-date {
    width: 6rem; /* 開始日の幅を設定 */
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.75rem;
    border-right: 1px solid #e5e7eb;
}

.task-detail-incharge {
    width: 4rem; /* 担当の幅を設定 */
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.75rem;
    border-right: 1px solid #e5e7eb;
}

.task-detail-percentage {
    width: 3rem; /* 進捗の幅を設定 */
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 0.75rem;
}

.task-list-item:first-child {
    font-weight: bold;
    background-color: #059669; /* 背景色 */
    color: white; /* 文字色 */
}
</style>
