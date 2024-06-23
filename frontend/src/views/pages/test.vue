<template>
  <div>
      <div class="controls">
          <div class="settings" v-for="(setting, index) in settingsOptions" :key="setting.value">
              <h3>{{ setting.text }}</h3>
              <button @click="saveControlPoint(setting.value)">Save</button>
              <button @click="resetToDefault(setting.value)">Reset</button>
              <div class="chart-container" :ref="'chartContainer-' + setting.value">
                  <div :ref="'chart-' + setting.value"></div>
              </div>
              <div class="pointer-position">Pointer Position: x={{ controlPoints[setting.value].x.toFixed(2) }}, y={{ controlPoints[setting.value].y.toFixed(2) }}</div>
              <div class="history-container">
                  <h4>History</h4>
                  <ul>
                      <li v-for="history in historyData[setting.value]" :key="history.timestamp" @click="loadHistoryPoint(setting.value, history)">
                        {{ formatTimestamp(history.timestamp) }}: x={{ history.x.toFixed(2) }}, y={{ history.y.toFixed(2) }}
                      </li>
                  </ul>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaのストアをインポート

export default {
  name: 'RiskMatrixImpactForProduction',
  props: {
      inputData: {
          type: Array,
          required: true,
          default: () => []
      }
  },
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
              { value: 1, text: 'Low Setting' },
              { value: 2, text: 'Middle Setting' },
              { value: 3, text: 'High Setting' }
          ],
          resizeObservers: {},
          riskTexts: [],
          selectedSetting: 1,
          riskMatrix: [],
          historyData: {
              1: [],
              2: [],
              3: []
          }
      };
  },
  mounted() {
      this.settingsOptions.forEach((setting) => {
          this.drawChart(setting.value);
          this.setupResizeObserver(setting.value);
          this.loadHistory(setting.value); // 各設定の履歴データをロード
      });
      this.calculateRiskTexts(); // 初期設定でリスクテキストを計算
  },
  watch: {
      inputData: {
          handler() {
              this.calculateRiskTexts();
          },
          deep: true
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

          const svg = d3
              .select(this.$refs[`chart-${setting}`][0])
              .append('svg')
              .attr('width', width + margin.left + margin.right)
              .attr('height', height + margin.top + margin.bottom)
              .append('g')
              .attr('transform', `translate(${margin.left},${margin.top})`);

          const xScale = d3.scalePoint().domain([1, 3, 7, 10, 30, '30+']).range([0, width]);

          const yScale = d3.scaleLinear().domain([0, 5]).range([height, 0]);

          // 色の定義
          const colorMap = {
              L: '#4c7c04',
              M: '#f9d909',
              H: '#f99d09',
              VH: '#f90909'
          };

          // テキストの定義
          const riskTextMap = {
              L: 'Low',
              M: 'Middle',
              H: 'High',
              VH: 'High+'
          };

          const updateRiskMatrixColors = (setting) => {
              const riskMatrix = this.getSelectedRiskMatrix(setting);
              if (!riskMatrix) return;

              const xRatio = (this.controlPoints[setting].x - 1) / 29;
              const yRatio = this.controlPoints[setting].y / 5;

              this[`riskMatrix${this.getSettingName(setting)}`] = riskMatrix.map((row) => ({
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

              const riskMatrix = this.getSelectedRiskMatrix(setting);
              if (!riskMatrix) return;

              riskMatrix.forEach((row, i) => {
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

          const line = d3
              .line()
              .x((d) => xScale(d.x))
              .y((d) => yScale(d.y))
              .curve(d3.curveBasis);

          const updateChart = () => {
              svg.selectAll('.line-path').remove();
              svg.selectAll('.axis').remove();
              svg.selectAll('.control-point').remove();

              updateRiskMatrixColors(setting);
              drawRiskMatrix();

              const dataWithControl = [
                  { x: 1, y: 0 }, // リスクマトリックスの左下
                  this.controlPoints[setting],
                  { x: '30+', y: 5 } // リスクマトリックスの右上
              ];

              svg.append('path').datum(dataWithControl).attr('class', 'line-path').attr('fill', 'none').attr('stroke', 'steelblue').attr('stroke-width', 1.5).attr('d', line);

              svg.append('g')
                  .attr('class', 'axis')
                  .attr('transform', `translate(0,${height})`)
                  .call(d3.axisBottom(xScale).tickFormat((d, i) => (i === 5 ? '30+' : d)));

              svg.append('g').attr('class', 'axis').call(d3.axisLeft(yScale).ticks(5));

              svg.append('text')
                  .attr('transform', 'rotate(-90)')
                  .attr('y', 0 - margin.left)
                  .attr('x', 0 - height / 2)
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
                  .attr('cx', (d) => xScale(d.x))
                  .attr('cy', (d) => yScale(d.y))
                  .attr('r', 5)
                  .attr('fill', 'red')
                  .call(
                      d3
                          .drag()
                          .on('start', function (event) {
                              d3.select(this).raise().attr('stroke', 'black');
                          })
                          .on('drag', (event, d) => {
                              const invertX = Math.max(1, Math.min(width, event.x));
                              const closestX = [1, 3, 7, 10, 30].reduce((prev, curr) => (Math.abs(xScale(curr) - invertX) < Math.abs(xScale(prev) - invertX) ? curr : prev));
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
                          })
                  );
          };

          updateChart();
      },
      async saveControlPoint(setting) {
const userStore = useUserStore();
const companyCode = userStore.companyCode;
const levelSetValue = this.getSettingName(setting);

const payload = {
  companyCode: companyCode,
  levelSetValue: levelSetValue,
  x: this.controlPoints[setting].x,
  y: this.controlPoints[setting].y,
};

console.log('Payload:', payload);

try {
  const response = await axios.post('http://127.0.0.1:8000/api/ceList/risk_matrix_impact/', payload, {
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  });

  console.log('Response data:', response.data);
} catch (error) {
  console.error('Error saving control point:', error);
  if (error.response) {
    console.error('Response data:', error.response.data);
  }
}
},
      resetToDefault(setting) {
          this.controlPoints[setting] = { x: 7, y: 2.5 };
          this.drawChart(setting);
      },
      async loadHistory(setting) {
          const userStore = useUserStore();
          const companyCode = userStore.companyCode;
          const levelSetValue = this.getSettingName(setting);

          try {
              const response = await axios.get(`http://127.0.0.1:8000/api/ceList/risk_matrix_impact/${companyCode}/${levelSetValue}/`, {
                  headers: {
                      Authorization: `Bearer ${localStorage.getItem('token')}`
                  }
              });

              console.log('History data:', response.data);
              this.historyData[setting] = response.data;
          } catch (error) {
              console.error('Error loading history:', error);
              if (error.response) {
                  console.error('Response data:', error.response.data);
              }
          }
      },
      loadHistoryPoint(setting, history) {
          this.controlPoints[setting] = { x: history.x, y: history.y };
          this.drawChart(setting);
      },
      formatTimestamp(timestamp) {
          const date = new Date(timestamp);
          return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
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
              L: 'Low',
              M: 'Middle',
              H: 'High',
              VH: 'High+'
          };
          return textMap[riskText] || riskText;
      },
      calculateRiskTexts() {
          if (!this.inputData) return; // inputDataが存在しない場合は終了

          const riskTexts = this.inputData.map((data) => {
              if (data.mttr !== null && data.possibilityOfContinuousProduction !== null) {
                  const setting = this.getSettingFromLevelSetValue(data.levelSetValue);
                  const mttrIndex = this.getMttrIndex(data.mttr);
                  const possibilityIndex = this.getPossibilityIndex(data.possibilityOfContinuousProduction);
                  const riskMatrix = this.getSelectedRiskMatrix(setting);

                  if (riskMatrix && riskMatrix[possibilityIndex] && riskMatrix[possibilityIndex].risk[mttrIndex]) {
                      const riskText = riskMatrix[possibilityIndex].risk[mttrIndex];
                      console.log(`Setting: ${setting}, MTTR: ${data.mttr}, Possibility: ${data.possibilityOfContinuousProduction}, MTTR Index: ${mttrIndex}, Possibility Index: ${possibilityIndex}, RiskText: ${riskText}`);
                      console.log('RiskMatrix at this position:', riskMatrix[possibilityIndex].risk);
                      return this.mapRiskText(riskText);
                  } else {
                      console.error('Invalid risk matrix index:', { mttrIndex, possibilityIndex });
                      return '';
                  }
              } else {
                  return '';
              }
          });

          this.riskTexts = riskTexts;
          this.$emit('update-risk-texts', riskTexts);
      },
      getSettingFromLevelSetValue(levelSetValue) {
          switch (levelSetValue) {
              case 'Low':
                  return 1;
              case 'Middle':
                  return 2;
              case 'High':
              case 'High+':
                  return 3;
              default:
                  return 1;
          }
      },
      getSettingName(setting) {
          switch (setting) {
              case 1:
                  return 'Low';
              case 2:
                  return 'Middle';
              case 3:
                  return 'High';
              default:
                  return 'Low';
          }
      },
      getSelectedRiskMatrix(setting) {
          const riskMatrix = this[`riskMatrix${this.getSettingName(setting)}`];
          return riskMatrix || [];
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

.history-container {
  margin-top: 10px;
}

.history-container ul {
  list-style-type: none;
  padding: 0;
}

.history-container li {
  cursor: pointer;
  padding: 5px;
  margin: 2px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #4c7c04; /* グリーン背景色 */
  transition: background-color 0.3s;
  color: white; /* 白文字色 */
  width: 150px; /* 幅を調整 */
}

.history-container li:hover {
  background-color: #3b6203; /* 少し暗めの緑色 */
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

.control-point {
  cursor: pointer;
}

.line-path {
  stroke: steelblue;
  stroke-width: 1.5;
  fill: none;
}
</style>
