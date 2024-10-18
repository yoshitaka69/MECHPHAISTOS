<template>
    <div id="TaskList">
        <!-- 成功時または失敗時のアラート表示 -->
        <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />

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

        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />

        <div class="button-container">
            <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
            <Button label="Add Rows" icon="pi pi-plus" class="p-button-primary blue-button" @click="addRows" />
            <Button label="Save Data" icon="pi pi-save" class="p-button-primary blue-button ml-3" @click="saveData" />
            <Button label="Export CSV" icon="pi pi-file-excel" class="p-button-primary green-button ml-3" @click="exportCSV" />
            <!-- 行番号入力と計算ボタン -->
            <input type="number" v-model="rowToRecalculate" placeholder="Row number to recalculate (1-based)" class="row-input" />
            <Button label="Recalculate Row" icon="pi pi-refresh" class="p-button-primary orange-button ml-3" @click="recalculateRowByInput" />
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
import moment from 'moment'; // 日付計算のために moment.js を使用

// register Handsontable's modules
registerAllModules();

const TaskListComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [],
                colHeaders: this.generateColHeaders(),
                columns: [
                    {
                        data: 'taskListNo',
                        type: 'text',
                        readOnly: true,
                        renderer: this.taskListNoRenderer
                    },
                    {
                        data: 'taskName',
                        type: 'text'
                    },
                    {
                        data: 'plant',
                        type: 'text'
                    },
                    {
                        data: 'equipment',
                        type: 'text'
                    },
                    {
                        data: 'machineName',
                        type: 'text'
                    },
                    {
                        data: 'pmType',
                        type: 'dropdown',
                        source: ['PM01', 'PM02', 'PM03', 'PM04', 'PM05'],
                        strict: true,
                        allowInvalid: false
                    },
                    {
                        data: 'maintenanceType',
                        type: 'dropdown',
                        source: ['Overhaul', 'Regular Maintenance', 'Inspection and Check', 'Adjustment', 'Parts Replacement', 'Calibration', 'Cleaning', 'Lubrication', 'Balancing', 'Testing and Trial Operation'],
                        strict: true,
                        allowInvalid: false
                    },
                    {
                        data: 'latestEventDate',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false
                    },
                    {
                        data: 'taskPeriod',
                        type: 'numeric'
                    },
                    {
                        data: 'taskLaborCost',
                        type: 'numeric'
                    },
                    {
                        data: 'bomCode',
                        type: 'text'
                    },
                    {
                        data: 'bomCost',
                        type: 'numeric'
                    },
                    {
                        data: 'totalCost',
                        type: 'numeric',
                        readOnly: true
                    },
                    {
                        data: 'nextEventDate',
                        type: 'text',
                        readOnly: true
                    },
                    {
                        data: 'situation',
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

                afterGetColHeader: (col, TH) => {
                    if (col === -1) return;
                    TH.style.backgroundColor = '#FFFFCC';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },

                afterChange: (changes, source) => {
                    if (source === 'edit' || source === 'autofill') {
                        changes.forEach(([row, prop, oldValue, newValue]) => {
                            if (['taskLaborCost', 'bomCost'].includes(prop)) {
                                this.calculateTotalCost(row);
                            }
                            if (['latestEventDate', 'taskPeriod'].includes(prop)) {
                                this.calculateNextEventDate(row);
                                this.calculateYears(row);
                            }
                        });
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
                fixedRowsTop: 0,
                manualColumnFreeze: true,
                manualColumnResize: true,
                manualRowResize: true,
                filters: true,
                dropdownMenu: true,
                comments: false,  // コメント機能をオフにする
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
            errorMessages: [],
            companyCode: '',
            rowsToShow: 10,
            rowToRecalculate: 1 // 再計算する行番号を格納（1-based index）
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
                    headers: {
                        'Content-Type': 'application/json'
                    },
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

        addRows() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const blankRows = Array.from({ length: this.rowsToAdd }, () => {
                return {
                    taskListNo: '',
                    taskName: '',
                    plant: '',
                    equipment: '',
                    machineName: '',
                    pmType: 'PM01',
                    maintenanceType: 'Overhaul',
                    latestEventDate: '',
                    taskPeriod: 0,
                    taskLaborCost: 0,
                    bomCode: '',
                    bomCost: 0,
                    totalCost: 0,
                    nextEventDate: '',
                    situation: '',
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
                        taskName: row[1],
                        plant: row[2],
                        equipment: row[3],
                        machineName: row[4],
                        pmType: row[5],
                        maintenanceType: row[6],
                        latestEventDate: row[7],
                        taskPeriod: row[8],
                        taskLaborCost: row[9],
                        bomCode: row[10],
                        bomCost: row[11],
                        totalCost: row[12],
                        nextEventDate: row[13],
                        situation: row[14],
                        thisYear: row[15] !== null ? row[15] : false,
                        thisYear1later: row[16] !== null ? row[16] : false,
                        thisYear2later: row[17] !== null ? row[17] : false,
                        thisYear3later: row[18] !== null ? row[18] : false,
                        thisYear4later: row[19] !== null ? row[19] : false,
                        thisYear5later: row[20] !== null ? row[20] : false,
                        thisYear6later: row[21] !== null ? row[21] : false,
                        thisYear7later: row[22] !== null ? row[22] : false,
                        thisYear8later: row[23] !== null ? row[23] : false,
                        thisYear9later: row[24] !== null ? row[24] : false,
                        thisYear10later: row[25] !== null ? row[25] : false
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
        },

        // totalCost を計算する関数
        calculateTotalCost(row) {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;

            // taskLaborCost と bomCost を数値に変換
            const taskLaborCost = parseFloat(hotInstance.getDataAtRowProp(row, 'taskLaborCost')) || 0;
            const bomCost = parseFloat(hotInstance.getDataAtRowProp(row, 'bomCost')) || 0;

            // 合計を計算
            const totalCost = taskLaborCost + bomCost;

            // 計算結果を totalCost に設定
            hotInstance.setDataAtRowProp(row, 'totalCost', totalCost);
        },

        // nextEventDate を計算する関数
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

        // 年次チェックボックスを更新する関数
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

            if (!latestEventDate || !taskPeriod) {
                return;
            }

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

        // situation を計算する関数
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

        // 入力された行番号で再計算を行う関数
        recalculateRowByInput() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            // 1-based index から 0-based index に変換
            const row = this.rowToRecalculate - 1;

            if (row < 0 || row >= this.dataStore.length) {
                console.error(`Invalid row number: ${row + 1}`);
                return;
            }

            console.log(`Recalculating for row: ${row + 1}`);
            this.calculateTotalCost(row);
            this.calculateNextEventDate(row);
            this.calculateYears(row);
        },

        exportCSV() {
            const headers = [
                'TaskListNo',
                'TaskName',
                'Plant',
                'Equipment',
                'MachineName',
                'PM Type',
                'Maintenance Type',
                'LatestEvent Date',
                'Task Period',
                'TaskLabor Cost',
                'BomCode',
                'BomCost',
                'TotalCost',
                'Next Event Date',
                'Situation',
                ...Array.from({ length: 11 }, (_, index) => `Year ${index + 1}`)
            ];

            const csvContent = [headers];

            this.dataStore.forEach((item) => {
                csvContent.push([
                    item.taskListNo,
                    item.taskName,
                    item.plant,
                    item.equipment,
                    item.machineName,
                    item.pmType,
                    item.maintenanceType,
                    item.latestEventDate,
                    item.taskPeriod,
                    item.taskLaborCost,
                    item.bomCode,
                    item.bomCost,
                    item.totalCost,
                    item.nextEventDate,
                    item.situation,
                    item.thisYear,
                    item.thisYear1later,
                    item.thisYear2later,
                    item.thisYear3later,
                    item.thisYear4later,
                    item.thisYear5later,
                    item.thisYear6later,
                    item.thisYear7later,
                    item.thisYear8later,
                    item.thisYear9later,
                    item.thisYear10later
                ]);
            });

            const csvString = csvContent.map((row) => row.join(',')).join('\n');
            const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });

            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            link.href = url;
            link.setAttribute('download', 'task_list.csv');
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
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
#TaskList {
    padding: 20px;
}

.company-code-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
    font-weight: bold;
}

.row-count-container {
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.row-count-container span {
    margin-right: 10px;
    font-weight: bold;
}

.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
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

.read-only-cell {
    background-color: #f5f5f5;
    color: black;
}
</style>
