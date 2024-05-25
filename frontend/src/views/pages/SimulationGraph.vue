<template>
  <div>
    <div class="graphs-container">
      <div id="MonthlyGraph" class="graph"></div>
      <div id="TotalCostGraph" class="graph"></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import Plotly from 'plotly.js-dist-min';

const props = defineProps(['costData']);

const baseData = ref([{ x: [1, 2, 3], y: [1, 4, 2], type: 'scatter', mode: 'lines+markers', name: 'Base Data' }]);
const monthlyData = ref([]);
const totalCostData = ref([]);

const currentYear = new Date().getFullYear();
const years = Array.from({ length: 10 }, (_, i) => currentYear + i);

const monthlyLayout = { 
  title: '月別コストグラフ',
  xaxis: { title: '月', tickvals: Array.from({ length: 12 }, (_, i) => i), ticktext: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] }
};
const totalCostLayout = { 
  title: '総コストグラフ',
  xaxis: { title: '年', tickvals: Array.from({ length: 10 }, (_, i) => i), ticktext: years }
};
const config = { responsive: true };

onMounted(() => {
  Plotly.newPlot('MonthlyGraph', [...baseData.value, ...monthlyData.value], monthlyLayout, config);
  Plotly.newPlot('TotalCostGraph', [...baseData.value, ...totalCostData.value], totalCostLayout, config);
});

watch(
  () => props.costData,
  (newData) => {
    if (newData) {
      const { totalCostData: totalCostRawData, monthlyCostData } = newData;
      monthlyData.value = [
        { x: Array.from({ length: 12 }, (_, i) => i), y: monthlyCostData[0], type: 'bar', name: 'Monthly Cost' }
      ];
      totalCostData.value = [
        { x: Array.from({ length: 10 }, (_, i) => i), y: totalCostRawData[0], type: 'scatter', mode: 'lines+markers', line: { dash: 'dot' }, name: 'Total Cost' }
      ];
      Plotly.react('MonthlyGraph', [...baseData.value, ...monthlyData.value], monthlyLayout, config);
      Plotly.react('TotalCostGraph', [...baseData.value, ...totalCostData.value], totalCostLayout, config);
    }
  },
  { immediate: true }
);
</script>

<style>
.graphs-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.graph {
  width: 48%;
}
</style>
