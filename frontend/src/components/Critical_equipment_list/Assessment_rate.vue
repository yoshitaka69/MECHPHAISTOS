<template>
  <div>
      <v-card>
          <v-card-title>Assessment Distribution</v-card-title>
          <div id="AssessmentChart"></div>
      </v-card>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore';


export default {
  data() {
      return {
          error: null
      };
  },

  mounted() {
      this.fetchDataAndPlot();
  },

  methods: {
      fetchDataAndPlot() {
          const userStore = useUserStore();
          const companyCode = userStore.companyCode; // Pinia ストアから companyCode を取得

          if (!companyCode) {
              this.error = 'No company code found for the user.';
              return;
          }

          const url = `http://127.0.0.1:8000/api/junctionTable/masterDataTableByCompany/?format=json&companyCode=${companyCode}`;

          axios
              .get(url)
              .then((response) => {
                  const masterData = response.data.find((data) => data.companyCode === companyCode)?.MasterDataTable || [];
                  const assessmentCounts = this.countAssessments(masterData);

                  this.plotAssessmentData(assessmentCounts);
              })
              .catch((error) => {
                  console.error('Error fetching data:', error);
                  this.error = 'Failed to fetch data.';
              });
      },

      countAssessments(data) {
          const assessmentValues = ['Very High', 'High', 'Middle', 'Low', 'Very Low'];
          let counts = {};

          // Initialize counts
          assessmentValues.forEach((value) => {
              counts[value] = 0;
          });

          data.forEach((item) => {
              if (item.assessment && assessmentValues.includes(item.assessment)) {
                  counts[item.assessment]++;
              }
          });

          return counts;
      },

      plotAssessmentData(assessmentCounts) {
          const data = [
              {
                  type: 'pie',
                  values: Object.values(assessmentCounts),
                  labels: Object.keys(assessmentCounts),
                  textinfo: 'label+percent',
                  insidetextorientation: 'radial'
              }
          ];

          const layout = {
              title: 'Assessment Distribution',
              width: 500,
              height: 500,
              automargin: true
          };

          const config = { responsive: true };

          this.$nextTick(() => {
              Plotly.newPlot('AssessmentChart', data, layout, config);
          });
      }
  }
};
</script>
