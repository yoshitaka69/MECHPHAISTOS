<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Maintenance Optimization">
                        <p class="line-height-3 m-0"></p>
                        <OptimaizeByBaize />
                    </TabPanel>
                    <TabPanel header="Cost Estimate">
                        <p class="line-height-3 m-0"></p>
                        <div id="appCost" style="display: flex">
                            <div style="width: 50%">
                                <RepairCostPredictionChart />
                            </div>
                            <div style="width: 50%">
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
import OptimaizeByBaize from '@/components/Maintenance_Optimization/OptimaizeByBaize.vue';
//second tab
import RepairCostPredictionChart from '@/components/Cost_Prediction/RepairCostPredictionChart.vue';
import AnnualCostPredictionChart from '@/components/Cost_Prediction/AnnualCostPredictionChart.vue';

export default {
    components: {
        OptimaizeByBaize,
        RepairCostPredictionChart,
        AnnualCostPredictionChart
    },
    data() {
        return {
            activeIndex: parseInt(localStorage.getItem('maintenanceOptimizationTabIndex')) || 0 // キー名を変更
        };
    },
    methods: {
        onTabChange(event) {
            this.activeIndex = event.index;
            localStorage.setItem('maintenanceOptimizationTabIndex', this.activeIndex); // キー名を変更
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
