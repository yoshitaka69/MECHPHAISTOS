<template>
  <div id="SafeRateContainer" ref="plotArea" style="width: 100%; height: 100%;">
    <span class="block text-500 font-medium mb-3">Safety factor rate</span>
    <div class="graph-wrapper">
      <div id="SafeRate" style="width: 100%; height: 100%;"></div>
    </div>
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
      resizeObserver: null // ResizeObserverを保存
    };
  },

  mounted() {
    const userStore = useUserStore();
    const userCompanyCode = userStore.companyCode;

    if (!userCompanyCode) {
      console.error('Error: No company code found for the user.');
      return;
    }

    const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${userCompanyCode}`;

    axios
      .get(url, {
        headers: {
          'Content-Type': 'application/json'
        },
        withCredentials: true
      })
      .then((response) => {
        console.log('Data fetched successfully:', response.data);
        const nearMissData = response.data;
        const allNearMisses = nearMissData.flatMap((companyData) => companyData.nearMissList);
        const factorArray = allNearMisses.map((item) => item['factor']);

        this.values = factorArray.reduce((accumulator, factor) => {
          accumulator[factor] = (accumulator[factor] || 0) + 1;
          return accumulator;
        }, {});

        console.log('Processed values:', this.values);

        this.$nextTick(() => {
          this.plotGraph(); // DOMの更新後に初期描画
          // ResizeObserverの設定
          this.resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
              this.plotGraph();
            }
          });
          this.resizeObserver.observe(this.$refs.plotArea);
        });
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  },

  beforeDestroy() {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  },

  methods: {
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
      d3.select("#SafeRate").selectAll('*').remove();

      const svg = d3.select("#SafeRate")
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
        .outerRadius(radius * 1.2)
        .innerRadius(radius * 1.2);

      const g = svg.selectAll('.arc')
        .data(pie(data))
        .enter().append('g')
        .attr('class', 'arc');

      g.append('path')
        .attr('d', arc)
        .style('fill', d => color(d.data.label));

      const text = g.append('text')
        .attr('transform', d => `translate(${outerArc.centroid(d)})`)
        .attr('dy', '-0.35em')
        .attr('text-anchor', d => d.endAngle + d.startAngle / 2 > Math.PI ? 'end' : 'start');

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
          pos[0] = radius * 1.25 * (d.endAngle + d.startAngle / 2 > Math.PI ? -1 : 1);
          return [arc.centroid(d), outerArc.centroid(d), pos];
        });
    }
  }
};
</script>

<style scoped>
#SafeRateContainer {
  width: 100%;
  height: 100%;
}

.graph-wrapper {
  width: 100%;
  height: calc(100% - 30px); /* タイトルの高さを考慮 */
  overflow: hidden; /* コンテンツがラッパーを超えないようにする */
}

.block.text-500.font-medium.mb-3 {
  font-weight: bold; /* 太字に設定 */
  font-size: 1.5em; /* 現在のフォントサイズの2倍 */
  color: black; /* 文字色を黒に設定 */
}

#SafeRate {
  width: 100%;
  height: 100%;
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
