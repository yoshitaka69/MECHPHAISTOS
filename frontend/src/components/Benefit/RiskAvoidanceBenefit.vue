<template>
  <div class="benefit-container">
    <h2 class="benefit-title">Risk Avoidance Benefit</h2>
    <div class="line-chart-wrapper" ref="lineChart"></div>
    <div class="text-left">
      <p class="cost-text">Risk Avoidance Rate: <span>{{ riskAvoidanceRate }}</span></p>
      <p class="cost-text">Cost Benefit: <span>{{ costBenefit }}</span></p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'RiskAvoidanceBenefit',
  setup() {
    const riskAvoidanceRate = ref('75%'); // Sample data
    const costBenefit = ref('¥1,000,000'); // Sample data

    const drawLineChart = () => {
      const beforeData = [
        { date: '2024-01', value: 80 },
        { date: '2024-02', value: 90 },
        { date: '2024-03', value: 85 },
        { date: '2024-04', value: 88 },
        { date: '2024-05', value: 92 },
      ];

      const afterData = [
        { date: '2024-01', value: 100 },
        { date: '2024-02', value: 110 },
        { date: '2024-03', value: 105 },
        { date: '2024-04', value: 115 },
        { date: '2024-05', value: 120 },
      ];

      const width = 300;
      const height = 150;
      const margin = { top: 20, right: 20, bottom: 30, left: 40 };

      const svg = d3
        .select('.line-chart-wrapper')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3
        .scalePoint()
        .domain(beforeData.map((d) => d.date))
        .range([0, width]);

      const y = d3
        .scaleLinear()
        .domain([0, d3.max(afterData, (d) => d.value)])
        .range([height, 0]);

      const lineBefore = d3
        .line()
        .x((d) => x(d.date))
        .y((d) => y(d.value));

      const lineAfter = d3
        .line()
        .x((d) => x(d.date))
        .y((d) => y(d.value));

      // Draw Before Line
      svg
        .append('path')
        .datum(beforeData)
        .attr('fill', 'none')
        .attr('stroke', '#ff5733')
        .attr('stroke-width', 2)
        .attr('d', lineBefore);

      // Draw After Line
      svg
        .append('path')
        .datum(afterData)
        .attr('fill', 'none')
        .attr('stroke', '#007bff')
        .attr('stroke-width', 2)
        .attr('d', lineAfter);

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
        .attr('x', width - 50)
        .attr('y', height + 30)
        .attr('fill', '#ff5733')
        .text('Before');

      svg
        .append('text')
        .attr('x', width - 100)
        .attr('y', height + 30)
        .attr('fill', '#007bff')
        .text('After');
    };

    onMounted(() => {
      drawLineChart();
    });

    return {
      riskAvoidanceRate,
      costBenefit,
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

.line-chart-wrapper {
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
