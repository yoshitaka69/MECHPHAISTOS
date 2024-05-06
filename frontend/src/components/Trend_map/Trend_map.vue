<template>
  <div>
    <div style="display: flex; height: 500px;">
      <div ref="plotContainer" style="flex: 1;"></div>
      <div ref="tableContainer" style="flex: 1; overflow-y: auto; max-height: 500px;"></div>
    </div>
    <div style="width: 100%; padding: 10px 0;">
      <input type="range" min="0" :max="state.months.length - 1" v-model="state.currentMonthIndex" @input="updateMapAndTable" style="width: 100%;" step="1">
      <div style="display: flex; justify-content: space-between;">
        <span v-for="month in state.months" :key="month" style="text-align: center; flex-grow: 1;">
          {{ month.substring(5, 7) }} <!-- 月の表示 -->
        </span>
      </div>
    </div>
    <div>Selected Month: {{ state.months[state.currentMonthIndex] }}</div>
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
      title: 'Parts Count',
      thickness: 10
    }
  };

  const layout = {
    title: 'Monthly Parts Count by Country',
    geo: {
      projection: {
        type: 'natural earth'
      }
    }
  };

  Plotly.newPlot(plotContainer.value, [trace], layout);
};

const renderTable = (data) => {
  const headers = ["plant", "partsName", "eventDate", "orderAlertDate", "country"];
  const headerValues = headers.map(header => [header]);
  const cellValues = headers.map(header => data.map(alert => alert[header] || ''));

  const tableData = {
    type: 'table',
    columnwidth: [200, 200, 200, 200, 200],
    header: {
      values: headerValues,
      align: "center",
      fill: {color: ['rgb(235, 100, 230)']},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: cellValues,
      align: ["center"],
      fill: {color: ['rgb(245, 245, 245)', 'rgb(235, 235, 235)']},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  };

  Plotly.newPlot(tableContainer.value, [tableData]);
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

