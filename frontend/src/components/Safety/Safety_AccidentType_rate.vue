<template>
    <div>
        <v-card>
          <v-card-title>Safety Accident type</v-card-title>
          <div id="SafeAccidentRate"></div>
        </v-card>
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
        axios.get("http://127.0.0.1:8000/api/nearMiss/?format=json")
    .then(response => {
        const typeArray = response.data.map(item => item['typeOfAccident']);

        console.log("typeArray:", typeArray);  // 追加

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
            Plotly.newPlot('SafeAccidentRate', [data], layout,config);

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
  