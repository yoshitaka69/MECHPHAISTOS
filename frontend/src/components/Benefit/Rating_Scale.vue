<template>
	<div class="container">
	  <div ref="ratingContainer" class="gradient-rating"></div>
	</div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  
  export default {
	mounted() {
	  this.createGradientRating();
	  window.addEventListener('resize', this.resizeGradientRating);
	},
	beforeUnmount() {
	  window.removeEventListener('resize', this.resizeGradientRating);
	},
	methods: {
	  createGradientRating() {
		const containerWidth = this.$refs.ratingContainer.offsetWidth;
		const width = containerWidth - 40; // パディングを引く
		const height = 40; // 高さを縮小
		const sections = 20;
		const sectionWidth = width / sections;
  
		const svg = d3.select(this.$refs.ratingContainer)
		  .append('svg')
		  .attr('width', width + 40) // パディングを含む
		  .attr('height', height + 50) // パディングとラベルの高さを含む
		  .append('g')
		  .attr('transform', 'translate(20, 20)'); // パディングで移動
  
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
  
		// Draw a single rect with initial gray fill
		const rect = svg.append('rect')
		  .attr('x', 0)
		  .attr('y', 0)
		  .attr('width', width)
		  .attr('height', height)
		  .attr('fill', 'lightgray');
  
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
		  .attr('text-anchor', 'middle')
		  .attr('font-size', '10px') // フォントサイズを小さく
		  .text(d => `${d * 5}%`); // 0% to 100%
  
		// Adjust the last label to not overlap with the previous one
		svg.select(`text:nth-child(${sections + 1})`)
		  .attr('x', width + sectionWidth / 2);
  
		// Draw rating labels
		const ratingLabels = [
		  { text: 'Poor', position: 0 },
		  { text: 'Average', position: width * 0.25 },
		  { text: 'Good', position: width * 0.5 },
		  { text: 'Very Good', position: width * 0.75 },
		  { text: 'Excellent', position: width }
		];
  
		svg.selectAll('.rating-label')
		  .data(ratingLabels)
		  .enter()
		  .append('text')
		  .attr('x', d => d.position)
		  .attr('y', -10) // Position above the bar
		  .attr('text-anchor', 'middle')
		  .attr('font-size', '10px') // フォントサイズを小さく
		  .attr('font-weight', 'bold')
		  .text(d => d.text);
  
		// Draw draggable triangle
		const triangle = svg.append('polygon')
		  .attr('points', '0,0 -8,8 8,8') // トライアングルを小さく
		  .attr('fill', 'black')
		  .attr('transform', `translate(0, ${height + 20})`)
		  .call(d3.drag().on('drag', dragged));
  
		function dragged(event) {
		  const x = Math.max(0, Math.min(width, event.x));
		  triangle.attr('transform', `translate(${x}, ${height + 20})`);
		  rect.attr('width', x).attr('fill', 'url(#gradient)');
		}
	  },
	  resizeGradientRating() {
		// Remove existing SVG
		d3.select(this.$refs.ratingContainer).selectAll('*').remove();
		// Recreate with new dimensions
		this.createGradientRating();
	  }
	}
  };
  </script>
  
  <style>
  .container {
	display: flex;
	justify-content: center;
	align-items: center;
	background-color: white;
	padding: 10px;
	border: 1px solid #ccc;
	margin: 20px;
	max-width: 100%;
  }
  
  .gradient-rating {
	display: flex;
	justify-content: center;
	margin-top: 20px;
	width: 100%; /* 親の幅にフィット */
  }
  </style>
  