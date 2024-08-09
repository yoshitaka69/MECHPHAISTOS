<template>
  <div class="chart-container">
    <h1>ワイブル分布のシミュレーション</h1>
    <svg ref="chart" width="800" height="400"></svg>
    <div v-if="parameters.isWearoutIncreasing">
      <p>摩耗故障期は右肩上がりです: 定期整備が有効です。</p>
    </div>
    <div v-else>
      <p>摩耗故障期は右肩下がりです: 定期整備が不要かもしれません。</p>
    </div>
    <div class="parameters">
      <p><strong>Company Code:</strong> {{ parameters.companyCode }}</p>
      <p><strong>CE List No:</strong> {{ parameters.ceListNo }}</p>
      <p><strong>MTTR:</strong> {{ parameters.mttr }} 日</p>
      <p><strong>MTBF:</strong> {{ parameters.mtbf }} 日</p>
      <p><strong>MTTF:</strong> {{ parameters.mttf }} 日</p>
      <p><strong>Total Operating Time:</strong> {{ parameters.totalOperatingTime }} 時間</p>
      <p><strong>Failure Count:</strong> {{ parameters.failureCount }}</p>
      <p><strong>摩耗期バスタブ曲線の傾き:</strong> {{ parameters.slope.toFixed(2) }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import * as d3 from 'd3';
import { useUserStore } from '@/stores/userStore';  // Piniaのストアをインポート

export default {
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },
  data() {
    return {
      times: [],
      pdf_initial: [],
      pdf_random: [],
      pdf_wearout: [],
      bathtub_curve: [],
      parameters: {
        companyCode: '',
        ceListNo: '',
        mttr: 0,
        mtbf: 0,
        mttf: 0,
        totalOperatingTime: 0,
        failureCount: 0,
        slope: 0,
        isWearoutIncreasing: false,
      },
    };
  },
  mounted() {
    this.fetchWeibullData();
    this.fetchParameters();
  },
  methods: {
    async fetchWeibullData() {
      const companyCode = this.userStore.companyCode;  // PiniaからcompanyCodeを取得
      if (!companyCode) {
        console.error('Company code is required');
        return;
      }

      console.log('Sending request with companyCode:', companyCode);  // デバッグ用

      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/weibull_distribution/`, {
          params: { companyCode }  // クエリパラメータとしてcompanyCodeを送信
        });

        console.log('API response:', response.data); // レスポンスデータのログ出力

        if (!response.data || response.data.length === 0) {
          console.error('No data found for this company code');
          return;
        }

        const data = response.data[0];  // 確実にデータが存在することを確認
        if (!data.bathtub_curve) {
          console.error('No valid bathtub_curve data');
          console.log('Data received:', data);
          return;
        }

        this.times = data.times || [];
        this.pdf_initial = data.pdf_initial || [];
        this.pdf_random = data.pdf_random || [];
        this.pdf_wearout = data.pdf_wearout || [];
        this.bathtub_curve = data.bathtub_curve || [];

        this.renderChart();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async fetchParameters() {
      const companyCode = this.userStore.companyCode;  // PiniaからcompanyCodeを取得
      if (!companyCode) {
        console.error('Company code is required');
        return;
      }

      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/reliability/reliabilityByCompany/reliability_parameters/`, {
          params: { companyCode }  // クエリパラメータとしてcompanyCodeを送信
        });

        console.log('Parameter API response:', response.data); // パラメータのレスポンスデータのログ出力

        if (!response.data || response.data.length === 0) {
          console.error('No parameter data found for this company code');
          return;
        }

        const data = response.data[0];  // 最初のパラメータセットを使用
        this.parameters = {
          companyCode: data.companyCode || '',
          ceListNo: data.ceListNo || '',
          mttr: data.mttr || 0,
          mtbf: data.mtbf || 0,
          mttf: data.mttf || 0,
          totalOperatingTime: data.totalOperatingTime || 0,
          failureCount: data.failureCount || 0,
          slope: data.slope || 0,
          isWearoutIncreasing: data.isWearoutIncreasing || false,
        };

        console.log('Parameters:', this.parameters); // パラメータのログ出力
      } catch (error) {
        console.error('Error fetching parameters:', error);
      }
    },
    renderChart() {
      if (!this.bathtub_curve || this.bathtub_curve.length === 0) {
        console.error('No bathtub_curve data to render');
        return;
      }

      const svg = d3.select(this.$refs.chart);
      svg.selectAll('*').remove(); // 以前のチャートをクリア

      const margin = { top: 20, right: 100, bottom: 60, left: 80 };
      const width = +svg.attr('width') - margin.left - margin.right;
      const height = +svg.attr('height') - margin.top - margin.bottom;

      // 時間軸を日数に変換（1日=24時間）
      const x = d3.scaleLinear().domain([0, 125]).range([margin.left, width - margin.right]);
      const y = d3.scaleLinear().domain([0, d3.max(this.bathtub_curve)]).range([height - margin.bottom, margin.top]);

      const line = d3.line()
        .x((d, i) => x(this.times[i] / 24))  // 時間を日数に変換
        .y((d) => y(d));

      // 領域の描画
      svg.append('rect')
        .attr('x', x(0))
        .attr('y', y(d3.max(this.bathtub_curve)))
        .attr('width', x(41.67) - x(0))  // 約1000時間を日数に変換
        .attr('height', height - margin.bottom - y(d3.max(this.bathtub_curve)))
        .attr('fill', 'lightblue')
        .attr('opacity', 0.3);

      svg.append('rect')
        .attr('x', x(41.67))
        .attr('y', y(d3.max(this.bathtub_curve)))
        .attr('width', x(83.33) - x(41.67))  // 約2000時間を日数に変換
        .attr('height', height - margin.bottom - y(d3.max(this.bathtub_curve)))
        .attr('fill', 'lightgreen')
        .attr('opacity', 0.3);

      svg.append('rect')
        .attr('x', x(83.33))
        .attr('y', y(d3.max(this.bathtub_curve)))
        .attr('width', x(125) - x(83.33))  // 約3000時間を日数に変換
        .attr('height', height - margin.bottom - y(d3.max(this.bathtub_curve)))
        .attr('fill', 'lightcoral')
        .attr('opacity', 0.3);

      // グラフを描画
      svg.append('path')
        .datum(this.bathtub_curve)
        .attr('fill', 'none')
        .attr('stroke', 'black')
        .attr('stroke-width', 2)
        .attr('d', line)
        .attr('class', 'line-bathtub');

      // X軸のラベル
      svg.append('g')
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x))
        .append('text')
        .attr('x', width / 2)
        .attr('y', 50)
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .style('font-size', '14px')
        .text('日数');

            // Y軸のラベル
            svg.append('g')
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(y))
        .append('text')
        .attr('transform', 'rotate(-90)')
        .attr('x', -height / 2)
        .attr('y', -60)
        .attr('dy', '0.71em')
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .style('font-size', '14px')
        .text('故障率');

      // 領域の凡例
      const legend = svg.append('g')
        .attr('transform', `translate(${width + margin.right / 2},${margin.top})`);

      legend.append('rect')
        .attr('x', 0)
        .attr('y', 0)
        .attr('width', 10)
        .attr('height', 10)
        .attr('fill', 'lightblue')
        .attr('opacity', 0.3);

      legend.append('text')
        .attr('x', 20)
        .attr('y', 10)
        .text('初期故障期');

      legend.append('rect')
        .attr('x', 0)
        .attr('y', 20)
        .attr('width', 10)
        .attr('height', 10)
        .attr('fill', 'lightgreen')
        .attr('opacity', 0.3);

      legend.append('text')
        .attr('x', 20)
        .attr('y', 30)
        .text('偶発故障期');

      legend.append('rect')
        .attr('x', 0)
        .attr('y', 40)
        .attr('width', 10)
        .attr('height', 10)
        .attr('fill', 'lightcoral')
        .attr('opacity', 0.3);

      legend.append('text')
        .attr('x', 20)
        .attr('y', 50)
        .text('磨耗故障期');

      legend.append('rect')
        .attr('x', 0)
        .attr('y', 60)
        .attr('width', 10)
        .attr('height', 10)
        .attr('fill', 'black');

      legend.append('text')
        .attr('x', 20)
        .attr('y', 70)
        .text('バスタブ曲線');
    },
  },
};
</script>

<style>
.chart-container {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: auto;
  width: fit-content;
}

.parameters {
  margin-top: 20px;
  font-size: 14px;
  text-align: left;
}

.parameters p {
  margin: 5px 0;
}
</style>
