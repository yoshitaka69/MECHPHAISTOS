<template>
    <div>
      <v-card>
        <v-card-title>Safety factor type</v-card-title>
        <div id="SafeRate"></div>
      </v-card>
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
  
      const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${userCompanyCode}`;
  
      axios.get(url, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: true
      })
        .then(response => {
          const nearMissData = response.data;
  
          // 全ての nearMissList をフラットなリストに変換
          const allNearMisses = nearMissData.flatMap(companyData => companyData.nearMissList);
  
          // factor の配列を作成
          const factorArray = allNearMisses.map(item => item['factor']);
  
          this.values = factorArray.reduce((accumulator, factor) => {
            accumulator[factor] = (accumulator[factor] || 0) + 1;
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
            width: 500,
            height: 500,
            automargin: true,
          };
  
          const config = { responsive: true }
  
          // SafeRate 要素が存在することを確認してからグラフを描画
          if (document.getElementById('SafeRate')) {
            console.log("Before plotting");  // 追加
            Plotly.newPlot('SafeRate', [data], layout, config);
            console.log("After plotting"); // 追加
          } else {
            console.error("Element with id 'SafeRate' not found.");
          }
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    },
  };
  </script>