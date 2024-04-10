<template>
    <div>
        <v-flex>
            <v-card>
                <v-card-title>Well Water trend</v-card-title>
                <div id="wellWater"></div>
            </v-card>
        </v-flex>
    </div>
</template>

<script>
import Plotly from "plotly.js-dist-min";
import axios from "axios";
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

        const url = `http://127.0.0.1:8000/api/sustainability/wellWaterByCompany/?format=json&companyCode=${userCompanyCode}`;
        const response = await axios.get(url);
        console.log("Fetched Sustainability Data:", response.data); // データ取得ログ

        let sustainabilityData = response.data;
        for (const companyData of sustainabilityData) {
          for (const plantData of companyData.WellWaterList) {
            const wellWaterData = plantData.WellWater;
            const transformedData = wellWaterData.map(entry => ({ date: entry.date, wellWater: entry.wellWater }));
            this.sustainabilityData.push({ plant: plantData.plant, wellWaterData: transformedData });
          }
        }
      } catch (error) {
        console.error('Error fetching Sustainability data:', error);
        if (error.response) {
          // サーバーからの応答が存在する場合、その詳細をログ出力
          console.log("Error Response:", error.response);
        }
      }
    };
        // 上記関数の実行
        getSustainabilityData().then(() => {
            // 取得したデータを使ってグラフを描画
            const plotData = this.sustainabilityData.map((plantData, index) => {
                const xValues = plantData.wellWaterData.map(entry => entry.date);
                const yValues = plantData.wellWaterData.map(entry => entry.wellWater);

                // xの最小値と最大値を取得
                const minX = Math.min(...xValues);
                const maxX = Math.max(...xValues);

                return {
                    type: "scatter",
                    mode: "lines",
                    name: `${plantData.plant} wellWater`,
                    x: xValues,
                    y: yValues,
                    line: { color: `#${Math.floor(Math.random() * 16777215).toString(16)}` }
                };
            });

            // layout内でxの最小値と最大値を取得
            const minDate = Math.min(...this.sustainabilityData.flatMap(plantData => plantData.wellWaterData.map(entry => entry.date)));
            const maxDate = Math.max(...this.sustainabilityData.flatMap(plantData => plantData.wellWaterData.map(entry => entry.date)));

            const layout = {
                xaxis: {
                    autorange: true,
                    range: [minDate, maxDate],
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
                    rangeslider: { range: [minDate, maxDate] },
                    type: 'date'
                },
                yaxis: {
                    autorange: true,
                    range: [Math.min(...this.sustainabilityData.flatMap(plantData => plantData.wellWaterData.map(entry => entry.wellWater))), Math.max(...this.sustainabilityData.flatMap(plantData => plantData.wellWaterData.map(entry => entry.wellWater)))],
                    type: 'linear'
                }
            };

            Plotly.newPlot('wellWater', plotData, layout);
        });
    },
};
</script>