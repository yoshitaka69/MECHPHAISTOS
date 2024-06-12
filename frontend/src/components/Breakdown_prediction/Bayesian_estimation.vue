<template>
	<div>
	  <h1>Failure Prediction By Baysian estimation</h1>
	  <div id="failureChart"></div> <!-- Plotlyグラフを描画するためのdiv要素 -->
	</div>
  </template>
  
  <script>
  import axios from 'axios'; // HTTPクライアントライブラリ
  import { ref, onMounted } from 'vue'; // VueのコンポジションAPI
  import Plotly from 'plotly.js-dist-min'; // Plotlyライブラリ
  
  export default {
	setup() {
	  const chartData = ref(null); // APIから取得したデータを保持するリアクティブ変数
  
	  onMounted(async () => {
		// APIからデータを取得
		const response = await axios.get('http://localhost:8000/api/reliability/predict/');
		chartData.value = response.data; // 取得したデータをchartDataに保存
		createChart(); // グラフを描画
	  });
  
	  const createChart = () => {
		const trace = {
		  x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], // 横軸のラベル（月）
		  y: chartData.value.probabilities, // 縦軸のデータ（故障発生確率）
		  type: 'scatter', // 散布図
		  mode: 'lines+markers', // 線とマーカーを表示
		  marker: { color: 'rgba(75, 192, 192, 1)' } // マーカーの色
		};
  
		const layout = {
		  title: 'Failure Probability Over Time',
		  xaxis: {
			title: 'Month',
			tickmode: 'array',
			tickvals: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
			ticktext: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
		  },
		  yaxis: {
			title: 'Probability'
		  }
		};
  
		Plotly.newPlot('failureChart', [trace], layout); // Plotlyでグラフを描画
	  };
  
	  return {
		chartData, // コンポーネントで使用するリアクティブ変数を返す
	  };
	},
  };
  </script>
  
  <style scoped>
  #failureChart {
	width: 100%;
	height: 400px;
  }
  </style>
  