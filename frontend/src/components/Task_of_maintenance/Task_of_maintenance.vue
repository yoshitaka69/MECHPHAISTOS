<template>
  <div class="wrapper">
    <div id="HeadSetSpreadSheet" ref="refspreadsheet"></div>
    <br>
    <input type="button" value="行を追加" @click="jspreadsheetObj.insertRow()" /><br />
    <input type="button" value="csvをダウンロード" @click="jspreadsheetObj.download()" /><br />
  </div>
</template>

<script>
import "jsuites/dist/jsuites.js"
import "jsuites/dist/jsuites.css"
import "jspreadsheet-ce/dist/jspreadsheet.css"
import jSpreadSheet from "jspreadsheet-ce"

export default {
name: "Critical equipment list",
data() {
return {
  //表の初期値を入れておく
  //画像なども可能
  Tasklist: [
    [
      "1",//Id
      "ex.) change motor for replace",//task name
      "Plant A",//plant
      "No.1 mixing tank",//equipment
      "600",//cost
      "motor",//parts
      "14",//period task
      "",//next event
      "late",//situation
      "change motor for replace",//note
    ],
    [
      "2",//Id
      "ex.) prevent maintenance depend on time",//task name
      "Plant A",//plant
      "No.1 mixing tank",//equipment
      "800",//cost
      "agitator",//parts
      "18",//period task
      "",//next event
      "late",//situation
      "need change with the motor",//note
    ],
    [
      "3",//Id
      "ex.) change a belt",//task name
      "Plant B",//plant
      "No.2 belt conveyor",//equipment
      "50",//cost
      "belt",//parts
      "24",//period task
      "",//next event
      "",//situation
      "this belt is not important",//note
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
    data: this.Tasklist,
    minDimensions:[10,10],   
    columns: [

      {
        type: "numeric",
        title: "Id",
        width: "60px",}, //1 Id

      { type: "text", title: "Task name", width: "350px" }, //2
      { type: "text", title: "Plant", width: "100px" }, //3 
      { type: "text", title: "Equipment", width: "150px" }, //4
      { type: "text", title: "Cost", width: "100px", mask:'$ #.##,00', decimal:',' }, //5
      { type: "text", title: "Parts", width: "100px" }, //6
      { type: "text", title: "Period of Task", width: "100px" }, //7
      { type: "calendar", title: "Next Event", width: "100px" }, //8
      { type: "text", title: "Situation", width: "80px" }, //9
      { type: "text", title: "Note", width: "200px" }, //10
    ],
    //INITIALIZATIONはここに書く https://bossanova.uk/jspreadsheet/v4/docs/quick-reference
    search:true,
    csvFileName: "Task_of_maintenance", // ダウンロード時のファイル名
    filters: true,

  };
},
},
methods: {
//メソッドの使用例 https://bossanova.uk/jspreadsheet/v4/docs/programmatically-changes
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