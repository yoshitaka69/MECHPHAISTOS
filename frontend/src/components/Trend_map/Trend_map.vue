<template>
  <div>
    <!-- プロットコンテナを上部に配置 -->
    <div ref="plotContainer" style="width: 100%; height: 500px;"></div>
    
    <!-- スライドバーを中央に配置 -->
    <div style="width: 100%; padding: 10px 0;">
      <input type="range" min="0" :max="state.months.length - 1" v-model="state.currentMonthIndex" @input="updateMapAndTable" style="width: 100%;" step="1">
      <div style="display: flex; justify-content: space-between;">
        <span v-for="month in state.months" :key="month" style="text-align: center; flex-grow: 1;">
          {{ month.substring(5, 7) }} <!-- 月の表示 -->
        </span>
      </div>
    </div>
    
    <!-- 選択された月を表示 -->
    <div style="font-size: 1.5rem; margin-bottom: 20px;">Selected Month: {{ state.months[state.currentMonthIndex] }}</div>
    
    <!-- テーブルコンテナをスライドバーの下に配置 -->
    <div ref="tableContainer" style="width: 100%; overflow-y: auto; max-height: 500px; padding: 10px;"></div> <!-- テーブルの余白を設定 -->
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore';

const plotContainer = ref(null);
const tableContainer = ref(null);
const userStore = useUserStore();

const state = reactive({
  data: [],
  months: [],
  currentMonthIndex: 0,
  alertLists: []
});

// 月の範囲を設定するロジック
const today = new Date();
const startMonth = new Date(today.getFullYear() - 0.5, today.getMonth() - 6);
const endMonth = new Date(today.getFullYear() + 2, today.getMonth());
for (let d = new Date(startMonth); d <= endMonth; d.setMonth(d.getMonth() + 1)) {
  state.months.push(d.toISOString().slice(0, 7)); // YYYY-MM 形式で月を追加
}

const fetchData = async () => {
  const url = `http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?format=json&companyCode=${userStore.companyCode}`;
  try {
    const response = await axios.get(url);
    state.alertLists = response.data.flatMap(company => company.AlertScheduleList || []);
    updateMapAndTable(); // Initial update
  } catch (error) {
    console.error('Failed to fetch data:', error);
  }
};

const preparePlotData = (data) => {
  const monthPartsCount = {};
  data.forEach(alert => {
    const month = new Date(alert.orderAlertDate).toISOString().slice(0, 7); // YYYY-MM 形式
    const country = alert.country;
    const key = `${country}-${month}`;
    if (!monthPartsCount[key]) {
      monthPartsCount[key] = { country, month, count: 0 };
    }
    monthPartsCount[key].count++;
  });
  return Object.values(monthPartsCount);
};

const renderPlot = (data) => {
  let filteredData = data.filter(d => d.month === state.months[state.currentMonthIndex]);
  const locations = filteredData.map(d => d.country);
  const counts = filteredData.map(d => d.count);
  const texts = filteredData.map(d => `${d.country}: ${d.count} parts`);

  const trace = {
    type: 'choropleth',
    locationmode: 'country names',
    locations: locations,
    z: counts,
    text: texts,
    colorscale: [
      [0, 'rgb(242,240,247)'], 
      [1, 'rgb(84,39,143)']
    ],
    colorbar: {
      title: {
        text: 'Parts Count',
        font: {
          family: "Arial",
          size: 12,
          color: "yellow" // カラーバーのタイトルを黄色に変更
        }
      },
      thickness: 10,
      tickfont: { color: 'yellow' } // カラーバーの目盛りフォントを黄色に変更
    }
  };

  const layout = {
    title: {
      text: 'Monthly Parts Count by Country',
      font: {
        family: 'Arial',
        size: 18,
        color: 'yellow' // タイトルのフォントを黄色に変更
      }
    },
    geo: {
      projection: {
        type: 'natural earth'
      },
      bgcolor: 'rgb(0, 0, 0)' // 地図部分の背景色を黒に設定
    },
    width: 600,  // 幅の設定
    height: 500,  // 高さの設定
    margin: {
      l: 20,  // 左マージン
      r: 20,  // 右マージン
      t: 50,  // 上マージン
      b: 50   // 下マージン
    },
    paper_bgcolor: 'rgb(0, 0, 0)', // 全体の背景色を黒に設定
    plot_bgcolor: 'rgb(0, 0, 0)', // プロット領域の背景色を黒に設定
    font: {
      color: 'yellow' // 全体のフォントを黄色に設定
    }
  };

  const config = {
    displayModeBar: false // 右上のツールバーを非表示にする
  };

  Plotly.newPlot(plotContainer.value, [trace], layout, config);
};

const renderTable = (data) => {
  const headers = ["plant", "partsName", "eventDate", "orderAlertDate", "country"];
  const headerValues = headers.map(header => [header]);
  
  // データがない場合、15行の空データを生成
  const rows = data.length > 0 ? data : Array(15).fill({ plant: '', partsName: '', eventDate: '', orderAlertDate: '', country: '' });
  
  const cellValues = headers.map(header => rows.map(alert => alert[header] || ''));

  const tableData = {
    type: 'table',
    columnwidth: [250, 250, 250, 250, 250],  // 列の幅を調整
    header: {
      values: headerValues,
      align: "center",
      fill: { color: 'rgb(50, 50, 50)' },  // ヘッダーの背景色を黒に変更
      font: { 
        family: "Arial", 
        size: 18, // フォントサイズを18に設定（2回り大きく）
        color: "yellow" // ヘッダーの文字色を黄色に変更
      }
    },
    cells: {
      values: cellValues,
      align: ["center"],
      fill: { color: ['rgb(30, 30, 30)', 'rgb(50, 50, 50)'] }, // セルの背景色を黒に変更（交互の色も設定）
      font: { 
        family: "Arial", 
        size: 11, 
        color: ["white"] 
      }
    }
  };

  const layout = {
    width: 800,  // テーブルの全体幅を指定
    height: 400, // テーブルの高さを指定
    margin: {
      l: 30,  // 左マージン
      r: 30,  // 右マージン
      t: 30,  // 上マージン
      b: 30   // 下マージン
    },
    paper_bgcolor: 'rgb(0, 0, 0)', // テーブル全体の背景色を黒に変更
    plot_bgcolor: 'rgb(0, 0, 0)' // テーブル領域の背景色を黒に変更
  };

  const config = {
    displayModeBar: false // 右上のツールバーを非表示にする
  };


  Plotly.newPlot(tableContainer.value, [tableData], layout, config);
};


const updateMapAndTable = () => {
  const filteredAlerts = state.alertLists.filter(alert =>
    alert.orderAlertDate.startsWith(state.months[state.currentMonthIndex])
  );
  const plotData = preparePlotData(filteredAlerts);
  renderPlot(plotData);
  renderTable(filteredAlerts);
};

// Watch for changes in the current month index to update the map and table
watch(() => state.currentMonthIndex, updateMapAndTable);

onMounted(fetchData);
</script>

<style scoped>
/* テーブルコンテナの最小高さを指定 */
#tableContainer {
  min-height: 400px; 
}
</style>
