<template>
    <div class="main-container">
      <h2>特徴量重要度の評価（ランダムフォレスト）</h2>
      <div class="importance-chart">
        <svg ref="importanceChart"></svg>
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref, onMounted } from 'vue'
  import * as d3 from 'd3'
  // ml5はブラウザ上での動作を想定しているため、npmパッケージが動作しない場合はCDNを利用する
  // import ml5 from 'ml5'  // ローカルでの利用が可能な場合
  import 'https://cdn.jsdelivr.net/npm/ml5@0.6.0/dist/ml5.min.js'
  
  // サンプルデータ（単純化）
  const data = [
    { failureTime: 5, MTTR: 1, MTBF: 0.7, MTRF: 0.4 },
    { failureTime: 7, MTTR: 0.7, MTBF: 1, MTRF: 0.5 },
    { failureTime: 6, MTTR: 0.4, MTBF: 0.5, MTRF: 1 },
    { failureTime: 8, MTTR: 0.8, MTBF: 0.6, MTRF: 0.3 },
    { failureTime: 9, MTTR: 0.2, MTBF: 0.2, MTRF: 0.7 }
  ]
  
  // 特徴量とターゲット変数の分離
  const features = ['MTTR', 'MTBF', 'MTRF']
  
  // 各データポイントの特徴量とターゲット変数を抽出
  const featureData = data.map(d => features.map(f => d[f]))
  const targetData = data.map(d => d.failureTime)
  
  const importanceChart = ref<SVGSVGElement | null>(null)
  
  onMounted(() => {
    try {
      // 特徴量データとターゲットデータの形状を確認
      console.log("Feature Data Shape: ", featureData.length, featureData[0].length)
      console.log("Target Data Length: ", targetData.length)
      console.log("Feature Data Content: ", featureData)
      console.log("Target Data Content: ", targetData)
  
      // ランダムフォレストの代わりに、単純なニューラルネットワークを使用
      const options = {
        inputs: features.length,
        outputs: 1,
        task: 'regression',
        debug: true
      }
  
      const nn = ml5.neuralNetwork(options)
  
      // データの追加
      featureData.forEach((features, i) => {
        nn.addData(features, [targetData[i]])
      })
  
      // データを正規化
      nn.normalizeData()
  
      // モデルのトレーニング
      nn.train({ epochs: 100 }, () => {
        // 訓練完了後に特徴量重要度を推定
        nn.predict(featureData, (err, results) => {
          if (err) {
            console.error(err)
            return
          }
          // ダミーでの重要度の計算例（実際には実装が必要）
          const importances = features.map(() => Math.random())
  
          console.log("Importances: ", importances)
  
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
            .domain(features)
            .range([0, width])
            .padding(0.1)
  
          const yScale = d3.scaleLinear()
            .domain([0, d3.max(importances) as number])
            .range([height, 0])
  
          const group = svgEl.append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`)
  
          // 棒グラフを描画
          group.selectAll('rect')
            .data(importances)
            .join('rect')
            .attr('x', (_, i) => xScale(features[i])!)
            .attr('y', d => yScale(d))
            .attr('width', xScale.bandwidth())
            .attr('height', d => height - yScale(d))
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
        })
      })
    } catch (error) {
      console.error("Error in RandomForestRegression:", error)
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
  </style>
  