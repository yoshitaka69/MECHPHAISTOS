<template>
    <div>
        Safety Measure trend
        <div id="smt"></div>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート

export default {
    data() {
        return {
            x: [],
            y: []
        };
    },

    mounted() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        if (!userCompanyCode) {
            console.error('Error: No company code found for the user.');
            return; // companyCodeがない場合、処理を中断
        }

        const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;

        axios
            .get(url, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                const nearMissData = response.data;

                // データから年ごとの measures のカウントを抽出
                const dataByYear = nearMissData
                    .flatMap((companyData) => companyData.nearMissList)
                    .reduce((acc, item) => {
                        const year = new Date(item.dateOfOccurrence).getFullYear();

                        // measures の要素数をカウント
                        acc[year] = acc[year] || { A: 0, B: 0, C: 0, D: 0, E: 0 };
                        acc[year][item.measures]++;

                        return acc;
                    }, {});

                // データをPlotlyのtraceに変換
                const measures = ['A', 'B', 'C', 'D', 'E'];
                const traces = measures.map((measure) => ({
                    x: Object.keys(dataByYear),
                    y: Object.values(dataByYear).map((count) => count[measure]),
                    type: 'bar',
                    name: measure
                }));

                const layout = {
                    barmode: 'stack',
                    yaxis: {
                        dtick: 1
                    }
                };

                Plotly.newPlot('smt', traces, layout);
            });
    }
};
</script>
