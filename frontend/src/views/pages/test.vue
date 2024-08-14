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
  
  // サンプルデータ（設備停止の指標間の相関）
  const data = [
    { x: 'MTTR', MTTR: 1, MTBF: -0.7, MTRF: 0.4, failureCount: 0.8, totalOperatingTime: 0.2, failureType: 0.1, failureMode: 0.5, maintenanceMethod: 0.6, maintenanceFrequency: 0.4, maintenanceImpact: 0.3, failureCause: 0.2, environmentCondition: 0.1, operationalCondition: 0.5, componentCondition: 0.6 },
    { x: 'MTBF', MTTR: -0.7, MTBF: 1, MTRF: -0.5, failureCount: -0.6, totalOperatingTime: -0.2, failureType: -0.4, failureMode: -0.3, maintenanceMethod: -0.5, maintenanceFrequency: -0.4, maintenanceImpact: -0.2, failureCause: -0.6, environmentCondition: -0.7, operationalCondition: -0.1, componentCondition: -0.5 },
    { x: 'MTRF', MTTR: 0.4, MTBF: -0.5, MTRF: 1, failureCount: 0.3, totalOperatingTime: 0.7, failureType: 0.2, failureMode: 0.3, maintenanceMethod: 0.1, maintenanceFrequency: 0.2, maintenanceImpact: 0.4, failureCause: 0.5, environmentCondition: 0.2, operationalCondition: 0.3, componentCondition: 0.6 },
    { x: 'failureCount', MTTR: 0.8, MTBF: -0.6, MTRF: 0.3, failureCount: 1, totalOperatingTime: 0.4, failureType: 0.5, failureMode: 0.7, maintenanceMethod: 0.6, maintenanceFrequency: 0.8, maintenanceImpact: 0.9, failureCause: 0.1, environmentCondition: 0.3, operationalCondition: 0.2, componentCondition: 0.4 },
    { x: 'totalOperatingTime', MTTR: 0.2, MTBF: -0.2, MTRF: 0.7, failureCount: 0.4, totalOperatingTime: 1, failureType: 0.6, failureMode: 0.5, maintenanceMethod: 0.3, maintenanceFrequency: 0.4, maintenanceImpact: 0.5, failureCause: 0.7, environmentCondition: 0.2, operationalCondition: 0.1, componentCondition: 0.6 },
    { x: 'failureType', MTTR: 0.1, MTBF: -0.4, MTRF: 0.2, failureCount: 0.5, totalOperatingTime: 0.6, failureType: 1, failureMode: 0.3, maintenanceMethod: 0.4, maintenanceFrequency: 0.3, maintenanceImpact: 0.2, failureCause: 0.4, environmentCondition: 0.5, operationalCondition: 0.1, componentCondition: 0.3 },
    { x: 'failureMode', MTTR: 0.5, MTBF: -0.3, MTRF: 0.3, failureCount: 0.7, totalOperatingTime: 0.5, failureType: 0.3, failureMode: 1, maintenanceMethod: 0.6, maintenanceFrequency: 0.7, maintenanceImpact: 0.2, failureCause: 0.1, environmentCondition: 0.3, operationalCondition: 0.4, componentCondition: 0.2 },
    { x: 'maintenanceMethod', MTTR: 0.6, MTBF: -0.5, MTRF: 0.1, failureCount: 0.6, totalOperatingTime: 0.3, failureType: 0.4, failureMode: 0.6, maintenanceMethod: 1, maintenanceFrequency: 0.2, maintenanceImpact: 0.3, failureCause: 0.2, environmentCondition: 0.4, operationalCondition: 0.5, componentCondition: 0.7 },
    { x: 'maintenanceFrequency', MTTR: 0.4, MTBF: -0.4, MTRF: 0.2, failureCount: 0.8, totalOperatingTime: 0.4, failureType: 0.3, failureMode: 0.7, maintenanceMethod: 0.2, maintenanceFrequency: 1, maintenanceImpact: 0.6, failureCause: 0.5, environmentCondition: 0.7, operationalCondition: 0.6, componentCondition: 0.1 },
    { x: 'maintenanceImpact', MTTR: 0.3, MTBF: -0.2, MTRF: 0.4, failureCount: 0.9, totalOperatingTime: 0.5, failureType: 0.2, failureMode: 0.2, maintenanceMethod: 0.3, maintenanceFrequency: 0.6, maintenanceImpact: 1, failureCause: 0.4, environmentCondition: 0.6, operationalCondition: 0.5, componentCondition: 0.3 },
    { x: 'failureCause', MTTR: 0.2, MTBF: -0.6, MTRF: 0.5, failureCount: 0.1, totalOperatingTime: 0.7, failureType: 0.4, failureMode: 0.1, maintenanceMethod: 0.2, maintenanceFrequency: 0.5, maintenanceImpact: 0.4, failureCause: 1, environmentCondition: 0.3, operationalCondition: 0.2, componentCondition: 0.5 },
    { x: 'environmentCondition', MTTR: 0.1, MTBF: -0.7, MTRF: 0.2, failureCount: 0.3, totalOperatingTime: 0.2, failureType: 0.5, failureMode: 0.3, maintenanceMethod: 0.4, maintenanceFrequency: 0.7, maintenanceImpact: 0.6, failureCause: 0.3, environmentCondition: 1, operationalCondition: 0.4, componentCondition: 0.6 },
    { x: 'operationalCondition', MTTR: 0.5, MTBF: -0.1, MTRF: 0.3, failureCount: 0.2, totalOperatingTime: 0.1, failureType: 0.1, failureMode: 0.4, maintenanceMethod: 0.5, maintenanceFrequency: 0.6, maintenanceImpact: 0.5, failureCause: 0.2, environmentCondition: 0.4, operationalCondition: 1, componentCondition: 0.7 },
    { x: 'componentCondition', MTTR: 0.6, MTBF: -0.5, MTRF: 0.6, failureCount: 0.4, totalOperatingTime: 0.6, failureType: 0.3, failureMode: 0.2, maintenanceMethod: 0.7, maintenanceFrequency: 0.1, maintenanceImpact: 0.3, failureCause: 0.5, environmentCondition: 0.6, operationalCondition: 0.7, componentCondition: 1 },
  ]
  
  // SVGの参照を定義
  const svg = ref<SVGSVGElement | null>(null)
  
  // コンポーネントがマウントされたときにヒートマップを描画
  onMounted(() => {
    if (!svg.value) return
  
    const svgEl = d3.select(svg.value)
    const containerWidth = parseInt(d3.select('.heatmap-wrapper').style('width'), 10)
    const containerHeight = parseInt(d3.select('.heatmap-wrapper').style('height'), 10)
  
    // ヒートマップの寸法と余白を設定
    const margin = { top: 150, right: 150, bottom: 100, left: 150 }
    const width = containerWidth - margin.left - margin.right
    const height = containerHeight - margin.top - margin.bottom
  
    // SVGのサイズを設定
    svgEl
      .attr('width', containerWidth)
      .attr('height', containerHeight)
      .style('background', '#fff')
  
    // スケールを作成
    const xScale = d3.scaleBand()
      .range([0, width])
      .domain(data.map(d => d.x))
      .padding(0.05)
  
    const yScale = d3.scaleBand()
      .range([0, height])
      .domain(data.map(d => d.x))
      .padding(0.05)
  
    // カラースケールを定義（相関が高いほど淡い赤く、低いほど青く）
    const colorScale = d3.scaleSequential(d3.interpolateRdYlBu)
      .domain([1, -1]) // 高い相関が淡い赤、低い相関が青
  
    // ヒートマップを作成
    const group = svgEl.append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`)
  
    const cellData = data.flatMap(row =>
      Object.entries(row)
        .filter(([key]) => key !== 'x')
        .map(([key, value]) => ({ x: row.x, y: key, value }))
    )
  
    group.selectAll()
      .data(cellData)
      .join('rect')
      .attr('x', d => xScale(d.y)!)
      .attr('y', d => yScale(d.x)!)
      .attr('width', xScale.bandwidth())
      .attr('height', yScale.bandwidth())
      .style('fill', d => colorScale(d.value))
  
    // 各セルに数値を表示
    group.selectAll()
      .data(cellData)
      .join('text')
      .attr('x', d => xScale(d.y)! + xScale.bandwidth() / 2)
      .attr('y', d => yScale(d.x)! + yScale.bandwidth() / 2)
      .attr('dy', '.35em')
      .style('text-anchor', 'middle')
      .style('fill', '#000')
      .style('font-size', '10px')
      .text(d => (d.x === d.y ? '' : d.value.toFixed(1))) // 対角線のセルにはテキストを表示しない
  
    // ラベルを追加（垂直表示、下を基準に開始）
    group.selectAll('.label-x')
      .data(data.map(d => d.x))
      .join('text')
      .attr('x', d => xScale(d)! + xScale.bandwidth() / 2)
      .attr('y', -10) // ラベルを下から揃えて配置
      .attr('transform', d => `rotate(-90, ${xScale(d)! + xScale.bandwidth() / 2}, -10)`)
      .style('text-anchor', 'start')
      .style('alignment-baseline', 'baseline')
      .style('font-size', '10px')
      .text(d => d)
  
    group.selectAll('.label-y')
      .data(data.map(d => d.x))
      .join('text')
      .attr('x', -10)
      .attr('y', d => yScale(d)! + yScale.bandwidth() / 2)
      .style('text-anchor', 'end')
      .attr('dominant-baseline', 'middle')
      .style('font-size', '10px')
      .text(d => d)
  
    // カラーバーを追加
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
  