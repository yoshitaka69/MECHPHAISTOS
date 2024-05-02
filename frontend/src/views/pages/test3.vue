<template>
  <div class="graph-container">
    <div id="MonthGraph" class="graph"></div>
    <i class="pi pi-arrow-right-arrow-left" style="font-size: 5rem"></i>
    <div id="chart" class="graph"></div>
  </div>
  <button @click="applySimulation">シミュレーション適用</button>
</template>

<script>
import { onMounted, ref } from 'vue';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import axios from 'axios';

export default {
  data() {
    return {
      years: [],
      ppmData: [],
      baseData: [{ x: [1, 2, 3], y: [2, 6, 3], type: 'scatter', mode: 'lines+markers' }],
      simData: [{ x: [1, 2, 3], y: [3, 2, 5], type: 'scatter', mode: 'lines+markers', line: { dash: 'dot' } }],
      layout: { title: 'ベースとシミュレーションのグラフ' },
      config: { responsive: true }
    };
  },
  mounted() {
    this.fetchPPMData();
    Plotly.newPlot('MonthGraph', [...this.baseData, ...this.simData], this.layout, this.config);
  },
  methods: {
    async fetchPPMData() {
      const userStore = useUserStore();
      const url = `http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${userStore.companyCode}`;
      console.log('Fetching PPM data from:', url); // URLログ出力
      try {
        const response = await axios.get(url);
        console.log('PPM data received:', response.data); // 受け取ったデータログ出力
        this.processPPMData(response.data);
      } catch (error) {
        console.error('API error: ', error);
      }
    },
    processPPMData(data) {
      const currentYear = new Date().getFullYear();
      data.forEach((item) => {
        item.EventYearPPMList.forEach((event) => {
          // 過去5年から未来10年までのデータを取得するためにループを調整
          for (let i = -5; i <= 10; i++) {
            const yearKey = i < 0 ? `PPM${-i}YearCostAgo` : `PPM${i}YearCost`;
            if (event[yearKey] !== undefined) {
              // キーが存在する場合のみデータを追加
              this.ppmData.push({
                x: currentYear + i,
                y: parseFloat(event[yearKey])
              });
            }
          }
        });
      });
      console.log('Processed PPM data:', this.ppmData); // 処理後のPPMデータログ出力
      this.drawChart();
    },
    drawChart() {
      let trace2 = {
        x: this.ppmData.map((d) => d.x),
        y: this.ppmData.map((d) => d.y),
        type: 'scatter',
        mode: 'lines+markers',
        name: 'PPM Cost'
      };

      const layout = {
        title: 'PPM by Year',
        xaxis: {
          title: 'Year',
          tickmode: 'linear',
          dtick: 1
        },
        yaxis: {
          title: 'Cost'
        }
      };

      console.log('Drawing chart with trace:', trace2); // グラフ描画前のトレースデータログ出力
      Plotly.newPlot('chart', [trace2], layout);
    },
    applySimulation() {
      // シミュレーションデータの線スタイルを通常の線に変更
      const updatedSimData = this.simData.map(data => ({
        ...data,
        line: { dash: 'solid' }
      }));
      
      // ベースデータに更新したシミュレーションデータを適用
      this.baseData = [...updatedSimData];
      this.simData = []; // シミュレーションデータをクリア
      Plotly.react('MonthGraph', this.baseData, this.layout, this.config);
    }
  }
};
</script>

<style scoped>
.graph-container {
  display: flex;
  justify-content: space-between;
  align-items: center; /* 追加 */
}

.graph {
  width: 45%; /* 2つのグラフの間に少しスペースを残すために100%より少し小さい値を設定 */
}
</style>