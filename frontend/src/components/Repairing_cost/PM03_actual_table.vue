<template>
    <div id="PM03actualtable">
        <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
        <p>*You cannot enter the same plant name and year more than once.</p>
        <!-- エラーメッセージを表示 -->
        <div v-if="errorMessages.length" class="error-message-container">
            <p v-for="(error, index) in errorMessages" :key="index" class="error-message">{{ error }}</p>
        </div>
        <div class="button-container">
            <input type="number" v-model="rowsToAdd" placeholder="Number of rows" class="row-input" />
            <button class="p-button-primary blue-button" @click="addRows"><i class="pi pi-plus"></i> Add Rows</button>
            <button class="p-button-primary blue-button ml-3" @click="saveData"><i class="pi pi-save"></i> Save Data</button>
            <button class="p-button-primary green-button ml-3" @click="exportCSV"><i class="pi pi-file-excel"></i> Export CSV</button>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import Save_Alert from '@/components/Alert/Save_Alert.vue';

registerAllModules();

// totalCostの計算と表示のためのカスタムレンダラー
function totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties) {
    const rowData = instance.getDataAtRow(row);
    const totalCost = Object.keys(monthColumnIndices)
        .map((month) => parseFloat(rowData[monthColumnIndices[month]]) || 0)
        .reduce((sum, amount) => sum + amount, 0);

    td.innerText = totalCost.toFixed(2); // 2桁の小数点で表示
    td.style.backgroundColor = '#f0f0f0'; // より薄い灰色
    return td;
}

const monthColumnIndices = {
    jan: 2,
    feb: 3,
    mar: 4,
    apr: 5,
    may: 6,
    jun: 7,
    jul: 8,
    aug: 9,
    sep: 10,
    oct: 11,
    nov: 12,
    dec: 13,
    commitment: 14
};

// PlantとYearの組み合わせをチェックするバリデーション関数
function plantYearValidator(hotInstance, row, col) {
    if (!hotInstance) {
        console.error('HotTable instance is not defined in validator.');
        return false;
    }

    const currentRowData = hotInstance.getDataAtRow(row);
    if (!currentRowData) {
        console.error(`No data found for row ${row}.`);
        return false;
    }

    const currentPlant = currentRowData[0]; // 'Plant' 列
    let currentYear = parseInt(currentRowData[1], 10); // 'Year' 列

    // nullや空文字の場合はバリデーションをスキップ
    if (!currentPlant || isNaN(currentYear)) {
        console.log(`Skipping validation for row ${row}: Plant or Year is null or invalid.`);
        return true; // バリデーションを通す
    }

    const tableData = hotInstance.getData();
    if (!tableData || !Array.isArray(tableData)) {
        console.error('Invalid table data:', tableData);
        return false;
    }

    console.log('Validating Plant and Year:', currentPlant, currentYear);

    let duplicateFound = false;

    // 現在の行を除外して他の行と同じPlantとYearの組み合わせを持っているか確認
    tableData.forEach((rowData, index) => {
        if (index !== row) {
            const plant = rowData[0];
            let year = parseInt(rowData[1], 10);
            if (plant === currentPlant && year === currentYear) {
                console.log(`Duplicate found at row ${index} for Plant: ${currentPlant}, Year: ${currentYear}`);
                duplicateFound = true;
            }
        }
    });

    return !duplicateFound;
}

const TableComponent = defineComponent({
    data() {
        return {
            hotInstance: null,
            hotSettings: {
                data: [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],
                colHeaders: ['Plant', 'Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'Total'],
                columns: [
                    { type: 'text' }, // 'Plant'
                    { type: 'numeric' }, // 'Year'
                    { type: 'numeric' }, // 'Jan'
                    { type: 'numeric' }, // 'Feb'
                    { type: 'numeric' }, // 'Mar'
                    { type: 'numeric' }, // 'Apr'
                    { type: 'numeric' }, // 'May'
                    { type: 'numeric' }, // 'Jun'
                    { type: 'numeric' }, // 'Jul'
                    { type: 'numeric' }, // 'Aug'
                    { type: 'numeric' }, // 'Sep'
                    { type: 'numeric' }, // 'Oct'
                    { type: 'numeric' }, // 'Nov'
                    { type: 'numeric' }, // 'Dec'
                    { type: 'numeric' }, // 'Commitment'
                    {
                        type: 'numeric',
                        readOnly: true,
                        renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties)
                    } // 'Total'
                ],
                afterGetColHeader: (col, TH) => {
                    if (col === -1) return;
                    TH.style.backgroundColor = '#FFCC99';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },
                rowHeaders: true,
                width: '100%',
                height: 'auto',
                contextMenu: true,
                autoWrapRow: true,
                autoWrapCol: true,
                fixedRowsTop: 2,
                manualColumnFreeze: true,
                manualColumnResize: true,
                manualRowResize: true,
                filters: true,
                dropdownMenu: true,
                comments: true,
                fillHandle: { autoInsertRow: true },
                licenseKey: 'non-commercial-and-evaluation',
                afterChange: null,
                afterValidate: (isValid, value, row, prop) => {
                    const cell = this.hotInstance.getCell(row, this.hotInstance.propToCol(prop));
                    console.log(`AfterValidate: row ${row}, prop ${prop}, value: ${value}, isValid: ${isValid}`);
                    cell.style.backgroundColor = isValid ? '' : '#ffcccc';
                }
            },
            rowsToAdd: 1,
            showAlert: false,
            alertType: 'success',
            alertMessage: '',
            errorMessages: []
        };
    },
    mounted() {
        this.hotInstance = this.$refs.hotTableComponent.hotInstance;
        if (!this.hotInstance) {
            console.error('HotTable instance could not be initialized.');
        } else {
            console.log('HotTable instance initialized:', this.hotInstance);

            // `afterChange` フックの設定
            this.hotInstance.addHook('afterChange', (changes, source) => {
                if (source !== 'loadData' && changes) {
                    changes.forEach(([row, prop, oldValue, newValue]) => {
                        console.log(`Change detected: row ${row}, prop ${prop}, oldValue: ${oldValue}, newValue: ${newValue}`);

                        if (prop === 'plant' || prop === 'year') {
                            const plantColIndex = this.hotInstance.propToCol('plant');
                            const yearColIndex = this.hotInstance.propToCol('year');

                            // エラーメッセージをクリア
                            this.errorMessages = [];

                            if (!plantYearValidator(this.hotInstance, row, plantColIndex)) {
                                // エラーメッセージをエラーメッセージ配列に追加
                                this.errorMessages.push(`Validation error at row ${row}: Duplicate Plant and Year combination detected.`);

                                // PlantとYearのセルの背景色を赤に設定
                                const plantCell = this.hotInstance.getCell(row, plantColIndex);
                                const yearCell = this.hotInstance.getCell(row, yearColIndex);
                                plantCell.style.backgroundColor = '#ffcccc';
                                yearCell.style.backgroundColor = '#ffcccc';

                                // アラートメッセージを設定
                                this.showAlert = true;
                                this.alertType = 'error';
                                this.alertMessage = 'Duplicate Plant name and Year exist. Please correct it.';
                            } else {
                                // バリデーションが通った場合、セルの背景色をリセット
                                const plantCell = this.hotInstance.getCell(row, plantColIndex);
                                const yearCell = this.hotInstance.getCell(row, yearColIndex);
                                plantCell.style.backgroundColor = '';
                                yearCell.style.backgroundColor = '';
                            }
                        }
                    });
                }
            });
        }
    },
    created() {
        this.getDataAxios();
    },
    methods: {
        getDataAxios() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;
            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const url = `http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/?format=json&companyCode=${userCompanyCode}`;
            console.log('Request URL:', url);

            axios
                .get(url, { headers: { 'Content-Type': 'application/json' }, withCredentials: true })
                .then((response) => {
                    const actualCostData = response.data;
                    const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'commitment'];
                    const tableData = actualCostData.flatMap((companyData) =>
                        companyData.actualPM03List.map((plantData) => {
                            const rowData = {
                                plant: plantData.plant || 'Unknown Plant',
                                year: plantData.year || 'Unknown Year'
                            };
                            months.forEach((month) => {
                                rowData[month] = parseFloat(plantData[month]) || 0;
                            });
                            return rowData;
                        })
                    );

                    const columns = [
                        { data: 'plant', type: 'text' },
                        { data: 'year' },
                        ...months.map((month) => ({ data: month })),
                        {
                            data: 'totalCost',
                            readOnly: true,
                            renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties)
                        }
                    ];

                    console.log('Table Data:', tableData);

                    const blankRows = Array.from({ length: 5 }, () => ({}));
                    const newData = tableData.concat(blankRows);

                    if (this.hotInstance) {
                        this.hotInstance.updateSettings({
                            data: newData,
                            columns
                        });
                    } else {
                        console.error('HotTable instance is not defined when updating settings.');
                    }
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },
        saveData() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const tableData = this.hotInstance.getData();
            console.log('Table Data to be posted:', tableData);

            let actualPM03List = tableData
                .filter((row) => row.some((cell) => cell !== null && cell !== ''))
                .map((row) => {
                    let year = parseInt(row[1]);
                    if (isNaN(year) || year < 2000 || year > 2100) {
                        console.warn(`Invalid year detected: ${row[1]}. Setting to 0.`);
                        year = 0;
                    }

                    return {
                        companyCode: userCompanyCode,
                        plant: row[0] || null,
                        year: year,
                        jan: (row[2] || 0).toString(),
                        feb: (row[3] || 0).toString(),
                        mar: (row[4] || 0).toString(),
                        apr: (row[5] || 0).toString(),
                        may: (row[6] || 0).toString(),
                        jun: (row[7] || 0).toString(),
                        jul: (row[8] || 0).toString(),
                        aug: (row[9] || 0).toString(),
                        sep: (row[10] || 0).toString(),
                        oct: (row[11] || 0).toString(),
                        nov: (row[12] || 0).toString(),
                        dec: (row[13] || 0).toString(),
                        commitment: (row[14] || 0).toString(),
                        totalCost: row
                            .slice(2, 15)
                            .reduce((acc, val) => acc + (parseFloat(val) || 0), 0)
                            .toFixed(2)
                    };
                });

            console.log('Post Data:', actualPM03List);

            axios
                .post('http://127.0.0.1:8000/api/repairingCost/actualPM03/', actualPM03List)
                .then((response) => {
                    console.log('Data posted successfully', response.data);
                    this.alertType = 'success';
                    this.alertMessage = 'データが正常に保存されました。';
                    this.showAlert = true;
                    setTimeout(() => {
                        this.showAlert = false;
                    }, 3000);
                })
                .catch((error) => {
                    console.error('Error in posting data', error);
                    this.alertType = 'error';
                    this.alertMessage = 'データの保存に失敗しました。エラーを確認してください。';
                    this.errorMessages = [error.response.data.detail || 'Unknown error'];
                    this.showAlert = true;
                    setTimeout(() => {
                        this.showAlert = false;
                    }, 5000);
                });
        },
        addRows() {
            const blankRows = Array.from({ length: this.rowsToAdd }, () => {
                return {
                    plant: '',
                    year: '',
                    jan: 0,
                    feb: 0,
                    mar: 0,
                    apr: 0,
                    may: 0,
                    jun: 0,
                    jul: 0,
                    aug: 0,
                    sep: 0,
                    oct: 0,
                    nov: 0,
                    dec: 0,
                    commitment: 0,
                    totalCost: 0
                };
            });

            const newData = this.hotInstance.getData().concat(blankRows);
            this.hotInstance.updateSettings({
                data: newData
            });
        },
        exportCSV() {
            const data = this.hotInstance.getData();
            const headers = this.hotInstance.getColHeader();
            const csvData = [headers, ...data].map((row) => row.join(',')).join('\n');

            const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            if (link.download !== undefined) {
                const url = URL.createObjectURL(blob);
                link.setAttribute('href', url);
                link.setAttribute('download', 'PM03_actual_data.csv');
                link.style.visibility = 'hidden';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }
        }
    },
    components: {
        HotTable,
        Save_Alert
    }
});

export default TableComponent;
</script>

<style scoped>
.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
}

.row-input {
    width: 150px;
    padding: 5px;
    margin-right: 10px;
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

.ml-3 {
    margin-left: 1rem;
}

.error-message-container {
    margin-top: 10px;
}

.error-message {
    color: red;
    font-weight: bold;
}

</style>
