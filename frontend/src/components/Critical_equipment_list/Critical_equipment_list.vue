<template>
  <div id="example1">
    <h2>Critical Equipment List</h2>
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
          const data = response.data;
          const id = data.id;
          const plant = data.plant;
          const location_No = data.locationNo;
          const function_code = data.function;
          const equipment = data.equipment;
          const parts = data.parts;
          const value_impact = data.valueImpact;
          const construction_period = data.constructionPeriod;
          const parts_delivery_date = data.partsDeliveryYear;
          const mttr = data.mttr;
          const count_of_PM02 = data.countOfPM02;
          const latest_PM02 = data.latestPM02;
          const count_of_PM03 = data.countOfPM03;
          const latest_PM03 = data.latestPM03;
          const count_of_PM04 = data.countOfPM04;

          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
            columns: [{ data: "id" }, { data: "plant" },{data:"locationNo"},{data:"function"},{data:"equipment"}, { data: "parts" },{data:"valueImpact"},{data:"constructionPeriod"},{data:"partsDeliveryYear"}, { data: "mttr" },{data:"countOfPM02"},{data:"latestPM02"},{data:"countOfPM03"},{data:"latestPM03"},{data:"countOfPM04"}]
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
        "Id",
        "Plant",
        "Location No",
        "Function",
        "Equipment",
        "Parts",
        "Value Impact",
        "Construction Period",
        "Parts Delivery Date",
        "MTTR",
        "CountOfPM02",
        "LatestPM02",
        "CountOfPM03",
        "LatestPM03",
        "CountOfPM04",
        "LatestPM04",
        "ImpactProduction",
        "ProbabilityOfFailure",
        "Assessment",
      ],

      columns: [
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" },
        { type: "text" }
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