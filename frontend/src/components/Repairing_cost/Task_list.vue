<template>
  <div id="example1">
    <h2>PM02 Task List</h2>
    <HotTable ref="hotTableComponent" :settings="hotSettings"></HotTable>
  </div>
</template>


<script>
import { HotTable } from "@handsontable/vue3";
import axios from "axios";
import 'handsontable/dist/handsontable.full.css';


const URL = "http://localhost:3000/CeList";


export default {
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
          const Id = data.id;
          const TaskName = data.taskOfPM02;
          const Plant = data.plant;
          const Equipment = data.equipment;
          const Cost = data.costOfPM02;
          const Parts = data.parts;
          const PeriodOfTask = data.mttr;
          const NextEventYear = data.nextEventYear;
          const Situation = data.situation;
          const Note = data.note;

          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
            columns: [{ data: "id" }, { data: "taskOfPM02" },{data:"plant"},{data:"equipment"},{data:"costOfPM02"}, { data: "parts" },{data:"mttr"},{data:"nextEventYear"},{data:"situation"}, { data: "note" }]
          });
        })
        .catch(error => console.log("error"));
    }
  },

  data: () => ({
    data: null,
    hotSettings: {
      data: null,
      colHeaders: [
        "Id",//1
        "Task name",//2
        "Plant",//3
        "Equipment",//4
        "Cost",//5
        "Parts",//6
        "Period of Task (MTTR)",//7
        "Next Event date",//8
        "Situation",//9
        "Note",//10
      ],

      columns: [
        { type: "text" },//1
        { type: "text" },//2
        { type: "text" },//3
        { type: "text" },//4
        { type: "text" },//5
        { type: "text" },//6
        { type: "text" },//7
        { type: "text" },//8
        { type: "text" },//9
        { type: "text" },//10
      ],
      rowHeaders: true,
      manualRowMove: true,
      contextMenu: true,
      manualColumnMove: true,//カラムのドラッグ＆ドロップ
      fixedColumnsStart: 1,//1列目の固定
      manualColumnFreeze: true,//手動でのカラムの固定
      manualColumnResize: true,//手動での列幅固定
      stretchH: 'all', // 'none' is default
      dropdownMenu: true,//dropdownメニュー
      licenseKey: 'non-commercial-and-evaluation',
    }
  }),

  components: {
    HotTable
  }
};

</script>