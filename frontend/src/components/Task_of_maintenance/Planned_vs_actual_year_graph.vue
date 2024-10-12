<template>
    <div style="width: 100%; height: 100%">
        <div id="chart" style="width: 100%; height: 100%"></div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート

export default {
    data() {
        return {
            years: [],
            costData: [],
            ppmData: []
        };
    },
    mounted() {
        this.fetchData();
        this.fetchPPMData();
        const chartElement = document.getElementById('chart');
        const resizeObserver = new ResizeObserver(() => {
            this.drawChart();
        });
        resizeObserver.observe(chartElement);
    },
    methods: {
        async fetchData() {
            const userStore = useUserStore();
            const url = `http://127.0.0.1:8000/api/calculation/summedActualCostByCompany/?companyCode=${userStore.companyCode}`;
            try {
                const response = await axios.get(url);
                this.processData(response.data);
            } catch (error) {
                console.error('API error: ', error);
            }
        },
        async fetchPPMData() {
            const userStore = useUserStore();
            const url = `http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?format=json&companyCode=${userStore.companyCode}`;
            try {
                const response = await axios.get(url);
                this.processPPMData(response.data);
            } catch (error) {
                console.error('API error: ', error);
            }
        },
        processData(data) {
            data.forEach((company) => {
                company.summedActualCostList.forEach((record) => {
                    this.years.push(record.year);
                    this.costData.push(record.totalActualCost);
                });
            });
            this.drawChart();
        },
        processPPMData(data) {
            const currentYear = new Date().getFullYear();
            data.forEach((item) => {
                item.EventYearPPMList.forEach((event) => {
                    for (let i = -5; i <= 10; i++) {
                        const yearKey = i < 0 ? `PPM${-i}YearCostAgo` : `PPM${i}YearCost`;
                        if (event[yearKey] !== undefined) {
                            this.ppmData.push({
                                x: currentYear + i,
                                y: parseFloat(event[yearKey])
                            });
                        }
                    }
                });
            });
            this.drawChart();
        },
        drawChart() {
            const trace1 = {
                x: this.years,
                y: this.costData,
                type: 'bar',
                name: 'Total Actual Cost', // グラフの名前を修正
                text: this.costData,
                textposition: 'auto'
            };
            const trace2 = {
                x: this.ppmData.map((d) => d.x),
                y: this.ppmData.map((d) => d.y),
                type: 'scatter',
                mode: 'lines+markers', // ラインとマーカーを表示
                name: 'PPM Cost',
                text: this.ppmData.map(() => 'PPM Cost'), // 各データポイントに固定のテキストを表示
                textposition: 'top center' // データポイントの上にテキストを表示
            };
            const chartElement = document.getElementById('chart');
            const layout = {
                title: 'Total Actual Costs and PPM by Year',
                xaxis: { title: 'Year', tickmode: 'linear', dtick: 1 },
                yaxis: { title: 'Cost', gridcolor: '#d3d3d3', showline: true },
                height: chartElement.clientHeight,
                width: chartElement.clientWidth,
                paper_bgcolor: '#e0f7e0', // グラフの外側の領域の背景色を設定
                plot_bgcolor: '#ffffff' // プロット領域の背景色を設定
            };
            const config = {
                displayModeBar: false // 右上の設定を非表示にする
            };
            Plotly.newPlot('chart', [trace1, trace2], layout, config);
        }
    }
};
</script>
