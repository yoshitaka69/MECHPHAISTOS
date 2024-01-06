<template>
    <div class="wrapper">
      <h1>PM03 </h1>
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
name: "sheet",
data() {
  return {
    //表の初期値を入れておく
    //画像なども可能
    VRHeadSets: [
      [
        "PlantA",
        "450000",
        "500000",
        "450000",
        "450000",
        "800000",
        "50000",
        "450000",
        "900000",
        "1350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "2256000",
      ],
      [
        "PlantB",
        "450000",
        "500000",
        "450000",
        "40000",
        "800000",
        "50000",
        "450000",
        "900000",
        "2350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "2256000",
      ],
      [
        "PlantC",
        "450000",
        "500000",
        "450000",
        "450000",
        "800000",
        "50000",
        "450000",
        "900000",
        "1350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "2256000",
      ],
      [
        "PlantD",
        "450000",
        "500000",
        "450000",
        "450000",
        "800000",
        "50000",
        "450000",
        "900000",
        "1350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "2256000",
      ],
      [
        "PlantE",
        "450000",
        "500000",
        "450000",
        "450000",
        "800000",
        "50000",
        "450000",
        "900000",
        "1350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "1820000",
      ],
      [
        "Total",
        "450000",
        "500000",
        "450000",
        "450000",
        "800000",
        "50000",
        "450000",
        "900000",
        "1350000",
        "500000",
        "200000",
        "150000",
        "1820000",
        "2256000",
        "2256000",
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
      index:[
        {type:"Text", title:"PM02"}

      ],      
      columns: [

        {
          type: "text",
          title: "Plant",
          width: "100px",},

        { type: "numeric'", title: "Jan.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Feb.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Mar.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Apr.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "May.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Jun.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Jul.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Aug.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Sep.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Oct.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Nov.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Dec.", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Commitment", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "Total", width: "100px",mask:'$ #.##,00', decimal:',' },
        { type: "numeric'", title: "PM02(target)", width: "100px",mask:'$ #.##,00', decimal:',' },
        //{ type: "calendar", title: "Release date", width: "250px" },
        //{ type: "Text", title: "Resolution", width: "250px"},
        //{ type: "checkbox", title: "Get?", width: "80px" },
      ],
      //INITIALIZATIONはここに書く https://bossanova.uk/jspreadsheet/v4/docs/quick-reference
      csvFileName: "HeadSetsData" // ダウンロード時のファイル名

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