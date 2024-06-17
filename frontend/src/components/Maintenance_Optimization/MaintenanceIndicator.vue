<template>
	<div class="container">
	  <div ref="ternaryPlot" class="plot-container"></div>
	  <div class="coordinates">
		<p>test1: <span id="coordTest1">0</span>%</p>
		<p>test2: <span id="coordTest2">0</span>%</p>
		<p>test3: <span id="coordTest3">0</span>%</p>
	  </div>
	</div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  
  export default {
	name: 'MaintenanceIndicator',
	props: {
	  width: {
		type: Number,
		default: 500
	  },
	  height: {
		type: Number,
		default: 500
	  }
	},
	mounted() {
	  this.drawTernaryPlot();
	},
	methods: {
	  drawTernaryPlot() {
		const width = this.width;
		const height = this.height;
		const margin = { top: 60, right: 60, bottom: 60, left: 60 };
		const plotWidth = width - margin.left - margin.right;
		const plotHeight = height - margin.top - margin.bottom;
  
		const svg = d3.select(this.$refs.ternaryPlot)
		  .append('svg')
		  .attr('width', width)
		  .attr('height', height)
		  .style('background', 'white')
		  .append('g')
		  .attr('transform', `translate(${margin.left}, ${margin.top})`);
  
		const vertices = [
		  { x: plotWidth / 2, y: 0 },
		  { x: 0, y: plotHeight },
		  { x: plotWidth, y: plotHeight }
		];
  
		svg.append('polygon')
		  .attr('points', vertices.map(d => `${d.x},${d.y}`).join(' '))
		  .attr('stroke', 'black')
		  .attr('fill', '#FFE4C4'); // 三角形の内部を肌色で塗りつぶす
  
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
  
		const nTicks = 5; // 20% 単位にするために5分割
		const tickLabels = ["20%", "40%", "60%", "80%"];
		const lineFunction = d3.line()
		  .x(d => d.x)
		  .y(d => d.y);
  
		for (let i = 1; i < nTicks; i++) {
		  const ratio = i / nTicks;
  
		  // 左側の目盛り
		  const leftTick = [
			{ x: vertices[1].x * (1 - ratio) + vertices[0].x * ratio, y: vertices[1].y * (1 - ratio) + vertices[0].y * ratio },
			{ x: vertices[1].x * (1 - ratio) + vertices[2].x * ratio, y: vertices[1].y * (1 - ratio) + vertices[2].y * ratio }
		  ];
		  svg.append('path')
			.attr('d', lineFunction(leftTick))
			.attr('stroke', 'black')
			.attr('stroke-width', 0.5)
			.attr('fill', 'none');
  
		  svg.append('text')
			.attr('x', leftTick[0].x - 10)
			.attr('y', leftTick[0].y)
			.attr('text-anchor', 'end')
			.attr('font-size', '14px')  // フォントサイズを変更
			.text(tickLabels[i - 1]);
  
		  // 右側の目盛り
		  const rightTick = [
			{ x: vertices[2].x * (1 - ratio) + vertices[0].x * ratio, y: vertices[2].y * (1 - ratio) + vertices[0].y * ratio },
			{ x: vertices[2].x * (1 - ratio) + vertices[1].x * ratio, y: vertices[2].y * (1 - ratio) + vertices[1].y * ratio }
		  ];
		  svg.append('path')
			.attr('d', lineFunction(rightTick))
			.attr('stroke', 'black')
			.attr('stroke-width', 0.5)
			.attr('fill', 'none');
  
		  svg.append('text')
			.attr('x', rightTick[0].x + 10)
			.attr('y', rightTick[0].y)
			.attr('text-anchor', 'start')
			.attr('font-size', '14px')  // フォントサイズを変更
			.text(tickLabels[i - 1]);
  
		  // 上側の目盛りを底辺に移動
		  const topTick = [
			{ x: vertices[0].x * (1 - ratio) + vertices[1].x * ratio, y: vertices[0].y * (1 - ratio) + vertices[1].y * ratio },
			{ x: vertices[0].x * (1 - ratio) + vertices[2].x * ratio, y: vertices[0].y * (1 - ratio) + vertices[2].y * ratio }
		  ];
		  svg.append('path')
			.attr('d', lineFunction(topTick))
			.attr('stroke', 'black')
			.attr('stroke-width', 0.5)
			.attr('fill', 'none');
  
		  // 底辺に目盛りラベルを配置
		  svg.append('text')
			.attr('x', vertices[1].x + (vertices[2].x - vertices[1].x) * ratio)
			.attr('y', plotHeight + 20)
			.attr('text-anchor', 'middle')
			.attr('font-size', '14px')  // フォントサイズを変更
			.text(tickLabels[i - 1]);
		}
  
		// Single Example Point
		const point = { a: 0.3, b: 0.3, c: 0.4 };
  
		const x = point.b * plotWidth + (point.a * plotWidth / 2);
		const y = point.c * plotHeight;
		const cartesianPoint = { x, y };
  
		const drag = d3.drag()
		  .on('start', dragstarted)
		  .on('drag', dragged)
		  .on('end', dragended);
  
		svg.append('circle')
		  .attr('cx', cartesianPoint.x)
		  .attr('cy', cartesianPoint.y)
		  .attr('r', 5)
		  .attr('fill', 'red')
		  .call(drag);
  
		function dragstarted(event, d) {
		  d3.select(this).raise().attr('stroke', 'black');
		}
  
		function dragged(event, d) {
		  d3.select(this)
			.attr('cx', event.x)
			.attr('cy', event.y);
		  updateCoordinates(event.x, event.y);
		}
  
		function dragended(event, d) {
		  d3.select(this).attr('stroke', null);
		  updateCoordinates(event.x, event.y);
		}
  
		function updateCoordinates(x, y) {
		  const a = (plotHeight - y) / plotHeight;
		  const b = (x / plotWidth) * 2 / 2;
		  const c = 1 - a - b;
  
		  document.getElementById('coordTest1').textContent = (a * 100).toFixed(2);
		  document.getElementById('coordTest2').textContent = (b * 100).toFixed(2);
		  document.getElementById('coordTest3').textContent = (c * 100).toFixed(2);
		}
	  }
	}
  };
  </script>
  
  <style scoped>
  .container {
	display: flex;
	flex-direction: column;
	align-items: center;
  }
  
  .plot-container {
	background: white;
  }
  
  .coordinates {
	margin-top: 20px;
	font-family: Arial, sans-serif;
  }
  
  .coordinates p {
	margin: 0;
  }
  </style>
  