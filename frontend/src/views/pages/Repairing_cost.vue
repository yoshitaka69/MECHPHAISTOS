<template>
    <div class="base-content">
      <section class="content">
        <div class="card card-solid">
          <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
            <TabPanel header="Repairing cost">
              <div class="col-12 xl:col-12">
                <div class="card" style="background-color: #f2f2f2">
                  <total_graph />
                  <Display_repairing_cost />
                  <p>Planned cost</p>
                  <Total_cost_table />
                  <p>actual summary cost (readOnly)</p>
                  <Actual_summary_table />
                  <Message :closable="false">
                    AI recommendation
                    <br />
                    Now developing
                  </Message>
                </div>
              </div>
              <div class="row">
                <div class="col-12 xl:col-6">
                  <div class="card" style="background-color: #f2f2f2">
                    <PM02_actual_graph />
                    <div>
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
                  <div class="card" style="background-color: #f2f2f2">
                    <PM03_actual_graph />
                    <PM03_actual_table />
                    <Message :closable="false">
                      AI recommendation
                      <br />
                      Now developing
                    </Message>
                  </div>
                </div>
                <div class="col-12 xl:col-6">
                  <div class="card" style="background-color: #f2f2f2">
                    <PM04_actual_graph />
                    <PM04_actual_table />
                    <Message :closable="false">
                      AI recommendation
                      <br />
                      Now developing
                    </Message>
                  </div>
                </div>
                <div class="col-12 xl:col-6">
                  <div class="card" style="background-color: #f2f2f2">
                    <PM05_actual_graph />
                    <PM05_actual_table />
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
                  <div class="card card-mb0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <Card_predict_cost />
                    </div>
                  </div>
                </div>
                <div class="col-12 lg:col-6 xl:col-6">
                  <div class="card card-mb0">
                    <div class="flex justify-content-between mb-3" style="height: 150px">
                      <div>
                        <span class="block text-500 font-medium mb-3">Next month task event</span>
                        <div class="text-900 font-medium text-xl">28441</div>
                      </div>
                      <div class="flex align-items-center justify-content-center bg-cyan-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-inbox text-cyan-500 text-xl"></i>
                      </div>
                    </div>
                  </div>
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
  import Gap_of_repairing_cost from '@/components/Repairing_cost/Gap_of_repairing_cost.vue';
  import Display_repairing_cost from '@/components/Repairing_cost/Cards/Display_repairing_cost.vue';
  import Card_predict_cost from '@/components/Task_of_maintenance/Cards/Card_predict_cost.vue';
  

  //Simulation
  import Simulation_table from '@/components/Simulations/Simulation_table.vue';
  import SimulationGraph from '@/components/Simulations/Simulation_graph.vue';
  
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
      Card_predict_cost,
      Simulation_table,
      SimulationGraph,
    },
    data() {
      return {
        activeIndex: parseInt(localStorage.getItem('repairingCostTabIndex')) || 0, // キー名を変更
        costData: null,
      };
    },
    methods: {
      onTabChange(event) {
        this.activeIndex = event.index;
        localStorage.setItem('repairingCostTabIndex', this.activeIndex); // キー名を変更
      },
      handleUpdateCostData(data) {
        this.costData = data;
      },
    },
  };
  </script>
  
  <style scoped>
  .row {
    display: flex;
    flex-wrap: wrap;
  }
  
  .text-center {
    text-align: center;
  }
  
  h3 {
    font-size: 1.25rem; /* Adjust the font size as needed */
  }
  
  .card-mb0 {
    background-color: #e0f7e0; /* Light green background color */
  }
  </style>
  