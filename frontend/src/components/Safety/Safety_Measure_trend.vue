<template>
    <div>
      <v-flex>
        <v-card>
          <v-card-title>Safety Measure trend</v-card-title>
          <div id="smt"></div>
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
        x: [],
        y: [],
      };
    },
  
    mounted() {
      axios.get("http://localhost:3000/NearMiss").then((response) => {
        // データから年ごとの measures のカウントを抽出
        const dataByYear = response.data.reduce((acc, item) => {
          const year = new Date(item.date).getFullYear();
  
          // measures の要素数をカウント
          acc[year] = acc[year] || { A: 0, B: 0, C: 0, D: 0, E: 0 };
          acc[year][item.measures]++;
  
          return acc;
        }, {});
  
        // データをPlotlyのtraceに変換
        const measures = ["A", "B", "C", "D", "E"];
        const traces = measures.map((measure) => ({
          x: Object.keys(dataByYear),
          y: Object.values(dataByYear).map((count) => count[measure]),
          type: "bar",
          name: measure,
        }));
  
        const layout = { barmode: "stack" };
  
        Plotly.newPlot("smt", traces, layout);
      });
    },
  };
  </script>