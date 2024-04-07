<template>
    <div id="Total actual cost">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { HotTable } from '@handsontable/vue3';
  import axios from "axios";
  
  export default defineComponent({
    data() {
      const currentYear = new Date().getFullYear();
      const futureYears = Array.from({ length: 11 }, (_, i) => currentYear + i);
  
      const colHeaders = [
        'Plant',
        ...futureYears.map((year) => year.toString()), // 年のリストを colHeaders に追加
      ];
  
      const columns = [
        { data: "plant" },
        ...futureYears.map((year) => ({ data: year })),
      ];
  
      return {
        hotSettings: {
          data: [[]],
          colHeaders,
          columns,
          width: '100%',
          height: 'auto',
          contextMenu: true,
          autoWrapRow: true,
          autoWrapCol: true,
          fixedRowsTop: 2,
          manualColumnFreeze: true,
          manualColumnResize: true,
          manualRowResize: true,
          filters: true,
          dropdownMenu: true,
          comments: true,
          fillHandle: { autoInsertRow: true },
          licenseKey: 'non-commercial-and-evaluation',
        },
      };
    },
  
    created() {
      this.getDataAxios();
    },
  
    methods: {
      getDataAxios() {
        axios
          .get('http://localhost:3000/RepairingCost', {
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
  
            const plantName = repairingCostData.map(data => data.plant);
  
            const yearData = repairingCostData.reduce((acc, data) => {
              data.TotalActualCost.forEach(entry => {
                if (!acc[entry.year]) {
                  acc[entry.year] = [];
                }
                acc[entry.year].push(entry.cost);
              });
              return acc;
            }, {});
  
            const tableData = plantName.map((name, index) => {
              const rowData = { plant: name };
              Object.keys(yearData).forEach(year => {
                rowData[year] = yearData[year][index] || 0;
              });
              return rowData;
            });

            					// 空行を追加
					const blankRows = Array.from({ length: 5 }, () => ({}));
					const newData = tableData.concat(blankRows);

  
            this.$refs.hotTableComponent.hotInstance.updateSettings({
              data: newData,
            });
          })
          .catch(error => console.log("error"));
      },
    },
  
    components: {
      HotTable,
    },
  });
  </script>
  