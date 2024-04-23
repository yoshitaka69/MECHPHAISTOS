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

  // API からデータを取得
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/gapOfRepairingCostByCompany/?format=json`, {
      params: { companyCode }
    });
    if (response.data && response.data.length > 0) {
      const traceData = response.data[0].GapOfRepairingCostList.map(costData => ({
        x: Object.keys(costData).filter(key => key.startsWith('GapCost')),
        y: Object.values(costData).filter((value, index) => index > 4 && typeof value === 'string').map(Number),
        type: 'bar',
        name: costData.companyCode
      }));
      const layout = {
        title: 'Cost Gap Analysis',
        xaxis: {title: 'Period'},
        yaxis: {title: 'Cost'}
      };
      Plotly.newPlot(plotDiv.value, traceData, layout);  // refの.valueを使用してDOM要素を指定
    }
  } catch (error) {
    console.error('API request failed:', error);
  }
});
</script>

<style>
/* スタイルは必要に応じて */
</style>
