<template>
    <div class="gantt-container">
        <div class="gantt-title">ガントチャート</div>

        <!-- タスク追加ボタン -->
        <div class="buttons-container">
            <button @click="addTask" class="task-add-button">タスク追加</button>
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
                    <div class="task-header-item task-checkbox"></div> <!-- チェックボックス用 -->
                    <div class="task-header-item task-name">タスク名</div>
                    <div class="task-header-item task-plant">プラント</div>
                    <div class="task-header-item task-pm-type">PM Type</div>
                    <div class="task-header-item task-date">開始日</div>
                    <div class="task-header-item task-date">終了日</div>
                </div>

                <!-- 入力フォーム -->
                <div v-for="(task, index) in tasks" :key="task.id" class="task-input-row">
                    <input type="checkbox" v-model="task.selected" class="task-checkbox" /> <!-- チェックボックス -->
                    <input type="text" v-model="task.name" placeholder="タスク名" class="task-input task-name" @change="updateTaskName(index, task.name)" />
                    <input type="text" v-model="task.plant" placeholder="プラント" class="task-input task-plant" />
                    <input type="text" v-model="task.pmType" placeholder="PM Type" class="task-input task-pm-type" />
                    <input type="date" v-model="task.startDate" class="task-input task-date" @change="updateTaskDates(index)" />
                    <input type="date" v-model="task.endDate" class="task-input task-date" @change="updateTaskDates(index)" />
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

// 追加: 現在の日付を取得し、その前後1か月の日付範囲を計算
const today = dayjs(); // 今日の日付
const startDate = today.subtract(1, 'month'); // 1か月前
const endDate = today.add(1, 'month'); // 1か月後

const tasks = ref([]); // タスクデータ

const rowHeight = 40;
const blockWidth = 30;
const totalDays = endDate.diff(startDate, 'day') + 1; // 表示する合計日数

// xScaleの修正: 現在の日付を基準に前後1か月のスケールを計算
const xScale = d3
    .scaleTime()
    .domain([startDate.toDate(), endDate.toDate()]) // 追加: 前後1か月の日付範囲を設定
    .range([0, blockWidth * totalDays]); // 表示する日数に応じて幅を設定

// タスクデータを取得する関数
async function fetchTasks() {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/schedules/');
        tasks.value = response.data;
        updateChart();
    } catch (error) {
        console.error('Error fetching tasks:', error);
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

onMounted(() => {
    fetchTasks();
    drawGanttChart();
    drawMonthHeader();
    drawDateHeader();
    drawDayOfWeekHeader();
});

// ガントチャート描画関数
function drawGanttChart() {
    const svg = d3
        .select('#gantt-chart')
        .attr('width', blockWidth * totalDays) // 修正: 表示する日数に応じた幅
        .attr('height', tasks.value.length * rowHeight);

    drawVerticalGridLines(svg);

    svg.selectAll('.row-grid-line')
        .data(tasks.value)
        .enter()
        .append('line')
        .attr('x1', 0)
        .attr('x2', blockWidth * totalDays) // 修正: 表示する日数に応じたグリッド線の幅
        .attr('y1', (d, i) => (i + 1) * rowHeight)
        .attr('y2', (d, i) => (i + 1) * rowHeight)
        .attr('stroke', 'black');

    const drag = d3.drag().on('start', dragStarted).on('drag', dragged).on('end', dragEnded);

    const resizeLeft = d3.drag().on('start', resizeStarted).on('drag', resizingLeft).on('end', resizeEnded);

    const resizeRight = d3.drag().on('start', resizeStarted).on('drag', resizingRight).on('end', resizeEnded);

    // タスクバーの描画
    const bars = svg.selectAll('g').data(tasks.value).enter().append('g');

    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.startDate).toDate())) // 修正: 日付範囲に基づいてバーの位置を調整
        .attr('y', (d, i) => i * rowHeight)
        .attr('width', (d) => xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()))
        .attr('height', rowHeight)
        .attr('fill', 'steelblue')
        .call(drag);

    // 左側のリサイズハンドルを追加
    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.startDate).toDate()) - 5)
        .attr('y', (d, i) => i * rowHeight)
        .attr('width', 10)
        .attr('height', rowHeight)
        .attr('fill', 'gray')
        .attr('cursor', 'ew-resize')
        .call(resizeLeft); // 左端のリサイズハンドルを追加

    // 右側のリサイズハンドルを追加
    bars.append('rect')
        .attr('x', (d) => xScale(dayjs(d.endDate).toDate()) - 5)
        .attr('y', (d, i) => i * rowHeight)
        .attr('width', 10)
        .attr('height', rowHeight)
        .attr('fill', 'gray')
        .attr('cursor', 'ew-resize')
        .call(resizeRight); // 右端のリサイズハンドルを追加

    svg.selectAll('text')
        .data(tasks.value)
        .enter()
        .append('text')
        .attr('x', (d) => xScale(dayjs(d.startDate).toDate()) + 5)
        .attr('y', (d, i) => i * rowHeight + rowHeight / 2 + 5)
        .text((d) => d.name)
        .attr('fill', 'white');
}

// ドラッグ開始時の処理
function dragStarted(event, d) {
    d3.select(this).raise().attr('stroke', 'black');
}

// ドラッグ中の処理
function dragged(event, d) {
    const newX = event.x;
    const numDaysDragged = Math.round(newX / blockWidth); // ドラッグされた日数を計算

    const newStartDate = startDate.add(numDaysDragged, 'day'); // 修正: currentMonthではなくstartDateを基準に計算
    const taskDuration = dayjs(d.endDate).diff(dayjs(d.startDate), 'day');
    const newEndDate = newStartDate.add(taskDuration, 'day');

    // 開始日と終了日を更新
    d.startDate = newStartDate.format('YYYY-MM-DD');
    d.endDate = newEndDate.format('YYYY-MM-DD');

    // バーの位置を更新
    d3.select(this)
        .attr('x', newX)
        .attr('width', blockWidth * (taskDuration + 1));
}

// ドラッグ終了時の処理
function dragEnded(event, d) {
    d3.select(this).attr('stroke', null);
    updateTaskDates(d.id); // 日付をフォームに反映
}

// リサイズ開始時の処理
function resizeStarted(event, d) {
    d3.select(this).raise().attr('stroke', 'black');
}

// 左端リサイズ中の処理
function resizingLeft(event, d) {
    const newX = event.x;
    const numDaysResized = Math.round(newX / blockWidth);

    const newStartDate = startDate.add(numDaysResized, 'day'); // 修正: currentMonthではなくstartDateを基準に計算
    d.startDate = newStartDate.format('YYYY-MM-DD');

    d3.select(this.parentNode)
        .select('rect')
        .attr('x', newX)
        .attr('width', xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()));
}

// 右端リサイズ中の処理
function resizingRight(event, d) {
    const newX = event.x;
    const numDaysResized = Math.round(newX / blockWidth);

    const newEndDate = startDate.add(numDaysResized, 'day'); // 修正: currentMonthではなくstartDateを基準に計算
    d.endDate = newEndDate.format('YYYY-MM-DD');

    d3.select(this.parentNode)
        .select('rect')
        .attr('width', xScale(dayjs(d.endDate).toDate()) - xScale(dayjs(d.startDate).toDate()));
}

// リサイズ終了時の処理
function resizeEnded(event, d) {
    d3.select(this).attr('stroke', null);
    updateTaskDates(d.id); // 日付をフォームに反映
}

// 月のヘッダーを表示する関数
function drawMonthHeader() {
    // 修正: currentMonthではなく、startDateを使用
    const monthHeader = d3.select('#month-header');

    monthHeader
        .append('div')
        .style('display', 'inline-block')
        .style('width', `${blockWidth * totalDays}px`) // 表示する日数に基づいて幅を設定
        .style('text-align', 'center')
        .style('font-weight', 'bold')
        .text(startDate.format('MMMM YYYY')); // 開始日の月と年を表示
}

// 日付のヘッダーを表示する関数
function drawDateHeader() {
    const dateHeader = d3.select('#date-header');

    for (let i = 0; i < totalDays; i++) {
        const currentDay = startDate.add(i, 'day');
        const dayOfWeek = currentDay.day();

        dateHeader.append('div').style('display', 'inline-block').style('width', `${blockWidth}px`).style('text-align', 'center').style('color', getDayColor(dayOfWeek)).style('border-right', '1px solid black').text(currentDay.format('D'));
    }
}

// 曜日ヘッダーを表示する関数
function drawDayOfWeekHeader() {
    const dayOfWeekHeader = d3.select('#day-of-week-header');

    // 修正: currentMonthではなくstartDateを使用し、表示する日数分ループ
    for (let i = 0; i < totalDays; i++) {
        const currentDay = startDate.add(i, 'day');
        const dayOfWeek = currentDay.day();

        dayOfWeekHeader.append('div').style('display', 'inline-block').style('width', `${blockWidth}px`).style('text-align', 'center').style('color', getDayColor(dayOfWeek)).style('border-right', '1px solid black').text(currentDay.format('dd')); // 修正: 曜日を表示
    }
}

// 曜日に応じて色を決定
function getDayColor(dayOfWeek) {
    if (dayOfWeek === 0) {
        return 'red';
    } else if (dayOfWeek === 6) {
        return 'blue';
    } else {
        return 'black';
    }
}

// 日付の更新時にガントチャートを再描画
function updateTaskDates(id) {
    const task = tasks.value.find((t) => t.id === id);
    if (task) {
        task.startDate = dayjs(task.startDate).format('YYYY-MM-DD');
        task.endDate = dayjs(task.endDate).format('YYYY-MM-DD');
        updateChart();
    }
}

// ガントチャートを更新
function updateChart() {
    d3.select('#gantt-chart').selectAll('*').remove();
    drawGanttChart();
}

// 縦グリッド線の描画
function drawVerticalGridLines(svg) {
    const daysArray = Array.from({ length: totalDays }, (_, i) => i + 1);

    svg.selectAll('.column-grid-line')
        .data(daysArray)
        .enter()
        .append('line')
        .attr('x1', (d) => d * blockWidth)
        .attr('x2', (d) => d * blockWidth)
        .attr('y1', 0)
        .attr('y2', tasks.value.length * rowHeight)
        .attr('stroke', '#ccc');
}

//task追加関数
function addTask() {
    const newTaskId = tasks.value.length + 1;
    const newTask = {
        id: newTaskId,
        name: `Task ${newTaskId}`,
        pmType: `PM${newTaskId}`,
        startDate: startDate.format('YYYY-MM-DD'), // 修正: currentMonthではなくstartDateを使用
        endDate: startDate.add(1, 'day').format('YYYY-MM-DD') // 修正: currentMonthではなくstartDateを使用
    };
    tasks.value.push(newTask); // 新しいタスクを追加
    updateChart(); // ガントチャートを更新
}


// タスク削除の実際の処理
function deleteTask() {
    tasks.value = tasks.value.filter((task) => !task.selected); // チェックが入っていないタスクのみ残す
    updateChart(); // ガントチャートを更新
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
    font-weight: bold; /* 太字に変更 */
    text-align: center; /* 中央揃え */
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
</style>
