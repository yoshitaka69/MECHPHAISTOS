<template>
  <div>
    <div class="controls">
      <h3>Possibility_Of_Failure</h3>
      <button @click="saveControlPoint">保存</button>
      <button @click="resetToDefault">初期値</button>
    </div>
    <div class="chart-container">
      <div ref="chart"></div>
      <div class="pointer-position">ポインターの位置: x={{ controlPoint.x.toFixed(2) }}, y={{ controlPoint.y.toFixed(2) }}</div>
    </div>
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
        { x: 3, y: 2.5 },
        { x: 6, y: 6 }
      ],
      controlPoint: { x: 3, y: 4 },
      riskMatrix: [
        { likelihood: 7, description: 'Almost certain', risk: ['H', 'VH', 'VH', 'VH', 'VH', 'VH'] },
        { likelihood: 6, description: 'Likely', risk: ['M', 'H', 'VH', 'VH', 'VH', 'VH'] },
        { likelihood: 5, description: 'Possible', risk: ['L', 'M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'Unlikely', risk: ['L', 'L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'Rare', risk: ['L', 'L', 'L', 'M', 'H', 'VH'] },
        { likelihood: 2, description: 'Very rare', risk: ['L', 'L', 'L', 'L', 'M', 'H'] }
      ],
      riskMatrixInitial: [
        { likelihood: 7, description: 'Almost certain', risk: ['H', 'VH', 'VH', 'VH', 'VH', 'VH'] },
        { likelihood: 6, description: 'Likely', risk: ['M', 'H', 'VH', 'VH', 'VH', 'VH'] },
        { likelihood: 5, description: 'Possible', risk: ['L', 'M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'Unlikely', risk: ['L', 'L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'Rare', risk: ['L', 'L', 'L', 'M', 'H', 'VH'] },
        { likelihood: 2, description: 'Very rare', risk: ['L', 'L', 'L', 'L', 'M', 'H'] }
      ],
      riskClasses: ['Near Miss', 'Minor Inquiry', 'Lost Time Accident', 'Major Inquiry', 'Fatality'],
      savedControlPoints: {
        1: { x: 3, y: 4 },
        2: { x: 3, y: 4 },
        3: { x: 3, y: 4 }
      }
    };
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    drawChart() {
      const margin = { top: 20, right: 20, bottom: 50, left: 120 };
      const width = 500 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      d3.select(this.$refs.chart).selectAll('*').remove();

      const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const xScale = d3.scalePoint()
        .domain([0, 1, 2, 3, 4, 5, 6])
        .range([0, width]);

      const yScale = d3.scalePoint()
        .domain([0, 2, 3, 4, 5, 6, 7])
        .range([height, 0]);

      const yScaleLeft = d3.scalePoint()
        .domain([0, 0, 0, 0.5, 1, 1.5, 2, 2.5, 3])
        .range([height, 0]);

      const colorMap = {
        'L': '#4c7c04',
        'LM': '#a0d070',
        'M': '#f9d909',
        'H': '#f99d09',
        'VH': '#f90909'
      };

      const riskTextMap = {
        'L': '見直し検討',
        'LM': '適正',
        'M': '注意',
        'H': '対策検討',
        'VH': '要対策'
      };

      const updateRiskMatrixColors = () => {
        const xRatio = (this.controlPoint.x - 1) / 29;
        const yRatio = (this.controlPoint.y - 2) / 5;

        this.riskMatrix = this.riskMatrixInitial.map(row => ({
          ...row,
          risk: row.risk.map((risk, j) => {
            const adjustedX = j + xRatio * 6 - 3;
            const adjustedY = row.likelihood - yRatio * 6 + 3;
            const average = (adjustedX + adjustedY) / 2;
            if (average < 1) return 'L';
            if (average < 2) return 'LM';
            if (average < 3) return 'M';
            if (average < 4) return 'H';
            return 'VH';
          })
        }));
      };

      const drawRiskMatrix = () => {
        svg.selectAll('.risk-cell').remove();
        svg.selectAll('.risk-text').remove();

        const cellWidth = width / 6;
        const cellHeight = height / 6;

        this.riskMatrix.forEach((row, i) => {
          row.risk.forEach((risk, j) => {
            svg.append('rect')
              .attr('x', j * cellWidth)
              .attr('y', (7 - row.likelihood) * cellHeight)
              .attr('width', cellWidth)
              .attr('height', cellHeight)
              .attr('fill', colorMap[risk])
              .attr('stroke', '#000')
              .attr('stroke-width', 1)
              .attr('class', 'risk-cell');

            svg.append('text')
              .attr('x', j * cellWidth + cellWidth / 2)
              .attr('y', (7 - row.likelihood) * cellHeight + cellHeight / 2)
              .attr('dy', '.35em')
              .attr('text-anchor', 'middle')
              .attr('class', 'risk-text')
              .text(riskTextMap[risk])
              .attr('fill', '#000');
          });
        });
      };

      const line = d3.line()
        .x(d => xScale(d.x))
        .y(d => yScale(d.y))
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
          .call(d3.axisBottom(xScale).tickPadding(15).tickFormat(d => d.toString()));

        svg.append('g')
          .attr('class', 'axis')
          .call(d3.axisLeft(yScale).tickPadding(15).tickFormat(d => d.toString()));

        svg.append('g')
          .attr('class', 'axis')
          .attr('transform', `translate(${-60},0)`)
          .call(d3.axisLeft(yScaleLeft).tickPadding(15).tickFormat((d, i) => ['0', '0', '0', '0.5', '1', '1.5', '2', '2.5', '3'][i]));

        svg.append('text')
          .attr('transform', 'rotate(-90)')
          .attr('y', 0 - margin.left + 60)
          .attr('x', 0 - (height / 2))
          .attr('dy', '1em')
          .style('text-anchor', 'middle')
          .text('Number of PM04 occurrences in the past 5 years');

        svg.append('text')
          .attr('transform', 'rotate(-90)')
          .attr('y', 0 - margin.left + 100)
          .attr('x', 0 - (height / 2))
          .attr('dy', '1em')
          .style('text-anchor', 'middle')
          .text('Number of PM03 occurrences in the past 5 years');

        svg.append('text')
          .attr('x', width / 2)
          .attr('y', height + margin.bottom)
          .attr('dy', '-0.5em')
          .style('text-anchor', 'middle')
          .text('Time of occurrence on PM02');

        svg.selectAll('circle')
          .data([this.controlPoint])
          .enter()
          .append('circle')
          .attr('class', 'control-point')
          .attr('cx', d => xScale(d.x))
          .attr('cy', d => yScale(d.y))
          .attr('r', 5)
          .attr('fill', 'red')
          .call(d3.drag()
            .on('start', function (event) {
              d3.select(this).raise().attr('stroke', 'black');
            })
            .on('drag', (event, d) => {
              const invertX = Math.max(0, Math.min(width, event.x));
              const closestX = [0, 1, 2, 3, 4, 5, 6].reduce((prev, curr) => Math.abs(xScale(curr) - invertX) < Math.abs(xScale(prev) - invertX) ? curr : prev);
              const invertY = Math.max(0, Math.min(height, event.y));
              const closestY = [0, 2, 3, 4, 5, 6, 7].reduce((prev, curr) => Math.abs(yScale(curr) - invertY) < Math.abs(yScale(prev) - invertY) ? curr : prev);
              d.x = closestX;
              d.y = closestY;
              this.controlPoint = { x: d.x, y: d.y };
              updateChart();
            })
            .on('end', function (event) {
              d3.select(this).attr('stroke', null);
            }));
      };

      updateChart();
    },
    saveControlPoint() {
      this.savedControlPoints[1] = { ...this.controlPoint };
    },
    loadControlPoint() {
      this.controlPoint = { ...this.savedControlPoints[1] };
      this.drawChart();
    },
    resetToDefault() {
      this.controlPoint = { x: 3, y: 4 };
      this.saveControlPoint();
      this.drawChart();
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

.impact-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.impact-table th, .impact-table td {
  border: 1px solid black;
  padding: 10px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.impact-table th {
  background-color: grey;
  color: white;
}

.impact-table tr:nth-child(even) {
  background-color: lightgrey;
}

.impact-table tr:nth-child(odd) {
  background-color: white;
}

.impact-table td {
  vertical-align: top;
}

.failure-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.failure-table th, .failure-table td {
  border: 1px solid black;
  padding: 10px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.failure-table th {
  color: black;
}

.failure-table tr:nth-child(even) {
  background-color: lightgrey;
}

.failure-table tr:nth-child(odd) {
  background-color: white;
}

.failure-table td {
  vertical-align: top;
}

.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 400px;
  margin-top: 40px; /* テーブルとチャート間のマージン */
}

.controls {
  display: inline-block;
  vertical-align: top;
  margin-right: 20px;
}

.pointer-position {
  margin-top: 10px;
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

.LM {
  background-color: #a0d070;
  font-weight: 550 !important;
}

.L {
  background-color: #4c7c04;
  font-weight: 550 !important;
}

.risk-text {
  font-size: 12px;
  font-weight: bold;
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
