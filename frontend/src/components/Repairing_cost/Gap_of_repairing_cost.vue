<template>
  <div ref="plotDiv"></div> <!-- ref属性を追加 -->
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore';  // Pinia store のパスを適切に設定してください

const plotDiv = ref(null);  // DOM element の ref を作成

onMounted(async () => {
  const userStore = useUserStore();
  const companyCode = userStore.companyCode;  // Pinia ストアから companyCode を取得
  const currentYear = new Date().getFullYear();  // 現在の西暦年を取得

  // API からデータを取得
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/gapOfRepairingCostByCompany/?format=json`, {
      params: { companyCode }
    });
    if (response.data && response.data.length > 0) {
      const traceData = response.data[0].GapOfRepairingCostList.map(costData => {
        const x = [];
        const y = [];
        Object.keys(costData).forEach(key => {
          if (key.startsWith('GapCost')) {
            const yearsAgo = parseInt(key.match(/GapCostPPM(\d+)?(Ago)?/)[1] || 0);
            const year = key.includes('Ago') ? currentYear - yearsAgo : currentYear + yearsAgo;
            x.push(year);
            y.push(Number(costData[key]));
          }
        });
        return {
          x: x,
          y: y,
          type: 'bar',
          name: costData.companyCode
        };
      });
      const layout = {
        title: 'Cost Gap Analysis',
        xaxis: {
          title: 'Year',
          range: [2019, 2034],  // X軸の範囲を2019年から2034年に設定
          tickmode: 'linear',
          dtick: 1  // 1年ごとに目盛りを設定
        },
        yaxis: {title: 'Cost'}
      };
      Plotly.newPlot(plotDiv.value, traceData, layout);
    }
  } catch (error) {
    console.error('API request failed:', error);
  }
});
</script>

<style>
/* スタイルは必要に応じて */
</style>
