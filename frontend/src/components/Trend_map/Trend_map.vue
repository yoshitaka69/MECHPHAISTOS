<template>
  <div>
    <div style="display: flex; height: 500px;">
      <div ref="plotContainer" style="flex: 1;"></div>
      <div ref="tableContainer" style="flex: 1; overflow-y: auto; max-height: 500px;"></div>
    </div>
    <div style="width: 100%; padding: 10px 0;">
      <input type="range" min="0" :max="state.months.length - 1" v-model="state.currentMonthIndex" @input="updateMap" style="width: 100%;" step="1">
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
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import Plotly from 'plotly.js-dist-min';
import { useUserStore } from '@/stores/userStore';

const plotContainer = ref(null);
const tableContainer = ref(null);
const userStore = useUserStore();

const state = reactive({
  data: [],
  months: [],
  currentMonthIndex: 0
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
    if (response.data && Array.isArray(response.data)) {
      // 取得したデータを出力
      console.log('Fetched data:', response.data);

      // AlertScheduleListを抽出し、flatMapで一つの配列にまとめる
      const alertLists = response.data.flatMap(company => company.AlertScheduleList);

      // 抽出したalertListsを出力
      console.log('Alert lists:', alertLists);

      const tableData = prepareTableData(alertLists);
      renderTable(tableData);
      state.data = prepareData(response.data);
      renderPlot(state.data, state.months[state.currentMonthIndex]);
    } else {
      console.error('No valid data or AlertScheduleList missing in the response');
    }
  } catch (error) {
    console.error('Failed to fetch data:', error);
  }
};

// 以下のコードはそのままにします...
// prepareData, renderPlot, updateMap, prepareTableData, renderTable

const prepareData = (data) => {
    const monthPartsCount = {};
    data.forEach(company => {
      company.AlertScheduleList.forEach(alert => {
        const month = new Date(alert.orderAlertDate).toISOString().slice(0, 7); // YYYY-MM 形式
        const country = alert.country;
        const key = `${country}-${month}`;
        if (!monthPartsCount[key]) {
          monthPartsCount[key] = { country, month, count: 0 };
        }
        monthPartsCount[key].count++;
      });
    });
    console.log("Prepared data:", monthPartsCount); // デバッグ用のログ
    return Object.values(monthPartsCount);
  };
  
  
  const renderPlot = (data, selectedMonth) => {
  let filteredData = data.filter(d => d.month === selectedMonth);
  console.log("Filtered data for the selected month:", filteredData);
  
    if (filteredData.length === 0) {
      console.warn("No data available for the selected month:", selectedMonth);
      // デフォルトの地図表示を保証するためにダミーデータを用意
      filteredData = [{ country: 'USA', count: 0 }]; // USAを例として使うが、適宜変更可能
    }
  
    const locations = filteredData.map(d => d.country);
    const counts = filteredData.map(d => d.count);
    const texts = filteredData.map(d => `${d.country}: ${d.count} parts`);
  
    const trace = {
      type: 'choropleth',
      locationmode: 'world',
      locations: locations,
      z: counts,
      text: texts,
      zauto: false,
      zmin: 0,
      zmax: Math.max(...counts, 1) // 0だけの場合は最大値を1とする
    };
  
    const layout = {
      title: 'Monthly Parts Count by Country',
      geo: {
        scope: 'world',
        countrycolor: 'rgb(255, 255, 255)',
        showland: true,
        landcolor: 'rgb(217, 217, 217)',
        showlakes: true,
        lakecolor: 'rgb(255, 255, 255)',
        subunitcolor: 'rgb(255, 255, 255)'
      }
    };
  
    Plotly.newPlot(plotContainer.value, [trace], layout);
  };
  
  
  
  
  const prepareTableData = (alertLists) => {
  const selectedMonth = state.months[state.currentMonthIndex];

  // フィルタリング対象となるalertListsを出力
  console.log('Alert lists:', alertLists);

  // 選択された月と一致するorderAlertDateを持つアラートのみをフィルタリング
  const filteredAlerts = alertLists.filter(alert => {
    const alertMonth = new Date(alert.orderAlertDate).toISOString().slice(0, 7); // YYYY-MM 形式

    // 各アラートのorderAlertDateを出力
    console.log('Order alert date:', alert.orderAlertDate);

    return alertMonth === selectedMonth;
  });

  // フィルタリングされたアラートと選択された月をコンソールに出力
  console.log('Selected month:', selectedMonth);
  console.log('Filtered alerts:', filteredAlerts);

  let headerValues = [['Order Alert'],['Parts Name'], ['Event Date'], ['Delivery Time'], ['Country'], ];

  // 各列のデータを配列で保持
  let partsNames = filteredAlerts.map(alert => alert.partsName || '');
  let eventDates = filteredAlerts.map(alert => alert.eventDate || '');
  let deliveryTimes = filteredAlerts.map(alert => alert.deliveryTime ? alert.deliveryTime.toString() : '');
  let countries = filteredAlerts.map(alert => alert.country || '');
  let orderAlertDates = filteredAlerts.map(alert => alert.orderAlertDate || '');

  // 確認して、各列が15行に満たない場合は空の行で補う
  const numRows = 15;
  [orderAlertDates,partsNames, eventDates, deliveryTimes, countries, ].forEach(column => {
    while (column.length < numRows) {
      column.push(''); // 空の文字列で追加
    }
  });

  let cellValues = [ orderAlertDates,partsNames, eventDates, deliveryTimes, countries,];

  return {headerValues, cellValues};
};

const updateMap = () => {
  const selectedMonth = state.months[state.currentMonthIndex];
  renderPlot(state.data, selectedMonth);

  // テーブルも更新
  const tableData = prepareTableData(state.data.flatMap(company => company.AlertScheduleList || []));
  renderTable(tableData);
};
  
  
  const renderTable = ({ headerValues, cellValues }) => {
    var table = {
      type: 'table',
      columnwidth: [180, 200, 180, 120, 150], // 各列の幅を広げる
      columnorder: [0, 1, 2, 3, 4],
      header: {
        values: headerValues,
        align: "center",
        line: {width: 1, color: 'rgb(50, 50, 50)'},
        fill: {color: ['rgb(235, 100, 230)']},
        font: {family: "Arial", size: 12, color: "white"}
      },
      cells: {
        values: cellValues,
        align: ["center", "center"],
        line: {color: "black", width: 1},
        fill: {color: ['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']},
        font: {family: "Arial", size: 11, color: ["black"]}
      },
      domain: {x: [0, 1.5], y: [0, 1]} // ドメインを調整してテーブルの横幅を広げる
    };
    Plotly.newPlot(tableContainer.value, [table]);
  };



onMounted(fetchData);
</script>