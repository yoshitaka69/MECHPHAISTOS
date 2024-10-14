<template>
    <div id="TaskList">
        <!-- Toastの表示 -->
        <Toast />

        <!-- テーブル追加 -->
        <div class="tables-container">
            <div id="monthlyCostTable">
                <hot-table ref="monthlyCostTableComponent" :settings="monthlyCostSettings"></hot-table>
            </div>
            <div id="totalCostTable">
                <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
            </div>
        </div>
        <!-- Simulation ボタンの追加 -->
        <div class="simulation-buttons-container">
            <button @click="handleSimulation(1)" :disabled="!isSimulationActive" class="simulation-button">Simulation 1</button>
            <button @click="handleSimulation(2)" :disabled="!isSimulationActive" class="simulation-button">Simulation 2</button>
            <button @click="handleSimulation(3)" :disabled="!isSimulationActive" class="simulation-button">Simulation 3</button>
        </div>

        <!-- 説明文の追加 -->
        <p class="simulation-description">* Simulation buttons cannot be pressed unless some data, such as the base date, has been changed.</p>

        <!-- Post Simulation データのボタン -->
        <div class="post-simulation-container">
            <button @click="postSimulationData(1)" class="post-simulation-btn">Post Simulation 1 Data</button>
            <button @click="postSimulationData(2)" class="post-simulation-btn">Post Simulation 2 Data</button>
            <button @click="postSimulationData(3)" class="post-simulation-btn">Post Simulation 3 Data</button>
        </div>

        <!-- companyCode 表示 -->
        <div class="company-code-container">
            <span>Company Code: {{ companyCode }}</span>
        </div>
        <div class="legend">
            <div class="legend-item">
                <div class="color-box" style="background-color: #f0a0a0"></div>
                <span>Form input format is incorrect</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background-color: #f0f0f0"></div>
                <span>Input not allowed. Value is automatically filled.</span>
            </div>
        </div>

        <!-- 行数選択ドロップダウン -->
        <div class="row-count-container">
            <span>表示する行数:</span>
            <select v-model="rowsToShow" @change="updateRowCount">
                <option value="10">10行</option>
                <option value="30">30行</option>
                <option value="50">50行</option>
                <option value="100">100行</option>
            </select>
        </div>

        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>

        <!-- Calculationボタンの追加 -->

        <br />
        <button @click="calculateCosts" class="calculation-button">Calculation</button>
    </div>
</template>
<script>
import Handsontable from 'handsontable'; // Handsontableのインポート
import { defineComponent } from 'vue'; // Vueのコンポーネント定義に必要なインポート
import { HotTable } from '@handsontable/vue3'; // HandsontableとVueを統合するためのインポート
import { registerAllModules } from 'handsontable/registry'; // Handsontableの全モジュールを登録
import 'handsontable/dist/handsontable.full.css'; // HandsontableのCSSファイルをインポート
import axios from 'axios'; // API通信に使用するaxiosライブラリをインポート
import { useUserStore } from '@/stores/userStore'; // ユーザーストアからcompanyCodeを取得するために使用
import Button from 'primevue/button'; // PrimeVueのボタンコンポーネント
import moment from 'moment'; // 日付計算を容易にするためのmoment.jsをインポート
import { useToast } from 'primevue/usetoast'; // Toast用のフックをインポート

// Handsontableのすべてのモジュールを登録
registerAllModules();

const TaskListComponent = defineComponent({
    data() {
        return {
            isSimulationActive: false, // シミュレーションボタンの有効/無効状態を管理
            hotSettings: {
                data: [], // 初期データとして空の配列を指定
                colHeaders: this.generateColHeaders(), // ヘッダーを生成する関数を呼び出す
                columns: [
                    {
                        data: 'taskListNo', // タスクリスト番号列
                        type: 'text',
                        readOnly: true, // 読み取り専用
                        renderer: this.taskListNoRenderer // 独自のレンダラーを使用してリンクを作成
                    },
                    {
                        data: 'taskName', // タスク名列
                        type: 'text'
                    },
                    {
                        data: 'plant', // プラント名列
                        type: 'text'
                    },
                    {
                        data: 'equipment', // 設備列
                        type: 'text'
                    },
                    {
                        data: 'machineName', // 機械名列
                        type: 'text'
                    },
                    {
                        data: 'pmType', // PMタイプ列（ドロップダウンメニュー）
                        type: 'dropdown',
                        source: ['PM01', 'PM02', 'PM03', 'PM04', 'PM05'], // 選択肢
                        strict: true,
                        allowInvalid: false
                    },
                    {
                        data: 'maintenanceType', // 保全タイプ列（ドロップダウンメニュー）
                        type: 'dropdown',
                        source: ['Overhaul', 'Regular Maintenance', 'Inspection and Check', 'Adjustment', 'Parts Replacement', 'Calibration', 'Cleaning', 'Lubrication', 'Balancing', 'Testing and Trial Operation'],
                        strict: true,
                        allowInvalid: false
                    },
                    {
                        data: 'latestEventDate', // 最新のイベント日付列
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD', // 日付フォーマット
                        correctFormat: false // 正しいフォーマットでなくても許可
                    },
                    {
                        data: 'taskPeriod', // タスク周期列（数値）
                        type: 'numeric'
                    },
                    {
                        data: 'taskLaborCost', // タスクの労働コスト列
                        type: 'numeric'
                    },
                    {
                        data: 'bomCode', // BOMコード列
                        type: 'text'
                    },
                    {
                        data: 'bomCost', // BOMコスト列
                        type: 'numeric'
                    },
                    {
                        data: 'totalCost', // 合計コスト列
                        type: 'numeric',
                        readOnly: true // 読み取り専用
                    },
                    {
                        data: 'nextEventDate', // 次回イベント日列
                        type: 'text',
                        readOnly: true // 読み取り専用
                    },
                    {
                        data: 'situation', // 状況列
                        type: 'text',
                        readOnly: true
                    },
                    {
                        data: 'thisYear',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear1later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear2later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear3later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear4later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear5later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear6later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear7later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear8later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear9later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        data: 'thisYear10later',
                        type: 'checkbox',
                        className: 'htCenter'
                    }
                ],

                // 列ヘッダーのスタイル設定
                afterGetColHeader: (col, TH) => {
                    if (col === -1) return;
                    TH.style.backgroundColor = '#FFFFCC';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },
                afterChange: (changes, source) => {
                    if (source === 'edit' || source === 'autofill') {
                        let isChanged = false; // 変更があったかを確認するフラグ
                        changes.forEach(([row, prop, oldValue, newValue]) => {
                            if (['taskLaborCost', 'bomCost'].includes(prop)) {
                                this.calculateTotalCost(row); // コストが変わった場合、合計コストを再計算
                                isChanged = true; // 変更があったことを記録
                            }
                            if (['latestEventDate', 'taskPeriod'].includes(prop)) {
                                this.calculateNextEventDate(row); // イベント日またはタスク期間が変わった場合、次回イベント日を再計算
                                this.calculateYears(row); // 年次チェックボックスを更新
                                isChanged = true; // 変更があったことを記録
                            }

                            // 年次チェックボックスの変更も確認
                            if (this.isYearCheckboxChanged(row)) {
                                isChanged = true; // 年次チェックボックスが変更された場合
                            }
                        });

                        // 変更があった場合にシミュレーションボタンを有効化
                        if (isChanged) {
                            this.isSimulationActive = true; // シミュレーションボタンを有効化
                        }
                    }
                },

                cells: function (row, col, prop) {
                    const cellProperties = {};
                    const readOnlyColumns = ['taskListNo', 'situation', 'totalCost', 'nextEventDate'];

                    if (readOnlyColumns.includes(this.columns[col].data)) {
                        cellProperties.readOnly = true;
                    }
                    return cellProperties;
                },

                afterRenderer: function (TD, row, col, prop, value, cellProperties) {
                    const readOnlyColumns = ['taskListNo', 'situation', 'totalCost', 'nextEventDate'];

                    if (readOnlyColumns.includes(cellProperties.prop)) {
                        TD.style.backgroundColor = '#f5f5f5';
                        TD.style.color = 'black';
                    }

                    if (prop === 'situation' && value === 'delay') {
                        TD.style.backgroundColor = '#ffcccc';
                        TD.style.color = 'black';
                    }
                },

                rowHeaders: true,
                width: '100%',
                height: 'auto',
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                fixedColumnsStart: 2,
                manualColumnFreeze: true,
                manualColumnResize: true,
                manualRowResize: true,
                filters: true,
                dropdownMenu: true,
                comments: true,
                fillHandle: {
                    autoInsertRow: true
                },
                licenseKey: 'non-commercial-and-evaluation'
            },
            dataStore: [],
            companyCode: '',
            rowsToShow: 10,

            // 警告解消のため monthlyCostSettings の定義
            monthlyCostSettings: {
                data: Array.from({ length: 4 }, () => Array(13).fill('')), // 4行に変更（Base + Simulation1, 2, 3）
                columns: Array.from({ length: 13 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter' // セルを中央に配置
                })),
                colHeaders: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total'], // 列のヘッダー
                rowHeaders: ['Base Monthly Total', 'Simulation1', 'Simulation2', 'Simulation3', 'Gap with Simulation1', 'Gap with Simulation2', 'Gap with Simulation3'],

                width: '100%',
                height: 150,
                readOnly: true, // 読み取り専用
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true,
                autoRowSize: true,
                rowHeaderWidth: 150, // 行ヘッダーの幅を150pxに変更
                licenseKey: 'non-commercial-and-evaluation'
            },

            // 警告解消のため totalCostSettings の定義
            totalCostSettings: {
                data: Array.from({ length: 4 }, () => Array(11).fill('')), // 4行に変更（Base + Simulation1, 2, 3）
                columns: Array.from({ length: 11 }, (_, i) => ({
                    data: i,
                    type: 'numeric',
                    className: 'htCenter' // セルを中央に配置
                })),
                colHeaders: Array.from({ length: 11 }, (_, i) => `${moment().year() + i}`), // 現在の年から11年間のヘッダーを生成
                rowHeaders: ['Base Yearly Total', 'Simulation1', 'Simulation2', 'Simulation3', 'Gap with Simulation1', 'Gap with Simulation2', 'Gap with Simulation3'],
                width: '100%',
                height: 150,
                readOnly: true, // 読み取り専用
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true,
                autoRowSize: true,
                rowHeaderWidth: 150, // 行ヘッダーの幅を150pxに変更
                licenseKey: 'non-commercial-and-evaluation'
            }
        };
    },

    watch: {
        // Vueのdataプロパティにあるテーブルデータの変更を監視
        tableData: {
            handler(newVal, oldVal) {
                this.checkSimulationButtonStatus(newVal, oldVal);
            },
            deep: true // データの深い変更も監視
        }
    },

    created() {
        this.getDataAxios(); // コンポーネント作成時にデータを取得
    },

    methods: {
        // Simulation ボタンが押されたときの処理
        handleSimulation(simulationNumber) {
            this.calculateCostsForSimulation(simulationNumber);
        },

        calculateCostsForSimulation(simulationRowIndex) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = moment().year();
            const endYear = currentYear + 10;

            // 月次コスト計算
            let monthlyCosts = new Array(12).fill(0);
            hotInstance.getData().forEach((row, rowIndex) => {
                const latestEventDate = hotInstance.getDataAtRowProp(rowIndex, 'latestEventDate');
                const taskPeriod = parseInt(hotInstance.getDataAtRowProp(rowIndex, 'taskPeriod'));
                const totalCost = parseFloat(hotInstance.getDataAtRowProp(rowIndex, 'totalCost'));

                if (latestEventDate && moment(latestEventDate, 'YYYY-MM-DD', true).isValid() && !isNaN(taskPeriod) && !isNaN(totalCost)) {
                    let checkDate = moment(latestEventDate, 'YYYY-MM-DD');
                    while (checkDate.isSameOrBefore(moment().endOf('year'))) {
                        const eventYear = checkDate.year();
                        const eventMonth = checkDate.month();

                        if (eventYear === currentYear) {
                            monthlyCosts[eventMonth] += totalCost;
                        }
                        checkDate.add(taskPeriod, 'days');
                    }
                }
            });
            const totalMonthlyCost = monthlyCosts.reduce((a, b) => a + b, 0);
            monthlyCosts.push(totalMonthlyCost);

            // 月次コストをSimulation行に反映
            let currentMonthlyData = this.$refs.monthlyCostTableComponent.hotInstance.getData();
            currentMonthlyData[simulationRowIndex] = monthlyCosts;
            this.$refs.monthlyCostTableComponent.hotInstance.loadData(currentMonthlyData);

            // ギャップを計算して表示
            if (simulationRowIndex > 0) {
                let baseMonthlyCosts = currentMonthlyData[0]; // Base Monthly Total行
                let gapMonthlyCosts = baseMonthlyCosts.map((baseCost, index) => baseCost - monthlyCosts[index]);

                currentMonthlyData[simulationRowIndex + 3] = gapMonthlyCosts; // ギャップ行に反映
                this.$refs.monthlyCostTableComponent.hotInstance.loadData(currentMonthlyData);
            }

            // 年次コスト計算
            let yearlyCosts = new Array(11).fill(0);
            hotInstance.getData().forEach((row, rowIndex) => {
                const latestEventDate = hotInstance.getDataAtRowProp(rowIndex, 'latestEventDate');
                const taskPeriod = parseInt(hotInstance.getDataAtRowProp(rowIndex, 'taskPeriod'));
                const totalCost = parseFloat(hotInstance.getDataAtRowProp(rowIndex, 'totalCost'));

                if (latestEventDate && moment(latestEventDate, 'YYYY-MM-DD', true).isValid() && !isNaN(taskPeriod) && !isNaN(totalCost)) {
                    let checkDate = moment(latestEventDate, 'YYYY-MM-DD');
                    while (checkDate.year() <= endYear) {
                        const eventYear = checkDate.year();
                        if (eventYear >= currentYear && eventYear <= endYear) {
                            yearlyCosts[eventYear - currentYear] += totalCost;
                        }
                        checkDate.add(taskPeriod, 'days');
                    }
                }
            });

            let currentYearlyData = this.$refs.totalCostTableComponent.hotInstance.getData();
            currentYearlyData[simulationRowIndex] = yearlyCosts; // シミュレーション行に反映
            this.$refs.totalCostTableComponent.hotInstance.loadData(currentYearlyData);

            // ギャップを計算して表示
            if (simulationRowIndex > 0) {
                let baseYearlyCosts = currentYearlyData[0]; // Base Yearly Total行
                let gapYearlyCosts = baseYearlyCosts.map((baseCost, index) => baseCost - yearlyCosts[index]);

                currentYearlyData[simulationRowIndex + 3] = gapYearlyCosts; // ギャップ行に反映
                this.$refs.totalCostTableComponent.hotInstance.loadData(currentYearlyData);
            }

            console.log(`Simulation ${simulationRowIndex} Costs Updated`);
        },

        // Post Simulationボタンを押した際のPOST処理
        postSimulationData(simulationRowIndex) {
            const userStore = useUserStore();
            const companyCode = userStore.companyCode; // PiniaからcompanyCodeを取得

            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const taskListData = hotInstance.getData(); // TaskListのデータ全体を取得

            // 送信するデータをマッピング
            const mappedData = taskListData.map((rowData, index) => {
                // taskOfPeriodが数値でない場合は0にデフォルト設定
                const taskOfPeriod = parseInt(rowData[7], 10);
                const validTaskOfPeriod = isNaN(taskOfPeriod) ? 0 : taskOfPeriod;

                // 日付をYYYY-MM-DD形式に変換
                let latestEventDate = rowData[6];
                if (latestEventDate && moment(latestEventDate, 'YYYY-MM-DD', true).isValid()) {
                    latestEventDate = moment(latestEventDate).format('YYYY-MM-DD'); // moment.jsで日付フォーマット
                } else {
                    latestEventDate = null; // 無効な日付はnullに設定
                }

                return {
                    companyCode: companyCode, // companyCodeは同じ
                    taskListNo: rowData[0], // taskListNoを取得
                    typicalTaskName: rowData[1], // タスク名
                    plant: rowData[2], // プラント名
                    equipment: rowData[3], // 設備名
                    machineName: rowData[4], // 機械名
                    PMType: rowData[5], // PMタイプ
                    typicalLatestDate: latestEventDate, // 最新イベント日付 (YYYY-MM-DD形式)
                    taskOfPeriod: validTaskOfPeriod, // タスク期間 (整数に変換)
                    totalLaborCost: parseFloat(rowData[8]) || 0, // 労働コスト
                    bomCode: rowData[9], // BOMコード
                    bomCost: parseFloat(rowData[10]) || 0 // BOMコスト
                };
            });

            // データを送信
            axios
                .post(`http://127.0.0.1:8000/api/simulation/no${simulationRowIndex}simulations/`, mappedData)
                .then((response) => {
                    // POST成功時に成功メッセージを表示
                    this.toast.add({ severity: 'success', summary: 'Success', detail: 'Simulation data posted successfully!', life: 3000 });
                    console.log(`Simulation ${simulationRowIndex} data posted successfully:`, response.data);
                })
                .catch((error) => {
                    // POST失敗時にエラーメッセージを表示
                    this.toast.add({ severity: 'error', summary: 'Error', detail: `Failed to post Simulation ${simulationRowIndex} data`, life: 3000 });
                    console.error(`Failed to post Simulation ${simulationRowIndex} data:`, error.response.data);
                });
        },

        // ここにシミュレーションの処理を追加
        // 月次コスト計算
        calculateMonthlyCosts() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = moment().year();
            const currentMonth = moment().month();
            let monthlyCosts = new Array(12).fill(0);

            hotInstance.getData().forEach((row, rowIndex) => {
                const latestEventDate = hotInstance.getDataAtRowProp(rowIndex, 'latestEventDate');
                const taskPeriod = parseInt(hotInstance.getDataAtRowProp(rowIndex, 'taskPeriod'));
                const totalCost = parseFloat(hotInstance.getDataAtRowProp(rowIndex, 'totalCost'));

                if (latestEventDate && moment(latestEventDate, 'YYYY-MM-DD', true).isValid() && !isNaN(taskPeriod) && !isNaN(totalCost)) {
                    let checkDate = moment(latestEventDate, 'YYYY-MM-DD');

                    while (checkDate.isSameOrBefore(moment().endOf('year'))) {
                        const eventYear = checkDate.year();
                        const eventMonth = checkDate.month();

                        if (eventYear === currentYear && eventMonth >= currentMonth) {
                            monthlyCosts[eventMonth] += totalCost;
                        }

                        checkDate.add(taskPeriod, 'days');
                    }
                }
            });

            const total = monthlyCosts.reduce((a, b) => a + b, 0);
            monthlyCosts.push(total);

            // Simulation1~3のデータを保持
            let currentData = this.$refs.monthlyCostTableComponent.hotInstance.getData();
            currentData[0] = monthlyCosts; // ベース行を更新
            this.$refs.monthlyCostTableComponent.hotInstance.loadData(currentData);

            console.log('Monthly Costs Updated:', monthlyCosts);
        },

        calculateTotalCostsPerYear() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = moment().year();
            const endYear = currentYear + 10;
            let yearlyCosts = new Array(11).fill(0);

            hotInstance.getData().forEach((row, rowIndex) => {
                const latestEventDate = hotInstance.getDataAtRowProp(rowIndex, 'latestEventDate');
                const taskPeriod = parseInt(hotInstance.getDataAtRowProp(rowIndex, 'taskPeriod'));
                const totalCost = parseFloat(hotInstance.getDataAtRowProp(rowIndex, 'totalCost'));

                if (latestEventDate && moment(latestEventDate, 'YYYY-MM-DD', true).isValid() && !isNaN(taskPeriod) && !isNaN(totalCost)) {
                    let checkDate = moment(latestEventDate, 'YYYY-MM-DD');

                    while (checkDate.year() <= endYear) {
                        const eventYear = checkDate.year();

                        if (eventYear >= currentYear && eventYear <= endYear) {
                            yearlyCosts[eventYear - currentYear] += totalCost;
                        }

                        checkDate.add(taskPeriod, 'days');
                    }
                }
            });

            let currentData = this.$refs.totalCostTableComponent.hotInstance.getData();
            currentData[0] = yearlyCosts; // ベース行を更新
            this.$refs.totalCostTableComponent.hotInstance.loadData(currentData);

            console.log('Yearly Costs Updated:', yearlyCosts);
        },

        // 新しいコスト計算関数を呼び出す
        calculateCosts() {
            this.calculateMonthlyCosts(); // 月次コストを計算
            this.calculateTotalCostsPerYear(); // 年次コストを計算
        },

        generateColHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());

            return [
                'TaskListNo',
                'TaskName',
                'Plant',
                'Equipment',
                'MachineName',
                'PM <br> type',
                'Maintenance <br> type',
                'LatestEvent<br>Date',
                'Task<br>Period',
                'TaskLabor<br>Cost',
                'BomCode',
                'BomCost',
                'TotalCost',
                'Next Even<br>Date',
                'Situation',
                ...futureYears
            ];
        },

        taskListNoRenderer(instance, td, row, col, prop, value, cellProperties) {
            Handsontable.renderers.TextRenderer.apply(this, arguments);
            if (value) {
                const link = document.createElement('a');
                link.href = `/task_list_detail/${value}`;
                link.target = '_blank';
                link.textContent = value;
                link.style.color = 'blue';
                td.innerHTML = '';
                td.appendChild(link);
            }
        },

        updateRowCount() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const newData = this.dataStore.slice(0, this.rowsToShow);
            hotInstance.loadData(newData);
        },

        getDataAxios() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;

            axios
                .get(url, {
                    headers: { 'Content-Type': 'application/json' },
                    withCredentials: true
                })
                .then((response) => {
                    const taskListData = response.data.flatMap((companyData) => companyData.taskList);

                    if (response.data.length > 0) {
                        this.companyCode = response.data[0].companyCode;
                    }

                    this.dataStore = taskListData;

                    if (taskListData.length < 15) {
                        const blankRows = Array.from({ length: 15 - taskListData.length }, () => ({}));
                        this.dataStore = this.dataStore.concat(blankRows);
                    }

                    this.$refs.hotTableComponent.hotInstance.updateSettings({
                        data: this.dataStore
                    });
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },

        calculateTotalCost(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const taskLaborCost = parseFloat(hotInstance.getDataAtRowProp(row, 'taskLaborCost')) || 0;
            const bomCost = parseFloat(hotInstance.getDataAtRowProp(row, 'bomCost')) || 0;
            const totalCost = taskLaborCost + bomCost;
            hotInstance.setDataAtRowProp(row, 'totalCost', totalCost);
        },

        calculateNextEventDate(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const latestEventDate = hotInstance.getDataAtRowProp(row, 'latestEventDate');
            const taskPeriod = hotInstance.getDataAtRowProp(row, 'taskPeriod');

            if (!taskPeriod || taskPeriod === 0) {
                hotInstance.setDataAtRowProp(row, 'nextEventDate', '');
                this.calculateSituation(row);
                return;
            }

            if (latestEventDate) {
                const nextEventDate = moment(latestEventDate).add(taskPeriod, 'days').format('YYYY-MM-DD');
                hotInstance.setDataAtRowProp(row, 'nextEventDate', nextEventDate);
                this.calculateSituation(row);
            }
        },

        calculateYears(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const latestEventDate = hotInstance.getDataAtRowProp(row, 'latestEventDate');
            const taskPeriod = hotInstance.getDataAtRowProp(row, 'taskPeriod');
            const startYear = moment().year();
            const endYear = startYear + 10;

            if (taskPeriod && taskPeriod <= 365) {
                for (let i = 0; i <= 10; i++) {
                    hotInstance.setDataAtRowProp(row, `thisYear${i === 0 ? '' : `${i}later`}`, true);
                }
                return;
            }

            for (let i = 0; i <= 10; i++) {
                hotInstance.setDataAtRowProp(row, `thisYear${i === 0 ? '' : `${i}later`}`, false);
            }

            if (!latestEventDate || !taskPeriod) return;

            let currentEventDate = moment(latestEventDate);
            while (currentEventDate.year() <= endYear) {
                const currentYear = currentEventDate.year();
                if (currentYear >= startYear && currentYear <= endYear) {
                    const yearIndex = currentYear - startYear;
                    hotInstance.setDataAtRowProp(row, `thisYear${yearIndex === 0 ? '' : `${yearIndex}later`}`, true);
                }
                currentEventDate.add(taskPeriod, 'days');
            }
        },

        calculateSituation(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const nextEventDate = hotInstance.getDataAtRowProp(row, 'nextEventDate');
            const today = moment().format('YYYY-MM-DD');

            if (nextEventDate && moment(nextEventDate).isBefore(today)) {
                hotInstance.setDataAtRowProp(row, 'situation', 'delay');
            } else {
                hotInstance.setDataAtRowProp(row, 'situation', '');
            }
        },
        // シミュレーションボタンの有効化を確認する関数
        checkSimulationButtonStatus(newVal, oldVal) {
            for (let i = 0; i < newVal.length; i++) {
                if (newVal[i].latestEventDate !== oldVal[i].latestEventDate || newVal[i].taskPeriod !== oldVal[i].taskPeriod || newVal[i].taskLaborCost !== oldVal[i].taskLaborCost || this.isYearCheckboxChanged(newVal[i])) {
                    this.isSimulationActive = true;
                    return; // 条件を満たしたら即座に有効化して終了
                }
            }
        },

        isYearCheckboxChanged(row) {
            const currentYear = moment().year();
            for (let i = 0; i <= 10; i++) {
                const yearProp = `thisYear${i === 0 ? '' : `${i}later`}`;
                if (row[yearProp] !== undefined && row[yearProp]) {
                    return true;
                }
            }
            return false;
        },

        handleTableChange(changes) {
            changes.forEach(([row, prop, oldValue, newValue]) => {
                if (oldValue !== newValue) {
                    this.tableData[row][prop] = newValue; // Vueのdataプロパティに値を反映
                }
            });
        },
        mounted() {
            // 変更監視のための設定
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            hotInstance.addHook('afterChange', this.handleTableChange);
        }
    },

    setup() {
        const toast = useToast(); // Toastフックの利用
        return {
            toast
        };
    },
    components: {
        HotTable,
        Button
    }
});

export default TaskListComponent;
</script>

<style scoped>
#TaskList {
    padding: 20px;
}

.tables-container {
    display: flex; /* 横並び配置 */
    gap: 20px; /* テーブル間のスペース */
}

#monthlyCostTable,
#totalCostTable {
    width: 50%; /* テーブルの幅を50%ずつに設定 */
}

.company-code-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
    font-weight: bold;
}

.simulation-buttons-container,
.post-simulation-container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    margin-bottom: 15px;
}

.simulation-button,
.post-simulation-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
}

.simulation-button {
    background-color: #007bff;
    color: white;
}

.post-simulation-btn {
    background-color: #28a745;
    color: white;
}

.simulation-button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

.row-count-container {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-bottom: 15px;
}

.row-count-container span {
    margin-right: 10px;
    font-weight: bold;
}

.legend {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.legend-item {
    display: flex;
    align-items: center;
    margin-right: 15px;
}

.color-box {
    width: 20px;
    height: 20px;
    margin-right: 10px;
    border: 1px solid #000;
}

.read-only-cell {
    background-color: #f5f5f5;
    color: black;
}

.blue-button {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
}

.green-button {
    background-color: #28a745;
    border-color: #28a745;
    color: white;
}

.orange-button {
    background-color: #ff7f0e;
    border-color: #ff7f0e;
    color: white;
}

.row-input {
    width: 150px;
    padding: 5px;
    margin-right: 10px;
}

.simulation-description {
    font-size: 12px;
    color: #666; /* グレー色で目立たせない */
    margin-top: 5px; /* ボタンとの間に少し間隔を空ける */
}

/* Calculationボタンのデザイン */
.calculation-button {
    background-color: #ff6347;  /* 鮮やかなオレンジ色 */
    color: white;
    border: none;
    border-radius: 5px;  /* ボタンの角を丸く */
    padding: 10px 20px;  /* パディングでボタンを大きく */
    font-size: 16px;  /* フォントサイズを調整 */
    cursor: pointer;
    transition: background-color 0.3s ease;  /* マウスホバー時の背景色変更をスムーズに */
}

.calculation-button:hover {
    background-color: #e55335;  /* ホバー時に少し暗くなる */
}
</style>
