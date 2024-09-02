<template>
  <div>
    <h2>Annual Repairing Costs</h2>
    <div id="annualCostChart"></div>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'AnnualCostChart',
  setup() {
    const renderChart = () => {
      // ダミーデータを定義
      const data = {
        years: ['2018', '2019', '2020', '2021', '2022', '2023'],
        costs: [50000, 60000, 55000, 70000, 75000, 80000],
      };

      const margin = { top: 20, right: 30, bottom: 30, left: 40 };
      const width = 800 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3.select('#annualCostChart')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3.scaleBand()
        .domain(data.years)
        .range([0, width])
        .padding(0.1);

      const y = d3.scaleLinear()
        .domain([0, d3.max(data.costs)]).nice()
        .range([height, 0]);

      svg.append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

      svg.append('g')
        .attr('class', 'y-axis')
        .call(d3.axisLeft(y));

      svg.append('path')
        .datum(data.costs)
        .attr('fill', 'none')
        .attr('stroke', 'blue')
        .attr('stroke-width', 1.5)
        .attr('d', d3.line()
          .x((d, i) => x(data.years[i]) + x.bandwidth() / 2)
          .y(d => y(d))
        );
    };

    onMounted(() => {
      renderChart();
    });
  },
};
</script>

<style scoped>
#annualCostChart {
  max-width: 100%;
}
</style>
