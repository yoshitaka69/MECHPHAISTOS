<template>
  <div>
    <div ref="chart" style="width: 100%; height: 600px;"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Plotly from "plotly.js-dist-min";
import { useUserStore } from '@/stores/userStore';

export default {
  name: 'AnnualCostPredictionChart',
  async mounted() {
    const userStore = useUserStore();
    const companyCode = userStore.companyCode;
    const thisYear = new Date().getFullYear();
    const years = Array.from({ length: 10 }, (_, i) => thisYear + i + 1);

    try {
      // 予測コストデータを取得
      const response = await axios.get(`http://127.0.0.1:8000/api/junctionTable/eventYearPPMByCompany/?companyCode=${companyCode}`);
      console.log('API Response:', response.data);

      const data = response.data.find(item => item.companyCode === companyCode);
      if (!data || !data.EventYearPPMList.length) {
        console.error('No data found for the specified company code.');
        return;
      }

      const costData = data.EventYearPPMList[0];
      console.log('Relevant Data:', costData);

      // 年ごとの予測コストデータ
      const predictedCosts = [
        parseFloat(costData.PPM0YearCost),
        parseFloat(costData.PPM1YearCost),
        parseFloat(costData.PPM2YearCost),
        parseFloat(costData.PPM3YearCost),
        parseFloat(costData.PPM4YearCost),
        parseFloat(costData.PPM5YearCost),
        parseFloat(costData.PPM6YearCost),
        parseFloat(costData.PPM7YearCost),
        parseFloat(costData.PPM8YearCost),
        parseFloat(costData.PPM9YearCost),
        parseFloat(costData.PPM10YearCost),
      ];

      // 上下限値を仮の計算で設定
      const lowerBound = predictedCosts.map(value => value * 0.9); // 仮の計算
      const upperBound = predictedCosts.map(value => value * 1.1); // 仮の計算

      // 予測コストの線
      const trace1 = {
        x: years,
        y: predictedCosts,
        mode: 'lines',
        name: 'Predicted Cost',
        line: { color: 'blue' },
      };

      // 下限の線
      const trace2 = {
        x: years,
        y: lowerBound,
        mode: 'lines',
        name: 'Lower Bound',
        line: { color: 'lightblue', dash: 'dash' },
      };

      // 上限の線
      const trace3 = {
        x: years,
        y: upperBound,
        mode: 'lines',
        name: 'Upper Bound',
        line: { color: 'lightblue', dash: 'dash' },
      };

      // エラーバンド
      const trace4 = {
        x: [...years, ...years.slice().reverse()],
        y: [...lowerBound, ...upperBound.slice().reverse()],
        fill: 'toself',
        fillcolor: 'rgba(173, 216, 230, 0.2)',
        line: { color: 'transparent' },
        showlegend: false,
      };

      const plotData = [trace1, trace2, trace3, trace4];

      // BathtubCurvePredictionデータを追加
      const bathtubYears = years;
      const bathtubData = bathtubYears.map((_, index) => Math.sin(index) * 50 + 100); // サンプルデータ

      const bathtubTrace = {
        x: bathtubYears,
        y: bathtubData,
        mode: 'lines',
        name: 'BathtubCurvePrediction',
        line: { color: 'red', dash: 'dash' },
      };

      plotData.push(bathtubTrace);

      const layout = {
        title: 'Annual Repair Costs Prediction and Bathtub Curve',
        xaxis: {
          title: 'Year',
          tickmode: 'linear',
          dtick: 1,
        },
        yaxis: {
          title: 'Cost (in thousand dollars)',
        }
      };

      Plotly.newPlot(this.$refs.chart, plotData, layout);

    } catch (error) {
      console.error('Error fetching data from API:', error);
    }
  }
};
</script>

<style scoped>
/* 任意のスタイルを追加 */
</style>
