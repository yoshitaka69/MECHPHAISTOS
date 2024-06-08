<template>
    <div id="app" style="display: flex;">
      <div style="width: 50%;">
        <RepairCostPredictionChart />
      </div>
      <div style="width: 50%;">
        <AnnualCostPredictionChart />
      </div>
    </div>
  </template>
  
  <script>
  import RepairCostPredictionChart from '../../../views/pages./../components/Repairing_cost/Prediction/RepairCostPredictionChart.vue';
  import AnnualCostPredictionChart from '../../../views/pages./../components/Repairing_cost/Prediction/AnnualCostPredictionChart.vue';
  
  export default {
    name: 'App',
    components: {
      RepairCostPredictionChart,
      AnnualCostPredictionChart,
    },
  };
  </script>
  
  <style>
  /* 任意のスタイルを追加 */
  </style>
  