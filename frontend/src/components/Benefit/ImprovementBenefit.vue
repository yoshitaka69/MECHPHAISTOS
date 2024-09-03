<template>
  <div class="benefit-container">
    <h2 class="benefit-title">Improvement Benefit</h2>
    <div class="waterfall-chart-wrapper" ref="waterfallChart"></div>
    <div class="text-left">
      <p class="cost-text">Investment Benefit: <span>{{ investmentBenefit }}</span></p>
      <p class="cost-text">Improvement Benefit: <span>{{ improvementBenefit }}</span></p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

export default {
  name: 'ImprovementBenefit',
  setup() {
    const investmentBenefit = ref('Sample Investment Benefit');
    const improvementBenefit = ref('Sample Improvement Benefit');

    const drawWaterfallChart = () => {
      const data = [
        { name: 'Start', value: 1000 },
        { name: 'Investment', value: 200 },
        { name: 'Improvement', value: 150 },
        { name: 'Savings', value: -100 },
        { name: 'Total', value: 0 },
      ];

      // Calculate the cumulative value for each step
      let cumulative = 0;
      data.forEach((d, i) => {
        if (i < data.length - 1) {
          cumulative += d.value;
          d.cumulative = cumulative;
        } else {
          d.cumulative = cumulative;
        }
      });
      data[data.length - 1].value = cumulative;

      const width = 300;
      const height = 150;
      const margin = { top: 20, right: 20, bottom: 30, left: 40 };

      const svg = d3
        .select('.waterfall-chart-wrapper')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3
        .scaleBand()
        .domain(data.map((d) => d.name))
        .range([0, width])
        .padding(0.2);

      const y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.cumulative)])
        .range([height, 0]);

      svg
        .selectAll('.bar')
        .data(data)
        .enter()
        .append('rect')
        .attr('class', 'bar')
        .attr('x', (d) => x(d.name))
        .attr('width', x.bandwidth())
        .attr('y', (d) => y(Math.max(0, d.cumulative)))
        .attr('height', (d) => Math.abs(y(d.value) - y(0)))
        .attr('fill', (d, i) =>
          i === data.length - 1 ? '#007bff' : d.value > 0 ? '#28a745' : '#dc3545'
        );

      svg
        .append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

      svg.append('g').attr('class', 'y-axis').call(d3.axisLeft(y));
    };

    onMounted(() => {
      drawWaterfallChart();
    });

    return {
      investmentBenefit,
      improvementBenefit,
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

.waterfall-chart-wrapper {
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
