<template>
  <button v-on:click="updateData" class="controls">Update Data</button>
  <div id="Input_repairingCost">
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
        data: [
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//1
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//2
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//3
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//4
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//5
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//6
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//6
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//7
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//8
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//9
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//10
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//11
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//12
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//13
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//14
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//15
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//16
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//17
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//18
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//19
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//20
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//21
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//22
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//23
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//24
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//25
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//26
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//27
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//28
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//29
          ['', '', "", "", "", "", "", "", "", "", "", "", ""],//30
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

  },
  components: {
    HotTable,
  },
});

export default TableComponent;
</script>