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
      const trueValues = this.sampleDataX.filter(x =>
        (x >= -0.1 && x <= 0.1) || // Yellow
        (x >= -0.25 && x <= 0.25) || // Red
        (x >= -0.5 && x <= 0.5) || // Blue
        (x >= -0.75 && x <= 0.75) || // Black
        (x >= -1 && x <= 1) // White
      );

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
  },
};
</script>
