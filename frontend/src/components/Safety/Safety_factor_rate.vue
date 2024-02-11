<template>
    <div>
      <v-flex>
        <v-card>
          <v-card-title>Safety factor</v-card-title>
          <div id="SafeRate"></div>
        </v-card>
      </v-flex>
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
    axios.get("http://localhost:3000/NearMiss")
    .then(response => {
        const factorArray = response.data.map(item => item['factor']);

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
            height: 500,
            width: 500,
          };
  
          // SafeRate 要素が存在することを確認してからグラフを描画
          if (document.getElementById('SafeRate')) {
            console.log("Before plotting");  // 追加
            Plotly.newPlot('SafeRate', [data], layout);
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
  