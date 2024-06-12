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
  name: 'RepairCostPredictionChart',
  async mounted() {
    const userStore = useUserStore();
    const companyCode = userStore.companyCode;
    const currentYear = new Date().getFullYear();

    console.log('companyCode:', companyCode);
    console.log('currentYear:', currentYear);

    try {
      // 計画コストデータを取得
      const response = await axios.get(`http://127.0.0.1:8000/api/calculation/summedPlannedCostByCompany/?companyCode=${companyCode}`);
      console.log('API Response:', response.data);
      
      const data = response.data.find(item => item.companyCode === companyCode);
      if (!data || !data.summedPlannedCostList.length) {
        console.error('No data found for the specified company code.');
        return;
      }

      const relevantData = data.summedPlannedCostList.filter(item => item.year === currentYear);
      if (!relevantData.length) {
        console.error('No data found for the current year.');
        return;
      }

      const costData = relevantData[0];
      console.log('Relevant Data:', costData);

      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const predictedCosts = [
        parseFloat(costData.sumJan),
        parseFloat(costData.sumFeb),
        parseFloat(costData.sumMar),
        parseFloat(costData.sumApr),
        parseFloat(costData.sumMay),
        parseFloat(costData.sumJun),
        parseFloat(costData.sumJul),
        parseFloat(costData.sumAug),
        parseFloat(costData.sumSep),
        parseFloat(costData.sumOct),
        parseFloat(costData.sumNov),
        parseFloat(costData.sumDec)
      ];

      // ここで3つの変数によって予測される上下限値を計算
      const lowerBound = predictedCosts.map(value => value * 0.9); // 仮の計算
      const upperBound = predictedCosts.map(value => value * 1.1); // 仮の計算

      // 予測コストの線
      const trace1 = {
        x: months,
        y: predictedCosts,
        mode: 'lines',
        name: 'Predicted Cost',
        line: { color: 'blue' },
      };

      // 下限の線
      const trace2 = {
        x: months,
        y: lowerBound,
        mode: 'lines',
        name: 'Lower Bound',
        line: { color: 'lightblue', dash: 'dash' },
      };

      // 上限の線
      const trace3 = {
        x: months,
        y: upperBound,
        mode: 'lines',
        name: 'Upper Bound',
        line: { color: 'lightblue', dash: 'dash' },
      };

      // エラーバンド
      const trace4 = {
        x: [...months, ...months.slice().reverse()],
        y: [...lowerBound, ...upperBound.slice().reverse()],
        fill: 'toself',
        fillcolor: 'rgba(173, 216, 230, 0.2)',
        line: { color: 'transparent' },
        showlegend: false,
      };

      const plotData = [trace1, trace2, trace3, trace4];

      // 誤差計算をバックエンドにリクエスト
      const errorResponse = await axios.get(`http://127.0.0.1:8000/api/calculation/calculate-errors/`, {
        params: {
          companyCode: companyCode,
          year: currentYear
        }
      });
      console.log('Error Metrics:', errorResponse.data);

      // 各月ごとの誤差指標をプロット
      const errorMetrics = errorResponse.data;
      const errorTraces = ['MAE', 'MSE', 'RMSE', 'MAPE'].map(metric => ({
        x: months,
        y: errorMetrics[metric],
        mode: 'lines+markers',
        name: metric,
        yaxis: 'y2',
      }));

      plotData.push(...errorTraces);

      // BathtubCurvePredictionデータを追加
      const bathtubMonths = months;
      const bathtubData = bathtubMonths.map((_, index) => Math.sin(index) * 50 + 100); // サンプルデータ

      const bathtubTrace = {
        x: bathtubMonths,
        y: bathtubData,
        mode: 'lines',
        name: 'BathtubCurvePrediction',
        line: { color: 'red', dash: 'dash' },
      };

      plotData.push(bathtubTrace);

      const layout = {
        title: 'Monthly Repair Costs Prediction, Error Metrics, and Bathtub Curve',
        xaxis: {
          title: 'Month',
        },
        yaxis: {
          title: 'Cost (in thousand dollars)',
        },
        yaxis2: {
          title: 'Error Value',
          overlaying: 'y',
          side: 'right'
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
