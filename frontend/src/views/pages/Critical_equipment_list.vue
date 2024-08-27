<template>
  <div class="base-content">
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="Critical equipment list">
            <p class="line-height-3 m-0"></p>
            <div>
              <Button label="Open Impact Matrix" icon="pi pi-external-link" @click="showImpactMatrixModal = true" class="mb-3 mr-3" />
              <Button label="Open Possibility Matrix" icon="pi pi-external-link" @click="showPossibilityMatrixModal = true" class="mb-3" />
              <CriticalEquipmentList
                :riskTexts="riskTexts"
                @data-emitted="handleDataEmitted"
                ref="equipmentList"
              />
            </div>
          </TabPanel>
          
          <TabPanel header="Priority Tasks">
            <div class="row">
              <div class="col-12 xl:col-8">
                <div class="card" style="background-color: #f2f2f2">
                  priority tasks top 20
                  <Top20_priority_task />
                </div>
              </div>
              <div class="col-12 xl:col-4">
                <div class="card" style="background-color: #f2f2f2">
                  <Assessment_rate />
                </div>
              </div>
            </div>
          </TabPanel>
          
          <TabPanel header="Risk-Matrix">
            <p class="line-height-3 m-0"></p>
            <div class="risk-matrix-container">
              <div class="risk-matrix-item">
                <Risk_Matrix_impact_for_production />
              </div>
              <div class="risk-matrix-item">
                <Risk_matrix_possibility_Of_Failure />
              </div>
            </div>
          </TabPanel>
          
        </TabView>
      </div>
    </section>

    <!-- RiskMatrixImpact Modal -->
    <Dialog :visible="showImpactMatrixModal" modal @hide="showImpactMatrixModal = false" :style="{ width: '70vw' }" :closable="false">
      <template #header>
        <h3>Impact Matrix</h3>
      </template>
      <RiskMatrixImpact :inputData="emittedData" @update-risk-texts="updateImpactForProduction" />
      <template #footer>
        <Button label="Close" icon="pi pi-times" @click="showImpactMatrixModal = false" />
      </template>
    </Dialog>

    <!-- RiskMatrixPossibility Modal -->
    <Dialog :visible="showPossibilityMatrixModal" modal @hide="showPossibilityMatrixModal = false" :style="{ width: '50vw' }" :closable="false">
      <template #header>
        <h3>Possibility Matrix</h3>
      </template>
      <RiskMatrixPossibility :inputData="emittedData" @update-risk-texts="handleRiskTexts" />
      <template #footer>
        <Button label="Close" icon="pi pi-times" @click="showPossibilityMatrixModal = false" />
      </template>
    </Dialog>
  </div>
</template>

<script>
//first tab
import CriticalEquipmentList from '@/components/Critical_equipment_list/CriticalEquipmentList.vue';
import RiskMatrixImpact from '@/components/Risk_Matrix/Risk_Matrix_impact_for_productionOnlyMatrix.vue';
import RiskMatrixPossibility from '@/components/Risk_Matrix/Risk_matrix_possibility_Of_FailureOnlyMatrix.vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';

//second tab
import Assessment_rate from '@/components/Critical_equipment_list/Assessment_rate.vue';
import Top20_priority_task from '@/components/Critical_equipment_list/Top20_priority_task.vue';

//third tab
import Risk_Matrix_impact_for_production from '@/components/Risk_Matrix/Risk_Matrix_impact_for_production.vue';
import Risk_matrix_possibility_Of_Failure from '@/components/Risk_Matrix/Risk_matrix_possibility_Of_Failure.vue';

export default {
  components: {
    CriticalEquipmentList,
    RiskMatrixImpact,
    RiskMatrixPossibility,
    Assessment_rate,
    Top20_priority_task,
    Risk_Matrix_impact_for_production,
    Risk_matrix_possibility_Of_Failure,
    Dialog,
    Button,
  },
  data() {
    return {
      activeIndex: parseInt(localStorage.getItem('criticalEquipmentTabIndex')) || 0,
      emittedData: [],
      riskTexts: [],
      showImpactMatrixModal: false, // モーダルの表示状態を管理するためのデータ
      showPossibilityMatrixModal: false, // Possibility Matrixのモーダル表示状態を管理するフラグ
    };
  },
  methods: {
    onTabChange(event) {
      this.activeIndex = event.index;
      localStorage.setItem('criticalEquipmentTabIndex', this.activeIndex);
    },
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
    },
  },
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
}

.risk-matrix-item {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.mb-3 {
  margin-bottom: 1.5rem;
}

.mr-3 {
  margin-right: 1rem;
}
</style>
