<template>
  <div ref="plotArea" style="width: 100%; height: 100%;">
    <div id="SafeAccidentRate" style="width: 100%; height: 100%;"></div>
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
      resizeObserver: null,
    };
  },

  mounted() {
    this.initialize();
  },

  beforeDestroy() {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  },

  methods: {
    async initialize() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }
      try {
        const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;
        const response = await axios.get(url, {
          headers: { "Content-Type": "application/json" },
          withCredentials: true
        });
        const nearMissData = response.data;
        const allNearMisses = nearMissData.flatMap(companyData => companyData.nearMissList);
        const typeArray = allNearMisses.map(item => item['typeOfAccident']);
        this.values = typeArray.reduce((accumulator, typeOfAccident) => {
          accumulator[typeOfAccident] = (accumulator[typeOfAccident] || 0) + 1;
          return accumulator;
        }, {});
        this.plotGraph();
      } catch (error) {
        console.error("Error fetching data:", error);
      }
      this.setupResizeObserver();
    },

    setupResizeObserver() {
      this.resizeObserver = new ResizeObserver(entries => {
        for (let entry of entries) {
          if (entry.target === this.$refs.plotArea.parentNode) {
            this.resizePlot();
          }
        }
      });
      this.resizeObserver.observe(this.$refs.plotArea.parentNode); // 監視対象を設定
    },

    resizePlot() {
      const width = this.$refs.plotArea.clientWidth;
      const height = this.$refs.plotArea.clientHeight;
      this.plotGraph(width, height);
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
        showlegend: false
      };

      const config = { responsive: true };
      Plotly.newPlot('SafeAccidentRate', data, layout, { displayModeBar: false }, config);
    }
  },
};
</script>
