<template>
  <div>
    <!--<v-flex>-->
      <v-card>
        <v-card-title>Safety Accident type (world)</v-card-title>
        <div id="SafeAccidentRate"></div>
      </v-card>
    <!--<v-flex>-->
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";

export default {
  data() {
    return {
      values: {},
      error: null,
    };
  },

  mounted() {
    axios.get("http://127.0.0.1:8000/api/company-near-misses/?format=json", {
      headers: {
        'Authorization': 'Token a860caa1717c3ce1b47474728f10677aa04c440c'
      }

    })

      .then(response => {
        // response.data は期待されるJSON構造の配列を持っていると想定
        const nearMissData = response.data;

        console.log("nearMissData", nearMissData)

        // companyCode をキーとして、対応する nearMissList を格納するオブジェクトを作成
        const companyNearMiss = nearMissData.reduce((accumulator, item) => {
          accumulator[item.companyCode] = item.nearMissList;
          return accumulator;
        }, {});

        // companyNearMiss から全ての nearMissList を抽出してフラットなリストを作成
        const allNearMisses = Object.values(companyNearMiss).flat();

        // allNearMisses から typeOfAccident を抽出して配列を作成
        const typeArray = allNearMisses.map(item => item['typeOfAccident']);

        console.log("typeArray:", typeArray);

        // typeOfAccident の出現回数を集計
        this.values = typeArray.reduce((accumulator, typeOfAccident) => {
          accumulator[typeOfAccident] = (accumulator[typeOfAccident] || 0) + 1;
          return accumulator;
        }, {});



        // グラフのデータ
        let data = {
          type: "pie",
          values: Object.values(this.values),
          labels: Object.keys(this.values),
          textinfo: "label+percent",
          insidetextorientation: "radial",
        };

        const layout = {
          height: 550,
          width: 550,
          automargin: true,
        };

        const config = { responsive: true }

        // SafeRate 要素が存在することを確認してからグラフを描画
        if (document.getElementById('SafeAccidentRate')) {
          console.log("Before plotting");  // 追加
          Plotly.newPlot('SafeAccidentRate', [data], layout, config);

          console.log("After plotting"); // 追加
        } else {
          console.error("Element with id 'SafeAccidentRate' not found.");
        }
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  },
};
</script>
