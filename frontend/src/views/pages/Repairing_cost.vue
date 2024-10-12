<template>
    <div class="base-content">
        <section class="content">
            <div class="card card-solid">
                <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
                    <TabPanel header="Repairing cost">
                        <div class="col-12 xl:col-12">
                            <div class="card" style="background-color: #f2f2f2">
                                <div class="total-cost-label">Total Graph (Planned vs Actual)</div>

                                <total_graph />
                                <Display_repairing_cost />

                                <div class="cost-section">
                                    <p>Planned cost</p>
                                    <Total_cost_table />
                                </div>

                                <div class="cost-section">
                                    <p>actual summary cost (readOnly)</p>
                                    <Actual_summary_table />
                                </div>

                                <Message :closable="false">
                                    AI recommendation
                                    <br />
                                    Now developing
                                </Message>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12 xl:col-6">
                                <div class="card fixed-height" style="background-color: #f2f2f2; padding: 1rem">
                                    <div class="pm02-actual-cost-label">PM02 Actual cost</div>
                                    <PM02_actual_graph />
                                    <div style="margin-top: 2rem">
                                        <PM02_actual_table />
                                    </div>
                                    <Message :closable="false">
                                        AI recommendation
                                        <br />
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card fixed-height" style="background-color: #f2f2f2; padding: 1rem">
                                    <div class="pm03-actual-cost-label">PM03 Actual cost</div>
                                    <PM03_actual_graph />
                                    <div style="margin-top: 2rem">
                                        <PM03_actual_table />
                                    </div>
                                    <Message :closable="false">
                                        AI recommendation
                                        <br />
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card fixed-height" style="background-color: #f2f2f2; padding: 1rem">
                                    <div class="pm04-actual-cost-label">PM04 Actual cost</div>
                                    <PM04_actual_graph />
                                    <div style="margin-top: 2rem">
                                        <PM04_actual_table />
                                    </div>
                                    <Message :closable="false">
                                        AI recommendation
                                        <br />
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                            <div class="col-12 xl:col-6">
                                <div class="card fixed-height" style="background-color: #f2f2f2; padding: 1rem">
                                    <div class="pm05-actual-cost-label">PM05 Actual cost</div>
                                    <PM05_actual_graph />
                                    <div style="margin-top: 2rem">
                                        <PM05_actual_table />
                                    </div>
                                    <Message :closable="false">
                                        AI recommendation
                                        <br />
                                        Now developing
                                    </Message>
                                </div>
                            </div>
                        </div>
                    </TabPanel>
                    <TabPanel header="Task list">
                        <div class="row">
                            <div class="col-12 lg:col-6 xl:col-6">
                                <Card_predict_cost />
                            </div>
                            <div class="col-12 lg:col-6 xl:col-6">
                                <Nextmonth_High_cost_event />
                            </div>
                        </div>
                        <div class="col-12 xl:col-12">
                            <div class="card" style="background-color: #f2f2f2">
                                <div class="row">
                                    <div class="col-12 lg:col-6 xl:col-6">
                                        <Planned_vs_actual_year_graph />
                                    </div>
                                    <div class="col-12 lg:col-6 xl:col-6">
                                        <Gap_of_repairing_cost />
                                    </div>
                                </div>
                                <Pandora />
                            </div>
                           
                        </div>
                        <div>
                            <Task_list />
                            <div class="text-center">
                                <h3>Table. Task list</h3>
                            </div>
                        </div>
                    </TabPanel>
                    <TabPanel header="Simulations">
                        <SimulationGraph :costData="costData" />
                        <div class="text-center">
                            <h3>Table. Trend of repairing cost month and year</h3>
                        </div>
                        <br />
                        <Simulation_table @update-cost-data="handleUpdateCostData" />
                        <div class="text-center">
                            <h3>Table. Task simulation table</h3>
                        </div>
                    </TabPanel>
                </TabView>
            </div>
        </section>
    </div>
</template>

<script>
import Total_graph from '@/components/Repairing_cost/Total_graph.vue';

//Task List
import Total_cost_table from '@/components/Task_of_maintenance/Total_cost_table.vue';
import Planned_vs_actual_year_graph from '@/components/Task_of_maintenance/Planned_vs_actual_year_graph.vue';

//repairing cost
import Actual_summary_table from '@/components/Repairing_cost/Actual_summary_table.vue';
import PM02_actual_graph from '@/components/Repairing_cost/PM02_actual_graph.vue';
import PM02_actual_table from '@/components/Repairing_cost/PM02_actual_table.vue';
import PM03_actual_graph from '@/components/Repairing_cost/PM03_actual_graph.vue';
import PM03_actual_table from '@/components/Repairing_cost/PM03_actual_table.vue';
import PM04_actual_graph from '@/components/Repairing_cost/PM04_actual_graph.vue';
import PM04_actual_table from '@/components/Repairing_cost/PM04_actual_table.vue';
import PM05_actual_graph from '@/components/Repairing_cost/PM05_actual_graph.vue';
import PM05_actual_table from '@/components/Repairing_cost/PM05_actual_table.vue';
import Task_list from '@/components/Task_of_maintenance/Task_list.vue';

import Gap_of_repairing_cost from '@/components/Task_of_maintenance/Gap_of_repairing_cost.vue';
import Display_repairing_cost from '@/components/Repairing_cost/Cards/Display_repairing_cost.vue';

import Nextmonth_High_cost_event from '@/components/Task_of_maintenance/Cards/Nextmonth_High_cost_event.vue';
import Card_predict_cost from '@/components/Task_of_maintenance/Cards/Card_predict_cost.vue';

//Simulation
import Simulation_table from '@/components/Simulations/Simulation_table.vue';
import SimulationGraph from '@/components/Simulations/Simulation_graph.vue';

import Pandora from '@/components/Mechphaistos_Ai/Pandora.vue';

export default {
    components: {
        Total_graph,
        Total_cost_table,
        Planned_vs_actual_year_graph,
        Actual_summary_table,
        PM02_actual_graph,
        PM02_actual_table,
        PM03_actual_graph,
        PM03_actual_table,
        PM04_actual_graph,
        PM04_actual_table,
        PM05_actual_graph,
        PM05_actual_table,
        Task_list,
        Gap_of_repairing_cost,
        Display_repairing_cost,
        Nextmonth_High_cost_event,
        Card_predict_cost,
        Simulation_table,
        SimulationGraph,
        Pandora,
    },
    data() {
        return {
            activeIndex: parseInt(localStorage.getItem('repairingCostTabIndex')) || 0, // キー名を変更
            costData: null
        };
    },
    methods: {
        onTabChange(event) {
            this.activeIndex = event.index;
            localStorage.setItem('repairingCostTabIndex', this.activeIndex); // キー名を変更
        },
        handleUpdateCostData(data) {
            this.costData = data;
        }
    }
};
</script>

<style scoped>
/* 共通スタイル */
.row {
    display: flex;
    flex-wrap: wrap;
}

.text-center {
    text-align: center;
}

h3 {
    font-size: 1.25rem; /* 必要に応じてフォントサイズを調整 */
}

.card-mb0 {
    background-color: #e0f7e0; /* 薄い緑色の背景色 */
}

/* 各コンポーネントのラベルのスタイル */
.total-cost-label,
.pm02-actual-cost-label,
.pm03-actual-cost-label,
.pm04-actual-cost-label,
.pm05-actual-cost-label {
    font-weight: bold; /* 太字に設定 */
    font-size: 2rem; /* フォントサイズを調整 */
    color: #2c3e50; /* 目立つ色を設定 */
    margin-bottom: 0.5rem; /* 下に余白を追加 */
}

/* テーブル配置用のスタイル */
.cost-section {
    text-align: center; /* 横方向のセンター配置 */
    margin-bottom: 2rem; /* 要素間の余白を調整 */
}

/* カードの高さを固定 */
.card.fixed-height {
    height: 1200px; /* 固定の高さ */
    overflow-y: auto; /* スクロールを有効に */
}

/* メッセージコンテンツのマージン調整 */
.card.fixed-height .Message {
    margin-top: auto; /* 最後にメッセージを固定 */
}
</style>
