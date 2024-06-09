<template>
  <div>
    <div>
      <label>設定:
        <select v-model="selectedSetting">
          <option v-for="option in settingsOptions" :key="option.value" :value="option.value">
            {{ option.text }}
          </option>
        </select>
      </label>
    </div>
    <div v-for="(data, index) in inputData" :key="index">
      <label>MTTR[days] (Index {{ index }}):
        <input type="number" v-model.number="data.mttr" />
      </label>
      <label>Possibility of Continuous Production (Index {{ index }}):
        <input type="number" v-model.number="data.possibility" />
      </label>
      <p>Risk Text (Index {{ index }}): {{ riskTexts[index] }}</p>
    </div>
    <button @click="calculateRiskTexts">Calculate Risk Texts</button>
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
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'ToneCurve',
  data() {
    return {
      controlPoints: {
        1: { x: 7, y: 2.5 },
        2: { x: 7, y: 2.5 },
        3: { x: 7, y: 2.5 }
      },
      riskMatrixLow: [
        { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
        { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
        { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
      ],
      riskMatrixMiddle: [
        { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
        { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
        { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
      ],
      riskMatrixHigh: [
        { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
        { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
        { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
        { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
        { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
      ],
      settingsOptions: [
        { value: 1, text: 'Low 設定' },
        { value: 2, text: 'Middle 設定' },
        { value: 3, text: 'High 設定' }
      ],
      resizeObservers: {},
      inputData: [
        { mttr: null, possibility: null },
      ],
      riskTexts: [],
      selectedSetting: 1,
      riskMatrix: []
    };
  },
  mounted() {
    this.settingsOptions.forEach(setting => {
      this.drawChart(setting.value);
      this.setupResizeObserver(setting.value);
    });
    this.updateRiskMatrix(); // 初期設定
  },
  watch: {
    inputData: {
      handler() {
        this.calculateRiskTexts();
      },
      deep: true
    },
    selectedSetting() {
      this.updateRiskMatrix(); // 設定が変更された時にリスクマトリックスを更新
      this.drawChart(this.selectedSetting); // 設定が変更された時にチャートを再描画する
      this.calculateRiskTexts();
    }
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
        const xRatio = (this.controlPoints[setting].x - 1) / 29;
        const yRatio = this.controlPoints[setting].y / 5;

        this.riskMatrix = this.getSelectedRiskMatrix().map(row => ({
          ...row,
          risk: row.risk.map((risk, j) => {
            const adjustedX = j + xRatio * 6 - 3;
            const adjustedY = row.likelihood - yRatio * 6 + 3;
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
              .attr('y', (5 - row.likelihood) * cellHeight)
              .attr('width', cellWidth)
              .attr('height', cellHeight)
              .attr('fill', colorMap[risk])
              .attr('stroke', '#000')
              .attr('stroke-width', 1)
              .attr('class', 'risk-cell');

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
          this.controlPoints[setting]
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
              if (setting === this.selectedSetting) {
                this.calculateRiskTexts(); // 現在の設定の場合のみリスクテキストを更新
              }
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
    getMttrIndex(mttr) {
      if (mttr < 1 || mttr >= 30) return 4;
      if (mttr < 3) return 0;
      if (mttr < 7) return 1;
      if (mttr < 10) return 2;
      return 3;
    },
    getPossibilityIndex(possibility) {
      if (possibility < 1) return 4;
      if (possibility < 2) return 3;
      if (possibility < 3) return 2;
      if (possibility < 4) return 1;
      return 0;
    },
    mapRiskText(riskText) {
      const textMap = {
        'L': 'Low',
        'M': 'Middle',
        'H': 'High',
        'VH': 'High+'
      };
      return textMap[riskText] || riskText;
    },
    updateRiskMatrix() {
      switch (this.selectedSetting) {
        case 1:
          this.riskMatrix = this.riskMatrixLow;
          break;
        case 2:
          this.riskMatrix = this.riskMatrixMiddle;
          break;
        case 3:
          this.riskMatrix = this.riskMatrixHigh;
          break;
        default:
          this.riskMatrix = this.riskMatrixLow;
      }
    },
    calculateRiskTexts() {
      this.riskTexts = this.inputData.map(data => {
        if (data.mttr !== null && data.possibility !== null) {
          const mttrIndex = this.getMttrIndex(data.mttr);
          const possibilityIndex = this.getPossibilityIndex(data.possibility);

          if (this.riskMatrix[possibilityIndex] && this.riskMatrix[possibilityIndex].risk[mttrIndex]) {
            const riskText = this.riskMatrix[possibilityIndex].risk[mttrIndex];
            console.log(`Setting: ${this.selectedSetting}, MTTR: ${data.mttr}, Possibility: ${data.possibility}, MTTR Index: ${mttrIndex}, Possibility Index: ${possibilityIndex}, RiskText: ${riskText}`);
            console.log('RiskMatrix at this position:', this.riskMatrix[possibilityIndex].risk);
            return this.mapRiskText(riskText);
          } else {
            console.error('Invalid risk matrix index:', { mttrIndex, possibilityIndex });
            return '';
          }
        } else {
          return '';
        }
      });
    },
    getSelectedRiskMatrix() {
      switch (this.selectedSetting) {
        case 1:
          return this.riskMatrixLow;
        case 2:
          return this.riskMatrixMiddle;
        case 3:
          return this.riskMatrixHigh;
        default:
          return this.riskMatrixLow;
      }
    }
  }
};
</script>

<style scoped>
.chart-container {
  display: inline-block;
  vertical-align: top;
  width: 100%;
  height: 400px;
  margin-top: 40px;
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
</style>
