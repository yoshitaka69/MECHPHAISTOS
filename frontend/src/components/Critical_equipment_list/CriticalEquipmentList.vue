<template>
    <div id="CeList">
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
        <hot-table ref="hotTableComponent" :settings="hotSettings" :data="dataStore"></hot-table><br />
        <div class="button-container">
            <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
            <Button label="Add Rows" icon="pi pi-plus" class="p-button-primary blue-button" @click="addRows" />
            <Button label="Save" icon="pi pi-save" class="p-button-primary blue-button ml-3" @click="saveData" />
            <Button label="Refresh" icon="pi pi-refresh" class="p-button-primary blue-button ml-3" @click="refreshData" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Handsontable from 'handsontable';
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import { useUserStore } from '@/stores/userStore';
import Button from 'primevue/button';
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // 新しいアラートコンポーネントをインポート

// register Handsontable's modules
registerAllModules();

function applyBaseStyle(td) {
    if (td && td.style) {
        td.style.backgroundColor = '#F0F0F0'; // 灰色
        td.style.color = 'black';
    }
}

// カスタムレンダラー関数
function customRenderer(instance, td, row, col, prop, value, cellProperties) {
    console.log(`customRenderer - Row: ${row}, Col: ${col}, Value: ${value}`);
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
    const impactColIndex = 15;
    if (col === impactColIndex) {
        if (value === 'High+') {
            td.style.backgroundColor = '#FF0000';
        } else if (value === 'High') {
            td.style.backgroundColor = '#FFC000';
        } else if (value === 'Middle') {
            td.style.backgroundColor = '#f9d909';
        } else if (value === 'Low') {
            td.style.backgroundColor = '#00B050';
        }
    }
}

function customRendererForProbability(instance, td, row, col, prop, value, cellProperties) {
    console.log(`customRendererForProbability - Row: ${row}, Col: ${col}, Value: ${value}`);
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
    const probabilityColIndex = 16;
    if (col === probabilityColIndex) {
        switch (value) {
            case 'Caution':
                td.style.backgroundColor = '#f9d909';
                break;
            case 'Measures':
                td.style.backgroundColor = '#f99d09';
                break;
            case 'Danger':
                td.style.backgroundColor = '#f90909';
                break;
            case 'Review':
                td.style.backgroundColor = '#4c7c04';
                break;
            case 'Appropriate':
                td.style.backgroundColor = '#a0d070';
                break;
        }
    }
}

function customRendererForReadOnlyCells(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);
}

function customRendererForCeListNo(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);

    td.style.cursor = 'pointer'; // ポインタに変更してクリック可能に見せる
    td.style.color = 'blue'; // テキスト色を青に設定
    td.style.textDecoration = 'underline'; // テキストに下線を付ける

    // クリックイベントを追加
    td.addEventListener('click', () => {
        if (value) {
            window.open(`/celist_detail/${value}`, '_blank'); // 新しいタブで詳細ページを開く
        }
    });
}

//-------------------------------------------------------------------------
//以下の関数はAssessment列、NextEventYear列、Situation列、MTTR列のためのカスタムレンダラー関数です。
//-------------------------------------------------------------------------

function customRendererForAssessment(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);

    const rcaOrReplaceColIndex = 25; // 'RCA or <br>Replace(hard)'列のインデックス
    const rcaOrReplaceValue = instance.getDataAtCell(row, rcaOrReplaceColIndex);

    const probabilityOfFailureColIndex = 16; // 'Probability <br>of failure'列のインデックス
    const probabilityOfFailureValue = instance.getDataAtCell(row, probabilityOfFailureColIndex);

    const coveredFromTaskColIndex = 27; // 'Covered <br>from task'列のインデックス
    const coveredFromTaskValue = instance.getDataAtCell(row, coveredFromTaskColIndex);

    // 'Review'かつ'PM Task'の両方の条件が満たされる場合を最優先で処理
    if (coveredFromTaskValue === true && probabilityOfFailureValue === 'Review') {
        td.style.backgroundColor = '#4c7c04'; // 特定の濃い緑色
        td.innerText = 'Review'; // セルに"Review"を表示
    } else if (coveredFromTaskValue === true) {
        // 'PM Task'にチェックが入っていた場合、このセルに'PM Task'を表示
        value = 'PM Task';
        td.innerText = 'PM Task';
        td.style.backgroundColor = '#FFFF00'; // 黄色
    } else if (rcaOrReplaceValue === true) {
        // 'RCA or <br>Replace(hard)'にチェックが入っていた場合、このセルに'Dealt'を表示
        value = 'Dealt';
        td.innerText = 'Dealt';
        td.style.backgroundColor = '#92D050'; // 緑色
    } else {
        const impactForProductionColIndex = 15;
        const impactForProductionValue = instance.getDataAtCell(row, impactForProductionColIndex);

        if (impactForProductionValue === 'High+' || probabilityOfFailureValue === 'Danger') {
            td.style.backgroundColor = '#FF0000'; // 赤色
            td.innerText = 'High+'; // セルに"High+"を表示
        } else if (impactForProductionValue === 'High' || probabilityOfFailureValue === 'Measures') {
            td.style.backgroundColor = '#FFC000'; // オレンジ色
            td.innerText = 'High'; // セルに"High"を表示
        } else if (probabilityOfFailureValue === 'Review') {
            td.style.backgroundColor = '#00B050'; // 濃い緑色
            td.innerText = 'Review'; // セルに"Review"を表示
        }
    }
}




//-------------------------------------------------------------------------


function customRendererForNextEventYear(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);

    const latestPM02ColIndex = 10; // LatestPM02列のインデックス
    const periodColIndex = 20; // Period列のインデックス

    const latestPM02Value = instance.getDataAtCell(row, latestPM02ColIndex);
    const periodValue = instance.getDataAtCell(row, periodColIndex);

    if (latestPM02Value && periodValue) {
        const latestPM02Date = new Date(latestPM02Value);
        const nextEventDate = new Date(latestPM02Date);
        nextEventDate.setDate(latestPM02Date.getDate() + parseInt(periodValue));

        const formattedDate = nextEventDate.toISOString().split('T')[0];
        td.innerText = formattedDate;

        // セルのメタデータとして次のイベント日付を保存
        cellProperties.nextEventDate = nextEventDate;
    }
}

function customRendererForSituation(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    applyBaseStyle(td);

    const currentDate = new Date();

    // nextEventDate を customRendererForNextEventYear から取得
    const nextEventYearColIndex = 21; // NextEventYear列のインデックス
    const nextEventCellMeta = instance.getCellMeta(row, nextEventYearColIndex);
    const nextEventDate = nextEventCellMeta.nextEventDate;

    if (nextEventDate && currentDate > nextEventDate) {
        td.style.backgroundColor = '#FFFF00';
        td.innerText = 'Delay';
    } else if (value === 'Delay') {
        td.style.backgroundColor = '#FFFF00';
    }
}

function customRendererForMttr(instance, td, row, col, prop, value, cellProperties) {
    if (td) {
        Handsontable.renderers.TextRenderer.apply(this, arguments);
        applyBaseStyle(td);
    }

    const constructionPeriodColIndex = 5;
    const partsDeliveryDateColIndex = 6;
    const constructionPeriod = instance.getDataAtCell(row, constructionPeriodColIndex);
    const partsDeliveryDate = instance.getDataAtCell(row, partsDeliveryDateColIndex);
    const mttrValue = Math.max(constructionPeriod, partsDeliveryDate);

    if (td) {
        // nullチェックを追加
        td.innerHTML = mttrValue === 0 ? '' : mttrValue;
    }

    return mttrValue; // MTTR値を返す
}

const CriticalEquipmentList = defineComponent({
    props: {
        riskTexts: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            hotSettings: {
                data: [], // 初期データを空に設定
                nestedHeaders: [
                    [
                        '',
                        '',
                        '',
                        '',
                        { label: 'Impact', colspan: 5 },
                        { label: 'Probability of failure', colspan: 6 },
                        { label: 'Critical equipment Level', colspan: 3 },
                        '',
                        '',
                        '',
                        '',
                        '',
                        { label: 'Spare parts', colspan: 2 },
                        { label: 'Status of measures', colspan: 4 },
                        { label: 'Order', colspan: 2 }
                    ],
                    [
                        'CeListNo',
                        'Plant',
                        'Equipment',
                        'Machine',
                        'Level set <br>value',
                        'Construction <br>period',
                        'Parts <br>delivery date',
                        'MTTR',
                        'PossibilityOf<br>ContinuousProduction',
                        'Count <br>of PM02',
                        'Latest <br>PM02',
                        'Count <br>of PM03',
                        'Latest <br>PM03',
                        'Count <br>of PM04',
                        'Latest <br>PM04',
                        'Impact for <br>production',
                        'Probability <br>of failure',
                        'Assessment',
                        'Typical Task',
                        'Labor <br>Cost(PM02)',
                        'Period',
                        'Next <br>event date',
                        'situation',
                        'BomCode',
                        'Stock',
                        'RCA or <br>Replace(hard)',
                        'Spear parts or <br>Alternative(soft)',
                        'Covered <br>from task',
                        'Two <br>ways'
                    ]
                ],

                columns: [
                    {
                        data: 'ceListNo',
                        type: 'text',
                        readOnly: true,
                        renderer: customRendererForCeListNo
                    },
                    { data: 'plant', type: 'text' },
                    { data: 'equipment', type: 'text' },
                    { data: 'machineName', type: 'text' },
                    {
                        data: 'levelSetValue',
                        type: 'dropdown',
                        source: ['Low', 'Middle', 'High']
                    },
                    { data: 'typicalConstPeriod', type: 'numeric' },
                    {
                        data: 'maxPartsDeliveryTimeInBom',
                        type: 'numeric',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    { data: 'mttr', type: 'numeric', renderer: customRendererForMttr },
                    {
                        data: 'possibilityOfContinuousProduction',
                        type: 'dropdown',
                        source: [1, 2, 3, 4, 5],
                        className: 'htRight',
                        readOnly: false
                    },
                    {
                        data: 'countOfPM02',
                        width: 100,
                        className: 'htRight',
                        type: 'numeric'
                    },
                    {
                        data: 'latestPM02',
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false
                    },
                    {
                        data: 'countOfPM03',
                        width: 100,
                        className: 'htRight',
                        type: 'numeric'
                    },
                    {
                        data: 'latestPM03',
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false
                    },
                    {
                        data: 'countOfPM04',
                        width: 100,
                        className: 'htRight',
                        type: 'numeric'
                    },
                    {
                        data: 'latestPM04',
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false
                    },
                    {
                        data: 'impactForProduction',
                        renderer: customRenderer,
                        width: 100,
                        className: 'htCenter',
                        readOnly: true
                    },
                    {
                        data: 'probabilityOfFailure',
                        renderer: customRendererForProbability,
                        width: 100,
                        className: 'htCenter',
                        readOnly: false
                    },
                    {
                        data: 'assessment',
                        renderer: customRendererForAssessment,
                        readOnly: true,
                        width: 100,
                        className: 'htCenter'
                    },
                    {
                        data: 'typicalTaskName',
                        type: 'text',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    {
                        data: 'typicalTaskCost',
                        type: 'numeric',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    {
                        data: 'typicalConstPeriod',
                        type: 'numeric',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    {
                        data: 'typicalNextEventDate',
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,
                        readOnly: true,
                        renderer: customRendererForNextEventYear
                    },
                    {
                        data: 'typicalSituation',
                        className: 'htCenter',
                        renderer: customRendererForSituation,
                        readOnly: true
                    },
                    {
                        data: 'bomCode',
                        className: 'htRight',
                        type: 'text',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    {
                        data: 'bomStock',
                        type: 'dropdown',
                        source: ['有', '無'],
                        className: 'htCenter',
                        readOnly: true,
                        renderer: customRendererForReadOnlyCells
                    },
                    { data: 'rcaOrReplace', width: 100, className: 'htCenter', type: 'checkbox' },
                    {
                        data: 'sparePartsOrAlternative',
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'
                    },
                    { data: 'coveredFromTask', width: 100, className: 'htCenter', type: 'checkbox' },
                    { data: 'twoways', width: 100, className: 'htCenter', type: 'checkbox' }
                ],
                rowHeaders: true, // 行ヘッダーを有効化

                afterGetColHeader: (col, TH) => {
                    if (col === -1) {
                        return;
                    }
                    TH.style.backgroundColor = '#FFCC99';
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';
                },

                width: '100%',
                height: 'auto',
                stretchH: 'all',
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
                    if (source !== 'loadData' && changes) {
                        changes.forEach(([row, prop, oldValue, newValue]) => {
                            const relevantColumns = ['levelSetValue', 'mttr', 'possibilityOfContinuousProduction', 'countOfPM02', 'countOfPM03', 'countOfPM04'];
                            if (relevantColumns.includes(prop)) {
                                this.emitData();
                            }
                        });
                    }
                }
            },
            rowsToAdd: 1, // 追加する行数のデフォルト値
            dataStore: [], // フルデータストア
            showAlert: false, // アラート表示用のフラグ
            alertType: 'success', // 'success' か 'error' を指定
            alertMessage: 'データが正常に保存されました。',
            errorMessages: [] // エラーメッセージのリスト
        };
    },

    created() {
        this.getDataAxios();
    },

    methods: {
            // MTTR値を計算するメソッド
    getMttrValue(hotInstance, row) {
        const constructionPeriodColIndex = 5;
        const partsDeliveryDateColIndex = 6;
        const constructionPeriod = hotInstance.getDataAtCell(row, constructionPeriodColIndex);
        const partsDeliveryDate = hotInstance.getDataAtCell(row, partsDeliveryDateColIndex);
        return Math.max(constructionPeriod, partsDeliveryDate);
    },
        // Handsontableの初期化
        initHandsontable() {
            const container = this.$el;
            this.hot = new Handsontable(container, {
                afterChange: (changes, source) => {
                    if (source !== 'loadData') {
                        const data = this.hot.getData();
                        this.emitData();
                    }
                }
            });
        },

        // Axiosを使用してデータを取得
        getDataAxios() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${userCompanyCode}`;

            axios
                .get(url, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                .then((response) => {
                    const masterDataTable = response.data;
                    this.dataStore = masterDataTable;
                    this.$refs.hotTableComponent.hotInstance.loadData(this.dataStore); // データを Handsontable にロード
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },

        addRows() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const blankRows = Array.from({ length: this.rowsToAdd }, () => {
                return {
                    ceListNo: '',
                    plant: '',
                    equipment: '',
                    machineName: '',
                    levelSetValue: '',
                    typicalConstPeriod: 0,
                    maxPartsDeliveryTimeInBom: 0,
                    mttr: 0,
                    possibilityOfContinuousProduction: '',
                    countOfPM02: 0,
                    latestPM02: '',
                    countOfPM03: 0,
                    latestPM03: '',
                    countOfPM04: 0,
                    latestPM04: '',
                    impactForProduction: '',
                    probabilityOfFailure: '',
                    assessment: '',
                    typicalTaskName: '',
                    typicalTaskCost: 0,
                    typicalNextEventDate: '',
                    typicalSituation: '',
                    bomCode: '',
                    bomStock: '',
                    rcaOrReplace: false,
                    sparePartsOrAlternative: false,
                    coveredFromTask: false,
                    twoways: false
                };
            });

            this.dataStore = this.dataStore.concat(blankRows);

            hotInstance.loadData(this.dataStore); // Handsontable に現在のページデータをロード
        },

        saveData() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const dataToSave = hotInstance.getData();

            // Handsontableから取得したデータを適切な形式に変換し、companyCodeを追加
            const formattedData = dataToSave.map((row) => {
                return {
                    companyCode: userCompanyCode, // companyCodeを追加
                    ceListNo: row[0], // ceListNo
                    plant: row[1], // Plant
                    equipment: row[2], // Equipment
                    machineName: row[3], // Machine Name
                    levelSetValue: row[4], // Level set value
                    typicalConstPeriod: row[5], // Construction period
                    maxPartsDeliveryTimeInBom: row[6], // Parts delivery date
                    mttr: row[7], // MTTR
                    possibilityOfContinuousProduction: row[8], // Possibility of Continuous Production
                    countOfPM02: row[9], // Count of PM02
                    latestPM02: row[10], // Latest PM02
                    countOfPM03: row[11], // Count of PM03
                    latestPM03: row[12], // Latest PM03
                    countOfPM04: row[13], // Count of PM04
                    latestPM04: row[14], // Latest PM04
                    impactForProduction: row[15], // Impact for Production
                    probabilityOfFailure: row[16], // Probability of Failure
                    assessment: row[17], // Assessment
                    typicalTaskName: row[18], // Typical Task Name
                    typicalTaskCost: row[19], // Typical Task Cost
                    period: row[20], // Period (最新のイベント日を計算する期間)
                    typicalNextEventDate: row[21], // 次のイベント日付
                    situation: row[22], // Situation
                    bomCode: row[23], // BOMコード
                    bomStock: row[24], // BOMストック
                    rcaOrReplace: row[25], // RCAまたはハード交換
                    sparePartsOrAlternative: row[26], // スペアパーツまたはソフト代替
                    coveredFromTask: row[27], // タスクによりカバー
                    twoways: row[28], // 2つの方法
                    ceDescription: row[29] // CE説明
                };
            });

            // POSTリクエストを送信
            const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTable/`;

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
                    }, 3000); // 3秒後にアラートを非表示にする
                })
                .catch((error) => {
                    console.error('Error saving data:', error);
                    if (error.response) {
                        console.error('Error response data:', error.response.data);
                    }
                    this.alertType = 'error';
                    this.alertMessage = 'データの保存に失敗しました。エラーを確認してください。';
                    this.errorMessages = ['入力内容を確認してください。', 'もう一度お試しください。'];
                    this.showAlert = true;
                    setTimeout(() => {
                        this.showAlert = false;
                    }, 5000); // 5秒後にアラートを非表示にする
                });
        },

        emitData() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const rows = hotInstance.countRows();
            const emittedData = [];

            for (let row = 0; row < rows; row++) {
                const levelSetValue = hotInstance.getDataAtCell(row, 4);
                const mttr = this.getMttrValue(hotInstance, row);
                const possibilityOfContinuousProduction = hotInstance.getDataAtCell(row, 8);
                const countOfPM02 = hotInstance.getDataAtCell(row, 9);
                const countOfPM03 = hotInstance.getDataAtCell(row, 11);
                const countOfPM04 = hotInstance.getDataAtCell(row, 13);

                emittedData.push({
                    levelSetValue,
                    mttr,
                    possibilityOfContinuousProduction,
                    countOfPM02,
                    countOfPM03,
                    countOfPM04
                });
            }

            console.log('Emitting Data:', emittedData);
            this.$emit('data-emitted', emittedData);
        },

        // Impact for Productionの更新
        updateImpactForProduction({ index, impactForProduction }) {
            console.log(`Updating impactForProduction at row ${index} with value ${impactForProduction}`);
            this.$refs.hotTableComponent.hotInstance.setDataAtCell(index, 15, impactForProduction);
        },

        // Probability of Failureの更新
        updateProbabilityOfFailure({ index, probabilityOfFailure }) {
            console.log(`Updating probabilityOfFailure at row ${index} with value ${probabilityOfFailure}`);

            if (typeof index === 'number' && index >= 0) {
                // indexが正の整数であることを確認
                this.$refs.hotTableComponent.hotInstance.setDataAtCell(index, 16, probabilityOfFailure);
            } else {
                console.error('Invalid index value:', index);
            }
        },

        openDetailPage(ceListNo) {
            // 詳細ページを新しいタブで開く
            window.open(`/#/ce-list-detail/${ceListNo}`, '_blank');
        },

        refreshData() {
            console.log('Refreshing data...');
            this.$emit('refresh-requested');
        }
    },

    components: {
        HotTable,
        Button,
        Save_Alert
    }
});

export default CriticalEquipmentList;
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
