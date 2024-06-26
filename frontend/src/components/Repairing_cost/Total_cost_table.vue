<template>
  <div id="TotalPlannedCostTable">
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

const TableComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [],
        colHeaders: ['Plant', 'Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'Total'],
        columns: [
          { data: "plant", readOnly: true },
          { data: "year", readOnly: true },
          { data: "jan", readOnly: true },
          { data: "feb", readOnly: true },
          { data: "mar", readOnly: true },
          { data: "apr", readOnly: true },
          { data: "may", readOnly: true },
          { data: "jun", readOnly: true },
          { data: "jul", readOnly: true },
          { data: "aug", readOnly: true },
          { data: "sep", readOnly: true },
          { data: "oct", readOnly: true },
          { data: "nov", readOnly: true },
          { data: "dec", readOnly: true },
          { data: "commitment", readOnly: true },
          { data: "total", readOnly: true },
        ],
        afterGetColHeader: (col, TH) => {
          if (col === -1) {  // ヘッダー行の場合
            return;
          }
          // 特定の列インデックスまたはすべてのヘッダーに適用したい場合
          TH.style.backgroundColor = '#FFCC99'; // 薄いオレンジ色
          TH.style.color = 'black';
          TH.style.fontWeight = 'bold';  // テキストを太字に設定
        },
        width: '100%',
        height: 'auto',
        contextMenu: true, // コンテキストメニュー
        autoWrapRow: true,
        autoWrapCol: true,
        fixedRowsTop: 2, // 列固定
        manualColumnFreeze: true, // コンテキストメニュー手動でコラム解除
        manualColumnResize: true, // 手動での列幅調整
        manualRowResize: true, // 列の手動高さ調整
        filters: true,
        dropdownMenu: true,
        comments: true, // コメントの有り無し
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
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;

      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }

      const url = `http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/?format=json&companyCode=${userCompanyCode}`;

      axios.get(url, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: true
      })
        .then(response => {
          const actualCostData = response.data;
          const currentYear = new Date().getFullYear();

          // データ抽出
          const tableData = actualCostData.flatMap(companyData =>
            companyData.summedPlannedCostList
              .filter(yearData => yearData.year === currentYear)
              .map(yearData => ({
                plant: yearData.plant,
                year: yearData.year,
                jan: parseFloat(yearData.sumJan) || 0,
                feb: parseFloat(yearData.sumFeb) || 0,
                mar: parseFloat(yearData.sumMar) || 0,
                apr: parseFloat(yearData.sumApr) || 0,
                may: parseFloat(yearData.sumMay) || 0,
                jun: parseFloat(yearData.sumJun) || 0,
                jul: parseFloat(yearData.sumJul) || 0,
                aug: parseFloat(yearData.sumAug) || 0,
                sep: parseFloat(yearData.sumSep) || 0,
                oct: parseFloat(yearData.sumOct) || 0,
                nov: parseFloat(yearData.sumNov) || 0,
                dec: parseFloat(yearData.sumDec) || 0,
                commitment: parseFloat(yearData.sumCommitment) || 0,
                total: parseFloat(yearData.totalPlannedCost) || 0
              }))
          );

          console.log("Table Data:", tableData); // テーブルデータをログに出力

          // 空行を追加
          const blankRows = Array.from({ length: 5 }, () => ({}));
          const newData = tableData.concat(blankRows);

          // table setting
          this.$refs.hotTableComponent.hotInstance.updateSettings({
            data: newData
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
