<template>
    <div>
      <h2>Repairing Costs by Plant</h2>
      <div id="costByPlantChart" class="grid-container"></div>
    </div>
  </template>
  
  <script>
  import { onMounted } from 'vue';
  import * as d3 from 'd3';
  
  export default {
    name: 'CostByPlantChart',
    setup() {
      const renderChart = () => {
        // ダミーデータを定義
        const data = {
          plants: ['Plant A', 'Plant B', 'Plant C', 'Plant D'],
          pm02: { actual: [30000, 20000, 15000, 25000], planned: [28000, 21000, 16000, 23000] },
          pm03: { actual: [32000, 22000, 17000, 26000], planned: [30000, 20000, 15000, 24000] },
          pm04: { actual: [31000, 23000, 16000, 27000], planned: [29000, 22000, 14000, 25000] },
          pm05: { actual: [33000, 24000, 18000, 28000], planned: [31000, 23000, 16000, 26000] },
        };
  
        const margin = { top: 20, right: 30, bottom: 50, left: 50 };
        const width = 400 - margin.left - margin.right;
        const height = 300 - margin.top - margin.bottom;
  
        const svgContainer = d3.select('#costByPlantChart');
  
        const drawBars = (containerId, title, actualData, plannedData) => {
          const svg = svgContainer
            .append('div')
            .attr('class', 'chart-container')
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);
  
          const x = d3.scaleBand()
            .domain(data.plants)
            .range([0, width])
            .padding(0.1);
  
          const y = d3.scaleLinear()
            .domain([0, d3.max([...actualData, ...plannedData])]).nice()
            .range([height, 0]);
  
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
  
          svg.selectAll('.bar.actual')
            .data(actualData)
            .enter()
            .append('rect')
            .attr('class', 'bar actual')
            .attr('x', (d, i) => x(data.plants[i]))
            .attr('y', d => y(d))
            .attr('width', x.bandwidth() / 2)
            .attr('height', d => height - y(d))
            .attr('fill', 'blue');
  
          svg.selectAll('.bar.planned')
            .data(plannedData)
            .enter()
            .append('rect')
            .attr('class', 'bar planned')
            .attr('x', (d, i) => x(data.plants[i]) + x.bandwidth() / 2)
            .attr('y', d => y(d))
            .attr('width', x.bandwidth() / 2)
            .attr('height', d => height - y(d))
            .attr('fill', 'green');
  
          svg.append('text')
            .attr('x', 0)
            .attr('y', -10)
            .attr('text-anchor', 'start')
            .attr('font-weight', 'bold')
            .text(title);
        };
  
        drawBars('pm02Chart', 'PM02 Repairing Costs', data.pm02.actual, data.pm02.planned);
        drawBars('pm03Chart', 'PM03 Repairing Costs', data.pm03.actual, data.pm03.planned);
        drawBars('pm04Chart', 'PM04 Repairing Costs', data.pm04.actual, data.pm04.planned);
        drawBars('pm05Chart', 'PM05 Repairing Costs', data.pm05.actual, data.pm05.planned);
      };
  
      onMounted(() => {
        renderChart();
      });
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
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  