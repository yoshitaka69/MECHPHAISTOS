<template>
    <div>
      <v-card>
        <v-card-title>PM03 Actual cost</v-card-title>
        <div id="rpcPM03"></div>
      </v-card>
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
            const ActualPM03Data = plantData.ActualPM03;
            // monthとcostの列だけを抽出して新しいデータ形式に変換
            const transformedData = ActualPM03Data.map(entry => ({ x: entry.month, y: entry.cost }));
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
          // 取得したデータを使ってグラフを描画
          const plotData = this.RepairingCostData.map((plantData, index) => {
            const xValues = plantData.data.map(entry => entry.x);
            const yValues = plantData.data.map(entry => entry.y);
  
            let trace = {
              x: xValues,
              y: yValues,
              name: plantData.plant,
            };
  
            return trace;
          });
  
          const layout = {
            height: 500,
            width: 600,
            title: 'Repairing Cost',
          };
  
          Plotly.newPlot('rpcPM03', plotData, layout);
        })
        .catch(error => {
          console.error('Error plotting Repairing Cost graph:', error);
          throw error;
        });
    },
  };
  </script>
  