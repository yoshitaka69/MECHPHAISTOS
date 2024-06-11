<template>
  <div>
    <RiskMatrixImpact :inputData="emittedData" @update-risk-texts="updateImpactForProduction" />
    <RiskMatrixPossibility :inputData="emittedData" @update-risk-texts="handleRiskTexts" />
    <CriticalEquipmentList :riskTexts="riskTexts" @data-emitted="handleDataEmitted" ref="equipmentList" />
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
      emittedData: [],
      riskTexts: [] // 新たに追加
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
    handleRiskTexts(data) {
      console.log('Received Risk Texts:', data);
      this.riskTexts.push(data);
      this.$refs.equipmentList.updateProbabilityOfFailure(data);
    }
  }
};
</script>
