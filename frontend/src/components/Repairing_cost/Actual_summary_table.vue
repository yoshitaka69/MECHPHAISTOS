<template>
  <div id="actual_summary_table">
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

// totalCostの計算と表示のためのカスタムレンダラー
function totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties) {
  const rowData = instance.getDataAtRow(row);
  const totalCost = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'commitment']
    .map(month => parseFloat(rowData[monthColumnIndices[month]]) || 0)
    .reduce((sum, amount) => sum + amount, 0);

  td.innerText = totalCost.toFixed(2); // 2桁の小数点で表示
  return td;
}

const monthColumnIndices = {
  jan: 3, feb: 4, mar: 5, jun:6, jul:7, aug:8, sep:9, oct:10, nov:11, dec:12, commitment:13// ... 各月のカラムインデックス...
};




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
            renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties),
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
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;

      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }

      const url = `http://127.0.0.1:8000/api/calculation/summedByCompany/?format=json&companyCode=${userCompanyCode}`;

      axios.get(url, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: true
      }).then(response => {
        const actualCostData = response.data;
        // データ変換
        const tableData = actualCostData.flatMap(companyData =>
          companyData.summedActualCostList.map(item => ({
            plant: item.plant,
            year: item.year,
            jan: parseFloat(item.sumJan) || 0,
            feb: parseFloat(item.sumFeb) || 0,
            mar: parseFloat(item.sumMar) || 0,
            apr: parseFloat(item.sumApr) || 0,
            may: parseFloat(item.sumMay) || 0,
            jun: parseFloat(item.sumJun) || 0,
            jul: parseFloat(item.sumJul) || 0,
            aug: parseFloat(item.sumAug) || 0,
            sep: parseFloat(item.sumSep) || 0,
            oct: parseFloat(item.sumOct) || 0,
            nov: parseFloat(item.sumNov) || 0,
            dec: parseFloat(item.sumDec) || 0,
            commitment: parseFloat(item.sumCommitment) || 0,
          }))
        );

        console.log("Table Data:", tableData); // テーブルデータをログに出力

        const columns = [
          {
            data: "plant",
          },
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
          { data: 'total', readOnly: true, renderer: (instance, td, row, col, prop, value, cellProperties) => totalCostRenderer(monthColumnIndices, instance, td, row, col, prop, value, cellProperties), },
        ];

        const blankRows = Array.from({ length: 5 }, () => ({}));
        const newData = tableData.concat(blankRows);

        this.$refs.hotTableComponent.hotInstance.updateSettings({
          data: newData,
          columns,
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