<template>
    <div class="base-content">
      <section class="content">
        <div class="card card-solid">
          <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
            <TabPanel header="Breakdown Prediction">
              <p class="line-height-3 m-0"></p>
              <BathtubCurve />
              <weibull_Distribution />
              <Bayesian_estimation /> 
            </TabPanel>
            <TabPanel header="Cost Estimate">
              <p class="line-height-3 m-0"></p>
              <div id="appCost" style="display: flex;">
                <div style="width: 50%;">
                  <RepairCostPredictionChart />
                </div>
                <div style="width: 50%;">
                  <AnnualCostPredictionChart />
                </div>
              </div>
            </TabPanel>
          </TabView>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  //first tab
  import BathtubCurve from '@/components/Breakdown_prediction/BathtubCurve.vue';
  import Bayesian_estimation from '@/components/Breakdown_prediction/Bayesian_estimation.vue';
  import weibull_Distribution from '@/components/Breakdown_prediction/Weibull_Distribution.vue';

  //second tab
  import RepairCostPredictionChart from '@/components/Cost_Prediction/RepairCostPredictionChart.vue';
  import AnnualCostPredictionChart from '@/components/Cost_Prediction/AnnualCostPredictionChart.vue';
  
  export default {
    components: {
      BathtubCurve,
      Bayesian_estimation,
      weibull_Distribution,
      RepairCostPredictionChart,
      AnnualCostPredictionChart,
    },
    data() {
      return {
        activeIndex: parseInt(localStorage.getItem('activeTabIndex')) || 0
      };
    },
    methods: {
      onTabChange(event) {
        this.activeIndex = event.index;
        localStorage.setItem('activeTabIndex', this.activeIndex);
      }
    }
  };
  </script>
  
  <style>
  .row {
      display: flex;
      flex-wrap: wrap;
  }
  
  .risk-matrix-container {
      display: flex;
      flex-direction: column;
      gap: 40px;
      /* コンポーネント間の隙間 */
  }
  
  .risk-matrix-item {
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
  }
  </style>
  