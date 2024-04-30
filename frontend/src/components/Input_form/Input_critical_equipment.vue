<template>
    <div id="Input_CeList">
        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
        <button v-on:click="updateData" class="controls">Update Data</button>
    </div>
</template>


<script>
import axios from 'axios';
import Handsontable from 'handsontable';
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

// register Handsontable's modules
registerAllModules();


const CriticalEquipmentComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//1
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//2
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//3
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//4
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//5
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//6
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//7
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//8
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//9
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//11
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//12
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//13
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//14
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//15
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//16
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//17
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//18
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//19
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//20
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//21
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//22
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//23
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//24
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//25
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//26
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//27
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//28
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//29
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//30
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//31
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//32
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//33
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//34
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//35
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//36
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//37
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//38
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//39
                    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//40
                ],
                nestedHeaders: [
                    ["", "", "", { label: "Impact", colspan: 3 }, { label: "Probability of failure", colspan: 6 }, { label: "Critical equipment Level", colspan: 3 },{ label: "Status of measures", colspan: 4 }, ],
                    ["Plant", "Equipment", "Machine", "Level set <br>value", "Construction <br>period", "Parts <br>delivery date", "Count <br>of PM02", "Latest <br>PM02", "Count <br>of PM03", "Latest <br>PM03", "Count <br>of PM04", "Latest <br>PM04", "Impact for <br>production", "Probability <br>of failure", "Assessment",  "RCA or <br>Replace(hard)", "Spear parts or <br>Alternative(soft)", "Covered <br>from task", "Two <br>ways",],
                ],

                columns: [
                    {//Plant 1番
                        data: "plant",
                        type: "text",

                    },
                    {//Equipment　2番
                        data: "equipment",
                        type: "text",

                    },
                    {//Machine　3番
                        data: "machineName",
                        type: "text",

                    },
                    {//Level set value　4番
                        data: "levelSetValue",
                        type: 'numeric',

                    },
                    {//Construction period　5番
                        data: "typicalConstPeriod",
                        type: 'numeric',

                    },
                    {//Parts delivery date　6番
                        data: "maxPartsDeliveryTimeInBom",
                        type: 'numeric',

                    },
                    {//Counts of PM02　7番
                        data: "countOfPM02",
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM02　8番
                        data: "latestPM02",
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//Count of PM03　9番
                        data: "countOfPM03",
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM03　10番
                        data: "latestPM03",
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//Count of PM04　11番
                        data: "countOfPM04",
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM04　12番
                        data: "latestPM04",
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,
                    },
                    {//Impact for production　13番
                        data: "impactForProduction",
                        width: 100,
                        className: 'htCenter',
                        readOnly: true,
                       

                    },
                    {//Probability of failure　14番
                        data: "probabilityOfFailure",
                        width: 100,
                        className: 'htCenter',
                        readOnly: true,

                    },
                    {//Assessment　15番
                        data: "assessment",
                        readOnly: true,
                        width: 100,
                        className: 'htCenter',

                    },
                    {//RCA or Replace(hard)　16番
                        data: "rcaOrReplace",
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Spear parts or Alternative(soft)　17番
                        data: "sparePartsOrAlternative",
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Covered from task　18番
                        data: "coveredFromTask",
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Two ways　19番
                        data: "twoways",
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                ],

                afterGetColHeader: (col, TH) => {
                    if (col === -1) {  // ヘッダー行の場合
                        return;
                    }
                    // 特定の列インデックスまたはすべてのヘッダーに適用したい場合
                    TH.style.backgroundColor = '#FFCC99'; // 薄いオレンジ色
                    TH.style.color = 'black';
                    TH.style.fontWeight = 'bold';  // テキストを太字に設定
                },
                
                cells: function(row, col, prop) {
                    var cellProperties = {};
                    var myData = this.instance.getDataAtCol(col);
                    if (this.instance.getSettings().columns[col].readOnly) {
                        cellProperties.renderer = function(instance, td, row, col, prop, value, cellProperties) {
                            Handsontable.renderers.TextRenderer.apply(this, arguments);
                            td.style.background = '#f0f0f0'; // Light gray color
                        };
                    }
                    return cellProperties;
                },

                width: '100%',
                height: 'auto',
                stretchH: 'all', // 'none' is default 様子見
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


    methods: {

        updateData(data) {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;
            const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${userCompanyCode}`;
            const payload = { companyCode: userCompanyCode, masterDataTable: data };

            axios.post(url, payload)
                .then(response => console.log('Data successfully updated:', response))
                .catch(error => console.error('Error updating data:', error));
        },

        sendData() {
            const data = this.$refs.hotTableComponent.hotInstance.getSourceData();
            this.updateData(data);
        }

    },



    components: {
        HotTable,
    },
});

export default CriticalEquipmentComponent;
</script>
