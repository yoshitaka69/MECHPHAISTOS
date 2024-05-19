<template>
  <div>
    <div class="controls">
      <label for="settings">設定:</label>
      <select id="settings" v-model="selectedSetting" @change="loadControlPoint">
        <option v-for="option in settingsOptions" :key="option.value" :value="option.value">
          {{ option.text }}
        </option>
      </select>
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
        { x: 150, y: 150 },
        { x: 255, y: 255 }
      ],
      controlPoint: { x: 125, y: 150 },
      riskMatrix: [
        { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
        { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
        { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
      ],
      riskMatrixInitial: [
        { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
        { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
        { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
      ],
      riskClasses: ['Near Miss', 'Minor Inquiry', 'Lost Time Accident', 'Major Inquiry', 'Fatality'],
      selectedSetting: 1,
      settingsOptions: [
        { value: 1, text: '設定 1' },
        { value: 2, text: '設定 2' },
        { value: 3, text: '設定 3' }
      ],
      savedControlPoints: {
        1: { x: 150, y: 150 },
        2: { x: 150, y: 150 },
        3: { x: 150, y: 150 }
      }
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

      d3.select(this.$refs.chart).selectAll('*').remove(); // 既存の内容をクリア

      const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3.scaleLinear().domain([0, 255]).range([0, width]);
      const y = d3.scaleLinear().domain([0, 255]).range([height, 0]);

      // 色の定義
      const colorMap = {
        'L': '#4c7c04',
        'M': '#f9d909',
        'H': '#f99d09',
        'VH': '#f90909'
      };

      const updateRiskMatrixColors = () => {
  // コントロールポイントの位置に基づいて色を変更
  const xRatio = this.controlPoint.x / 255;
  const yRatio = 1 - (this.controlPoint.y / 255); // yは逆方向

  this.riskMatrix = this.riskMatrixInitial.map(row => ({
    ...row,
    risk: row.risk.map((risk, j) => {
      // 変化率を強調
      const adjustedX = j + xRatio * 6 - 3; // 変化率を強調
      const adjustedY = row.likelihood + yRatio * 6 - 3; // 変化率を強調
      const average = (adjustedX + adjustedY) / 2;
      if (average < 1) return 'L';
      if (average < 2) return 'M';
      if (average < 3) return 'H';
      return 'VH';
    })
  }));
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
              .attr('fill', colorMap[risk])
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
    },
    saveControlPoint() {
      this.savedControlPoints[this.selectedSetting] = { ...this.controlPoint };
    },
    loadControlPoint() {
      this.controlPoint = { ...this.savedControlPoints[this.selectedSetting] };
      this.drawChart();
    },
    resetToDefault() {
      this.controlPoint = { x: 125, y: 150 };
      this.saveControlPoint(); // 初期値を保存
      this.drawChart();
    }
  },
  watch: {
    selectedSetting() {
      this.loadControlPoint();
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

.chart-container {
  display: inline-block;
  vertical-align: top;
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
