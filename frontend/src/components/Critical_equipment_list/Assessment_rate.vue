<template>
  <div>
    Assessment Distribution
    <div id="AssessmentChart" ref="chartContainer" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';

export default {
  data() {
    return {
      error: null,
      assessmentCounts: {},
    };
  },

  mounted() {
    this.fetchDataAndPlot();
    this.setupResizeObserver();
  },

  beforeDestroy() {
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  },

  methods: {
    fetchDataAndPlot() {
      const userStore = useUserStore();
      const companyCode = userStore.companyCode;

      if (!companyCode) {
        this.error = 'No company code found for the user.';
        return;
      }

      const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`;
      
      axios.get(url)
        .then((response) => {
          const masterData = response.data.find((data) => data.companyCode === companyCode)?.MasterDataTable || [];
          this.assessmentCounts = this.countAssessments(masterData);
          this.$nextTick(() => {
            this.plotGraph();
          });
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
          this.error = 'Failed to fetch data.';
        });
    },

    countAssessments(data) {
      const assessmentValues = ['Very High', 'High', 'Middle', 'Low', 'Very Low'];
      let counts = {};

      assessmentValues.forEach(value => {
        counts[value] = 0;
      });

      data.forEach(item => {
        if (item.assessment && assessmentValues.includes(item.assessment)) {
          counts[item.assessment]++;
        }
      });

      return counts;
    },

    plotGraph() {
      const chartElement = this.$refs.chartContainer;
      const width = chartElement.clientWidth;
      const height = chartElement.clientHeight;

      const data = [{
        type: 'pie',
        values: Object.values(this.assessmentCounts),
        labels: Object.keys(this.assessmentCounts),
        textinfo: 'label+percent',
        insidetextorientation: 'radial',
      }];

      const layout = {
  title: 'Assessment Distribution',
  automargin: true,
  width: width,
  height: height,
  margin: { l: 10, r: 10, t: 10, b: 10 },
  legend: {
    font: {
      size: 10, // 凡例のフォントサイズを小さくする
      color: '#333' // 凡例のフォントカラーを設定
    },
    yanchor: 'top', // 凡例の縦位置のアンカーをトップに設定
    xanchor: 'right', // 凡例の横位置のアンカーを右に設定
    x: 1, // 凡例のx位置を調整
    y: 1, // 凡例のy位置を調整
    bgcolor: 'rgba(255,255,255,0.5)', // 凡例の背景色を設定、透明度も可能
    bordercolor: '#666', // 凡例のボーダーカラーを設定
    borderwidth: 1 // 凡例のボーダーの幅を設定
  }
};


      const config = { responsive: true };

      Plotly.newPlot('AssessmentChart', data, layout, config);
    },

    setupResizeObserver() {
      this.resizeObserver = new ResizeObserver(entries => {
        for (let entry of entries) {
          this.plotGraph();
        }
      });
      this.resizeObserver.observe(this.$refs.chartContainer);
    }
  }
};
</script>
