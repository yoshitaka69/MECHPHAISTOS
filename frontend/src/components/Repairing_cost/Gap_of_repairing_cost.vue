<template>
  <div style="width: 100%; height: 100%;" ref="plotDiv"></div> <!-- ref属性を使用し、全画面のスタイルを適用 -->
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
  const debounce = (func, delay) => {
  let timerId;
  return (...args) => {
    if (timerId) {
      clearTimeout(timerId);
    }
    timerId = setTimeout(() => {
      func(...args);
      timerId = null;
    }, delay);
  };
};

const debouncedDrawChart = debounce(() => {
  Plotly.Plots.resize(plotDiv.value);
}, 100); // 100ミリ秒のデバウンス時間


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
          range: [2019, 2034],
          tickmode: 'linear',
          dtick: 1
        },
        yaxis: {title: 'Cost'}
      };
      Plotly.newPlot(plotDiv.value, traceData, layout);
      watchResize();
    }
  } catch (error) {
    console.error('API request failed:', error);
  }
});

// Resize observer to handle chart resizing
const watchResize = () => {
  const resizeObserver = new ResizeObserver(() => {
    Plotly.Plots.resize(plotDiv.value);
  });
  resizeObserver.observe(plotDiv.value);
};
</script>
