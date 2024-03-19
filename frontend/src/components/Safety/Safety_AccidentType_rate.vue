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
import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート

export default {
  data() {
    return {
      values: {},
      error: null,
    };
  },

  mounted() {
    const userStore = useUserStore();
    const userCompanyCode = userStore.companyCode;

    if (!userCompanyCode) {
      console.error("Error: No company code found for the user.");
      return; // companyCodeがない場合、処理を中断
    }

    const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;

    axios.get(url, {
      headers: {
        "Content-Type": "application/json"
      },
      withCredentials: true
    })
      .then(response => {
        const nearMissData = response.data;
        console.log("nearMissData", nearMissData);

        // 全ての nearMissList をフラットなリストに変換
        const allNearMisses = nearMissData.flatMap(companyData => companyData.nearMissList);

        console.log("allNearMisses", allNearMisses);

        // typeOfAccident を抽出して配列を作成
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
