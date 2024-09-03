<template>
  <div class="benefit-container">
    <h2 class="benefit-title">Vendor Selection Benefit</h2>
    <div class="bar-chart-wrapper" ref="barChart"></div>
    <div class="text-left">
      <p class="cost-text">Vendor Selection Benefit: <span>{{ vendorSelectionBenefit }}</span></p>
      <p class="cost-text">Cost Benefit: <span>{{ costBenefit }}</span></p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'VendorSelectionBenefit',
  setup() {
    const vendorSelectionBenefit = ref('Better quality and service'); // Sample data
    const costBenefit = ref('¥500,000'); // Sample data

    const drawBarChart = () => {
      const data = [
        { label: 'Before', value: 80 },
        { label: 'After', value: 120 },
      ];

      const width = 300;
      const height = 150;
      const margin = { top: 20, right: 20, bottom: 30, left: 40 };

      const svg = d3
        .select('.bar-chart-wrapper')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3
        .scaleBand()
        .range([0, width])
        .domain(data.map((d) => d.label))
        .padding(0.1);

      const y = d3
        .scaleLinear()
        .range([height, 0])
        .domain([0, d3.max(data, (d) => d.value)]);

      svg
        .selectAll('.bar')
        .data(data)
        .enter()
        .append('rect')
        .attr('class', 'bar')
        .attr('x', (d) => x(d.label))
        .attr('width', x.bandwidth())
        .attr('y', (d) => y(d.value))
        .attr('height', (d) => height - y(d.value))
        .attr('fill', '#007bff');

      svg
        .append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

      svg.append('g').attr('class', 'y-axis').call(d3.axisLeft(y));
    };

    onMounted(() => {
      drawBarChart();
    });

    return {
      vendorSelectionBenefit,
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

.bar-chart-wrapper {
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
