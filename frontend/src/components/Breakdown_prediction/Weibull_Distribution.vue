<template>
	<div ref="chart"></div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  import axios from 'axios';
  
  export default {
	name: 'WeibullChart',
	mounted() {
	  this.drawChart();
	},
	methods: {
	  async drawChart() {
		const response = await axios.get('http://localhost:8000/api/weibull-data/');
		const failureData = response.data.map(d => d.failure_time);
  
		// ワイブル分布のパラメータを計算（ここでは仮定している）
		const shape = 1.5; // 形状パラメータ k
		const scale = 1000; // 尺度パラメータ λ
  
		// D3.jsでグラフを描画
		const margin = { top: 50, right: 30, bottom: 50, left: 60 };
		const width = 800 - margin.left - margin.right;
		const height = 400 - margin.top - margin.bottom;
  
		const svg = d3.select(this.$refs.chart)
		  .append('svg')
		  .attr('width', width + margin.left + margin.right)
		  .attr('height', height + margin.top + margin.bottom)
		  .style('background-color', 'white')
		  .append('g')
		  .attr('transform', `translate(${margin.left},${margin.top})`);
  
		const x = d3.scaleLinear().domain([0, 2000]).range([0, width]);
		const y = d3.scaleLinear().domain([0, 1]).range([height, 0]);
  
		const xAxis = d3.axisBottom(x);
		const yAxis = d3.axisLeft(y);
  
		svg.append('g').attr('transform', `translate(0,${height})`).call(xAxis);
		svg.append('g').call(yAxis);
  
		// 背景の薄い灰色のグリッドライン
		svg.append('g')
		  .attr('class', 'grid')
		  .attr('transform', `translate(0,${height})`)
		  .call(d3.axisBottom(x)
			.tickSize(-height)
			.tickFormat(''))
		  .selectAll('line')
		  .style('stroke', '#d3d3d3')
		  .style('stroke-opacity', 0.5);
  
		svg.append('g')
		  .attr('class', 'grid')
		  .call(d3.axisLeft(y)
			.tickSize(-width)
			.tickFormat(''))
		  .selectAll('line')
		  .style('stroke', '#d3d3d3')
		  .style('stroke-opacity', 0.5);
  
		svg.append('text')
		  .attr('class', 'axis-label')
		  .attr('transform', `translate(${width / 2},${height + margin.bottom - 10})`)
		  .style('text-anchor', 'middle')
		  .text('Time (days)');
  
		svg.append('text')
		  .attr('class', 'axis-label')
		  .attr('transform', 'rotate(-90)')
		  .attr('y', -margin.left + 20)
		  .attr('x', -height / 2)
		  .style('text-anchor', 'middle')
		  .text('Probability');
  
		svg.append('text')
		  .attr('class', 'title')
		  .attr('x', width / 2)
		  .attr('y', -20)
		  .style('text-anchor', 'middle')
		  .text('Weibull Distribution');
  
		// 累積分布関数（CDF）のデータを生成
		const cdfData = d3.range(0, 2000, 10).map(t => {
		  const cdf = 1 - Math.exp(-((t / scale) ** shape));
		  return { t, cdf };
		});
  
		// 生存関数（SF）のデータを生成
		const survivalData = d3.range(0, 2000, 10).map(t => {
		  const survivalProb = Math.exp(-((t / scale) ** shape));
		  return { t, survivalProb };
		});
  
		const lineCDF = d3.line()
		  .x(d => x(d.t))
		  .y(d => y(d.cdf));
  
		const lineSF = d3.line()
		  .x(d => x(d.t))
		  .y(d => y(d.survivalProb));
  
		svg.append('path')
		  .datum(cdfData)
		  .attr('fill', 'none')
		  .attr('stroke', 'steelblue')
		  .attr('stroke-width', 2)
		  .attr('d', lineCDF)
		  .attr('class', 'cdf-line');
  
		svg.append('path')
		  .datum(survivalData)
		  .attr('fill', 'none')
		  .attr('stroke', 'orange')
		  .attr('stroke-width', 2)
		  .attr('d', lineSF)
		  .attr('class', 'sf-line');
  
		// 凡例を追加
		const legend = svg.append('g')
		  .attr('transform', `translate(${width - 230}, 20)`);
  
		legend.append('rect')
		  .attr('width', 220)
		  .attr('height', 60)
		  .attr('fill', 'white')
		  .attr('stroke', 'black')
		  .attr('stroke-width', 1);
  
		legend.append('line')
		  .attr('x1', 10)
		  .attr('y1', 15)
		  .attr('x2', 30)
		  .attr('y2', 15)
		  .attr('stroke', 'steelblue')
		  .attr('stroke-width', 2);
  
		legend.append('text')
		  .attr('x', 40)
		  .attr('y', 15)
		  .attr('dy', '0.35em')
		  .attr('font-size', '8px')
		  .text('CDF (Cumulative Distribution Function)');
  
		legend.append('line')
		  .attr('x1', 10)
		  .attr('y1', 35)
		  .attr('x2', 30)
		  .attr('y2', 35)
		  .attr('stroke', 'orange')
		  .attr('stroke-width', 2);
  
		legend.append('text')
		  .attr('x', 40)
		  .attr('y', 35)
		  .attr('dy', '0.35em')
		  .attr('font-size', '8px')
		  .text('Survival Function');
	  }
	}
  };
  </script>
  
  <style scoped>
  svg {
	font: 10px sans-serif;
  }
  .axis path,
  .axis line {
	fill: none;
	shape-rendering: crispEdges;
	stroke: #000;
  }
  .cdf-line {
	stroke: steelblue;
  }
  .sf-line {
	stroke: orange;
  }
  .title {
	font-size: 16px;
	font-weight: bold;
  }
  .axis-label {
	font-size: 12px;
  }
  .legend text {
	font-size: 8px;
  }
  .grid line {
	stroke: #d3d3d3;
	stroke-opacity: 0.3;
	shape-rendering: crispEdges;
  }
  .grid path {
	stroke-width: 0;
  }
  </style>
  