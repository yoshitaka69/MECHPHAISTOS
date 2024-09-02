<template>
    <div id="TaskList">
        <!-- 成功時または失敗時のアラート表示 -->
        <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />

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
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
        <div class="button-container">
            <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
            <Button label="Add Rows" icon="pi pi-plus" class="p-button-primary blue-button" @click="addRows" />
            <Button label="Save Data" icon="pi pi-save" class="p-button-primary blue-button ml-3" @click="saveData" />
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
import Save_Alert from '@/components/Alert/Save_Alert.vue';

// register Handsontable's modules
registerAllModules();

const TaskListComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', 'true'], //1
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', 'true'], //2
                    ['PlantA', 'Dryer', 'blower', '2018-10-20', 'Change bearing', '5000', '5', 'true', 'BomCode-1', '58090', '111222', '', '遅延', 'true', '', '', '', '', '', '', '', '', 'true'], //3
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
                    {
                        data: 'taskListNo',
                        type: 'text',
                        readOnly: true,
                        renderer: this.taskListNoRenderer // 修正したカスタムレンダラーを使用
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
                        readOnly: true
                    },
                    {
                        //TaskName
                        data: 'typicalTaskName',
                        type: 'text'
                    },
                    {
                        //TaskLaborCost
                        data: 'typicalTaskCost',
                        type: 'numeric'
                    },
                    {
                        //TaskConstructionCost
                        data: 'typicalConstPeriod',
                        type: 'numeric'
                    },
                    {
                        //MultiTasking
                        data: 'multiTasking',
                        type: 'checkbox',
                        className: 'htCenter'
                    },
                    {
                        //BomCode
                        data: 'bomCode',
                        type: 'text',
                        readOnly: true
                    },
                    {
                        //BomCost
                        data: 'bomCodeCost',
                        type: 'numeric',
                        readOnly: true
                    },
                    {
                        //TotalCost
                        data: 'totalCost',
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
                        return;
                    }
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
                licenseKey: 'non-commercial-and-evaluation'
            },
            rowsToAdd: 1,
            dataStore: [],
            showAlert: false,
            alertType: 'success',
            alertMessage: 'データが正常に保存されました。',
            errorMessages: []
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
                'TaskListNo',
                'Plant',
                'Equipment',
                'MachineName',
                'LatestDate<br>PM',
                'TaskName',
                'TaskLabor<br>Cost',
                'TaskConstruction<br>Period',
                'Multi<br>Tasking',
                'BomCode',
                'BomCost',
                'TotalCost',
                'Next Even<br>date',
                'Situation',
                ...futureYears
            ];
        },

        taskListNoRenderer(instance, td, row, col, prop, value, cellProperties) {
            Handsontable.renderers.TextRenderer.apply(this, arguments);
            if (value) {
                const link = document.createElement('a');
                link.href = `/task_list_detail/${value}`; // ルーティングに対応するURLを生成
                link.target = '_blank';
                link.textContent = value;
                link.style.color = 'blue';
                td.innerHTML = '';
                td.appendChild(link);
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

        addRows() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const blankRows = Array.from({ length: this.rowsToAdd }, () => {
                return {
                    taskListNo: '',
                    plant: '',
                    equipment: '',
                    machineName: '',
                    typicalLatestDate: '',
                    typicalTaskName: '',
                    typicalTaskCost: 0,
                    typicalConstPeriod: 0,
                    multiTasking: false,
                    bomCode: '',
                    bomCodeCost: 0,
                    totalCost: 0,
                    typicalNextEventDate: '',
                    typicalSituation: '',
                    thisYear: false,
                    thisYear1later: false,
                    thisYear2later: false,
                    thisYear3later: false,
                    thisYear4later: false,
                    thisYear5later: false,
                    thisYear6later: false,
                    thisYear7later: false,
                    thisYear8later: false,
                    thisYear9later: false,
                    thisYear10later: false
                };
            });

            this.dataStore = this.dataStore.concat(blankRows);

            hotInstance.updateSettings({
                data: this.dataStore
            });
        },

        saveData() {
            try {
                const userStore = useUserStore();
                const userCompanyCode = userStore.companyCode;

                if (!userCompanyCode) {
                    console.error('Error: No company code found for the user.');
                    return;
                }

                const hotInstance = this.$refs.hotTableComponent.hotInstance;
                const dataToSave = hotInstance.getData();

                const formattedData = dataToSave.map((row, index) => {
                    return {
                        companyCode: userCompanyCode,
                        taskListNo: row[0] || null,
                        plant: row[1],
                        equipment: row[2],
                        machineName: row[3],
                        typicalLatestDate: row[4],
                        typicalTaskName: row[5],
                        typicalTaskCost: row[6],
                        typicalConstPeriod: row[7],
                        multiTasking: row[8],
                        bomCode: row[9],
                        bomCost: row[10],
                        totalCost: row[11],
                        typicalNextEventDate: row[12],
                        typicalSituation: row[13],
                        thisYear: row[14] !== null ? row[14] : false,
                        thisYear1later: row[15] !== null ? row[15] : false,
                        thisYear2later: row[16] !== null ? row[16] : false,
                        thisYear3later: row[17] !== null ? row[17] : false,
                        thisYear4later: row[18] !== null ? row[18] : false,
                        thisYear5later: row[19] !== null ? row[19] : false,
                        thisYear6later: row[20] !== null ? row[20] : false,
                        thisYear7later: row[21] !== null ? row[21] : false,
                        thisYear8later: row[22] !== null ? row[22] : false,
                        thisYear9later: row[23] !== null ? row[23] : false,
                        thisYear10later: row[24] !== null ? row[24] : false
                    };
                });

                console.log('送信するデータ:', JSON.stringify(formattedData, null, 2));

                const url = `http://127.0.0.1:8000/api/task/taskList/`;

                axios
                    .post(url, formattedData, {
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        withCredentials: true
                    })
                    .then((response) => {
                        console.log('Data saved successfully:', response.data);
                        this.alertType = 'success';
                        this.alertMessage = 'データが正常に保存されました。';
                        this.showAlert = true;
                        setTimeout(() => {
                            this.showAlert = false;
                        }, 3000);
                    })
                    .catch((error) => {
                        console.error('Error saving data:', error);

                        if (error.response) {
                            console.error('Error response status:', error.response.status);
                            console.error('Error response headers:', error.response.headers);
                            console.error('Error response data:', error.response.data);
                        } else if (error.request) {
                            console.error('Error request data:', error.request);
                        } else {
                            console.error('Error message:', error.message);
                        }

                        console.error('Error config:', error.config);
                        this.alertType = 'error';
                        this.alertMessage = 'データの保存に失敗しました。エラーを確認してください。';
                        this.errorMessages = ['Quis commodo odio aenean sed adipiscing diam.', 'Risus pretium quam vulputate dignissim suspendisse.', 'Bibendum enim facilisis gravida neque convallis a cras semper。'];
                        this.showAlert = true;
                        setTimeout(() => {
                            this.showAlert = false;
                        }, 5000);
                    });
            } catch (err) {
                console.error('An error occurred in saveData:', err);
            }
        }
    },
    components: {
        HotTable,
        Button,
        Save_Alert
    }
});
export default TaskListComponent;
</script>

<style scoped>
.button-container {
    display: flex;
    gap: 10px;
    margin-top: 10px;
}

.legend {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
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

.blue-button {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
}
</style>
