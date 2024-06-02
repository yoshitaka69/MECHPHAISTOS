<template>
    <div>
      <RiskMatrix :emittedData="emittedData" @update-impact-for-production="updateImpactForProduction" />
      <CriticalEquipmentList @data-emitted="handleDataEmitted" ref="equipmentList" />
    </div>
  </template>
  
  <script>
  import CriticalEquipmentList from './CriticalEquipmentList.vue';
  import RiskMatrix from './Risk_Matrix_impact_for_production.OnlyMatrix.vue';
  
  export default {
    components: {
      CriticalEquipmentList,
      RiskMatrix
    },
    data() {
      return {
        emittedData: []
      };
    },
    methods: {
      handleDataEmitted(data) {
        console.log('Emitted Data:', data);
        this.emittedData = data;
      },
      updateImpactForProduction({ index, impactForProduction }) {
        console.log(`Updating impactForProduction at row ${index} with value ${impactForProduction}`);
        this.$refs.equipmentList.updateImpactForProduction({ index, impactForProduction });
      }
    }
  }
  </script>
  