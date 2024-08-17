<template>
  <div class="main-container">
    <h2>ランダムフォレストの評価結果</h2>

    <div>
      <h3>トレーニングデータ（サンプル）</h3>
      <pre>{{ trainingData }}</pre>
    </div>

    <div>
      <h3>予測結果（サンプル）</h3>
      <pre>{{ predictions }}</pre>
    </div>

    <div class="importance-chart">
      <h3>特徴量重要度</h3>
      <svg ref="importanceChart"></svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'
import axios from 'axios'

const trainingData = ref(null)
const predictions = ref(null)
const importanceChart = ref<SVGSVGElement | null>(null)
const companyCode = '001-testChemical-001'  // 会社コードを指定

onMounted(async () => {
  try {
    // DjangoのAPIから特徴量重要度データを取得
    const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/feature_importance_details/?companyCode=${companyCode}`)
    const data = response.data

    trainingData.value = data.training_data
    predictions.value = data.predictions
    const featureImportance = data.feature_importance

    if (!importanceChart.value) return

    const svgEl = d3.select(importanceChart.value)
    const containerWidth = 800
    const containerHeight = 400

    const margin = { top: 20, right: 20, bottom: 50, left: 60 }
    const width = containerWidth - margin.left - margin.right
    const height = containerHeight - margin.top - margin.bottom

    svgEl
      .attr('width', containerWidth)
      .attr('height', containerHeight)

    const xScale = d3.scaleBand()
      .domain(featureImportance.map(d => d.feature))
      .range([0, width])
      .padding(0.1)

    const yScale = d3.scaleLinear()
      .domain([0, d3.max(featureImportance, d => d.importance) as number])
      .range([height, 0])

    const group = svgEl.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`)

    // 棒グラフを描画
    group.selectAll('rect')
      .data(featureImportance)
      .join('rect')
      .attr('x', d => xScale(d.feature)!)
      .attr('y', d => yScale(d.importance))
      .attr('width', xScale.bandwidth())
      .attr('height', d => height - yScale(d.importance))
      .attr('fill', '#69b3a2')

    // 軸を描画
    group.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(xScale))
      .selectAll('text')
      .attr('transform', 'rotate(-45)')
      .style('text-anchor', 'end')

    group.append('g')
      .call(d3.axisLeft(yScale))

    // 軸ラベルを追加
    svgEl.append('text')
      .attr('x', width / 2 + margin.left)
      .attr('y', height + margin.top + margin.bottom - 10)
      .style('text-anchor', 'middle')
      .style('font-size', '12px')
      .text('Features')

    svgEl.append('text')
      .attr('x', -height / 2)
      .attr('y', margin.left - 50)
      .attr('transform', 'rotate(-90)')
      .style('text-anchor', 'middle')
      .style('font-size', '12px')
      .text('Importance')
  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
})
</script>

<style scoped>
.main-container {
  max-width: 900px;
  margin: auto;
  background-color: white;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.importance-chart {
  width: 100%;
  height: 400px;
}

pre {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
</style>
