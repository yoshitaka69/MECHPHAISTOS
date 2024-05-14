<template>
    <div>
      <div ref="chart"></div>
    </div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  
  export default {
    name: 'ToneCurve',
    data() {
      return {
        data: [
          { x: 0, y: 0 },
          { x: 150, y: 150 },
          { x: 255, y: 255 }
        ],
        controlPoint: { x: 150, y: 150 },
        riskMatrix: [
          { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'H', 'VH', 'VH'] },
          { likelihood: 4, description: 'It will probably happen', risk: ['M', 'M', 'H', 'VH', 'VH'] },
          { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'M', 'M', 'H', 'H'] },
          { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'M', 'M', 'H'] },
          { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'M', 'M'] },
        ],
        riskClasses: ['Near Miss', 'Minor Inquiry', 'Lost Time Accident', 'Major Inquiry', 'Fatality']
      };
    },
    mounted() {
      this.drawChart();
    },
    methods: {
      drawChart() {
        const margin = { top: 20, right: 20, bottom: 30, left: 40 };
        const width = 500 - margin.left - margin.right;
        const height = 400 - margin.top - margin.bottom;
  
        const svg = d3.select(this.$refs.chart)
          .append('svg')
          .attr('width', width + margin.left + margin.right)
          .attr('height', height + margin.top + margin.bottom)
          .append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`);
  
        const x = d3.scaleLinear().domain([0, 255]).range([0, width]);
        const y = d3.scaleLinear().domain([0, 255]).range([height, 0]);
  
        const colorScale = d3.scaleLinear()
          .domain([0, 127, 255])
          .range(['green', 'yellow', 'red']);
  
        const updateRiskMatrixColors = () => {
          // グラデーションの更新ロジック
          this.riskMatrix.forEach((row, i) => {
            row.risk = row.risk.map((risk, j) => {
              const intensity = (j * 51 + i * 51) / 2;
              return colorScale(intensity);
            });
          });
        };
  
        const drawRiskMatrix = () => {
          svg.selectAll('.risk-cell').remove();
  
          const cellWidth = width / 5;
          const cellHeight = height / 5;
  
          this.riskMatrix.forEach((row, i) => {
            row.risk.forEach((risk, j) => {
              svg.append('rect')
                .attr('x', j * cellWidth)
                .attr('y', i * cellHeight)
                .attr('width', cellWidth)
                .attr('height', cellHeight)
                .attr('fill', risk)
                .attr('stroke', '#000')
                .attr('stroke-width', 1)
                .attr('class', 'risk-cell');
            });
          });
        };
  
        const line = d3.line()
          .x(d => x(d.x))
          .y(d => y(d.y))
          .curve(d3.curveBasis);
  
        const updateChart = () => {
          svg.selectAll('.line-path').remove();
          svg.selectAll('.axis').remove();
          svg.selectAll('.control-point').remove();
  
          updateRiskMatrixColors();
          drawRiskMatrix();
  
          const dataWithControl = [
            this.data[0],
            this.controlPoint,
            this.data[2]
          ];
  
          svg.append('path')
            .datum(dataWithControl)
            .attr('class', 'line-path')
            .attr('fill', 'none')
            .attr('stroke', 'steelblue')
            .attr('stroke-width', 1.5)
            .attr('d', line);
  
          svg.append('g')
            .attr('class', 'axis')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x));
  
          svg.append('g')
            .attr('class', 'axis')
            .call(d3.axisLeft(y));
  
          svg.selectAll('circle')
            .data([this.controlPoint])
            .enter()
            .append('circle')
            .attr('class', 'control-point')
            .attr('cx', d => x(d.x))
            .attr('cy', d => y(d.y))
            .attr('r', 5)
            .attr('fill', 'red')
            .call(d3.drag()
              .on('start', function (event) {
                d3.select(this).raise().attr('stroke', 'black');
              })
              .on('drag', (event, d) => {
                d.x = Math.max(0, Math.min(255, x.invert(event.x)));
                d.y = Math.max(0, Math.min(255, y.invert(event.y)));
                this.controlPoint = { x: d.x, y: d.y };
                updateChart();
              })
              .on('end', function (event) {
                d3.select(this).attr('stroke', null);
              }));
        };
  
        updateChart();
      }
    }
  };
  </script>
  
  <style scoped>
  #app {
    font-family: Arial, sans-serif;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  
  .chart {
    font-family: Arial, sans-serif;
    font-size: 14px;
  }
  
  .VH {
    background-color: #f90909;
    font-weight: 550 !important;
  }
  
  .H {
    background-color: #f99d09;
    font-weight: 550 !important;
  }
  
  .M {
    background-color: #f9d909;
    height: 60px;
    font-weight: 550 !important;
  }
  
  .L {
    background-color: #4c7c04;
    font-weight: 550 !important;
  }
  
  #rMatrix > tbody > tr > td,
  #rMatrix > tbody > tr > th,
  #rMatrix > tfoot > tr > td,
  #rMatrix > tfoot > tr > th,
  #rMatrix > thead > tr > td,
  #rMatrix > thead > tr > th {
    vertical-align: middle;
    text-align: center;
    font-weight: 550;
  }
  </style>
  