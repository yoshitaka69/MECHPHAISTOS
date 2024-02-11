<template>
  <div id="example1">
    <h2>PM02 Repairing cost</h2>
    <HotTable ref="hotTableComponent" :settings="hotSettings"></HotTable>
  </div>
</template>


<script>
import { HotTable } from "@handsontable/vue3";
import axios from "axios";
import 'handsontable/dist/handsontable.full.css';


const URL = "http://localhost:3000/PlannedPM02";


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
          const plant = data.plant;
          const jan = data.jan;
          const feb = data.feb;
          const mar = data.mar;
          const apr = data.apr;
          const may = data.may;
          const jun = data.jun;
          const jul = data.jul;
          const aug = data.aug;
          const sep = data.sep;
          const oct = data.oct;
          const nov = data.nov;
          const dec = data.dec;
          const total = data.total;


          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
            columns: [{ data: "plant" }, { data: "jan" },{data:"feb"},{data:"mar"},{data:"apr"}, { data: "may" },{data:"jun"},{data:"jul"},{data:"aug"}, { data: "sep" },{data:"oct"},{data:"nov"},{data:"dec"},{data:"total"}]
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
        "Plant",//1
        "Jan",//2
        "Feb",//3
        "Mar",//4
        "Apr",//5
        "May",//6
        "Jun",//7
        "Jul",//8
        "Aug",//9
        "Sep",//10
        "Oct",//11
        "Nov",//12
        "Dec",//13
        "Total"//14
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
        { type: "text" },//11
        { type: "text" },//12
        { type: "text" },//13
        { type: "text" },//14
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