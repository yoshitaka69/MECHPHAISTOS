<template>
  <div class="heatmap-container">
    <h2>設備停止に関する相関行列ヒートマップ</h2>
    <div class="heatmap-wrapper">
      <svg ref="svg"></svg>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'
import axios from 'axios'

// SVGの参照を定義
const svg = ref<SVGSVGElement | null>(null)
const companyCode = '001-testChemical-001'  // 会社コードを指定（動的に変更可能）

onMounted(async () => {
  try {
    // DjangoのAPIからデータを取得
    const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/correlation/?companyCode=${companyCode}`)
    const data = response.data

    console.log("Fetched data:", data);

    if (!svg.value) return

    const svgEl = d3.select(svg.value)
    const containerWidth = parseInt(d3.select('.heatmap-wrapper').style('width'), 10)
    const containerHeight = parseInt(d3.select('.heatmap-wrapper').style('height'), 10)

    const margin = { top: 150, right: 150, bottom: 100, left: 150 }
    const width = containerWidth - margin.left - margin.right
    const height = containerHeight - margin.top - margin.bottom

    svgEl
      .attr('width', containerWidth)
      .attr('height', containerHeight)
      .style('background', '#fff')

    // すべてのキーをドメインに含める
    const xScale = d3.scaleBand()
      .range([0, width])
      .domain([...new Set(data.map(d => d.x))])
      .padding(0.05)

    const yScale = d3.scaleBand()
      .range([0, height])
      .domain([...new Set(data.map(d => d.y))])
      .padding(0.05)

    console.log("xScale domain:", xScale.domain());
    console.log("yScale domain:", yScale.domain());

    const colorScale = d3.scaleSequential(d3.interpolateRdYlBu)
      .domain([1, -1])

    const group = svgEl.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`)

    group.selectAll()
      .data(data)
      .join('rect')
      .attr('x', d => xScale(d.y))
      .attr('y', d => yScale(d.x))
      .attr('width', xScale.bandwidth())
      .attr('height', yScale.bandwidth())
      .style('fill', d => colorScale(d.value))

    group.selectAll()
      .data(data)
      .join('text')
      .attr('x', d => xScale(d.y)! + xScale.bandwidth() / 2)
      .attr('y', d => yScale(d.x)! + yScale.bandwidth() / 2)
      .attr('dy', '.35em')
      .style('text-anchor', 'middle')
      .style('fill', '#000')
      .style('font-size', '10px')
      .text(d => (d.x === d.y ? '1.0' : d.value.toFixed(1)))

    // ラベルの追加
    group.selectAll('.label-x')
      .data(xScale.domain())
      .join('text')
      .attr('x', d => xScale(d)! + xScale.bandwidth() / 2)
      .attr('y', -10)
      .attr('transform', d => `rotate(-90, ${xScale(d)! + xScale.bandwidth() / 2}, -10)`)
      .style('text-anchor', 'start')
      .style('alignment-baseline', 'baseline')
      .style('font-size', '10px')
      .text(d => d)

    group.selectAll('.label-y')
      .data(yScale.domain())
      .join('text')
      .attr('x', -10)
      .attr('y', d => yScale(d)! + yScale.bandwidth() / 2)
      .style('text-anchor', 'end')
      .attr('dominant-baseline', 'middle')
      .style('font-size', '10px')
      .text(d => d)

    // カラーバーの追加
    const legendWidth = 20
    const legendHeight = height
    const legendX = width + 20
    const legendY = 0

    const legendScale = d3.scaleLinear()
      .domain([1, -1])
      .range([0, legendHeight])

    const legendAxis = d3.axisRight(legendScale)
      .ticks(5)

    const legend = svgEl.append('g')
      .attr('transform', `translate(${margin.left + legendX},${margin.top + legendY})`)

    legend.append('g')
      .selectAll('rect')
      .data(d3.range(-1, 1.1, 0.1))
      .join('rect')
      .attr('x', 0)
      .attr('y', d => legendScale(d)!)
      .attr('width', legendWidth)
      .attr('height', legendHeight / 20)
      .style('fill', d => colorScale(d))

    legend.append('g')
      .attr('transform', `translate(${legendWidth},0)`)
      .call(legendAxis)

  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
})
</script>

<style scoped>
.heatmap-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: white;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.heatmap-wrapper {
  width: 100%;
  max-width: 1000px;
  height: 800px;
}
</style>
