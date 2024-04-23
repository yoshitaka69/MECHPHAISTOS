<template>
  <div>
    Assessment Distribution
    <div id="AssessmentChart" style="width: 100%; height: 100%"></div>
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
      assessmentCounts: {}, // 状態としてassessmentCountsを保持
    };
  },

  mounted() {
    this.fetchDataAndPlot();
    window.addEventListener('resize', this.handleResize);
  },

  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize);
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
          this.plotAssessmentData();
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

    plotAssessmentData() {
      const chartElement = this.$el.querySelector('#AssessmentChart');
      const { width, height } = chartElement.getBoundingClientRect();

      const data = [{
        type: 'pie',
        values: Object.values(this.assessmentCounts),
        labels: Object.keys(this.assessmentCounts),
        textinfo: 'label+percent',
        insidetextorientation: 'radial'
      }];

      const layout = {
        title: 'Assessment Distribution',
        automargin: true,
        width: width,
        height: height
      };

      const config = { responsive: true };

      this.$nextTick(() => {
        Plotly.newPlot('AssessmentChart', data, layout, config);
      });
    },

    handleResize() {
      this.plotAssessmentData(); // 現在のassessmentCountsを使用してグラフを再プロット
    },
  }
};
</script>