<template>
  <div class="main-container">
    <h2>PCA プロット</h2>
    <div class="pca-chart">
      <svg ref="pcaChart"></svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'
import { PCA } from 'ml-pca' // 修正: 名前付きインポートを使用

// サンプルデータ
const sampleData = [
  [2.5, 2.4, 3.2],
  [0.5, 0.7, 0.8],
  [2.2, 2.9, 3.1],
  [1.9, 2.2, 2.8],
  [3.1, 3.0, 3.7],
  [2.3, 2.7, 3.4],
  [2, 1.6, 2.5],
  [1, 1.1, 1.2],
  [1.5, 1.6, 1.8],
  [1.1, 0.9, 1.4]
]

// PCA の実行
const pca = new PCA(sampleData)
const scores = pca.predict(sampleData, { nComponents: 2 }).to2DArray()

const pcaChart = ref<SVGSVGElement | null>(null)

onMounted(() => {
  if (!pcaChart.value) return

  const svgEl = d3.select(pcaChart.value)
  const containerWidth = 500
  const containerHeight = 500
  const margin = { top: 20, right: 20, bottom: 50, left: 50 }
  const width = containerWidth - margin.left - margin.right
  const height = containerHeight - margin.top - margin.bottom

  svgEl.attr('width', containerWidth).attr('height', containerHeight)

  const xScale = d3.scaleLinear()
    .domain(d3.extent(scores, d => d[0]) as [number, number])
    .range([0, width])

  const yScale = d3.scaleLinear()
    .domain(d3.extent(scores, d => d[1]) as [number, number])
    .range([height, 0])

  const group = svgEl.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

  // 散布図の描画
  group.selectAll('circle')
    .data(scores)
    .join('circle')
    .attr('cx', d => xScale(d[0]))
    .attr('cy', d => yScale(d[1]))
    .attr('r', 5)
    .attr('fill', '#1f77b4')

  // 軸の描画
  group.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(d3.axisBottom(xScale))

  group.append('g')
    .call(d3.axisLeft(yScale))

  // 軸ラベルの追加
  svgEl.append('text')
    .attr('x', width / 2 + margin.left)
    .attr('y', height + margin.top + margin.bottom - 10)
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('PC1')

  svgEl.append('text')
    .attr('x', -height / 2)
    .attr('y', margin.left - 30)
    .attr('transform', 'rotate(-90)')
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('PC2')
})
</script>

<style scoped>
.main-container {
  max-width: 600px;
  margin: auto;
  background-color: white;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pca-chart {
  width: 100%;
  height: 500px;
}
</style>
