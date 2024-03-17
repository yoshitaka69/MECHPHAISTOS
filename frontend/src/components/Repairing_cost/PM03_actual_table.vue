<template>
  <div id="PM03actualtable">
      <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
  </div>
</template>

<script>
  import { defineComponent } from 'vue';
  import { HotTable } from '@handsontable/vue3';
  import { registerAllModules } from 'handsontable/registry';
  import 'handsontable/dist/handsontable.full.css';
  import axios from "axios";
  import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
  
  // register Handsontable's modules
  registerAllModules();
  
  const URL = "http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/?format=json";
  
  const TableComponent = defineComponent({
    data() {
      return {
        hotSettings: {
          data: [
            ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ],
          colHeaders: ['Plant', 'Year', 'Jan', "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "commitment", "Total"],
          columns: [
            {//'Plant'
              type: "text",
  
            },
            {//'Jan'
              type: 'numeric',
  
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
        axios.get(URL, {
          headers: {
            "Content-Type": "application/json"
          },
          withCredentials: true
        })
          .then(response => {
            let actualCostData = response.data;
  
            // Pinia ストアから companyCode を取得
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;
  
            // ユーザーの companyCode に基づいてデータをフィルタリング
            if (userCompanyCode) {
              actualCostData = actualCostData.filter(companyData => companyData.companyCode === userCompanyCode);
            }
  
            //データ抽出
            const months = ["year","jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment",];
            const tableData = actualCostData.flatMap(companyData =>
              companyData.actualPM03List.flatMap(plantData =>
                plantData.actualPM03.map(yearData => {
                  const rowData = { plant: plantData.plant, year: yearData.year };
                  months.forEach(month => {
                    rowData[month] = parseFloat(yearData[month]) || 0;
                  });
                  rowData["totalCost"] = parseFloat(yearData["totalCost"]) || 0;
                  return rowData;
                })
              )
            );
  
            // columns の設定
            const columns = [
              { data: "plant" },
              { data: "year" },
              { data: "jan" },
              { data: "feb" },
              { data: "mar" },
              { data: "apr" },
              { data: "may" },
              { data: "jun" },
              { data: "jul" },
              { data: "aug" },
              { data: "sep" },
              { data: "oct" },
              { data: "nov" },
              { data: "dec" },
              { data: "commitment" },
              { data: "totalCost" },
            ];
            console.log("Table Data:", tableData); // テーブルデータをログに出力
  
            //table setting
            this.$refs.hotTableComponent.hotInstance.updateSettings({
              data: tableData,
              columns,
            });
          })
          .catch(error => {
            console.error("Error fetching data:", error);
          });
      },
    },
    components: {
      HotTable,
    },
  });
  
  export default TableComponent;
  </script>