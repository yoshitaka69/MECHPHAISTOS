<template>
  <div id="AfterGraph"></div>
  <button @click="applySimulation">シミュレーション適用</button>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import Plotly from 'plotly.js-dist-min';

const baseData = ref([{ x: [1, 2, 3], y: [2, 6, 3], type: 'scatter', mode: 'lines+markers' }]);
const simData = ref([{ x: [1, 2, 3], y: [3, 2, 5], type: 'scatter', mode: 'lines+markers', line: { dash: 'dot' } }]);

const layout = { title: 'ベースとシミュレーションのグラフ' };
const config = { responsive: true };

onMounted(() => {
  Plotly.newPlot('AfterGraph', [...baseData.value, ...simData.value], layout, config);
});

const applySimulation = () => {
  // シミュレーションデータの線スタイルを通常の線に変更
  const updatedSimData = simData.value.map(data => ({
    ...data,
    line: { dash: 'solid' }
  }));
  
  // ベースデータに更新したシミュレーションデータを適用
  baseData.value = [...updatedSimData];
  simData.value = []; // シミュレーションデータをクリア
  Plotly.react('AfterGraph', baseData.value, layout, config);
};
</script>
