<template>
  <div id="TaskList">
    <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table><br />
    <button v-on:click="swapHotData" class="controls">Load new data</button>
  </div>
</template>
  
  
<script>
import Handsontable from 'handsontable';
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import axios from "axios";

// register Handsontable's modules
registerAllModules();



const URL = "http://localhost:3000/CeList";

const TaskListComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['PlantA', 'モーターA', 'N401/A plant__', '2018-10-20', '2021-08-09', '', 'change motor', '34000', 'motor', '58090', '5', '', '', '', ''],
        ],
        colHeaders: this.generateColHeaders(), // ヘッダーを生成するメソッドを使用

        columns: [
          {//plant
            type: "text",

          },
          {//Equipment
            type: "text",

          },
          {//Function
            type: "text",

          },
          {//Latest PM02
            type: 'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,
            readOnly: true,

          },
          {//LatestPM03
            type: 'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,
            readOnly: true,

          },
          {//LatestPM04
            type: 'date',
            dateFormat: 'YYYY-MM-DD',
            correctFormat: false,
            readOnly: true,
          },
          {//Task name
            type: 'text',

          },
          {//Labor cost
            type: 'numeric',

          },
          {//Parts
            type: 'text',

          },
          {//Parts Cost
            type: 'numeric',

          },
          {//Period of task(MTTR)
            type: 'numeric',

          },
          {//Next event date
            type: 'numeric',
            readOnly: true,
            renderer: this.customRendererForNextEventDate,


          },
          {//Situation
            type: 'text',

          },
          {//現時点からの10年先まで繰り返し（今）
            type: 'checkbox',
            className: 'htCenter' 

          },
          {//現時点からの10年先まで繰り返し（1年後）
            type: 'checkbox',
            className: 'htCenter'
          

          },
          {//現時点からの10年先まで繰り返し（2年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（3年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（4年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（5年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（6年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（7年後）
            type: 'checkbox',
            className: 'htCenter'

          },
          {//現時点からの10年先まで繰り返し（8年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（9年後）
            type: 'checkbox',
            className: 'htCenter'


          },
          {//現時点からの10年先まで繰り返し（10年後）
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
    getDataAxios() {
      axios
        .get(URL, {
          method: "GET",
          mode: "no-cors",
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
          },
          withCredentials: true,
          credentials: "same-origin"
        })
        .then(response => {
          const data = response.data
          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
            columns: [{ data: "plant" }, { data: "equipment" },{data:"function"},{data:"latestPM02"},{data:"latestPM03"}, { data: "latestPM04" },{data:"taskOfPM02"},{data:"costOfPM02"},{data:"parts"}, { data: "" }, { data: "" }, { data: "" },{ data: "" },{ data: "" }, { data: "" }, { data: "" },{ data: "" },{ data: "" },{ data: "" },{ data: "" }, { data: "" }, { data: "" },{ data: "" },]
          });
        })
        .catch(error => console.log("error"));
    },

    swapHotData: function () {
      //load new data
      // The Handsontable instance is stored under the `hotInstance` property of the wrapper component.
      this.$refs.hotTableComponent.hotInstance.loadData([['new', 'data']]);
    },
    // 年数を生成するメソッド
    generateColHeaders() {
      const currentYear = new Date().getFullYear(); // 現在の年を取得
      // 現在の年から10年後までの年数を生成して文字列に変換
      const futureYears = Array.from({ length: 11 }, (_, index) => (currentYear + index).toString());

      // colHeadersに年数を追加
      return [
        'Plant', 'Equipment', 'Function', 'Latest<br>PM02', 'Latest<br>PM03', 'Latest<br>PM04', 'Task Name',
        'Labor<br>Cost', 'Parts', 'Parts cost', 'Period', 'Next Even<br>date', 'Situation', ...futureYears
      ];
    },

    // Custom renderer for Next event date column
    customRendererForNextEventDate(instance, td, row, col, prop, value, cellProperties) {
      Handsontable.renderers.TextRenderer.apply(this, arguments);
      const latestPM02 = instance.getDataAtCell(row, 3); // Assuming the index of Latest PM02 is 3
      const latestPM03 = instance.getDataAtCell(row, 4); // Assuming the index of Latest PM03 is 4
      const latestPM04 = instance.getDataAtCell(row, 5); // Assuming the index of Latest PM04 is 5
      const period = instance.getDataAtCell(row, 10); // Assuming the index of 'Period' is 10

      const latestDate = this.getLatestDate([latestPM02, latestPM03, latestPM04]);
      const nextEventDate = this.calculateNextEventDate(latestDate, period);

      // Set the calculated date to the cell
      td.innerHTML = nextEventDate;
    },

    getLatestDate(dates) {
      const validDates = dates.filter(date => date); // Filter out invalid dates
      return validDates.length > 0 ? new Date(Math.max.apply(null, validDates.map(date => new Date(date).getTime()))) : null;
    },

    calculateNextEventDate(latestDate, period) {
      if (!latestDate) return ''; // Return empty string if latestDate is null

      const nextEventDate = new Date(latestDate);
      nextEventDate.setFullYear(nextEventDate.getFullYear() + parseInt(period, 10));
      return nextEventDate.getFullYear().toString();
    },
  },

  components: {
    HotTable,
  },
});

export default TaskListComponent;

</script>