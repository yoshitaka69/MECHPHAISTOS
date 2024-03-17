<template>
    <div>
        <v-flex>
            <v-card>
                <v-card-title>Electricity usage trend</v-card-title>
                <div id="elec"></div>
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
                const response = await axios.get('http://127.0.0.1:8000/api/sustainability/elecByCompany/?format=json');
                let sustainabilityData = response.data;

                // Pinia ストアから companyCode を取得
                const userStore = useUserStore();
                const userCompanyCode = userStore.companyCode;

                // ユーザーの companyCode に基づいてデータをフィルタリング
                if (userCompanyCode) {
                    sustainabilityData = sustainabilityData.filter(companyData => companyData.companyCode === userCompanyCode);
                }

                // 各工場のデータごとに処理
                for (const companyData of sustainabilityData) {
                    for (const plantData of companyData.ElecList) {

                        const elecData = plantData.Elec; // ここで elecData を定義


                        // dateとco2の列だけを抽出して新しいデータ形式に変換
                        const transformedData = elecData.map(entry => ({ date: entry.date, elec: entry.elec }));
                        // Vueのdataに追加
                        this.sustainabilityData.push({ plant: plantData.plant, elecData: transformedData });
                    }
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
                const xValues = plantData.elecData.map(entry => entry.date);
                const yValues = plantData.elecData.map(entry => entry.elec);

                // xの最小値と最大値を取得
                const minX = Math.min(...xValues);
                const maxX = Math.max(...xValues);

                return {
                    type: "scatter",
                    mode: "lines",
                    name: `${plantData.plant} ElectricityUsage`,
                    x: xValues,
                    y: yValues,
                    line: { color: `#${Math.floor(Math.random() * 16777215).toString(16)}` }
                };
            });

            // layout内でxの最小値と最大値を取得
            const minDate = Math.min(...this.sustainabilityData.flatMap(plantData => plantData.elecData.map(entry => entry.date)));
            const maxDate = Math.max(...this.sustainabilityData.flatMap(plantData => plantData.elecData.map(entry => entry.date)));

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
                    range: [Math.min(...this.sustainabilityData.flatMap(plantData => plantData.elecData.map(entry => entry.elec))), Math.max(...this.sustainabilityData.flatMap(plantData => plantData.elecData.map(entry => entry.elec)))],
                    type: 'linear'
                }
            };

            Plotly.newPlot('elec', plotData, layout);
        });
    },
};
</script>