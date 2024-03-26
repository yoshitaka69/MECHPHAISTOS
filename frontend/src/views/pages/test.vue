<template>
    <div id="CeList">
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

// register Handsontable's modules
registerAllModules();


function customRenderer(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    // 'Impact for production' 列のインデックス（0から始まる）
    const impactColIndex = 15;
    // インデックスが 'Impact for production' の列であり、値が 'High+' の場合にスタイルを設定
    if (col === impactColIndex) {
        if (value === 'High+') {
            td.style.backgroundColor = '#FF0000'; // 赤
            td.style.color = 'black';
        } else if (value === 'High') {
            td.style.backgroundColor = '#FFC000'; // オレンジ
            td.style.color = 'black';
        } else if (value === 'Low') {
            td.style.backgroundColor = '#00B050'; // 緑
            td.style.color = 'black';
        }
        // 他の条件があれば、if ステートメントを拡張してください
    }
}

function customRendererForProbability(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);

    // 'Probability of failure' 列のインデックス
    const probabilityColIndex = 16;

    // インデックスが 'Probability of failure' の列であり、値に基づいてスタイルを設定
    if (col === probabilityColIndex) {
        // セル内の文字に基づいてスタイルを変更
        switch (value) {
            case '要対策':
                td.style.backgroundColor = '#FF0000';
                td.style.color = 'black';
                break;
            case '対策検討':
                td.style.backgroundColor = '#FFC000';
                td.style.color = 'black';
                break;
            case '適切':
                td.style.backgroundColor = '#92D050';
                td.style.color = 'black';
                break;
            case '見直検討':
                td.style.backgroundColor = '#00B050';
                td.style.color = 'black';
                break;
            // 他の条件があればここに追加
        }
    }
}

function customRendererForAssessment(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);

    // セル内の文字に基づいてスタイルを変更
    switch (value) {
        case '対策済':
            td.style.backgroundColor = '#92D050'; // 条件1
            td.style.color = 'black';
            break;
        case '見直検討':
            td.style.backgroundColor = '#00B050'; // 条件2
            td.style.color = 'black';
            break;
        case '保全タスク':
            td.style.backgroundColor = '#FFFF00'; // 条件3
            td.style.color = 'black';
            break;
        // 他の条件があればここに追加
    }

    // 'Probability of failure' 列の値に基づいてスタイルを変更
    const probabilityOfFailureColIndex = 16; // 'Probability of failure' 列のインデックス
    const probabilityOfFailureValue = instance.getDataAtCell(row, probabilityOfFailureColIndex);

    // 'Impact for production' 列の値に基づいてスタイルを変更
    const impactForProductionColIndex = 15; // 'Impact for production' 列のインデックス
    const impactForProductionValue = instance.getDataAtCell(row, impactForProductionColIndex);

    // 条件の優先順位を考慮してスタイルを適用
    if (value === '対策済' || value === '見直検討' || value === '保全タスク') {
        // 条件1, 2, 3 の場合
        // 何もしない（条件1, 2, 3が優先される）
    } else if (impactForProductionValue === 'High+' || probabilityOfFailureValue === '要対策') {
        // 条件4, 5 の場合
        td.style.backgroundColor = '#FF0000'; // 条件4, 5 が優先される
        td.style.color = 'black';
    } else if (impactForProductionValue === 'High' || probabilityOfFailureValue === '対策検討') {
        // 条件6, 7 の場合
        td.style.backgroundColor = '#FFC000'; // 条件6, 7 が優先される
        td.style.color = 'black';
    }
}

function customRendererForSituation(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);
    if (value === '遅延') {
        td.style.backgroundColor = '#FFFF00'; // 黄色
        td.style.color = 'black';
    }
}

function customRendererForMttr(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments);

    const constructionPeriodColIndex = 5;  // Construction period の列のインデックス
    const partsDeliveryDateColIndex = 6;  // Parts delivery date の列のインデックス

    const constructionPeriod = instance.getDataAtCell(row, constructionPeriodColIndex);
    const partsDeliveryDate = instance.getDataAtCell(row, partsDeliveryDateColIndex);

    // Construction period と Parts delivery date の比較
    const mttrValue = Math.max(constructionPeriod, partsDeliveryDate);

    // MTTR セルに表示
    td.innerHTML = mttrValue === 0 ? '' : mttrValue;
}


const CriticalEquipmentComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [
                    ['', 'PlantA', 'モーターA', 'N401/A plant__', '4', '10', '6', '10', '4', '今年', '2022-10-02', '3', '2019-11-01', '0', '', 'High+', '', '対策済', 'A plant/変換器室 変換器盤1-3パワーサプライ交換', '10000', '3', '2025', '', 'Standard', '', '', '', '', '',],//1
                    ['','PlantA', 'モーターA', 'N401/A plant__/OX2_', '3', '10', '6', '10', '4', '', '', '4', '2018-08-10', '', '', 'High', '対策検討', '', '', '750000', '3', '', '遅延', '', '', '', '', '', '',],//2
                    ['','PlantB', 'Attach系機械設備', 'N401/A plant__/OX2_/A', '3', '10', '6', '10', '今年', '2', '2022-05-20', '0', '', '', '', '', '注意', '', 'A plant/Di槽撹拌機交換（A）', '5000', '', '', '', '', '', '', '', '', '',],//3
                    ['','PlantC', '回収温水熱交', 'N401/A plant__/OX2_/A/5E-09', '3', '10', '60', '10', '4', '', '', '', '', '', '', 'Low', '見直検討', '', '', '', '', '', '', '', '', '', '', '', '',],//4
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//5
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//6
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//7
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//8
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//9
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//11
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//12
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//13
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//14
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//15
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//16
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//17
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//18
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//19
                    ['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',],//20
                ],
                nestedHeaders: [
                    ["", "", "", "", { label: "Impact", colspan: 5 }, { label: "Probability of failure", colspan: 6 }, { label: "Critical equipment Level", colspan: 3 }, "", "", "", "", "", { label: "Spare parts", colspan: 2 }, { label: "Status of measures", colspan: 4 }, { label: "Order", colspan: 2 },],
                    ["CeListNo", "Plant", "Equipment", "Machine", "Level set <br>value", "Construction <br>period", "Parts <br>delivery date", "MTTR", "Possibility of <br>production Lv", "Count <br>of PM02", "Latest <br>PM02", "Count <br>of PM03", "Latest <br>PM03", "Count <br>of PM04", "Latest <br>PM04", "Impact for <br>production", "Probability <br>of failure", "Assessment", "Typical Task", "Labor <br>Cost(PM02)", "Period", "Next <br>event year", "situation", "BomCode", "Stock", "RCA or <br>Replace(hard)", "Spear parts or <br>Alternative(soft)", "Covered <br>from task", "Two <br>ways",],
                ],

                columns: [
                    {//CeListNo
                        type: "text",

                    },
                    {//Plant
                        type: "text",

                    },
                    {//Equipment
                        type: "text",

                    },
                    {//Machine
                        type: "text",

                    },
                    {//Level set value
                        type: 'numeric',

                    },
                    {//Construction period
                        type: 'numeric',

                    },
                    {//Parts delivery date
                        type: 'numeric',

                    },
                    {//MTTR
                        type: 'numeric',
                        renderer: customRendererForMttr,

                    },
                    {//Possibility of production Lv
                        type: 'numeric',
                        className: 'htRight',
                        readOnly: true,

                    },
                    {//Counts of PM02
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM02
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//Count of PM03
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM03
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//Count of PM04
                        width: 100,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Latest PM04
                        width: 100,
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//Impact for production
                        renderer: customRenderer,
                        width: 100,
                        className: 'htCenter',
                        readOnly: true,

                    },
                    {//Probability of failure
                        renderer: customRendererForProbability,
                        width: 100,
                        className: 'htCenter',
                        readOnly: true,

                    },
                    {//Assessment
                        renderer: customRendererForAssessment,
                        readOnly: true,
                        width: 100,
                        className: 'htCenter',

                    },
                    {//Typical Task
                        type: "text",

                    },
                    {//Typical Task Cost
                        type: 'numeric',

                    },
                    {//Period
                        type: 'numeric',

                    },
                    {//Next event year
                        className: 'htRight',
                        type: 'date',
                        dateFormat: 'YYYY-MM-DD',
                        correctFormat: false,

                    },
                    {//situation
                        className: 'htCenter',
                        renderer: customRendererForSituation,

                    },
                    {//BomCode
                        className: 'htRight',
                        type: 'dropdown',
                        source: ['Standard', 'Inventory', 'consumables']

                    },
                    {//Stock
                        type: 'dropdown',
                        source: ['有', '無'],
                        className: 'htCenter',

                    },
                    {//RCA or Replace(hard)
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Spear parts or Alternative(soft)
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Covered from task
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                    {//Two ways
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'

                    },
                ],

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

        updateData: function () {
            // JSONデータを取得
            const jsonData = this.$refs.hotTableComponent.hotInstance.getData();

            // ここでバックエンドのURLを設定
            const backendUrl = 'http://127.0.0.1:8000/api/v1/ceList/';

            // Axiosを使用してJSONデータをPOST
            axios.post(backendUrl, jsonData)
                .then(response => {
                    console.log(response.data);
                    // 成功時の処理
                })
                .catch(error => {
                    console.error(error);
                    // エラー時の処理
                });
        }



    },

    components: {
        HotTable,
    },
});

export default CriticalEquipmentComponent;
</script>