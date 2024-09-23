<template>
    <div class="chart-container">
        <div class="aspect-ratio-box">
            <div id="rpcPM05P"></div>
        </div>
    </div>
</template>


<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Piniaのstoreをインポート

export default {
  data() {
      return {
          RepairingCostData: []
      };
  },

  async mounted() {
      const userStore = useUserStore(); // Piniaのストアを取得
      const companyCode = userStore.companyCode; // companyCodeを取得

      console.log('companyCode:', companyCode); // companyCodeをコンソールに表示

      // データを取得する関数
      const getRepairingCostData = async () => {
          try {
              // axiosを使用してデータを取得
              const response = await axios.get('http://127.0.0.1:8000/api/repairingCost/APM05ByCompany/', {
                  params: {
                      companyCode: companyCode // クエリパラメータとしてcompanyCodeを設定
                  }
              });

              console.log('API Response:', response); // APIのレスポンス全体をログに表示
              console.log('Response Data:', response.data); // レスポンスデータのみをログに表示

              // RepairingCostデータを取り出す
              const repairingCostData = response.data;

              // 各工場のデータが存在するか確認
              if (!repairingCostData || repairingCostData.length === 0) {
                  console.warn('No repairing cost data available'); // データがない場合の警告を表示
                  return;
              }

              // 各会社の `actualPM05List` を取り出して処理
              for (const company of repairingCostData) {
                  const actualPM05List = company.actualPM05List;
                  if (!actualPM05List || actualPM05List.length === 0) {
                      console.warn(`No actualPM05 data for company ${company.companyCode}`);
                      continue;
                  }

                  // 各プラントの `actualPM05` データを取り出す
                  for (const plantData of actualPM05List) {
                      const actualPM05 = plantData;

                      // データが全て `null` の場合はスキップ
                      if (
                          !actualPM05.jan &&
                          !actualPM05.feb &&
                          !actualPM05.mar &&
                          !actualPM05.apr &&
                          !actualPM05.may &&
                          !actualPM05.jun &&
                          !actualPM05.jul &&
                          !actualPM05.aug &&
                          !actualPM05.sep &&
                          !actualPM05.oct &&
                          !actualPM05.nov &&
                          !actualPM05.dec &&
                          !actualPM05.commitment &&
                          !actualPM05.totalCost
                      ) {
                          console.warn('No actual data available for this entry');
                          continue;
                      }

                      // データが `null` の場合は0に置き換え
                      const transformedData = {
                          x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment', 'Total'],
                          y: [
                              parseFloat(actualPM05.jan) || 0,
                              parseFloat(actualPM05.feb) || 0,
                              parseFloat(actualPM05.mar) || 0,
                              parseFloat(actualPM05.apr) || 0,
                              parseFloat(actualPM05.may) || 0,
                              parseFloat(actualPM05.jun) || 0,
                              parseFloat(actualPM05.jul) || 0,
                              parseFloat(actualPM05.aug) || 0,
                              parseFloat(actualPM05.sep) || 0,
                              parseFloat(actualPM05.oct) || 0,
                              parseFloat(actualPM05.nov) || 0,
                              parseFloat(actualPM05.dec) || 0,
                              parseFloat(actualPM05.commitment) || 0, // commitment データを追加
                              parseFloat(actualPM05.totalCost) || 0 // totalCost データを追加
                          ],
                          name: `${plantData.plant || 'Unknown Plant'}, ${actualPM05.year || 'Unknown Year'}` // 凡例にプラント名と年を表示
                      };

                      console.log('Transformed Data:', transformedData); // 変換されたデータを表示

                      // Vueのdataに追加
                      this.RepairingCostData.push(transformedData);
                  }
              }
          } catch (error) {
              console.error('Error fetching RepairingCost data:', error);
              throw error;
          }
      };

      // データ取得とグラフ描画
      try {
          await getRepairingCostData();
          console.log('RepairingCostData:', this.RepairingCostData); // 修理コストデータを表示

          if (this.RepairingCostData.length === 0) {
              console.warn('No data to plot'); // データがない場合の警告を表示
              return;
          }

          // グラフデータを作成
          const plotData = this.RepairingCostData.map((plantData) => ({
              x: plantData.x,
              y: plantData.y,
              name: plantData.name,
              type: 'scatter', // ラインチャートに変更
              mode: 'lines+markers', // 線とマーカーを表示
              line: {
                  shape: 'linear' // 線の形状を設定（必要に応じて変更可能）
              }
          }));

          const layout = {
              // titleプロパティを削除
              xaxis: { title: 'Month & Total' },
              yaxis: {
                  title: 'Cost',
                  showticklabels: true, // y軸のラベルを表示
                  showline: true, // y軸の線を表示
                  linecolor: 'black', // y軸の線を黒に設定
                  linewidth: 1 // y軸の線の太さを設定
              },
              showlegend: true, // 凡例の表示
              autosize: true, // 自動リサイズを有効にする
              paper_bgcolor: '#FFE5CC', // グラフの外側の背景色をさらに薄いオレンジ色に設定
              plot_bgcolor: 'white', // グラフの内側の背景色を白に設定
              margin: {
                  l: 50, // 左マージンを狭める
                  r: 30, // 右マージンを狭める
                  t: 10, // 上マージンを小さく設定
                  b: 50 // 下マージンはデフォルト
              }
          };

          const config = {
              responsive: true, // グラフが親要素に応じてリサイズされるように設定
              displayModeBar: false // グラフのツールバーを非表示
          };

          // グラフを描画
          Plotly.newPlot('rpcPM05P', plotData, layout, config);

          // ウィンドウリサイズ時にグラフを更新
          window.addEventListener('resize', () => {
              Plotly.Plots.resize(document.getElementById('rpcPM05P'));
          });
      } catch (error) {
          console.error('Error plotting Repairing Cost graph:', error);
      }
  }
};
</script>

<style scoped>
.chart-container {
    width: 100%; /* 親要素の幅に合わせる */
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative; /* 子要素を絶対配置にするために設定 */
}

#rpcPM05P {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}

.aspect-ratio-box {
    width: 100%;
    padding-bottom: 56.25%; /* 16:9 のアスペクト比を設定 */
    position: relative;
}
</style>
