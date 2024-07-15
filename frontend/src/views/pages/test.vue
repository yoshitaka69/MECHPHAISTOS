<template>
	<div id="app" style="display: flex;">
	  <div style="margin-right: 20px; display: flex; flex-direction: column;">
		<label for="chartType">Select Chart Type:</label>
		<p-dropdown v-model="chartType" :options="chartOptions" optionLabel="label" @change="drawTree"></p-dropdown>
  
		<label for="layoutType">Select Layout Type:</label>
		<p-dropdown v-model="layoutType" :options="layoutOptions" optionLabel="label" @change="drawTree"></p-dropdown>
		
		<label for="backgroundColor">Select Background Color:</label>
		<p-dropdown v-model="backgroundColor" :options="backgroundColorOptions" optionLabel="label" @change="drawTree"></p-dropdown>
  
		<label for="nodeTextDisplay">Select Node Text Display:</label>
		<p-dropdown v-model="nodeTextDisplay" :options="nodeTextDisplayOptions" optionLabel="label" @change="drawTree"></p-dropdown>
		
		<label for="marginx">Margin X:</label>
		<p-input-number v-model.number="marginx" @input="drawTree"></p-input-number>
  
		<label for="marginy">Margin Y:</label>
		<p-input-number v-model.number="marginy" @input="drawTree"></p-input-number>
  
		<label for="radius">Node Radius:</label>
		<p-input-number v-model.number="radius" @input="drawTree"></p-input-number>
  
		<label for="duration">Animation Duration:</label>
		<p-input-number v-model.number="duration" @input="drawTree"></p-input-number>
  
		<label for="leafTextMargin">Leaf Text Margin:</label>
		<p-input-number v-model.number="leafTextMargin" @input="drawTree"></p-input-number>
  
		<label for="nodeTextMargin">Node Text Margin:</label>
		<p-input-number v-model.number="nodeTextMargin" @input="drawTree"></p-input-number>
	  </div>
	  <svg ref="svg" :style="{ backgroundColor: backgroundColor, border: '1px solid black' }" width="800" height="600"></svg>
	</div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  import 'primevue/resources/primevue.min.css';
  import 'primevue/resources/themes/saga-blue/theme.css';
  import 'primeicons/primeicons.css';
  import InputNumber from 'primevue/inputnumber';
  import Dropdown from 'primevue/dropdown';
  
  export default {
	name: 'App',
	components: {
	  'p-input-number': InputNumber,
	  'p-dropdown': Dropdown
	},
	data() {
	  return {
		chartType: 'tree',   // デフォルトのチャートタイプ
		layoutType: 'horizontal', // デフォルトのレイアウトタイプ
		backgroundColor: 'white', // デフォルトの背景色
		nodeTextDisplay: 'all', // デフォルトのノードテキスト表示
		marginx: 160, // デフォルトのXマージン
		marginy: 100, // デフォルトのYマージン
		radius: 4, // デフォルトのノード半径
		duration: 750, // デフォルトのアニメーション継続時間
		leafTextMargin: 6, // デフォルトのリーフノードテキストマージン
		nodeTextMargin: 8, // デフォルトのノードテキストマージン
		chartOptions: [
		  { label: 'Tree', value: 'tree' },
		  { label: 'Cluster', value: 'cluster' }
		],
		layoutOptions: [
		  { label: 'Horizontal', value: 'horizontal' },
		  { label: 'Vertical', value: 'vertical' },
		  { label: 'Circular', value: 'circular' }
		],
		backgroundColorOptions: [
		  { label: 'White', value: 'white' },
		  { label: 'Light Blue', value: 'lightblue' },
		  { label: 'Light Green', value: 'lightgreen' },
		  { label: 'Light Yellow', value: 'lightyellow' }
		],
		nodeTextDisplayOptions: [
		  { label: 'All', value: 'all' },
		  { label: 'Leaves', value: 'leaves' },
		  { label: 'Extremities', value: 'extremities' }
		]
	  };
	},
	mounted() {
	  this.drawTree();
	},
	methods: {
	  drawTree() {
		const data = {
		  name: "Root",
		  children: [
			{ name: "Child 1" },
			{
			  name: "Child 2",
			  children: [
				{ name: "Grandchild 1" },
				{ name: "Grandchild 2" },
				{ name: "Grandchild 3" },
				{ name: "Grandchild 4" },
				{ name: "Grandchild 5" },
				{ name: "Grandchild 6" },
				{ name: "Grandchild 7" },
				{ name: "Grandchild 8" },
				{ name: "Grandchild 9" },
				{ name: "Grandchild 10" }
			  ]
			},
			{ name: "Child 3" },
			{
			  name: "Child 4",
			  children: [
				{ name: "Grandchild 11" },
				{ name: "Grandchild 12" },
				{ name: "Grandchild 13" },
				{ name: "Grandchild 14" },
				{ name: "Grandchild 15" },
				{ name: "Grandchild 16" },
				{ name: "Grandchild 17" },
				{ name: "Grandchild 18" },
				{ name: "Grandchild 19" },
				{ name: "Grandchild 20" }
			  ]
			},
			{ name: "Child 5" },
			{ name: "Child 6" },
			{ name: "Child 7" },
			{ name: "Child 8" },
			{ name: "Child 9" },
			{ name: "Child 10" }
		  ]
		};
  
		const svg = d3.select(this.$refs.svg);
		svg.selectAll('*').remove(); // 既存の描画をクリア
		const width = +svg.attr("width");
		const height = +svg.attr("height");
  
		const zoom = d3.zoom()
		  .scaleExtent([0.5, 2])
		  .on("zoom", event => {
			g.attr("transform", event.transform);
		  });
  
		svg.call(zoom);
  
		const g = svg.append("g");
  
		const root = d3.hierarchy(data);
		let layout;
		
		if (this.chartType === 'tree') {
		  layout = d3.tree();
		} else if (this.chartType === 'cluster') {
		  layout = d3.cluster();
		}
  
		if (this.layoutType === 'horizontal') {
		  layout.size([height, width - this.marginx]);
		  this.drawHorizontalTree(g, root, layout);
		} else if (this.layoutType === 'vertical') {
		  layout.size([width, height - this.marginy]);
		  this.drawVerticalTree(g, root, layout);
		} else if (this.layoutType === 'circular') {
		  this.drawCircularTree(g, root);
		}
	  },
	  shouldDisplayText(node) {
		if (this.nodeTextDisplay === 'all') return true;
		if (this.nodeTextDisplay === 'leaves') return !node.children;
		if (this.nodeTextDisplay === 'extremities') return !node.children || !node.parent;
		return false;
	  },
	  drawHorizontalTree(svg, root, layout) {
		layout(root);
  
		svg.selectAll('.link')
		  .data(root.links())
		  .enter().append('path')
		  .attr('class', 'link')
		  .attr('d', d3.linkHorizontal()
			.x(d => d.y)
			.y(d => d.x))
		  .attr('fill', 'none')
		  .attr('stroke', '#555')
		  .attr('stroke-width', '1.5px');
  
		const node = svg.selectAll('.node')
		  .data(root.descendants())
		  .enter().append('g')
		  .attr('class', 'node')
		  .attr('transform', d => `translate(${d.y},${d.x})`);
  
		node.append('circle')
		  .attr('r', this.radius)
		  .attr('fill', '#999');
  
		node.append('text')
		  .attr('dy', 3)
		  .attr('x', d => d.children ? -this.nodeTextMargin : this.leafTextMargin)
		  .style('text-anchor', d => d.children ? 'end' : 'start')
		  .text(d => this.shouldDisplayText(d) ? d.data.name : '');
	  },
	  drawVerticalTree(svg, root, layout) {
		layout(root);
  
		svg.selectAll('.link')
		  .data(root.links())
		  .enter().append('path')
		  .attr('class', 'link')
		  .attr('d', d3.linkVertical()
			.x(d => d.x)
			.y(d => d.y))
		  .attr('fill', 'none')
		  .attr('stroke', '#555')
		  .attr('stroke-width', '1.5px');
  
		const node = svg.selectAll('.node')
		  .data(root.descendants())
		  .enter().append('g')
		  .attr('class', 'node')
		  .attr('transform', d => `translate(${d.x},${d.y})`);
  
		node.append('circle')
		  .attr('r', this.radius)
		  .attr('fill', '#999');
  
		node.append('text')
		  .attr('dy', 3)
		  .attr('x', d => d.children ? -this.nodeTextMargin : this.leafTextMargin)
		  .style('text-anchor', d => d.children ? 'end' : 'start')
		  .text(d => this.shouldDisplayText(d) ? d.data.name : '');
	  },
	  drawCircularTree(svg, root) {
		const radius = Math.min(+svg.attr("width"), +svg.attr("height")) / 2;
  
		const tree = d3.tree()
		  .size([2 * Math.PI, radius - 100])
		  .separation((a, b) => (a.parent === b.parent ? 1 : 2) / a.depth);
  
		tree(root);
  
		const g = svg.append("g")
		  .attr("transform", `translate(${+svg.attr("width") / 2},${+svg.attr("height") / 2})`);
  
		g.selectAll('.link')
		  .data(root.links())
		  .enter().append('path')
		  .attr('class', 'link')
		  .attr('d', d3.linkRadial()
			.angle(d => d.x)
			.radius(d => d.y))
		  .attr('fill', 'none')
		  .attr('stroke', '#555')
		  .attr('stroke-width', '1.5px');
  
		const node = g.selectAll('.node')
		  .data(root.descendants())
		  .enter().append('g')
		  .attr('class', 'node')
		  .attr('transform', d => `rotate(${d.x * 180 / Math.PI - 90})translate(${d.y})`);
  
		node.append('circle')
		  .attr('r', this.radius)
		  .attr('fill', '#999');
  
		node.append('text')
		  .attr('dy', 3)
		  .attr('x', d => d.x < Math.PI === !d.children ? this.leafTextMargin : -this.nodeTextMargin)
		  .attr('text-anchor', d => d.x < Math.PI === !d.children ? 'start' : 'end')
		  .attr('transform', d => d.x >= Math.PI ? 'rotate(180)' : null)
		  .text(d => this.shouldDisplayText(d) ? d.data.name : '');
	  }
	}
  };
  </script>
  
  <style>
  .link {
	fill: none;
	stroke: #555;
	stroke-width: 1.5px;
  }
  .node circle {
	fill: #999;
  }
  .node text {
	font: 12px sans-serif;
  }
  </style>
  