<template>
  <div id="PM03actualtable">
    <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>
    <button v-on:click="updateData" class="controls">Update Data</button>
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
  jan: 3, feb: 4, mar: 5, jun: 6, jul: 7, aug: 8, sep: 9, oct: 10, nov: 11, dec: 12, commitment: 13// ... 各月のカラムインデックス...
};


const TableComponent = defineComponent({
  data() {
    return {
      hotSettings: {
        data: [
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],
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
            readOnly: true,
          },

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


  methods: {

    addRow() {
      const hotInstance = this.$refs.hotTableComponent.hotInstance;
      hotInstance.alter('insert_row', hotInstance.countRows());
    },


  },
  components: {
    HotTable,
  },
});

export default TableComponent;
</script>