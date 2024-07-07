<template>
  <div id="app">
    <div ref="plotGraph" class="graph"></div>
    <div ref="histogramGraph" class="graph"></div>
    <div ref="costHistogramGraph" class="graph"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'App',
  data() {
    return {
      data: [
        { date: new Date('2023-01-01'), equipmentNo: 1, cost: 1000 },
        { date: new Date('2023-01-02'), equipmentNo: 2, cost: 2000 },
        { date: new Date('2023-01-03'), equipmentNo: 1, cost: 1500 },
        { date: new Date('2023-01-04'), equipmentNo: 3, cost: 3000 },
        { date: new Date('2023-01-05'), equipmentNo: 4, cost: 2500 },
        { date: new Date('2023-01-06'), equipmentNo: 5, cost: 500 },
        { date: new Date('2024-01-01'), equipmentNo: 1, cost: 1100 },
        { date: new Date('2024-01-02'), equipmentNo: 2, cost: 2100 },
        { date: new Date('2024-01-03'), equipmentNo: 1, cost: 1600 },
        { date: new Date('2025-01-04'), equipmentNo: 3, cost: 3100 },
        { date: new Date('2025-01-05'), equipmentNo: 4, cost: 2600 },
        { date: new Date('2023-01-06'), equipmentNo: 5, cost: 600 },
        // さらにデータを追加...
      ],
      faultMap: [
        { date: new Date('2023-02-01'), equipmentNo: 1, cost: 1200, typeOfTask: 'PM04' },
        { date: new Date('2023-03-15'), equipmentNo: 2, cost: 2200, typeOfTask: 'PM03' },
        { date: new Date('2023-05-20'), equipmentNo: 3, cost: 3200, typeOfTask: 'PM04' },
        { date: new Date('2024-07-10'), equipmentNo: 4, cost: 2700, typeOfTask: 'PM03' },
        { date: new Date('2024-09-25'), equipmentNo: 5, cost: 700, typeOfTask: 'PM04' },
      ],
      xScale: null,
      histXScale: null,
      costHistXScale: null,
      dragOffset: 0,
      width: 1000, // 幅を大きく設定
      margin: { top: 50, right: 50, bottom: 50, left: 80 }, // マージンを調整
      plotHeight: 500, // プロットグラフの高さ
      histogramHeight: 300, // ヒストグラムの高さ
      costHistogramHeight: 300, // コストヒストグラムの高さ
      yStartDate: new Date('2023-01-01'), // y軸の開始日
      legendState: {
        event: true,
        PM04: true,
        PM03: true,
        eventCost: true,
        faultCost: true,
      }
    };
  },
  mounted() {
    this.createPlotGraph();
    this.createHistogramGraph();
    this.createCostHistogramGraph();
  },
  methods: {
    createPlotGraph() {
      const { margin, width, plotHeight, yStartDate } = this;
      const graphWidth = width - margin.left - margin.right;
      const height = plotHeight - margin.top - margin.bottom;

      // SVG要素の作成
      const svg = d3
        .select(this.$refs.plotGraph)
        .append('svg')
        .attr('width', width)
        .attr('height', plotHeight + margin.top + margin.bottom)
        .style('background', 'white')
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      // グラフタイトルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', -margin.top / 2)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .style('font-weight', 'bold')
        .text('Precision of the task');

      // x軸の設定
      const xDomain = d3.range(1, 31); // 1から30までの範囲
      this.xScale = d3.scaleBand().domain(xDomain).range([0, graphWidth]).padding(0.1);

      const currentDate = new Date();
      const yEndDate = new Date(yStartDate);
      yEndDate.setMonth(yStartDate.getMonth() + 23);

      // y軸の設定
      this.yScale = d3.scaleTime().domain([new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1), new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1)]).range([height, 0]);

      // データのフィルタリング
      const filteredData = this.data.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));
      const filteredFaultMap = this.faultMap.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));

      // x軸とy軸の描画
      this.xAxis = svg.append('g').call(d3.axisBottom(this.xScale)).attr('transform', `translate(0,${height})`);
      this.yAxis = svg.append('g').call(d3.axisLeft(this.yScale).ticks(d3.timeMonth.every(1)).tickFormat(d3.timeFormat('%Y-%m')));

      // x軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(this.xScale).tickSize(-height).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // y軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .call(d3.axisLeft(this.yScale).tickSize(-graphWidth).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // x軸ラベルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', height + margin.bottom / 1.5)
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Critical equipment No.');

      // y軸ラベルの追加
      svg.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -margin.left / 1.5)
        .attr('dy', '-1.5em') // ラベルを目盛りに近づける
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Date');

      // イベントデータのプロット
      this.circles = svg.selectAll('circle.event')
        .data(filteredData)
        .enter()
        .append('circle')
        .attr('class', 'event')
        .attr('cx', d => this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2)
        .attr('cy', d => this.yScale(d.date))
        .attr('r', 5)
        .style('fill', 'blue');

      // 故障マップのプロット
      this.faultGroups = svg.selectAll('g.fault')
        .data(filteredFaultMap)
        .enter()
        .append('g')
        .attr('class', 'fault')
        .attr('transform', d => `translate(${this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2},${this.yScale(d.date)})`);

      const sizesPM04 = [15, 12, 9, 6, 3];
      const colorsPM04 = ['white', 'black', 'lightblue', 'red', 'yellow'];

      const sizesPM03 = [15, 10, 5];
      const colorsPM03 = ['white', 'black', 'white'];

      filteredFaultMap.forEach(d => {
        const group = this.faultGroups.filter(dd => dd === d);
        if (d.typeOfTask === 'PM04') {
          sizesPM04.forEach((size, i) => {
            group.append('circle')
              .attr('r', size)
              .style('fill', colorsPM04[i])
              .style('stroke', i === 0 ? 'black' : 'none')
              .style('stroke-width', i === 0 ? 1 : 0);
          });
        } else if (d.typeOfTask === 'PM03') {
          sizesPM03.forEach((size, i) => {
            group.append('circle')
              .attr('r', size)
              .style('fill', colorsPM03[i])
              .style('stroke', 'black')
              .style('stroke-width', 1);
          });
        }
      });

      // 縦方向の薄い青色の帯を追加 (PM04のみ)
      this.bands = svg.selectAll('rect.band')
        .data(filteredFaultMap.filter(d => d.typeOfTask === 'PM04'))
        .enter()
        .append('rect')
        .attr('class', 'band')
        .attr('x', d => this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2 - sizesPM04[0]) // 矢の的の最外周の位置に帯を配置
        .attr('y', 0) // 上端から下端まで
        .attr('width', sizesPM04[0] * 2) // 矢の的の最外周の幅に合わせる
        .attr('height', height) // グラフの高さに合わせる
        .style('fill', 'lightblue')
        .style('opacity', 0.3); // 半透明にする

      // PM04と日付を表示するためのテキスト要素を追加
      this.faultGroups.append('text')
        .attr('y', 30) // 円の下に距離を空けて表示
        .attr('text-anchor', 'middle')
        .style('fill', 'red')
        .style('font-size', '10px')
        .selectAll('tspan')
        .data(d => [`${d.typeOfTask}`, `(${d.date.toISOString().split('T')[0]})`])
        .enter()
        .append('tspan')
        .attr('x', 0)
        .attr('dy', (d, i) => i * 12) // 各行の間にスペースを追加
        .text(d => d);

      // イベントデータの凡例の追加
      const eventLegend = svg.append('g').attr('class', 'legend-event');
      eventLegend.append('circle')
        .attr('cx', graphWidth - 120)
        .attr('cy', 10)
        .attr('r', 5)
        .style('fill', 'blue')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('event'));
      eventLegend.append('text')
        .attr('x', graphWidth - 110)
        .attr('y', 15)
        .text('Event')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('event'));

      // PM04の凡例の追加
      const PM04Legend = svg.append('g').attr('class', 'legend-pm04');
      PM04Legend.append('circle')
        .attr('cx', graphWidth - 120)
        .attr('cy', 30)
        .attr('r', 7.5)
        .style('fill', 'yellow')
        .style('stroke', 'black')
        .style('stroke-width', 1)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('PM04'));
      PM04Legend.append('text')
        .attr('x', graphWidth - 110)
        .attr('y', 35)
        .text('PM04')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('PM04'));

      // PM03の凡例の追加
      const PM03Legend = svg.append('g').attr('class', 'legend-pm03');
      PM03Legend.append('circle')
        .attr('cx', graphWidth - 120)
        .attr('cy', 50)
        .attr('r', 7.5)
        .style('fill', 'white')
        .style('stroke', 'black')
        .style('stroke-width', 1)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('PM03'));
      PM03Legend.append('text')
        .attr('x', graphWidth - 110)
        .attr('y', 55)
        .text('PM03')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('PM03'));

      // ドラッグ機能の設定
      const drag = d3.drag()
        .on('drag', (event) => {
          this.dragOffset += event.dx;
          this.updateAxes();
        });

      // ドラッグ機能をSVGに追加
      svg.append('rect')
        .attr('width', graphWidth)
        .attr('height', height)
        .style('fill', 'none')
        .style('pointer-events', 'all')
        .call(drag);
    },
    createHistogramGraph() {
      const { margin, width, histogramHeight } = this;
      const graphWidth = width - margin.left - margin.right;
      const height = histogramHeight - margin.top - margin.bottom;

      // SVG要素の作成
      const svg = d3
        .select(this.$refs.histogramGraph)
        .append('svg')
        .attr('width', width)
        .attr('height', histogramHeight + margin.top + margin.bottom)
        .style('background', 'white')
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      // グラフタイトルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', -margin.top / 2)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .style('font-weight', 'bold')
        .text('Accuracy of the task');

      const currentDate = new Date();

      // データのフィルタリング
      const filteredData = this.data.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));
      const filteredFaultMap = this.faultMap.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));

      // ヒストグラムデータの作成
      const histogramData = d3.rollup(
        filteredData,
        v => v.length,
        d => d.equipmentNo
      );

      const faultHistogramData = d3.rollup(
        filteredFaultMap,
        v => v.length,
        d => d.equipmentNo
      );

      // x軸の設定
      const xDomain = d3.range(1, 31); // 1から30までの範囲
      this.histXScale = d3.scaleBand().domain(xDomain).range([0, graphWidth]).padding(0.1);
      const yScale = d3.scaleLinear().domain([0, d3.max([...histogramData.values(), ...faultHistogramData.values()])]).range([height, 0]);

      // x軸とy軸の描画
      this.histXAxis = svg.append('g').call(d3.axisBottom(this.histXScale)).attr('transform', `translate(0,${height})`);
      this.histYAxis = svg.append('g').call(d3.axisLeft(yScale).ticks(1)); // 目盛り間隔を1に設定

      // x軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(this.histXScale).tickSize(-height).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // y軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .call(d3.axisLeft(yScale).tickSize(-graphWidth).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // x軸ラベルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', height + margin.bottom / 1.5)
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Critical equipment No.');

      // y軸ラベルの追加
      svg.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -margin.left / 1.5)
        .attr('dy', '-1.5em') // ラベルを目盛りに近づける
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Frequency of the task');

      // ヒストグラムのバーの描画
      this.bars = svg.selectAll('rect.event')
        .data(Array.from(histogramData))
        .enter()
        .append('rect')
        .attr('class', 'event')
        .attr('x', d => this.histXScale(d[0]))
        .attr('y', d => yScale(d[1]))
        .attr('width', this.histXScale.bandwidth())
        .attr('height', d => height - yScale(d[1]))
        .style('fill', 'green')
        .style('opacity', 0.5); // 半透明にする

      // 故障マップのヒストグラムのバーの描画
      this.faultBars = svg.selectAll('rect.fault')
        .data(Array.from(faultHistogramData))
        .enter()
        .append('rect')
        .attr('class', 'fault')
        .attr('x', d => this.histXScale(d[0]))
        .attr('y', d => yScale(d[1]))
        .attr('width', this.histXScale.bandwidth())
        .attr('height', d => height - yScale(d[1]))
        .style('fill', 'red')
        .style('opacity', 0.5); // 半透明にする

      // イベントデータの凡例の追加
      const eventLegend = svg.append('g').attr('class', 'legend-event');
      eventLegend.append('rect')
        .attr('x', graphWidth - 120)
        .attr('y', 10)
        .attr('width', 10)
        .attr('height', 10)
        .style('fill', 'green')
        .style('opacity', 0.5)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('event'));
      eventLegend.append('text')
        .attr('x', graphWidth - 105)
        .attr('y', 20)
        .text('Event')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('event'));

      // 故障マップの凡例の追加
      const faultLegend = svg.append('g').attr('class', 'legend-fault');
      faultLegend.append('rect')
        .attr('x', graphWidth - 120)
        .attr('y', 30)
        .attr('width', 10)
        .attr('height', 10)
        .style('fill', 'red')
        .style('opacity', 0.5)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('fault'));
      faultLegend.append('text')
        .attr('x', graphWidth - 105)
        .attr('y', 40)
        .text('Fault')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('fault'));

      // ドラッグ機能の設定
      const drag = d3.drag()
        .on('drag', (event) => {
          this.dragOffset += event.dx;
          this.updateAxes();
        });

      // ドラッグ機能をSVGに追加
      svg.append('rect')
        .attr('width', graphWidth)
        .attr('height', height)
        .style('fill', 'none')
        .style('pointer-events', 'all')
        .call(drag);
    },
    createCostHistogramGraph() {
      const { margin, width, costHistogramHeight } = this;
      const graphWidth = width - margin.left - margin.right;
      const height = costHistogramHeight - margin.top - margin.bottom;

      // SVG要素の作成
      const svg = d3
        .select(this.$refs.costHistogramGraph)
        .append('svg')
        .attr('width', width)
        .attr('height', costHistogramHeight + margin.top + margin.bottom)
        .style('background', 'white')
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      // グラフタイトルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', -margin.top / 2)
        .attr('text-anchor', 'middle')
        .style('font-size', '16px')
        .style('font-weight', 'bold')
        .text('Cost of the task');

      // データのフィルタリング
      const currentDate = new Date();
      const filteredData = this.data.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));
      const filteredFaultMap = this.faultMap.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));

      // 合計コストデータの作成
      const eventCostData = Array.from(d3.rollup(
        filteredData,
        v => d3.sum(v, d => d.cost),
        d => d.equipmentNo
      ), ([equipmentNo, totalCost]) => ({ equipmentNo, totalCost }));

      const faultCostData = Array.from(d3.rollup(
        filteredFaultMap,
        v => d3.sum(v, d => d.cost),
        d => d.equipmentNo
      ), ([equipmentNo, totalCost]) => ({ equipmentNo, totalCost }));

      // x軸の設定
      const xDomain = d3.range(1, 31); // 1から30までの範囲
      this.costHistXScale = d3.scaleBand().domain(xDomain).range([0, graphWidth]).padding(0.1);

      // y軸の設定
      const yMax = d3.max([...eventCostData.map(d => d.totalCost), ...faultCostData.map(d => d.totalCost)]);
      const yScale = d3.scaleLinear().domain([0, yMax]).range([height, 0]);

      // x軸とy軸の描画
      this.costHistXAxis = svg.append('g').call(d3.axisBottom(this.costHistXScale)).attr('transform', `translate(0,${height})`);
      this.costHistYAxis = svg.append('g').call(d3.axisLeft(yScale));

      // x軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(this.costHistXScale).tickSize(-height).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // y軸グリッド線の追加
      svg.append('g')
        .attr('class', 'grid')
        .call(d3.axisLeft(yScale).tickSize(-graphWidth).tickFormat(''))
        .selectAll('line')
        .style('stroke', 'lightgrey')
        .style('stroke-opacity', '0.7')
        .style('shape-rendering', 'crispEdges');

      // x軸ラベルの追加
      svg.append('text')
        .attr('x', graphWidth / 2)
        .attr('y', height + margin.bottom / 1.5)
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Critical equipment No.');

      // y軸ラベルの追加
      svg.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -margin.left / 1.5)
        .attr('dy', '-1.5em') // ラベルを目盛りに近づける
        .attr('text-anchor', 'middle')
        .style('font-size', '12px')
        .text('Cost');

      // コストヒストグラムのバーの描画
      this.costBars = svg.selectAll('rect.cost')
        .data(eventCostData)
        .enter()
        .append('rect')
        .attr('class', 'cost')
        .attr('x', d => this.costHistXScale(d.equipmentNo))
        .attr('y', d => yScale(d.totalCost))
        .attr('width', this.costHistXScale.bandwidth() / 2) // バーの幅を半分にする
        .attr('height', d => height - yScale(d.totalCost))
        .style('fill', 'blue')
        .style('opacity', 0.5); // 半透明にする

      // 故障マップのコストヒストグラムのバーの描画
      this.faultCostBars = svg.selectAll('rect.faultCost')
        .data(faultCostData)
        .enter()
        .append('rect')
        .attr('class', 'faultCost')
        .attr('x', d => this.costHistXScale(d.equipmentNo) + this.costHistXScale.bandwidth() / 2) // 横並びにする
        .attr('y', d => yScale(d.totalCost))
        .attr('width', this.costHistXScale.bandwidth() / 2) // バーの幅を半分にする
        .attr('height', d => height - yScale(d.totalCost))
        .style('fill', 'red')
        .style('opacity', 0.5); // 半透明にする

      // イベントデータの凡例の追加
      const eventCostLegend = svg.append('g').attr('class', 'legend-eventCost');
      eventCostLegend.append('rect')
        .attr('x', graphWidth - 120)
        .attr('y', 10)
        .attr('width', 10)
        .attr('height', 10)
        .style('fill', 'blue')
        .style('opacity', 0.5)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('eventCost'));
      eventCostLegend.append('text')
        .attr('x', graphWidth - 105)
        .attr('y', 20)
        .text('Event Cost')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('eventCost'));

      // 故障マップの凡例の追加
      const faultCostLegend = svg.append('g').attr('class', 'legend-faultCost');
      faultCostLegend.append('rect')
        .attr('x', graphWidth - 120)
        .attr('y', 30)
        .attr('width', 10)
        .attr('height', 10)
        .style('fill', 'red')
        .style('opacity', 0.5)
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('faultCost'));
      faultCostLegend.append('text')
        .attr('x', graphWidth - 105)
        .attr('y', 40)
        .text('Fault Cost')
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle')
        .style('cursor', 'pointer')
        .on('click', () => this.toggleVisibility('faultCost'));

      // ドラッグ機能の設定
      const drag = d3.drag()
        .on('drag', (event) => {
          this.dragOffset += event.dx;
          this.updateAxes();
        });

      // ドラッグ機能をSVGに追加
      svg.append('rect')
        .attr('width', graphWidth)
        .attr('height', height)
        .style('fill', 'none')
        .style('pointer-events', 'all')
        .call(drag);
    },
    updateAxes() {
      const { margin, width, plotHeight } = this;
      const graphWidth = width - margin.left - margin.right;
      const height = plotHeight - margin.top - margin.bottom;
      const xDomain = d3.range(1, 31); // 1から30までの範囲
      const domainLength = xDomain.length;

      const currentOffset = this.dragOffset % graphWidth;
      const visibleStartIndex = Math.floor(-currentOffset / this.xScale.bandwidth());
      const visibleEndIndex = visibleStartIndex + Math.ceil(graphWidth / this.xScale.bandwidth());

      const newDomain = [];
      for (let i = visibleStartIndex; i <= visibleEndIndex; i++) {
        newDomain.push(xDomain[(i + domainLength) % domainLength]);
      }

      const newXScale = this.xScale.copy().domain(newDomain).range([currentOffset, currentOffset + graphWidth]);
      const newHistXScale = this.histXScale.copy().domain(newDomain).range([currentOffset, currentOffset + graphWidth]);
      const newCostHistXScale = this.costHistXScale.copy().domain(newDomain).range([currentOffset, currentOffset + graphWidth]);

      // x軸の更新
      this.xAxis.call(d3.axisBottom(newXScale));
      this.histXAxis.call(d3.axisBottom(newHistXScale));
      this.costHistXAxis.call(d3.axisBottom(newCostHistXScale));

      // プロットグラフの円の位置を更新
      this.circles.attr('cx', d => {
        const posX = newXScale(d.equipmentNo);
        return posX;
      });

      // 縦方向の薄い青色の帯の位置を更新
      this.bands.attr('x', d => {
        const posX = newXScale(d.equipmentNo) + newXScale.bandwidth() / 2 - 15; // 矢の的の最外周の位置に帯を配置
        return posX;
      });

      // 故障マップの位置を更新
      this.faultGroups.attr('transform', d => `translate(${newXScale(d.equipmentNo) + newXScale.bandwidth() / 2},${this.yScale(d.date)})`);

      // ヒストグラムのバーの位置を更新
      this.bars.attr('x', d => {
        const posX = newHistXScale(d[0]);
        return posX;
      });

      // 故障マップのヒストグラムのバーの位置を更新
      this.faultBars.attr('x', d => {
        const posX = newHistXScale(d[0]);
        return posX;
      });

      // コストヒストグラムのバーの位置を更新
      this.costBars.attr('x', d => {
        const posX = newCostHistXScale(d.equipmentNo);
        return posX;
      });

      // 故障マップのコストヒストグラムのバーの位置を更新
      this.faultCostBars.attr('x', d => {
        const posX = newCostHistXScale(d.equipmentNo) + newCostHistXScale.bandwidth() / 2;
        return posX;
      });
    },
    toggleVisibility(type) {
      this.legendState[type] = !this.legendState[type];
      d3.selectAll(`.${type}`).style('display', this.legendState[type] ? null : 'none');
    },
  },
};
</script>

<style>
.graph {
  margin-bottom: 50px;
}
</style>
