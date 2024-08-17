<template>
  <div class="main-container">
    <h2>SHAP値の可視化</h2>
    <div class="summary-bar-plot">
      <h3>Summary Plot (Bar Graph)</h3>
      <svg ref="summaryBarPlot"></svg>
    </div>
    <div class="contribution-plot">
      <h3>特徴量の貢献度 vs 目的変数</h3>
      <svg ref="contributionPlot"></svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue'
import * as d3 from 'd3'
import axios from 'axios'

const companyCode = '001-testChemical-001'  // 会社コードを指定
const shapValues = ref({})
const features = ref([])

const summaryBarPlot = ref<SVGSVGElement | null>(null)
const contributionPlot = ref<SVGSVGElement | null>(null)

onMounted(async () => {
  try {
    // DjangoのAPIからSHAP値を取得
    const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/shap_values/?companyCode=${companyCode}`)
    shapValues.value = response.data.shap_values
    features.value = response.data.features

    nextTick(() => {
      drawSummaryBarPlot()
      drawContributionPlot()
    })
  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
})

function drawSummaryBarPlot() {
  const svgEl = d3.select(summaryBarPlot.value)
  const containerWidth = 600
  const containerHeight = 400

  const margin = { top: 20, right: 20, bottom: 50, left: 80 }
  const width = containerWidth - margin.left - margin.right
  const height = containerHeight - margin.top - margin.bottom

  svgEl
    .attr('width', containerWidth)
    .attr('height', containerHeight)

  const group = svgEl.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  // SHAP値の絶対値の平均を計算
  const avgShapValues = features.value.map(feature => ({
    feature,
    value: d3.mean(shapValues.value.map(v => Math.abs(v[feature])))
  }))

  const yScale = d3.scaleBand()
    .domain(avgShapValues.map(d => d.feature))
    .range([height, 0])
    .padding(0.1)

  const xScale = d3.scaleLinear()
    .domain([0, d3.max(avgShapValues, d => d.value)!])
    .range([0, width])

  // バーグラフを描画
  group.selectAll('rect')
    .data(avgShapValues)
    .join('rect')
    .attr('x', 0)
    .attr('y', d => yScale(d.feature)!)
    .attr('width', d => xScale(d.value))
    .attr('height', yScale.bandwidth())
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
    .text('SHAP値 (平均絶対値)')

  group.append('text')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 20)
    .attr('transform', 'rotate(-90)')
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('特徴量')
}

function drawContributionPlot() {
  const svgEl = d3.select(contributionPlot.value)
  const containerWidth = 600
  const containerHeight = 400

  const margin = { top: 20, right: 20, bottom: 50, left: 80 }
  const width = containerWidth - margin.left - margin.right
  const height = containerHeight - margin.top - margin.bottom

  svgEl
    .attr('width', containerWidth)
    .attr('height', containerHeight)

  const group = svgEl.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`)

  const xScale = d3.scaleLinear()
    .domain([d3.min(Object.values(shapValues.value).flat())!, d3.max(Object.values(shapValues.value).flat())!])
    .range([0, width])

  const yScale = d3.scaleLinear()
    .domain([0, 1])  // 目的変数の範囲を適宜設定
    .range([height, 0])

  group.selectAll('circle')
    .data(features.value)
    .join('circle')
    .attr('cx', feature => d3.mean(shapValues.value.map(v => xScale(v[feature])))!)
    .attr('cy', feature => yScale(feature)!)
    .attr('r', 5)
    .style('fill', 'blue')

  group.append('g')
    .attr('transform', `translate(0,${height})`)
    .call(d3.axisBottom(xScale))

  group.append('g')
    .call(d3.axisLeft(yScale))

  group.append('text')
    .attr('x', width / 2)
    .attr('y', height + margin.bottom)
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('SHAP値')

  group.append('text')
    .attr('x', -height / 2)
    .attr('y', -margin.left + 20)
    .attr('transform', 'rotate(-90)')
    .style('text-anchor', 'middle')
    .style('font-size', '12px')
    .text('目的変数')
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

.summary-bar-plot, .contribution-plot {
  margin-bottom: 40px;
}

svg {
  width: 100%;
  height: 400px;
}
</style>
