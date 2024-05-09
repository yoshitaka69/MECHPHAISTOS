<template>
    <div id="TaskList">
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
        <button v-on:click="updateData" class="controls">Update Data</button>
    </div>
</template>

<script>
import Handsontable from 'handsontable'; //独自のレンダラーを使用するときに使う。
import { defineComponent } from 'vue';
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
                        correctFormat: false,
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
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（1年後）
                        data: 'thisYear1later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（2年後）
                        data: 'thisYear2later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（3年後）
                        data: 'thisYear3later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（4年後）
                        data: 'thisYear4later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（5年後）
                        data: 'thisYear5later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（6年後）
                        data: 'thisYear6later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（7年後）
                        data: 'thisYear7later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（8年後）
                        data: 'thisYear8later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（9年後）
                        data: 'thisYear9later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //現時点からの10年先まで繰り返し（10年後）
                        data: 'thisYear10later',
                        type: 'checkbox',
                        className: 'htCenter'
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
            }
        };
    },

    created() {
        this.getDataAxios();
    },

    methods: {
        generateColHeaders() {
            const currentYear = new Date().getFullYear();
            const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());

            return ['TaskName', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'Multi<br>Tasking', 'TotalCost', 'Task Of Period', 'Next Even<br>date', 'Situation', ...futureYears];
        },

    customCheckboxRenderer(instance, td, row, col, prop, value, cellProperties) {
        // 標準のチェックボックスレンダラーを適用
        Handsontable.renderers.CheckboxRenderer.apply(this, arguments);
        // 特定の年に該当するかどうかをチェック
        if (this.isMatchingYear(instance, row, col)) {
            // 条件に合致した場合、セルの背景をライトグリーンに設定
            td.style.background = '#90EE90';
            // チェックボックスを選択状態にする
            td.querySelector('input[type="checkbox"]').checked = true;
        }
    },


    isMatchingYear(instance, row, col) {
        // 'typicalLatestDate'から日付を取得
        const latestDate = instance.getDataAtRowProp(row, 'typicalLatestDate');
        // 'taskOfPeriod'から期間（日数）を取得
        const taskOfPeriod = instance.getDataAtRowProp(row, 'taskOfPeriod');
        // 日付または期間が存在しない場合、falseを返す
        if (!latestDate || !taskOfPeriod) return false;

        // 日付を加工
        let checkDate = new Date(latestDate);
        // 現在の年を取得
        const currentYear = new Date().getFullYear();
        // 列に対応する年を計算（'thisYear'列が10番目であるためのオフセット）
        const colYear = currentYear + (col - 10);

        // 日付に期間を加算
        checkDate.setDate(checkDate.getDate() + taskOfPeriod);
        // 計算された年が列の年と一致するかを確認
        return checkDate.getFullYear() === colYear;
    },

    /**
     * 各セルの年に基づいてチェックボックスを自動的にチェックする
     */
    checkAndFillYearlyTasks() {
        // Handsontableインスタンスを取得
        const hotInstance = this.$refs.hotTableComponent.hotInstance;
        // 行数を取得
        const rowCount = hotInstance.countRows();

        // 全行と特定の列（年に対応する列）に対してループ
        for (let row = 0; row < rowCount; row++) {
            for (let col = 10; col <= 20; col++) { // 'thisYear'から'thisYear10later'まで
                // 指定した年がマッチするかチェック
                if (this.isMatchingYear(hotInstance, row, col)) {
                    // マッチした場合、セルの値をtrue（チェック済み）に設定
                    hotInstance.setDataAtCell(row, col, true);
                }
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

            axios
                .get(url, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                .then((response) => {
                    const taskListData = response.data.flatMap((companyData) => companyData.taskList);
                    console.log('Fetched Task List Data:', taskListData);

                    // 空行を追加
                    const blankRows = Array.from({ length: 20 }, () => ({}));
                    const newData = taskListData.concat(blankRows);

                    // Handsontable設定の更新
                    this.$refs.hotTableComponent.hotInstance.updateSettings({
                        data: newData
                        // ここで他の必要な設定を更新することも可能
                    });
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        }
    },
    components: {
        HotTable
    }
});
export default TaskListComponent;
</script>
