<template>
  <div>
    <div ref="targetPlot"></div>
    <div>
      <p>Accuracy: {{ accuracy }}%</p>
      <p>Precision: {{ precision }}%</p>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';

export default {
  name: 'TargetPlot',
  props: ['sampleDataX', 'sampleDataY'],
  data() {
    return {
      accuracy: 0,
      precision: 0,
    };
  },
  mounted() {
    this.renderPlot();
  },
  watch: {
    sampleDataX() {
      this.renderPlot();
    },
    sampleDataY() {
      this.renderPlot();
    },
  },
  methods: {
    renderPlot() {
      const data = [
        {
          x: this.sampleDataX,
          y: this.sampleDataY,
          mode: 'markers',
          type: 'scatter',
          marker: { size: 12, color: 'rgba(31, 119, 180, 0.7)', opacity: 0.8 },
          name: 'Sample Data',
        },
      ];

      const layout = {
        title: 'Target Plot for Precision and Accuracy',
        xaxis: { range: [-1.5, 1.5], zeroline: false, showgrid: false },
        yaxis: { range: [-1.5, 1.5], zeroline: false, showgrid: false },
        shapes: [
          {
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -1,
            y0: -1,
            x1: 1,
            y1: 1,
            fillcolor: 'white',
            line: { color: 'rgba(0, 0, 0, 1)' },
            layer: 'below',
          },
          {
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -0.75,
            y0: -0.75,
            x1: 0.75,
            y1: 0.75,
            fillcolor: 'black',
            line: { color: 'rgba(0, 0, 0, 1)' },
            layer: 'below',
          },
          {
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -0.5,
            y0: -0.5,
            x1: 0.5,
            y1: 0.5,
            fillcolor: 'blue',
            line: { color: 'rgba(0, 0, 0, 1)' },
            layer: 'below',
          },
          {
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -0.25,
            y0: -0.25,
            x1: 0.25,
            y1: 0.25,
            fillcolor: 'red',
            line: { color: 'rgba(0, 0, 0, 1)' },
            layer: 'below',
          },
          {
            type: 'circle',
            xref: 'x',
            yref: 'y',
            x0: -0.1,
            y0: -0.1,
            x1: 0.1,
            y1: 0.1,
            fillcolor: 'yellow',
            line: { color: 'rgba(0, 0, 0, 1)' },
            layer: 'below',
          },
        ],
        width: 600,
        height: 600,
      };

      Plotly.react(this.$refs.targetPlot, data, layout);

      // Calculate Accuracy and Precision
      const meanX = this.sampleDataX.reduce((a, b) => a + b, 0) / this.sampleDataX.length;
      const meanY = this.sampleDataY.reduce((a, b) => a + b, 0) / this.sampleDataY.length;

      const accuracy = 100 - (Math.sqrt(Math.pow(meanX, 2) + Math.pow(meanY, 2)) * 100 / Math.sqrt(2));
      const precision = 100 - (Math.sqrt(this.sampleDataX.map((x, i) => Math.pow(x - meanX, 2)).reduce((a, b) => a + b, 0) / this.sampleDataX.length) * 100);

      this.accuracy = accuracy.toFixed(2);
      this.precision = precision.toFixed(2);
    },
  },
};
</script>
