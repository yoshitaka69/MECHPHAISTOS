// src/components/TernaryPlot.vue
<template>
  <div ref="ternaryPlot" class="plot-container"></div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'TernaryPlot',
  mounted() {
    this.drawTernaryPlot();
  },
  methods: {
    drawTernaryPlot() {
      const width = 500;
      const height = 500;
      const margin = {top: 60, right: 60, bottom: 60, left: 60};
      const plotWidth = width - margin.left - margin.right;
      const plotHeight = height - margin.top - margin.bottom;

      const svg = d3.select(this.$refs.ternaryPlot)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .style('background', 'white')
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);

      svg.append('rect')
        .attr('width', plotWidth)
        .attr('height', plotHeight)
        .attr('fill', '#FFE4C4');

      const vertices = [
        {x: plotWidth / 2, y: 0}, 
        {x: 0, y: plotHeight}, 
        {x: plotWidth, y: plotHeight}
      ];

      svg.append('polygon')
        .attr('points', vertices.map(d => `${d.x},${d.y}`).join(' '))
        .attr('stroke', 'black')
        .attr('fill', 'none');

      const labels = ["test1", "test2", "test3"];
      const labelOffset = 20;
      svg.selectAll('.label')
        .data(vertices)
        .enter()
        .append('text')
        .attr('class', 'label')
        .attr('x', (d, i) => i === 0 ? d.x - labelOffset : d.x)
        .attr('y', (d, i) => i === 0 ? d.y - labelOffset : d.y + labelOffset)
        .attr('text-anchor', 'middle')
        .text((d, i) => labels[i]);

      const nTicks = 10;
      const lineFunction = d3.line()
        .x(d => d.x)
        .y(d => d.y);

      for (let i = 1; i < nTicks; i++) {
        const ratio = i / nTicks;
        
        const leftTick = [
          {x: vertices[1].x * (1 - ratio) + vertices[0].x * ratio, y: vertices[1].y * (1 - ratio) + vertices[0].y * ratio},
          {x: vertices[1].x * (1 - ratio) + vertices[2].x * ratio, y: vertices[1].y * (1 - ratio) + vertices[2].y * ratio}
        ];
        svg.append('path')
          .attr('d', lineFunction(leftTick))
          .attr('stroke', 'black')
          .attr('stroke-width', 0.5)
          .attr('fill', 'none');

        const rightTick = [
          {x: vertices[2].x * (1 - ratio) + vertices[0].x * ratio, y: vertices[2].y * (1 - ratio) + vertices[0].y * ratio},
          {x: vertices[2].x * (1 - ratio) + vertices[1].x * ratio, y: vertices[2].y * (1 - ratio) + vertices[1].y * ratio}
        ];
        svg.append('path')
          .attr('d', lineFunction(rightTick))
          .attr('stroke', 'black')
          .attr('stroke-width', 0.5)
          .attr('fill', 'none');

        const topTick = [
          {x: vertices[0].x * (1 - ratio) + vertices[1].x * ratio, y: vertices[0].y * (1 - ratio) + vertices[1].y * ratio},
          {x: vertices[0].x * (1 - ratio) + vertices[2].x * ratio, y: vertices[0].y * (1 - ratio) + vertices[2].y * ratio}
        ];
        svg.append('path')
          .attr('d', lineFunction(topTick))
          .attr('stroke', 'black')
          .attr('stroke-width', 0.5)
          .attr('fill', 'none');
      }

      // Example points
      const points = [
        {a: 0.2, b: 0.5, c: 0.3},
        {a: 0.3, b: 0.3, c: 0.4},
        {a: 0.1, b: 0.8, c: 0.1}
      ];

      const cartesianPoints = points.map(p => {
        const x = p.b * plotWidth + (p.a * plotWidth / 2);
        const y = p.c * plotHeight;
        return {x, y};
      });

      const drag = d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended);

      const circles = svg.selectAll('circle')
        .data(cartesianPoints)
        .enter()
        .append('circle')
        .attr('cx', d => d.x)
        .attr('cy', d => d.y)
        .attr('r', 5)
        .attr('fill', 'red')
        .call(drag);

      function dragstarted(event, d) {
        d3.select(this).raise().attr('stroke', 'black');
      }

      function dragged(event, d) {
        d3.select(this)
          .attr('cx', d.x = event.x)
          .attr('cy', d.y = event.y);
        console.log(`Position: x=${event.x}, y=${event.y}`);
      }

      function dragended(event, d) {
        d3.select(this).attr('stroke', null);
        const a = (2 * (plotHeight - d.y)) / (2 * plotHeight);
        const b = (2 * d.x - plotWidth) / plotWidth;
        const c = 1 - a - b;
        console.log(`Ternary Coordinates: a=${a.toFixed(2)}, b=${b.toFixed(2)}, c=${c.toFixed(2)}`);
      }
    }
  }
};
</script>

<style scoped>
.plot-container {
  background: white;
}
</style>
