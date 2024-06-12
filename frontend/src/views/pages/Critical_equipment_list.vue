<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Critical equipment list">
                        <p class="line-height-3 m-0"></p>
                        <div>
                            <RiskMatrixImpact :inputData="emittedData" @update-risk-texts="updateImpactForProduction" />
                            <RiskMatrixPossibility :inputData="emittedData" @update-risk-texts="handleRiskTexts" />
                            <CriticalEquipmentList :riskTexts="riskTexts" @data-emitted="handleDataEmitted"
                                ref="equipmentList" />
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
    </div>
</template>

<script>
//first tab
import CriticalEquipmentList from '@/components/Critical_equipment_list/CriticalEquipmentList.vue';
import RiskMatrixImpact from '@/components/Risk_Matrix/Risk_Matrix_impact_for_productionOnlyMatrix.vue';
import RiskMatrixPossibility from '@/components/Risk_Matrix/Risk_matrix_possibility_Of_FailureOnlyMatrix.vue';

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
        Risk_matrix_possibility_Of_Failure
    },
    data() {
        return {
            activeIndex: parseInt(localStorage.getItem('activeTabIndex')) || 0,
            emittedData: [],
            riskTexts: [] // 新たに追加
        };
    },
    methods: {
        onTabChange(event) {
            this.activeIndex = event.index;
            localStorage.setItem('activeTabIndex', this.activeIndex);
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
