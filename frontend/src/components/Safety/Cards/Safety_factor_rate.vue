<template>
        <div id="SafeRate" ref="plotArea" style="width: 100%; height: 100%"></div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

export default {
    data() {
        return {
            values: {},
            error: null
        };
    },

    mounted() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        if (!userCompanyCode) {
            console.error('Error: No company code found for the user.');
            return;
        }

        const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?format=json&companyCode=${userCompanyCode}`;

        axios
            .get(url, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            })
            .then((response) => {
                const nearMissData = response.data;
                const allNearMisses = nearMissData.flatMap((companyData) => companyData.nearMissList);
                const factorArray = allNearMisses.map((item) => item['factor']);

                this.values = factorArray.reduce((accumulator, factor) => {
                    accumulator[factor] = (accumulator[factor] || 0) + 1;
                    return accumulator;
                }, {});

                this.$nextTick(() => {
                    this.resizePlot(); // DOMの更新後に初期描画
                });
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });

        // Resize Observerのセットアップ
        const ro = new ResizeObserver((entries) => {
            for (let entry of entries) {
                this.resizePlot();
            }
        });
        ro.observe(this.$refs.plotArea);
    },

    beforeDestroy() {
        // Resize Observerのクリーンアップ
        if (this.ro && this.$refs.plotArea) {
            this.ro.unobserve(this.$refs.plotArea);
        }
    },

    methods: {
        resizePlot() {
            if (this.$refs.plotArea) {
                const width = this.$refs.plotArea.clientWidth;
                const height = this.$refs.plotArea.clientHeight;
                this.plotGraph(width, height);
            }
        },

        plotGraph(width, height) {
            const data = [
                {
                    type: 'pie',
                    values: Object.values(this.values),
                    labels: Object.keys(this.values),
                    textinfo: 'label+percent',
                    insidetextorientation: 'radial'
                }
            ];

            const layout = {
                width: width,
                height: height,
                margin: { l: 10, r: 10, t: 10, b: 15 },
                showlegend: false // レジェンドを非表示に設定
                //legend: { x: 5, y: 0, xanchor: 'right', yanchor: 'bottom', font: { size: 10, color: '#000' } }
            };

            const config = { responsive: true };

            Plotly.newPlot('SafeRate', data, layout, { displayModeBar: false }, config);
        }
    }
};
</script>
