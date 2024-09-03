<template>
  <div class="main-container">
    <h2>PCA（主成分分析）の可視化</h2>
    <div class="pca-scatter-plot">
      <h3>主成分得点プロット</h3>
      <svg ref="pcaScatterPlot"></svg>
    </div>
    <div class="pca-variance-plot">
      <h3>寄与率（バープロット）</h3>
      <svg ref="pcaVariancePlot"></svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue'
import * as d3 from 'd3'
import axios from 'axios'

const companyCode = '001-testChemical-001'  // 会社コードを指定
const pcaScores = ref([])
const explainedVariance = ref([])
const features = ref([])

const pcaScatterPlot = ref<SVGSVGElement | null>(null)
const pcaVariancePlot = ref<SVGSVGElement | null>(null)

onMounted(async () => {
  try {
    // DjangoのAPIからPCA結果を取得
    const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/pca/?companyCode=${companyCode}`)
    pcaScores.value = response.data.pca_scores
    explainedVariance.value = response.data.explained_variance
    features.value = response.data.features

    nextTick(() => {
      drawPCAScatterPlot()
      drawPCAVariancePlot()
    })
  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
})

function drawPCAScatterPlot() {
  const svgEl = d3.select(pcaScatterPlot.value)
  const containerWidth = 600
  const containerHeight = 400

  const margin = { top: 20, right: 20, bottom: 50, left: 60 }
  const width = containerWidth - margin.left - margin.right
  const height = containerHeight - margin.top - margin.bottom

  svgEl
    .attr('width', containerWidth)
    .attr('height', containerHeight)

  const group = svgEl.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  const xScale = d3.scaleLinear()
    .domain(d3.extent(pcaScores.value, d => d.PC1)!)
    .range([0, width])

  const yScale = d3.scaleLinear()
    .domain(d3.extent(pcaScores.value, d => d.PC2)!)
    .range([height, 0])

  // 散布図を描画
  group.selectAll('circle')
    .data(pcaScores.value)
    .join('circle')
    .attr('cx', d => xScale(d.PC1))
    .attr('cy', d => yScale(d.PC2))
    .attr('r', 5)
    .style('fill', '#69b3a2')

  // 軸を描画
  group.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(d3.axisBottom(xScale))

  group.append('g')
    .call(d3.axisLeft(yScale))

  // 軸ラベルを追加
  group.append('text')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom)
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('主成分1 (PC1)')

  group.append('text')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 20)
    .attr('transform', 'rotate(-90)')
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('主成分2 (PC2)')
}

function drawPCAVariancePlot() {
  const svgEl = d3.select(pcaVariancePlot.value)
  const containerWidth = 600
  const containerHeight = 400

  const margin = { top: 20, right: 20, bottom: 50, left: 60 }
  const width = containerWidth - margin.left - margin.right
  const height = containerHeight - margin.top - margin.bottom

  svgEl
    .attr('width', containerWidth)
    .attr('height', containerHeight)

  const group = svgEl.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  const xScale = d3.scaleBand()
    .domain(['PC1', 'PC2'])
    .range([0, width])
    .padding(0.1)

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(explainedVariance.value)!])
    .range([height, 0])

  // バーグラフを描画
  group.selectAll('rect')
    .data(explainedVariance.value)
    .join('rect')
    .attr('x', (_, i) => xScale(`PC${i + 1}`)!)
    .attr('y', d => yScale(d))
    .attr('width', xScale.bandwidth())
    .attr('height', d => height - yScale(d))
    .attr('fill', '#69b3a2')

  // 軸を描画
  group.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(d3.axisBottom(xScale))

  group.append('g')
    .call(d3.axisLeft(yScale))

  // 軸ラベルを追加
  group.append('text')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom)
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('主成分')

  group.append('text')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 20)
    .attr('transform', 'rotate(-90)')
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('寄与率')
}
</script>

<style scoped>
.main-container {
  max-width: 1200px;
  margin: auto;
  background-color: white;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.pca-scatter-plot, .pca-variance-plot {
  margin-top: 20px;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

h3 {
  text-align: center;
  font-size: 16px;
  margin-bottom: 10px;
}
</style>
