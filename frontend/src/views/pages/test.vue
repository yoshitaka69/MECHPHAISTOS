<template>
  <div>
    <div class="controls">
      <div class="settings" v-for="setting in settingsOptions" :key="setting.value">
        <h3>{{ setting.text }}</h3>
        <button @click="saveControlPoint(setting.value)">保存</button>
        <button @click="resetToDefault(setting.value)">初期値</button>
        <div class="chart-container" :ref="'chartContainer-' + setting.value">
          <div :ref="'chart-' + setting.value"></div>
        </div>
        <div class="pointer-position">
          ポインターの位置: x={{ controlPoints[setting.value].x.toFixed(2) }}, y={{ controlPoints[setting.value].y.toFixed(2) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import * as d3 from 'd3';

const data = [
  { x: 1, y: 0 },
  { x: 7, y: 2.5 },
  { x: 30, y: 5 }
];

const controlPoints = ref({
  1: { x: 7, y: 2.5 },
  2: { x: 7, y: 2.5 },
  3: { x: 7, y: 2.5 }
});

const riskMatrixInitial = [
  { likelihood: 5, description: 'It is or has already happened', risk: ['M', 'H', 'VH', 'VH', 'VH'] },
  { likelihood: 4, description: 'It will probably happen', risk: ['L', 'M', 'H', 'VH', 'VH'] },
  { likelihood: 3, description: 'It could possibly happen', risk: ['L', 'L', 'M', 'H', 'H'] },
  { likelihood: 2, description: 'It is to happen', risk: ['L', 'L', 'L', 'M', 'H'] },
  { likelihood: 1, description: 'It is unlikely to happen', risk: ['L', 'L', 'L', 'L', 'M'] }
];

const riskMatrix = ref([...riskMatrixInitial]);

const settingsOptions = [
  { value: 1, text: 'Low 設定' },
  { value: 2, text: 'Middle 設定' },
  { value: 3, text: 'High 設定' }
];

const resizeObservers = ref({});

const setupResizeObserver = (setting) => {
  const container = document.querySelector(`[ref=chartContainer-${setting}]`);
  resizeObservers.value[setting] = new ResizeObserver(() => {
    drawChart(setting);
  });
  resizeObservers.value[setting].observe(container);
};

const saveControlPoint = (setting) => {
  controlPoints.value[setting] = { ...controlPoints.value[setting] };
};

const resetToDefault = (setting) => {
  controlPoints.value[setting] = { x: 7, y: 2.5 };
  drawChart(setting);
};

const calculateRatios = (x, y) => {
  return {
    xRatio: (x - 1) / 29,
    yRatio: y / 5
  };
};

const updateRiskMatrixColors = (setting) => {
  const { xRatio, yRatio } = calculateRatios(controlPoints.value[setting].x, controlPoints.value[setting].y);

  riskMatrix.value = riskMatrixInitial.map(row => ({
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

const drawRiskMatrix = (svg, width, height, margin, xScale, yScale, colorMap, riskTextMap) => {
  const cellWidth = width / 5;
  const cellHeight = height / 5;

  svg.selectAll('.risk-cell').remove();
  svg.selectAll('.risk-text').remove();

  riskMatrix.value.forEach((row) => {
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

const drawChart = (setting) => {
  const container = document.querySelector(`[ref=chartContainer-${setting}]`);
  const containerWidth = container.offsetWidth;
  const containerHeight = container.offsetHeight;
  const margin = { top: 20, right: 20, bottom: 30, left: 40 };
  const width = containerWidth - margin.left - margin.right;
  const height = containerHeight - margin.top - margin.bottom;

  const svg = d3.select(document.querySelector(`[ref=chart-${setting}]`))
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);

  const xScale = d3.scalePoint()
    .domain([1, 3, 7, 10, 30, '30+'])
    .range([0, width]);

  const yScale = d3.scaleLinear().domain([0, 5]).range([height, 0]);

  const colorMap = {
    'L': '#4c7c04',
    'M': '#f9d909',
    'H': '#f99d09',
    'VH': '#f90909'
  };

  const riskTextMap = {
    'L': 'Low',
    'M': 'Middle',
    'H': 'High',
    'VH': 'High+'
  };

  updateRiskMatrixColors(setting);
  drawRiskMatrix(svg, width, height, margin, xScale, yScale, colorMap, riskTextMap);

  const line = d3.line()
    .x(d => xScale(d.x))
    .y(d => yScale(d.y))
    .curve(d3.curveBasis);

  const dataWithControl = [
    data[0],
    controlPoints.value[setting],
    data[2]
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
    .data([controlPoints.value[setting]])
    .enter()
    .append('circle')
    .attr('class', 'control-point')
    .attr('cx', d => xScale(d.x))
    .attr('cy', d => yScale(d.y))
    .attr('r', 5)
    .attr('fill', 'red')
    .call(d3.drag()
      .on('start', function () {
        d3.select(this).raise().attr('stroke', 'black');
      })
      .on('drag', function (event, d) {
        const invertX = Math.max(1, Math.min(width, event.x));
        const closestX = [1, 3, 7, 10, 30].reduce((prev, curr) => Math.abs(xScale(curr) - invertX) < Math.abs(xScale(prev) - invertX) ? curr : prev);
        const invertY = Math.max(0, Math.min(5, yScale.invert(event.y)));
        d.x = closestX;
        d.y = invertY;
        controlPoints.value[setting] = { x: d.x, y: d.y };
        drawChart(setting);
      })
      .on('end', function () {
        d3.select(this).attr('stroke', null);
      }));
};

onMounted(() => {
  settingsOptions.forEach(setting => {
    drawChart(setting.value);
    setupResizeObserver(setting.value);
  });
});

onBeforeUnmount(() => {
  settingsOptions.forEach(setting => {
    if (resizeObservers.value[setting.value]) {
      resizeObservers.value[setting.value].disconnect();
    }
  });
});
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
