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
      // バスタブ曲線データ
      const dataBathtub = [
        { time: 0, rate: 4 },
        { time: 1, rate: 3.8 },
        { time: 2, rate: 2 },
        { time: 3, rate: 1.1 },
        { time: 4, rate: 1 },
        { time: 5, rate: 1 },
        { time: 6, rate: 1 },
        { time: 7, rate: 1 },
        { time: 8, rate: 2 },
        { time: 9, rate: 2.8 },
        { time: 10, rate: 3 },
      ];

      // Constant(Random) Failuresデータ
      const dataConstant = [
        { time: 0, rate: 0.8 },
        { time: 10, rate: 0.8 }
      ];

      // Early "Infant Mortality" Failuresデータ
      const dataEarlyFailure = [
        { time: 0, rate: 3 },
        { time: 2, rate: 2 },
        { time: 4, rate: 1 },
        { time: 6, rate: 0.5 },
        { time: 8, rate: 0.2 },
        { time: 10, rate: 0 }
      ];

      // Wear Out Failuresデータ
      const dataWearOutFailure = [
        { time: 0, rate: 0 },
        { time: 2, rate: 0.2 },
        { time: 4, rate: 0.5 },
        { time: 6, rate: 1 },
        { time: 8, rate: 2 },
        { time: 10, rate: 3 }
      ];

      const margin = { top: 20, right: 30, bottom: 50, left: 60 },
            width = 800 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;

      const svg = d3.select(this.$refs.bathtubCurve)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .style('background', 'white')
        .append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

      const x = d3.scaleLinear()
        .domain([0, d3.max(dataBathtub, d => d.time)])
        .range([0, width]);

      const y = d3.scaleLinear()
        .domain([0, d3.max(dataBathtub, d => d.rate)])
        .range([height, 0]);

      // 背景の領域を追加
      svg.append('rect')
        .attr('x', x(0))
        .attr('y', 0)
        .attr('width', x(3) - x(0))
        .attr('height', height)
        .attr('fill', '#e6f7ff');

      svg.append('rect')
        .attr('x', x(3))
        .attr('y', 0)
        .attr('width', x(7) - x(3))
        .attr('height', height)
        .attr('fill', '#ffffcc');

      svg.append('rect')
        .attr('x', x(7))
        .attr('y', 0)
        .attr('width', x(10) - x(7))
        .attr('height', height)
        .attr('fill', '#ffcccc');

      svg.append('g')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x))
        .append('text')
        .attr('x', width / 2)
        .attr('y', 40)
        .attr('fill', '#000')
        .style('text-anchor', 'middle')
        .text('Elapsed Time');

      svg.append('g')
        .call(d3.axisLeft(y))
        .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -50)
        .attr('fill', '#000')
        .style('text-anchor', 'middle')
        .text('Failure Rate');

      // バスタブ曲線を描画
      const lineBathtub = d3.line()
        .x(d => x(d.time))
        .y(d => y(d.rate))
        .curve(d3.curveBasis);

      svg.append('path')
        .datum(dataBathtub)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 2)
        .attr('d', lineBathtub);

      // バスタブ曲線の凡例
      svg.append('text')
        .attr('x', width - 60)
        .attr('y', y(dataBathtub[dataBathtub.length - 1].rate) - 10)
        .attr('fill', 'steelblue')
        .style('font-size', '12px')
        .text('Observed Failure Rate');

      // Constant(Random) Failuresを描画
      const lineConstant = d3.line()
        .x(d => x(d.time))
        .y(d => y(d.rate));

      svg.append('path')
        .datum(dataConstant)
        .attr('fill', 'none')
        .attr('stroke', 'green')
        .attr('stroke-width', 2)
        .attr('d', lineConstant);

      // Constant(Random) Failuresの凡例
      svg.append('text')
        .attr('x', width - 60)
        .attr('y', y(dataConstant[0].rate) - 10)
        .attr('fill', 'green')
        .style('font-size', '12px')
        .text('Constant(Random) Failures');

      // Early "Infant Mortality" Failuresを描画
      const lineEarlyFailure = d3.line()
        .x(d => x(d.time))
        .y(d => y(d.rate))
        .curve(d3.curveBasis);

      svg.append('path')
        .datum(dataEarlyFailure)
        .attr('fill', 'none')
        .attr('stroke', 'orange')
        .attr('stroke-width', 2)
        .attr('stroke-dasharray', '5,5')
        .attr('d', lineEarlyFailure);

      // Early "Infant Mortality" Failuresの凡例
      svg.append('text')
        .attr('x', width - 60)
        .attr('y', y(dataEarlyFailure[dataEarlyFailure.length - 1].rate) - 10)
        .attr('fill', 'orange')
        .style('font-size', '12px')
        .text('Early "Infant Mortality" Failure');

      // Wear Out Failuresを描画
      const lineWearOutFailure = d3.line()
        .x(d => x(d.time))
        .y(d => y(d.rate))
        .curve(d3.curveBasis);

      svg.append('path')
        .datum(dataWearOutFailure)
        .attr('fill', 'none')
        .attr('stroke', 'red')
        .attr('stroke-width', 2)
        .attr('stroke-dasharray', '5,5')
        .attr('d', lineWearOutFailure);

      // Wear Out Failuresの凡例
      svg.append('text')
        .attr('x', width - 60)
        .attr('y', y(dataWearOutFailure[dataWearOutFailure.length - 1].rate) - 10)
        .attr('fill', 'red')
        .style('font-size', '12px')
        .text('Wear Out Failures');

      // 領域ラベル
      svg.append('text')
        .attr('x', x(1.5))
        .attr('y', -5)
        .attr('fill', 'black')
        .style('text-anchor', 'middle')
        .text('Decreasing Failure Rate');

      svg.append('text')
        .attr('x', x(5))
        .attr('y', -5)
        .attr('fill', 'black')
        .style('text-anchor', 'middle')
        .text('Constant Failure Rate');

      svg.append('text')
        .attr('x', x(8.5))
        .attr('y', -5)
        .attr('fill', 'black')
        .style('text-anchor', 'middle')
        .text('Increasing Failure Rate');
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
