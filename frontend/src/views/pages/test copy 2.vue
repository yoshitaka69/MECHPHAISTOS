<template>
  <div>
    <div class="controls">
      <div class="settings" v-for="(setting, index) in settingsOptions" :key="setting.value">
        <h3>{{ setting.text }}</h3>
        <button @click="saveControlPoint(setting.value)">保存</button>
        <button @click="resetToDefault(setting.value)">初期値</button>
        <div class="chart-container" :ref="'chartContainer-' + setting.value">
          <div :ref="'chart-' + setting.value"></div>
        </div>
        <div class="pointer-position">ポインターの位置: x={{ controlPoints[setting.value].x.toFixed(2) }}, y={{ controlPoints[setting.value].y.toFixed(2) }}</div>
      </div>
    </div>
    <div class="input-form">
      <h3>MTTRとPossibility of Continuous Productionの入力</h3>
      <div v-for="(input, index) in inputs" :key="index" class="input-group">
        <h4>{{ input.label }}</h4>
        <label :for="'mttr-input-' + index">MTTR (days):</label>
        <input type="number" :id="'mttr-input-' + index" v-model.number="input.mttrValue">
        <label :for="'production-input-' + index">Possibility of Continuous Production:</label>
        <input type="number" :id="'production-input-' + index" v-model.number="input.productionValue" step="0.1" min="0" max="5">
        <button @click="updateRiskLevel(index)">リスクレベルを更新</button>
        <div class="risk-output">
          <h4>現在のリスクレベル: {{ input.currentRiskLevel }}</h4>
        </div>
      </div>
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
      controlPoints: {
        1: { x: 7, y: 2.5 },
        2: { x: 7, y: 2.5 },
        3: { x: 7, y: 2.5 }
      },
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
      settingsOptions: [
        { value: 1, text: 'Low 設定' },
        { value: 2, text: 'Middle 設定' },
        { value: 3, text: 'High 設定' }
      ],
      resizeObservers: {},
      inputs: [
        { label: 'Low 設定', mttrValue: 7, productionValue: 2.5, currentRiskLevel: '' },
        { label: 'Middle 設定', mttrValue: 7, productionValue: 2.5, currentRiskLevel: '' },
        { label: 'High 設定', mttrValue: 7, productionValue: 2.5, currentRiskLevel: '' }
      ]
    };
  },
  mounted() {
    this.settingsOptions.forEach(setting => {
      this.drawChart(setting.value);
      this.setupResizeObserver(setting.value);
    });
  },
  beforeDestroy() {
    this.settingsOptions.forEach(setting => {
      if (this.resizeObservers[setting.value]) {
        this.resizeObservers[setting.value].disconnect();
      }
    });
  },
  methods: {
    setupResizeObserver(setting) {
      const container = this.$refs[`chartContainer-${setting}`][0];
      this.resizeObservers[setting] = new ResizeObserver(() => {
        this.drawChart(setting);
      });
      this.resizeObservers[setting].observe(container);
    },
    drawChart(setting) {
      const container = this.$refs[`chartContainer-${setting}`][0];
      const containerWidth = container.offsetWidth;
      const containerHeight = container.offsetHeight;
      const margin = { top: 20, right: 20, bottom: 30, left: 40 };
      const width = containerWidth - margin.left - margin.right;
      const height = containerHeight - margin.top - margin.bottom;

      d3.select(this.$refs[`chart-${setting}`][0]).selectAll('*').remove(); // 既存の内容をクリア

      const svg = d3.select(this.$refs[`chart-${setting}`][0])
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
        const xRatio = (this.controlPoints[setting].x - 1) / 29; // 修正
        const yRatio = this.controlPoints[setting].y / 5; // 縦軸の最大値に合わせる

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
          this.controlPoints[setting],
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
          .data([this.controlPoints[setting]])
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
              this.controlPoints[setting] = { x: d.x, y: d.y };
              updateChart();
            })
            .on('end', function (event) {
              d3.select(this).attr('stroke', null);
            }));
      };

      updateChart();
    },
    saveControlPoint(setting) {
      this.controlPoints[setting] = { ...this.controlPoints[setting] };
    },
    resetToDefault(setting) {
      this.controlPoints[setting] = { x: 7, y: 2.5 };
      this.drawChart(setting);
    },
    updateRiskLevel(index) {
      const riskTextMap = {
        'L': 'Low',
        'M': 'Middle',
        'H': 'High',
        'VH': 'High+'
      };

      const mttrValue = this.inputs[index].mttrValue;
      const productionValue = this.inputs[index].productionValue;

      // MTTRの範囲に従ってインデックスを計算
      let mttrIndex;
      if (mttrValue <= 3) {
        mttrIndex = 0;
      } else if (mttrValue <= 7) {
        mttrIndex = 1;
      } else if (mttrValue <= 10) {
        mttrIndex = 2;
      } else if (mttrValue <= 30) {
        mttrIndex = 3;
      } else {
        mttrIndex = 4;
      }

      // Production valueをlikelihoodのインデックスに変換
      const likelihoodIndex = Math.min(4, Math.max(0, Math.floor(productionValue)));

      // リスクレベルのテキストを取得
      const riskLevel = this.riskMatrix[4 - likelihoodIndex].risk[mttrIndex];
      this.$set(this.inputs, index, { ...this.inputs[index], currentRiskLevel: riskTextMap[riskLevel] });
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

.chart-container {
  display: inline-block;
  vertical-align: top;
  width: 100%;
  height: 400px;
  margin-top: 40px; /* テーブルとチャート間のマージン */
}

.controls {
  display: flex;
  justify-content: space-around;
}

.settings {
  display: inline-block;
  vertical-align: top;
  margin-right: 20px;
  width: 30%;
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

.input-form {
  margin: 20px 0;
}

.input-form label {
  margin-right: 10px;
}

.input-form input {
  margin-right: 20px;
}

.input-group {
  margin-bottom: 20px;
}

.risk-output {
  margin-top: 10px;
  font-size: 18px;
  font-weight: bold;
}
</style>
