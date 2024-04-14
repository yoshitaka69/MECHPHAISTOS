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
    const actualCostData = ref([]);

    const getActualCostData = async () => {
      const companyCode = userStore.companyCode;
      if (!companyCode) {
        console.error('No company code found.');
        return;
      }

      const url = `http://127.0.0.1:8000/api/calculation/summedByCompany/?format=json&companyCode=${companyCode}`;
      try {
        const response = await axios.get(url);
        console.log("API Response:", response.data);  // データ構造を確認

        const currentYear = new Date().getFullYear().toString();
        console.log("Current Year:", currentYear); // 現在の年をログ出力

        // summedActualCostList 内の年に対するフィルタリング
        if (response.data.length > 0 && response.data[0].summedActualCostList) {
          actualCostData.value = response.data[0].summedActualCostList.filter(item => item.year.toString() === currentYear);
          console.log("Filtered Data:", actualCostData.value); // フィルタリング後のデータをログ出力
        } else {
          console.log("No valid data found or improper structure");
        }
      } catch (error) {
        console.error('Error fetching actual cost data:', error);
      }
    };

    onMounted(async () => {
      await getActualCostData();
      const barTraces = actualCostData.value.map(costData => {
        const xValues = Object.keys(costData).filter(key => key.startsWith('sum') || key === 'totalActualCost');
        const yValues = xValues.map(key => parseFloat(costData[key] || 0));
        return {
          x: xValues.map(key => key.replace('sum', '')), // Format month names
          y: yValues,
          type: 'bar',
          name: costData.plant || 'Total Cost'
        };
      });

      const layout = {
        title: 'Total Graph (Planned vs Actual)',
        barmode: 'stack',
        height: 400,
        width: 900,
      };

      // Plot the graph with bar traces
      Plotly.newPlot('Totalrpc', barTraces, layout);
    });

    return {
      actualCostData
    };
  }
};
</script>
