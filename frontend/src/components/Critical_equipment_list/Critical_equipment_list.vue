<template>
  <div id="example1">
    <h>test</h>
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
          const id = data.Id;
          const plant = data.Plant;
          const location_No = data.LocationNo;
          const function_code = data.Function;
          const equipment = data.Equipment;
          const parts = data.Parts;
          const value_impact = data.ValueImpact;
          const construction_period = data.ConstructionPeriod;
          const parts_delivery_date = data.PartsDeliveryDate;
          const mttr = data.MTTR;
          const count_of_PM02 = data.CountOfPM02;
          const latest_PM02 = data.LatestPM02;
          const count_of_PM03 = data.CountOfPM03;
          const latest_PM03 = data.LatestPM03;
          const count_of_PM04 = data.CountOfPM04;

          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: data,
            columns: [{ data: "Id" }, { data: "Plant" },{data:"LocationNo"},{data:"Function"},{data:"Equipment"}, { data: "Parts" },{data:"ValueImpact"},{data:"ConstructionPeriod"},{data:"PartsDeliveryDate"}, { data: "MTTR" },{data:"CountOfPM02"},{data:"LatestPM02"},{data:"CountOfPM03"},{data:"LatestPM03"},{data:"CountOfPM04"}]
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