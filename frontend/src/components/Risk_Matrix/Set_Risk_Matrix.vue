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
        { x: 1, y: 0 },
        { x: 7, y: 2.5 },
        { x: 30, y: 5 }
      ],
      controlPoint: { x: 7, y: 2.5 },
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
        1: { x: 7, y: 2.5 },
        2: { x: 7, y: 2.5 },
        3: { x: 7, y: 2.5 }
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

      const xScale = d3.scalePoint()
        .domain([1, 3, 7, 10, 30, '30+'])
        .range([0, width]);

      const yScale = d3.scaleLinear().domain([0, 5]).range([height, 0]);

      // 色の定義
      const colorMap = {
        'L': '#4c7c04',
        'M': '#f9d909',
        'H': '#f99d09',
        'VH': '#f90909'
      };

      // テキストの定義
      const riskTextMap = {
        'L': 'Low',
        'M': 'Middle',
        'H': 'High',
        'VH': 'High+'
      };

      const updateRiskMatrixColors = () => {
        const xRatio = (this.controlPoint.x - 1) / 29; // 修正
        const yRatio = this.controlPoint.y / 5; // 縦軸の最大値に合わせる

        this.riskMatrix = this.riskMatrixInitial.map(row => ({
          ...row,
          risk: row.risk.map((risk, j) => {
            const adjustedX = j + xRatio * 6 - 3; // 変化率を強調
            const adjustedY = row.likelihood - yRatio * 6 + 3; // 変化率を強調
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
        svg.selectAll('.risk-text').remove();

        const cellWidth = width / 5;
        const cellHeight = height / 5;

        this.riskMatrix.forEach((row, i) => {
          row.risk.forEach((risk, j) => {
            svg.append('rect')
              .attr('x', j * cellWidth)
              .attr('y', (5 - row.likelihood) * cellHeight) // 縦軸の目盛りに合わせる
              .attr('width', cellWidth)
              .attr('height', cellHeight)
              .attr('fill', colorMap[risk])
              .attr('stroke', '#000')
              .attr('stroke-width', 1)
              .attr('class', 'risk-cell');

            // リスクレベルのテキストを追加
            svg.append('text')
              .attr('x', j * cellWidth + cellWidth / 2)
              .attr('y', (5 - row.likelihood) * cellHeight + cellHeight / 2)
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
          .call(d3.axisBottom(xScale).tickFormat((d, i) => i === 5 ? '30+' : d));

        svg.append('g')
          .attr('class', 'axis')
          .call(d3.axisLeft(yScale).ticks(5));

        svg.append('text')
          .attr('transform', 'rotate(-90)')
          .attr('y', 0 - margin.left)
          .attr('x', 0 - (height / 2))
          .attr('dy', '1em')
          .style('text-anchor', 'middle')
          .text('Possibility of continuous production');

        svg.append('text')
          .attr('x', width / 2)
          .attr('y', height + margin.bottom)
          .attr('dy', '-0.5em')
          .style('text-anchor', 'middle')
          .text('MTTR[days]');

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
              const invertX = Math.max(1, Math.min(width, event.x));
              const closestX = [1, 3, 7, 10, 30].reduce((prev, curr) => Math.abs(xScale(curr) - invertX) < Math.abs(xScale(prev) - invertX) ? curr : prev);
              const invertY = Math.max(0, Math.min(5, yScale.invert(event.y)));
              d.x = closestX;
              d.y = invertY;
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
      this.controlPoint = { x: 7, y: 2.5 };
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
