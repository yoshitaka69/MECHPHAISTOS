<template>
    <div style="width: 100%; height: 100%;">
        PM02 Actual cost
        <div id="rpcPM02A" style="width: 100%; height: 100%;"></div>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
    data() {
        return {
            RepairingCostData: []
        };
    },

    mounted() {
        const graphContainer = document.getElementById('rpcPM02A');
        const resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
                const { width, height } = entry.contentRect;
                Plotly.relayout('rpcPM02A', { width, height });
            }
        });

        resizeObserver.observe(graphContainer);


        const getRepairingCostData = async () => {
            try {
                const userStore = useUserStore();
                const userCompanyCode = userStore.companyCode;

                if (!userCompanyCode) {
                    console.error('Error: No company code found for the user.');
                    return; // 処理を中断
                }

                const url = `http://127.0.0.1:8000/api/repairingCost/APM02ByCompany/?format=json&companyCode=${userCompanyCode}`;
                const response = await axios.get(url);
                console.log('Fetched RepairingCost Data:', response.data); // データ取得ログ

                let repairingCostData = response.data;
                for (const companyData of repairingCostData) {
                    for (const plantData of companyData.actualPM02List) {
                        const actualPM02Data = plantData.actualPM02;

                        // 各月ごとのデータを新しい形式に変換
                        actualPM02Data.forEach((yearData) => {
                            const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'commitment', 'totalCost'];
                            let monthCosts = [];
                            months.forEach((month) => {
                                if (yearData[month]) {
                                    monthCosts.push({
                                        month: month,
                                        cost: parseFloat(yearData[month])
                                    });
                                }
                            });

                            this.RepairingCostData.push({
                                plant: plantData.plant,
                                data: monthCosts
                            });
                        });
                    }
                }

                // 取得したデータを使ってグラフを描画
                const plotData = this.RepairingCostData.map((plantData) => {
                    const xValues = plantData.data.map((entry) => entry.month);
                    const yValues = plantData.data.map((entry) => entry.cost);

                    return {
                        x: xValues,
                        y: yValues,
                        name: plantData.plant
                    };
                });

                const layout = {
                    height: document.getElementById('rpcPM02A').clientHeight,
                    width: document.getElementById('rpcPM02A').clientWidth,
                    title: 'Repairing Cost'
                };

                Plotly.newPlot('rpcPM02A', plotData, layout);

            } catch (error) {
                console.error('Error fetching RepairingCost data:', error);
            }
        };

        // 上記関数の実行
        getRepairingCostData();
    },

    beforeDestroy() {
        if (resizeObserver) {
            resizeObserver.disconnect();
        }
    }
};
</script>
