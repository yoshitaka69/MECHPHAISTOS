<template>
  <div style="width: 100%; height: 100%;">
    PM03 Actual cost
    <div id="rpcPM03A" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
  data() {
    return {
      RepairingCostData: [],
    };
  },

  mounted() {
    this.getRepairingCostData().then(data => {
      this.RepairingCostData = data;
      this.plotGraph(); // データ取得後にグラフを描画
    }).catch(error => {
      console.error('Error during data fetching or plotting:', error);
    });

    const graphContainer = document.getElementById('rpcPM03A');
    const resizeObserver = new ResizeObserver(() => {
      this.plotGraph(); // サイズ変更時にグラフを再描画
    });
    resizeObserver.observe(graphContainer);
  },

  methods: {
    async getRepairingCostData() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;

      if (!userCompanyCode) {
        throw new Error("Error: No company code found for the user.");
      }

      const url = `http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/?format=json&companyCode=${userCompanyCode}`;
      const response = await axios.get(url);

      return response.data.flatMap(companyData =>
        companyData.actualPM03List.flatMap(plantData =>
          plantData.actualPM03.map(yearData => {
            const months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment", "totalCost"];
            return {
              plant: plantData.plant,
              data: months.map(month => ({
                month: month,
                cost: parseFloat(yearData[month]) || 0
              })).filter(monthData => monthData.cost !== 0)
            };
          })
        )
      );
    },

    plotGraph() {
      const plotData = this.RepairingCostData.map(plantData => ({
        x: plantData.data.map(entry => entry.month),
        y: plantData.data.map(entry => entry.cost),
        name: plantData.plant,
        type: 'scatter'
      }));

      const graphContainer = document.getElementById('rpcPM03A');
      const layout = {
        height: graphContainer.clientHeight,
        width: graphContainer.clientWidth,
        title: 'Repairing Cost PM03 Actual'
      };

      Plotly.newPlot('rpcPM03A', plotData, layout);
    }
  },

  beforeDestroy() {
    if (resizeObserver) {
      resizeObserver.disconnect();
    }
  }
};
</script>
