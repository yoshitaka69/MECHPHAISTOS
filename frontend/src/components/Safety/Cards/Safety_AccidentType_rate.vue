<template>
  <div ref="plotArea" style="width: 100%; height: 100%;">
    <span class="block text-500 font-medium mb-3">Accident type rate</span>
    <div id="SafeAccidentRate" style="width: 100%; height: calc(100% - 30px);"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

export default {
  data() {
    return {
      values: {},
      error: null,
      resizeObserver: null
    };
  },

  mounted() {
    this.initialize();
  },

  beforeDestroy() {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  },

  methods: {
    async initialize() {
      const userStore = useUserStore();
      const userCompanyCode = userStore.companyCode;
      if (!userCompanyCode) {
        console.error("Error: No company code found for the user.");
        return;
      }
      try {
        const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;
        const response = await axios.get(url, {
          headers: { "Content-Type": "application/json" },
          withCredentials: true
        });
        const nearMissData = response.data;
        const allNearMisses = nearMissData.flatMap(companyData => companyData.nearMissList);
        const typeArray = allNearMisses.map(item => item['typeOfAccident']);
        this.values = typeArray.reduce((accumulator, typeOfAccident) => {
          accumulator[typeOfAccident] = (accumulator[typeOfAccident] || 0) + 1;
          return accumulator;
        }, {});
        this.plotGraph();
      } catch (error) {
        console.error("Error fetching data:", error);
      }
      this.setupResizeObserver();
    },

    setupResizeObserver() {
      this.resizeObserver = new ResizeObserver(entries => {
        for (let entry of entries) {
          if (entry.target === this.$refs.plotArea) {
            this.plotGraph();
          }
        }
      });
      this.resizeObserver.observe(this.$refs.plotArea); // 監視対象を設定
    },

    plotGraph() {
      const data = Object.entries(this.values).map(([key, value]) => ({
        label: key,
        value: value
      }));

      console.log('Data for plotting:', data);

      const width = this.$refs.plotArea.clientWidth;
      const height = this.$refs.plotArea.clientHeight - 30; // Adjust for the title height
      const radius = Math.min(width, height) / 2.5; // Smaller radius

      // 既存のSVGを削除
      d3.select("#SafeAccidentRate").selectAll('*').remove();

      const svg = d3.select("#SafeAccidentRate")
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2}, ${height / 2})`);

      const color = d3.scaleOrdinal(d3.schemeCategory10);

      const pie = d3.pie()
        .value(d => d.value);

      const arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

      const outerArc = d3.arc()
        .outerRadius(radius * 1.3)
        .innerRadius(radius * 1.3);

      const g = svg.selectAll('.arc')
        .data(pie(data))
        .enter().append('g')
        .attr('class', 'arc');

      g.append('path')
        .attr('d', arc)
        .style('fill', d => color(d.data.label));

      const text = g.append('text')
        .attr('transform', d => {
          const pos = outerArc.centroid(d);
          pos[0] = radius * 1.35 * (d.endAngle + d.startAngle / 2 > Math.PI ? -1 : 1);
          return `translate(${pos})`;
        })
        .attr('dy', '-0.35em')
        .attr('text-anchor', d => d.endAngle + d.startAngle / 2 > Math.PI ? 'end' : 'start')
        .style('font-size', '12px'); // フォントサイズを小さく設定

      text.append('tspan')
        .attr('x', 0)
        .text(d => d.data.label);

      text.append('tspan')
        .attr('x', 0)
        .attr('dy', '1.2em')
        .text(d => `${Math.round((d.data.value / d3.sum(data, d => d.value)) * 100)}%`);

      g.append('polyline')
        .attr('points', d => {
          const pos = outerArc.centroid(d);
          pos[0] = radius * 1.35 * (d.endAngle + d.startAngle / 2 > Math.PI ? -1 : 1);
          return [arc.centroid(d), outerArc.centroid(d), pos]; // ラベルまで線をつなぐ
        })
        .style('fill', 'none') // 塗りつぶしをなしに設定
        .style('stroke', 'black') // 線の色を黒に設定
        .style('stroke-width', 1); // 線の太さを設定
    }
  }
};
</script>

<style scoped>
#SafeAccidentRate {
  width: 100%;
  height: calc(100% - 30px); /* Adjust for the title height */
}

.block.text-500.font-medium.mb-3 {
    font-weight: bold; /* 太字に設定 */
    font-size: 1.5em; /* 現在のフォントサイズの2倍 */
    color: black; /* 文字色を黒に設定 */
}

.block {
  display: block;
}

.text-500 {
  font-weight: 500;
}

.font-medium {
  font-size: 1.25rem; /* Medium font size */
}

.mb-3 {
  margin-bottom: 1rem; /* Margin bottom */
}
</style>
