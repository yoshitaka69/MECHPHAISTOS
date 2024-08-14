<template>
  <div>
    <div ref="chart" class="chart"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'JohnMoubrayBathtubCurveChart',
  props: {
    pattern: {
      type: String,
      required: true,
    },
  },
  mounted() {
    this.drawChart();
    window.addEventListener('resize', this.drawChart);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.drawChart);
  },
  methods: {
    drawChart() {
      // Clear existing chart
      d3.select(this.$refs.chart).select('svg').remove();

      const margin = { top: 10, right: 20, bottom: 20, left: 30 };
      const width = this.$refs.chart.clientWidth - margin.left - margin.right; // 親要素に合わせてリサイズ
      const height = 150 - margin.top - margin.bottom; // 高さを小さく

      const svg = d3
        .select(this.$refs.chart)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      const x = d3.scaleLinear().domain([0, 200]).range([0, width]);
      const y = d3.scaleLinear().domain([0, 1.5]).range([height, 0]);

      const line = d3
        .line()
        .x((d) => x(d.x))
        .y((d) => y(d.y));

      let data;

      switch (this.pattern) {
        case 'A':
          data = d3.range(0, 200).map((x) => ({ x, y: Math.exp(-x / 40) + 0.1 }));
          break;
        case 'B':
          data = d3.range(0, 200).map((x) =>
            x < 140 ? { x, y: 0.1 } : { x, y: 0.1 + (x - 140) / 60 }
          );
          break;
        case 'C':
          data = d3.range(0, 200).map((x) => ({ x, y: 0.1 + 0.0025 * x }));
          break;
        case 'D':
          data = d3.range(0, 200).map((x) => ({ x, y: 0.1 }));
          break;
        case 'E':
          data = d3.range(0, 200).map((x) => ({ x, y: 1 - Math.exp(-x / 40) }));
          break;
        case 'F':
          data = d3.range(0, 200).map((x) =>
            x < 140 ? { x, y: 0.1 } : { x, y: 0.1 * Math.pow(x - 139, 2) }
          );
          break;
        default:
          data = [];
          break;
      }

      svg
        .append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x).ticks(5)) // 軸ラベルを小さく
        .selectAll('text')
        .style('font-size', '10px'); // 軸ラベルのフォントサイズを小さく

      svg.append('g').call(d3.axisLeft(y).ticks(5))
        .selectAll('text')
        .style('font-size', '10px'); // 軸ラベルのフォントサイズを小さく

      svg
        .append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 1.5)
        .attr('d', line);

      svg
        .append('text')
        .attr('x', width / 2)
        .attr('y', height + margin.bottom)
        .attr('text-anchor', 'middle')
        .style('font-size', '12px') // テキストのフォントサイズを小さく
        .text('Time');

      svg
        .append('text')
        .attr('x', -height / 2)
        .attr('y', -margin.left / 2)
        .attr('text-anchor', 'middle')
        .style('font-size', '12px') // テキストのフォントサイズを小さく
        .attr('transform', 'rotate(-90)')
        .text('Failure Rate');
    },
  },
};
</script>

<style scoped>
.chart {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 5px;
  background-color: white;
  width: 100%; 
  height: auto; 
}
</style>
