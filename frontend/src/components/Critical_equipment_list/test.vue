<template>
  <div>
    <RiskMatrix :inputData="emittedData" @update-risk-texts="updateImpactForProduction" />
    <CriticalEquipmentList @data-emitted="handleDataEmitted" ref="equipmentList" />
  </div>
</template>

<script>
import CriticalEquipmentList from './CriticalEquipmentList.vue';
import RiskMatrix from './Risk_Matrix_impact_for_productionOnlyMatrix.vue';

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
    updateImpactForProduction(riskTexts) {
      console.log('Updated Risk Texts:', riskTexts);
      riskTexts.forEach((impactForProduction, index) => {
        this.$refs.equipmentList.updateImpactForProduction({ index, impactForProduction });
      });
    }
  }
};
</script>
