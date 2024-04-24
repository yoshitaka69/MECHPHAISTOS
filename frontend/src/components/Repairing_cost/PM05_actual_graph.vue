<template>
  <div>
    PM05 Actual cost
    <div id="rpcPM05"></div>
  </div>
</template>

<script lang="ts" setup>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/userStore';

const RepairingCostData = ref([]);
const BarChartData = ref([]);
const currentYear = new Date().getFullYear();

const getRepairingCostData = async () => {
  try {
    const userStore = useUserStore();
    const userCompanyCode = userStore.companyCode;

    if (!userCompanyCode) {
      console.error("エラー: ユーザーの会社コードが見つかりません。");
      return;
    }

    const lineUrl = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json&companyCode=${userCompanyCode}`;
    const responseLine = await axios.get(lineUrl);
    console.log("折れ線グラフの修理コストデータの取得:", responseLine.data);

    const barUrl = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json`;
    const responseBar = await axios.get(barUrl);
    console.log("棒グラフの修理コストデータの取得:", responseBar.data);

    let repairingCostData = responseLine.data;
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

          RepairingCostData.value.push({
            plant: plantData.plant,
            data: monthCosts
          });
        });
      }
    }

    // 棒グラフデータの取得
    let barChartData = responseBar.data;
    for (const companyData of barChartData) {
      for (const plantData of companyData.actualPM05List) {
        const actualPM05Data = plantData.actualPM05.filter(item => item.year === currentYear);

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

          BarChartData.value.push({
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

onMounted(async () => {
  await getRepairingCostData();
  
  const plotData = [
    ...RepairingCostData.value.map(plantData => {
      const xValues = plantData.data.map(entry => entry.month);
      const yValues = plantData.data.map(entry => entry.cost);
      return {
        x: xValues,
        y: yValues,
        type: 'scatter', // 折れ線グラフ
        mode: 'lines+markers',
        name: `${plantData.plant} - Line`
      };
    }),
    ...BarChartData.value.map(plantData => {
      const xValues = plantData.data.map(entry => entry.month);
      const yValues = plantData.data.map(entry => entry.cost);
      return {
        x: xValues,
        y: yValues,
        type: 'bar', // 棒グラフ
        name: `${plantData.plant} - Bar`
      };
    })
  ];

  const layout = {
    height: 500,
    width: 600,
    title: '修理コスト',
    barmode: 'group'
  };

  Plotly.newPlot('rpcPM05', plotData, layout);
});
</script>
