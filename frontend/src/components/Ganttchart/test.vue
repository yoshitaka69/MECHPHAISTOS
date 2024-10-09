<template>
    <div class="gantt-container">
        <div class="gantt-title">ガントチャート</div>
        <!-- 年と月の選択ボタンを追加 -->
        <div class="date-selector">
            <label for="year-select">年</label>
            <select v-model="selectedYear" @change="updateChart">
                <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
            </select>

            <label for="month-select">月</label>
            <select v-model="selectedMonth" @change="updateChart">
                <option v-for="month in monthOptions" :key="month" :value="month">{{ month }}</option>
            </select>
        </div>

        <!-- タスク追加ボタン -->
        <div class="buttons-container">
            <button @click="addTask" class="task-add-button">タスク追加</button>
            <!-- サブタスク追加ボタンを追加 -->
            <button @click="addSubtask" class="task-subtask-button">サブタスク追加</button>
            <!-- タスク削除ボタンを追加 -->
            <button @click="deleteTask" class="task-delete-button">タスク削除</button>
            <!-- 保存ボタン -->
            <button @click="saveTasks" class="task-save-button">保存</button>
            <!-- 読み込みボタンを追加 -->
            <button @click="fetchTasks" class="task-load-button">読み込み</button>
        </div>

        <div id="gantt" class="space-y-8 flex">
            <!-- 左側に入力フォームのヘッダーを追加 -->
            <div class="task-inputs">
                <!-- ヘッダー -->
                <div class="task-input-header">
                    <div class="task-header-item task-checkbox"></div>
                    <!-- チェックボックス用 -->
                    <div class="task-header-item task-name">タスク名</div>
                    <div class="task-header-item task-plant">プラント</div>
                    <div class="task-header-item task-pm-type">PM Type</div>
                    <div class="task-header-item task-date">開始日</div>
                    <div class="task-header-item task-date">終了日</div>
                </div>

                <!-- 入力フォーム -->
                <div v-for="(task, rowIndex) in tasks" :key="task.id" class="task-input-row">
                    <input type="checkbox" v-model="task.selected" class="task-checkbox" />
                    <input type="text" v-model="task.name" placeholder="タスク名" class="task-input task-name" @keydown="moveToNextCell($event, rowIndex, 0)" />
                    <input type="text" v-model="task.plant" placeholder="プラント" class="task-input task-plant" @keydown="moveToNextCell($event, rowIndex, 2)" />
                    <input type="text" v-model="task.pmType" placeholder="PM Type" class="task-input task-pm-type" @keydown="moveToNextCell($event, rowIndex, 3)" />
                    <input type="date" v-model="task.startDate" class="task-input task-date" @keydown="moveToNextCell($event, rowIndex, 4)" />
                    <input type="date" v-model="task.endDate" class="task-input task-date" @keydown="moveToNextCell($event, rowIndex, 5)" />
                </div>
            </div>

            <!-- D3.jsでタスクバーと日付を表示するコンテナ -->
            <div id="gantt-chart-container-2" class="overflow-auto w-full select-none bg-white">
                <!-- 月と日付表示エリア -->
                <div id="month-header" class="month-header"></div>
                <div id="date-header" class="date-header"></div>
                <div id="day-of-week-header" class="day-of-week-header"></div>
                <svg id="gantt-chart"></svg>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import * as d3 from 'd3';
import dayjs from 'dayjs';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaのストアをインポート
import { watch } from 'vue';

// 選択可能な年と月のオプション
const yearOptions = ref([2022, 2023, 2024, 2025]); // 必要に応じて年を追加
const monthOptions = ref([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]);

// デフォルトの年と月
const selectedYear = ref(dayjs().year());
const selectedMonth = ref(dayjs().month() + 1); // dayjsのmonthは0始まりなので+1

// 追加: 現在の日付を取得し、その前後1か月の日付範囲を計算
const today = dayjs(); // 今日の日付

// 日付範囲を表す変数を let に変更
let startDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-01`);
let endDate = startDate.endOf('month');

const tasks = ref([]); // タスクデータ

const rowHeight = 40;
const blockWidth = 30;
let totalDays = endDate.diff(startDate, 'day') + 1;

// 年と月が変更されたときにガントチャートを更新する
function updateChart() {
    startDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-01`); // 月初
    endDate = startDate.endOf('month'); // 月末
    totalDays = endDate.diff(startDate, 'day') + 1;

    // ガントチャートの日付スケールを更新
    xScale.domain([startDate.toDate(), endDate.toDate()]).range([0, blockWidth * totalDays]);

    // チャートを再描画
    fetchTasks(); // 年と月に基づいてタスクデータを取得
}

// xScaleの設定
const xScale = d3
    .scaleTime()
    .domain([startDate.toDate(), endDate.toDate()])
    .range([0, blockWidth * totalDays]);

// タスクデータの取得
async function fetchTasks() {
    const userStore = useUserStore();
    const companyCode = userStore.companyCode;

    try {
        const response = await axios.get('http://127.0.0.1:8000/api/junctionTable/scheduleForGanttByCompany/', {
            params: {
                companyCode: companyCode,
                year: selectedYear.value, // 選択された年を渡す
                month: selectedMonth.value // 選択された月を渡す
            }
        });

        // companyCodeが無い場合も処理する
        const companyData = response.data.find((company: any) => company.companyCode === companyCode);
        tasks.value = companyData ? companyData.ScheduleForGanttList : [];

        updateChartContent(); // ガントチャートを描画
    } catch (error) {
        console.error('タスクの取得エラー:', error);
    }
}

// 保存処理
async function saveTasks() {
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/schedules/save/', tasks.value);
        console.log('Response from server:', response.data);
    } catch (error) {
        console.error('Error saving tasks:', error);
    }
}

// チャートの描画内容を更新する関数
function updateChartContent() {
    const svg = d3.select('#gantt-chart'); // svg要素を取得
    svg.selectAll('*').remove(); // 既存のチャートをクリア

    drawGanttChart(); // ガントチャートを描画
    drawMonthHeader(); // 月ヘッダーの描画
    drawDateHeader(); // 日ヘッダーの描画
    drawDayOfWeekHeader(); // 曜日ヘッダーの描画

    const daysInMonth = dayjs(`${selectedYear.value}-${selectedMonth.value}`).daysInMonth(); // 選択された月の日数
    drawGridLines(svg, daysInMonth); // 縦と横のグリッド線を描画
}

onMounted(() => {
    fetchTasks(); // 初回描画時にタスクを取得
    drawGanttChart();
    drawMonthHeader();
    drawDateHeader();
    drawDayOfWeekHeader();

    // tasksの変更を監視して、日付が変更されたらチャートを更新
    watch(
    tasks,
    (newTasks, oldTasks) => {
        newTasks.forEach((task, index) => {
            // Check if the start or end dates have changed
            if (task.startDate && task.endDate && (task.startDate !== oldTasks[index]?.startDate || task.endDate !== oldTasks[index]?.endDate)) {
                // Recalculate the task bar position and size
                const svg = d3.select('#gantt-chart');
                const taskBar = svg.selectAll('g').filter((d) => d.id === task.id); // Select the task bar by id
                
                const newStartDate = dayjs(task.startDate).toDate();
                const newEndDate = dayjs(task.endDate).add(1, 'day').toDate();
                
                taskBar.select('rect')
                    .attr('x', xScale(newStartDate)) // Update the task's starting position
                    .attr('width', xScale(newEndDate) - xScale(newStartDate)); // Update the task's width
            }
        });
    },
    { deep: true }
);

});

//-----------------------------------------------------------------------------------
// 入力セルでEnterキーが押された場合、次のセルに移動する関数
//-----------------------------------------------------------------------------------
function moveToNextCell(event: KeyboardEvent, rowIndex: number, columnIndex: number) {
    if (event.key === 'Enter') {
        // 各行のすべての入力セルを取得
        const row = document.querySelectorAll('.task-input-row')[rowIndex];
        if (row) {
            const inputs = row.querySelectorAll('input'); // 行内の全てのinput要素を取得
            if (columnIndex + 1 < inputs.length) {
                const nextInput = inputs[columnIndex + 1] as HTMLInputElement;
                nextInput.focus();
            }
        }
    }
}

//-----------------------------------------------------------------------------------

// ガントチャート描画関数にタスクの日付変更に基づく再描画を適用
function drawGanttChart() {
    const daysInMonth = dayjs(`${selectedYear.value}-${selectedMonth.value}`).daysInMonth(); // 選択された月の日数
    const monthHeaderWidth = blockWidth * daysInMonth; // ブロック幅×月の日数で幅を計算

    const svg = d3
        .select('#gantt-chart')
        .attr('width', monthHeaderWidth)
        .attr('height', tasks.value.length * rowHeight);

    // タスクバーの描画
    const bars = svg.selectAll('g').data(tasks.value).enter().append('g');

    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.startDate).toDate())) // タスク開始日をx座標に
        .attr('y', (d, i) => i * rowHeight) // タスクの位置をy座標に
        .attr('width', (d) => Math.max(1, xScale(dayjs(d.endDate).add(1, 'day').toDate()) - xScale(dayjs(d.startDate).toDate()))) // タスク期間の幅を計算
        .attr('height', rowHeight) // 各タスクバーの高さ
        .attr('fill', 'steelblue'); // タスクバーの色

    applyDrag(bars); // ここでドラッグ機能を適用
    applyResize(bars); // ここでリサイズ機能を適用
}

// 縦および横のグリッド線の描画
function drawGridLines(svg, daysInMonth) {
    const daysArray = Array.from({ length: daysInMonth }, (_, i) => i + 1); // 月の日数を取得
    const chartHeight = tasks.value.length * rowHeight; // タスク数に基づいてチャートの高さを計算
    const todayDate = dayjs().format('YYYY-MM-DD'); // 今日の日付を取得

    // 縦グリッド線の描画
    svg.selectAll('.column-grid-line')
        .data(daysArray)
        .enter()
        .append('line')
        .attr('x1', (d) => (d - 1) * blockWidth) // グリッド線の開始x座標
        .attr('x2', (d) => (d - 1) * blockWidth) // グリッド線の終了x座標
        .attr('y1', 0) // グリッド線の開始y座標
        .attr('y2', chartHeight) // グリッド線の終了y座標
        .attr('stroke', '#ccc') // グリッド線の色
        .attr('stroke-width', 1) // グリッド線の太さ
        .attr('class', 'column-grid-line');

    // 今日の日付をハイライト
    svg.selectAll('.today-highlight')
        .data(daysArray)
        .enter()
        .append('rect')
        .attr('x', (d) => (d - 1) * blockWidth) // 今日の日付のx座標
        .attr('y', 0)
        .attr('width', blockWidth) // 1日のブロック幅
        .attr('height', chartHeight) // タスク数に基づくチャートの高さ
        .attr('fill', (d) => {
            const currentDay = dayjs(`${selectedYear.value}-${selectedMonth.value}-${d}`);
            return currentDay.format('YYYY-MM-DD') === todayDate ? '#ffe6e6' : 'none'; // 今日の日付をピンクに
        })
        .attr('class', 'today-highlight');

    // 横グリッド線の描画（タスクごとの水平線）
    svg.selectAll('.row-grid-line')
        .data(tasks.value)
        .enter()
        .append('line')
        .attr('x1', 0) // 水平線の開始x座標
        .attr('x2', blockWidth * daysInMonth) // 水平線の終了x座標（1ヶ月分の幅）
        .attr('y1', (d, i) => (i + 1) * rowHeight) // 各タスクの位置に応じてy座標を設定
        .attr('y2', (d, i) => (i + 1) * rowHeight) // 同じy座標で水平線を引く
        .attr('stroke', '#ccc') // グリッド線の色
        .attr('stroke-width', 1) // グリッド線の太さ
        .attr('class', 'row-grid-line');
}

//-----------------------------------------------------------------------------------

// ドラッグ開始時の処理
function dragStarted(event, d) {
    d3.select(this).raise().attr('stroke', 'black'); // バーを前面に表示し、枠線を黒に変更
}

// ドラッグ中の処理
function dragged(event, d) {
    const newX = event.x; // ドラッグされた新しいx座標
    const numDaysDragged = Math.round(newX / blockWidth); // ドラッグされた日数を計算
    const newStartDate = startDate.add(numDaysDragged, 'day'); // 新しい開始日を計算
    const taskDuration = dayjs(d.endDate).diff(dayjs(d.startDate), 'day'); // タスクの期間を取得
    const newEndDate = newStartDate.add(taskDuration, 'day'); // 新しい終了日を計算

    // ドラッグ中にタスクの日付をリアルタイムに更新
    d.startDate = newStartDate.format('YYYY-MM-DD');
    d.endDate = newEndDate.format('YYYY-MM-DD');

    // バーの位置と幅を更新
    d3.select(this)
        .attr('x', xScale(newStartDate.toDate())) // 新しいx座標に設定
        .attr('width', xScale(newEndDate.toDate()) - xScale(newStartDate.toDate())); // バーの幅を期間に応じて設定
}

// ドラッグ終了時の処理
function dragEnded(event, d) {
    d3.select(this).attr('stroke', null); // ドラッグ終了後に枠線を元に戻す
    updateTaskDates(d); // タスク全体を渡すように修正
}

// D3.jsのドラッグイベントをバーに適用する関数
function applyDrag(bars) {
    bars.call(
        d3
            .drag()
            .on('start', dragStarted) // ドラッグ開始時のイベント
            .on('drag', dragged) // ドラッグ中のイベント
            .on('end', dragEnded)
    ); // ドラッグ終了時のイベント
}

function applyResize(bars) {
    // 右端のリサイズハンドル (終了日を変更)
    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.endDate).add(1, 'day').toDate()) - 10) // 右端のハンドルの位置を終了日に合わせる
        .attr('y', (d, i) => i * rowHeight)
        .attr('width', 10) // ハンドルの幅を20pxに広げる
        .attr('height', rowHeight)
        .attr('fill', 'gray')
        .attr('cursor', 'ew-resize') // 右端でリサイズできるときのカーソル
        .call(
            d3
                .drag()
                .on('start', resizeStarted)
                .on('drag', resizeRight) // 右端のリサイズ処理
                .on('end', resizeEnded)
        );

    // 左端のリサイズハンドル (開始日を変更)
    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.startDate).toDate()) - 10) // 左端のハンドルの位置調整
        .attr('y', (d, i) => i * rowHeight)
        .attr('width', 10) // ハンドルの幅を20pxに広げる
        .attr('height', rowHeight)
        .attr('fill', 'gray')
        .attr('cursor', 'ew-resize') // 左端でリサイズできるときのカーソル
        .call(
            d3
                .drag()
                .on('start', resizeStarted)
                .on('drag', resizeLeft) // 左端のリサイズ処理
                .on('end', resizeEnded)
        );
}


// リサイズ開始時の処理
function resizeStarted(event, d) {
    d3.select(this).raise().attr('stroke', 'black');
}

// 右端のリサイズ処理 (終了日を変更)
function resizeRight(event, d) {
    const newX = event.x;
    const newEndDate = dayjs(xScale.invert(newX));

    if (!newEndDate.isValid()) {
        console.error('Invalid End Date:', newEndDate);
        return;
    }

    d.endDate = newEndDate.format('YYYY-MM-DD');

    d3.select(this.parentNode).select('rect')
        .attr('width', xScale(newEndDate.toDate()) - xScale(dayjs(d.startDate).toDate()));

    updateTaskDates(d);
}

// 左端のリサイズ処理 (開始日を変更)
function resizeLeft(event, d) {
    const newX = event.x;
    const newStartDate = dayjs(xScale.invert(newX));

    if (!newStartDate.isValid()) {
        console.error('Invalid Start Date:', newStartDate);
        return;
    }

    d.startDate = newStartDate.format('YYYY-MM-DD');

    d3.select(this.parentNode).select('rect')
        .attr('x', xScale(newStartDate.toDate()))
        .attr('width', xScale(dayjs(d.endDate).toDate()) - xScale(newStartDate.toDate()));

    updateTaskDates(d);
}

// リサイズ終了時の処理
function resizeEnded(event, d) {
    d3.select(this).attr('stroke', null);
    updateTaskDates(d); // 日付を保存
}

//月、日、曜日の表示関数
//-----------------------------------------------------------------------------------

// 月ヘッダー
function drawMonthHeader() {
    const monthHeader = d3.select('#month-header');
    const monthData = [{ month: `${selectedYear.value}年 ${selectedMonth.value}月`, daysInMonth: dayjs(`${selectedYear.value}-${selectedMonth.value}`).daysInMonth() }];

    monthHeader
        .style('width', `${blockWidth * monthData[0].daysInMonth}px`)
        .style('display', 'flex')
        .style('overflow', 'hidden');

    monthHeader
        .selectAll('div')
        .data(monthData)
        .enter()
        .append('div')
        .style('width', `${blockWidth * monthData[0].daysInMonth}px`)
        .text((d) => d.month)
        .style('text-align', 'center')
        .style('border-right', '1px solid black');
}

// 日ヘッダー
function drawDateHeader() {
    const dateHeader = d3.select('#date-header');
    const daysInMonth = dayjs(`${selectedYear.value}-${selectedMonth.value}`).daysInMonth();
    const dateData = Array.from({ length: daysInMonth }, (_, i) => i + 1);

    dateHeader
        .style('width', `${blockWidth * daysInMonth}px`)
        .style('display', 'flex')
        .style('overflow', 'hidden');

    dateHeader
        .selectAll('div')
        .data(dateData)
        .enter()
        .append('div')
        .style('width', `${blockWidth}px`)
        .style('text-align', 'center')
        .style('border-right', '1px solid black')
        .style('background-color', (d) => {
            const currentDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-${d}`);
            return currentDate.isSame(dayjs(), 'day') ? '#ffe6e6' : '#f0f0f0';
        })
        .text((d) => d);
}

// 曜日ヘッダー
function drawDayOfWeekHeader() {
    const dayOfWeekHeader = d3.select('#day-of-week-header');
    const daysInMonth = dayjs(`${selectedYear.value}-${selectedMonth.value}`).daysInMonth();
    const dayOfWeekData = Array.from({ length: daysInMonth }, (_, i) => {
        const date = dayjs(`${selectedYear.value}-${selectedMonth.value}-${i + 1}`);
        return date.format('dd');
    });

    dayOfWeekHeader
        .style('width', `${blockWidth * daysInMonth}px`)
        .style('display', 'flex')
        .style('overflow', 'hidden');

    dayOfWeekHeader
        .selectAll('div')
        .data(dayOfWeekData)
        .enter()
        .append('div')
        .style('width', `${blockWidth}px`)
        .style('text-align', 'center')
        .style('border-right', '1px solid black')
        .style('color', (d) => (d === 'Sun' ? 'red' : d === 'Sat' ? 'blue' : 'black'))
        .style('background-color', (d, i) => {
            const currentDate = dayjs(`${selectedYear.value}-${selectedMonth.value}-${i + 1}`);
            return currentDate.isSame(dayjs(), 'day') ? '#ffe6e6' : '#f0f0f0';
        })
        .text((d) => d);
}

// 日付の更新時にガントチャートを再描画
function updateTaskDates(task) {
    task.startDate = dayjs(task.startDate).format('YYYY-MM-DD');
    task.endDate = dayjs(task.endDate).format('YYYY-MM-DD');
    updateChartContent(); // タスクの日付に基づいてチャートを再描画
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
        target.element.style.transform = `translateX(${realX}px)`;  // スムーズな位置変更
        target.element.style.width = `${realWidth}px`;  // スムーズな幅の変更
    }
}

function calcResizeWidth(currentPageX, direction) {
    const diff = target.pageX - currentPageX;
    const widthAdjustment = direction === 'left' ? diff : -diff;
    const newWidth = keepThreshold(target.task.pos.width + widthAdjustment, BLOCK_SIZE, contentWidth.value - target.task.pos.x);
    
    return newWidth;
}

function calcResizePositionX(currentPageX) {
    const diff = target.pageX - currentPageX;
    const newPosition = keepThreshold(target.task.pos.x - diff, 0, target.task.pos.x + target.task.pos.width - BLOCK_SIZE);
    
    return newPosition;
}

function keepThreshold(value, min, max) {
    return Math.min(Math.max(value, min), max);
}


function onMouseDown_ResizeStop(e) {
    if (leftResizing.value || rightResizing.value) {
        const realWidth = calcResizeWidth(e.pageX, target.direction);
        const daysChanged = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE);

        if (daysChanged !== 0) {
            const task = target.taskList.find(t => t.id === target.task.id);
            if (leftResizing.value) {
                task.startDate = dayjs(task.startDate).add(daysChanged, 'day').format('YYYY-MM-DD');
            } else {
                task.endDate = dayjs(task.endDate).add(-daysChanged, 'day').format('YYYY-MM-DD');
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

</script>

<style scoped>
.gantt-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: white; /* 背景を白に変更 */
}

.gantt-title {
    font-size: 2rem; /* 文字サイズを大きく */
    font-weight: bold; /* 太字 */
    text-align: left; /* 左寄せに変更 */
    margin-bottom: 20px; /* ボタンとの間に余白を追加 */
}

/* タスク入力ヘッダーのスタイル */
.task-input-header {
    display: flex;
    font-weight: bold;
    text-align: center;
    background-color: #28a745; /* 緑色に変更 */
    border-bottom: 2px solid black;
    height: 90px; /* ヘッダーの高さ */
    align-items: center;
}

/* 各項目のスタイル */
.task-header-item,
.task-input {
    padding: 10px;
    border-right: 1px solid black;
    height: 100%; /* ヘッダーと入力フォームの高さを揃える */
}

/* 各列の幅を統一 */
.task-name,
.task-plant,
.task-pm-type,
.task-date {
    width: 150px; /* 各項目の横幅を150pxに統一 */
}

/* 入力フォームのスタイル */
.task-input-row {
    display: flex;
    height: 40px;
    margin: 0;
}

.task-input {
    margin: 0;
    padding: 5px;
    height: 100%;
    border: 1px solid black;
    border-top: none;
}

/* 月のヘッダー */
.month-header {
    display: flex;
    justify-content: flex-start;
    padding: 0px;
    background-color: #f0f0f0;
    border-bottom: 1px solid black;
    font-size: 1.2rem;
    height: 30px;
}

/* 日付ヘッダー */
.date-header {
    display: flex;
    justify-content: flex-start;
    padding: 0px;
    background-color: #f0f0f0;
    border-bottom: 1px solid black;
    height: 30px;
}

/* 曜日ヘッダー */
.day-of-week-header {
    display: flex;
    justify-content: flex-start;
    padding: 0px;
    background-color: #f0f0f0;
    border-bottom: 1px solid black;
    height: 30px;
}

/* 日付と曜日のスタイル */
.date-header div,
.day-of-week-header div {
    width: 30px;
    text-align: center;
}

/* buttons-container を横並びにするための修正 */
.buttons-container {
    display: flex; /* 横並びに配置 */
    flex-direction: row; /* 水平方向に並べる */
    gap: 10px; /* ボタン間の隙間を追加 */
    margin-bottom: 20px; /* ガントチャートの他の要素との間に余白を追加 */
}

/* タスク追加ボタンのスタイル */
.task-add-button {
    margin-bottom: 10px;
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.task-add-button:hover {
    background-color: #0056b3;
}

/* 保存ボタンのスタイル */
.task-save-button {
    margin-bottom: 10px;
    padding: 8px 16px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.task-save-button:hover {
    background-color: #218838;
}

/* 読み込みボタンのスタイルを追加 */
.task-load-button {
    margin-bottom: 10px;
    padding: 8px 16px;
    background-color: #17a2b8; /* ブルー系の色 */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.task-load-button:hover {
    background-color: #138496;
}

/* タスク削除ボタンのスタイル */
.task-delete-button {
    margin-bottom: 10px;
    padding: 8px 16px;
    background-color: #dc3545; /* レッド系の色 */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.task-delete-button:hover {
    background-color: #c82333;
}

/* チェックボックスのスタイルを追加 */
.task-checkbox {
    width: 30px;
    height: 30px;
    margin: 5px;
}

/* サブタスク追加ボタンのスタイルを追加 */
.task-subtask-button {
    margin-bottom: 10px;
    padding: 8px 16px;
    background-color: #ffc107; /* イエロー系の色 */
    color: black;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.task-subtask-button:hover {
    background-color: #e0a800;
}

/* サブタスク名の入力セルのスタイル */
.task-subtask-name {
    width: 150px;
    padding: 5px;
    border-right: 1px solid black;
    height: 100%;
}
</style>
