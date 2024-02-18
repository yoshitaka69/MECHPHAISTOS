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

export default {
    data() {
        return {
            sustainabilityData: [],
        };
    },
    mounted() {
        // Sustainabilityデータを取得する関数
        const getSustainabilityData = async () => {
            try {
                // axiosを使用してデータを取得
                const response = await axios.get('http://localhost:3000/Sustainability');
                // Sustainabilityデータを取り出す
                const sustainabilityData = response.data;

                // 各工場のデータごとに処理
                for (const plantData of sustainabilityData) {
                    const wellWaterData = plantData.wellWater;
                    // dateとco2の列だけを抽出して新しいデータ形式に変換
                    const transformedData = wellWaterData.map(entry => ({ date: entry.date, wellWater: entry.wellWater }));
                    // Vueのdataに追加
                    this.sustainabilityData.push({ plant: plantData.plant, wellWaterData: transformedData });
                }
            } catch (error) {
                console.error('Error fetching Sustainability data:', error);
                throw error;
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
  