<template>
  <div style="width: 100%; height: 100%;">
    PM04 Actual cost
    <div id="rpcPM04A" style="width: 100%; height: 100%;"></div>
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
    const getRepairingCostData = async () => {
      try {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        if (!userCompanyCode) {
          console.error("Error: No company code found for the user.");
          return; // 処理を中断
        }

        const url = `http://127.0.0.1:8000/api/repairingCost/APM04ByCompany/?format=json&companyCode=${userCompanyCode}`;
        const response = await axios.get(url);
        console.log("Fetched RepairingCost Data:", response.data); // データ取得ログ

        let repairingCostData = response.data;
        for (const companyData of repairingCostData) {
          for (const plantData of companyData.actualPM04List) {
            const actualPM04Data = plantData.actualPM04;

            // 各月ごとのデータを新しい形式に変換
            actualPM04Data.forEach(yearData => {
              const months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment", "totalCost"];
              let monthCosts = [];
              months.forEach(month => {
                if (yearData[month]) {
                  monthCosts.push({
                    month: month,
                    cost: parseFloat(yearData[month])
                  });
                }
              });

              this.RepairingCostData.push({
                plant: plantData.plant,
                data: monthCosts
              });
            });
          }
        }
      } catch (error) {
        console.error('Error fetching RepairingCost data:', error);
      }
    };

    // 上記関数の実行
    getRepairingCostData()
      .then(() => {
        // 取得したデータを使ってグラフを描画
        const plotData = this.RepairingCostData.map(plantData => {
          const xValues = plantData.data.map(entry => entry.month);
          const yValues = plantData.data.map(entry => entry.cost);

          let trace = {
            x: xValues,
            y: yValues,
            name: plantData.plant,
          };

          return trace;
        });

        const layout = {
          height: 500,
          width: 600,
          title: 'Repairing Cost',
        };

        Plotly.newPlot('rpcPM04A', plotData, layout);
      })
      .catch(error => {
        console.error('Error plotting Repairing Cost graph:', error);
        throw error;
      });
  },
};
</script>