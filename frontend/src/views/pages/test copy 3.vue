<template>
  <div>
    <v-card>
      <v-card-title>Total Graph (Planned vs Actual)</v-card-title>
      <div id="Totalrpc" style="width: 100%; height: 100%"></div>
    </v-card>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
import { useUserStore } from '@/stores/userStore';
import { onMounted, ref } from 'vue';

export default {
  setup() {
    const userStore = useUserStore();
    const repairingCostData = ref([]);
    const actualCostData = ref([]);

    const getRepairingCostData = async () => {
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error('No company code found.');
        return;
      }

      const url = `http://127.0.0.1:8000/api/repairingCost/PPM02ByCompany/?format=json&companyCode=${companyCode}`;
      try {
        const response = await axios.get(url);
        console.log("Repairing Cost Data:", response.data);  // レスポンスデータのログ出力
        repairingCostData.value = response.data[0]?.plannedPM02List || [];
        actualCostData.value = response.data[0]?.actualCostList || []; // 実際のコストリストを取得
      } catch (error) {
        console.error('Error fetching Repairing Cost data:', error);
      }
    };

    onMounted(async () => {
      await getRepairingCostData();
      const lineTraces = [];
      const barTraces = [];

      repairingCostData.value.forEach(plant => {
        plant.plannedPM02.forEach(pmData => {
          const xValues = Object.keys(pmData).filter(key => key !== 'companyCode' && key !== 'plant' && key !== 'year');
          const yValues = xValues.map(key => parseFloat(pmData[key] || 0));
          
          const trace = {
            x: xValues,
            y: yValues,
            type: 'scatter',
            mode: 'lines+markers',
            name: plant.plant
          };
          lineTraces.push(trace);
        });
      });

      // 実際のコストのバーチャートを生成
      actualCostData.value.forEach(costData => {
        const xValues = ['Total Actual Cost']; // すべてのバーを同じカテゴリに配置
        const yValues = [parseFloat(costData.totalCost || 0)];

        const barTrace = {
          x: xValues,
          y: yValues,
          type: 'bar',
          name: costData.plant
        };
        barTraces.push(barTrace);
      });

      const layout = {
        title: 'Total Graph (Planned vs Actual)',
        barmode: 'stack',
        height: 400,
        width: 900,
      };

      // ラインとバーチャートのトレースを合成してグラフを描画
      Plotly.newPlot('Totalrpc', [...lineTraces, ...barTraces], layout);
    });

    return {
      repairingCostData,
      actualCostData
    };
  }
};
</script>



