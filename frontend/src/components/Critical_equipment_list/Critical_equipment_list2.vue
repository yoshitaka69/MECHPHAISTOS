<template>
    <div class="wrapper">

      <br>
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
    CElist: [
      [
        "1",//Id
        "ex.) PlantA",//plant text
        "n400-A-1-1",//location No text
        "No.1 mixing Tank",//function text
        "Motor",//equipment text 
        "Bearing 6310,6210", //parts
        "very High(5)",//value impact text
        "5",//construction period numeric
        "14",//parts delivery date numeric
        "14",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "very High(5)",//impact production
        "Low(2)",//probability of failure
        "Middle(3)",//assessment
      ],
      [
        "2",//Id
        "ex.) PlantA",//plant text
        "n400-A-1-2",//location No text
        "No.1 mixing Tank",//function text
        "Agitator",//equipment text
        "reduction gear", //parts
        "middle(3)",//value impact text
        "2",//construction period numeric
        "5",//parts delivery date numeric
        "5",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "middle(3)",//impact production
        "Low(2)",//probability of failure
        "Low(2)",//assessment
      ],
      [
        "3",//Id
        "ex.) PlantB",//plant text
        "n400-B-5-1",//location text
        "No.1 Dryer",//function text
        "No.1 supply blower",//equipment text 
        "Bearing 6310, Motor", //parts
        "High(4)",//value impact text
        "5",//construction period numeric
        "14",//parts delivery date numeric
        "14",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "very High(5)",//impact production
        "High(4)",//probability of failure
        "Very High(5)",//assessment
      ],
      [
        "4",//Id
        "ex.) PlantC",//plant text
        "n400-C-4-1",//location text
        "No.2 belt conveyor",//equipment text 
        "",//function text
        "Belt", //parts
        "very High(5)",//value impact text
        "5",//construction period numeric
        "14",//parts delivery date numeric
        "14",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "very High(5)",//impact production
        "Low(2)",//probability of failure
        "Middle(3)",//assessment
      ],
      [
        "5",//Id
        "ex.) PlantC",//plant text
        "n400-C-4-1",//location text
        "No.2 belt conveyor",//equipment text 
        "Feed motor",//function text
        "motor", //parts
        "very High(5)",//value impact text
        "5",//construction period numeric
        "14",//parts delivery date numeric
        "14",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "very High(5)",//impact production
        "Low(2)",//probability of failure
        "Middle(3)",//assessment
      ],
      [
        "6",//Id
        "ex.) PlantC",//plant text
        "n400-C-4-1",//location text
        "No.2 belt conveyor",//equipment text 
        "Hopper",//function text
        "", //parts
        "very High(5)",//value impact text
        "5",//construction period numeric
        "14",//parts delivery date numeric
        "14",//mttr numeric
        "2",//count of PM02 numeric
        "",//latest PM02 
        "1",//count of PM03
        "",//latest PM03
        "1",//count of PM04
        "",//latest PM04
        "very High(5)",//impact production
        "Low(2)",//probability of failure
        "Middle(3)",//assessment
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
      data: this.CElist,
      minDimensions:[18,20],   
      columns: [

        {
          type: "numeric",
          title: "Id",
          width: "60px",},

        { type: "text", title: "Plant", width: "150px" },
        { type: "text", title: "Location No.", width: "120px" },
        { type: "text", title: "Function", width: "150px" },
        { type: "text", title: "Equipment", width: "150px" },
        { type: "text", title: "Parts", width: "150px" },
        { type: "text", title: "Value impact", width: "100px" },
        { type: "numeric", title: "Construction period", width: "100px" },
        { type: "numeric", title: "Parts delivery date", width: "100px" },
        { type: "numeric", title: "MTTR", width: "100px" },
        { type: "numeric", title: "Count of PM02", width: "100px" },
        { type: "calendar", title: "Latest PM02", width: "100px" },
        { type: "numeric", title: "Count of PM03", width: "100px" },
        { type: "calendar", title: "Latest PM03", width: "100px" },
        { type: "numeric", title: "Count of PM04", width: "100px" },
        { type: "calendar", title: "Latest PM04", width: "100px" },
        { type: "text", title: "Impact production", width: "100px" },
        { type: "text", title: "Probability of failure", width: "100px" },
        { type: "text", title: "Assessment", width: "100px" },



        //{ type: "calendar", title: "Release date", width: "250px" },
        //{ type: "Text", title: "Resolution", width: "250px"},
        //{ type: "checkbox", title: "Get?", width: "80px" },
      ],
      //INITIALIZATIONはここに書く https://bossanova.uk/jspreadsheet/v4/docs/quick-reference
      search:true,
      csvFileName: "Critical_equipment_list",// ダウンロード時のファイル名
      filters: true, 
      pagination: 50,
      paginationOptions: [10,25,50],
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