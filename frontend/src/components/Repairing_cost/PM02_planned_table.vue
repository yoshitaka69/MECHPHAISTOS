<template>
  <div id="PM02plannedtable">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import axios from "axios";

// register Handsontable's modules
registerAllModules();

const URL = "http://localhost:3000/RepairingCost";

const TableComponent = defineComponent({
  data() {
      return {
          hotSettings: {
              data: [
                  ['', '', "", "", "", "", "", "", "", "", "", "", ""],
              ],
              colHeaders: ['Plant', 'Jan', "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Total"],
              columns: [
                  {//'Plant'
                      type: "text",

                  },
                  {//'Jan'
                      type: 'numeric',

                  },
                  {//"Feb"
                      type: 'numeric',

                  },
                  {//"Mar"
                      type: 'numeric',

                  },
                  {//"Apr"
                      type: 'numeric',
                  },

                  {//"May"
                      type: 'numeric',

                  },
                  {//"Jun"
                      type: 'numeric',

                  },
                  {//"Jul"
                      type: 'numeric',

                  },
                  {//"Aug"
                      type: 'numeric',

                  },
                  {//"Sep"
                      type: 'numeric',

                  },
                  {//"Oct"
                      type: 'numeric',

                  },
                  {//"Nov"
                      type: 'numeric',

                  },
                  {//"Dec"
                      type: 'numeric',

                  },
                  {//"Total"
                      type: 'numeric',
                  },

              ],

              width: '100%',
              height: 'auto',
              contextMenu: true,//コンテキストメニュー
              autoWrapRow: true,
              autoWrapCol: true,
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
                  const repairingCostData = response.data;

                  console.log("Repairing Cost Data:", repairingCostData);

                  // plantName は配列で、各要素が plant の値です
                  const plantName = repairingCostData.map(data => data.plant);

                  // 各月のデータを plant ごとにまとめる
                  const monthData = repairingCostData.reduce((acc, data) => {
                      data.PlannedPM02.forEach(entry => {
                          if (!acc[entry.month]) {
                              acc[entry.month] = [];
                          }
                          acc[entry.month].push(entry.cost);
                      });
                      return acc;
                  }, {});

                  console.log("Plant Names:", plantName);
                  console.log("Month Data:", monthData);

                  // columns の設定
                  const columns = [
                      { data: "plant" },
                      { data: "Jan" },
                      { data: "Feb" },
                      { data: "Mar" },
                      { data: "Apr" },
                      { data: "May" },
                      { data: "Jun" },
                      { data: "Jul" },
                      { data: "Aug" },
                      { data: "Sep" },
                      { data: "Oct" },
                      { data: "Nov" },
                      { data: "Dec" },
                      { data: "Total" },
                  ];

                  // テーブルデータの作成
                  const tableData = plantName.map((name, index) => {
                      const rowData = {
                          plant: name,
                      };
                      Object.keys(monthData).forEach(month => {
                          rowData[month] = monthData[month][index] || 0;
                      });
                      return rowData;
                  });

                  console.log("Columns:", columns);
                  console.log("Table Data:", tableData);

                  this.$refs.hotTableComponent.hotInstance.updateSettings({
                      data: tableData,
                      columns,
                  });
              })
              .catch(error => console.log("error"));
      },
  },
  components: {
      HotTable,
  },
});

export default TableComponent;

</script>