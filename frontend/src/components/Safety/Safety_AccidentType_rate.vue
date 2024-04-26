<template>
  <div>
    <div id="SafeAccidentRate" ref="plotArea" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
import { useUserStore } from '@/stores/userStore';

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
      return;
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
      const allNearMisses = nearMissData.flatMap(companyData => companyData.nearMissList);
      const typeArray = allNearMisses.map(item => item['typeOfAccident']);

      this.values = typeArray.reduce((accumulator, typeOfAccident) => {
        accumulator[typeOfAccident] = (accumulator[typeOfAccident] || 0) + 1;
        return accumulator;
      }, {});

      this.plotGraph();
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });

    this.resizePlot();  // 初期描画
    window.addEventListener('resize', this.resizePlot);
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.resizePlot);
  },

  methods: {
    resizePlot() {
      if (this.$refs.plotArea) {
        const width = this.$refs.plotArea.clientWidth;
        const height = this.$refs.plotArea.clientHeight;
        this.plotGraph(width, height);
      }
    },

    plotGraph(width, height) {
      const data = [{
        type: "pie",
        values: Object.values(this.values),
        labels: Object.keys(this.values),
        textinfo: "label+percent",
        insidetextorientation: "radial"
      }];

      const layout = {
        width: width,
        height: height,
        margin: { l: 5, r: 5, t: 5, b: 5 },
        showlegend: false  // レジェンドを非表示に設定
        //legend: { x: 5, y: 0, xanchor: 'right', yanchor: 'bottom', font: { size: 10, color: '#000' } }
      };

      const config = { responsive: true };

      Plotly.newPlot('SafeAccidentRate', data, layout, {displayModeBar: false}, config);
    }
  },
};
</script>
