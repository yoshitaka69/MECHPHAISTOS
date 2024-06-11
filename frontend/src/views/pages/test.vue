<template>
  <div>
    <RiskMatrixImpact :inputData="emittedData" @update-risk-texts="updateImpactForProduction" />
    <RiskMatrixPossibility :inputData="emittedData" @update-risk-texts="updateProbabilityOfFailure" />
    <CriticalEquipmentList @data-emitted="handleDataEmitted" ref="equipmentList" />
  </div>
</template>

<script>
import CriticalEquipmentList from './CriticalEquipmentList.vue';
import RiskMatrixImpact from './Risk_Matrix_impact_for_productionOnlyMatrix.vue';
import RiskMatrixPossibility from './Risk_matrix_possibility_Of_FailureOnlyMatrix.vue';

export default {
  components: {
    CriticalEquipmentList,
    RiskMatrixImpact,
    RiskMatrixPossibility
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
    },
    updateProbabilityOfFailure(probabilityOfFailure, index) {
      console.log(`Updating probabilityOfFailure at row ${index} with value ${probabilityOfFailure}`);
      this.$refs.equipmentList.updateProbabilityOfFailure({ index, probabilityOfFailure });
    }
  }
};
</script>
