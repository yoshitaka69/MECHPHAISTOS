<template>
  <div ref="plotlyChart"></div>
</template>

<script>
import Plotly from 'plotly.js-dist-min'
import axios from 'axios'
import { useUserStore } from '@/stores/userStore'

export default {
  name: 'PlotlyChart',
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const userStore = useUserStore();
      console.log('Fetching data for company code:', userStore.companyCode);

      const response = await axios.get(`http://127.0.0.1:8000/api/nearMiss/trendSafetyIndicatorsByCompany/`, {
        params: {
          companyCode: userStore.companyCode,
          format: 'json'
        }
      });

      console.log('API Response:', response.data);
      this.drawChart(response.data);
    },
    drawChart(data) {
      let groupedData = {};
      data.forEach(company => {
        company.trendSafetyIndicatorsList.forEach(indicator => {
          if (!groupedData[company.companyCode]) {
            groupedData[company.companyCode] = {
              x: [],
              y: [],
              type: 'scatter',
              mode: 'lines+markers',
              name: company.companyCode
            };
          }
          groupedData[company.companyCode].x.push(new Date(indicator.lastUpdateDay));
          groupedData[company.companyCode].y.push(this.mapSafetyIndicator(indicator.safetyIndicators));
        });
      });

      let traceData = Object.values(groupedData);
      const annotations = this.createAnnotations(traceData);

      const layout = {
        title: 'Safety Indicators Trend',
        xaxis: { title: 'Year', type: 'date' },
        yaxis: {
          title: 'Safety Level',
          tickmode: 'array',
          tickvals: [1, 2, 3, 4, 5],
          ticktext: ['Very Low', 'Low', 'Middle', 'High', 'Very High'],
          range: [0.5, 5.5]
        },
        annotations
      };

      Plotly.newPlot(this.$refs.plotlyChart, traceData, layout);
    },
    mapSafetyIndicator(indicator) {
      const levels = { 'Very Low': 1, 'Low': 2, 'Middle': 3, 'High': 4, 'Very High': 5 };
      return levels[indicator] || 0;
    },
    createAnnotations(traceData) {
      const annotations = [
        {
          xref: 'paper',
          yref: 'paper',
          x: 0.0,
          y: 1.05,
          xanchor: 'left',
          yanchor: 'bottom',
          text: 'Safety Level Trends',
          font: { family: 'Arial', size: 18, color: 'rgb(37,37,37)' },
          showarrow: false
        }
      ];

      const labels = ['Very Low', 'Low', 'Middle', 'High', 'Very High'];
      traceData.forEach(trace => {
        const firstLabel = labels[trace.y[0] - 1];
        const lastLabel = labels[trace.y[trace.y.length - 1] - 1];
        const firstX = trace.x[0];
        const lastX = trace.x[trace.x.length - 1];

        annotations.push({
          x: firstX,
          y: trace.y[0],
          xref: 'x',
          yref: 'y',
          text: firstLabel,
          xanchor: 'right',
          showarrow: true,
          arrowhead: 2
        }, {
          x: lastX,
          y: trace.y[trace.y.length - 1],
          xref: 'x',
          yref: 'y',
          text: lastLabel,
          xanchor: 'left',
          showarrow: true,
          arrowhead: 2
        });
      });

      return annotations;
    }
  }
}
</script>


