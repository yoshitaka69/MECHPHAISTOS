<template>
  <div class="main-container">
    <h2>特徴量と故障時間の回帰分析</h2>
    <div class="regression-container">
      <div v-for="feature in features" :key="feature" class="regression-chart">
        <h3>{{ feature }} vs Failure Time</h3>
        <svg :ref="el => featureRefs[feature] = el"></svg>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue'
import * as d3 from 'd3'

// サンプルデータ
const data = [
  { failureTime: 5, MTTR: 1, MTBF: 0.7, MTRF: 0.4, failureCount: 0.8, totalOperatingTime: 0.2, failureType: 0.1, failureMode: 0.5, maintenanceMethod: 0.6, maintenanceFrequency: 0.4, maintenanceImpact: 0.3, failureCause: 0.2, environmentCondition: 0.1, operationalCondition: 0.5, componentCondition: 0.6 },
  { failureTime: 7, MTTR: 0.7, MTBF: 1, MTRF: 0.5, failureCount: 0.6, totalOperatingTime: 0.4, failureType: 0.3, failureMode: 0.6, maintenanceMethod: 0.5, maintenanceFrequency: 0.6, maintenanceImpact: 0.2, failureCause: 0.4, environmentCondition: 0.3, operationalCondition: 0.2, componentCondition: 0.5 },
  { failureTime: 6, MTTR: 0.4, MTBF: 0.5, MTRF: 1, failureCount: 0.3, totalOperatingTime: 0.5, failureType: 0.6, failureMode: 0.4, maintenanceMethod: 0.3, maintenanceFrequency: 0.2, maintenanceImpact: 0.5, failureCause: 0.3, environmentCondition: 0.2, operationalCondition: 0.6, componentCondition: 0.4 },
  { failureTime: 8, MTTR: 0.8, MTBF: 0.6, MTRF: 0.3, failureCount: 1, totalOperatingTime: 0.4, failureType: 0.7, failureMode: 0.3, maintenanceMethod: 0.5, maintenanceFrequency: 0.7, maintenanceImpact: 0.6, failureCause: 0.2, environmentCondition: 0.5, operationalCondition: 0.4, componentCondition: 0.7 },
  { failureTime: 9, MTTR: 0.2, MTBF: 0.2, MTRF: 0.7, failureCount: 0.4, totalOperatingTime: 1, failureType: 0.5, failureMode: 0.8, maintenanceMethod: 0.2, maintenanceFrequency: 0.3, maintenanceImpact: 0.4, failureCause: 0.1, environmentCondition: 0.3, operationalCondition: 0.7, componentCondition: 0.5 }
]

// 特徴量リスト
const features = ['MTTR', 'MTBF', 'MTRF', 'failureCount', 'totalOperatingTime', 'failureType', 'failureMode', 'maintenanceMethod', 'maintenanceFrequency', 'maintenanceImpact', 'failureCause', 'environmentCondition', 'operationalCondition', 'componentCondition']

// 各特徴量に対するSVG参照を保持するオブジェクト
const featureRefs = {} as Record<string, SVGSVGElement | null>

// 各特徴量に対する回帰分析を描画
onMounted(() => {
  nextTick(() => {
    features.forEach(feature => {
      const svgEl = d3.select(featureRefs[feature])
      const containerWidth = 300
      const containerHeight = 200

      // 回帰分析の寸法と余白を設定
      const margin = { top: 20, right: 20, bottom: 40, left: 40 }
      const width = containerWidth - margin.left - margin.right
      const height = containerHeight - margin.top - margin.bottom

      // SVGのサイズを設定
      svgEl
        .attr('width', containerWidth)
        .attr('height', containerHeight)

      const xScale = d3.scaleLinear()
        .domain(d3.extent(data, d => d[feature]) as [number, number])
        .range([0, width])

      const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.failureTime) as number])
        .range([height, 0])

      const group = svgEl.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`)

      // 散布図の点を描画
      group.selectAll('circle')
        .data(data)
        .join('circle')
        .attr('cx', d => xScale(d[feature]))
        .attr('cy', d => yScale(d.failureTime))
        .attr('r', 3)
        .style('fill', '#69b3a2')

      // 回帰直線を描画
      const regression = linearRegression(data.map(d => [d[feature], d.failureTime]))

      const line = d3.line()
        .x(d => xScale(d[0]))
        .y(d => yScale(d[1]))

      group.append('path')
        .datum(regression.points)
        .attr('fill', 'none')
        .attr('stroke', 'red')
        .attr('stroke-width', 2)
        .attr('d', line)

      // 信頼区間の帯を描画
      const ci = confidenceInterval(regression, data.map(d => d[feature]))

      const area = d3.area()
        .x(d => xScale(d[0]))
        .y0(d => yScale(d[1]))
        .y1(d => yScale(d[2]))

      group.append('path')
        .datum(ci.points)
        .attr('fill', 'rgba(255, 0, 0, 0.2)') // 薄い赤色
        .attr('d', area)

      // 信頼区間ラベル
      group.append('text')
        .attr('x', width - 10)
        .attr('y', yScale(ci.points[0][1]) - 5)
        .style('text-anchor', 'end')
        .style('font-size', '10px')
        .style('fill', 'black')
        .text('95%信頼区間')

      // 軸を描画
      group.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(xScale))

      group.append('g')
        .call(d3.axisLeft(yScale))

      // 軸ラベルを追加
      group.append('text')
        .attr('x', width / 2)
        .attr('y', height + margin.bottom - 10)
        .style('text-anchor', 'middle')
        .style('font-size', '12px') 
        .text(feature)

      group.append('text')
        .attr('x', -height / 2)
        .attr('y', -margin.left + 10)
        .attr('transform', 'rotate(-90)')
        .style('text-anchor', 'middle')
        .style('font-size', '12px') 
        .text('Failure Time')
    })
  })
})

// 線形回帰分析を計算する関数
function linearRegression(data: [number, number][]) {
  const n = data.length
  const sumX = data.reduce((acc, val) => acc + val[0], 0)
  const sumY = data.reduce((acc, val) => acc + val[1], 0)
  const sumXY = data.reduce((acc, val) => acc + val[0] * val[1], 0)
  const sumXX = data.reduce((acc, val) => acc + val[0] * val[0], 0)

  const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX)
  const intercept = (sumY - slope * sumX) / n

  const points = data.map(([x]) => [x, slope * x + intercept])

  return { slope, intercept, points }
}

// 信頼区間を計算する関数
function confidenceInterval(regression: { slope: number; intercept: number }, xData: number[]) {
  const n = xData.length
  const meanX = d3.mean(xData)!
  const sumXX = d3.sum(xData, x => Math.pow(x - meanX, 2))

  const xRange = d3.extent(xData) as [number, number]
  const xSeq = d3.range(xRange[0], xRange[1], (xRange[1] - xRange[0]) / 100)

  const tValue = 1.96 // 95% confidence interval for large sample size
  const stderr = d3.deviation(xData.map(x => regression.slope * x + regression.intercept))!

  const ci = xSeq.map(x => {
    const fx = regression.slope * x + regression.intercept
    const marginError = tValue * stderr * Math.sqrt(1 / n + Math.pow(x - meanX, 2) / sumXX)
    return {
      x,
      lower: fx - marginError,
      upper: fx + marginError
    }
  })

  return {
    points: ci.map(d => [d.x, d.lower, d.upper])
  }
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

.regression-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 20px;
}

.regression-chart {
  width: 300px;
  margin-bottom: 30px;
  flex: 0 0 calc(25% - 20px); /* 横に4つ並べるためのサイズ設定 */
}

h3 {
  font-size: 14px; /* グラフタイトルのフォントサイズを小さく */
  margin-bottom: 5px;
}

svg {
  width: 100%;
  height: 200px;
}
</style>
