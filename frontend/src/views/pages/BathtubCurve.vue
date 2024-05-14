<template>
  <div ref="bathtubCurve" class="bathtub-curve"></div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'BathtubCurve',
  mounted() {
    this.drawBathtubCurve();
  },
  methods: {
    drawBathtubCurve() {
      const data = [
        { time: 0, rate: 5 },
        { time: 1, rate: 4 },
        { time: 2, rate: 3 },
        { time: 3, rate: 2.5 },
        { time: 4, rate: 2 },
        { time: 5, rate: 2 },
        { time: 6, rate: 2 },
        { time: 7, rate: 2.5 },
        { time: 8, rate: 3 },
        { time: 9, rate: 4 },
        { time: 10, rate: 5 },
      ];

      const margin = { top: 20, right: 30, bottom: 30, left: 40 },
            width = 800 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;

      const svg = d3.select(this.$refs.bathtubCurve)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

      const x = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.time)])
        .range([0, width]);

      const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.rate)])
        .range([height, 0]);

      svg.append('g')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x));

      svg.append('g')
        .call(d3.axisLeft(y));

      const line = d3.line()
        .x(d => x(d.time))
        .y(d => y(d.rate));

      svg.append('path')
        .datum(data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 2)
        .attr('d', line);
    }
  }
};
</script>

<style scoped>
.bathtub-curve {
  max-width: 800px;
  margin: auto;
}
</style>
