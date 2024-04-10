<template>
  <div>
    <v-flex>
      <v-card>
        <v-card-title>Total Graph (Planned vs Actual)</v-card-title>
        <div id="Totalrpc"></div>
      </v-card>
    </v-flex>
  </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";

export default {
  data() {
    return {
      RepairingCostData: [],
    };
  },

  mounted() {
    // 各工場のデータを取得する関数
    const getRepairingCostData = async () => {
      try {
        // axiosを使用してデータを取得
        const response = await axios.get('http://localhost:3000/RepairingCost');
        // RepairingCostデータを取り出す
        const repairingCostData = response.data;

        // 各工場のデータごとに処理
        for (const plantData of repairingCostData) {
          const ActualPM02Data = plantData.ActualPM02;
          // monthとcostの列だけを抽出して新しいデータ形式に変換
          const transformedData = ActualPM02Data.map(entry => ({ x: entry.month, y: entry.cost }));
          // Vueのdataに追加
          this.RepairingCostData.push({ plant: plantData.plant, data: transformedData });
        }
      } catch (error) {
        console.error('Error fetching RepairingCost data:', error);
        throw error;
      }
    };

    // 上記関数の実行
    getRepairingCostData()
      .then(() => {
        // ラインチャート用のトレースを作成
        const lineTraces = this.RepairingCostData.map((plantData, index) => {
          const xValues = plantData.data.map(entry => entry.x);
          const yValues = plantData.data.map(entry => entry.y);

          let trace = {
            x: xValues,
            y: yValues,
            name: plantData.plant,
            type: 'scatter', // ラインチャートに変更
            mode: 'lines+markers',
          };

          return trace;
        });

        // バーチャート用のトレースを追加
        const barTracePM02 = {
          x: ['planned', 'actual'],
          y: [100000, 150000],
          type: 'bar',
          name: 'PM02 Total',
        };

        const barTracePM03 = {
          x: ['planned', 'actual'],
          y: [100000, 150000],
          type: 'bar',
          name: 'PM03 Total',
        };

        const barTracePM04 = {
          x: ['planned', 'actual'],
          y: [100000, 150000],
          type: 'bar',
          name: 'PM04 Total',
        };

        const barTracePM05 = {
          x: ['planned', 'actual'],
          y: [100000, 150000],
          type: 'bar',
          name: 'PM05 Total',
        };

        const layout = {
          height: 350,
          width: 900,
          barmode: 'stack', // スタックされたバーチャート
        };

        // トレースを合成してグラフを描画
        Plotly.newPlot('Totalrpc', [...lineTraces, barTracePM02, barTracePM03, barTracePM04, barTracePM05], layout);
      })
      .catch(error => {
        console.error('Error plotting Repairing Cost graph:', error);
        throw error;
      });
  },
};

</script>
