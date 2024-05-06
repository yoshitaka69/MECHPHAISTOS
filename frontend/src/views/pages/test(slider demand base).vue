<template>
    <div>
      <input type="range" min="0" :max="dateRange.length - 1" v-model="sliderValue" @input="filterDataByDate">
      <div>{{ currentYearMonth }}</div>
      <div ref="plotlyTable"></div>
    </div>
  </template>
  
  <script>
  import Plotly from 'plotly.js-dist-min'
  import axios from 'axios'
  import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート
  
  export default {
    name: 'PlotlyTableChart',
    data() {
      return {
        rawData: [],
        sliderValue: 0,
        dateRange: []
      };
    },
    computed: {
      currentYearMonth() {
        return this.dateRange[this.sliderValue] || '';
      }
    },
    mounted() {
      this.fetchData();
    },
    methods: {
      async fetchData() {
        const userStore = useUserStore();
        const response = await axios.get(`http://127.0.0.1:8000/api/agora/alertScheduleByCompany/?companyCode=${userStore.companyCode}&format=json`);
        this.rawData = response.data;
        this.initializeDateRange();
        this.filterDataByDate();
      },
      initializeDateRange() {
        let dates = this.rawData.flatMap(item => item.AlertScheduleList.map(schedule => schedule.orderAlertDate));
        dates = [...new Set(dates)].sort();
        this.dateRange = dates.map(date => date.slice(0, 7)); // YYYY-MM を抽出
        this.dateRange = [...new Set(this.dateRange)];
      },
      filterDataByDate() {
        const selectedMonth = this.currentYearMonth;
        const filteredData = this.rawData.flatMap(item => ({
          ...item,
          AlertScheduleList: item.AlertScheduleList.filter(schedule => schedule.orderAlertDate.slice(0, 7) === selectedMonth)
        })).filter(item => item.AlertScheduleList.length > 0);
  
        this.drawTable(filteredData);
      },
      drawTable(data) {
        const headers = ["plant", "partsName", "eventDate", "orderAlertDate", "country"];
        const headerValues = headers.map(header => [header]);
        const cellValues = headers.map(header => []);
  
        data.forEach(item => {
          item.AlertScheduleList.forEach(schedule => {
            headers.forEach((header, index) => {
              cellValues[index].push(schedule[header] || '');
            });
          });
        });
  
        const tableData = [{
          type: 'table',
          columnwidth: [200, 200, 200, 200, 200],
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
            fill: {color: ['rgba(228, 222, 249, 0.65)', 'rgb(235, 193, 238)']},
            font: {family: "Arial", size: 11, color: ["black"]}
          }
        }];
  
        const layout = {
          title: "Alert Schedule by Company",
          autosize: true
        };
  
        Plotly.newPlot(this.$refs.plotlyTable, tableData, layout);
      }
    }
  }
  </script>
  
  <style>
  /* 必要に応じてスタイルを追加 */
  </style>
  