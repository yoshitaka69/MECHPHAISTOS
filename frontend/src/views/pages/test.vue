<template>
	<div ref="ratingContainer" class="gradient-rating"></div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  
  export default {
	mounted() {
	  this.createGradientRating();
	},
	methods: {
	  createGradientRating() {
		const width = 600;
		const height = 50;
		const sections = 20;
		const sectionWidth = width / sections;
  
		const svg = d3.select(this.$refs.ratingContainer)
		  .append('svg')
		  .attr('width', width)
		  .attr('height', height + 20); // +20 for the labels
  
		// Create gradient
		const gradient = svg.append('defs')
		  .append('linearGradient')
		  .attr('id', 'gradient')
		  .attr('x1', '0%')
		  .attr('y1', '0%')
		  .attr('x2', '100%')
		  .attr('y2', '0%');
  
		gradient.append('stop')
		  .attr('offset', '0%')
		  .attr('stop-color', 'green');
  
		gradient.append('stop')
		  .attr('offset', '33%')
		  .attr('stop-color', 'yellow');
  
		gradient.append('stop')
		  .attr('offset', '66%')
		  .attr('stop-color', 'orange');
  
		gradient.append('stop')
		  .attr('offset', '100%')
		  .attr('stop-color', 'red');
  
		// Draw a single rect with gradient fill
		svg.append('rect')
		  .attr('x', 0)
		  .attr('y', 0)
		  .attr('width', width)
		  .attr('height', height)
		  .attr('fill', 'url(#gradient)');
  
		// Draw section borders
		svg.selectAll('line')
		  .data(d3.range(1, sections))
		  .enter()
		  .append('line')
		  .attr('x1', d => d * sectionWidth)
		  .attr('y1', 0)
		  .attr('x2', d => d * sectionWidth)
		  .attr('y2', height)
		  .attr('stroke', 'black')
		  .attr('stroke-width', 0.5);
  
		// Draw percentage labels
		svg.selectAll('text')
		  .data(d3.range(sections + 1)) // +1 to include 100%
		  .enter()
		  .append('text')
		  .attr('x', d => d * sectionWidth)
		  .attr('y', height + 15)
		  .attr('text-anchor', (d, i) => i === sections ? 'end' : 'middle')
		  .attr('font-size', '12px')
		  .text(d => `${d * 5}%`); // 0% to 100%
  
		// Adjust the last label to not overlap with the previous one
		svg.select(`text:nth-child(${sections + 1})`)
		  .attr('x', width)
		  .attr('text-anchor', 'end');
	  }
	}
  };
  </script>
  
  <style>
  .gradient-rating {
	display: flex;
	justify-content: center;
	margin-top: 20px;
  }
  </style>
  