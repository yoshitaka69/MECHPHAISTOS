<template>
    <div>
      <v-flex>
        <v-card>
          <v-card-title>Safety Measure</v-card-title>
          <div id="SafeMeasureRate"></div>
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
        axios.get("http://127.0.0.1:8000/api/v1/nearMiss/")
    .then(response => {
        const measuresArray = response.data.map(item => item['measures']);

        this.values = measuresArray.reduce((accumulator, measures) => {
            accumulator[measures] = (accumulator[measures] || 0) + 1;
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
          if (document.getElementById('SafeMeasureRate')) {
            console.log("Before plotting");  // 追加
            Plotly.newPlot('SafeMeasureRate', [data], layout);

            console.log("After plotting"); // 追加
          } else {
            console.error("Element with id 'SafeMeasureRate' not found.");
          }
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    },
  };
  </script>
  