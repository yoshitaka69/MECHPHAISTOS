<template>
  <div ref="histogram"></div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';

export default {
  name: 'Histogram',
  props: ['sampleDataX'],
  mounted() {
    this.renderPlot();
  },
  watch: {
    sampleDataX() {
      this.renderPlot();
    },
  },
  methods: {
    renderPlot() {
      // サンプルデータの総数を取得
      const sampleDataCount = this.sampleDataX.length;

      // 理想的な指標データ（正規分布に基づくデータ）を生成
      const trueValues = this.generateTrueValues(sampleDataCount);

      const histogramData = [
        {
          x: this.sampleDataX,
          type: 'histogram',
          opacity: 0.6,
          marker: {
            color: 'rgba(31, 119, 180, 0.7)',
          },
          name: 'Sample Data',
          nbinsx: 40, // ビンの数を増やしてバーを細くする
        },
        {
          x: trueValues,
          type: 'histogram',
          opacity: 0.4,
          marker: {
            color: 'rgba(255, 99, 71, 0.6)',
          },
          name: 'True Values',
          nbinsx: 40, // ビンの数を増やしてバーを細くする
        },
      ];

      // カーブ用のデータを計算
      const histogramX = [];
      const histogramY = [];
      const binSize = (3) / 40; // -1.5から1.5までを40ビンに分割

      for (let i = -1.5; i <= 1.5; i += binSize) {
        histogramX.push(i);
        const count = this.sampleDataX.filter(x => x >= i && x < i + binSize).length;
        histogramY.push(count);
      }

      const lineData = [
        {
          x: histogramX,
          y: histogramY,
          mode: 'lines',
          name: 'Line',
          line: { shape: 'spline', color: 'rgba(31, 119, 180, 1)' }
        }
      ];

      const data = histogramData.concat(lineData);

      const layout = {
        title: 'Precision and Accuracy Histogram',
        barmode: 'overlay',
        xaxis: { title: 'Values', range: [-1.5, 1.5] },
        yaxis: { title: 'Frequency' },
      };

      Plotly.react(this.$refs.histogram, data, layout);
    },
    generateTrueValues(count) {
      // 理想的な正規分布データを生成
      const mean = 0; // 平均
      const stdDev = 0.3; // 標準偏差
      const trueValues = [];

      for (let i = 0; i < count; i++) {
        let value;
        do {
          value = this.randomNormal(mean, stdDev);
        } while (value < -1.5 || value > 1.5); // -1.5から1.5の範囲内に収める
        trueValues.push(value);
      }

      return trueValues;
    },
    randomNormal(mean, stdDev) {
      let u = 0, v = 0;
      while (u === 0) u = Math.random(); // Converting [0,1) to (0,1)
      while (v === 0) v = Math.random();
      let num = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
      num = num * stdDev + mean; // Transform to the desired mean and standard deviation
      return num;
    }
  },
};
</script>
