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
import axios from "axios";
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

// register Handsontable's modules
registerAllModules();

const TaskListComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', '', 'true',],//1
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', '', 'true',],//2
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', '', 'true',],//3
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//4
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//5
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//6
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//7
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//8
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//9
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//10
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//11
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//12
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//13
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//14
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//15

                ],
                colHeaders: this.generateColHeaders(), // ヘッダーを生成するメソッドを使用 消すな‼

                columns: [
                    {//taskListNo
                        data: 'taskListNo',
                        type: "text",
                    },
                    {//plant
                        data: 'plant',
                        type: "text",
                    },
                    {//Equipment
                        data: 'equipment',
                        type: "text",

                    },
                    {//MachineName
                        data: 'machineName',
                        type: "text",

                    },
                    {//Latest Date PM
                        data: 'typicalLatestDate',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,
                        readOnly: true,
                    },
                    {//TaskName
                        data: 'typicalTaskName',
                        type: "text",
                    },
                    {//TaskLaborCost
                        data: 'typicalTaskCost',
                        type: 'numeric',
                    },
                    {//TaskConstructionCost
                        data: 'typicalConstPeriod',
                        type: 'numeric',
                    },
                    {//MultiTasking
                        data: 'multiTasking',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//BomCode
                        data: 'bomCode',
                        type: 'text',
                        readOnly: true,
                    },
                    {//BomCost
                        data: 'bomCodeCost',
                        type: 'numeric',
                        readOnly: true,
                    },
                    {//TotalCost
                        data: 'totalCost',
                        type: 'numeric',
                    },
                    {//Next event date
                        data: 'typicalNextEventDate',
                        type: 'numeric',
                        readOnly: true,
                    },
                    {//Situation
                        data: 'typicalSituation',
                        type: 'text',
                    },
                    {//現時点からの10年先まで繰り返し（今）
                        data: 'thisYear',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（1年後）
                        data: 'thisYear1later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（2年後）
                        data: 'thisYear2later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（3年後）
                        data: 'thisYear3later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（4年後）
                        data: 'thisYear4later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（5年後）
                        data: 'thisYear5later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（6年後）
                        data: 'thisYear6later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（7年後）
                        data: 'thisYear7later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（8年後）
                        data: 'thisYear8later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（9年後）
                        data: 'thisYear9later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {//現時点からの10年先まで繰り返し（10年後）
                        data: 'thisYear10later',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                ],

                width: '100%',
                height: 'auto',
                contextMenu: true,//コンテキストメニュー
                autoWrapRow: true,
                autoWrapCol: true,
                fixedColumnsStart: 2,//カラム固定
                fixedRowsTop: 2,//列固定
                manualColumnFreeze: true,//コンテキストメニュー手動でコラム解除
                manualColumnResize: true,//手動での列幅調整
                manualRowResize: true,//列の手動高さ調整
                filters: true,
                dropdownMenu: true,
                comments: true,//コメントの有り無し
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

            return [
                'TaskListNo', 'Plant', 'Equipment', 'MachineName', 'LatestDate<br>PM', 'TaskName', 'TaskLabor<br>Cost', 'TaskConstruction<br>Period',
                'Multi<br>Tasking', 'BomCode', 'BomCost', 'TotalCost', 'Next Even<br>date', 'Situation', ...futureYears
            ];
        },

        getDataAxios() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error("Error: No company code found for the user.");
                return;
            }

            const url = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;

            axios.get(url, {
                headers: {
                    "Content-Type": "application/json"
                },
                withCredentials: true
            })
                .then(response => {
                    const taskListData = response.data.flatMap(companyData => companyData.taskList);
                    console.log("Fetched Task List Data:", taskListData);

                    // Handsontable設定の更新
                    this.$refs.hotTableComponent.hotInstance.updateSettings({
                        data: taskListData,
                        // ここで他の必要な設定を更新することも可能
                    });
                })
                .catch(error => {
                    console.error("Error fetching data:", error);
                });
        },

        updateData() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error("Error: No company code found for the user.");
                return;
            }

            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const rowCount = hotInstance.countRows();
            let taskList = [];

            for (let i = 0; i < rowCount; i++) {
                let rowData = hotInstance.getDataAtRow(i);
                let taskListNo = i + 1; // 0-indexedから1-indexedに変更

                let taskListItem = {
                    companyCode: userCompanyCode,
                    taskListNo: taskListNo,
                    plant: rowData[1],
                    equipment: rowData[2],
                    machineName: rowData[3],
                    typicalLatestDatePM: rowData[4],
                    typicalTaskName: rowData[5],
                    typicalTaskCost: rowData[6],
                    typicalConstPeriod: rowData[7],
                    multiTasking: rowData[8],
                    bomCode: rowData[9],
                    bomCodeCost: rowData[10],
                    totalCost: rowData[11],
                    typicalNextEventDate: rowData[12],
                    typicalSituation: rowData[13],
                    thisYear: rowData[14],
                    thisYear1later: rowData[15],
                    thisYear2later: rowData[16],
                    thisYear3later: rowData[17],
                    thisYear4later: rowData[18],
                    thisYear5later: rowData[19],
                    thisYear6later: rowData[20],
                    thisYear7later: rowData[21],
                    thisYear8later: rowData[22],
                    thisYear9later: rowData[23],
                    thisYear10later: rowData[24],
                };

                taskList.push(taskListItem);
            }

            let postData = {
                companyCode: userCompanyCode,
                taskList: taskList
            };

            console.log("postData", postData);

            const backendUrl = `http://127.0.0.1:8000/api/task/taskListByCompany/?format=json&companyCode=${userCompanyCode}`;
            axios.post(backendUrl, postData)
                .then(response => {
                    console.log("Data posted successfully", response.data);
                })
                .catch(error => {
                    console.error("Error in posting data", error);
                });
        }

    },
    components: {
        HotTable,
    },
}
);
export default TaskListComponent;
</script>