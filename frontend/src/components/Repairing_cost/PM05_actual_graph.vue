<template>
  <div style="width: 100%; height: 100%;">
    PM05 Actual cost
    <div id="rpcPM05" ref="graphContainer" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

const RepairingCostData = ref([]);
const BarChartData = ref([]);
const currentYear = new Date().getFullYear();
const graphContainer = ref(null);

const getRepairingCostData = async () => {
  const userStore = useUserStore();
  const userCompanyCode = userStore.companyCode;
  if (!userCompanyCode) {
    console.error("エラー: ユーザーの会社コードが見つかりません。");
    return;
  }

  const lineUrl = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json&companyCode=${userCompanyCode}`;
  const responseLine = await axios.get(lineUrl);
  const barUrl = `http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/?format=json`;
  const responseBar = await axios.get(barUrl);

  RepairingCostData.value = processData(responseLine.data);
  BarChartData.value = processData(responseBar.data);
};

const processData = (data) => data.flatMap(companyData =>
  companyData.actualPM05List.flatMap(plantData =>
    plantData.actualPM05.map(yearData => ({
      plant: plantData.plant,
      data: extractMonthCosts(yearData)
    }))
  )
);

const extractMonthCosts = (yearData) => {
  const months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "commitment", "totalCost"];
  return months.map(month => ({
    month,
    cost: parseFloat(yearData[month]) || 0
  })).filter(monthData => monthData.cost !== 0);
};

onMounted(async () => {
  await getRepairingCostData();
  nextTick(() => {
    if (graphContainer.value) {
      plotGraph();
      const resizeObserver = new ResizeObserver(plotGraph);
      resizeObserver.observe(graphContainer.value);
    }
  });
});

const plotGraph = () => {
  const plotData = [
    ...RepairingCostData.value.map(data => ({
      x: data.data.map(entry => entry.month),
      y: data.data.map(entry => entry.cost),
      type: 'scatter',
      mode: 'lines+markers',
      name: `${data.plant} - Line`
    })),
    ...BarChartData.value.map(data => ({
      x: data.data.map(entry => entry.month),
      y: data.data.map(entry => entry.cost),
      type: 'bar',
      name: `${data.plant} - Bar`
    }))
  ];

  const layout = {
    height: graphContainer.value.clientHeight,
    width: graphContainer.value.clientWidth,
    title: '修理コスト PM05 実際',
    barmode: 'group'
  };

  Plotly.newPlot('rpcPM05', plotData, layout);
};
</script>
