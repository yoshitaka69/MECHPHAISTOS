<template>
    <div>
        <v-flex>
            <v-card>
                <v-card-title>Co2 trend</v-card-title>
                <div id="co2"></div>
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
                const response = await axios.get('http://127.0.0.1:8000/api/sustainability/co2ByCompany/?format=json');
                // Sustainabilityデータを取り出す
                const sustainabilityData = response.data;

                // 各工場のデータごとに処理
                for (const plantData of sustainabilityData) {
                    const co2Data = plantData.Co2;
                    // dateとco2の列だけを抽出して新しいデータ形式に変換
                    const transformedData = co2Data.map(entry => ({ date: entry.date, co2: entry.co2 }));
                    // Vueのdataに追加
                    this.sustainabilityData.push({ plant: plantData.plant, co2Data: transformedData });
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
                const xValues = plantData.co2Data.map(entry => entry.date);
                const yValues = plantData.co2Data.map(entry => entry.co2);

                // xの最小値と最大値を取得
                const minX = Math.min(...xValues);
                const maxX = Math.max(...xValues);

                return {
                    type: "scatter",
                    mode: "lines",
                    name: `${plantData.plant} Co2`,
                    x: xValues,
                    y: yValues,
                    line: { color: `#${Math.floor(Math.random() * 16777215).toString(16)}` }
                };
            });

            // layout内でxの最小値と最大値を取得
            const minDate = Math.min(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.date)));
            const maxDate = Math.max(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.date)));

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
                    range: [Math.min(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.co2))), Math.max(...this.sustainabilityData.flatMap(plantData => plantData.co2Data.map(entry => entry.co2)))],
                    type: 'linear'
                }
            };

            Plotly.newPlot('co2', plotData, layout);
        });
    },
};
</script>
  