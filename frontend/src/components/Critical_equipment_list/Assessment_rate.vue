<template>
    <div>
        <v-card>
          <v-card-title>Assessment rate</v-card-title>
          <div id="AssessmentRate"></div>
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
        axios.get("http://localhost:3000/CeList")
    .then(response => {
        const typeArray = response.data.map(item => item['assessment']);

        console.log("typeArray:", typeArray);  // 追加

        this.values = typeArray.reduce((accumulator, assessment) => {
            accumulator[assessment] = (accumulator[assessment] || 0) + 1;
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
            height: 400,
            width: 400,
            automargin: true,
          };

          const config = { responsive: true }
  
          // SafeRate 要素が存在することを確認してからグラフを描画
          if (document.getElementById('AssessmentRate')) {
            console.log("Before plotting");  // 追加
            Plotly.newPlot('AssessmentRate', [data], layout,config);

            console.log("After plotting"); // 追加
          } else {
            console.error("Element with id 'AssessmentRate' not found.");
          }
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
    },
  };
  </script>
  
