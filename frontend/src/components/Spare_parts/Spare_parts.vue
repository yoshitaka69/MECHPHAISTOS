<template>
      <div class="wrapper">
        <input type="button" value="行を追加" @click="jspreadsheetObj.insertRow()" /><br />
        <input type="button" value="ヘッダー一覧を取得" @click="getHeaders()" /><br />
        <div id="HeadSetSpreadSheet" ref="refspreadsheet"></div>
        <br>
        <input type="button" value="csvをダウンロード" @click="jspreadsheetObj.download()" /><br />
      </div>
</template>

<script>
import "jsuites/dist/jsuites.js"
import "jsuites/dist/jsuites.css"
import "jspreadsheet-ce/dist/jspreadsheet.css"
import jSpreadSheet from "jspreadsheet-ce"

export default {
  name: "sheet",
  data() {
    return {
      //表の初期値を入れておく
      //画像なども可能
      VRHeadSets: [
        [
          "",//image
          "1",//Id
          "(ex.) Motor",//name
          "Standard",//category
          "RX-78-5.7",//model
          "1234569-9",//serial number
          "change motor",//task name
          "900000",//price
          "1",//number of ~
          "pieces",//unit
          "warehouse 1",//location
          "8",//delivery time
          "when we change No.1 agitator, we have to change this motor too",//description
        ],
        [
          "",//image
          "2",//Id
          "(ex.) agitator",//name
          "Standard",//category
          "ag89-78-5.7",//model
          "1233333-9",//serial number
          "replace agitator",//task name
          "180000",//price
          "4",//number of ~
          "pieces",//unit
          "warehouse 2",//location
          "14",//delivery time
          "This agitator is bad actor,we keep this agitator every time",//description
        ],
        [
          "",//image
          "3",//Id
          "(ex.) pump",//name
          "Standard",//category
          "zew99-0045",//model
          "135455333-9",//serial number
          "exchange pump",//task name
          "550000",//price
          "2",//number of ~
          "pieces",//unit
          "plantA",//location
          "60",//delivery time
          "This pump is needed exchange by operator",//description
        ],
      ],
    };
  },
  computed: {
    //表の初期値
    jSpreadSheetOptins() {
      return {
        //表の設定等
        //チェックボックスやカレンダー、プルダウンメニューも可能
        data: this.VRHeadSets,
        columns: [

          { type: "image", title: "Image",width:120},
          { type: "text", title: "Id",width:50},
          { type: "text", title: "Name",width:200 },
          {
            type: "dropdown",
            title: "Category",
            width: "130px",
            source: ["Assembly", "Standard", "consumables", "supplies"],
          },
          { type: "text", title: "Model" ,width:150},
          { type: "text", title: "serial number", width:150},
          { type: "text", title: "Task name",width:250 },
          { type: "text", title: "Price" ,width:120, mask:'$ #.##,00', decimal:','},
          { type: "text", title: "Number of ~",width:100 },
          { type: "text", title: "Unit",width:80 },
          { type: "text", title: "Location",width:150 },
          { type: "text", title: "Delivery time",width:100 },
          { type: "text", title: "Description" ,width:600},

          
          //{ type: "calendar", title: "Release date", width: "250px" },
          //{ type: "Text", title: "Resolution", width: "250px"},
          //{ type: "checkbox", title: "Get?", width: "80px" },
        ],
        //INITIALIZATIONはここに書く https://bossanova.uk/jspreadsheet/v4/docs/quick-reference
        filters: true,
        csvFileName: "BOM",// ダウンロード時のファイル名
        search:true,
        toolbar:[
        {
            type: 'i',
            content: 'undo',
            onclick: function() {
                table.undo();
            }
        },
        {
            type: 'i',
            content: 'redo',
            onclick: function() {
                table.redo();
            }
        },
        {
            type: 'i',
            content: 'save',
            onclick: function () {
                table.download();
            }
        },
        {
            type: 'select',
            k: 'font-family',
            v: ['Arial','Verdana']
        },
        {
            type: 'select',
            k: 'font-size',
            v: ['9px','10px','11px','12px','13px','14px','15px','16px','17px','18px','19px','20px']
        },
        {
            type: 'i',
            content: 'format_align_left',
            k: 'text-align',
            v: 'left'
        },
        {
            type:'i',
            content:'format_align_center',
            k:'text-align',
            v:'center'
        },
        {
            type: 'i',
            content: 'format_align_right', 
            k: 'text-align',
            v: 'right'
        },
        {
            type: 'i',
            content: 'format_bold',
            k: 'font-weight',
            v: 'bold'
        },
        {
            type: 'color',
            content: 'format_color_text',
            k: 'color'
        },
        {
            type: 'color',
            content: 'format_color_fill',
            k: 'background-color'
        },
    ], 

      };
    },
  },
  methods: {
    //メソッドの使用例 https://bossanova.uk/jspreadsheet/v4/docs/programmatically-changes
    getHeaders: function () {
      alert(this.jspreadsheetObj.getHeaders());
    },
  },
  mounted: function () {
    //インスタンス化
    const jspreadsheetObj = jSpreadSheet(
      //DOM参照
      this.$refs["refspreadsheet"],
      //表の設定データ
      this.jSpreadSheetOptins
    );
    //オブジェクトから thisに対してコピー
    Object.assign(this, { jspreadsheetObj });
  },
};

</script>