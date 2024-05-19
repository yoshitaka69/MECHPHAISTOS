<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Critical equipment list">
                        <p class="line-height-3 m-0">
                            Critical Equipment List. This data is sample.
                            <br />
                            <br />
                            <Critical_equipment_list />
                        </p>
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
                        <div>
                            <Risk_matrix />
                        </div>
                        <div class="row">
                            <div class="col-12 xl:col-6">
                                <div>
                                    <Impact_for_production :isActive="activeTab === 'Risk-Matrix'" />
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card" style="background-color: #f2f2f2">
                                    <Probability_of_failure />
                                </div>
                            </div>
                        </div>
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Critical_equipment_list from '@/components/Critical_equipment_list/Critical_equipment_list.vue';
import Assessment_rate from '@/components/Critical_equipment_list/Assessment_rate.vue';
import Risk_matrix from '@/components/Risk_Matrix/Risk_matrix.vue';
import Impact_for_production from '@/components/Risk_Matrix/Impact_for_production.vue';
import Probability_of_failure from '@/components/Risk_Matrix/Probability_of_failure.vue';
import Top20_priority_task from '@/components/Critical_equipment_list/Top20_priority_task.vue';

export default {
    components: {
        Critical_equipment_list,
        Assessment_rate,
        Risk_matrix,
        Impact_for_production,
        Probability_of_failure,
        Top20_priority_task
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
</style>
