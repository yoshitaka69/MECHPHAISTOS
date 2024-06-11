<template>
  <div>
    <div class="controls">
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
  name: 'RiskMatrixPossibilityOfFailureOnlyMatrix',
  props: {
    inputData: {
      type: Array,
      required: true
    }
  },
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
      riskClasses: ['Review', 'Appropriate', 'Caution', 'Measures', 'Danger'],
      savedControlPoints: {
        1: { x: 3, y: 4 },
        2: { x: 3, y: 4 },
        3: { x: 3, y: 4 }
      },
      timeOfOccurrence: null,
      numPm03Occurrences: null,
      numPm04Occurrences: null,
      riskText: '',
      selectedSetting: 1
    };
  },
  watch: {
    inputData: {
      handler(newVal) {
        if (newVal.length > 0) {
          newVal.forEach((item, index) => {
            this.timeOfOccurrence = item.countOfPM02;
            this.numPm03Occurrences = item.countOfPM03;
            this.numPm04Occurrences = item.countOfPM04;
            this.updateRiskText(index);
          });
        }
      },
      immediate: true
    }
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
  font-size: 8px; /* フォントサイズを小さく変更 */
  font-weight: bold;
  white-space: pre-line; /* 改行を有効にする */
  text-align: center; /* テキストを中央揃えにする */
}
</style>
