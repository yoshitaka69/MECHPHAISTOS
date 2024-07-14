<template>
  <div id="app">
    <div ref="plotGraph" class="graph"></div>
    <div ref="plotLegend" class="legend"></div><CeList />
    <div ref="histogramGraph" class="graph"></div>
    <div ref="histogramLegend" class="legend"></div>
    <div ref="costHistogramGraph" class="graph"></div>
    <div ref="costLegend" class="legend"></div>
  </div>
</template>

<script>
import axios from 'axios';
import * as d3 from 'd3';
import { useUserStore } from '@/stores/userStore'; // Piniaのstoreをインポート
import CeList from './CeList.vue'; // CeListコンポーネントをインポート

export default {
  name: 'App',
  components: {
    CeList, // CeListコンポーネントを登録
  },
  data() {
    return {
      data: [],
      faultData: [],
      predictionData: [],
      xScale: null,
      histXScale: null,
      costHistXScale: null,
      dragOffset: 0,
      width: 1000,
      margin: { top: 50, right: 50, bottom: 50, left: 80 },
      plotHeight: 500,
      histogramHeight: 300,
      costHistogramHeight: 300,
      yStartDate: new Date('2023-01-01'),
      legendState: {
        event: true,
        PM04: true,
        PM03: true,
        eventCost: true,
        faultCost: true,
        prediction: true
      }
    };
  },
  async mounted() {
    try {
      await this.fetchData();
      console.log('Data fetched successfully');
    } catch (error) {
      console.error('Error in fetchData:', error);
    }

    try {
      this.createPlotGraph();
      console.log('Plot graph created successfully');
    } catch (error) {
      console.error('Error in createPlotGraph:', error);
    }

    try {
      this.createHistogramGraph();
      console.log('Histogram graph created successfully');
    } catch (error) {
      console.error('Error in createHistogramGraph:', error);
    }

    try {
      this.createCostHistogramGraph();
      console.log('Cost histogram graph created successfully');
    } catch (error) {
      console.error('Error in createCostHistogramGraph:', error);
    }

    try {
      this.createPlotLegend();
      console.log('Plot legend created successfully');
    } catch (error) {
      console.error('Error in createPlotLegend:', error);
    }

    try {
      this.createHistogramLegend();
      console.log('Histogram legend created successfully');
    } catch (error) {
      console.error('Error in createHistogramLegend:', error);
    }

    try {
      this.createCostLegend();
      console.log('Cost legend created successfully');
    } catch (error) {
      console.error('Error in createCostLegend:', error);
    }
  },
  methods: {
    async fetchEventData() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      try {
        // PPM02のデータを取得
        const responsePPM02 = await axios.get('http://127.0.0.1:8000/api/task/taskListPPM02ByCompany/', {
          params: { companyCode }
        });

        // PPM03のデータを取得
        const responsePPM03 = await axios.get('http://127.0.0.1:8000/api/task/taskListPPM03ByCompany/', {
          params: { companyCode }
        });

        // データの整形
        const eventDataPPM02 = responsePPM02.data.flatMap(item => item.taskListPPM02.map(task => ({
          date: new Date(task.nextEventDate),
          repairCost: parseFloat(task.laborCostOfPPM02),
          ceListNo: task.ceListNo,
          equipmentNo: parseInt(task.ceListNo), // ここでceListNoを整数に変換
          pmType: 'PPM02'
        })));

        const eventDataPPM03 = responsePPM03.data.flatMap(item => item.taskListPPM03.map(task => ({
          date: new Date(task.nextEventDate),
          repairCost: parseFloat(task.laborCostOfPPM03),
          ceListNo: task.ceListNo,
          equipmentNo: parseInt(task.ceListNo), // ここでceListNoを整数に変換
          pmType: 'PPM03'
        })));

        // PPM02とPPM03のデータをマージ
        this.data = [...eventDataPPM02, ...eventDataPPM03];
        console.log('Event data:', this.data);
      } catch (error) {
        console.error('Error fetching event data', error);
      }
    },

    async fetchFaultData() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      try {
        // Fault dataのデータを取得
        const response = await axios.get('http://127.0.0.1:8000/api/reliability/troubleHistoryByCompany/', {
          params: { companyCode }
        });

        // データの整形
        this.faultData = response.data.flatMap(item => item.troubleHistory.map(task => ({
          date: new Date(task.date),
          repairCost: parseFloat(task.repairCost),
          ceListNo: task.ceListNo,
          equipmentNo: parseInt(task.ceListNo), // ここでceListNoを整数に変換
          pmType: task.pmType
        })));

        console.log('Fault data:', this.faultData);
      } catch (error) {
        console.error('Error fetching fault data', error);
      }
    },

    async fetchPredictionData() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      try {
        // Prediction Pointのデータを取得
        const response = await axios.get('http://127.0.0.1:8000/api/reliability/failurePredictionPointByCompany/', {
          params: { companyCode }
        });

        // データの整形
        this.predictionData = response.data.flatMap(item => item.failurePredictionPoint.map(task => ({
          date: new Date(task.date),
          ceListNo: task.ceListNo,
          equipmentNo: parseInt(task.ceListNo), // ここでceListNoを整数に変換
          pmType: task.pmType
        })));

        console.log('Prediction data:', this.predictionData);
      } catch (error) {
        console.error('Error fetching prediction data', error);
      }
    },

    async fetchData() {
      await this.fetchEventData();
      await this.fetchFaultData();
      await this.fetchPredictionData();

      // 既存の処理
      this.faultMap = this.faultData.map(d => ({
        ...d,
        date: new Date(d.date),
        cost: parseFloat(d.repairCost),
        equipmentNo: parseInt(d.ceListNo), // ceListNoを整数に変換
        typeOfTask: d.pmType
      }));

      this.predictionData = this.predictionData.map(d => ({
        ...d,
        date: new Date(d.date),
        equipmentNo: parseInt(d.ceListNo) // ceListNoを整数に変換
      }));
    },

   // createPlotGraphメソッドの修正部分

createPlotGraph() {
    const { margin, width, plotHeight, yStartDate } = this;
    const graphWidth = width - margin.left - margin.right;
    const height = plotHeight - margin.top - margin.bottom;

    // 雷の形状パス
    const lightningPath = "M10 0 L20 20 L0 20 L10 40 L30 10 L10 10 Z";

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
    const filteredPredictionData = this.predictionData.filter(d => d.date >= new Date(currentDate.getFullYear(), currentDate.getMonth() - 12, 1) && d.date <= new Date(currentDate.getFullYear(), currentDate.getMonth() + 12, 1));

    console.log('Filtered event data:', filteredData);
    console.log('Filtered fault data:', filteredFaultMap);
    console.log('Filtered prediction data:', filteredPredictionData);

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
        .attr('cx', d => {
            const posX = this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2;
            console.log('Event cx:', posX, 'for equipmentNo:', d.equipmentNo);
            return posX;
        })
        .attr('cy', d => this.yScale(d.date))
        .attr('r', 5)
        .style('fill', 'blue');

    // 故障マップのプロット
    this.faultGroups = svg.selectAll('g.fault')
        .data(filteredFaultMap)
        .enter()
        .append('g')
        .attr('class', d => `fault ${d.typeOfTask}`)
        .attr('transform', d => {
            const posX = this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2;
            const posY = this.yScale(d.date);
            return `translate(${posX},${posY})`;
        });

    const sizesPM04 = [15, 12, 9, 6, 3];
    const colorsPM04 = ['white', 'black', 'lightblue', 'red', 'yellow'];

    const sizesPM03 = [15, 10, 5];
    const colorsPM03 = ['white', 'black', 'white'];

    filteredFaultMap.forEach(d => {
        const group = this.faultGroups.filter(dd => dd === d);
        if (d.typeOfTask === 'PM04') {
            // 雷の形状を赤色にしてプロット
            group.append('path')
                .attr('d', lightningPath)
                .attr('transform', `scale(0.5) translate(-10,-20)`)
                .style('fill', 'red');
        } else if (d.typeOfTask === 'PM03') {
            sizesPM03.forEach((size, i) => {
                group.append('circle')
                    .attr('r', size)
                    .style('fill', colorsPM03[i])
                    .style('stroke', 'black')
                    .style('stroke-width', 1);
            });
        }

        // テキスト要素の追加
        group.append('text')
            .attr('x', 0)
            .attr('y', 30)
            .attr('text-anchor', 'middle')
            .style('fill', 'red')
            .style('font-size', '10px')
            .selectAll('tspan')
            .data([`${d.pmType}`, `(${d.date.toISOString().split('T')[0]})`])
            .enter()
            .append('tspan')
            .attr('x', 0)
            .attr('dy', (dd, i) => i * 12) // 各行の間にスペースを追加
            .text(dd => dd);
    });

    // 予測データのプロット（的の形状）
    this.predictionPaths = svg.selectAll('g.prediction')
        .data(filteredPredictionData)
        .enter()
        .append('g')
        .attr('class', 'prediction')
        .attr('transform', d => {
            const posX = this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2;
            const posY = this.yScale(d.date);
            return `translate(${posX},${posY})`;
        });

    sizesPM04.forEach((size, i) => {
        this.predictionPaths.append('circle')
            .attr('r', size)
            .style('fill', colorsPM04[i])
            .style('stroke', i === 0 ? 'black' : 'none')
            .style('stroke-width', i === 0 ? 1 : 0);
    });

    // 予測データのテキスト要素の追加
    this.predictionPaths.append('text')
        .attr('x', 0)
        .attr('y', 30)
        .attr('text-anchor', 'middle')
        .style('fill', 'red')
        .style('font-size', '10px')
        .selectAll('tspan')
        .data(d => [`${d.pmType}`, `(${d.date.toISOString().split('T')[0]})`])
        .enter()
        .append('tspan')
        .attr('x', 0)
        .attr('dy', (d, i) => i * 12) // 各行の間にスペースを追加
        .text(d => d);

    // 縦方向の薄い青色の帯を追加 (予測データのみ)
    this.predictionBands = svg.selectAll('rect.predictionBand')
        .data(filteredPredictionData)
        .enter()
        .append('rect')
        .attr('class', 'predictionBand')
        .attr('x', d => this.xScale(d.equipmentNo) + this.xScale.bandwidth() / 2 - sizesPM04[0]) // 矢の的の最外周の位置に帯を配置
        .attr('y', 0) // 上端から下端まで
        .attr('width', sizesPM04[0] * 2) // 矢の的の最外周の幅に合わせる
        .attr('height', height) // グラフの高さに合わせる
        .style('fill', 'lightblue')
        .style('opacity', 0.3); // 半透明にする

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
        .attr('x', d => {
          const posX = this.histXScale(d[0]);
          return posX;
        })
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
        .attr('x', d => {
          const posX = this.histXScale(d[0]);
          return posX;
        })
        .attr('y', d => yScale(d[1]))
        .attr('width', this.histXScale.bandwidth())
        .attr('height', d => height - yScale(d[1]))
        .style('fill', 'red')
        .style('opacity', 0.5); // 半透明にする

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
        v => d3.sum(v, d => d.repairCost),
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
      this.costBars = svg.selectAll('rect.eventCost')
        .data(eventCostData)
        .enter()
        .append('rect')
        .attr('class', 'eventCost')
        .attr('x', d => {
          const posX = this.costHistXScale(d.equipmentNo);
          return posX;
        })
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
        .attr('x', d => {
          const posX = this.costHistXScale(d.equipmentNo) + this.costHistXScale.bandwidth() / 2;
          return posX;
        }) // 横並びにする
        .attr('y', d => yScale(d.totalCost))
        .attr('width', this.costHistXScale.bandwidth() / 2) // バーの幅を半分にする
        .attr('height', d => height - yScale(d.totalCost))
        .style('fill', 'red')
        .style('opacity', 0.5); // 半透明にする

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

    createPlotLegend() {
      const legendData = [
        { label: 'Event', color: 'blue', type: 'event' },
        { label: 'PM04', color: 'yellow', type: 'PM04' },
        { label: 'PM03', color: 'white', type: 'PM03' },
        { label: 'Prediction Point', color: 'orange', type: 'prediction' }
      ];

      const legend = d3.select(this.$refs.plotLegend)
        .append('svg')
        .attr('width', 600)
        .attr('height', 30);

      const legendItem = legend.selectAll('g')
        .data(legendData)
        .enter()
        .append('g')
        .attr('transform', (d, i) => `translate(${i * 150}, 0)`)
        .style('cursor', 'pointer')
        .on('click', (event, d) => this.toggleVisibility(d.type));

      legendItem.append('rect')
        .attr('x', 10)
        .attr('y', 10)
        .attr('width', 20)
        .attr('height', 20)
        .style('fill', d => d.color);

      legendItem.append('text')
        .attr('x', 40)
        .attr('y', 25)
        .text(d => d.label)
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle');
    },

    createHistogramLegend() {
      const legendData = [
        { label: 'Event', color: 'green', type: 'event' },
        { label: 'Fault', color: 'red', type: 'fault' }
      ];

      const legend = d3.select(this.$refs.histogramLegend)
        .append('svg')
        .attr('width', 400)
        .attr('height', 30);

      const legendItem = legend.selectAll('g')
        .data(legendData)
        .enter()
        .append('g')
        .attr('transform', (d, i) => `translate(${i * 150}, 0)`)
        .style('cursor', 'pointer')
        .on('click', (event, d) => this.toggleVisibility(d.type));

      legendItem.append('rect')
        .attr('x', 10)
        .attr('y', 10)
        .attr('width', 20)
        .attr('height', 20)
        .style('fill', d => d.color);

      legendItem.append('text')
        .attr('x', 40)
        .attr('y', 25)
        .text(d => d.label)
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle');
    },

    createCostLegend() {
      const legendData = [
        { label: 'Event Cost', color: 'blue', type: 'eventCost' },
        { label: 'Fault Cost', color: 'red', type: 'faultCost' }
      ];

      const legend = d3.select(this.$refs.costLegend)
        .append('svg')
        .attr('width', 400)
        .attr('height', 30);

      const legendItem = legend.selectAll('g')
        .data(legendData)
        .enter()
        .append('g')
        .attr('transform', (d, i) => `translate(${i * 150}, 0)`)
        .style('cursor', 'pointer')
        .on('click', (event, d) => this.toggleVisibility(d.type));

      legendItem.append('rect')
        .attr('x', 10)
        .attr('y', 10)
        .attr('width', 20)
        .attr('height', 20)
        .style('fill', d => d.color);

      legendItem.append('text')
        .attr('x', 40)
        .attr('y', 25)
        .text(d => d.label)
        .style('font-size', '12px')
        .attr('alignment-baseline', 'middle');
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

      console.log('Updated xScale domain:', newXScale.domain());

      // x軸の更新
      this.xAxis.call(d3.axisBottom(newXScale));
      this.histXAxis.call(d3.axisBottom(newHistXScale));
      this.costHistXAxis.call(d3.axisBottom(newCostHistXScale));

      // プロットグラフの円の位置を更新
      this.circles.attr('cx', d => {
        const posX = newXScale(d.equipmentNo);
        console.log('Event cx:', posX, 'for equipmentNo:', d.equipmentNo);
        return posX;
      });

      // 予測データの円の位置を更新
      this.predictionPaths.attr('transform', d => {
        const posX = newXScale(d.equipmentNo) + newXScale.bandwidth() / 2;
        const posY = this.yScale(d.date);
        return `translate(${posX},${posY})`;
      });

      // 縦方向の薄い青色の帯の位置を更新
      this.predictionBands.attr('x', d => {
        const posX = newXScale(d.equipmentNo) + newXScale.bandwidth() / 2 - 15; // 矢の的の最外周の位置に帯を配置
        return posX;
      });

      // 故障マップの位置を更新
      this.faultGroups.attr('transform', d => {
        const posX = newXScale(d.equipmentNo) + newXScale.bandwidth() / 2;
        const posY = this.yScale(d.date);
        return `translate(${posX},${posY})`;
      });

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
  margin-bottom: 10px;
}
.legend {
  margin-bottom: 50px;
}
</style>
