<template>

<div id="example1">
  <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br/>
  <button v-on:click="swapHotData" class="controls">Load new data</button>
</div>

</template>


<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';

// register Handsontable's modules
registerAllModules();

const ExampleComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['PlantA','モーターA', 'N401/A plant__', '4','10','6','10','4','今年','2022-10-02','3','2019-11-01','0','','High+','','対策済','A plant/変換器室 変換器盤1-3パワーサプライ交換','10000','3年','2025','','A parts','0','','','','','',''],
          ['PlantA', 'モーターA', 'N401/A plant__/OX2_', '3','10','6','10','4','','','4','2018-08-10','','','High','対策検討','','','750000','3','','遅延','','2','','','','','order',''],
          ['PlantB', 'Attach系機械設備', 'N401/A plant__/OX2_/A', '3','10','6','10','今年','2','2022-05-20','0','L3','M3','N3','High','注意','','A plant/Di槽撹拌機交換（A）','5000','','','','','','','','','','order',''],
          ['PlantC', 'B4', 'C4', 'D4','E4','F4','G4','H4','I4','J4','K4','L4','M4','N4','O4','P4','Q4','R4','S4','T4','U4','V4','W4','X4','','','','','',''],
        ],
        nestedHeaders: [
          ["","","",{label:"Impact", colspan:5},{label:"Probability of failure", colspan:6},{label:"Critical equipment Level", colspan:3},"","","","","",{label:"Spare parts", colspan:2},{label:"Status of measures", colspan:4},{label:"Order", colspan:2},],
          ["Plant","Equipment","Function","Level set value","Construction period", "Parts delivery date","MTTR","Possibility of production","Count of PM02","Latest PM02","Count of PM03","Latest PM03","Count of PM04","Latest PM04","Impact for production","Probability of failure","Assessment","Task of PM02","Cost(PM02)","Period","Next event year","situation","Category","Stock","RCA or Replace(hard)","Spear parts or Alternative(soft)","Covered from task","Two ways","Alert order","Order situation"],
        ],

        columns:[
          {//Plant
            type:"text",

          },
          {//Equipment
            type:"text",

          },
          {//Function
            type:"text",

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

          },
          {//Possibility of production
            type: 'numeric',
            readOnly:true,

          },
          {//Counts of PM02
            type: 'numeric',

          },
          {//Latest PM02
            type:'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,

          },
          {//Count of PM03
            type: 'numeric',

          },
          {//Latest PM03
            type:'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,

          },
          {//Count of PM04
            type: 'numeric',

          },
          {//Latest PM04
            type:'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,

          },
          {//Impact for production
            readOnly:true,

          },
          {//Probability of failure
            readOnly:true,

          },
          {//Assessment
            readOnly:true,

          },
          {//Task of PM02
            type:"text",

          },
          {//Cost(PM02)
            type: 'numeric',

          },
          {//Period
            type: 'numeric',

          },
          {//Next event year
            type:'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,

          },
          {//situation

          },
          {//Category
            type: 'dropdown',
            source: ['A parts','B parts', 'C parts']

          },
          {//Stock

          },
          {//RCA or Replace(hard)
            type: 'checkbox'

          },
          {//Spear parts or Alternative(soft)
            type: 'checkbox'

          },
          {//Covered from task
            type: 'checkbox'

          },
          {//Two ways
            type: 'checkbox'

          },
          {//Alert order
            type:"text",

          },
          {//Order situation
            type: 'checkbox'
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
  methods: {
    swapHotData: function() {
      //load new data
      // The Handsontable instance is stored under the `hotInstance` property of the wrapper component.
      this.$refs.hotTableComponent.hotInstance.loadData([['new', 'data']]);
    }
  },

  components: {
    HotTable,
  }
});

export default ExampleComponent;

</script>