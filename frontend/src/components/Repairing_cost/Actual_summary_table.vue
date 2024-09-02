<template>
  <div id="actual_summary_table">
    <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import Handsontable from 'handsontable'; // Handsontableをインポート
import 'handsontable/dist/handsontable.full.css';
import axios from "axios";
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

// register Handsontable's modules
registerAllModules();

// plant列のカスタムレンダラー
function plantLinkRenderer(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments); // 基本のテキストレンダラーを適用
    if (value) {
        const link = document.createElement('a');
        link.href = `/repairing_cost_detail/${value}`; // RepairingCostDetail.vueを表示するURLを生成
        link.target = '_blank'; // 新しいタブで開く
        link.textContent = value; // テキストをリンクに設定
        link.style.color = 'blue'; // リンクの色を青に設定
        td.innerHTML = ''; // 既存の内容をクリア
        td.appendChild(link); // リンクをセルに追加
    }
}

const TableComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
        ],
        colHeaders: ['Plant', 'Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'Total'],
        rowHeaders: true,
        columns: [
          { data: "plant", readOnly: true, renderer: plantLinkRenderer }, // plant列にカスタムレンダラーを追加
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
        fillHandle: {
          autoInsertRow: true
        },
        licenseKey: 'non-commercial-and-evaluation',
        afterGetColHeader: (col, TH) => {
          if (col === -1) {
            return;
          }
          TH.style.backgroundColor = '#add8e6'; // 薄い青色
          TH.style.color = 'black';
          TH.style.fontWeight = 'bold';
        },
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

      const url = `http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?format=json&companyCode=${userCompanyCode}`;

      axios.get(url, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: true
      }).then(response => {
        const actualCostData = response.data;
        const currentYear = new Date().getFullYear();

        // データ変換
        const tableData = actualCostData.flatMap(companyData =>
          companyData.summedActualCostList
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
              total: parseFloat(yearData.totalActualCost) || 0
            }))
        );

        console.log("Table Data:", tableData); // テーブルデータをログに出力

        const blankRows = Array.from({ length: 5 }, () => ({}));
        const newData = tableData.concat(blankRows);

        this.$refs.hotTableComponent.hotInstance.updateSettings({
          data: newData
        });
      }).catch(error => {
        console.error("Error fetching data:", error);
      });
    }
  },

  components: {
    HotTable,
  },
});

export default TableComponent;
</script>
