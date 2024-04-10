<template>
    <div>
      <v-card>
        <v-card-title>Planned VS Actual cost</v-card-title>
        <div id="PvsA"></div>
      </v-card>
    </div>
  </template>
  
  <script>
  import Plotly from "plotly.js-dist-min";
  import axios from "axios";
  
  export default {
    data() {
      return {
        RepairingCostDataPlan: [],
        RepairingCostDataActual: [],
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
            const PM02forecastData = plantData.PM02forecast;
            const TotalActualCostData = plantData.TotalActualCost;
  
            // yearとcostの列だけを抽出して新しいデータ形式に変換
            const transformedDataPlan = PM02forecastData.map(entry => ({ x: entry.year, y: entry.cost }));
            const transformedDataActual = TotalActualCostData.map(entry => ({ x: entry.year, y: entry.cost }));
  
            // Vueのdataに追加
            this.RepairingCostDataPlan.push({ plant: plantData.plant, data: transformedDataPlan });
            this.RepairingCostDataActual.push({ plant: plantData.plant, data: transformedDataActual });
  
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
          const plotData = this.RepairingCostDataPlan.map((plantData, index) => {
            const xValues = plantData.data.map(entry => entry.x);
            const yValuesPlan = plantData.data.map(entry => entry.y);
            const yValuesActual = this.RepairingCostDataActual[index].data.map(entry => entry.y);
  
            let traceLine = {
              x: xValues,
              y: yValuesPlan,
              name: plantData.plant,
              type: 'scatter',
            };
  
            let traceBar = {
              x: xValues,
              y: yValuesActual,
              name: plantData.plant,
              type: 'bar',
            };
  
            return [traceLine, traceBar];
          }).flat(); // flat() で2次元の配列を1次元に平坦化
  
          const layout = {
            height: 500,
            width: 600,
            title: 'Repairing Cost',
          };
  
          Plotly.newPlot('PvsA', plotData, layout);
        })
        .catch(error => {
          console.error('Error plotting Repairing Cost graph:', error);
          throw error;
        });
    },
  };
  </script>
  