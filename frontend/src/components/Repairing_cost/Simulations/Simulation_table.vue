<template>
    <div id="app">
        <div id="totalCostTable">
            <hot-table ref="totalCostTableComponent" :settings="totalCostSettings"></hot-table>
        </div>
        <div id="TaskList">
            <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
            <button v-on:click="updateData" class="controls">Update Data</button>
            <!-- 新しいボタンを追加 -->
            <button v-on:click="calculateTotalCostSums" class="controls">Calculate Total Costs</button>
        </div>
    </div>
</template>

<script>
import Handsontable from 'handsontable'; //独自のレンダラーを使用するときに使う。
import { defineComponent, watch } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

// register Handsontable's modules
registerAllModules();

const TaskListComponent = defineComponent({
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
                colHeaders: this.generateColHeaders(), // ヘッダーを生成するメソッドを使用 消すな‼
                columns: [
                    {
                        //TaskName
                        data: 'typicalTaskName',
                        type: 'text'
                    },
                    {
                        //plant
                        data: 'plant',
                        type: 'text'
                    },
                    {
                        //Equipment
                        data: 'equipment',
                        type: 'text'
                    },
                    {
                        //MachineName
                        data: 'machineName',
                        type: 'text'
                    },
                    {
                        //Latest Date PM
                        data: 'typicalLatestDate',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false
                    },

                    {
                        //MultiTasking
                        data: 'multiTasking',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //TotalCost
                        data: 'totalCost',
                        type: 'numeric'
                    },
                    {
                        data: 'taskOfPeriod',
                        type: 'numeric'
                    },
                    {
                        //Next event date
                        data: 'typicalNextEventDate',
                        type: 'numeric',
                        readOnly: true
                    },
                    {
                        //Situation
                        data: 'typicalSituation',
                        type: 'text',
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（今）
                        data: 'thisYear',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（1年後）
                        data: 'thisYear1later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（2年後）
                        data: 'thisYear2later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（3年後）
                        data: 'thisYear3later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（4年後）
                        data: 'thisYear4later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（5年後）
                        data: 'thisYear5later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（6年後）
                        data: 'thisYear6later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（7年後）
                        data: 'thisYear7later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（8年後）
                        data: 'thisYear8later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（9年後）
                        data: 'thisYear9later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    },
                    {
                        //現時点からの10年先まで繰り返し（10年後）
                        data: 'thisYear10later',
                        type: 'checkbox',
                        className: 'htCenter',
                        renderer: this.customCheckboxRenderer,
                        readOnly: true
                    }
                ],

                afterGetColHeader: (col, TH) => {
                    if (col === -1) {
                        // ヘッダー行の場合
                        return;
                    }
                    // 全ヘッダーセルにスタイルを設定
                    TH.style.backgroundColor = '#FFFFCC'; // 薄い黄色
                    TH.style.color = 'black'; // テキスト色を黒に設定
                    TH.style.fontWeight = 'bold'; // テキストを太字に設定
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
                contextMenu: true, //コンテキストメニュー
                autoWrapRow: true,
                autoWrapCol: true,
                fixedColumnsStart: 2, //カラム固定
                fixedRowsTop: 2, //列固定
                manualColumnFreeze: true, //コンテキストメニュー手動でコラム解除
                manualColumnResize: true, //手動での列幅調整
                manualRowResize: true, //列の手動高さ調整
                filters: true,
                dropdownMenu: true,
                comments: true, //コメントの有り無し
                fillHandle: {
                    autoInsertRow: true
                },
                licenseKey: 'non-commercial-and-evaluation'
            },

            //上部の別のtotalCostTabel
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
                rowHeaders: ['Total'], // ここで各行の名前を設定
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                autoColumnSize: true, // 列幅を自動調整
                autoRowSize: true, // 行の高さを自動調整
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
            }
        };
    },
    watch: {
        // 'hotSettings.data' の変更を監視
        'hotSettings.data': {
            deep: true,
            handler(newVal, oldVal) {
                if (newVal !== oldVal) {
                    this.calculateTotalCostSums();
                }
            }
        }
    },

    methods: {
        generateColHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());

            return ['TaskName', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'Multi<br>Tasking', 'TotalCost', 'Task Of Period', 'Next Even<br>date', 'Situation', ...futureYears];
        },

        //totalCostSettingsのヘッダーを生成
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
                td.style.background = '#90EE90'; // ライトグリーン
                td.querySelector('input[type="checkbox"]').checked = true;
            }
        },

        // 10年間でマッチする全ての年を返す
        getMatchingYears(instance, row) {
            const latestDate = instance.getDataAtRowProp(row, 'typicalLatestDate');
            const taskOfPeriod = instance.getDataAtRowProp(row, 'taskOfPeriod');
            const matchedYears = [];

            if (!latestDate || !taskOfPeriod) return matchedYears;

            let checkDate = new Date(latestDate);
            const currentYear = new Date().getFullYear();
            const endYear = currentYear + 10;

            //console.log(`Starting check from date: ${latestDate} with period of ${taskOfPeriod} days.`);

            while (checkDate.getFullYear() <= endYear) {
                const futureYear = checkDate.getFullYear();
                if (futureYear >= currentYear) {
                    matchedYears.push(futureYear);
                }
                //console.log(`FutureDate: ${checkDate.toISOString()}, FutureYear: ${futureYear}`);

                checkDate = new Date(checkDate.setDate(checkDate.getDate() + taskOfPeriod));
            }

            //console.log(`Matched Years: ${matchedYears}`);
            return matchedYears;
        },

        /**
         * 各セルの年に基づいてチェックボックスを自動的にチェックする
         */
        checkAndFillYearlyTasks() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const rowCount = hotInstance.countRows();
            for (let row = 0; row < rowCount; row++) {
                const matchedYears = this.getMatchingYears(hotInstance, row);
                const currentYear = new Date().getFullYear();
                for (let col = 10; col <= 20; col++) {
                    // 'thisYear'から'thisYear10later'まで
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

                    this.$refs.hotTableComponent.hotInstance.updateSettings({
                        data: newData
                    });
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },

        // 他のメソッドと...
        calculateTotalCostSums() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const currentYear = new Date().getFullYear();

            // 各年の合計値を格納する配列を初期化
            let sums = new Array(11).fill(0);

            console.log('Starting total cost calculation for each year.');

            // 全データ行をループして処理
            hotInstance.getData().forEach((row, rowIndex) => {
                for (let i = 0; i < 11; i++) {
                    // この年から10年後までの各年について
                    const checkboxColumnIndex = 10 + i; // チェックボックスの列インデックス
                    const isChecked = row[checkboxColumnIndex]; // チェックボックスがtrueかどうか
                    const totalCost = parseFloat(row[6]); // TotalCostは6番目の列
                    console.log(`Year index ${i}: Checkbox is ${isChecked ? 'checked' : 'not checked'}, TotalCost: ${totalCost}`);

                    if (!isChecked && !isNaN(totalCost)) {
                        // チェックボックスが未チェックの場合に加算
                        sums[i] += totalCost; // 対応する年の合計に加算
                        console.log(`Added ${totalCost} to year ${currentYear + i} sum, new total: ${sums[i]}`);
                    }
                }
            });

            console.log('All rows processed, final sums for each year:', sums);

            // totalCostTableのデータを更新
            this.$refs.totalCostTableComponent.hotInstance.loadData([sums]); // 2D配列としてデータを渡す
            console.log('Total Costs Sums Updated:', sums);
        },

        mounted() {
            this.getDataAxios().then(() => {
                this.checkAndFillYearlyTasks();
                this.calculateTotalCostSums(); // データ取得後、合計計算も実行
            });
        }
    },
    components: {
        HotTable
    }
});
export default TaskListComponent;
</script>

<style>
#totalCostTable {
    margin-bottom: 20px;
}
</style>
