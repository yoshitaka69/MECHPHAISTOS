<template>
  <div class="container">
      <div class="chart-section">
          <div class="chart-container">
              <div ref="chart"></div>
          </div>
          <div class="pointer-position">Pointer Position: x={{ controlPoint.x.toFixed(2) }}, y={{ controlPoint.y.toFixed(2) }}</div>
          <div class="controls">
              <Button label="Save" icon="pi pi-save" @click="saveControlPoint" class="p-button-primary blue-button" />
              <Button label="Reset" icon="pi pi-refresh" @click="resetToDefault" class="p-button-primary blue-button ml-3" />
          </div>
      </div>
      <div class="history-container">
          <h3>History</h3>
          <div class="history-buttons">
              <div v-for="(item, index) in history" :key="item.timestamp" class="history-item">
                  <span @click.stop="toggleFavorite(index)" class="star-container">
                      <i :class="favoriteHistoryPossibility === index ? 'pi pi-star-fill' : 'pi pi-star'" class="star-icon"></i>
                  </span>
                  <Button @click="setControlPoint(item)" class="p-button history-button"> 
                      {{ item.formattedTimestamp }} - x: {{ item.x }}, y: {{ item.y }} 
                  </Button>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';
import Button from 'primevue/button';

export default {
  name: 'RiskMatrixPossibilityOfFailureOnlyMatrix',
  props: {
        inputData: {
            type: Array,
            required: true,
            default: () => []
        }
    },
  components: {
      Button
  },
  data() {
      return {
          controlPoint: { x: 3, y: 4 },
          history: [],
          favoriteHistory: null,
          riskMatrixInitial: [
              { likelihood: 7, description: 'Almost certain', risk: ['H', 'VH', 'VH', 'VH', 'VH', 'VH'] },
              { likelihood: 6, description: 'Likely', risk: ['M', 'H', 'VH', 'VH', 'VH', 'VH'] },
              { likelihood: 5, description: 'Possible', risk: ['L', 'M', 'H', 'VH', 'VH', 'VH'] },
              { likelihood: 4, description: 'Unlikely', risk: ['L', 'L', 'M', 'H', 'VH', 'VH'] },
              { likelihood: 3, description: 'Rare', risk: ['L', 'L', 'L', 'M', 'H', 'VH'] },
              { likelihood: 2, description: 'Very rare', risk: ['L', 'L', 'L', 'L', 'M', 'H'] }
          ],
          riskMatrix: [],
          data: [
              { x: 0, y: 0 },
              { x: 3, y: 4 },
              { x: 6, y: 6 }
          ] // ここで初期化
      };
  },
  created() {
    console.log('Received props:', this.inputData); // propsの確認
    this.initializeComponent();
},
  methods: {
      async initializeComponent() {
          try {
              await this.loadHistory();  // 履歴をロード
              this.loadFavoriteControlPoint();  // ★をロードしてデータを出力
              this.drawChart();  // チャートを描画
          } catch (error) {
              console.error('Error during component initialization:', error);
          }
      },
      async loadHistory() {
          const userStore = useUserStore();
          const companyCode = userStore.companyCode;

          try {
              const response = await axios.get(`http://127.0.0.1:8000/api/ceList/risk_matrix_possibility/${companyCode}/`, {
                  headers: {
                      Authorization: `Bearer ${localStorage.getItem('token')}`
                  }
              });

              this.history = response.data.map((item, index) => {
                  const date = new Date(item.timestamp);
                  item.formattedTimestamp = `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).slice(-2)}-${('0' + date.getDate()).slice(-2)} ${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}`;
                  return item;
              });
              
              // PiniaからfavoriteHistoryPossibilityを取得してセット
              this.favoriteHistoryPossibility = userStore.favoriteHistoryPossibility;
              if (this.favoriteHistoryPossibility !== null && this.history[this.favoriteHistoryPossibility]) {
                  this.setControlPoint(this.history[this.favoriteHistoryPossibility]);
                  console.log('Favorite control point loaded:', this.history[this.favoriteHistoryPossibility]);
              }

              console.log('History loaded:', this.history);
          } catch (error) {
              console.error('Error loading history:', error);
          }
      },
      loadFavoriteControlPoint() {
          const userStore = useUserStore();
          console.log('Loading favorite control point, index:', userStore.favoriteHistoryPossibility);
          this.favoriteHistoryPossibility = userStore.favoriteHistoryPossibility;
          if (this.favoriteHistoryPossibility !== null && this.history[this.favoriteHistoryPossibility]) {
              this.setControlPoint(this.history[this.favoriteHistoryPossibility]);
              console.log('Loaded favorite control point:', this.history[this.favoriteHistoryPossibility]);
          }
      },
      toggleFavorite(index) {
          const userStore = useUserStore();
          console.log('Toggling favorite. Current favorite index:', userStore.favoriteHistoryPossibility);
          if (userStore.favoriteHistoryPossibility === index) {
              userStore.setFavoriteHistoryPossibility(null);
              this.favoriteHistoryPossibility = null;
              console.log('Favorite history cleared.');
          } else {
              userStore.setFavoriteHistoryPossibility(index);
              this.favoriteHistoryPossibility = index;
              this.loadFavoriteControlPoint(); // ★を切り替えた時にもロードする
              console.log('New favorite history set:', index);
          }
      },
      setControlPoint(item) {
          this.controlPoint = { x: item.x, y: item.y };
          this.drawChart();
      },

      drawChart() {
          const margin = { top: 20, right: 20, bottom: 50, left: 120 };
          const width = 500 - margin.left - margin.right;
          const height = 400 - margin.top - margin.bottom;

          d3.select(this.$refs.chart).selectAll('*').remove();

          const svg = d3
              .select(this.$refs.chart)
              .append('svg')
              .attr('width', width + margin.left + margin.right)
              .attr('height', height + margin.top + margin.bottom)
              .append('g')
              .attr('transform', `translate(${margin.left},${margin.top})`);

          const xScale = d3.scalePoint().domain([0, 1, 2, 3, 4, 5, 6]).range([0, width]);

          const yScale = d3.scalePoint().domain([0, 2, 3, 4, 5, 6, 7]).range([height, 0]);

          const yScaleLeft = d3.scalePoint().domain([0, '0', 0, 1, 2, 3, 4, 5]).range([height, 0]);

          console.log(yScaleLeft.domain()); // 目盛りの数を確認するために追加

          const colorMap = {
              L: '#4c7c04',
              LM: '#a0d070',
              M: '#f9d909',
              H: '#f99d09',
              VH: '#f90909'
          };

          const riskTextMap = {
              L: 'Review',
              LM: 'Appropriate',
              M: 'Caution',
              H: 'Measures',
              VH: 'Danger'
          };

          const updateRiskMatrixColors = () => {
              if (!this.riskMatrixInitial || !this.riskMatrixInitial.length) {
                  console.error('riskMatrixInitial is not defined or empty');
                  return;
              }

              const xRatio = (this.controlPoint.x - 1) / 29;
              const yRatio = (this.controlPoint.y - 2) / 5;

              this.riskMatrix = this.riskMatrixInitial.map((row) => ({
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

                      const textLines = riskTextMap[risk].split(' ');

                      textLines.forEach((line, index) => {
                          svg.append('text')
                              .attr('x', j * cellWidth + cellWidth / 2)
                              .attr('y', (7 - row.likelihood) * cellHeight + cellHeight / 2)
                              .attr('dy', '.35em')
                              .attr('text-anchor', 'middle')
                              .attr('class', 'risk-text')
                              .append('tspan')
                              .attr('x', j * cellWidth + cellWidth / 2)
                              .attr('dy', `${index * 10}px`)
                              .text(line)
                              .attr('fill', '#000')
                              .style('font-size', '10px'); /* フォントサイズを小さく変更 */
                      });
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

              if (!this.data || this.data.length < 3) {
                  console.error('data is not defined or does not have enough points');
                  return;
              }

              updateRiskMatrixColors();
              drawRiskMatrix();

              const dataWithControl = [this.data[0], this.controlPoint, this.data[2]];

              svg.append('path').datum(dataWithControl).attr('class', 'line-path').attr('fill', 'none').attr('stroke', 'steelblue').attr('stroke-width', 1.5).attr('d', line);

              svg.append('g')
                  .attr('class', 'axis')
                  .attr('transform', `translate(0,${height})`)
                  .call(
                      d3
                          .axisBottom(xScale)
                          .tickPadding(15)
                          .tickFormat((d) => d.toString())
                  );

              svg.append('g')
                  .attr('class', 'axis')
                  .call(
                      d3
                          .axisLeft(yScale)
                          .tickPadding(15)
                          .tickFormat((d) => d.toString())
                  );

              svg.append('g')
                  .attr('class', 'axis')
                  .attr('transform', `translate(${-60},0)`)
                  .call(
                      d3
                          .axisLeft(yScaleLeft)
                          .tickPadding(15)
                          .tickFormat((d) => d.toString())
                  );

              svg.append('text')
                  .attr('transform', 'rotate(-90)')
                  .attr('y', 0 - margin.left + 60)
                  .attr('x', 0 - height / 2)
                  .attr('dy', '1em')
                  .style('text-anchor', 'middle')
                  .text('Number of PM04 occurrences in the past 5 years');

              svg.append('text')
                  .attr('transform', 'rotate(-90)')
                  .attr('y', 0 - margin.left + 100)
                  .attr('x', 0 - height / 2)
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
                              const invertX = Math.max(0, Math.min(width, event.x));
                              const closestX = [0, 1, 2, 3, 4, 5, 6].reduce((prev, curr) => (Math.abs(xScale(curr) - invertX) < Math.abs(xScale(prev) - invertX) ? curr : prev));
                              const invertY = Math.max(0, Math.min(height, event.y));
                              const closestY = [0, 2, 3, 4, 5, 6, 7].reduce((prev, curr) => (Math.abs(yScale(curr) - invertY) < Math.abs(yScale(prev) - invertY) ? curr : prev));
                              d.x = closestX;
                              d.y = closestY;
                              this.controlPoint = { x: d.x, y: d.y };
                              updateChart();
                              this.updateRiskText();
                          })
                          .on('end', function (event) {
                              d3.select(this).attr('stroke', null);
                          })
                  );
          };

          updateChart();
      },

      async saveControlPoint() {
          const userStore = useUserStore();
          const companyCode = userStore.companyCode;

          console.log('Starting saveControlPoint...');
          console.log('Control Point:', this.controlPoint);
          console.log('Company Code:', companyCode);

          // エラーチェック: controlPointが正しく設定されているか
          if (!this.controlPoint || typeof this.controlPoint.x !== 'number' || typeof this.controlPoint.y !== 'number') {
              console.error('Invalid control point data:', this.controlPoint);
              alert('Invalid control point data. Please check your inputs.');
              return;
          }

          const payload = {
              x: this.controlPoint.x,
              y: this.controlPoint.y,
              companyCode: companyCode
          };

          console.log('Payload:', payload);

          try {
              const response = await axios.post('http://127.0.0.1:8000/api/ceList/risk_matrix_possibility/', payload, {
                  headers: {
                      Authorization: `Bearer ${localStorage.getItem('token')}`
                  }
              });

              console.log('Control point saved successfully:', response.data);
              this.loadHistory();
          } catch (error) {
              console.error('Error during saving control point:', error);
              if (error.response) {
                  console.error('Response data:', error.response.data);
              } else {
                  console.error('No response received from server.');
              }
              alert('Failed to save control point. Please try again later.');
          }

          console.log('saveControlPoint finished.');
      },

      setControlPoint(item) {
          this.controlPoint = { x: item.x, y: item.y };
          this.drawChart();
      },
      resetToDefault() {
          this.controlPoint = { x: 3, y: 4 };
          this.saveControlPoint();
          this.drawChart();
      },
      toggleFavorite(index) {
          if (this.favoriteHistory === index) {
              this.favoriteHistory = null;
          } else {
              this.favoriteHistory = index;
              this.loadFavoriteControlPoint(); // ★を切り替えた時にもロードする
          }
      },
      getIndex(value, thresholds) {
          for (let i = 0; i < thresholds.length; i++) {
              if (value < thresholds[i]) {
                  return i;
              }
          }
          return thresholds.length;
      },
      updateRiskText(index) {
          const pm04Index = this.getPm04Index(this.numPm04Occurrences);
          const pm03Index = this.getPm03Index(this.numPm03Occurrences, pm04Index);
          const timeIndex = this.getIndex(this.timeOfOccurrence, [1, 2, 3, 4, 5]);

          const selectedIndex = pm04Index !== null ? pm04Index : pm03Index;

          let riskText = '';
          if (selectedIndex === null || timeIndex === null) {
              riskText = '';
          } else {
              const riskMatrix = this.riskMatrix;
              riskText = riskMatrix[selectedIndex]?.risk[timeIndex] ?? '';
          }

          console.log(`Time of occurrence on PM02: ${this.timeOfOccurrence}, Number of PM03: ${this.numPm03Occurrences}, Number of PM04: ${this.numPm04Occurrences}`);
          console.log(`Selected Index: ${selectedIndex}, Time Index: ${timeIndex}, Risk Text: ${riskText}`);
          this.riskText = this.mapRiskText(riskText);
          console.log(`Emitting risk text to parent: { index: ${index}, probabilityOfFailure: ${this.riskText} }`);
          this.$emit('update-risk-texts', { index, probabilityOfFailure: this.riskText }); // 親にテキストを渡す
      },
      getPm04Index(value) {
          if (value === null || value <= 0) {
              return null;
          } else if (value >= 1 && value < 2) {
              return 3;
          } else if (value >= 2 && value < 3) {
              return 2;
          } else if (value >= 3 && value < 4) {
              return 1;
          } else if (value >= 4) {
              return 0;
          }
      },
      getPm03Index(value, pm04Index) {
          if (value === null || value <= 0 || pm04Index !== null) {
              return null;
          } else if (value < 2) {
              return 5;
          } else if (value >= 2 && value < 3) {
              return 4;
          } else if (value >= 3 && value < 4) {
              return 3;
          } else if (value >= 4 && value < 5) {
              return 2;
          } else if (value >= 5 && value < 6) {
              return 1;
          } else if (value >= 6) {
              return 0;
          }
      },

      mapRiskText(riskText) {
          const textMap = {
              L: 'Review',
              LM: 'Appropriate',
              M: 'Caution',
              H: 'Measures',
              VH: 'Danger'
          };
          return textMap[riskText] || riskText;
      }
  }
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.chart-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 400px;
  margin-top: 40px;
  padding: 0 20px;
}

.pointer-position {
  margin-top: 20px;
  font-size: 16px; /* フォントサイズを大きく変更 */
  font-weight: bold; /* 文字を太字に変更 */
  text-align: center;
}

.controls {
  display: flex;
  justify-content: center; /* 中央揃えに変更 */
  margin-top: 20px; /* Pointer Positionとの間隔を確保 */
}

.controls .ml-3 {
  margin-left: 1rem;
}

.history-container {
  width: 250px;
  margin-left: 20px;
  text-align: center;
}

.history-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.history-item {
  display: flex;
  align-items: center;
}

.star-container {
  margin-right: 10px;
}

.history-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  cursor: pointer;
  border-radius: 5px;
  transition-duration: 0.4s;
  width: 100%;
  max-width: 100%;
}

.history-button:hover {
  background-color: #45a049;
}

.blue-button {
  background-color: #007bff;
  border-color: #007bff;
  color: white;
}

.star-icon {
  cursor: pointer;
  color: black;
  font-size: 1.5em;
}
</style>
