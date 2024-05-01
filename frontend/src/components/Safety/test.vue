<template>
    <div>
      <div id="myDiv" style="height: 600px; width: 600px;"></div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Plotly from 'plotly.js-dist-min';
  import { useUserStore } from '@/stores/userStore';
  
  export default {
    data() {
      return {
        xData: [],
        yData: [],
        colors: ['rgba(67,67,67,1)', 'rgba(115,115,115,1)'],
        lineSize: [2, 2],
        labels: ['world_indicators', 'companyCode_indicators'],
        safetyLevels: ['Very Low', 'Low', 'Middle', 'High', 'Very High']
      };
    },
    async created() {
  try {
    const userStore = useUserStore();
    const companyCode = userStore.companyCode;
    console.log('companyCode:', companyCode);
    const response = await axios.get('http://127.0.0.1:8000/api/nearMiss/trendSafetyIndicatorsByCompany/', {
      params: {
        format: 'json',
        companyCode: companyCode
      }
    });
    console.log('response:', response);
    const companyData = response.data.find(item => item.companyCode === companyCode);
    if (companyData && companyData.trendSafetyIndicatorsList) {
      this.xData = companyData.trendSafetyIndicatorsList.map(item => new Date(item.lastUpdateDay).getFullYear());
      this.yData = companyData.trendSafetyIndicatorsList.map(item => this.safetyLevels.indexOf(item.safetyIndicators));
      console.log('xData:', this.xData);
      console.log('yData:', this.yData);
      this.generateChart();
    } else {
      console.log('trendSafetyIndicatorsList does not exist for the company:', companyCode);
    }
  } catch (error) {
    console.error('Error in created hook:', error);
  }
},
    methods: {
      generateChart() {
        const data = [];
  
        for (let i = 0; i < this.xData.length; i++) {
          const result = {
            x: this.xData[i],
            y: this.yData[i],
            type: 'scatter',
            mode: 'lines',
            line: {
              color: this.colors[i],
              width: this.lineSize[i]
            }
          };
          const result2 = {
            x: [this.xData[i][0], this.xData[i][11]],
            y: [this.yData[i][0], this.yData[i][11]],
            type: 'scatter',
            mode: 'markers',
            marker: {
              color: this.colors[i],
              size: 12
            }
          };
          data.push(result, result2);
        }
  
        const layout = {
          showlegend: false,
          height: 600,
          width: 600,
          xaxis: {
            showline: true,
            showgrid: false,
            showticklabels: true,
            linecolor: 'rgb(204,204,204)',
            linewidth: 2,
            autotick: false,
            ticks: 'outside',
            tickcolor: 'rgb(204,204,204)',
            tickwidth: 2,
            ticklen: 5,
            tickfont: {
              family: 'Arial',
              size: 12,
              color: 'rgb(82, 82, 82)'
            },
            range: [new Date().getFullYear() - 3, new Date().getFullYear() + 1]
          },
          yaxis: {
            showgrid: false,
            zeroline: false,
            showline: false,
            showticklabels: true,
            tickvals: [0, 1, 2, 3, 4],
            ticktext: this.safetyLevels
          },
          autosize: false,
          margin: {
            autoexpand: false,
            l: 100,
            r: 20,
            t: 100
          },
          annotations: [
            {
              xref: 'paper',
              yref: 'paper',
              x: 0.0,
              y: 1.05,
              xanchor: 'left',
              yanchor: 'bottom',
              text: 'Main Source for News',
              font: {
                family: 'Arial',
                size: 30,
                color: 'rgb(37,37,37)'
              },
              showarrow: false
            },
            {
              xref: 'paper',
              yref: 'paper',
              x: 0.5,
              y: -0.1,
              xanchor: 'center',
              yanchor: 'top',
              text: 'Source: Pew Research Center & Storytelling with data',
              showarrow: false,
              font: {
                family: 'Arial',
                size: 12,
                color: 'rgb(150,150,150)'
              }
            }
          ]
        };
  
        for (let i = 0; i < this.xData.length; i++) {
          const result = {
            xref: 'paper',
            x: 0.05,
            y: this.yData[i][0],
            xanchor: 'right',
            yanchor: 'middle',
            text: this.labels[i] + ' ' + this.yData[i][0] + '%',
            showarrow: false,
            font: {
              family: 'Arial',
              size: 16,
              color: 'black'
            }
          };
          const result2 = {
            xref: 'paper',
            x: 0.95,
            y: this.yData[i][11],
            xanchor: 'left',
            yanchor: 'middle',
            text: this.yData[i][11] + '%',
            font: {
              family: 'Arial',
              size: 16,
              color: 'black'
            },
            showarrow: false
          };
  
          layout.annotations.push(result, result2);
        }
  
        Plotly.newPlot('myDiv', data, layout);
      },
    },
  };
  </script>