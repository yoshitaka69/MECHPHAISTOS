<template>
    <div>

PM05 Actual cost
        <div id="rpcPM05"></div>

    </div>
  </template>


 <script lang="ts" setup>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
import { useUserStore } from '@/stores/userStore';

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
          console.error("エラー: ユーザーの会社コードが見つかりません。");
          return;
        }

        const url = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json&companyCode=${userCompanyCode}`;
        const response = await axios.get(url);
        console.log("修理コストデータの取得:", response.data);

        let repairingCostData = response.data;
        for (const companyData of repairingCostData) {
          for (const plantData of companyData.actualPM05List) {
            const actualPM05Data = plantData.actualPM05;

            actualPM05Data.forEach(yearData => {
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
        console.error('修理コストデータの取得エラー:', error);
      }
    };

    getRepairingCostData()
      .then(() => {
        const plotData = this.RepairingCostData.map(plantData => {
          const xValues = plantData.data.map(entry => entry.month);
          const yValues = plantData.data.map(entry => entry.cost);

          // 折れ線グラフと棒グラフのトレースを作成
          let lineTrace = {
            x: xValues,
            y: yValues,
            type: 'scatter', // 折れ線グラフ
            mode: 'lines+markers',
            name: `${plantData.plant} - Line`
          };

          let barTrace = {
            x: xValues,
            y: yValues,
            type: 'bar', // 棒グラフ
            name: `${plantData.plant} - Bar`
          };

          return [lineTrace, barTrace];
        }).flat();

        const layout = {
          height: 500,
          width: 600,
          title: '修理コスト',
          barmode: 'group'
        };

        Plotly.newPlot('rpcPM05', plotData, layout);
      })
      .catch(error => {
        console.error('修理コストグラフ描画エラー:', error);
        throw error;
      });
  },
};
</script>
