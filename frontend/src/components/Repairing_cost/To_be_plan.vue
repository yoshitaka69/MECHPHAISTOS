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
        "HTC",
        "VIVE",
        "2016-12-1",
        "2160x1200",
        true
      ],
      [
        "Oculus",
        "Rift S",
        "2019-05-20",
        "2560×1440",
        false
      ],
      [
        "Valve",
        "Index",
        "2019-06-28",
        "2880×1600",
        true
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

        { type: "text", title: "Id" },
        { type: "text", title: "Plant" },
        { type: "text", title: "Task" },
        { type: "text", title: "Cost" },

        //{ type: "calendar", title: "Release date", width: "250px" },
        //{ type: "Text", title: "Resolution", width: "250px"},
        //{ type: "checkbox", title: "Get?", width: "80px" },
      ],
      //INITIALIZATIONはここに書く https://bossanova.uk/jspreadsheet/v4/docs/quick-reference

      tableOverflow: true, // スクロールの有効化
      csvFileName: "HeadSetsData" // ダウンロード時のファイル名

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