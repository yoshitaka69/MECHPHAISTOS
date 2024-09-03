<template>
  <div>
    <h2>Repairing Costs for Plant A</h2>
    <div id="costByPlantChart" class="grid-container"></div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'CostByPlantChart',
  setup() {
    const showDifferencePm02 = ref(true);
    const showDifferencePm03 = ref(true);
    const showDifferencePm04 = ref(true);
    const showDifferencePm05 = ref(true);

    const renderChart = () => {
      // グラフをクリア
      d3.select('#costByPlantChart').selectAll('*').remove();

      // ダミーデータを定義
      const data = {
        pm02: { months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], actual: [3000, 2500, 2000, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300], planned: [2800, 2400, 2200, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200] },
        pm03: { months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], actual: [3100, 2600, 2100, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400], planned: [2900, 2500, 2300, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300] },
        pm04: { months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], actual: [3200, 2700, 2200, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500], planned: [3000, 2600, 2400, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400] },
        pm05: { months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], actual: [3300, 2800, 2300, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600], planned: [3100, 2700, 2500, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500] },
      };

      const margin = { top: 20, right: 30, bottom: 50, left: 50 };
      const width = 400 - margin.left - margin.right;
      const height = 300 - margin.top - margin.bottom;

      const svgContainer = d3.select('#costByPlantChart');

      const drawLineChart = (title, months, actualData, plannedData, showDifference, toggleDifferenceDisplay) => {
        const chartDiv = svgContainer
          .append('div')
          .attr('class', 'chart-container');

        const svg = chartDiv
          .append('svg')
          .attr('width', width + margin.left + margin.right)
          .attr('height', height + margin.top + margin.bottom)
          .append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`);

        const x = d3.scaleBand()
          .domain(months)
          .range([0, width])
          .padding(0.1);

        const y = d3.scaleLinear()
          .domain([0, d3.max([...actualData, ...plannedData])]).nice()
          .range([height, 0]);

        const line = d3.line()
          .x((d, i) => x(months[i]) + x.bandwidth() / 2)
          .y(d => y(d));

        svg.append('g')
          .attr('class', 'x-axis')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x))
          .selectAll("text")
          .attr("transform", "rotate(-40)")
          .style("text-anchor", "end");

        svg.append('g')
          .attr('class', 'y-axis')
          .call(d3.axisLeft(y));

        svg.append('path')
          .datum(actualData)
          .attr('fill', 'none')
          .attr('stroke', 'blue')
          .attr('stroke-width', 1.5)
          .attr('d', line);

        svg.append('path')
          .datum(plannedData)
          .attr('fill', 'none')
          .attr('stroke', 'green')
          .attr('stroke-width', 1.5)
          .attr('d', line);

        if (showDifference.value) {
          svg.selectAll('.difference-text')
            .data(actualData)
            .enter()
            .append('text')
            .attr('class', 'difference-text')
            .attr('x', (d, i) => x(months[i]) + x.bandwidth() / 2)
            .attr('y', (d, i) => y((d + plannedData[i]) / 2) - 10)
            .attr('text-anchor', 'middle')
            .attr('fill', 'red')
            .attr('font-size', '16px')
            .attr('font-weight', 'bold')
            .text((d, i) => d - plannedData[i]);
        }

        svg.append('text')
          .attr('x', 0)
          .attr('y', -10)
          .attr('text-anchor', 'start')
          .attr('font-weight', 'bold')
          .text(title);

        chartDiv.append('button')
          .attr('class', 'toggle-button')
          .text(showDifference.value ? 'Hide Differences' : 'Show Differences')
          .on('click', () => {
            showDifference.value = !showDifference.value;
            toggleDifferenceDisplay();
          });
      };

      drawLineChart('PM02 Repairing Costs', data.pm02.months, data.pm02.actual, data.pm02.planned, showDifferencePm02, renderChart);
      drawLineChart('PM03 Repairing Costs', data.pm03.months, data.pm03.actual, data.pm03.planned, showDifferencePm03, renderChart);
      drawLineChart('PM04 Repairing Costs', data.pm04.months, data.pm04.actual, data.pm04.planned, showDifferencePm04, renderChart);
      drawLineChart('PM05 Repairing Costs', data.pm05.months, data.pm05.actual, data.pm05.planned, showDifferencePm05, renderChart);
    };

    onMounted(() => {
      renderChart();
    });

    return {
      showDifferencePm02,
      showDifferencePm03,
      showDifferencePm04,
      showDifferencePm05,
      renderChart,
    };
  },
};
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 20px;
}

.chart-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.toggle-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 4px 8px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.toggle-button:hover {
  background-color: #0056b3;
}
</style>
