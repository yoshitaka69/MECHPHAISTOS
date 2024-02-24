<template>
  <div>
    <v-flex>
      <v-card>
        <v-card-title>Safety Factor trend</v-card-title>
        <div id="sft"></div>
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
    axios.get("hhttp://127.0.0.1:8000/api/v1/nearMiss/").then((response) => {
      // データから年ごとの factors のカウントを抽出
      const dataByYear = response.data.reduce((acc, item) => {
        const year = new Date(item.date).getFullYear();

        // factor の要素数をカウント
        acc[year] = acc[year] || { Rule: 0, Methods: 0, Person: 0, Equipment: 0 };
        acc[year][item.factor]++;

        return acc;
      }, {});

      // データをPlotlyのtraceに変換
      const factors = ["Rule", "Methods", "Person", "Equipment"];
      const traces = factors.map((factor) => ({
        x: Object.keys(dataByYear),
        y: Object.values(dataByYear).map((count) => count[factor]),
        type: "bar",
        name: factor,
      }));

      const layout = { barmode: "stack" };

      Plotly.newPlot("sft", traces, layout);
    });
  },
};
</script>