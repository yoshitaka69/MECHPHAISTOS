<template>
  <div style="width: 100%; height: 100%" ref="plotDiv"></div>
  <!-- ref属性を使用し、全画面のスタイルを適用 -->
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore'; // Pinia store のパスを適切に設定してください

const plotDiv = ref(null); // DOM element の ref を作成

onMounted(async () => {
  const userStore = useUserStore();
  const companyCode = userStore.companyCode; // Pinia ストアから companyCode を取得
  const currentYear = new Date().getFullYear(); // 現在の西暦年を取得

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
          const allYValues = []; // 全てのy値を格納するための配列

          const traceData = response.data[0].GapOfRepairingCostList.map((costData) => {
              const x = [];
              const y = [];
              const textPositions = []; // テキストの位置を設定する配列
              Object.keys(costData).forEach((key) => {
                  if (key.startsWith('GapCost')) {
                      const yearsAgo = parseInt(key.match(/GapCostPPM(\d+)?(Ago)?/)[1] || 0);
                      const year = key.includes('Ago') ? currentYear - yearsAgo : currentYear + yearsAgo;
                      const cost = Number(costData[key]);
                      x.push(year);
                      y.push(cost);
                      allYValues.push(cost); // 全てのy値を収集

                      // 値がプラスなら上、マイナスなら下にテキストを表示
                      textPositions.push(cost >= 0 ? 'auto' : 'bottom');
                  }
              });
              return {
                  x: x,
                  y: y,
                  type: 'bar',
                  name: costData.companyCode,
                  text: y, // 値を表示
                  textposition: textPositions // テキストの位置をプラスとマイナスで分ける
              };
          });

          // 全てのy値から最大値と最小値を取得し、それに余力を加える
          const yMax = Math.max(...allYValues) * 1.25; // 最大値に25%の余裕を持たせる
          const yMin = Math.min(...allYValues) * 1.25; // 最小値に25%の余裕を持たせる

          const layout = {
              title: 'Cost Gap Analysis',
              xaxis: {
                  title: {
                      text: 'Year',
                      standoff: 20 // x軸ラベルとグラフの間に隙間を設定
                  },
                  range: [currentYear - 5, currentYear + 10], // 現在の年から5年前〜10年先
                  tickmode: 'linear',
                  dtick: 1,
                  zeroline: true,
                  ticklabelpadding: 30,
                  ticks: '',
                  automargin: true
              },
              yaxis: {
                  title: 'Cost',
                  showline: true,
                  zeroline: true,
                  range: [yMin, yMax], // 最小値・最大値に余力を持たせた範囲を設定
                  automargin: true
              },
              paper_bgcolor: '#e0f7e0', // グラフの外側の領域の背景色を設定
              plot_bgcolor: '#ffffff' // プロット領域の背景色を設定
          };

          const config = {
              displayModeBar: false // 右上の設定を非表示
          };

          Plotly.newPlot(plotDiv.value, traceData, layout, config); // configオプションを追加
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
