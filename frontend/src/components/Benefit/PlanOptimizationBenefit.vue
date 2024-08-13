<template>
  <div class="benefit-container">
    <h2 class="benefit-title">Plan Optimization Benefit</h2>
    <div class="stacked-bar-chart-wrapper" ref="stackedBarChart"></div>
    <div class="text-left">
      <p class="cost-text">Initial Repair Cost: <span>{{ initialCost }}</span></p>
      <p class="cost-text">Updated Repair Cost: <span>{{ updatedCost }}</span></p>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'PlanOptimizationBenefit',
  setup() {
    const initialCost = ref(5000);
    const updatedCost = ref(3000);

    const benefit = computed(() => {
      return initialCost.value - updatedCost.value;
    });

    const drawStackedBarChart = () => {
      const data = [
        { category: 'Before', initial: 4000, updated: 1000 },
        { category: 'After', initial: 2000, updated: 1000 },
      ];

      const width = 300;
      const height = 150;
      const margin = { top: 20, right: 20, bottom: 30, left: 40 };

      const svg = d3
        .select('.stacked-bar-chart-wrapper')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3
        .scaleBand()
        .domain(data.map((d) => d.category))
        .range([0, width])
        .padding(0.2);

      const y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.initial + d.updated)])
        .range([height, 0]);

      const color = d3.scaleOrdinal().domain(['initial', 'updated']).range(['#007bff', '#28a745']);

      svg
        .append('g')
        .selectAll('g')
        .data(d3.stack().keys(['initial', 'updated'])(data))
        .enter()
        .append('g')
        .attr('fill', (d) => color(d.key))
        .selectAll('rect')
        .data((d) => d)
        .enter()
        .append('rect')
        .attr('x', (d) => x(d.data.category))
        .attr('y', (d) => y(d[1]))
        .attr('height', (d) => y(d[0]) - y(d[1]))
        .attr('width', x.bandwidth());

      // Add X Axis
      svg
        .append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

      // Add Y Axis
      svg.append('g').attr('class', 'y-axis').call(d3.axisLeft(y));

      // Add Legend
      svg
        .append('text')
        .attr('x', width - 80)
        .attr('y', height + 30)
        .attr('fill', '#007bff')
        .text('Initial');

      svg
        .append('text')
        .attr('x', width - 150)
        .attr('y', height + 30)
        .attr('fill', '#28a745')
        .text('Updated');
    };

    onMounted(() => {
      drawStackedBarChart();
    });

    return {
      initialCost,
      updatedCost,
      benefit,
    };
  },
};
</script>

<style scoped>
.benefit-container {
  width: 100%;
  text-align: center;
  padding: 20px;
  box-sizing: border-box;
  background-color: #f7faff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.benefit-container:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}

.benefit-title {
  font-size: 2.2em;
  font-weight: bold;
  margin-bottom: 20px;
  color: #0056b3;
}

.stacked-bar-chart-wrapper {
  margin: 20px auto;
  width: 100%;
  max-width: 400px;
  height: auto;
}

.text-left {
  text-align: left;
  padding: 10px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.cost-text {
  font-size: 1.5em;
  margin: 12px 0;
  color: #333;
}

.cost-text span {
  font-weight: bold;
  color: #007bff;
}
</style>
