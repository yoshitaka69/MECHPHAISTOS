<template>
  <div id="app">
    <!-- タスクリストを表示 -->
    <div id="TaskList" v-if="isDataReady">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
      <br />
      <Button @click="calculateTotalCostSums" label="Calculate Total Costs" class="controls button-margin blue-button" />
      <Button @click="runSimulation(1)" label="Simulation No1" class="controls button-margin" />
      <Button @click="runSimulation(2)" label="Simulation No2" class="controls button-margin" />
      <Button @click="runSimulation(3)" label="Simulation No3" class="controls button-margin" />
    </div>

    <!-- 月次コストテーブルと合計コストテーブルを表示 -->
    <div class="tables-container" v-if="isDataReady">
      <div id="monthlyCostTable">
        <hot-table ref="monthlyCostTableComponent" :settings="monthlyCostSettings"></hot-table>
      </div>
      <div id="totalCostTable">
        <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import { HotTable } from '@handsontable/vue3';
import Handsontable from 'handsontable';  // Handsontableをインポート

// データの準備が完了したかどうかのフラグ
const isDataReady = ref(false);

// テーブルの参照を取得するためのref
const hotTableComponent = ref(null);
const totalCostTableComponent = ref(null);
const monthlyCostTableComponent = ref(null);

// タスクリストテーブルの設定
const hotSettings = ref({
  data: Array.from({ length: 15 }, () => Array(25).fill('')),
  colHeaders: generateColHeaders(),
  columns: [
    { data: 'taskListNo', type: 'text' },
    { data: 'typicalTaskName', type: 'text' },
    { data: 'plant', type: 'text' },
    { data: 'equipment', type: 'text' },
    { data: 'machineName', type: 'text' },
    { data: 'typicalLatestDate', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: true },
    { data: 'multiTasking', type: 'checkbox', className: 'htCenter' },
    { data: 'totalCost', type: 'numeric' },
    { data: 'taskOfPeriod', type: 'numeric' },
    { data: 'typicalNextEventDate', type: 'text', readOnly: true },
    { data: 'typicalSituation', type: 'text', readOnly: true },
    { data: 'thisYear', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear1later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear2later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear3later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear4later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear5later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear6later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear7later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear8later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear9later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true },
    { data: 'thisYear10later', type: 'checkbox', className: 'htCenter', renderer: customCheckboxRenderer, readOnly: true }
  ],
  afterGetColHeader: (col, TH) => {
    if (col === -1) return;
    TH.style.backgroundColor = '#FFFFCC';
    TH.style.color = 'black';
    TH.style.fontWeight = 'bold';
  },
  rowHeaders: true,
  width: '100%',
  height: 'auto',
  contextMenu: true,
  autoWrapRow: true,
  autoWrapCol: true,
  fixedColumnsStart: 2,
  fixedRowsTop: 2,
  manualColumnFreeze: true,
  manualColumnResize: true,
  manualRowResize: true,
  filters: true,
  dropdownMenu: true,
  comments: true,
  fillHandle: {
    autoInsertRow: true
  },
  licenseKey: 'non-commercial-and-evaluation',
  afterChange: (changes, source) => {
    if (source === 'loadData') return;
    changes.forEach(([row, prop, oldValue, newValue]) => {
      if (prop === 'typicalLatestDate' || prop === 'taskOfPeriod') {
        calculateNextEventDate(row);
      }
    });
  }
});

// 合計コストテーブルの設定
const totalCostSettings = ref({
  data: Array.from({ length: 4 }, () => Array(11).fill('')),
  columns: Array.from({ length: 11 }, (_, i) => ({
    data: i,
    type: 'numeric',
    className: 'htCenter'
  })),
  colHeaders: generateColTotalCostHeaders(),
  rowHeaders: ['Base repairing Cost', 'Simulation No.1', 'Simulation No.2', 'Simulation No.3'],
  rowHeaderWidth: 150,
  contextMenu: true,
  autoWrapRow: true,
  autoWrapCol: true,
  autoColumnSize: true,
  autoRowSize: true,
  licenseKey: 'non-commercial-and-evaluation'
});

// 月次コストテーブルの設定
const monthlyCostSettings = ref({
  data: Array.from({ length: 4 }, () => Array(11).fill('')),
  columns: Array.from({ length: 13 }, (_, i) => ({
    data: i,
    type: 'numeric',
    className: 'htCenter'
  })),
  colHeaders: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total'],
  rowHeaders: ['Base repairing Cost', 'Simulation No.1', 'Simulation No.2', 'Simulation No.3'],
  rowHeaderWidth: 150,
  contextMenu: true,
  autoWrapRow: true,
  autoWrapCol: true,
  autoColumnSize: true,
  autoRowSize: true,
  licenseKey: 'non-commercial-and-evaluation'
});

// データ取得用の関数
const getDataAxios = () => {
  const userStore = useUserStore();
  const userCompanyCode = userStore.companyCode;

  console.log("Fetching data for company code:", userCompanyCode);

  if (!userCompanyCode) {
    console.error('Error: No company code found.');
    return;
  }

  const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;
  
  axios.get(url)
    .then((response) => {
      console.log("Axios response data:", response.data);

      const companyData = response.data.find((company) => {
        return String(company.companyCode) === String(userCompanyCode);
      });

      if (companyData) {
        if (Array.isArray(companyData.taskList) && companyData.taskList.length > 0) {
          console.log("Task list data found for company:", companyData.taskList);

          nextTick(() => {
            if (hotTableComponent.value) {
              hotTableComponent.value.hotInstance.loadData(companyData.taskList);
              isDataReady.value = true;
            } else {
              console.warn('hotTableComponent is null, skipping data loading.');
            }
          });
        } else {
          console.error('Task list is empty or invalid for this company.');
        }
      } else {
        console.error('No company data found for this company code.');
      }
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
};

onMounted(() => {
  getDataAxios();
});

// カラムヘッダー生成の関数
function generateColHeaders() {
  const currentYear = new Date().getFullYear();
  const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
  return ['TaskListNo', 'TaskName', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'Multi<br>Tasking', 'TotalCost', 'Task Of Period', 'Next Even<br>date', 'Situation', ...futureYears];
}

// 合計コスト用のカラムヘッダー生成
function generateColTotalCostHeaders() {
  const currentYear = new Date().getFullYear();
  const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
  return [...futureYears];
}

// カスタムチェックボックスレンダラ
function customCheckboxRenderer(instance, td, row, col, prop, value, cellProperties) {
  Handsontable.renderers.CheckboxRenderer.apply(this, arguments);
  const matchedYears = getMatchingYears(instance, row);
  const currentYear = new Date().getFullYear();
  const yearOfThisColumn = currentYear + (col - 10);

  if (matchedYears.includes(yearOfThisColumn)) {
    td.style.background = '#90EE90';
    td.querySelector('input[type="checkbox"]').checked = true;
  }
}

// マッチする年を取得する関数
function getMatchingYears(instance, row) {
  const latestDate = instance.getDataAtRowProp(row, 'typicalLatestDate');
  const taskOfPeriod = instance.getDataAtRowProp(row, 'taskOfPeriod');
  const matchedYears = [];

  if (!latestDate || !taskOfPeriod) return matchedYears;

  let checkDate = new Date(latestDate);
  const currentYear = new Date().getFullYear();
  const endYear = currentYear + 10;

  while (checkDate.getFullYear() <= endYear) {
    const futureYear = checkDate.getFullYear();
    if (futureYear >= currentYear) {
      matchedYears.push(futureYear);
    }
    checkDate = new Date(checkDate.setDate(checkDate.getDate() + taskOfPeriod));
  }

  return matchedYears;
}

// 合計コストの計算
function calculateTotalCostSums() {
  if (!hotTableComponent.value) return;
  const hotInstance = hotTableComponent.value.hotInstance;
  const currentYear = new Date().getFullYear();
  const endYear = currentYear + 10;
  let sums = new Array(11).fill(0);

  hotInstance.getData().forEach((row, rowIndex) => {
    const latestDatePM = hotInstance.getDataAtCell(rowIndex, 4);
    const taskOfPeriod = parseInt(hotInstance.getDataAtCell(rowIndex, 7));
    const totalCost = parseFloat(hotInstance.getDataAtCell(rowIndex, 6));

    if (latestDatePM && !isNaN(taskOfPeriod) && !isNaN(totalCost)) {
      let checkDate = new Date(latestDatePM);

      while (checkDate.getFullYear() <= endYear) {
        const year = checkDate.getFullYear();
        if (year >= currentYear && year <= endYear) {
          sums[year - currentYear] += totalCost;
        }
        checkDate.setDate(checkDate.getDate() + taskOfPeriod);
      }
    }
  });

  totalCostTableComponent.value?.hotInstance.loadData([sums]);
  calculateMonthlyCosts();
  emitData();
}

// 次のイベント日を計算
function calculateNextEventDate(row) {
  if (!hotTableComponent.value) return;
  const hotInstance = hotTableComponent.value.hotInstance;
  const latestDatePM = hotInstance.getDataAtCell(row, 4);
  const taskOfPeriod = parseInt(hotInstance.getDataAtCell(row, 7));

  if (latestDatePM && !isNaN(taskOfPeriod)) {
    const latestDate = new Date(latestDatePM);
    const nextEventDate = new Date(latestDate.setDate(latestDate.getDate() + taskOfPeriod));

    const year = nextEventDate.getFullYear();
    const month = ('0' + (nextEventDate.getMonth() + 1)).slice(-2);
    const day = ('0' + nextEventDate.getDate()).slice(-2);

    hotInstance.setDataAtCell(row, 8, `${year}-${month}-${day}`);
  }
}

// 月次コストを計算
function calculateMonthlyCosts() {
  if (!hotTableComponent.value) return;
  const hotInstance = hotTableComponent.value.hotInstance;
  const currentYear = new Date().getFullYear();
  let monthlyCosts = new Array(12).fill(0);

  hotInstance.getData().forEach((row, rowIndex) => {
    const latestDatePM = hotInstance.getDataAtCell(rowIndex, 4);
    const taskOfPeriod = parseInt(hotInstance.getDataAtCell(rowIndex, 7));
    const totalCost = parseFloat(hotInstance.getDataAtCell(rowIndex, 6));

    if (latestDatePM && !isNaN(taskOfPeriod) && !isNaN(totalCost)) {
      let checkDate = new Date(latestDatePM);

      while (checkDate.getFullYear() === currentYear) {
        const month = checkDate.getMonth();
        monthlyCosts[month] += totalCost;
        checkDate.setDate(checkDate.getDate() + taskOfPeriod);
      }
    }
  });

  const total = monthlyCosts.reduce((a, b) => a + b, 0);
  monthlyCosts.push(total);

  monthlyCostTableComponent.value?.hotInstance.loadData([monthlyCosts]);
}

// 計算結果をemitする
function emitData() {
  const totalCostData = totalCostTableComponent.value?.hotInstance.getData();
  const monthlyCostData = monthlyCostTableComponent.value?.hotInstance.getData();
  // 計算結果をemit
  // this.$emitで親コンポーネントに送信
}
</script>


<style>
/* テーブルのコンテナ */
.tables-container {
    display: flex;
    justify-content: space-between;
}
/* コストテーブルのスタイル */
#totalCostTable,
#monthlyCostTable {
    width: 48%;
}

/* ボタン間にマージンを追加 */
.button-margin {
    margin-right: 10px;
}

/* 青色のCalculationボタン */
.blue-button {
    background-color: blue;
    color: white;
}
</style>
