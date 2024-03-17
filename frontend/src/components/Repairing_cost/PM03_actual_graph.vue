<template>
  <div>
    <v-flex>
      <v-card>
        <v-card-title>PM03 Actual cost</v-card-title>
        <div id="rpcPM03"></div>
      </v-card>
    </v-flex>
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
        const response = await axios.get('http://127.0.0.1:8000/api/repairingCost/APM03ByCompany/?format=json');
        let repairingCostData = response.data;

        // Pinia ストアから companyCode を取得
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        // ユーザーの companyCode に基づいてデータをフィルタリング
        if (userCompanyCode) {
          repairingCostData = repairingCostData.filter(companyData => companyData.companyCode === userCompanyCode);
        }

        // 各工場のデータごとに処理
        for (const companyData of repairingCostData) {
          for (const plantData of companyData.actualPM03List) {
            const actualPM03Data = plantData.actualPM03;

            // 各月ごとのデータを新しい形式に変換
            actualPM03Data.forEach(yearData => {
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

        Plotly.newPlot('rpcPM03', plotData, layout);
      })
      .catch(error => {
        console.error('Error plotting Repairing Cost graph:', error);
        throw error;
      });
  },
};
</script>