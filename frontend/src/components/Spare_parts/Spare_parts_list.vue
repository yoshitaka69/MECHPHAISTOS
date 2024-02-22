<template>
    <div id="SparePartsList">
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

function customRendererForAlertOrder(instance, td, row, col, prop, value, cellProperties) {
        Handsontable.renderers.TextRenderer.apply(this, arguments);
        if (value === 'order') {
            td.style.backgroundColor = '#FF0000'; // 赤
            td.style.color = 'black';
        }
    }


const SparePartsComponent = defineComponent({
    data() {
        return {
            hotSettings: {
                data: [
                    ["", 1, "Motor", "Standard", "RX-78-5.7", "12345-98", "Change motor", 900000, 1, "pieces", "warehouse1", "8", "", "", "when we change No.1 agitator, we have to change this motor too"],//1
                    ["", 2, "Agitator", "Inventory", "ag89-78-5.7", "1233333-9", "Replace agitator", 180000, 4, "pieces", "warehouse2", "14","", "", "This agitator is bad actor,we keep this agitator every time"],//2
                    ["", 3, "Pump", "Standard", "zew99-0045", "135455333-9", "Exchange pump", 550000, 2, "pieces", "plantA", "60", "", "","This pump is needed exchange by operator"],//3
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//4
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//5
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//6
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//7
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//8
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//9
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//10
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//11
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//12
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//13
                    ["", "", "", "", "", "", "", "", "", "", "", "", ""],//14
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//15
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//16
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//17
                    ["", "", "", "", "", "", "", "", "", "", "","", "", "", ""],//18
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//19
                    ["", "", "", "", "", "", "", "", "", "", "", "", "","", ""],//20

                ],
                colHeaders: [
                    "Image", "BOM <br>No.", "Parts Name", "Category", "Model", "Serial Number", "Task Name", "Price", "Number <br>of ~", "Unit", "Location", "Delivery <br>Time", "Alert <br>order","Order <br>situation","Description"
                ],

                columns: [
                    {//Image


                    },
                    {//BOM No.
                        type: "numeric",

                    },
                    {//PartsName
                        type: "text",
                        className: 'htCenter',

                    },
                    {//Category
                        className: 'htRight',
                        type: 'dropdown',
                        source: ['Standard', 'Inventory', 'consumables']

                    },
                    {//Model
                        type: 'text',

                    },
                    {//SerialNumber
                        type: 'text',
                        className: 'htRight',

                    },
                    {//TaskName
                        type: 'text',
                        className: 'htCenter',

                    },
                    {//PartsCost
                        type: 'numeric',
                        className: 'htRight',

                    },
                    {//Number of ~
                        width: 60,
                        className: 'htRight',
                        type: 'numeric',

                    },
                    {//Unit
                        width: 60,
                        type: 'numeric',
                        className: 'htRight',

                    },
                    {//Location
                        className: 'htRight',
                        type: 'text',
                        className: 'htRight',

                    },
                    {//Delivery Parts time
                        width: 60,
                        className: 'htRight',
                        type: 'numeric',
                    },
                    {//Alert order
                        width: 100,
                        className: 'htCenter',
                        type: "text",
                        renderer: customRendererForAlertOrder
                    },
                    {//Order situation
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'
                    },
                    {//Description
                        className: 'htCenter',
                        type: 'text',
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
        swapHotData: function () {
            //load new data
            // The Handsontable instance is stored under the `hotInstance` property of the wrapper component.
            this.$refs.hotTableComponent.hotInstance.loadData([['new', 'data']]);
        },

        updateData: function () {
            // JSONデータを取得
            const jsonData = this.$refs.hotTableComponent.hotInstance.getData();

            // ここでバックエンドのURLを設定
            const backendUrl = 'http://localhost:3000/Celist2';

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

export default SparePartsComponent;
</script>