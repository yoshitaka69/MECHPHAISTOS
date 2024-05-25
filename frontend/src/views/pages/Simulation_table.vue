<template>
    <div id="app">
      <div class="tables-container">
        <div id="monthlyCostTable">
          <hot-table ref="monthlyCostTableComponent" :settings="monthlyCostSettings"></hot-table>
        </div>
        <div id="totalCostTable">
          <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
        </div>
      </div>
      <div id="TaskList">
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
        <br />
        <button @click="updateData" class="controls">Update Data</button>
        <button @click="calculateTotalCostSums" class="controls">Calculate Total Costs</button>
      </div>
    </div>
  </template>
  
  
  <script>
  import Handsontable from 'handsontable';
  import { defineComponent } from 'vue';
  import { HotTable } from '@handsontable/vue3';
  import { registerAllModules } from 'handsontable/registry';
  import 'handsontable/dist/handsontable.full.css';
  import axios from 'axios';
  import { useUserStore } from '@/stores/userStore';
  
  registerAllModules();
  
  const Simulation_table = defineComponent({
    emits: ['update-cost-data'],
    data() {
        return {
            hotSettings: {
                data: [
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //1
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //2
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //3
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //4
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //5
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //6
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //7
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //8
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //9
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //10
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //11
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //12
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //13
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], //14
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] //15
                ],
                colHeaders: this.generateColHeaders(),
                columns: [
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
                    { data: 'thisYear', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear1later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear2later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear3later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear4later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear5later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear6later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear7later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear8later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear9later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true },
                    { data: 'thisYear10later', type: 'checkbox', className: 'htCenter', renderer: this.customCheckboxRenderer, readOnly: true }
                ],
                afterGetColHeader: (col, TH) => {
                    if (col === -1) return;
                    TH.style.backgroundColor = '#FFFFCC';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },
                cells: (row, col, prop) => {
                    const cellProperties = {};
                    if (prop === 'thisYear' || prop.startsWith('thisYear')) {
                        cellProperties.renderer = this.customCheckboxRenderer;
                    }
                    return cellProperties;
                },
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
                    if (source === 'loadData') return; // `loadData`による変更は無視
  
                    changes.forEach(([row, prop, oldValue, newValue]) => {
                        if (prop === 'typicalLatestDate' || prop === 'taskOfPeriod') {
                            this.calculateNextEventDate(row);
                        }
                    });
                }
            },
  
            totalCostSettings: {
                data: [
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] //1
                ],
                columns: Array.from({ length: 11 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter'
                })),
                colHeaders: this.generateColTotalCostHeaders(),
                rowHeaders: true,
                width: '100%',
                height: 150,
                readOnly: true,
                rowHeaders: ['Total'],
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true,
                autoRowSize: true,
                licenseKey: 'non-commercial-and-evaluation',
                columnSummary: [
                    ...Array.from({ length: 11 }, (_, i) => ({
                        destinationRow: 0,
                        destinationColumn: i,
                        type: 'custom',
                        reversedRowCoords: true,
                        customFunction: function (endpoint) {
                            let sum = 0;
                            endpoint.ranges.forEach((range) => {
                                for (let row = range[0]; row <= range[1]; row++) {
                                    const isChecked = this.hot.getDataAtCell(row, 10 + i); // チェックボックス列
                                    const totalCost = this.hot.getDataAtCell(row, 6); // TotalCost 列
                                    if (isChecked && !isNaN(totalCost)) {
                                        sum += parseFloat(totalCost);
                                    }
                                }
                            });
                            return sum;
                        }
                    }))
                ]
            },
  
            monthlyCostSettings: {
                data: [
                    ['', '', '', '', '', '', '', '', '', '', '', '', ''] // 1行目
                ],
                columns: Array.from({ length: 13 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter'
                })),
                colHeaders: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total'],
                rowHeaders: true,
                width: '100%',
                height: 150,
                readOnly: true,
                rowHeaders: ['Monthly Total'],
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true,
                autoRowSize: true,
                licenseKey: 'non-commercial-and-evaluation'
            }
        };
    },
    methods: {
        generateColHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
            return ['TaskName', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'Multi<br>Tasking', 'TotalCost', 'Task Of Period', 'Next Even<br>date', 'Situation', ...futureYears];
        },
        generateColTotalCostHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
            return [...futureYears];
        },
        customCheckboxRenderer(instance, td, row, col, prop, value, cellProperties) {
            Handsontable.renderers.CheckboxRenderer.apply(this, arguments);
            const matchedYears = this.getMatchingYears(instance, row);
            const currentYear = new Date().getFullYear();
            const yearOfThisColumn = currentYear + (col - 10);
            if (matchedYears.includes(yearOfThisColumn)) {
                td.style.background = '#90EE90';
                td.querySelector('input[type="checkbox"]').checked = true;
            }
        },
        getMatchingYears(instance, row) {
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
        },
        checkAndFillYearlyTasks() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const rowCount = hotInstance.countRows();
            for (let row = 0; row < rowCount; row++) {
                const matchedYears = this.getMatchingYears(hotInstance, row);
                const currentYear = new Date().getFullYear();
                for (let col = 10; col <= 20; col++) {
                    const yearOfThisColumn = currentYear + (col - 10);
                    if (matchedYears.includes(yearOfThisColumn)) {
                        hotInstance.setDataAtCell(row, col, true);
                    }
                }
            }
        },
        getDataAxios() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;
            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }
  
            const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;
            return axios
                .get(url, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                .then((response) => {
                    const taskListData = response.data.flatMap((companyData) => companyData.taskList);
                    console.log('Fetched Task List Data:', taskListData);
  
                    const blankRows = Array.from({ length: 20 }, () => ({}));
                    const newData = taskListData.concat(blankRows);
  
                    this.$refs.hotTableComponent.hotInstance.loadData(newData);
  
                    this.checkAndFillYearlyTasks();
                    this.calculateTotalCostSums();
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },
        calculateTotalCostSums() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = new Date().getFullYear();
            let sums = new Array(11).fill(0);
  
            hotInstance.getData().forEach((row, rowIndex) => {
                for (let i = 0; i < 11; i++) {
                    const checkboxColumnIndex = 10 + i;
                    const isChecked = row[checkboxColumnIndex];
                    const totalCost = parseFloat(row[6]);
  
                    if (!isChecked && !isNaN(totalCost)) {
                        sums[i] += totalCost;
                    }
                }
            });
  
            this.$refs.totalCostTableComponent.hotInstance.loadData([sums]);
  
            this.calculateMonthlyCosts(); // 月ごとの修繕費を計算
  
            this.emitData(); // データをemitする
        },
  
        calculateNextEventDate(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
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
        },
  
        calculateMonthlyCosts() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = new Date().getFullYear();
            let monthlyCosts = new Array(12).fill(0);
  
            console.log('Starting monthly cost calculation.');
  
            hotInstance.getData().forEach((row, rowIndex) => {
                const latestDatePM = hotInstance.getDataAtCell(rowIndex, 4);
                const taskOfPeriod = parseInt(hotInstance.getDataAtCell(rowIndex, 7));
                const totalCost = parseFloat(hotInstance.getDataAtCell(rowIndex, 6));
  
                console.log(`Row ${rowIndex}: latestDatePM = ${latestDatePM}, taskOfPeriod = ${taskOfPeriod}, totalCost = ${totalCost}`);
  
                if (latestDatePM && !isNaN(taskOfPeriod) && !isNaN(totalCost)) {
                    let checkDate = new Date(latestDatePM);
  
                    while (checkDate.getFullYear() === currentYear) {
                        const month = checkDate.getMonth(); // 0から始まるためそのまま使う
                        monthlyCosts[month] += totalCost;
                        console.log(`Added ${totalCost} to month ${month + 1}, new total: ${monthlyCosts[month]}`);
  
                        // 次の期間に進む前にデバッグ情報を出力
                        console.log(`Before adding period: ${checkDate.toISOString()}`);
                        checkDate.setDate(checkDate.getDate() + taskOfPeriod);
                        console.log(`After adding period: ${checkDate.toISOString()}`);
                    }
                } else {
                    console.log(`Skipping row ${rowIndex} due to invalid latestDatePM or taskOfPeriod or totalCost`);
                }
            });
  
            const total = monthlyCosts.reduce((a, b) => a + b, 0);
            monthlyCosts.push(total); // Totalを追加
  
            this.$refs.monthlyCostTableComponent.hotInstance.loadData([monthlyCosts]);
  
            console.log('Monthly Costs Updated:', monthlyCosts);
        },
  
        emitData() {
            const totalCostData = this.$refs.totalCostTableComponent.hotInstance.getData();
            const monthlyCostData = this.$refs.monthlyCostTableComponent.hotInstance.getData();
  
            console.log('Emitting data:', { totalCostData, monthlyCostData });
            this.$emit('update-cost-data', { totalCostData, monthlyCostData });
        },
  
        mounted() {
            this.getDataAxios();
        }
    },
    components: {
        HotTable
    }
  });
  export default Simulation_table;
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
  