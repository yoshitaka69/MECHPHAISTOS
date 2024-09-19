<template>
  <div class="charts-row">
    <!-- 各チャートコンテナをループで表示 -->
    <div class="chart-container" v-for="(data, index) in chartData" :key="index">
      <!-- Vueのrefを使ってSVG要素にアクセス -->
      <svg :ref="el => chartRefs[index] = el"></svg>
    </div>
  </div>
</template>

<script setup>
import * as d3 from 'd3';
import { onMounted, ref } from 'vue';

// サンプルデータ
const chartData = [
  { label: 'Chart 1', data: [12, 19, 3, 5, 2, 3] },
  { label: 'Chart 2', data: [7, 11, 5, 8, 3, 7] },
  { label: 'Chart 3', data: [3, 5, 2, 3, 12, 19] },
  { label: 'Chart 4', data: [5, 6, 3, 4, 6, 5] }
];

// SVG要素へのリファレンス配列
const chartRefs = ref([]);

// チャート描画の関数
const drawChart = (svg, data) => {
  const margin = { top: 20, right: 20, bottom: 30, left: 40 };
  const width = 400 - margin.left - margin.right; // SVGの幅
  const height = 300 - margin.top - margin.bottom; // SVGの高さ

  // SVGの全体サイズを設定
  svg.attr('viewBox', `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
     .attr('preserveAspectRatio', 'xMinYMin meet')
     .style('width', '100%')
     .style('height', '100%');

  // 描画エリアのグループ要素を追加
  const g = svg.append('g')
               .attr('transform', `translate(${margin.left},${margin.top})`);

  // x軸スケールの設定
  const x = d3.scaleBand()
              .domain(data.map((d, i) => i))
              .range([0, width])
              .padding(0.1);

  // y軸スケールの設定
  const y = d3.scaleLinear()
              .domain([0, d3.max(data)])
              .nice()
              .range([height, 0]);

  // x軸の描画
  g.append('g')
   .attr('class', 'x-axis')
   .attr('transform', `translate(0,${height})`)
   .call(d3.axisBottom(x).tickFormat(i => `Label ${i + 1}`))
   .selectAll('text')
   .style('fill', 'white'); // ラベルを白色に

  // y軸の描画
  g.append('g')
   .attr('class', 'y-axis')
   .call(d3.axisLeft(y).ticks(5))
   .selectAll('text')
   .style('fill', 'white'); // ラベルを白色に

  // バーの描画
  g.selectAll('.bar')
   .data(data)
   .enter().append('rect')
   .attr('class', 'bar')
   .attr('x', (d, i) => x(i))
   .attr('y', d => y(d))
   .attr('width', x.bandwidth())
   .attr('height', d => height - y(d))
   .attr('fill', 'yellow'); // バーの色を黄色に
};

// Vueのライフサイクルフックを使用して、チャート描画を実行
onMounted(() => {
  chartData.forEach((data, index) => {
    // D3でSVGを選択し、描画関数を呼び出し
    const svg = d3.select(chartRefs.value[index]);
    drawChart(svg, data.data);
  });
});
</script>

<style scoped>
.charts-row {
  display: flex;
  justify-content: space-between; /* チャートの間隔を設定 */
  gap: 20px; /* チャート間の隙間を設定 */
}

.chart-container {
  width: 24%; /* 各チャートの幅を設定（横に4つ並べるために約25%） */
  height: 250px; /* 各チャートの高さを設定 */
  background-color: #333; /* 背景色を設定 */
  padding: 10px; /* チャートの内側に余白を設定 */
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

svg {
  width: 100%;
  height: 100%;
}
</style>
