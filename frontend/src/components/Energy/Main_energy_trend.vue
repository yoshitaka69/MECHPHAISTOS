<template>
    <div>

          <v-card-title>Main Energy Trend</v-card-title>
          <div id="main"></div>

    </div>
  </template>
  
  <script>
  import Plotly from "plotly.js-dist-min";
  import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
  
  export default {
    data() {
      return {
        sustainabilityData: [],
      };
    },
    mounted() {
      const getSustainabilityData = async () => {
        try {
          const userStore = useUserStore();
          const userCompanyCode = userStore.companyCode;
  
          if (!userCompanyCode) {
            console.error("Error: No company code found for the user.");
            return; // 処理を中断
          }
  
          // サンプルデータを生成
          const generateSampleData = () => {
            const sampleData = [];
            const startDate = new Date();
            startDate.setDate(startDate.getDate() - 30); // 過去30日間のデータを生成
            for (let i = 0; i < 30; i++) {
              const date = new Date(startDate);
              date.setDate(startDate.getDate() + i);
              sampleData.push({
                date: date.toISOString().split('T')[0], // YYYY-MM-DD形式の文字列
                co2: Math.floor(Math.random() * 100) + 50, // 50から150のランダムな値
              });
            }
            return sampleData;
          };
  
          const sampleSustainabilityData = [
            {
              plant: 'Plant A',
              co2Data: generateSampleData(),
            },
            {
              plant: 'Plant B',
              co2Data: generateSampleData(),
            }
          ];
  
          this.sustainabilityData = sampleSustainabilityData;
        } catch (error) {
          console.error('Error fetching Sustainability data:', error);
        }
      };
  
      // 上記関数の実行
      getSustainabilityData().then(() => {
        // 取得したデータを使ってグラフを描画
        const plotData = this.sustainabilityData.map((plantData, index) => {
          const xValues = plantData.co2Data.map(entry => entry.date);
          const yValues = plantData.co2Data.map(entry => entry.co2);
  
          return {
            type: "scatter",
            mode: "lines",
            fill: "tozeroy", // 下とX軸の間を塗りつぶし
            name: `${plantData.plant} Co2`,
            x: xValues,
            y: yValues,
            line: { color: `#${Math.floor(Math.random() * 16777215).toString(16)}` }
          };
        });
  
        const minDate = Math.min(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => new Date(entry.date).getTime())));
        const maxDate = Math.max(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => new Date(entry.date).getTime())));
  
        const layout = {
          xaxis: {
            autorange: true,
            range: [new Date(minDate), new Date(maxDate)],
            rangeselector: {
              buttons: [
                {
                  count: 1,
                  label: '1m',
                  step: 'month',
                  stepmode: 'backward'
                },
                {
                  count: 6,
                  label: '6m',
                  step: 'month',
                  stepmode: 'backward'
                },
                { step: 'all' }
              ]
            },
            rangeslider: { range: [new Date(minDate), new Date(maxDate)] },
            type: 'date'
          },
          yaxis: {
            autorange: true,
            range: [Math.min(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.co2))), Math.max(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.co2)))],
            type: 'linear'
          }
        };
  
        Plotly.newPlot('main', plotData, layout);
  
        // リアルタイム更新のためのインターバル設定
        setInterval(() => {
          this.sustainabilityData.forEach(plantData => {
            const lastDate = new Date(plantData.co2Data[plantData.co2Data.length - 1].date);
            const newDate = new Date(lastDate);
            newDate.setDate(lastDate.getDate() + 1);
  
            plantData.co2Data.shift(); // 最古のデータを削除
            plantData.co2Data.push({
              date: newDate.toISOString().split('T')[0],
              co2: Math.floor(Math.random() * 100) + 50,
            });
          });
  
          // グラフを再描画
          Plotly.update('main', {
            x: this.sustainabilityData.map(plantData => plantData.co2Data.map(entry => entry.date)),
            y: this.sustainabilityData.map(plantData => plantData.co2Data.map(entry => entry.co2))
          });
        }, 5000); // 5秒ごとに更新
      });
    },
  };
  </script>
  