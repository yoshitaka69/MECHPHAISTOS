<template>
    <div id="app">
        <!-- テーブルを表示するためのコンテナ -->
        <div class="tables-container">
            <!-- 月ごとのコストテーブル -->
            <div id="monthlyCostTable">
                <hot-table ref="monthlyCostTableComponent" :settings="monthlyCostSettings"></hot-table>
            </div>
            <!-- 合計コストテーブル -->
            <div id="totalCostTable">
                <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
            </div>
        </div>
        <!-- タスクリストと操作ボタン -->
        <div id="TaskList">
            <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
            <br />
            <!-- 合計コスト計算ボタン（青色） -->
            <Button @click="calculateTotalCostSums" label="Calculate Total Costs" class="controls button-margin blue-button" />
  
            <!-- 追加されたSimulationボタン -->
            <Button @click="runSimulation(1)" label="Simulation No1" class="controls button-margin" />
            <Button @click="runSimulation(2)" label="Simulation No2" class="controls button-margin" />
            <Button @click="runSimulation(3)" label="Simulation No3" class="controls button-margin" />
            <Button @click="getDataAxios" label="Test Data Fetch" />
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
  import Button from 'primevue/button';
  
  // Handsontableのすべてのモジュールを登録
  registerAllModules();
  
  const Simulation_table = defineComponent({
    // 親コンポーネントにデータ更新を知らせるイベント
    emits: ['update-cost-data'],
    data() {
        return {
            // タスクリストテーブルの設定
            hotSettings: {
                data: Array.from({ length: 15 }, () => Array(25).fill('')), // 15行×25列の空データ
                colHeaders: this.generateColHeaders(), // カラムヘッダーを生成
                columns: [
                    { data: 'taskListNo', type: 'text' }, // TaskListNoフィールド
                    { data: 'typicalTaskName', type: 'text' }, // タスク名
                    { data: 'plant', type: 'text' }, // プラント名
                    { data: 'equipment', type: 'text' }, // 設備名
                    { data: 'machineName', type: 'text' }, // 機械名
                    { data: 'typicalLatestDate', type: 'date', dateFormat: 'YYYY-MM-DD', correctFormat: true }, // 最終日付
                    { data: 'multiTasking', type: 'checkbox', className: 'htCenter' }, // 複数タスク
                    { data: 'totalCost', type: 'numeric' }, // 合計コスト
                    { data: 'taskOfPeriod', type: 'numeric' }, // 期間タスク
                    { data: 'typicalNextEventDate', type: 'text', readOnly: true }, // 次のイベント日（読み取り専用）
                    { data: 'typicalSituation', type: 'text', readOnly: true }, // 現状（読み取り専用）
                    // 次年以降のチェックボックス
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
                // ヘッダーのスタイル設定
                afterGetColHeader: (col, TH) => {
                    if (col === -1) return;
                    TH.style.backgroundColor = '#FFFFCC';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },
                // その他のテーブルオプション
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
                // 非商用・評価ライセンスキー
                licenseKey: 'non-commercial-and-evaluation',
                // セルの値が変更された後に次のイベント日を再計算
                afterChange: (changes, source) => {
                    if (source === 'loadData') return; // `loadData`による変更は無視
  
                    changes.forEach(([row, prop, oldValue, newValue]) => {
                        if (prop === 'typicalLatestDate' || prop === 'taskOfPeriod') {
                            this.calculateNextEventDate(row);
                        }
                    });
                }
            },
  
            // 合計コストテーブルの設定
            totalCostSettings: {
                // 行データを4行に増やす（Base repairing Cost, Simulation No.1~No.3 のため）
                data: Array.from({ length: 4 }, () => Array(11).fill('')), // 4行×11列のデータ
                columns: Array.from({ length: 11 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter'
                })),
                colHeaders: this.generateColTotalCostHeaders(), // 年次ヘッダー
                rowHeaders: true,
                width: '100%',
                height: 150,
                readOnly: true, // 読み取り専用
                rowHeaders: ['Base repairing Cost', 'Simulation No.1', 'Simulation No.2', 'Simulation No.3'], // Simulation No.1~No.3を追加
                rowHeaderWidth: 150, // 行ヘッダーの幅を広げる
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true,
                autoRowSize: true,
                licenseKey: 'non-commercial-and-evaluation'
            },
  
            // 月次コストテーブルの設定
            monthlyCostSettings: {
                // 行データを4行に増やす（Base repairing Cost, Simulation No.1~No.3 のため）
                data: Array.from({ length: 4 }, () => Array(11).fill('')), // 4行×11列のデータ
                columns: Array.from({ length: 13 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter'
                })),
                colHeaders: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total'], // 月次ヘッダー
                rowHeaders: true,
                width: '100%',
                height: 150,
                readOnly: true, // 読み取り専用
                rowHeaders: ['Base repairing Cost', 'Simulation No.1', 'Simulation No.2', 'Simulation No.3'], // Simulation No.1~No.3を追加
                rowHeaderWidth: 150, // 行ヘッダーの幅を広げる
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
        // カラムヘッダーを動的に生成
        generateColHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
            return ['TaskListNo', 'TaskName', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'Multi<br>Tasking', 'TotalCost', 'Task Of Period', 'Next Even<br>date', 'Situation', ...futureYears];
        },
        // 合計コスト用のカラムヘッダーを生成
        generateColTotalCostHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());
            return [...futureYears];
        },
        // カスタムチェックボックスレンダラ
        customCheckboxRenderer(instance, td, row, col, prop, value, cellProperties) {
            Handsontable.renderers.CheckboxRenderer.apply(this, arguments);
            const matchedYears = this.getMatchingYears(instance, row);
            const currentYear = new Date().getFullYear();
            const yearOfThisColumn = currentYear + (col - 10);
            // マッチした年に応じて背景色を緑に設定
            if (matchedYears.includes(yearOfThisColumn)) {
                td.style.background = '#90EE90';
                td.querySelector('input[type="checkbox"]').checked = true;
            }
        },
        // マッチする年を取得する
        getMatchingYears(instance, row) {
            const latestDate = instance.getDataAtRowProp(row, 'typicalLatestDate');
            const taskOfPeriod = instance.getDataAtRowProp(row, 'taskOfPeriod');
            const matchedYears = [];
  
            if (!latestDate || !taskOfPeriod) return matchedYears;
  
            let checkDate = new Date(latestDate);
            const currentYear = new Date().getFullYear();
            const endYear = currentYear + 10;
  
            // 最終日からタスクの期間ごとに年を加算
            while (checkDate.getFullYear() <= endYear) {
                const futureYear = checkDate.getFullYear();
                if (futureYear >= currentYear) {
                    matchedYears.push(futureYear);
                }
                checkDate = new Date(checkDate.setDate(checkDate.getDate() + taskOfPeriod));
            }
  
            return matchedYears;
        },
        // 年次タスクのチェックボックスを自動で埋める
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
        // 確認ウィンドウを表示するメソッド
  
        // Axiosでデータを取得する
        getDataAxios() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
  
      if (!userCompanyCode) {
        console.error("Error: No company code found.");
        return;
      }
  
      const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;
      axios.get(url)
        .then((response) => {
          const companyData = response.data.find(company => company.companyCode === userCompanyCode);
          if (companyData) {
            this.$refs.hotTableComponent.hotInstance.loadData(companyData.taskList);
          } else {
            console.error("No taskList found for this company.");
          }
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    },
  
  
        // 合計コストを計算する
        calculateTotalCostSums() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = new Date().getFullYear();
            const endYear = currentYear + 10;
            let sums = new Array(11).fill(0); // 11年間の合計を初期化
  
            // 各行をループして合計コストを計算
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
  
            // 合計コストテーブルにデータをロード
            this.$refs.totalCostTableComponent.hotInstance.loadData([sums]);
  
            this.calculateMonthlyCosts(); // 月次コストも計算
            this.emitData(); // 計算結果をemitで親コンポーネントに送信
        },
  
        // 次のイベント日を計算
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
  
        // 月次コストを計算
        calculateMonthlyCosts() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = new Date().getFullYear();
            let monthlyCosts = new Array(12).fill(0); // 各月のコスト
  
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
  
            const total = monthlyCosts.reduce((a, b) => a + b, 0); // 合計値を計算
            monthlyCosts.push(total); // Totalを追加
  
            // 月次コストテーブルにデータをロード
            this.$refs.monthlyCostTableComponent.hotInstance.loadData([monthlyCosts]);
  
            console.log('Monthly Costs Updated:', monthlyCosts);
        },
  
        // 計算結果をemitする
        emitData() {
            const totalCostData = this.$refs.totalCostTableComponent.hotInstance.getData();
            const monthlyCostData = this.$refs.monthlyCostTableComponent.hotInstance.getData();
  
            console.log('Emitting data:', { totalCostData, monthlyCostData });
            this.$emit('update-cost-data', { totalCostData, monthlyCostData });
        },
  
        // コンポーネントがマウントされたらデータを取得
        mounted() {
            console.log('Component mounted'); // コンポーネントがマウントされたときにログを出力
            this.getDataAxios();
        },
  
        // 状況列のレンダラ
        situationRenderer(instance, td, row, col, prop, value, cellProperties) {
            const nextEventDateStr = instance.getDataAtRowProp(row, 'typicalNextEventDate');
            const nextEventDate = new Date(nextEventDateStr);
            const currentDate = new Date();
  
            Handsontable.renderers.TextRenderer.apply(this, arguments);
  
            // 次のイベント日が現在より前の場合は赤色背景
            if (nextEventDateStr && nextEventDate < currentDate) {
                td.style.backgroundColor = 'red';
                td.innerHTML = 'Delay';
            } else {
                td.style.backgroundColor = '';
                td.innerHTML = value || '';
            }
        }
    },
    components: {
        HotTable,
        Button // PrimeVueのButtonコンポーネントを登録
    }
  });
  
  export default Simulation_table;
  
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
  