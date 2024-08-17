<template>
  <div class="main-container">
    <h2>特徴量と故障時間の回帰分析</h2>
    <div class="regression-container">
      <div v-for="(result, feature) in regressionResults" :key="feature" class="regression-chart">
        <h3>{{ feature }} vs Failure Time</h3>
        <svg :ref="el => featureRefs[feature] = el"></svg>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue'
import * as d3 from 'd3'
import axios from 'axios'

const companyCode = '001-testChemical-001'  // 会社コードを指定
const regressionResults = ref({})
const featureRefs = {} as Record<string, SVGSVGElement | null>

onMounted(async () => {
  try {
    // DjangoのAPIから回帰分析データを取得
    const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/regression_analysis/?companyCode=${companyCode}`)
    regressionResults.value = response.data

    nextTick(() => {
      for (const feature in regressionResults.value) {
        const svgEl = d3.select(featureRefs[feature])
        const containerWidth = 300
        const containerHeight = 200

        const margin = { top: 20, right: 20, bottom: 40, left: 40 }
        const width = containerWidth - margin.left - margin.right
        const height = containerHeight - margin.top - margin.bottom

        const xScale = d3.scaleLinear()
          .domain(d3.extent(regressionResults.value[feature].points, d => d[0]) as [number, number])
          .range([0, width])

        const yScale = d3.scaleLinear()
          .domain([0, d3.max(regressionResults.value[feature].points, d => d[1]) as number])
          .range([height, 0])

        const group = svgEl.append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`)

        // 散布図の点を描画
        group.selectAll('circle')
          .data(regressionResults.value[feature].points)
          .join('circle')
          .attr('cx', d => xScale(d[0]))
          .attr('cy', d => yScale(d[1]))
          .attr('r', 3)
          .style('fill', '#69b3a2')

        // 回帰直線を描画
        const line = d3.line()
          .x(d => xScale(d[0]))
          .y(d => yScale(d[1]))

        group.append('path')
          .datum(regressionResults.value[feature].points)
          .attr('fill', 'none')
          .attr('stroke', 'red')
          .attr('stroke-width', 2)
          .attr('d', line)

        // 信頼区間の帯を描画
        const ciLower = regressionResults.value[feature].confidence_interval.lower
        const ciUpper = regressionResults.value[feature].confidence_interval.upper

        const ciArea = d3.area()
          .x((_, i) => xScale(regressionResults.value[feature].points[i][0]))
          .y0((_, i) => yScale(ciLower[i]))
          .y1((_, i) => yScale(ciUpper[i]))

        group.append('path')
          .datum(regressionResults.value[feature].points)
          .attr('fill', 'rgba(255, 0, 0, 0.2)')
          .attr('d', ciArea)

        // 信頼区間ラベル
        group.append('text')
          .attr('x', width - 10)
          .attr('y', yScale(ciUpper[0]) - 5)
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
      }
    })
  } catch (error) {
    console.error('データの取得に失敗しました:', error)
  }
})
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
