<template>
    <div class="plot-container">
      <div ref="targetPlot" class="plot"></div>
      <div ref="histogram" class="plot"></div>
      <div>
        <p>Accuracy: {{ accuracy }}%</p>
        <p>Precision: {{ precision }}%</p>
      </div>
    </div>
  </template>
  
  <script>
  import Plotly from 'plotly.js-dist-min';
  
  export default {
    name: 'CombinedPlot',
    data() {
      return {
        sampleDataX: [],
        sampleDataY: [],
        accuracy: 0,
        precision: 0,
      };
    },
    mounted() {
      this.generateSampleData();
      this.renderPlots();
    },
    watch: {
      sampleDataX() {
        this.renderPlots();
      },
      sampleDataY() {
        this.renderPlots();
      },
    },
    methods: {
      generateSampleData() {
        console.log('Generating sample data');
        this.sampleDataX = Array.from({ length: 100 }, () => Math.random() * 30 - 15);
        this.sampleDataY = Array.from({ length: 100 }, () => Math.random() * 30 - 15);
        console.log('Sample data generated:', this.sampleDataX, this.sampleDataY);
      },
      renderPlots() {
        console.log('Rendering plots');
        this.renderTargetPlot();
        this.renderHistogram();
      },
      renderTargetPlot() {
        console.log('Rendering target plot with data:', this.sampleDataX, this.sampleDataY);
        const targetPlotData = [
          {
            x: this.sampleDataX,
            y: this.sampleDataY,
            mode: 'markers',
            type: 'scatter',
            marker: { size: 12, color: 'rgba(31, 119, 180, 0.3)', opacity: 0.8 },
            name: 'Sample Data',
          },
        ];
  
        const targetPlotLayout = {
          title: 'Target Plot for Precision and Accuracy',
          xaxis: { range: [-15, 15], dtick: 1, zeroline: true, showgrid: false, tick0: 0 },
          yaxis: { range: [-15, 15], dtick: 1, zeroline: true, showgrid: false, tick0: 0 },
          shapes: [
            { type: 'circle', xref: 'x', yref: 'y', x0: -15, y0: -15, x1: 15, y1: 15, fillcolor: 'rgba(255, 255, 255, 0.3)', line: { color: 'rgba(0, 0, 0, 0.3)' }, layer: 'below' },
            { type: 'circle', xref: 'x', yref: 'y', x0: -7.5, y0: -7.5, x1: 7.5, y1: 7.5, fillcolor: 'rgba(0, 0, 0, 0.3)', line: { color: 'rgba(0, 0, 0, 0.3)' }, layer: 'below' },
            { type: 'circle', xref: 'x', yref: 'y', x0: -5, y0: -5, x1: 5, y1: 5, fillcolor: 'rgba(0, 0, 255, 0.3)', line: { color: 'rgba(0, 0, 0, 0.3)' }, layer: 'below' },
            { type: 'circle', xref: 'x', yref: 'y', x0: -2.5, y0: -2.5, x1: 2.5, y1: 2.5, fillcolor: 'rgba(255, 0, 0, 0.3)', line: { color: 'rgba(0, 0, 0, 0.3)' }, layer: 'below' },
            { type: 'circle', xref: 'x', yref: 'y', x0: -1, y0: -1, x1: 1, y1: 1, fillcolor: 'rgba(255, 255, 0, 0.3)', line: { color: 'rgba(0, 0, 0, 0.3)' }, layer: 'below' },
          ],
          width: 800,
          height: 800,
        };
  
        Plotly.react(this.$refs.targetPlot, targetPlotData, targetPlotLayout);
  
        // Calculate Accuracy and Precision
        const meanX = this.sampleDataX.reduce((a, b) => a + b, 0) / this.sampleDataX.length;
        const meanY = this.sampleDataY.reduce((a, b) => a + b, 0) / this.sampleDataY.length;
  
        const accuracy = 100 - (Math.sqrt(Math.pow(meanX, 2) + Math.pow(meanY, 2)) * 100 / Math.sqrt(2));
        const precision = 100 - (Math.sqrt(this.sampleDataX.map((x, i) => Math.pow(x - meanX, 2)).reduce((a, b) => a + b, 0) / this.sampleDataX.length) * 100);
  
        this.accuracy = accuracy.toFixed(2);
        this.precision = precision.toFixed(2);
      },
      renderHistogram() {
        console.log('Rendering histogram with data:', this.sampleDataX);
        const sampleDataCount = this.sampleDataX.length;
        const trueValues = this.generateTrueValues(sampleDataCount);
  
        console.log('True values:', trueValues);
  
        const histogramData = [
          {
            x: this.sampleDataX,
            type: 'histogram',
            opacity: 0.6,
            marker: { color: 'rgba(31, 119, 180, 0.3)' },
            name: 'Sample Data',
            nbinsx: 40,
          },
          {
            x: trueValues,
            type: 'histogram',
            opacity: 0.4,
            marker: { color: 'rgba(255, 99, 71, 0.3)' },
            name: 'True Values',
            nbinsx: 40,
          },
        ];
  
        const histogramX = [];
        const histogramY = [];
        const binSize = 30 / 40;
  
        for (let i = -15; i <= 15; i += binSize) {
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
            line: { shape: 'spline', color: 'rgba(31, 119, 180, 1)' },
          },
        ];
  
        console.log('Histogram line data:', lineData);
  
        const histogramPlotData = histogramData.concat(lineData);
  
        const histogramPlotLayout = {
          title: 'Precision and Accuracy Histogram',
          barmode: 'overlay',
          xaxis: { title: 'Values', range: [-15, 15], dtick: 1, zeroline: true, showgrid: false, tick0: 0 },
          yaxis: { title: 'Frequency', rangemode: 'tozero', dtick: 1, zeroline: true, showgrid: false, tick0: 0 },
          legend: { x: 1, y: 1, xanchor: 'right', yanchor: 'top' },
          width: 800,
          height: 400,
        };
  
        Plotly.react(this.$refs.histogram, histogramPlotData, histogramPlotLayout);
      },
      generateTrueValues(count) {
        const mean = 0;
        const stdDev = 5;
        const trueValues = [];
  
        for (let i = 0; i < count; i++) {
          let value;
          do {
            value = this.randomNormal(mean, stdDev);
          } while (value < -15 || value > 15);
          trueValues.push(value);
        }
  
        return trueValues;
      },
      randomNormal(mean, stdDev) {
        let u = 0, v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        let num = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
        num = num * stdDev + mean;
        return num;
      },
    },
  };
  </script>
  
  <style>
  .plot-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .plot {
    width: 800px;
  }
  </style>
  